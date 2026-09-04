# strumenti/genera_toppe_riga_stato.py
"""La riga di stato dell'editor di mazzo: che ordinamento e che filtro sono attivi.

`tcg.hsp:3348-:3360` monta con tredici `+=` la riga che l'editor di mazzo
scrive in fondo alla schermata — «Sort by: Cost   Filter: Domain   » — e la
disegna quindici righe piu' giu' (`mes s@tcg`, `:3363`).

⚠️⚠️ **Nessuna delle due reti del progetto la vedeva, e per due motivi
diversi.** `copertura._PROSA` pretende due parole alfabetiche e ne contava solo
cinque su tredici: «Filter: DBID» non gli basta. `disegnate.py` fa **un salto
solo** e da un'assegnazione semplice: qui il valore arriva per `+=` ripetuti e
viene disegnato altrove, cioe' e' esattamente il **secondo salto** che la 139a
aveva messo fra le cose da misurare. Il risultato e' che tredici etichette
stavano a schermo, in inglese, dentro un file dichiarato e contato, e il
referto diceva cinque.

## Il tetto, misurato e non stimato

    tcg_mod.hsp:3490   basew@tcg = 800                    il pannello e' largo 800
    tcg.hsp:3362       pos basex@tcg + 130, basey@tcg + 500   la riga parte a 130
    tcg.hsp:3345       font ..., 13 - en * 2              corpo 11 (en == 1)

`Courier New` monospaziato fa **6,6 px a corpo 11** (`decisioni.md`, la misura
delle carte), e la riga di sopra non ha niente alla sua destra:

    (800 - 130) / 6,6 = 101,5  ->  TETTO 101 CARATTERI

⭐ **L'ancora e' di monte, e sta sulla riga di sotto.** `tcg.hsp:3366` scrive la
legenda dei tasti a `basex + 130` e `tcg.hsp:3368` scrive «Pag. N/M» a
`basex + 700`: quella riga ha percio' 570 px, cioe' 86 caratteri, e la legenda
inglese ne fa 77. Due misure indipendenti che stanno d'accordo.

⚠️ **Il tetto vale sulla COPPIA, non sulla singola etichetta**: la riga porta
sempre un ordinamento **e** un filtro, concatenati. Il cancello misura la
coppia peggiore.

## Le rese

Le parole non sono nuove: `Domain` e' «dominio» in `glossario.md` (con la sua
toppa), e `Cost`, `Attack`, `Hp` sono «Costo», «Attacco», «Vita» nelle
linguette del menu dei filtri decise dalla 139a
(`genera_toppe_filtri.ALTRE`). ⚠️ **`DBID` resta `DBID`**: e' il numero di
riga del database delle carte, non una parola.
"""
from __future__ import annotations

import json
import re

from strumenti import percorsi

TETTO = 101

PRIMA_RIGA = 3348
ULTIMA_RIGA = 3360

# Letterale inglese -> letterale italiano. Le tre spaziature in coda separano
# l'ordinamento dal filtro e si conservano com'erano.
RESE = {
    "Sort by: DBID   ": "Ordina per: DBID   ",
    "Sort by: Domain   ": "Ordina per: Dominio   ",
    "Sort by: Cost   ": "Ordina per: Costo   ",
    "Sort by: Attack   ": "Ordina per: Attacco   ",
    "Sort by: Hp   ": "Ordina per: Vita   ",
    "Filter: DBID   ": "Filtro: DBID   ",
    "Filter: Domain   ": "Filtro: Dominio   ",
    "Filter: Cost   ": "Filtro: Costo   ",
    "Filter: Attack   ": "Filtro: Attacco   ",
    "Filter: Hp   ": "Filtro: Vita   ",
    "Filter: Race": "Filtro: Razza",
    "Filter: Class1   ": "Filtro: Classe1   ",
    "Filter: Class2 & Sex   ": "Filtro: Classe2 e sesso   ",
}

