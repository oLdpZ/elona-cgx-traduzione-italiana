# -*- coding: utf-8 -*-
"""Le rese del lotto 012 (le ARMI, `FILTER_WEAPON`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 012 scratchpad/lotti-110

**105 righe del sorgente, 105 firme, 105 giapponesi distinti.** Nessuna formula,
nessuna famiglia: è la categoria meno formulaica dell'indice 3, e costa quanto
pesa. Ogni riga dice **che arma è** e **una cosa sola** su di lei.

⭐ **Il vocabolario delle armi non si inventa: sta nei NOMI degli oggetti**, che
sono già resi. 長剣 «spada lunga», 短剣 «pugnale», 大剣 «spadone», 細剣
«fioretto», 刀 «katana», 忍刀 «wakizashi», 海賊刀 «scimitarra», 大斧 «ascia
lunga», 戦斧 «ascia da battaglia», 手斧 «accetta», 投斧 «tomahawk», 鎌 «falcetto»,
大鎌 «falce», 骨鎌 «falce d'ossa», 鎖鎌 «falce a catena», 鋏鎌 «cesoie», 長槍
«lancia», 鉾槍 «alabarda», 三叉槍 «tridente», 騎士槍 «lancia da cavaliere»,
棍棒 «randello», 大槌 «martello», 戦槌 «martello da guerra», 星球槌 «mazza
ferrata», 杖 «bastone», 長棒 «bastone lungo», 錫杖 «shakujo», 節棍 «nunchaku»,
鞭 «frusta», 螺旋機 «trapano», 鎖鋸 «motosega», 包丁 «coltello da cucina»,
苦無 «kunai».

⭐ **E le cinque divinità erano già decise nello stesso file**: 大地の神 «il dio
della terra», 収穫の神 «il dio del raccolto», 元素の神 «il dio degli elementi»,
幸運の女神 «la dea della fortuna», 癒しの女神 «la dea della guarigione» — dalle
statue e dai pendoli, resi in una sessione precedente.
"""

