# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-007: i rapporti, la tag-team, la sella e la coda
sparsa (chara_func.hsp 0-5999, quello che restava).

22 rese, e **con questo `chara_func.hsp` e' CHIUSO**: 331 firme su 331, meno le
quattro rinviate apposta. E' il tredicesimo file al 100% del progetto, e il
quarto in due giorni dopo `proc.hsp`, `chips.hsp` e `custom_enemyevolution.hsp`.
Le voci di questo lotto non stanno in una zona: sono quello che avanzava sopra
il 2000 e sotto il 6000, cioe' i rapporti con i PNG, la squadra, la cavalcatura
e tre righe di trama.

⚠️ **`:748` non e' testo, ed e' la terza «Party Room» del progetto.**
`lang("JP", "EN")` sta dentro `instr(locvar_customtalk_buff, 0,
locvar_customtalk_s + "," + lang("JP", "EN"))`: e' la **chiave di ricerca** nel
file dei dialoghi personalizzati, non una frase. Tradurla romperebbe la ricerca.
✅ E la risposta era gia' nel dizionario due volte — `action.hsp:4816` e
`text.hsp:9361` la lasciano `EN` — quindi si copia invece di ridecidere. 💡 Non
serve rinviarla: la resa **e'** «EN», ed e' una resa vera, non un rinvio.

⚠️⚠️ **La sella e' la testa di frase piu' lunga del progetto, e continua in
un'altra istruzione.** `:1654` finisce con «`->`» e la frase si chiude a
`:1665`, che stampa `"" + cdata(CDATA_SPEED, ...) + ") "`: la parentesi si apre
in una `lang()` e si chiude **undici righe dopo**, fuori da qualunque
traduzione. ✅ La resa deve quindi finire com'e' cominciata, con la freccia e lo
spazio, e la parentesi resta aperta apposta.
⚠️ **E dentro ci stavano due fusioni**: «Sali **in sella a** X» e «la velocita'
**di** X». ✅ Girate col nome dentro parentesi come **etichetta** — «Cavalchi X.
(X, velocita': 100 -> 120)» — che e' la forma dei referti di stato e non chiede
nessuna preposizione. I due `name()` che la rete 11 pretende restano tutt'e due.

⚠️ **`:1080`, `:1086`, `:1183`, `:1189`, `:1627`: cinque righe su ventidue
vogliono «con», e non e' un caso.** Il giapponese le scrive tutte con 「と」 —
「Xとの関係」, 「Xとタッグを組んだ」 — cioe' il complemento di compagnia, e
l'italiano lo rende con **«con»**, che e' una delle preposizioni che **non si
fondono** con l'articolo che `cdatan()` porta dentro. 💡 Dopo «sotto» del lotto
005, e' la seconda volta in due lotti che la soluzione e' scegliere la
preposizione giusta invece di girare la frase: vale la pena scriverlo una volta
per tutte — **«con», «contro», «per», «tra», «sotto», «sopra» non si fondono**,
e davanti a `name()` sono le uniche utilizzabili.
✅ **E la rete 8 l'ha imposto sul campo**: la prima stesura di `:1169` diceva
«fai colare la cera **su** X», la rete l'ha fermata («su il putit») e la
correzione e' stata cambiare **una parola** — «sopra» — invece di riscrivere la
frase. E' il caso piu' economico che la rete 8 abbia mai prodotto in nove lotti.

⚠️ **`:1668` dice due cose diverse nelle due lingue, e vince il giapponese.**
「この生物は乗馬用にちょうどいい！」 e' «questa creatura e' perfetta da
cavalcare», cioe' un giudizio **sulla cavalcatura**; l'inglese scrive «`You feel
comfortable.`», che parla di **te**. Il ramo lo conferma:
`cbit(CHARA_BIT_SUPERIOR_RIDING, gdata(GDATA_RIDER))` guarda una proprieta'
della bestia. E' la classe di `:3380` del lotto 001, la terza volta in
`chara_func.hsp`.

💡 **E le ultime due copie del file**: 「不明」 e' «Ignoto» in `text.hsp:2969`
sotto lo stesso inglese, e 媚赤蝋燭 e' `<Candela di Lulwy>` in
`db_item.hsp:138261` — che l'inglese chiama «Candle of Lulwy», per una volta
d'accordo col giapponese.
"""
