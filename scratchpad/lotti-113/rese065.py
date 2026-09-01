import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56737
    (56737, 'The ring possesses two different elemental powers. It also assists the regenerative capabilities. The red and blue lines intertwine like a spiral. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello in cui abitano due forze diverse. Ha anche il compito di dare una mano alla capacità di rigenerarsi. Nel disegno, una linea rossa e una azzurra si intrecciano come una spirale. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75581
    (75581, 'Ring that seals magic power, created by the God of Elements. It suppresses immense amounts of magical power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello che sigilla il potere magico, nato dal dio degli elementi. Tiene a bada anche un potere magico immenso. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86671
    (86671, 'This ring is filled with magical power that constantly accelerates a person. Since it has no harmful effects of aging, many adventurers seem to love using it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello in cui è racchiuso un potere magico che tiene una persona sempre accelerata. Non ha la controindicazione di far invecchiare, e pare che molti avventurieri se ne servano volentieri. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :93627
    (93627, 'The ring senses the surrounding seasonal weather and is effective in bad weather. In doing so, the ring emits a soft light and creates a force field that maintains tranquility in the surrounding area. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello che sente il clima intorno e fa effetto quando il tempo si guasta. In quel momento, dicono, manda una luce morbida e crea attorno a sé un campo di forza che tiene la calma. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :99162
    (99162, 'Rings of love are given to the spouse at the wedding ceremony. Naturally, the ring belongs to the spouse, and forcibly taking it away from him or her will provoke his or her fury. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello carico d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento l'anello appartiene a lui, e a strapparglielo per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99233
    (99233, 'Rings of ornaments worn on the fingers. There are a variety of types, including simple ones used for ceremonial purposes and ones in which significant magical power is enclosed. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto a forma di cerchio che si infila al dito. Ce n'è di ogni specie: dai più semplici, buoni per le cerimonie, a quelli in cui è sigillato un potere magico grave. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99305
    (99305, 'This ring is more specialized in protecting the finger. Although less valuable as an ornament, this is a better choice when protecting oneself. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello fatto apposta per proteggere meglio il dito. Come ornamento vale poco, ma quando si tratta di difendersi è questo che conviene. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99377
    (99377, 'Rings made by mixing a variety of materials to achieve a higher level of performance. Many of them are more expensive than ordinary rings because of their durability and novelty. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello che punta più in alto mescolando materiali di ogni sorta. Siccome dura molto se ne vedono parecchi nati da tentativi arditi, e pare che costino un po' più dei soliti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :107181
    (107181, "Lovely small ring with a blue-green gemstone. It is said to enhance the owner's nobility through its hidden power. \\n# ~Lumiest Art Catalogue~"):
        "Un anello piccolo e grazioso, che porta una gemma verde-azzurra. Dicono che, con una forza nascosta, alzi l'eleganza di chi lo possiede. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :107390
    (107390, 'Ring said to have been made from the bones of a steel dragon. It is said to be so powerful that the wearer is made to believe he or she has become a steel dragon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello rozzo, che dicono ricavato dalle ossa di un drago d'acciaio. A portarlo si acquista una forza tanto immensa da far credere di essere diventati un drago d'acciaio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :130385
    (130385, 'Beautiful ring with a variety of decorations. It is said that once there was a competition among craftsmen to see how much color they could put onto this small ring. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello reso bellissimo da ornamenti d'ogni sorta. Dicono che un tempo gli artigiani si sfidassero a chi riuscisse a stipare più colore dentro quel piccolo cerchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 11 voci, 0 ambigue
}
