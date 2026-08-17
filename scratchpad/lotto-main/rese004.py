import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2625 il carico. «zaino» e' la parola gia' fissata (ai.hsp:1100,
    # command.hsp:12929, item_func.hsp:587).
    (2625, 'Your backpack is squashing you!'):
        'Lo zaino ti sta schiacciando!',
    # Stesso giapponese e stesso inglese di chara_func.hsp:1380: si ricopia.
    (2641, 'Time starts to run again.'):
        'Il tempo riprende a scorrere.',

    # --- :3024-:3031 l'arena degli alleati. Gli asterischi sono il cartello,
    # e restano: sono la forma di altre 137 rese del progetto.
    (3024, '*Loss on points*'):
        '*Sconfitta ai punti*',
    (3031, 'Do you want to give up the game?'):
        "Vuoi abbandonare l'incontro?",

    (3089, 'You change your equipment.'):
        'Hai cambiato equipaggiamento.',

    # --- :3130 ⚠️ `_s3` e' morfologia inglese e va tolta; senza, «da 1 ore»
    # sarebbe sbagliato e aggiungere una funzione italiana e' vietato dalla
    # rete 11. Il numero va dietro i due punti, dove il plurale non si pone.
    # ⚠️ Lo spazio finale c'e' anche nell'inglese e serve a chi concatena.
    (3130, 'You have been playing ElonaPlus for  hour. '):
        '"Ore di gioco su ElonaPlus: " + hour_played + ". "',
    # Stesso giapponese di otto rese in cinque file: si ricopia la formula.
    (3147, 'You have learned new ability, .'):
        '"Hai imparato una nuova capacità: " '
        '+ skillname(SKILL_SPACT_CLEMENTIA) + "."',

    # --- :3343-:3347 la raccolta automatica. Il nome per esteso e' quello del
    # menu che la accende (action.hsp:1067).
    (3343, 'Autopickup is now disabled.'):
        'La raccolta automatica è disattivata.',
    (3347, 'Autopickup is now enabled.'):
        'La raccolta automatica è attivata.',

    (3924, 'Hit ? key to display help.'):
        "Premi ? per vedere l'elenco dei comandi.",

    # --- :3937-:3964 lo scherzo dell'uscita, da leggere in fila: il gioco
    # reagisce mentre si digita, e alla fine evoca dieci chiocciole.
    (3937, 'What...'):
        'Come...',
    (3946, 'No... no...'):
        'Non dirai sul serio...',
    (3964, 'Ahhhhh!!'):
        'Aaaaahh!!',

    # --- :3986-:3999 la fine di Lesimas.
    (3986, 'Unbelievable! You conquered Lesimas!'):
        'Incredibile! Hai conquistato Lesimas!',
    (3999, 'From the pedestal, you can hear a voice.'):
        'Dal piedistallo si sente una voce.',
}
