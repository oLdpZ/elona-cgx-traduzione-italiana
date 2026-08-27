import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42917
    (42917, "It's a card that can be used to record info on a creature."):
        "Una carta che registra i dati di chi colpisci.",

    # ---------------------------------------------------------- :42979
    (42979, 'Throwable shit. Causes a poisonous explosion on impact.'):
        "Uno sterco che, lanciato, fa un'esplosione velenosa.",

    # ---------------------------------------------------------- :43177
    (43177, 'Throwable, inedible metal can. Causes a nerve explosion on impact.'):
        "Una scatoletta immangiabile. Lanciata, fa un'esplosione neurale.",

    # ---------------------------------------------------------- :43305
    (43305, 'Throwable, crystalized snowflakes. Causes an icy explosion on impact.'):
        "Un cristallo di neve che, lanciato, sprigiona gelo.",

    # ---------------------------------------------------------- :43367
    (43367, 'Throwable grenades that unleashes darkness explosion.'):
        "Un attrezzo che, lanciato, sprigiona oscurità.",

    # ---------------------------------------------------------- :43429
    (43429, 'Throwable batteries that discharges electrical shocks.'):
        "Un lungo ago che, lanciato, sprigiona fulmini.",

    # ---------------------------------------------------------- :43491
    (43491, "Throwable boxes packed with plagues, probably shouldn't open them."):
        "Una scatola piena di pestilenza. Meglio non aprirla.",

    # ---------------------------------------------------------- :43770
    (43770, 'It is a coupon covering basic pet training fees.'):
        "Paga l'addestramento di un compagno di LV non superiore al tuo.",

    # ---------------------------------------------------------- :43832
    (43832, "It's a bland potion cork."):
        "Un tappo di pozione come tanti.",

    # ---------------------------------------------------------- :43965
    (43965, 'It is an item rewarded to obedient slaves.'):
        "Una catena gradita a chi ha un alto grado di sottomissione.",

    # ---------------------------------------------------------- :46013
    (46013, '(Reusable) tool. Worth less than you think.'):
        "Si può usare sempre.",

    # ---------------------------------------------------------- :46216
    (46216, 'It is an edible plant that heals you.'):
        "Una pianta che, mangiata, cura un poco.",

    # ---------------------------------------------------------- :46278
    (46278, 'It is a bottle cap.'):
        "Il tappo di una bottiglia. Non serve ad altro.",

    # ---------------------------------------------------------- :46340
    (46340, "It is a bottle cap for Ramune soda. It's useless."):
        "Il tappo di una bottiglia di gazzosa. Non serve ad altro.",

    # ---------------------------------------------------------- :47152
    (47152, '(Reusable) tool that reduces the guard break gauge.'):
        "Un fischietto che abbassa la rottura guardia. Si usa sempre.",

    # ---------------------------------------------------------- :48738
    (48738, 'It is an insect that frightens the opponent when you hit them with it.'):
        "Una cicala moribonda.",

    # ---------------------------------------------------------- :50881
    (50881, 'These are materials for book publishing.'):
        "Un materiale per fare libri.",

    # ---------------------------------------------------------- :52582
    (52582, 'It is a bead that prevents objects from shattering due to low-temp.'):
        "Una perla ricurva: portandola, il gelo non spacca gli oggetti.",

    # ---------------------------------------------------------- :55276
    (55276, 'Threwable barrel that spews flame when burning.'):
        "Un barile che bruciando sputa fuoco. Lanciato, esplode in fiamme.",

    # ---------------------------------------------------------- :55862
    (55862, 'These are remains of ancient organisms.'):
        "La traccia di un essere vivente.",

    # ---------------------------------------------------------- :55924
    (55924, 'It is some sticky soil.'):
        "Della terra appiccicosa.",

    # ---------------------------------------------------------- :55986
    (55986, 'It is a yellow crystal.'):
        "Un cristallo giallo.",

    # ---------------------------------------------------------- :56536
    (56536, 'It is a device that keeps the holder in shape.'):
        "Un apparecchio che conserva la linea di chi lo porta.",

    # ---------------------------------------------------------- :57896
    (57896, 'It is a ticket that can be used instead of platinum when teaching skills.'):
        "Un foglio che sostituisce il platino quando impari un'abilità.",

    # ---------------------------------------------------------- :58027
    (58027, 'It is a sharp interim material.'):
        "Un materiale intermedio affilato.",

    # ---------------------------------------------------------- :58151
    (58151, 'It is a hard interim material.'):
        "Un materiale intermedio duro.",

    # ---------------------------------------------------------- :58275
    (58275, 'It is a soft interim material.'):
        "Un materiale intermedio morbido.",

    # ---------------------------------------------------------- :59731
    (59731, 'It is a bunch of fresh flowers. Used to convey feelings.'):
        "Un mazzo di fiori freschi. Si usa per dire quel che si prova.",

    # ---------------------------------------------------------- :59793
    (59793, 'It is a thrown talisman that erases buffs.'):
        "Un talismano che cancella un potenziamento. Si può lanciare.",

    # ---------------------------------------------------------- :60128
    (60128, "It is a box that can't be opened. But it can be thrown."):
        "Una scatola che non si può aprire. Ma si può lanciare.",

    # ---------------------------------------------------------- :60851
    (60851, 'These are cigarette butts that ignites when thrown.'):
        "Un mozzicone di sigaretta. Lanciato, prende fuoco.",

    # ---------------------------------------------------------- :61181
    (61181, '(Single-use) medicinal tool that is highly addictive.'):
        "Foglie di una pianta che dà dipendenza. Si usa (usa e getta).",

    # ---------------------------------------------------------- :61313
    (61313, 'These are red coins used for special services.'):
        "Una moneta rossastra. Dà diritto a certi servizi.",

    # ---------------------------------------------------------- :62735
    (62735, '(Reusable) tool that designates the target and raises the morale.'):
        "Un bastone che alza il morale dei compagni e sceglie il bersaglio.",

    # ---------------------------------------------------------- :62868
    (62868, '(Autoused) tool that helps with training.'):
        "Un oggetto che si usa da sé quando ti alleni.",

    # ---------------------------------------------------------- :62932
    (62932, '(Autoused) tool that cure your sickness.'):
        "Un oggetto che scatta da sé quando ti ammali.",

    # ---------------------------------------------------------- :62996
    (62996, '(Autoused) tool that helps with special training.'):
        "Un oggetto che si usa da sé quando addestri.",

    # ---------------------------------------------------------- :63060
    (63060, '(Autoused) tool that helps with tactical instruction.'):
        "Un oggetto che si usa da sé quando dai ordini tattici.",

    # ---------------------------------------------------------- :63124
    (63124, '(Autoused) tool that reveals extra character information.'):
        "Un oggetto che si usa da sé quando guardi una scheda.",

    # ---------------------------------------------------------- :63188
    (63188, '(Autoused) tool that helps reading.'):
        "Un oggetto che si usa da sé quando leggi un libro di studio.",

    # ---------------------------------------------------------- :63252
    (63252, '(Autoused) tool for drinking potions.'):
        "Un oggetto che si usa da sé quando bevi una pozione.",

    # ---------------------------------------------------------- :63316
    (63316, '(Autoused) tool that helps harvest.'):
        "Un oggetto che si usa da sé quando raccogli.",

    # ---------------------------------------------------------- :63586
    (63586, 'It is a throwable item that inflicts damage and disorientates opponent.'):
        "Un oggetto che all'urto ferisce e rompe la guardia.",

    # ---------------------------------------------------------- :64618
    (64618, 'It is a woven basket with no contents.'):
        "Un cesto di vimini senza niente dentro.",

    # ---------------------------------------------------------- :64872
    (64872, 'Throwable magic crystal that explodes thrice upon impact.'):
        "Un cristallo che, lanciato, esplode più volte.",

    # ---------------------------------------------------------- :64934
    (64934, 'Throwable magical crystal that explodes on impact.'):
        "Un cristallo che esplode all'urto.",

    # ---------------------------------------------------------- :66012
    (66012, 'It is a bead that soaks the holder in water.'):
        "Una perla ricurva: portandola addosso, ci si bagna.",

    # ---------------------------------------------------------- :66264
    (66264, 'It is an item used for artifact fusion.'):
        "Un oggetto per la sintesi.",

    # ---------------------------------------------------------- :66326
    (66326, 'It is a stork E.G.G, or S.E.G.Gs.'):
        "Il dono dei figli.",

    # ---------------------------------------------------------- :66768
    (66768, 'It is a large stone suitable for sculpture.'):
        "Una grande pietra buona per scolpire.",

    # ---------------------------------------------------------- :68048
    (68048, 'It is a bead that prevents objects from shattering due to high-temp.'):
        "Una perla ricurva: portandola, il fuoco non provoca incendi.",

    # ---------------------------------------------------------- :68391
    (68391, 'It is a tree processed into a carpentry material.'):
        "Del legno lavorato per farne materiale.",

    # ---------------------------------------------------------- :69391
    (69391, '(Autoused) tool for rubbing livestocks.'):
        "Si usa da sé, sempre, quando accarezzi il bestiame.",

    # ---------------------------------------------------------- :71646
    (71646, '(Autoused) tool that catches the fish automatically.'):
        "Un'esca automatica. Si usa da sé quando peschi.",

    # ---------------------------------------------------------- :75378
    (75378, 'They sell for a reasonable price.'):
        "Un oggetto che si vende a un prezzo discreto.",

    # ---------------------------------------------------------- :86738
    (86738, '(Autoused) tool that enhances your mastery of monsters.'):
        "Portato addosso, alza le probabilità di dominare i mostri.",

    # ---------------------------------------------------------- :89761
    (89761, 'It is bait for a fishing pole.'):
        "Un'esca per la canna da pesca.",

    # ---------------------------------------------------------- :91463
    (91463, 'It is a scarecrow covered in snow.'):
        "Uno spaventapasseri coperto di neve.",

    # ---------------------------------------------------------- :92454
    (92454, 'It is biological excrement.'):
        "Gli escrementi di un essere vivente.",

    # ---------------------------------------------------------- :109211
    (109211, "It is the remain's of a tree. It can be used as a seat."):
        "Quel che resta di un albero tagliato. Si può usare sempre.",

    # ---------------------------------------------------------- :111066
    (111066, 'It is a bundle of fresh flowers.'):
        "Un mazzo di fiori freschi.",

    # ---------------------------------------------------------- :112758
    (112758, 'It is an item for cleaning.'):
        "Un attrezzo per pulire.",

    # ---------------------------------------------------------- :112820
    (112820, 'It is a bird deterrent placed in the field.'):
        "Uno scacciauccelli da mettere nel campo.",

    # ---------------------------------------------------------- :112882
    (112882, 'It is dried wood ready for burning.'):
        "Pezzi di legno tagliati per il focolare.",

    # ---------------------------------------------------------- :116411
    (116411, 'These are bones of a dead animal.'):
        "Le ossa abbandonate di un animale.",

    # ---------------------------------------------------------- :116473
    (116473, 'It is a bundle of dried grass.'):
        "Erba secca legata in fascio.",

    # ---------------------------------------------------------- :116543
    (116543, 'It is a dried fish. Cannot be used.'):
        "Un pesce secco. Non si può usare.",

    # ---------------------------------------------------------- :116668
    (116668, "It is the empty space which makes the bowl useful, and it's full already."):
        "Un recipiente con qualcosa dentro.",

    # ---------------------------------------------------------- :116730
    (116730, 'It is an empty bowl.'):
        "Un recipiente senza niente dentro.",

    # ---------------------------------------------------------- :116792
    (116792, 'It is a woven basket.'):
        "Un cesto di vimini.",

    # ---------------------------------------------------------- :116854
    (116854, 'These are chipped empty bottles. Cannot be used.'):
        "Bottiglie vuote e scheggiate, tutte insieme. Non si possono usare.",

    # ---------------------------------------------------------- :116916
    (116916, 'These are minerals that are mostly made of rock.'):
        "Un minerale fatto quasi tutto di roccia.",

    # ---------------------------------------------------------- :127672
    (127672, 'These are abandoned human bones.'):
        "Le ossa abbandonate di una persona.",

    # ---------------------------------------------------------- :127734
    (127734, 'These are abandoned bones.'):
        "Le ossa abbandonate di qualcosa.",

    # ---------------------------------------------------------- :127796
    (127796, 'It is a useless damaged sword.'):
        "Una spada rotta che non serve a niente.",

    # ---------------------------------------------------------- :127858
    (127858, 'It is an ornament made of cloth.'):
        "Un ornamento fatto di stoffa.",

    # ---------------------------------------------------------- :127920
    (127920, 'It is a simple lighting fixture. Always illuminates the surroundings.'):
        "Una lampada semplice. Illumina sempre di luce viva.",

    # ---------------------------------------------------------- :127982
    (127982, 'These are dirty clothes in a basket.'):
        "Vestiti sporchi dentro un cesto.",

    # ---------------------------------------------------------- :128044
    (128044, 'It is a useless and damaged crucible.'):
        "Un vaso rotto che non serve a niente.",

    # ---------------------------------------------------------- :128106
    (128106, 'It is a bunch of dry grass.'):
        "Un fascio di erba secca.",

    # ---------------------------------------------------------- :128238
    (128238, 'It is a damaged piece of wood.'):
        "Una scheggia di legno rotto.",

# 81 voci, 0 ambigue
}