_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
# ⚠️ `:3358` spezza in due il suo letterale per infilarci il numero di razza:
#    `"Filter: Race" + (filtertype@tcg - 4) + "   "`. La coda e' spaziatura
#    pura, non testo, e resta com'e' — come i sette intervalli di
#    identificativo del menu dei filtri.
_SENZA_LETTERE = re.compile(r"^[^A-Za-z]*$")

GENERATA = "riga-stato-mazzo"


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe() -> list[str]:
    testo = (percorsi.SORGENTE_HSP / "tcg.hsp").read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def righe_sorgente() -> list[tuple[int, str]]:
    """(numero, riga) delle tredici righe che montano `s@tcg`."""
    righe = _righe()
    fuori = []
    for numero in range(PRIMA_RIGA, ULTIMA_RIGA + 1):
        riga = righe[numero - 1]
        if "s@tcg +=" not in riga:
            raise MonteMosso(
                "tcg.hsp:%d doveva montare `s@tcg +=` e dice %r: il blocco "
                "della riga di stato si e' mosso, e i numeri di riga qui "
                "vanno rifatti guardando, non aggiornati a mano."
                % (numero, riga.strip()))
        fuori.append((numero, riga))
    return fuori


# (file, riga, testo atteso, che cosa dichiara) — le tre misure da cui il tetto
# deriva. Stanno qui, e non dentro la funzione, perche' una prova possa
# esercitare il cancello invece di fidarsi che ci sia.
GEOMETRIA = [
    ("tcg_mod.hsp", 3490, "basew@tcg = 800", "la larghezza del pannello"),
    ("tcg.hsp", 3362, "pos basex@tcg + 130, basey@tcg + 500",
     "dove la riga comincia"),
    ("tcg.hsp", 3345, "font lang(cfg_font1, cfg_font2), 13 - en * 2, 0",
     "il corpo"),
]


def _controlla_geometria() -> None:
    """Rilegge dal sorgente i tre numeri da cui il tetto deriva."""
    for nome, numero, atteso, che_cosa in GEOMETRIA:
        percorso = percorsi.SORGENTE_HSP / nome
        riga = percorso.read_bytes().decode("cp932").split("\n")[numero - 1]
        if riga.strip() != atteso:
            raise MonteMosso(
                "%s:%d dichiarava %s con %r e ora dice %r. Il tetto di %d "
                "caratteri veniva da li': va rifatta la misura."
                % (percorso.name, numero, che_cosa, atteso, riga.strip(),
                   TETTO))


def coppia_peggiore(tabella: dict[str, str]) -> tuple[str, str, int]:
    """L'ordinamento e il filtro piu' lunghi, e quanto misura la loro somma.

    ⚠️ Il tetto vale sulla coppia: la riga porta sempre tutt'e due.
    """
    ordinamenti = [v for k, v in tabella.items() if k.startswith("Sort by")]
    filtri = [v for k, v in tabella.items() if k.startswith("Filter")]
    # «Filtro: Razza» prende in coda una cifra e le tre spaziature.
    filtri = [f + "N   " if f == tabella["Filter: Race"] else f
              for f in filtri]
    ordine = max(ordinamenti, key=len)
    filtro = max(filtri, key=len)
    return ordine, filtro, len(ordine) + len(filtro)


def problemi() -> list[str]:
    """Vuoto = nessuna resa e' fuori misura o fuori tabella."""
    guai = []
    for numero, riga in righe_sorgente():
        for pezzo in _LETTERALE.findall(riga):
            if _SENZA_LETTERE.match(pezzo):
                continue
            if pezzo not in RESE:
                guai.append(
                    "tcg.hsp:%d porta il letterale %r e la tabella non lo ha: "
                    "o il monte ha aggiunto un modo di ordinare, o la tabella "
                    "e' incompleta." % (numero, pezzo))
    for inglese, italiano in RESE.items():
        if not italiano.isascii():
            guai.append("%r -> %r: non e' ASCII, e la build e' CP932"
                        % (inglese, italiano))
        if italiano.strip() and italiano.endswith(" ") != inglese.endswith(" "):
            guai.append(
                "%r -> %r: la spaziatura in coda separa l'ordinamento dal "
                "filtro e non si tocca" % (inglese, italiano))
    ordine, filtro, misura = coppia_peggiore(RESE)
    if misura > TETTO:
        guai.append(
            "la coppia peggiore %r + %r fa %d caratteri e il tetto e' %d: "
            "la riga uscirebbe dal pannello."
            % (ordine, filtro, misura, TETTO))
    return guai


