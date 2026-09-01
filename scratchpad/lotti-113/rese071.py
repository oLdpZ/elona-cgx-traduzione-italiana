import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :44863
    (44863, 'A seaweed with long, slender, branched bodies that can grow to over a meter in length. It has an excellent texture and throat, but is often pickled in vinegar and is not well-liked.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga dal corpo lungo, sottile e ramificato, che a volte passa il metro. La consistenza è ottima e scende bene in gola, ma la si mette quasi sempre sott'aceto, e per questo non piace a molti.\\n#~Alghe e Piante Marine: la Differenza~",

    # ---------------------------------------------------------- :44865
    (44865, "It's seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~"):
        "Un'alga. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ---------------------------------------------------------- :44926
    (44926, 'Seaweed that grows very long. It is also quite heavy due to its high water content. It takes some skill to dry it, but when it dries, it makes a good broth.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga che diventa lunghissima. Ha molta acqua dentro, e perciò pesa parecchio. Farla seccare richiede il suo mestiere, ma da secca se ne ricava un buon brodo.\\n#~Alghe e Piante Marine: la Differenza~",

    # ---------------------------------------------------------- :44928
    (44928, 'Giant seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~'):
        "Un'alga gigantesca. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ---------------------------------------------------------- :44989
    (44989, 'Large seaweed. It grows rapidly by absorbing nutrients from the sea. In some regions, it has long been valued as an ingredient in various dishes.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga di taglia grande. Assorbe il nutrimento del mare e si moltiplica in fretta. In certe regioni, fin da tempi antichi, è tenuta cara come ingrediente di piatti d'ogni sorta.\\n#~Alghe e Piante Marine: la Differenza~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :44991
    (44991, 'Huge seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~'):
        "Un'alga grande. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

# 3 voci, 0 ambigue
}
