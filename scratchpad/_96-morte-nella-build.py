# -*- coding: utf-8 -*-
"""96a - Le firme contate come lavoro che nella build **non esistono piu'**.

Una toppa puo' **riscrivere** la riga che contiene una `lang()`. E' quel che fa
la toppa del materiale con `item_func.hsp:1399`, che nel sorgente e'

    locvar_itemowner_s += mtname(0, …) + lang("細工の", "work ")

e nella build diventa

    locvar_itemname_s6 += " di manifattura in " + mtname(0, …)

cioe' il materiale **spostato in coda**, come vuole l'italiano. Quella `lang()`
nella build non c'e' piu'.

⚠️ Ma il conto delle «non ancora tradotte» la conta ancora, perche' si misura
sul **sorgente pinnato**, dove la riga c'e' eccome. Il risultato e' un numero
che non scendera' mai a zero e, peggio, una voce che un lotto futuro tradurra'
in buona fede: una resa scritta per una riga che il giocatore non incontrera'
mai, e nessuna guardia che lo dica.

E' la stessa famiglia delle righe spente — il `;`, il `/* … */`, il ramo
`if ( jp )` — con una differenza che conta: qui a spegnere la riga **siamo stati
noi**, con una toppa nostra, in una sessione precedente.

⚠️⚠️ **Due errori miei, nel primo e nel secondo giro di questa rete, e vale la
pena tenerli scritti perche' sono la stessa svista da due lati:**

1. il primo giro guardava **anche le voci gia' rese**. Su una voce tradotta
   l'inglese sparisce dalla build **per costruzione** — ce lo mette l'italiano
   al posto suo — e il referto diceva «sparite: 21.302», cioe' tutto il lavoro
   fatto dal progetto;
2. il secondo giro leggeva `dizionario/*.jsonl`, che contiene **solo** le voci
   gia' rese: quelle da fare non ci sono mai state. Referto: «sparite: 0», con
   `item_func.hsp:1399` che invece c'era.

La forma giusta e' la terza: si **estrae dal sorgente pinnato** (come fa
`verifica --dizionario`), si tolgono le rese e le rinviate, e quel che resta si
cerca nella build.

⚠️ Il referto NON e' un elenco di difetti. Una voce qui dentro va guardata e
decisa: quasi sempre si **rinvia** con `rinviata_a: "nessuna fase: risolta da
toppa"`, come `action.hsp` «The ». Se invece la toppa e' stata scritta male, la
voce viva e' il sintomo.

Uso:  python scratchpad/_96-morte-nella-build.py
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import estrai

SORGENTE = Path('C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx')
BUILD = Path('C:/Games/Elona/_traduzione/build/2.05-custom-gx')

rinviate = {json.loads(l)['firma']
            for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()}

rese = set()
for percorso in sorted(Path('dizionario').glob('*.jsonl')):
    for riga in io.open(percorso, encoding='utf-8'):
        if riga.strip():
            v = json.loads(riga)
            if (v.get('it') or '').strip():
                rese.add(v['firma'])

trovate = []
saltati = []
for hsp in sorted(SORGENTE.glob('*.hsp')):
    build_hsp = BUILD / hsp.name
    if not build_hsp.exists():
        saltati.append(hsp.name)
        continue
    testo = build_hsp.read_bytes().decode('cp932', 'replace')
    for v in estrai.estrai_da_file(hsp):
        if v['firma'] in rese or v['firma'] in rinviate:
            continue
        # il termine di paragone e' la forma grezza: per una dinamica il
        # letterale nudo non basta a ritrovarla
        ago = v.get('en_grezzo') or v.get('en') or ''
        if not ago.strip():
            continue
        if ago not in testo:
            trovate.append(v)

if saltati:
    print('sorgenti senza corrispondente nella build: %s' % saltati)
print('FIRME DA FARE CHE NELLA BUILD NON CI SONO PIU\': %d' % len(trovate))
per_file = {}
for v in trovate:
    per_file.setdefault(v['file'], []).append(v)
for f in sorted(per_file):
    voci = per_file[f]
    print('  %-24s %d' % (f, len(voci)))
    for v in voci[:10]:
        print('     :%-7s %-18s %r' % (v['riga'], (v.get('jp') or '')[:18], v.get('en')))
    if len(voci) > 10:
        print('     ... e altre %d' % (len(voci) - 10))
