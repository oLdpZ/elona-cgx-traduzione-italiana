# -*- coding: utf-8 -*-
"""110a - Lotto 012 di `db_item.hsp`: il rapporto delle ARMI.

`FILTER_WEAPON`, `description(3)`: **105 righe del sorgente, 105 firme, 105
giapponesi distinti**. Zero doppioni, zero famiglie, zero formule: e' la
categoria **meno** formulaica dell'indice 3, e l'unica dove il numero delle
righe e quello delle rese coincidono.

### ⓘ Che cos'e' un rapporto quando non c'e' una formula

Le altre categorie hanno una frase che si ripete e un fatto che cambia. Qui il
giapponese scrive, per ognuna delle 105, **che arma e'** e **una cosa sola** su
di lei — una forma, un materiale, un potere, una storia. E' un referto lo
stesso: la struttura c'e', ma sta nella **sintassi**, non nel lessico.

    〈una cosa sola〉 + 〈il tipo d'arma〉だ。

L'italiano tiene lo stesso ordine rovesciato che ha sempre — «Un'ascia da
battaglia che pare fatta d'osso» — e ogni riga sta in una frase.

### ⭐⭐ IL VOCABOLARIO DELLE ARMI NON SI E' DOVUTO INVENTARE

Trentatre parole di tipo d'arma, e c'erano **tutte** nei nomi degli oggetti,
resi in sessioni precedenti. La ricerca e' costata un comando; inventarle
avrebbe prodotto un rapporto che chiama «spadone» quel che il nome chiama
«spada lunga»:

    長剣 spada lunga · 短剣 pugnale · 大剣 spadone · 細剣 fioretto · 刀 katana
    忍刀 wakizashi · 海賊刀 scimitarra · 大斧 ascia lunga · 戦斧 ascia da
    battaglia · 手斧 accetta · 投斧 tomahawk · 鎌 falcetto · 大鎌 falce ·
    骨鎌 falce d'ossa · 鎖鎌 falce a catena · 鋏鎌 cesoie · 長槍 lancia ·
    鉾槍 alabarda · 三叉槍 tridente · 騎士槍 lancia da cavaliere · 棍棒 randello
    大槌 martello · 戦槌 martello da guerra · 星球槌 mazza ferrata · 杖 bastone
    長棒 bastone lungo · 錫杖 shakujo · 節棍 nunchaku · 鞭 frusta ·
    螺旋機 trapano · 鎖鋸 motosega · 包丁 coltello da cucina · 苦無 kunai

⚠️ **E il tipo d'arma va letto nel giapponese, non nel nome.** `:52720` e'
un budino di mandorle a forma di spada laser, e il giapponese dice
「長剣として装備可能」: si impugna come **spada lunga**. `:67533` e' un
大太刀 e il giapponese si prende la briga di avvertire che
「刀だが大剣に属する」 — *e' un katana, ma sta fra gli spadoni*. Due righe dove
la categoria di gioco e la forma dell'oggetto non coincidono, e il giapponese lo
dice apposta.

### ⭐ LE CINQUE ARMI DEGLI DEI, e le divinita' erano gia' decise

`:85645`, `:85717`, `:85788`, `:85860`, `:85930`:
「〜の神から下賜される〜だ。」 — il martello, il pugnale, la lancia, il bastone
e la falce che le cinque divinita' concedono. I nomi delle divinita' stanno
**nello stesso file**, dalle statue e dai pendoli resi prima:

    大地の神     -> il dio della terra        (「大地の神を模したペンデュラム」)
    収穫の神     -> il dio del raccolto       (「収穫の神のぬいぐるみ」)
    元素の神     -> il dio degli elementi     (「元素の神を模した胸像」)
    幸運の女神   -> la dea della fortuna      (「幸運の女神を描いた絵」)
    癒しの女神   -> la dea della guarigione   (「癒しの女神を模った彫像」)

⚠️ **Non sono gli epiteti.** Il dizionario ha anche «Jure della Cura»,
«Ehekatl della Sorte», «Kumiromi della Messe»: quelli sono **nomi**, e si usano
dove il giapponese scrive il nome. Qui il giapponese scrive la **perifrasi**
(癒しの女神, *la dea che guarisce*), e la perifrasi ha gia' la sua resa in
questo stesso file. Confondere le due avrebbe fatto dire alla scheda «donata da
Jure della Cura» dove il giapponese non nomina Jure.

### ⓘ Tre righe dove l'inglese aggiunge e il giapponese no

- `:53911`, la spada leggerissima: l'inglese aggiunge «with electric
  properties», il giapponese dice solo 「非常に軽くて細い剣だ。」;
- `:66843`, il pugnale che suona: l'inglese precisa «Rank 0-6 instrument», il
  giapponese dice 「一応、楽器としても使える」 — *volendo, vale anche da
  strumento*. E' il **rango taciuto** della 109a e del lotto 011, per la terza
  volta;
- `:117463`, il pugnale del tuono: l'inglese dice «wind and lightning», il
  giapponese solo 雷.

### ⓘ I termini, verificati nel dizionario

クリティカル → «colpi critici» (`buff.hsp`, «Ottiene più colpi critici») ·
主能力 → «attributi base» (109ª) · マナ → «mana» (`invariati.md`) ·
地獄 → «oltretomba» · 混沌 → «caos» · `MP` invariato.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-012.jsonl'
RIGHE = {
    43561, 51782, 51852, 51920, 52720, 52790, 52860, 52930, 52999, 53070,
    53140, 53209, 53281, 53421, 53843, 53911, 53978, 54045, 54115, 54183,
    54251, 54319, 54387, 54456, 54524, 54594, 56811, 60198, 60789, 61251,
    61796, 63457, 63726, 64488, 65136, 65268, 65882, 66843, 66913, 67048,
    67116, 67184, 67463, 67533, 69329, 70270, 70890, 70961, 71779, 73093,
    73425, 73495, 73634, 74033, 75448, 75787, 75920, 76659, 76866, 77008,
    77218, 77288, 77497, 77709, 77986, 78055, 78190, 78860, 80289, 81472,
    81609, 81882, 82948, 84585, 85645, 85717, 85788, 85860, 85930, 107255,
    107327, 107463, 113389, 115524, 115592, 115723, 115944, 116013, 116081, 116149,
    116218, 116285, 116985, 117054, 117122, 117463, 126224, 126852, 126921, 127352,
    127424, 130980, 131048, 131117, 131185,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
