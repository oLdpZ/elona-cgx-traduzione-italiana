# -*- coding: utf-8 -*-
"""`economy.hsp` si apre e si chiude: le 39 firme del governo della citta'.

Il prospetto cittadino, il bilancio, il giudizio dei cittadini, le leggi e la
costruzione degli edifici. `economy.hsp` non aveva dizionario, ed era anche uno
dei due file che `file_senza_dizionario.py` chiamava **mezzo tradotto**: una
toppa (`:778`, «k gp» -> «k oro») e nessun dizionario, cioe' una riga italiana
in un file che per il referto non esisteva. Adesso e' intero.

## ⚠️ Le colonne si allineano con gli SPAZI, e l'italiano ne conta di piu'

`economy.hsp:319`-`:365` scrive dodici righe fatte cosi':

    mes lang("...", "Water pollution     " + mdata(...) + " (dead " + ... )

L'etichetta e' **imbottita a 20 caratteri** e il numero comincia sempre alla
stessa colonna: e' un allineamento a mano, non una tabella. Le rese tengono i
20 caratteri, e per questo 発言力 diventa «Influenza» e non «Autorita'»:
⚠️⚠️ **un'etichetta con l'accento romperebbe l'allineamento**, perche' nel
dizionario si scrive «Autorità» (8 caratteri) e `applica` scrive «Autorita'»
(9). L'imbottitura andrebbe contata sulla forma degradata, cioe' su una cosa che
il file del dizionario non mostra. Meglio un sinonimo senza accento.

## Il tetto delle due leggi, letto dalla striscia e non dalla finestra

`economy.hsp:440`-`:441` sono due voci di `chatList`, e la rete 15 le pretende
misurate. La finestra e' larga 480 (`:458`), ma il confine vero e' la
**striscia** che il gioco disegna sotto le righe pari — `gfini 365, 18` da
wx+74 (`:494`-`:495`) — e la voce comincia a wx+104 (`:509` piu' i 4 di
`cs_list`). Sono **47 caratteri**, non 53.

⚠️ E il contenitore si chiama `*skip_rule`, che e' un'etichetta di salto: i due
`chatList` stanno sopra, il disegno sotto, e in mezzo c'e' un `goto`. E' il
quarto contenitore misurato dopo la pergamena, la finestra dell'evento e il
pannello degli dei.

## ⚠️ Due volte l'inglese di monte perde qualcosa

1. `:440` **perde il segno di percentuale.** Il giapponese scrive
   「この街の消費税は%だ。」, l'inglese «The consumption tax of this town is .»
   — e a schermo esce «...is 15.», un numero senza unita'.
2. `:327` **cambia l'ordine e perde la parola.** 「今までの死者N人」 e' «N morti
   fino a oggi»; l'inglese scrive «(dead N people)», che si legge come un
   aggettivo.

## Il vocabolario, e da dove viene

    oro                 gp / GP, gia' otto volte nelle toppe
    cgp                 resta: e' la valuta della citta' (city gold piece),
                        una sigla del gioco come GP
    Leggi               la linguetta di module.hsp:5163
    citta'              mdatan(MDATAN_NAME), come ovunque
    Prospetto           チャート: e' il quadro dello stato della citta',
                        non un grafico — quello e' la linguetta «Grafico»
"""
