# -*- coding: utf-8 -*-
"""92a - BETHEL (`chat.hsp:13216`-`:13265`, 15 firme).

白き鷹『ヴェセル』 = **«<Bethel> il falco bianco»** (`db_creature.hsp:63303`,
`db_card.hsp:4612`). E' un uomo (`chat.hsp:1652`, «quello scemo di Bethel»,
gia' reso), compagno di **Larnneire**, e in questo blocco lo si incontra nella
**Culla del Caos**: prima che si alleni, poi che si unisce alla battaglia
contro il dio del caos.

LESSICO EREDITATO (non deciso qui):
  - «<Bethel> il falco bianco»   db_creature.hsp:63303
  - ラーネイレ «Larnneire»        chat.hsp:1600, :1649, :7701
  - 決戦因子   «Fattore Decisivo» chat.hsp:10137, :10246, :16253, :16475
  - 神の間     «Sigillo Eterno»   47 siti
  - 凶獣       «la belva»         chat.hsp:10343, :10344, db_card.hsp:1947

REGISTRO: 私 / だ, tono asciutto e cavalleresco, con l'autoironia di chi e'
tornato in campo dopo anni.

⭐⭐⭐ DEROGA 1 — `:13231` E' UN PROVERBIO STORPIATO SUL PROPRIO ANIMALE.
Il giapponese e' 「猫の手ならぬ、鷹の翼も借りたい、といったところか。」: il
modo di dire e' 猫の手も借りたい — *ho talmente da fare che mi farei prestare
perfino le zampe del gatto* — e Bethel ci mette **le ali del falco**, cioe' le
proprie, perche' lui **e' il falco bianco**. E' la stessa figura del bisticcio
di Mary della 90a: la battuta e' nel nome del personaggio.

L'inglese la scioglie in una frase piana («So I guess that makes you rather
short-handed right now... although, all I have to offer are these talons of
mine»): resta il senso, sparisce il proverbio. In italiano il modo di dire
esiste ed e' sulle **braccia**, quindi la stessa mossa si fa senza inventare
niente:

    «Vedo che qui non bastano due braccia. Ci vogliono anche due ali, allora.»

⚠️ DEROGA 2 — `:13228` E `:13258` PORTANO `cdatan(CDATAN_AKA, CHARA_PLAYER)`,
cioe' **l'epiteto** del giocatore, e `decisioni.md` dice che non regge
articoli: la forma che tiene e' l'**apposizione**. Quindi `:13258` diventa
«per caso sei " + AKA + " in persona?», che e' esattamente il modello gia'
deciso, e `:13228` lo usa come vocativo, dove il problema non si pone.

⚠️ DEROGA 3 — `:13224`, L'INGLESE NOMINA QUEL CHE IL GIAPPONESE NON NOMINA.
「まさか目と鼻の先にあったとは」 non dice **che cosa** avesse a un passo:
l'inglese ci mette «the Eternal Seal». La battuta seguente (`:13228`, il `buff`
che sta sopra il menu) e' proprio quella in cui lo scopre — «quello e' il dio
del caos?» — quindi nominarlo prima gli toglie la sorpresa. Resta senza nome.

💡 `:13250` 廃人 e' *chi resta rovinato per sempre*, non «crippled»: si rende
«resterebbe rovinato all'istante», che tiene il definitivo del giapponese.

PERIMETRO: 15 firme su 15 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 13216`). Blocco **tutto da fare**.

MENU: uno, 3 voci — una colonna sola, tetto 58.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    13219: "Larnneire...",
    13258: "\"Tu... per caso sei \" + cdatan(CDATAN_AKA, CHARA_PLAYER) + \" in persona? Che combinazione, trovare una faccia nota in un posto come questo.\"",
    13259: "Finché non avrò ritrovato almeno il colpo d'occhio di una volta, ho intenzione di allenarmi su questo piano. Già adesso mi sento inadeguato, e non è dato sapere quanti piani manchino ancora.",
    13254: "Il Sigillo Eterno, il Fattore Decisivo... C'è qualcosa che non mi torna, in tutto questo. Tanto da farmi esitare ad andare avanti.",
    13224: "Un presentimento mi ha fatto scendere, e chi l'avrebbe detto che fosse a un passo da qui. Credevo ci fossero ancora sessanta piani.",
    13228: "\"...Quello è il dio del caos di cui si sente parlare? \" + cdatan(CDATAN_AKA, CHARA_PLAYER) + \", ti do una mano.\"",
    13225: "Mi sei di grande aiuto!",
    13226: "È pericoloso!",
    13227: "Larnneire e gli altri ti cercavano",
    13231: "Vedo che qui non bastano due braccia. Ci vogliono anche due ali, allora.",
    13234: "Ah... il pericolo lo conosco. Ormai anch'io sono uno che va all'avventura, sia pure l'ultimo della fila.",
    13237: "Larnneire? Mi dispiace per lei, ma dovrà avere pazienza finché non abbiamo sistemato questo!",
    13242: "Adesso mi è parso che qualcosa lo tenesse fermo...",
    13246: "Per quanto gli abbiamo bloccato i movimenti, se poi non riusciamo ad abbatterlo...",
    13250: "Quella è la forza della belva... Un essere umano, a prenderla in pieno, resterebbe rovinato all'istante.",
}
