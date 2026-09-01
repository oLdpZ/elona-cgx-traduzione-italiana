# -*- coding: utf-8 -*-
"""119a - Toglie dal template di un lotto le righe che stanno in `rinviate.jsonl`.

⚠️ **Perche' serve.** `scratchpad/_107-chiavi-item.py` legge l'estrazione
(`lavoro/_107-daitem.jsonl`) **direttamente**, senza passare da
`estrai.da_tradurre`, quindi non filtra le rinviate: `categorie.py` le filtra,
lui no. Una riga rinviata resta nel template, `_monta` muore con `KeyError`
perche' la resa non c'e', e chi non sa perche' e' tentato di rimetterla.

Il caso che l'ha fatto nascere e' `db_item.hsp:129299` (119a): giapponese e
inglese sono tutt'e due `\\t\\t\\n\\n`, cioe' uno slot vuoto. Resa identica
`reimporta` la rifiuta, resa vuota non e' esprimibile: l'unica forma e' il
rinvio, e allora il template deve smettere di chiederla.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_119-togli-rinviate.py 050 scratchpad/lotti-113

Riscrive `righeNNN.py` e `chiaviNNN.txt` nella cartella data, e stampa quante
righe sono uscite e quante restano. ⚠️ Va rilanciato **dopo ogni** `_corpo.py`,
che i due file li riscrive da capo.
"""
import io
import json
import os
import re
import sys

from strumenti import estrai, percorsi


def righe_rinviate(file_hsp):
    """I numeri di riga dell'estrazione le cui firme sono rinviate."""
    firme = estrai.carica_rinviate(None, file_hsp)
    righe = set()
    percorso = percorsi.PROGETTO / 'lavoro' / '_107-daitem.jsonl'
    for linea in io.open(percorso, encoding='utf-8'):
        if linea.strip():
            voce = json.loads(linea)
            if voce['firma'] in firme:
                righe.add(voce['riga'])
    return righe


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    numero, cartella = sys.argv[1], sys.argv[2]

    fuori = righe_rinviate('db_item.hsp')

    percorso_righe = os.path.join(cartella, 'righe%s.py' % numero)
    testo = io.open(percorso_righe, encoding='utf-8').read()
    numeri = [int(n) for n in re.findall(r'\d+', testo)]
    tenuti = [n for n in numeri if n not in fuori]
    tolti = [n for n in numeri if n in fuori]

    if not tolti:
        print('nessuna riga rinviata nel lotto %s: i file restano com\'erano' % numero)
        return

    righe_py = ['RIGHE = {']
    for inizio in range(0, len(tenuti), 10):
        righe_py.append('    ' + ', '.join(str(n) for n in tenuti[inizio:inizio + 10]) + ',')
    righe_py.append('}')
    nuovo = '\n'.join(righe_py) + '\n'

    with io.open(percorso_righe, 'w', encoding='utf-8', newline='\n') as f:
        f.write(nuovo)

    # ⚠️ `chiaviNNN.txt` e' a blocchi: una riga di commento `# ---- :NNN`, poi
    #    la chiave e la resa vuota. Si taglia sul commento, che e' l'unico
    #    posto in cui il numero di riga compare da solo.
    percorso_chiavi = os.path.join(cartella, 'chiavi%s.txt' % numero)
    vecchio = io.open(percorso_chiavi, encoding='utf-8').read()
    testa, resto = vecchio.split('\n\n', 1)
    blocchi = re.split(r'(?m)^(?=    # -+ :\d+$)', resto)
    tenuti_b = []
    for blocco in blocchi:
        trovato = re.match(r'    # -+ :(\d+)$', blocco.split('\n')[0])
        if trovato and int(trovato.group(1)) in fuori:
            continue
        tenuti_b.append(blocco)

    testa = nuovo + '# %d righe, da %d a %d' % (len(tenuti), tenuti[0], tenuti[-1])
    with io.open(percorso_chiavi, 'w', encoding='utf-8', newline='\n') as f:
        f.write(testa + '\n\n' + ''.join(tenuti_b))

    print('lotto %s: %d righe tolte perche\' rinviate (%s), ne restano %d'
          % (numero, len(tolti), ', '.join(':%d' % n for n in tolti), len(tenuti)))


if __name__ == '__main__':
    main()
