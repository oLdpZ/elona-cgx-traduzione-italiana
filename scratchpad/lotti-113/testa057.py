# -*- coding: utf-8 -*-
"""120a - Lotto 057 di `db_item.hsp`: I CONTENITORI, e la categoria CHIUDE.

`FILTER_CONTAINER`, righe da `:57125` a `:115260`: **25 righe** — 22
dell'indice 0 e 3 dell'indice 2 — su 22 oggetti. Con questo lotto
`FILTER_CONTAINER` va a **0 da fare su 25 vive**, ed e' la **dodicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 057`: **+25** per 25 rese,
nessuna gemella. ⓘ `_gia-reso.py 057`: 0 su 25. `_code.py 057`: 0 righe senza
resa in tabella.

### ⓘ QUI SERIE NON CE NE SONO, E A DIRLO E' STATO UNO STRUMENTO

`_120-serie-bacchette.py 057` — lo strumento nato per il lotto delle bacchette
— ha risposto in un secondo: **25 righe, 24 aperture distinte, nessuna coppia
col giapponese identico**. Vale la pena scriverlo perche' e' il **valore
atteso** di quello strumento: un lotto normale non ha serie, e saperlo in un
secondo evita di cercarle a mano per venti minuti.

⭐ L'unica coppia e' `:103233` / `:103295`, le due sfere del tesoro: stessa
frase, e cambia il nome della speranza che ci sta dentro — 「欲望」 la **brama**
nella sfera rara, 「期待」 l'**attesa** in quella normale. Le due rese cambiano
quella parola e nient'altro.

### ⚠️⚠️ OTTO CODE SU VENTICINQUE LE AVEVO SCRITTE A MEMORIA, E OTTO ERANO SBAGLIATE

Scrivendo le rese ho ricostruito i titoli-fonte **a senso** dal giapponese,
invece di copiarli dall'uscita di `_code.py`. Tutti e otto erano plausibili e
tutti e otto diversi da quelli in tabella:

    «Alla Faccia della Chiusura! Box Mania, Numero Primo»
                              -> «Chiudeteci Pure! Box Mania, Numero Uno»
    «Manuale dei Giochi: Edizione per Tutte le Età»
                              -> «Grande Compendio dei Giochi: Per Tutte le Età»
    «Cose Belle da Ricevere in Regalo» -> «Regali che Fa Piacere Ricevere»
    «Libro da Donare a Chi Sta per Morire» -> «Libro in Dono a Chi Sta Morendo»
    «I Cinquanta Articoli Più Amati dai Carcerati»
                              -> «I 50 Prodotti Preferiti dai Detenuti»
    … e altre tre.

⚠️ **Il preflight non le prende**: guarda la spaziatura e la struttura, non il
testo del titolo. A prenderle sarebbe stato `_112-corpo-descrizioni`, il cui
«titoli resi in PIU' modi» sarebbe salito da 7 a **15** — ma solo *dopo* il
reimporta, cioe' dopo aver messo nel dizionario quindici titoli doppi.

⭐ **`_code.py` esiste esattamente per non farlo, e io non l'ho letto.** La
regola non e' «stare piu' attento»: e' che i titoli si **copiano** dall'uscita
dello strumento, come le righe si copiano dal template. Un titolo somiglia
abbastanza al giusto da non insospettire chi lo rilegge.

### ⓘ Tre punti dove l'inglese e il giapponese non dicono la stessa cosa

  - `:57127`, la lettera nella busta misteriosa. はく製 nel dizionario e' la
    **statuetta** — l'oggetto che il giocatore raccoglie ed espone — e ユニーク
    sono le creature **uniche** del gioco: la lettera ringrazia per una
    collezione di statuette di personaggi unici aperta al pubblico. L'inglese
    scrive «fossils», che non e' ne' l'una ne' l'altra cosa;
  - `:78658`, il pacchetto di carte. Il giapponese dice **una** cosa (le carte
    dentro non mostrano l'immagine finche' non le metti nel mazzo); l'inglese
    ci **aggiunge** «Pack of 5 collectible cards», che nell'indice 0 non c'e'.
    Il conto delle cinque sta nell'indice 3, gia' reso: dirlo due volte lo
    farebbe leggere due volte nello stesso pannello;
  - `:115260`, le parole del guardiano della gilda dei ladri. マスター e' **il
    maestro** della gilda, un personaggio del gioco; l'inglese scrive «a
    gentleman» e la battuta perde la persona — la prima volta che il guardiano
    si e' stupito e' stato per il **proprio capo**.
  - ⓘ E `:107114`: il giapponese dice che la magia della borsa mette addosso
    不安, **inquietudine**; l'inglese dice «guilty», colpa. Sono due cose
    diverse, e la resa segue il giapponese.

### ⓘ Un nome che l'inglese perde e che la tabella aveva gia' recuperato

`:112196`, il portafoglio: chi parla e' ならずもののオネスト, «**Onest** il
farabutto», e il nome **e'** la battuta — uno che si chiama Onesto e raccoglie
portafogli altrui. L'inglese lo cancella e ci mette un punto interrogativo
(«words of the honest? rogue»). La tabella dei titoli lo aveva gia' ripescato
in una sessione passata, e la resa ci si appoggia.
"""
