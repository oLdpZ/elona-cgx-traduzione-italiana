# strumenti/genera_toppe_filtri.py
"""Le diciassette righe del menu dei filtri dell'editor di mazzo, toppate dal sorgente.

`tcg.hsp:3552-3632` assegna `cfname@tcg` diciassette volte, una per pagina di
filtro, e ogni riga porta **due `lang()`** — «List» e «Deck», che il dizionario
copre — piu' da sette a nove **letterali nudi**, che nessun dizionario
raggiunge. E' il caso esatto per cui esiste la deroga `prima`
(`applica._controlla_toppa_prima`): la toppa gira sul sorgente pinnato, tocca i
soli letterali fuori da `lang()`, e il dizionario passa dopo sulle due `lang()`
che la toppa lascia intatte.

## Il tetto, misurato e non stimato

    tcg.hsp:3287   x@tcg = basex@tcg + 180 + cnt * 63     passo 63 px
    tcg.hsp:3300   gcopy 7, 360, 96, 63, 20               la linguetta e' 63
    tcg.hsp:3302   pos x@tcg + 1, y@tcg + 4               il testo parte da x+1
    tcg.hsp:3283   font ..., 10 + en - en * 2             corpo 9 (en == 1)

Il carattere della build inglese e' `Courier New`, monospaziato: 6,6 px a corpo
11 e 7,2 a 12, cioe' 0,6 per il corpo, quindi **5,4 px** a corpo 9.

    (63 - 2) / 5,4 = 11,3  ->  TETTO 11 CARATTERI

⭐ **L'ancora e' di monte**: l'etichetta inglese piu' lunga di tutt'e diciassette
le pagine e' `largeanimal`, **11 caratteri esatti**. E' la regola di
`guida-stile.md`: il metro e' l'inglese di monte, e da correggere sono solo i
nomi dove l'inglese ci sta e noi no.

⚠️ **Chi sfora non viene tagliato: viene coperto.** Le linguette si disegnano
in un ciclo solo, e lo sfondo della linguetta seguente (`gcopy`) si posa
**dopo** il testo di quella prima. Una parola troppo lunga finisce sotto la
linguetta accanto, che e' semitrasparente (`gmode 4, , , 120`): non sparisce,
sporca.

## Da dove vengono i nomi

⭐ **Cinquantadue delle sessantadue razze e classi non si decidono qui**: il
nome italiano c'e' gia' in `dizionario/db_race.hsp.jsonl` e
`dizionario/db_class.hsp.jsonl`, e ci sta nel tetto. Questo generatore lo
**legge di li'** invece di riscriverlo, cosi' il filtro non puo' allontanarsi
dalla carta: se il filtro dicesse «dragon» e la carta «Drago», il giocatore non
troverebbe le sue carte.

Le dieci che sforano sono l'unica decisione nuova, presa il 2026-09-04:
si tiene la parola del glossario e si abbrevia il resto col punto.

⚠️ **`cfname@tcg` e' solo visualizzazione**, verificato: l'unico lettore e'
`mes cfname@tcg(p@tcg)` (`tcg.hsp:3303`), e il filtro vero lavora sull'indice
(`cflist@tcg(ccf@tcg)`) e su `filtertype@tcg`, non sul nome. E' l'opposto delle
dodici classi di `action.hsp:13670`, che sono chiavi e non si toccano.
"""
from __future__ import annotations

import json
import re

from strumenti import accenti, percorsi

TETTO = 11

# La prima riga e l'ultima dell'assegnazione di `cfname@tcg` dentro
# `if ( deckmode@tcg == 0 )`. Fuori di li' `cfname@tcg` porta i nomi dei domini
# (`domname@tcg`), che stanno gia' nel dizionario di `tcg_mod.hsp`.
PRIMA_RIGA = 3552
ULTIMA_RIGA = 3632

# ⚠️ Le dieci abbreviazioni sono una decisione, non una derivata: il nome del
# glossario resta riconoscibile e si abbrevia il resto col punto. Dove la testa
# da sola sarebbe ambigua la si tiene: `Bestia` e' la testa di due razze
# diverse -- `beast` e `largeanimal` -- e da sola non distinguerebbe.
ABBREVIATE = {
    "beast": "Bestia f.",         # Bestia fantastica, 17
    "catgod": "Dio gatti",        # Dio dei gatti, 13
    "doggod": "Dio cani",         # Dio dei cani, 12
    "largeanimal": "Bestia gig.",  # Bestia gigante, 14
    "lizardman": "Uomo luc.",     # Uomo lucertola, 14
    "machinegod": "Dio macch.",   # Dio delle macchine, 18
    "seamonster": "Mostro mar.",  # Mostro marino, 13
    "servant": "Incarnaz.",       # Incarnazione, 12
    "undeadgod": "Dio non m.",    # Dio dei non morti, 17
    "warmage": "Mago guerr.",     # Mago guerriero, 14
}

