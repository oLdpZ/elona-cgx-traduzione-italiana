# -*- coding: utf-8 -*-
"""119a - Lotto 050 di `db_item.hsp`: LE POZIONI, il CORPO, e la categoria CHIUDE.

`FILTER_ITEM_POTION`, righe da `:90769` a `:129439`: **41 righe** su 40 oggetti —
40 dell'indice 0 e **1 dell'indice 1**. Con questo lotto `FILTER_ITEM_POTION` va
a **0 da fare su 82 vive**, ed e' la **settima** categoria del corpo che si
chiude, dopo mobilio, attrezzi, cibi, scarti, armi e grimori.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese, nessuna gemella.
`_gia-reso.py 050`: 0 su 41.

### ⚠️⚠️⚠️ `:129299` NON E' UNA FRASE: E' UNO SLOT VUOTO, E VA RESO IDENTICO

L'indice 1 della pozione di confusione ha, in tutt'e due le lingue, lo stesso
contenuto:

    JP  \\t\\t\\n\\n
    EN  \\t\\t\\n\\n

Due tabulazioni e due a capo. Non c'e' niente da tradurre, e `_code.py` lo dice
a modo suo — «righe senza resa in tabella: 1», perche' una coda `#...` non c'e'.

**La decisione**: si rende **identica**. Le altre due strade non stanno in piedi:

  - una resa **vuota** non e' esprimibile — e' la lezione della rinviata di
    `tcg.hsp:2470`, dove `estrai.firme_tradotte` conta come non tradotta ogni
    voce con `it` falso, e per spegnere quella riga ci volle una toppa;
  - **lasciarla fuori** terrebbe `FILTER_ITEM_POTION` a «1 da fare» per sempre,
    cioe' un cancello che non si chiude mai e che nessuno saprebbe piu' leggere.

ⓘ Il precedente vicino e' della 110a — «due righe dell'indice 3 hanno il
giapponese VUOTO... la riga si rende com'e'». Qui e' vuoto **anche l'inglese**,
ed e' il caso limite di quella stessa decisione.

### ⚠️⚠️ L'INGLESE E' ROTTO DUE VOLTE, E LE DUE VOLTE HA RICOPIATO UN'ALTRA RIGA

Il lotto 049 ne aveva trovata una (il te' nero con la frase del te' verde).
Qui ce n'e' un'altra, ed e' la stessa forma di guasto:

    :93069  il liquido ANTIACIDO
      JP   ...飲みすぎた日の強烈な胃酸に対して何ら耐性を得ることはないだろう
           (i succhi gastrici feroci del giorno dopo una bevuta)
      EN   ...the burns that occur when you eat something hot
           (che e' la chiusa del liquido IGNIFUGO, `:81811`, lotto 049)

Le due righe sono gemelle per costruzione — stessa struttura, un liquido che
protegge dal fuoco e uno che protegge dall'acido — e monte ha ricopiato la
chiusa dall'una all'altra senza cambiare l'ultima parola. Il giapponese
distingue, e la resa lo segue.

⭐ **Come si trovano**: non le trova nessuna rete, si vedono solo mettendo le due
righe **una accanto all'altra**, e in questo caso le due righe stanno in due
lotti diversi. E' la stessa forma della famiglia sparsa della 111a.

### ⭐ TRE FAMIGLIE CHE ATTRAVERSANO IL LOTTO

  - **le sette pozioni di cura** (`:126007`-`:126576`) sono una **scala**, e il
    giapponese la scrive con l'ironia crescente: la sacra guaritrice in cima,
    il bastone del goblin sciamano in fondo — «l'efficacia si sa gia' dove
    arriva». Le rese tengono la scala, e non alzano il registro di quelle
    basse;
  - **le due del ripristino** (`:112063` e `:112134`) sono la stessa frase due
    volte, una per la mente e una per il corpo, e cambia solo la battuta
    finale: 格好よかったあの頃 contro スラっとしていたあの頃. Rese in
    parallelo, e nessuna delle due chiede il genere del giocatore;
  - **i quattro liquori** (`:114277`, `:117531`, `:129085`, piu' l'idromele del
    049) portano tutti la coda `~Il Mondo Profondo dei Liquori~`.

### ⓘ I nomi che venivano da altre tabelle, e che il dossier non dava

Cinque termini della prosa sono nomi gia' decisi altrove, e copiarli
dall'inglese li avrebbe sdoppiati:

    スライム        -> **la melma** (non «slime»), e la riga la nomina due volte
    ハウンド        -> **il segugio** (glossario), due volte nella stessa riga
    パラライザー    -> **il paralizzatore**
    パンプキン      -> **la zucca**
    ダイオウサソリ  -> **lo scorpione re** ⚠️ l'inglese scrive «giant scorpion»
    沈黙の霧        -> **Nebbia di silenzio**, l'incantesimo (lotto 048)
    悪夢 / 元素の傷 -> **Incubo** / **Cicatrice elementale** (lotto 048)
    ポート・カプール -> **Porto Kapul** (non «Port Kapul»)

### ⓘ Due cose che il preflight ha fermato prima del dizionario

  - una **lineetta lunga** su `:106108`: CP932 non ce l'ha;
  - due **caporali** su `:126078`: nel dizionario non ce n'e' uno su 25.000
    rese. Il nome dell'oggetto si cita senza virgolette.

E tre parole dentro la finestra di rinculo (`proprietà` per «caratteristiche»,
`tensione` per «agitazione», e la perifrasi al posto di «dell'invisibilità»,
che era da 17): sciolte prima di reimportare invece che dopo.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **cinque**, tutte gia' in tabella (`_code.py 050`: una
sola riga «senza resa», ed e' `:129299`, che una coda non ce l'ha). Il cancello
«titoli resi in PIU' modi» resta a **7**.

⚠️ La forma: **9** righe su 41 hanno lo spazio prima del `\\n` e 32 no; **32**
code hanno lo spazio dopo il `#` e 9 no. E **cinque** righe chiudono con un
`\\n` DOPO la coda: `:92522`, `:93554`, `:114277`, `:117531`, `:129085`.
ⓘ `:114277` porta anche la **tilde larga** nella coda inglese — e' una delle due
che `_112-corpo-descrizioni` conta come «titoli scritti con la tilde LARGA», e
la coda italiana usa quella normale, come vuole la tabella.
"""
