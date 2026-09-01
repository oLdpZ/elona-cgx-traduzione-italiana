import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :65947
    (65947, 'Bullets with the same caliber but with a greatly increased amount of gunpowder. It can be used in handguns with high power, but the recoil is significant. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un proiettile che, a parità di calibro, porta molta più polvere da sparo. Anche da una pistola tira fuori una gran potenza, ma il contraccolpo è forte. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :96634
    (96634, 'High-energy materials are processed into bullets using special technology. A special firearm is required to use them. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un corpo ad alta energia lavorato in proiettile da una tecnica speciale. Per adoperarlo serve un'arma da fuoco apposita. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :98725
    (98725, 'A thin rod-shaped arrowhead with a square arrowhead used in mechanical bows. Although heavy, it is the only one that can be loaded into a mechanical bow. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un dardo sottile, a forma d'asta, con la punta quadrata, che si adopera nelle balestre. Pesa, ma è l'unica cosa che in una balestra si possa caricare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :126986
    (126986, 'Small spheres machined to be fired from a firearm. Without it, a firearm would be nothing but a mere tube, no matter how prestigious the gun may be. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una piccola sfera lavorata per essere sparata da un'arma da fuoco. Senza di questa, per quanto famosa sia un'arma, non è che un tubo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :127062
    (127062, 'A bundle of arrows for use with a bow. Because they are bundled, some materials are very heavy and must be carried with care. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un fascio di frecce da adoperare con l'arco. Essendo in fascio, a seconda del materiale pesano moltissimo, e a portarsele dietro ci vuole attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 5 voci, 0 ambigue
}
