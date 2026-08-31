import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :68650
    (68650, 'Small berries with medicinal properties. When fermented, the toxicity disappears and it makes an excellent ale. On the other hand, when dried, it becomes a highly addictive narcotic, making it a favorite of many smugglers. \\n#~Everchanging Food of Tyris~'):
        "Una bacca piccola che ha proprietà medicinali. A farla fermentare il veleno se ne va e ne viene una birra come si deve. A seccarla, invece, diventa una droga che dà una dipendenza fortissima, e per questo chi la lavora di nascosto non finisce mai. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69527
    (69527, 'A glossy, shiny purple vegetable. The fruit is spongy and easily soaks up water and oil. It has a light flavor and blends well with other ingredients.\\n#~Everchanging Food of Tyris~'):
        "Una verdura viola con una lucentezza lucida. La polpa è come una spugna e si beve facilmente l'acqua e l'olio. Ha un sapore delicato e sta bene insieme agli altri ingredienti.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69598
    (69598, 'Crop with beautifully aligned yellow grains. It is not suitable for eating raw, and the fresh taste at harvest is lost soon after harvest.\\n#~Everchanging Food of Tyris~'):
        "Una pianta bella da vedere, coi chicchi gialli allineati per bene. Cruda non va tanto, e il sapore fresco che ha appena colta lo perde subito dopo. Fra l'altro, la parte che pare una barba fa venire da urinare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69669
    (69669, 'Crop that is suitable for stewing as it does not fall apart when cooked. The skin and buds contain poison, so it is dangerous to scrape them off carefully before eating.\\n#~Everchanging Food of Tyris~'):
        "È quasi la stessa specie dell'imo, ma più grande e un po' sgraziata. Bollendola non si sfa, quindi va bene per gli stufati. Buccia e germogli contengono veleno, e se prima di mangiarla non li togli con cura è pericolosa.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69734
    (69734, 'Fruit combining a refreshing acidity with a rich sweetness. It contains substances that help break down meat and can also tenderize it. Be careful not to eat too much, as it can break down the tissues in the mouth.\\n#~Everchanging Food of Tyris~'):
        "Un frutto che tiene insieme un'acidità fresca e una dolcezza piena. Contiene sostanze che aiutano a disfare la carne, e sa anche renderla tenera. Attento a non mangiarne troppo: disfa anche i tessuti dentro la bocca.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69799
    (69799, 'Fruit with a crunchy texture. Sweet and juicy, but like apples, the core is highly acidic. Universally eaten raw, and were rarely cooked.\\n#~Everchanging Food of Tyris~'):
        "Un frutto che sotto i denti fa croc. È dolce e pieno di succo, ma come nella mela la parte vicina al torsolo è molto acida. Di base si mangia cruda, e cucinarla è raro.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69864
    (69864, 'A slender, curved yellow fruit. Popular as a snack, but also a staple food in some countries due to its high nutritional value and high yield. Note that ripe bananas can quickly become sore if left to ripen.\\n#~Everchanging Food of Tyris~'):
        "Un frutto giallo, lungo e ricurvo. Piace molto come merenda, ma dà molto nutrimento e molto raccolto, e in certi paesi è il cibo principale. Attento: una banana matura, se la lasci lì, si guasta in fretta.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69929
    (69929, 'Fruits known for its high quality. Many farmers aim to make a fortune from high-quality muskmelons. It is not known how they became so different from watermelons.\\n#~Everchanging Food of Tyris~'):
        "Un frutto famoso per essere carissimo. Molti contadini puntano a fare fortuna con meloni di gran qualità. Perché sia finito così lontano dall'anguria non si sa.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69994
    (69994, 'A close relative of the cucumber, it is a vegetable... but because of its sweetness, it is treated exclusively as a fruit. It is a wonderful fruit that can be smashed with a long stick.\\n#~Everchanging Food of Tyris~'):
        "Una verdura parente stretta della zucca... ma per quanto è dolce la trattano da frutto e basta. E ci si può anche giocare a spaccarla con un bastone lungo: un frutto splendido.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :70396
    (70396, "Nut with a spiky shell. It is still called sea urchin by some people, perhaps because it looks like one. It's shorter spikes makes it an excellent throwing weapon.\\n#~Everchanging Food of Tyris~"):
        "Un frutto chiuso in un riccio pieno di spine. Fino a poco tempo fa lo confondevano col riccio di mare, e forse per questo c'è ancora chi lo chiama riccio. Rispetto al riccio di mare ha le spine più corte, quindi si tira meglio.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :70398
    (70398, "A type of nut that restores satiety, it's used to make candies.\\n#~Identification Report: <Food> Category~"):
        "\\\"R-rovinare un riccio porta castigo!\\\"\\n#~Parole di <Naplus> l'alchimista spaventata~",

    # ---------------------------------------------------------- :70671
    (70671, 'It is a member of the hermit crab family, although it looks a lot like a crab. They are generally distributed in a boiled state because their fibers are tough and tasteless without being cooked. Before being boiled, their body color is dark purple. Although they are boiled this way, they are still alive.\\n#~Everchanging Food of Tyris~'):
        "Somiglia molto a un granchio, ma è parente del paguro. Se non lo si cuoce le fibre restano dure e il sapore è poco, quindi in giro lo si trova quasi sempre già bollito. Prima di bollirlo il colore del corpo è viola scuro. Si indebolisce, sì, ma di regola bollirlo tanto non basta a ucciderlo.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :71163
    (71163, 'Salad made from the vegetative parts of mandrake corpses. It does not contain magic itself, but it does contain a large amount of ingredients that generate magic.\\n#~Everchanging Food of Tyris~'):
        "Un'insalata fatta con la parte vegetale del cadavere di una mandragora. Forza magica non ne contiene, ma è piena di sostanze che la magia la producono.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :71706
    (71706, 'Sweet treats. A strange custom of giving chocolate on certain days to express gratitude has taken hold in recent years. \\n#~Everchanging Food of Tyris~'):
        "Un dolce. Da qualche anno sta prendendo piede l'usanza curiosa di regalare cioccolato in certi giorni per dire grazie. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :73153
    (73153, 'Yith tentacles, chopped into small pieces, are placed in a flour dough and baked into a spherical shape. The secret of this dish is that it contains a trace amount of hallucinogenic ingredients. \\n#~Everchanging Food of Tyris~'):
        "Un piatto fatto tagliando a pezzi i tentacoli della stirpe degli yith, mettendoli in un impasto di farina e cuocendoli a palline. L'ingrediente segreto è la piccola dose di sostanze che fanno vedere le allucinazioni. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74164
    (74164, 'Ingredients unknown. Emits a suspicious odor and makes one want to refuse to eat it. Only those who are prepared to eat it should do so. \\n#~Everchanging Food of Tyris~'):
        "Composizione ignota. Manda un odore sospetto che fa venir voglia di rifiutarsi di mangiarlo. Che lo mangi solo chi si è deciso davvero. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74298
    (74298, 'Strange bentos that instantly turn you into a child when you eat them. \\n#~Everchanging Food of Tyris~'):
        "Un pranzo al sacco misterioso: a mangiarlo si torna bambini in un attimo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74361
    (74361, "Bento box lunches that contain time. Don't eat it. \\n#~Everchanging Food of Tyris~"):
        "Un pranzo al sacco in cui è chiuso il tempo. Non si deve mangiare per nessun motivo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74631
    (74631, "An icy treat made by pouring syrup over shaved ice. When eaten in a hurry, it causes a sharp headache, which is due to the brain's misidentification of the stimulation to the pharynx. \\n#~Everchanging Food of Tyris~"):
        "Un dolce di ghiaccio, fatto versando lo sciroppo sul ghiaccio tritato. A mangiarlo di fretta viene una fitta alla testa, e il motivo è che il cervello scambia per mal di testa quel che si sente in gola. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :75847
    (75847, 'One of the last products made by a caramel maker in despair after his business failed. It evokes an apocalypse. \\n#~Everchanging Food of Tyris~'):
        "L'ultima cosa che fece un caramellaio disperato perché il lavoro non gli andava. Chiama la fine del mondo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :75849
    (75849, '\\"Tomorrow is the day for debt collection, and I don\'t have the money ready... I wish the world would end tomorrow...\\" \\n# ~an Indebted Caramel Maker~'):
        "\\\"Domani viene chi riscuote il debito e i soldi non li ho... magari domani il mondo finisse...\\\" \\n# ~Parole di un Caramellaio sull'Orlo del Fallimento~",

    # ---------------------------------------------------------- :76719
    (76719, 'Simple dish of rice, hardened and seasoned with a firm fist. It is characterized by its ability to be eaten quickly, even with one hand. \\n#~Everchanging Food of Tyris~'):
        "Un piatto semplice: riso stretto in mano fino a compattarlo e insaporito. Quel che lo distingue è che si mangia in fretta, anche mentre fai altro. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78115
    (78115, 'The combination of a thick texture and a crunchy texture makes it a popular food. In the past, washed Putits were used directly, but due to numerous incidents of unwary customers being eaten by Putits, they now use Putits that have been put in a state of suspended animation. \\n#~Everchanging Food of Tyris~'):
        "Un cibo che piace per come mette insieme il morbido che si scioglie e i granelli che scrocchiano sotto i denti. Un tempo si usavano putit lavati e basta, ma siccome è successo più volte che un cliente distratto finisse mangiato dal putit, adesso si usano putit messi in morte apparente. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78117
    (78117, '\\"Look at this Lily, this Putit is quite lively... wait.. noooooooooooo! \\" \\n# ~Victim\'s Last Words~'):
        "\\\"Guarda un po', <Lily>, questo putit è proprio vivace... uwaaa!!\\\" \\n# ~Le Ultime Parole della Vittima~",

    # ---------------------------------------------------------- :78462
    (78462, 'By adding unique elements to the process, the bread has a fluffier texture. The softness of the bread is not only apparent when you touch it, but it is even more obvious when you taste it. \\n#~Everchanging Food of Tyris~'):
        "Un pane a cui, aggiungendo qualcosa di proprio alla lavorazione, hanno dato una consistenza più soffice. La morbidezza si sente già a toccarlo, ma in bocca si capisce molto meglio. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78464
    (78464, '\\"Oh, the fluffy bread made by my big sister is delicious!\\" \\n# ~a girl with nausea~'):
        "\\\"I-il pane soffice che ha fatto la mia sorella maggiore è buonissimo!\\\" \\n# ~Parole di una Bambina che Trattiene la Nausea~",

    # ---------------------------------------------------------- :78529
    (78529, 'One of the basic seasonings that can make or break a dish. It is an excellent seasoning that not only adds sweetness, but also brings out the umami and saltiness of the ingredients when used in small quantities. \\n#~Everchanging Food of Tyris~'):
        "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge dolcezza, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il salato che l'ingrediente ha già. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78596
    (78596, "One of the basic seasonings that can make or break a dish. While it obviously imparts a salty flavor on any food, using it sparingly can bring out the ingredients' natural sweetness and umami, making for an excellent seasoning in moderation.\\n#~Everchanging Food of Tyris~\\n"):
        "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge sapore salato, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il dolce che l'ingrediente ha già.\\n#~Il Cibo Mutevole di Tyris~\\n",

    # ---------------------------------------------------------- :79241
    (79241, "A very tasty dish that fills you with juices that overflow when you put it in your mouth. It's probably a silly question to ask what ingredients are used. \\n#~Everchanging Food of Tyris~"):
        "Un piatto buonissimo che, appena te lo metti in bocca, ti riempie di un sugo che trabocca. Chiedere che cosa ci sia dentro sarebbe soltanto di cattivo gusto. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :79243
    (79243, '\\"Hm. The texture when you put it in your mouth, the juicy meat juices that pour out of it with great vigor, and the unique flavor that lingers in your mouth. This dish deserves the highest rank I have ever had. By the way, what kind of meat is used in this dish?\\" \\n# ~ Words of the great food critic, Gratona ~'):
        "\\\"Uhm. La consistenza appena entra in bocca, il sugo che ne esce fuori con impeto, quel sapore tutto suo che resta. Questo piatto merita il posto più alto fra quanti ne ho mangiati. ...A proposito, che carne ci mettono dentro?\\\" \\n# ~Parole di <Gratona>, grande critico gastronomico~",

