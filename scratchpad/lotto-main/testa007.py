# -*- coding: utf-8 -*-
"""Lotto fase4-main-007: gli esiti degli incarichi e le battute degli dèi
(main.hsp, righe 4520-4712).

Sedici rese, due gruppi. Il primo e' il verdetto che chiude ogni incarico a
tempo — festa, consegna, campo minato, caccia — cioe' la riga che il giocatore
legge **ogni volta** che ne finisce uno. Il secondo sono le sette battute che
gli dèi dicono prima di scatenare il Ragnarok (`ANIMATION_RAGNA`), una per
divinita'.

⭐⭐ **`:4549` e `:4562` sono lo stesso inglese per due incarichi diversi, e la
rete 13 ha ragione a segnalarlo.** Upstream ha scritto `"You complete the
task!"` due volte, ma il giapponese distingue: 「無事に納入を終えた！」 e' la
**consegna** (`QUEST_TYPE_HARVEST`, si portano le merci) e 「無事に撤去を終えた！」
e' la **rimozione** (`QUEST_TYPE_MINEFIELD`, si tolgono le mine). Lo stesso vale
per la coppia dei fallimenti, `:4554` e `:4567`.
✅ L'italiano tiene la distinzione, e le parole non sono scelte qui:
«consegna» viene da `command.hsp:15499` («Hai consegnato...», « Consegnato »),
che e' la riga di quello stesso incarico. Per il campo minato «bonifica» e' il
termine italiano proprio del togliere le mine.
💡 E' il rovescio del caso di `:4050` nel lotto 005: li' upstream distingueva
dove il giapponese non lo faceva, qui appiattisce dove il giapponese distingue.
Sono le due facce della stessa domanda — **quale delle due lingue di monte sa la
cosa che serve** — e la risposta si trova sempre guardando il codice intorno,
qui `gdata(GDATA_QUEST)`.

⚠️ **`:4712` perde `he(cc)`, che e' morfologia.** L'inglese chiude con «...the
dust from whence " + he(cc) + " came!», cioe' col pronome che l'italiano
dovrebbe accordare con un genere che non conosce. `he` con **un** argomento sta
in `MORFOLOGIA_INGLESE` e `verifica` pretende che sparisca. La resa segue allora
il giapponese, che quel pronome non ce l'ha: 「今こそ、あるべき姿へと還るのだ！」,
«e' ora di tornare alla forma che ti spetta». ⚠️ E non si mette «questo sciocco
torni alla polvere da cui e' **venuto**»: sarebbe lo stesso participio, entrato
dalla finestra.

⚠️ **`:4572` non dice «non sei riuscito».** 「討伐に失敗した…」 e' impersonale in
giapponese e lo diventa in italiano — «La caccia e' fallita...» — perche' il
participio con `essere` accorderebbe col genere del giocatore. Stessa ragione di
`:4353` nel lotto 006, dove «Sei sottoterra» ha preso il posto di «sei stato
sepolto».

💡 **Le sette battute degli dèi vanno lette come sette voci diverse**, e il
sorgente dice di chi sono: `EVENT_GOD_INSIDE_LULWY` a `:4619`, poi Ehekatl,
Opatos, Kumiromi, Mani, Jure e Itzpalt. Quella di Ehekatl e' un verso di gatto
(「みみゃぁ」 / «MEWWWWWW»), quella di Jure una battuta sulla stupidita' che non si
cura — e' la dea che guarisce — e quella di Itzpalt un'invocazione ai tre
elementi. Tradurle tutte con lo stesso tono le avrebbe appiattite.

⚠️ **`:4616` e' una citazione**, e resta tale: la Sorellina che scivola dalla
spalla del Papa'-Bombola e grida «Mr. Bubbles!» viene da *BioShock*, dove in
italiano quel nome **non e' stato tradotto**. Le due creature hanno gia' il loro
nome nel gioco; qui si tiene la citazione come la tiene l'inglese.
"""
