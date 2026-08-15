# -*- coding: utf-8 -*-
"""Il budget di larghezza della schermata «Background» (`*setHistory1`..`5`).

Le cinque righe si disegnano con `mes` a `pos wx + 75, wy + 200 + n * 15` dentro
una finestra larga 360 (`chara.hsp:3305`-`:3335`): nessuna guardia le misura,
come per la scheda del personaggio della 43a. Il metro possibile e' quello di
`tetti_buffdesc.py` — l'italiano **contro l'inglese di monte** — perche' la
finestra la larghezza ce l'ha gia' e upstream ci sta dentro (o non ci sta, e
allora l'italiano non deve peggiorare).

Stampa, per ciascuno dei cinque gruppi, la voce inglese piu' lunga: quel numero
e' il tetto in caratteri della riga corrispondente.
"""
import io, json, sys

ESTRAZIONE = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_command.jsonl'

GRUPPI = [
    ('setHistory1  origine',      9454, 9594),
    ('setHistory2  perche parti', 9595, 9732),
    ('setHistory3  pregio (testa)', 9733, 9870),
    ('setHistory4  difetto (coda)', 9871, 10008),
    ('setHistory5  vizio privato', 10009, 10146),
]

voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]

for nome, da, a in GRUPPI:
    zona = [v for v in voci if da <= v['riga'] <= a]
    if not zona:
        print('%-28s  nessuna voce da fare' % nome)
        continue
    lung = sorted(((len(v['en']), v['riga'], v['en']) for v in zona), reverse=True)
    n, riga, testo = lung[0]
    media = sum(x[0] for x in lung) / len(lung)
    print('%-28s  %3d voci   tetto %3d caratteri   media %4.1f' % (nome, len(zona), n, media))
    for n, riga, testo in lung[:3]:
        print('        %3d  :%d  %s' % (n, riga, testo))
