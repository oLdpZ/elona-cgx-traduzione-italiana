# -*- coding: utf-8 -*-
"""107a - Lo scheletro delle chiavi di un lotto di descrizioni di `db_item.hsp`.

Stampa le chiavi `(riga, en)` gia' pronte da incollare nel `RESE` di un lotto,
col `repr()` dell'inglese: cosi' la chiave non si trascrive a mano e non puo'
divergere di un apostrofo dal file di lavoro. E' `_103-chiavi-card.py` con i
filtri di `_107-dossier-item.py`, **gli stessi**, perche' un lotto e il suo
dossier che selezionano in modo diverso sono un guasto che non si vede.

⚠️⚠️ **I LOTTI DI QUESTO FILE NON SONO INTERVALLI DI RIGHE, E NON POSSONO
ESSERLO SE SI VUOLE LAVORARE PER FAMIGLIA.** Le descrizioni di una categoria
sono sparse per novantamila righe: i cinque cibi del primo dossier stanno a
42.785, 44.659, 44.731, 44.803 e 52.111. Il modello di lotto del progetto
seleziona la zona con `DA <= riga <= A`, e su un intervallo cosi' prenderebbe
dentro mezzo file. Per questo qui si emette anche un `RIGHE = {...}`: la zona
si dichiara per **insieme di righe**, e il contratto del lotto — «ogni voce
della zona e' resa» — resta identico e altrettanto verificabile.

    python scratchpad/_107-chiavi-item.py --categoria FILTER_ITEM_FOOD --indice 3
    python scratchpad/_107-chiavi-item.py --da 42400 --a 43000
"""
import argparse
import collections
import io
import json
import re
import sys

from strumenti.categorie import categorie
from strumenti.estrai import spezza_righe
from strumenti.percorsi import SORGENTE_HSP

LAVORO = 'lavoro/_107-daitem.jsonl'
FILE = 'db_item.hsp'
_INDICE = re.compile(r'^\s*description\((\d+)\)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--categoria')
    ap.add_argument('--indice', type=int)
    ap.add_argument('--da', type=int)
    ap.add_argument('--a', type=int)
    ap.add_argument('--solo-righe', action='store_true',
                    help='solo il RIGHE = {...}, senza lo scheletro')
    a = ap.parse_args()

    righe_sorgente, _, _ = spezza_righe(
        (SORGENTE_HSP / FILE).read_text(encoding='cp932'))
    mappa = categorie()

    tutte = [json.loads(l) for l in io.open(LAVORO, encoding='utf-8') if l.strip()]
    zona = []
    for voce in tutte:
        if a.da is not None and voce['riga'] < a.da:
            continue
        if a.a is not None and voce['riga'] > a.a:
            continue
        if a.categoria and mappa.get(voce.get('oggetto')) != a.categoria:
            continue
        if a.indice is not None:
            trovato = _INDICE.match(righe_sorgente[voce['riga'] - 1])
            if trovato is None or int(trovato.group(1)) != a.indice:
                continue
        zona.append(voce)

    if not zona:
        print('# nessuna voce con questi filtri')
        return

    numeri = sorted(v['riga'] for v in zona)
    print('# la zona non e\' un intervallo: si dichiara per insieme di righe')
    print('RIGHE = {')
    for inizio in range(0, len(numeri), 10):
        print('    ' + ', '.join(str(n) for n in numeri[inizio:inizio + 10]) + ',')
    print('}')
    print(f'# {len(numeri)} righe, da {numeri[0]} a {numeri[-1]}')
    if a.solo_righe:
        return
    print()

    ambigue = {k for k, n in collections.Counter(
        (v['riga'], v['en']) for v in zona).items() if n > 1}
    for voce in sorted(zona, key=lambda v: v['riga']):
        corta = (voce['riga'], voce['en'])
        chiave = (voce['riga'], voce['en'], voce['jp']) if corta in ambigue else corta
        print('    # ---------------------------------------------------------- :%d'
              % voce['riga'])
        print('    %r:' % (chiave,))
        print('        "",')
        print()
    print('# %d voci, %d ambigue' % (len(zona), len(ambigue)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
