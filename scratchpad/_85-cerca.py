# -*- coding: utf-8 -*-
"""Cerca nel dizionario per testo inglese, giapponese o italiano.

    python scratchpad/_85-cerca.py --en "Origin of Vice" [--max 8]
    python scratchpad/_85-cerca.py --jp "常闇の眼"
    python scratchpad/_85-cerca.py --it "diario"
"""
import io, json, sys, glob, re

campo = 'en'
if sys.argv[1] in ('--en', '--jp', '--it'):
    campo = sys.argv[1][2:]
ago = sys.argv[2]
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 8
chiave = {'en': 'en', 'jp': 'jp', 'it': 'it'}[campo]
n = 0
for p in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if ago.lower() in (v.get(chiave) or '').lower() and (v.get('it') or '').strip():
            print('%s:%s' % (p.split('/')[-1].replace('.jsonl', ''), v['riga']))
            print('   JP %s' % (v.get('jp') or '')[:120])
            print('   EN %s' % (v.get('en') or '')[:160])
            print('   IT %s' % (v.get('it') or '')[:180])
            n += 1
            if n >= mx:
                sys.exit()
