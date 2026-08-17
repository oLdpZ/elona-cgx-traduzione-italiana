# -*- coding: utf-8 -*-
"""Le due questioni della nascita: le parentesi del nome e «figlio di X».

1. `main.hsp:6325` avvolge il nome del figlio in 「《」/「》」, che in inglese sono
   `{` e `}`. `module.hsp:264` ha gia' reso gli stessi due caratteri giapponesi
   con `<` e `>`: sono lo stesso segno o due segni diversi? Si guarda il SITO.
2. `main.hsp:6324` compone «son of X» con `cdatan`, e la rete 8 boccia una
   preposizione davanti a un nome. Come l'ha risolta il progetto altrove?
"""
import glob
import io
import json
import re
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')

print('=== 1. le parentesi: dove il sorgente usa 《 》 e come sono rese ===')
per_riga = {}
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    for i, riga in enumerate(righe, start=1):
        if 'lang("《"' in riga or 'lang("》"' in riga:
            per_riga[(percorso.name, i)] = riga.strip()[:150]
for (nome, riga), testo in sorted(per_riga.items()):
    print(f'  {nome}:{riga}  {testo}')

print()
print('=== e le rese gia\' date per 《 e 》 ===')
for percorso in sorted(glob.glob('dizionario/*.jsonl')):
    nome = percorso.replace('\\', '/').split('/')[-1]
    for linea in io.open(percorso, encoding='utf-8'):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if d.get('it') and d['jp'] in ('《', '》'):
            print(f"  {nome}:{d['riga']}  jp={d['jp']}  en={d['en']!r}  it={d['it']!r}")

print()
print('=== module.hsp:264, il sito ===')
righe = (SORGENTE / 'module.hsp').read_bytes().decode('cp932', 'replace').split('\n')
for i in range(258, 272):
    print(f'  {i + 1}: {righe[i][:140]}')

print()
print('=== 2. «X di Y» con cdatan o name: come si e\' gia\' scritto ===')
_FONDE = re.compile(r'\b(a|di|da|in|su|del|della)\s*"\s*\+\s*(name|cdatan|itemname)\b')
_PRIMA = re.compile(r'(cdatan|name)\s*\([^)]*\)\s*\+\s*"')
quante = 0
for percorso in sorted(glob.glob('dizionario/*.jsonl')):
    nome = percorso.replace('\\', '/').split('/')[-1]
    for linea in io.open(percorso, encoding='utf-8'):
        if not linea.strip():
            continue
        d = json.loads(linea)
        it = d.get('it') or ''
        if not it or '+' not in it:
            continue
        if 'of ' in (d.get('en_grezzo') or '') and _PRIMA.search(it):
            quante += 1
            if quante <= 10:
                print(f"  {nome}:{d['riga']}")
                print(f"      en: {(d.get('en_grezzo') or '')[:80]}")
                print(f"      it: {it[:80]}")
print(f'  ... voci «of» risolte mettendo il nome PRIMA: {quante}')

print()
print('=== e sncnv, che map.hsp usa davanti a cdatan ===')
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    for i, riga in enumerate(righe, start=1):
        if '#deffunc sncnv' in riga or '#defcfunc sncnv' in riga:
            for j in range(i - 1, min(len(righe), i + 22)):
                print(f'  {percorso.name}:{j + 1}: {righe[j][:130]}')
