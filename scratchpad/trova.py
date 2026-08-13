# -*- coding: utf-8 -*-
"""Cerca frammenti inglesi nell'estrazione, per trovare la zona giusta."""
import io, json, sys

sorgente = sys.argv[1]
aghi = [a.lower() for a in sys.argv[2:]]
voci = [json.loads(l) for l in io.open(sorgente, encoding='utf-8') if l.strip()]
trovate = []
for v in voci:
    testo = (v['en_grezzo'] or '').lower()
    if any(a in testo for a in aghi):
        trovate.append(v)
trovate.sort(key=lambda v: v['riga'])
for v in trovate:
    print(f"{v['riga']:6d} [{v['tipo'][:3]}] {v['en_grezzo'][:120]}")
print(f'--- {len(trovate)} voci')
