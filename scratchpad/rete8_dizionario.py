# -*- coding: utf-8 -*-
"""La rete 8 applicata all'indietro: le rese GIA' ENTRATE che mettono una
preposizione semplice davanti a un nome che porta gia' l'articolo.

⚠️ La rete 8 e' nata nel lotto 009 (35a) e da allora ferma i lotti nuovi, ma
nessuno l'ha mai passata su quello che c'era prima. `name()` e
`cdatan(CDATAN_NAME, x)` restituiscono la **stessa** stringa — la toppa di
`init.hsp:1717` toglie il `"the "` e l'articolo lo porta il nome della creatura
(`db_creature.hsp`) — quindi «su » + `cdatan(...)` stampa «su il putit».

Referto, non guardia: la lettura di ogni riga e' obbligatoria, perche' un nome
proprio («Sinaha») regge la preposizione nuda e i nomi fra `<>` pure.

⚠️ **«con» non c'e', ed e' voluto**: non si fonde in italiano moderno («con il
putit» e' corretto, «col» e' facoltativo). La prima versione lo includeva e
faceva cinque falsi positivi su quattordici.

Atteso al 2026-08-14, dopo `correzione-rete8.py`: **3**, tutti dichiarati falsi
positivi —
  - `proc.hsp:5055` «Hai tirato **su** » + `itemname`: verbo sintagmatico, non
    una preposizione che regge il nome;
  - `proc.hsp:11893` e `:11898`: li' `valn = skillname(i)` (riga 11891) e i nomi
    di abilita' non portano articolo, quindi «il potenziale di Forza» e' giusto.
Un quarto vuol dire che qualcuno ha scritto un genitivo davanti a un nome.
"""
import glob
import io
import json
import re

FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')

quante = 0
for percorso in sorted(glob.glob('dizionario/*.jsonl')):
    nome = percorso.replace('\\', '/').split('/')[-1]
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        it = d.get('it') or ''
        if d.get('tipo') != 'dinamica':
            continue
        for preposizione, funzione in FONDONO.findall(it):
            quante += 1
            print(f'{nome}:{d["riga"]}  «{preposizione} » + {funzione}')
            print(f'    {it[:150]}')
print(f'--- {quante} rese con una preposizione che si fonde')
