# -*- coding: utf-8 -*-
"""Dump di una zona di righe dell'estrazione, con jp/en grezzi e contesto."""
import io, json, sys

sorgente = sys.argv[1]          # es. lavoro/_proc.jsonl
da = int(sys.argv[2])
a = int(sys.argv[3])
uscita = sys.argv[4]

voci = [json.loads(l) for l in io.open(sorgente, encoding='utf-8') if l.strip()]
zona = [v for v in voci if da <= v['riga'] <= a]
zona.sort(key=lambda v: (v['riga'], v['occorrenza']))

with io.open(uscita, 'w', encoding='utf-8') as f:
    for v in zona:
        f.write(f"--- riga {v['riga']}.{v['occorrenza']}  [{v['tipo']}]\n")
        f.write(f"jp: {v['jp_grezzo']}\n")
        f.write(f"en: {v['en_grezzo']}\n")
print(f'{len(zona)} voci fra {da} e {a} (su {len(voci)} da fare) -> {uscita}')
tot = len(voci)
print(f'prima riga da fare: {min(v["riga"] for v in voci)}, ultima: {max(v["riga"] for v in voci)}')
