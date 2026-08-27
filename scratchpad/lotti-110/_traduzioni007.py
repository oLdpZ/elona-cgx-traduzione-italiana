# -*- coding: utf-8 -*-
"""Le rese del lotto 007 (i MINERALI, `FILTER_ORE`), indicizzate per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 007 scratchpad/lotti-110

**33 righe del sorgente, 21 firme.** Dodici righe su trentatre sono le **dodici
gemme dei mesi** (`:48808`-`:49508`), che hanno **un solo giapponese**: una resa
le copre tutte. Le altre due righe in piu' sono i due tesori della sintesi.

Le formule:

    〜の要素が含まれる鉱石だ。 -> Un minerale che contiene tracce di ...  (3)
    〜色をした鉱石だ。         -> Un minerale di colore ...              (4)
    合成用のアイテムだ。       -> Un oggetto per la sintesi.  (come il lotto 006)
    模造品だ。                 -> Una riproduzione.  (come `db_item.hsp` altrove)

⚠️ `:82613`, il biglietto del concerto: l'inglese racconta che i biglietti si
danno ai musicisti promettenti, il giapponese dice solo che il foglio **non fa
niente**. Vince il giapponese, per la regola di `decisioni.md`.
"""

IT = {
    # --- le dodici gemme dei mesi: un giapponese solo per dodici righe
    48808: "Una gemma adatta a farne un regalo.",

    # --- i minerali: due formule, sette righe
    128308: "Un minerale che contiene tracce di diamante.",
    128378: "Un minerale che contiene tracce di smeraldo.",
    128518: "Un minerale che contiene tracce di rubynus.",
    128448: "Un minerale di colore bianco.",
    128658: "Un minerale di colore giallo.",
    128728: "Un minerale di colore rosso.",
    128798: "Un minerale di colore arancione.",
    128588: "Un minerale che brilla d'oro.",
    52316: "Un minerale che può servire come materiale per armi e armature.",
    128176: "Un sassolino da niente.",

    # --- le pietre lavorate
    69051: "Del rubynus lavorato.",
    69121: "Una tavoletta fatta di smeraldo.",
    69191: "Un diamante lavorato.",

    # --- i due tesori della sintesi
    66140: "Un oggetto per la sintesi.",

    # --- il resto
    49711: "Una statua di valore, ma pesante.",
    52173: "L'arte del mare profondo.",
    82216: "Stringe il legame con chi è più di un amico. Si può dare.",
    82613: "Un foglio senza alcun effetto. Cerca qualcuno che li collezioni.",
    89422: "Dicono che da qualche parte ci sia chi le colleziona.",
    117321: "Una riproduzione.",
}
