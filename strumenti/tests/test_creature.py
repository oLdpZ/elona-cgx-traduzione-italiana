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
    AZIONI, FILE, classi, classi_da_testo, evoluzioni, evoluzioni_con_jp,
    lotto_nucleo, nessuna_firma_in_due_classi, nomi_per_creatura,
    nomi_per_creatura_con_jp, nomi_visibili, nomi_visibili_con_jp,
    nucleo_atomico,
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


def rese_per_firma() -> dict[tuple[str, str], str] | None:
    """(giapponese, inglese) -> italiano, dai due dizionari del nucleo.

    `None` se non c'e' ancora niente da guardare, cosi' il chiamante salta.
    La chiave e' la coppia e non l'inglese: e' l'unica che tiene distinti i due
    `wild horse` di `action.hsp`.
    """
    tradotte = list(carica(FILE).values()) + list(carica(AZIONI).values())
    if not tradotte:
        return None
    return {(v["jp"], v["en"]): v["it"] for v in tradotte}


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


# --- il nucleo atomico -------------------------------------------------------

def test_il_nucleo_ha_la_misura_che_il_piano_dichiara():
    """378 stringhe inglesi, 380 firme, 203 + 373 voci nei due file.

    Se il sorgente cambiasse a monte questi numeri si muoverebbero, ed e'
    proprio cio' che il pin al tag deve rendere impossibile in silenzio.
    """
    voci = lotto_nucleo()
    per_file = {}
    for voce in voci:
        per_file[voce["file"]] = per_file.get(voce["file"], 0) + 1
    assert len(nucleo_atomico()) == 378
    assert len({v["firma"] for v in voci}) == 380
    assert per_file == {FILE: 203, AZIONI: 373}


def test_la_stessa_firma_ha_la_stessa_resa_nei_due_dizionari():
    """⚠️ Il vincolo atomico, quello che nessuna guardia vedeva.

    198 firme del nucleo vivono **in tutti e due** i file, quindi in due
    dizionari distinti: `db_creature.hsp.jsonl` e `action.hsp.jsonl`. Niente
    impedisce di scrivere due rese diverse — i dizionari sono per file e non si
    parlano — e il risultato sarebbe un `evold` che non aggancia piu' il nome
    che dovrebbe riconoscere, in silenzio.

    E' il motivo per cui il lotto entra tutto insieme o niente, e questa e' la
    rete sotto quella regola.

    ⚠️ Non chiede che lo **stesso inglese** abbia la stessa resa, e sarebbe
    sbagliato chiederlo: `wild horse` in `action.hsp` sono due firme — `野生馬`
    e `サラブレッド` — e sono due creature diverse. La chiave e' la firma.
    """
    creature_it, azioni_it = carica(FILE), carica(AZIONI)
    if not creature_it or not azioni_it:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    divergenti = [
        f"{firma[:10]} {creature_it[firma]['en']!r}: "
        f"{creature_it[firma]['it']!r} contro {azioni_it[firma]['it']!r}"
        for firma in set(creature_it) & set(azioni_it)
        if creature_it[firma]["it"] != azioni_it[firma]["it"]
    ]
    assert not divergenti, (
        "la stessa firma ha due rese nei due dizionari: il taglio confronta "
        "stringhe, e cosi' non aggancia piu':\n" + "\n".join(divergenti)
    )


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


