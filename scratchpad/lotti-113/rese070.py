import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :97263
    (97263, 'A piece of paper on which information is clearly described. It contains detailed descriptions of height and weight as well as characteristics, but it is rarely used for collecting such information and is said to be used exclusively for collecting and playing with, helped by its shiny material.  \\n# ~Lumiest Art Catalogue~'):
        "Un foglietto su cui le informazioni sono descritte per filo e per segno: altezza e peso, s'intende, ma anche i tratti particolari, scritti nei minimi dettagli. Eppure per raccogliere informazioni non si usa quasi mai; complice il materiale lucido, pare che serva soltanto da collezione e da gioco.  \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :97325
    (97325, 'The statues are so elaborately crafted that they seem to be living replicas of their victims. The figure is so lifelike that it looks as if it could start moving at any moment. \\n# ~Lumiest Art Catalogue~'):
        "Una statua fatta con tale finezza da sembrare il ritratto vivente della vittima. La figura è così piena di vita che pare stia per muoversi da un momento all'altro. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :108519
    (108519, 'Bone fragments of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Schegge d'osso di una creatura, schizzate via nel frantumare un nemico. Gran valore non ne hanno, ma si usano per le pozioni e per la stregoneria, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108581
    (108581, 'Heart of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Il cuore di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si usa per le pozioni e per la stregoneria, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108643
    (108643, 'Eyes of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "L'occhio di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si lavora in ornamenti e in medicine, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108705
    (108705, 'Collected body fluids of scattered creatures. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Il sangue di una creatura, schizzato via e raccolto. Gran valore non ne ha, ma si lavora in pozioni e simili, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108767
    (108767, 'Skin patches of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Lembi di pelle di una creatura, schizzati via nel frantumare un nemico. Gran valore non ne hanno, ma si lavorano in vestiti e in borse, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

# 7 voci, 0 ambigue
}
