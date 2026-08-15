import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6577-:6589 il gioco di carte.
    # ⚠️ «sei sicuro?» concorderebbe col giocatore; lo spazio in coda e' dell'inglese
    (6577, 'They had a lot more health than you, you will be put into great disadvantage, are you sure about this? '):
        'Ha molto più vigore di te: sei in netto svantaggio. Vuoi continuare? ',
    # ⭐ copiata parola per parola da action.hsp:19128, stesso jp e stesso en
    (6589, 'You put away the deck.'):
        'Hai riposto il mazzo.',

    # --- :6608-:6613 i due rifiuti del ranch.
    # ⚠️ «appeso» concorderebbe con la bestia: si toglie il participio
    (6608, 'You cannot leave livestock on hanging.'):
        'Finché sta al gancio non si può portare fuori.',
    # ⭐ la famiglia sta in tre file (action.hsp:11036, adv.hsp:4, proc.hsp:19056):
    #    cambia solo la coda, e qui e' «portarne fuori»
    (6613, "Your party is already full. You can't invite someone anymore."):
        'Hai già il massimo di compagni: non puoi portarne fuori altri.',

    # --- :6631 la frase da insegnare. ⚠️ `name(tc)` ce l'ha l'inglese, non il
    #     giapponese: la rete 11 pretende quella dell'inglese.
    # ⚠️ rete 8: «a » + name() darebbe «a il putit». Il nome passa a soggetto.
    (6631, 'What sentence should  learn? '):
        'name(tc) + ": che frase deve imparare? "',

    # --- :6651-:6655 quando lo fai tacere e quando lo lasci parlare.
    (6651, ' stops talking...'):
        'name(tc) + " si azzittisce..."',
    (6655, ' hugs you.'):
        'name(tc) + " ti abbraccia."',

    # --- :6667-:6676 le quattro reazioni a «Metti fra gli indispensabili»,
    #     una per grado d'affetto. ⚠️ `his(tc)` e' morfologia e sparisce.
    (6667, ' puffs out  chest with pride.'):
        'name(tc) + " gonfia il petto con orgoglio."',
    # ⚠️ «imbarazzato» concorderebbe: l'accordo cade su «aria» (la 41a)
    (6670, ' looks a little embarrassed.'):
        'name(tc) + " ha un\'aria imbarazzata."',
    (6673, ' looks surprised.'):
        'name(tc) + " ha un\'aria sorpresa."',
    (6676, ' clicks  tongue disapprovingly.'):
        'name(tc) + " schiocca la lingua con disgusto."',

    # --- :6683-:6692 le quattro reazioni a «Togli dagli indispensabili», sulle
    #     stesse quattro soglie e in ordine rovesciato di gradimento.
    (6683, ' looks depressed...'):
        'name(tc) + " ha un\'aria disperata..."',
    (6686, ' appears to be lost in thought...'):
        'name(tc) + " si perde nei propri pensieri..."',
    (6689, ' looks scared...'):
        'name(tc) + " ha paura..."',
    (6692, ' spits on the ground...'):
        'name(tc) + " sputa per terra..."',

    # --- :6703-:6714 i tre ordini. ⚠️ rete 8: «a » + name() darebbe «a il
    #     putit», quindi nei primi due il nome passa a SOGGETTO.
    (6703, 'You instructed  to not pick up items off the ground.'):
        'name(tc) + " ha l\'ordine di non raccogliere gli oggetti per terra."',
    (6707, 'You instructed  to do as they like with items on the ground.'):
        'name(tc) + " può fare come vuole con gli oggetti per terra."',
    # ⭐ la forma viene da proc.hsp:19030, che dice la stessa cosa altrove
    (6714, 'You order  to wait in town.'):
        '"Hai lasciato " + name(tc) + " ad aspettare in città."',
    # ⭐ copiata parola per parola da proc.hsp:10749
    (6718, "There's no place to get off."):
        "Non c'è spazio per scendere.",

    # --- :6762 il sacco da botte, che il menu slega con «Slega» (:6110).
    (6762, 'You release .'):
        '"Hai slegato " + name(tc) + "."',

    # --- :6770 la trasformazione.
    (6770, 'Which rank?'):
        'Quale rango?',
}
