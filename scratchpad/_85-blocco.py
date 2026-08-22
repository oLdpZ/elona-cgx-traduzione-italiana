# -*- coding: utf-8 -*-
"""Il confine vero di un blocco `if ( _switch_val == ... )` e il suo perimetro.

    python scratchpad/_85-blocco.py <riga di partenza> [...]
"""
import io, json, re, sys, collections

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
EST = 'scratchpad/_84-chat-tutte.jsonl'
VIA_STRINGA = re.compile('"(?:[^"' + chr(92) + chr(92) + ']|' + chr(92) + chr(92) + '.)*"')

_testo = io.open(SORG, encoding='cp932', errors='replace').read()
righe = _testo.split('\n')

# ⚠️ 87a: i commenti /* ... */ MULTIRIGA vanno tolti PRIMA di contare le
# graffe. In chat.hsp tre ne contengono una spaiata (`:169`, `:10752` dentro
# il blocco di ARASIEL, `:19629`): bastano a far correre il confine fino a
# fine file. Le righe restano al loro posto, svuotate.
_nudo = re.sub(r'/\*.*?\*/',
               lambda m: re.sub(r'[^\n]', ' ', m.group(0)), _testo, flags=re.S)
righe_nude = _nudo.split('\n')


def pulisci(n):
    """La riga n (1-based) senza stringhe, commenti di blocco e di riga."""
    l = VIA_STRINGA.sub('""', righe_nude[n - 1])
    l = re.sub(r'//.*', '', l)
    l = re.sub(r';.*', '', l)
    return l


voci = [json.loads(l) for l in io.open(EST, encoding='utf-8') if l.strip()]
rese = set()
for l in io.open('dizionario/chat.hsp.jsonl', encoding='utf-8'):
    if l.strip():
        v = json.loads(l)
        if v.get('it', '').strip():
            rese.add(v['firma'])
per_firma = collections.defaultdict(list)
for v in voci:
    per_firma[v['firma']].append(v['riga'])

for arg in sys.argv[1:]:
    start = int(arg)
    d = 0
    began = False
    fine = None
    for n in range(start, len(righe) + 1):
        c = pulisci(n)
        d += c.count('{') - c.count('}')
        if not began and '{' in c:
            began = True
        if began and d <= 0:
            fine = n
            break
    dentro = lambda r: start <= r <= fine
    firme = {f for f, rr in per_firma.items() if any(dentro(r) for r in rr)}
    da_fare = firme - rese
    fuori = [f for f in da_fare if any(not dentro(r) for r in per_firma[f])]
    print('%d-%d   %s' % (start, fine, righe[start - 1].strip()[:70]))
    print('   firme dentro: %d   da fare: %d   con occorrenze FUORI: %d'
          % (len(firme), len(da_fare), len(fuori)))
    for f in sorted(fuori, key=lambda f: min(per_firma[f])):
        print('      %s  %s' % (f[:8], sorted(set(per_firma[f]))))
