# -*- coding: utf-8 -*-
"""Quante voci gia' tradotte stanno dentro un commento di blocco `/* ... */`?

La domanda nasce nella 37a con `proc.hsp:11796`: se una voce dentro un blocco
spento e' arrivata nel dizionario, e' lavoro speso su testo che il giocatore non
legge, e la rete 6 non l'avrebbe fermata.
"""
import glob
import importlib.util
import io
import json
import os

spec = importlib.util.spec_from_file_location('cb', os.path.join('scratchpad', 'commenti-blocco.py'))
cb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cb)

totale = 0
for percorso in sorted(glob.glob(os.path.join('dizionario', '*.jsonl'))):
    nome_hsp = os.path.basename(percorso)[:-len('.jsonl')]
    sorgente = os.path.join(cb.SORGENTE, nome_hsp)
    if not os.path.exists(sorgente):
        print(f'{nome_hsp}: sorgente assente, saltato')
        continue
    spente = cb.righe_in_commento(sorgente)
    colpite = []
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('riga') in spente:
            colpite.append(d['riga'])
    marca = ' ⚠️' if colpite else ''
    print(f'{nome_hsp}: {len(spente)} righe spente, {len(colpite)} voci tradotte dentro'
          f'{marca} {sorted(set(colpite))[:12]}')
    totale += len(colpite)
print('TOTALE voci tradotte dentro un blocco spento:', totale)
