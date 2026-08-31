import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :82945
    (82945, 'Huge, unadorned silver cross-sword. The sword has no decoration except for a mysterious engraving on the blade, and its design, which is solely dedicated to cutting down the enemy, is breathtaking. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada a croce d'argento, enorme e senza ornamenti. A parte un'incisione misteriosa sulla lama non ha decorazione nessuna, e quella fattura, fatta solo per abbattere il nemico e nient'altro, mette perfino una specie di soggezione. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :84582
    (84582, 'A great red axe that looks as if it is painted with blood. The blow from it is said to pierce and shatter anything. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'ascia lunga rossa, come fosse imbrattata di sangue. Dicono che il colpo che ne esce passi e sbricioli qualunque cosa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85642
    (85642, 'Huge, heavy hammer with an imposing appearance. The figure wielding the hammer seems to be a manifestation of the God of Earth. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un martello enorme e pesante, di aspetto maestoso. Chi lo gira sembra il dio della terra che si mostra in carne e ossa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85714
    (85714, 'Dagger carved out of mica, an ancient sign of good fortune. According to one theory, it was accidentally dropped to the mortal world by the Goddess of Fortune when she was cutting up a fish. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale ricavato scavando la mica, che fin dai tempi antichi è segno di fortuna. Secondo una versione, la dea della fortuna lo lasciò cadere per sbaglio sulla terra mentre puliva il pesce. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85785
    (85785, 'A holy spear, without a trace of shadow. Once you strike your enemy, you might have a glimpse of the power of the Goddess of Healing. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lancia sacra senza un'ombra addosso. Basta che tu infilzi il nemico una volta, e ci vedrai un frammento della forza della dea della guarigione. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85857
    (85857, 'Black staff decorated with three types of gemstones. Each gemstone is said to symbolize an element, which dramatically increases the magic power of the wielder. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un bastone nero ornato di tre specie di pietre preziose. Ciascuna pietra è il simbolo di un elemento, e dicono che facciano crescere di colpo la forza magica di chi lo maneggia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85927
    (85927, "There are probably no farmers who doen't know this fairy tale. In the past, when there was no harvest due to continuous drought, this appeared out of nowhere and the surrounding area was covered with greenery eventually. \\n# ~Irva Fantasy Encyclopedia~"):
        "Fra chi lavora la terra non c'è nessuno che non conosca questa favola. Ai tempi in cui la siccità non finiva e il raccolto non veniva, quella comparve da chissà dove, e poi tutt'intorno si coprì di verde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107252
    (107252, 'This amazing spear is said to have been forged in the flames of the netherworld. It is said that as it is forged, the spear gradually absorbs the power of hell, and when wielded, opens the gates of hell. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lancia prodigiosa che, si dice, fu forgiata con le fiamme che l'oltretomba manda. Forgiandola, si è bevuta a poco a poco la forza che l'oltretomba dà; e dicono che, a girarla, apra le porte che l'oltretomba tiene chiuse. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107324
    (107324, 'It is said that only those who have fallen into darkness are qualified to hold this staff. It is said to contain the souls of its past owners, which often come back to haunt them in nightmares when they attack. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un bastone che, dicono, solo chi è caduto nelle tenebre ha il diritto di impugnare. Dentro ci starebbero chiuse le anime di chi lo ha posseduto prima, e quando colpisce spesso quelle piombano addosso al nemico come un incubo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107326
    (107326, '\\"I heard that in the past, the staff was in the hands of a mage who wished to destroy himself. At the time, I laughed at what a foolish person he was, but now I think I understand somewhat how he felt. He must have lost too much.\\" \\n# ~words of <Renton> the suffering wizard~'):
        "\\\"Ho sentito dire che è il bastone che, tanto tempo fa, tenne in mano un mago che voleva la propria rovina. Allora ridevo, e pensavo che uomini sciocchi ci fossero al mondo; adesso invece mi pare quasi di capire come si sentiva. Anche lui avrà perso troppo.\\\" \\n# ~Parole di <Renton> il mago tormentato~",

    # ---------------------------------------------------------- :107460
    (107460, 'A club with an iron ball attached to it that looks like a bloody full moon. The sphere is said to be enchanted to absorb the spirit of the opponent and convert its energy into flames. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un randello con attaccata una palla di ferro che pare una luna piena imbrattata di sangue. Sulla sfera, dicono, sta un incantesimo che assorbe lo spirito del nemico e ne rende la forza in fiamme. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :113386
    (113386, "This is a shortsword used by an intelligence organization that grew up in secrecy in a foreign land, and is processed to fit comfortably in one's hand. The blade is said to be dyed black so that it does not reflect light. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una spada corta che usa un gruppo di spie cresciuto in segreto in un paese straniero: è piuttosto piccola, ma lavorata per stare bene in mano. La lama, dicono, è tinta di nero perché non rifletta la luce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115521
    (115521, 'A spear that can be used in a variety of fighting styles such as slashing, thrusting, and striking all by itself. In ancient times, when people were constantly fighting each other, this weapon was used by various races as well as its usage. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una lancia che da sola permette di combattere in molti modi: taglia, punge e batte. Nei tempi antichi, quando gli uomini non smettevano mai di combattersi, quest'arma la usavano razze diverse, tante quante erano i suoi usi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115589
    (115589, 'An axe with a blade larger than a battle-axe. It even looks like a wide sword attached to a long pole, but because of its weight, it is mainly used for smashing rather than slashing. It can also be used for felling trees. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia con una lama ancora più grande di quella dell'ascia da battaglia. Ormai pare quasi una spada larga infilata in cima a un palo lungo, ma per via del peso pare che si usi più per schiacciare che per tagliare. Serve anche ad abbattere gli alberi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115720
    (115720, 'A huge sword designed to be handled with both hands. Although heavy, it is a sharp weapon whose purpose is not to crush the enemy with its weight, but to cut them down. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada enorme, fatta perché si maneggi a due mani. Pesa, ma non è affatto un'arma che schiaccia il nemico lasciando fare al peso: taglia bene, ed è fatta per recidere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115941
    (115941, 'A stick with a considerable length. It has no blades, so its lethality is low, but because of its lightness, it is often wielded or used as a medium to put magic power into. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone di una certa lunghezza. Non ha lame, quindi uccide poco; ma è leggero, e per questo spesso lo si gira in mano o lo si usa come tramite in cui mettere la forza magica. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116010
    (116010, 'The spear originally invented to catch fish. The three-parted end of the handle makes it easier to hit an opponent, and it is also thought to have the effect of delaying healing due to wounds inflicted in close proximity. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una lancia pensata all'origine per prendere il pesce. La punta del manico si divide in tre, e questo la rende più facile da mandare a segno; e pare che sia stato studiato anche l'effetto di ritardare la guarigione, con le ferite prese così da vicino. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116078
    (116078, "A large hammer, fashioned from a blacksmith's hammer for use in battle. The blow struck from the tip of a large hammer is said to crush any enemy. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un martello grande, ricavato da quello del fabbro e lavorato per il combattimento. Dicono che il colpo, calato da un braccio alzato per bene, schiacci qualunque nemico. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116146
    (116146, 'Axes developed for combat use. The blade is larger and heavier, so it must be handled with both hands. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia sviluppata per il combattimento. Anche la lama è fatta piuttosto grande, e questo ne ha aumentato il peso: alla fine bisogna per forza maneggiarla a due mani. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116215
    (116215, 'A double-edged sword used by the bandit groups that plague the seas. It is made to be easy to handle on the battlefield, with a rather small blade and a broad hilt to defend against swords. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada a doppio taglio che usano le bande di predoni che infestano il mare. Perché stia bene in mano anche in battaglia, ha la lama piuttosto piccola e larga di costa, così da poter parare le spade. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116282
    (116282, "Longswords said to have been favored by exotic fighting groups. It has a unique curve, and each is said to have a unique design and bears the swordsmith's soul. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una spada lunga che, dicono, i gruppi di guerrieri di un paese straniero preferivano a ogni altra. Ha una curva tutta sua, e dicono che in ognuna stiano chiusi una firma tutta sua e l'anima del fabbro che l'ha battuta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116982
    (116982, 'A stick born to assist magic. Despite its everyday look, if you hit with it with all your might, your opponent will probably fall unconscious. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma con la punta acuminata in cima a un manico lungo. Ha una struttura semplice e la può usare chiunque, e il manico lungo permette di combattere a mezza distanza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117051
    (117051, 'A stick born to assist magic. Despite its everyday look, if you hit with it with all your might, your opponent will probably fall unconscious. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone nato per dare una mano alla magia. A vederlo non lo chiameresti un'arma, eppure, se ci batti con tutta la forza, probabilmente il nemico va giù svenuto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117119
    (117119, 'Originally, this weapon was used to cut grass. On the battlefield, this weapon is used to hunt for heads and is considered an object of fear. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arnese che serve, di suo, a tagliare l'erba e simili. Sul campo di battaglia lo si usa per mietere teste, e per questo fa paura. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117460
    (117460, 'Dagger made from an unknown mineral. It is said to be extremely light, and the quick sword flashes from it look as if they are swinging a cord. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale fatto con un minerale sconosciuto. È leggerissimo, e dicono che i lampi rapidi della lama sembrino un nastro che si gira in aria. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :126221
    (126221, 'A long sword that was said to have been quietly stuck in a small hill. How many enemies has the black blade slaughtered? The sword does not speak silently. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada lunga che, dicono, stava piantata in silenzio su una collinetta. Quanti nemici avrà macellato quella lama nera? La spada tace e non risponde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :126918
    (126918, 'A scythe with multiple layers of enhancement magic. It was said to strengthen the magic of the wielder and bring him closer to the ultimate existence, but it has long since been lost to the world. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce su cui sono stati stesi strati e strati di incantesimi di rinforzo. Dicevano che rafforzasse la magia di chi la maneggia e lo avvicinasse all'essere supremo, ma è sparita dal mondo da moltissimo tempo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127349
    (127349, 'It is said that there is nothing in this world that cannot be cut. As rumor has it, it can cut through anything, but it is said to be unable to cut through only gray food, which is rich in elasticity. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un miracolo di lama, di cui si canta che a questo mondo non c'è cosa che non tagli. Come dice la voce, passa qualunque cosa; ma a quel che raccontano, l'unica che non riesce a tagliare è un cibo grigio e pieno di elasticità. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127421
    (127421, "This is a breathtaking sword bearing the name 'Diablos'. It is said that its black blade disrupts not only the spirit of the cutter, but even the flow of time. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una spada che incute timore e porta il nome di \\\"demone\\\". Dicono che la sua lama nera scombini non soltanto la mente di chi viene tagliato, ma perfino lo scorrere del tempo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127423
    (127423, '\\"I have heard about that weapon. I have heard that it is a sword born of a black dragon that harbors evil, and that its cutting blade cuts through time. I don\'t know if this is true or not, but if it is, I would love to see it. It may be a weapon worthy of my power.\\" \\n# ~words of <Loyter> the crimson of Zanan~'):
        "\\\"Di quell'arma ho sentito parlare. Sarebbe una spada nata da un drago nero che porta sventura, e la sua lama taglierebbe perfino il tempo. Non so se sia vero, ma se lo è mi piacerebbe proprio vederla. Potrebbe essere un'arma degna della mia forza.\\\" \\n# ~Parole di <Loyter> l'eroe cremisi di Zanan~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :130977
    (130977, 'A simple weapon designed for striking. It is very simple to make and use, and many adventurers are said to be its favorite users. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma semplice, fatta per picchiare. Il modo di farla e quello di usarla sono tutt'e due semplicissimi, e per questo dicono che anche fra chi va all'avventura ci sia chi non la lascia mai. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131045
    (131045, 'Axe light enough to be handled with one hand. It is more of an everyday tool than a weapon, but its lightness makes it versatile enough to be used like a club. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia fatta leggera perché si maneggi con una mano sola. Nella fattura si sente ancora forte il lato di ogni giorno, spaccare la legna più che combattere; ma è leggera, e per questo è buona a tutto: si può usare anche come un randello. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131114
    (131114, 'Originating from an ancient domain, it is a short and light sword that can be easily handled with one hand. Its simple shape is still in use today. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada corta e leggera, nata presso un clan antico, fatta per maneggiarsi facile anche con una mano sola. La sua forma semplice è arrivata fino a oggi senza cambiare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131182
    (131182, 'A sword with a long blade, widely used for killing. The variety of these swords is said to be still evolving. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada dalla lama lunga, fatta in generale per tagliare. Dicono che le sue varietà, che sono tantissime, continuino a evolversi ancora adesso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 32 voci, 0 ambigue
}
