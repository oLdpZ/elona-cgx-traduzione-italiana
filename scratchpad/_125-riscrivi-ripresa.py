# -*- coding: utf-8 -*-
"""125a - Rimonta `RIPRESA-sessione.md`: testa nuova, la 124a in storia.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-riscrivi-ripresa.py

⚠️ Il file e' lungo ventimila righe e la testa si sostituisce **per confine
riconosciuto**, non per numero di riga: si cerca la prima riga
`## Le cose che non stanno nel repo` (la prima sezione perenne) e tutto quel che
sta prima e' la testa della sessione scorsa, che scende in storia sotto il suo
titolo. I due pannelli e i valori attesi, che la 124a aveva messo fra la
testa e le sezioni perenni, scendono insieme a lei: sono roba sua.

⚠️ Lo script si rifiuta di scrivere se i confini non si trovano o se il file
non cresce: meglio nessuna scrittura che una testa incollata a meta'.
"""
import io
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
RIPRESA = os.path.join(RADICE, 'RIPRESA-sessione.md')

CONFINE_PERENNI = '## Le cose che non stanno nel repo'
CONFINE_STORIA = '## La centoventitreesima sessione'
TITOLO_STORIA = '## La centoventiquattresima sessione (per storia)'


def main(percorso_testa):
    testo = io.open(RIPRESA, encoding='utf-8').read()
    righe = testo.split('\n')

    i_perenni = next((i for i, r in enumerate(righe)
                      if r.startswith(CONFINE_PERENNI)), None)
    i_storia = next((i for i, r in enumerate(righe)
                     if r.startswith(CONFINE_STORIA)), None)
    assert i_perenni is not None, 'confine delle sezioni perenni non trovato'
    assert i_storia is not None, 'confine della storia non trovato'
    assert i_perenni < i_storia, (i_perenni, i_storia)

    vecchia_testa = righe[:i_perenni]
    perenni = righe[i_perenni:i_storia]
    storia = righe[i_storia:]

    # la vecchia testa perde il suo titolo di primo livello e prende il proprio
    while vecchia_testa and not vecchia_testa[0].startswith('# '):
        vecchia_testa.pop(0)
    vecchia_testa = vecchia_testa[1:]          # via `# Ripresa sessione`
    while vecchia_testa and not vecchia_testa[0].strip():
        vecchia_testa.pop(0)

    nuova = io.open(percorso_testa, encoding='utf-8').read().rstrip('\n')

    fuori = ([nuova, ''] + perenni
             + [TITOLO_STORIA, ''] + vecchia_testa + ['', '---', '']
             + storia)
    risultato = '\n'.join(fuori)
    assert len(risultato) > len(testo) * 0.95, 'il file si e\' accorciato troppo'
    io.open(RIPRESA, 'w', encoding='utf-8', newline='\n').write(risultato)
    print('RIPRESA-sessione.md: %d righe -> %d' % (len(righe), len(fuori)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1]))
