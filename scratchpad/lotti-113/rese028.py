import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :80612
    (80612, 'A red-colored toy considered a good-luck charm. In foreign countries, the most common toy has no eyes written on it, and every time a wish is granted, an eye is drawn on it with black dye. \\n# ~Gifts that I am Happy to Receive~'):
        "Un balocco rosso che si tiene per portafortuna. In terra straniera vanno per lo più quelli senza occhi dipinti: ogni volta che un desiderio si avvera, gliene si disegna uno con l'inchiostro nero. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :80674
    (80674, 'Heating furniture used in the cold season. It is said that there is no end to the number of children who fall asleep in them, saying that they feel like cave explorers when they crawl into them. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un mobile che scalda, per la stagione fredda. A infilarcisi sotto ci si sente esploratori di caverne, e pare che i bambini che lo dicono e poi si addormentano lì dentro non finiscano mai. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :80798
    (80798, 'Welcome to the underground! This excellent tool instantly creates a path that leads to underground space. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Benvenuti nel sottosuolo! Questo attrezzo eccellente apre in un attimo una via che porta agli spazi sotterranei. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :80860
    (80860, 'Welcome to the overworld! This excellent tool instantly creates a path that leads to the outside world. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Bentornati in superficie! Questo attrezzo eccellente apre in un attimo una via che porta al mondo di fuori. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :82275
    (82275, "A gift used to convey one's feelings on one's own behalf. Of course, it cannot be used. \\n# ~Gifts that I am Happy to Receive~"):
        "Un dono che si usa per dire, al posto proprio, quel che si sente. Naturalmente non si può usare. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :82875
    (82875, "A very high quality bed, said to be God's gift to the world. Its gentle touch is said to enrich the hearts of those who sleep on it. \\n#~ Great Encyclopedia of North Tyris Furnitures~"):
        "Un letto di qualità altissima, che qualcuno dice perduto da un dio. Quel tocco gentile, dicono, fa ricco il cuore di chi ci dorme.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :83764
    (83764, 'The legendary violin is said to be a favorite of virtuoso performers. Its sound resonates so loudly in the hearts of its listeners that there is no end to the number of people who give the violinist a gift of appreciation. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il violino leggendario che, si dice, va a cercarsi i maestri dell'esecuzione. Il suo timbro risuona forte nel cuore di chi ascolta, e non finiscono mai quelli che fanno un dono di riconoscenza a chi suona. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :84644
    (84644, 'Furniture used as room dividers. It can create a stylish atmosphere in a house. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un mobile che si usa per dividere le stanze. Dà alla casa un'aria di eleganza. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :84709
    (84709, 'A stringed instrument that is held with both hands and the strings are plucked to produce sound. It is not suitable for carrying around, but its relaxing sound will make the audience feel elegant. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a corde che si tiene con tutte e due le mani e suona a pizzico. Portarselo dietro non è comodo, ma il suo suono disteso metterà chi ascolta in uno stato d'animo elegante. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :84774
    (84774, 'A special instrument that plays a melody with a light sound. The joyful sound emitted from its small body is said to make even the listener happy. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento particolare, che porta la melodia con un suono leggero. Il suono allegro che esce da quel corpo piccolo, dicono, mette allegria anche a chi ascolta. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :84839
    (84839, 'A stringed instrument that produces sound by scratching. Its peculiar shape, which resembles an egg cut in half lengthwise, helps to reverberate the sound inside and give depth to the tone. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a corde che dà suono se lo si gratta. La forma singolare, come un uovo tagliato per il lungo, serve a far risuonare il suono all'interno e a dare profondità al timbro. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :84904
    (84904, 'A wind instrument consisting of several layered tubes. It is said to be difficult to keep the pitch stable, so players who handle it need to tune it constantly. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a fiato fatto di più canne accostate. L'intonazione fa fatica a restare ferma, e chi lo suona deve accordarlo di continuo. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :87002
    (87002, 'An atmospheric partition that can be folded. A young monk from another country once tried to defeat a tiger enclosed in one of these. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un paravento pieghevole, di quelli che fanno atmosfera. Pare che in terra straniera un giovane monaco abbia provato una volta ad abbattere la tigre chiusa dentro uno di questi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87064
    (87064, 'Lighting devices made to be easily carried around. Besides being treated as ornaments, it is said that in foreign countries, guards carry them with them for night watch. \\n# ~Daily Necessities for the Home~'):
        "Un lume fatto per portarlo in giro comodamente. Oltre a servire da ornamento, in terra straniera pare che le guardie se lo portino appresso per la ronda di notte. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :87126
    (87126, 'Exotic round windows. When installed, they are said to make people feel as if they are visiting a foreign country. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una finestra tonda, tutta profumo di terre lontane. Montata in casa, dicono, mette addosso la sensazione di essere in viaggio all'estero. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87188
    (87188, 'A stone structure used to enshrine lighting. It is said that the mere presence of one of these lamps creates a solemn atmosphere in the surrounding area. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una costruzione di pietra fatta per posarci dentro un lume. Basta che ce ne sia una perché tutto intorno si riempia di un'aria solenne. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87319
    (87319, 'A rather wide bedding for two. The beds are designed for two people, but can accommodate up to four if they are packed together, so a group of adventurers in dire straits may split the cost and sleep together on these beds. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un letto un po' largo, per due. Il conto è di due persone, ma stringendosi ci si sta anche in quattro, e capita che una brigata di avventurieri al verde divida la spesa e ci dorma tutta insieme.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87381
    (87381, 'Unused items are gathered up and piled up high in a very heavy pile. It is not something you would normally carry, but if you have to carry it under certain circumstances, be very careful not to become part of the waste. \\n#~Thousands of pieces of Junk I love~'):
        "Roba inutile raccattata e ammucchiata fin su, pesantissima. Non è cosa che di solito si porti in giro; ma se proprio tocca farlo, conviene stare attentissimi a non finire parte del mucchio.\\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :87443
    (87443, 'A sink that takes care of all water-related work. It is very huge and heavy, so care must be taken when carrying it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un lavello che si prende in carico tutto il lavoro dell'acqua. È enorme e pesa molto, quindi a portarlo in giro ci vuole attenzione. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87505
    (87505, 'A cupboard created by professionals who put their hearts and souls into their work. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una credenza costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma nelle parti che di solito non si vedono si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87644
    (87644, 'A flower bed with a simple fence attached to protect the small flowers. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un'aiuola a cui hanno montato una recinzione semplice, per proteggere i fiori piccoli. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87707
    (87707, "A spacious and stable chaise longue. It would be the perfect furniture for relaxing in one's own home. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un divano ampio, di una stabilità eccellente. È il mobile giusto per starsene in pace a casa propria. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87769
    (87769, 'A huge board on which letters written in white ink can be written and erased. Most schools are equipped with this board. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una tavola enorme su cui si scrive col gesso bianco e si cancella. Quasi tutte le scuole ne hanno una. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87831
    (87831, "A board with a list of items. It contains the restaurant's recommended dishes, but it is not certain which town they are from. \\n# ~Supporting Roles on the Streets~"):
        "Una tavola con scritta la lista dei piatti. Ci sono le specialità del locale, ma di che città siano non è chiaro. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :87893
    (87893, "A cabinet of drawers honored by the King's warrant. It is so brilliantly decorated that its functionality is compromised. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Una cassettiera di gran fama, fornitrice del re. È decorata così vivacemente da rimetterci in funzionalità. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :87955
    (87955, "An interior window with a partition attached. It is said that ladies who don't like peeping are buying them all the time. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Una finestra da interni con un divisorio montato sopra. Dicono che le dame a cui dà noia essere spiate la comprino a gara. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :88083
    (88083, 'Straw bags filled with grain. Widely used because of its good ventilation and resistance to damage of grains. \\n# ~Daily Necessities for the Home~'):
        "Un sacco di paglia pieno di granaglie. Si usa molto perché lascia passare l'aria e il grano si guasta poco. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :88803
    (88803, "Gate that looks suspiciously dangerous. From the mysterious flickering light, it is said that sometimes an unusual figure or a scream can be heard. \\n#~ Worlds you've Never Seen~"):
        "Un portale che dà una sensazione di pericolo. Dicono che dentro quella luce che ondeggia inquieta si vedano a tratti figure deformi, o si sentano delle grida.\\n#~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :89212
    (89212, "Wooden gate that claims the domain of Gods of the foreign lands. Tinted red, it somehow evokes the vibrancy of life. \\n#~ Worlds you've Never Seen~"):
        "Un portale di legno che, si dice, segna il dominio di un dio straniero. Tinto di rosso, ha in sé qualcosa che fa pensare allo slancio della vita.\\n#~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :89946
    (89946, 'An arched structure decorated with flowers. Why on earth do I feel a little embarrassed when I go through it? \\n# ~Supporting Roles on the Streets~'):
        "Una costruzione ad arco ornata di fiori. Come mai, a passarci sotto, si prova un po' di imbarazzo? \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :90012
    (90012, "Bedding acclaimed by the King's warrant. This bed, which is made with various luxuries, not to mention its soft and comfortable sleep, is the greatest dream for those who love furniture. \\n#~ Great Encyclopedia of North Tyris Furnitures~"):
        "Un letto di gran fama, fornitore del re. Del sonno morbido non c'è nemmeno da dire: fatto com'è con ogni sorta di lusso, è il sogno più grande di chi ama i mobili.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :90074
    (90074, 'Windows that create a relaxing space. The warm light shining through the window frame will provide you with temporary peace of mind. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una finestra che mette in scena uno spazio in cui riposare. La luce tiepida che entra dal telaio saprà dare un momento di quiete. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :90199
    (90199, 'A plant that has been well taken care of by people. The reason why it does not lose its shape no matter how much time passes is probably due to the presence of a street gardener who neatly trims it away without people knowing about it. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta curata dall'uomo quanto basta. Se non perde mai la forma per quanto tempo passi, sarà perché c'è un giardiniere di strada che la pota per bene senza farsi vedere. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :90261
    (90261, 'These are common windows that are widely found. It has no outstanding features, but is widely distributed because it is relatively easy to obtain. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una finestra comune, di quelle che si vedono dappertutto. Non ha nessuna particolarità di rilievo, ma si trova facilmente e per questo circola molto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :90323
    (90323, 'The window is characterized by its hard metal frame. Its hardness is said to be so great that it was once used in a prison camp somewhere. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una finestra che si riconosce dal telaio di metallo duro. Tanto duro, dicono, che una volta lo adottarono in un campo di prigionia. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :90385
    (90385, 'Plant with a charming shape. In recent years, there is a Palmian urban legend, involving a plant that quietly slips out of its pot at night when people are asleep and runs freely outside the city, which has drawn laughter in Palmia. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta dalla forma simpatica. Di notte, quando tutti dormono, sguscerebbe piano dal vaso e correrebbe libera fuori città: è una frottola che in questi anni a Palmia fa ridere la gente. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :90449
    (90449, 'An excellent cooking utensil that uses an open flame. The savory smell that spreads when cooking with it will be the best seasoning for those who eat with it. \\n# ~Supporting Roles in Kitchen~'):
        "Un ottimo arnese da cucina che lavora a fiamma viva. Il profumo tostato che si spande cucinandoci sarà il miglior condimento per chi mangia. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :90511
    (90511, "Tropical potted plants. If you don't have the money, buy this potted plant and enjoy the tropical atmosphere by all means. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Una pianta in vaso che dà un'aria da paese tropicale. Quando i soldi non ci sono, si compri questo vaso e ci si immagini di essere ai tropici. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :90573
    (90573, 'Potted plant that is said to relieve eye fatigue. Whether this is used externally or taken internally, only the seller can know. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che, dicono, toglie la stanchezza dagli occhi. Se sia per via esterna o perché va ingerita, lo sa solo chi la vende. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :90637
    (90637, 'A dignified chair that offers a comfortable and relaxed atmosphere. From what I hear, the official way to sit in this chair is to hold a silver cat in your left hand and a whiskey in your right. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una poltrona autorevole, che offre una seduta distesa. A quel che si dice, il modo ufficiale di sedercisi è con un gatto d'argento nella mano sinistra e un whisky nella destra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :91088
    (91088, 'Great works of art created by the best of artists. The light that shines through it moves and amazes people. \\n# ~Lumiest Art Catalogue~'):
        "Una grande opera che raccoglie il fior fiore dell'arte. La luce che entra passandoci attraverso commuove e stupisce. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :91150
    (91150, 'Pillars specialized for the purpose of supporting ceilings. Its unique shape allows it to support much heavier weights than ordinary columns. \\n# ~Lumiest Art Catalogue~'):
        "Una colonna fatta apposta per sostenere il soffitto. La forma singolare le permette di reggere un peso molto maggiore di una colonna normale. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :91212
    (91212, "The furnishings are the embodiment of the power and authority of a divine being. Its size is said to overwhelm those who see it, so much so that they are forced to kneel down. \\n# ~Worlds you've Never Seen~"):
        "Una suppellettile che incarna la forza e l'autorità di un essere sublime. È così grande, dicono, da schiacciare chi la guarda e fargli piegare le ginocchia da sé. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :91274
    (91274, 'A street lamp, fashionably polished thanks to the snow. It is said that the light gently illuminated by a tall gentleman on a snowy night will light a fire between two people in love. \\n# ~Supporting Roles on the Streets~'):
        "Un lampione che la neve ha reso ancora più elegante. Nelle notti di neve la luce che questo signore allampanato getta con dolcezza, dicono, accende il fuoco fra due innamorati. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91336
    (91336, 'Placed in the cold air, and adorned with white makeup of snow, the figure of this barrel could be mistaken for some kind of work of art. \\n# ~Supporting Roles on the Streets~'):
        "Un barile posato sotto il cielo freddo, che si è truccato di bianco. A vederlo, lo si scambierebbe per un'opera d'arte. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91398
    (91398, 'This small-sized snowman was created from the opinion that people want to feel snow close at hand. The adorable expression on his face remains unchanged even in his smaller size as he continues to gaze out at the world. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un pupazzo di neve piccolo, nato dall'idea di avere la neve a portata di mano. Quel muso adorabile non cambia nemmeno rimpicciolito, e continua a guardare il mondo. \\n# ~Viaggio in Tyris del Nord: Inverno~",

# 46 voci, 0 ambigue
}
