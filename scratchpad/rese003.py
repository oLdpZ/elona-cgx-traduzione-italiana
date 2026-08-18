import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :604-:622 il campo e l'editor delle piastrelle.
    (604, 'You harvested all grown crops and fruits.'):
        'Hai raccolto tutta la frutta e le colture cresciute.',
    # 💡 «piastrelle» viene dal menu del lotto 001, «Cambia gruppo di piastrelle».
    (622, 'Left click to place the tile, right click to pick the tile under your'
          ' mouse cursor, movement keys to move current position, hit the enter'
          ' key to show the list of tiles, hit the cancel key to exit.'):
        'Clic sinistro per posare la piastrella, destro per prendere quella sotto'
        " il cursore, i tasti di movimento per spostare lo schermo, Invio per l'elenco"
        ' delle piastrelle, Esc per uscire.',

    # --- :672-:730 l'esperienza di viaggio e il nome della proprieta'.
    # 💡 Stesso giapponese di main.hsp:8475: si copia parola per parola.
    (672, 'Organize and share your accumulated  travelExp?'):
        '"Vuoi mettere in ordine e spartire i " + gdata(GDATA_TRAVEL_DISTANCE)'
        ' + " punti di esperienza di viaggio accumulati?"',
    # 💡 Stesso giapponese di main.hsp:8493.
    (687, " didn't seem to have anything to gain from the travel."):
        'name(tc) + " non sembra averci guadagnato granché."',
    # 💡 La forma «X: domanda» invece di «domanda a X» evita la preposizione
    #    davanti a un nome che porta gia' il suo articolo (contratto-nomi.md §4).
    (718, 'What do you want to call ? '):
        'mdatan(MDATAN_NAME) + ": che nome vuoi usare? "',
    # 💡 Stesso giapponese di command.hsp:7466.
    (724, 'You changed your mind.'): 'Hai cambiato idea.',

    # --- :749-:776 la finestra del valore della casa.
    (749, 'Home Value'): 'Valore della casa',
    # 💡 I tasti si abbreviano, come in command.hsp:11849 («Dx,Sx [Cambia]»).
    (749, 'Enter key,'): 'Invio,',
    (752, 'Value'): 'Valore',
    (753, 'Heirloom Rank'): 'Rango dei cimeli',
    # ⚠️ 43 px fra l'etichetta e la prima stella, con un carattere da 10: sei
    #    lettere sono il massimo prudente. Vedi il docstring.
    (762, 'Base'): 'Base',
    (762, 'Deco'): 'Arredi',
    (762, 'Heir'): 'Cimeli',
    (762, 'Total'): 'Totale',
    # 💡 Un segno, non testo: resta com'e', come main.hsp:980 e text.hsp:12.
    (776, '*'): '*',

    # --- :824-:907 spostare, ospitare, incaricare.
    (824, 'Move who?'): 'Chi vuoi spostare?',
    (834, " Don't touch me!"): '" " + cnvtalk("Non toccarmi!")',
    (842, 'Where do you want to move ?'):
        '"Dove vuoi spostare " + cdatan(CDATAN_NAME, tc) + "?"',
    (848, 'The location is invalid.'): 'Lì non si può spostare.',
    # ⚠️ `is(tc)` e' morfologia inglese e se ne va.
    (863, '  moved to the location.'):
        '"Hai spostato " + cdatan(CDATAN_NAME, tc) + "."',
    # 💡 Stesso giapponese di proc.hsp:10793.
    (878, 'You need to dissolve the tag-team.'): 'Prima devi sciogliere la coppia.',
    (885, "Your party is already full. You can't invite someone anymore."):
        'Hai già il massimo dei compagni: non puoi portarne altri.',
    (890, '  no longer staying at your home.'):
        'cdatan(CDATAN_NAME, c) + " non è più ospite in casa tua."',
    # ⚠️ `his(c)` a un argomento e' morfologia: in italiano il possessivo si
    #    omette, perche' concorda con la cosa posseduta e non con chi possiede.
    (895, 'You remove  from  job.'):
        '"Hai sollevato " + cdatan(CDATAN_NAME, c) + " dall\'incarico."',
    (903, ' stay at your home now.'):
        'cdatan(CDATAN_NAME, c) + " ora è ospite in casa tua."',
    (907, ' take charge of the job now.'):
        'cdatan(CDATAN_NAME, c) + " ora ha l\'incarico."',

    # --- :924-:985 l'allevamento e il mangime.
    (924, 'You can only leave 150 allies in this ranch.'):
        "Qui puoi lasciarne al massimo 150.",
    (937, "You can't release escort targets."):
        'Non puoi lasciare qui chi devi scortare.',
    (949, ' stay at this ranch.'):
        'cdatan(CDATAN_NAME, c) + " resta all\'allevamento."',
    # 💡 Stesso giapponese di command.hsp:7098, su un'altra variabile.
    (953, ' changed original cloth.'):
        'cdatan(CDATAN_NAME, c) + " riprende l\'aspetto di prima."',
    (974, 'You need a livestock feed.'): 'Non hai mangime per il bestiame.',
    (979, 'Really use ?'): '"Vuoi davvero usare " + itemname(ci, 1) + "?"',
    # ⚠️ Il giapponese non nomina nessuno, l'inglese nomina due cose: la rete 11
    #    pretende le funzioni dell'inglese, e sono `name` e `itemname`.
    (985, ' sprinkled .'):
        'name(CHARA_PLAYER) + " sparge " + itemname(ci, 1) + " qui intorno."',
}
