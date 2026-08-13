# -*- coding: utf-8 -*-
"""Toglie da rinviate.jsonl le tre code della scena e le rende.

Erano rinviate perche' la testa (`proc.hsp:3372`) stava in un blocco `if ( en )`
fuori da lang(). Adesso la testa e' tradotta da una toppa, quindi le code si
possono rendere: la frase intera e' italiana.

💡 Il dizionario e' indicizzato per contenuto, quindi le tre voci coprono OTTO
siti: `lang("」", "\\"")` sta a :3376, :3402, :3537 e :3621; l'offerta di
spiccioli a :3383 e :3629; il portafogli vuoto a :3389 e :3635.
"""
import io, json

RESE = {
    'Here, take this.\\"': '! Ecco, prendi questi spiccioli.\\"',
    'Take this money, it\'s all I have!\\"': '! Questo è tutto quello che ho nel portafogli.\\"',
    # ⚠️ La chiusura delle virgolette e' identica in inglese e in italiano, e non
    #    e' una resa dimenticata: e' un segno di interpunzione. Dichiarata in
    #    invariati.md.
    '\\"': '\\"',
}

voci = [json.loads(l) for l in io.open('lavoro/_proc_tutte.jsonl', encoding='utf-8') if l.strip()]
# 8 occorrenze, 3 firme: il dizionario e' indicizzato per firma, quindi una voce
# per firma copre tutti i siti che la condividono.
per_firma = {}
for v in voci:
    if v['en'] in RESE:
        per_firma.setdefault(v['firma'], []).append(v)
scelte = [gruppo[0] for gruppo in per_firma.values()]
if len(scelte) != 3:
    raise SystemExit(f'attese 3 firme, trovate {len(scelte)}: '
                     f'{[(v["firma"][:8], v["en"]) for v in scelte]}')
for firma, gruppo in per_firma.items():
    righe_siti = sorted(v['riga'] for v in gruppo)
    print(f'  {firma[:8]}  {gruppo[0]["en"]!r}  -> siti {righe_siti}')

for v in scelte:
    v['it'] = RESE[v['en']]

with io.open('lavoro/fase4-proc-004.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in scelte:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')

# e via da rinviate.jsonl
firme = {v['firma'] for v in scelte}
righe = [json.loads(l) for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
restano = [r for r in righe if r['firma'] not in firme]
tolte = len(righe) - len(restano)
with io.open('rinviate.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in restano:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

for v in scelte:
    print(f"{v['riga']:6d}  {v['en']!r} -> {v['it']!r}")
print(f'{tolte} rinviate tolte, ne restano {len(restano)}')
