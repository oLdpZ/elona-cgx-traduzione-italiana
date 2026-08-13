import glob, io, json, difflib

voci = [json.loads(l) for l in io.open('lavoro/_buff.jsonl', encoding='utf-8') if l.strip()]

diz = []
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.split('\\')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            diz.append((nome, d['riga'], d['jp'], d['it']))

out = io.open('lavoro/_buff_simili.txt', 'w', encoding='utf-8')
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
print('scritto lavoro/_buff_simili.txt')
