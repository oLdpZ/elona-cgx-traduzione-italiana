import glob, io, json, sys

# argv[1]: l'estrazione da guardare, es. lavoro/_command.jsonl
ESTRAZIONE = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_buff.jsonl'

reso = {}
for p in glob.glob('dizionario/*.jsonl'):
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it'):
            reso.setdefault(d['jp'], []).append((p.split('\\')[-1], d['riga'], d['it']))

voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]
n = 0
for v in voci:
    if v['jp'] in reso:
        n += 1
        print(f"riga {v['riga']}  jp={v['jp']!r}")
        for f, r, it in reso[v['jp']]:
            print(f"    -> {f}:{r}  {it!r}")
print(f'{n} su {len(voci)} gia rese altrove')
