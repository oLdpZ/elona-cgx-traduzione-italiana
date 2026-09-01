# -*- coding: utf-8 -*-
"""120a - Lotto 056 di `db_item.hsp`: LE BACCHETTE, e la categoria CHIUDE.

`FILTER_ITEM_ROD`, righe da `:61946` a `:130030`: **32 righe**, tutte
dell'indice 0, su 32 oggetti — la categoria intera in un lotto solo. Con questo
lotto `FILTER_ITEM_ROD` va a **0 da fare su 32 vive**, ed e' l'**undicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 056`: **+32** per 32 rese,
nessuna gemella. ⓘ `_gia-reso.py 056`: 0 su 32. `_code.py 056`: 0 righe senza
resa in tabella, e tutte e 32 le code sono «~Compendio Completo degli Oggetti
Magici~».

### ⭐⭐⭐ E' UNA SERIE DI TRENTADUE, E STAVOLTA L'HO MISURATA INVECE DI GUARDARLA

Tutte e 32 le bacchette aprono con la stessa frase e poi descrivono **la
gemma** (o l'incisione, dove gemma non c'e'). Vederlo dal dossier e' facile;
rispondere alle tre domande che contano, no, perche' il dossier mostra una voce
per volta. Le ha risposte `scratchpad/_120-serie-bacchette.py`, scritto qui:

  - **31 righe su 32 aprono IDENTICHE**, 特定の魔法が封じ込められた杖。 Le 31
    rese italiane ripetono la stessa frase parola per parola, per la ragione
    della serie delle tre armi: la ripetizione **e' il testo**;
  - ⭐⭐ **una sola diverge, ed e' `:111777`** — la bacchetta dei **desideri**,
    la piu' rara del gioco. Il giapponese dice 貴重な杖, «una bacchetta
    **preziosa**», e **l'inglese lo lascia cadere**: «Rods encasing specific
    magic, a cat-eye-shaped gem is attached to it», identico agli altri
    trentuno. Chi rendesse dall'inglese scriverebbe trentadue righe uguali
    dove il giapponese ne ha trentuno piu' una;
  - ⚠️⚠️ **`:71856` e `:106766` hanno il giapponese IDENTICO** — l'eclissi e il
    silenzio, tutt'e due 黒く濁った宝石 — e due inglesi che differiscono per una
    **virgola** («a black and murky gem» / «a black, murky gem»). Le due rese
    devono essere identiche: altrimenti sarebbero due rese diverse per lo
    stesso originale, che e' il difetto che `battute --divergenti` misura. Nel
    file delle rese le due voci puntano a **una costante sola**, cosi' non
    possono divergere per distrazione.

⭐ **Perche' uno strumento e non l'occhio.** Il gradino di `:111777` sta in due
caratteri dentro una formula ripetuta trentadue volte: e' esattamente il tipo
di differenza che l'occhio salta, perche' l'occhio sta leggendo la parte che
cambia (la gemma) e da' per identica quella che si ripete. Il conto lo trova in
un secondo. ⚠️ E la coppia col giapponese identico non si vede affatto
leggendo: le due righe stanno a trentacinquemila righe di distanza, in due
punti diversi del dossier.

ⓘ E' la stessa lezione della scala delle navi (119a) e della serie delle tre
armi (120a), ma il metodo e' salito di un gradino: **la` la struttura si
cercava a mano, qui si conta**. La domanda «questa riga ha delle sorelle, e che
cosa cambia fra loro?» ha smesso di dipendere da quanto sto attento.

### ⓘ Due scelte di resa che il giapponese detta

  - `:96275`, la bacchetta dell'alchimia: il giapponese dice
    自分の尾を咥えた竜 — «un drago che si tiene in bocca la propria coda» — e
    **non lo nomina**; l'inglese scrive «a Uroboros». La resa **descrive**,
    come l'originale: chi non conosce l'uroboro se lo vede lo stesso, e chi lo
    conosce lo riconosce. Nominarlo sarebbe spiegare una figura che
    l'originale sceglie di mostrare;
  - `:93149`, la bacchetta del suolo acido, e' **l'unica delle 32 senza gemma**,
    e il giapponese lo dice esplicitamente (宝石が付いておらず, «di gemme non ne
    ha») prima di descrivere l'asta. La resa apre allo stesso modo, con la
    negazione: e' il secondo gradino della serie, dopo quello di `:111777`.
"""
