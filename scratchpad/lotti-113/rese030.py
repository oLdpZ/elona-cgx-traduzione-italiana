import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :108393
    (108393, "Stone with ancient letters written on it. When used, it is said to open a gateway to another world. \\n#~ Worlds you've Never Seen~"):
        "Una pietra con sopra scritti caratteri antichi. A usarla, dicono, si apre l'ingresso di un posto che non sta in questo mondo. \\n#~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :108829
    (108829, 'A flashy shiny golden statue representing a symbol of wealth. It is said that if you have several of them in your house, your friends will call you a parvenu. \\n# ~Totally Made-up Stories that are Mistaken for Lies, Volume 2~'):
        "Una statua d'oro dal luccichio vistoso, fatta a immagine della ricchezza. A tenerne in casa parecchie, dicono, l'amico che torna dopo tanto ti dà del nuovo ricco. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # ---------------------------------------------------------- :108891
    (108891, 'Golden columns decorated with flowers and grasses are a glittering work of art. In addition to the detailed carvings, the material used for the sculpture is said to shine even more brightly at night when bathed in ambient light. \\n# ~Lumiest Art Catalogue~'):
        "Un'opera d'arte sfolgorante: una colonna d'oro guarnita di erbe e fiori. Belli gli intagli minuti, ma è il materiale che conta: di notte, dicono, prende la luce intorno e brilla ancora di più. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :108954
    (108954, 'A magnificent chair made only for the king to sit on. Since it is not intended for mass production, it is made with the utmost luxury. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una sedia magnifica, fatta perché ci si sieda il re e nessun altro. Nessuno ha pensato a produrla in serie, e così è lavorata con ogni lusso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109083
    (109083, 'A magnificent chair made only for the king to sit on. Since it is not intended for mass production, it is made with the utmost luxury. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo con sopra della roba. A giudicare dalla grandezza, più che un tavolo sarebbe giusto chiamarlo scrivania. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109145
    (109145, 'Beautiful garment of the latest model. It is very delicately made and cannot even be tried on. \\n# ~Palmian Winter Fashion~'):
        "Un bel tessuto dell'ultimo modello. È fatto in modo così delicato che non lo si può nemmeno provare. \\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :109270
    (109270, "The furnishings exude prestige. Perhaps it is because of its spiritual significance, or perhaps it is because it is polished every day. It lights up the surroundings at night. \\n# ~Worlds you've Never Seen~"):
        "Una suppellettile da cui si sente la maestà. Sarà la sua virtù miracolosa, o forse che la lucidano ogni giorno: di notte fa una luce viva tutto intorno. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :109335
    (109335, 'Rectangular black box-like keyboard instrument. It is lighter than a grand piano, but still heavy enough to be suitable for long trips. \\n# ~Music of the Melodious Irva~'):
        "Uno strumento a tasti che pare una scatola nera rettangolare. È più leggero del pianoforte a coda, ma pesa comunque anche troppo, e per un viaggio lungo non va bene. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :109398
    (109398, 'A horizontal chair made of hard material. When placed outdoors, it is said that on rare occasions some people take a nap on it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una sedia lunga di traverso, fatta di materiale duro. Quando ne mettono una all'aperto, dicono, ogni tanto ci si trova qualcuno che ci schiaccia un pisolino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109460
    (109460, 'This shelf is the ultimate pursuit of functional beauty. It is a truly elegant piece of furniture with no unnecessary functions. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale che insegue fino in fondo la bellezza dell'utile. Non ha nemmeno una funzione di troppo: un mobile di una nettezza esemplare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109526
    (109526, "The bedding is so soft that one's hands sink into it, and when the bedding is just right and the quilt is full of the smell of the sun, one is enveloped in a strange sensation as if one were a baby again. \\n#~ Great Encyclopedia of North Tyris Furnitures~"):
        "Un giaciglio così morbido che la mano ci affonda. Quando il letto che cede al punto giusto si unisce a una coperta piena di odore di sole, dicono, ti prende una sensazione strana, come di essere tornato neonato. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109588
    (109588, 'Small altar shining brightly. Since it is more of a furnishing element, it does not seem to be able to accommodate offerings. \\n# ~Daily Necessities for the Home~'):
        "Un piccolo altare che risplende. Conta più come suppellettile che come altare, e infatti pare che non ci si possano fare offerte. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :109650
    (109650, 'A cupboard made larger than usual. It is mainly a piece of furniture for nobles who host parties with many guests. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una credenza fatta più grande del solito. È un mobile pensato per i nobili, che invitano molta gente e danno feste. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109713
    (109713, 'A mirror stand that pursues functional beauty to the extreme. It is a piece of furniture that is so drastic that it makes one think that a mirror is all that is needed. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una toeletta che insegue all'estremo la bellezza dell'utile. Un mobile così risoluto da far pensare che basti lo specchio e nient'altro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109775
    (109775, 'Clean, dust-free shelves. They are often bought by indolent customers because of their reputation for staying this way for several years. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale pulito, senza un granello di polvere. Ha fama di restare così per anni, e per questo, dicono, lo compra spesso il cliente pigro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109837
    (109837, 'This is a desk with an uneven surface for artistic purposes. Due to its characteristics, it is not suitable for precision work. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo a cui hanno dato apposta un piano tutto gobbe, per un'intenzione d'arte. Fatto così, per il lavoro di precisione non va. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109903
    (109903, 'Bedding with only the bare minimum of functionality. Even if you use this bed, which is said to be used for meditation rather than sleeping, you will probably not get very fatigued. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio con il minimo indispensabile e nient'altro. C'è chi dice che serva più a passare il tempo a occhi chiusi che a dormire, e infatti a usarlo la stanchezza non se ne va granché. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :109966
    (109966, 'The bookshelves are so old that even the books in them seem to have a certain charm. The unique damage to the bookshelf is said to be irresistible to antique lovers. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una libreria tanto vecchia che perfino i libri dentro sembrano avere una storia. Quel modo tutto suo di essersi rovinata, dicono, manda in visibilio chi ama le cose antiche. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110028
    (110028, 'The shelf has a somehow nostalgic atmosphere. Its texture resembles the warmth of wood that I certainly touched as a child. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale che ha addosso, chissà da dove, un'aria di cose passate. Al tatto somiglia al tepore del legno che da bambini si è toccato di sicuro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110090
    (110090, 'Potted plant stands out for its lush foliage. The lush foliage growing sideways is truly full of vitality. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso che si fa notare per il fogliame folto e verdissimo. Le foglie tenere, allungate proprio di lato, traboccano davvero di vita. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :110155
    (110155, 'A game table where you can enjoy throwing darts at the target. Some adventurers play with it to see if their throwing skills have improved. \\n# ~Game Tricks, All Ages Version~'):
        "Un tavolo da gioco dove ci si diverte a piantare la freccetta dove si mira. Pare che qualche avventuriero ci giochi per mettersi alla prova e vedere se è migliorato nel lancio. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :110220
    (110220, 'Legend has it that when a seven appears in any of the three frames, a mysterious voice is heard from the heavens. \\n# ~Game Tricks, All Ages Version~'):
        "Un tavolo da gioco dove ci si diverte a far combaciare le figure. Pare ci sia una leggenda: quando nei tre riquadri escono tre sette, dal cielo rimbomba uno strano grido che nessuno sa spiegare. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :110285
    (110285, 'This is an amusement table where you can enjoy a variety of grown-up games. It claims to be able to do everything, but the staff is stubborn and will only let you play blackjack. \\n# ~Game Tricks, All Ages Version~'):
        "Un tavolo da gioco con ogni sorta di svaghi da adulti. Si vanta che ci si può fare di tutto, ma il commesso non demorde e ti lascia giocare solo a blackjack. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :110350
    (110350, 'An amusement table that uses a small metal ball. It can be played by a single person in a short time, but it is said that sometimes people get too absorbed in the game and find that it is nighttime before they realize it. \\n# ~Game Tricks, All Ages Version~'):
        "Un tavolo da gioco che va a palline di metallo. Ci si gioca anche da soli e in poco tempo, ma pare che a volte ci si scaldi troppo e ci si accorga solo dopo che è venuta notte. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :110412
    (110412, 'Furniture that stores hot water and heals the body by soaking. Floating bubbles in it is said to be popular among aristocrats. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un mobile che si riempie d'acqua calda e cura il corpo di chi ci si immerge. Fra i nobili, pare, va di moda farci galleggiare sopra la schiuma. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110478
    (110478, 'The bedding is crisp right down to the hem of the sheets. Its cleanliness is often likened to that of a white healer and sold as such. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio ben teso fin sull'orlo del lenzuolo. È così pulito che spesso, dicono, per venderlo lo paragonano alla bianca guaritrice. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110541
    (110541, 'A mirror stand used by the public. This is basically a piece of furniture whose value is determined by the amount of decoration, so it would be perfect in terms of functionality. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una toeletta di quelle che usano tutti. È un mobile il cui valore si misura in fondo su quanti ornamenti porta, e quanto a servire allo scopo questa non ha niente da farsi perdonare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110603
    (110603, 'The shelves are simply made. It is reasonably priced, so if you are living alone, this is probably enough. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale di fattura spartana. Costa poco, e per chi vive da solo tanto basta. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110669
    (110669, "The bedding's soothing colors are easy on the eyes. The bed is simple, with no superfluous features, so it seems to be surprisingly popular with men as well. \\n#~ Great Encyclopedia of North Tyris Furnitures~"):
        "Un giaciglio dai colori riposanti, che calmano l'animo. È un letto semplice, senza una funzione di troppo, e forse per questo pare piaccia molto anche agli uomini. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110733
    (110733, 'An excellent cooking utensil that crushes food with its sharp blade. It is said that there used to be a pair of merchants in Palmia who would put on somewhat deliberate skits in order to sell these extremely expensive utensils. \\n# ~Supporting Roles in Kitchen~'):
        "Un ottimo arnese da cucina che sminuzza i cibi con lame affilate. A Palmia, un tempo, pare ci fosse una coppia di mercanti che per vendere questo arnese carissimo si metteva a recitare una scenetta un po' finta. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :110799
    (110799, 'Bedclothes that are not normally used by living people. Some adventurers seem to have no choice but to use it because it at least shelters them from the wind and rain. \\n#~ Book for the Dying Ones~'):
        "Un giaciglio che chi è vivo di regola non usa. Almeno ripara dalla pioggia e dal vento, e pare che qualche avventuriero, non avendo di meglio, ci si adatti. \\n#~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :110801
    (110801, '\\"It is too hard to be used as bedding, and it\'s sturdy enough to withstand attack from any direction. The only drawback is that you have to get out of it somehow.\\" \\n# ~words of <Ainc> the novice knight~'):
        "\\\"È così duro che tenerlo per giaciglio è quasi uno spreco, e finché ci stai dentro non ti arriva un colpo da nessuna parte. Il difetto, semmai, è che per colpire devi uscirne\\\" \\n# ~Parole di <Ainc> il cavaliere novizio~",

    # ---------------------------------------------------------- :110865
    (110865, 'This bedding is rattling in places. Just lying on the bed is noisy and noisy, so people with nervousness will not be able to sleep on it. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio che qua e là comincia a cedere. Basta stendercisi che scricchiola e fa baccano, e chi ha il sonno delicato non riuscirà a dormirci. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110931
    (110931, 'The bedding is more than enough even if you sleep with arms and legs spread wide apart. It is useful when you have a sudden guest and you want to put everyone to bed together. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio dove ci si sdraia a gambe e braccia larghe e avanza ancora posto. Comodo quando arrivano ospiti all'improvviso e bisogna far dormire tutti insieme. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :110993
    (110993, 'A chest of drawers specializing in storing clothes. They are made slightly wider than normal ones and can be used to store different seasons. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassettiera che serve solo a riporre i vestiti. È fatta un po' più larga del solito, così da tenerli divisi per stagione. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111125
    (111125, 'A magnificent desk made to be installed in a bar. It has more storage capacity, but keeps its size unchanged. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo di pregio, fatto apposta per stare in una taverna. Ci sta dentro più roba di prima, e intanto la misura è rimasta quella. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111188
    (111188, 'A mirror stand that looks expensive. It is one of the most coveted pieces of furniture for women. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una toeletta che dà l'idea di costare parecchio. È uno dei mobili che le donne sognano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111258
    (111258, 'Vase made of expensive-looking material. Its surface is so glossy that it shines. \\n# ~Lumiest Art Catalogue~'):
        "Un vaso cotto in un materiale che ha tutta l'aria di costare caro. La superficie è lucida al punto di brillare. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :111324
    (111324, 'The bedding is of the highest quality and made of the finest materials. Its smooth feel gives the illusion that it is a work of art. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio di gran classe, fatto di materiali pregiati senza risparmiarne un filo. Al tatto è così liscio da far credere per un attimo di avere davanti un'opera d'arte. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111386
    (111386, "A cupboard made for storing alcoholic beverages. Don't try to sneak out and drink from it, as it is an act that will cause terrible resentment from those who have saved it for their enjoyment. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un armadietto costruito per tenerci i liquori. Tirarne fuori una bottiglia di nascosto e berla fa odiare a morte da chi la teneva da parte per il piacere: meglio lasciar perdere. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111449
    (111449, 'A desk that has been used for many years and is somewhat worn out. The reason why he continues to use the desk is not only because he is used to using it, but also because he is attached to it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo consumato da anni di uso, che qua e là comincia a cedere. Se lo si tiene lo stesso è anche perché ci si è abituati, ma soprattutto per affetto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111511
    (111511, 'Woven textile with high water absorbency. No fabric softener is used.\\n# ~Palmian Winter Fashion~'):
        "Un tessuto di filo che assorbe molto bene l'acqua. Ammorbidente non ne ha visto.\\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :111573
    (111573, 'Shelves crammed with various decorative items. The items are stacked in a perfect balance so that it is impossible to remove items from them. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale stipato di ninnoli di ogni genere, che non ci sta più niente. Il mucchio sta su per un equilibrio così preciso che di lì non si può tirare fuori niente. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111635
    (111635, 'Shelves crammed with various commodities. The items are stacked in a perfect balance so that it is impossible to remove items from them. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Uno scaffale stipato di roba di tutti i giorni, che non ci sta più niente. Il mucchio sta su per un equilibrio così preciso che di lì non si può tirare fuori niente. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :111697
    (111697, 'Armor that has been beautifully polished and prepared for all eventualities. All of them are marked as sold, so you cannot equip them without permission. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Un'armatura lucidata a dovere e pronta a ogni evenienza. Su ogni pezzo c'è scritto che è già venduto, e perciò non la si può indossare di propria iniziativa. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :112320
    (112320, 'The map has an enigmatic atmosphere. It is said to have no particular remarkable effect, just a sense of significance. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una mappa che si porta addosso un'aria di mistero. Ha solo quell'aria, dicono: un effetto degno di nota non ce l'ha. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :112382
    (112382, 'Buoyancy aid mainly used by non-swimmers to increase their buoyancy. Often seen used by town children in Port Kapul swimming pools. \\n# ~Daily Necessities for the Home~'):
        "Un attrezzo che aumenta il galleggiamento, usato soprattutto da chi non sa nuotare. A Porto Kapul capita spesso di vederlo addosso ai bambini del posto. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :112445
    (112445, 'A warm, circular table. What is it about it that makes you want to use it without chairs or flip the table over with your hands? \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo rotondo che ha qualcosa di caldo. Come mai viene voglia di usarlo senza sedie, o di prenderlo per il bordo e rovesciarlo? Chi lo sa. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :112507
    (112507, 'A very heavy container filled with water. Since it is mainly used for livestock, even the most adventurous of adventurers are not likely to touch it. \\n# ~Supporting Roles on the Streets~'):
        "Un attrezzo pesantissimo, colmo d'acqua fino all'orlo. Serve soprattutto per il bestiame, e pare che nemmeno l'avventuriero più intraprendente ci metta le mani. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :112509
    (112509, '\\"Not suitable for golems\\" \\n# ~a Mysterious Note~'):
        "\\\"Non adatto ai golem\\\" \\n# ~un appunto misterioso~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :112569
    (112569, 'It is the second moonlight. They are always creating shadows for the people on the street without a break. \\n# ~Supporting Roles on the Streets~'):
        "È il secondo chiaro di luna. Loro, senza mai riposare, disegnano l'ombra della gente che passa per la strada. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :112631
    (112631, 'A very heavy pillar, broken from the base for some reason. Its unique shape is somehow artistic. \\n# ~Lumiest Art Catalogue~'):
        "Una colonna pesantissima, spezzata alla base per chissà quale ragione. Quella forma che è solo sua ha, chissà come, qualcosa d'arte. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :112693
    (112693, 'Majestic and very heavy, it is a pillar that stretches straight up to the sky. Its motionless form reminds us of the God of Earth. \\n# ~Lumiest Art Catalogue~'):
        "Una colonna pesantissima e fiera, che sale dritta verso il cielo. Quella figura che non si muove di un capello fa venire in mente il dio della terra. \\n# ~Catalogo d'Arte di Lumiest~",

# 51 voci, 0 ambigue
}
