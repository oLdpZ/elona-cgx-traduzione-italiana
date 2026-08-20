# -*- coding: utf-8 -*-
"""Per ogni voce del lotto dice CHE COSA la disegna: una voce di menu
(`chatList`, registro giapponese, tetto 58), la battuta del PNG (`buff`,
53 caratteri per riga) o `chatMore` (battuta + un solo bottone).

    python scratchpad/chat-lotto-classe.py 22616 22961
"""
import io
import json
import sys
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')


def classe(riga: str) -> str:
    s = riga.strip()
    if s.startswith('chatList') or s.startswith('chatlist'):
        return 'MENU'
    if s.startswith('chatMore'):
        return 'PIU'
    if s.startswith('buff'):
        return 'BUFF'
    if s.startswith('txt'):
        return 'TXT'
    return s.split(' ')[0][:12]


def main() -> int:
    da, a = int(sys.argv[1]), int(sys.argv[2])
    src = io.open(SORGENTE, encoding='cp932', errors='replace').read().split('\n')
    for l in io.open('scratchpad/chat-restante.jsonl', encoding='utf-8'):
        v = json.loads(l)
        r = v['riga']
        if not (da <= r <= a):
            continue
        c = classe(src[r - 1])
        jp = v['jp'] if c == 'MENU' else ''
        print('%-5s %6d  %-46s %s' % (c, r, v['en'][:46], jp))
    return 0


if __name__ == '__main__':
    sys.exit(main())
