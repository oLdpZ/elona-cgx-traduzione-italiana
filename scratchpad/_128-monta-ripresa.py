# -*- coding: utf-8 -*-
"""Monta la ripresa della 128a in testa, e manda la 127a nella storia.

  - le righe 1..22 (la testa della 127a) si buttano: le sostituisce la testa
    nuova, scritta a mano in `_128-nuova-ripresa.md`;
  - le righe 24..324 (il dettaglio della 127a) restano, ma sotto un titolo
    «La centoventisettesima sessione (per storia)» e con i loro `##` abbassati
    a `###`, come gia' fatto per la 126a, la 125a e la 124a;
  - dalla riga 325 in poi (la 126a e tutto il resto) non si tocca niente.

⚠️ Si compone e si valida PRIMA di aprire il file in scrittura (regola della 39a).
"""
import io

RIPRESA = 'RIPRESA-sessione.md'
NUOVA_TESTA = 'scratchpad/_128-nuova-ripresa.md'

righe = io.open(RIPRESA, encoding='utf-8').read().split('\n')

# Le ancore si controllano invece di fidarsi dei numeri.
if not righe[23].startswith("## ⭐⭐⭐ IL FRONTE DELLE RIGHE NUDE E' QUASI CHIUSO"):
    raise SystemExit('riga 24 non e\' l\'inizio del dettaglio della 127a: {!r}'
                     .format(righe[23][:80]))
if not righe[324].startswith('## La centoventiseiesima sessione'):
    raise SystemExit('riga 325 non e\' l\'inizio della 126a: {!r}'.format(righe[324][:80]))

dettaglio_127 = righe[23:324]
resto = righe[324:]

dettaglio_127 = ['#' + r if r.startswith('## ') else r for r in dettaglio_127]

testa = io.open(NUOVA_TESTA, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = (testa
         + ['', '---', '', '## La centoventisettesima sessione (per storia)', '']
         + dettaglio_127
         + resto)

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(RIPRESA, 'wb') as f:
    f.write(dati)
print('ripresa montata: {} righe ({} di testa nuova, {} di dettaglio 127a, '
      '{} di storia)'.format(len(nuovo), len(testa), len(dettaglio_127), len(resto)))
