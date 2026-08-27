# -*- coding: utf-8 -*-
"""Le rese del lotto 025 (LA CODA dell'indice 3), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 025 scratchpad/lotti-111

Il ragionamento sta per esteso in `testa025.py`. Lo scheletro lo fa
`lotti-111/_coda.py`, non `_107-chiavi-item.py`.
"""

IT = {
    # === le munizioni: 〜と共に装備する武器だ
    96637: "Un'arma da equipaggiare insieme a un'arma da fuoco.",
    65950: "Un'arma da equipaggiare insieme a una pistola (solo pistole).",
    127065: "Un'arma da equipaggiare insieme a un arco.",
    98728: "Un'arma da equipaggiare insieme a una balestra.",

    # === i resti di creatura: 生物の〜だ
    108522: "L'osso di una creatura.",
    108584: "Il cuore di una creatura.",
    108646: "L'occhio di una creatura.",
    108708: "Il sangue di una creatura.",
    108770: "La pelle di una creatura.",

    # === l'acqua: tre righe che il giapponese distingue e l'inglese no
    87577: "Un impianto che usa l'acqua. Si può bere più volte.",
    123939: "Un impianto che raccoglie l'acqua. Si può bere.",
    90710: "Un pozzo pieno d'acqua santa. Si può bere.",

    # === le alghe
    44866: "Un'alga. Si può mangiare.",
    44929: "Un'alga gigantesca. Si può mangiare.",
    44992: "Un'alga grande. Si può mangiare.",

    # === i due altari
    119822: "Un altare semplice. Ci si possono fare offerte.",
    119884: "Un piedistallo in lode del dio. Ci si possono fare offerte.",

    # === le monete
    127486: "Una moneta speciale e lucente. Serve a pagare l'istruttore.",
    127548: "La moneta corrente in tutto il mondo.",

    # === il resto
    97266: "Un foglio con i dati di una creatura. Si mette nel mazzo.",
    97328: "Una statua che riproduce un mostro.",
    109023: "Un cibo del tipo che si carica sul carretto.",

    # === la voce che non esiste: giapponese vuoto, e l'inglese dice il vero
    131247: "Non è usato nel gioco.",
}
