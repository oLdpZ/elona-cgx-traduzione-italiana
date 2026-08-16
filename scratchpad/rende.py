# -*- coding: utf-8 -*-
"""Cerca un frammento INGLESE in tutto il dizionario e mostra come e' stato reso.

    python scratchpad/rende.py "shadow step" [--max 40]

Serve a non inventare un traducente che il progetto ha gia' deciso altrove:
e' la domanda «questa parola l'ho gia' resa?» fatta in un comando solo.
"""
import glob
import io
import json
import sys

argv = [a for a in sys.argv[1:]]
massimo = 40
if '--max' in argv:
    i = argv.index('--max')
    massimo = int(argv[i + 1])
    del argv[i:i + 2]
aghi = [a.lower() for a in argv]

for f in sorted(glob.glob('dizionario/*.jsonl')):
    nome = f.replace('\\', '/').split('/')[-1]
    trovate = []
    for l in io.open(f, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        en = (d.get('en') or '').lower()
        if any(a in en for a in aghi):
            trovate.append(d)
    for d in trovate[:massimo]:
        print(f"{nome}:{d['riga']}")
        print(f"    en = {d.get('en')!r}")
        print(f"    it = {d.get('it')!r}")
    if len(trovate) > massimo:
        print(f"  ... e altre {len(trovate) - massimo} in {nome}")
