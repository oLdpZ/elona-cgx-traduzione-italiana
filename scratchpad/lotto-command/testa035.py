# -*- coding: utf-8 -*-
"""Lotto `command-035`: **la coppia da combattimento e la raccolta dei pezzi da
un alleato**. Sedici rese.

⭐⭐ **Dieci rese su sedici sono cinque coppie con l'inglese IDENTICO e il
giapponese diverso, e la differenza è il consenso.** `:7249`-`:7273` e
`:7284`-`:7308` dicono in inglese le stesse cinque frasi — «You take out a bone
from …», e così cuore, occhio, sangue, pelle — mentre il giapponese mette
**「無理やり」**, «a forza», solo nella prima serie.
✅ **E non è una sfumatura: è il ramo che si raggiunge dopo un avvertimento.**
`:7240` è `if ( sorg(SKILL_ATTR_LIFE, tc) < 4 )`, cioè l'alleato è già troppo
debole; `:7242` chiede conferma dicendo che morirà; `:7243` è `promptYesNo`; e se
rispondi di sì parte **quella** serie. L'altra è il caso ordinario. In inglese le
due strade dicono la stessa cosa e il giocatore non sa quale ha preso.
⭐ La rete 11 autorizza — `name` di qua e di là, in tutt'e due le lingue — quindi
l'italiano si riprende la distinzione: «perde un osso» contro «perde un osso,
strappato via a forza».

⚠️⚠️ **E l'avvertimento stesso è sbagliato in inglese: parla di LATTE.** `:7242`
è «If you squeeze more milk, … will die», ma il ramo copre `p` da 18 a 22, cioè
osso, cuore, occhio, sangue e pelle — il latte non c'entra. Il giapponese è
generico: 「無理に行うと死にそうだ」, «a insistere rischia di morirci». È una dinamica
con `name` in tutt'e due le lingue, quindi la resa può essere generica come
l'originale senza toccare il contratto.

⚠️⚠️ **`:7191` è l'inglese che dice una cosa diversa, e stavolta senza scampo.**
Il giapponese è 「…には既にタッグパートナーがいる。」, «ha già un compagno di coppia»;
l'inglese è **«There's no place.»**, che è il messaggio di un'altra scena. ⚠️ La
voce è tipata **statica** — l'inglese non ha nessuna funzione, mentre il
giapponese ha `cdatan()` — quindi la resa **non può nominare nessuno**: resta
«Ha già un compagno di coppia.», senza soggetto. Il soggetto lo capisce chi
gioca, perché ha appena scelto quel compagno.

⭐ **Riscosso senza decidere: «compagno di coppia».** 「タッグパートナー」 è già così in
`action.hsp:1024` e in cinque righe di `:1877`-`:1889`, dove il compagno di
coppia guarda storto, china il capo, indietreggia di un passo.

⚠️⚠️ **E tutte e undici le rese con `name()` hanno la stessa forma, non per
gusto ma per la rete 8.** `name()` per il giocatore è «il viandante», cioè un
sintagma **con l'articolo**: «a il viandante» e «di il viandante» sono
sgrammaticati, e la preposizione non si può fondere a scrittura perché
l'articolo non si conosce. ✅ Quindi `name()` non sta **mai** dopo una
preposizione: o è soggetto («X perde un osso») o segue un verbo («uccidere X»,
«Hai rimandato a casa X»). È il motivo per cui queste frasi non dicono «estrai
un osso **da** X», che sarebbe l'italiano ovvio.
💡 E gli accordi cadono tutti sul **pezzo**, mai su `name()`: «strappato» va con
«osso», «strappata» con «pelle». Il genere di chi subisce non entra mai in gioco.
⚠️ Due parole scelte per evitare un modo di dire: 「心臓」 è «il **proprio** cuore»
perché «perdere il cuore» in italiano vuol dire innamorarsi, e 「皮」 è «**tutta**
la pelle» perché «rimetterci la pelle» vuol dire morire.

⚠️ `:7332` è un'altra statica in cui il giapponese dice di più: la parentesi
spiega anche che **digitando 1 si torna all'immagine predefinita**, e l'inglese
lo perde. Nessun contratto da rispettare, quindi la resa lo tiene.
"""