# I nomi dei domini: la decisione e' gia' presa in `tcg_mod.hsp:3479-:3486`,
# dove il dizionario rende BLUE «BLU» e LEGENDARY «LEGGENDARIO». Qui la
# linguetta li scrive con l'iniziale maiuscola, come fa l'inglese.
DOMINI = {
    "Blue": "Blu", "Green": "Verde", "White": "Bianco", "Black": "Nero",
    "Neutral": "Neutro", "Legendary": "Leggendario", "Gray": "Grigio",
    "Red": "Rosso",
}

# Le etichette che non sono ne' razze ne' classi ne' domini.
# ⚠️ «Atk» e' «attacco» e «HP» e' «vita» in tutto il gioco di carte
# (`dizionario/carte/effdesc.jsonl`), e la linguetta mette il nome davanti al
# numero come fa gia' «Costo N».
ALTRE = {
    "All": "Tutte",
    "classless": "Nessuna",  # la stessa parola con cui db_class rende «None»
    "male": "Maschio", "female": "Femmina",
    "random": "Casuale", "other": "Altro",
}
for _n in range(9):
    ALTRE["Cost %d" % _n] = "Costo %d" % _n
ALTRE["Cost 8+"] = "Costo 8+"
ALTRE["1- Atk"] = "Attacco 1-"
ALTRE["9+ Atk"] = "Attacco 9+"
ALTRE["9+ HP"] = "Vita 9+"
for _n in range(2, 9):
    ALTRE["%d Atk" % _n] = "Attacco %d" % _n
for _n in range(1, 9):
    ALTRE["%d HP" % _n] = "Vita %d" % _n

_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
_SENZA_LETTERE = re.compile(r"^[^A-Za-z]*$")


def _nomi(file_dizionario: str) -> dict[str, str]:
    """Le rese gia' decise, lette dal dizionario invece che riscritte."""
    voci: dict[str, str] = {}
    percorso = percorsi.PROGETTO / "dizionario" / file_dizionario
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it"):
            voci.setdefault(voce["en"], voce["it"])
    return voci


def rese() -> dict[str, str]:
    """Etichetta inglese -> etichetta italiana, per tutte quelle con lettere.

    Alza `KeyError` su un'etichetta che nessuno ha deciso: un generatore che
    tira a indovinare scrive una resa che nessuno ha guardato.
    """
    razze = _nomi("db_race.hsp.jsonl")
    classi = _nomi("db_class.hsp.jsonl")
    fuori: dict[str, str] = {}
    for etichetta in etichette():
        if etichetta in ABBREVIATE:
            fuori[etichetta] = ABBREVIATE[etichetta]
        elif etichetta in DOMINI:
            fuori[etichetta] = DOMINI[etichetta]
        elif etichetta in ALTRE:
            fuori[etichetta] = ALTRE[etichetta]
        elif etichetta in razze:
            fuori[etichetta] = razze[etichetta]
        elif etichetta.capitalize() in classi:
            fuori[etichetta] = classi[etichetta.capitalize()]
        else:
            raise KeyError(
                "l'etichetta %r del menu dei filtri non ha una resa decisa: "
                "non e' una razza di db_race.hsp, non e' una classe di "
                "db_class.hsp, e non sta in nessuna delle tabelle di questo "
                "file. Il monte si e' mosso, oppure la tabella e' incompleta."
                % etichetta)
    return fuori


def righe_sorgente() -> list[tuple[int, str]]:
    testo = (percorsi.SORGENTE_HSP / "tcg.hsp").read_bytes().decode("cp932")
    righe = testo.split("\n")
    fuori = []
    for numero in range(PRIMA_RIGA, ULTIMA_RIGA + 1):
        riga = righe[numero - 1].rstrip("\r")
        if "cfname@tcg =" in riga:
            fuori.append((numero, riga))
    return fuori


def etichette() -> list[str]:
    """I letterali nudi delle diciassette righe, quelli che portano lettere.

    ⚠️ I sette intervalli di identificativo (`0-150`, `900+  `) non portano
    nemmeno una lettera: non sono testo e restano com'erano, esattamente come
    `disegnate.py` non li conta.
    """
    viste: list[str] = []
    for _numero, riga in righe_sorgente():
        coda = riga.split('"Deck")', 1)[-1]
        for pezzo in _LETTERALE.findall(coda):
            if not _SENZA_LETTERE.match(pezzo) and pezzo not in viste:
                viste.append(pezzo)
    return viste


