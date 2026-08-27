# -*- coding: utf-8 -*-
"""Le rese di un lotto contro TUTTO il dizionario, in due direzioni.

Generalizza `_coerenza004.py`, che aveva il lotto scritto dentro.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-109/_coerenza.py \
        lavoro/fase5-db_item-005.jsonl

La rete 13 del lotto guarda solo **dentro** il lotto. Queste due domande
guardano fuori, e sono quelle che nessuna rete del lotto puo' porsi:

  A) lo stesso GIAPPONESE reso in due modi diversi (dentro o fuori dal lotto);
  B) lo stesso INGLESE reso in due modi diversi.

⚠️⚠️ **Lo zero da solo non e' un risultato.** Accanto si stampa quanti gruppi
avessero davvero **piu' di una voce** da confrontare: un gruppo di una voce
sola non puo' divergere, e una rete che ne guarda solo di quelli dice zero
senza aver giudicato niente. E in fondo la prova al contrario **cerca** il caso
peggiore — il giapponese con piu' voci nel dizionario — e stampa dove si
accende, invece di un ✅.
"""
import collections
import glob
import io
import json
import os
import sys


def voci_dizionario():
    for percorso in sorted(glob.glob(os.path.join('dizionario', '*.jsonl'))):
        for riga in io.open(percorso, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            if v.get('it'):
                v['_file'] = os.path.basename(percorso)
                yield v


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    percorso = sys.argv[1]
    lotto = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    # ⚠️⚠️ La stringa VUOTA non e' un giapponese, e raggruppa tutto quello che
    #      non ne ha. `db_item.hsp:89761` (l'esca) ha `description(3)` giapponese
    #      vuota, e la 110a l'ha vista accendere il cancello su un gruppo da
    #      **trenta voci** — segnaposti, concatenazioni, battute — che di comune
    #      hanno solo il non avere una fonte. Non era una divergenza: era il
    #      raggruppamento a non voler dire niente.
    jp_lotto = {v['jp'] for v in lotto if (v.get('jp') or '').strip()}
    en_lotto = {v['en'] for v in lotto if (v.get('en') or '').strip()}

    per_jp = collections.defaultdict(set)
    per_en = collections.defaultdict(set)
    dove = collections.defaultdict(list)
    for v in voci_dizionario():
        if v['jp'] in jp_lotto:
            per_jp[v['jp']].add(v['it'])
            dove[('jp', v['jp'])].append(f"{v['_file']}:{v.get('riga')}")
        if v['en'] in en_lotto:
            per_en[v['en']].add(v['it'])
            dove[('en', v['en'])].append(f"{v['_file']}:{v.get('riga')}")

    divergenti_jp = {k: v for k, v in per_jp.items() if len(v) > 1}
    divergenti_en = {k: v for k, v in per_en.items() if len(v) > 1}

    for lato, etichetta, mappa, tutti in (('jp', 'GIAPPONESE', divergenti_jp, per_jp),
                                          ('en', 'INGLESE', divergenti_en, per_en)):
        giudicabili = sum(1 for k in tutti if len(dove[(lato, k)]) > 1)
        print(f'--- lo stesso {etichetta}, rese diverse: {len(mappa)}   '
              f'(gruppi con piu\' di una voce, cioe\' davvero giudicati: {giudicabili})')
        for chiave, rese in sorted(mappa.items())[:12]:
            print(f'    {chiave[:44]}')
            for r in sorted(rese):
                print(f'        {r[:78]}')
        print()

    print(f'{len(lotto)} rese del lotto, {len(jp_lotto)} giapponesi e '
          f'{len(en_lotto)} inglesi distinti')

    candidati = sorted(((len(dove[('jp', k)]), k) for k in per_jp), reverse=True)
    if not candidati:
        # ⚠️ succede quando il lotto NON e' ancora stato reimportato: il
        #    dizionario non ha nessuna di queste rese, quindi i due zeri qui
        #    sopra non dicono niente. Va lanciato DOPO `strumenti.reimporta`.
        sys.exit('⚠️ nessuna resa del lotto e\' nel dizionario: reimporta prima, '
                 'altrimenti i due zeri qui sopra non hanno guardato niente')
    quante, peggiore = candidati[0]
    finto = dict(per_jp)
    finto[peggiore] = set(list(per_jp[peggiore]) + ['RESA FINTA'])
    acceso = [k for k, v in finto.items() if len(v) > 1]
    if not acceso:
        sys.exit('⚠️ la prova al contrario NON si accende: la rete non guarda niente')
    print(f'prova al contrario: sul giapponese con piu\' voci ({quante} nel dizionario, '
          f'{peggiore[:30]}...) una resa cambiata accende la rete su {len(acceso)} gruppo')

    if divergenti_jp:
        sys.exit('⚠️ lo stesso giapponese e\' reso in piu\' di un modo: e\' il cancello')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
