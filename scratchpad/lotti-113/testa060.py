# -*- coding: utf-8 -*-
"""121a - Lotto 060 di `db_item.hsp`: LE ARMATURE, e la categoria CHIUDE.

`FILTER_ARMOR`, righe da `:51640` a `:130779`: **20 righe**, tutte dell'indice
0, su 20 oggetti. Con questo lotto `FILTER_ARMOR` va a **0 da fare su 20 vive**,
ed e' la **quindicesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 060`: **+20** per 20 rese,
nessuna gemella. ⓘ `_gia-reso.py 060`: 0 su 20. `_code.py 060`: 0 righe senza
resa in tabella.

### ⭐⭐⭐ DUE FAMIGLIE ATTRAVERSANO IL LOTTO DI UN'ORA FA

Due righe di questo lotto hanno l'apertura **identica** a due righe del lotto
**058**, gli scudi, chiuso in questa stessa sessione. Cambia un carattere:

    :100717  非常に分厚く作られた盾。  ->  Uno scudo fatto spessissimo.
    :101964  非常に分厚く作られた鎧。  ->  Una corazza fatta spessissima.

    :100849  特殊な素材をかけ合わせてより強固な防護を得た盾。
    :101769  特殊な素材をかけ合わせてより強固な防護を得た鎧。
             ->  «Uno scudo / Una corazza che, incrociando materiali
                 speciali, ha ottenuto una protezione piu' solida.»

⚠️ **`_gia-reso.py` dice 0 su 20 e ha ragione**: cerca la prosa **intera**, e
queste due stringhe differiscono. **`_120-serie-bacchette.py` dice «nessuna
serie» e ha ragione**: guarda dentro il lotto, e la sorella sta fuori. E
`_coerenza` non le vede per lo stesso motivo. E' il «sesto posto dove guardare»
della 111a — *le altre righe della stessa famiglia, anche se stanno in un altro
lotto* — e qui l'altro lotto e' quello di un'ora fa.
💡 La forma del guasto e' quella del 014 contro il 024: un lotto rende in un
modo, il lotto dopo lo disfa senza saperlo. Qui non e' successo solo perche' le
rese del 058 erano ancora sotto gli occhi. **Su una macchina che riprende
domani non lo sarebbero**, e nessuno strumento lo direbbe.

### ⭐⭐⭐ DUE ARMATURE CHE SI NOMINANO A VICENDA, E L'INGLESE SLEGA IL NODO

`:101574` (軽鎧, la corazza leggera) e `:101964` (厚鎧, la corazza a bande)
chiudono con la stessa frase, e ciascuna **nomina l'altra**:

    :101574   厚鎧とどちらを取るかは冒険者の好みと言ったところだろう。
    :101964   軽鎧とどちらを取るかは冒険者の好みと言ったところだろう。

Sono due nomi di oggetto — due oggetti che il giocatore ha nell'inventario — e
la riga gli sta dicendo *questo o quello, scegli*. L'inglese perde tutt'e due
i nomi e scrive «standard thick armor» e «lighter armor»: chi rende
dall'inglese non manda il lettore da nessuna parte.

⭐ Le due rese usano i nomi veri — «corazza a bande» e «corazza leggera» — e per
il resto sono **identiche parola per parola**, perche' identiche sono in
giapponese.

### ⭐ ALTRE DUE COPPIE, PIU' PICCOLE

  - `:101379` e `:101509`: 服の中に**多数の**素材片を埋め込み… contro
    服の中に素材片を埋め込み… — il giubbotto antiproiettile e il cappotto,
    e a distinguerli e' **多数の**. Le due rese cambiano «molti» e nient'altro.
    ⓘ Qui l'inglese la differenza la tiene («numerous pieces» / «pieces»): non
    tutte le righe gemelle sono un guasto di monte, e questa non lo e';
  - `:70463` e `:70530`: バリアコーティング — il trattamento **fallito** sul
    costume da bagno pericoloso e quello riuscito sulla tuta da guerra. Il
    termine non e' nel dizionario, **nasce qui**, e nasce gia' in tre righe
    (c'e' anche `:77561`): «rivestimento a barriera» in tutt'e tre. Deciderlo
    su una riga sola e ritrovarsi le altre due dopo sarebbe stato il modo di
    scriverne tre versioni.

### ⓘ 防具 e 鎧 stanno nello stesso lotto, e restano due parole

Il glossario della 111a le tiene distinte — 防具 «armatura», 鎧 «corazza» — e
questo lotto le mette a contatto: `:101639` dice che la veste papale «e'
un'**armatura** che pesa un po' di piu', ma sempre meno di una **corazza**».
⚠️ E `:101639` nomina 法衣 **due volte**, che e' il nome di un altro oggetto di
questo stesso lotto (`:130714`, «veste»): tenere la parola rende leggibile il
paragone — la veste papale e' piu' solida della veste.
⭐ Stessa cosa in `:101899`: 鎖帷子 e' la maglia di ferro, e in gioco quel
pezzo si chiama «cotta di maglia» (`:101704`, poche righe sopra). Dirlo col suo
nome dice al giocatore di che cosa e' fatta la corazza a piastre.

### ⓘ Tre punti dove l'inglese legge a modo suo

  - `:75983`, il vincolo del dio delle macchine: 脱いだらスゴイことになる — *a
    toglierselo succedono cose grosse*. L'inglese scrive «It looks cool when
    taken off»: il giapponese non dice bello, dice grosso;
  - `:51640`, il 《世界制服》: 世界征服 «la conquista del mondo» e 制服
    «l'uniforme» si leggono uguali, ed e' il bisticcio del nome. In italiano il
    bisticcio non c'e', ma le due parole restano tutt'e due nella riga, vicine,
    dove il lettore le vede;
  - `:65809`, l'《Argent Snow》: メイルーン e' **Mayroon**, il paese
    dell'incarico del demone, e non un nome da traslitterare a orecchio.
"""
