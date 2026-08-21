# -*- coding: utf-8 -*-
"""Come chat-lotto-dump.py, ma stampa anche il giapponese grezzo."""
import io, json, sys

def main() -> int:
    zone = [tuple(int(x) for x in a.split('-')) for a in sys.argv[1:]]
    n = 0
    for l in io.open('scratchpad/chat-restante.jsonl', encoding='utf-8'):
        v = json.loads(l)
        r = v['riga']
        if not any(a <= r <= b for a, b in zone):
            continue
        n += 1
        print('--- %d occ%d [%s]' % (r, v['occorrenza'], v['tipo']))
        print('JP  %s' % v['jp_grezzo'])
        print('EN  %s' % v['en_grezzo'])
    print('=== %d voci' % n)
    return 0

sys.exit(main())
