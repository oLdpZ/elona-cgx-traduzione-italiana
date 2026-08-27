# -*- coding: utf-8 -*-
"""Le rese del lotto 010 (i CONTENITORI, `FILTER_CONTAINER`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 010 scratchpad/lotti-110

**22 righe del sorgente, 21 firme.** Venti righe su ventidue chiudono con
「開けることができる。」, che si aggancia alle code della 109a:

    開けることができる -> Si può aprire.

⚠️⚠️ `:115137` e `:115261` hanno lo **stesso giapponese**
(「金品が入った箱。開けることができる。」) e due inglesi diversi — «container
containing money and goods» contro «ancient jeweled chest». Il fatto che
l'inglese aggiunge (antica, ingioiellata) e' gia' il **nome dell'oggetto**: una
resa per due firme, come le sette tombe della 109a.
"""

IT = {
    # --- la famiglia dei valori: quattro contenitori, un solo fatto
    112199: "Un sacchetto con denaro e beni. Si può aprire.",
    112261: "Una borsa con denaro e beni. Si può aprire.",
    # ⚠️ due righe, stesso giapponese, stessa resa: il template le vuole
    #    tutt'e due, e `_monta.py` si ferma se ne manca una
    115137: "Una scatola con denaro e beni. Si può aprire.",
    115261: "Una scatola con denaro e beni. Si può aprire.",
    115199: "Una scatola pesantissima con denaro e beni. Si può aprire.",

    # --- le due dispense
    88150: "Tiene 4 cibi senza farli marcire. Si può aprire.",
    92189: "Tiene 15 cibi senza farli marcire. Si può aprire.",

    # --- le scatole di servizio
    89824: "Una scatola per la fattura e i soldi delle tasse. Si può aprire.",
    93486: "Una scatola per riporre le cose indicate. Si può aprire.",
    94384: "Una scatola dove arriva la paga. Si può aprire.",
    96847: "Una borsa con l'eredità dei personaggi passati. Si può aprire.",
    104728: "Una scatola con materiali da lavorazione. Si può aprire.",
    107117: "Una borsa con armi e armature. Si può aprire.",

    # --- il resto
    57128: "Un sacchetto di carta: dentro non si vede. Si può aprire.",
    78661: "Un pacchetto di carte a caso, numerate di seguito.",
    80739: "Un sacco pieno di cose di ogni genere. Si può aprire.",
    81263: "Una scatola con dentro un gatto. Si può aprire.",
    81944: "Una scatola con spiccioli, e di rado un tesoro. Si può aprire.",
    90835: "I ceppi che tengono legato un gigante. Si può aprire.",
    93423: "La cassaforte con l'incasso del negozio. Si può aprire.",
    103236: "Una sfera piena di oggetti. Si può aprire.",
}
