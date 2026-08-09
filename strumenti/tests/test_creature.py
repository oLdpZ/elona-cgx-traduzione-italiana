# strumenti/tests/test_creature.py
"""Le due proprieta' che la rinomina dell'evoluzione pretende dai nomi italiani.

`action.hsp:18640` non rinomina una creatura assegnandole un nome nuovo: taglia
la stringa **gia' salvata**, cercando `evold` come prefisso o come suffisso e
mettendo `evname` al suo posto. Da qui due obblighi che non riguardano il
significato delle rese ma la loro **forma**, e che nessun occhio verifica su
mille voci.

Sono armati prima del lavoro, non dopo: finche' i due dizionari non esistono
passano a vuoto, ed e' voluto. Il giorno che arriva il primo lotto sono gia' li'.
"""
import json

import pytest

from strumenti import percorsi
from strumenti.creature import (
    FILE, classi, classi_da_testo, evoluzioni, nessuna_firma_in_due_classi,
    nomi_per_creatura, nomi_visibili,
)

SORGENTE = """\
	if ( dbid == 1 ) {
		return lang("ビッグモスキート", "big mosquito")
		cdatan(CDATAN_NAME, rc) = lang("ビッグモスキート", "big mosquito")
		txt lang("「ガウッ」", "*gulp*")
		p = lang("これは", "this is")
	}
"""


def carica(nome: str) -> dict[str, dict]:
    percorso = percorsi.PROGETTO / "dizionario" / f"{nome}.jsonl"
    if not percorso.exists():
        return {}
    voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    return {v["firma"]: v for v in voci if v.get("it")}


# --- il classificatore -------------------------------------------------------

def test_la_classe_la_dichiara_il_sito_non_il_contenuto():
    mappa = classi_da_testo(SORGENTE)
    assert mappa[("ビッグモスキート", "big mosquito")] == "nome"
    assert mappa[("「ガウッ」", "*gulp*")] == "voce"


def test_una_riga_che_non_e_ne_nome_ne_voce_resta_fuori():
    # non e' un errore: chi la chiede se la trova assente invece che
    # classificata per sbaglio. E' la stessa scelta di categorie.py
    assert ("これは", "this is") not in classi_da_testo(SORGENTE)


def test_lo_stesso_nome_vale_da_return_e_da_assegnazione():
    # le due forme sono la stessa firma, ed e' la ragione per cui la classe si
    # legge dalla riga e non dalla stringa
    assert classi_da_testo(SORGENTE)[("ビッグモスキート", "big mosquito")] == "nome"


def test_nessuna_firma_del_sorgente_vero_sta_in_due_classi():
    """La rete. Oggi le due classi sono disgiunte.

    Se un domani una stringa comparisse come nome **e** come voce, il criterio
    tornerebbe a essere un occhio in silenzio: meglio saperlo da qui.
    """
    assert nessuna_firma_in_due_classi() == set()


def test_il_sorgente_pinnato_ha_le_classi_che_il_piano_dichiara():
    conto = {}
    for classe in classi().values():
        conto[classe] = conto.get(classe, 0) + 1
    assert conto == {"nome": 1131, "voce": 320}


# --- le due proprieta' della rinomina ---------------------------------------

def accoppia_dal_sorgente() -> list[tuple[str, str]]:
    """Le coppie (evold inglese, evname inglese), lette da `action.hsp`.

    Nel sorgente `evname` viene **prima** e vale per tutti gli `evold` che lo
    seguono fino al successivo `evname`: un mostro nasce da piu' antenati, e
    `Unicorn` ne ha cinque (`lame horse`, `wild horse`, `Noyel horse`…).
    Fino a sette.

    ⚠️ `action.hsp:12383` assegna `evold = " Lv"` **senza** `evname`: e' l'altro
    sito, quello che *toglie* un suffisso invece di sostituirlo, e non e' un
    nome di specie. Resta fuori perche' non ha un `evname` davanti, non perche'
    qualcuno se lo ricordi.
    """
    import re
    testo = (percorsi.SORGENTE_HSP / "action.hsp").read_bytes().decode("cp932")
    coppie, evname = [], None
    for riga in testo.split("\r\n"):
        m = re.match(r'\s*(evold|evname) = lang\("([^"]*)", "([^"]*)"\)', riga)
        if not m:
            continue
        if m.group(1) == "evname":
            evname = m.group(3)
        elif evname is not None:
            coppie.append((m.group(3), evname))
    return coppie


def coppie_evoluzione() -> list[tuple[dict, dict]]:
    """Le stesse coppie, ma con le voci di dizionario tradotte al posto dei nomi."""
    dizionario = carica("action.hsp")
    if not dizionario:
        return []
    per_inglese = {v["en"]: v for v in dizionario.values()}
    coppie = []
    for vecchio_en, nuovo_en in accoppia_dal_sorgente():
        vecchio, nuovo = per_inglese.get(vecchio_en), per_inglese.get(nuovo_en)
        if vecchio and nuovo:
            coppie.append((vecchio, nuovo))
    return coppie


