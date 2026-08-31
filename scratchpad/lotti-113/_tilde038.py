# -*- coding: utf-8 -*-
"""115a - I caratteri della coda di un gruppo di righe, uno per uno.

Nato su `db_item.hsp:46213`, dove il dossier stampa `#?ティリス園芸図鑑?` con
un punto interrogativo al posto della tilde e l'inglese la coda non ce l'ha
proprio. Prima di decidere che cosa scrivere bisogna sapere **che carattere e'**.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_tilde038.py 46213 46214
"""
import io
import json
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'
ACAPO = '\\n'


def coda(testo):
    pezzi = (testo or '').split(ACAPO)
    return pezzi[-1] if len(pezzi) > 1 else None


def main():
    volute = {int(a) for a in sys.argv[1:]}
    for r in io.open(LAVORO, encoding='utf-8'):
        d = json.loads(r)
        if d.get('riga') not in volute:
            continue
        for lingua in ('jp', 'en'):
            c = coda(d.get(lingua))
            if c is None:
                print(':%d  %s  coda: NESSUNA' % (d['riga'], lingua))
                continue
            print(':%d  %s  coda: %r' % (d['riga'], lingua, c))
            print('        %s' % ' '.join('U+%04X' % ord(x) for x in c[:6]))
            print('        ...%s' % ' '.join('U+%04X' % ord(x) for x in c[-3:]))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
