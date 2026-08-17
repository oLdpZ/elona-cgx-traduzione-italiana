import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2007-:2097 gli effetti del terreno: acido, residuo elementale, fuoco,
    # pozza. Tutte dinamiche con name(tc): terza persona, nessun participio.
    # 「は酸に焼かれた。」 e' la stessa riga di chara_func.hsp:4754: stessa resa.
    (2007, ' melt.'):
        'name(tc) + " brucia nell\'acido."',
    (2027, ' was harmed by remnants of the elements.'):
        'name(tc) + " subisce il residuo degli elementi."',
    # 「は燃えた。」 non e' 「は燃え上がった。」 di chara_func.hsp:4614 («prende fuoco»).
    (2075, '  burnt.'):
        'name(tc) + " brucia."',
    # Il giapponese dice «e' stato investito dal liquido», e la riga dopo fa `wet`.
    (2097, ' step in the pool.'):
        'name(tc) + " si bagna nella pozza."',

    # --- :2163-:2184 i quattro cuccioli che si addormentano, uno per taglia
    # (CDATA_SPRITE_SIZE_MILK da -5 a -2). ⚠️ Niente participi: il genere di
    # cdatan(CDATAN_NAME, cc) non si conosce.
    (2163, ' fell asleep soundly...'):
        'cdatan(CDATAN_NAME, cc) + " scivola in un sonno profondo..."',
    (2169, ' suddenly fell asleep as if the battery had run out...'):
        'cdatan(CDATAN_NAME, cc) + " si spegne di colpo, come una batteria scarica..."',
    (2176, ' got tired of playing and fell asleep...'):
        'cdatan(CDATAN_NAME, cc) + " gioca fino a stancarsi e prende sonno..."',
    (2184, ' yawned and went to sleep...'):
        'cdatan(CDATAN_NAME, cc) + " sbadiglia e si addormenta piano..."',

    # --- :2219-:2228 la prima lettura della rivista: tre battute stupite.
    (2219, 'Wow... Is this really okay?'):
        'Uh... ma questa roba è lecita?',
    (2222, 'Too extreme...'):
        'Che roba spinta...',
    (2225, 'C-could this be!?'):
        'M-ma questo...!?',
    (2228, ' turn the page...'):
        'name(cc) + " gira la pagina..."',

    # --- :2236-:2242 la seconda lettura: tre battute sconcertate.
    (2236, "I don't get it!"):
        'Non ci capisco niente!',
    (2239, 'This seems like a trivial level of nudity...'):
        'Al confronto, il nudo integrale è poca cosa...',
    (2242, "What's this?"):
        'Ma che cos\'è questa roba...',

    # --- :2272-:2288 l'ubriaco che attacca briga.
    # ⚠️ «alza il gomito» e non «è ubriaco»: il genere di name(cc) non si conosce.
    (2272, ' gets the worse for drink and catches .'):
        'name(cc) + " alza il gomito e importuna " + name(tc) + "."',
    # ⚠️ Le quattro battute seguono il GIAPPONESE: l'inglese ha scambiato le due
    # di mezzo. 「一杯どうだい？」 era gia' reso in db_creature.hsp:50914.
    (2274, 'Have a drink baby.'):
        'Che ne dici di un bicchiere?',
    (2274, 'What are you looking at?'):          # jp 「飲んでないよ」
        'Ma io non ho bevuto.',
    (2274, "I ain't drunk."):                    # jp 「何見てるのさ」
        "Che cos'hai da guardare?",
    (2274, "Let's have fun."):
        'Dai, divertiamoci.',
    # 「はカチンときた。」 e' proprio «perdere la pazienza», l'esempio della guida.
    (2280, '  pretty annoyed with the drunkard.'):
        'name(tc) + " perde la pazienza."',
    # ⚠️ «Basta con» e non «Sono stufo»: chi parla e' tc, di genere ignoto.
    (2282, 'Your time is over, drunk!'):
        'Basta con gli ubriaconi!',
    (2288, "What, don't like it?"):
        "Che c'è, vuoi menare le mani?",
    (2288, "You can't drink?"):
        'Non reggi il bicchiere?',
    (2288, 'Just a prank bro.'):
        "Ecco, c'è sempre chi non capisce uno scherzo.",
    (2288, "Alright, let's fight!"):
        'Va bene, allora facciamo a botte!',

    # --- :2333 l'azione di fila interrotta. `actlistn` non porta l'articolo:
    # command.hsp:17267 scrive gia' «Interrompere " + actlistn(...) + "? "».
    (2333, ' stop .'):
        'name(cc) + " interrompe " + actlistn(cdata(CDATA_ROW_ACT, cc)) + "."',
}
