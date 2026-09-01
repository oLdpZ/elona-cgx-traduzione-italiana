import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :96567
    (96567, 'A super-heavyweight device that ejects a substance at high speed. In addition to the complex mechanism, it has succeeded in reducing weight by processing special materials. However, since both of these technologies are now lost, it would be impossible to mass produce them. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un apparecchio pesantissimo, che scaglia materia portata ad altissima velocità. Oltre al meccanismo complicato, lavorando materiali speciali si è riusciti anche ad alleggerirlo. Ma tutt'e due sono ormai tecniche perdute, e produrlo in serie sarebbe impossibile. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :96710
    (96710, 'Firearms that shoot a massive beam of light by loading a special bullet. Unlike other ranged weapons whose power diminishes as the distance increases, this is an excellent weapon whose power hardly diminishes at all. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco che, caricata con un proiettile speciale, scaglia dal foro di sparo un raggio di luce dotato di massa. A differenza delle altre armi da tiro, che perdono forza a mano a mano che la distanza cresce, questa non cala quasi per niente: un pezzo notevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :97803
    (97803, 'Firearms used to fire projectiles that scatter over a wide area. It is incomparably powerful at close range, but its power decreases at an accelerated rate as you move away from it, so it must be handled with care. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco fatta per sparare proiettili che si sparpagliano su un'area larga. Da vicino ha una forza senza pari, ma allontanandosi quella forza cala sempre più in fretta, e va maneggiata con attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :98801
    (98801, 'Bows are designed for easy firing of arrows. The advantage  is that it can be handled by anyone without the need for bow skill, but on the other hand, it takes a lot of strength and time to prepare for loading, so it has its advantages and disadvantages. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco pensato per scagliare frecce senza fatica. Il pregio è che lo usa chiunque, senza bisogno di pratica; il rovescio, che preparare la carica costa parecchia forza e parecchio tempo. Insomma, ha un pregio e un difetto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115796
    (115796, 'Firearms with a long barrel designed for continuous firing. Although its size and weight make it somewhat maneuverable, it is still much easier to operate than a bow. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco a canna lunga, fatta per sparare di continuo. Per taglia e peso non è arma per tutti, ma anche così, a differenza dell'arco, si può dire che sia molto più facile da manovrare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115872
    (115872, 'Short bow developed for hunting. Requires skill to handle, but once you get the hang of it, it will be a reliable friend to hunters. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco di lunghezza contenuta, messo a punto per la caccia. Usarlo richiede pratica, ma una volta presa la mano può diventare per i cacciatori un amico di cui fidarsi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117185
    (117185, 'A collection of roadside pebbles, hard as iron, used as weapons. They certainly do hurt when thrown, but since they are only pebbles, they are little more than a scare tactic. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un pugno di sassi duri come il ferro, raccolti sul ciglio della strada e messi insieme come arma. A prenderli in faccia fanno male davvero, ma sassi restano: poco più di uno spauracchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117388
    (117388, 'Longbows are said to be filled with the wisdom of the Vindalian folk. It seems to have been devised in several ways to keep the prey from escaping. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco lungo che si dice racchiuda tutto il sapere della gente della foresta. Pare che ci sia dentro più di un accorgimento perché la preda presa di mira non scappi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127138
    (127138, "A heavy, compact firearm. It is designed to be handled by any person, but due to the short barrel, its range won't be very long. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'arma da fuoco piccola, che si sente pesante in mano. È progettata perché chiunque la sappia usare, ma con la canna corta che ha la gittata non sarà granché lunga. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :127280
    (127280, 'A bow longer than the body size, designed to extend the range of a bow. By angling the shot, it can snipe the enemy from a very long range.\\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco che, per allungare la gittata, è cresciuto fino a superare la statura di un uomo. Già così arriva abbastanza lontano, ma dandogli l'angolo giusto si dice che possa colpire il nemico da distanze lunghissime.\\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
