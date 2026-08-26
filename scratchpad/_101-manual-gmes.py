# -*- coding: utf-8 -*-
"""RETE: la geometria di `data\\manual_ENG.txt`, cioe' la guida in gioco.

    python scratchpad/_101-manual-gmes.py            # la build (manual_ENG_it.txt)
    python scratchpad/_101-manual-gmes.py --monte    # l'inglese di monte, per taratura

E' `scratchpad/_98-exhelp-gmes.py` puntato su un'altra finestra, e i due
vincoli sono gli stessi perche' a disegnare e' lo stesso `gmes`
(`module.hsp:4918`), chiamato da `help.hsp:468`:

    gmesw = 510 px          help.hsp:462
    7 px per carattere      module.hsp:5015 — `locvar_gmes_size` vale **14**
                            dentro `gmes`, qualunque font si sia scelto prima
    -> 73 caratteri per riga disegnata

⚠️⚠️ **QUI IL VINCOLO CHE MORDE E' L'ALTEZZA DELLA SEZIONE, NON LA LARGHEZZA.**
Una riga piu' lunga di 73 caratteri non si perde: `gmes` la manda a capo da
sola. Ma ogni a capo costa **16 px** (`module.hsp:5004`, `size + 2`) in una
pagina che ne ha **436** in tutto — 496 di finestra (`help.hsp:352`) meno i 60
a cui il testo comincia (`:461`) — e ogni riga del file ne costa gia' **18**
(`module.hsp:5017`, `size + 4`). Ventiquattro righe e la pagina e' piena.

⭐ **La sezione e' l'unita', e non c'e' impaginazione che la spezzi**: il ciclo
di `:465` disegna dalla riga dopo il `{}` fino al `{` successivo, e quel che
esce dalla finestra e' **perso**, non rimandato a una pagina dopo. `page_change`
impagina l'**elenco dei titoli**, non il corpo.

⚠️ **Due sezioni sfondano gia' in inglese**, e il referto le stampa: *Abnormal
States* (32 righe, 624 px) e *Ranged Weapons* (26 righe, 468 px). Non e' una
regressione nostra e non si aggiusta traducendo — ma dice che il metro e'
giusto, perche' un metro che desse tutto verde su un file che sfonda davvero
starebbe misurando un'altra cosa.

⭐ **Il tetto del titolo e' un'altra geometria ancora.** Il titolo della sezione
si legge in due posti: l'elenco a sinistra (`cs_list s, wx + 66`, `:479`) e
l'intestazione del corpo (`display_topic s(1), wx + 206`, `:458`). L'ostacolo
piu' a sinistra e' il corpo, che comincia a **wx + 216**: (216 - 66) / 7 fa
**21 caratteri**. L'inglese si ferma a 20, cioe' monte ci sta dentro per un
carattere — la lezione della 68a dice di guardare quel che si disegna piu' a
sinistra, non quel che viene dopo nel sorgente.
"""
import argparse
import io
import os
import re
import sys

MARCATORE = re.compile(r"<[^>]*>")

GMESW = 510                 # help.hsp:462
PIXEL_PER_CARATTERE = 7     # module.hsp:5015, size 14 / 2
TETTO_RIGA = GMESW // PIXEL_PER_CARATTERE + 1        # 73
COSTO_RIGA = 18             # module.hsp:5017, size + 4
COSTO_CAPO = 16             # module.hsp:5004, size + 2
TETTO_ALTEZZA = 496 - 60    # help.hsp:352 e :461 — 436 px
TETTO_TITOLO = (216 - 66) // PIXEL_PER_CARATTERE     # 21

BUILD = r"C:\Games\Elona\_traduzione\build\dati\manual_ENG_it.txt"
MONTE = r"C:\Games\Elona\_traduzione\dati-sorgente\manual_ENG.txt"


def visibile(riga):
    """Quel che `gmes` disegna: i marcatori `<emp1>` `<def>` li mangia."""
    return MARCATORE.sub("", riga)


def a_capo(riga):
    """Quante volte `gmes` manda a capo dentro una riga del file."""
    return max(1, -(-len(visibile(riga)) // TETTO_RIGA)) - 1


def sezioni(percorso):
    """(titolo, [righe del corpo]) — il corpo e' fin dove `help.hsp:467` legge."""
    testo = io.open(percorso, encoding="cp932").read()
    righe = testo.replace("\r\n", "\n").split("\n")
    uscita = []
    i = 0
    while i < len(righe):
        if righe[i].startswith("{}"):
            titolo = righe[i][2:].strip()
            corpo = []
            i += 1
            # ⚠️ `help.hsp:469` esce su un `{` QUALUNQUE, non su `{}`: la
            # condizione e' `instr(q, 0, "{") != -1`
            while i < len(righe) and "{" not in righe[i]:
                corpo.append(righe[i])
                i += 1
            uscita.append((titolo, corpo))
        else:
            i += 1
    return uscita


def altezza(corpo):
    return sum(COSTO_RIGA + COSTO_CAPO * a_capo(r) for r in corpo)


def main():
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--monte", action="store_true",
                              help="misura l'inglese di monte invece della build")
    analizzatore.add_argument("--tutte", action="store_true",
                              help="stampa tutte le sezioni, non solo quelle che sfondano")
    scelte = analizzatore.parse_args()

    percorso = MONTE if scelte.monte else BUILD
    if not os.path.exists(percorso):
        raise SystemExit(f"{percorso} non c'e'")
    print(f"file: {percorso}")
    print(f"tetto: {TETTO_RIGA} caratteri per riga disegnata, "
          f"{TETTO_ALTEZZA} px di pagina, {TETTO_TITOLO} caratteri di titolo\n")

    elenco = sezioni(percorso)
    alte, titoli_larghi = [], []
    for titolo, corpo in elenco:
        h = altezza(corpo)
        if h > TETTO_ALTEZZA:
            alte.append((h, titolo, len(corpo)))
        if len(visibile(titolo)) > TETTO_TITOLO:
            titoli_larghi.append((len(visibile(titolo)), titolo))

    if scelte.tutte:
        for titolo, corpo in elenco:
            h = altezza(corpo)
            segno = "  ⚠️ SFONDA" if h > TETTO_ALTEZZA else ""
            print(f"  {h:4} px  {len(corpo):3} righe   {titolo}{segno}")
        print()

    for h, titolo, n in sorted(alte, reverse=True):
        print(f"  ALTA    {titolo}: {h} px su {TETTO_ALTEZZA}, {n} righe "
              f"({(h - TETTO_ALTEZZA + COSTO_RIGA - 1) // COSTO_RIGA} righe di troppo)")
    for n, titolo in sorted(titoli_larghi, reverse=True):
        print(f"  TITOLO  {titolo!r}: {n} caratteri su {TETTO_TITOLO}")

    piu_alta = max(altezza(c) for _, c in elenco)
    print(f"\nsezioni: {len(elenco)}   che sfondano in altezza: {len(alte)}   "
          f"titoli fuori misura: {len(titoli_larghi)}")
    print(f"la sezione piu' alta misura {piu_alta} px su {TETTO_ALTEZZA}")
    print("⚠️ atteso sull'inglese di monte: 2 sezioni alte (Abnormal States, "
          "Ranged Weapons) e 0 titoli fuori misura")
    # ⚠️ Le due sezioni alte sono di monte: la rete non puo' pretendere zero,
    # ma **non deve peggiorare**. Il numero da confrontare e' quello.
    return 1 if len(alte) > 2 or titoli_larghi else 0


if __name__ == "__main__":
    sys.exit(main())
