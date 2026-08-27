# -*- coding: utf-8 -*-
"""Le rese del lotto 013 (le armi a DISTANZA, `FILTER_RANGE`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 013 scratchpad/lotti-110

**56 righe del sorgente, 55 firme**, 53 giapponesi distinti. Come le armi del
lotto 012, non c'è una formula: c'è un vocabolario, e sta nei nomi degli oggetti.

⭐ **La scala della gittata**, che il giapponese grada in quattro scalini con la
stessa parola (減衰, *il calo*), e che in italiano si legge in ordine:

    遠距離でも安定した威力 -> tiene la forza anche a distanza   (:76392)
    距離による減衰が殆どない -> con la distanza non cala quasi   (:96713)
    距離による減衰が少ない  -> con la distanza cala poco        (:115799)
    距離によって威力が減衰する -> con la distanza perde forza    (:127141)

⚠️ `:77148` è 非常に重い e `:77916` è とても重い: due mitragliatrici, due
giapponesi diversi per «molto pesante». Rese «pesantissima» e «molto pesante».
"""

IT = {
    # === la scala della gittata
    76392: "Un'arma da fuoco che tiene la forza anche a distanza.",
    96713: "Un'arma da fuoco che con la distanza non cala quasi.",
    115799: "Un'arma da fuoco che con la distanza cala poco.",
    127141: "Un'arma da fuoco che con la distanza perde forza.",
    97806: "Un'arma da fuoco che porta poco lontano.",

    # === gli archi
    53704: "Un arco corto piccolissimo.",
    54670: "Un arco con le lame.",
    61446: "Un arco d'ossa che fa ribrezzo.",
    61516: "Un arco tagliente che scaglia anche fulmini.",
    72693: "Un arco lungo dai colori dell'arcobaleno.",
    78401: "Un arco lavorato nell'osso.",
    115875: "Un arco buono da vicino e a media distanza.",
    127283: "Un arco buono a media e lunga distanza.",
    117391: "Un arco lungo che ha la forza di tirarti addosso i nemici.",
    72763: "Un arco meccanico che spara più colpi di fila.",
    77078: "Un arco meccanico pesantissimo.",

    # === le balestre
    53351: "Una balestra di fuoco a ingranaggi, non finita.",
    53492: "Una balista fatta per il tiro di precisione.",
    53634: "Un arco a ripetizione ispirato a un serpente velenoso.",
    54746: "Una balestra con un meccanismo che accende le frecce.",
    67261: "Una balestra grandissima.",
    68329: "Una balestra piccola, che al poco potere supplisce col veleno.",
    98804: "Un'arma da tiro che si equipaggia coi dardi da balestra.",

    # === le armi da fuoco
    54822: "Due armi da fuoco piccole che fanno una cosa sola.",
    65066: "Una pistola laser potente, ma pesante.",
    96570: "Una pistola laser con effetti magici di ogni genere.",
    67393: "Un fucile di precisione di grosso calibro.",
    76461: "Un fucile di precisione modificato parecchio.",
    72284: "Un fucile a pompa per il corpo a corpo.",
    77148: "Una mitragliatrice pesantissima.",
    77916: "Una mitragliatrice molto pesante.",
    80359: "Una pistola che passa da parte a parte anche chi non si vede.",
    71582: "Due pistole gemelle che paiono voler diventare una.",
    77427: "Due pistole gemelle uguali come due gocce d'acqua.",

    # === le due armi donate dagli dei
    86000: "Un fucile a pompa donato dal dio delle macchine.",
    86070: "Un arco lungo donato dalla dea del vento.",

    # === quel che si lancia
    68185: "Un'arma da lancio.",
    117188: "Un'arma da lancio.",
    72354: "Un'arma da lancio che fa sanguinare il nemico.",
    74238: "Un'arma da lancio che fa sanguinare il nemico.",
    # ⓘ `:83345` ha la stessa firma di `:74238` — stesso giapponese E stesso
    #    inglese — quindi il template non la porta: la copre la resa qui sopra.
    #    `:72354` invece ha lo stesso giapponese ma un inglese diverso, e il
    #    template la porta a parte.
    83278: "Un'arma da lancio che cadendo fa scoppiare l'aria intorno.",
    43708: "Si può usare sempre. Vale anche da arma da lancio.",
    74506: "Un coltello da lancio.",
    64416: "Uno shuriken a forma di anello.",
    57387: "Uno scarabeo da lanciare.",
    43634: "Delle foglie che esplodono.",
    52651: "Un gambero fritto che esplode. Vale da granata.",
    73225: "Una granata con uno scoppio potente.",
    77846: "Soldi d'una volta. Si possono lanciare come mance.",
    53564: "Una scheggia di roccia gigantesca.",
    75518: "Una moneta di pietra pesantissima: portarla basta a stupire.",
    83149: "Un sasso pesante. Si può equipaggiare.",

    # === il resto
    82550: "Un pianoforte pesante, fatto per assassinare.",
    83018: "La biancheria che Shena ha portato.",
    88673: "La biancheria che ha portato una donna.",
}
