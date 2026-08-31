import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :55673
    (55673, 'Dolls made of twice-fired porcelain. Popular among noble girls. Rumor has it that if a special formula is used to put magic power into the doll, it will start to move. \\n# ~Lumiest Art Catalogue~'):
        "Bambole fatte di porcellana cotta due volte. Piacciono molto alle ragazze di nobile famiglia. Corre voce che, infondendovi il potere magico con una formula speciale, si mettano a muoversi. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55735
    (55735, 'Exquisite ceramics with beautiful decorations. Artistic pieces in particular fetch high prices and are often used not as tableware but as interior decorations. \\n# ~Lumiest Art Catalogue~'):
        "Ceramiche magnifiche, ornate con grande finezza. I pezzi più artistici si vendono a caro prezzo, e spesso non si usano come stoviglie ma come arredo. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55797
    (55797, 'Reproduction of pottery said to have been laid out in the tombs of ancient civilizations. The modeling is charming, but a little scary when seen in the dark. \\n# ~Lumiest Art Catalogue~'):
        "Riproduzione delle ceramiche che, si dice, stavano allineate nelle tombe delle civiltà antiche. La forma ha la sua grazia, ma al buio mette un po' di paura. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :57446
    (57446, 'A pendulum in the shape of Opatos. It seems to be made by some craftsman working on a rock stripped from Opatos himself. It reacts with ores and spins around and laughs. There is talk among miners that it may reduce the chance of missing buried ores when digging them out. \\n# ~Choosing the Best Tools for the Best Craftsmen~'):
        "Un pendolo a forma di Opatos. Pare che un certo artigiano lo ricavi dalla roccia staccata da Opatos stesso. Reagisce ai minerali: gira su sé stesso e ride forte. Fra i minatori si dice che, a scavare, faccia sfuggire di meno il metallo sepolto. \\n# ~Scegliere Bene gli Attrezzi da Artigiano~",

    # ---------------------------------------------------------- :57508
    (57508, 'A giant stuffed doll made by Kumiromi in his own image. It was previously given to Ehekatl countless times, but all of them were discarded in the human world. Its true functionality is that it is a cursed tool to kill anyone who comes close to Ehekatl. It moves when no one is looking and attacks surrounding creatures. It is useful to leave it in the field to kill vermin. \\n# ~Lumiest Art Catalogue~'):
        "Un enorme peluche che Kumiromi ha fatto a propria immagine. Ne regalò alla precedente Ehekatl un numero incalcolabile, e lei li buttò tutti quaggiù. In verità è un oggetto maledetto, fatto per uccidere chi si avvicina a Ehekatl: si muove quando nessuno guarda e assale le creature intorno. Lasciato nel campo fa comodo, perché ammazza gli animali nocivi. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :57707
    (57707, "The austere decor that imitates the figure of Itzpalt. It is said that an overly devout believer asked on his knees to collect Itzpalt's flame and mass-produced it like crazy. It is lit by a primordial flame that is charged with magical power, and when applied to the preparation of food, it burns away both curses and blessings. \\n# ~ Great Encyclopedia of North Tyris Furnitures~"):
        "Un arredo solenne che riproduce la figura di Itzpalt, e ne accentua il lato di demone del fuoco furioso. Si racconta che un fedele troppo devoto implorò in ginocchio di poter raccogliere la fiamma di Itzpalt, e poi ne fece produzione di massa come un forsennato. Dentro arde la fiamma primordiale carica di magia: applicata alla preparazione dei cibi, brucia via tanto le maledizioni quanto le benedizioni. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :57769
    (57769, 'Ehekatl holding a lucky fish...an unknown painter who witnessed an unusual scene in the world. The artist was so excited that he borrowed money to make a large number of prints, but they were not appreciated at all and he died in obscurity. After his death, it was revealed that if this painting was hung in the house, unwanted guests would no longer be invited, and there has been a trend toward reevaluation of the work. \\n# ~Lumiest Art Catalogue~'):
        "Opera di un pittore ignoto che assistette a una scena rarissima al mondo: Ehekatl che stringe fra le braccia il pesce che porta fortuna. Entusiasta, l'artista si indebitò per stamparne una gran quantità, ma nessuno le apprezzò e lui morì sconosciuto. Dopo la sua morte si scoprì che questo quadro, appeso in casa, tiene lontani gli ospiti sgraditi, e ora c'è chi lo rivaluta. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :57831
    (57831, 'A clock that forces you to wake up after 8 hours of sleep. A poke to the head will stop it. It is said that it used to be distributed to believers in place of the hidden treasure, but production was discontinued after many incidents of it being stolen and destroyed by militant Lulwy believers. It has a premium among enthusiasts, but the general public has no idea of its value. \\n# ~Discovery! Curiosities of the World~'):
        "Un orologio che, passate otto ore di sonno, sveglia per forza. Si ferma dandogli un colpetto in testa. Pare che un tempo lo distribuissero ai fedeli al posto del tesoro sacro, ma i seguaci più accesi di Lulwy lo rubavano e lo distruggevano di continuo, e la produzione fu sospesa. Fra gli appassionati vale un premio; la gente comune non ne capisce il valore. \\n# ~Scoperta! Le Rarità del Mondo~",

    # ---------------------------------------------------------- :59997
    (59997, 'Impressive flower that continues to bloom regardless of its environment. It is said that it was improved by the technology of biochemical civilization so that it would not wither, and then it spread into the wild. Besides being ornamental, it has a certain amount of academic value. Although it is an ancient plant, it seems to have developed strong vitality. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un fiore straordinario, che continua a fiorire qualunque cosa gli capiti intorno. Pare che la tecnica della civiltà biochimica lo avesse migliorato perché non appassisse, e che poi sia tornato allo stato selvatico. Oltre che ornamentale ha un certo valore per gli studiosi. All'origine era una pianta antica, ma la forza vitale gli è cresciuta troppo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :63869
    (63869, 'A cooking utensil that crushes and squeezes food into small pieces. Even if you do not have cooking skills, just throw in the ingredients and press the switch, and it will squeeze the juice on its own. It is an excellent tool for making juice easily. \\n# ~Supporting Roles in Kitchen~'):
        "Un utensile da cucina che tritura gli ingredienti e li spreme. Anche senza saper cucinare basta buttarci dentro la roba e premere il pulsante: il succo lo tira fuori da sé. Ottimo arnese per farsi un succo senza fatica. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :65331
    (65331, 'A huge, fuzzy, restful sleep pillow in the shape of a sheep. However, on rare occasions, I feel lonely and I wake up suddenly feeling lonely. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un enorme cuscino soffice a forma di pecora, per dormire bene. Pare che faccia sognare di essere una pecora che dorme in una prateria sconfinata, con addosso un vento gradevole. Ogni tanto però prende un senso di solitudine, e ci si sveglia di soprassalto sentendosi soli.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :66385
    (66385, 'A statue in the shape of a pure white angel. The wings are fragile and should not be touched carelessly. It is said that if you stand on the pedestal, you will feel as if you have grown wings. \\n# ~Lumiest Art Catalogue~'):
        "Una statua a forma di angelo candido. Le ali sono fragili e non vanno toccate alla leggera. Dicono che a salire sul piedistallo venga la sensazione di aver messo le ali. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :66451
    (66451, 'A small stone golem. Although small in size, it can be properly activated by pouring magic power into it. It is a classic design that is rarely seen today. \\n# ~Lumiest Art Catalogue~'):
        "Un piccolo golem di pietra. Piccolo sì, ma se gli si infonde il potere magico si attiva come si deve. È un disegno classico, che oggi non si vede quasi più. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :66513
    (66513, 'Stone statues that are said to save people in distress by enveloping them with their infinite great compassion. It is also generally regarded as a guardian deity for children. It is said that if you put a hat on it to protect it from the snow, it will return the favor or not. \\n# ~Lumiest Art Catalogue~'):
        "Una statua di pietra che, si dice, avvolge chi soffre nella sua misericordia infinita e lo salva. In genere la si considera anche la divinità che protegge i bambini. Dicono che a metterle in testa un cappello di paglia contro la neve venga a sdebitarsi; o forse no. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :66575
    (66575, 'Statues that imitate the objects of belief of ancient religions. Sacred trees such as sacred trees are sometimes used, but there is no particular difference in appearance. They have artistic value and are collected by some collectors. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che riproduce l'oggetto di culto di una religione antica. A volte la si intaglia in un legno sacro, come quello degli alberi consacrati, ma a vederla non cambia niente. Ha valore artistico, e c'è chi le colleziona. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :66641
    (66641, 'A small wooden golem. Although small in size, it can be properly activated by pouring magic power into it. It is a classic design that is rarely seen today. \\n# ~Lumiest Art Catalogue~'):
        "Un piccolo golem di legno. Piccolo sì, ma se gli si infonde il potere magico si attiva come si deve. È un disegno classico, che oggi non si vede quasi più. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :66703
    (66703, 'Shed for pets. It is carefully constructed to prevent ventilation. It will be cozy for creatures that like small spaces. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una casetta per gli animali domestici. È fatta con cura, perché non ci passi uno spiffero. Chi ama gli spazi stretti ci starà comodo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :68848
    (68848, 'A teardrop-shaped instrument made of ceramics. It has no fixed shape or number of holes. It has a singing mouth almost the same structure as a recorder, making it easy to produce sound. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento di ceramica a forma di goccia. La forma e il numero dei fori non sono fissi. Ha un'imboccatura quasi identica a quella del flauto dolce, e il suono viene facile. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :68913
    (68913, "A vertical flute with the name of 'recorder'. The special fipple structure stabilizes the air bundle and makes it easy to play. On the other hand, it is positioned as a beginner's instrument because its volume is low and its tone is difficult to express. \\n# ~Music of the Melodious Irva~"):
        "Un flauto diritto: il nome che porta in un'altra lingua vuol dire chi registra. Una struttura particolare, il becco, tiene ferma la colonna d'aria e rende facile suonarlo. In compenso ha poco volume e un timbro difficile da colorare, e per questo lo si tiene per uno strumento da principianti. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :68978
    (68978, 'A very thick, long, shiny black brass instrument. It is mainly used to reinforce the volume, but is rarely used in practice and is now an endangered instrument. \\n# ~Music of the Melodious Irva~'):
        "Un ottone molto grosso, molto lungo e nero lucente. Serve soprattutto a rinforzare il volume, ma in pratica lo si usa di rado ed è ormai uno strumento a rischio di estinzione. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :70127
    (70127, 'This non-scale miniature is a faithful reproduction of a magically powered airship. Unfortunately, it does not float.\\n# ~Irva Airlines Sales Catalogue~'):
        "Una miniatura fuori scala che riproduce fedelmente una nave magica volante. Purtroppo non sta a galla.\\n# ~Catalogo di Vendita di Irva Airlines~",

    # ---------------------------------------------------------- :72822
    (72822, 'A guardian dog with its mouth open. Sometimes called a lion. Place it on the right side of the gate. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un koma-inu con la bocca aperta. C'è chi lo chiama leone. Va messo a destra, guardando il cancello. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :72884
    (72884, 'A guardian dog with its mouth open. Sometimes called a lion. Place it on the left side of the gate. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un koma-inu con la bocca chiusa. Va messo a sinistra, guardando il cancello. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :73352
    (73352, "A wooden torture device. It inflicts pain on the groin using the person's body weight. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un attrezzo di tortura in legno. Fa male all'inguine sfruttando il peso di chi ci sta sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :73354
    (73354, '\\"It\'s a reward in our trade!\\" \\n# ~words of an adventurer who has entered a new world~'):
        "\\\"Nel nostro giro è un premio!\\\" \\n# ~Parole di un Avventuriero che si è Risvegliato~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :74568
    (74568, 'A percussion instrument made with a body made of wood and lined with leather. It is generally characterized by a very good reverberation and lingering sound. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a percussione fatto di una cassa di legno con la pelle tesa sopra. In genere risuona benissimo, e la coda del suono resta a lungo. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :76520
    (76520, 'It is a magnificent castle made of sand from the beach. This is the work of a person who came here to swim but got absorbed in playing in the sand. It is solid and surprisingly strong.\\n# ~North Tyris Travels - Summer Edition~'):
        "Un magnifico castello fatto con la sabbia della spiaggia. Opera di qualcuno che era venuto per nuotare e si è perso a giocare con la sabbia. È ben compattato, e più solido di quanto sembri.\\n# ~Viaggio in Tyris del Nord: Estate~",

    # ---------------------------------------------------------- :78789
    (78789, 'Flatware used to place food on. They range from the most expensive to the most expensive, and some are widely used in daily life, while others are so valuable that they are equivalent to the price of a horse. \\n# ~Supporting Roles in Kitchen~'):
        "Una stoviglia piatta su cui si mette il cibo. Ce n'è di ogni sorta, dalla migliore alla peggiore: certe si usano tutti i giorni, altre valgono tanto da poterci comprare un cavallo. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :78919
    (78919, 'The skins of wild beasts are tanned and used as furnishings. The appearance of the luxurious use of a whole animal is enough to make one believe that there is still some wildness left in the animal. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "La pelle di una bestia feroce abbattuta, conciata e ridotta a suppellettile. Usarne una intera è un lusso, e l'insieme dà l'impressione che là dentro sia rimasto qualcosa di selvatico. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :78981
    (78981, 'The head of a hunted beast is given a special treatment and made into a furnishing. Some aristocrats are not satisfied with merely decorating, but rather satisfy their desires to possess by processing their own hunted animals. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "La testa di una bestia abbattuta, trattata in modo speciale e ridotta a suppellettile. C'è qualche nobile a cui non basta appenderla: si lavora da sé la preda che ha cacciato, e così si sazia la voglia di possesso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79044
    (79044, 'This is an expensive-looking chaise longue made of very soft fur. It is a very comfortable but rather delicate piece of furniture that requires a great deal of care. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un divano dall'aria costosa, rivestito di una pelliccia morbidissima. Ci si sta benissimo seduti, ma è un mobile un po' delicato e tenerlo in ordine costerà parecchie attenzioni. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79303
    (79303, 'A very tactile and prestigious cupboard. It has a somewhat sophisticated atmosphere. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un armadietto di gran classe, piacevolissimo al tatto. Ha un che di adulto nell'aria che si porta dietro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79366
    (79366, 'A bookcase that could hold all kinds of books. According to the story, it all started when a retired historian ordered the ideal furniture to organize his stacks of books. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una libreria in cui pare ci stiano libri di ogni sorta. A quanto si racconta, tutto cominciò quando uno storico ormai ritirato ordinò il mobile ideale per mettere in ordine i libri che gli traboccavano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79636
    (79636, 'Small Christmas tree. This is a tree for the average homeowner who wants to celebrate the festival but does not have space for a tree in their home. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un piccolo albero di Natale. È l'albero per la famiglia comune, che vuole festeggiare ma non ha in casa lo spazio per un albero vero. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :79698
    (79698, 'An ornament made especially for celebrations. It is believed to be a marker for the descent of an exotic deity. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un ornamento fatto apposta per le feste. Si ritiene che serva da segnale perché un dio straniero possa scendere. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :79764
    (79764, "Hugpillow with a Goddess of Healing printed on it. It is said that by holding the long stick-shaped pillow, the Goddess herself lures not only believers but also all who use it into the depths of sleep and heals their body and soul in their dreams. \\n#~ Worlds you've Never Seen~"):
        "Un cuscino da abbracciare, morbido, con sopra dipinta la dea della cura. Dicono che, stringendo quel lungo cilindro, la dea in persona porti al fondo del sonno non solo i fedeli ma chiunque lo usi, e che nel sogno gli guarisca il corpo e l'animo.\\n#~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :79826
    (79826, 'A simple stall built to sell things during a festival. You may hear some kind of refreshing sound when you pass by. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una bancarella tirata su alla svelta per vendere roba durante una festa. A passarci accanto, certe volte si sente un suono che dà fresco. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79888
    (79888, 'A simple stall built to sell things during a festival. There is sometimes a savory smell mixed with some kind of sourness as you pass by. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una bancarella tirata su alla svelta per vendere roba durante una festa. A passarci accanto, certe volte si sente un profumo tostato con dentro una punta di acido. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :79950
    (79950, 'Furniture that serves as a partition for dialogue and accounting. It is said that conversing through this furniture makes one feel as if one has opened a store. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un mobile che serve a parlare e a fare i conti, e insieme fa da divisorio. Dicono che a conversare da dietro venga la sensazione di aver aperto bottega. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :80012
    (80012, "A little step that makes you feel like you've seen the world one step above. If you want to make a statement, you can stand here and talk. \\n# ~Supporting Roles on the Streets~"):
        "Un gradino da poco che dà l'impressione di vedere il mondo un piano più su. Quando si vuole dire la propria, conviene salirci e parlare da lì. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :80082
    (80082, 'Decorations made especially for celebratory occasions. Each person weaves them with flowers of his or her own choice, so there is a wide variety of shapes. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un ornamento fatto apposta per le feste. Ognuno lo intreccia con i fiori che preferisce, e così le forme sono le più varie. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :80149
    (80149, 'This piano was the favorite of a solitary genius composer. This piano potentially inherited his unique style of interpreting existing compositions, and this style seems to appear in the tone of the piano when it is played. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il pianoforte prediletto di un compositore geniale e solitario. Pare che abbia ereditato in potenza il suo modo tutto personale di leggere i pezzi altrui, e che a suonarlo quel modo riaffiori nel timbro. \\n# ~Dizionario Fantastico di Irva~",

# 41 voci, 0 ambigue
}
