# -*- coding: utf-8 -*-
"""Dove si addensano le voci che restano, per scegliere la zona."""
import io, json, sys, collections

sorgente = sys.argv[1]
passo = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
voci = [json.loads(l) for l in io.open(sorgente, encoding='utf-8') if l.strip()]
c = collections.Counter(v['riga'] // passo * passo for v in voci)
for k in sorted(c):
    barra = '#' * min(60, c[k])
    print(f'{k:7d}-{k+passo-1:<7d} {c[k]:4d} {barra}')
print(f'--- {len(voci)} voci in tutto')
