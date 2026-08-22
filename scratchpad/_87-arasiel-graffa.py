# -*- coding: utf-8 -*-
"""Dove il contatore di graffe perde una chiusura dentro il blocco di ARASIEL.

Stampa ogni riga di :10729-:10880 con la profondita' e il delta, e segnala
le righe con un numero DISPARI di virgolette (la trappola classica: una
stringa che il regex non chiude e si porta dietro il resto della riga).
"""
import io
import re

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
DA, A = 10729, 10880

righe = io.open(SORG, encoding='cp932', errors='replace').read().split('\n')
VIA_STRINGA = re.compile(r'"(?:[^"\\]|\\.)*"')

prof = [0] * (len(righe) + 2)
delta = [0] * (len(righe) + 2)
d = 0
for i, r in enumerate(righe, 1):
    r2 = VIA_STRINGA.sub('""', r)
    r2 = re.sub(r'/\*.*?\*/', '', r2)
    r2 = re.sub(r'(;|//).*$', '', r2)
    prof[i] = d
    delta[i] = r2.count('{') - r2.count('}')
    d += delta[i]

print('--- righe sospette (virgolette dispari, o graffa dentro una stringa) ---')
for n in range(DA, A + 1):
    r = righe[n - 1]
    nudo = VIA_STRINGA.sub('""', r)
    virg = nudo.count('"')
    dentro = ('{' in r or '}' in r) and ('{' not in nudo and '}' not in nudo)
    if virg or dentro:
        print('%6d  virgolette residue=%d  %s' % (n, virg, r[:150]))

print()
print('--- il blocco riga per riga (solo quelle con graffe) ---')
for n in range(DA, A + 1):
    if delta[n]:
        print('%6d  prof=%2d  d=%+d  %s' % (n, prof[n], delta[n], righe[n - 1][:120]))
