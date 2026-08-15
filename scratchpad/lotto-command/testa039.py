# -*- coding: utf-8 -*-
"""Lotto `command-039`: **dare qualcosa a un alleato**. Quindici rese, da
`:14842` a `:14993`, la coda di `*com_inventory_loop`.

⭐ **La zona si chiude qui**: con questo lotto la 14000-14999 è finita, ed è la
terza zona di `command.hsp` chiusa in due sessioni dopo la 12000-12999 e la
7000-7999.

⚠️⚠️ **`:14852` è la rete 11 nella sua forma più stretta, e va guardata due
volte.** Il giapponese è 「<name>はこれ以上持てない。」 con `name(tc)`; l'inglese è
`his(tc) + " inventory is full."`, e `his` a **un** argomento è morfologia
(`funzioni.py:78`, la regola per sito). Quindi le funzioni di contenuto
dell'inglese sono **zero**, e la resa non può nominare nessuno: «Non riesce a
portare altro.», soggetto sottinteso. ✅ Ma la voce è tipata **dinamica**, quindi
la rete 12 pretende un'espressione: la resa è un letterale fra virgolette, come
`:7724` nel lotto 036. Chi la vedesse a schermo senza nome non deve
«aggiustarla»: è il contratto dell'inglese, non una dimenticanza.

⭐⭐ **`:14874` e `:14980` hanno lo STESSO giapponese e due inglesi diversi, e la
rete 4 pretende — giustamente — una resa sola.** 「あなたは<name>に<item>を渡した。」
diventa «You give X Y.» in un ramo e «You give the Y to X.» nell'altro: è la
stessa frase, girata due volte da chi traduceva. In italiano è una sola.
✅ **E la forma non si è dovuta scegliere**: `:15250` rende già 「を渡した。」 con
`name(tc) + " riceve " + itemname(ci, 1) + "."`, e sta in questa stessa routine,
duecento righe più giù.
💡 **Il motivo per cui quella forma esiste è la rete 8**: l'italiano ovvio
sarebbe «Dai <item> **a** <name>», e `name()` per il giocatore è «il viandante»,
cioè un sintagma con l'articolo — «a il viandante» non si può scrivere, e
l'articolo a scrittura non si conosce. Misurato su tutto il dizionario: le rese
che mettono una preposizione davanti a `name()` sono **zero**. Girare la frase
sul ricevente è l'unica strada, ed è già battuta.
⭐ `:14860` è il terzo della famiglia e ha un giapponese suo — 「プレゼントした」,
non 「渡した」 — quindi può distinguersi: «riceve **in regalo**».

⚠️ **Le otto battute di risposta sono `cnvtalk(...)`, e l'inglese ne ha solo
tre.** «Thank you!» copre `:14863`, `:14878` e `:14984`; «Hmm...» copre `:14887`
e `:14993`. Il giapponese invece dice cinque cose diverse, e la scena le
distingue: `:14863` è il regalo accettato, `:14878` il pegno d'amicizia con
l'impressione ≥ 100, `:14887` lo stesso pegno con l'impressione bassa, `:14984`
il mazzo di fiori con l'impressione ≥ 150, `:14993` lo stesso mazzo senza.
✅ Sono **statiche**, cioè senza contratto di funzioni: la resa segue il
giapponese, come `:4764` nella 46ª e come gli otto dèi nella 47ª. La rete 13
segnalerà i due inglesi ripetuti; la distinzione va tenuta, ed è tutto il punto
della scena.
💡 Le due battute tiepide sono tiepide anche in giapponese: 「友情、ねぇ…」 è
«Amicizia, eh?...» e 「う、うん…」 è un sì esitante. Chi legge deve capire che il
regalo non è bastato.

⭐ `:14911` («Beautiful...») ha lo stesso inglese di `proc.hsp:1367`, già reso
«Che bellezza...», e il giapponese 「綺麗だな…」 dice la stessa cosa: si ricopia.
⚠️ Ma `:14984` non può ricopiare `:14897`: 「素敵！」 e 「なんと立派な！」 sono due
battute diverse su due oggetti diversi, e l'inglese le ha appiattite in modo
opposto (una in «Thank you!», l'altra in «How splendid!»).

💡 **`:14847` non dice «sviene» ma «ha perso i sensi»**, perché il giapponese è
「気絶している」, uno **stato** e non un evento: `proc.hsp:10303` usa «sviene» per
「気絶した」, che è il momento in cui succede. E «ha perso i sensi» non concorda con
niente, che serve perché l'alleato può essere di qualunque genere.
"""
