import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :114206
    (114206, "A horn with a high-pitched sound. Basically, it can only produce a single note, but its heroic tone is sure to move people's hearts enough. \\n# ~Music of the Melodious Irva~"):
        "Un corno che manda un suono squillante. In sostanza sa fare una nota sola, ma quel timbro fiero basterà a scuotere il cuore della gente. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :115320
    (115320, 'The furnishings are so large that they could easily be mistaken for actual weapons. It was made in the image of a sword stuck in the earth, but some brave warrior may or may not have used it as a weapon in the past. \\n# ~Game Tricks, All Ages Version~'):
        "Una suppellettile che si potrebbe scambiare per un'arma vera. È fatta a immagine di una spada piantata nella terra, e si dice, ma chi lo sa, che in passato un prode l'abbia usata a forza come arma. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :115382
    (115382, "These are movable dolls that resemble elaborately crafted warriors. Although expensive, they are said to be the object of children's admiration because of their ability to respond to a variety of movements. \\n# ~Game Tricks, All Ages Version~"):
        "Un pupazzo snodabile fatto a immagine di un guerriero, lavorato con cura minuta. Costa caro, ma sa mettersi in ogni posa, e per questo, dicono, i bambini lo sognano. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :115384
    (115384, '\\"Muhahahaha! Great! Cool!\\" \\n# ~words of <Seth> the kid~'):
        "\\\"Uahahaha! Che forte! Che figo!\\\" \\n# ~Parole di <Seth>, ragazzino di città~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :118643
    (118643, "Furniture with plates of the same kind stacked on top of each other. They are useful when you have a sudden guest, but you probably shouldn't put them on the floor lest you trip over them in your haste and break them. \\n# ~Supporting Roles in Kitchen~"):
        "Un mobile con impilati piatti tutti dello stesso tipo. Comodo quando arrivano ospiti all'improvviso, ma meglio non posarlo per terra: basta inciampare nella fretta e va tutto in pezzi. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :119687
    (119687, 'Efficient bedding stacked vertically. They are often provided in inns, and when adventurers stay there, they often see fights over who gets to sleep on top. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio efficiente, con un letto impilato sopra l'altro. Si trova spesso nelle locande, e dicono che quando ci dormono gli avventurieri capiti di vederli litigare su chi va di sopra. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :119943
    (119943, 'A tomb with a sense of history in it. Naturally it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba da cui si sente il passare della storia. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120005
    (120005, 'A huge tomb built for an ancient ruler. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Un tumulo enorme, costruito per un potente dei tempi antichi. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120067
    (120067, "The tomb is so large that you can't help but gasp and back away. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~"):
        "Una tomba davanti a cui si trattiene il fiato e si fa un passo indietro senza volerlo. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120129
    (120129, 'The tomb is so large that it could be mistaken for a magnificent stone monument. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che si potrebbe scambiare per un bel monumento di pietra. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120191
    (120191, 'A beautiful tomb covered in flowers. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una bella tomba, sepolta sotto i fiori. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120253
    (120253, 'The tomb that made one finally want a tomb for oneself. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che fa venire voglia, finalmente, di averne una propria. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120315
    (120315, 'The tomb has long since left human hands. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che da parecchio nessuno cura più. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120377
    (120377, "Woven silk antique. It is marked 'sold' in large letters and cannot be used. \\n# ~Palmian Summer Fashion~"):
        "Una pezza tessuta in seta. C'è scritto a lettere grandi che è già venduta, e perciò non si può usare. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :120439
    (120439, 'Clothes scattered on the ground. It is not certain whether they were taken off and scattered before washing or before tidying up after washing. \\n#~Thousands of pieces of Junk I love~'):
        "Vestiti sparsi per terra. Se siano stati buttati lì prima del bucato, o se il bucato sia fatto e manchi solo di piegarli, non è chiaro. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :120633
    (120633, 'For all intents and purposes, it is the shelf itself. Nothing more, nothing less. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Da qualunque parte lo si guardi, è uno scaffale e basta. Niente di più e niente di meno. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120695
    (120695, 'This is a candelabra with an emphasis on the decorative aspect. The base is also lavishly processed, it shines so brightly that candles are unnecessary. \\n# ~Daily Necessities for the Home~'):
        "Un candelabro pensato soprattutto come ornamento. Anche il piede è lavorato con un lusso senza risparmio, e risplende al punto che la candela non serve. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :120757
    (120757, "An atmospheric table that is every lady's dream. It is just a table, but it is full of elegance. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un tavolo pieno di atmosfera, il sogno delle signore. È un tavolo e nient'altro, eppure trabocca di nobiltà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120819
    (120819, 'This dining table has been miniaturized to meet the expectations of housewives. Unless you are eating a full course meal, this size is probably sufficient. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo da pranzo rimpicciolito, come le padrone di casa chiedevano. A meno di non mangiare un pranzo a tutte portate, una misura così basterà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120883
    (120883, 'Cooking table equipped with a stove. Because two tasks can be done with a single stove, it is popular among ladies who are busy in the mornings. \\n# ~Supporting Roles in Kitchen~'):
        "Un bancone da cucina con i fornelli sopra. Un mobile solo fa due cose, e per questo va per la maggiore fra le signore che al mattino hanno fretta. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :120947
    (120947, "A sink suitable for food preparation. Some impatient people can't resist and cook their food right here. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un lavello adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121011
    (121011, "A table suitable for food preparation. Some impatient people can't resist and cook their food right here. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un bancone adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121073
    (121073, 'So much booze that it is too much for both hands. Cannot be used because it is undrinkable. \\n# ~Gifts that I am Happy to Receive~'):
        "Tanto liquore che non sta in due mani. Non lo si finirebbe mai, e perciò non si può usare. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :121136
    (121136, 'A bookshelf created by professionals who put their heart and soul into their work. At first glance, it looks simple, but the playful spirit of a master craftsman is hidden in parts that are not usually seen. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una libreria costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma nelle parti che di solito non si vedono si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121198
    (121198, 'Cabinet made by craftsmen who put their hearts and souls into their work. At first glance, they may look simple, but the playful spirit of the artisan is hidden behind the scenes, hidden from view. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassettiera costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma sul retro, che di solito non si vede, si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121260
    (121260, 'These books were carefully stacked on the floor after reading. Most of the books are technical, so there will be nothing special to read. \\n# ~Daily Necessities for the Home~'):
        "Libri impilati con cura sul pavimento dopo la lettura. Sono quasi tutti libri da specialisti, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121322
    (121322, 'Books that one could not put away after reading. Mostly magazines, so there would be no special information to read. \\n# ~Daily Necessities for the Home~'):
        "Libri che dopo la lettura nessuno ha rimesso a posto. Sono quasi tutti rotocalchi, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121384
    (121384, 'Full-body armor with a stern atmosphere. Although it looks like special equipment, it is in fact a replica and cannot be worn. \\n# ~Lumiest Art Catalogue~'):
        "Un'armatura completa che si porta addosso un'aria severa. Sembra proprio un pezzo con una storia dietro, ma in realtà è una copia e non si può indossare. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :121446
    (121446, "Armor placed for display. It is marked 'not for try-on' so you cannot equip it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~"):
        "Un'armatura messa lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121508
    (121508, "Clothes placed for display. It is marked 'not for try-on' so you cannot equip it. \\n# ~Palmian Summer Fashion~"):
        "Un abito messo lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :121570
    (121570, 'Stack of weapons bundled for display. They seem to be for sale in bulk and not sold individually. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Armi e armature legate in fascio per l'esposizione. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121632
    (121632, 'Stacked bows of various sizes. They seem to be for bulk sale only and are not sold individually. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Archi di ogni misura, impilati uno sull'altro. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121696
    (121696, 'This is an excellent all-around cookware for baking, steaming, and stewing. It is very large and heavy, which may make people hesitate to purchase it, but it is a proven performer. \\n# ~Supporting Roles in Kitchen~'):
        "Un ottimo arnese da cucina che fa tutto: arrostisce, cuoce a vapore, lessa. È grandissimo e pesa molto, tanto che a comprarlo si esita, ma in cambio la sua bravura è garantita. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :121767
    (121767, 'A map of the entire continent. Adventurers and non-adventurers alike are encouraged to read this map and think of the lands yet to be discovered. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una mappa che disegna il continente intero. Avventurieri e non, leggendola, lasciano andare il pensiero alle terre che non hanno ancora visto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :121891
    (121891, 'Magnificent pillars with flowers decorated at the zenith. This is said to be a restoration of an ancient architectural style. \\n# ~Lumiest Art Catalogue~'):
        "Una bella colonna con dei fiori guarniti in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :121953
    (121953, 'Magnificent pillars decorated with plants at the zenith. This is said to be a restoration of an ancient architectural style. \\n# ~Lumiest Art Catalogue~'):
        "Una bella colonna con delle piante guarnite in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",

# 35 voci, 0 ambigue
}
