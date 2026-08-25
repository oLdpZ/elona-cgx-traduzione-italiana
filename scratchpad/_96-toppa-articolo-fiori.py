# -*- coding: utf-8 -*-
"""96a - La toppa che da' a ogni fiore selvatico il suo articolo.

⚠️ IL PROBLEMA. `item_func.hsp:1442`-`:1480` sceglie **il nome** del fiore su
`INV_ITEM_PARAM2` — tredici possibilita' — ma l'articolo lo prende una volta
sola da `ioriginalnamearticolo(ITEM_ID_WILD_FLOWER)`, cioe' dal genere che il
dizionario dichiara per «fiore selvatico»: **maschile**. Sei fiori su tredici
sono femminili e uno vuole l'elisione, quindi senza rimedio si legge «un rosa»,
«un margherita», «un ortensia».

E' la stessa asimmetria che `contratto-nomi.md` §1-ter descrive per il nome non
identificato — «l'articolo e il plurale sono di un ALTRO sostantivo» — ma
arrivata da un'altra strada: li' sono due nomi dello stesso oggetto, qui sono
tredici nomi che dividono un `ITEM_ID`.

⭐ LA FORMA DEL RIMEDIO ERA GIA' NEL FILE. `item_func.hsp:1967`-`:1974` fa
esattamente questo per i **pesci**: dopo il ripiego sugli array generali,
sovrascrive `locvar_itemname_s8` / `s9` con `fishdatanarticolo()`, indicizzato
sul sottonome. La toppa infila lo stesso gesto per i fiori, **prima** di quel
blocco.

⚠️ L'ANCORA E' STRUTTURALE, APPOSTA. La riga cercata e' l'`if` dei pesci, che
non contiene nessuna `lang()`: nessun lotto potra' mai tradurla, quindi la toppa
non si disinnesca da sola. E' la lezione della stessa sessione — la toppa del
«(marcio)» era ancorata a `lang("(防腐処理)", " (Antiseptic)")`, il primo lotto
della 96a l'ha tradotta, e la toppa ha smesso di agganciare in silenzio.

⚠️ GLI ARTICOLI NON SONO SCRITTI A MANO. Li calcola `strumenti/articolo.py` dal
**genere**, che e' il dato che il dizionario porta; la scelta fra «un/uno/una/
un'» e' una regola meccanica sulla parola che segue, e chiederla a chi traduce
vorrebbe dire chiedergli di applicarla a mano tredici volte. La tabella dei
generi sta in `scratchpad/_96-rese-coda.py`, accanto ai nomi: **si cambiano
insieme**.

⚠️ E il fiore puo' portarsi dietro il materiale — «una rosa di manifattura in
mithril» — ma quello finisce in `locvar_itemname_s6`, che si appende a `:1899`,
cioe' **dopo** il nome. La testa del sintagma resta il fiore, quindi l'articolo
scelto qui e' quello giusto anche allora.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti.articolo import articoli

# la stessa tabella di `_96-rese-coda.py`: nome e genere, per PARAM2
FIORI = {
    0: ('fiore selvatico', 'm'),
    1: ('narciso', 'm'),
    2: ('margherita', 'f'),
    3: ('tarassaco', 'm'),
    4: ('tulipano', 'm'),
    5: ('rosa', 'f'),
    6: ('ortensia', 'f'),
    7: ('giglio', 'm'),
    8: ('girasole', 'm'),
    9: ('calendula', 'f'),
    10: ('cosmea', 'f'),
    11: ('crisantemo', 'm'),
    12: ('primula', 'f'),   # ⚠️ e' il ramo `>= 12`, non solo il 12
}

ANCORA = ('\t\t\tif ( inv(INV_ITEM_ID, itemname_itemid) == ITEM_ID_FISH'
          ' | inv(INV_ITEM_ID, itemname_itemid) == ITEM_ID_FISH_JUNK ) {')

BUILD = Path('C:/Games/Elona/_traduzione/build/2.05-custom-gx/item_func.hsp')

# --- si raggruppano i fiori per coppia di articoli, cosi' il blocco resta corto
per_coppia = {}
for p, (nome, genere) in FIORI.items():
    per_coppia.setdefault(articoli(genere, nome), []).append(p)

I = '\t\t\t'
blocco = [f'{I}if ( inv(INV_ITEM_ID, itemname_itemid) == ITEM_ID_WILD_FLOWER ) {{']
for (indet, det), params in sorted(per_coppia.items(), key=lambda x: min(x[1])):
    prove = []
    for p in sorted(params):
        confronto = '>=' if p == 12 else '=='
        prove.append(f'inv(INV_ITEM_PARAM2, itemname_itemid) {confronto} {p}')
    commento = ', '.join(FIORI[p][0] for p in sorted(params))
    blocco.append(f'{I}\tif ( {" | ".join(prove)} ) {{\t// {commento}')
    blocco.append(f'{I}\t\tlocvar_itemname_s8 = "{indet}"')
    blocco.append(f'{I}\t\tlocvar_itemname_s9 = "{det}"')
    blocco.append(f'{I}\t}}')
blocco.append(f'{I}}}')

# --- l'ancora esiste, ed e' unica, nella build gia' tradotta ----------------
testo = BUILD.read_bytes().decode('cp932').split('\n')
quante = sum(1 for l in testo if l.rstrip('\r') == ANCORA)
if quante != 1:
    raise SystemExit(f"l'ancora compare {quante} volte, ne serve una sola")

MOTIVO = (
    "L'articolo dei tredici fiori selvatici (`item_func.hsp`). Il **nome** lo "
    "sceglie `INV_ITEM_PARAM2` fra tredici, ma l'articolo viene una volta sola "
    "da `ioriginalnamearticolo(ITEM_ID_WILD_FLOWER)`, cioe' dal genere di "
    "«fiore selvatico»: maschile. Sei fiori su tredici sono femminili e "
    "«ortensia» vuole l'elisione, quindi senza toppa si legge «un rosa», «un "
    "margherita», «un ortensia». "
    "⭐ La forma del rimedio era gia' nel file: `:1967`-`:1974` fa lo stesso per "
    "i **pesci** con `fishdatanarticolo()`, e questa toppa infila lo stesso "
    "gesto per i fiori subito prima. "
    "⚠️ L'ancora e' l'`if` dei pesci, che non contiene nessuna `lang()`: e' "
    "**strutturale apposta**, perche' nella stessa sessione la toppa del "
    "«(marcio)» — ancorata a una `lang()` traducibile — ha smesso di agganciare "
    "in silenzio appena quella riga e' entrata in un lotto. "
    "⚠️ Gli articoli li calcola `strumenti/articolo.py` dal genere; la tabella "
    "dei tredici nomi con il loro genere sta in `scratchpad/_96-rese-coda.py` e "
    "in `scratchpad/_96-toppa-articolo-fiori.py`, e le due si cambiano insieme. "
    "Scritta nella 96a."
)

righe = [l for l in io.open('toppe.jsonl', encoding='utf-8').read().splitlines()
         if l.strip()]
if any(json.loads(l).get('cerca') == [ANCORA] for l in righe):
    raise SystemExit('toppa gia\' presente: niente da fare')

righe.append(json.dumps({
    'file': 'item_func.hsp',
    'cerca': [ANCORA],
    'sostituisci': blocco + [ANCORA],
    'motivo': MOTIVO,
}, ensure_ascii=False))

with io.open('toppe.jsonl', 'wb') as f:
    f.write(('\n'.join(righe) + '\n').encode('utf-8'))

print('toppa scritta, %d righe di blocco:' % len(blocco))
for l in blocco:
    print('   ' + l.replace('\t', '    '))
