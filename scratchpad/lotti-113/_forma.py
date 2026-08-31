# -*- coding: utf-8 -*-
"""116a - La FORMA di ogni riga di un lotto, in una tabella sola.

`_scheda034.py` stampa il `repr()` dell'inglese e `_code.py` stampa la coda:
per scrivere le rese servono tutt'e due insieme, riga per riga. Nato nel lotto
044, il primo **disomogeneo**: 30 code su 39 senza spazio dopo il `#`, 9 con,
e solo 18 righe con lo spazio prima del `\\n`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_forma.py 044

Per ogni riga stampa:
    :riga   spazio-prima-del-\\n (SI/NO)   la coda italiana esatta da incollare
"""
import io
import json
import os
import subprocess
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'


def main():
    numero = sys.argv[1] if len(sys.argv) > 1 else '044'
    spazio = {}
    exec(io.open(os.path.join(QUI, 'righe%s.py' % numero),
                 encoding='utf-8').read(), spazio)
    righe = spazio['RIGHE']

    # le code italiane, dallo strumento che le assegna
    uscita = subprocess.run(
        [sys.executable, os.path.join(QUI, '_code.py'), numero],
        capture_output=True, text=True, encoding='utf-8').stdout
    code = {}
    corrente = None
    for r in uscita.split('\n'):
        if r.startswith(':'):
            corrente = int(r[1:].strip())
        elif r.strip().startswith('IT  ') and corrente is not None:
            code[corrente] = r.strip()[4:]
            corrente = None

    voci = {}
    for r in io.open(LAVORO, encoding='utf-8'):
        d = json.loads(r)
        if d.get('riga') in righe:
            voci[d['riga']] = d

    con = senza = 0
    for n in sorted(righe):
        en = voci[n]['en']
        coda = en.split('\\n')[-1]
        corpo = en[:len(en) - len(coda) - 2]
        ha_spazio = corpo.endswith(' ')
        con += ha_spazio
        senza += not ha_spazio
        print(':%-7d spazio prima del \\n: %-3s   %s'
              % (n, 'SI' if ha_spazio else 'NO', code.get(n, '???')))
    print()
    print('%d righe: %d con lo spazio prima del \\n, %d senza' % (len(righe), con, senza))
    scoda = sum(1 for c in code.values() if c.startswith('# ~'))
    print('code: %d con lo spazio dopo il #, %d senza' % (scoda, len(code) - scoda))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
