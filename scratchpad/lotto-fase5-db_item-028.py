# -*- coding: utf-8 -*-
"""113a - Lotto 028 di `db_item.hsp`: IL MOBILIO, seconda parte.

`FILTER_FURNITURE`, righe 80.200-91.500, **indice 0 soltanto**: 46 righe su 46
oggetti, una firma per riga. Continua il lotto 027; del fronte del mobilio
restano 164 righe dell'indice 0 e 9 dell'indice 2.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **Le due scale** (`:80798`, `:80860`): 「地下へようこそ！」 e
  「地上へおかえり！」 — *benvenuti* di sotto, *bentornati* di sopra. Il
  giapponese distingue l'andare dal tornare, e l'inglese scrive «Welcome» tutt'e
  due le volte. Le rese restano due.
- **I due letti di fama** (`:87893` la cassettiera, `:90012` il letto): tutt'e
  due 国王御用達, *fornitore del re*. Stessa formula, stessa resa.
- **Le sette finestre** (`:87126`, `:87955`, `:90074`, `:90261`, `:90323`,
  `:91088` piu' `:87064` il lume): ciascuna ha il suo tratto e nessuna
  ripete l'altra.
- **Le quattro piante in vaso** (`:90199`, `:90385`, `:90511`, `:90573`).

### ⭐⭐ L'INGLESE SBAGLIA QUATTRO VOLTE

1. **`:87505`, la credenza di pregio.** L'inglese si ferma a «A cupboard created
   by professionals who put their hearts and souls into their work» e **butta
   via la seconda frase**: 「一見シンプルに見えるが、普段見えない部分に匠の遊び心が
   隠れている」 — a prima vista sembra semplice, ma dove non si guarda c'e'
   nascosto l'estro del maestro. E' la frase che dice l'oggetto.
2. **`:87769`, la lavagna.** 白墨 e' il **gesso**; l'inglese scrive «white ink».
3. **`:88083`, il barile di riso.** 米俵 e' un **sacco di paglia**, non un
   barile: il nome dell'oggetto e' «barile di riso» e resta com'e' (e' il nome),
   ma la prosa dice quel che il giapponese dice.
4. **`:91274`, il lampione innevato.** 「長身の紳士」, *il signore allampanato*,
   **e' il lampione**: e' lui che illumina. L'inglese lo legge come una persona
   («the light gently illuminated by a tall gentleman»), e la riga perde
   l'immagine intera.

### ⭐ I TERMINI CERCATI A MANO

    シルバーキャット -> il gatto d'argento   (`db_item.hsp`, gia' nel dizionario)
    バーベキューセット -> set da barbecue     (`db_item.hsp:144489`)
    <Stradivarius>  -> <Stradivarius>       (invariato)
    daruma, kotatsu, chochin  -> invariati, gia' in `invariati.md`

⚠️ `:90637`, la poltrona direzionale, nomina **due** oggetti del gioco — il
gatto d'argento e il whisky — e tutt'e due hanno gia' un nome nel dizionario.
E' il caso che la 110a ha incontrato trentacinque volte: prima di coniare, si
guarda se il **nome dell'oggetto** c'e' gia'.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-028.jsonl'
RIGHE = {
    80612, 80674, 80798, 80860, 82275, 82875, 83764, 84644, 84709, 84774,
    84839, 84904, 87002, 87064, 87126, 87188, 87319, 87381, 87443, 87505,
    87644, 87707, 87769, 87831, 87893, 87955, 88083, 88803, 89212, 89946,
    90012, 90074, 90199, 90261, 90323, 90385, 90449, 90511, 90573, 90637,
    91088, 91150, 91212, 91274, 91336, 91398,
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
