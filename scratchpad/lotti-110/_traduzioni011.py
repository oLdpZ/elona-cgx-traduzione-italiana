# -*- coding: utf-8 -*-
"""Le rese del lotto 011 (i GRIMORI, `FILTER_ITEM_SPELLBOOK`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 011 scratchpad/lotti-110

**82 righe del sorgente, 82 firme**, e 79 giapponesi distinti.

    〜を唱える為に必要な本。読むことができる。 -> Un libro per ... Si può leggere.
    〜を唱える為に必要な本だ。                 -> Un libro per ...   (senza coda)

⚠️⚠️ **La coda c'è o non c'è, e non è una svista da riparare.** Cinquantasei
righe chiudono con 「読むことができる。」 e ventisei con 「…必要な本だ。」 e
basta. Si segue il giapponese riga per riga: tutte le righe lunghe stanno fra
quelle senza coda, e infatti ci stanno nei 69.

⚠️ **Il RANGO non si scrive.** Ogni inglese apre con «Book of Rank N Magic», e
il giapponese non lo dice **mai**, su nessuna delle 82. È la prova positiva
della 109ª (il rango degli strumenti musicali): questo file scrive
「（ランクN）」 quando vuole dirlo — su tutti i letti e su tutti i fornelli — e
qui ha scelto di non dirlo.

⭐ **Le tre classi di magia, che in italiano si leggono in scala:**

    〜属性の矢       -> una freccia ...        (12 firme)
    〜属性のボルト   -> una saetta ...         (12 firme)
    〜属性の範囲魔法 -> una magia ad area ...  (12 firme)

I nomi degli elementi vengono da `skill.hsp`, dove la famiglia delle saette è
già tutta resa: gelo, fuoco, fulmine, d'oscurità, mentale, d'oltretomba,
velenosa, sonora, caotica, dei nervi, magica.
"""

