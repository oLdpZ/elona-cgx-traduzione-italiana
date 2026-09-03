"""Mette la testa della 133a in cima a `RIPRESA-sessione.md`.

La testa vecchia (dalla riga 1 fino al primo `## La centotrentunesima sessione`)
diventa storia: le si mette sopra il titolo della sua sessione e la si lascia
dov'e'. Il resto del documento non si tocca.

    PYTHONIOENCODING=utf-8 python scratchpad/_133-chiude.py [--scrivi]
"""
from __future__ import annotations

import sys
from pathlib import Path

RIPRESA = Path("RIPRESA-sessione.md")
TESTA = Path("scratchpad/_133-testa-ripresa.md")
CONFINE = "## La centotrentunesima sessione (per storia)"


def main() -> int:
    scrivi = "--scrivi" in sys.argv
    testo = RIPRESA.read_text(encoding="utf-8")
    taglio = testo.find(CONFINE)
    if taglio == -1:
        print("non trovo %r: la testa non e' quella che credevo" % CONFINE)
        return 1

    vecchia = testo[:taglio]
    resto = testo[taglio:]
    nuova = TESTA.read_text(encoding="utf-8")

    # la testa vecchia era della 132a e non lo diceva: ora lo dice, e le righe
    # che parlavano al presente ("l'eseguibile e' ancora quello delle 02:00")
    # restano leggibili perche' hanno sopra il titolo che le data.
    corpo = nuova.rstrip("\n") + "\n\n" + vecchia.split("\n", 1)[1].lstrip("\n") + resto

    print("testa vecchia: %d righe -> diventa storia sotto il suo titolo"
          % vecchia.count("\n"))
    print("testa nuova:   %d righe" % nuova.count("\n"))
    if scrivi:
        RIPRESA.write_text(corpo, encoding="utf-8")
        print("scritto %s (%d righe)" % (RIPRESA, corpo.count("\n")))
    else:
        print("(prova a vuoto: aggiungi --scrivi)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
