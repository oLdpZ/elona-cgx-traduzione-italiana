# -*- coding: utf-8 -*-
"""Quante voci gia' tradotte stanno dentro un commento di blocco `/* ... */`?

La domanda nasce nella 37a con `proc.hsp:11796`: se una voce dentro un blocco
spento e' arrivata nel dizionario, e' lavoro speso su testo che il giocatore non
legge, e la rete 6 non l'avrebbe fermata.

⚠️⚠️ **E per otto sessioni il conto era gonfio, perche' guardava la riga e non
la firma** (45a). `estrai --da-tradurre` ancora una voce alla **prima**
occorrenza, che puo' stare nel blocco spento mentre le altre sono vive: allora
la resa non e' sprecata affatto, e' l'ancora a essere nel posto sbagliato.
Il caso che l'ha fatto vedere e' `command.hsp:17285`, dove il mod ha spento
l'`ORIGINAL` e ha riscritto lo stesso menu dieci righe sotto.

✅ Adesso le due cose si contano separate: **sprecate** (tutte le occorrenze
della firma sono spente) e **vive altrove** (l'ancora e' spenta ma il testo si
legge). Atteso al 15/08: **4 sprecate** e **3 vive altrove**, dove il conto
vecchio diceva 7 sprecate. E' la stessa correzione che ha rifatto la rete 6.
"""
import collections
import glob
import importlib.util
import io
import json
import os
from pathlib import Path

from strumenti import estrai

spec = importlib.util.spec_from_file_location('cb', os.path.join('scratchpad', 'commenti-blocco.py'))
cb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cb)

sprecate_tot = 0
vive_tot = 0
for percorso in sorted(glob.glob(os.path.join('dizionario', '*.jsonl'))):
    nome_hsp = os.path.basename(percorso)[:-len('.jsonl')]
    sorgente = os.path.join(cb.SORGENTE, nome_hsp)
    if not os.path.exists(sorgente):
        print(f'{nome_hsp}: sorgente assente, saltato')
        continue
    spente = cb.righe_in_commento(sorgente)

    # tutte le occorrenze di ogni firma, per distinguere l'ancora dal testo vivo
    righe_per_firma = collections.defaultdict(list)
    for v in estrai.estrai_da_file(Path(sorgente)):
        righe_per_firma[v['firma']].append(v['riga'])

    sprecate, vive = [], []
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if not d.get('it') or d.get('riga') not in spente:
            continue
        righe = righe_per_firma.get(d.get('firma')) or [d['riga']]
        if all(r in spente for r in righe):
            sprecate.append(d['riga'])
        else:
            vive.append((d['riga'], [r for r in righe if r not in spente]))

    marca = ' ⚠️' if sprecate else ''
    print(f'{nome_hsp}: {len(spente)} righe spente, {len(sprecate)} sprecate'
          f'{marca} {sorted(set(sprecate))[:12]}')
    for riga, altrove in vive:
        print(f'      💡 :{riga} e\' spenta ma la firma vive a {altrove}: non e\' sprecata')
    sprecate_tot += len(sprecate)
    vive_tot += len(vive)

print('TOTALE voci tradotte dentro un blocco spento e SPRECATE:', sprecate_tot)
print('TOTALE con l\'ancora spenta ma il testo vivo altrove   :', vive_tot)
