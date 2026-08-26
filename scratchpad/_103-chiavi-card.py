# -*- coding: utf-8 -*-
"""103a - Lo scheletro delle chiavi di una zona di `db_card.hsp`.

Stampa le chiavi `(riga, en)` di una zona gia' pronte da incollare nel `RESE`
di un lotto, con il `repr()` dell'inglese: cosi' la chiave non si trascrive a
mano e non puo' divergere di un apostrofo dal file di lavoro.

    python scratchpad/_103-chiavi-card.py 3101 3600
"""
import collections
import io
import json
import sys

LAVORO = 'lavoro/_102-dacard.jsonl'


def main():
    da, a = int(sys.argv[1]), int(sys.argv[2])
    tutte = [json.loads(l) for l in io.open(LAVORO, encoding='utf-8') if l.strip()]
    zona = [v for v in tutte if da <= v['riga'] <= a]
    ambigue = {k for k, n in collections.Counter(
        (v['riga'], v['en']) for v in zona).items() if n > 1}
    for v in zona:
        corta = (v['riga'], v['en'])
        chiave = (v['riga'], v['en'], v['jp']) if corta in ambigue else corta
        print('    # ---------------------------------------------------------- :%d' % v['riga'])
        print('    %r:' % (chiave,))
        print('        "",')
        print()
    print('# %d voci fra la riga %d e la %d, %d ambigue' % (len(zona), da, a, len(ambigue)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
