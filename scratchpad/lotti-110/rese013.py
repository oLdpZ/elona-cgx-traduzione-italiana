import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43634
    (43634, "It's a bunch of explosive leaves."):
        "Delle foglie che esplodono.",

    # ---------------------------------------------------------- :43708
    (43708, '(Reusable) throwable artefact.'):
        "Si può usare sempre. Vale anche da arma da lancio.",

    # ---------------------------------------------------------- :52651
    (52651, 'It is an exploding fried shrimp. Can be used as a grenade.'):
        "Un gambero fritto che esplode. Vale da granata.",

    # ---------------------------------------------------------- :53351
    (53351, 'It is an imperfect mechanical flame crossbow.'):
        "Una balestra di fuoco a ingranaggi, non finita.",

    # ---------------------------------------------------------- :53492
    (53492, 'It is a crossbow designed for extreme ranges.'):
        "Una balista fatta per il tiro di precisione.",

    # ---------------------------------------------------------- :53564
    (53564, 'It is a giant rock that reeks of death.'):
        "Una scheggia di roccia gigantesca.",

    # ---------------------------------------------------------- :53634
    (53634, 'It is a crossbow with the image of a viper.'):
        "Un arco a ripetizione ispirato a un serpente velenoso.",

    # ---------------------------------------------------------- :53704
    (53704, 'It is a very small shortbow.'):
        "Un arco corto piccolissimo.",

    # ---------------------------------------------------------- :54670
    (54670, 'It is a bow with a blade.'):
        "Un arco con le lame.",

    # ---------------------------------------------------------- :54746
    (54746, 'It is a crossbow with a mechanism to ignite the arrow.'):
        "Una balestra con un meccanismo che accende le frecce.",

    # ---------------------------------------------------------- :54822
    (54822, 'These are two-in-one small firearms.'):
        "Due armi da fuoco piccole che fanno una cosa sola.",

    # ---------------------------------------------------------- :57387
    (57387, 'It is a beetles made for throwing.'):
        "Uno scarabeo da lanciare.",

    # ---------------------------------------------------------- :61446
    (61446, 'It is a terrifying bone bow.'):
        "Un arco d'ossa che fa ribrezzo.",

    # ---------------------------------------------------------- :61516
    (61516, 'It is a slashing bow that can also release electric shocks.'):
        "Un arco tagliente che scaglia anche fulmini.",

    # ---------------------------------------------------------- :64416
    (64416, 'It is a wheel-shaped shuriken.'):
        "Uno shuriken a forma di anello.",

    # ---------------------------------------------------------- :65066
    (65066, 'It is a high-performance but heavy photon gun.'):
        "Una pistola laser potente, ma pesante.",

    # ---------------------------------------------------------- :67261
    (67261, 'It is a supersized crossbow.'):
        "Una balestra grandissima.",

    # ---------------------------------------------------------- :67393
    (67393, 'It is a large caliber sniper rifle.'):
        "Un fucile di precisione di grosso calibro.",

    # ---------------------------------------------------------- :68185
    (68185, 'It is a throwing weapon. Difficult to use. Hurt as hell when hit.'):
        "Un'arma da lancio.",

    # ---------------------------------------------------------- :68329
    (68329, 'It is a small crossbow with poison to compensate for their power.'):
        "Una balestra piccola, che al poco potere supplisce col veleno.",

    # ---------------------------------------------------------- :71582
    (71582, 'These are twin guns that look like they could combine somehow.'):
        "Due pistole gemelle che paiono voler diventare una.",

    # ---------------------------------------------------------- :72284
    (72284, 'It is a shotgun for close-quarter combat.'):
        "Un fucile a pompa per il corpo a corpo.",

    # ---------------------------------------------------------- :72354
    (72354, 'It is a thrown weapon that causes the opponent to bleed.'):
        "Un'arma da lancio che fa sanguinare il nemico.",

    # ---------------------------------------------------------- :72693
    (72693, 'It is a seven colored longbow.'):
        "Un arco lungo dai colori dell'arcobaleno.",

    # ---------------------------------------------------------- :72763
    (72763, 'It is a mechanical bow with enhanced firing rate.'):
        "Un arco meccanico che spara più colpi di fila.",

    # ---------------------------------------------------------- :73225
    (73225, 'It is a grenade with a powerful blast.'):
        "Una granata con uno scoppio potente.",

    # ---------------------------------------------------------- :74238
    (74238, 'It is a throwing weapon that causes the opponent to bleed.'):
        "Un'arma da lancio che fa sanguinare il nemico.",

    # ---------------------------------------------------------- :74506
    (74506, 'It is a throwing knife.'):
        "Un coltello da lancio.",

    # ---------------------------------------------------------- :75518
    (75518, 'It is a terrific to hold, very heavy stone coin.'):
        "Una moneta di pietra pesantissima: portarla basta a stupire.",

    # ---------------------------------------------------------- :76392
    (76392, 'It is a firearm that are stable and powerful even at long distances.'):
        "Un'arma da fuoco che tiene la forza anche a distanza.",

    # ---------------------------------------------------------- :76461
    (76461, 'It is a very customized sniper rifle.'):
        "Un fucile di precisione modificato parecchio.",

    # ---------------------------------------------------------- :77078
    (77078, 'It is a very heavy mechanical bow.'):
        "Un arco meccanico pesantissimo.",

    # ---------------------------------------------------------- :77148
    (77148, 'It is a very heavy machine gun.'):
        "Una mitragliatrice pesantissima.",

    # ---------------------------------------------------------- :77427
    (77427, 'These are twin guns that look exactly alike.'):
        "Due pistole gemelle uguali come due gocce d'acqua.",

    # ---------------------------------------------------------- :77846
    (77846, 'These are old money. Can be used for throwing.'):
        "Soldi d'una volta. Si possono lanciare come mance.",

    # ---------------------------------------------------------- :77916
    (77916, 'It is a very heavy machine gun.'):
        "Una mitragliatrice molto pesante.",

    # ---------------------------------------------------------- :78401
    (78401, 'It is a bow made of processed bone.'):
        "Un arco lavorato nell'osso.",

    # ---------------------------------------------------------- :80359
    (80359, 'It is a pistol that strikes down even those it cannot see.'):
        "Una pistola che passa da parte a parte anche chi non si vede.",

    # ---------------------------------------------------------- :82550
    (82550, 'It is a heavy piano for assassination.'):
        "Un pianoforte pesante, fatto per assassinare.",

    # ---------------------------------------------------------- :83018
    (83018, "It is Shena's used underwears."):
        "La biancheria che Shena ha portato.",

    # ---------------------------------------------------------- :83149
    (83149, 'It is a heavy pebble. Can be equipped.'):
        "Un sasso pesante. Si può equipaggiare.",

    # ---------------------------------------------------------- :83278
    (83278, 'It is a throwing weapon that creates a blast around it when it lands.'):
        "Un'arma da lancio che cadendo fa scoppiare l'aria intorno.",

    # ---------------------------------------------------------- :86000
    (86000, 'It is a shotgun bestowed by the God of Machine.'):
        "Un fucile a pompa donato dal dio delle macchine.",

    # ---------------------------------------------------------- :86070
    (86070, 'It is a longbow bestowed by the Goddess of Wind.'):
        "Un arco lungo donato dalla dea del vento.",

    # ---------------------------------------------------------- :88673
    (88673, 'It is an underwear worn by a woman.'):
        "La biancheria che ha portato una donna.",

    # ---------------------------------------------------------- :96570
    (96570, 'It is a photon gun with various magical effects.'):
        "Una pistola laser con effetti magici di ogni genere.",

    # ---------------------------------------------------------- :96713
    (96713, 'It is a firearm with little or no attenuation with distance.'):
        "Un'arma da fuoco che con la distanza non cala quasi.",

    # ---------------------------------------------------------- :97806
    (97806, 'It is a firearm with a short effective range.'):
        "Un'arma da fuoco che porta poco lontano.",

    # ---------------------------------------------------------- :98804
    (98804, 'It is a weapon to be equipped along with a bundle of crossbow bolts.'):
        "Un'arma da tiro che si equipaggia coi dardi da balestra.",

    # ---------------------------------------------------------- :115799
    (115799, 'It is a firearm with good medium range accuracy.'):
        "Un'arma da fuoco che con la distanza cala poco.",

    # ---------------------------------------------------------- :115875
    (115875, 'It is a bow specialized for short to medium range.'):
        "Un arco buono da vicino e a media distanza.",

    # ---------------------------------------------------------- :117188
    (117188, 'It is just a stone.'):
        "Un'arma da lancio.",

    # ---------------------------------------------------------- :117391
    (117391, 'It is a longbow with the power to draw in the enemy.'):
        "Un arco lungo che ha la forza di tirarti addosso i nemici.",

    # ---------------------------------------------------------- :127141
    (127141, 'It is a firearm made for short distances.'):
        "Un'arma da fuoco che con la distanza perde forza.",

    # ---------------------------------------------------------- :127283
    (127283, 'It is a bow specialized for medium to long range.'):
        "Un arco buono a media e lunga distanza.",

# 55 voci, 0 ambigue
}
