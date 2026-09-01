import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :59062
    (59062, 'Exquisite weapons said to have been created by a goddess from another world. It is a sword of light and protection. These golden wings are said to transcend the world, descend from the sky, and repel darkness. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno zekki che dicono creato da una dea di un altro mondo. È la spada dello splendore e della custodia. Ali d'oro che, dicono, scendono dal cielo attraversando i mondi e spazzano via le tenebre. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63652
    (63652, 'Originally a prosthetic hand designed for combat, it has been developed into an easily replaceable piece of equipment. Electrical signals are read from the clothing without any neural connection, so depending on the situation, it may not work as desired. The manipulators are made to be sturdy, and by changing the gear ratio, powerful attacks can be unleashed. \\n# ~Irva Fantasy Encyclopedia~'):
        "Nasceva come protesi da combattimento, e da lì è stato sviluppato in un equipaggiamento che si cambia con facilità. Siccome legge i segnali elettrici da sopra i vestiti, senza collegarsi ai nervi, a seconda dei casi può non muoversi come si vorrebbe. I manipolatori sono costruiti robusti, e cambiando il rapporto degli ingranaggi si arriva a sferrare colpi violentissimi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76587
    (76587, 'Flight and propulsion unit developed by the Yerles military based on the wings of a flaming dragon. It is sturdy and can be used for defense. It was developed as personal equipment for soldiers, but lost in a competition to a leg-mounted flying unit and was not adopted. However, its flight capability was so strong that it was later used as a component in air combat weapons. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'unità di volo e propulsione che l'esercito di Yerles ha sviluppato partendo dalle ali di un drago di fuoco. È robusta, e a difendersi non è che non serva. La svilupparono come equipaggiamento personale del soldato, ma in gara perse contro un'unità di volo da montare sulle gambe e non fu adottata. La capacità di volo però era solida, e più tardi l'hanno riutilizzata come pezzo per le armi da combattimento aereo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77354
    (77354, 'A cloak worn by heroes in the past. Because it is tattered and shabby, it looks bad when worn by someone who seems to be less fortunate. A person who is austere may be able to wear it, though. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il mantello che portava un eroe di un tempo. È tutto strappato e sformato, e addosso a chi ha già l'aria sfortunata sta bene nel senso peggiore. Uno con un certo stile asciutto, magari, riuscirebbe a portarlo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :93692
    (93692, 'This cloak is designed to protect against the abominable winds that arise from the Vindale Forest. It is designed to prevent etherwind-induced mutation, so it will not be able to withstand everyday mutation or rain and wind. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un mantello che, dicono, para il vento maledetto che si leva dalla Foresta Eretica. Serve unicamente a fermare le mutazioni portate da quel vento, e contro le mutazioni di tutti i giorni, o contro la pioggia e il vento, non riparerà. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :94022
    (94022, 'Ornaments that resemble the wings of a bat. It can prevent attacks on the back, but it is made only to decorate the appearance of the wearer. It allows floating in the air, albeit only slightly. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto da indossare, fatto a somiglianza delle ali di un pipistrello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :96124
    (96124, 'Ornaments that resemble the wings of a bird. It can prevent attacks on the back, but it is made only to decorate the appearance of the wearer. It allows floating in the air, albeit only slightly. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto da indossare, fatto a somiglianza delle ali di un uccello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100197
    (100197, 'A loose-fitting fabric that wraps around the body. The strength of the cloth itself is increased by weaving in a number of materials. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un tessuto ampio da avvolgersi attorno al corpo. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100262
    (100262, 'A cloak of hard metal attached to the back of a cloth made of interwoven materials. Wearing this cloak can protect the wearer from some attacks. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un mantello con del metallo duro applicato dietro a una stoffa in cui sono intrecciati dei materiali. Addosso, para una parte dei colpi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :126777
    (126777, 'A thin cloth fabric worn over armor. The strength of the cloth itself is increased by weaving in a number of materials. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un tessuto sottile da buttarsi sulle spalle sopra l'armatura. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
