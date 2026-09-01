# -*- coding: utf-8 -*-
"""122a - L'inglese di monte ricopiato su un ALTRO oggetto, in `db_item.hsp`.

`_103-inglese-ripetuto.py` e `_104-inglese-slittato.py` fanno gia' questa
domanda, ma su `db_card.hsp`: e' scritto nella prima riga di tutt'e due
(`FILE = 'db_card.hsp'`). Su `db_item.hsp` la stessa domanda la fa **solo la
rete 13 del lotto**, che guarda dentro il lotto e basta.

Il lotto 061 l'ha trovato per fortuna: `:56267`, la `description(0)` inglese
del dipinto dell'eruzione, e' la copia **letterale** di quella della zampa di
coniglio (`:56333`), che nel sorgente e' l'oggetto immediatamente successivo.
Il giapponese e' quello giusto, e la `description(3)` inglese della stessa voce
pure — monte ha sbagliato **una riga sola**. Le due righe sono cadute nello
stesso lotto, e per questo la rete 13 e' arrivata; in due lotti diversi non
avrebbe detto niente.

⚠️⚠️ **Perche' conta.** Su una riga cosi', una resa presa dall'inglese descrive
**l'oggetto sbagliato**, e non c'e' cancello che se ne accorga: la riga e'
pulita in ogni senso misurabile — coda al suo posto, larghezza dentro, accenti
veri, glossario rispettato. E' la forma di 神の間 della 121a: il guasto esiste
solo per il giocatore che ha in mano l'oggetto.

⚠️ **Le gemelle vere non sono un difetto**, e vanno tolte dal conto: quando due
righe hanno **lo stesso giapponese E lo stesso inglese** sono lo stesso testo
per due oggetti, ed e' il moltiplicatore che `_previsione.py` gia' misura. Il
difetto e' *lo stesso inglese per due giapponesi **diversi***.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_122-inglese-doppio-item.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_122-inglese-doppio-item.py --prova

⚠️ Referto da leggere, non un cancello: il sorgente di monte non si tocca, e il
valore atteso non e' zero. Quel che conta e' **la lista**, e per ogni gruppo la
domanda «la resa italiana di queste righe viene dal giapponese o dall'inglese?».

⭐ `--prova` e' la prova al contrario, e **cerca** invece di ipotizzare: prende
la coppia nota (`:56267`/`:56333`) e verifica che la rete la stampi; poi prende
il gruppo di gemelle vere piu' numeroso del file e verifica che la rete lo
**taccia**. Una rete che accende su tutto non sta trovando niente.
"""
import collections
import io
import json
import sys
from pathlib import Path

from strumenti.estrai import estrai_da_testo
from strumenti.percorsi import SORGENTE_HSP

FILE = 'db_item.hsp'
DIZIONARIO = Path(__file__).resolve().parent.parent / 'dizionario' / (FILE + '.jsonl')

# sotto questa lunghezza due inglesi uguali sono formule, non copie
CORTA = 60


def voci_del_sorgente():
    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    return estrai_da_testo(FILE, testo)


def rese_del_dizionario():
    """riga -> resa italiana, per le righe gia' tradotte."""
    per_firma = {}
    if not DIZIONARIO.exists():
        return per_firma
    with io.open(DIZIONARIO, encoding='utf-8') as f:
        for linea in f:
            d = json.loads(linea)
            if d.get('it'):
                per_firma[d['firma']] = d['it']
    return per_firma


def gruppi(voci):
    """inglese -> le voci che lo portano, solo dove i giapponesi sono >1."""
    per_en = collections.defaultdict(list)
    for v in voci:
        en = (v.get('en') or '').strip()
        if len(en) < CORTA:
            continue
        per_en[en].append(v)

    fuori = []
    for en, mie in per_en.items():
        jp = {v.get('jp') or '' for v in mie}
        if len(jp) > 1:
            fuori.append((en, sorted(mie, key=lambda v: v['riga'])))
    return sorted(fuori, key=lambda c: c[1][0]['riga'])


def stampa(fuori, rese):
    print('=== LO STESSO INGLESE PER GIAPPONESI DIVERSI: %d gruppi' % len(fuori))
    print()
    for en, mie in fuori:
        righe = ', '.join(':%d' % v['riga'] for v in mie)
        print('%s   (%d righe, %d giapponesi distinti)'
              % (righe, len(mie), len({v.get('jp') or '' for v in mie})))
        print('    en   %s' % en[:150])
        for v in mie:
            resa = rese.get(v['firma'])
            stato = 'RESA' if resa else 'da fare'
            print('    :%-8d %-8s jp  %s' % (v['riga'], stato, (v.get('jp') or '')[:90]))
            if resa:
                print('    %-9s          it  %s' % ('', resa[:90]))
        print()


def prova_al_contrario(voci, fuori):
    print('=== LA PROVA AL CONTRARIO, in due direzioni')
    accese = {v['riga'] for _, mie in fuori for v in mie}

    # 1) deve ACCENDERSI sulla coppia nota del lotto 061
    nota = (56267, 56333)
    if set(nota) <= accese:
        print('  ⭐ si accende sulla coppia nota :56267/:56333 (il dipinto e il coniglio)')
    else:
        print('  ⚠️ NON si accende su :56267/:56333, e li\' il difetto c\'e\': la rete e\' rotta')
        return 1

    # 2) deve TACERE sul gruppo di gemelle vere piu' numeroso
    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v['riga'])
    peggiore = max(per_firma.values(), key=len)
    if len(peggiore) < 2:
        print('  ⓘ nessuna gemella vera nel file: la seconda direzione non si puo\' provare')
        return 0
    if set(peggiore) & accese:
        print('  ⚠️ si accende sulle gemelle VERE %s, che sono lo stesso testo per due '
              'oggetti: la rete conta difetti che non ci sono' % peggiore)
        return 1
    print('  ⭐ tace sul gruppo di gemelle vere piu\' numeroso (%d righe, %s): stesso '
          'giapponese E stesso inglese, non e\' una copia' % (len(peggiore), peggiore))
    return 0


def main():
    voci = voci_del_sorgente()
    rese = rese_del_dizionario()
    fuori = gruppi(voci)

    if '--prova' in sys.argv:
        return prova_al_contrario(voci, fuori)

    stampa(fuori, rese)

    con_resa = sum(1 for _, mie in fuori for v in mie if rese.get(v['firma']))
    totale = sum(len(mie) for _, mie in fuori)
    print('voci di %s: %d   gruppi col solo inglese in comune: %d   righe toccate: %d'
          % (FILE, len(voci), len(fuori), totale))
    print('di quelle righe, gia\' rese: %d' % con_resa)
    print()
    print('ⓘ referto, non cancello: il valore atteso non e\' zero. Per ogni gruppo la')
    print('  domanda e\' se la resa italiana venga dal giapponese (e allora e\' salva)')
    print('  o dall\'inglese (e allora descrive l\'oggetto sbagliato).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
