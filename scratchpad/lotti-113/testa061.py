# -*- coding: utf-8 -*-
"""122a - Lotto 061 di `db_item.hsp`: LE MERCI DA COMMERCIO, e la categoria CHIUDE.

`FILTER_CARGO_TRADE`, righe da `:56267` a `:104375`: **19 righe**, tutte
dell'indice 0, su 19 oggetti. Con questo lotto `FILTER_CARGO_TRADE` va a **0 da
fare su 19 vive**, ed e' la **sedicesima** categoria del corpo che si chiude —
e la prima da otto lotti che non e' un pezzo d'equipaggiamento.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 061`: **+19** per 19 rese,
nessuna gemella. ⓘ `_gia-reso.py 061`: 0 su 19. `_code.py 061`: 0 righe senza
resa in tabella. `_forma.py 061`: 19 su 19 con lo spazio prima del `\\n`, 19 su
19 con lo spazio dopo il `#`.

### ⭐⭐⭐ L'INGLESE DI `:56267` E' QUELLO DELL'OGGETTO DOPO, PAROLA PER PAROLA

E' la cosa piu' riusabile del lotto, e la piu' scomoda.

    db_item.hsp:56261  (jp)  実際に噴火の現場で描かれたという…版画。  <- il dipinto
    db_item.hsp:56267  (en)  In some parts of Gaius Vis, a rabbit's foot…  <- il CONIGLIO
    db_item.hsp:56333  (en)  In some parts of Gaius Vis, a rabbit's foot…  <- il coniglio

Le due stringhe inglesi sono **identiche**, e quella giusta e' la seconda:
`ITEM_ID_PAINTING_ERUPTION` ha preso l'inglese di `ITEM_ID_RABBIT_FOOT`, che nel
sorgente e' l'oggetto **immediatamente successivo**. Il giapponese e' a posto, e
anche la `description(3)` inglese della stessa voce («It is a cargo of
painting.»): monte ha sbagliato **una riga sola**.

⭐ **LA RETE 13 DEL LOTTO L'HA VISTA**, e va detto perche' e' il suo merito:
«l'inglese "In some parts of Gaius Vis…" sta per 2 giapponesi diversi: guarda
se la distinzione va tenuta». Le due righe stanno tutt'e due in questo lotto, e
li' la rete arriva.

⚠️⚠️⚠️ **MA LA STESSA DOMANDA SU TUTTO IL FILE NON LA FA NESSUNO.** E' il
difetto della 103a e della 104a — «l'inglese di monte slitta di una carta» — e
`_103-inglese-ripetuto.py` e `_104-inglese-slittato.py` lo cercano davvero, ma
leggono **solo** `db_card.hsp`: e' scritto nella prima riga di tutt'e due
(`FILE = 'db_card.hsp'`). Su `db_item.hsp` la rete esiste **solo dentro il
lotto**: se `:56267` e `:56333` fossero caduti in due lotti diversi — e sono
due categorie vicine, non la stessa — nessuno avrebbe detto niente. E le 1.374
rese del corpo gia' scritte non sono mai state misurate contro questa domanda.
💡 Lo strumento e' la cosa da costruire subito dopo questo lotto, e il
denominatore e' **tutto il file**, non il lotto: *due `description` inglesi
identiche (o quasi) con giapponesi diversi*. E' lo stesso allargamento che la
121a chiedeva per `_120-serie-bacchette`, dall'altro lato. Se ne esistono altre,
ogni resa presa dall'inglese su quelle righe descrive **l'oggetto sbagliato**, e
nessun cancello se ne accorgerebbe — la riga e' pulita in ogni senso
misurabile, esattamente come 神の間 della 121a.

ⓘ Qui il danno non c'e' stato perche' la resa viene dal giapponese, che e' la
regola del progetto; ma la regola vale finche' qualcuno legge il giapponese, e
una riga dove il giapponese manca (il caso `:89358` della 121a) si renderebbe
dall'inglese **sbagliato** senza nessun segnale.

### ⭐⭐ LA SERIE C'E' ANCHE QUANDO GLI STRUMENTI DICONO CHE NON C'E'

`_120-serie-bacchette 061` dice «nessun giapponese ripetuto» e «0 aggettivi che
distinguono», e ha ragione su quel che misura. Ma la categoria e' **una formula
sola** ripetuta:

    undici righe su diciannove aprono con  ◯な交易品。   (una merce da commercio ◯)
    cinque di quelle undici chiudono con   使用することはできない。

Le rese tengono la stessa impalcatura — la merce apre la frase, il divieto si
rende sempre «Non si può usare: <ragione>» — perche' il giocatore che ne legge
cinque di fila deve riconoscere la regola e leggere solo la parte che cambia.
⚠️ `_120-serie-bacchette` raggruppa per **prosa intera**: una formula con dentro
un aggettivo diverso ogni volta gli e' invisibile. E' lo stesso buco della riga
sorella fuori dal lotto, dall'altro lato.

### ⭐⭐ DUE PESCI TROPPO GROSSI, E DUE GRADI DI VALORE CHE NON VANNO APPIATTITI

La coppia sorella **dentro** il lotto:

    :103913  個人で食すには余りにも巨大なツナ。主に交易品として取引される。
    :104045  個人で食すには余りにも巨大なマンボー。主に交易品として取引される。

Giapponese identico tranne il nome del pesce, e le due rese lo sono di
proposito: «Un tonno / Un pesce luna decisamente troppo grosso perché una
persona sola se lo mangi.»

⚠️ E il rovescio, che e' la lezione della 119a: due righe della famiglia del
divieto d'uso dicono due cose **diverse** e vanno tenute distinte.

    :103847 (il whisky)   開封すると価値が大幅に落ちる  ->  il valore CROLLA
    :104375 (la bambola)  開封してしまうと価値が下がる  ->  il valore CALA

### ⓘ Le decisioni minori, e da dove vengono

  - 交易品 -> «merce da commercio», glossario della 111a, e gia' in gioco
    sull'indice 3 di tutta la categoria («Merce da commercio.»);
  - la scala del peso si tiene distinta come sull'indice 3: 重い e'
    «pesante», とても重い e' «molto pesante» (`:91026`, `:103979`, `:104243`);
  - 版画 e' la **stampa**, non il dipinto, e il progetto la rende gia' cosi'
    nel quadro di Ehekatl, in questo stesso file. Il NOME dell'oggetto resta
    «dipinto dell'eruzione»: la descrizione non lo contraddice, lo specifica;
  - i nomi di luogo vengono tutti dal dizionario: ガイアス・ヴィス «Gaius Vis»,
    サウスティリス «Tyris del Sud», イェルス軍 «l'esercito di Yerles»,
    ノイエル «Noyel», エウダーナ «Eulderna», イムウエル «Aimwell»;
  - マンボー «pesce luna» e 浮き輪 «salvagente» sono gia' nel dizionario come
    nomi di oggetto: la descrizione usa la parola che il giocatore legge
    nell'inventario;
  - `:103979` (la tomba) ripete la parola «tomba» come fa il giapponese —
    墓運びが墓に埋もれる — perche' la battuta sta nella ripetizione;
  - `:104111` (la bara) tiene la battuta nera di 先約がいる: «c'è già chi
    l'ha prenotata».
"""
