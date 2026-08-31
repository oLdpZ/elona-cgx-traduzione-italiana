# -*- coding: utf-8 -*-
"""113a - Lotto 026 di `db_item.hsp`: IL PRIMO LOTTO DI PROSA DEL CORPO.

`FILTER_ITEM_FOOD`, righe 42.700-68.000, **indici 0, 1 e 2**: 50 righe su 41
oggetti. E' il primo lotto che non tocca il rapporto di identificazione (indice
3, chiuso nella 111a su 1.319 rese) ma il **corpo** della descrizione — la prosa
lunga che il gioco impagina, piu' la riga-fonte in coda.

⚠️⚠️ **LA ZONA E' L'UNIONE DEI TRE INDICI, NON L'INDICE 0.** I tre segmenti di
un oggetto il gioco li disegna **nello stesso pannello**, uno sotto l'altro:
rendere l'indice 0 e lasciare l'1 e il 2 in inglese produce un pannello meta'
italiano. `_107-chiavi-item.py` prende un indice per volta, quindi lo scheletro
lo fa `lotti-113/_corpo.py`, che chiede tre volte allo strumento di sempre e ne
incolla i blocchi. Qui: 41 righe dell'indice 0, 1 dell'indice 1, 8 dell'indice 2.

### ⭐⭐ LA CODA NON SI SCEGLIE A MANO

Ogni riga finisce con `\\n#<titolo>`: la **riga-fonte**, il libro da cui la
notizia viene, che `command.hsp:16901` disegna a destra in corsivo col trattino
davanti. La famiglia e' decisa dalla 112a (`lotti-112/titoli_fonte.py`) e la
assegna `lotti-113/_code.py`, che passa dal **giapponese** — l'inglese
appiattisce. Le code di questo lotto sono otto:

    #~Il Cibo Mutevole di Tyris~                        38 righe
    #~Rapporto di Identificazione: categoria <Cibo>~     5   (righe MUTE)
    # ~Bevande da Bere e Bevande da Non Bere~            2
    # ~Vivere Insieme al Bestiame~                       1
    # ~Il Gemito dello Sconfitto~                        1
    # ~Parole del Calamaro Provocatore ...~              1
    # ~Le Parole nel Sonno di una Bambina~               1
    # ~Alle Radici degli Antichi Riti~                   1
    # ~Erbe che si Mangiano ed Erbe che Non si Mangiano~ 1
    # ~Parole di <Lomias> il messaggero di Vindale~      1

⚠️ **`:60514` (la salsa di soia) scrive la fonte con la TILDE LARGA** `～`, che
sta fra i caratteri proibiti di `guardie.py`. Copiata verbatim farebbe bocciare
il lotto: la resa usa la tilde normale.

### ⭐⭐⭐ DIECI TITOLI DELLA 112a CONTRADDICEVANO UN NOME GIA' A SCHERMO

Cercando a mano i termini di questo lotto e' saltato fuori che
`～異形の森の使者『ロミアス』の言葉～` — la fonte di `:67794` — era reso «messo
della **foresta deforme**», mentre lo **stesso identico giapponese**
`異形の森の使者『ロミアス』` sta gia' nel dizionario due volte
(`db_card.hsp:10579`, `db_creature.hsp:100005`) reso **«<Lomias> il messaggero
di Vindale»**. Una terza forma, che nel dizionario non esiste.

Da li' e' nata `scratchpad/_113-fonti-gia-rese.py`: **45 titoli su 200** hanno il
giapponese gia' reso altrove, e **dieci** divergevano. Corretti tutti sulla forma
che il giocatore vede gia' — Balzak («netturbino» -> **custode**), Gwen
(«bambina innocente» -> **l'innocente**), Milis («capo» -> **la comandante**),
Poppy («cucciolo» -> **cagnolino**), Erystia, Loyter, Sin e Abyss (**Gilda dei
Ladri** maiuscola), il sunbararian. ⓘ `<Sophia>` resta nudo: li' l'inglese del
titolo e' `~words of <Sophia>~`, come per le altre quindici divinita'.

### ⭐⭐ L'INGLESE SBAGLIA TRE VOLTE, E TRE VOLTE SI SEGUE IL GIAPPONESE

1. **`:56997`, l'ozouni.** L'inglese ha copiato di peso il testo dell'osiruko —
   «A sweet dish... put in azuki bean soup». Il giapponese dice che e' una
   **zuppa** (スープ料理), che il brodo non e' di azuki, e che il nome viene da un
   piatto ritrovato in testi antichi. Le due righe sono gemelle e vanno lette
   insieme: e' la stessa storia (smaltire i kagami mochi induriti) che finisce
   in due piatti diversi.
2. **`:67983`, la ghianda.** L'inglese dice «They taste good when eaten raw»; il
   giapponese dice **そのままだと渋みが強い**, cruda e' molto allappante. E'
   l'opposto, e la riga dopo («cucinata pare venga discreta») da' ragione al
   giapponese.
3. **`:55607`, la gomma.** L'inglese scrive «Some **gorillas** use gum»: e'
   ごろつき, i **teppisti**. Un katakana letto per un'altra parola.

⚠️ E `:55011` chiama la cicoria «just like **fern**»: e' フェーン, la **fane**,
l'erba della riga `:54948`. Le due righe sono gemelle e la seconda nomina la
prima — un caso che nessuna rete vede, perche' gli inglesi sono diversi.

### ⭐ I TERMINI CERCATI A MANO, che nessuna rete legge

    バーベキューセット  -> set da barbecue        (`db_item.hsp:144489`)
    サンドイッチ       -> panino imbottito
    エーテル抗体       -> cura della corruzione   (`db_item.hsp:145141`)
    黄衣の王          -> il Re in Giallo
    鬼               -> demone                  (鬼熊 «orso demoniaco»)
    幸運の女神 / 収穫の神 -> la dea della fortuna / il dio del raccolto
    もち / 鏡もち / 納豆 / とうふ  -> invariati, gia' in `invariati.md`

💡 **`ぜんざい` e' una parola nuova**: dolce giapponese senza nome italiano,
citato dentro la riga dell'osiruko. Va in `invariati.md` accanto a `osiruko`.

### ⚠️ IL VINCOLO CHE MORDE NON E' LA LARGHEZZA

La 112a l'ha misurato: la coda persa vuole parole da 56 caratteri, il taglio a
70 sta dentro un budget di 77 e il pannello **sfoglia** invece di tagliare. Le
due cose vere sono il **tetto dei 66** sulla riga-fonte (la piu' lunga di questo
lotto ne misura 52) e la **parola spezzata a 17**, che l'italiano raggiunge.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42782
    (42782, "Delightfully Devillish Female Clams (Mesu-Kakis) renowned for their creamy flavor and crisp texture, normally two-shelled but often deliberately displayed to provoke reactions. Hazardous individuals are frequently mixed in, leading to days of one's dignity being trampled upon contact. Though those with proper labeling are safe, insufficiently processed ones with live tissue remain dangerous. Despite many experiencing hell due to losing to Mesukakis, numerous individuals continue challenging them based on chance alone. \\n#~Everchanging Food of Tyris~"):
        "Un mollusco dal sapore cremoso e dalla polpa soda. Sarebbe un bivalve, ma si apre apposta per godersi le reazioni di chi passa. Fra i mesugaki capita spesso l'esemplare nocivo, e a chi ci finisce contro toccano giorni interi di dignità calpestata. Quelli a cui la lezione è stata insegnata bene sono sicuri; quelli lasciati a metà, ancora sfrontati, sono pericolosi. Molti hanno conosciuto l'inferno perdendo contro un mesugaki, eppure continuano a sfidarli affidandosi alla sorte. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :42783
    (42783, 'Uohhhhhh, my belly rumbles and my chest aches on my way to work.\\n# ~words of the defeated~'):
        "\\\"Mangio il mesugaki / e mi brontola il ventre / mentre vado al lavoro\\\"\\n# ~Il Gemito dello Sconfitto~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :42784
    (42784, 'This clam is the worst of our kind! It needs urgent correction via legal action!\\n# ~words of a Provocasquid~'):
        "\\\"È un essere infame, mi diffama! Sto valutando le vie legali\\\"\\n# ~Parole del Calamaro Provocatore con gli Occhi Lucidi~",

    # ---------------------------------------------------------- :44656
    (44656, "Giants sea snail characterized by it's drill-shaped conch and multitude of thorns. It's usually made into sashimi, but it's reported in some regions, it is eaten roasted in its shell.\\n#~Everchanging Food of Tyris~"):
        "Una grossa chiocciola di mare. La riconosci dalle spine e dalla conchiglia a spirale, che pare la punta di un trapano. La si mangia cruda a fettine, ma in certe regioni la si arrostisce così com'è, nel guscio.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :44658
    (44658, "A type of seafood that restores satiety, it's used in many cooking dishes.\\n#~Identification Report: <Food> Category~"):
        "Un cibo di mare che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    # ---------------------------------------------------------- :44728
    (44728, "Clams with a rich taste and umami. They were used to be much smaller, but are gradually getting large due to change in environments. It's two shells are famous for not fitting together unless they are from the same individual.\\n#~Everchanging Food of Tyris~"):
        "Un bivalve dal sapore pieno e intenso. Un tempo era più piccolo, ma pare che il cambiamento dell'ambiente lo stia facendo crescere a poco a poco. È famoso perché le sue due valve combaciano solo se vengono dallo stesso animale.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :44730
    (44730, 'A type of seafood that restores satiety, they can be grilled with a Barbeque Set, obviously.\\n#~Identification Report: <Food> Category~'):
        "Un cibo di mare che sazia, e che ovviamente si può arrostire sul set da barbecue.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    # ---------------------------------------------------------- :44800
    (44800, 'Giant scallop packing a strong umami. The front and back sides of the shell are different colors. Normally, they live on the seafloor with the reddish-brown side up and the white side down.\\n#~Everchanging Food of Tyris~'):
        "Un grosso bivalve. Il muscolo, spesso e carnoso, è tutto sapore. Le due valve hanno colori diversi: di solito vive sul fondale con quella rosso-bruna in alto e quella bianca in basso.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :52108
    (52108, 'Plants that have adapted both aquatic and non-aqualitc environment. Widely used for ornamental purposes, but not inedible.\\n#~Everchanging Food of Tyris~'):
        "Una pianta che si era adattata alla vita sulla terraferma e poi è tornata a vivere sott'acqua. Si usa molto per ornamento, ma non è che non si possa mangiare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :52110
    (52110, "A type of vegetable that restores satiety, it's used in many cooking dishes.\\n#~Identification Report: <Food> Category~"):
        "Una verdura che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    # ---------------------------------------------------------- :52243
    (52243, 'A type of small fish with funny looking face. They are usually half buried on the ocean floor, eating only the food that flows by. Therefore, they cannot be caught, and even if they are brought to the surface, they try to bury themselves somewhere. When you drag them out of their burrows, they are surprisingly long.\\n#~Everchanging Food of Tyris~'):
        "Un pesciolino dalla faccia buffa. Sta quasi sempre mezzo sepolto nel fondale e mangia solo quel che gli passa davanti: per questo non abbocca mai, e anche tirato fuori dall'acqua cerca subito un posto dove infilarsi. Il nome che porta viene da una razza di cane dal muso somigliante. A strapparla fuori dalla tana, è lunga più di quanto ci si aspetti.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :54948
    (54948, 'Weed that are native to all regions of Aimwell. It is highly prolific, and at one time it was said to grow in the city. The leaves produce a sweet juice that is used as a sweetener, and the thick, long roots are edible.\\n#~Everchanging Food of Tyris~'):
        "Un'erba che cresce spontanea in tutta la Tyris del Nord di Aimwell. Si riproduce in fretta, e pare che a un certo punto spuntasse perfino in mezzo alle città. Dalle foglie esce un succo dolce che si usa come dolcificante, e la radice, grossa e lunga, è buona da mangiare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :55011
    (55011, 'Weed that are native to all regions of Aimwell. It looks just like fern at first glance, but the leaves have spines and the roots are thin and emit a pungent odor. The leaves are surprisingly tasty when the spines are removed, and the roots are used in medicine.\\n#~Everchanging Food of Tyris~'):
        "Un'erba che cresce spontanea in tutta la Tyris del Nord di Aimwell. A prima vista somiglia in tutto alla fane, ma ha le foglie spinose e la radice sottile, dall'odore pungente. Tolte le spine, le foglie sono buone più di quanto si creda, e la radice serve a preparare medicine.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :55074
    (55074, 'Coagulated ether antibodies. It has increased shelf life, but is less effective due to alteration. Not recognized as an antibody by the public.\\n#~Everchanging Food of Tyris~'):
        "La cura della corruzione, fatta rapprendere in un solido. Si conserva più a lungo, ma alterandosi ha perso efficacia. In generale non la si considera nemmeno una cura della corruzione.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :55544
    (55544, "Flavorless gum. It can be used to distract hunger, but it doesn't taste good and it is hard. It's better to throw it away, but please refrain from littering.\\n#~Everchanging Food of Tyris~"):
        "Una gomma che ha perso ogni sapore. A ingannare la fame serve ancora, ma è dura e non sa di niente. Meglio buttarla, però non per terra.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :55607
    (55607, 'A resin called gum base to which sweeteners and flavorings are added. It gives a pleasant taste and texture. It is not nutritious and does not fill you up, but it can at least distract you from hunger if you keep chewing it. Some gorillas use gum as a kind of intimidating behavior by chewing it.\\n#~Everchanging Food of Tyris~'):
        "Una resina detta base per gomme, con l'aggiunta di dolcificanti e aromi. Dà gusto e piacere alla bocca. Non nutre e non riempie la pancia, ma masticandola a lungo la fame si inganna. Certi teppisti la masticano rumorosamente e ne fanno una specie di minaccia.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :56400
    (56400, 'Bait used for fish in the water. It can be eaten, but it smells unpleasant and tastes bad. It seems to be very nutritious for fish, and it makes their scales beautiful and their flesh tighter. You should feed it to your fish as it can improve their quality. It does not seem to have any particular effect on fish monsters, and it is a mystery where the difference comes from.\\n#~Everchanging Food of Tyris~'):
        "Esca da gettare ai pesci in acqua. Mangiarla si può, ma sa di pesce marcio ed è cattiva. Per i pesci invece è nutrientissima: le squame si fanno belle e le carni sode. Siccome ne migliora la qualità, conviene darla ai pesci che si allevano. Sui pesci mostruosi pare non avere alcun effetto, e da dove venga la differenza resta un mistero.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :56871
    (56871, 'A dish recreated from ancient writings. It is a relative of the sandwich, but it seems to place more emphasis on the meat. It is too large, heavy, and difficult to eat, and many scholars question whether this size was really the standard.\\n#~Everchanging Food of Tyris~'):
        "Un piatto ricostruito a partire da testi antichi. È parente del panino imbottito, ma sembra puntare tutto sulla carne. È enorme, pesante e scomodo da mangiare, e molti studiosi dubitano che questa fosse davvero la misura normale.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :56934
    (56934, 'A sweet dish using rice cake as the ingredient. Kagamimochi, which had turned hard and dry, was put in azuki bean soup to treat it. However, there is a theory that dumplings or chestnuts should be added instead of mochi, and a similar product called zenzai has also been discovered, causing controversy in academic circles.\\n#~Everchanging Food of Tyris~'):
        "Un dolce che ha il mochi per ingrediente. Nacque per smaltire i kagami mochi ormai duri e secchi, buttandoli in un brodo di fagioli azuki. C'è però chi sostiene che al posto del mochi vadano messi gnocchetti o castagne, ed è saltato fuori anche un piatto somigliante chiamato zenzai: negli ambienti accademici se ne discute ancora.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :56997
    (56997, 'A sweet dish using rice cake as the ingredient. Kagamimochi, which had turned hard and dry, was put in azuki bean soup to treat it. At first, it was called something like mochi soup, but later a similar item was found in ancient documents, and it has now taken on that name. However, since there are differences in details in different documents, even experts cannot tell to what extent they are the same.\\n#~Everchanging Food of Tyris~'):
        "Una zuppa che ha il mochi per ingrediente. Nacque per smaltire i kagami mochi ormai duri e secchi, mettendoli in un brodo. All'inizio la chiamavano brodo di mochi; poi in certi testi antichi si trovò un piatto somigliante, e da allora ne porta il nome. I dettagli però cambiano da un documento all'altro, e nemmeno gli esperti sanno fin dove i due piatti coincidano.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :57188
    (57188, 'To prevent damaging the seafood, it is cured in salt water and then dried under the sun to increase portability and shelf life. It is very savory when grilled. For some reason, it is said that the Goddess of Fortune is not pleased with it.\\n#~Everchanging Food of Tyris~'):
        "Pesce messo in salamoia e poi seccato al sole perché non si guasti: così si trasporta meglio e dura di più. Arrostito profuma moltissimo. Chissà perché, alla dea della fortuna non fa piacere.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :57251
    (57251, 'To prevent damaging the vegetables, it is cured in salt water and then dried under the sun to increase portability and shelf life. This resulted in sweetness and flavor being concentrated. For some reason, it is said that the God(dess?) of Harvest is not pleased with it.\\n#~Everchanging Food of Tyris~'):
        "Verdura seccata al sole perché non si guasti: così si trasporta meglio e dura di più. Persa l'acqua, il dolce e il sapore si concentrano. Chissà perché, al dio del raccolto non fa piacere.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :57314
    (57314, 'To prevent damaging the fruits, it is cured in sugar and then dried under the sun to increase portability and shelf life. The skin, which is difficult to eat raw, becomes easier to eat. There are people who do not like the unique sweet taste.\\n#~Everchanging Food of Tyris~'):
        "Frutta candita nello zucchero o seccata al sole perché non si guasti: persa l'acqua, si trasporta meglio e dura di più. Anche la buccia, che cruda è scomoda da mangiare, diventa facile. C'è chi non sopporta quel dolce così particolare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :58589
    (58589, 'Processed food made from soybeans. It is made by frying thin slices of tofu. It has been a favorite food of foxes since very ancient times, but for a long time the reason for this was unknown, and it was generally believed that it was a substitute for rat meat. Recent research has revealed that the spongy interior contains magical elements and that foxes instinctively sense them.\\n#~Everchanging Food of Tyris~'):
        "Un alimento ricavato dalla soia: fette sottili di tofu fritte. Fin dall'antichità remota è il cibo preferito delle volpi, e per molto tempo nessuno seppe perché; si diceva che facesse le veci della carne di topo. Ricerche recenti hanno mostrato che dentro quella pasta spugnosa c'è materia magica, e che le volpi la fiutano d'istinto.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :58652
    (58652, 'Processed food made from soybeans. Fermented with natto bacteria. It is very sticky and requires some skill to eat it neatly. In addition to its stickiness, it also has a distinctive smell, and people get very angry if you pour it on them.\\n#~Everchanging Food of Tyris~'):
        "Un alimento ricavato dalla soia, fatto fermentare con il bacillo del natto. È di una viscosità tremenda, e mangiarlo con garbo richiede pratica. Oltre a filare ha un odore tutto suo, e a rovesciarlo addosso a qualcuno ci si prende una sfuriata.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :58715
    (58715, "Processed food made from soybeans. Solidified squeezed juice. Besides useful for maintaining a healthy body, the corners will stick into the opponent's head if thrown. It is already flavored, so there is no need to put soy sauce on it.\\n#~Everchanging Food of Tyris~"):
        "Un alimento ricavato dalla soia, ottenuto rassodandone il latte. Aiuta a farsi un corpo sano e, se lo si tira, lo spigolo si conficca nella testa dell'avversario. È di quelli già conditi: non serve versarci sopra la salsa di soia.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :58778
    (58778, 'It is the only plant that contains enough protein to rival meat. For this reason, it is nicknamed the meat of the field. It can be eaten or thrown. It is also used to dispel demons and other things.\\n#~Everchanging Food of Tyris~'):
        "L'unica pianta che contenga tanta proteina quanta la carne: per questo la chiamano la carne dei campi. Buona da mangiare, buona da tirare. Dicono che serva anche a scacciare i demoni.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :59125
    (59125, 'Processed food made from milk. The solids are extracted and hardened. It has a high shelf life and is often produced in areas where dairy farming is popular.\\n#~Everchanging Food of Tyris~'):
        "Un alimento ricavato dal latte: se ne estrae la parte solida e la si fa rapprendere. Si conserva a lungo, e lo si produce soprattutto dove l'allevamento da latte è fiorente.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :59188
    (59188, 'Processed food made from milk. It is made by coagulating separated fat, but it becomes sticky at room temperature. It is like a lump of oil and is flammable, so be careful when pouring it on people.\\n#~Everchanging Food of Tyris~'):
        "Un alimento ricavato dal latte: il grasso separato e fatto rapprendere. A temperatura ambiente si spappola. È in pratica un blocco di unto e prende fuoco con niente, quindi meglio badarci quando lo si rovescia addosso a qualcuno.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :59251
    (59251, 'Processed food made from milk. It is fermented with special bacteria, which prevents the growth of weak germs and thus has a high shelf life despite its appearance. It helps to build a healthy body, but people get very angry if you pour it on them.\\n#~Everchanging Food of Tyris~'):
        "Un alimento ricavato dal latte, fatto fermentare con fermenti particolari che tengono a bada i germi più deboli: per questo, contro ogni apparenza, si conserva bene. Aiuta a farsi un corpo sano, ma a rovesciarlo addosso a qualcuno ci si prende una sfuriata.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :59314
    (59314, 'Foods and other ingredients are crushed into a powdered granular form. They are concentrated in calories and are designed to make you feel a little fuller and fatter. However, taste and texture are not considered. It can be given to hungry livestock. \\n# ~Living with Livestock~'):
        "Alimenti e altro tritati fino a ridurli in granuli. Le calorie sono concentrate: sazia poco e fa ingrassare molto, ed è fatto apposta. Al gusto e alla consistenza però non ha pensato nessuno. Si può dare anche al bestiame affamato. \\n# ~Vivere Insieme al Bestiame~",

    # ---------------------------------------------------------- :60258
    (60258, 'Plucked leaves. Different colors and flavors appear depending on how they are fermented. They are used worldwide as an ingredient in tea. It can also be eaten as is... \\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Foglie appena colte. A seconda di come le si fa fermentare cambiano colore e profumo. In tutto il mondo sono preziose come materia prima del tè. Mangiarle così come sono si può, volendo... \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :60321
    (60321, 'The raw material for coffee. Originally, it was said that it had to be heated to undergo chemical changes and produce a proper aroma and taste. However, the varieties grown today all undergo chemical changes from the harvest stage due to improvements, so heat treatment is no longer necessary. \\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "La materia prima del caffè. In origine, pare, senza cottura non avveniva nessuna trasformazione chimica e non ne uscivano né aroma né sapore decenti. Le varietà coltivate oggi però sono tutte migliorate, e la trasformazione comincia già alla raccolta: tostarle non serve più. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :60384
    (60384, 'Although it is originally suited for wet areas, it has been enhanced for drought tolerance and grows well even when left in the field. In fact, excessive moisture increases the time and difficulty of cultivation.\\n#~Everchanging Food of Tyris~'):
        "Di suo è un cereale da terreni umidi, ma è stato reso resistente alla siccità e cresce bene anche lasciato in un campo qualunque. Anzi, dargli troppa acqua non fa che aumentare la fatica e la difficoltà della coltivazione.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :60447
    (60447, 'This grain combines the characteristics of wheat and barley through breeding. 80% of the flour distributed today is milled from here, instead of pure wheat.\\n#~Everchanging Food of Tyris~'):
        "Un cereale che, per selezione, unisce le qualità del frumento e dell'orzo. L'80% della farina che oggi circola non viene dal frumento puro, ma da lui.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :60514
    (60514, 'One of the basic seasonings that can make or break a dish. This reddish-brown liquid has a distinct aroma. Its salty flavor carries undertones of rich umami and sweetness.\\n#~Everchanging Food of Tyris～\\n'):
        "Uno dei condimenti di base, di quelli che decidono se un piatto riesce o no. Un liquido rosso-bruno dall'odore inconfondibile. Sotto il salato ha un sapore pieno e dolce.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :60581
    (60581, "A typical example of a spice, it's one of the seasonings that can make or break a dish. It was once treasured for its preservative properties and fetched a high price at market. Goes well on meat.\\n#~Everchanging Food of Tyris~\\n"):
        "Uno dei condimenti che decidono se un piatto riesce o no, e la spezia per eccellenza. Un tempo era preziosa per conservare a lungo il cibo, e c'è stata un'epoca in cui si vendeva a caro prezzo. Sta bene con la carne.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :60712
    (60712, "The final form of a flying creature serving the King in Yellow. It was working as a courier, playing music, making honey wine, etc., but it was not satisfied with that and became dried meat on it's own will. It goes well with alcohol.\\n#~Everchanging Food of Tyris~"):
        "Quel che resta di una creatura alata al servizio del Re in Giallo. Per il suo signore faceva il corriere, suonava, produceva idromele... amava servire più di ogni altra cosa, e non contenta si è fatta carne secca da accompagnare al bere. Va benissimo con l'alcol.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :61373
    (61373, 'This soup is made from a mysterious mushroom held by a girl who woke up from a daydream. It is blended in a perfect ratio, and when eaten, your body grows larger or smaller. It has a strange color, but the taste is good. It is said that those who continue to eat it will grow to the same size as the girl.\\n#~Everchanging Food of Tyris~'):
        "Una zuppa fatta con i funghi misteriosi che una bambina, svegliandosi da un sogno a occhi aperti, si ritrovò in mano senza sapere come. Il dosaggio è perfetto: a mangiarla il corpo si fa più grande o più piccolo. Ha un colore strano, ma il sapore non è male. Si dice che chi continua a mangiarne finisca per avvicinarsi alla corporatura di quella bambina.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :61375
    (61375, '\\"I can\'t go back to yesterday. Because I\'m not the same person I was yesterday.\\" \\n# ~a Little Girl\'s Bedtime Story~'):
        "\\\"A ieri non posso tornare. La me di ieri era un'altra persona\\\" \\n# ~Le Parole nel Sonno di una Bambina~",

    # ---------------------------------------------------------- :65527
    (65527, 'A lantern made from a hollowed-out pumpkin. Although it does not have the power to repel evil spirits, as the legend says, it does have a mysterious power, albeit in very small quantities. It can be eaten. \\n# ~a Close Look at the Ancient Rituals~'):
        "Una lanterna ricavata svuotando una zucca. Il potere di respingere gli spiriti maligni, quello che la tradizione le attribuisce, non ce l'ha; ma un po' di forza misteriosa dentro ce l'ha davvero. Volendo, si può anche mangiare. \\n# ~Alle Radici degli Antichi Riti~",

    # ---------------------------------------------------------- :67321
    (67321, 'This dish contains the flavor of shellfish and seaweed from the deep sea. No fish is used. The cooking process may or may not involve the application of advanced magic.\\n#~Everchanging Food of Tyris~'):
        "Un piatto che racchiude il sapore dei molluschi e delle alghe raccolti negli abissi. Di pesce non ce n'è. Per prepararlo, dicono, si ricorre all'alta magia; o forse no.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :67729
    (67729, "A clover with four leaves. Each leaf symbolizes hope, faithfulness, love, and good luck. You can keep it as a good luck charm, but eating it may make you happier. \\n# ~Weeds you can Eat and Weeds you can't Eat~"):
        "Un trifoglio con quattro foglie. Le foglie stanno per speranza, sincerità, amore e fortuna. Lo si può tenere come portafortuna, ma a mangiarlo forse si diventa più felici. \\n# ~Erbe che si Mangiano ed Erbe che Non si Mangiano~",

    # ---------------------------------------------------------- :67792
    (67792, 'Pastry characterized by its flower-like shape. The combination of thin, textured sabl? and savory almonds is delicious. It takes a lot of skill to squeeze out the dough.\\n#~Everchanging Food of Tyris~'):
        "Un dolce che si riconosce dalla forma di fiore. La pasta frolla, sottile e friabile, insieme al profumo tostato della mandorla è una delizia. Per far uscire l'impasto dalla sacca ci vuole una certa mano.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :67794
    (67794, '\\"..why are you looking at me? My name isn\'t spelled like that.\\" \\n# ~<Lomias> The Messenger From Vindale~'):
        "\\\"...perché guardi me? Il mio nome si scrive in un altro modo\\\" \\n# ~Parole di <Lomias> il messaggero di Vindale~",

    # ---------------------------------------------------------- :67857
    (67857, 'Fruit has a horizontal tomato-like shape. When ripe, it becomes dramatically sweeter. It contains an abundance of vitamins and minerals, and there was a time when it was treated as a panacea.\\n#~Everchanging Food of Tyris~'):
        "Un frutto largo e schiacciato come un pomodoro. Maturando diventa dolcissimo. È ricco di vitamine e di sali minerali, e c'è stata un'epoca in cui lo trattavano da panacea: quando il caco si fa rosso, dicevano, il medico si fa pallido.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :67859
    (67859, "A type of fruit that restores satiety, it's used in many cooking dishes.\\n#~Identification Report: <Food> Category~"):
        "Un frutto che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    # ---------------------------------------------------------- :67920
    (67920, 'Golden acorns of miraculous color. It is not that rare, but the cause of its appearance remains unclear, and it has great academic value. Even more so than ordinary gold nuggets. It is almost impossible to cook because there is almost no fruit part, but the taste itself does not seem to be that bad. Although it is too wasteful to eat. \\n#~Everchanging Food of Tyris~'):
        "Una ghianda leggendaria che brilla d'oro. Non è poi così rara, ma perché nasca non si è ancora capito, e per gli studiosi vale moltissimo: più di un lingotto d'oro vero. Di polpa non ne ha quasi, quindi cucinarla non si può; il sapore in sé non sembra male. Mangiarla resta uno spreco. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :67983
    (67983, "A nut with a smooth shell. Because it's abundancy and starch-rich nature, it's an important food source for those who live in the forest. They taste good when eaten raw, and tastes much better after cooking.\\n#~Everchanging Food of Tyris~"):
        "Un frutto dal guscio liscio. Accumula molto amido e se ne produce in quantità, perciò è un cibo importante per chi vive nel bosco. Spesso lo si trova sotterrato ai piedi degli alberi, messo da parte. Crudo è molto allappante, ma cucinato pare venga discreto.\\n#~Il Cibo Mutevole di Tyris~",

# 41 voci, 0 ambigue

    # ---------------------------------------------------------- :67985
    (67985, "A type of nut that restores satiety, it's used to make candies.\\n#~Identification Report: <Food> Category~"):
        "Un frutto a guscio che sazia, e con cui si fanno dolciumi.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

# 8 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-026.jsonl'
RIGHE = {
    42782, 42783, 42784, 44656, 44658, 44728, 44730, 44800, 52108, 52110,
    52243, 54948, 55011, 55074, 55544, 55607, 56400, 56871, 56934, 56997,
    57188, 57251, 57314, 58589, 58652, 58715, 58778, 59125, 59188, 59251,
    59314, 60258, 60321, 60384, 60447, 60514, 60581, 60712, 61373, 61375,
    65527, 67321, 67729, 67792, 67794, 67857, 67859, 67920, 67983, 67985,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
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
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
