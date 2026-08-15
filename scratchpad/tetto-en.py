# -*- coding: utf-8 -*-
"""Il tetto in caratteri di una zona che nessuna guardia misura: l'inglese di monte.

    python scratchpad/tetto-en.py lavoro/_command.jsonl 1196 1536
    python scratchpad/tetto-en.py lavoro/_command.jsonl 1196 1536 lavoro/fase4-command-009.jsonl

⚠️ **`larghezze.py` misura SOLO `text.hsp`** (`larghezze.py:68`, `FILE =
"text.hsp"`): i suoi 75 menu sono tutti di li'. `riquadri.py` guarda l'HUD e le
tattiche, `diario.py` il diario delle missioni. Tutto il resto — la scheda del
personaggio (43a), la schermata del «Background» (44a), i menu di
`command.hsp` — non lo misura nessuno.

Il metro possibile in quei posti e' quello di `tetti_buffdesc.py`: **l'italiano
contro l'inglese di monte**. Il tetto e' la voce inglese piu' lunga della zona,
perche' quella il riquadro la contiene gia' — per il fatto che upstream ci gira.
Una resa che non la supera non puo' stare peggio.

⚠️ **E' un referto, non una guardia**: si rilancia a mano quando si tocca la
zona, e stima in caratteri quel che lo schermo disegna in pixel. Dove il
sorgente il budget lo dichiara davvero — due `pos` a poca distanza, come la
scheda del personaggio della 43a — quello vince su questo.

Col terzo argomento facoltativo confronta anche le rese di un lotto gia'
scritto, e stampa quelle che sforano.
"""
import io, json, sys

if len(sys.argv) not in (4, 5):
    sys.exit(__doc__)

estrazione, da, a = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lotto = sys.argv[4] if len(sys.argv) == 5 else None

voci = [json.loads(l) for l in io.open(estrazione, encoding='utf-8') if l.strip()]
zona = [v for v in voci if da <= v['riga'] <= a]
if not zona:
    sys.exit(f'nessuna voce fra {da} e {a} in {estrazione}')

lung = sorted(((len(v['en']), v['riga'], v['en']) for v in zona), reverse=True)
tetto = lung[0][0]
media = sum(x[0] for x in lung) / len(lung)
print(f'{len(zona)} voci fra {da} e {a}   tetto {tetto} caratteri   media {media:.1f}')
for n, riga, testo in lung[:3]:
    print(f'    {n:3d}  :{riga}  {testo}')

if lotto:
    # ⚠️ una dinamica e' un'espressione HSP: si misura il TESTO che produce, non
    # la lunghezza dell'espressione. `larghezze.reso` lo sa gia' fare — tiene i
    # pezzi letterali, conta ogni valore interpolato per tre cifre e degrada gli
    # accenti (che nel sorgente valgono due caratteri).
    from strumenti.larghezze import reso

    rese = [json.loads(l) for l in io.open(lotto, encoding='utf-8') if l.strip()]
    rese = [r for r in rese if r.get('it')]
    sfori = sorted(((len(reso(r['it'])), r['riga'], reso(r['it'])) for r in rese), reverse=True)
    print(f'\n{len(rese)} rese   la piu\' lunga ne fa {sfori[0][0]}')
    fuori = [x for x in sfori if x[0] > tetto]
    for n, riga, testo in fuori:
        print(f'  ⚠️ {n:3d} > {tetto}  :{riga}  {testo}')
    print(f'fuori tetto: {len(fuori)}')
