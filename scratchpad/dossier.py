# -*- coding: utf-8 -*-
"""Il dossier di un lotto: per ogni voce, il sorgente intorno e le rese gemelle.

    python scratchpad/dossier.py lavoro/_proc.jsonl proc.hsp 9201 10100 uscita.txt

Mette insieme le tre letture che ogni lotto rifà a mano:
  - la riga del sorgente e le due righe sopra/sotto, che dicono in che ramo sta
    la voce (`if ( en )`, un confronto, un commento) e chi e' `tc`;
  - le rese gia' decise per lo STESSO giapponese in qualunque file (la regola
    «cercare prima di scrivere»: nella 14a ha reso due volte su tre);
  - le rese gia' decise per lo stesso INGLESE, che pescano i casi in cui
    upstream ricicla una frase sotto giapponesi diversi.
"""
import collections
import glob
import io
import json
import sys

# ⚠️ Il SORGENTE, non la build: le toppe possono aggiungere righe (`text.hsp` ne
# ha una in piu'), e da li' in giu' i numeri di riga del dizionario non tornano.
# Vedi la 37a, «Chi incrocia numeri di riga e dizionario deve leggere il SORGENTE».
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

sorgente_jsonl, nome_hsp, da, a, uscita = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]

voci = [json.loads(l) for l in io.open(sorgente_jsonl, encoding='utf-8') if l.strip()]
zona = sorted((v for v in voci if da <= v['riga'] <= a), key=lambda v: (v['riga'], v['occorrenza']))

righe = io.open(f'{SORGENTE}\\{nome_hsp}', encoding='cp932').read().split('\n')

per_jp = collections.defaultdict(list)
per_en = collections.defaultdict(list)
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if not d.get('it'):
            continue
        if d.get('jp'):
            per_jp[d['jp']].append((nome, d['riga'], d['it']))
        if d.get('en'):
            per_en[d['en']].append((nome, d['riga'], d['it']))

with io.open(uscita, 'w', encoding='utf-8', newline='\n') as f:
    for v in zona:
        n = v['riga']
        f.write(f"{'=' * 78}\n=== riga {n}.{v['occorrenza']}  [{v['tipo']}]\n")
        f.write(f"jp: {v['jp_grezzo']}\n")
        f.write(f"en: {v['en_grezzo']}\n")
        f.write("--- sorgente\n")
        for i in range(max(0, n - 4), min(len(righe), n + 3)):
            marca = '>>' if i == n - 1 else '  '
            f.write(f"{marca}{i + 1}: {righe[i]}\n")
        gemelle_jp = [g for g in per_jp.get(v['jp'], ()) if v['jp']]
        if gemelle_jp:
            f.write("--- STESSO GIAPPONESE, gia' reso:\n")
            for nome, riga, it in gemelle_jp:
                f.write(f"    {nome}:{riga}  {it}\n")
        gemelle_en = [g for g in per_en.get(v['en'], ()) if v['en']]
        if gemelle_en:
            f.write("--- stesso inglese, gia' reso:\n")
            for nome, riga, it in gemelle_en:
                f.write(f"    {nome}:{riga}  {it}\n")

quante_jp = sum(1 for v in zona if per_jp.get(v['jp']))
quante_en = sum(1 for v in zona if per_en.get(v['en']))
print(f'{len(zona)} voci fra {da} e {a} -> {uscita}')
print(f'con lo stesso giapponese gia\' reso altrove: {quante_jp}')
print(f'con lo stesso inglese gia\' reso altrove:    {quante_en}')
