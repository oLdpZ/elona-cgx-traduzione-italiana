# -*- coding: utf-8 -*-
import io, json, sys
da, a = int(sys.argv[1]), int(sys.argv[2])
for l in io.open('dizionario/chat.hsp.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    v = json.loads(l)
    if da <= v['riga'] <= a and (v.get('it') or '').strip():
        print('--- %d' % v['riga'])
        print('EN %s' % v.get('en', '')[:180])
        print('IT %s' % v['it'][:200])
