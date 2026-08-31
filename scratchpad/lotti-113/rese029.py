import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :91718
    (91718, 'A streetlight with a stylish decoration. At night, they glow faintly with their own light, making the area look gorgeous. \\n# ~Supporting Roles on the Streets~'):
        "Un lampione ornato con un tocco di eleganza. Quando viene notte brilla di luce propria, tenue, e dà a tutto quello che ha intorno un'aria sfarzosa. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91780
    (91780, 'This lighting fixture was once created by a genius of the century. Its innovative construction is still one of the most popular among aristocrats. \\n# ~Daily Necessities for the Home~'):
        "Un apparecchio per fare luce che si dice costruito, un tempo, da un genio del secolo. La sua fattura ardita è ancora oggi fra le più amate dai nobili. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :91842
    (91842, 'Atmospheric lighting made of wax. Its small flickering flame is said to bring two people in love even closer together. \\n# ~Daily Necessities for the Home~'):
        "Un lume di cera, di quelli che fanno atmosfera. Quella piccola fiamma che ondeggia, dicono, accorcia ancora di più la distanza fra due innamorati. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :92124
    (92124, "A shelf that is widely used by the masses. It is a safe piece of furniture that can't be used for more than you expect, but does the bare minimum of what you need it to do. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Uno scaffale di quelli che circolano dappertutto. Non serve a niente di più di quel che ci si aspetta, ma il minimo indispensabile lo fa: un mobile senza rischi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :94801
    (94801, 'Very funny looking snow sculptures. When it snows, children gather to make snowmen of their own design and show them to each other. \\n# ~North Tyris Travels, Winter Edition~'):
        "Una statua di neve dall'espressione buffissima. Quando nevica, dicono, i bambini si radunano, fanno ciascuno il pupazzo che ha in mente e poi se li mostrano a vicenda. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :94863
    (94863, 'Giant mineral that is said to purge evil spirits. It is said to have occupied an important position in magic since ancient times. \\n#~Arcane Almanac~'):
        "Un minerale enorme che, dicono, scaccia gli influssi maligni. Rifrange la luce del sole in ogni direzione e sfolgora, e fin dall'antichità occupa un posto importante nelle arti magiche. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94925
    (94925, "Pillar with an adorable cat modeled at the top. It is said that the charming rear figure was carved by an artist who sensed the cat's inherent whimsy. \\n# ~Lumiest Art Catalogue~"):
        "Una colonna di pietra con in cima un gatto grazioso. Quella schiena piena di garbo, si dice, l'artista l'ha scolpita dopo aver colto il capriccio che è proprio dei gatti. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :94927
    (94927, '\\"I went to Vernis before, and there it was, that thing! The horrible tail and those ears, I can\'t stop shaking just thinking about it.... Who in the world could have made a stone pillar like that? The only relief was that it wasn\'t facing me.\\" \\n# ~<Tam> the cat hater~'):
        "\\\"Tempo fa sono stato a Vernis, e c'era quella cosa! La coda spaventosa, e quelle orecchie: solo a pensarci non smetto di tremare... Ma chi mai avrà fatto una colonna del genere? L'unica consolazione è che non era girata verso di me\\\" \\n# ~Parole di <Tam> il nemico dei gatti~",

    # ---------------------------------------------------------- :94987
    (94987, "Still-life painting said to have been painted by a famous artist. The canvas is said to be filled with many sunflowers, attracting the viewer's eyes and heart. \\n# ~Lumiest Art Catalogue~"):
        "Una natura morta che si dice dipinta da un pittore famoso. I molti girasoli che riempiono la tela, dicono, prendono l'occhio e il cuore di chi guarda e non li lasciano più. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95049
    (95049, 'Landscape painting said to have been painted by a famous artist. It is said that this painting, which evokes a nostalgic atmosphere, reminds people of their hometowns. \\n# ~Lumiest Art Catalogue~'):
        "Un paesaggio che si dice dipinto da un pittore famoso. In questo quadro, che desta un'aria di nostalgia venuta chissà da dove, ognuno finisce per rivedere il proprio paese. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95111
    (95111, "Portrait painting said to have been painted by a famous artist. The melancholy expression on her face possesses something that moves the viewer's heart. \\n# ~Lumiest Art Catalogue~"):
        "Un ritratto che si dice dipinto da un pittore famoso. Quella sua espressione velata di malinconia, dicono, ha in sé qualcosa che smuove il cuore di chi guarda. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95174
    (95174, 'The table is big enough to accommodate unexpected guests. One should learn from the depth of this open-mindedness. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo generoso, capace di far posto anche all'ospite che arriva all'improvviso. Quella larghezza di cuore sarebbe da imparare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95236
    (95236, 'Potted plants are so tall that they almost reach the ceiling. Every stem is growing toward the sun single-mindedly. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso così alta da sfiorare il soffitto. Ogni stelo, tutti quanti, si allunga verso il sole e non guarda altro. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95298
    (95298, 'Equipment used to cook food. It is not allowed to cook as it is being used anytime you see it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un'attrezzatura per cuocere e bollire i cibi. Ogni volta che la si guarda è occupata, e perciò non ci si può cucinare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95360
    (95360, 'A heating device used to warm a room. The crackling flames inside the furnace will slowly melt your hearty cold body. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un apparecchio che serve a scaldare gli ambienti. La fiamma che divampa crepitando dentro il focolare scioglierà piano il corpo intirizzito fino al midollo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95422
    (95422, 'Furnace for melting metals. The inside is always heated by red-hot wood. \\n# ~Aiming for Better Workmanship~'):
        "Un forno per fondere i metalli. Dentro è tenuto caldo di continuo da legna arroventata. \\n# ~Verso una Lama Migliore~",

    # ---------------------------------------------------------- :97873
    (97873, 'A disk in unused condition. It is a worthless item because it cannot be used, but it is said to be bought as a souvenir by Yowyn farmers on rare occasions when they visit the area for sightseeing. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco ancora da usare. Non essendo utilizzabile non vale niente, ma di rado, dicono, qualche contadino di Yowyn venuto in gita se lo compra per ricordo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :97943
    (97943, 'A mysterious small piece with a regular pattern engraved on it. It is presumed to be very beautiful and ornamental, but cannot be equipped. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un piccolo frammento misterioso, inciso con un disegno regolare. Tanto è bello che lo si suppone un ornamento, ma non si può equipaggiare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98005
    (98005, 'A container made to hold specific waste materials. It is said that if you put anything other than specific items in this in the cyberdome, the residents will look at you with disgust. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una scatola fatta per raccogliere certi rifiuti e non altri. In quella della Cupola Cibernetica, dicono, a metterci dentro qualcosa di diverso gli abitanti fanno una faccia storta. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98007
    (98007, '\\"This is one of those things that I\'ve witnessed and gotten. It\'s not just any old thing. First of all, the color is nice, and the shape. There\'s something fun about it. And between you and me, it has a secret...oops, you\'ll have to wait until after you buy it.\\" \\n# ~<Moyer> the crooked~'):
        "\\\"Avvicinatevi, avvicinatevi! Guardate che pezzo mi sono procurato. Roba che non si trova in giro, eh. Intanto il colore, e poi questa forma. Ha un'aria allegra. E, detto fra noi, questo qui ha un segreto... ehi, ehi, quello ve lo godete dopo che l'avete comprato\\\" \\n# ~La Cantilena di <Moyer> l'imbonitore~",

    # ---------------------------------------------------------- :98075
    (98075, 'Cylindrical metal objects used to store something. Its purpose is now lost, so it is usually filled with garbage. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un corpo di metallo a forma di cilindro, che serviva a conservare qualcosa. A che cosa di preciso ormai è perduto, e così di solito dentro ci si trova spazzatura. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98145
    (98145, 'Mysterious memory device that is said to contain ancient memories. Such is the rumor, but there is still no one who has been able to open the memory. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un misterioso apparecchio di memoria in cui, si dice, sono sigillati i ricordi antichi. Così vuole la voce; ma finora nessuno è riuscito ad aprirli. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98215
    (98215, 'Amazing box that destroys stored items by applying powerful heat to them. It is currently broken and unusable. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una scatola prodigiosa che, dicono, distrugge quello che le si mette dentro sottoponendolo a un calore fortissimo. Adesso è rotta, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98285
    (98285, 'Amazing device that can contain ones existence. Currently it is broken and cannot be used. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un apparecchio prodigioso che, dicono, sa imprigionare l'esistenza di una cosa. Adesso è rotto, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98356
    (98356, '\\"Try this for 5 minutes a day, 5 minutes a day! That fat, ugly body of yours will somehow get rid of itself just by working out with this for 5 minutes a day! The results are unknown!\\" \\n# ~Mysterious Memo on the Training Machine~'):
        "\\\"Cinque minuti al giorno, bastano cinque minuti al giorno, provate! Anche quel vostro corpo grasso e sgraziato, con cinque minuti al giorno qui sopra, in qualche modo si sistema! L'efficacia? Tutta da vedere!\\\" \\n# ~Istruzioni Misteriose in un Angolo dell'Attrezzo~",

    # ---------------------------------------------------------- :98358
    (98358, 'A machine that, when used, can stimulate growth in the body. Some of the Palmia Guard, whose bodies are their most important assets, have even gone to the trouble of purchasing the machine and using it at home. \\n# ~Daily Necessities for the Home~'):
        "Una macchina che, a usarla, fa crescere il fisico. Fra le guardie di Palmia, che sul corpo ci campano, c'è perfino chi se l'è comprata apposta per usarla in casa. \\n# ~Casalinghi che Danno Colore alla Casa~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :98426
    (98426, "A strange box with a dull sound. There is no place to open it, so you can't stuff things inside. \\n# ~The Yowyn Book of Secrt Knowledge!~"):
        "Una scatola strana che manda un suono sordo. Non ha nessun punto da cui aprirla, e perciò dentro non ci si può mettere niente. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98496
    (98496, 'Strange object with a flickering light. Its use is unknown, but it is said to be bought by wealthy people on rare occasions as a decorative item for their rooms. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Uno strano oggetto che manda lampi. A che serva non si sa, ma passa per ornamento da stanza, e di rado, dicono, qualche riccone se lo compra. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :103360
    (103360, 'A machine that ejects spheres containing items by using exotic coins. It requires more valuable materials than the red ones, but you can expect better items to come out of it. \\n# ~Game Tricks, All Ages Version~'):
        "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Vuole un materiale di più valore di quella rossa, ma in cambio da quel che ne esce c'è da aspettarsi di più. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :103425
    (103425, "A machine that ejects spheres containing items by using exotic coins. I don't know why, but I hear there are a lot of kids hanging out in that area. \\n# ~Game Tricks, All Ages Version~"):
        "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Chissà perché, pare che lì attorno ci siano spesso dei bambini a bighellonare. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

# 27 voci, 0 ambigue
}
