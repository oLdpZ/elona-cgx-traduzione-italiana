import glob, io, json, difflib, sys

# argv[1]: l'estrazione da guardare, es. lavoro/_command.jsonl
ESTRAZIONE = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_buff.jsonl'
USCITA = ESTRAZIONE.replace('.jsonl', '_simili.txt')

voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]

diz = []
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.split('\\')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            diz.append((nome, d['riga'], d['jp'], d['it']))

out = io.open(USCITA, 'w', encoding='utf-8')
for v in voci:
    jp = v['jp']
    if not jp:
        continue
    cand = []
    for nome, riga, djp, dit in diz:
        r = difflib.SequenceMatcher(None, jp, djp).ratio()
        if r >= 0.55:
            cand.append((r, nome, riga, djp, dit))
    if not cand:
        continue
    cand.sort(reverse=True)
    out.write(f"--- riga {v['riga']}  jp={jp}\n    en={v['en']}\n")
    for r, nome, riga, djp, dit in cand[:3]:
        out.write(f"    {r:.2f} {nome}:{riga}  {djp}  ==  {dit}\n")
out.close()
print(f'scritto {USCITA}')
