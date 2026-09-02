# -*- coding: utf-8 -*-
"""Infila le decisioni della 127a in cima a `decisioni.md`, sotto l'intestazione.

Il documento tiene le voci in ordine inverso di data: l'intestazione, un `---`,
e poi la sessione piu' recente. Qui si inserisce subito dopo quel `---`.

⚠️ Si compone e si valida PRIMA di aprire il file (regola della 39a).
"""
import io

DECISIONI = 'decisioni.md'
NUOVE = 'scratchpad/_127-decisioni.md'

righe = io.open(DECISIONI, encoding='utf-8').read().split('\n')

# il primo `---` da solo su una riga chiude l'intestazione
try:
    taglio = next(i for i, r in enumerate(righe) if r.strip() == '---')
except StopIteration:
    raise SystemExit("decisioni.md non ha il `---` dopo l'intestazione")

if not any(r.startswith('## ') for r in righe[taglio:taglio + 6]):
    raise SystemExit('dopo il `---` non c\'e\' una voce `## `: il documento e\' '
                     'cambiato, non inserisco alla cieca')

nuove = io.open(NUOVE, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = righe[:taglio + 1] + [''] + nuove + [''] + righe[taglio + 1:]

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(DECISIONI, 'wb') as f:
    f.write(dati)
print('decisioni montate: {} righe nuove in cima, {} totali'
      .format(len(nuove), len(nuovo)))
