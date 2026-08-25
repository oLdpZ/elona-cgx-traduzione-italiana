# -*- coding: utf-8 -*-
"""96a - `item_func.hsp`: i tredici fiori selvatici, la chiave `EN` e le cornici.

19 rese fra `:1407` e `:1797`. Sono quel che resta della «coda» del file una
volta tolto il muro dei prefissi.

⭐⭐⭐ IL MURO DEI PREFISSI ERA GIA' MEZZO ABBATTUTO, E NON LO SAPEVAMO.
Questa sessione era partita convinta che tutte e 24 le firme fra `:1300` e
`:1458` fossero bloccate, perche' stanno in `itemname()` **prima** del nome
dell'oggetto e in italiano il complemento va dopo. Non e' cosi': la rete nuova
`scratchpad/_96-morte-nella-build.py` ha trovato che `:1399` e `:1404` **nella
build non esistono piu'**. Una toppa gia' scritta le trasforma in

    locvar_itemname_s6 += " di manifattura in " + mtname(0, …)

e `locvar_itemname_s6` si appende a `:1899`, cioe' **in coda al nome**. I mobili
e i fiori dicono gia' «una sedia di manifattura in mithril».

⚠️ Conseguenza per i fiori: il materiale non gli sta piu' davanti, quindi il
nome del fiore e' **la testa del sintagma** e si traduce normalmente. Restava un
problema solo, e non e' il lessico.

⭐⭐⭐ L'ARTICOLO E' DI UN ALTRO FIORE. Il nome che si legge lo sceglie
`INV_ITEM_PARAM2` fra tredici, ma l'articolo lo prende
`ioriginalnamearticolo(ITEM_ID_WILD_FLOWER)`, che e' **uno solo** e viene dal
genere dichiarato nel dizionario per «fiore selvatico»: maschile. Sei fiori su
tredici sono femminili, e uno vuole l'elisione:

    un narciso, un tarassaco, un tulipano, un giglio, un girasole, un crisantemo
    una margherita, una rosa, una calendula, una cosmea, una primula
    un'ortensia                                    <- e questo elide

Senza rimedio uscirebbero «un rosa» e «un ortensia». Il rimedio non e' una resa:
e' la toppa `_96-toppa-articolo-fiori.py`, che sceglie l'articolo su `PARAM2`
esattamente come `item_func.hsp` fa gia' per i **pesci** (`fishdatanarticolo`,
`:1967`-`:1974`) — la forma era gia' nel file. ⚠️ E gli articoli non sono
scritti a mano: li calcola `strumenti/articolo.py` dal genere, che e' il dato
che il dizionario porta.

⚠️ I NOMI SCELTI. Dove l'inglese e' il nome comune del fiore si traduce col nome
comune italiano; `margaret` e' **la margherita** (マーガレット, Leucanthemum) e
non un nome di persona, e `cosmos` e' la **cosmea**, non il cosmo. たんぽぽ e'
il **tarassaco** — «soffione» e' la testa sfiorita, cioe' un'altra fase della
stessa pianta. `野花` resta «fiore selvatico», che e' gia' il nome dell'oggetto
in `db_item.hsp:137631`: e' il caso in cui il fiore non e' nessuno dei dodici.

LE SEI CHE NON SONO TESTO:
  - `:1705`  `lang("JP", "EN")` — **la chiave di un blocco**, non una sigla di
    lingua: `instr()` la cerca dentro il file dell'oggetto personalizzato
    (`%txtName,EN`). Tradotta, il gioco non trova piu' il nome. La famiglia sta
    gia' in `invariati.md` sotto «Chiavi e nomi di file», e con lei `EN` di
    `help.hsp:228`;
  - `:1786`, `:1794`, `:1797` — le cornici attorno al **titolo casuale** di un
    libro prodotto in gioco. ⚠️ Le angolari e le graffe **non** sono la stessa
    cornice: `<` marca il titolo di qualita' «miracolo», `{` quello sotto. Le
    tiene separate upstream, e uniformarle cancellerebbe una distinzione voluta.

PERIMETRO: 24 firme fra `:1300` e `:1797`; 19 qui, 1 rinviata perche' risolta da
toppa (`:1399`), 4 rinviate perche' sono il muro dei prefissi vero
(`:1308`, `:1386`, `:1390`, `:1458`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io, json, sys

# il fiore, e il genere da cui `strumenti/articolo.py` ricava l'articolo.
# ⚠️ La toppa dell'articolo legge QUESTA tabella: si cambiano insieme.
FIORI = {
    1407: ('fiore selvatico', 'm'),
    1410: ('narciso', 'm'),
    1413: ('margherita', 'f'),
    1416: ('tarassaco', 'm'),
    1419: ('tulipano', 'm'),
    1422: ('rosa', 'f'),
    1425: ('ortensia', 'f'),
    1428: ('giglio', 'm'),
    1431: ('girasole', 'm'),
    1434: ('calendula', 'f'),
    1437: ('cosmea', 'f'),
    1440: ('crisantemo', 'm'),
    1443: ('primula', 'f'),
}

RESE = {(r, None): nome for r, (nome, _) in FIORI.items()}
RESE.update({
    (1705, 'EN'): 'EN',
    (1786, '<'): '<',
    (1786, '>'): '>',
    (1794, ' <'): ' <',
    (1797, ' {'): ' {',
    (1797, '}'): '}',
})

LOTTO = 'lavoro/96-item_func-coda.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]


def chiave(v):
    if v['riga'] in FIORI:
        return (v['riga'], None)
    trovate = [k for k in RESE if k[0] == v['riga'] and k[1] == v['en']]
    return trovate[0] if len(trovate) == 1 else None


mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
usate = {chiave(v) for v in voci if chiave(v)}
in_piu = [k for k in RESE if k not in usate]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
