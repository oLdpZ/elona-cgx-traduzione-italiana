# -*- coding: utf-8 -*-
"""125a - Stampa per intero le voci di dizionario di un file, per riga.

    PYTHONIOENCODING=utf-8 python scratchpad/_125-mostra.py chat.hsp 11290 11325 ...
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)


def main():
    nome = sys.argv[1]
    righe = set(int(a) for a in sys.argv[2:])
    percorso = os.path.join(RADICE, 'dizionario', nome + '.jsonl')
    for r in io.open(percorso, encoding='utf-8'):
        v = json.loads(r)
        if righe and v['riga'] not in righe:
            continue
        print('=== %s:%d' % (v['file'], v['riga']))
        print('  tipo %s' % v.get('tipo'))
        print('  jp   %s' % v.get('jp_grezzo', v.get('jp')))
        print('  en   %s' % v.get('en_grezzo', v.get('en')))
        print('  it   %s' % v.get('it'))
        print('')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
