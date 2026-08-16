# -*- coding: utf-8 -*-
"""Lotto fase4-tcg_custom-001: il **negozio delle carte**, e chiude
`tcg_custom.hsp` per il perimetro `lang()` (70 firme, righe 1710-2244).

Il negozio e' la porta del gioco di carte: ventinove set in vendita, ognuno con
una descrizione lunga e una voce di menu, piu' le battute della negoziante e le
conferme d'acquisto.

⭐⭐⭐ **Si poteva scrivere solo dopo `db_card.hsp`.** Ventisei descrizioni
portano in coda un elenco `[Contains]` di **141 nomi di carta**, e i nomi che il
giocatore legge sulla carta non stavano nel perimetro: stavano in `db_card.hsp`,
il nono punto cieco. Tradurre l'elenco prima avrebbe dato un negozio italiano e
una carta inglese nella stessa partita — la trappola della 53ª. Adesso i nomi
sono gli stessi (`scratchpad/nomi_carte_negozio.py`: 141 su 141 con una resa).

⭐⭐⭐ **RETE 14, nuova: il tetto della finestra del dialogo.** La descrizione
finisce in `buff` e la disegna `chat.hsp:25725`, una riga ogni 19 px a partire da
`wy + 43`, con `talk_conv buff, 53` che manda a capo. I bottoni salgono dal
basso a `wy + 324 - opzioni * 19`: con due opzioni — «Ecco, prendi N biglietti»
e «Non ho abbastanza da scambiare» — il primo bottone sta a 286, e l'ultima riga
che ci sta tutta e' la **dodicesima**. Oltre, il testo va a sbattere sui bottoni.

⚠️⚠️ **E l'inglese e' GIA' al soffitto**: otto descrizioni su ventinove ne
occupano esattamente **dodici su dodici** (`scratchpad/chat_righe.py`). L'italiano
e' in media il 10-15% piu' lungo dell'inglese: per un terzo del negozio il
margine per una resa letterale era **zero**, e la prosa si e' dovuta stringere.
Non e' una licenza: e' il vincolo del sito. La rete 14 lo misura sulla resa
**prima** che il testo arrivi a schermo, invece di scoprirlo al collaudo.

⚠️ **I blocchi di effetto restano INGLESI, ed e' una scelta.** Due descrizioni
citano l'effetto della carta parola per parola:

    tcg_custom.hsp:1956   "Battlecry/OnKill: Kyu-bi gives you a Fried Tofu."
    tcg_mod.hsp:2268      effdesc@tcg(TCG_EFF_KYUBI) = la stessa frase

Sono **copie a mano** di `effdesc@tcg`, cioe' delle 835 descrizioni di effetto
dell'ottavo punto cieco, che sono ancora inglesi e si leggono su ogni carta.
Tradurre la copia lascerebbe il negozio a dire una cosa e la carta un'altra.
💡 E questo e' un debito **accoppiato**: quando `effdesc@tcg` si traduce, queste
due citazioni vanno riscritte nello stesso momento, o divergono in silenzio.
Vale anche per la parola chiave `'Trample'`, che qui resta come la carta la
scrive.
⚠️ Eccezione: `Bleeding` **si traduce**, perche' non e' una parola di `effdesc`
ma uno **stato**, e `command.hsp` lo rende gia' «Sanguinamento» nella scheda del
personaggio: il giocatore quella parola la legge in italiano da mesi.

⭐ **L'elenco `[Contiene]` porta i nomi NUDI, senza articolo**, perche' davanti
ha un numerale: « 1 scheletro guerriero». Sulla carta il nome porta l'articolo
(«lo scheletro guerriero»), come vuole `contratto-nomi.md` §4, e le due forme si
riconoscono a vista. E' il rovescio della decisione del lotto `db_card-001`: la'
il nome entra nelle frasi del gioco e l'articolo serve, qui sta dietro un numero
e l'articolo sarebbe sbagliato.

⚠️ **Il conto dell'elenco e' stato controllato contro il codice, non creduto**:
`scratchpad/nomi_carte_negozio.py` confronta le carte dichiarate in prosa con
quelle che `cardsetcontent@tcg` concede davvero — **0 divergenze su 23 elenchi**.

⚠️ **Un refuso di monte non ricalcato**: `:2086` scrive «an Asterious», che e'
`Asterius`. La resa scrive il nome giusto, come la 53ª col «2 copy» singolare.

⚠️ **Due nomi propri diversi da come li chiama il negozio**: la carta di Kyu-bi
si chiama «<Nove Code Dorate>» (`db_card.hsp`), non «Kyu-Bi», e quella della
recluta «la recluta», non «avventuriero alle prime armi». Le voci di menu usano
il nome della **carta**, cosi' chi legge il menu e chi guarda la carta leggono
la stessa parola.

⚠️ **La rete degli accenti non distingue una virgoletta di CHIUSURA dopo una
vocale da un accento degradato.** `'Trample'` e `'proiettile'` — le virgolette
d'enfasi che l'inglese usa — finiscono con `e'`, che e' esattamente la forma che
`ha_apostrofo_scritto_a_mano` cerca (`accenti.py:61`). Sono due falsi positivi
veri, e la rete ha comunque ragione a esserci: cosi' com'e', non puo' sapere se
quell'apostrofo chiude una citazione o e' una `è` scritta male. La resa toglie
le virgolette invece di indebolire la rete — l'enfasi era decorazione, la
garanzia no. 💡 Le altre citazioni del negozio passano perche' chiudono dopo una
consonante o un segno: `'poker'`, `'…vecchietto.'`, `'…rosa?'`.

💡 **Le voci di menu del set: «[Set blu]», non «[Blue Card Set]».** I domini sono
gia' fissati dal lotto `tcg_mod-001` (BLU VERDE BIANCO NERO ROSSO GRIGIO), e la
voce di menu ha un tetto suo — la colonna delle opzioni parte da `wx + 166` su
una finestra di 600, cioe' una settantina di caratteri a font 12. «[Set di carte
blu]» ci starebbe, ma la piu' lunga («Il gran teatro delle spettacameriere»)
arriverebbe al bordo: «[Set blu]» lascia margine e dice la stessa cosa.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata
from pathlib import Path

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg_custom.hsp'
ESTRAZIONE = 'lavoro/_tcg_custom.jsonl'
USCITA = 'lavoro/fase4-tcg_custom-001.jsonl'

LARGHEZZA_CHAT = 53
TETTO_RIGHE = 12

P = 'cardprice@tcg(currentthing@tcg)'

RESE = {
    # ---------------------------------------------------------- la negoziante
    # Miches, la gatta di Vernis. たらばがに e' il granchio reale, ma l'inglese
    # ha scelto «coconut crab», che `db_item.hsp` rende «granchio del cocco»:
    # la resa segue l'inglese e riusa la parola che il gioco ha gia'.
    (1710, '\\"Mewmewmew? Coconut crab!\\"'):
        '\\"Miao miao miao? Granchio del cocco!\\"',
    (1725, '\\"Mew?\\"'):
        '\\"Miao?\\"',

    # ------------------------------------------------- l'ingresso del negozio
    (1899, "We aren't selling physical cards. You need to bring a Deck to redeem the card codes."):
        'Non vendiamo carte vere e proprie. Per riscattare i codici serve un mazzo.',
    (1909, "Here's a list of redeemable card sets."):
        "Ecco l'elenco dei set che puoi riscattare.",

    # ⚠️ «Card of » + nome diventa «Carta: » + nome, non «Carta di »: il nome
    # porta l'articolo e «Carta di la zanzara gigante» non si puo' scrivere.
    # E' la rete 8 applicata a mano, su una funzione che la rete non conosce.
    (1917, '[ Tickets] Card of .'):
        '"[" + ' + P + ' + " biglietti] Carta: " + carddailyt@tcg(cnt) + "."',

    # ------------------------------------------------------------- la recluta
    (1926, "These cards, depicting a random 'Novice' Adventurer of varying race, class, stats, "
           "and abilities each game, can be stuffed into your deck to your heart's content. "
           "After all, what could possibly be more wholesome than amassing a collection of "
           "countless, indistinguishable, generic adventurers? Certainly not any alternative "
           "that might be even remotely unsettling, right?"):
        'Queste carte ritraggono una recluta presa a caso: razza, classe, valori e abilità '
        'cambiano a ogni partita. Tecnicamente sono carte diverse, quindi puoi infilarne nel '
        'mazzo quante ne vuoi. E del resto, cosa c\'è di più sano che collezionare una folla '
        'di avventurieri qualunque, tutti identici e tutti anonimi? Di sicuro niente di anche '
        'solo vagamente inquietante, vero?',
    (1928, '[ Tickets] Card of a novice adventurer.'):
        '"[" + ' + P + ' + " biglietti] Carta della recluta."',

    # -------------------------------------------------------------- <Yonorne>
    (1936, 'Card of Yonorne, she does her best to guide people with her natural cheerfulness...?'):
        'Carta di <Yonorne>: fa del suo meglio per guidare la gente con quel buonumore che si '
        'ritrova... credo?',
    (1938, '[ Tickets] Card of Yonorne, the Rookie Guide.'):
        '"[" + ' + P + ' + " biglietti] Carta di <Yonorne>, la guida novellina."',

    # -------------------------------------------------- <Misterioso Produttore>
    # L'elenco qui e' `[Targets…]`, i BERSAGLI dell'effetto, non il contenuto
    # del pacchetto: il pacchetto contiene una carta sola.
    (1946, "Card of some shady 'Mysterious Producer' guy, he's got the power to help those "
           "Roran folks in your deck reach their full potential, even if half the people out "
           "there can't stand his guts. Isn't that just peachy?\\n[Targets the following "
           "cards:]\\nLittle Girl\\nYoung Lady\\nYounger Sister\\nOlder Sister\\nGwen the Innocent."):
        'Carta di un tale <Misterioso Produttore>, tipo poco raccomandabile: ha il potere di '
        'far sbocciare i roran del tuo mazzo, anche se mezzo mondo non lo sopporta. Bello, no?'
        '\\n[Bersaglia queste carte:]\\nbambina\\ngiovane dama\\nsorella minore\\nsorella '
        'maggiore\\n<Gwen> l\'innocente.',
    (1948, '[ Tickets] Card of a Mysterious Producer.'):
        '"[" + ' + P + ' + " biglietti] Carta del <Misterioso Produttore>."',

    # ----------------------------------------------------- <Nove Code Dorate>
    # ⚠️ Il blocco degli effetti resta inglese: e' copia di `effdesc@tcg`.
    (1956, "Card of a Foxgod with nine fluffy tails. It is apparently difficult to move each "
           "tail separately. You ask me why the 'Golden Nine-Tail' is blue? Well, that's the "
           "issue of your beautify pack. \\n\\n Kyu-Bi:\\n  Battlecry/OnKill: Kyu-bi gives you "
           "a Fried Tofu. \\n\\n Fried Tofu: \\n  Battlecry: Feed the Fried Tofu to 1 of your "
           "Card, and give it the Tofu's stats."):
        'Carta di un dio volpe con nove code morbidissime. Muoverle una per una, dicono, non è '
        'affatto semplice. Mi chiedi perché le <Nove Code Dorate> sono blu? Quello è un '
        'problema del tuo pacchetto di bellezza. \\n\\n Kyu-Bi:\\n  Battlecry/OnKill: Kyu-bi '
        'gives you a Fried Tofu. \\n\\n Fried Tofu: \\n  Battlecry: Feed the Fried Tofu to 1 '
        'of your Card, and give it the Tofu\'s stats.',
    (1958, '[ Tickets] Card of a Golden Nine-Tail.'):
        '"[" + ' + P + ' + " biglietti] Carta delle <Nove Code Dorate>."',

    # ------------------------------------------------------------ <Kamikakushi>
    (1966, "Card of a spirit paper ninja summoned via an obscure papercraft curse technique, "
           "whose name is too cumbersome to recall, leaving it largely unknown.\\n\\n "
           "Kamikakushi:\\n  Battlecry: Turn every Card in your Hand into kamikaze paper "
           "bombs. \\n\\n Paper Bomb: \\n  Battlecry: Deal 3 Dmg to Target and Draw 1 Card."):
        'Carta di un ninja di carta evocato con un\'arte segreta poco nota, dal nome talmente '
        'lungo che nessuno se lo ricorda.\\n\\n Kamikakushi:\\n  Battlecry: Turn every Card in '
        'your Hand into kamikaze paper bombs. \\n\\n Paper Bomb: \\n  Battlecry: Deal 3 Dmg to '
        'Target and Draw 1 Card.',
    (1968, '[ Tickets] Card of Super-Secret-Papercraft-Spirit-Familiar <KamiKakushi>.'):
        '"[" + ' + P + ' + " biglietti] Carta del dio-di-carta-piegata-segretissimo '
        '<Kamikakushi>."',

    # ------------------------------------------------------------------ <Aime>
    (1976, "Card of a mysterious narrator - Aime. She said that she possesses the ability to "
           "connect worlds of possibility through children's card games.\\n\\nWell, what "
           "happens is, if you put her in your deck, she replaces your entire deck with "
           "someone else's deck when the duel begins, pretty annoying, but some weird dudes "
           "might be into that kind of stuff."):
        'Carta di una narratrice misteriosa: <Aime>. Dice di saper collegare mondi possibili '
        'attraverso i giochi di carte per bambini.\\n\\nQuel che succede è che, se la metti '
        'nel mazzo, all\'inizio del duello ti scambia tutto il mazzo con quello di qualcun '
        'altro. Fastidioso, ma c\'è gente strana a cui piace.',
    (1978, '[ Tickets] Card of a Mysterious Storyteller.'):
        '"[" + ' + P + ' + " biglietti] Carta della narratrice misteriosa."',

    # ---------------------------------------------------------------- <Rianna>
    (1986, "Card of a legendary gambler - Rianna. While messing around with her life, she "
           "accidentally stumbles into the underground world of gambling on children's card "
           "games, but uses her memory and insight to turn the tables and win at gambling, "
           "thus surviving. \\n\\nWhen putted into your deck, she plays the game for you - for "
           "the first few turns, pretty neat, huh?"):
        'Carta di una giocatrice leggendaria: <Rianna>. Girovagando senza meta è finita per '
        'caso nel mondo sommerso delle scommesse sui giochi di carte per bambini, e con '
        'memoria e intuito ha ribaltato il tavolo, vinto e tirato avanti. \\n\\nSe la metti '
        'nel mazzo, per i primi turni gioca lei al posto tuo. Mica male, eh?',
    (1988, '[ Tickets] Card of a Legendary Gambler.'):
        '"[" + ' + P + ' + " biglietti] Carta della giocatrice leggendaria."',

    # ------------------------------------------------------------------ poker
    (1996, "I recently came into possession of a rather... unusual deck of 52 cards, called "
           "'poker' apparently. I have no particular interest in playing this game myself, but "
           "it seems to be quite the collectors' item. So, in an effort to clear some space, "
           "I've decided to sell bundles containing a single copy of each suit from this deck. "
           "Fancy a set, perchance? \\n[Contains]\\n 1 Spade Warrior.\\n 1 Club Feather.\\n "
           "1 Diamond Eyes.\\n 1 Heart Witch."):
        'Mi è capitato tra le mani un mazzo piuttosto... insolito: 52 carte, si chiama '
        '\'poker\', a quanto pare. Giocarci non mi interessa, ma tra i collezionisti va forte. '
        'Così, per fare spazio, ho deciso di venderlo a mazzetti: una carta per ogni seme. Ne '
        'prendi uno?\\n[Contiene]\\n 1 guerriero di picche.\\n 1 piuma di fiori.\\n 1 occhi di '
        'quadri.\\n 1 strega di cuori.',
    (1998, '[ Tickets][Card Set] 1/13 of a Poker Deck'):
        '"[" + ' + P + ' + " biglietti][Set] 1/13 di un mazzo da poker"',

    # -------------------------------------------------- soldati oscuri arcobaleno
    (2006, "Oh, let me introduce you to the Rainbow Dark Guardians of Irva, the sentai team "
           "for all the lovely evil dudes out there. Now, I know what you're thinking: 'Hey, "
           "wait a second! Where are the Yellow and Pink Dark Guardians?' Well, apparently, "
           "those two just couldn't keep up with the rest of the team's... villainous fervor. "
           "It's a shame, really - I bet they had great color coordination. \\n[Contains]\\n "
           "1 Crimson Dark Guardian\\n 1 Blue Dark Guardian\\n 1 Green Dark Guardian."):
        'Oh, ti presento i Soldati oscuri arcobaleno di Irva, la squadra sentai di tutti i cari '
        'cattivi. Lo so cosa stai pensando: \'Un attimo! E il Soldato oscuro giallo e quello '
        'rosa?\' Ecco, a quei due la foga malvagia del resto della squadra non stava dietro. Un '
        'peccato: i colori li avevano coordinati bene.\\n[Contiene]\\n 1 soldato oscuro '
        'cremisi\\n 1 soldato oscuro blu\\n 1 soldato oscuro verde.',
    (2008, '[ Tickets][Card Set] Rainbow Dark Guardians'):
        '"[" + ' + P + ' + " biglietti][Set] Soldati oscuri arcobaleno"',

    # ------------------------------------------------------------------ squali
    (2016, "Oh, these bad boys? Can't be stopped by any non-blue card, they can't. No, no, no "
           "- you see, they've got a special talent for trading health, almost as good as the "
           "real thing. Quite impressive, really.\\n[Contains]\\n 1 SP Champion. (800% Value!)"
           "\\n 1 Abyss Animal\\n 2 Flight Fish\\n 1 Nightmare Shark\\n 1 Raging Shark\\n "
           "1 Captain Shark\\n 1 Orcinus Orca"):
        'Ah, questi bestioni? Nessuna carta che non sia blu li ferma, no signore. E hanno un '
        'talento speciale per barattare punti vita, quasi come quelli veri. Notevole.'
        '\\n[Contiene]\\n 1 SP Champion. (valore 800%!)\\n 1 creatura dei fondali\\n 2 pesci '
        'volanti rapaci\\n 1 squalo incubo\\n 1 squalo furioso\\n 1 squalo capitano\\n '
        '1 demone marino Orcinus',
    (2018, '[ Tickets][Blue Card Set] Shark Trade.'):
        '"[" + ' + P + ' + " biglietti][Set blu] Baratto di squali."',

    # ------------------------------------------------------------ fuochi fatui
    (2026, "Oh joy, wisps. Those delightful little creatures that just love to stun lock your "
           "opponent into oblivion. And the best part? They replicate like there's no "
           "tomorrow, quickly flooding the board.\\n[Contains]\\n 1 Clouddragon. \\n 1 Cloud "
           "Beast. \\n 2 Electric Clouds.  1 Chaos Cloud.\\n 1 Wisp.  1 Demon's Soul.\\n "
           "1 Kesalanpatharan."):
        'Che gioia, i fuochi fatui. Quelle creaturine adorabili che non aspettano altro che '
        'bloccare l\'avversario nel torpore. E la parte migliore? Si duplicano come se non ci '
        'fosse un domani, e il campo si riempie in fretta.\\n[Contiene]\\n 1 nuvoldrago. \\n '
        '1 bestia di nuvola. \\n 2 nubi elettriche.  1 nube del caos.\\n 1 fuoco fatuo.  '
        '1 anima del demone.\\n 1 kesaranpasaran.',
    (2028, '[ Tickets][Blue Card Set] Eye of the Typhoon.'):
        '"[" + ' + P + ' + " biglietti][Set blu] Occhio del tifone."',

    # -------------------------------------------------------------------- Yith
    (2036, "Experience the insanity from the Great Race of Yith, as their reality-warping "
           "power takes over the duels - take over your opponent's monsters, at least."
           "\\n[Contains]\\n 1 King in Yellow.\\n 1 Spiral King.\\n 1 Great Race of Yith\\n "
           "2 Shub Niggurath.\\n 1 Shoggoth.\\n 1 Missionary of Darkness\\n 1 Cthulhick (Cute)."):
        'Prova la follia della Grande Razza di Yith: il loro potere che piega la realtà si '
        'impadronisce del duello - o almeno dei mostri dell\'avversario.\\n[Contiene]\\n 1 Re '
        'in Giallo.\\n 1 re della spirale.\\n 1 Grande Razza di Yith\\n 2 Shub-Niggurath.\\n '
        '1 shoggoth.\\n 1 missionario dell\'oscurità\\n 1 cthulhick (tenero).',
    (2038, '[ Tickets][Blue Card Set] Forbidden Fun.'):
        '"[" + ' + P + ' + " biglietti][Set blu] Divertimento proibito."',

    # --------------------------------------------------------------------- ent
    (2046, "Treants, fueled by the very essence of the forest itself. They're resilient little "
           "things, I'll give them that. But goodness help you if they're powered by that "
           "Skogsras fellow - then they're absolutely ferocious. It's like giving a teddy bear "
           "a bunch of energy drinks and telling it to go wild.\\n[Contains]\\n 1 Skogsra "
           "(it's cute).\\n 1 Alraune (also cute).\\n 2 Fire Ents (not so cute).\\n 2 Ice Ents. "
           "1 Grand Ent.\\n 1 Hinocchio."):
        'Ent, alimentati dall\'essenza stessa della foresta. Resistenti, questo glielo '
        'concedo. Ma se li muove quel tale skogsra, diventano feroci: come dare a un '
        'orsacchiotto una cassa di energetici e dirgli di scatenarsi.\\n[Contiene]\\n 1 skogsra '
        '(tenero).\\n 1 alraune (anche lei).\\n 2 ent di fuoco (meno teneri).\\n 2 ent di '
        'ghiaccio. 1 albero del mondo.\\n 1 Pinocipresso.',
    (2048, '[ Tickets][Green Card Set] Living Forest.'):
        '"[" + ' + P + ' + " biglietti][Set verde] Foresta vivente."',

    # -------------------------------------------------------------------- orsi
    # 💡 «Bear with me» e' un gioco di parole fra «abbi pazienza» e «orso»:
    # «Pazienza da orsi» tiene tutt'e due i sensi con le stesse due parole.
    (2056, "Oh, bears! Everyone's favorite cuddly bruins. I used to have one as a pet, can you "
           "believe it? Gentle giants, until you go and threaten their little ones in battle. "
           "It's downright adorable... if you don't mind the potential mauling, that is."
           "\\n[Contains]\\n 1 Dobiel.\\n 1 Panda (very rare!).\\n 1 Arktouros.\\n 1 Dark "
           "Koala.\\n 2 Brown Bears.\\n 2 Grizzlies."):
        'Oh, gli orsi! I cucciolotti preferiti da tutti. Ne avevo uno anch\'io, ci credi? '
        'Giganti buoni, finché non minacci i loro piccoli in battaglia. Adorabile... se non ti '
        'dispiace il rischio di finire sbranato.\\n[Contiene]\\n 1 Dobiel.\\n 1 panda gigante '
        'redivivo (rarissimo!).\\n 1 Arcturus.\\n 1 koala mangiabuio.\\n 2 orsi bruni.\\n '
        '2 grizzly.',
    (2058, '[ Tickets][Green Card Set] Bear with me.'):
        '"[" + ' + P + ' + " biglietti][Set verde] Pazienza da orsi."',

    # ----------------------------------------------------------------- Ganesha
    (2066, "Unleash destruction with the 'Trample' cards! Lead the charge with Ganesa, pierce "
           "through even the toughest defenses.\\n[Contains]\\n 1 Ganesa.\\n 1 Kirin.\\n "
           "1 Tyrannobreaker. \\n 1 Cerberus. \\n 1 Zilla. \\n 2 Mammoths. \\n 1 Big Mosquito."):
        'Scatena la distruzione con le carte Trample! Guida la carica con Ganesha e sfonda '
        'anche le difese più solide.\\n[Contiene]\\n 1 Ganesha.\\n 1 Kirin.\\n 1 tiranno '
        'demolitore. \\n 1 Cerbero. \\n 1 zilla. \\n 2 mammut. \\n 1 zanzara gigante.',
    (2068, '[ Tickets][Green Card Set] Ganesa Impact.'):
        '"[" + ' + P + ' + " biglietti][Set verde] Impatto Ganesha."',

    # ------------------------------------------------------------------- yeek
    (2076, "Ah, Yeeks - the bane of the Fighter's Guild's existence. These pests come in "
           "swarms, ruining everything in their path like a horde of tiny, destructive "
           "tornados. And the worst part? They're so common, you can hardly give away their "
           "card set, even at the bargain basement price of 800 tickets.\\n[Contains]\\n "
           "1 Master Yeek. \\n 2 Yeeks. \\n 2 Yeek Warriors. \\n 2 Yeek Archers. \\n "
           "1 Kamikaze Yeek."):
        'Ah, gli yeek: la sciagura della Gilda dei Guerrieri. Arrivano a sciami e rovinano '
        'tutto quel che incontrano, come una mandria di tornado in miniatura. E la parte '
        'peggiore? Sono così comuni che il loro set non lo regali nemmeno, al prezzo di saldo '
        'di 800 biglietti.\\n[Contiene]\\n 1 yeek maestro. \\n 2 yeek. \\n 2 yeek guerrieri. '
        '\\n 2 yeek arcieri. \\n 1 yeek kamikaze.',
    (2078, '[ Tickets][Gray Card Set] Yeeeeeeks!.'):
        '"[" + ' + P + ' + " biglietti][Set grigio] Yeeeeeeek!."',

    # -------------------------------------------------------------- minotauri
    (2086, "Minotaurs, the bull-headed terrors of the maze. Let me tell you, their hitting "
           "power is no joke - I once had the misfortune of facing an Asterious with Trample "
           "and 35+ attack... (That card is not in the set.)\\n[Contains]\\n 1 Minotaur King. "
           "\\n 1 Steel Minotaur. \\n 1 Minotaur Magician. \\n 1 Minotaur Boxer. \\n "
           "2 Minotaurs. \\n (Bonus) 2 Cattles."):
        'I minotauri, il terrore cornuto del labirinto. Lascia che ti dica: picchiano sodo. Una '
        'volta ho avuto la sfortuna di trovarmi davanti un Asterius con Trample e 35 e passa '
        'di attacco... (Quella carta nel set non c\'è.)\\n[Contiene]\\n 1 minotauro re. \\n '
        '1 toro d\'acciaio. \\n 1 minotauro mago. \\n 1 minotauro pugile. \\n 2 minotauri. \\n '
        '(in regalo) 2 bovini.',
    (2088, '[ Tickets][Gray Card Set] Hazy Maze Days.'):
        '"[" + ' + P + ' + " biglietti][Set grigio] Giorni di nebbia nel labirinto."',

    # ------------------------------------------------------------------ arpie
    (2096, "Ahoy, harpies, I got them, you love them. Bleed your foes dry with these feisty "
           "fowl! Watch as they strip your opponent's life points away - via Bleeding."
           "\\n[Contains]\\n 1 Black Wing.\\n 1 Alkonost.\\n 1 Mayu Sibaru.\\n 1 Space Horned "
           "Owl.\\n 2 Bird Archers.\\n 2 Harpies."):
        'Ehilà, le arpie: io le ho, tu le adori. Dissangua i nemici con questi pennuti '
        'bellicosi! Guarda come scippano i punti vita all\'avversario - a furia di '
        'Sanguinamento.\\n[Contiene]\\n 1 ala nera.\\n 1 alkonost.\\n 1 mayu sibayu.\\n 1 gufo '
        'spaziale.\\n 2 arcieri alati.\\n 2 arpie.',
    (2098, '[ Tickets][Gray Card Set] Black Feathers.'):
        '"[" + ' + P + ' + " biglietti][Set grigio] Piume nere."',

    # -------------------------------------------------------- spettacameriere
    (2106, "Performaids - the cruel, bloodthirsty entertainers of the Mansion. They'll have "
           "you dancing to their tune, quite literally, as they seize control of the field "
           "with an iron fist. And would you look at that, their high demand means they come "
           "at a premium price of 4000 tickets.\\n[Contains]\\n 1 Performaid Pinchief. \\n "
           "1 Performaid Desweeper. \\n 1 Performaid Cocruel. \\n 1 Performaid Bloodress. \\n "
           "1 Performaid Bitchiack."):
        'Le spettacameriere: le intrattenitrici crudeli e sanguinarie della Villa. Ti faranno '
        'ballare al loro ritmo, letteralmente, mentre prendono il campo col pugno di ferro. E '
        'guarda un po\': tanta richiesta si paga, 4000 biglietti.\\n[Contiene]\\n '
        '1 spettacameriera pinzacapo. \\n 1 spettacameriera spazzamorte. \\n '
        '1 spettacameriera cuocrudele. \\n 1 spettacameriera vestisangue. \\n '
        '1 spettacameriera stregaccia.',
    (2108, '[ Tickets][Red Card Set] Performaid Grand Theatre.'):
        '"[" + ' + P + ' + " biglietti][Set rosso] Il gran teatro delle spettacameriere."',

    # ----------------------------------------------------------------- rocce
    (2116, "Oh, are you in the market for some explosive fun? Tired of those pesky bards with "
           "their annoying draw effects? Well, fear not! Just lob one of these rocks onto the "
           "field, and BAM! - no more bard to bother you. Trust me, you'll learn to love the "
           "sweet, sweet sound of destruction.\\n[Contains]\\n 1 Mag Count. \\n 1 Blue Moai.  "
           "1 Moai. \\n 1 Cluster Bomb Rock. \\n 2 Giga Bomb Rocks. 2 Bomb Rocks."):
        'Cerchi qualcosa di esplosivo? Stanco di quei menestrelli fastidiosi con i loro effetti '
        'di pesca? Nessun timore! Scaraventa una di queste rocce sul campo e BAM! - nessun '
        'menestrello a darti noia. Fidati, imparerai ad amare il dolce suono della '
        'distruzione.\\n[Contiene]\\n 1 conte magnetico. \\n 1 moai blu.  1 moai. \\n 1 roccia '
        'esplosiva a grappolo. \\n 2 rocce esplosive al deuterio. 2 rocce esplosive.',
    (2118, '[ Tickets][Red Card Set] Rock and Roll.'):
        '"[" + ' + P + ' + " biglietti][Set rosso] Rock and roll."',

    # ------------------------------------------------------------- X-Mutanti
    (2126, "Introducing the All New X-Mutants! These genetic marvels bring a whole new level "
           "of chaos to the battlefield. (They suffer extreme emotional and physical pain due "
           "to Ether Disease.)\\n[Contains]\\n 1 Chaoshaprincess ZEHLS\\n 1 Chaoshaprincess "
           "CHRDH\\n 1 Chaoshaprincess FWBS\\n 1 Chaoshaprincess MEM\\n 1 Etherian\\n 1 Big "
           "Sister\\n 2 Mutant."):
        'Ecco a te i nuovissimi X-Mutanti! Queste meraviglie genetiche portano sul campo di '
        'battaglia un livello di caos mai visto. (Soffrono dolori atroci, nel corpo e '
        'nell\'animo, per la malattia dell\'etere.)\\n[Contiene]\\n 1 principessa ibrida '
        '<salma celeste>\\n 1 principessa ibrida <bestia e piuma>\\n 1 principessa ibrida '
        '<insetto e verme>\\n 1 principessa ibrida <fiore e spora>\\n 1 eteriano\\n 1 Big '
        'Sister\\n 2 mutanti.',
    (2128, '[ Tickets][Red Card Set] All New X-Mutants.'):
        '"[" + ' + P + ' + " biglietti][Set rosso] I nuovissimi X-Mutanti."',

    # ------------------------------------------------------------------ zombi
    (2136, "It is the Night of the Dead! The zombies are rising, and they're hungry for... "
           "cards? \\nYour opponent will have one heck of a time trying to eliminate these "
           "undead horrors. After all, how do you kill something that's already dead?"
           "\\n[Contains]\\n 1 Hel. \\n 1 Master Lich. 1 Lich. \\n 1 Coffin. \\n 1 Mummy. "
           "1 Zombie. \\n 1 Skeleton.  1 Living Armor."):
        'È la Notte dei Morti! Gli zombi si rialzano e hanno fame di... carte? \\nIl tuo '
        'avversario se la vedrà brutta a far fuori questi orrori. Del resto, come si uccide '
        'una cosa che è già morta?\\n[Contiene]\\n 1 Hel. \\n 1 lich maestro. 1 lich. \\n '
        '1 sarcofago antico. \\n 1 mummia. 1 zombi. \\n 1 scheletro guerriero.  '
        '1 armatura vivente.',
    (2138, '[ Tickets][Black Card Set] Hell on Earth'):
        '"[" + ' + P + ' + " biglietti][Set nero] L\'inferno in terra"',

    # ------------------------------------------------------------------ vermi
    (2146, "Here's a fun little paradox for you - meet the Worm Cards! These devious critters "
           "pop up whenever you destroy them in your own deck! ...Just try not to mill too "
           "much and deck out yourself first, hmm?\\n[Contains]\\n 1 Mega Gordian Worm. \\n "
           "1 Dragon Centipede \\n 1 Fire Centipede.  2 Centipedes. \\n 1 Sand Worm.  1 Rock "
           "Worm. \\n 1 Dhole."):
        'Ecco un bel paradosso: le carte Verme! Questi bricconi saltano fuori ogni volta che '
        'li distruggi nel tuo mazzo! ...Cerca solo di non macinare troppo e restare a secco '
        'per primo, eh?\\n[Contiene]\\n 1 gordio grossissimo. \\n 1 millepiedi drago argenteo '
        '\\n 1 millepiedi di fuoco.  2 millepiedi. \\n 1 verme delle sabbie.  1 verme '
        'proiettile. \\n 1 dhole.',
    (2148, '[ Tickets][Black Card Set] Lightsworm'):
        '"[" + ' + P + ' + " biglietti][Set nero] Vermi di luce"',

    # ----------------------------------------------------------------- scacchi
    (2156, "'Chess can't be that serious, nobody in Irva plays it anymore except for some old "
           "geezer.' But I'll tell ya, that red-haired fella in Vernis is into chess, and you "
           "better not let him hear you say that.\\n[Contains]\\n 1 Grandmaster.\\n 1 <King>.  "
           "1 <Queen>.  \\n 1 <Bishop>.  1 <Knight>.  \\n 1 <Rook>.  2 <Pawn>s."):
        '\'Gli scacchi non saranno mica una cosa seria, in Irva non ci gioca più nessuno a '
        'parte qualche vecchietto.\' Però io ti dico: quel tipo dai capelli rossi a Vernis ci '
        'gioca, e meglio che non ti senta.\\n[Contiene]\\n 1 <Gran Maestro>.\\n 1 <Re>.  '
        '1 <Regina>.  \\n 1 <Alfiere>.  1 <Cavallo>.  \\n 1 <Torre>.  2 <Pedone>.',
    (2158, '[ Tickets][Black Card Set] Checkmate da!'):
        '"[" + ' + P + ' + " biglietti][Set nero] Scacco matto, eh!"',

    # ----------------------------------------------------------------- Yerles
    (2166, "Ooh, Military Promotion Cards, courtesy of the Yerles Army. You know, those folks "
           "who just love churning out rank-and-file planes and tanks like it's nobody's "
           "business. \\n[Contains]\\n 1 Yerles Latest Outfit Soldier.\\n 2 Yerles Combat "
           "Plane. \\n 1 Yerles Infantry.  1 Yerles Elite Infantry. \\n 1 Security System.  "
           "1 Yerles Self-Propelled Gun. \\n 1 Putit Tank."):
        'Ooh, le carte di propaganda militare, per gentilezza dell\'esercito di Yerles: quelli '
        'che adorano sfornare aerei e carri armati a nastro.\\n[Contiene]\\n 1 soldato Yerles '
        'di nuovo modello.\\n 2 velivoli da combattimento Yerles. \\n 1 fanteria meccanica '
        'Yerles.\\n 1 fanteria meccanica scelta Yerles. \\n 1 sistema di difesa di Yerles.\\n '
        '1 cannone semovente di Yerles. \\n 1 putit corazzato.',
    (2168, '[ Tickets][White Card Set] Machine Force'):
        '"[" + ' + P + ' + " biglietti][Set bianco] Forza meccanica"',

    # ------------------------------------------------------------------- Elea
    (2176, "I lost my mother due to those wretched Eleas, and I'll never forgive them for it. "
           "So do me a favor, would you? Save your tickets and steer clear of these "
           "overpriced, underperforming duds.\\n[Contains]\\n 1 Mob of Elea.  1 Avenger of "
           "Elea. \\n 2 Refugees. \\n 1 Warrior of Elea.  1 Wizard of Elea. \\n 1 Knight of "
           "Elea.  1 Sage of Elea."):
        'Ho perso mia madre per colpa di quei maledetti Elea, e non li perdonerò mai. Quindi '
        'fammi un favore: tieniti i biglietti e sta\' lontano da queste ciofeche '
        'sopravvalutate.\\n[Contiene]\\n 1 rivoltoso degli Elea.  1 vendicatore degli Elea. '
        '\\n 2 profughi degli Elea. \\n 1 guerriero di Elea.  1 mago di Elea. \\n '
        '1 spadaccino magico degli Elea.\\n 1 gran saggio degli Elea.',
    (2178, '[ Tickets][White Card Set] Elea Remnants'):
        '"[" + ' + P + ' + " biglietti][Set bianco] I resti degli Elea"',

    # --------------------------------------------------------------- Eulderna
    (2186, "Ah, the Euldernas - those wizards with their infamous Wizard's Gathering Magic. "
           "Their mastery over card advantage is nothing short of astounding. \\n[Contains]\\n "
           "1 Eulderna Summonknight. \\n 1 Scholar. \\n 2 High Magicians. \\n 1 Magic Archer. "
           "\\n 1 Necro Doll.  2 Puppets."):
        'Ah, gli Eulderna: quei maghi con la loro famigerata Magia dell\'Adunanza. La '
        'padronanza del vantaggio di carte è, non esagero, sbalorditiva.\\n[Contiene]\\n '
        '1 cavaliere evocatore di Eulderna. \\n 1 erudito. \\n 2 alti incantatori. \\n '
        '1 arciere magico di Eulderna. \\n 1 necrobambola.  2 marionette.',
    (2188, '[ Tickets][White Card Set] Magic of Gathering'):
        '"[" + ' + P + ' + " biglietti][Set bianco] Magia dell\'Adunanza"',

    # ------------------------------------------------------------------ Juere
    (2196, "Oh, the Jueres - that kingdom with their big talk of Revolution and Liberation. "
           "Personally, I find they're a tad over-obsessed with bandits and rogues. I mean, "
           "half their card pool? Rogues and bandits.\\n[Contains]\\n 1 Rogue Boss.  1 Rogue "
           "Warrior. \\n 1 Rogue Wizard.  1 Rogue Archer. \\n 1 Bard.  1 Thief. \\n 1 Juere "
           "Infantry.  1 Juere Swordman."):
        'Oh, i juere: quel regno con i suoi gran discorsi su Rivoluzione e Libertà. '
        'Personalmente li trovo un filo fissati con banditi e ladri. Insomma, metà delle loro '
        'carte? Banditi e ladri.\\n[Contiene]\\n 1 capo della banda.  1 guardaspalle della '
        'banda. \\n 1 stregone della banda.  1 sicario della banda. \\n 1 menestrello.  '
        '1 ladro. \\n 1 fante juere.  1 spadaccino juere.',
    (2198, '[ Tickets][White Card Set] Rogue Kingdom'):
        '"[" + ' + P + ' + " biglietti][Set bianco] Il regno dei banditi"',

    # ----------------------------------------------------------------- pirati
    (2206, "Shiver me timbers with these swashbucklin' pirate cards! They generate 'bullet' "
           "cards with a variety of devastating effects. And why three pirates instead of "
           "three.. you know.. musketeers? Well, one of the three pirates in this pack just so "
           "happens to be a musketeer, if that counts.\\n[Contains]\\n 1 Pirate Musketeer. \\n "
           "1 Rough Pirate. \\n 1 Pirate."):
        'Sacramento, che carte da pirati! Generano carte proiettile con effetti '
        'devastanti di ogni sorta. E perché tre pirati invece di tre... come dire... '
        'moschettieri? Ecco, uno dei tre di questo pacchetto è per l\'appunto un moschettiere, '
        'se vale come risposta.\\n[Contiene]\\n 1 moschettiere pirata. \\n 1 pirata rissoso. '
        '\\n 1 pirata.',
    (2208, '[ Tickets][White Card Set] Pirate\'s Plunder.'):
        '"[" + ' + P + ' + " biglietti][Set bianco] Il bottino dei pirati."',

    # ------------------------------------------------------ le voci di servizio
    (2215, 'Next Page.'): 'Pagina successiva.',
    (2218, 'Prev Page.'): 'Pagina precedente.',
    # ⚠️ Le due voci qui sotto le dice il GIOCATORE, non la negoziante: sono
    # `chatList`, cioe' le risposte fra cui si sceglie. Il giapponese lo
    # conferma — 交換できるほど持ってない e' in prima persona, «non ne ho
    # abbastanza» — e l'inglese («You don't have enough») lo aveva girato.
    (2220, "I don't want these cards."): 'Non mi interessano queste carte.',
    (2228, 'Here, take  tickets.'):
        '"Ecco, prendi " + ' + P + ' + " biglietti."',
    (2231, "You don't have enough for an exchange."): 'Non ho abbastanza da scambiare.',
    (2242, 'A successful negotiation! The cards are added to your deck!'):
        'Affare fatto! Le carte sono nel tuo mazzo!',
    (2244, 'Oh, and a free Card Pack, as a bonus from purchasing a set.'):
        'Ah, e un pacchetto di carte in regalo, per aver comprato un set.',
}
RESE = {k: unicodedata.normalize('NFC', v) for k, v in RESE.items()}

RINVIATE = set()

# ------------------------------------------------------------------ il lotto
sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
tutte = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]
zona = tutte

AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> :{v['riga']} {v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> :{k[0]} {k[1]!r}')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# rete 6: righe spente.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        errori.append(f"rete 6: riga {v['riga']} e' spenta, va rinviata")

# rete 7: un confronto non e' testo.
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo")

# rete 8: niente preposizione che si fonde davanti a un nome.
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan|carddailyt)\b')
for v in voci:
    for _, nome in FONDONO.findall(RESE[chiave(v)]):
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde davanti "
                      f"a {nome}: il nome porta gia' l'articolo")

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo.
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo nudo")

# rete 11: le funzioni di CONTENUTO devono coincidere.
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            errori.append(f"rete 11: riga {v['riga']} — attese {attese}, trovate {trovate}")

# ------------------------------------------------------------------- RETE 14
#
# Il tetto della finestra del dialogo. Vedi `scratchpad/chat_righe.py` per da
# dove vengono i due numeri: 53 caratteri di larghezza e 12 righe di altezza.
_spec14 = importlib.util.spec_from_file_location('cr', 'scratchpad/chat_righe.py')
_cr = importlib.util.module_from_spec(_spec14)
_spec14.loader.exec_module(_cr)

DESCRIZIONE = re.compile(r'^\s*cardsetdesc@tcg\(')
for v in voci:
    if not DESCRIZIONE.match(sorgente[v['riga'] - 1]):
        continue
    resa = RESE[chiave(v)].replace('\\n', '\n')
    righe_a_schermo = _cr.talk_conv(resa, LARGHEZZA_CHAT)
    inglese = _cr.talk_conv(v['en'].replace('\\n', '\n'), LARGHEZZA_CHAT)
    if len(righe_a_schermo) > TETTO_RIGHE:
        errori.append(
            f"rete 14: :{v['riga']} occupa {len(righe_a_schermo)} righe su {TETTO_RIGHE} "
            f"(l'inglese ne fa {len(inglese)}): il testo va a sbattere sui bottoni")
        for i, r in enumerate(righe_a_schermo):
            marca = '<<<' if i >= TETTO_RIGHE else '   '
            print(f'        {i + 1:3d} {marca} {r}')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


# rete 3: lo stesso giapponese reso in modo diverso altrove.
gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = Path(p).name
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa or parole(it) == parole(resa):
            continue
        print(f"⚠️ rete 3: :{v['riga']} jp={v['jp'][:30]!r}\n"
              f"      qui      {resa[:70]!r}\n"
              f"      {nome}:{riga}  {it[:70]!r}")

# rete 4 / rete 13.
per_jp = collections.defaultdict(set)
per_en = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], v['en'])].add(parole(RESE[chiave(v)]))
    per_en[v['en']].add(v['jp'])
for (jp, en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} / {en!r} reso in {len(rese)} modi')
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi')

# ------------------------------------------------------------------- referto
print('\n=== rete 14: quanto occupa ogni descrizione, inglese contro resa')
for v in voci:
    if not DESCRIZIONE.match(sorgente[v['riga'] - 1]):
        continue
    a = len(_cr.talk_conv(v['en'].replace('\\n', '\n'), LARGHEZZA_CHAT))
    b = len(_cr.talk_conv(RESE[chiave(v)].replace('\\n', '\n'), LARGHEZZA_CHAT))
    segno = '  ' if b <= a else ('⚠️' if b > TETTO_RIGHE else '💡')
    print(f'{segno} :{v["riga"]:5d}  inglese {a:3d}  resa {b:3d}  '
          f'{"(al soffitto)" if b == TETTO_RIGHE else ""}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'\n{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
