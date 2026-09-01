import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :51640
    (51640, 'It was developed by a secret organization that once planned to conquer the world. It was a high-performance infiltration item that could be transformed at will into the uniforms of any organization in the world at that time. Currently, there are only a few of these items that have been excavated and restored by craftsmen. Due to the deterioration of the nanomachine control device, the number of forms that can be changed is very limited. \\n# ~Irva Fantasy Encyclopedia~'):
        "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È un oggetto d'infiltrazione ad alte prestazioni, e si trasforma a piacere nell'uniforme di qualunque organizzazione ci fosse allora al mondo. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. Col decadere del regolatore a nanomacchine, le forme che riesce a prendere si sono fatte pochissime. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51707
    (51707, 'Work of a magic item inventor. He realized the potential of bamboo when he saw a knight using bamboo armor. After designing it from scratch, splitting fine bamboo, coating it with high-grade paints, and reinforcing it repeatedly with magic, it became a first-class work of art that transcended armor. When he later tried to present it to the knight who gave him the idea, he was politely turned down with a complicated smile on his face for some reason. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'opera di un inventore di oggetti magici. Pare che, vedendo un cavaliere che maneggiava bene un'armatura di bambù, si sia accorto di quel che il bambù poteva dare. Progettata da zero, ricavata spaccando bambù di prima qualità, rivestita di vernice pregiata e rinforzata con la magia più e più volte, è diventata un'opera d'arte di primo rango, ben oltre un'armatura. Più tardi la volle regalare al cavaliere che gli aveva dato l'idea, e si dice che quello, con un sorriso difficile da spiegare, l'abbia rifiutata con garbo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :56670
    (56670, 'Insurance in case of a golem rampage. With a single signal from the master, the belt can be tightened to restrain the target. It also has a function to release excess magic power. Since it was the only gift from the master, it is cherished like a treasure and has almost no dirt on it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una garanzia per quando il golem va fuori controllo. A un solo cenno del padrone le cinghie si stringono e tengono fermo chi le porta. E c'è anche di che sfogare il potere magico in eccesso. Siccome era l'unico regalo che il padrone le avesse fatto, è tenuta da conto come un tesoro, e di fango non ne ha quasi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65809
    (65809, 'Great armor passed down through the Mayroon royal family. It is one of the items once presented by a master craftsman. Despite its thorough protection against cold, it can be worn even in hot climates by opening some parts. Imitations made by the common folk were useful as winter protection a long time ago, but in recent years, the rugged design has fallen into disrepute as unfashionable and has fallen into disuse.\\n# ~Irva Fantasy Encyclopedia~'):
        "Una grande corazza che si tramanda nella casa reale di Mayroon, una di quelle che a suo tempo donò un maestro artigiano. Benché sia pensata da cima a fondo contro il freddo, aprendone qualche parte la si può portare benissimo anche nei paesi caldi. Le imitazioni che la gente comune costruiva a occhio erano assai apprezzate come riparo dal freddo fino a una generazione fa; di questi tempi però la linea rozza non piace più, la dicono fuori moda, e sta sparendo.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :70463
    (70463, 'As a result of being stingy with materials, the barrier coating treatment failed. The surface has deteriorated to the point that it crumbles to pieces when lightly scratched. The color fading is also caused by the surface peeling. \\n# ~Irva Fantasy Encyclopedia~'):
        "A furia di risparmiare sui materiali, il rivestimento a barriera è venuto male. Si è degradato al punto che basta un graffio leggero perché la superficie si sbricioli. Anche il colore se n'è andato, e la causa è la stessa: la superficie che si sfoglia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :70530
    (70530, 'The barrier coating process gives this suit unparalleled lightness and defensive performance. Due to manufacturing cost issues, it was not officially adopted, and even the prototype was stored in a warehouse in an unfinished state. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una tuta che, grazie al rivestimento a barriera, mette insieme una leggerezza e una difesa che con quelle di prima non si possono nemmeno paragonare. Per via di quanto costava produrla non fu mai adottata davvero, e perfino il prototipo restò in magazzino a metà. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75983
    (75983, 'Restraints worn by the God of Machine to suppress his power. It looks cool when taken off. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il vincolo che il dio delle macchine si porta addosso per tenere a freno la propria forza. A toglierselo, succedono cose grosse. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77561
    (77561, 'Originally, the suit was to cover the entire body from the neck down, but development was halted midway due to higher-than-expected costs, and only the torso portion was made. Therefore, at first glance, it appears to be nothing more than a swimsuit. The surface of the suit is coated with a barrier coating to provide a certain level of protection. \\n# ~Irva Fantasy Encyclopedia~'):
        "In origine doveva essere una tuta che copriva tutto dal collo in giù, ma i costi sono cresciuti più del previsto, lo sviluppo si è fermato a metà strada e ne è stata fatta solo la parte del busto. Per questo a prima vista non sembra altro che un costume da bagno. La superficie ha il rivestimento a barriera, e una sua difesa ce l'ha. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :101379
    (101379, 'This armor is reinforced by embedding numerous pieces of material into the clothing. Some of the people of Yerles people are said to be eccentric enough to wear these clothes on a daily basis. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura rinforzata infilando molti pezzetti di materiale dentro il vestito. Pare che fra la gente di Yerles ci sia qualche tipo strano che lo porta tutti i giorni. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101444
    (101444, 'Armor made by attaching a plate-like material to the torso. Since the material is used as it is, the type of material used is directly related to its performance, which in turn is directly related to its weight, so be careful when selecting the material. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta legando al busto del materiale a forma di piastra. Siccome il materiale si usa così com'è, la qualità che si sceglie va dritta nelle prestazioni; ma allora ci va dritto anche il peso, e nello scegliere conviene stare bene attenti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101509
    (101509, 'Armor that has been reinforced by embedding pieces of material into the clothing. At first glance, it looks like ordinary clothing, so it is often worn by fashionable adventurers. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura rinforzata infilando pezzetti di materiale dentro il vestito. Siccome a prima vista sembra un vestito qualunque, capita spesso che se lo mettano gli avventurieri eleganti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101574
    (101574, 'Armor with metal attached only to specific parts of it. It is lightweight, allowing for quick and flexible movement, but it is not as strong as standard armor. It is up to the adventurer to choose between this and standard thick armor.\\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza che ha il metallo attaccato solo in certi punti. Essendo leggera lascia muoversi svelti e sciolti, ma ci si perde in robustezza. Se prendere questa o la corazza a bande, si dirà, è gusto dell'avventuriero.\\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101639
    (101639, 'A vestment woven to be worn by those of higher rank. They are slightly heavier, but still lighter than armor. They are more solid than vestments as a result of various embroideries and special weaving techniques. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una veste tessuta perché la porti chi sta più in alto. È un'armatura che pesa un po' di più, ma sempre meno di una corazza. A furia di ricami d'ogni sorta e di tessiture speciali, è venuta più solida di una veste comune. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101704
    (101704, 'This armor is made of small scale-like pieces of material joined together with strings. Its structure makes it both flexible and strong. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza fatta legando con dei lacci dei pezzetti di materiale piccoli come squame. Per come è costruita è insieme flessibile e solida. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101769
    (101769, 'Armor that combines special materials to provide stronger protection. It has the convenience of being able to be worn over clothing like a vest. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza che, incrociando materiali speciali, ha ottenuto una protezione più solida. Ha il comodo di potersi infilare sopra i vestiti come un gilè. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101834
    (101834, 'This armor is made of fabric with many rings sewn onto it. The rings on the surface of the armor are said to have the property of repelling sword blows. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza fatta cucendo un gran numero di anelli su una corazza di stoffa. Si dice che i molti anelli in superficie abbiano la proprietà di deviare il colpo di una spada. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101899
    (101899, 'Heavy-looking armor consisting of chainmail overlaid with armor. It has great defensive power, but you should be prepared to pay a heavy price for it. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza che sovrappone le piastre alla cotta di maglia, e a guardarla pesa. La difesa che dà è enorme, ma in cambio conviene mettere in conto un peso considerevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101964
    (101964, 'This armor is made of very thick layers. Because of its thick layers, it is impervious to most attacks, but at the cost of maneuverability. It is up to the adventurer to choose between this and lighter armor. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una corazza fatta spessissima. Con quegli strati spessi un attacco normale non la scalfisce, ma in cambio ci si perde in prontezza. Se prendere questa o la corazza leggera, si dirà, è gusto dell'avventuriero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130714
    (130714, "Protective gear made of a single piece of woven cloth, worn mainly by monks and priests. Although not suitable for protection, it doesn't interfere with the wearer's chanting and allows the wearer to act with ease. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'armatura fatta intrecciando il materiale in un unico pezzo di stoffa, e la portano soprattutto i monaci. Per come è fatta a difendere il corpo non serve, ma non intralcia gli incantesimi di chi la indossa e lascia muoversi leggeri. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130779
    (130779, 'Armor developed to match the evolution of weapons. Although it is heavy, it serves its purpose of preventing fatal injuries to vital organs. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura messa a punto via via che le armi si evolvevano. Il suo peso ce l'ha, ma il compito di non far arrivare un colpo mortale ai punti vitali lo assolve bene. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 20 voci, 0 ambigue
}
