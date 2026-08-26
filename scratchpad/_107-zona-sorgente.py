"""Dump di una zona di righe di un file del SORGENTE pinnato, decodificato in UTF-8.

`zona.py` legge l'estrazione e `dossier.py` il dizionario: nessuno dei due serve
per un file che il dizionario non ha ancora, come `db_item.hsp`. Questo legge il
sorgente e basta.

    python scratchpad/_107-zona-sorgente.py db_item.hsp 42400 42480
"""
import sys

from strumenti.percorsi import SORGENTE_HSP


def main() -> None:
    nome = sys.argv[1]
    da = int(sys.argv[2])
    a = int(sys.argv[3])
    righe = (SORGENTE_HSP / nome).read_text(encoding="cp932").splitlines()
    for n in range(da, min(a, len(righe)) + 1):
        print(f"{n:>7}  {righe[n - 1]}")


if __name__ == "__main__":
    main()
