# -*- coding: utf-8 -*-
"""107a - Le firme di `db_item.hsp` che hanno lo STESSO INGLESE.

⚠️⚠️ **2.580 firme non sono 2.580 traduzioni da scrivere, e la differenza non
si vede aprendo un lotto.** La firma e' `(giapponese, inglese)`: due voci con
lo stesso inglese ma il giapponese diverso **di un carattere invisibile** —
un `\t` in testa, un `\n` in coda — sono due firme, e il dizionario le vuole
tutte e due. Se le si traduce in due momenti diversi escono due rese diverse
per la stessa frase, e nessuna rete del progetto lo vede: `battute
--divergenti` guarda i **giapponesi** uguali, non gli inglesi.

⭐ Il rendimento e' quello che dice il referto qui sotto: dice quanto lavoro
apparente e' la stessa frase scritta piu' volte, e quali gruppi vanno tradotti
**insieme** invece che a lotti diversi.

⚠️ E distingue due casi che non sono lo stesso problema:

  * **giapponese uguale a meno di spazi** — la frase e' la stessa e la resa
    deve essere identica: e' un difetto di monte, e va reso una volta sola;
  * **giapponese davvero diverso** — l'inglese di monte ha appiattito due cose
    che il giapponese distingue, e li' l'italiano puo' (deve?) distinguere.
    E' la forma di `_103-inglese-ripetuto.py` sulle carte.

    python scratchpad/_107-firme-gemelle.py
    python scratchpad/_107-firme-gemelle.py --mostra 10
"""
import argparse
import collections
import io
import json
import re
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'
_SPAZI = re.compile(r'\s+')
ACAPO = chr(92) + 'n'
TABULA = chr(92) + 't'


def _nudo(giapponese):
    """Il giapponese senza gli spazi e senza i marcatori di impaginazione."""
    return _SPAZI.sub('', giapponese.replace(ACAPO, '').replace(TABULA, ''))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mostra', type=int, default=0)
    a = ap.parse_args()

    voci = [json.loads(l) for l in io.open(LAVORO, encoding='utf-8') if l.strip()]
    per_inglese = collections.defaultdict(list)
    for voce in voci:
        per_inglese[voce['en']].append(voce)

    gruppi = [g for g in per_inglese.values() if len(g) > 1]
    stesso_jp = [g for g in gruppi if len({_nudo(v['jp']) for v in g}) == 1]
    jp_diverso = [g for g in gruppi if len({_nudo(v['jp']) for v in g}) > 1]

    doppie = sum(len(g) for g in gruppi) - len(gruppi)
    print(f'{len(voci)} firme da tradurre in {LAVORO}')
    print(f'  inglesi che tornano piu\' volte : {len(gruppi)}')
    print(f'  firme in piu\' che ne derivano  : {doppie}')
    print(f'  ⭐ traduzioni DAVVERO distinte  : {len(voci) - doppie}')
    print()
    print(f'  di cui, per gruppo:')
    print(f'    giapponese uguale a meno di spazi : {len(stesso_jp)} gruppi'
          f'  ({sum(len(g) for g in stesso_jp) - len(stesso_jp)} firme in piu\')')
    print(f'    ⚠️ giapponese DIVERSO              : {len(jp_diverso)} gruppi'
          f'  ({sum(len(g) for g in jp_diverso) - len(jp_diverso)} firme in piu\')')
    print()
    print('  💡 I primi sono la stessa frase e vogliono la STESSA resa: tradurne')
    print('     uno e propagarlo, non ritrovarseli in tre lotti diversi.')
    print('  ⚠️ I secondi sono l\'inglese di monte che appiattisce: li' + "'" +
          ' l\'italiano')
    print('     puo\' distinguere, e la scelta va presa guardando il giapponese.')

    if a.mostra:
        print()
        print(f'--- {a.mostra} gruppi col giapponese DIVERSO (i piu\' numerosi):')
        for gruppo in sorted(jp_diverso, key=len, reverse=True)[:a.mostra]:
            print(f'  EN  {gruppo[0]["en"][:100]}')
            for voce in gruppo[:6]:
                print(f'      :{voce["riga"]:<7} {voce["oggetto"]:<28} {voce["jp"][:60]}')
            if len(gruppo) > 6:
                print(f'      … e altre {len(gruppo) - 6}')
            print()


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
