import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43631
    (43631, 'A golden leaf created by a golden-haired Nine Tail polymorphing its body hair. It contains a special Yokai energy and explodes. Legend has it that if one goes to the shrine with a pair of silver leaves, a guardian deity of the forest will appear. \\n#~Irva Fantasy Encyclopedia~'):
        "Una foglia dorata che le Nove Code Dorate hanno creato trasformando il proprio pelo. Dentro ci sta chiusa un'aura sinistra fuori dal comune, ed esplode. Resta una leggenda: chi si presenta al sacello con la foglia d'argento che le fa il paio vede comparire il nume che veglia sul bosco. \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :43632
    (43632, 'Lemme give you a little nudge...boom!\\n# ~words of Kyu-Bi~'):
        "\\\"Adesso ti do io la carica... BUM!\\\"\\n# ~Parole della Volpe a Nove Code dal Manto d'Oro~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :43705
    (43705, 'Mysterious, antiquated paper. It is woven with hidden magic and special fibres, and is robust enough to be used as a throwing weapon. However, it is believed that its true ability lies elsewhere and that only those who have mastered the ancient magic of manipulating paper can unleash it.\\n# ~Irva Fantasy Encyclopedia~'):
        "Una carta antica e misteriosa. Ci sono intessute dentro una magia segreta e fibre speciali, ed è tanto robusta da servire come arma nascosta da lancio. Ma la sua capacità vera è un'altra, e si dice che possa liberarla solo chi ha imparato l'antica magia che governa la carta magica.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52648
    (52648, 'While its ingredients are almost the same as those of ordinary fried shrimp, it is a hazardous substance that causes a phenomenon known as the shell-shocking effect, which can cause an explosion for various reasons. When scattered in the air, it can fly away like a missile or remain behind like a land mine. Children who are interested in the appearance of the product tend to become victims, shrimply devilish. \\n# ~Irva Fantasy Encyclopedia~'):
        "Negli ingredienti non è quasi diverso da un gambero fritto normale, ma provoca il fenomeno detto effetto gambero fritto e, per un motivo o per l'altro, finisce con l'esplodere: è materiale pericoloso. Sparso in aria, o vola via come un missile o resta a terra come una mina. Cadono vittime soprattutto i bambini, incuriositi dall'aspetto, e per questo lo chiamano anche l'arma del diavolo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52650
    (52650, '\\"Haha! a traveling merchant with some prawn money!! I\'m gonna hit the shrimping ground running!\\" \\n# ~words of a eccentric bandit~'):
        "\\\"Guarda che te ne tiro addosso cinque, di gamberi fritti!\\\" \\n# ~Parole di un Commesso Confuso~",

    # ---------------------------------------------------------- :53348
    (53348, 'A flame crossbow made by a shadowy criminal syndicate. It is said to accelerate and shoot out arrows by electromagnetic induction, and ignite them by using the excess heat generated. The structure is imperfect, and the crossed parts sometimes glow. In that case, it is very dangerous, so do not touch it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una balestra di fuoco costruita da un'organizzazione criminale dell'ombra. Pare che acceleri e scagli i dardi per induzione elettromagnetica, e che li accenda col calore in più che la corrente lascia. La struttura non è perfetta, e ogni tanto il punto d'incrocio manda scintille: quando succede è pericolosissima, e non va toccata. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53489
    (53489, "The late work of a now deceased crossbowman. A lightweight ballista with sharpshooter specifications. As a result of the craftsman's full knowledge, it has a range equivalent to that of a sniper rifle. Penetration and handling have also been improved. A coveted item for crossbow collectors. \\n# ~Irva Fantasy Encyclopedia~"):
        "L'opera degli ultimi anni di un artigiano di baliste che non c'è più. Una balista leggera, fatta per il tiro di precisione. L'artigiano ci ha versato dentro tutto il suo sapere, e ne è uscita una gittata pari a quella di un fucile di precisione. Migliorano anche la forza di penetrazione e il maneggio. Un pezzo da far venire l'acquolina a chi colleziona baliste. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53561
    (53561, 'Yomi-To Shards. A piece of a large rock that was blocking the gateway to the underworld. The management is apparently having a hard time replacing it because no matter how many times it is replaced, the deceased keep smashing it up. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una scheggia dello Yomi-To. È il frammento del masso che chiudeva il passaggio verso l'Oltretomba. Per quante volte lo si rimetta i morti lo riducono in pezzi, e pare che chi ne ha la cura sia in grande difficoltà. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53631
    (53631, 'It was lying at the innermost part of the cave covered with poisonous snakes. It seems to be a repeating crossbow based on the concept of a venom attack to the face. The tips of the arrows are coated with splashing venom and fired in rapid succession. When the poison enters the eye, it causes severe pain. \\n# ~Irva Fantasy Encyclopedia~'):
        "Dormiva in fondo a una grotta piena di serpenti velenosi. Pare un arco a ripetizione pensato per colpire il viso col veleno: la punta delle frecce si spalma di un veleno che schizza, e si tira colpo su colpo. Se il veleno entra negli occhi, il dolore è violento. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53701
    (53701, 'This is a short bow that has been handed down from generation to generation among the Quicklings. It is much smaller than an ordinary bow, but it is said that this is just right for the Quicklings. It is covered with magic, so although it is small, it is powerful. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco corto che si tramanda fra i quickling. È molto più piccolo di un arco normale, ma pare che per un quickling questa misura sia quella giusta. Al resto rimedia la magia, e per quanto piccolo la forza ce l'ha. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :54667
    (54667, 'This is a bow designed for close-quarter combat. The arc has a double structure, with the blade on the exterior. The rim is separate on the inside, so arrows can be released even if the exterior bends in a swordfight. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco che tiene conto anche del corpo a corpo improvviso. La parte curva ha una doppia struttura, e di fuori porta una lama con la sua guardia. I flettenti restano dentro, staccati, così anche quando l'esterno si piega nell'incrociare le guardie la freccia parte lo stesso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54743
    (54743, 'A crossbow with an ignition barrel at the tip. When fired, the bolt burns up and flies as a fire arrow. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una balestra con in punta una canna che serve ad accendere. Al momento del tiro il dardo prende fuoco e vola via come freccia infuocata. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54819
    (54819, 'A pair of guns. They are designed to suppress recoil so that they can be handled with one hand. It is not recommended to fire at multiple enemies at the same time. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un paio di pistole. Sono studiate per frenare il rinculo, così da tenerne una per mano. Sparare con tutt'e due insieme su nemici diversi non conviene: non si prende niente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :57384
    (57384, 'Long ago, these beetles were cyborgified for the sole purpose of insect wrestling. Due to being cultivated extensively in the past, these beetles are now only found in the wild, abandoned, and living in secret. When thrown, it can destroy even the most ferocious of beasts, and when synchronized with its wielder, it can produce mysterious beams of light and destruction. Although they do not speak, they have an ego, so you should name them and take good care of them. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno scarabeo che tanto tempo fa fu reso cibernetico solo per farlo lottare con altri insetti. Un tempo se ne allevavano molti; oggi restano soltanto quelli abbandonati, inselvatichiti, che vivono nascosti. A lanciarlo spazza via perfino una belva, e se va all'unisono con chi lo usa scaglia raggi misteriosi e soffi di scoppio. Non parla, ma un io ce l'ha: dagli un nome e vogliagli bene. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :61443
    (61443, 'A bone bow that shoots arrows carrying strong hatred. It is made from the bones of a brutally slaughtered beast that has been abused to the point of hatred for everything in the world. The person being shot will be inconvenienced by the hatred being unleashed on them. Most of bows were made in ancient times, but it is said that even today, some tribes continue to make them in secret. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco d'ossa che scaglia frecce cariche d'odio. Si ricava dalle ossa di una bestia torturata fino a farle odiare ogni cosa al mondo, e poi uccisa in modo atroce. Per chi si prende la freccia, ricevere addosso quell'odio è una bella seccatura. Quasi tutti vengono dall'antichità, ma pare che ancora oggi qualche tribù continui a farne di nascosto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :61513
    (61513, 'Enhanced from Eulderna magic bow, it is a slashing bow that incorporates the mechanical technology of the Yerles army. In addition to being able to engage in hand-to-hand combat, it can also release electric blasts from its stabilizers when you pull its strings. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco a lame che parte da un arco magico di Eulderna e lo rinforza innestandoci la tecnica meccanica di Yerles. Regge anche il corpo a corpo, e a premere il grilletto dagli stabilizzatori parte una scarica elettrica. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :64413
    (64413, 'It is a type of shuriken that is coated with powerful energy. A direct hit is sharp enough to penetrate the armor of a fighter plane. It is not made of ions, but is so called because it is processed by ion beams. The color changes to blue or light blue depending on the energy state. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un tipo di shuriken, avvolto in un'energia potente. Se coglie in pieno taglia tanto da passare da parte a parte anche la corazza di un aereo da combattimento. Di ioni non è fatto affatto: lo chiamano così perché è stato lavorato con un fascio di ioni. Secondo lo stato dell'energia il colore vira all'azzurro o al celeste. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65063
    (65063, "Photon guns found at archaeological sites. It is rather heavy. For some reason, crows are sometimes equipped with this gun, so it is called 'Karasawa' together with its model number. The official name is unknown. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una pistola laser che si ritrova in certe rovine. È pesante più di quanto sembri. Chissà perché, capita che ce l'abbiano addosso i corvi, e per questo, mettendoci insieme la sigla, la chiamano karasuwa. Come si chiami davvero non si sa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :67258
    (67258, 'A type of large crossbow. The smaller ones can be carried somehow by carrying or on the back, but they are essentially stationary turrets. It has a foldable prop at the bottom, but it is not easy to maneuver. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un tipo di balestra di grande taglia. Le più piccole si riesce in qualche modo a portarle in spalla o a tracolla, ma di suo è un pezzo d'artiglieria da postazione fissa. Sotto ha dei sostegni pieghevoli, ma restare comoda da maneggiare non ci riesce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :67390
    (67390, 'In the midst of a chaotic battle, the God of Machine created this weapon on the spur of the moment using spare parts from the sub-cannon of a battleship. It is said that the shot it fires, which was filled with divine power, easily penetrated the hull of the chaos fleet, and its shockwave obliterated all the chaos servants in the fleet. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma che il dio delle macchine mise insieme lì per lì, nel folto della mischia, coi pezzi di ricambio del cannone secondario di una corazzata. Si racconta che il colpo, carico di forza divina, passasse da parte a parte lo scafo della flotta del caos, e che l'onda d'urto riducesse in nebbia i suoi servitori. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68182
    (68182, 'A big chunk of rock. It is not enough to say that it hurts if you are hit by such a thing. Because it is heavy and its distorted shape makes it difficult to throw, it is more powerful than other throwing weapons only at close range. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un grosso blocco di roccia. Prendersene uno addosso non finisce con un semplice male. È pesante, e per giunta ha una forma storta che lo rende difficile da tirare: più ancora delle altre armi da lancio, la sua forza si vede solo da vicino. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :68326
    (68326, 'This crossbow uses a handle, not a winder, to raise the string. It is equipped with a magazine, which increases the loading speed, but the power and accuracy of each shot are much less powerful.It does not have the power to pierce armor, and its power is compensated for by poison applied to the bolt. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una balestra che tende la corda con una manovella invece che con l'argano. Ha un caricatore, quindi si ricarica più in fretta, ma colpo per colpo forza e precisione calano di parecchio. Bucare un'armatura non può: alla forza che le manca supplisce col veleno spalmato sui dardi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :71579
    (71579, 'This two-in-one gun, created from a griffon, has extremely high rapid-firing performance. It features a large, easy-to-hold grip. \\n# ~Irva Fantasy Encyclopedia~'):
        "Due pistole che fanno una cosa sola, nate da un grifone, e che sparano di fila a gran velocità. Le distingue l'impugnatura grande, comoda da tenere. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72281
    (72281, 'A modified version of a rare shotgun found at the ruins, capable of full-auto fire and firing a dedicated small grenade. The discoverer proposed mass production to the military, but it was not considered because it was heavy, bulky, and had excessive firepower. Afterwards, the discoverer dared to modify it to specialize in close quarters combat by trimming the stock and barrel, etc. The destructive and suppressive power is triple-A as the name suggests, but at the cost of missing various important qualities for a gun. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il rifacimento di un raro fucile a pompa trovato fra le rovine, capace di tiro tutto automatico e di lanciare piccole granate apposite. Chi lo trovò propose all'esercito di produrlo in serie, ma pesante, ingombrante e con troppa potenza di fuoco com'era, nessuno lo degnò di uno sguardo. Allora, presala di petto, lo rifece apposta per il combattimento ravvicinato, accorciando calcio e canna. Per forza distruttiva e capacità di tenere a bada il nemico è tripla A come dice il nome, ma in cambio ha perso per strada parecchie cose che a un fucile servono. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72283
    (72283, '\\"What\'s with this renovation plan? This is madness...\\" \\n# ~words of <Garok> the Legendary Smith~'):
        "\\\"Ma che roba è questo piano di rifacimento?! Qui è da matti...\\\" \\n# ~Parole di <Garok> il fabbro leggendario~",

    # ---------------------------------------------------------- :72351
    (72351, 'Card-shaped hidden-weapons. The edge has a sharp blade that can easily cut off a human head. It is made a little heavier to enhance stability when throwing. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma nascosta a forma di carta da gioco. Il bordo è una lama affilata, e un collo umano lo taglia senza fatica. È fatta un po' pesante per restare stabile quando la si lancia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72690
    (72690, "The great bow created by the goddess of winds and once used by her. The light that it emits changes seven times, just like a woman's mind, which is changeable and fickle. She gave it up because she was tired of being too flashy. \\n# ~Irva Fantasy Encyclopedia~"):
        "Il grande arco che la dea del vento creò e portò a lungo con sé. La luce che scaglia cambia sette volte, come un cuore di donna volubile e capriccioso. Se ne è disfatta perché si era stancata di quanto fosse vistoso. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72760
    (72760, 'A type of rapid bowgun. It is a gem designed by fundamentally reviewing the structure of crossbow. It excels in rapid and continuous fire performance. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un tipo di balestra rapida. Un pezzo pregiato, progettato ripensando da capo la struttura della balestra. Eccelle nel tiro veloce e di fila. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73222
    (73222, 'Grenade with the highest-spec firepower. Therefore, extreme care must be taken to avoid being caught in the blast. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una granata potente, che vanta la forza più alta di tutte. Proprio per questo bisogna badare con la massima attenzione a non restare presi nello scoppio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :74235
    (74235, 'A shuriken designed for power at the expense of portability and concealment. Its size makes it no longer a hidden-weapon, but it has the advantage that it can be used for defense. The blade is made of rare metal and can cut through hard objects. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno shuriken che ha cercato la forza sacrificando il poco ingombro e la segretezza. Grande com'è non è più un'arma nascosta, ma ha il pregio di servire anche a parare. La lama è di metallo raro, e taglia anche le cose dure. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :74503
    (74503, 'Dagger that sever nightmares. It is not very sharp, but when thrown, it flies for a long distance. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale che recide gli incubi. Non taglia granché, ma a lanciarlo vola lontano e dritto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75515
    (75515, 'Huge stone money. It was circulated in ancient civilizations and is extremely valuable. It is so heavy that it cannot be handled by a human being, but when a person who knows how to use it appears, this weapon will bestow upon the user a tremendous charm. And a little whimsy.\\n# ~Irva Fantasy Encyclopedia~'):
        "Una moneta di pietra gigantesca. È il pezzo vero che circolava nella civiltà antica, ed è preziosissima. Pesa troppo perché un uomo la maneggi, ma quando comparirà qualcuno capace di usarla, quest'arma gli donerà un carisma smisurato. E insieme un pizzico di capriccio.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76389
    (76389, 'Firearm specialized for sniping. Suitable for shooting from a long distance. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco fatta apposta per il tiro di precisione. Adatta a sparare da lontano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :76458
    (76458, 'Sniper rifle, nicknamed the \\"white death\\". It does not have a sniper\'s scope, making it very difficult for an amateur to hit a target. Also, the barrel is a little short and heavy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un fucile di precisione che porta il soprannome di un tiratore formidabile. Non ha il cannocchiale da tiro, e per un profano prendere il bersaglio è difficilissimo. La canna, poi, è un po' corta e pesante. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77075
    (77075, 'Giant crossbow. It is too heavy for a single person to handle, but when someone finds a way to use it, this weapon will give the user extraordinary dexterity. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una balestra gigantesca. Pesa troppo perché un uomo la maneggi, ma quando comparirà qualcuno capace di usarla, quest'arma gli donerà una destrezza fuori dal comune. E insieme un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77145
    (77145, 'Huge grenade gravity gun. To compensate for the instability of the gravity gun, a grenade launcher is attached. It is too heavy for one person to handle, but when the right person comes along, this weapon will give the user extraordinary perception. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un enorme cannone a gravità con le granate. Per rimediare all'instabilità del cannone a gravità gli hanno montato sopra un lanciagranate. Pesa troppo perché un uomo lo maneggi, ma quando comparirà qualcuno capace di usarlo, quest'arma gli donerà una percezione fuori dall'umano. E insieme un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77424
    (77424, 'Two guns in one. It is said that a pair of twins used to use one gun each. After the older brother was killed in battle, the gun was passed down to the younger brother as a memento. The younger brother spent his life developing the fundamentals of the two-gun combat technique. \\n# ~Irva Fantasy Encyclopedia~'):
        "Due pistole che fanno una cosa sola. Si racconta che un tempo le usassero due gemelli, una per uno. Quando il maggiore cadde in battaglia, la sua pistola passò al minore come ricordo. E si dice che il minore abbia speso la vita intera a mettere a punto le basi dell'arte delle due pistole. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77843
    (77843, 'A coin that was used in an island nation a long, long time ago. According to later documents, some of the guards of the time used to fight by throwing it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una moneta che si usava in un paese d'isole tanto tempo fa da far girare la testa. Stando a testi più recenti, pare che fra le guardie di allora ci fosse chi combatteva lanciandola. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77913
    (77913, 'A type of machine gun in which multiple barrels are rotated and fired to reduce frictional heat during firing and to increase rapid-fire performance. However, the rate of fire is intentionally slightly reduced to suppress the recoil and vibration when firing. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un tipo di mitragliatrice che, facendo ruotare e sparare più canne insieme, è riuscita a smorzare il calore d'attrito del tiro e a spingere più in alto la rapidità di fuoco. Ma per frenare rinculo e vibrazioni la cadenza è stata abbassata un poco di proposito. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :78398
    (78398, 'This short bow combines flexibility and toughness by layering other materials on a foundation of carved biological bones. It is an excellent product that has been processed so that no unnecessary force is applied when drawing it. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco corto che mette insieme flessibilità e tenacia: alla base ci sono ossa d'animale intagliate, e sopra si sovrappongono altri materiali. Un pezzo pregiato, lavorato in modo che nel tenderlo non si sprechi forza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :80356
    (80356, 'An improved version of the pistol that succeeded in mechanizing the work of loading the bullets. Unfortunately, all of the original improvements have been lost over the ages, but this gun is still alive and well. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il perfezionamento di una pistola che era riuscita a meccanizzare il lavoro di caricare i colpi. Nel lunghissimo tempo passato da allora, purtroppo, gli esemplari da cui viene sono andati tutti perduti: solo questa è ancora in forma. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82547
    (82547, 'Thrown weapon in the name of a musical instrument. It is said to have slaughtered many performers in the past. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma da lancio che di strumento musicale ha solo il nome. Quella cosa, che si scambierebbe per un enorme lingotto d'oro, si dice abbia macellato in passato un gran numero di musicisti. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :83015
    (83015, 'A lovely, neat piece of fabric with a cute little ribbon on the front. Often it is in the possession of someone else, but not the owner, and the only one who is unaware of this is Shena herself. \\n# ~Intel of the Informant Wiesem~'):
        "Un pezzo di stoffa graziosa e per bene, con un nastrino sul davanti. Il più delle volte non ce l'ha lei, ma qualcun altro, e pare che l'unica a non essersene accorta sia proprio Shena. \\n# ~Le Notizie Raccolte da <Wiesem> l'informatore~",

    # ---------------------------------------------------------- :83017
    (83017, '\\"I was minding my business in the mining town of Vernis, and BAM, I fell in love! But I didn\'t dare to spoke to her, so instead I asked a thief and stole this from her. And wow, love was much softer than what I had imagined! She and I will always be together.\\" \\n# ~last words, of Luster the noble~'):
        "\\\"Quando andai nella città mineraria, mi innamorai. Ma non ebbi il coraggio di rivolgerle la parola, e allora chiesi a un certo ladro famoso di procurarmi questo. Così io e lei siamo sempre insieme. Ebbene, mi invidiate, vero?\\\" \\n# ~Le Ultime Parole di <Luster> il nobile~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :83146
    (83146, 'Adamantite ore shards. Since it is relatively crude, it cannot be used as an ornament, and can only be used as a projectile weapon. \\n#~Irva Fantasy Encyclopedia~'):
        "Una scheggia di minerale d'adamantio. È di qualità piuttosto scadente, quindi non va bene neanche da ornamento, e usarla così come arma da lancio è il massimo che se ne possa fare. \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :83275
    (83275, 'Small bombs designed for throwing. After landing in a bow, the bomb explodes in a large area, giving it a wide range of effects, but at the same time, it is powerful regardless of friend or foe, so it must be handled with care. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una bomba piccola, fatta per essere lanciata. Cade dopo un arco e scoppia su un'area larga, quindi l'effetto arriva lontano; ma la forza la scarica su amici e nemici allo stesso modo, e va maneggiata con attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :83342
    (83342, 'A bladed throwing weapon used by foreign intelligence organizations. They come in a variety of shapes and sizes, but all are said to be coated with a poison that delays coagulation and causes the target to bleed. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da lancio con la lama, in uso presso i servizi segreti di un paese straniero. Le forme sono le più varie, ma su tutte è spalmato per bene un veleno che ritarda la chiusura delle ferite, e si dice che faccia sanguinare chi viene colpito. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :85997
    (85997, 'Shotgun that reflects light diffusely, said to have been created by a master gunmaker. The special gunpowder smoke that is vigorously emitted from the muzzle is said to have a special power to interfere with chanting. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un fucile a pompa che rimanda la luce in ogni direzione, e che si dice sia opera di un maestro armaiolo. Il fumo di polvere speciale che erompe con forza dalla bocca dell'arma avrebbe il potere singolare di disturbare il lancio degli incantesimi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86067
    (86067, 'Longbow made of an unknown material. It is said to give the wearer the blessing of the wind, and once the bow is drawn, the wearer will see the Goddess of Wind. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco lungo fatto di un materiale sconosciuto. Dà a chi lo porta addosso la protezione del vento, e si dice che, una volta teso l'arco, là si veda la figura della dea del vento. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :88670
    (88670, "A 'weapon' woven by a craftsman exclusively for maidens. You will understand why underwear can be used as a weapon when you have a taste of it. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'\\\"arma\\\" che a quanto si dice un artigiano apposito tesse per le fanciulle. Perché mai la biancheria sia un'arma, lo si capisce da sé una volta che la si è presa in faccia. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 46 voci, 0 ambigue
}
