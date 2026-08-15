# -*- coding: utf-8 -*-
"""Lotto `command-010`: i 39 pensieri di `*com_knowOther`, prima meta'.

E' la telepatia: quel che un compagno sta pensando, letto col comando che apre
la finestra «こころの中» / «In the heart» (`:1928`). Il sorgente e' una cascata
di `if` che si sovrascrivono a vicenda — l'ultima condizione vera vince — e
questo lotto prende i primi cinque blocchi:

| blocco | quando | voci |
|---|---|---|
| generico | sempre, `rnd(17)` | 17 |
| fame | `CDATA_HUNGER <= 10000` | 5 |
| sete | `CDATA_THIRST <= 10000` | 4 |
| affetto | `CDATA_EVOCHAT_POINTS > 0`, poi `== 10` | 6 |
| combattimento | `CDATA_AI_AGGRO > 0`, uno per `CDATA_TONE` | 7 |

✅ **Il registro e' il monologo interiore in prima persona**, che e' quel che il
giapponese fa senza soggetto — 「もっと刺激がほしい」, 「昔のことを思い出して
いる」 — e che in italiano non ha genere finche' si resta al **presente e senza
participio**: «Voglio piu' emozioni», «Sto ripensando ai vecchi tempi». Il
compagno puo' essere di qualunque genere, come nel «Background» della stessa
sessione.
⚠️ Due rese sono state girate proprio per questo: 「もっと自分のことを理解して
ほしい」 non e' «vorrei essere capito» ma «vorrei che mi capissi di piu'», e
「愛を感じていたい」 non e' «vorrei sentirmi amato» ma «ho bisogno di sentire
l'amore».

⚠️ **L'inglese cambia persona a meta' elenco, e il giapponese no.** Dentro lo
stesso blocco della fame ci sono «Want to eat anything» (prima persona
sottintesa) e «Wants to eat a lot» / «Wants a sweet one» (terza), e nel blocco
generico «Hungry and has no strength.» e' terza persona con tanto di punto.
Il giapponese e' uniforme: sono tutti pensieri, e in italiano sono tutti in
prima persona.

⚠️ **I sette pensieri di combattimento sono lo stesso momento in sette
caratteri**, uno per valore di `CDATA_TONE`, cioe' il tono che si sceglie col
comando «Change Tone». Vanno tenuti distinti fra loro: `:1678` e `:1690` dicono
tutt'e due «non perdo», ma il primo e' una promessa e il secondo un'arroganza —
「絶対負けない」 contro 「負けるわけがない」. E `:1693` 「いざ尋常に勝負！」 e'
lingua da duello antico.

💡 **Tetto 42 caratteri** (`:1590`), misurato con `scratchpad/tetto-en.py`.
⚠️ Anche questa finestra non la guarda nessuna guardia: `*com_knowOther` disegna
con `gmes` a `wx + 54` dentro una finestra da 400 px (`:1929`, `:1942`), quindi
non passa da `*prompt_key` e `larghezze.py` — che comunque legge solo
`text.hsp` — non c'entra niente.

💡 Zero copie da `dossier.py`.
"""
