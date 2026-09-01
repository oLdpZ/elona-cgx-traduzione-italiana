# -*- coding: utf-8 -*-
"""120a - Lotto 053 di `db_item.hsp`: LE ARMI A DISTANZA, prima meta'.

`FILTER_RANGE`, righe da `:43631` a `:88670`: **50 righe** — 46 dell'indice 0,
1 dell'indice 1, 3 dell'indice 2 — su 46 oggetti. La categoria e' la piu'
grossa che restasse (**60 su 60 da fare**) e con questo lotto scende a **10**:
la chiude il 054.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 053`: **+50** per 50 rese,
**nessuna gemella**: le 50 firme coprono 50 righe del sorgente e basta.
ⓘ `_gia-reso.py 053`: 0 su 50. `_code.py 053`: 0 righe senza resa in tabella.

⚠️ La zona non e' l'intera categoria per scelta: `0 200000` dava **60** righe,
sopra il tetto di 55 che la 115a dichiara sano. `0 90000` ne da' 50, e le 10
che restano stanno fra `:90000` e `:127280`.

### ⭐⭐⭐ LA SERIE DELLE TRE ARMI CHE NESSUN UOMO SOLLEVA

E' la cosa che vale oltre questo lotto, ed e' la lezione della 119a — cercare
per **struttura**, sull'originale — applicata **in avanti** invece che a
posteriori.

Tre righe chiudono con la stessa formula, parola per parola:

    人では扱えない程の重さだが、使いこなす者が現れた時
    この武器は使用者に ◯◯ を授けるだろう。それと少しばかりの気まぐれを。

    :75515  la moneta di pietra     魅力          -> carisma
    :77075  la balestra gigantesca  飛びぬけた器用さ -> destrezza fuori dal comune
    :77145  il cannone a gravita'   超感覚         -> percezione fuori dall'umano

⚠️⚠️ **Le tre parole sono TRE ATTRIBUTI DEL GIOCO**, non tre aggettivi: sono
CHR, DEX e PER, e il giocatore le legge nella propria scheda. Le rese vengono
dal dizionario e non dall'inglese — `_cerca.py` da' 「魅力の成長」 -> «Cresce
carisma» e 「器用の成長」 -> «Cresce destrezza». L'inglese scrive «a tremendous
charm»: chi rendesse da li' scriverebbe «fascino» su una statistica che a
schermo si chiama **carisma**, e il legame fra la descrizione e cio' che l'arma
fa davvero si spezzerebbe.

⭐ E la formula si ripete **identica** nelle tre rese, di proposito. La
tentazione di variare («dona», «concede», «regala») cancellerebbe la serie:
qui la ripetizione e' il testo, ed e' come il giocatore riconosce che la terza
arma e' parente delle prime due. Stessa forma della scala delle navi della
119a, al rovescio: la' l'inglese aveva appiattito quattro gradini in uno, qui
ci sono tre righe che devono restare **uguali** tranne una parola.

⚠️ Nessuna rete poteva vederle: firme diverse, tre oggetti di tre tipi
(moneta, balestra, cannone), e ognuna presa da sola e' a posto. Il dossier le
mostra a distanza di dodici voci l'una dall'altra.

### ⭐⭐ IL DOPPIO SENSO DELLA FOGLIA, CHE L'ITALIANO TIENE PER INTERO

`:43632`, le parole della volpe a nove code:「おぬしにハッパをかけてやろうぞ…
ドカーン！」. ハッパ e' insieme:

  - 葉っぱ, **la foglia** — che e' l'oggetto;
  - 発破, **la carica esplosiva** — che e' il nome dell'oggetto, 金毛発破;
  - e ハッパをかける, la locuzione, vuol dire **«dare la carica, incitare»**.

Tre sensi in una parola sola, e l'italiano ne ha una che ne tiene due: «ti do
io **la carica**» e' insieme l'incitamento e l'esplosivo, e il «BUM!» che segue
fa scattare il secondo. L'inglese («Lemme give you a little nudge...boom!»)
tiene solo l'incitamento.

### ⚠️⚠️ DUE RIGHE DOVE L'INGLESE HA RISCRITTO, E LA CODA LO DENUNCIA

  - `:52650`, il gambero fritto esplosivo. Il giapponese e' un **commesso
    confuso** che minaccia 「エビフライ５本くらいぶつけんぞ」, *guarda che te ne
    tiro addosso cinque*. L'inglese ci mette un **bandito eccentrico** con un
    gioco di parole tutto suo su shrimp/shrimping. ⭐ A dire quale delle due e'
    la fonte non e' stato il giudizio: e' `_code.py`, che assegna la coda
    passando dal **giapponese** e scrive «Parole di un Commesso Confuso».
    Rendere dall'inglese avrebbe messo la battuta del bandito sotto il titolo
    del commesso, **nello stesso pannello**;
  - `:52648`, la voce sopra, stesso oggetto. Il giapponese chiude con
    「悪魔の兵器」の別称でも知られている — *lo chiamano anche l'arma del
    diavolo*, che e' un fatto sull'oggetto. L'inglese lo butta e ci mette
    «shrimply devilish», un bisticcio. La resa tiene il fatto.

ⓘ Le due righe stanno **a due voci di distanza** nel dossier, ed e' lo stesso
oggetto: il pannello le disegna una sotto l'altra.

### ⓘ Tre termini presi dal dizionario e non dall'inglese

  - 光子銃 (`:65063`) e' **«pistola laser»**, non «cannone a fotoni»:
    `_cerca.py` da' 光子銃 | laser gun | pistola laser, ed e' il nome che il
    giocatore vede sull'oggetto. ⚠️ Il dizionario porta anche «cannone a
    fotoni» su un **altro** oggetto (la bazooka), e quella e' la resa di
    大口径化された光子銃: le due non si confondono;
  - 詠唱 (`:85997`) e' **«incantesimi»**, la voce della scheda
    (詠唱スキル上昇 -> «bonus in Incantesimi»), non «canto» ne' «recitazione»;
  - 冥界 (`:53561`) e' **«Oltretomba»** con la maiuscola, come nelle sei rese
    di `text.hsp` che il giocatore legge in combattimento.

### ⓘ 妖気 non e' nel dizionario, e non lo diventa qui

`:43631` dice 特殊な妖気が込められており — l'aura sinistra che emana uno
spirito. `_cerca.py` non la trova da nessuna parte, e l'inglese la lascia in
giapponese («special Yokai energy»). La resa la **descrive** («un'aura sinistra
fuori dal comune») invece di coniare un termine: coniarlo qui vorrebbe dire
decidere per tutte le volte che tornera', e questa riga non e' il posto.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-053.jsonl'
RIGHE = {
    43631, 43632, 43705, 52648, 52650, 53348, 53489, 53561, 53631, 53701,
    54667, 54743, 54819, 57384, 61443, 61513, 64413, 65063, 67258, 67390,
    68182, 68326, 71579, 72281, 72283, 72351, 72690, 72760, 73222, 74235,
    74503, 75515, 76389, 76458, 77075, 77145, 77424, 77843, 77913, 78398,
    80356, 82547, 83015, 83017, 83146, 83275, 83342, 85997, 86067, 88670,
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
