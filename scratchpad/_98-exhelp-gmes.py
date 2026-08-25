# -*- coding: utf-8 -*-
"""RETE: la geometria di `exhelp.txt`, cioe' la finestra dei consigli di Norne.

    python scratchpad/_98-exhelp-gmes.py            # la build (exhelp_it.txt)
    python scratchpad/_98-exhelp-gmes.py --monte    # l'inglese di monte, per taratura

⚠️⚠️ **IL METRO DEGLI ALTRI FILE DATI QUI MENTIREBBE.** `board.txt` e `talk.txt`
passano da `talk_conv`, che manda a capo **sulle spaziature** a un tetto in
caratteri; `exhelp.txt` non ci passa affatto. `help.hsp:227` lo carica con
`noteload` e `help.hsp:273` lo disegna con `gmes` (`module.hsp:4918`), che manda
a capo **per carattere**:

    locvar_gmes_lim = gmesx + gmesw           gmesw = 330 px   (help.hsp:264)
    if ( gmesx >= lim ) { a capo }            prima di disegnare
    gmesx += size / 2 * p                     size = 14, p = 1 per l'ASCII -> 7 px

cioe' il carattere k si disegna finche' 7k < 330, k < 47,14: **48 caratteri per
riga disegnata**. I marcatori `<emp1>` `<emp2>` `<def>` non consumano larghezza —
`gmes` li mangia con un `continue` — e percio' non si contano.

⚠️ **L'altezza e' il vincolo vero, non la larghezza.** La finestra e' alta 175 px
(`help.hsp:243`) e il testo parte a `wy + 55` (`:259`), quindi ne restano 120. Ogni
riga di nota costa `size + 4 = 18` px (`module.hsp:5017`) e ogni a capo dentro la
riga altri `size + 2 = 16` (`:5003`). Sei righe = 108 px, la settima sfonda:

    riga 0   in cima a wy + 55
    riga 5   in cima a wy + 145, il fondo del glifo a ~wy + 158   dentro
    riga 6   in cima a wy + 163, il fondo del glifo a ~wy + 176   FUORI

⭐ **E le due strade danno lo stesso numero**: il tetto geometrico dice 6 righe, e
il **corpus** di monte — quel che l'inglese ci fa stare — dice 108 px, cioe' sei
righe. Quando la misura dello schermo e quella del corpus coincidono il tetto non
e' una stima.

⚠️ Il gruppo e' quel che sta fra due righe vuote: `help.hsp:270` esce dal ciclo
appena `s == ""`, e li' il giocatore preme un tasto. Un gruppo di piu' di **10**
righe di nota verrebbe spezzato lo stesso da `repeat 10` (`:267`).
"""
import argparse
import io
import os
import re
import sys

MARCATORE = re.compile(r"<[^>]*>")

GMESW = 330            # help.hsp:264
PIXEL_PER_CARATTERE = 7    # module.hsp:5014, size 14 / 2
TETTO_RIGA = GMESW // PIXEL_PER_CARATTERE + 1     # 48
COSTO_RIGA = 18        # module.hsp:5017, size + 4
COSTO_CAPO = 16        # module.hsp:5003, size + 2
TETTO_ALTEZZA = 120    # help.hsp:243 e :259 — 175 di finestra meno 55 di cima
TETTO_NOTE = 10        # help.hsp:267

BUILD = r"C:\Games\Elona\_traduzione\build\dati\exhelp_it.txt"
MONTE = r"C:\Games\Elona\_traduzione\dati-sorgente\exhelp.txt"

INTESTAZIONE = re.compile(r"^%(\w+),(JP|EN)\s*$")


def visibile(riga):
    return MARCATORE.sub("", riga)


def righe_disegnate(riga):
    larghi = len(visibile(riga))
    return max(1, -(-larghi // TETTO_RIGA))


def gruppi(percorso):
    """I gruppi della sezione EN: (blocco, [righe]), spezzati sulle righe vuote."""
    testo = io.open(percorso, encoding="cp932", errors="replace").read()
    sezione = blocco = None
    corrente, uscita = [], []
    for grezza in testo.split("\n"):
        riga = grezza.rstrip("\r")
        secca = riga.strip()
        testa = INTESTAZIONE.match(secca)
        if testa:
            if corrente:
                uscita.append((blocco, corrente))
                corrente = []
            blocco, sezione = testa.group(1), testa.group(2)
            continue
        if secca.startswith("%END") or secca.startswith("#"):
            if corrente:
                uscita.append((blocco, corrente))
                corrente = []
            sezione = None
            continue
        if sezione != "EN":
            continue
        if secca == "":
            if corrente:
                uscita.append((blocco, corrente))
                corrente = []
            continue
        corrente.append(riga)
    if corrente:
        uscita.append((blocco, corrente))
    return uscita


def main():
    parla = argparse.ArgumentParser(description=__doc__)
    parla.add_argument("--monte", action="store_true",
                       help="misura l'inglese di monte invece della build")
    parla.add_argument("--file", help="un file qualsiasi, per provare la rete al contrario")
    scelte = parla.parse_args()

    percorso = scelte.file or (MONTE if scelte.monte else BUILD)
    if not os.path.exists(percorso):
        raise SystemExit(f"{percorso} non c'e': costruisci con "
                         "`python -m strumenti.dati_applica`")

    larghe, alte, lunghe = [], [], []
    massima = 0
    for blocco, gruppo in gruppi(percorso):
        altezza = sum(COSTO_RIGA + COSTO_CAPO * (righe_disegnate(r) - 1) for r in gruppo)
        massima = max(massima, altezza)
        if altezza > TETTO_ALTEZZA:
            alte.append((blocco, altezza, gruppo))
        if len(gruppo) > TETTO_NOTE:
            lunghe.append((blocco, len(gruppo)))
        for numero, riga in enumerate(gruppo, 1):
            largo = len(visibile(riga))
            if largo > TETTO_RIGA:
                larghe.append((blocco, numero, largo, riga))

    print(f"file: {percorso}")
    for blocco, numero, largo, riga in larghe:
        print(f"  LARGA    %{blocco} riga {numero}: {largo} caratteri, tetto "
              f"{TETTO_RIGA} — {visibile(riga)!r}")
    for blocco, altezza, gruppo in alte:
        print(f"  ALTA     %{blocco}: {altezza} px su {len(gruppo)} righe, tetto "
              f"{TETTO_ALTEZZA} — {visibile(gruppo[0])[:40]!r}...")
    for blocco, quante in lunghe:
        print(f"  SPEZZATA %{blocco}: {quante} righe di nota, `repeat {TETTO_NOTE}` "
              "ne disegna dieci e le altre le perde")

    print(f"\nrighe fuori misura: {len(larghe)}   gruppi troppo alti: {len(alte)}   "
          f"gruppi spezzati: {len(lunghe)}   (atteso: 0 0 0)")
    print(f"il gruppo piu' alto misura {massima} px su {TETTO_ALTEZZA} disponibili")
    return 1 if (larghe or alte or lunghe) else 0


if __name__ == "__main__":
    sys.exit(main())
