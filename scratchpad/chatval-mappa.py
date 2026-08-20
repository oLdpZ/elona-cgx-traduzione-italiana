# -*- coding: utf-8 -*-
"""Mappa `chatval` -> la voce di menu che lo sceglie, con la resa italiana.

Serve a tagliare i lotti di `*chat_default` per TEMA invece che per numero:
ogni blocco `if ( chatval == N )` e' la risposta a una voce che fa
`chatList N, lang(...)`.

⚠️⚠️ **I numeri di `chatval` sono PER MENU, non globali.** Lo stesso numero e'
riusato da menu diversi: `32` e' «chain» nel menu dei materiali del fabbro e il
portafoglio smarrito dentro `*chat_default`. Una mappa che prende la **prima**
`chatList` del file con quel numero risponde con la voce sbagliata, e la prima
stesura di questo strumento lo faceva. Quindi le voci si cercano solo dentro il
menu che porta davvero a quei blocchi: quello costruito nel ramo `evochat == 0`
di `*chat_default`.

    python scratchpad/chatval-mappa.py
"""
import io
import json
import re
import sys
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')
DIZ = Path('dizionario/chat.hsp.jsonl')

# il menu di *chat_default: il ramo `if ( evochat == 0 )` a :19320, fino allo
# smistamento `if ( chatval == ... )` che comincia a :19881
MENU_DA, MENU_A = 19320, 19880

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
        if not (MENU_DA <= n <= MENU_A):
            continue
        c = CL.search(l)
        if not c:
            continue
        val = int(c.group(1))
        g = LANG.search(c.group(2))
        en = g.group(2) if g else c.group(2).strip()[:60]
        mappa.setdefault(val, []).append((n, en, reso.get(n, '')))

    da_fare = json.loads(io.open('scratchpad/chatval-da-fare.json', encoding='utf-8').read())
    orfani = 0
    for val, quante in da_fare:
        voci = mappa.get(val)
        if not voci:
            orfani += 1
            print('%6d  %4d rese   ??? nessuna voce nel menu di *chat_default' % (val, quante))
            continue
        n, en, it = voci[0]
        marchio = '' if it else '  [VOCE NON TRADOTTA]'
        print('%6d  %4d rese   %6d  %-44s | %s%s' % (val, quante, n, en[:44], it[:32], marchio))
    print()
    print('%d blocchi, %d senza voce nel menu' % (len(da_fare), orfani))
    return 0


if __name__ == '__main__':
    sys.exit(main())
