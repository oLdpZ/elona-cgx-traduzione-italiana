import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :13013-:13066 il negozio, il borseggio, il compagno occupato.
    (13013, "You can't carry it."):
        'Non si può portare via.',
    # ⚠️ «rubarlo» concorderebbe col genere dell'oggetto: niente clitico
    (13028, 'You see a  weight . Do you want to attempt to steal it?'):
        '"Vedi " + s + ", peso " + s(1) + ". Provi a rubare?"',
    # ⚠️ «occupato» concorderebbe col personaggio: «ha da fare» e' invariabile.
    #    L'helper `is(tc)` e' morfologia inglese e si toglie.
    (13066, '  busy now.'):
        '"In questo momento " + name(tc) + " ha da fare."',

    # --- :13849-:13895 i motivi per cui la lista esce vuota.
    # ⚠️ rete 8: «quanto» al posto di «di» davanti a itemname()
    (13849, "You don't have anything that matches ."):
        '"Non hai niente che valga quanto " + itemname(citrade) + "."',
    (13854, ' has nothing to steal.'):
        'name(tc) + " non ha niente da rubare."',
    (13858, "There's nothing to steal."):
        "Non c'è niente da rubare.",
    (13867, 'You have no seeds in your backpack.'):
        'Non hai semi nello zaino.',
    (13879, "There's no altar here."):
        "Qui non c'è nessun altare.",
    (13886, "You don't want to rob your ally."):
        'Non vuoi derubare un compagno.',
    # ⚠️ 「ノルマ」 e' «obiettivo» (chara_func.hsp:7247), e il glossario fissa
    #    Mages Guild -> «Gilda dei Maghi»
    (13895, 'You have no quota for Mages Guild.'):
        'Al momento non hai nessun obiettivo per la Gilda dei Maghi.',

    # --- :13924 ⭐⭐ i ventotto prompt, una riga sola.
    #     «Quale oggetto» dove l'inglese dice *which item* e il giapponese
    #     「どのアイテム」; «Che cosa» dove dicono *what* e 「何」.
    (13924, 'Examine what? '):
        'Quale oggetto vuoi esaminare? ',
    (13924, 'Drop what? '):
        'Quale oggetto vuoi posare? ',
    (13924, 'Which item do you want to pick up? '):
        'Quale oggetto vuoi raccogliere? ',
    # ⚠️ l'unica delle ventotto senza spazio in coda, in tutt'e due le lingue
    (13924, 'Equip what?'):
        'Che cosa vuoi equipaggiare?',
    (13924, 'Eat what? '):
        'Che cosa vuoi mangiare? ',
    (13924, 'Read what? '):
        'Che cosa vuoi leggere? ',
    (13924, 'Drink what? '):
        'Che cosa vuoi bere? ',
    # ⭐ «Zap» e' «agitare»: text.hsp:135 e proc.hsp:7610
    (13924, 'Zap what? '):
        'Che cosa vuoi agitare? ',
    (13924, 'Which item do you want to give? '):
        'Quale oggetto vuoi dare? ',
    (13924, 'What do you want to buy? '):
        'Che cosa vuoi comprare? ',
    (13924, 'What do you want to sell? '):
        'Che cosa vuoi vendere? ',
    (13924, 'Which item do you want to identify? '):
        'Quale oggetto vuoi identificare? ',
    (13924, 'Use what? '):
        'Quale oggetto vuoi usare? ',
    (13924, 'Open what? '):
        'Che cosa vuoi aprire? ',
    (13924, 'Cook what? '):
        'Che cosa vuoi cucinare? ',
    (13924, 'Blend what? '):
        'Che cosa vuoi mescolare? ',
    # ⚠️ rete 8: `valn` e' itemname(citrade), quindi «l'effetto di valn» e'
    #    vietato. Il nome esce dalla frase e va in parentesi, come nel giapponese
    (13924, 'Which item do you want to apply the effect of ? '):
        '"Su quale oggetto applicare l\'effetto? (" + valn + ") "',
    (13924, 'What do you want to offer to your god? '):
        'Che cosa vuoi offrire al tuo dio? ',
    # ⚠️ 「何を交換する？」: che cosa DAI
    (13924, 'Which item do you want to trade? '):
        'Quale oggetto vuoi scambiare? ',
    # 💡 «per» non si fonde (40a): il nome puo' restare nella frase
    (13924, 'What do you offer for ? '):
        '"Che cosa offri per " + valn + "? "',
    (13924, 'Take what? '):
        'Che cosa vuoi prendere? ',
    # ⭐ «prendere di mira» e' la forma del lotto 001 (:858, :864, :993)
    (13924, 'Target what? '):
        'Che cosa vuoi prendere di mira? ',
    (13924, 'Put what? '):
        'Che cosa vuoi metterci dentro? ',
    (13924, 'Which item do you want to take? '):
        'Quale oggetto vuoi farti dare? ',
    (13924, 'Throw what? '):
        'Che cosa vuoi lanciare? ',
    (13924, 'Steal what? '):
        'Che cosa vuoi rubare? ',
    # ⚠️ 「何と交換する？」: con che cosa fai il CAMBIO. «scambiarlo»
    #    concorderebbe col genere dell'oggetto
    (13924, 'Trade what? '):
        'Con che cosa vuoi fare il cambio? ',
    (13924, 'Which item do you want to reserve? '):
        'Quale oggetto vuoi prenotare? ',

    # --- :13941-:13958 le tre monete alternative.
    # ⚠️ l'inglese dice «Coins», il giapponese メダル: sono le medagliette
    (13941, '(Coins: )'):
        '"(Medagliette: " + p + ")"',
    (13952, '(tickets: )'):
        '"(Biglietti: " + p + ")"',
    (13958, ' guild points are needed to gain a rank.'):
        '"Obiettivo rimasto: " + gdata(GDATA_FLAG_GUILD_MAGE_NORMA) + " PG"',

    # --- :13991-:13995 i due rifiuti.
    (13991, "The item doesn't exist."):
        "Quell'oggetto non esiste.",
    # ⚠️ «vuoto» concorda con «oggetto», che ci mette la resa: non col gioco
    (13995, 'The item is empty!'):
        "Quell'oggetto è ormai vuoto!",

    # --- :14077-:14091 i tre tasti in coda alla finestra dell'inventario.
    (14077, '[Change]'):
        '[Cambia menu]',
    (14087, '[Tag No-Drop]'):
        '[Non posare]',
    (14091, '[Multi Drop]'):
        '[Posa in serie]',

    # --- :14101-:14120 le cinque etichette di colonna.
    (14101, 'Price'):
        'Prezzo',
    (14105, 'Medal'):
        'Medagliette',
    (14108, 'ticket'):
        'Biglietti',
    (14115, 'Guild Point'):
        'Punti gilda',
    (14120, 'Name'):
        'Nome',

    # --- :14176-:14193 il piede della finestra: peso, carretto, equipaggiamento.
    (14176, '  (Weight '):
        '  (Peso ',
    # ⚠️ 荷車 e' il carretto: action.hsp:1906
    (14176, ' Cargo '):
        ' Carretto ',
    (14193, 'EquipWt:'):
        'Peso eq.:',
}
