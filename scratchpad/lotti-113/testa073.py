# -*- coding: utf-8 -*-
"""123a - Lotto 073 di `db_item.hsp`: I POZZI, e la categoria CHIUDE.

`FILTER_FURNITURE_WELL`, righe da `:87574` a `:123936`: **4 righe**, tutte
dell'indice 0, su 4 oggetti (gabinetto, pozzo sacro, fontana, pozzo). Con
questo lotto la categoria va a **0 da fare su 4 vive**, ed e' la
**ventottesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 073`: **+4** per 4 rese,
nessuna gemella. ⓘ `_code.py 073`: 0 righe senza resa in tabella.
`_forma.py 073`: 4 su 4 con lo spazio prima del `\\n`; **3 con lo spazio dopo
il `#` e 1 senza** — quattro righe e **tre titoli diversi**, che e' la densita'
piu' alta vista in un lotto di questa fase. Preflight: 0 guasti, 0 parole
lunghe. `_122-sorelle-per-frase 073`: 0. `_gia-reso 073`: 0 su 4.

### ⚠️⚠️⚠️ «WATER PILLS» NON E' NIENTE

L'inglese di `:90707`, il pozzo sacro:

    JP  もし軽い気持ちで**水薬**を投げようものなら…
    EN  if you throw **water pills** into it lightly…

水薬 e' **pozione**, e sta cosi' nel glossario e in una quarantina di voci del
dizionario. Monte ha tradotto il composto a pezzi — 水 acqua, 薬 medicina — e
ne e' uscita una cosa che nel gioco non esiste. ⭐ E il fatto e' vero e di
gioco: nel pozzo sacro **si gettano le pozioni**, ed e' una meccanica; chi
avesse reso «pillole d'acqua» avrebbe scritto una frase incomprensibile su
un'azione che il giocatore fa davvero.

⭐ E' la quinta fonte della 110a — **il codice del gioco vince quando l'inglese
scioglie un termine in una parola comune** — vista qui nel modo piu' semplice:
non serviva il codice, bastava il glossario, ma solo dopo aver notato che
l'inglese diceva una cosa che non torna.

### ⭐⭐ `:119757` REGGE SU UNA PAROLA CHE IL GIAPPONESE RIPETE APPOSTA

    辺りに**清浄**な音とひんやりとした空間を作り出す避暑設備。
    …お世辞にも**清浄**といえるものではないだろう。

清浄 sta in tutt'e due le frasi, e la battuta e' esattamente li': la fontana fa
un suono *limpido*, e l'acqua *limpida* non e'. Se in italiano le due parole
divergono — «cristallino» e poi «pulita», per dire — il perno salta e la riga
diventa una constatazione qualunque.

⚠️ **Nessuna rete lo vede**, perche' la ripetizione sta **dentro una riga
sola**: `_122-sorelle-per-frase` cerca la frase gemella in **un'altra** riga, e
`_120-serie-bacchette` confronta righe fra loro. Una parola che torna dentro la
stessa stringa e' un caso che gli strumenti di questa fase non coprono, e si
prende leggendo.

### ⓘ Le parole, e da dove vengono

- 設備 -> **«impianto»**, come gli indici 3 di questa stessa categoria
  («Un impianto che usa l'acqua», «Un impianto che raccoglie l'acqua»).
- 聖なる水 -> **«acqua santa»**, come l'indice 3 della stessa voce.
- ノースティリス -> **«Tyris del Nord»** (dizionario e glossario).
- 生命線 non ha una voce, e l'italiano ha **«linfa vitale»**, che e' quel che
  si dice davvero. La traduzione a calco («linea di vita») sarebbe la mano di
  un lettore di palmo.
- 決して汚すことなかれ e' un imperativo **arcaico** (ことなかれ), e la resa lo
  tiene alto: «Guardati dal profanarlo».
- 雨の日にはしばしば燃えている光景を目にする: il giapponese e' impersonale e
  canzonatorio — «capita spesso di vederlo che brucia» — e l'inglese lo
  appiattisce in un passivo.

### ▶ Il conto

Il corpo passa da **1.503 a 1.507 rese su 1.513**, e restano **6 righe** — di
cui una rinviata (`:129299`). Dopo il 073 mancano **quattro** categorie:

    2  FILTER_FURNITURE_ALTAR   1  FILTER_GOLD
    1  FILTER_PLATINUM          1  FILTER_CARGO_FOOD

⚠️ La tabella si rilegge con `_114-corpo-da-fare`, non si eredita da qui.
"""
