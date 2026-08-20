# -*- coding: utf-8 -*-
"""Stampa le voci di `scratchpad/chat-restante.jsonl` in un intervallo di righe,
con il tipo, il grezzo giapponese e quello inglese.

    python scratchpad/chat-lotto-dump.py 22616 22961
"""
import io
import json
import sys


def main() -> int:
    da, a = int(sys.argv[1]), int(sys.argv[2])
    n = 0
    for l in io.open('scratchpad/chat-restante.jsonl', encoding='utf-8'):
        v = json.loads(l)
        r = v['riga']
        if not (da <= r <= a):
            continue
        n += 1
        print('--- %d occ%d [%s]' % (r, v['occorrenza'], v['tipo']))
        print('EN  %s' % v['en_grezzo'])
    print('=== %d voci' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
