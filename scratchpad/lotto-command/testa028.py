# -*- coding: utf-8 -*-
"""Lotto `command-028`: **la dea dei desideri e gli otto dèi che rispondono**.
Ventun rese, il cuore della zona 4000-4999.

⭐⭐ **Otto battute su ventuno sono di divinità che hanno già una voce, e
`action.hsp:14051`-`:14228` me l'ha data tutta.** Chi ha chiuso quel file ha
deciso come parla ciascuno, e qui si riscuote invece di ridecidere: Opatos ride
«Muahahah», Jure balbetta «N-non è mica…», Kumiromi parla a puntini, Mani
comanda, Itzpalt invoca gli elementi al vocativo, Yacatect fa la commerciante
in tono familiare, Lulwy apre con un sostantivo di disprezzo («Che ingenuità»,
qui «Che sfacciataggine»), Ehekatl raddoppia le frasi come una gatta.
💡 È la stessa cosa del punto 5 della 46ª un piano più su: là a tornare erano
sei battute **identiche**, qui torna il **registro** di otto personaggi. La
domanda di `repertorio.py` — «questo file fa parlare qualcuno che un altro ha già
fatto parlare?» — vale anche quando le parole sono nuove.

⭐⭐ **E l'inglese sbaglia due volte in questo lotto, tutte e due per una NEGAZIONE
persa.** A `:4454` il giapponese dice 「神力に余裕がない」, cioè che alla dea **non**
avanzano forze; l'inglese scrive «can afford to use her powers now», che dice
l'opposto e in mezzo a un `if` che blocca il desiderio. A `:4482` il giapponese
chiude con 「聞かなかったことにしてね」 — «fa' finta di non aver sentito» — e l'inglese
ci mette «Hey, listen to me!», che è il rovescio esatto della battuta: la dea si
lascia sfuggire che dentro Ehekatl c'è un dio e poi si rimangia tutto.
✅ In tutt'e due i casi la resa segue il **giapponese**, e nessuna rete deve
intervenire perché sono statiche: non c'è un contratto di funzioni da rispettare.
💡 È il terzo tipo di errore di monte in tre sessioni di lavoro su questo file —
dopo lo slot copiato (`:15188`) e l'inglese che appiattisce (`:15636`): qui
l'inglese **capovolge**.

⚠️ **Una voce non ha niente da tradurre e va dichiarata.** `:4465` è
`cnvtalk(inputlog + "!!")`: il gioco rimanda a schermo, gridata, la frase che il
giocatore ha appena **digitato**. Fuori da `inputlog` non c'è nessuna parola —
due punti esclamativi e le virgolette che ci mette `cnvtalk`. La resa coincide
con l'inglese **per costruzione**, ed è lo stesso criterio di
`"*" + skillname(efid) + "* "` (`proc.hsp:12101`): sta nella sezione «non c'è
niente da rendere» di `invariati.md`.

⚠️ **`:4436` non è un messaggio: è quello che parte in rete.** Tre righe sotto
c'è `net_send "wish" + s`, cioè il desiderio che finisce sulla bacheca condivisa.
Si traduce lo stesso — è anche il testo che il giocatore vede — ma vale la pena
saperlo: quella riga esce dal gioco.

⭐ Riscosso senza decidere: «Nemmeno il potere della dea dei desideri arriva fin
qui...» (`proc.hsp:14492`, stesso inglese), «il dio dentro» (`db_creature.hsp:101284`,
`<Il dio dentro Ehekatl>`) e «Alias» per 異名 (`command.hsp:10504`, la scheda del
personaggio). ⚠️ E «Quu» per 「きゅー」 della creatura quantistica, che
`db_creature.hsp` aveva già scelto: è una delle tredici divergenze volute di
`battute --divergenti`, e va tenuta.
"""
