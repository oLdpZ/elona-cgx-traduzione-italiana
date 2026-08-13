# -*- coding: utf-8 -*-
"""Correzione: `_sex2` deve portare dentro il proprio dimostrativo.

`text.hsp:110` rende 「男」/「女」 con «ragazzo»/«ragazza», nomi nudi. I suoi
**unici due siti di chiamata** (proc.hsp:3290 e :3450) sono la stessa frase, e
in italiano ci vuole un dimostrativo che concorda: «quel ragazzo» / «quella
ragazza». Un determinante non si puo' mettere nella frase, perche' varrebbe per
un genere solo — e' la stessa regola per cui la preposizione sta nel valore e
non nella frase.

Misurato prima di toccare: le due voci sono uniche in dizionario (firme diverse
da 「男」/「女」 = `Male`/`Female` di `text.hsp:109`), e nessun'altra resa del file
contiene «ragazz».
"""
import io, json

NUOVE = {
    ('boy', 'ragazzo'): 'quel ragazzo',
    ('girl', 'ragazza'): 'quella ragazza',
}

voci = [json.loads(l) for l in io.open('dizionario/text.hsp.jsonl', encoding='utf-8') if l.strip()]
scelte = []
for v in voci:
    k = (v.get('en'), v.get('it'))
    if v['riga'] == 110 and k in NUOVE:
        v['it'] = NUOVE[k]
        scelte.append(v)

if len(scelte) != 2:
    raise SystemExit(f'attese 2 voci a text.hsp:110, trovate {len(scelte)}')

with io.open('lavoro/correzione-sex2.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in scelte:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
for v in scelte:
    print(f"{v['riga']}  en={v['en']!r}  ->  it={v['it']!r}")
print('scritto lavoro/correzione-sex2.jsonl')
