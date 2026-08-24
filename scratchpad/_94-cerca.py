# -*- coding: utf-8 -*-
"""Cerca una stringa (UTF-8) nel sorgente CP932.

    python scratchpad/_94-cerca.py <testo> [file.hsp ...]
"""
import io, os, sys, glob
BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
ago = sys.argv[1]
files = sys.argv[2:] or [os.path.basename(p) for p in glob.glob(os.path.join(BASE, '*.hsp'))]
for f in files:
    try:
        r = io.open(os.path.join(BASE, f), encoding='cp932', errors='replace').read().split('\n')
    except IOError:
        continue
    for n, l in enumerate(r, 1):
        if ago in l:
            print('%s:%d: %s' % (f, n, l.strip()[:220]))
