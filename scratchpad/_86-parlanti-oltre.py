# -*- coding: utf-8 -*-
"""I parlanti OLTRE :8694 presi sul CODICE: la mappa che mancava (86a).

Per ogni blocco `if ( _switch_val == ... )` di primo livello dentro la zona:
il confine vero (graffa che lo chiude), le firme non tradotte con almeno
un'occorrenza dentro, e quante di quelle hanno occorrenze anche FUORI.
"""
import io, json, re, collections

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
EST = 'scratchpad/_84-chat-tutte.jsonl'
DA = 8630

righe = io.open(SORG, encoding='cp932', errors='replace').read().split('\n')
A = len(righe)

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

VIA_STRINGA = re.compile(r'"(?:[^"\\]|\\.)*"')

# profondita' di graffe riga per riga
prof = [0] * (len(righe) + 2)
d = 0
for i, r in enumerate(righe, 1):
    r2 = VIA_STRINGA.sub('""', r)
    r2 = re.sub(r'/\*.*?\*/', '', r2)
    r2 = re.sub(r'(;|//).*$', '', r2)
    prof[i] = d
    d += r2.count('{') - r2.count('}')

blocchi = []
i = DA
while i <= A:
    r = righe[i - 1]
    m = re.search(r'_switch_val\s*==\s*(\S+)', r)
    if m and prof[i] == 1:
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
for a, b, nome in blocchi:
    dentro = {f for f, rr in per_firma.items() if any(a <= x <= b for x in rr)}
    dafare = dentro - rese
    coperte |= dafare
    fuori = sum(1 for f in dafare if any(not (a <= x <= b) for x in per_firma[f]))
    if not dafare:
        continue
    tot += len(dafare)
    print('%6d-%-6d %-46s %4d da fare  %s' % (
        a, b, nome[:46], len(dafare),
        ('ZONA CHIUSA' if fuori == 0 else '%d fuori' % fuori)))
print()
print('totale da fare dentro i blocchi: %d' % tot)

# quel che nella zona non sta in nessun blocco di primo livello
zona = {f for f, rr in per_firma.items() if any(DA <= x <= A for x in rr)} - rese
print('firme da fare nella zona intera : %d' % len(zona))
print('fuori da ogni blocco            : %d' % len(zona - coperte))
for f in sorted(zona - coperte, key=lambda f: min(per_firma[f])):
    print('   riga %6d' % min(x for x in per_firma[f] if DA <= x <= A))
