# -*- coding: utf-8 -*-
"""115a - Le domande da fare alle rese PRIMA di montarle.

Non sostituisce i cancelli del lotto: li anticipa, cosi' un difetto si vede
mentre si scrive e non dopo aver rifatto la build.

  1. le chiavi sono esattamente quelle di `righeNNN.py`
  2. ogni resa finisce con la coda che `_code.py` le assegna
  3. la spaziatura prima del `\\n` e' quella dell'inglese
  4. nessuna parola supera la finestra di rinculo (15): sono quelle che
     l'impaginatore puo' spezzare, ed e' l'unico difetto che l'italiano
     raggiunge piu' dell'inglese

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_preflight034.py 034
"""
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'
RINCULO = 15


def carica(nome):
    spazio = {}
    exec(io.open(os.path.join(QUI, nome), encoding='utf-8').read(), spazio)
    return spazio


def main():
    numero = sys.argv[1] if len(sys.argv) > 1 else '034'
    righe = carica('righe%s.py' % numero)['RIGHE']
    it = carica('_traduzioni%s.py' % numero)['IT']

    guasti = 0
    print('chiavi: %d rese, %d righe' % (len(it), len(righe)))
    if set(it) != set(righe):
        guasti += 1
        print('  ⚠️ in piu\': %s' % sorted(set(it) - set(righe)))
        print('  ⚠️ mancanti: %s' % sorted(set(righe) - set(it)))

    voci = {}
    for r in io.open(LAVORO, encoding='utf-8'):
        d = json.loads(r)
        if d.get('riga') in righe:
            voci[d['riga']] = d

    print()
    print('=== LA SPAZIATURA PRIMA DEL `\\\\n` E IL `#`')
    for n in sorted(righe):
        en = voci[n].get('en') or ''
        resa = it[n]
        coda_en = en.split('\\n')[-1]
        coda_it = resa.split('\\n')[-1]
        corpo_en = en[:len(en) - len(coda_en) - 2]
        corpo_it = resa[:len(resa) - len(coda_it) - 2]
        if en.count('\\n') != resa.count('\\n'):
            guasti += 1
            print('  ⚠️ :%d segmenti diversi: en %d, it %d'
                  % (n, en.count('\\n'), resa.count('\\n')))
            continue
        fine_en = re.search(r'\s*$', corpo_en).group(0)
        fine_it = re.search(r'\s*$', corpo_it).group(0)
        if fine_en != fine_it:
            guasti += 1
            print('  ⚠️ :%d spaziatura: en %r, it %r' % (n, fine_en, fine_it))
        marca_en = coda_en[:coda_en.index('~')] if '~' in coda_en else coda_en
        marca_it = coda_it[:coda_it.index('~')] if '~' in coda_it else coda_it
        if marca_en.strip('~') != marca_it.strip('~') and '~' in coda_en:
            guasti += 1
            print('  ⚠️ :%d marca: en %r, it %r' % (n, marca_en, marca_it))
        if coda_en.startswith('#') != coda_it.startswith('#'):
            guasti += 1
            print('  ⚠️ :%d il `#` non corrisponde' % n)
    print('  guasti finora: %d' % guasti)

    print()
    print('=== LE PAROLE LUNGHE (finestra di rinculo %d)' % RINCULO)
    lunghe = 0
    for n in sorted(righe):
        for pezzo in it[n].split('\\n'):
            if pezzo.startswith('#'):
                continue
            for parola in pezzo.split(' '):
                p = parola.strip('.,;:!?()«»"\'')
                if len(p) > RINCULO - 1:
                    lunghe += 1
                    print('  ⚠️ :%d  %d caratteri  %s' % (n, len(p), p))
    if not lunghe:
        print('  nessuna parola oltre i %d caratteri' % (RINCULO - 1))

    print()
    print('=== LE CODE, contate')
    print('  righe: %d   guasti di struttura: %d   parole lunghe: %d'
          % (len(righe), guasti, lunghe))
    return 1 if guasti else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
