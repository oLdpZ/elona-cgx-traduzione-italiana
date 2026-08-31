# -*- coding: utf-8 -*-
"""114a - Lotto 032 di `db_item.hsp`: IL MOBILIO SI CHIUDE.

`FILTER_FURNITURE`, righe 122.000 in su: **54 righe** su 51 oggetti — 51
dell'indice 0 e tre dell'indice 2 (`:122025` <Noel>, `:122157` <Gwen>,
`:127609` <Erystia>). Con questo lotto il **corpo del mobilio e' finito**: 261
righe su 261, dal lotto 027 al 032.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **Le dieci piante in vaso** (`:122023` garofano, `:122085` coda di volpe,
  `:122155` anemone, `:122225` nerina, `:122295` gazania, `:122365` salvia,
  `:122427`, `:122489` rosa banksiae, `:122551`): tutte aprono con 鉢植え, e
  tutte e dieci le rese aprono con «Una pianta in vaso». Due di loro portano
  una battuta appresso — <Noel> sul garofano, <Gwen> sull'anemone — e sono le
  due che il gioco regala.
- **I tre ripiani che si spostano** (`:123866` i vestiti, `:123998` le
  cianfrusaglie, `:124060` la roba di casa): la **seconda frase giapponese e'
  identica** in tutti e tre, e in italiano lo e' altrettanto.
- **Le due tavole della strada** (`:123616` il segnavia, `:123678` l'insegna):
  seconda frase identica, e il testo dice proprio che i due si somigliano —
  類似品に注意, attenzione a non confonderli. Renderle in due modi avrebbe
  disfatto la battuta.
- **La sedia quadrata e lo sgabello tondo** (`:124434`, `:125936`): ciascuno
  nomina l'altro. Le due rese si rispondono parola per parola.
- **La sedia e il letto a buon mercato** (`:124371`, `:125748`): stessa
  formula 比較的安価な材質でできた + 市民の殆どは…ごく一般的な. Le due rese
  hanno la stessa struttura: «È la sedia / il letto comune per eccellenza:
  quasi tutti i cittadini...».
- **I due tavoli da bar** (`:125119`, `:125181`): **prima frase identica**,
  e cambia solo l'aria — losca l'una, da adulti l'altra.

### ⭐⭐ UNA FAMIGLIA ATTRAVERSA IL CONFINE DEL LOTTO

`:125432` (le armature esposte) porta
大きく試着不可と書かれている為、装備することはできない, che e' **la stessa
frase** di `:121446` e `:121508` del lotto **031**. La resa e' identica alle
due gia' scritte: «C'è scritto a lettere grandi che non si può provare, e
perciò non si può indossare».

⚠️ Nessuna rete l'avrebbe visto: `_coerenza.py` confronta le stringhe
**intere**, e queste tre differiscono nella prima frase. E' la lezione della
111a — le altre righe della stessa famiglia, anche se stanno in un altro lotto
— applicata a due lotti scritti nella stessa sessione.

### ⭐ I TERMINI CERCATI A MANO

    スライム       -> la melma           (`db_creature.hsp`)
    ノースティリス -> Tyris del Nord     (`chat.hsp`)
    ティリスの民   -> la gente di Tyris
    メッキ         -> una patina di metallo (non e' nel dizionario)
    飴細工         -> le figurine di zucchero (non e' nel dizionario)

### ⚠️ L'inglese sbaglia poco, e per omissione

`:122023` (il garofano) scrive due volte «modesty» dove il giapponese ha due
parole diverse — 慎ましやか (il fiore discreto) e 謙虚さ (l'umilta' come
virtu') — e la ripetizione fa sembrare la frase una tautologia. `:125057` (la
botte) traduce タル con «tar» invece che «barrel», che e' un refuso di monte.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :122023
    (122023, 'Potted plant with modest flowers. Its modesty is sometimes used as an anniversary gift as a sign of modesty. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che dà fiori discreti. Quel suo modo sommesso passa per prova di umiltà, e capita che la si regali negli anniversari. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122025
    (122025, '\\"It\'s my favorite flower. Well, you see, its petals look like splattered, fresh blood.\\" \\n# ~words of <Noel> the bomber~'):
        "\\\"Questo fiore mi piace da matti. Perché, guarda: i petali non sembrano sangue fresco schizzato dappertutto?\\\" \\n# ~Parole di <Noel> la dinamitarda~",

    # ---------------------------------------------------------- :122085
    (122085, "Potted plants that attracts the interest of certain animals and does not let go. The story goes that if you put it in the right place, before you know it, you'll have a cat crowd. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Una pianta in vaso che attira certi animali e non li lascia più. A metterla in un posto qualunque, dicono, senza accorgersene ci si ritrova un capannello di gatti. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122155
    (122155, 'Potted plants with brightly colored flowers. Their colors vary and are said to be very pleasing to the eye. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che dà fiori dai colori vivaci. I colori sono i più diversi e, dicono, rallegrano molto chi li guarda. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122157
    (122157, '\\"Oh, you\'re going to give it to me? Wow, I love it!\\" \\n# ~words of <Gwen> the innocent~'):
        "\\\"Eh, me lo regali? Evviva, mi piace tantissimo!\\\" \\n# ~Parole di <Gwen> l'innocente~",

    # ---------------------------------------------------------- :122225
    (122225, 'Potted plant is a little tricky to grow. Also known as a floral jewel, this potted plant is said to produce beautifully colored flowers that look like artisan candies. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che per crescere vuole un po' di mano. La chiamano anche la gemma dei fiori, e dicono che dia fiori di un colore bello come le figurine di zucchero. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122295
    (122295, 'Potted plant that produces dazzlingly bright yellow flowers. Another characteristic of this potted plant is that it grows into a flower so large that it looks like a brooch. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che dà fiori di un giallo vivo, da svegliare gli occhi. E ha anche questo di suo: cresce fino a fare fiori così grandi da scambiarli per una spilla. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122365
    (122365, 'Potted plant bearing many flowers from a single stem. It is said to have a sweet nectar, but in North Tyris it is often deadly poisonous, so never lick it. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che da un solo stelo tira fuori molti fiori. Si dice che abbia un nettare dolce, ma in Tyris del Nord quel nettare spesso diventa un veleno feroce: non provate mai a leccarlo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122427
    (122427, 'Well-grown potted plant. In some regions, this kind of plant, which grows quickly, is considered a sign of prosperity and is given as a gift. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso cresciuta in bellezza. Pare che in certe regioni questa specie, che viene su svelta, la prendano per segno di prosperità e la regalino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122489
    (122489, 'Potted plant with light-colored flowers. It is resistant to disease and pests and is relatively easy to grow. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che dà fiori di colore tenue. Regge bene le malattie e gli insetti, e si può dire che sia piuttosto facile da tenere. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122551
    (122551, 'Potted plant with pretty leaves. The house of a young lady who lives alone usually has this plant. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso dalle foglie graziose. In casa di una signorina che vive da sola, dicono, questa pianta di solito c'è. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :122613
    (122613, 'A special circle with ancient characters engraved on it. It is now a formality and is used exclusively as a fashionable way to decorate a room. \\n# ~Arcane Almanac~'):
        "Un cerchio particolare, inciso con caratteri antichi. Oggi è rimasto solo il guscio, e lo si usa unicamente per far bello un ambiente. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :122741
    (122741, "Containers used to hold liquids. We should not use them because we don't know what kind of liquid they contained. \\n# ~Daily Necessities for the Home~"):
        "Un recipiente che serve a tenere i liquidi. Che cosa ci fosse dentro non lo sa nessuno, e conviene lasciar perdere l'idea di usarlo. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :122884
    (122884, 'Shelves for the bakery, designed to be placed in an easy-to-see position. The price tags are posted so large that it would be better not to pick them up. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale da fornaio, studiato perché lo si possa mettere dove si vede bene. I cartellini del prezzo sono attaccati bene in vista, quindi meglio non allungare la mano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :123554
    (123554, 'A board with information about the city. There, trivial incidents and gossip that happened in the town are pasted. \\n# ~Supporting Roles on the Streets~'):
        "Una tavola con su scritte le notizie della gente comune. Ci sono attaccati i fatterelli e le chiacchiere che girano in città. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :123616
    (123616, 'Board that indicates the direction of a road, etc. Be careful of imitations, as there are some with similar designs. \\n# ~Supporting Roles on the Streets~'):
        "Una tavola che indica dove portano le strade. Ne esiste una col nome molto simile, quindi attenzione a non confonderle. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :123678
    (123678, 'A board used as a landmark. Be careful of imitations, as there are some with similar designs. \\n# ~Supporting Roles on the Streets~'):
        "Una tavola che si usa come segnale. Ne esiste una col nome molto simile, quindi attenzione a non confonderle. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :123742
    (123742, 'Cooking utensils for steaming and roasting food. Because the food is cooked by placing it inside, the sense of the cook is the most important factor. \\n# ~Supporting Roles in Kitchen~'):
        "Un arnese da cucina che cuoce i cibi al chiuso, fra vapore e calore. Si cucina mettendo dentro gli ingredienti, e perciò più di tutto conta il colpo d'occhio di chi cucina. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :123804
    (123804, 'A furnace into which liquid metal is poured. Those metals are burning very reddish red and brightly illuminate the surroundings. \\n# ~Aiming for Better Workmanship~'):
        "Un forno in cui è colato del metallo fuso. Quel metallo arde di un rosso violentissimo e illumina tutto intorno. \\n# ~Verso una Lama Migliore~",

    # ---------------------------------------------------------- :123866
    (123866, 'A small shelf on which miscellaneous clothing is placed. It is a movable piece of furniture and can be adjusted to a more visible position. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un ripiano con sopra vestiti d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :123998
    (123998, 'A small shelf on which miscellaneous commodities is placed. It is a movable piece of furniture and can be adjusted to a more visible position. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un ripiano con sopra cianfrusaglie d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124060
    (124060, 'A small shelf on which miscellaneous items is placed. It is a movable piece of furniture and can be adjusted to a more visible position. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un ripiano con sopra roba di casa d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124122
    (124122, 'A shelf that has room between tiers to accommodate everything. Along with ordinary shelves, it is a widely used piece of furniture. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale con i ripiani ben distanziati, così da farci stare qualunque cosa. Insieme allo scaffale comune, è un mobile che tutti usano volentieri. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124184
    (124184, "Shelves made to hold books as well. It is a highly flexible piece of furniture that allows the purchaser's sense of style to shine through in its storage. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Uno scaffale fatto perché ci stiano anche i libri. È un mobile che lascia molta libertà, e nel modo di riporre si vede il gusto di chi l'ha comprato. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124246
    (124246, 'Furniture for storing things that are not needed for the time being. It cannot be used because it is stuffed with things inside. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un mobile dove mettere via le cose che per adesso non servono. Dentro è già pieno, e perciò non si può usare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124308
    (124308, 'Shelves designed to hold tableware. With free partitions, it is possible to put away diverse types of tableware. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale costruito per riporci le stoviglie. Ha divisori che si spostano a piacere, e così ci stanno stoviglie di ogni tipo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124371
    (124371, 'A chair made of relatively inexpensive material. It is a very common chair that most of the citizens use. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una sedia fatta con un materiale piuttosto a buon mercato. È la sedia comune per eccellenza: quasi tutti i cittadini usano questa. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124434
    (124434, 'A chair with a rectangular seating area. It is almost a matter of taste as to which is better, the round chair or the square chair. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una sedia con la seduta quadrata. Se sia meglio di quella tonda è quasi solo questione di gusti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124497
    (124497, "A rather small shelf made for storing potions. Only the person who lays them out knows which potion is which, so it's best not to take them out too badly. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Uno scaffale un po' piccolo, costruito per tenerci le pozioni. Quale sia quale lo sa solo chi le ha disposte, e meglio non tirarne fuori una a caso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124560
    (124560, "A desk suitable for studying. It is made of hard material, but if you look closely, you can see someone's doodle carved into the corner of the desk, which seems to have been scraped off with a small knife. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un tavolo adatto a chi si applica allo studio. È di materiale duro, ma a guardare bene, in un angolo, c'è inciso lo scarabocchio di qualcuno, fatto, a quanto pare, con un coltellino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :124622
    (124622, 'A jar with an open mouth. It is very fragile and cannot be used to put anything inside. \\n# ~Daily Necessities for the Home~'):
        "Un vaso con la bocca aperta. È fragilissimo, e perciò non lo si può usare per metterci dentro qualcosa. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :124684
    (124684, 'A tightly sealed jar. The contents of the jar are intriguing, but it is sealed so tightly that it cannot be opened. \\n# ~Daily Necessities for the Home~'):
        "Un vaso sigillato ben stretto. La curiosità di sapere che c'è dentro viene, ma è chiuso così saldamente che non si apre. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :124746
    (124746, 'A metal stand used for forging metals. Apart from its original use, it is also said to be used in a fictional way, as a musical instrument by striking it with a hammer. \\n# ~Aiming for Better Workmanship~'):
        "Un banco di metallo che serve a forgiare i metalli. Oltre all'uso suo proprio, pare ce ne sia un altro che sembra inventato: batterlo col martello e farne uno strumento musicale. \\n# ~Verso una Lama Migliore~",

    # ---------------------------------------------------------- :124808
    (124808, 'Carefully polished armor. However, upon closer inspection, it appears to be a shoddy piece of armor that has only been painted with plating. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Un'armatura lucidata con cura. Ma a guardarla bene sembra roba scadente, appena ricoperta da una patina di metallo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :124870
    (124870, 'A hand-held lighting device that gives off a faint light. Just holding it in your hand makes you feel like a great adventurer. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un lume da tenere in mano, che fa una luce tenue. Basta averlo in pugno per sentirsi un grande esploratore. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :124932
    (124932, 'Tool for digging. However, it is possible to dig without any particular tool. The people of Tyris is just that strong. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un attrezzo per scavare. Però, a dirla tutta, si scava anche senza. La gente di Tyris è di tempra dura. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :124995
    (124995, "This is a chair that captivates everyone's heart for a moment. The chair is soft to the touch, and is truly an ideal chair. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Una sedia che, dicono, per un attimo rapisce chiunque. Anche al tatto è morbida e vellutata: la sedia ideale, si può ben dire. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125057
    (125057, 'Containers made to store water. Most are filled with liquor, but there are stories of adventurers who have accidentally opened a tar filled with slime while trying to steal a drink, so it is best not to open them unintentionally. \\n# ~Supporting Roles on the Streets~'):
        "Un recipiente costruito per conservare i liquidi. Di solito è pieno di vino, ma si racconta di un avventuriero che, volendo berne di nascosto, ha aperto per sbaglio una botte piena di melma: meglio non aprirne a casaccio. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :125119
    (125119, 'A desk made to be installed in a bar. It is a calm furniture with a suspicious atmosphere. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo fatto apposta per stare in una taverna. Un mobile sobrio, con addosso un'aria un po' losca. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125181
    (125181, 'A desk made to be installed in a bar. It is a calm furniture with a mature atmosphere. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo fatto apposta per stare in una taverna. Un mobile sobrio, con addosso un'aria da adulti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125246
    (125246, 'A very heavy keyboard instrument. It is said that there was once a musician who traveled with this piano on his back. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a tasti di un peso enorme. Dicono che un tempo ci fu un musicista che continuò il suo viaggio portandosi questo pianoforte sulla schiena. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :125308
    (125308, 'A small shelf with beautifully displayed ornaments. It is on two levels for easy viewing. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un ripiano con i soprammobili esposti con ordine. È su due piani, perché si vedano bene. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125370
    (125370, 'A shelf where a mountain of items are neatly stored. They are arranged in the same type for easy selection. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale con una montagna di articoli riposti in bell'ordine. Sono raccolti per tipo, così che scegliere sia facile. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125432
    (125432, "Armor displayed in a horizontal row. It is not possible to try it on as it is marked 'Not for Trying on'. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Armature esposte tutte in fila. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125494
    (125494, 'A table used for eating. The table is of moderate size, and even with a certain amount of plates on it, there is no need to worry about them overlapping. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo che si usa per mangiare. È largo il giusto, e anche mettendoci su un bel po' di piatti non c'è da temere che si accavallino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125557
    (125557, 'This table has a stylish atmosphere and is very current. Currently, the most popular type seems to be the simple type dyed in one color. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo all'ultima moda, con addosso un'aria elegante. Adesso, pare, va per la maggiore il tipo semplice, tinto tutto di un colore solo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125619
    (125619, 'Toys mainly used for children to play with. As time goes by, they become more complicated and more luxurious, which is always a headache for adults. \\n# ~Game Tricks, All Ages Version~'):
        "Un gioco che serve soprattutto ai bambini per divertirsi. Col passare del tempo si fa sempre più complicato e sempre più caro, ed è in ogni epoca il cruccio dei grandi. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :125682
    (125682, 'The dolls are sewn with cotton stuffed into the cloth. It is said that various memories are stuffed into the cloth as well as the cotton. \\n# ~Gifts that I am Happy to Receive~'):
        "Una bambola cucita riempiendo la stoffa di ovatta. Dentro, dicono, oltre all'ovatta è stipata una quantità di ricordi. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :125748
    (125748, 'Bedding made of relatively inexpensive materials. It is a very common bed, with most of the citizens sleeping and waking up in it. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio fatto con un materiale piuttosto a buon mercato. È il letto comune per eccellenza: quasi tutti i cittadini dormono in questo. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125810
    (125810, 'A prestigious chest of drawers with a moist surface. It is said that every person keeps his or her hidden possessions in these chests. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassettiera di gran classe, dall'aspetto morbido e pacato. Dicono che ognuno, nessuno escluso, tenga in una di queste il proprio tesoro nascosto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125873
    (125873, 'Shelves to hold books, often sold in furniture stores. There is nothing particularly bad or good about it, and it is a safe workmanship. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale per riporre i libri, di quelli che si trovano spesso dai mobilieri. Non ha difetti né pregi che saltino all'occhio: una fattura senza rischi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :125936
    (125936, 'A chair with a circular seating area. It is almost a matter of taste as to which is better, the square chair or the round chair. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno sgabello con la seduta tonda. Se sia meglio di quella quadrata è quasi solo questione di gusti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :127607
    (127607, "A stone slab with an ancient language inscribed on it. It cannot be deciphered, but it seems to be purchased on rare occasions by citizens who want to experience history. \\n# ~Worlds you've Never Seen~"):
        "Una tavola dura, incisa in una lingua antica. Non si riesce a decifrarla, ma pare che ogni tanto la compri qualche cittadino che vuole toccare la storia con mano. \\n# ~I Mondi che Non Hai Mai Visto~",

# 51 voci, 0 ambigue

    # ---------------------------------------------------------- :127609
    (127609, '\\"I wonder how it feels to have your words become eternal.\\" \\n# ~words of <Erystia> the scholar of history~'):
        "\\\"Chissà che effetto fa sapere che le parole che hai pronunciato diventeranno una cosa eterna\\\" \\n# ~Parole di <Erystia> la studiosa di storia~",

# 3 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-032.jsonl'
RIGHE = {
    122023, 122025, 122085, 122155, 122157, 122225, 122295, 122365, 122427, 122489,
    122551, 122613, 122741, 122884, 123554, 123616, 123678, 123742, 123804, 123866,
    123998, 124060, 124122, 124184, 124246, 124308, 124371, 124434, 124497, 124560,
    124622, 124684, 124746, 124808, 124870, 124932, 124995, 125057, 125119, 125181,
    125246, 125308, 125370, 125432, 125494, 125557, 125619, 125682, 125748, 125810,
    125873, 125936, 127607, 127609,
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
