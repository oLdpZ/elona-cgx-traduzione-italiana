# -*- coding: utf-8 -*-
import io, json, glob, os, sys
pat = sys.argv[1:]
for f in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(f, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        s = v.get('en', '') + v.get('jp', '') + v.get('it', '')
        if any(p in s for p in pat):
            print('%s:%s' % (os.path.basename(f), v['riga']))
            print('   EN %s' % v.get('en', '')[:140])
            print('   IT %s' % v.get('it', '')[:160])
