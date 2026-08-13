# -*- coding: utf-8 -*-
"""Il repertorio gia' reso di una creatura: la sua riga di nome piu' le
battute che le stanno intorno nel file."""
import io, json, sys

NOMI = sys.argv[1:]

voci = [json.loads(l) for l in io.open('dizionario/db_creature.hsp.jsonl', encoding='utf-8') if l.strip()]
voci.sort(key=lambda v: v['riga'])

for nome in NOMI:
    ancore = [v for v in voci if nome in (v.get('it') or '') or nome in (v.get('en') or '')]
    if not ancore:
        print(f'### {nome}: non trovato')
        continue
    for a in ancore:
        r = a['riga']
        vicine = [v for v in voci if r - 60 <= v['riga'] <= r + 260]
        if len(vicine) < 3:
            continue
        print(f'### {nome}  (ancora a riga {r})')
        for v in vicine:
            print(f"  {v['riga']}  jp={v['jp']}\n        it={v.get('it')}")
        print()
        break
