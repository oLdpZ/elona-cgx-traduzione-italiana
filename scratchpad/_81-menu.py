# -*- coding: utf-8 -*-
import io, json
voci = [json.loads(l) for l in io.open('dizionario/chat.hsp.jsonl', encoding='utf-8') if l.strip()]
d = {}
for v in voci:
    d.setdefault(v['riga'], v)
src = io.open(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\chat.hsp', encoding='cp932', errors='replace').read().split('\n')
n = 0
for i, l in enumerate(src):
    if 'chatlist' in l.lower() and (i + 1) in d and d[i + 1].get('it'):
        print('%6d EN %-58s | IT %s' % (i + 1, d[i + 1].get('en', '')[:58], d[i + 1]['it'][:58]))
        n += 1
    if n > 40:
        break
