# -*- coding: utf-8 -*-
"""Il MARGINE delle rese di un lotto contro il tetto secco di 69, degradate.

Lo zero della rete dice «nessuna sfora»; questo dice **di quanto**, che e' il
numero che serve per sapere se la formula reggera' anche sulle categorie dopo.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-108/_margine.py \
        lavoro/fase5-db_item-002.jsonl

⚠️ Il file si passa come argomento e non sta scritto qui dentro: la prima
versione lo aveva fisso, e al secondo lotto ho dovuto riscriverlo con `sed` —
cioe' un attimo prima di misurare il lotto sbagliato credendo di misurare quello
giusto.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 69


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    percorso = sys.argv[1]
    voci = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    misurate = sorted(((len(degrada(v['it'])), len(v['en']), v['riga'], v['it'])
                       for v in voci), reverse=True)
    for lunghezza, en, riga, it in misurate[:5]:
        print(f'  :{riga:<7} {lunghezza:>3} car. degradati (inglese {en:>3})   {it}')
    print()
    piu_lunga = misurate[0][0]
    print(f'{len(voci)} rese in {percorso}: la piu\' lunga misura {piu_lunga} '
          f'caratteri degradati su {TETTO} di budget, margine {TETTO - piu_lunga}')
    piu_lunghe = [m for m in misurate if m[0] > m[1]]
    print(f'rese piu\' lunghe del loro inglese: {len(piu_lunghe)} su {len(voci)}')
    if piu_lunga > TETTO:
        sys.exit(f'⚠️ {piu_lunga} caratteri: il tetto e\' sfondato')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
