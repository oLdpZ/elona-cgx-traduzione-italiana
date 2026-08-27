# -*- coding: utf-8 -*-
"""111a - Lo scheletro dell'ULTIMO lotto dell'indice 3: la coda.

`_107-chiavi-item.py` seleziona per **categoria**, e la coda dell'indice 3 non
e' una categoria: sono nove categorie minuscole piu' una voce che categoria non
ha (`ITEM_ID_DUMMY`). Questo script prende lo scheletro intero dell'indice 3 —
generato dallo strumento di sempre, cosi' i filtri restano gli stessi — e tiene
solo le righe che nel dizionario **non hanno ancora una resa**.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-111/_coda.py

Scrive `scratchpad/lotti-111/chiavi025.txt` e `scratchpad/lotti-111/righe025.py`.
"""
import io
import json
import re
import subprocess
import sys

CARTELLA = 'scratchpad/lotti-111'


def gia_rese():
    """Le righe che nel dizionario hanno gia' una resa.

    ⚠️ Si guarda il POSITIVO, non il negativo: le righe della coda non stanno
    ancora nel dizionario **per niente** — cercare quelle con l'italiano vuoto
    ne trovava zero e lo script diceva «l'indice 3 e' chiuso» quando restavano
    venticinque righe. Un elenco vuoto non e' una risposta.
    """
    numeri = set()
    with io.open('dizionario/db_item.hsp.jsonl', encoding='utf-8') as f:
        for riga in f:
            voce = json.loads(riga)
            if (voce.get('it') or '').strip():
                numeri.add(voce['riga'])
    return numeri


def main():
    uscita = subprocess.run(
        [sys.executable, 'scratchpad/_107-chiavi-item.py', '--indice', '3'],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout

    fatte = gia_rese()
    blocchi = re.split(r'(?m)^    # -+ :(\d+)$\n', uscita)
    # blocchi[0] e' la testa col RIGHE; poi (numero, corpo) a coppie
    tenuti = []
    for i in range(1, len(blocchi) - 1, 2):
        numero = int(blocchi[i])
        if numero not in fatte:
            tenuti.append((numero, blocchi[i + 1]))

    if not tenuti:
        print('niente da fare: l\'indice 3 e\' chiuso')
        return

    numeri = sorted(n for n, _ in tenuti)
    with io.open(f'{CARTELLA}/righe025.py', 'w', encoding='utf-8') as f:
        f.write('RIGHE = {\n')
        for inizio in range(0, len(numeri), 10):
            f.write('    ' + ', '.join(str(n) for n in numeri[inizio:inizio + 10]) + ',\n')
        f.write('}\n')

    with io.open(f'{CARTELLA}/chiavi025.txt', 'w', encoding='utf-8') as f:
        f.write(io.open(f'{CARTELLA}/righe025.py', encoding='utf-8').read())
        # ⚠️ `_monta.py` cerca QUESTA riga per sapere dove finisce il RIGHE e
        #    dove comincia lo scheletro: senza, muore con StopIteration.
        f.write('# %d righe, da %d a %d\n' % (len(numeri), numeri[0], numeri[-1]))
        f.write('\n')
        for numero, corpo in tenuti:
            f.write('    # ---------------------------------------------------------- :%d\n'
                    % numero)
            f.write(corpo.rstrip('\n') + '\n\n')

    print(f'{len(tenuti)} righe ancora da fare, scritte in {CARTELLA}/chiavi025.txt')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
