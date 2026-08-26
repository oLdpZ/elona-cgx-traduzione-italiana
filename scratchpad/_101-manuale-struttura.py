# -*- coding: utf-8 -*-
"""La struttura di `manual_ENG.txt`: sezioni, paragrafi, righe e numeri di riga.

    python scratchpad/_101-manuale-struttura.py                 # l'indice
    python scratchpad/_101-manuale-struttura.py "For Beginners" # una sezione

E' il ponte fra il file e il lotto: `dati_estrai` numera le righe **piene**
(1..591) e questo modulo dice, per ogni sezione, quali numeri le appartengono e
come sono raggruppate in paragrafi — cioe' quante righe deve occupare ogni
paragrafo italiano. Lo importano `_101-manuale-rese.py` e il referto.
"""
from __future__ import annotations

import io
import sys

MONTE = r"C:\Games\Elona\_traduzione\dati-sorgente\manual_ENG.txt"


def righe_numerate(percorso=MONTE):
    """[(numero o None, testo)] — il numero e' quello che usa `dati_estrai`."""
    testo = io.open(percorso, encoding="cp932").read()
    uscita, numero = [], 0
    for riga in testo.replace("\r\n", "\n").split("\n"):
        if riga.strip():
            numero += 1
            uscita.append((numero, riga))
        else:
            uscita.append((None, riga))
    return uscita


def sezioni(percorso=MONTE):
    """{titolo: {"numero": n, "paragrafi": [[(n, testo), ...], ...]}}.

    ⚠️ La testa del file — le due righe prima del primo `{}` — e' una sezione
    che il giocatore non vede mai nell'elenco ma che sta nel file e va tradotta
    lo stesso: qui si chiama `(testa)`.
    """
    elenco, titolo = {}, "(testa)"
    elenco[titolo] = {"numero": None, "paragrafi": []}
    paragrafo: list = []

    def chiudi():
        if paragrafo:
            elenco[titolo]["paragrafi"].append(list(paragrafo))
            paragrafo.clear()

    for numero, riga in righe_numerate(percorso):
        if riga.startswith("{}"):
            chiudi()
            titolo = riga[2:].strip()
            elenco[titolo] = {"numero": numero, "paragrafi": []}
        elif riga.strip():
            paragrafo.append((numero, riga))
        else:
            chiudi()
    chiudi()
    return elenco


def main():
    elenco = sezioni()
    if len(sys.argv) > 1:
        chiave = sys.argv[1]
        if chiave not in elenco:
            raise SystemExit(f"sezione ignota: {chiave!r}")
        sezione = elenco[chiave]
        print(f"{chiave}   (riga {sezione['numero']})")
        for i, paragrafo in enumerate(sezione["paragrafi"], 1):
            print(f"\n  -- paragrafo {i}: {len(paragrafo)} righe "
                  f"({paragrafo[0][0]}-{paragrafo[-1][0]})")
            for numero, riga in paragrafo:
                print(f"  {numero:4} |{riga}")
        return

    print(f"{'righe':>5} {'par.':>5}  sezione")
    for titolo, sezione in elenco.items():
        righe = sum(len(p) for p in sezione["paragrafi"])
        print(f"{righe:5} {len(sezione['paragrafi']):5}  {titolo}")


if __name__ == "__main__":
    main()
