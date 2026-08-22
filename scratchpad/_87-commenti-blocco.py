# -*- coding: utf-8 -*-
"""I commenti /* ... */ MULTIRIGA di chat.hsp che contengono graffe.

Sono la trappola del confine: `_86-parlanti-oltre.py` toglie solo i commenti
di blocco che cominciano e finiscono sulla STESSA riga, quindi conta le
graffe commentate dei blocchi BLOODYSHADE CUSTOM / ORIGINAL.
"""
import io
import re
import sys

SORG = sys.argv[1] if len(sys.argv) > 1 else \
    r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'

testo = io.open(SORG, encoding='cp932', errors='replace').read()
righe = testo.split('\n')

# posizione (riga) di ogni carattere
inizio_riga = []
p = 0
for r in righe:
    inizio_riga.append(p)
    p += len(r) + 1


def riga_di(pos):
    lo, hi = 0, len(inizio_riga) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if inizio_riga[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1


tot = 0
for m in re.finditer(r'/\*.*?\*/', testo, re.S):
    corpo = m.group(0)
    if '\n' not in corpo:
        continue
    ap, ch = corpo.count('{'), corpo.count('}')
    if ap or ch:
        tot += ap - ch
        a, b = riga_di(m.start()), riga_di(m.end())
        print(':%d-:%d   { %d   } %d   %s' % (a, b, ap, ch, righe[a - 1].strip()[:80]))

print()
print('sbilanciamento totale portato dai commenti multiriga: %+d' % tot)
