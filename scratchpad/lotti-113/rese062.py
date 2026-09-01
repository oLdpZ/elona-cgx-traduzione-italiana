import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :68450
    (68450, 'Mysterious cherry tree blooms and then falls forever in the world of the dead. The petals that fall to the ground disappear like a phantom. This phenomenon of the cycle of flowers is more maddening than transient. \\n# ~Special Edition: Pursuing Mythical Plants~'):
        "Un ciliegio misterioso che nel mondo dei morti fiorisce e sfiorisce, fiorisce e sfiorisce, per sempre. I petali che toccano terra svaniscono piano, come un'illusione. In quel fiorire fuori stagione si va oltre la caducità: quello che si sente è follia. \\n# ~Speciale: sulle Tracce delle Piante Leggendarie~",

    # ---------------------------------------------------------- :90894
    (90894, 'A fir tree with numerous decorations. The bright ornaments attached to the tree brightly illuminate its surroundings as if it were glowing with its own power. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un abete a cui hanno attaccato addobbi a non finire. Gli ornamenti sgargianti illuminano tutt'intorno, come se l'albero splendesse di luce propria. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :91522
    (91522, 'Evergreen tree that does not produce any fruit. It is said that in the cold season, festivals are held in Noyel to celebrate the Saint by decorating these trees with various ornaments. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un sempreverde che non lascia cadere frutti. Pare che nella stagione fredda, a Noyel, questi alberi li carichino di addobbi d'ogni sorta e si faccia una festa per un certo santo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :91584
    (91584, 'Trees with all their leaves fallen off. They look very frigid, but this is their way of surviving the winter. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero a cui sono cadute tutte le foglie. Sembra infreddolito, ma è il suo modo di passare l'inverno. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95484
    (95484, 'Deciduous tree that does not produce fruit. It is very hard and is primarily used as wood to make various types of furniture. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che perde le foglie e non lascia cadere frutti. È durissimo, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95546
    (95546, 'Trees of tropical origin. It is said that its fruit is hard and looks like a huge cannonball, but these trees do not seem to bear fruit in North Tyris. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che viene dai paesi caldi. Dicono che il suo frutto sia duro e grosso come una palla di cannone, ma a Tyris del Nord questi alberi pare non ne portino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95608
    (95608, 'Deciduous trees that does not produce any fruit. It has very high quality and is mainly used as wood to make various types of furniture. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che perde le foglie e non lascia cadere frutti. È di ottima qualità, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95670
    (95670, 'Completely dead old tree. It is highly flammable, so do not play with fire in the vicinity. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero vecchio, seccato del tutto. Prende fuoco con niente: meglio non giocare con le fiamme lì vicino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95672
    (95672, '\\"It makes you think a lot. Of course, this is just a rotting tree, but with a different perspective, it could be us or it could be a forest. I wonder who this projector will capture as time goes by.\\" \\n# ~words of <Barius> the blue haired~'):
        "\\\"Fa pensare a molte cose. Questo di sicuro è solo un legno marcito, ma basta cambiare sguardo e diventa noi, o quel bosco. Col tempo che passa, chissà quale delle due cose finirà per riprendere, questo proiettore.\\\" \\n# ~Parole di <Barius> dai capelli blu~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :95734
    (95734, "This is a tree that drops fruit when you bash it. Be careful not to get carried away and hit yourself too many times, because you won't be able to get unlimited fruits this way. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che, a dargli una spallata, lascia cadere i frutti. Ma se ci si prende gusto e si insiste, per un po' di frutti non se ne avranno più: occhio. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95796
    (95796, "A tree that hasn't been producing any fruit even after years of waiting. Forget about it and look for a tree that has borne fruit. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che, per quanto lo si aspetti, non ha nessuna intenzione di dare frutti. Meglio rassegnarsi e cercarne uno che i frutti li abbia. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95858
    (95858, 'Evergreen tree that does not produce any fruit. It is said that in the cold season, festivals are held in Noyel to celebrate the Saint by decorating these trees with various ornaments. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un sempreverde che non lascia cadere frutti. Succede spesso di credere che qualcuno stia intralciando i propri incantesimi e scoprire poi che era il polline di questo albero. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95920
    (95920, "A deciduous tree that does not produce fruit. In recent years, it has been discovered that as it grows, it releases toxins from its roots and kills the surrounding trees. The Mages' Guild is currently researching the possibility of using it as a potion. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che perde le foglie e non lascia cadere frutti. Di recente si è scoperto che, crescendo, dalle radici emette tossine che fanno seccare gli alberi intorno, e la Gilda dei Maghi sta studiando se se ne possa ricavare una pozione. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

# 12 voci, 0 ambigue
}
