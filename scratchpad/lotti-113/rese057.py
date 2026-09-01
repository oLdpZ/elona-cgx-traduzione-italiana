import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :57125
    (57125, 'Envelope made of thick brown paper. The sender is not written, but a letter is attached. \\n# ~Gifts that I am Happy to Receive~'):
        "Una busta fatta di carta marrone e spessa. Chi la manda non c'è scritto, ma insieme c'è una lettera. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :57127
    (57127, '\\"Thank you for generously opening up your unique collection of fossils to the public. They are things that we would not be able to see if we lived in a straight life, and they excite me every day. Keep up the good work in collecting these unique finds!\\" \\n# ~words of an Fossil Enthusiast~'):
        "\\\"La ringrazio d'aver aperto al pubblico, con tanta generosità, le sue statuette uniche. Sono tutte cose che una vita per bene non permetterebbe di vedere, e mi emozionano un giorno sì e l'altro pure. Continui così a raccogliere statuette uniche!\\\" \\n# ~Lettera di un Fissato di Tassidermia~",

    # ---------------------------------------------------------- :78658
    (78658, 'Pack of 5 collectible cards. The contained cards have no images, but can be putted into your deck.\\n# ~Heated Duelists~'):
        "Le carte che ci sono dentro non mostrano l'immagine finché non le metti nel mazzo.\\n# ~Duellanti Ardenti~",

    # ---------------------------------------------------------- :80736
    (80736, 'In some regions, it is customary to give gifts to acquaintances at the beginning of the year. The gifts are filled with good things for those who are close to the recipient, but on the other hand, for those who are not so close to the recipient, a prank is sometimes played on the recipient. It is said that some people become a good person on all sides just for this reason. \\n# ~Gifts that I am Happy to Receive~'):
        "In certe zone c'è l'usanza di farne dono ai conoscenti all'inizio dell'anno. A chi si è amici ci si mette dentro roba buona in proporzione; a chi lo si è meno, invece, capita che ci si nasconda uno scherzo. Si dice che ci sia chi, solo per questo, si mette a fare il gentile con tutti. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :81260
    (81260, 'Cat in a box. Whether the cat inside is alive or dead will not be known until the box is opened. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una scatola dentro cui è stato messo un gatto. Se il gatto lì dentro sia vivo o morto, non lo si saprà finché non si prova ad aprirla. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81941
    (81941, '\\"A great experience for a handful of lucky people! Please bring your lockpicks to the challenge.\\" \\n# ~note written on the back of the box~'):
        "\\\"Un'esperienza sublime per una manciata di fortunati! Chiunque voglia tentare, si presenti col grimaldello\\\" \\n# ~Avvertenza Scritta sul Retro della Scatola~",

    # ---------------------------------------------------------- :88147
    (88147, 'A mechanical box that allows food to be stored without spoiling. Extremely useful item, but only holds four kinds of food, so beware if you are going on a picnic with a lot of people. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una scatola a ingranaggi, che conserva il cibo senza farlo marcire. È comodissima, ma ci stanno solo quattro qualità di cibo: attenzione, quando si va a far merenda in molti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :89821
    (89821, 'Special box for payment of designated taxes. Visit the Palmia Embassy to pay tax once a month. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola apposita, per versare le tasse dovute. Una volta al mese conviene fare un salto all'ambasciata di Palmia. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :90832
    (90832, 'Huge, sturdy fetters made of metal. It does not seem to be affected by pushing or pulling, but the joints seem to be a little loose. \\n# ~Top 50 Most Popular Products Among Prisoners~'):
        "Un ceppo di metallo, enorme e saldo. A spingerlo o a tirarlo pare non muoversi di un dito, eppure a guardarlo bene la giuntura sembra un po' allentata. \\n# ~I 50 Prodotti Preferiti dai Detenuti~",

    # ---------------------------------------------------------- :92186
    (92186, 'A work of wisdom that can store foodstuffs semi-permanently. However, there is a secret to this furniture. No matter how many units you own, their doors can only lead to the same space! \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un frutto dell'ingegno, che conserva gli ingredienti quasi per sempre. C'è però un segreto in questo mobile: per quanti se ne posseggano, oltre lo sportello si arriva sempre e solo allo stesso spazio! \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :93420
    (93420, "A special safe that takes care of all the store's sales. For security purposes, the system is such that it can never be opened outside of the store. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~"):
        "Una cassaforte apposita, che raccoglie tutto l'incasso del negozio. Contro i furti, è congegnata in modo da non aprirsi mai fuori dal negozio. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :93422
    (93422, 'A safe is essential to running a store. This is where all sales proceeds are stored. \\"If you lose it by accident, don\'t worry. Everything is available at the Palmia Embassy, the keystone of the economy.\\" \\n# ~Tyris Armor Compendium, page of advertisements~'):
        "Una cassaforte indispensabile per mandare avanti un negozio. Qui dentro finisce tutto l'incasso. \\\"Se un incidente ve la fa perdere, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    # ---------------------------------------------------------- :93483
    (93483, 'A special box for the delivery of designated items. It is said that a little effort is made at the slot to prevent wrong everything from being dumped. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola apposita, per consegnare la merce richiesta. Pare che la fessura abbia qualche accorgimento, perché non ci si butti dentro di tutto. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :94381
    (94381, 'A box to receive the earned salary twice a month. Even if the box is lost due to unforeseen circumstances, the salary will be properly transferred. But remember that Palmia officials are inflexible, you need to buy another box from them. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola per ritirare la paga, due volte al mese. Anche se un imprevisto la fa perdere, la paga viene versata lo stesso; conviene però ricordarsi che i funzionari di Palmia non fanno sconti a nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :96844
    (96844, 'An old briefcase. Inside the briefcase are items left behind by those who left the continent in the midst of their ambitions. To receive them, one must follow the proper procedures. \\n# ~Book for the Dying Ones~'):
        "Una borsa vecchiotta. Dentro ci stanno le cose lasciate da chi se n'è andato dal continente a metà del cammino. Per averle bisogna passare per la trafila dovuta. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :103233
    (103233, "Sphere containing some item. Inside it is filled with hope in the name of 'desire'. \\n# ~Game Tricks, All Ages Version~"):
        "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"brama\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :103295
    (103295, "Sphere containing some item. Inside it is filled with hope in the name of 'expectation'. \\n# ~Game Tricks, All Ages Version~"):
        "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"attesa\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :104725
    (104725, 'A black box that pops out materials when opened. A wide variety of items pop out all at once, but no one knows how they fit into this box. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola nera da cui, ad aprirla, saltano fuori i materiali. Ne esce di tutto in una volta sola, e si dice che come ci stiano dentro non lo sappia nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :107114
    (107114, 'A briefcase filled with the best goods that a peddler has worked tirelessly to collect. For security purposes, the bag is said to be enchanted with a spell that makes people feel extremely guilty if anyone other than the registered owner opens it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Una borsa piena dei pezzi pregiati che un mercante ambulante ha raccolto con la propria fatica. Contro i furti, si dice porti addosso una magia che a chi la apre, e non sia l'intestatario, mette dentro un'inquietudine fortissima. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :112196
    (112196, '\\"Oh, I found a wallet here. Good, I was worried it might be lost. You say I look familiar? That\'s right, \'cause I have a lot of wallets.\\" \\n# ~words of the honest? rogue~'):
        "\\\"Oh, un portafoglio qui. Meno male, ero in pena perché credevo d'averlo perso. Dici che somiglia a quello che hai perso tu l'altro giorno? Ma certo che sì: è perché di portafogli io ne ho tanti\\\" \\n# ~Parole di <Onest> il farabutto~",

    # ---------------------------------------------------------- :112258
    (112258, '\\"This bag belongs to me. No, I used to have it. No, I remember I had it, no, I wanted to buy it - no, wait. Oh yes, I remember, it was a bag that some old gentleman put there. In other words, it belonged to me.\\" \\n# ~words of <Gleed> the thief~'):
        "\\\"Questa borsa è mia. Anzi no, ce l'avevo tempo fa. Anzi, mi ricordo d'averla avuta; anzi, la volevo comprare... anzi, aspetta. Ah, ecco, mi è tornato: era la borsa che aveva posato lì un vecchio signore. E dunque è mia\\\" \\n# ~Parole di <Gleed> il topo d'appartamento~",

    # ---------------------------------------------------------- :115134
    (115134, '\\"Is there hope inside, or is it despair? I guess the only thing I know is that for those who keep it, it\'s all despair.\\" \\n# ~words of <Marks> the great thief~'):
        "\\\"Dentro c'è la speranza, oppure la disperazione? L'unica cosa che si può sapere è che per chi la tiene chiusa lì non sarà altro che disperazione\\\" \\n# ~Parole di <Marks>, ladro senza pari~",

    # ---------------------------------------------------------- :115196
    (115196, 'A box containing items that are said to be mainly kept in Nephia. The boxes are made to be very heavy so that adventurers who cannot unlock them will not be able to rob them by brute force. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola che custodisce oggetti, e che si dice stia soprattutto nelle Nefia. È fatta pesantissima, perché l'avventuriero che non riesce ad aprirla non se la porti via a forza. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :115258
    (115258, 'A shining treasure box decorated with jewelry. Despite its appearance, it is surprisingly lightweight, and some customers seem to buy it as a glamorous accessory box. \\n# ~Censored! Box Mania, First Issue~'):
        "Un baule splendente, ornato di gioielli. Contro le apparenze è insolitamente leggero, e con quel rivestimento sfavillante pare che ci siano clienti che lo comprano per tenerci le cianfrusaglie. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

# 22 voci, 0 ambigue

    # ---------------------------------------------------------- :115260
    (115260, '\\"I\'ve been here all my life, sifting through the stolen goods, and I\'ve been surprised twice in the past. The first time was by a gentleman who brought me a golden statue of a giant god. The second time was to a man like you who brought not the contents of the treasure, but its bejeweled exterior.\\" \\n# ~words of <Abyss> the thief watchman~'):
        "\\\"Io sto qui da sempre a stimare la refurtiva, e in tutto questo tempo mi sarò stupito sì e no due volte. La prima per il maestro, che mi portò una statua d'oro di un gigante. La seconda per uno come te, che della refurtiva mi ha portato non il dentro, ma il fuori\\\" \\n# ~Parole di <Abyss> il guardiano della Gilda dei Ladri~",

# 3 voci, 0 ambigue
}
