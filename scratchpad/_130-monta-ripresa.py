# -*- coding: utf-8 -*-
"""Monta la ripresa della 130a in testa, e manda la 129a nella storia.

  - le righe 1..11 (la testa della 129a) si buttano: le sostituisce la testa
    nuova, scritta a mano in `_130-nuova-ripresa.md`;
  - le righe 14..270 (il dettaglio della 129a) restano, ma sotto un titolo
    «La centoventinovesima sessione (per storia)» e con i loro `##` abbassati
    a `###`, come gia' fatto per la 128a, la 127a, la 126a e le altre;
  - dalla riga 271 in poi (la 128a e tutto il resto) non si tocca niente.

⚠️ Si compone e si valida PRIMA di aprire il file in scrittura (regola della 39a).
"""
import io

RIPRESA = 'RIPRESA-sessione.md'
NUOVA_TESTA = 'scratchpad/_130-nuova-ripresa.md'

righe = io.open(RIPRESA, encoding='utf-8').read().split('\n')

# Le ancore si controllano invece di fidarsi dei numeri.
if not righe[13].startswith("## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 129a"):
    raise SystemExit('riga 14 non e\' l\'inizio del dettaglio della 129a: {!r}'
                     .format(righe[13][:80]))
if not righe[270].startswith('## La centoventottesima sessione'):
    raise SystemExit('riga 271 non e\' l\'inizio della 128a: {!r}'.format(righe[270][:80]))

dettaglio_129 = righe[13:270]
resto = righe[270:]

dettaglio_129 = ['#' + r if r.startswith('## ') else r for r in dettaglio_129]

testa = io.open(NUOVA_TESTA, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = (testa
         + ['', '---', '', '## La centoventinovesima sessione (per storia)', '']
         + dettaglio_129
         + resto)

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(RIPRESA, 'wb') as f:
    f.write(dati)
print('ripresa montata: {} righe ({} di testa nuova, {} di dettaglio 129a, '
      '{} di storia)'.format(len(nuovo), len(testa), len(dettaglio_129), len(resto)))
