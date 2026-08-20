# -*- coding: utf-8 -*-
"""Mappa `chatval` -> la voce di menu che lo sceglie, con la resa italiana.

Serve a tagliare i lotti di `*chat_default` per TEMA invece che per numero:
ogni blocco `if ( chatval == N )` e' la risposta alla voce di menu che fa
`chatList N, lang(...)`, e quella voce e' gia' tradotta dalla 73a.

    python scratchpad/chatval-mappa.py
"""
import io
import json
import re
import sys
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')
DIZ = Path('dizionario/chat.hsp.jsonl')

LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
CL = re.compile(r'chat[Ll]ist\s+(\d+)\s*,\s*(.*)$')


def main() -> int:
    righe = io.open(SORGENTE, encoding='cp932', errors='replace').read().split('\n')
    reso = {}
    for l in io.open(DIZ, encoding='utf-8'):
        v = json.loads(l)
        reso.setdefault(v['riga'], v.get('it', ''))

    mappa = {}
    for n, l in enumerate(righe, 1):
        c = CL.search(l)
        if not c:
            continue
        val = int(c.group(1))
        if val == 0:
            continue
        g = LANG.search(c.group(2))
        en = g.group(2) if g else c.group(2).strip()[:60]
        mappa.setdefault(val, []).append((n, en, reso.get(n, '')))

    da_fare = json.loads(io.open('scratchpad/chatval-da-fare.json', encoding='utf-8').read())
    for val, quante in da_fare:
        voci = mappa.get(val)
        if not voci:
            print('%6d  %4d rese   ??? nessun chatList lo sceglie' % (val, quante))
            continue
        n, en, it = voci[0]
        marchio = '' if it else '  [MENU NON TRADOTTO]'
        print('%6d  %4d rese   %-50s | %s%s' % (val, quante, en[:50], it[:34], marchio))
    return 0


if __name__ == '__main__':
    sys.exit(main())