def test_l_accoppiamento_trova_tutti_gli_evold_tranne_quello_senza_evname():
    """La rete sotto i due test che seguono.

    Loro leggono `coppie_evoluzione()`, e se l'accoppiamento sbagliasse forma
    tornerebbe una lista vuota o dimezzata: guarderebbero il vuoto e
    passerebbero lo stesso. Qui si conta sul sorgente, senza dizionari di mezzo.
    """
    import re
    testo = (percorsi.SORGENTE_HSP / "action.hsp").read_bytes().decode("cp932")
    evold = len(re.findall(r'\bevold = lang\(', testo))
    coppie = accoppia_dal_sorgente()
    # ogni evold ha la sua coppia, tranne il ' Lv' di action.hsp:12383
    assert len(coppie) == evold - 1, f"{len(coppie)} coppie per {evold} evold"
    assert (" Lv", None) not in coppie
    assert ("younger cat sister", "Cat Princess") in coppie
    # un evname vale per piu' evold: Unicorn ne raccoglie cinque
    assert sum(1 for _, nuovo in coppie if nuovo == "Unicorn") == 5


def test_il_campo_della_rinomina_e_delimitato_dal_cancello():
    """Senza il cancello la prima proprieta' e' impossibile da soddisfare.

    `imp` e' prefisso di `impure eye` e `zombie` di `zombie girl`: il taglio non
    ha un controllo di confine di parola, e una guardia che pretendesse
    conservati **tutti** gli agganci chiederebbe che «occhio impuro» cominci per
    «folletto». Il cancello su `cdata(CDATA_ID, tc)` li rende innocui, perche'
    un occhio impuro non entrera' mai nel ramo dei folletti.

    Dentro al cancello gli agganci parziali che restano sono **veri**:
    `mummy` -> `greater mummy`, `orc` -> `king orc`.
    """
    mappa, nomi = evoluzioni(), nomi_per_creatura()
    esatti = parziali = 0
    for evmode, dati in mappa.items():
        visibili = nomi_visibili(evmode, mappa, nomi)
        for vecchio, _ in dati["coppie"]:
            for nome in visibili:
                if nome == vecchio:
                    esatti += 1
                elif nome.startswith(vecchio) or nome.endswith(vecchio):
                    parziali += 1
    assert (esatti, parziali) == (236, 47)


def test_evold_resta_agganciato_ai_nomi_che_in_inglese_lo_erano():
    """Prima proprieta': la rinomina deve continuare ad attaccare.

    Il taglio riconosce `evold` **solo** in testa o in coda, e solo sui nomi che
    possono entrare in quel ramo. Se in inglese un nome cominciava o finiva con
    `evold` e in italiano non lo fa piu', quella creatura evolve e **non viene
    rinominata** — in silenzio, e solo per chi ce l'ha in squadra.

    ⚠️ Il ramo che scatta puo' cambiare fra le due lingue, ed e' previsto: il
    codice li prova tutti e due. `lesser mummy` aggancia `mummy` in coda, mentre
    «mummia minore» lo aggancia in testa — l'italiano mette la specie davanti.
    Cio' che conta e' che agganci, non da che parte.
    """
    nomi_it = carica(FILE)
    azioni_it = carica("action.hsp")
    if not nomi_it or not azioni_it:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    reso = {v["en"]: v["it"] for v in list(nomi_it.values()) + list(azioni_it.values())}
    mappa, nomi_en = evoluzioni(), nomi_per_creatura()
    rotte = []
    for evmode, dati in mappa.items():
        visibili = nomi_visibili(evmode, mappa, nomi_en)
        for vecchio_en, _ in dati["coppie"]:
            vecchio_it = reso.get(vecchio_en)
            if vecchio_it is None:
                continue
            for nome_en in visibili:
                if not (nome_en.startswith(vecchio_en) or nome_en.endswith(vecchio_en)):
                    continue
                nome_it = reso.get(nome_en)
                if nome_it is None:
                    continue
                if not (nome_it.startswith(vecchio_it) or nome_it.endswith(vecchio_it)):
                    rotte.append(
                        f"evmode {evmode}: {nome_en!r} -> {nome_it!r} non aggancia piu' "
                        f"{vecchio_en!r} -> {vecchio_it!r} ne' in testa ne' in coda"
                    )
    assert not rotte, "la rinomina dell'evoluzione non attacca piu':\n" + "\n".join(rotte[:20])


def test_le_due_meta_di_ogni_coppia_concordano_nel_genere():
    """Seconda proprieta', e la piu' insidiosa.

    Il taglio sostituisce **solo** la frase di specie: l'articolo che la
    precede nel nome salvato resta quello di prima. Se `evold` e `evname` hanno
    generi diversi esce «`<Nome>` **la** principe gatto», e il difetto non si
    vede finche' una creatura non evolve — cioe' quasi mai in un collaudo.
    """
    coppie = coppie_evoluzione()
    if not coppie:
        pytest.skip("il dizionario di action.hsp non esiste ancora")

    discordi = [
        f"{vecchio['it']!r} ({vecchio.get('genere')}) -> {nuovo['it']!r} ({nuovo.get('genere')})"
        for vecchio, nuovo in coppie
        if vecchio.get("genere") and nuovo.get("genere")
        and vecchio["genere"] != nuovo["genere"]
    ]
    assert not discordi, "coppie evold/evname di genere diverso:\n" + "\n".join(discordi)


def test_ogni_meta_di_ogni_coppia_dichiara_il_genere():
    """Senza il campo il test qui sopra non guarda niente e passa lo stesso.

    E' la lezione di `una-procura-non-e-una-proprieta`: un test che si accontenta
    di cio' che trova non difende la proprieta', difende la propria comodita'.
    """
    coppie = coppie_evoluzione()
    if not coppie:
        pytest.skip("il dizionario di action.hsp non esiste ancora")
    senza = [v["en"] for coppia in coppie for v in coppia if not v.get("genere")]
    assert not senza, f"{len(senza)} meta' di coppia senza campo `genere`: {senza[:10]}"
