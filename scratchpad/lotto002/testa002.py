# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-002: lo sguardo storto, l'ira, le maledizioni respinte
e i ventidue messaggi di resistenza (chara_func.hsp 2000-2999).

58 rese e **una rinviata**, su 59 voci. La zona e' stata scelta guardando lo
schermo, non l'elenco: lo screenshot del collaudo della 39ª aveva `glares at
you` (`:2021`) e `gets furious!` (`:2047`) fra le righe inglesi rimaste, e
`:2021` parte a **ogni** azione ostile contro un cittadino amichevole. E' la
lezione della 26ª — *la frequenza, non l'elenco* — per la seconda volta di
fila.

⭐⭐ **Quarantaquattro voci su cinquantanove sono lo STESSO blocco scritto due
volte.** `resistmod` (`:2675`-`:2741`) e `resistmodh` (`:2769`-`:2835`) sono i
due punti da cui il gioco annuncia che una resistenza e' salita o scesa — undici
elementi per due segni — e upstream li ha ricopiati **parola per parola**,
cambiando solo il nome della variabile (`resistmod_charid` /
`resistmodh_charid`). Quindi **ventidue rese coprono quarantaquattro siti**, e la
rete 4 le tiene inchiodate a coppie: stesso giapponese, stessa firma `['name']`,
stessi letterali. E' la percentuale di duplicazione piu' alta mai vista in un
lotto — piu' del menu delle tattiche del lotto `proc-026` (dodici su
trentaquattro) e dell'X-Frame del `-018` (nove su quarantadue).

⚠️⚠️ **E i ventidue sono tutti genitivo o participio, cioe' le due strade
insieme.** Il giapponese dice 「name **の**身体は…」, 「name **の**神経は…」,
「name **の**魂は…」, 「name **の**皮膚は…」: in italiano sarebbe «il corpo
**di** X», «i nervi **di** X», «l'anima **di** X», e `name()` porta gia'
l'articolo dentro (rete 8). E l'inglese ci mette il participio sopra — «`is
struck by an electric shock`», «`is covered by a magical aura`» — che
concorderebbe col personaggio.
✅ La strada e' una sola e vale per tutt'e ventidue: **il possesso implicito col
dativo riflessivo**, «X **si sente** il corpo in fiamme», «X **si sente** la
pelle avvolta in un'aura magica». Il possessivo sparisce e la concordanza cade
su un nome di genere fisso — «pelle» femminile, «corpo» maschile — non sul
personaggio. Dove il dativo non serviva basta il nome soggetto: «X ha i nervi
saldi», «X non teme piu' il buio», «X regge meglio i veleni».
💡 **E' la stessa scoperta del lotto 001 in forma nuova**: li' i sedici recuperi
si giravano col nome soggetto e il possesso implicito; qui il possesso implicito
si ottiene con «si sente», che l'italiano ha e l'inglese no.

⚠️⚠️ **`:2310` e' la seconda voce del progetto dentro un blocco spento.** Sta
in un `/********** ORIGINAL - BEGINNING
**********/ ... /********** ORIGINAL - ENDING **********/` — la riga con cui
monte annunciava un buff prima che il mod la sostituisse — ed e' testo che il
giocatore non legge mai. E' la classe di `proc.hsp:11796` della 37ª, la riga per
cui la rete 6 e' stata allargata ai commenti di BLOCCO. ✅ Rinviata, e **non c'e'
toppa da fare**: non e' un difetto a schermo, e' testo morto.
💡 **L'ha trovata il `dossier.py`, non la rete**: il blocco si vede nelle due
righe di contesto sopra la voce, e la rete 6 sarebbe scattata dopo — provato
girando `commenti-blocco.py` sul sorgente, che mette `:2310` fra le sue 46 righe
spente. Le due letture si confermano a vicenda, ed e' il motivo per cui il
dossier si legge prima di scrivere le rese e non dopo.

⚠️ **`:2280` e `:2298` sono un inglese solo per due giapponesi diversi**, ed e'
la rete 13 per la quarta volta. «`The holy veil repels the hex.`» sta per
「呪いを**防いだ**」 — la maledizione **respinta**, e il codice fa `return`
subito dopo — e per 「呪いを**弱めた**」, dove invece la maledizione entra e il
codice le **accorcia la durata** (`locvar_addbuff_fixeddur = limit(...)` due
righe sopra). L'inglese ha appiattito due esiti diversi in una riga; il
giapponese **e il codice** li distinguono. ✅ «respinge» e «attenua».

⚠️ **`:2021` e' un errore di monte piccolo e frequentissimo, ed e' il
trentaquattresimo.** Il giapponese e' 「name は嫌な顔をした。」 — *ha fatto una
faccia scocciata* — e l'inglese scrive «`glares at you`», cioe' **nomina il
giocatore**. Ma il ramo e' `cdata(CDATA_RELATION, hostileaction_target) == 10` e
basta: chi compie l'azione ostile puo' essere **chiunque**, e infatti il ramo
`else` di `:2024` guarda `hostileaction_source` proprio perche' li' la
distinzione serve. ✅ Reso sul giapponese, «`X storce il naso.`», che non nomina
nessun osservatore. 💡 E la rete 11 sarebbe stata d'accordo lo stesso:
l'inglese ha **un** `name()` e «you» non e' una funzione.

💡 **Quattro rese su cinquantotto sono copie**, tutte pescate da `dossier.py`:
«interrompe l'azione» (`adv.hsp:18`, stesso giapponese **e** stesso inglese),
«resiste» (`action.hsp:8844` e `proc.hsp:9322`), «L'etere ti corrode il corpo»
(`proc.hsp:25789`, stesso giapponese identico) e il termine «malattia
dell'etere» (`text.hsp:10113`).

💡 **E un termine tolto all'inglese**: `:2122` dice «`Incognito`», che e' il nome
del buff (`buff.hsp:67`, invariato), ma il giapponese scrive 「変装」, il nome
comune, che `buff.hsp:1020` rende gia' «Travestimento». Si segue il giapponese:
la riga parla della cosa, non del buff.
"""
