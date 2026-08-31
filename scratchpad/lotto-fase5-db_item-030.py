# -*- coding: utf-8 -*-
"""114a - Lotto 030 di `db_item.hsp`: IL MOBILIO, quarta parte.

`FILTER_FURNITURE`, righe 108.000-113.000: **53 righe** su 51 oggetti — 51
dell'indice 0 e due dell'indice 2 (`:110801` e `:112509`). E' il primo lotto
del tratto **alto** del file: dopo il 029 il mobilio che resta sta tutto sopra
la riga 108.000, e questo ne prende la prima meta'.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **I sette giacigli** (`:109526` soffice, `:109903` dozzinale, `:110478`
  pulito, `:110669` accogliente, `:110865` misero, `:110931` gigante,
  `:111324` di lusso) piu' la **bara** (`:110799`), che il giapponese chiama
  寝具 come gli altri sette: e' un giaciglio anche lei, e la battuta di <Ainc>
  che segue gioca proprio su questo. Tutte e otto le rese aprono con
  «Un giaciglio», che e' la parola che tiene insieme la famiglia.
- **I sette scaffali e le due toelette**: `:109460` e `:109713` dicono la
  **stessa formula** — 機能美を究極/極端までに追求した, «insegue fino in
  fondo / all'estremo la bellezza dell'utile» — uno di uno scaffale e una di
  una toeletta. Le due rese si rispondono.
- **I quattro tavoli da gioco** (`:110155` freccette, `:110220` slot,
  `:110285` casino', `:110350` pachislot): tutti e quattro 遊技台, «tavolo da
  gioco», e ciascuno apre con quella parola.
- **I due scaffali gemelli** (`:111573` i ninnoli, `:111635` i casalinghi): la
  **seconda frase giapponese e' identica parola per parola**. La resa della
  seconda frase e' identica nelle due righe, e per riuscirci il soggetto e'
  «il mucchio» — un soggetto che va bene sia per i ninnoli (maschile plurale)
  sia per la roba (femminile singolare).

### ⭐⭐⭐ L'INGLESE SBAGLIA TRE VOLTE, E DUE SONO ROVESCIAMENTI

1. **`:109083`, il tavolo — l'inglese e' la COPIA di quello del trono.**
   `:108954` (il trono) e `:109083` (il tavolo) hanno **lo stesso identico
   inglese**: «A magnificent chair made only for the king to sit on...». Il
   giapponese del tavolo dice tutt'altro — 物が載せられているテーブル。
   大きさからするとテーブルというより机といった方が正しいだろう, un tavolo con
   sopra della roba, e a giudicare dalla grandezza sarebbe piu' giusto
   chiamarlo scrivania. E' la forma che `_104-inglese-slittato.py` cerca sulle
   carte, e qui si e' vista **leggendo il dossier**, perche' le due righe
   stanno a 129 righe di distanza e nessuna rete di lotto le confronta.
2. **`:109335`, il pianoforte verticale — l'inglese perde la negazione.**
   長旅には適さないだろう: per un viaggio lungo **non** va bene. L'inglese
   scrive «still heavy enough to be suitable for long trips», che dice il
   contrario.
3. **`:109903`, il letto dozzinale — l'inglese rovescia la frase.**
   余り疲れは取れないだろう: la **stanchezza non se ne va** granche'. L'inglese
   scrive «you will probably not get very fatigued», cioe' che non ci si
   stanca. E' l'opposto del punto del testo, che e' un letto che non riposa.

⚠️ E un'aggiunta e un taglio piu' piccoli: `:110220` (la slot) **butta via la
prima frase** 絵柄を揃えて楽しむ遊技台 e sbaglia la seconda — ７が揃った vuole
i sette **tutti e tre** allineati, mentre l'inglese scrive «when a seven
appears in any of the three frames». `:112382` (il salvagente) **aggiunge**
delle piscine che il giapponese non ha.

### ⭐⭐ `:112509` NON HA GIAPPONESE AFFATTO

E' l'appunto sulla tinozza — `\\"Not suitable for golems\\"` — e nel dossier il
campo `JP` e' **vuoto**: e' un'aggiunta del CGX. Delle cinque fonti della 110a
qui ne resta **una sola**, l'inglese, e la resa si scrive da li'.

### ⭐ I TERMINI CERCATI A MANO

    ポート・カプール -> Porto Kapul          (`chat.hsp`, gia' nel dizionario)
    白き癒し手       -> la bianca guaritrice (癒し手 -> «guaritrice»)
    大地の神         -> il dio della terra   (Opatos, `db_item.hsp` e `book`)
    ゴーレム         -> il golem             (`db_creature.hsp`)
    ブラックジャック -> blackjack            (`chat.hsp`, invariato)
    パルミア         -> Palmia               (`invariati.md:41`)

### ⭐ LE TRE FORME DELLA MARCA, e perche' `#~ ` perde lo spazio

L'inglese scrive la riga-fonte in **tre** modi: `# ~Titolo~` (118 righe),
`#~Titolo~` (43) e `#~ Titolo~` (7), con uno spazio **dentro** il titolo. Il
dizionario rende il terzo caso come il secondo, `#~Titolo~`, e lo fa **7 volte
su 7** da sessioni precedenti: `lotti-113/_code.py` fa lo stesso, e va bene
cosi'. Il motivo non e' l'imitazione ma il cancello: `_112-corpo-descrizioni.py`
conta i **titoli resi in piu' modi**, e mescolare `#~ Grande Enciclopedia~` con
`#~Grande Enciclopedia~` lo accenderebbe.

⚠️ Un'altra forma invece **si conserva**: `:111511` e' l'unica riga del lotto
in cui l'inglese non mette lo spazio prima del `\\n`.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-030.jsonl'
RIGHE = {
    108393, 108829, 108891, 108954, 109083, 109145, 109270, 109335, 109398, 109460,
    109526, 109588, 109650, 109713, 109775, 109837, 109903, 109966, 110028, 110090,
    110155, 110220, 110285, 110350, 110412, 110478, 110541, 110603, 110669, 110733,
    110799, 110801, 110865, 110931, 110993, 111125, 111188, 111258, 111324, 111386,
    111449, 111511, 111573, 111635, 111697, 112320, 112382, 112445, 112507, 112509,
    112569, 112631, 112693,
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
