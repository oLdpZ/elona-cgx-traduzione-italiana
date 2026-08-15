# -*- coding: utf-8 -*-
"""Lotto fase4-command-001: quel che c'è per terra, i letti, il bersaglio
(command.hsp, righe 13-993).

⭐⭐ **Apre `command.hsp`, e a chiederlo è stato lo SCHERMO.** Il collaudo della
42ª ha mostrato che il log di combattimento è italiano e che l'inglese rimasto
è **la cornice del mondo**: questo file ne è il grosso, 1.304 firme. Il lotto è
il primo di otto o dieci, 37 rese e **3 rinviate** dalla rete 6.

⭐⭐ **`:23` è la riga che parte a OGNI passo su un oggetto**, ed è probabilmente
la stringa più letta fra tutte quelle che restano.

⚠️⚠️ **Le tre righe della casella non possono copiare «Si vede» di `text.hsp`, e
la ragione è il NUMERO.** `text.hsp:3095` rende 「がある。」 «Si vede " + s + ".»,
e la rete 3 lo dirà: ma lì `s` è il nome di un edificio, sempre singolare,
mentre qui `rtvaln` è `itemname()` di una **pila** — «Si vede 3 pozioni» è
sgrammaticato, perché l'impersonale italiano vuole «si vedono». ✅ «**Vedi** X»
è di seconda persona e regge un oggetto diretto: non concorda con niente, né in
genere né in numero, e copre tutt'e tre le righe.
💡 Ed è la stessa trappola vista da capo: `:13` compone `rtvaln` come «a e b»
(fino a tre oggetti, `:8`-`:17`) e `:20` come `itemname(rtval(1))`, che porta il
conteggio dentro. Il plurale non è un caso raro, è il caso normale.

⚠️ **E il participio è vietato per la ragione opposta.** `:27` dice
「が設置されている。」, «X è installato qui», e «installato» concorderebbe col
**genere** dell'oggetto («la vetrina è installato»). ✅ «Vedi qui una
**costruzione**: X» — nome di genere fisso più due punti, che è la strada della
40ª unita alla forma «Entri qui: X» della 42ª.

⭐ **I sei giudizi sul letto si scrivono con l'impersonale, e l'accordo cade sul
«si».** L'inglese fa «It looks uncomfortable to sleep on», dove il soggetto è il
letto: in italiano «comodo» concorderebbe. ✅ «**Ci si dorme** scomodi», «ci si
riposa discretamente», «ci si dorme benissimo» — l'accordo cade sull'impersonale
(maschile plurale per convenzione) e il letto non c'entra più. È il dativo
riflessivo della 40ª applicato al soggetto invece che all'oggetto.
💡 Lo spazio in testa lo porta l'inglese e serve: le sei frasi si **saldano** a
`bedtxt`, cioè alla riga di `:23`-`:30`, e senza lo spazio si attaccherebbero al
punto. Il giapponese non ne ha bisogno perché non spazia.

⚠️ **rete 3 su 「と」, e la divergenza è voluta.** `text.hsp:11685` lo rende
«, più », ma lì è la ricompensa di una missione — «500 monete d'oro**, più** una
spada» — dove il secondo termine si aggiunge al primo. Qui `:13` congiunge una
**lista di oggetti sulla stessa casella**, e l'unica congiunzione italiana è
« e ». La particella è la stessa, il mestiere no.

⚠️ **`:127`: l'inglese dice «stacks», il giapponese e il CODICE dicono turni.**
La riga stampa `stato + ": " + cdata(...) + lang("ﾀｰﾝ", " stacks ")`, e quel
`cdata` è il contatore dei turni che restano allo stato. ✅ « turni», col
giapponese e col codice contro l'inglese.

⚠️ **`:78`: l'inglese conta i pezzi, il giapponese i TIPI.** 「N種類のアイテム」
è «N tipi di oggetti», e il ramo di sopra (`if stat <= 3`) è quello che li
nomina uno per uno: questo scatta quando sono troppi per elencarli. ✅ Seguito il
giapponese, che qui è anche l'unico dei due a dire la cosa giusta.

⚠️ **Tre rinviate, tutte della rete 6, e nessuna è un buco.** `:115` è
commentata col `;` (il vecchio elenco dei potenziamenti sul bersaglio), `:265` e
`:271` stanno dentro il blocco `ORIGINAL` che il mod ha spento e che si chiude a
`:273`. Sono la coppia gemella di `:160` e `:169`, che invece sono vive e rese.

💡 **« + » è un invariato nuovo**, dichiarato in `invariati.md`: `:282` unisce il
bersaglio e il suo compagno di coppia, il giapponese ci mette il ＋ a larghezza
intera (che CP932 ci vieta comunque) e l'italiano il segno che usa chiunque. È
la stessa specie di `/` e `:` della 41ª — un separatore, non un testo.

💡 **rete 13: «Name» sta per due giapponesi**, 「ルームの名称」 e 「チームの名称」
(`:453` e `:456`). La distinzione la porta già il titolo della finestra due
righe sopra — «Elenco delle stanze» o «Elenco delle squadre» — e la colonna si
chiama «Nome» in tutt'e due i casi, come in inglese.

⭐ **Tre copie da fuori**: `:602` è parola per parola `proc.hsp:20200` («Non c'è
nessun bersaglio in vista.», stesso giapponese), e `:858`/`:993` prendono la
forma di `proc.hsp:3681` («Prendi di mira X.»). ⭐ Il glossario fissa `Target` →
**bersaglio**, «mai obiettivo».
"""