IT = {
    # === le cinque armi donate dagli dei
    85645: "Un martello donato dal dio della terra.",
    85717: "Un pugnale donato dalla dea della fortuna.",
    85788: "Una lancia donata dalla dea della guarigione.",
    85860: "Un bastone donato dal dio degli elementi.",
    85930: "Una falce donata dal dio del raccolto.",

    # === le tre spade gemelle, e le altre spade lunghe leggendarie
    51782: "Una spada lunga che, dicono, ha una spada gemella.",
    76866: "Una spada lunga che, dicono, ha per gemella Mournblade.",
    126852: "Una spada lunga che, dicono, ha per gemella Stormbringer.",
    126224: "Una spada lunga che, dicono, chiama la fine del mondo.",
    127352: "Una spada lunga che, dicono, passa qualunque cosa.",
    127424: "Una spada lunga che ferma il tempo.",
    77008: "Una spada lunga pesantissima, con dentro una volontà enorme.",
    63726: "Una spada lunga tutta bianca.",

    # === le spade e le lame
    53911: "Una spada leggerissima e sottile.",
    115723: "Una spada che si sente pesante.",
    116285: "Una spada sottile venuta da un paese straniero.",
    131117: "Una spada piccola.",
    131185: "Una spada dalla lama sottile.",
    80289: "Una lama che risplende.",
    81882: "Una lama grande e molto ricurva.",
    52930: "Un fioretto che comanda l'elettricità.",
    51920: "Una lancetta lunga che si usa come spada lunga.",
    52720: "Un budino di mandorle a forma di spada laser. Vale da spada lunga.",
    71779: "Una spada laser che manda la luce della luna.",

    # === gli spadoni
    66913: "Uno spadone con la lama che si stacca.",
    73425: "Uno spadone rovente.",
    78190: "Uno spadone enorme che accoppa di sicuro anche un drago.",
    82948: "Uno spadone grandissimo e rozzo.",
    67533: "Un grande katana che sprigiona fuoco. Ma vale da spadone.",

    # === i katana e le lame d'oriente
    81472: "Un katana che sui draghi fa un effetto enorme.",
    75787: "Un wakizashi intriso di veleno. Non è un elmo.",
    77709: "Una scimitarra di fattura sfrontata.",

    # === i pugnali
    53843: "Un pugnale da ninja, buono anche da lanciare.",
    78860: "Un pugnale che serve soprattutto a cucinare.",
    113389: "Un pugnale in uso a un gruppo particolare.",
    116218: "Un pugnale con la lama ricurva.",
    117463: "Un pugnale con dentro la forza del tuono.",
    66843: "Un pugnale che suona. Volendo, vale da strumento.",
    52860: "Un gruppo di cinque kunai.",
    77497: "Un coltello da cucina che ha mozzato molte teste.",

    # === le asce
    43561: "Un'ascia da battaglia che pare fatta d'osso.",
    60198: "Un'ascia da battaglia azzurra e leggera.",
    77218: "Un'ascia da battaglia pesantissima, con dentro una forza enorme.",
    116149: "Un'ascia lavorata per il combattimento.",
    115592: "Un'ascia con la lama larga.",
    84585: "Un'ascia lunga che fa spesso colpi critici.",
    131048: "Un'ascia piccola.",
    54115: "Un'ascia piccola, buona anche da lanciare.",
    53070: "Un tomahawk lungo e a doppia lama.",
    70890: "Un'accetta che leva sfere di gravità.",
    54183: "Una sega a motore. Si usa come un'ascia.",
    77986: "Una motosega che squarcia perfino un dio.",

    # === le falci
    54251: "Una falce con più lame.",
    54319: "Una falce fatta d'ossa.",
    60789: "Una falce malvagia. Si può usare.",
    67184: "Una falce con la catena e il contrappeso.",
    61796: "Una falce a catena che leva vortici.",
    69329: "Una falce d'ossa che porta dentro la luce delle stelle.",
    77288: "Una falce d'ossa pesantissima.",
    126921: "Una falce che succhia il mana del nemico.",
    117122: "Un attrezzo da contadino.",
    52790: "Un paio di cesoie che paiono chele di granchio.",
    53140: "Un paio di cesoie come il becco di un uccello.",

    # === le lance
    51852: "Una lancia fatta di bambù.",
    53978: "Una lancia con la lama che gira a spirale.",
    54045: "Una lancia a cono, lunga e sottile.",
    73093: "Una lancia da cavaliere avvolta in un fiume di caos.",
    78055: "Una lancia a motore, potente, che passa da parte a parte.",
    115524: "Una lancia che si usa in più modi.",
    116013: "Una lancia con la punta divisa in tre.",
    116985: "Una lancia lunga e sottile.",
    107255: "Un'alabarda con dentro la forza dell'oltretomba.",
    64488: "Una pala buona a tutto, anche da alabarda.",
    67463: "Un tridente che, si dice, distrusse tre città.",
    75920: "Indossato, si trasforma in una lancia.",

    # === i contundenti
    54387: "Un'arma contundente con le punte sporgenti ai lati.",
    54456: "Un'arma contundente con una palla di ferro.",
    75448: "Uno spessore mostruoso. Un'arma contundente pesantissima.",
    116081: "Un martello che si sente pesante.",
    61251: "Un martello da guerra travestito da bastone.",
    56811: "Una mazza ferrata che stava in coda a un dinosauro.",
    65136: "Un randello enorme e pieno di nodi.",
    107463: "Un randello che succhia il mana del nemico.",
    130980: "Un bastone ricavato scavando il materiale.",
    67116: "Un calzino che si usa come arma contundente.",
    53421: "Un calzino del tipo che chiamano tabi.",

    # === i bastoni
    54524: "Un bastone con un anello in cima.",
    117054: "Un bastone che dà una mano alla magia.",
    115944: "Un bastone lungo e sottile.",
    70961: "Un bastone lungo che rende più svelti.",
    76659: "Un bastone lungo che brilla come il sole.",
    70270: "Un bastone che cela la sapienza delle tenebre.",
    63457: "Un bastone che muta gli MP in forza d'attacco.",
    73634: "Un bastone che rinforza la magia a spese degli attributi base.",
    81609: "Un bastone pesantissimo, con dentro una magia enorme.",
    107327: "Un bastone che manda in pezzi la mente del nemico.",
    53209: "Uno shakujo fatto con tecnologia avanzata.",
    54594: "Un bastone che si divide e si gira in fretta.",
    53281: "Un bastone a tre sezioni: tre in uno.",
    73495: "Un porro durissimo. Si usa come bastone lungo.",

    # === le fruste
    65268: "Una frusta sporca di sangue.",
    65882: "Una frusta con le spine avvelenate.",
    67048: "Una frusta da combattimento.",

    # === il resto
    52999: "Un trapano gigantesco che rimbomba fino al cielo.",
    74033: "Un violino di pregio, trafitto da un chiodo senza rimpianti.",
}
