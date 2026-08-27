# -*- coding: utf-8 -*-
"""Le rese del lotto 019 (gli ALBERI, `FILTER_ENVIRONMENT`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 019 scratchpad/lotti-111

Il ragionamento sta per esteso in `testa019.py`. In breve: 12 righe, 9 firme —
落葉樹だ copre tre alberi e 常緑樹だ ne copre due, perche' giapponese e inglese
coincidono. Il vocabolario e' tutto nei nomi, gia' resi (albero, abete,
ciliegio), e le descrizioni non lo ripetono.
"""

IT = {
    # === i due termini tecnici, che coprono cinque righe in due firme
    95487: "Un albero che perde le foglie.",
    91525: "Un sempreverde.",

    # === gli alberi che dicono una cosa sola
    91587: "Un albero senza foglie.",
    95673: "Un albero secco.",
    95549: "Un albero dei paesi caldi.",
    95737: "Un albero che lascia cadere i frutti.",
    95799: "Un albero rimasto senza frutti.",

    # === i due addobbati
    68453: "Un ciliegio i cui fiori cadono per sempre.",
    90897: "Un abete addobbato.",
}
