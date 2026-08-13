import glob, io, json, sys

# cerca voci del dizionario il cui jp o en contiene uno dei termini
termini = sys.argv[1:]
for f in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(f, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        jp = d.get('jp') or ''
        en = d.get('en') or ''
        it = d.get('it') or ''
        for t in termini:
            if t in jp or t == en:
                print(f"{f.split(chr(92))[-1]}:{d['riga']}  jp={jp!r}  en={en!r}  it={it!r}")
                break
