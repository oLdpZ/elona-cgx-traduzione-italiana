# -*- coding: utf-8 -*-
"""122a - Lotto 062 di `db_item.hsp`: GLI ALBERI, e la categoria CHIUDE.

`FILTER_ENVIRONMENT`, righe da `:68450` a `:95920`: **13 righe** — 12
dell'indice 0 e **una dell'indice 2** (`:95672`, la battuta di <Barius>) — su
11 oggetti. Con questo lotto `FILTER_ENVIRONMENT` va a **0 da fare su 13 vive**,
ed e' la **diciassettesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 062`: **+13** per 13 rese,
nessuna gemella. ⓘ `_gia-reso.py 062`: 0 su 13. `_code.py 062`: 0 righe senza
resa in tabella. `_forma.py 062`: 13 su 13 con lo spazio prima del `\\n`.

### ⭐⭐⭐ LA RETE NUOVA ARRIVA PRIMA DEL DANNO, E QUESTO E' IL PUNTO

Il lotto 061 aveva scoperto per fortuna che l'inglese di `:56267` era quello
dell'oggetto successivo, e la fortuna era che le due righe fossero cadute nello
stesso lotto. Da li' e' nato `scratchpad/_122-inglese-doppio-item.py`, che fa la
stessa domanda su **tutto `db_item.hsp`** invece che dentro un lotto. Fra i
dieci gruppi che ha trovato, uno solo riguardava righe **non ancora tradotte**:

    :91522  (モミ, l'abete)  実を落とさない常緑樹。…ノイエルで祭りが行われる
    :95858  (スギ, il cedro) 実を落とさない常緑樹。…この木の花粉だった

    en (tutt'e due)  «…festivals are held in Noyel to celebrate the Saint by
                       decorating these trees with various ornaments.»

Il giapponese del cedro non parla di feste: parla del **polline**, e della
battuta di chi crede che qualcuno gli stia intralciando gli incantesimi e
scopre che era l'albero. Tradotto dall'inglese, il cedro avrebbe portato la
festa di Noyel dell'abete, e **nessun cancello lo avrebbe visto**: la riga
sarebbe stata pulita in ogni senso misurabile.

⭐ E' la differenza fra una rete che spiega un difetto vecchio e una che ne
impedisce uno nuovo. Il conto della rete: **10 gruppi, 27 righe, 25 gia' rese**
— e tutte e 25 sono salve, perche' il progetto rende dal giapponese. Le due che
non lo erano sono queste.

### ⭐⭐ LA COPPIA CHE CAMBIA UNA PAROLA SOLA, E STAVOLTA E' L'INGLESE AD AVER RAGIONE

    :95484  (トネリコ, il frassino)  実を落とさない落葉樹。**非常に硬く**、…
    :95608  (ケヤキ, la zelkova)     実を落とさない落葉樹。**非常に良質で**、…

Il resto della frase e' identico. Qui l'inglese le distingue davvero («very
hard» / «very high quality»), quindi il rischio di appiattirle e' **nostro**:
le due rese sono identiche tranne quella parola — «È durissimo» contro «È di
ottima qualità» — esattamente come il giapponese.
ⓘ E' la 119a al rovescio, la stessa forma dei quattro diari del lotto 059.

### ⓘ Le decisioni minori, e da dove vengono

  - 常緑樹 «sempreverde» e 落葉樹 «albero che perde le foglie» sono gia' in
    gioco sull'**indice 3 di questi stessi oggetti**: la descrizione lunga usa
    la parola che il rapporto di identificazione usa gia';
  - 詠唱を妨害する -> «intralciare gli incantesimi», forma gia' in gioco sulla
    veste dei monaci (`:130714`, lotto 060 di ieri sera);
  - モミの木 «abete» e 飾り «addobbi» sono le stesse parole del lotto **061**
    (`:91026`, l'albero di Natale da commercio): sono lo stesso oggetto visto
    da due parti, ed e' la lezione della riga sorella fra lotti diversi
    applicata a mano;
  - 水薬 «pozione» e 魔術士ギルド «Gilda dei Maghi» dal dizionario;
    ノースティリス «Tyris del Nord», ノイエル «Noyel»;
  - `:68450`, il ciliegio del mondo dei morti, tiene tutt'e due le parole del
    gioco giapponese — 狂い咲き, il fiorire fuori stagione, e
    儚さを通り越して狂気, oltre la caducita' la follia;
  - ⓘ 映写機 (`:95672`) non e' nel dizionario da nessuna parte: e' il
    proiettore, e l'inglese dice «projector».

### ⚠️ Il preflight ha preso una resa, ed era un carattere

`Càpita` — accento **dentro** la parola, che `reimporta` rifiuta. Preso prima
del montaggio e riscritto «Succede spesso»: e' il punto 4 di
`_preflight034.py`, quello per cui tre lotti su otto della 115a erano stati
respinti.
"""
