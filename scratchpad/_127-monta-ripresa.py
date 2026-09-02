# -*- coding: utf-8 -*-
"""Monta la ripresa della 127a in testa, e manda la 126a nella storia.

Il documento tiene la testa della sessione appena chiusa e sotto, in ordine, le
sessioni vecchie. Qui:

  - le righe 1..85 (la testa della 126a) si buttano: le sostituisce la testa
    nuova, scritta a mano in `_127-nuova-ripresa.md`;
  - le righe 86..261 (il dettaglio della 126a) restano, ma sotto un titolo
    «La centoventiseiesima sessione (per storia)» e con i loro `##` abbassati a
    `###`, come gia' fatto per la 125a e la 124a;
  - dalla riga 262 in poi (la 125a e tutto il resto) non si tocca niente.

⚠️ Si compone e si valida PRIMA di aprire il file (regola della 39a).
"""
import io

RIPRESA = 'RIPRESA-sessione.md'
NUOVA_TESTA = 'scratchpad/_127-nuova-ripresa.md'

righe = io.open(RIPRESA, encoding='utf-8').read().split('\n')

# Le ancore si controllano invece di fidarsi dei numeri: se il documento e'
# cambiato, ci si ferma qui e non a meta' scrittura.
if not righe[85].startswith('## LE QUARANTA TOPPE DELLA 126a'):
    raise SystemExit('riga 86 non e\' l\'inizio del dettaglio della 126a: {!r}'
                     .format(righe[85][:80]))
if not righe[261].startswith('## La centoventicinquesima sessione'):
    raise SystemExit('riga 262 non e\' l\'inizio della 125a: {!r}'.format(righe[261][:80]))

dettaglio_126 = righe[85:261]
resto = righe[261:]

# i titoli della 126a scendono di un livello, cosi' stanno sotto il suo
# cappello di storia invece di sembrare sezioni della 127a
dettaglio_126 = ['#' + r if r.startswith('## ') else r for r in dettaglio_126]

testa = io.open(NUOVA_TESTA, encoding='utf-8').read().rstrip('\n').split('\n')

nuovo = (testa
         + ['', '---', '', '## La centoventiseiesima sessione (per storia)', '']
         + dettaglio_126
         + resto)

dati = ('\n'.join(nuovo)).encode('utf-8')
with io.open(RIPRESA, 'wb') as f:
    f.write(dati)
print('ripresa montata: {} righe ({} di testa nuova, {} di dettaglio 126a, '
      '{} di storia)'.format(len(nuovo), len(testa), len(dettaglio_126), len(resto)))
