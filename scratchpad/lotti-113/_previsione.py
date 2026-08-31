# -*- coding: utf-8 -*-
"""117a - La previsione di `applica` per un lotto, contata sul SORGENTE.

Nella 116a il lotto 042 aveva previsto «+35 esatte» e `applica` ha detto **+36**.
Il colpevole era `:126849` (Mournblade), il cui giapponese **e** il cui inglese
sono identici byte per byte a quelli di `<Stormbringer>`: stessa firma, una resa
sola che copre due righe del sorgente.

⚠️ La gemella **non e' in `lavoro/_107-daitem.jsonl`**, perche' l'estrazione
tiene una voce per firma. Non e' nel dossier, non e' nella tabella delle
categorie, non e' in nessuna tabella di lotto: sta **solo nel sorgente**. Per
questo il conto si fa qui e non leggendo una riga di tabella — e' la lezione
della 116a, che finora si rifaceva a mano ogni volta.

Il conto: si raggruppano per firma **tutte** le voci di `db_item.hsp`, e per
ogni riga del lotto si guarda quante righe del sorgente portano la sua stessa
firma. La previsione di `applica` e' la somma.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_previsione.py 045

Esce con 0 sempre: e' un referto. Una previsione diversa dal numero di rese non
e' un difetto — e' il moltiplicatore, e va scritta prima di lanciare `applica`.
"""
import collections
import importlib.util
import os
import sys

from strumenti.estrai import estrai_da_testo
from strumenti.percorsi import SORGENTE_HSP

QUI = os.path.dirname(os.path.abspath(__file__))
FILE = 'db_item.hsp'


def righe_del_lotto(numero):
    percorso = os.path.join(QUI, 'righe%s.py' % numero)
    spec = importlib.util.spec_from_file_location('righe%s' % numero, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return sorted(modulo.RIGHE)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    numero = sys.argv[1]
    righe = righe_del_lotto(numero)

    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    voci = estrai_da_testo(FILE, testo)

    per_riga = {v['riga']: v for v in voci}
    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v['riga'])

    mancanti = [r for r in righe if r not in per_riga]
    if mancanti:
        sys.exit('righe del lotto che il sorgente non ha: %s' % mancanti)

    firme = {}
    for r in righe:
        firme.setdefault(per_firma_di(per_riga, r), []).append(r)

    previsione = 0
    gemelle = []
    for firma, mie in sorted(firme.items(), key=lambda c: c[1][0]):
        tutte = sorted(per_firma[firma])
        previsione += len(tutte)
        if len(tutte) > len(mie):
            fuori = [r for r in tutte if r not in mie]
            gemelle.append((mie, fuori))
        elif len(mie) > 1:
            gemelle.append((mie, []))

    print('lotto %s: %d righe, %d firme distinte' % (numero, len(righe), len(firme)))
    print()
    if gemelle:
        print('=== LE GEMELLE: %d firme che coprono piu\' di una riga' % len(gemelle))
        for mie, fuori in gemelle:
            dentro = ', '.join(':%d' % r for r in mie)
            if fuori:
                print('   %s  ->  anche %s   ⚠️ FUORI DAL LOTTO'
                      % (dentro, ', '.join(':%d' % r for r in fuori)))
            else:
                print('   %s  ->  due righe dentro il lotto stesso' % dentro)
        print()
    else:
        print('=== NESSUNA GEMELLA: ogni firma del lotto copre una riga sola')
        print()

    print('previsione di `applica`: +%d sostituzioni per %d rese'
          % (previsione, len(righe)))
    if previsione != len(righe):
        print('   ⚠️ il moltiplicatore c\'e\': %d righe in piu\' del numero di rese'
              % (previsione - len(righe)))
    return 0


def per_firma_di(per_riga, riga):
    return per_riga[riga]['firma']


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