IT = {
    # === le dodici FRECCE (矢)
    48238: "Un libro per una freccia di fuoco. Si può leggere.",
    48311: "Un libro per una freccia di gelo. Si può leggere.",
    48384: "Un libro per una freccia di fulmine. Si può leggere.",
    48457: "Un libro per una freccia mentale. Si può leggere.",
    48530: "Un libro per una freccia velenosa. Si può leggere.",
    48603: "Un libro per una freccia sonora. Si può leggere.",
    48676: "Un libro per una freccia di tipo PV/DV. Si può leggere.",
    86943: "Un libro per una freccia d'oscurità. Si può leggere.",
    113462: "Un libro per una freccia dei nervi. Si può leggere.",
    113535: "Un libro per una freccia caotica. Si può leggere.",
    113608: "Un libro per una freccia d'oltretomba. Si può leggere.",
    114016: "Un libro per una freccia magica. Si può leggere.",

    # === le dodici SAETTE (ボルト)
    128944: "Un libro per una saetta di fuoco. Si può leggere.",
    129017: "Un libro per una saetta di gelo. Si può leggere.",
    128871: "Un libro per una saetta di fulmine. Si può leggere.",
    113247: "Un libro per una saetta mentale. Si può leggere.",
    47946: "Un libro per una saetta velenosa. Si può leggere.",
    48019: "Un libro per una saetta sonora. Si può leggere.",
    61869: "Un libro per una saetta di tipo PV/DV. Si può leggere.",
    113320: "Un libro per una saetta d'oscurità. Si può leggere.",
    48165: "Un libro per una saetta dei nervi. Si può leggere.",
    48092: "Un libro per una saetta caotica. Si può leggere.",
    47873: "Un libro per una saetta d'oltretomba. Si può leggere.",
    84443: "Un libro per una saetta magica. Si può leggere.",

    # === le dodici MAGIE AD AREA (範囲魔法呪文)
    113101: "Un libro per una magia ad area di fuoco. Si può leggere.",
    113174: "Un libro per una magia ad area di gelo. Si può leggere.",
    47362: "Un libro per una magia ad area di fulmine. Si può leggere.",
    47727: "Un libro per una magia ad area mentale. Si può leggere.",
    47581: "Un libro per una magia ad area velenosa. Si può leggere.",
    113028: "Un libro per una magia ad area sonora. Si può leggere.",
    47654: "Un libro per una magia ad area di tipo PV/DV. Si può leggere.",
    47435: "Un libro per una magia ad area d'oscurità. Si può leggere.",
    47800: "Un libro per una magia ad area dei nervi. Si può leggere.",
    112955: "Un libro per una magia ad area caotica. Si può leggere.",
    47508: "Un libro per una magia ad area d'oltretomba. Si può leggere.",
    84516: "Un libro per una magia ad area arcana. Si può leggere.",

    # === i tre grimori che alzano due attributi e danno due resistenze
    58996: "Un libro per alzare Cos e Car e resistere a paralisi e cecità.",
    105889: "Un libro per alzare For e Des e resistere a terrore e confusione.",
    65603: "Un libro per alzare Per e Vol e resistere a sonno e confusione.",

    # === quel che si crea nel punto scelto
    91985: "Un libro per aprire una porta dove vuoi. Si può leggere.",
    92873: "Un libro per alzare muri di fiamme dove vuoi. Si può leggere.",
    93225: "Un libro per creare una pozza d'acido dove vuoi. Si può leggere.",
    94457: "Un libro per alzare un muro dove vuoi. Si può leggere.",
    98652: "Un libro per tendere una ragnatela sul bersaglio. Si può leggere.",

    # === le cure
    94178: "Un libro per curare te o un compagno che ti sta accanto.",
    94322: "Un libro per curare i compagni qui intorno. Si può leggere.",
    114353: "Un libro per recuperare HP. Si può leggere.",
    114426: "Un libro per recuperare HP. Si può leggere.",
    114499: "Un libro per recuperare HP. Si può leggere.",
    114572: "Un libro per recuperare HP. Si può leggere.",
    106545: "Un libro per alzare per un po' la guarigione. Si può leggere.",

    # === le maledizioni, tolte e respinte
    105231: "Un libro per togliersi di dosso tutte le maledizioni.",
    105304: "Un libro per togliersi di dosso una maledizione.",
    105528: "Un libro per resistere un po' alle maledizioni. Si può leggere.",
    129727: "Un libro per purificare gli oggetti. Si può leggere.",

    # === quel che si abbassa al bersaglio
    104595: "Un libro per abbassare per un po' le resistenze mentali altrui.",
    105672: "Un libro per abbassare per un po' le resistenze elementali altrui.",
    105745: "Un libro per abbassare per un po' il PV del bersaglio.",
    106184: "Un libro per rallentare il bersaglio. Si può leggere.",
    106689: "Un libro per mettere il bersaglio in silenzio. Si può leggere.",
    98877: "Un libro per tirare il bersaglio dalla tua parte. Si può leggere.",

    # === quel che si alza a sé
    106257: "Un libro per accelerare. Si può leggere.",
    106401: "Un libro per alzare per un po' le resistenze. Si può leggere.",
    106842: "Un libro per alzare per un po' il DV e resistere al terrore.",
    72960: "Un libro per liberarsi dal peso e schivare meglio.",
    83558: "Un libro per azzerare, a volte, un colpo mortale.",

    # === i teletrasporti
    123495: "Un libro per un teletrasporto corto. Si può leggere.",
    129873: "Un libro per il teletrasporto. Si può leggere.",
    114645: "Un libro per tornare in un posto preciso. Si può leggere.",

    # === il resto
    82080: "Un libro per far piovere monete d'oro dal cielo. Si può leggere.",
    82153: "Un libro per evocare uno spazio dove tenere gli oggetti.",
    85104: "Un libro con dentro un sapere antico. Si può leggere.",
    89013: "Un libro per far dimenticare l'ostilità a chi non è un mostro.",
    102040: "Un libro per farsi venire una mutazione. Si può leggere.",
    103652: "Un libro per scoprire gli oggetti qui intorno. Si può leggere.",
    104522: "Un libro per farsi aiutare nella lettura. Si può leggere.",
    111853: "Un libro per poter esprimere un desiderio. Si può leggere.",
    114718: "Un libro per sapere dove sono finiti gli artefatti apparsi.",
    114791: "Un libro per rivelare le zone non esplorate. Si può leggere.",
    123360: "Un libro per evocare mostri. Si può leggere.",
    129800: "Un libro per identificare un oggetto. Si può leggere.",

    # ⚠️ non è un libro: è un foglio, e l'unico del lotto che si consuma
    78730: "Un foglio per imparare un piatto difficile. Si usa (usa e getta).",
}
