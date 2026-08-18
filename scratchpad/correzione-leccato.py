# -*- coding: utf-8 -*-
"""`event.hsp:669` aveva un participio che concorda col giocatore.

«Ti sei leccato i baffi.» rende 「あなたは舌鼓をうった。」 / «You smack your
lips.», ed e' una delle tre battute del banchetto misterioso (lotto
`fase4-event-001`, 59a). Il participio prende il genere del soggetto, e il
soggetto e' il giocatore: `guida-stile.md` lo vieta da sempre — «mai un
aggettivo o un participio riferito al giocatore o a `name()`: il genere non si
conosce».

Il difetto non lo ha visto nessuna guardia della catena: `verifica.py` non
guarda i participi, e `referti.py` — che li guarda — non e' fra le dieci
verifiche d'apertura, e' fra i referti da leggere. La 60a lo ha ereditato senza
saperlo, e la 61a lo ha trovato lanciando `referti.py` dopo un lotto che non
c'entrava niente.

La resa nuova e' al **presente**, come l'inglese di monte e come il resto del
registro: «Ti lecchi i baffi.» Le due battute sorelle (`Era buono.`, `Niente
male.`) sono impersonali e non avevano il problema.

⚠️ Si compone tutto in memoria e si scrive solo alla fine: e' la regola della
39a, quando uno script che apriva il file in scrittura e componeva dentro
`write()` ha lasciato `toppe.jsonl` a zero byte.
"""
import io
import json

PERCORSO = 'dizionario/event.hsp.jsonl'
FIRMA = 'e897d0b53565e739f80bf72377bcc5d1462a8e45'
PRIMA = 'Ti sei leccato i baffi.'
DOPO = 'Ti lecchi i baffi.'

righe = io.open(PERCORSO, encoding='utf-8').read().split('\n')
fatte = 0
nuove = []
for riga in righe:
    if not riga.strip():
        nuove.append(riga)
        continue
    d = json.loads(riga)
    if d.get('firma') == FIRMA:
        if d.get('it') != PRIMA:
            raise SystemExit(f'la voce {FIRMA} dice {d.get("it")!r}, non {PRIMA!r}')
        d['it'] = DOPO
        fatte += 1
        nuove.append(json.dumps(d, ensure_ascii=False))
        continue
    nuove.append(riga)

if fatte != 1:
    raise SystemExit(f'la firma {FIRMA} aggancia {fatte} voci, non una')

testo = '\n'.join(nuove)
io.open(PERCORSO, 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{PERCORSO}: {PRIMA!r} -> {DOPO!r}')
