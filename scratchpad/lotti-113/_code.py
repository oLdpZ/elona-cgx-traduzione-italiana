# -*- coding: utf-8 -*-
"""113a - La coda di ogni riga del lotto: il segmento dopo l'ultimo `\\n`.

Serve a scrivere le rese senza assegnare un titolo **a occhio**: stampa per ogni
riga la riga-fonte inglese verbatim e la resa che la tabella della 112a le da'.
⚠️ La chiave della tabella e' il GIAPPONESE, quindi si passa da li'; l'inglese
si stampa solo per riconoscere la riga.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_code.py 026
"""
import importlib.util
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'
TABELLA = 'scratchpad/lotti-112/titoli_fonte.py'


def tabelle():
    spec = importlib.util.spec_from_file_location('titoli_fonte', TABELLA)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.TITOLI_JP, modulo.TITOLI_EN


def coda(testo):
    """L'ultimo segmento, se comincia per `#`; altrimenti nessuna fonte."""
    pezzi = testo.split('\\n')
    for pezzo in reversed(pezzi):
        if pezzo.startswith('#'):
            return pezzo
    return None


def main():
    numero = sys.argv[1]
    spec = importlib.util.spec_from_file_location(
        'righe', os.path.join(QUI, 'righe%s.py' % numero))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    righe = modulo.RIGHE

    jp_it, en_it = tabelle()

    senza = 0
    for linea in io.open(LAVORO, encoding='utf-8'):
        if not linea.strip():
            continue
        voce = json.loads(linea)
        if voce['riga'] not in righe:
            continue
        coda_en = coda(voce.get('en') or '')
        coda_jp = coda(voce.get('jp') or '')
        resa = None
        if coda_jp:
            resa = jp_it.get(coda_jp[1:].strip())
        if resa is None and coda_en:
            resa = en_it.get(coda_en[1:].strip())
        print(':%d' % voce['riga'])
        print('   en  %s' % (coda_en if coda_en else '(nessuna fonte)'))
        if resa is None:
            senza += 1
            print('   IT  ⚠️ NESSUNA RESA IN TABELLA')
        else:
            marca = coda_en[:coda_en.index('~')] if coda_en and '~' in coda_en else '#'
            print('   IT  %s%s' % (marca, resa))
    print()
    print('righe senza resa in tabella: %d   (atteso 0)' % senza)
    return 1 if senza else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
