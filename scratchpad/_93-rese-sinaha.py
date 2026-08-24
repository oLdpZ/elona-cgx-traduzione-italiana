# -*- coding: utf-8 -*-
"""93a - SINAHA la gatta della sfortuna (`chat.hsp:10877`-`:10909`, 9 su 11).

《不幸のシナア》 / `<Sinaha>` (`db_card.hsp:6562`, `db_creature.hsp:75023`) e' la
gatta nera che, se la si sveglia, legge al giocatore il suo **grado di
sfortuna** — cioe' 100 meno la Fortuna. Due voci del blocco erano gia' rese e
danno il tono del menu: `:10879` «Leggimi la sfortuna», `:10880` «Scusa.».

⭐⭐⭐ IL PUNTO DEL LOTTO E' LA PARTICELLA ニャ, e non si inventa qui: il
progetto ha gia' deciso come si rende, ed e' **«miao» in coda alla frase**, con
la virgola:

    db_creature.hsp:44182  「おかえりニャン！」   -> «Eccoti, miao~»
    db_creature.hsp:54053  「馬鹿にゃあっ！？」   -> «Che sciocchezza, miao!?»
    db_creature.hsp:56489  「おかえりニャン！」   -> «Che bello riaverti a casa, miao!»

⚠️ Il giapponese la mette **quasi a ogni frase** (undici volte in nove righe) e
l'inglese pure («meow» quattordici volte): non si dirada, perche' e' tutto il
personaggio. Dove il giapponese allunga (ニャア) si allunga anche l'italiano
(«miaao»), come fa gia' `db_creature.hsp:56471` con «Miaao».

LESSICO EREDITATO (non deciso qui):
  - 不幸度   «sfortuna»   chat.hsp:10879, la voce di menu gia' resa
  - ごろごろ  le **fusa**  (il verso del gatto che si crogiola, non «laze»)

⭐ DEROGA 1 — `:10881`, ごろごろ SONO LE FUSA E NON IL PIGRO.
L'inglese scrive «my laze meow»: 「アタシのごろごろ」 e' l'onomatopea delle fusa
del gatto — cioe' quello che il giocatore le sta interrompendo. In italiano
«disturbare le fusa» esiste ed e' esattamente la scena.

⚠️⚠️ DEROGA 2 — I CINQUE VERDETTI NON POSSONO DARE UN GENERE AL GIOCATORE.
Quattro delle cinque battute del responso dicono 「ツイてないやつだ」 /
「ツイてるみたい」, cioe' *sei uno sfortunato* / *sei fortunato*: in italiano il
sostantivo e l'aggettivo predicativo concordano, e sbaglierebbero meta' delle
partite. Si gira sulla **cosa** invece che sulla persona — «che sfortuna da far
pena», «fortuna a palate» — che e' la stessa mossa della guida di stile per la
seconda persona e vale per tutti e cinque i rami.

⚠️ DEROGA 3 — `:10886` E' UNA DINAMICA e porta il numero: la resa e'
un'espressione, non una frase, e il numero resta dov'e' (`hukou`, che il
sorgente calcola come `100 - Fortuna`).

💡 TROVATO NEL VICINATO, NON TOCCATO: il nome di questa creatura in italiano e'
**«<Sinaha>» e basta**, mentre il giapponese e' 《不幸の シナア》 — l'epiteto
«della sfortuna» e' caduto seguendo l'inglese, che scrive solo «<Sinaha>». ⚠️ Il
progetto altrove **ricostruisce** l'epiteto proprio quando l'inglese lo butta:
«<Leiki> la tartaruga nera» (玄武の, inglese «<Leiki>»), «<Alice> la formica
gigante», «<Aribel> la monella», «<Alsapia> la maschera bianca». E' lo stesso
caso, ed e' l'epiteto che spiega **perche' questo personaggio legge la
sfortuna**. Non e' materia di questo lotto — un nome di creatura si cambia con
la sua misura di larghezza e con le rese che lo citano — ma va deciso.

PERIMETRO: 9 firme da fare su 11 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 10877`) e **zero firme gia' rese altrove**.

MENU: uno solo (`:10879`-`:10880`), **gia' reso**: il lotto non lo tocca.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- il risveglio e la richiesta
    10881: 'Mmmiao... Vieni a disturbarmi le fusa: si può sapere che '
           'intenzioni hai, miao?',
    10885: 'E va bene, miao! Se insisti tanto te la leggo, in via '
           'eccezionale, miao. Vediamo un po\'...',
    10886: '"...La tua sfortuna è " + hukou + "!!"',

    # --- i cinque verdetti, dal più sfortunato al più fortunato
    10888: 'Gnahaha! Che sfortuna da far pena, miao.',
    10891: 'Poca fortuna, proprio, miao. A me però diverte, miao.',
    10894: '...Beh, nella norma, miao.',
    10897: 'Fortuna a palate, a quanto pare, miao. Non mi va giù, miaao...',
    10900: 'Non mi va giù, miaao... Proprio per niente, miaao...',

    # --- se ci si scusa e basta
    10905: 'Basta che tu abbia capito, miao. Ti perdono, e adesso sparisci di '
           'là, miao.',
}
