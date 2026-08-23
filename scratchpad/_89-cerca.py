# -*- coding: utf-8 -*-
"""Cerca nel dizionario intero per giapponese, inglese o italiano.

    python scratchpad/_89-cerca.py <ago> [ago ...]
"""
import glob, io, json, os, sys

voci = []
for f in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(f, encoding='utf-8'):
        if l.strip():
            v = json.loads(l)
            v['_file'] = os.path.basename(f)
            voci.append(v)

for ago in sys.argv[1:]:
    print('=== %s' % ago)
    n = 0
    for v in voci:
        campi = (v.get('jp') or '') + '\x00' + (v.get('en') or '') + '\x00' + (v.get('it') or '')
        if ago in campi:
            n += 1
            if n > 12:
                continue
            print('  %s:%s' % (v['_file'], v['riga']))
            print('     jp %s' % (v.get('jp') or '')[:200])
            print('     en %s' % (v.get('en') or '')[:200])
            print('     it %s' % (v.get('it') or '')[:200])
    print('  (%d in tutto)' % n)
