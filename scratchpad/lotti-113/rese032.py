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
