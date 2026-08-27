# -*- coding: utf-8 -*-
"""Le 143 rese del lotto 004 contro TUTTO il dizionario, in due direzioni.

La rete 13 del lotto guarda solo **dentro** il lotto. Queste due domande
guardano fuori, e sono quelle che nessuna rete del lotto puo' porsi:

  A) lo stesso GIAPPONESE reso in due modi diversi (dentro o fuori dal lotto);
  B) lo stesso INGLESE reso in due modi diversi.

⚠️ Il valore atteso di (B) **non e' zero** in generale — inglesi diversi per
giapponesi diversi capitano — quindi si stampa il numero e il confronto e' con
le voci del lotto, non con uno zero.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-109/_coerenza004.py
"""
import collections
import glob
import io
import json
import os
import sys

LOTTO = 'lavoro/fase5-db_item-004.jsonl'


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
    lotto = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
    jp_lotto = {v['jp'] for v in lotto}
    en_lotto = {v['en'] for v in lotto}

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
        # ⚠️⚠️ IL NUMERO CHE RENDE LEGGIBILE LO ZERO non e' lo zero: e' quanti
        # gruppi avessero davvero PIU' DI UNA voce da confrontare. Un gruppo di
        # una voce sola non puo' divergere, e una rete che ne guarda solo di
        # quelli dice zero senza aver giudicato niente.
        # ⚠️ qui c'era `etichetta[:2].lower()`, cioe' 'gi' e 'in': la spia diceva
        #    «0 gruppi giudicati» mentre la prova al contrario ne trovava uno da
        #    quattro. L'ha presa la prova al contrario, non l'occhio.
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

    # --- la prova al contrario: si CERCA il caso peggiore invece di ipotizzarlo.
    # Si prende il giapponese del lotto che nel dizionario ha piu' voci, gli si
    # cambia una resa, e la rete deve accendersi dicendo QUALE.
    candidati = sorted(((len(dove[('jp', k)]), k) for k in per_jp), reverse=True)
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
