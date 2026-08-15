# -*- coding: utf-8 -*-
"""Lotto `command-026`: **le tasse, le medagliette, le cose da non posare**.
Trenta rese, e con queste **la zona 15000-15999 e' chiusa**.

⭐⭐ **Otto rese su trenta non le ho decise io, ed e' il record del progetto per
un lotto solo.** Sei sono il coro della schermata dei traguardi — «Finalmente!»,
«Era il risultato naturale.», «Uooooooh!», «Hmpf.», «Stanotte non chiudo
occhio.», «Stai scherzando.» — che `text.hsp:477`-`:492` ha gia' reso perche' la
stessa lista serve a **ogni** traguardo del gioco: qui `:15564`-`:15569` la
riscrive tale e quale per la sfida delle tasse doppie. Le altre due sono «Non hai
abbastanza denaro...» (`proc.hsp:15584`) e «Mai!», che ho scritto io **due lotti
fa** (`:15196`, lotto 024). ⭐ La rete 3 le ha nominate tutte e otto da sola.

⭐⭐ **E qui l'italiano puo' rimettere quel che l'inglese ha buttato via.**
`:15636` e `:15645` hanno **lo stesso identico inglese** — «name swallows
itemname angrily» — e due giapponesi che non si somigliano per niente: a `:15636`
l'alleato «va su tutte le furie e ingoia» l'anello di fidanzamento, a `:15645`
«si ficca in bocca il cioccolatino in fretta e, masticando, risponde che non ha
nessun oggetto del genere». L'inglese ha appiattito una scenetta comica su una
frase di rabbia. ✅ La resa italiana puo' tenerle distinte **senza violare la
rete 11**, perche' quella confronta l'insieme delle funzioni di contenuto e
tutt'e due le righe hanno `name` piu' `itemname`, in inglese come in giapponese.
💡 E' il rovescio del caso di `:15188` nel lotto 024: la' l'inglese diceva la
cosa sbagliata e la rete 3 ha imposto il giapponese, qui l'inglese dice **meno**
e nessuna rete obbliga a niente — a decidere e' che le funzioni bastano.
⚠️ La rete 13 lo segnala, ed e' il suo mestiere: un inglese per due giapponesi.

⚠️⚠️ **Tre delle quattro battute di `:15615` non le vede nessuno, e non e' una
riga spenta.** L'array e' `s = "", 「やだ」, 「あげないよ」, 「だめ」, 「イヤ！」` e
l'indice arriva da `f`, che due righe sopra vale **`0` oppure `2`**:
`f = 0` a `:15610`, `f = 2` a `:15612` se l'oggetto e' un minerale, e `:15614`
entra solo `if ( f != 0 )`. Quindi il gioco stampa **sempre e solo lo slot 2**,
«Non si tocca!», e gli slot 1, 3 e 4 sono irraggiungibili.
⚠️ **Ma non sono testo morto nel senso della rete 6**: la riga e' viva, la
`lang()` gira, il valore finisce dentro `s`. A spegnerli e' l'**aritmetica di un
indice**, che nessuno strumento del progetto guarda — non `commenti-blocco.py`,
non `lang-nel-ramo-jp.py`, non la rete 6. ✅ Si traducono lo stesso, e per un
motivo pratico: basta che upstream aggiunga un `f = 3` da qualche parte perche'
tornino vivi, e allora sarebbero inglese in mezzo all'italiano.
💡 E' la **quarta famiglia** dopo il `;`, il `/* */` e il ramo della lingua — ma
la prima che non e' un fatto del testo: e' un fatto del **flusso**.

⚠️ **`:15627` nomina il soggetto in giapponese e non in inglese, ed e' statica.**
Il giapponese e' `name(tc) + "は洗脳されていて、装備を外さない！"`, l'inglese «It is
impossible to change the equipment by confusing» — nessuna funzione. La resa non
puo' nominare nessuno (la regola del contratto con la riga), quindi va
all'impersonale: «Sotto plagio non si cambia equipaggiamento!». 💡 «Plagio» e' il
termine che `buff.hsp:1362` ha gia' scelto per `brainwash`.

⭐ Altri termini riscossi: «Medagliette» e «Biglietti» (`command.hsp:14105`,
`:14108`), «Carretto» (`:14176`), «Scorciatoia» (`text.hsp:10`, `:121`), e la
coppia «posare»/«[Non posare]» del menu (`:14087`, `:14091`), che decide come si
dicono `no-drop` e `continuously drop` senza inventare niente.
"""
