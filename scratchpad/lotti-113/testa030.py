# -*- coding: utf-8 -*-
"""114a - Lotto 030 di `db_item.hsp`: IL MOBILIO, quarta parte.

`FILTER_FURNITURE`, righe 108.000-113.000: **53 righe** su 51 oggetti — 51
dell'indice 0 e due dell'indice 2 (`:110801` e `:112509`). E' il primo lotto
del tratto **alto** del file: dopo il 029 il mobilio che resta sta tutto sopra
la riga 108.000, e questo ne prende la prima meta'.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **I sette giacigli** (`:109526` soffice, `:109903` dozzinale, `:110478`
  pulito, `:110669` accogliente, `:110865` misero, `:110931` gigante,
  `:111324` di lusso) piu' la **bara** (`:110799`), che il giapponese chiama
  寝具 come gli altri sette: e' un giaciglio anche lei, e la battuta di <Ainc>
  che segue gioca proprio su questo. Tutte e otto le rese aprono con
  «Un giaciglio», che e' la parola che tiene insieme la famiglia.
- **I sette scaffali e le due toelette**: `:109460` e `:109713` dicono la
  **stessa formula** — 機能美を究極/極端までに追求した, «insegue fino in
  fondo / all'estremo la bellezza dell'utile» — uno di uno scaffale e una di
  una toeletta. Le due rese si rispondono.
- **I quattro tavoli da gioco** (`:110155` freccette, `:110220` slot,
  `:110285` casino', `:110350` pachislot): tutti e quattro 遊技台, «tavolo da
  gioco», e ciascuno apre con quella parola.
- **I due scaffali gemelli** (`:111573` i ninnoli, `:111635` i casalinghi): la
  **seconda frase giapponese e' identica parola per parola**. La resa della
  seconda frase e' identica nelle due righe, e per riuscirci il soggetto e'
  «il mucchio» — un soggetto che va bene sia per i ninnoli (maschile plurale)
  sia per la roba (femminile singolare).

### ⭐⭐⭐ L'INGLESE SBAGLIA TRE VOLTE, E DUE SONO ROVESCIAMENTI

1. **`:109083`, il tavolo — l'inglese e' la COPIA di quello del trono.**
   `:108954` (il trono) e `:109083` (il tavolo) hanno **lo stesso identico
   inglese**: «A magnificent chair made only for the king to sit on...». Il
   giapponese del tavolo dice tutt'altro — 物が載せられているテーブル。
   大きさからするとテーブルというより机といった方が正しいだろう, un tavolo con
   sopra della roba, e a giudicare dalla grandezza sarebbe piu' giusto
   chiamarlo scrivania. E' la forma che `_104-inglese-slittato.py` cerca sulle
   carte, e qui si e' vista **leggendo il dossier**, perche' le due righe
   stanno a 129 righe di distanza e nessuna rete di lotto le confronta.
2. **`:109335`, il pianoforte verticale — l'inglese perde la negazione.**
   長旅には適さないだろう: per un viaggio lungo **non** va bene. L'inglese
   scrive «still heavy enough to be suitable for long trips», che dice il
   contrario.
3. **`:109903`, il letto dozzinale — l'inglese rovescia la frase.**
   余り疲れは取れないだろう: la **stanchezza non se ne va** granche'. L'inglese
   scrive «you will probably not get very fatigued», cioe' che non ci si
   stanca. E' l'opposto del punto del testo, che e' un letto che non riposa.

⚠️ E un'aggiunta e un taglio piu' piccoli: `:110220` (la slot) **butta via la
prima frase** 絵柄を揃えて楽しむ遊技台 e sbaglia la seconda — ７が揃った vuole
i sette **tutti e tre** allineati, mentre l'inglese scrive «when a seven
appears in any of the three frames». `:112382` (il salvagente) **aggiunge**
delle piscine che il giapponese non ha.

### ⭐⭐ `:112509` NON HA GIAPPONESE AFFATTO

E' l'appunto sulla tinozza — `\\"Not suitable for golems\\"` — e nel dossier il
campo `JP` e' **vuoto**: e' un'aggiunta del CGX. Delle cinque fonti della 110a
qui ne resta **una sola**, l'inglese, e la resa si scrive da li'.

### ⭐ I TERMINI CERCATI A MANO

    ポート・カプール -> Porto Kapul          (`chat.hsp`, gia' nel dizionario)
    白き癒し手       -> la bianca guaritrice (癒し手 -> «guaritrice»)
    大地の神         -> il dio della terra   (Opatos, `db_item.hsp` e `book`)
    ゴーレム         -> il golem             (`db_creature.hsp`)
    ブラックジャック -> blackjack            (`chat.hsp`, invariato)
    パルミア         -> Palmia               (`invariati.md:41`)

### ⭐ LE TRE FORME DELLA MARCA, e perche' `#~ ` perde lo spazio

L'inglese scrive la riga-fonte in **tre** modi: `# ~Titolo~` (118 righe),
`#~Titolo~` (43) e `#~ Titolo~` (7), con uno spazio **dentro** il titolo. Il
dizionario rende il terzo caso come il secondo, `#~Titolo~`, e lo fa **7 volte
su 7** da sessioni precedenti: `lotti-113/_code.py` fa lo stesso, e va bene
cosi'. Il motivo non e' l'imitazione ma il cancello: `_112-corpo-descrizioni.py`
conta i **titoli resi in piu' modi**, e mescolare `#~ Grande Enciclopedia~` con
`#~Grande Enciclopedia~` lo accenderebbe.

⚠️ Un'altra forma invece **si conserva**: `:111511` e' l'unica riga del lotto
in cui l'inglese non mette lo spazio prima del `\\n`.
"""
