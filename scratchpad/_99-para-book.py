# -*- coding: utf-8 -*-
"""I paragrafi di un blocco di `book.txt`: dove monte ha messo le righe vuote.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-para-book.py 9

⚠️ Serve perche' la numerazione della firma salta le righe vuote: nel lotto il
blocco e' un elenco continuo, ma nel file le righe vuote **separano i
paragrafi**, e dentro un paragrafo il testo si puo' ridistribuire mentre da un
paragrafo all'altro no. Qui si vede il confine.
"""
import io
import sys

from strumenti import dati, percorsi

MONTE = percorsi.DATI_SORGENTE / "book.txt"


def main(chiave):
    documento = dati.analizza(io.open(MONTE, encoding="cp932", errors="replace").read())
    blocco = documento.blocco(chiave, "EN")
    if blocco is None:
        raise SystemExit(f"%{chiave}: non c'e'")

    numero = 0
    gruppo = []
    gruppi = []
    for indice in blocco.indici:
        testo = documento.riga(indice)
        if testo.strip():
            numero += 1
            gruppo.append(numero)
        elif gruppo:
            gruppi.append(gruppo)
            gruppo = []
    if gruppo:
        gruppi.append(gruppo)

    print(f"%{chiave}: {len(gruppi)} paragrafi, {numero} righe piene")
    for g in gruppi:
        print(f"  {g[0]}-{g[-1]}  ({len(g)} righe)" if len(g) > 1 else f"  {g[0]}"
              "        (1 riga)")


if __name__ == "__main__":
    main(sys.argv[1])
