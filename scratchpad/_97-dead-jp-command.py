# -*- coding: utf-8 -*-
"""Quale delle 11 righe morte di command.hsp e' stata resa."""
import io, json, re, os, glob

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
APRE_JP = re.compile(r'^\s*if\s*\(\s*jp\s*\)\s*\{')
LANG = re.compile(r'\blang\s*\(')
STRINGA = '"(?:[^"' + chr(92)*2 + ']|' + chr(92)*2 + '.)*"'
LETTERALE = re.compile(STRINGA)

def righe_nel_ramo_jp(righe):
    dentro, prof = set(), None
    for n, riga in enumerate(righe, 1):
        if prof is None:
            if APRE_JP.match(riga):
                prof = 1
            continue
        dentro.add(n)
        f = re.sub(STRINGA, '', riga)
        prof += f.count('{') - f.count('}')
        if prof <= 0:
            dentro.discard(n)
            prof = None
    return dentro

rese = {}
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = os.path.basename(p).replace('.jsonl', '')
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if v.get('it'):
            rese.setdefault((nome, v['riga']), []).append(v)

righe = io.open(os.path.join(SORGENTE, 'command.hsp'), encoding='cp932', errors='replace').read().splitlines()
for n in sorted(righe_nel_ramo_jp(righe)):
    r = righe[n - 1]
    if LANG.search(r) and LETTERALE.search(r):
        marca = '   <<< GIA RESA' if ('command.hsp', n) in rese else ''
        print(f'{n:6d} {r.strip()[:100]}{marca}')
        for v in rese.get(('command.hsp', n), []):
            print(f'        en={v.get("en")!r}  it={v.get("it")!r}')
