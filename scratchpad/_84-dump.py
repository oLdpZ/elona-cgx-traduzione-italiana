# -*- coding: utf-8 -*-
"""Stampa righe del sorgente pinnato di chat.hsp (o di un altro file).

    python scratchpad/_84-dump.py da a [da a ...]
    python scratchpad/_84-dump.py --file main.hsp da a
"""
import io, sys

base = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
arg = sys.argv[1:]
nome = 'chat.hsp'
if arg and arg[0] == '--file':
    nome = arg[1]
    arg = arg[2:]
righe = io.open(base + '\\' + nome, encoding='cp932', errors='replace').read().split('\n')
for i in range(0, len(arg), 2):
    a, b = int(arg[i]), int(arg[i + 1])
    print('--- %s %d-%d' % (nome, a, b))
    for n in range(a, min(b, len(righe)) + 1):
        print('%5d %s' % (n, righe[n - 1].rstrip()))
    print()
