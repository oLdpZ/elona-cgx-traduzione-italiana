import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :86735
    (86735, "A mysterious heart that continues to beat even now. It is said that just by possessing it, one can possess the hearts of one's enemies. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un cuore misterioso che ancora adesso continua a battere. Dicono che, solo a portarlo addosso, si fa proprio anche il cuore dei nemici. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :91460
    (91460, 'A fashionable scarecrow with a white hat on his head. It is said that this is the figure of a scarecrow that got tired of guarding the farmland and made a bold debut in the city. \\n# ~Totally Made-up Stories that are Mistaken for Lies, Volume 2~'):
        "Uno spaventapasseri elegante, con in testa un cappello bianco. Dicono che sia uno di quelli stanchi di fare la guardia ai campi, che si è deciso a esordire in città. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # ---------------------------------------------------------- :92451
    (92451, 'Brown substance spawned from living organisms. It has an abominable odor, but it is said that some people, perhaps caught up in madness, collect these things. \\n#~Thousands of pieces of Junk I love~'):
        "Un oggetto bruno partorito da un essere vivente. Ha anche un odore, ed è cosa da schifare; eppure pare che qualcuno, forse preso dalla follia, ne raccolga di una certa specie come se ne fosse posseduto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :109208
    (109208, "Plain, unremarkable tree stump. It has a rugged, natural roughness that makes it ideal as a chair for the house! But don't fall for it, because although you can sit on it, it's really just a piece of junk. \\n#~Thousands of pieces of Junk I love~"):
        "Un ceppo d'albero senza niente di speciale. C'è chi te lo vende con l'astuzia dicendo che nel suo essere rozzo c'è l'asprezza della natura ed è perfetto da usare per sedia in casa; ma sederti ci puoi sedere, e per il resto è ciarpame: non cascarci. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :111063
    (111063, 'Miscellaneous goods consisting of cut flowers in a single package. Often used as a thoughtful gift. \\n# ~Gifts that I am Happy to Receive~'):
        "Un articolo fatto di fiori recisi messi insieme. Spesso si usa come dono che viene dal cuore. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :111065
    (111065, '\\"When you are as beautiful as I am, women will come to you, but when I want to approach a woman myself, I usually use this one. Women are weak against things, and the woman I love the most also says so.\\" \\n# ~words of <Raphael> the womanizer~'):
        "\\\"Quando sei bello come me sono le donne a venirti incontro; ma quando voglio essere io ad avvicinarmi, di solito uso questo. Le donne cedono alle cose, sai: me lo diceva anche la donna che amo di più.\\\" \\n# ~Parole di <Raphael> il donnaiolo~",

    # ---------------------------------------------------------- :112755
    (112755, "Tool used for cleaning. It has long been considered an abomination because it symbolizes a magician, but nowadays it is used exclusively as a plaything for children's sword fighting. \\n# ~Daily Necessities for the Home~"):
        "L'attrezzo che si usa per pulire. Dai tempi antichi la si è schifata perché è il simbolo dei maghi, ma oggi è ridotta a un gioco per le spade finte dei bambini. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :112817
    (112817, 'The guardian of the farmland, with its arms outstretched wide, threatening the vermin. Its legs are thrust into the ground, a sign of its will to engage in command without ever leaving the scene. \\n# ~Totally Made-up Stories that are Mistaken for Lies, Volume 2~'):
        "Il guardiano dei campi che, spalancate le braccia, mette paura alle bestie nocive. Che abbia i piedi piantati nel terreno sarà il segno della volontà di non lasciare mai il posto e di eseguire l'ordine. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # ---------------------------------------------------------- :112879
    (112879, 'Wood that has been prepared at a certain height and dried for use as fuel. Because it burns very well, it has a value in daily life, and is not expensive because it is a daily commodity. \\n#~Supporting Roles in Kitchen~'):
        "Legno tagliato a una certa altezza e fatto seccare per farne combustibile. Siccome brucia molto bene ha un suo valore nella vita di ogni giorno; ma essendo roba d'uso comune, caro non si può dire che sia. \\n#~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116408
    (116408, 'Weathered animal bones. There are many opportunities to use the bones for spells and for refining water medicine, but they are in such oversupply that they are worth little more than a dime. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa d'animale sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116470
    (116470, 'Dried and bundled grass. It has some elasticity and could be used for sleeping, but it would be best not to use it to rest, as the day would be consumed with the task of removing the straw from your clothes. \\n#~Thousands of pieces of Junk I love~'):
        "Erba fatta seccare e legata in fascio. Ha una certa elasticità e sembrerebbe buona per dormirci, ma poi la giornata se ne va a togliersi la paglia di dosso: meglio non riposarci sopra. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116540
    (116540, 'Dried fish carcasses. They are worthless and inedible, but when given to children, they are said to hold them in their hands and play with them as if they were legendary creatures. \\n#~Cheap Gifts for Your Kids~'):
        "La carcassa secca di un pesce. Anche a metterla in acqua non si mangia di certo, e non vale niente; ma dandola a un bambino, dicono, se la tiene in mano e ci gioca muovendola come fosse una bestia leggendaria. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :116665
    (116665, 'A bowl with something inside, but it is not food, so you cannot eat it even if you are hungry. \\n# ~Daily Necessities for the Home~'):
        "Un recipiente fatto più largo e più basso di una scodella. Dentro c'è qualcosa, ma non è cibo, quindi anche se hai fame non lo puoi mangiare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :116727
    (116727, 'An empty bowl with nothing inside. It can be used as a tableware, or put a plant in it for decoration. \\n# ~Supporting Roles in Kitchen~'):
        "Un recipiente vuoto, senza niente dentro. C'è chi lo usa per la tavola e chi ci mette una pianta per ornamento: ognuno a modo suo. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116789
    (116789, 'Woven baskets made of grass vines. It has some holding power, but its coarse texture makes it impossible to use for activities such as fetching water. \\n# ~Supporting Roles in Kitchen~'):
        "Un cesto intrecciato con tralci di piante. Qualcosa la tiene, ma ha le maglie larghe, quindi per cose come attingere acqua non si può usare. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116851
    (116851, "Empty bottles of various sizes. They are somewhat too small to hold water, but enough to catch a child's eye. \\n#~Cheap Gifts for Your Kids~"):
        "Bottiglie vuote di ogni misura. Per tenere l'acqua sono un po' troppo piccole, ma per attirare l'occhio di un bambino bastano e avanzano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :116913
    (116913, 'Rock lumps containing a small amount of minerals. It has no monetary value due to its very low content, but it is said to have certain uses, such as being used in cooking and bathing when heated red-hot. \\n#~Thousands of pieces of Junk I love~'):
        "Un pezzo di roccia con dentro un poco di minerale. Ce n'è così poco che di valore in denaro non ne ha, ma pare che a scaldarlo fino al rosso qualche uso lo trovi, in cucina o al bagno. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116915
    (116915, '\\"This ore piece is a real piece of trash.\\" \\n#~some Bearded Guy~'):
        "\\\"Questo pezzo di minerale è proprio un pezzo di spazzatura.\\\" \\n#~un tizio con la barba~",

    # ---------------------------------------------------------- :123419
    (123419, 'A basket with nothing in it. Most of them are disposable. \\n# ~Supporting Roles in Kitchen~'):
        "Un cesto senza niente dentro. Si usa soprattutto da contenitore quando si mangia all'aperto, e quasi tutti sono usa e getta. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :127669
    (127669, 'Weathered human bones. There are many opportunities to use the bones for spells, refining water medicine, and other purposes, however, there is an oversupply, so the value of the bones is a mere trifling sum. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa umane sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :127731
    (127731, 'Weathered bones. There are many opportunities to use the bones for spells, refining water medicine, and other purposes, however, there is an oversupply, so the value of the bones is a mere trifling sum. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa di qualcosa, sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :127733
    (127733, '\\"Woof! Woof! ..scut!\\" \\n#~Poppy the Puppy~'):
        "\\\"Uuuh, bau bau! Bau! ...mugolio.\\\" \\n#~Parole di <Poppy> il cagnolino~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :127793
    (127793, 'A sword broken in two from the middle. It has been exposed to the wind and rain and has spilled so much that it is no longer of any value, nevertheless, when given to children, they will try their best to imitate warriors, which is amusing. \\n#~Cheap Gifts for Your Kids~'):
        "Una spada spezzata in due a metà. Sbattuta da vento e pioggia, con la lama tutta sbeccata, non vale più un briciolo; eppure, a darla a un bambino, si mette a fare il guerriero con tutto se stesso, ed è divertente. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :127855
    (127855, 'Cloth that catches the wind and flutters in the wind. It is one of the most popular products among tourists as a memento of their trip because of the variety of colors and patterns, and each town has its own unique variant. \\n#~Cheap Gifts for Your Kids~'):
        "Un telo che prende il vento e sventola. I colori e i disegni sono tanti e ogni città ha i suoi, così è uno degli articoli che piacciono ai turisti come ricordo del viaggio. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :127917
    (127917, 'A simple light with an iron cage attached to the end of a pillar to hold a flame. The rugged construction gives a somewhat wild impression. In recent years, some restaurants have installed these lighting fixtures in their restaurants to achieve this effect. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una lampada semplice: in cima a un palo, una gabbia di ferro dove si tiene la fiamma. La fattura rozza dà un'aria un po' selvatica. Da qualche anno, pare, certe trattorie la mettono nel locale proprio per quell'effetto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :127979
    (127979, 'A tub with dirty clothes stuck in it. It is a wonder that anyone would want such a thing, but it is said to be irresistible to a certain type of cleaning enthusiast. \\n#~Thousands of pieces of Junk I love~'):
        "Una tinozza con dentro ficcati dei vestiti sporchi. C'è da stupirsi che qualcuno voglia una cosa simile, eppure pare che per certi patiti delle pulizie sia irresistibile. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :128041
    (128041, 'A jar that is broken and can no longer be used. Some artists see some potential in them and buy them half-heartedly, even though they have no value at all. \\n#~Thousands of pieces of Junk I love~'):
        "Un vaso rotto che non si può più usare. Non vale proprio niente, ma pare che qualche artista ci veda una possibilità e lo compri quasi per sfida. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :128103
    (128103, 'Withered grass curled up in a ball. It is very hard and cannot be used as a grass substitute, but when given to children, they play with it by kicking it around with all their hearts. \\n#~Cheap Gifts for Your Kids~'):
        "Erba secca appallottolata tutta insieme. È durissima e come foraggio non va, ma dandola a un bambino, dicono, si mette a prenderla a calci senza fermarsi mai. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128235
    (128235, 'Pieces of crushed wood. Completely useless, but it would at least be interesting to a child. \\n#~Cheap Gifts for Your Kids~'):
        "Schegge di legno spaccato. Non servono proprio a niente, ma per incuriosire un bambino bastano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

# 26 voci, 0 ambigue
}