def toppe() -> list[dict]:
    _controlla_geometria()
    fuori = []
    for numero, riga in righe_sorgente():
        def sostituisci(trovato: re.Match) -> str:
            pezzo = trovato.group(1)
            if _SENZA_LETTERE.match(pezzo):
                return trovato.group(0)
            return '"%s"' % RESE[pezzo]

        nuova = _LETTERALE.sub(sostituisci, riga)
        if nuova == riga:
            continue
        fuori.append({
            "file": "tcg.hsp",
            "cerca": riga,
            "sostituisci": nuova,
            "motivo": (
                "La riga di stato dell'editor di mazzo, %d di 13 "
                "(tcg.hsp:%d): quale ordinamento e quale filtro sono attivi. "
                "⚠️⚠️ Letterali NUDI che nessuna delle due reti vedeva: "
                "`copertura._PROSA` pretende due parole alfabetiche e ne "
                "contava 5 su 13, e `disegnate.py` fa un salto solo da "
                "un'assegnazione semplice mentre qui il valore si monta con "
                "tredici `+=` e si disegna quindici righe piu' giu' "
                "(`mes s@tcg`, :3363) — e' il SECONDO SALTO che la 139a aveva "
                "messo fra le cose da misurare. ⚠️ Tetto %d caratteri sulla "
                "COPPIA ordinamento+filtro, misurato: pannello largo 800 "
                "(`tcg_mod.hsp:3490`), riga a `basex + 130` (:3362), "
                "`Courier New` a corpo 11 (:3345), 6,6 px per carattere; e "
                "l'ancora di monte e' la riga di sotto, che in 570 px scrive "
                "77 caratteri di legenda. ⭐ Le parole non sono nuove: "
                "«dominio» sta in glossario.md, «Costo», «Attacco» e «Vita» "
                "sono quelle delle linguette decise dalla 139a. `DBID` resta "
                "`DBID`: e' il numero di riga del database, non una parola. "
                "Generata da `strumenti/genera_toppe_riga_stato.py`."
                % (len(fuori) + 1, numero, TETTO)),
            "generata": GENERATA,
        })
    return fuori


def scrivi() -> int:
    mie = toppe()
    righe = _righe()
    for toppa in mie:
        quante = righe.count(toppa["cerca"])
        if quante != 1:
            raise SystemExit(
                "la riga da cercare compare %d volte, non una: %r"
                % (quante, toppa["cerca"][:70]))
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    altre = [t for t in esistenti if t.get("generata") != GENERATA]
    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for toppa in altre + mie:
            f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("  toppe a mano o d'altri generatori: %d, generate qui: %d "
          "(ne sostituiscono %d)"
          % (len(altre), len(mie), len(esistenti) - len(altre)))
    return len(mie)


def main() -> None:
    import argparse
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--scrivi", action="store_true",
                              help="riscrive le toppe generate in toppe.jsonl")
    argomenti = analizzatore.parse_args()

    _controlla_geometria()
    guai = problemi()
    ordine, filtro, misura = coppia_peggiore(RESE)
    print("  righe della riga di stato : %d" % len(righe_sorgente()))
    print("  righe toppate             : %d" % (len(toppe()) if not guai else 0))
    print("  la coppia peggiore        : %r + %r = %d caratteri (tetto %d)"
          % (ordine, filtro, misura, TETTO))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        scrivi()
    print("\n  " + ("genera_toppe_riga_stato: la coppia peggiore sta nel "
                    "pannello" if not guai
                    else "genera_toppe_riga_stato: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
