import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43561
    (43561, "It's a battle axe shaped like a bone."):
        "Un'ascia da battaglia che pare fatta d'osso.",

    # ---------------------------------------------------------- :51782
    (51782, 'It is a longsword having another sword, as its counterpart.'):
        "Una spada lunga che, dicono, ha una spada gemella.",

    # ---------------------------------------------------------- :51852
    (51852, 'It is a lance made from bamboo sticks.'):
        "Una lancia fatta di bambù.",

    # ---------------------------------------------------------- :51920
    (51920, 'It is a long clock hand that can be used as a longsword.'):
        "Una lancetta lunga che si usa come spada lunga.",

    # ---------------------------------------------------------- :52720
    (52720, 'It is Annin-tofu that looks like a lightsabre, you can wield it.'):
        "Un budino di mandorle a forma di spada laser. Vale da spada lunga.",

    # ---------------------------------------------------------- :52790
    (52790, 'It is a crab-claw shaped scissors.'):
        "Un paio di cesoie che paiono chele di granchio.",

    # ---------------------------------------------------------- :52860
    (52860, 'It is a set of five Kunais.'):
        "Un gruppo di cinque kunai.",

    # ---------------------------------------------------------- :52930
    (52930, 'It is a thin sword that manipulates electricity.'):
        "Un fioretto che comanda l'elettricità.",

    # ---------------------------------------------------------- :52999
    (52999, 'It is a giant drill that pierce the heavens.'):
        "Un trapano gigantesco che rimbomba fino al cielo.",

    # ---------------------------------------------------------- :53070
    (53070, 'It is a long, double-bladed throwing axe.'):
        "Un tomahawk lungo e a doppia lama.",

    # ---------------------------------------------------------- :53140
    (53140, "It is a scissors-sickle like a bird's beak."):
        "Un paio di cesoie come il becco di un uccello.",

    # ---------------------------------------------------------- :53209
    (53209, 'It is a pewter staff made with advanced science and technology.'):
        "Uno shakujo fatto con tecnologia avanzata.",

    # ---------------------------------------------------------- :53281
    (53281, 'It is a staff of trinity of three sections.'):
        "Un bastone a tre sezioni: tre in uno.",

    # ---------------------------------------------------------- :53421
    (53421, 'It is a type of sock called a tabi.'):
        "Un calzino del tipo che chiamano tabi.",

    # ---------------------------------------------------------- :53843
    (53843, "It is a ninja's shortsword, also suitable for throwing."):
        "Un pugnale da ninja, buono anche da lanciare.",

    # ---------------------------------------------------------- :53911
    (53911, 'It is a very light and thin longsword with electric properties.'):
        "Una spada leggerissima e sottile.",

    # ---------------------------------------------------------- :53978
    (53978, 'It is a polearm with a spiral-rotating blade.'):
        "Una lancia con la lama che gira a spirale.",

    # ---------------------------------------------------------- :54045
    (54045, 'It is an elongated conical polearm.'):
        "Una lancia a cono, lunga e sottile.",

    # ---------------------------------------------------------- :54115
    (54115, 'It is a small axe suitable for throwing.'):
        "Un'ascia piccola, buona anche da lanciare.",

    # ---------------------------------------------------------- :54183
    (54183, 'It is a mechanically driven saw. You can use it like an axe.'):
        "Una sega a motore. Si usa come un'ascia.",

    # ---------------------------------------------------------- :54251
    (54251, 'It is a scythe with multiple blades.'):
        "Una falce con più lame.",

    # ---------------------------------------------------------- :54319
    (54319, 'It is a scythe made of bones.'):
        "Una falce fatta d'ossa.",

    # ---------------------------------------------------------- :54387
    (54387, 'It is a blunt weapon with the protruding ends on both sides.'):
        "Un'arma contundente con le punte sporgenti ai lati.",

    # ---------------------------------------------------------- :54456
    (54456, 'It is a blunt weapon with a wrecking ball.'):
        "Un'arma contundente con una palla di ferro.",

    # ---------------------------------------------------------- :54524
    (54524, 'It is a staff with a loop on the end.'):
        "Un bastone con un anello in cima.",

    # ---------------------------------------------------------- :54594
    (54594, 'It is a staff that can be splitted and wielded quickly.'):
        "Un bastone che si divide e si gira in fretta.",

    # ---------------------------------------------------------- :56811
    (56811, 'It is a star-sphere-hammer that was attached to the tail of a dinosaur.'):
        "Una mazza ferrata che stava in coda a un dinosauro.",

    # ---------------------------------------------------------- :60198
    (60198, 'It is a lightweight blue battle axe.'):
        "Un'ascia da battaglia azzurra e leggera.",

    # ---------------------------------------------------------- :60789
    (60789, '(Usable) Evil scythe.'):
        "Una falce malvagia. Si può usare.",

    # ---------------------------------------------------------- :61251
    (61251, 'It is a war hammer disguised as a staff.'):
        "Un martello da guerra travestito da bastone.",

    # ---------------------------------------------------------- :61796
    (61796, 'It is a vortex-generating chain scythe.'):
        "Una falce a catena che leva vortici.",

    # ---------------------------------------------------------- :63457
    (63457, 'It is a staff that converts MP into offensive power.'):
        "Un bastone che muta gli MP in forza d'attacco.",

    # ---------------------------------------------------------- :63726
    (63726, 'It is a pure white long sword.'):
        "Una spada lunga tutta bianca.",

    # ---------------------------------------------------------- :64488
    (64488, 'It is a multipurpose shovel that can also be used as a polearm.'):
        "Una pala buona a tutto, anche da alabarda.",

    # ---------------------------------------------------------- :65136
    (65136, 'It is a long, burly club.'):
        "Un randello enorme e pieno di nodi.",

    # ---------------------------------------------------------- :65268
    (65268, 'It is a bloody whip.'):
        "Una frusta sporca di sangue.",

    # ---------------------------------------------------------- :65882
    (65882, 'It is a whip with poisonous thorns.'):
        "Una frusta con le spine avvelenate.",

    # ---------------------------------------------------------- :66843
    (66843, 'It is a dagger of sound. Also, it can be used as Rank 0-6 instrument.'):
        "Un pugnale che suona. Volendo, vale da strumento.",

    # ---------------------------------------------------------- :66913
    (66913, 'It is a greatsword with a separable blade.'):
        "Uno spadone con la lama che si stacca.",

    # ---------------------------------------------------------- :67048
    (67048, 'It is a whip for combat.'):
        "Una frusta da combattimento.",

    # ---------------------------------------------------------- :67116
    (67116, 'It is a sturdy sock that can be used as a blunt weapon.'):
        "Un calzino che si usa come arma contundente.",

    # ---------------------------------------------------------- :67184
    (67184, 'It is a scythe with a chain weight.'):
        "Una falce con la catena e il contrappeso.",

    # ---------------------------------------------------------- :67463
    (67463, 'It is a trident said to have destroyed three cities.'):
        "Un tridente che, si dice, distrusse tre città.",

    # ---------------------------------------------------------- :67533
    (67533, 'It is a giant katana that discharges fire blossoms.'):
        "Un grande katana che sprigiona fuoco. Ma vale da spadone.",

    # ---------------------------------------------------------- :69329
    (69329, 'It is a bone scythe of the stars.'):
        "Una falce d'ossa che porta dentro la luce delle stelle.",

    # ---------------------------------------------------------- :70270
    (70270, 'It is a staff that holds dark wisdom.'):
        "Un bastone che cela la sapienza delle tenebre.",

    # ---------------------------------------------------------- :70890
    (70890, 'It is a hatchet that generates a gravity sphere.'):
        "Un'accetta che leva sfere di gravità.",

    # ---------------------------------------------------------- :70961
    (70961, 'It is a longstaff that improves agility.'):
        "Un bastone lungo che rende più svelti.",

    # ---------------------------------------------------------- :71779
    (71779, 'It is a lightsaber that emits moonlight.'):
        "Una spada laser che manda la luce della luna.",

    # ---------------------------------------------------------- :73093
    (73093, "It is a knight's lance, clothed in a torrent of chaos."):
        "Una lancia da cavaliere avvolta in un fiume di caos.",

    # ---------------------------------------------------------- :73425
    (73425, 'It is a burning greatsword.'):
        "Uno spadone rovente.",

    # ---------------------------------------------------------- :73495
    (73495, 'It is a very hard green onion. Can be used as a staff.'):
        "Un porro durissimo. Si usa come bastone lungo.",

    # ---------------------------------------------------------- :73634
    (73634, 'It is a staff that amplifies magic in exchange for your body functions.'):
        "Un bastone che rinforza la magia a spese degli attributi base.",

    # ---------------------------------------------------------- :74033
    (74033, 'It is a gem of a violin that has been pegged with a giant nail.'):
        "Un violino di pregio, trafitto da un chiodo senza rimpianti.",

    # ---------------------------------------------------------- :75448
    (75448, 'It is a very thick, very heavy blunt weapon.'):
        "Uno spessore mostruoso. Un'arma contundente pesantissima.",

    # ---------------------------------------------------------- :75787
    (75787, 'It is a ninja sword with deadly venom. It is not a hood.'):
        "Un wakizashi intriso di veleno. Non è un elmo.",

    # ---------------------------------------------------------- :75920
    (75920, 'It is a godly gift that when worn, transforms into a spear shape.'):
        "Indossato, si trasforma in una lancia.",

    # ---------------------------------------------------------- :76659
    (76659, 'It is a longstaff that shines like the sun.'):
        "Un bastone lungo che brilla come il sole.",

    # ---------------------------------------------------------- :76866
    (76866, 'It is a longsword having another sword, Mourneblade, as its counterpart.'):
        "Una spada lunga che, dicono, ha per gemella Mournblade.",

    # ---------------------------------------------------------- :77008
    (77008, 'It is a very heavy longsword with a powerful will.'):
        "Una spada lunga pesantissima, con dentro una volontà enorme.",

    # ---------------------------------------------------------- :77218
    (77218, 'It is a very heavy battle-axe with mighty strength.'):
        "Un'ascia da battaglia pesantissima, con dentro una forza enorme.",

    # ---------------------------------------------------------- :77288
    (77288, 'It is a very heavy bone scythe.'):
        "Una falce d'ossa pesantissima.",

    # ---------------------------------------------------------- :77497
    (77497, 'It is a kitchen knife that has cut off many heads.'):
        "Un coltello da cucina che ha mozzato molte teste.",

    # ---------------------------------------------------------- :77709
    (77709, 'It is a pirate sword of bold design.'):
        "Una scimitarra di fattura sfrontata.",

    # ---------------------------------------------------------- :77986
    (77986, 'It is a chainsaw that could tear even God apart.'):
        "Una motosega che squarcia perfino un dio.",

    # ---------------------------------------------------------- :78055
    (78055, 'It is a mechanically-driven spear that pierces through anything.'):
        "Una lancia a motore, potente, che passa da parte a parte.",

    # ---------------------------------------------------------- :78190
    (78190, 'It is a huge greatsword that can surely kill even a dragon.'):
        "Uno spadone enorme che accoppa di sicuro anche un drago.",

    # ---------------------------------------------------------- :78860
    (78860, 'It is a shortsword mainly used for cooking.'):
        "Un pugnale che serve soprattutto a cucinare.",

    # ---------------------------------------------------------- :80289
    (80289, 'It is a shiny sword.'):
        "Una lama che risplende.",

    # ---------------------------------------------------------- :81472
    (81472, 'It is a sword that is immensely effective against dragons.'):
        "Un katana che sui draghi fa un effetto enorme.",

    # ---------------------------------------------------------- :81609
    (81609, 'It is a very heavy staff with immense magical power.'):
        "Un bastone pesantissimo, con dentro una magia enorme.",

    # ---------------------------------------------------------- :81882
    (81882, 'It is a scythe with a large curved blade.'):
        "Una lama grande e molto ricurva.",

    # ---------------------------------------------------------- :82948
    (82948, 'It is a very large and martial greatsword.'):
        "Uno spadone grandissimo e rozzo.",

    # ---------------------------------------------------------- :84585
    (84585, 'It is a big axe that can easily deliver a critical hit.'):
        "Un'ascia lunga che fa spesso colpi critici.",

    # ---------------------------------------------------------- :85645
    (85645, 'It is a large hammer bestowed by the God of Earth.'):
        "Un martello donato dal dio della terra.",

    # ---------------------------------------------------------- :85717
    (85717, 'It is a dagger bestowed by the Goddess of Fortune.'):
        "Un pugnale donato dalla dea della fortuna.",

    # ---------------------------------------------------------- :85788
    (85788, 'It is a spear bestowed by the Goddess of Healing.'):
        "Una lancia donata dalla dea della guarigione.",

    # ---------------------------------------------------------- :85860
    (85860, 'It is a staff bestowed by the God of Element.'):
        "Un bastone donato dal dio degli elementi.",

    # ---------------------------------------------------------- :85930
    (85930, 'It is a scythe bestowed by the God of Harvest.'):
        "Una falce donata dal dio del raccolto.",

    # ---------------------------------------------------------- :107255
    (107255, 'It is a hooked spear with netherworldly power.'):
        "Un'alabarda con dentro la forza dell'oltretomba.",

    # ---------------------------------------------------------- :107327
    (107327, "It is a staff that disintegrates the opponent's psyche."):
        "Un bastone che manda in pezzi la mente del nemico.",

    # ---------------------------------------------------------- :107463
    (107463, "It is a blunt weapon that drains the opponent's mana."):
        "Un randello che succhia il mana del nemico.",

    # ---------------------------------------------------------- :113389
    (113389, 'It is a shortsword used by a special group of people.'):
        "Un pugnale in uso a un gruppo particolare.",

    # ---------------------------------------------------------- :115524
    (115524, 'It is a polearm with various way of attacking.'):
        "Una lancia che si usa in più modi.",

    # ---------------------------------------------------------- :115592
    (115592, 'It is a single-bladed axe with a longer pole.'):
        "Un'ascia con la lama larga.",

    # ---------------------------------------------------------- :115723
    (115723, 'It is a heavier-than-usual longsword.'):
        "Una spada che si sente pesante.",

    # ---------------------------------------------------------- :115944
    (115944, 'It is a long and thin staff.'):
        "Un bastone lungo e sottile.",

    # ---------------------------------------------------------- :116013
    (116013, 'It is a polearm with three separate tips.'):
        "Una lancia con la punta divisa in tre.",

    # ---------------------------------------------------------- :116081
    (116081, 'It is a very heavy blunt weapon.'):
        "Un martello che si sente pesante.",

    # ---------------------------------------------------------- :116149
    (116149, 'It is a large double-bladed battle axe.'):
        "Un'ascia lavorata per il combattimento.",

    # ---------------------------------------------------------- :116218
    (116218, 'It is a curved shortsword.'):
        "Un pugnale con la lama ricurva.",

    # ---------------------------------------------------------- :116285
    (116285, 'It is an unique curved longsword from a foreign land.'):
        "Una spada sottile venuta da un paese straniero.",

    # ---------------------------------------------------------- :116985
    (116985, 'It is a polearm with a sharp point.'):
        "Una lancia lunga e sottile.",

    # ---------------------------------------------------------- :117054
    (117054, 'It is a staff used to assist with magic.'):
        "Un bastone che dà una mano alla magia.",

    # ---------------------------------------------------------- :117122
    (117122, "It is a farmer's tool for harvesting crops."):
        "Un attrezzo da contadino.",

    # ---------------------------------------------------------- :117463
    (117463, 'It is a dagger with the power of wind and lightning.'):
        "Un pugnale con dentro la forza del tuono.",

    # ---------------------------------------------------------- :126224
    (126224, 'It is a longsword said to bring the end of the world.'):
        "Una spada lunga che, dicono, chiama la fine del mondo.",

    # ---------------------------------------------------------- :126852
    (126852, 'It is a longsword having another, Storm Bringer, as its counterpart.'):
        "Una spada lunga che, dicono, ha per gemella Stormbringer.",

    # ---------------------------------------------------------- :126921
    (126921, "It is a scythe that drains the opponent's mana."):
        "Una falce che succhia il mana del nemico.",

    # ---------------------------------------------------------- :127352
    (127352, 'It is the sword rumored to cut through anything.'):
        "Una spada lunga che, dicono, passa qualunque cosa.",

    # ---------------------------------------------------------- :127424
    (127424, 'It is the longsword that stops time.'):
        "Una spada lunga che ferma il tempo.",

    # ---------------------------------------------------------- :130980
    (130980, 'It is a simple but effective blunt weapon.'):
        "Un bastone ricavato scavando il materiale.",

    # ---------------------------------------------------------- :131048
    (131048, 'It is a smaller, single-bladed axe.'):
        "Un'ascia piccola.",

    # ---------------------------------------------------------- :131117
    (131117, 'It is a shortsword.'):
        "Una spada piccola.",

    # ---------------------------------------------------------- :131185
    (131185, 'It is a double-edged longsword.'):
        "Una spada dalla lama sottile.",

# 105 voci, 0 ambigue
}
