# -*- coding: utf-8 -*-
"""Stampa un intervallo di righe di un file del sorgente.

    python scratchpad/_94-dump.py <file.hsp> da a [da a ...]
"""
import io, os, sys
BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
f = sys.argv[1]
r = io.open(os.path.join(BASE, f), encoding='cp932', errors='replace').read().split('\n')
n = sys.argv[2:]
for i in range(0, len(n), 2):
    a, b = int(n[i]), int(n[i + 1])
    for k in range(a, b + 1):
        print('%d: %s' % (k, r[k - 1].rstrip()))
    print('---')
