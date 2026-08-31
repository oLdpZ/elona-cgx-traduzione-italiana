# -*- coding: utf-8 -*-
"""113a - Lo scheletro di un lotto del CORPO di `db_item.hsp` (indici 0, 1, 2).

`_107-chiavi-item.py` prende **un** indice per volta, e il corpo ne ha tre: la
prosa vera sta quasi tutta nell'indice 0, ma un oggetto puo' averne anche in 1 e
in 2, e quei tre segmenti il gioco li disegna **nello stesso pannello**, uno
sotto l'altro. Renderne uno e lasciare gli altri due in inglese produce un
pannello meta' italiano: la zona di un lotto del corpo dev'essere l'**unione**
dei tre indici sulle stesse righe.

⚠️ Lo scheletro non lo costruisce questo script: lo chiede tre volte allo
strumento di sempre e ne **incolla i blocchi**, come fa `lotti-111/_coda.py`.
Cosi' i filtri restano quelli del dossier, che e' l'unica cosa che conta.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_corpo.py \
        026 FILTER_ITEM_FOOD 42700 68000

Scrive `chiaviNNN.txt` e `righeNNN.py` nella cartella di questo script.
"""
import io
import os
import re
import subprocess
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
INDICI = (0, 1, 2)


def blocchi_di(categoria, indice, da, a):
    """(riga, corpo) per ogni voce che lo strumento emette con questi filtri."""
    uscita = subprocess.run(
        [sys.executable, 'scratchpad/_107-chiavi-item.py',
         '--categoria', categoria, '--indice', str(indice),
         '--da', str(da), '--a', str(a)],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout
    if 'nessuna voce con questi filtri' in uscita:
        return []
    pezzi = re.split(r'(?m)^    # -+ :(\d+)$\n', uscita)
    return [(int(pezzi[i]), pezzi[i + 1]) for i in range(1, len(pezzi) - 1, 2)]


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    numero, categoria, da, a = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

    tutti = {}
    for indice in INDICI:
        for riga, corpo in blocchi_di(categoria, indice, da, a):
            # ⚠️ una riga sta in un indice solo: se ricomparisse, uno dei due
            #    corpi andrebbe perso in silenzio, che e' il guasto che
            #    `_monta.py` esiste per rendere rumoroso.
            if riga in tutti:
                sys.exit('riga %d emessa da due indici diversi' % riga)
            tutti[riga] = corpo

    if not tutti:
        sys.exit('nessuna voce con questi filtri')

    numeri = sorted(tutti)
    righe_py = ['RIGHE = {']
    for inizio in range(0, len(numeri), 10):
        righe_py.append('    ' + ', '.join(str(n) for n in numeri[inizio:inizio + 10]) + ',')
    righe_py.append('}')
    testo_righe = '\n'.join(righe_py) + '\n'

    with io.open(os.path.join(QUI, 'righe%s.py' % numero), 'w',
                 encoding='utf-8', newline='\n') as f:
        f.write(testo_righe)

    with io.open(os.path.join(QUI, 'chiavi%s.txt' % numero), 'w',
                 encoding='utf-8', newline='\n') as f:
        f.write(testo_righe)
        # ⚠️ `_monta.py` cerca QUESTA riga per sapere dove finisce il RIGHE:
        #    senza, muore con StopIteration.
        f.write('# %d righe, da %d a %d\n' % (len(numeri), numeri[0], numeri[-1]))
        f.write('\n')
        for riga in numeri:
            f.write('    # ---------------------------------------------------------- :%d\n' % riga)
            f.write(tutti[riga].rstrip('\n') + '\n\n')

    per_indice = {i: len(blocchi_di(categoria, i, da, a)) for i in INDICI}
    print('lotto %s: %d righe (%s), da %d a %d'
          % (numero, len(numeri),
             ', '.join('indice %d: %d' % (i, n) for i, n in per_indice.items()),
             numeri[0], numeri[-1]))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
