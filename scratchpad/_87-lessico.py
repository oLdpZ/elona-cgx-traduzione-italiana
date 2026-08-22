# -*- coding: utf-8 -*-
"""Il lessico di un lotto, cercato nel DIZIONARIO invece che deciso.

    python scratchpad/_87-lessico.py "api nut" "cooler box" ...
    python scratchpad/_87-lessico.py --jp 旅糧 発言力

Per ogni termine stampa le voci gia' rese che lo contengono, le piu' CORTE
per prime: una voce corta e' un nome di oggetto, di abilita' o di menu —
cioe' la parola che il giocatore legge nell'interfaccia — mentre una lunga
e' una battuta, dove la stessa cosa puo' essere detta in mille modi.
"""
import glob
import io
import json
import sys

campo = 'en'
argomenti = sys.argv[1:]
if argomenti and argomenti[0] in ('--en', '--jp', '--it'):
    campo = argomenti[0][2:]
    argomenti = argomenti[1:]

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1][:-len('.jsonl')]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if (v.get('it') or '').strip():
            v['_file'] = nome
            voci.append(v)

PESO = {'db_item.hsp': 0, 'db_creature.hsp': 0, 'db_race.hsp': 0, 'text.hsp': 1,
        'command.hsp': 1, 'skill.hsp': 1, 'item.hsp': 1, 'god.hsp': 1}

for ago in argomenti:
    print('##### %s' % ago)
    trovate = [v for v in voci if ago.lower() in (v.get(campo) or '').lower()]
    trovate.sort(key=lambda v: (len(v.get(campo) or ''), PESO.get(v['_file'], 2)))
    if not trovate:
        print('   (niente in dizionario)')
    for v in trovate[:5]:
        print('   %s:%s' % (v['_file'], v['riga']))
        print('      JP %s' % (v.get('jp') or '')[:90])
        print('      EN %s' % (v.get('en') or '')[:130])
        print('      IT %s' % (v.get('it') or '')[:130])
    print()
