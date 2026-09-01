# -*- coding: utf-8 -*-
"""123a - Lotto 077 di `db_item.hsp`: IL CIBO DA VIAGGIO — e il CORPO CHIUDE.

`FILTER_CARGO_FOOD`, `:109020`: **1 riga**, indice 0, 1 oggetto. La categoria
va a **0 da fare su 1 viva**, ed e' la **trentaduesima** categoria del corpo
che si chiude.

⭐⭐⭐ **Ed e' l'ultima riga vera del corpo di `db_item.hsp`.** Dopo questa
restano **1.513 su 1.513** rese sugli indici 0-2, meno l'unica **rinviata**
(`:129299`, che non ha un testo in nessuna delle due lingue e quindi non e'
lavoro). Il corpo del file piu' grande del progetto si chiude qui.

⚠️⚠️ Previsione di `applica`: **+1**, nessuna gemella. `_forma.py 077`: 1 su 1
con lo spazio prima del `\\n`, 1 su 1 con lo spazio dopo il `#`. Preflight: 0
guasti. `_gia-reso 077`: 0 su 1.

### ⭐⭐ LA SORELLA E' L'INDICE 3 DI QUESTO STESSO OGGETTO, ED E' GIA' RESA

`_122-sorelle-per-frase 077` la trova a **0.89**, e la marca **GIA' RESA**:

    qui  荷車に積み込むタイプの食糧      (indice 0, da rendere)
    la   荷車に積み込むタイプの食物だ    (indice 3, gia' reso, :109023)
    IT   «Un cibo del tipo che si carica sul carretto.»

La resa la ricopia **parola per parola**, e il pannello si apre due volte con
la stessa immagine — che e' esattamente quel che fa il giapponese, cambiando
solo 糧 in 物だ.

⭐ E' la rete della 122a che fa il suo mestiere sull'ultima riga del corpo: la
frase da ricopiare stava a tre righe di distanza, ma in un **indice diverso**,
e senza lo strumento si trovava solo per fortuna.

### ⓘ Le parole, e da dove vengono

- 保存性が極めて高い -> **«si conserva benissimo»**. «Si conserva a lungo» sta
  gia' nel dizionario su tre alimenti (il formaggio, lo yogurt, la razione del
  soldato); qui il giapponese ha 極めて, quindi il grado sale.
- 質より量 e' il modo di dire, e l'italiano ce l'ha uguale: **«quantita' piu'
  che qualita'»**.
- 凌駕する -> **«contare piu' di»**: e' la quantita' che ha la meglio sul
  sapore, ed e' la battuta della riga.
- セットになっている -> «nella dotazione c'e' anche», che e' quel che il gioco
  intende: il carico comprende da bere.

### ▶ Il conto, e la fine del corpo

Il corpo passa da **1.511 a 1.512 rese su 1.513**, e resta **1 riga**, che e'
la rinviata `:129299`. `_114-corpo-da-fare` deve dire **TOTALE da fare 1 su
1.449 vive, di cui rinviate 1**, cioe' **zero lavoro**.

⚠️ Il numero si rilegge con lo strumento, non si eredita da qui — e va
riletto **dopo** `reimporta`, non prima.
"""
