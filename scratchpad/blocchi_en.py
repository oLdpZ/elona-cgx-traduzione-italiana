# -*- coding: utf-8 -*-
"""I blocchi `if ( en ) { ... }` con letterali nudi fuori da lang().

Sono invisibili a estrai.py: la meta' inglese della frase non e' nel
dizionario e resta inglese anche quando la meta' dentro lang() e' tradotta.
"""
import io, re, sys, glob, os

BASE = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
file_da_guardare = sys.argv[1:] or [os.path.basename(p) for p in glob.glob(BASE + r'\*.hsp')]

_LETTERALE = re.compile(r'"[^"]*[A-Za-z][^"]*"')

totale = 0
for nome in sorted(file_da_guardare):
    t = io.open(os.path.join(BASE, nome), encoding='cp932').read().split('\n')
    trovati = []
    dentro = False
    prof = 0
    for i, riga in enumerate(t):
        s = riga.strip()
        if re.match(r'^if\s*\(\s*en\s*\)\s*\{?\s*$', s):
            dentro, prof = True, 0
            continue
        if dentro:
            prof += riga.count('{') - riga.count('}')
            if 'lang(' not in riga and _LETTERALE.search(riga):
                trovati.append((i + 1, s[:120]))
            if prof < 0 or (prof == 0 and '}' in riga):
                dentro = False
    if trovati:
        print(f'=== {nome}: {len(trovati)} righe')
        for n, s in trovati:
            print(f'  {n:6d} | {s}')
        totale += len(trovati)
print(f'--- {totale} righe in tutto')