# 5 voci, 0 ambigue

    # ---------------------------------------------------------- :79431
    (79431, 'Vegetable with a strong acidity that has received all the blessings of the sun. It can be prepared in a variety of ways, but one unusual way to eat it is to cut it raw into round slices and dip it in sugar.\\n#~Everchanging Food of Tyris~'):
        "Una verdura molto acida che si è presa addosso tutto il bene del sole. La si cucina in molti modi, ma fra i più strani c'è chi la taglia a fette da cruda e la mangia con lo zucchero sopra.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :80487
    (80487, 'The white devil from a foreign land. It beckons people with its savory smell and soft touch, but once it has been eaten, it will suddenly pause at the throat and deprive the eater of action and consciousness! If this happens, get help from someone nearby.\\n#~Everchanging Food of Tyris~'):
        "Il demone bianco venuto da un paese straniero. Ti chiama con l'odore invitante e con la morbidezza, ma una volta che l'hai mangiato si ferma di colpo in gola e ti toglie di botto i movimenti e i sensi! Se ti succede, fatti aiutare da chi ti sta vicino.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :80550
    (80550, 'Special rice cake decorated with festive items. A grateful rice cake blessed by God, but eaten without concern. However, God cannot do anything about the rice cake getting stuck in your throat. So be careful when eating it. \\n# ~Gifts that I am Happy to Receive~'):
        "Un mochi speciale, ornato con le cose di festa. È un mochi benedetto e degno di riconoscenza, ma lo si può mangiare senza pensarci. Contro un mochi che va di traverso, però, non può niente nemmeno un dio: quando lo mangi, guardati bene intorno. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :81669
    (81669, "Fortune for you and me! Fortune! If you take a bite gently, happiness will surely arrive. If you ate the whole thing, God's blessing will come to you. \\n# ~Note Written on the Back of the Bag~"):
        "Fortuna per te e fortuna per me! Fortuna! Se ne dai un morso piano piano, la felicità di sicuro ti arriva. Se lo mangi tutto in un colpo, ti arriva il responso di un dio. \\n# ~Postilla Scritta sul Retro del Sacco~",

    # ---------------------------------------------------------- :84100
    (84100, 'The tail of a rabbit has been considered a sign of good luck since ancient times. Some regions use it as an ornament, but the ancient North Tyris belief is that eating it brings good luck. \\n#~Iron Stomach: A Complete Diet~'):
        "La parte della coda del coniglio, che fin dai tempi antichi è segno di fortuna. Pare che in certe zone se ne faccia un ornamento, ma l'insegnamento antico di Tyris del Nord è che mangiandola la fortuna te la prendi dentro direttamente. \\n#~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",

    # ---------------------------------------------------------- :86466
    (86466, 'A lunch made by your younger sister just for you. It never spoils because of love. It is said that just eating it generates negative ions around you and has an amazing relaxation effect, but I have yet to eat it... \\n# ~report of <Moxis>, leading imouto researcher~'):
        "Un pranzo al sacco che tua sorella minore ha fatto solo per te. C'è dentro l'amore, quindi non va mai a male. Dicono che soltanto a mangiarlo intorno si formino ioni negativi e che l'effetto di rilassamento sia straordinario, ma io non l'ho ancora mai mangiato... \\n# ~Studio di <Moxis>, massimo esperto di sorelle minori~",

    # ---------------------------------------------------------- :86800
    (86800, "It is said that when eaten, a fountain of knowledge springs up in one's head. A famous wizard spent all his knowledge in researching this fruit so that he could obtain it permanently, but in the end he was unable to propagate it. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un frutto che, dicono, a mangiarlo fa sgorgare in testa una fonte di sapere. Un mago di gran fama, per averne per sempre, ci spese sopra tutto il suo sapere; ma alla fine a farlo crescere non ci riuscì. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :87253
    (87253, 'Fragrant cheese that is said to be full of life force when eaten. Since ancient times, it is said to have been a favorite food of brave and daring heroes. \\n#~Everchanging Food of Tyris~'):
        "Un formaggio profumato che, dicono, a mangiarlo riempie di forza vitale. Fin dai tempi antichi, si racconta, era il preferito degli eroi coraggiosi e arditi. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :88275
    (88275, 'A rare apple with a faint golden color. It is said to contain plenty of honey and good fortune, and in the past, people wandered the continent in search of this miraculous fruit. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una mela rara che luccica appena di un colore d'oro. Dentro, dicono, c'è miele in abbondanza e insieme la fortuna, e in passato la gente vagò per il continente in cerca di questo frutto miracoloso. \\n# ~Dizionario Fantastico di Irva~",

# 34 voci, 0 ambigue
}
