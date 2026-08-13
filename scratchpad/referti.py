import glob, io, json, re

part = re.compile(r'\b(?:ti sei|te ne sei|sei|sarai|ti eri|eri|il prossimo|la prossima)\s+(\w+(?:ato|ata|uto|uta|ito|ita|tto|tta|so|sa))\b')
elis = re.compile(r"\b([Ll]|[Uu]n[ao]?|[Dd]ell|[Aa]ll|[Nn]ell|[Ss]ull|[Qq]uell)'([A-Za-z])")
voc = set('aeiouAEIOUhH')

n_part = n_elis = 0
for f in glob.glob('dizionario/*.jsonl'):
    for l in io.open(f, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        it = d.get('it') or ''
        for m in part.finditer(it):
            print('PARTICIPIO', f, d['riga'], m.group(0))
            n_part += 1
        for m in elis.finditer(it):
            if m.group(2) not in voc:
                print('ELISIONE', f, d['riga'], m.group(0))
                n_elis += 1
print(f'participi: {n_part}')
print(f'elisioni: {n_elis}')
