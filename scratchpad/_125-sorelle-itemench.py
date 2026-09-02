# -*- coding: utf-8 -*-
"""125a - Per ognuna delle 26 firme di `custom_itemenchantment.hsp`, cerca il
giapponese piu' somigliante in TUTTO il dizionario e stampa come e' gia' reso.

    PYTHONIOENCODING=utf-8 python scratchpad/_125-sorelle-itemench.py

E' la regola della 113a (settimo posto dove guardare: il giapponese di cio' che
stai per scrivere puo' essere gia' reso altrove), applicata a un lotto intero
come nella 124a. Qui serve piu' che altrove, perche' il file e' testo di
Custom-GX dove l'inglese e il giapponese divergono: se una riga sorella esiste
gia' resa, la resa nuova non la deve contraddire.

Stampa, per ogni voce da fare:
  = identica       stesso giapponese, byte per byte
  ~ somigliante    rapporto di somiglianza >= 0.75
"""
import difflib
import glob
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
LOTTO = os.path.join(QUI, '_124-itemench.jsonl')
SOGLIA = 0.75


def main():
    da_fare = [json.loads(r) for r in io.open(LOTTO, encoding='utf-8')]

    rese = []
    for percorso in sorted(glob.glob(os.path.join(RADICE, 'dizionario', '*.jsonl'))):
        for riga in io.open(percorso, encoding='utf-8'):
            v = json.loads(riga)
            if v.get('it') and v.get('jp'):
                rese.append(v)
    print('%d voci gia\' rese nel dizionario, %d da fare\n' % (len(rese), len(da_fare)))

    identiche = somiglianti = sole = 0
    for v in da_fare:
        jp = v['jp']
        print('--- %s:%d   %s' % (v['file'], v['riga'], jp[:60]))
        print('    en  %s' % v['en'][:100])

        esatte = [r for r in rese if r['jp'] == jp]
        if esatte:
            identiche += 1
            for r in esatte[:3]:
                print('    =   %s:%d  %s' % (r['file'], r['riga'], r['it'][:110]))
            print('')
            continue

        vicine = []
        for r in rese:
            if abs(len(r['jp']) - len(jp)) > max(6, len(jp) // 3):
                continue
            q = difflib.SequenceMatcher(None, jp, r['jp']).ratio()
            if q >= SOGLIA:
                vicine.append((q, r))
        vicine.sort(key=lambda x: -x[0])
        if vicine:
            somiglianti += 1
            for q, r in vicine[:3]:
                print('    ~%.2f %s:%d  %s' % (q, r['file'], r['riga'], r['jp'][:50]))
                print('          -> %s' % r['it'][:110])
        else:
            sole += 1
            print('    (nessuna sorella)')
        print('')

    print('identiche %d, somiglianti %d, sole %d' % (identiche, somiglianti, sole))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
