# -*- coding: utf-8 -*-
"""113a - Lotto 027 di `db_item.hsp`: IL MOBILIO, prima parte.

`FILTER_FURNITURE`, righe 55.600-80.200, indici 0 e 2: **42 righe su 41
oggetti**. Il fronte intero e' di 251 righe sull'indice 0 piu' 10 sull'indice 2
— la categoria piu' grossa del corpo — e questo e' il primo taglio.

⚠️ L'indice 1 qui non c'e': in tutta la categoria e' vuoto.

### ⭐ DIECI TITOLI-FONTE, e il mobilio ne porta molti piu' del cibo

Il cibo stava su otto code, e trentotto righe su cinquanta erano lo stesso
libro. Qui i libri sono **sedici** in quarantadue righe, e i due che pesano
sono `~Catalogo d'Arte di Lumiest~` (10) e `~Grande Enciclopedia dei Mobili di
Tyris del Nord~` (14). ⚠️ Quest'ultimo l'inglese lo scrive in **tre** forme
diverse — con e senza lo spazio dopo il `#`, con e senza lo spazio dopo la
tilde — e la tabella le riconduce a una.

### ⚠️⚠️ DIECI TITOLI DELLA TABELLA AVEVANO L'APOSTROFO AL POSTO DELL'ACCENTO

`~Scoperta! Le Rarita' del Mondo~`, `~Parole di un Avventuriero che si e'
Risvegliato~` e altri otto: la forma **degradata**, che nel dizionario e' un
errore che `verifica.py` segnala. La degradazione la fa `applica.py`, e la
fonte di verita' porta l'accento vero.

💡 Non se n'era accorto nessuno perche' il cibo non usava nessuno di quei dieci:
il primo lotto che ne tocca due e' questo. ⓘ La lunghezza non cambia — `à`
degrada in `a'`, due caratteri come prima — quindi il cancello dei 66 resta a
55 con margine 11, identico.

### ⭐⭐ L'INGLESE SBAGLIA SEI VOLTE, E SEI VOLTE SI SEGUE IL GIAPPONESE

1. **`:72884`, il koma-inu 吽形.** L'inglese scrive «with its mouth **open**»,
   copiato dal gemello `:72822`: il giapponese dice 口を**閉じた**, chiusa. E'
   la coppia che sta ai due lati del cancello, e l'inglese ne fa due uguali —
   perfino la frase «sometimes called a lion», che il giapponese ha solo sul
   primo. ⚠️ Un difetto che nessuna rete puo' vedere: gli inglesi sono quasi
   identici, e la differenza sta in due kanji.
2. **`:65331`, il cuscino-pecora.** L'inglese ha **perso una frase intera** —
   「広大な草原で、心地よい風に吹かれながら寝ている羊になった夢」, il sogno di
   essere una pecora che dorme in una prateria sconfinata — e attacca diretto
   con «However, on rare occasions». Senza quella frase il «pero'» non regge su
   niente, e la riga non vuol dire piu' nulla.
3. **`:78789`, il piatto grande.** «They range from the most expensive to the
   most expensive»: e' ピンからキリまで, *dal meglio al peggio*.
4. **`:66575`, il Budda.** «Sacred trees such as sacred trees» per 御神木などの
   神聖な木.
5. **`:66703`, la cuccia.** «constructed to prevent **ventilation**»: e'
   隙間風, gli **spifferi**.
6. **`:57707`, il busto di Itzpalt, e `:57769`, il dipinto di Ehekatl.**
   Tutt'e due perdono la prima proposizione — il lato di 猛る炎の魔神 nel primo,
   e nel secondo il pittore che *assiste* alla scena, che l'inglese riduce a
   un'apposizione senza verbo.

### ⭐ I TERMINI CERCATI A MANO

    魔導船      -> nave magica            (`db_item.hsp`, gia' nel dizionario)
    クリスマスツリー -> albero di Natale
    狛犬        -> koma-inu               (invariato, e il nome dell'oggetto)
    地蔵        -> zizou                  (la statua austera, decisa nella 109a)
    癒しの女神    -> la dea della cura      (癒しのジュア «Jure della Cura»)
    聖夜祭      -> la festa
    <Gould's Piano> -> <Pianoforte di Gould>

⚠️ **`:68913`, il flauto dolce, perde un gioco di parole e non si puo' fare
altrimenti.** 「記録するもの、の名を持つ縦笛」: il flauto che porta il nome di
*chi registra*, perche' in inglese `recorder` e' tutt'e due. In italiano si
chiama flauto dolce, e il rimando si tiene dicendo che quel nome ce l'ha **in
un'altra lingua** — che e' vero, e non spiega la battuta.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-027.jsonl'
RIGHE = {
    55673, 55735, 55797, 57446, 57508, 57707, 57769, 57831, 59997, 63869,
    65331, 66385, 66451, 66513, 66575, 66641, 66703, 68848, 68913, 68978,
    70127, 72822, 72884, 73352, 73354, 74568, 76520, 78789, 78919, 78981,
    79044, 79303, 79366, 79636, 79698, 79764, 79826, 79888, 79950, 80012,
    80082, 80149,
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
