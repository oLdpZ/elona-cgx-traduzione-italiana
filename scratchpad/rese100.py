import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ------------------------------------------------------------ i messaggi
    # :61 il modello non c'e' e il gioco propone di crearlo. Il nome del file
    # nel salvataggio resta `autopick.txt`: la toppa cambia solo quello di
    # `data\`, che e' il modello da cui si copia.
    (61, "There's no autopick.txt for this save. Create one?"):
        "Per questo salvataggio non c'è un autopick.txt. Crearlo?",
    # :76 «raccolta automatica» e' il nome che la voce ha a schermo
    # (`action.hsp:1067`, `main.hsp:3343`, `screen.hsp:1004`).
    (76, 'Which autopickup file do you want to load?'):
        'Quale file di raccolta automatica vuoi caricare?',
    (90, 'Reloaded autopick.txt.'):
        'autopick.txt ricaricato.',
    (93, 'Reloaded autopick_.txt.'):
        '"autopick_" + rtval + ".txt ricaricato."',

    # ------------------------------------------------- i modificatori (:150-:353)
    # ⚠️ La chiave porta gli spazi attorno e vanno tenuti: `:149` fa
    # `s = " " + s + " "` apposta, perche' senza di quelli `instr` aggancerebbe
    # la parola in mezzo a un'altra.
    (150, ' all '): ' ogni ',
    (152, ' all '): ' ogni ',
    (153, ' all '): ' ogni ',
    # i tre gradini dell'identificazione: invariabili, e paralleli fra loro
    (155, ' unknown '): ' senza nome ',
    (159, ' unknown '): ' senza nome ',
    (162, ' name identified '): ' con nome noto ',
    (166, ' name identified '): ' con nome noto ',
    (169, ' quality identified '): ' con pregio noto ',
    (173, ' quality identified '): ' con pregio noto ',
    (176, ' fully identified '): ' del tutto noto ',
    (180, ' fully identified '): ' del tutto noto ',
    # ⚠️ « senza valore » e' la coda che `db_item.hsp:149970` da' gia' al
    # lingotto falso: «lingotto d'oro falso e senza valore».
    (183, ' worthless '): ' senza valore ',
    (187, ' worthless '): ' senza valore ',
    # `rotten` vale solo sul cibo (`:191` chiede FILTER_ITEM_FOOD), e «marcio» e'
    # la parola che il gioco usa gia' (`command.hsp:2230`, «cibo marcio»).
    (190, ' rotten '): ' marcio ',
    (197, ' rotten '): ' marcio ',
    # `empty` vale sui contenitori (`:221` chiede FILTER_CONTAINER)
    (220, ' empty '): ' vuoto ',
    (227, ' empty '): ' vuoto ',
    # ⭐ le sei qualita' vengono da `_quality` (`text.hsp:106`), che e' la scala
    # che il giocatore legge nel pannello — e finiscono tutte in `-e`, cioe'
    # non si accordano. ⚠️ `good` e' l'indice 2, che a schermo dice `common`.
    (230, ' bad '): ' scadente ',
    (237, ' bad '): ' scadente ',
    (240, ' good '): ' comune ',
    (247, ' good '): ' comune ',
    (250, ' great '): ' eccellente ',
    (257, ' great '): ' eccellente ',
    (260, ' miracle '): ' eccezionale ',
    (267, ' miracle '): ' eccezionale ',
    (270, ' godly '): ' celestiale ',
    (277, ' godly '): ' celestiale ',
    (280, ' special '): ' speciale ',
    (287, ' special '): ' speciale ',
    # `precious` non e' un gradino della scala: e' ITEM_BIT_PRECIOUS
    (290, ' precious '): ' prezioso ',
    (297, ' precious '): ' prezioso ',
    # ⭐ i quattro stati sono la deroga gia' decisa in `glossario.md` per
    # `strblessed`/`strcursed`/`strdoomed`: complemento invariabile, e le stesse
    # parole che stanno **dentro il nome dell'oggetto** contro cui `:358`
    # confronta quel che resta della regola.
    (300, ' blessed '): ' con benedizione ',
    (307, ' blessed '): ' con benedizione ',
    (310, ' uncursed '): ' senza maledizione ',
    (317, ' uncursed '): ' senza maledizione ',
    (320, ' cursed '): ' con maledizione ',
    (327, ' cursed '): ' con maledizione ',
    (330, ' doomed '): ' con dannazione ',
    (337, ' doomed '): ' con dannazione ',
    (340, ' alive '): ' in vita ',
    (344, ' alive '): ' in vita ',
    # «oggetto evolutivo» sta in `glossario.md`, ma qui la chiave e' un
    # complemento per non accordarsi col genere di quel che segue.
    (347, ' evolution '): ' di evoluzione ',
    (351, ' evolution '): ' di evoluzione ',

    # ------------------------------------------------------- i tipi (:366-:555)
    # ⚠️ Chiavi **nude**, senza spazi, e nessuna si toglie da `s` quando
    # aggancia: bastano due chiavi di cui una e' dentro l'altra per rompere
    # tutt'e due. Le parole vengono dai nomi che gli oggetti hanno gia'.
    (366, 'item'): 'oggetto',
    (369, 'equipment'): 'equipaggiamento',
    # «Mischia» e «Tiro» sono i nomi delle due caselle a schermo
    # (`command.hsp:10517`, `:15309`).
    (375, 'melee weapon'): 'arma da mischia',
    (381, 'helm'): 'elmo',
    (387, 'shield'): 'scudo',
    (393, 'armor'): 'armatura',
    (399, 'boot'): 'stivali',
    (405, 'belt'): 'cintura',
    (411, 'cloak'): 'mantello',
    (417, 'glove'): 'guanti',
    (423, 'ranged weapon'): 'arma da tiro',
    (429, 'ammo'): 'dardi',
    (435, 'ring'): 'anello',
    (441, 'necklace'): 'collana',
    (447, 'potion'): 'pozione',
    (453, 'scroll'): 'pergamena',
    # ⭐ «grimorio» e «libro» non si fanno ombra, dove `spellbook` e `book` se
    # la fanno: la coppia inglese e' rotta e la nostra no, senza fare niente.
    (459, 'spellbook'): 'grimorio',
    (465, 'book'): 'libro',
    (471, 'rod'): 'bacchetta',
    # ⚠️ « commestibile » e non « cibo »: vedi il docstring, e `:549`.
    (477, 'food'): 'commestibile',
    (483, 'tool'): 'attrezzo',
    (489, 'furniture'): 'mobilio',
    (495, 'well'): 'pozzo',
    (501, 'altar'): 'altare',
    (507, 'remains'): 'resti',
    (513, 'junk'): 'cianfrusaglie',
    (519, 'gold piece'): "moneta d'oro",
    (525, 'platinum coin'): 'moneta di platino',
    (531, 'chest'): 'baule',
    (537, 'ore'): 'minerale',
    (543, 'tree'): 'albero',
    (549, "traveler's food"): 'cibo da viaggio',
    (555, 'cargo'): 'merce da commercio',

    # --------------------------------------------- le domande e i due avvisi
    # ⚠️ Il compagno fa da SOGGETTO e non da complemento: «far distruggere X a
    # Y» metterebbe la preposizione davanti a un nome proprio, e « a Erystia »
    # vuole «ad» mentre « a Kuroya » no — la rete 8 lo boccia, e ha ragione.
    (567, 'Destroy ?'):
        '"Distruggere " + itemname(cnt2) + "?"',
    (579, 'Let  destroy ?'):
        'name(cnt3) + " distrugge " + itemname(cnt2) + "?"',
    # ⚠️ Chi ha distrutto l'inglese lo butta via, e la rete 11 pretende le
    # **stesse funzioni di contenuto** dell'inglese: qui `name(cnt3)` non ci
    # puo' entrare, per quanto il giapponese ce l'abbia.
    # ⭐ «non esiste più» invece di «è stato distrutto» perche' il participio si
    # accorderebbe col genere dell'oggetto: e' la resa gemella che
    # `chara_func.hsp:1294` da' gia' allo stesso inglese («March was destroyed»).
    # Lo spazio in coda e' dell'inglese e si tiene.
    (596, ' was destroyed. '):
        'itemname(cnt2) + " non esiste più. "',
    (608, 'Pick up ?'):
        '"Raccogliere " + itemname(cnt2) + "?"',
    # ⭐ gemella di `action.hsp:946`, che rende « pick up » con lo stesso
    # impianto: `name(cc) + " raccoglie " + itemname(...)`.
    (620, 'Let  pick up ?'):
        'name(cnt3) + " raccoglie " + itemname(cnt2) + "?"',
    # ⭐ gemella di `command.hsp:15853`, che ha lo stesso inglese: la resa e'
    # gia' approvata, e «[Non posare]» e' il nome della linguetta.
    (644, 'You set  as no-drop.'):
        '"Non poserai più " + itemname(cnt2) + "."',
}
