"""Quanto pesa la DIFFERENZA fra l'eseguibile ufficiale e il nostro.

E' la misura che decide se la patch binaria vale: se i due file condividono
poco, la «patch» sarebbe grande quanto il gioco e tanto varrebbe chiedere il
permesso e pubblicare l'eseguibile.

Il metodo e' quello di rsync/bsdiff: si indicizzano i blocchi del file di
partenza e si cerca, per ogni posizione del file d'arrivo, il piu' lungo pezzo
che si puo' COPIARE invece che scrivere. Quel che non si copia e' letterale.
"""
import lzma
import sys
import zlib
from pathlib import Path

UFFICIALE = Path(r"C:\Games\Elona\elonaplus2.31\elonapluscgx.exe")
NOSTRO = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe")
BLOCCO = 64


def delta(sorgente: bytes, arrivo: bytes):
    indice = {}
    for i in range(0, len(sorgente) - BLOCCO + 1, BLOCCO):
        indice.setdefault(sorgente[i:i + BLOCCO], i)

    istruzioni = []          # ("copia", off, lung) | ("scrivi", inizio, fine)
    letterali = bytearray()
    p = 0
    inizio_letterale = 0
    n = len(arrivo)
    while p <= n - BLOCCO:
        posto = indice.get(arrivo[p:p + BLOCCO])
        if posto is None:
            p += 1
            continue
        # allunga in avanti
        fine_s, fine_a = posto + BLOCCO, p + BLOCCO
        while (fine_s < len(sorgente) and fine_a < n
               and sorgente[fine_s] == arrivo[fine_a]):
            fine_s += 1
            fine_a += 1
        # allunga all'indietro, senza rientrare nel letterale gia' chiuso
        inizio_s, inizio_a = posto, p
        while (inizio_s > 0 and inizio_a > inizio_letterale
               and sorgente[inizio_s - 1] == arrivo[inizio_a - 1]):
            inizio_s -= 1
            inizio_a -= 1
        if inizio_a > inizio_letterale:
            letterali += arrivo[inizio_letterale:inizio_a]
            istruzioni.append(("scrivi", inizio_a - inizio_letterale))
        istruzioni.append(("copia", inizio_s, fine_s - inizio_s))
        p = fine_a
        inizio_letterale = fine_a
    if inizio_letterale < n:
        letterali += arrivo[inizio_letterale:]
        istruzioni.append(("scrivi", n - inizio_letterale))
    return istruzioni, bytes(letterali)


def main():
    sorgente = UFFICIALE.read_bytes()
    arrivo = NOSTRO.read_bytes()
    print("ufficiale : %10d byte  %s" % (len(sorgente), UFFICIALE.name))
    print("nostro    : %10d byte" % len(arrivo))
    print()

    istruzioni, letterali = delta(sorgente, arrivo)
    copie = sum(1 for i in istruzioni if i[0] == "copia")
    copiati = sum(i[2] for i in istruzioni if i[0] == "copia")
    print("istruzioni: %d  (%d copie)" % (len(istruzioni), copie))
    print("copiati   : %10d byte  = %.1f%% del nostro"
          % (copiati, 100.0 * copiati / len(arrivo)))
    print("letterali : %10d byte" % len(letterali))
    print()
    # 12 byte per istruzione e' la stima larga: tipo + due interi
    grezza = len(letterali) + 12 * len(istruzioni)
    print("patch grezza      : %10d byte" % grezza)
    print("  con zlib        : %10d byte"
          % (len(zlib.compress(letterali, 9)) + 12 * len(istruzioni)))
    print("  letterali in xz : %10d byte" % len(lzma.compress(letterali)))
    print()
    print("per confronto, il nostro eseguibile intero:")
    print("  con zlib        : %10d byte" % len(zlib.compress(arrivo, 9)))
    print("  con xz          : %10d byte" % len(lzma.compress(arrivo)))


if __name__ == "__main__":
    main()
