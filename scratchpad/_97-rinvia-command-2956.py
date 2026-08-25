# -*- coding: utf-8 -*-
"""97a - L'undicesima riga morta di `command.hsp:2954`, che era stata TRADOTTA.

`command.hsp:2956` e' `noteadd "@BL 最深攻略階層 : " + gdata(GDATA_DEEPEST_LEVEL)
+ lang("階相当", " level")`: sta dentro lo stesso `if ( jp )` di `:2954`-`:3021`
delle altre dieci, quindi in italiano non viene valutata mai.

⚠️ **Le altre dieci sono in `rinviate.jsonl` dalla 45a. Questa no: e' stata
resa** (« liv.») nella 68a, commit `ecc3f33`. Il referto
`lang-nel-ramo-jp.py` era tornato a `21 | 0` nella 57a proprio togliendo una
resa morta, ed e' risalito a `21 | 1` nella 68a — dove nessuno l'ha guardato,
perche' quel referto **non e' fra le quindici verifiche d'apertura**: si lancia
solo quando si apre un file o una zona nuova. Ventinove sessioni di silenzio.

Il rimedio e' quello della 57a: la voce esce dal dizionario ed entra fra le
rinviate, con lo stesso motivo delle sue dieci sorelle. Il conto di «fatto»
cala di uno, ed e' giusto cosi': quella resa non l'ha mai letta nessuno.
"""
import io
import json

FIRMA = 'aa641c0418272ffb3a18fc8e6a045ffa367b1d4d'
RIGA, EN = 2956, ' level'

MOTIVO = None
esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
for l in esistenti:
    v = json.loads(l)
    if v.get('file') == 'command.hsp' and '2954' in (v.get('motivo') or ''):
        MOTIVO = v['motivo']
        RINVIATA_A = v['rinviata_a']
        break
if MOTIVO is None:
    raise SystemExit('non trovo il motivo delle dieci sorelle: non tocco niente')

if any(json.loads(l)['firma'] == FIRMA for l in esistenti):
    print('gia rinviata, niente da fare')
    raise SystemExit(0)

# 1. la voce esce dal dizionario
percorso = 'dizionario/command.hsp.jsonl'
tenute, tolte = [], []
for l in io.open(percorso, encoding='utf-8'):
    if not l.strip():
        continue
    v = json.loads(l)
    if v['firma'] == FIRMA:
        tolte.append(v)
    else:
        tenute.append(l)
if len(tolte) != 1:
    raise SystemExit(f'attese 1 voce da togliere, trovate {len(tolte)}: non tocco niente')
if tolte[0]['riga'] != RIGA or tolte[0]['en'] != EN:
    raise SystemExit(f'la voce non e\' quella attesa: {tolte[0]!r}')
print(f'tolta dal dizionario: :{RIGA} en={EN!r} it={tolte[0]["it"]!r}')

# 2. ed entra fra le rinviate, con il motivo delle sorelle
nuova = {
    'firma': FIRMA,
    'file': 'command.hsp',
    'en': EN,
    'rinviata_a': RINVIATA_A,
    'motivo': MOTIVO,
}

# ⚠️ si compone e si codifica prima di toccare i file (la 39a)
dati_dizionario = ''.join(tenute).encode('utf-8')
dati_rinviate = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')

with io.open(percorso, 'wb') as f:
    f.write(dati_dizionario)
with io.open('rinviate.jsonl', 'ab') as f:
    f.write(dati_rinviate)

print(f'dizionario: {len(tenute)} voci restano')
print(f'rinviate.jsonl: {len(esistenti) + 1} righe')
