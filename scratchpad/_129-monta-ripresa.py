# -*- coding: utf-8 -*-
"""Monta la ripresa della 129a in testa, e manda la 128a nella storia.

  - le righe 1..11 (la testa della 128a) si buttano: le sostituisce la testa
    nuova, scritta a mano in `_129-nuova-ripresa.md`;
  - le righe 14..280 (il dettaglio della 128a) restano, ma sotto un titolo
    «La centoventottesima sessione (per storia)» e con i loro `##` abbassati
    a `###`, come gia' fatto per la 127a, la 126a, la 125a e la 124a;
  - dalla riga 281 in poi (la 127a e tutto il resto) non si tocca niente.

⚠️ Si compone e si valida PRIMA di aprire il file in scrittura (regola della 39a).
"""
import io

RIPRESA = 'RIPRESA-sessione.md'
NUOVA_TESTA = 'scratchpad/_129-nuova-ripresa.md'

righe = io.open(RIPRESA, encoding='utf-8').read().split('\n')

# Le ancore si controllano invece di fidarsi dei numeri.
if not righe[13].startswith("## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 128a"):
    raise SystemExit('riga 14 non e\' l\'inizio del dettaglio della 128a: {!r}'
                     .format(righe[13][:80]))
if not righe[280].startswith('## La centoventisettesima sessione'):
    raise SystemExit('riga 281 non e\' l\'inizio della 127a: {!r}'.format(righe[280][:80]))

dettaglio_128 = righe[13:280]
resto = righe[280:]

dettaglio_128 = ['#' + r if r.startswith('## ') else r for r in dettaglio_128]

testa = io.open(NUOVA_TESTA, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = (testa
         + ['', '---', '', '## La centoventottesima sessione (per storia)', '']
         + dettaglio_128
         + resto)

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(RIPRESA, 'wb') as f:
    f.write(dati)
print('ripresa montata: {} righe ({} di testa nuova, {} di dettaglio 128a, '
      '{} di storia)'.format(len(nuovo), len(testa), len(dettaglio_128), len(resto)))
