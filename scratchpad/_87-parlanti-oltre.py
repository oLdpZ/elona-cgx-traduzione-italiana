# -*- coding: utf-8 -*-
"""I parlanti OLTRE :8694, col confine giusto (87a).

Come `_86-parlanti-oltre.py`, ma i commenti `/* ... */` MULTIRIGA vengono
tolti PRIMA di contare le graffe: dentro ce ne sono tre spaiate (`:169`,
`:10752` nel blocco di ARASIEL, `:19629`), e bastavano a far inghiottire ad
ARASIEL tutto il resto del file.

⚠️⚠️ **95a: toglie anche le RINVIATE, e prima non lo faceva.** Questa mappa e'
il documento su cui si sceglie il lotto della sessione, e per otto sessioni ha
dato **AJETALIO a 4 da fare** quando le sue quattro firme erano tutte in
`rinviate.jsonl` — quattro righe **commentate a monte** (`:13991`, `:14036`,
`:14038`), rinviate nell'87a con il motivo scritto. La ripresa della 94a ci ha
costruito sopra un piano («AJETALIO chiude il Seminario»), e il seminario era
gia' chiuso da otto sessioni. `_88-lotto.py` le toglieva da sempre: il taglio e
la mappa contavano due cose diverse, e a farsi credere era la mappa.
"""
import io
import json
import re
import collections

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
EST = 'scratchpad/_84-chat-tutte.jsonl'
DA = 8630

testo = io.open(SORG, encoding='cp932', errors='replace').read()

# i commenti di blocco spariscono, ma le righe restano al loro posto
def _svuota(m):
    return re.sub(r'[^\n]', ' ', m.group(0))


testo_nudo = re.sub(r'/\*.*?\*/', _svuota, testo, flags=re.S)
righe = testo.split('\n')
righe_nude = testo_nudo.split('\n')
A = len(righe)

voci = [json.loads(l) for l in io.open(EST, encoding='utf-8') if l.strip()]
rese = set()
for l in io.open('dizionario/chat.hsp.jsonl', encoding='utf-8'):
    if l.strip():
        v = json.loads(l)
        if v.get('it', '').strip():
            rese.add(v['firma'])

# Le rinviate hanno un motivo scritto e NON sono lavoro che aspetta: contarle
# fra le «da fare» fa scegliere lotti che non esistono. Vedi il docstring.
rinviate = {json.loads(l)['firma']
            for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()}
rese |= rinviate
print('rinviate tolte dal conto: %d (su tutto il progetto)' % len(rinviate))

per_firma = collections.defaultdict(list)
for v in voci:
    per_firma[v['firma']].append(v['riga'])

VIA_STRINGA = re.compile(r'"(?:[^"\\]|\\.)*"')

prof = [0] * (len(righe) + 2)
d = 0
for i, r in enumerate(righe_nude, 1):
    r2 = VIA_STRINGA.sub('""', r)
    r2 = re.sub(r'(;|//).*$', '', r2)
    prof[i] = d
    d += r2.count('{') - r2.count('}')
print('profondita a fine file: %d  (0 = le graffe tornano)' % d)
print()

blocchi = []
i = DA
while i <= A:
    r = righe_nude[i - 1]
    m = re.search(r'_switch_val\s*==\s*(\S+)', r)
    if m and prof[i] == 0:
        liv = prof[i]
        j = i + 1
        while j <= len(righe) and prof[j] > liv:
            j += 1
        blocchi.append((i, j - 1, m.group(1)))
        i = j
        continue
    i += 1

print('blocchi di primo livello: %d' % len(blocchi))
print()
tot = 0
coperte = set()
elenco = []
for a, b, nome in blocchi:
    dentro = {f for f, rr in per_firma.items() if any(a <= x <= b for x in rr)}
    dafare = dentro - rese
    coperte |= dafare
    fuori = sum(1 for f in dafare if any(not (a <= x <= b) for x in per_firma[f]))
    if not dafare:
        continue
    tot += len(dafare)
    elenco.append((len(dafare), a, b, nome, fuori))

for n, a, b, nome, fuori in sorted(elenco, reverse=True):
    print('%6d-%-6d %-46s %4d da fare  %s' % (
        a, b, nome[:46], n,
        ('ZONA CHIUSA' if fuori == 0 else '%d fuori' % fuori)))
print()
print('totale da fare dentro i blocchi: %d' % tot)

zona = {f for f, rr in per_firma.items() if any(DA <= x <= A for x in rr)} - rese
print('firme da fare nella zona intera : %d' % len(zona))
print('fuori da ogni blocco            : %d' % len(zona - coperte))
for f in sorted(zona - coperte, key=lambda f: min(per_firma[f])):
    print('   riga %6d' % min(x for x in per_firma[f] if DA <= x <= A))
