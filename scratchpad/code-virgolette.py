# -*- coding: utf-8 -*-
"""Le code della scena: la chiusura di virgolette e le due offerte di denaro."""
import io, re

P = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'
righe = io.open(P, encoding='cp932').read().split('\n')
AGHI = ('Here, take this', "it's all I have", 'You are awesome')
CHIUSURA = re.compile(r'lang\("\u300d",')
for i, l in enumerate(righe):
    if any(a in l for a in AGHI) or CHIUSURA.search(l):
        print(f'{i+1:6d} | ' + l.strip()[:160])
