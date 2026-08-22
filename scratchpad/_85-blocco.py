# -*- coding: utf-8 -*-
"""Il confine vero di un blocco `if ( _switch_val == ... )` e il suo perimetro.

    python scratchpad/_85-blocco.py <riga di partenza> [...]
"""
import io, json, re, sys, collections

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
EST = 'scratchpad/_84-chat-tutte.jsonl'
VIA_STRINGA = re.compile('"(?:[^"' + chr(92) + chr(92) + ']|' + chr(92) + chr(92) + '.)*"')

righe = io.open(SORG, encoding='cp932', errors='replace').read().split('\n')


def pulisci(l):
    l = VIA_STRINGA.sub('""', l)
    l = re.sub(r'/\*.*?\*/', '', l)
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
        c = pulisci(righe[n - 1])
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
