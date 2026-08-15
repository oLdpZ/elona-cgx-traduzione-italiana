# -*- coding: utf-8 -*-
"""Lotto fase4-command-002: i ventotto prompt, l'inventario, il furto
(command.hsp, righe 13013-14193).

⭐⭐ **`:13924` è UNA RIGA SOLA con ventotto `lang()`, ed è la domanda che il
gioco fa a ogni singola azione su un oggetto.** «Esamina», «Posa», «Raccogli»,
«Mangia», «Bevi», «Leggi», «Compra», «Vendi», «Cucina», «Lancia», «Ruba»: sono
i ventotto rami di `s(invctrl)`, e il giocatore ne legge uno ogni volta che apre
l'inventario per fare qualcosa. Nessuna riga del progetto si vede più spesso di
questa a parità di battute. 54 rese in tutto, zero rinviate.
💡 **La chiave corta regge lo stesso**, e stavolta con ventotto voci sulla stessa
riga: i ventotto inglesi sono tutti diversi. È lo stesso confine trovato dal
`map-005` — tante voci sulla stessa riga non bastano, servono due voci con lo
**stesso** inglese.

⭐ **Lo stile del prompt era già fissato e non ho deciso niente**:
`action.hsp:4019` scrive «Quale porta vuoi chiudere? », `proc.hsp:7607` «In che
direzione vuoi lanciare? ». Le ventotto seguono quella forma — «Quale oggetto
vuoi …? » quando l'inglese dice *which item*, «Che cosa vuoi …? » quando dice
*what*, che è anche la differenza che fa il giapponese fra 「どのアイテム」 e
「何」.

⭐⭐ **«Zap» è «agitare», e non l'ho scelto io**: `text.hsp:135` rende il comando
`Zap` «Agita» e `proc.hsp:7610` scrive «In che direzione vuoi agitare la
bacchetta? ». La resa che veniva in mente — «usare» — avrebbe spento la
distinzione con `Use what?`, che sta **cinque voci più in là sulla stessa riga**.

⚠️⚠️ **Due prompt di scambio, e a distinguerli è la PARTICELLA giapponese.**
「何を交換する？」 («What do you want to trade?») e 「何と交換する？」 («Trade
what?») differiscono per を contro と: il primo chiede che cosa dai, il secondo
con che cosa fai il cambio. L'inglese li appiattisce tutt'e due su *trade* e li
distingue solo per caso, con due giri di frase diversi. ✅ «Quale oggetto vuoi
scambiare? » e «Con che cosa vuoi fare il cambio? ».
💡 «fare il cambio» e non «scambiarlo» perché il clitico concorderebbe col
genere dell'oggetto, che qui non si conosce.

⚠️ **Il prompt del miscuglio è la rete 8 in agguato.** 「何に混ぜる？(valnの効果
を適用するアイテムを選択)」 vuole «l'effetto **di** valn», e `valn` è
`itemname(citrade)` (`:13921`), che porta l'articolo dentro: «l'effetto di la
pozione». ✅ Il nome esce dalla frase e finisce fra parentesi — «Su quale oggetto
applicare l'effetto? (X) » — che è anche la forma del giapponese, il quale mette
la spiegazione in parentesi tale e quale. La strada è quella dei due punti del
`map-005`, con le parentesi al posto loro.
💡 E il prompt gemello `What do you offer for X? ` non ha avuto bisogno di
niente: «**per**» è una delle preposizioni che non si fondono (40ª).

⚠️ **Tre participi che concorderebbero con l'oggetto, e tre modi di evitarli.**
«Do you want to attempt to steal **it**?» (`:13028`) → «Provi a rubare? », senza
clitico; «name(tc) is busy now» (`:13066`) → «**ha da fare**», che è invariabile
dove «occupato» avrebbe concordato col personaggio; «The item is empty!»
(`:13995`) → «Quell'**oggetto** è vuoto», dove l'accordo cade sulla parola
italiana che ho messo io, non su quella che arriva dal gioco.

⚠️ **「ノルマ」 è «obiettivo», e c'era già**: `chara_func.hsp:7247` e
`proc.hsp:241` rendono `Quota ` «Obiettivo ». Il glossario fissa `Guild` →
**Gilda** e `Mages Guild` → **Gilda dei Maghi**.

⚠️ **`:13941` dice «Coins» dove il giapponese dice メダル**, e sono le
**medagliette** — `db_item.hsp:144256` rende `small medal` «medaglietta». Le
monete non c'entrano: quella colonna è il prezzo in medaglie del negozio del re.
Seguito il giapponese.

⚠️ **`:14176` « Cargo » è il carretto**, non un carico generico:
`action.hsp:1906` rende «You carry too heavy cargo to move!» «Il **carretto** è
troppo pesante: non riesci a muoverti!». Il giapponese dice 荷車, che è proprio
quello.

💡 **Le cinque etichette di colonna dell'inventario** (`:14101`-`:14120`) sono la
stessa colonna con quattro monete diverse — prezzo, medagliette, biglietti,
punti gilda — più il nome. ⚠️ Sono le voci più esposte alla larghezza di tutto il
lotto: se `larghezze` o `diario` protestano, si accorciano lì e non altrove.
"""
