# -*- coding: utf-8 -*-
"""Chiude i tre rinvii dei nomi di mappa: la loro condizione era maturata.

I tre rinvii dicevano «va tradotta INSIEME a chi assegna, non prima». Chi
assegna e' stato tradotto in una sessione qualunque, e nessuno e' tornato a
leggerli: da allora i tre rami erano morti. La `lang()` **resta rinviata** —
e' la regola della rete 7 sui confronti contro un valore serializzato, ed e'
quel che rende stabile la stringa cercata dalla toppa — ma il motivo va
riscritto, perche' quello vecchio dice ancora «non prima» e chi lo legge domani
concluderebbe che c'e' del lavoro da fare.

⚠️ Si compone e si valida prima di riscrivere il file.
"""
import io
import json

CODA = (
    " ⚠️⚠️⚠️ AGGIORNATO NELLA 128a: LA CONDIZIONE DI QUESTO RINVIO E' MATURATA E "
    "NESSUNO SE N'ERA ACCORTO. Chi assegna il nome della mappa E' STATO TRADOTTO "
    "— map_rand.hsp:1287 dice «Sala feste», map.hsp:4092/:4104/:8296 dicono "
    "«Nave mercantile» e «Nave pirata» — quindi da quel giorno il confronto "
    "cercava una stringa che nessuno assegna piu' e IL RAMO ERA MORTO: il ballo "
    "nella sala delle feste durava 4 turni invece di 41, e lo scavo dentro una "
    "nave fruttava minerali invece di spazzatura. ✅ Riparato nella 128a con una "
    "toppa per sito, nella forma della migrazione di «Your Home» "
    "(toppa di map.hsp:1396): il letterale italiano si aggiunge FUORI da lang(), "
    "con un `|`, cosi' il confronto accetta tutt'e due e un salvataggio scritto "
    "prima della traduzione continua a funzionare. ⭐ LA lang() RESTA RINVIATA, "
    "ed e' voluto: e' la regola della rete 7, ed e' quel che rende stabile la "
    "stringa cercata dalla toppa. ⓘ Il cancello che d'ora in poi lo vede e' "
    "`scratchpad/_128-confronti-contro-un-nome-assegnato.py` (rami morti "
    "aggiunti dalla traduzione: atteso 0)."
)

FIRME = ('7de36b5b', 'a2a40494', '5ea77070')

righe = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
voci = [json.loads(l) for l in righe]

toccate = 0
for v in voci:
    if v['firma'].startswith(FIRME):
        if 'AGGIORNATO NELLA 128a' in v['motivo']:
            raise SystemExit('{}: la coda c\'e\' gia\''.format(v['firma'][:8]))
        v['motivo'] = v['motivo'] + CODA
        toccate += 1
        print('aggiornata', v['firma'][:8], v['file'])

if toccate != 3:
    raise SystemExit('attese 3 voci, toccate {}'.format(toccate))

dati = ''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in voci).encode('utf-8')
with io.open('rinviate.jsonl', 'wb') as f:
    f.write(dati)
print('{} voci riscritte in rinviate.jsonl'.format(len(voci)))
