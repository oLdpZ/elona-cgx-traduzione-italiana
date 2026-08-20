# -*- coding: utf-8 -*-
"""Conta le rese che restano in ogni blocco `if ( chatval == N )` di
`*chat_default`, e scrive `scratchpad/chatval-da-fare.json`.
"""
import bisect
import io
import json
import re
import sys
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')
DA, A = 18665, 24690
RESTANTE = Path('scratchpad/chat-restante.jsonl')

TOP = re.compile(r'^\tif \( (.*) \) \{$')
VAL = re.compile(r'chatval == (\d+)')


def main() -> int:
    righe = io.open(SORGENTE, encoding='cp932', errors='replace').read().split('\n')
    blocchi = []
    for i in range(DA - 1, A):
        m = TOP.match(righe[i])
        if m:
            blocchi.append((i + 1, m.group(1)))
    inizi = [b[0] for b in blocchi]

    conta = {}
    for l in io.open(RESTANTE, encoding='utf-8'):
        v = json.loads(l)
        r = v['riga']
        if not (DA <= r <= A):
            continue
        k = bisect.bisect_right(inizi, r) - 1
        if k < 0:
            continue
        conta[blocchi[k]] = conta.get(blocchi[k], 0) + 1

    fuori = []
    for (linea, cond), quante in sorted(conta.items()):
        m = VAL.search(cond)
        if m and cond.count('chatval') == 1:
            fuori.append((int(m.group(1)), quante))
    io.open('scratchpad/chatval-da-fare.json', 'w', encoding='utf-8').write(
        json.dumps(fuori, ensure_ascii=False))
    print('%d blocchi chatval semplici, %d rese' % (len(fuori), sum(q for _, q in fuori)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