# Gli agganci che esistono in inglese e che l'italiano **non** puo' conservare,
# uno per uno e col motivo. Ogni riga e' una decisione: cio' che non e' qui
# dentro deve agganciare, e il test lo pretende.
#
# Non e' un modo per zittire la guardia. Un aggancio che sparisce costa una
# rinomina mancata, e va speso solo dove la rinomina che si perde non esiste.
AGGANCI_SOLO_INGLESI = {
    # `bisque doll` e' prefisso di `bisque dolls` solo per la **-s del plurale**,
    # che in italiano non c'e': «la bambola di porcellana» diventa «le bambole di
    # porcellana», e cambiano articolo e sostantivo insieme.
    #
    # L'evoluzione vera — ビスクドール -> ビスクドールズ — passa lo stesso,
    # perche' li' il confronto e' **esatto**. L'aggancio parziale descrive solo
    # il rientro: una `bisque dolls` che ripassa da evmode 154 diventa in inglese
    # `bisque dollss`, che e' una stortura di upstream e non una rinomina.
    # In italiano il rientro non fa niente, ed e' il comportamento migliore.
    ("bisque doll", "bisque dolls"): "e' la -s del plurale inglese, non una specie",
}


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

    ⚠️ **La ricerca della resa e' per firma, non per inglese.** Prima questa
    funzione costruiva `{v["en"]: v["it"]}`, e su `wild horse` — che in
    `action.hsp` sono due creature, `野生馬` e `サラブレッド` — di due rese ne
    teneva una sola, silenziosamente quella che arrivava dopo.

    ⚠️ **Un aggancio inglese fra due giapponesi diversi non e' un aggancio**, e
    va saltato: e' l'artefatto della collisione, non un rapporto da conservare.
    `evold` `wild horse` che e' `サラブレッド` «aggancia» il nome `wild horse`
    che e' `野生馬` solo perche' upstream ha scritto lo stesso inglese per due
    creature. Pretenderlo in italiano vorrebbe dire chiamare il purosangue
    «cavallo selvatico», cioe' ricopiare l'errore.
    """
    reso = rese_per_firma()
    if reso is None:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    mappa, nomi = evoluzioni_con_jp(), nomi_per_creatura_con_jp()
    rotte = []
    for evmode, dati in mappa.items():
        visibili = nomi_visibili_con_jp(evmode, mappa, nomi)
        for vecchio, _ in dati["coppie"]:
            vecchio_it = reso.get(vecchio)
            if vecchio_it is None:
                continue
            for nome in visibili:
                if not (nome[1].startswith(vecchio[1]) or nome[1].endswith(vecchio[1])):
                    continue
                if nome[1] == vecchio[1] and nome[0] != vecchio[0]:
                    continue  # stesso inglese, giapponesi diversi: collisione
                if (vecchio[1], nome[1]) in AGGANCI_SOLO_INGLESI:
                    continue
                nome_it = reso.get(nome)
                if nome_it is None:
                    continue
                if not (nome_it.startswith(vecchio_it) or nome_it.endswith(vecchio_it)):
                    rotte.append(
                        f"evmode {evmode}: {nome[1]!r} -> {nome_it!r} non aggancia piu' "
                        f"{vecchio[1]!r} -> {vecchio_it!r} ne' in testa ne' in coda"
                    )
    assert not rotte, "la rinomina dell'evoluzione non attacca piu':\n" + "\n".join(rotte[:20])


def test_dove_agganciava_il_giapponese_aggancia_anche_l_italiano():
    """La proprieta' che l'inglese non puo' dare, perche' e' lui a essere rotto.

    Upstream ha scritto `フレアチック` come `Flare Chick` in un punto e
    `Flare chick` nell'altro (idem `イノブタ`, `ヤドナシ`, `デュラハン`), e ha
    chiamato `サラブレッド` `wild horse` mentre `db_creature.hsp` lo chiama
    `thoroughbred`. In tutti e cinque i casi l'`evold` **giapponese** coincide
    con il nome giapponese della creatura, e l'evoluzione in giapponese scatta;
    l'inglese non aggancia e la catena e' morta.

    Qui si chiede che l'italiano si comporti come il giapponese, che e'
    l'originale. Solo sulle coincidenze **esatte**: gli agganci parziali del
    giapponese hanno accidenti loro, e pretenderli sarebbe la guardia troppo
    severa che si finisce per spegnere.
    """
    reso = rese_per_firma()
    if reso is None:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    mappa, nomi = evoluzioni_con_jp(), nomi_per_creatura_con_jp()
    rotte = []
    for evmode, dati in mappa.items():
        visibili = nomi_visibili_con_jp(evmode, mappa, nomi)
        for vecchio, _ in dati["coppie"]:
            vecchio_it = reso.get(vecchio)
            if vecchio_it is None:
                continue
            for nome in visibili:
                nome_it = reso.get(nome)
                if nome_it is None or nome[0] != vecchio[0]:
                    continue
                if not (nome_it.startswith(vecchio_it) or nome_it.endswith(vecchio_it)):
                    rotte.append(
                        f"evmode {evmode}: {nome[0]} e' lo stesso giapponese di "
                        f"{vecchio[1]!r}, ma {nome_it!r} non aggancia {vecchio_it!r}"
                    )
    assert not rotte, (
        "in giapponese la rinomina scattava e in italiano no:\n" + "\n".join(rotte[:20]))


def test_il_taglio_rinomina_bene_anche_un_alleato_con_epiteto():
    """La chirurgia vera, simulata: `action.hsp:18640-18646` su un nome con epiteto.

    ⚠️ **E' il caso normale, non un caso limite.** I 152 personaggi con
    `CHARA_BIT_HAS_NAME` portano un nome composto — «Rashek il cavallo zoppo» —
    e sono proprio quelli che si tengono in squadra, cioe' quelli che evolvono.
    Li' `evold` non e' mai in testa, perche' davanti c'e' il nome proprio:
    **scatta il ramo del suffisso**, quello riparato.

    Le altre due guardie non lo vedono: guardano il nome nudo della specie, che
    aggancia in testa. Questa monta il nome come lo monta il gioco e controlla
    il **risultato**, non l'aggancio.
    """
    reso = rese_per_firma()
    if reso is None:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    def taglia(memorizzato: str, evold: str, evname: str) -> str:
        """`action.hsp:18640-18646`, col suffisso gia' riparato (`tc`, non `rc`)."""
        if memorizzato[:len(evold)] == evold:
            return evname + memorizzato[len(evold):]
        if memorizzato[len(memorizzato) - len(evold):] == evold:
            return memorizzato[:len(memorizzato) - len(evold)] + evname
        return memorizzato

    epiteto = "Rashek "
    mappa, nomi = evoluzioni_con_jp(), nomi_per_creatura_con_jp()
    rotte, quanti = [], 0
    for evmode, dati in mappa.items():
        visibili = nomi_visibili_con_jp(evmode, mappa, nomi)
        for vecchio, nuovo in dati["coppie"]:
            vecchio_it, nuovo_it = reso.get(vecchio), reso.get(nuovo)
            if vecchio_it is None or nuovo_it is None:
                continue
            for nome in visibili:
                if reso.get(nome) != vecchio_it:
                    continue  # solo la creatura che porta proprio quel nome
                quanti += 1
                atteso = epiteto + nuovo_it
                ottenuto = taglia(epiteto + vecchio_it, vecchio_it, nuovo_it)
                if ottenuto != atteso:
                    rotte.append(f"evmode {evmode}: {ottenuto!r} invece di {atteso!r}")

    assert quanti > 200, f"solo {quanti} tagli simulati: la simulazione non trova piu' niente"
    assert not rotte, (
        "il taglio dell'evoluzione sbaglia il nome di un alleato con epiteto:\n"
        + "\n".join(sorted(set(rotte))[:20])
    )


