# -*- coding: utf-8 -*-
"""Il confine del blocco di ARASIEL (:10729): blocco enorme o graffa non chiusa?

Stampa la profondita' di graffe intorno alla riga di partenza, la prima riga
in cui la profondita' torna a <= 1, e la mappa delle righe che aprono una
graffa senza chiuderla dentro il presunto blocco.
"""
import io
import re

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
DA = 10729

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

print('righe nel file: %d   profondita a fine file: %d' % (len(righe), d))
print()
print('--- intorno a :%d ---' % DA)
for n in range(DA - 4, DA + 6):
    print('%6d  prof=%2d  d=%+d  %s' % (n, prof[n], delta[n], righe[n - 1][:100]))

print()
print('--- prima riga con prof <= 1 dopo :%d ---' % DA)
for j in range(DA + 1, len(righe) + 1):
    if prof[j] <= 1:
        print('%6d  prof=%2d  %s' % (j, prof[j], righe[j - 1][:100]))
        break
else:
    print('nessuna: il blocco arriva a fine file')

print()
print('--- le righe che aprono senza chiudere, dentro il blocco ---')
aperte = []
for n in range(DA, len(righe) + 1):
    if delta[n] > 0:
        aperte.append(n)
    if prof[n] <= 1 and n > DA:
        break
print('righe con delta>0: %d (prime 30)' % len(aperte))
for n in aperte[:30]:
    print('%6d  prof=%2d  d=%+d  %s' % (n, prof[n], delta[n], righe[n - 1][:100]))

print()
print('--- i minimi di profondita nel blocco (dove quasi si chiude) ---')
mini = {}
for n in range(DA, min(len(righe), 26800) + 1):
    mini.setdefault(prof[n], n)
for p in sorted(mini)[:6]:
    n = mini[p]
    print('prof=%2d  prima a :%d  %s' % (p, n, righe[n - 1][:100]))
