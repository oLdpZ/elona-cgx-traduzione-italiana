# -*- coding: utf-8 -*-
"""115a - Lotto 035 di `db_item.hsp`: GLI ATTREZZI, terza parte.

`FILTER_ITEM_TOOL`, righe 62.000-75.000: **43 righe** su 36 oggetti — 36
dell'indice 0, nessuna dell'indice 1 e 7 dell'indice 2. Segue il 034.

### ⭐⭐⭐ QUATTRO VOLTE L'INGLESE LASCIA CADERE UNA FRASE INTERA

Non e' una sfumatura di stile: sono frasi che nel giapponese ci sono e
nell'inglese **non compaiono affatto**.

  - `:63937` e i quattro fratelli — «a volte cambia solo un pezzo del
    vestiario, a volte il corpo diventa tutt'altra cosa». L'inglese si ferma a
    «largely dependent on the state of the user» e taglia l'esempio, che e' la
    sola frase che dica **che cosa** cambia;
  - `:65195`, il guanto di sfida — «che nel duello l'altro resti ferito o ci
    muoia, il karma non ne risente». E' un **fatto di gioco**, e l'inglese non
    lo dice da nessuna parte;
  - `:68587`, la pipa da oppio — il giapponese dice che nelle trattative la
    mascherano da **キセル**, una pipa comune; l'inglese scrive «a pack of
    cigarettes», che e' un altro oggetto;
  - `:73828`, lo scanner — il punto ③ giapponese dice che gli HP di chi
    comanda l'oggetto vanno a **zero**; l'inglese scrive «you lose the Duel»,
    che nel gioco non e' la stessa cosa. E la testa （効果未実装）, che
    l'indice 3 conserva, nell'inglese dell'indice 0 sparisce.

Si segue il giapponese (109a), e le quattro frasi tornano.

### ⭐⭐ I CINQUE NUCLEI SONO UNA FAMIGLIA, E L'APERTURA VIENE DAL LOTTO 033

`:63937` (alfa), `:64005` (beta), `:64073` (gamma), `:64141` (delta), `:64209`
(omega) hanno lo stesso identico giapponese a meno della frase sugli attributi.
Cinque rese identiche fino a quella frase, come vuole la regola della famiglia
(111a).

⭐ L'apertura non si inventa: 魔石が組み込まれた魔道具 e' gia' reso a `:43240`
nel lotto 033 — «Un oggetto magico con dentro una pietra magica» — e l'inglese
li' come qui scrive «special gemstone», che 魔石 non e'. La formula si copia.

Gli attributi si copiano da `skill.hsp`, dove sono gia' resi: 筋力 Forza,
感覚 Percezione, 魔力 Magia, 器用 Destrezza, 回避 Schivata.

### ⚠️⚠️ UNA RIGA SENZA GIAPPONESE, LA SECONDA IN DUE LOTTI

`:72552` (l'indice 2 della maschera) ha il giapponese **vuoto** e un inglese
vero, come `:50410` nel 034. Li' l'inglese era quello giusto per caso; qui e'
l'unico che ci sia, e per giunta e' una **battuta**: «Stop playing the race
card!», dove *race* e' insieme la razza del gioco e il modo di dire inglese.

L'italiano non ha il modo di dire, ma ha la carta: «E piantala di giocarti la
carta della razza!» tiene tutt'e due i sensi perche' **l'oggetto e' una
maschera che cambia razza**, e la carta da giocare resta un'immagine viva.

⚠️ Queste righe non sono un errore da riparare: sono due su 460 rese del corpo,
e vanno **contate**. Se diventassero tante, vorrebbe dire che l'estrazione
perde il ramo giapponese da qualche parte, e sarebbe un altro guasto.

### ⭐⭐⭐ IL GENERE DEL GIOCATORE, IN UNA RIGA DI DUE PAROLE

`:65197` e' 「うそつき」, «bugiardo», ed e' la battuta di chi ha appena preso
in faccia il guanto di sfida: la dice **al giocatore**. In italiano
«bugiardo» sceglierebbe un genere che il gioco non conosce, ed e' la regola
di `guida-stile.md` (la stessa che ha riscritto `Full` in «Non riesci a mangiare
altro»).

La resa e' **«Menti.»**: il verbo non ha genere, l'accusa resta intera e sta in
due sillabe come l'originale. ⓘ L'inglese qui scrive «Scut!», che e' una terza
cosa ancora.

### ⚠️⚠️ LE VIRGOLETTE A CAPORALE NON ESISTONO IN QUESTO DIZIONARIO

Scrivendo `:65464` — l'oggetto che «porta il nome di *洞察*» — la prima stesura
metteva il nome fra virgolette a caporale. Contate: nel dizionario intero, su
**24.940** rese, le `«` sono **zero**. Non e' una consuetudine implicita, e'
un fatto: CP932 quel carattere non ce l'ha, e `degrada()` lo perderebbe.

Il nome va in maiuscola e senza virgolette. ⚠️ La domanda giusta non era «mi
piacciono?» ma «ce ne sono altre?», e la risposta si conta, non si ricorda.

### ⓘ I termini cercati a mano nel dizionario

イェルス «Yerles»; クラムベリー «crimberry»; 時止弾 «munizioni fermatempo»;
存在級位 «grado di esistenza»; アカシックネットワーク «rete akashica» (e da li'
アカシックレコード, «registro akashico»); 解剖学 «Anatomia»; 錬金術 «Alchimia»;
料理 «Cucina»; デッキ «mazzo»; ランク in senso di carta «valore»
(『ランクチェンジ』 -> «Cambia valore»); アンデッド «non morto»; カルマ «karma»;
情報屋 «informatore»; ブラックマーケット «mercato nero»; 元素の神 «dio degli
elementi»; 富の女神 «la dea della ricchezza».
"""
