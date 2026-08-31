# -*- coding: utf-8 -*-
"""115a - La scheda del lotto 034: per ogni riga, la STRUTTURA dell'inglese.

La resa deve copiare la spaziatura dell'inglese davanti al `\\n#`, il `#` con o
senza lo spazio dopo, e l'eventuale `\\n` in coda. Guardarli a occhio nel
dossier e' come si perde un carattere: qui si stampano col `repr()`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_scheda034.py
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'


def main():
    numero = sys.argv[1] if len(sys.argv) > 1 else '034'
    spazio = {}
    exec(io.open(os.path.join(QUI, 'righe%s.py' % numero),
                 encoding='utf-8').read(), spazio)
    righe = spazio['RIGHE']

    voci = {}
    for r in io.open(LAVORO, encoding='utf-8'):
        d = json.loads(r)
        if d.get('riga') in righe:
            voci[d['riga']] = d

    for n in sorted(righe):
        d = voci[n]
        en = d.get('en') or ''
        jp = d.get('jp') or ''
        pezzi = en.split('\\n')
        print(':%d   segmenti en: %d   jp vuoto: %s' % (n, len(pezzi), jp == ''))
        for i, p in enumerate(pezzi):
            marca = 'CORPO' if not p.startswith('#') else 'FONTE'
            if p == '':
                marca = 'VUOTO'
            # solo la coda del corpo interessa: gli ultimi 20 caratteri col repr
            print('     %s[%d] ...%s' % (marca, i, repr(p[-40:])))
    print()
    print('%d righe' % len(righe))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