def toppe() -> list[dict]:
    """Una toppa per riga: diciassette, tutte `prima`."""
    tabella = rese()
    fuori = []
    for numero, riga in righe_sorgente():
        testa, coda = riga.split('"Deck")', 1)

        def sostituisci(trovato: re.Match) -> str:
            pezzo = trovato.group(1)
            if _SENZA_LETTERE.match(pezzo):
                return trovato.group(0)
            return '"%s"' % tabella[pezzo]

        nuova = testa + '"Deck")' + _LETTERALE.sub(sostituisci, coda)
        if nuova == riga:
            continue
        fuori.append({
            "file": "tcg.hsp",
            "cerca": riga,
            "sostituisci": nuova,
            "prima": True,
            "motivo": (
                "Il menu dei filtri dell'editor di mazzo, pagina %d di 17 "
                "(tcg.hsp:%d). Letterali NUDI su una riga che porta anche due "
                "lang(): il dizionario prende «List» e «Deck» e queste "
                "restano inglesi, ed e' il caso per cui esiste la deroga "
                "`prima`. ⭐ Trovate dalla rete di `disegnate.py` nella 138a, "
                "dopo centotrentasei sessioni in cui nessun censimento le "
                "vedeva: `copertura._PROSA` pretende due parole alfabetiche e "
                "queste ne hanno una. ⚠️ Tetto 11 caratteri, misurato e non "
                "stimato: linguette a passo 63 px (:3287), testo a x+1 "
                "(:3302), `Courier New` a corpo 9 (:3283), 5,4 px per "
                "carattere; e l'ancora e' di monte, perche' `largeanimal` ne "
                "fa 11 esatti. Chi sfora non viene tagliato ma coperto dallo "
                "sfondo semitrasparente della linguetta seguente. ⚠️ I nomi "
                "di razza e classe NON si decidono qui: il generatore li "
                "legge da `db_race.hsp` e `db_class.hsp`, o il filtro direbbe "
                "una parola e la carta un'altra. ✅ `cfname@tcg` e' solo "
                "visualizzazione: l'unico lettore e' `mes cfname@tcg(p@tcg)` "
                "(:3303), e il filtro lavora sull'indice `cflist@tcg`, non "
                "sul nome. Generata da `strumenti/genera_toppe_filtri.py`."
                % (len(fuori) + 1, numero)),
        })
    return fuori


GENERATA = "filtri-mazzo"


def scrivi() -> int:
    """Riscrive le toppe generate dentro `toppe.jsonl`. Torna quante.

    ⚠️ Le generate del giro precedente si **sostituiscono**, non si accumulano:
    e' il modo di `genera_toppe_nomi.py`, e senza di lui una resa ritoccata
    lascerebbe in giro la sua versione vecchia. Le toppe scritte a mano non si
    toccano.
    """
    mie = toppe()
    righe_del_file = (percorsi.SORGENTE_HSP / "tcg.hsp") \
        .read_bytes().decode("cp932").split("\n")
    ripulite = [r.rstrip("\r") for r in righe_del_file]
    for toppa in mie:
        quante = ripulite.count(toppa["cerca"])
        if quante != 1:
            raise SystemExit(
                "la riga da cercare compare %d volte nel sorgente, non una: "
                "%r" % (quante, toppa["cerca"][:70]))
        toppa["generata"] = GENERATA

    percorso = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    a_mano = [t for t in esistenti if t.get("generata") != GENERATA]
    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for toppa in a_mano + mie:
            f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("  toppe a mano o d'altri generatori: %d, generate qui: %d "
          "(ne sostituiscono %d)"
          % (len(a_mano), len(mie), len(esistenti) - len(a_mano)))
    return len(mie)


def referto() -> list[str]:
    """Le rese, con la misura sulla forma degradata. Vuoto = nessuno sfora."""
    guai = []
    for etichetta, reso in rese().items():
        degradato = accenti.degrada(reso)
        if len(degradato) > TETTO:
            guai.append("%r -> %r: %d caratteri, il tetto e' %d"
                        % (etichetta, degradato, len(degradato), TETTO))
        if degradato != reso:
            guai.append("%r -> %r: la forma degradata e' %r e cambia la "
                        "misura" % (etichetta, reso, degradato))
    return guai


def main() -> None:
    import argparse
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--scrivi", action="store_true",
                              help="riscrive le toppe generate in toppe.jsonl")
    argomenti = analizzatore.parse_args()

    guai = referto()
    tabella = rese()
    print("  etichette con lettere : %d" % len(tabella))
    print("  righe toppate         : %d" % len(toppe()))
    piu_lunga = max(tabella.values(), key=lambda v: len(accenti.degrada(v)))
    print("  la piu' lunga         : %r, %d caratteri (tetto %d)"
          % (piu_lunga, len(accenti.degrada(piu_lunga)), TETTO))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        scrivi()
    print("\n  " + ("genera_toppe_filtri: nessuna etichetta sfora il tetto"
                    if not guai else "genera_toppe_filtri: %d fuori misura"
                    % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
