# -*- coding: utf-8 -*-
"""123a - Lotto 070 di `db_item.hsp`: I RESTI, e la categoria CHIUDE.

`FILTER_REMAINS`, righe da `:97263` a `:108767`: **7 righe**, tutte dell'indice
0, su 7 oggetti. Con questo lotto `FILTER_REMAINS` va a **0 da fare su 7 vive**,
ed e' la **venticinquesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 070`: **+7** per 7 rese,
nessuna gemella. ⓘ `_code.py 070`: 0 righe senza resa in tabella.
`_119-togli-rinviate 070`: nessuna rinviata. `_gia-reso 070`: 0 su 7.
`_120-serie-bacchette 070`: nessuna riga col giapponese identico.

### ⭐⭐⭐ IL CASO PIU' FORTE DELL'INGLESE CHE APPIATTISCE

E' quello che la 122a aveva visto e lasciato in eredita', ed e' l'ottavo posto
dove guardare (119a: la riga gemella per costruzione) nella sua forma piu'
netta. Cinque righe in fila, cinque volte la stessa frase inglese:

    «It is not particularly valuable, but can be used for medicine and
     sorcery, so it can be sold for a modest price.»

Il giapponese dice **quattro cose diverse**, con **due verbi diversi**:

    :108519  骨片  osso    水薬や呪術に**使用**できる     pozioni, stregoneria
    :108581  心臓  cuore   水薬や呪術に**使用**できる     pozioni, stregoneria
    :108643  瞳    occhio  装飾品や薬に**加工**できる     ornamenti, medicine
    :108705  体液  sangue  水薬等に**加工**できる         pozioni e simili
    :108767  皮    pelle   服や鞄に**加工**できる         vestiti, borse

⭐ **使用 contro 加工.** 使用できる e' «si usa»: la cosa entra intera in un
procedimento. 加工できる e' «si lavora»: la cosa e' materia prima che diventa
altro. Il giapponese sceglie, e sceglie «usare» due volte e «lavorare» tre.
L'inglese scrive «be used» cinque volte su cinque, e per tre righe su cinque
dice il verbo sbagliato.

⚠️ **Sono quattro frasi su cinque righe, non cinque.** Osso e cuore hanno il
giapponese **identico** in quella frase, e le due rese lo tengono identico. Chi
avesse letto «cinque usi diversi» e cercato cinque rese diverse avrebbe
introdotto una divergenza che il giapponese non ha.

### ⭐⭐ LE SORELLE GIA' RESE STANNO FUORI DAL LOTTO, SOTTO LO STESSO TITOLO

`_122-sorelle-per-frase 070` dice **32 frasi con una sorella, 0 gia' rese**:
tutte e trentadue stanno dentro il lotto, ed e' la famiglia piu' chiusa vista
finora. Ma le parole che servivano stavano gia' nel dizionario, in tre righe che
la rete **non** poteva accostare perche' la frase e' diversa — e che portano lo
stesso titolo, `#~Le Mille Cianfrusaglie che Amo~`:

    :116408  ITEM_ID_ANIMAL_BONE    風化した動物の骨。呪術や水薬精製など…
    :127669  ITEM_ID_SKELETON       風化した人間の骨。呪術や水薬精製など…
    :127731  ITEM_ID_BONE_FRAGMENT  風化した何かの骨。呪術や水薬精製など…

    IT  «…dalla stregoneria al distillare pozioni…»

Da li' si ricopiano le due parole: 呪術 -> **stregoneria**, 水薬 -> **pozioni**.
⭐ E' il settimo posto (113a: il giapponese di cio' che stai per scrivere puo'
essere gia' reso altrove) trovato **per titolo** invece che per frase: le tre
ossa sbiancate dal tempo sono lo stesso libro immaginario, e chi lo scrive usa
le sue parole.
⚠️ 薬 nudo (l'occhio) NON e' 水薬: resta «medicine», non «pozioni». Il
giapponese ha due parole e il dizionario le tiene due — `potion` -> pozione sta
nel glossario.

### ⭐⭐ LA TESTA E LA CODA SI TENGONO IDENTICHE, IN FORMA IMPERSONALE

Quattro righe su cinque aprono con 敵を破砕した際に飛び散った生物の…, che non
ha soggetto. In italiano i soggetti sarebbero quattro e diversi — «schegge»,
«il cuore», «l'occhio», «lembi di pelle» — e la frase condivisa si sarebbe
spezzata in quattro. 💡 **«schizzat* via nel frantumare un nemico»**: il
gerundio regge tutti e quattro senza cambiare una lettera oltre l'accordo.
E' lo stesso rimedio del 069, dove la coppia 靴/履物 aveva costretto a
«c'è poco da fidarsi».

Lo stesso vale per la coda, condivisa da tutte e cinque: «Gran valore non ne
ha/hanno, ma … e così si vende/vendono a un prezzo discreto».

⚠️ **Il rovescio, e c'e' anche qui.** `:108705` NON dice 敵を破砕した際に: dice
飛び散った生物の体液を集めたもの — il sangue si **raccoglie** invece di
schizzare via, e l'inglese ci mette pure «scattered» al posto di «shattered».
La resa lo segue e non uniforma: «schizzato via e raccolto».

### ⓘ IL NOME CHE IL GIOCATORE LEGGE IN CIMA AL PANNELLO VINCE

体液 e' «fluido corporeo», ma il NOME dell'oggetto nel dizionario e' **sangue**,
e l'indice 3 dice gia' «Il sangue di una creatura». La resa dice sangue.
E' la regola del 069 (gli stivali contro le scarpe), applicata al contrario:
li' il nome era piu' specifico del giapponese, qui e' meno.

⚠️ **Ma non vale meccanicamente.** `:97325` ha il nome «statuetta» (はく製,
tassidermia) e il giapponese del corpo dice 像, «statua»: li' la resa segue il
**giapponese della riga**, perche' il giapponese ha cambiato parola apposta.
Il nome vince quando la riga usa la stessa parola del nome, non quando ne usa
un'altra.

### ⚠️⚠️ IL PREFLIGHT HA PRESO UN GUASTO CHE `_forma.py` NON VEDE

`_forma.py 070` dice «7 righe su 7 con lo spazio prima del `\\n`»: e' un SI/NO.
L'inglese di `:97263` ne ha **due**, di spazi, e la prima stesura ne aveva messo
uno. Il preflight lo ha stampato — «en '  ', it ' '» — e il lotto e' ripartito
da li'.

⭐ **Un referto booleano non dice il margine.** E' la stessa lezione della 107a
sulla prova al contrario che stampa il punto in cui si accende invece di un ✅,
e qui il margine era **un byte**. `_forma.py` non e' sbagliato: risponde a
un'altra domanda, e la sua risposta verde non copre quella del preflight.

### ⓘ E DUE PEZZI DA COLLEZIONE, CHE NON C'ENTRANO CON I RESTI

`FILTER_REMAINS` tiene dentro anche la carta (`:97263`) e la statuetta
(`:97325`), che stanno sotto `# ~Catalogo d'Arte di Lumiest~` e sono gli unici
due del lotto con lo spazio dopo il `#`.

- 紙片 e' «foglietto» e non «foglio»: l'indice 3 della stessa voce dice 紙 nudo,
  ed e' li' che sta «Un foglio con i dati di una creatura». Due parole in
  giapponese, due in italiano, dentro lo stesso pannello.
- 遊戯用 e' il gioco di carte — デッキ e' gia' «mazzo» nel dizionario, ventitre
  voci — quindi «da gioco», non «da giocattolo».
- 生き写し e' il modo di dire italiano «il ritratto vivente», che si dice
  esattamente cosi'. ⚠️ 犠牲者 e' singolare in giapponese e l'inglese lo mette
  al plurale insieme al soggetto: vince il giapponese, una statua una vittima.

### ▶ Il conto

Il corpo passa da **1.485 a 1.492 rese su 1.513**, e restano **21 righe** — di
cui una rinviata (`:129299`). Dopo il 070 mancano **sette** categorie:

    6  FILTER_ENVIRONMENT_SEABED     2  FILTER_FURNITURE_ALTAR
    5  FILTER_AMMO                   1  FILTER_PLATINUM
    4  FILTER_FURNITURE_WELL         1  FILTER_GOLD
                                     1  FILTER_CARGO_FOOD

⚠️ La tabella si rilegge con `_114-corpo-da-fare`, non si eredita da qui.
"""
