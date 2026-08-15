import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15508-:15562 le tasse e la sfida delle tasse doppie.
    # ⭐ rete 3: proc.hsp:15584 ha già lo stesso giapponese.
    (15508, "You don't have enough money."): 'Non hai abbastanza denaro...',
    (15524, "You don't have to pay your tax yet."):
        'Non è ancora ora di pagare le tasse.',
    (15549, 'You pay .'): '"Hai pagato " + itemname(ci) + "."',
    # il nome della sfida, che compare sulla schermata del traguardo
    (15560, 'Double Tax Each Month'): 'Tasse doppie ogni mese',
    (15562, 'Unbelievable! You paid your taxes for  month!'):
        '"Incredibile! Hai pagato le tasse per " '
        '+ (TweakData(TWEAK_CHALLENGE_DOUBLE_TAX_EACH_MONTH, TWEAK_CATEGORY_CHALLENGE) - 1) '
        '+ " mesi!"',

    # --- :15564-:15569 il coro del traguardo. ⭐ tutte e sei da text.hsp:477-:492,
    #     dove la stessa lista serve a OGNI traguardo del gioco.
    (15564, 'Finally!'): 'Finalmente!',
    (15565, 'Just the natural outcome.'): 'Era il risultato naturale.',
    (15566, 'Woooooo!'): 'Uooooooh!',
    (15567, 'Heh.'): 'Hmpf.',
    (15568, "I can't sleep tonight."): 'Stanotte non chiudo occhio.',
    (15569, "You're kidding."): 'Stai scherzando.',

    # --- :15615 l'alleato che non ridà il minerale.
    #     ⚠️ solo lo slot 2 è raggiungibile: f vale 0 o 2 (:15610, :15612).
    #        Gli altri tre si traducono lo stesso. Vedi il docstring.
    (15615, 'No!'): 'Non voglio!',
    (15615, "It's mine."): 'Non si tocca!',
    (15615, 'Get off!'): 'Giù le mani!',
    # ⭐ rete 3: 「イヤ！」 è già «Mai!» a :15196, lotto 024.
    (15615, 'Never.'): 'Mai!',

    # --- :15623-:15627 l'equipaggiamento che non si toglie.
    # ⚠️ «maledetto» accorderebbe col genere dell'oggetto; «non si può togliere»
    #    è impersonale e vale per la spada come per lo scudo.
    (15623, " is cursed and can't be taken off."):
        'itemname(ci) + " porta una maledizione e non si può togliere."',
    # ⚠️ il giapponese nomina tc, l'inglese no, e la voce è STATICA: la resa non
    #    può nominare nessuno. «Plagio» è il termine di buff.hsp:1362.
    (15627, 'It is impossible to change the equipment by confusing.'):
        'Sotto plagio non si cambia equipaggiamento!',

    # --- :15636 e :15645 lo stesso inglese per due scene diverse.
    #     ⭐ il giapponese le distingue e la rete 11 lo permette: name + itemname
    #        in tutt'e due. Vedi il docstring.
    (15636, ' swallows  angrily.'):
        'name(tc) + " va su tutte le furie e ingoia " + itemname(ci, 1) + "."',
    (15645, ' swallows  angrily.'):
        'name(tc) + " si ficca in bocca " + itemname(ci, 1) + " in fretta e, '
        'masticando, risponde che non ha nessun oggetto del genere."',

    # --- :15659-:15762 prendere, lanciare, le medagliette e i biglietti.
    (15659, 'You take .'): '"Hai preso " + itemname(ci, in) + "."',
    # 「そこには投げられない。」: qui si lancia, non si spara — action.hsp:10122 ha
    # lo stesso inglese per il tiro, e infatti dice «sparare».
    (15692, 'The location is blocked.'): 'Non si può lanciare lì.',
    # ⭐ stesso inglese di text.hsp:14 e :15
    (15708, 'Your inventory is full.'): 'Il tuo zaino è pieno.',
    # ⭐ «Medagliette» e «Biglietti» sono i termini del menu, :14105 e :14108
    (15727, "You don't have enough coins."): 'Non hai abbastanza medagliette...',
    (15734, 'You receive !'): '"Hai ricevuto " + itemname(ti, 1) + "!"',
    (15762, "You don't have enough tickets."): 'Non hai abbastanza biglietti...',

    # --- :15853-:15884 le cose da non posare e la posa in serie.
    #     ⭐ il menu dice «[Non posare]» e «[Posa in serie]» (:14087, :14091):
    #        le frasi usano lo stesso verbo, così il giocatore le riconosce.
    (15853, 'You set  as no-drop.'): '"Non poserai più " + itemname(ci) + "."',
    (15857, ' is no longer set as no-drop.'):
        'itemname(ci) + " si può posare di nuovo."',
    (15862, 'You can continuously drop items.'): 'Adesso puoi posare in serie.',
    (15884, 'Really leave these items?'):
        'Ci sono ancora oggetti: vuoi lasciarli?',

    # --- :15923 la scorciatoia. ⭐ «Carretto» da :14176, «Scorciatoia» da
    #     text.hsp:10 e :121.
    (15923, "You can't make a shortcut for cargo stuff."):
        'Le cose sul carretto non si possono assegnare a una scorciatoia.',
}
