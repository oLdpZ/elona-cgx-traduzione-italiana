# -*- coding: utf-8 -*-
"""92a - LANKATA (`chat.hsp:13834`-`:13896`, 16 firme).

ランカータ = **Lankata**, ufficiale della **squadra speciale di Lothria** che
punta al Sigillo Eterno (`chat.hsp:24497`-`:24501`). E' una donna
(`:13869`, «shouted as to remind **herself**»; `:18157`, «Siete
un'**infermiera** da campo»), parla in ですます e comanda in 〜なさい: italiano
formale e militare, e **da' del voi al giocatore** — cosa gia' decisa, non da
decidere qui.

LESSICO EREDITATO (non deciso qui):
  - 「そこの冒険者」  «Voi che cercate avventura»   chat.hsp:18140 (stessa
                      persona, stesso modo di rivolgersi al giocatore)
  - 父上              «Padre»                       chat.hsp:18138, :18156
  - はく製 / 剥製     «statuetta»                   command.hsp:4849, chat.hsp:14106
  - 靴下              «calzini»                     chat.hsp:12431 e la catena
                                                    del ladro di calzini
  - アンデッド兵器    «armi non morte»              chat.hsp:10239, :24505
  - 冒険者            «chi va all'avventura»        decisioni.md

⭐⭐⭐ DEROGA 1 — `:13837`, 父上 E' **SUO** PADRE, NON QUELLO DEL GIOCATORE.
L'inglese scrive «I was able to rescue **your** father». Ma il padre di Lankata
ha un nome e un identificativo: e'
`CREATURE_ID_ALFRED_THE_CANGNAN_WIND`, e la scena in cui lo trova sta a venti
righe di distanza — `:18131` lo crea, `:18138` e' lei che dice
「やっと会えた…！父上っ！」 («Finalmente vi ho trovato...! Padre!», gia' resa),
`:18143` e' lei che gli estrae il reattore dimensionale, `:18155` e' **lui** che
chiede «Io... sono salvo?». Il giocatore in Elona non ha un padre da nessuna
parte. Si scrive «mio padre».

⭐⭐ DEROGA 2 — `:13852` E' LA PARODIA DI `:13856`, E VA COSTRUITA UGUALE.
Lankata dice 「速やかに**武器**を置いて**この階**を去りなさい」. La prima voce
del menu del giocatore e' 「**はく製**を置いて**この世**を去りなさい」: stessa
frase con due parole cambiate — *le armi* diventano *la statuetta*, *questo
piano* diventa *questo mondo*.
⚠️ E la battuta di lei e' il `buff`, cioe' sta **sopra il menu mentre si
sceglie**: le due righe si leggono nello stesso istante, quindi in italiano
devono usare gli stessi verbi, o la parodia non si vede. Rese «Posate subito le
armi e lasciate questo piano» / «Posate la statuetta e lasciate questo mondo».

⭐⭐ DEROGA 3 — `:13888`, L'INGLESE CAPOVOLGE LA FRASE.
「間に…合わなかった…。」 e' *non ce l'ho fatta in tempo*, ed e' la riga della
sua sconfitta (arriva tardi, e `:13890` dice perche': troppo tempo per sfondare
le armi non morte). L'inglese scrive «The time... has yet to come...», cioe' *il
momento non e' ancora arrivato* — un'attesa invece di un fallimento, che nel
posto dove sta capovolge la scena. Si segue il giapponese.

⚠️ DEROGA 4 — `:13870`, その者 NON DIVENTA UN PRONOME.
「その者を通すな」 e' *non fate passare quella persona*; l'inglese scrive «do not
let that adventurer pass». «Non lasciatelo passare» darebbe un genere al
giocatore: resta **«non fate passare quella persona»**.

💡 `:13869` e' una dinamica e l'accordo cade su **lei**, che ha sesso noto:
«come per convincere anche se stessa» e' corretto e non tocca il giocatore.

PERIMETRO: 16 firme su 16 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 13834`). ⭐ E' un blocco **tutto da fare**:
non c'era nessuna riga gia' resa.

MENU: uno, 4 voci — una colonna sola, tetto 58.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    13837: "Mio padre sono riuscita a salvarlo, ma i miei uomini, che ci hanno messo il corpo per farmi passare avanti, ormai...",
    13842: "Padre... dove siete, padre...",
    13845: "Io... non sono riuscita a proteggere niente. Né la missione, né mio padre, né i miei uomini. E nemmeno la mia vita.",
    13851: "Voi che cercate avventura, fermatevi.",
    13856: "Come vedete, adesso questo posto è occupato da noi. Posate subito le armi e lasciate questo piano.",
    13852: "Posate la statuetta e lasciate questo mondo",
    13853: "Passo lo stesso, che vi piaccia o no",
    13854: "Se non mi date dei calzini, faccio un casino",
    13855: "Parliamone e ci capiamo!",
    13860: "...!? Anche voi...",
    13863: "Penserete che siamo allo stremo... ma ci siamo procurati i rifornimenti e siamo di nuovo in condizione di combattere. Chi va all'avventura, da solo, per noi non è un nemico.",
    13866: "L'avvertimento ve l'ho dato. Non c'è altro da dire.",
    13869: "cdatan(CDATAN_NAME, tc) + \" grida, come per convincere anche se stessa.\"",
    13870: "\\\"Tutti quanti, aprite la difesa! Per portare a termine la nostra missione, non fate passare quella persona. Finché il corpo vi regge, combattete!\\\"",
    13888: "Non... sono arrivata in tempo...",
    13890: "Ho perso troppo tempo a sfondare le armi non morte...",
}
