# -*- coding: utf-8 -*-
"""Monta la ripresa della 131a in testa, e manda la 130a nella storia.

  - le righe 1..11 (la testa della 130a) si buttano: le sostituisce la testa
    nuova, scritta a mano in `_131-nuova-ripresa.md`;
  - le righe 13..337 (il dettaglio della 130a) restano, ma sotto un titolo
    «La centotrentesima sessione (per storia)» e con i loro `##` abbassati a
    `###`, come gia' fatto per la 129a e per tutte le altre;
  - dalla riga 338 in poi (la 129a e tutto il resto) non si tocca niente.

⚠️ Si compone e si valida PRIMA di aprire il file in scrittura (regola della 39a).
"""
import io

RIPRESA = 'RIPRESA-sessione.md'
NUOVA_TESTA = 'scratchpad/_131-nuova-ripresa.md'

righe = io.open(RIPRESA, encoding='utf-8').read().split('\n')

# Le ancore si controllano invece di fidarsi dei numeri.
if not righe[12].startswith("## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 130a"):
    raise SystemExit('riga 13 non e\' l\'inizio del dettaglio della 130a: {!r}'
                     .format(righe[12][:80]))
if not righe[337].startswith('## La centoventinovesima sessione'):
    raise SystemExit('riga 338 non e\' l\'inizio della 129a: {!r}'
                     .format(righe[337][:80]))

dettaglio_130 = righe[12:337]
resto = righe[337:]

dettaglio_130 = ['#' + r if r.startswith('## ') else r for r in dettaglio_130]

testa = io.open(NUOVA_TESTA, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = (testa
         + ['', '---', '', '## La centotrentesima sessione (per storia)', '']
         + dettaglio_130
         + resto)

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(RIPRESA, 'wb') as f:
    f.write(dati)
print('ripresa montata: {} righe ({} di testa nuova, {} di dettaglio 130a, '
      '{} di storia)'.format(len(nuovo), len(testa), len(dettaglio_130), len(resto)))
