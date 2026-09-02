# -*- coding: utf-8 -*-
"""125a - Sostituisce la TESTA di `RIPRESA-sessione.md` senza toccare la storia.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-sostituisci-testa.py scratchpad/_125-testa.md

⚠️ **Non e' `_125-riscrivi-ripresa.py`.** Quello fa scendere in storia la testa
vecchia, e va lanciato **una volta sola per sessione**: la 125a l'ha gia'
lanciato a meta' giornata, quando ha chiuso `custom_itemenchantment.hsp`, e la
124a e' gia' al suo posto. Rilanciarlo adesso spedirebbe in storia la testa
della 125a stessa, sotto il titolo sbagliato.

Questo script fa l'altra cosa: **riscrive la testa in posto**, cioe' sostituisce
tutto quel che sta prima della prima sezione perenne. Serve quando una sessione
lavora in due tranche e la seconda cambia i numeri della prima.

⚠️ Si rifiuta di scrivere se il confine non si trova o se il file si accorcia
troppo: meglio nessuna scrittura che una testa incollata a meta'.
"""
import io
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
RIPRESA = os.path.join(RADICE, 'RIPRESA-sessione.md')

CONFINE_PERENNI = '## Le cose che non stanno nel repo'


def main(percorso_testa):
    testo = io.open(RIPRESA, encoding='utf-8').read()
    righe = testo.split('\n')

    i_perenni = next((i for i, r in enumerate(righe)
                      if r.startswith(CONFINE_PERENNI)), None)
    assert i_perenni is not None, 'confine delle sezioni perenni non trovato'

    nuova = io.open(percorso_testa, encoding='utf-8').read().rstrip('\n')
    fuori = [nuova, ''] + righe[i_perenni:]
    risultato = '\n'.join(fuori)
    assert len(risultato) > len(testo) * 0.9, 'il file si e\' accorciato troppo'
    io.open(RIPRESA, 'w', encoding='utf-8', newline='\n').write(risultato)
    print('RIPRESA-sessione.md: testa sostituita, %d righe -> %d'
          % (len(righe), len(fuori)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1]))
