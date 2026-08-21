# -*- coding: utf-8 -*-
import io, json
n = 0
for l in io.open('dizionario/chat.hsp.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    v = json.loads(l)
    if v['tipo'] == 'dinamica' and v.get('it') and '+' in v.get('en_grezzo', ''):
        if '+' not in v['it']:
            print('%s\n  EN %s\n  IT %s' % (v['riga'], v['en_grezzo'][:150], v['it'][:150]))
            n += 1
    if n > 8:
        break