def test_ogni_nome_e_ogni_stringa_di_evoluzione_porta_il_proprio_articolo():
    """Seconda proprieta'. ⚠️ **Sostituisce la concordanza di genere**, che era
    la proprieta' sbagliata.

    `name()` (`init.hsp:1718`) anteponeva `"the "` al momento di mostrare, e la
    toppa l'ha tolto: in italiano l'articolo dipende da genere ed elisione,
    quindi lo porta il nome. Non e' una scelta di comodo — e' l'unica che
    **sopravvive all'evoluzione**, perche' un array parallelo indicizzato per
    `CREATURE_ID` darebbe l'articolo di prima della trasformazione: l'id non
    cambia, il nome si'.

    Se l'articolo sta dentro il nome, allora deve stare anche dentro `evold` e
    `evname`, e il taglio lo sostituisce insieme al resto. Da qui due
    conseguenze:

    - la concordanza di genere fra le due meta' **non serve piu'**:
      `giraffe` -> `Kirin` puo' andare da «la giraffa» a «il kirin» senza
      lasciare «la kirin», che era il difetto temuto;
    - ma se **una sola** delle due meta' dimentica l'articolo, il taglio
      produce un nome senza articolo o con due. Questo test e' quello che lo
      vede.

    I nomi propri fra `<>` e fra virgolette restano fuori: `name()` li
    riconosce dalla prima lettera (`init.hsp:1713-1716`) e non ci ha mai messo
    l'articolo davanti. ⚠️ **La maiuscola invece non c'entra**: `name()` guarda
    `CHARA_BIT_HAS_NAME`, che sta sul personaggio e non sulla stringa, quindi
    anche `Unicorn` e `Nekomata` ricevevano «the » e in italiano prendono
    l'articolo.

    ⚠️ **Solo le stringhe che il sorgente dichiara nomi.** `db_creature.hsp`
    contiene anche una **dinamica** — `randomname() + " the " + cdatan(...)`,
    l'epiteto dei 152 personaggi con nome proprio — che sta su una riga di forma
    `cdatan(CDATAN_NAME, rc) = lang(...)` ma non e' un nome: e' l'espressione
    che ne compone uno. Chiederle l'articolo era chiederle di cominciare per
    «il », cioe' di scrivere un articolo **fuori** dal nome, che e' l'opposto
    della regola. Il filtro e' `classi()`, la stessa autorita' che decide i
    lotti.
    """
    articoli = ("il ", "lo ", "la ", "i ", "gli ", "le ", "l'")
    nomi_it = carica(FILE)
    azioni_it = carica("action.hsp")
    if not nomi_it and not azioni_it:
        pytest.skip("i dizionari di db_creature.hsp e action.hsp non esistono ancora")

    mappa_classi = classi()
    da_guardare = [v for v in nomi_it.values()
                   if mappa_classi.get((v["jp"], v["en"])) == "nome"]
    evoluzione = {e for d in evoluzioni().values() for coppia in d["coppie"] for e in coppia}
    da_guardare += [v for v in azioni_it.values() if v["en"] in evoluzione]

    senza = [
        f"{v['en']!r} -> {v['it']!r}"
        for v in da_guardare
        if not v["it"].startswith(("<", '"')) and not v["it"].startswith(articoli)
    ]
    assert not senza, (
        f"{len(senza)} nomi senza articolo: il taglio dell'evoluzione lo "
        "sostituisce insieme alla specie, quindi deve esserci in tutti e due:\n"
        + "\n".join(senza[:20])
    )
