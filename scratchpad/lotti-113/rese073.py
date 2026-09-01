import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :87574
    (87574, 'Naturally, North Tyris also has toilets. They are even flush toilets. However, only a very eccentric person or a person who has left everything behind would try to satisfy his or her thirst in such a place. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Va da sé che i gabinetti esistono anche a Tyris del Nord, e per giunta con lo sciacquone. Ma chi, solo perché ha sete, si mettesse a saziarla in un posto come questo, o è un tipo assai strano o è uno che ha buttato via tutto. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :90707
    (90707, "There is only one well in the world that is filled with holy water. Do not defile it, and if you throw water pills into it lightly, you will surely regret it. \\n# ~Worlds you've Never Seen~"):
        "Un pozzo pieno d'acqua santa, che dicono esista in un solo posto al mondo. Guardati dal profanarlo: se a cuor leggero ci gettassi dentro una pozione, di sicuro te ne pentiresti. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :119757
    (119757, 'A summer retreat that creates a clean sound and cool space around it. It sounds good, but at the end of the day, the water in North Tyris is circulating, and it is probably not the cleanest water in the world. \\n# ~Supporting Roles on the Streets~'):
        "Un impianto per rinfrescare l'estate, che tutt'intorno crea un suono limpido e uno spazio fresco. Detta così suona bene, ma alla fine è acqua di Tyris del Nord che gira in tondo, e nemmeno per cortesia si potrebbe chiamarla limpida. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :123936
    (123936, 'It is a lifeline for the citizens and a facility where they can easily drink water. Although it is a social gathering place for ladies, North Tyris lacks water purification technology, and problems caused by drinking water are noticeable. Therefore, it is often seen burning on rainy days, perhaps to sterilize the water. \\n# ~Supporting Roles on the Streets~'):
        "È la linfa vitale dei cittadini, e un impianto dove si beve acqua senza tante cerimonie. È anche il ritrovo delle signore; ma a Tyris del Nord la tecnica per depurare l'acqua scarseggia, e i guai di chi l'ha bevuta si vedono. Sarà per questo che, forse per disinfettarla, nei giorni di pioggia capita spesso di vederlo che brucia. \\n# ~I Grandi Comprimari della Città~",

# 4 voci, 0 ambigue
}
