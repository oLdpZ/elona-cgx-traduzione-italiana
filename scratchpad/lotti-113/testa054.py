# -*- coding: utf-8 -*-
"""120a - Lotto 054 di `db_item.hsp`: LE ARMI A DISTANZA, e la categoria CHIUDE.

`FILTER_RANGE`, righe da `:96567` a `:127280`: **10 righe**, tutte dell'indice
0, su 10 oggetti. Con questo lotto `FILTER_RANGE` va a **0 da fare su 60
vive**, ed e' la **nona** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 054`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 054`: 0 su 10. `_code.py 054`: 0 righe senza
resa in tabella.

### ⭐⭐⭐ LE DIECI SONO LE ARMI BASE, E PORTANO UNA SCALA DI GIOCO

Non e' un lotto di pezzi unici come il 053: qui ci sono l'arco corto, l'arco
lungo, la balestra, la pistola, il fucile a pompa, la mitragliatrice, la
pistola laser e i sassi — cioe' le armi che ogni giocatore impugna nelle prime
ore, e le cui descrizioni si leggono piu' di ogni altra di questa categoria.

Sei di loro dicono, ciascuna a modo suo, **quanto la forza cali allontanandosi**.
E' un fatto di gioco, non un ornamento, e la scala e' gia' resa **nell'indice
3**, che e' chiuso da sessioni:

    光子銃    pistola laser     殆どない   -> «con la distanza non cala quasi»
    機関銃    mitragliatrice    少ない     -> «con la distanza cala poco»
    拳銃      pistola           減衰する   -> «con la distanza perde forza»
    散弾銃    fucile a pompa    射程が短い -> «porta poco lontano»

⚠️ Il pannello disegna il corpo e l'indice 3 **uno sotto l'altro**: usare qui
un verbo diverso — «diminuire», «scemare», «indebolirsi» — avrebbe spezzato in
due la stessa scala **nella stessa schermata**. Tutte le rese del corpo dicono
**calare**, che e' il verbo dell'indice 3.

⭐ E i due archi chiudono la scala dall'altro capo: 近～中距離 per l'arco corto,
中～遠距離 per il lungo. E' la stessa forma della scala delle navi della 119a —
un gradino per oggetto, che si vede solo mettendo le righe in fila — ma qui il
lavoro non e' stato ricostruirla: e' stato **non romperla**, perche' meta' era
gia' in gioco.

### ⓘ Due punti dove il giapponese sembra contraddirsi e non si contraddice

  - `:96567`, il rail gun: 超重量装置 «apparecchio di peso enorme» e tre righe
    dopo 軽量化に成功している «e' riuscito ad alleggerirsi». Non e' un errore:
    pesa un'enormita' di suo, e **nonostante questo** sono riusciti a
    scaricarne un po' lavorando materiali speciali. Il どちらも che segue sono
    le **due** tecniche — il meccanismo e la lavorazione — ed e' per questo
    che la resa deve dire «tutt'e due»;
  - `:98801`, la balestra: il dizionario rende 機械弓 «balestra», ma il
    giapponese di questa riga parla di 弓, **l'arco**, e ne descrive il
    compromesso (chiunque la usa, ma caricarla costa forza e tempo). La resa
    tiene l'arco, che e' cio' che la riga dice; il nome dell'oggetto resta
    «balestra» dove il nome si legge.

### ⓘ 森の民 e il nome che il giapponese abbrevia

`:117388`, l'arco di Vindale. Il giapponese dice 森の民, «la gente del bosco»;
il nome dell'oggetto e' 異形の森の弓, e 異形の森 il dizionario lo rende **«la
Foresta Eretica»** — l'inglese invece la chiama Vindale, e da li' viene il
nome reso `<Arco di Vindale>`. Le due forme convivono gia' nel gioco
(`_cerca.py` trova tutt'e due), e questa riga non e' il posto per sceglierne
una: la resa dice «la gente della foresta», che regge il legame senza
decidere.
"""
