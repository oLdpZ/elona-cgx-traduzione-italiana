import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

# Le due schede della colonna, riscritte in diciassette righe (una per ogni
# tipo di filtro): stessa firma, stessa resa, e il tetto e' il `sdim` di :3543.
_SCHEDE = {}
for _r in (3544, 3552, 3557, 3562, 3567, 3572, 3577, 3582, 3587,
           3592, 3597, 3602, 3607, 3612, 3617, 3622, 3627, 3632):
    _SCHEDE[(_r, 'List')] = 'Elenco'
    _SCHEDE[(_r, 'Deck')] = 'Mazzo'

RESE = {
    # --- :2781-:2828 i bottoni di fine partita e il saluto d'uscita.
    (2781, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    # ⚠️ Vinci: e' l'AVVERSARIO che ci finisce.
    (2786, 'To the Amur-cage you go!'):
        'Dritto nella gabbia di Amur!',
    # ⚠️ Perdi. Urlo: identico nelle due lingue.
    (2791, 'Noooooooooooooo!'):
        'Noooooooooooooo!',
    (2801, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2828, 'Game Over! Press Enter to leave.'):
        'Partita finita! Premi Invio per uscire.',

    # --- :3366 la riga d'aiuto in fondo all'editor. ⭐ «F8 [File]» e non
    #     «[Spec]»: il tasto apre il menu d'importazione (:3942).
    (3366, ',[Filter] , [Type]  [Sort]  [Info] Enter [Select] Cancel [Exit] F8 [Spec]'):
        '"" + key_next + "," + key_prev + "[Filtro] " + key_fire + "," + key_get'
        ' + " [Tipo] " + key_search + " [Ordine] " + key_charainfo'
        ' + " [Info] Invio [Scegli] Esc [Esci] F8 [File]"',

    # --- :3970-:3971 il menu del tasto di azzeramento. 200px -> 20 caratteri.
    (3970, 'Reset Your Deck'):
        'Azzera il mazzo',
    (3971, 'Cancel'):
        'Annulla',

    # --- :4059-:4077 le quattro regole sulle copie.
    # ⚠️ «copy» al singolare con un numero davanti e' un refuso di monte, e
    #    l'italiano mette il plurale. Vedi il docstring anche per il «2».
    (4059, 'You can only put 1 copy of the same Legendary Card in your deck.'):
        'Di una stessa carta leggendaria puoi metterne una sola nel mazzo.',
    (4065, 'You can only put 2 copy of the same Neutral Card in your deck.'):
        'Di una stessa carta neutrale puoi metterne solo due nel mazzo.',
    (4071, 'You can only put 4 copy of the same Card in your deck.'):
        'Di una stessa carta puoi metterne solo quattro nel mazzo.',
    (4077, 'You can only put 13 copy of the same suit Card in your deck.'):
        'Di uno stesso seme puoi mettere solo tredici carte nel mazzo.',

    # --- :4116-:4117 l'uscita dall'editor. 240px -> 25 caratteri.
    (4116, 'Save & Exit'):
        'Salva ed esci',
    (4117, 'Just Exit'):
        'Esci senza salvare',

    # --- :4193 la stessa firma di :1173, gia' resa nel lotto 001.
    (4193, 'Choose Randomly.'):
        'Scegli a caso.',

    # --- :4283-:4310 le azioni possibili sulla carta sotto il cursore.
    # ⚠️ Il `\n` in coda e' del sito: le righe si impilano.
    (4283, 'UP: Put the card.\\n'):
        'SU: gioca la carta.\\n',
    (4289, 'Down: Sacrifice the card.\\n'):
        'GIÙ: sacrifica la carta.\\n',
    (4298, 'UP: Declare an attack.\\n'):
        'SU: dichiara un attacco.\\n',
    (4305, 'UP: Block.\\n'):
        'SU: blocca.\\n',
    (4310, 'ENTER: Use the skill.\\n'):
        "INVIO: usa l'abilità.\\n",
    (4323, 'There is no action available.'):
        'Non ci sono azioni possibili.',

    # --- :4423-:4433 i due menu di conferma. 200px -> 20 caratteri.
    (4423, 'End Turn'):
        'Chiudi il turno',
    (4424, 'No'):
        'No',
    # ⭐ «Arrenditi» e' gia' la resa della barra in fondo al tavolo (:1095).
    (4432, 'Surrender'):
        'Arrenditi',
    (4433, 'No'):
        'No',

    # --- :4541-:4574 il menu dei file del mazzo.
    (4541, '[Deck] What do you want to do?'):
        '[Mazzo] Che cosa vuoi fare?',
    # ⭐ gia' resa a command.hsp:17552, stesso giapponese.
    (4553, 'Enter file name.'):
        'Con che nome salvare?',
    (4574, 'Choose the Deck file.'):
        'Da che file costruire il mazzo?',
}

RESE.update(_SCHEDE)
