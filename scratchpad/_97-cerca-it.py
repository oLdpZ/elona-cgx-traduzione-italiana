import glob, io, json, sys
# cerca nel dizionario per sottostringa in jp, en o it (case-insensitive su en/it)
termini = [t.lower() for t in sys.argv[1:]]
for f in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(f, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        jp, en, it = d.get('jp') or '', d.get('en') or '', d.get('it') or ''
        blob = (jp + '\n' + en + '\n' + it).lower()
        if any(t in blob for t in termini):
            print(f"{f.split(chr(92))[-1].split('/')[-1]}:{d['riga']}  en={en!r}\n      it={it!r}")
