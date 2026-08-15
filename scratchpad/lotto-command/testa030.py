# -*- coding: utf-8 -*-
"""Lotto `command-030`: **le feste, i sette dèi maggiori sconfitti, le parole
chiave del desiderio**. Ventun rese, e con queste **la zona 4000-4999 è chiusa**.

⭐⭐ **Cinque voci su ventuno sono parole chiave che il giocatore digita, e qui
la regola è l'opposta del lotto 027.** `:4832`-`:4855` sono
`instr(inputlog, 0, lang(…))`, cioè «il desiderio contiene questa parola?»: se la
contiene, il gioco crea una carta, una statuetta, una bambola dorata. ✅ La resa
di ognuna è **il nome dell'oggetto come sta in `db_item.hsp`** — «carta»
(`:145900`), «statuetta» (`:145913`), «bambola dorata» (`:135419`), «bambola di
carne» (`text.hsp:3356`), «biglietto d'abilità» (`:137176`) — e non una parola
inventata, perché il giocatore quel nome **lo legge sullo schermo** prima di
digitarlo.
💡 **E per questo qui l'accento si scrive normale**, dove nel lotto 027
«abilita» andava senza: «biglietto d'abilità» diventa in build «biglietto
d'abilita'», che è **esattamente quello che il giocatore vede scritto
sull'oggetto** e quindi quello che ricopia. Là la parola veniva dalla testa di
chi scrive, qui viene dallo schermo. La differenza non è una preferenza: è da
dove arriva la stringa.
⚠️ E il giro si chiude: chi scrive «abilita pesca» viene instradato da `:4840`
(la stessa firma di `:4336`, già resa «abilita») verso `*wish_skill`, che a
`:4860` chiama `*wish_fix` e toglie il prefisso. Le due decisioni del lotto 027 e
di questo devono per forza combaciare, ed è la ragione per cui vanno lette
insieme.

⭐⭐ **L'inglese butta via una battuta intera, e stavolta è una statica: la resa
può riprendersela tutta.** `:4764` in giapponese è
「え？今年もクリスマスは中止でしょ？」 — «Eh? Ma il Natale non è stato annullato anche
quest'anno?», che è una presa in giro — e in inglese diventa «Merry Christmas!».
Non c'è nessun contratto di funzioni da rispettare (è una statica), quindi la
resa segue il giapponese. ⚠️ Lo stesso a `:4802`, dove Iper Yacatect grida
「はなさんかいボケェ！」 — «mollami, deficiente!» — e l'inglese scrive «Count your
days, stupid!», che vuol dire un'altra cosa.
💡 Con `:15188` (l'inglese sbagliato), `:15636` (l'inglese che appiattisce),
`:4454` e `:4482` (l'inglese che capovolge) fanno **cinque famiglie** di errore
di monte incontrate in sei lotti su questo file. Non è sfortuna: è che l'inglese
di Elona+ è una traduzione di comunità e il giapponese è l'originale.

⚠️ **Sette battute sono di divinità nella loro forma potenziata**, e il registro è
quello che il lotto 028 ha già riscosso da `action.hsp`: Opatos ride ancora
(«Muahaan! Muah!»), Yacatect resta popolana, Kumiromi resta a puntini. ⭐ Per
Jure la Benedetta l'insulto è **«idiota»**, che in italiano non ha genere, ed è
la stessa parola che `action.hsp:14058` le mette già in bocca: il giocatore può
essere uomo o donna, e «scemo» o «cretino» sceglierebbero per lui.

⭐ Riscosso senza decidere anche: «bambola di carne» (`text.hsp:3356`).
⚠️ E una divergenza voluta: ` *Hiss* ` è già ` *frusc frusc* ` in
`db_creature.hsp:91012`, ma là è un fruscio e qui è il **soffio di un gatto**
(「フシャーッ！」, il dio dentro Ehekatl). Restano due cose diverse sotto lo stesso
inglese.
"""
