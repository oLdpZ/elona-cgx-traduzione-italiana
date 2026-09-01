import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42852
    (42852, "The claws of a giant man-eating bear. They are incredibly robust and can even tear through iron sheets. A single strike can blow off an Irva creature's face along with its skull, and the shockwave alone can kill nearby Indian elephants.\\n# ~Irva Fantasy Encyclopedia~"):
        "Gli artigli di un grande orso mangiatore d'uomini. Sono così robusti da lacerare una lastra di ferro: con un colpo solo spazzano via la faccia, ossa comprese, a una creatura dell'Irva di oggi, e l'onda d'urto arriva ad ammazzare perfino l'elefante indiano lì accanto.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :57962
    (57962, 'Chained shackles created by the ancient gods. Intended for the gods, they are made physically sturdy even without supplying divine power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Manette con la catena, forgiate dagli dei antichi. Pensate per l'uso al Sigillo Eterno, sono fatte robuste sul piano fisico e basta, senza l'aiuto di alcun potere divino. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59592
    (59592, 'Gift given to students of the Adventurer Seminar. In the past, it was given only to those who had broken through the comprehensive questions given by Prof. Redsword. At that time, it was called \\"Ganbari Shield\\", and there were other patterns besides the crown. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un oggetto che si dona agli allievi del Seminario d'Avventura. Un tempo lo si dava solo a chi superava la prova del maestro Spada Rossa. Allora si chiamava Scudetto Bravo, e pare che oltre alla corona ci fossero anche altri motivi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59860
    (59860, 'Mysterious mirror that exhales smoke when imbued with divine power. The first Tezcatlipoca had his leg bitten off while killing a certain goddess, and he attached this mirror to him as a prosthetic leg. Its name means \\"Mirror of the Night\\" in the ancient language. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno specchio misterioso che, se lo si carica di potere divino, sputa fumo. Si racconta che il primo Tezcatlipoca, cui una dea aveva staccato una gamba a morsi mentre la uccideva, per un certo tempo se lo sia attaccato addosso al posto della protesi. Il suo nome, in lingua antica, vuol dire \\\"lo specchio della notte\\\". \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :67599
    (67599, 'Claws forged by the secret arts of the ninja. They vibrate in resonance with specific sound waves, enhancing their sharpness. They can also amplify the power of chanted spells. \\n# ~Irva Fantasy Encyclopedia~'):
        "Artigli temprati con le arti segrete dei ninja. Vibrano entrando in risonanza con certe onde sonore, e così tagliano meglio. Pare che sappiano anche amplificare un incantesimo recitato e renderlo più potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68250
    (68250, 'Equipment that imitates the claws of a beast, bird of prey, insect, etc.Its original use is to hook onto a tree or the ground. However, since it can be used as armor to repel attacks or to enhance the power of weapons, it is used exclusively for combat purposes. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un equipaggiamento che imita gli artigli delle bestie, dei rapaci, degli insetti. In origine serviva ad aggrapparsi agli alberi e al terreno; ma siccome fa da armatura per deviare i colpi e insieme da arma per rendere più forte il corpo a corpo, oggi lo si usa soltanto per combattere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :69256
    (69256, 'Claw-shaped weapon that brings misfortune to the target it slices open. It used to bring eternal misfortune to those it touched, but lost most of its power during the battle with the Goddess of Fortune. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma a forma di artiglio, che porta sfortuna a chi squarcia. Un tempo era roba capace di portare sfortuna eterna a chiunque la sfiorasse, ma nella battaglia contro la dea della fortuna ha perso quasi tutta la sua forza. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71233
    (71233, 'Offensive-and-defensive equipment. It incorporates a small propulsion device to increase the penetration power of the attack through acceleration. Since it temporarily accelerates above the speed of sound, it is also heat and shock resistant. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Ha un piccolo propulsore incorporato, e l'accelerazione dà al colpo più forza di perforare. Siccome per un attimo accelera oltre la velocità del suono, regge anche il calore e gli urti. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71302
    (71302, "Offensive-and-defensive equipment. It has the ability to convert the user's mana to form a photon blade. If there is an opportunity, it can be connected directly from a strike to a slash. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un equipaggiamento che unisce attacco e difesa. Sa convertire il mana di chi lo impugna e formarne una lama laser. Se trova un varco, dalla botta passa dritto al fendente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71371
    (71371, 'Offensive-and-defensive equipment. Light and sturdy. It can be struck by slightly loosening its grip and then rotating it. It enables compact and quick combat attacks, smashing targets one after another. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Leggero e saldo. Si può anche allentare un poco la presa e colpire facendolo roteare. Permette attacchi corpo a corpo raccolti e svelti, e sbriciola i bersagli uno dopo l'altro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71439
    (71439, 'Offensive-and-defensive equipment. A repulsive shield generator is attached, which provides high defense despite being a tonfa.\\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Ci è montato sopra un generatore di scudo repulsivo, e così, pur essendo un tonfa, tiene una difesa alta.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71509
    (71509, "Offensive-and-defensive equipment. It allows it's user to sac\\n# ~Irva Fantasy Encyclopedia~"):
        "Un equipaggiamento che unisce attacco e difesa.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71511
    (71511, '\\"Reserved for ACT III.\\" \\n# ~Weird Memo~'):
        "Per la parte terza. \\n# ~Appunto Misterioso~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :73560
    (73560, 'Knight\'s shield that seals a curse. As a result, the \\"knight\'s soul that tries to protect the lord\\" that resides in the shield works to produce a high defensive power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno scudo da cavaliere in cui è stato sigillato il potere di una maledizione. Così agisce soltanto l'\\\"anima del cavaliere che vuole difendere il suo signore\\\" rimasta nello scudo, e ne esce una difesa altissima. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81328
    (81328, 'Part of the Queen Sedona, which sank in the etheric wind. It can be used as a shield, but its defensive capability is not so good. It floats on water, but it can only support one drowning person. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pezzo della <Regina Sedona>, la nave affondata per il vento d'etere. Come scudo si può anche usare, ma la difesa che dà è poca cosa. Galleggia, però al massimo tiene a galla una persona sola che stia annegando. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82410
    (82410, 'A shield with thorns of various sizes on its surface. It is not strong enough to protect itself, but when it is struck with full force, the poor enemy will scream in agony. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo pieno di spine grandi e piccole sulla faccia, che a guardarlo fa già male. Per difendersi non basta del tutto, ma quando lo si sbatte addosso con tutta la forza, il povero nemico si contorcerà dal dolore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :82478
    (82478, 'In ancient times, the lute was said to have sounded wonderful. Today, however, it is simply treated as an excellent shield made of very strong wood that does not show its age, and it will never sound as good as it did back then. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un liuto che nei tempi antichi, si dice, mandava un suono meraviglioso. Oggi però lo si tratta soltanto come un ottimo scudo, ricavato da un legno fortissimo su cui gli anni non si vedono, e un suono come quello d'allora non lo darà più. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :100717
    (100717, 'An extremely bulky shield. Naturally, it is not half as heavy as it should be, and it is said that once it is dropped to the ground, it will require the strength of several people to lift it back up. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo fatto spessissimo. Il peso, va da sé, non è cosa da poco: si dice che una volta caduto a terra ci voglia la forza di più persone per rimetterlo in mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100783
    (100783, 'A large rectangular shield. It is large enough to cover the body and can be used as a simple wall to shield the enemy, but it also has many harmful effects and requires skill to handle. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo grande e rettangolare. È tanto largo da coprire il corpo, e può fare da muro improvvisato per ripararsi dal nemico; ma proprio per questo dà anche parecchi impicci, e si dice che a maneggiarlo ci voglia esperienza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100849
    (100849, 'Shields made from a combination of special materials to provide stronger protection. It has the disadvantage of being somewhat heavy, but it just works. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Ha il difetto di essere un po' pesante, ma renderà molto più di quel poco che pesa in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100915
    (100915, "Protective gear designed to prevent attacks. Unlike armor, it can be held in one's own hands to oppose violence. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'armatura pensata per parare i colpi. A differenza della corazza la si tiene con la propria mano, e così si può fronteggiare la violenza che ti si getta addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100981
    (100981, 'Shield with its center of gravity attached to the center. It is said that the round shape of the shield was designed so that it would not hit the ground and impede walking when going into battle. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo tondo, col baricentro messo al centro. Si dice che quella forma tonda così particolare sia nata perché, andando al fronte, non battesse per terra e non impedisse di camminare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101047
    (101047, 'Shields smaller than normal shields. By attaching it to the arm, it succeeds in reducing the inconvenience of carrying it and its weight, but at the same time, the range in which it can be used for defense is considerably narrowed. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo più piccolo del normale. Legandolo al braccio si è riusciti a togliere di mezzo la scomodità di portarlo e il peso che ne veniva, ma in cambio lo spazio che si riesce a difendere si è fatto parecchio stretto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :127204
    (127204, 'A prestigious shield made for knights. They are elaborately engraved and decorated to suit the user, but they are not merely ceremonial and offer a certain degree of protection. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo di gran pregio, fatto per i cavalieri. Porta cesellature e ornamenti lavorati con cura, scelti su misura di chi lo impugna; ma non è soltanto da cerimonia, e una certa protezione ce l'ha. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 23 voci, 0 ambigue
}
