import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4192-:4201 la bacheca degli avventurieri.
    #     ⚠️ display_topic non lo misura nessuno strumento: la colonna di mezzo
    #        ha 104 px e l'inglese ne prende già di più. Regola dei siti non
    #        misurati: mai più lunghi dell'inglese. Vedi il docstring.
    (4192, 'Adventurer Rank'): 'Rango degli avventurieri',
    (4194, 'Name and Rank'): 'Nome e rango',
    # 「名声(友好)」: 14 caratteri contro i 13 dell'inglese
    (4196, 'Fame(Impress)'): 'Fama(amicizia)',
    # 「伝言種類(友好)」: 16 caratteri esatti come l'inglese
    (4199, 'Message(Impress)'): 'Messaggio(amic.)',
    (4201, 'Location'): 'Luogo',

    # --- :4253-:4256 la colonna del luogo.
    # ⭐ rete 3: chara_func.hsp:172 e text.hsp:2969 dicono già «Ignoto».
    (4253, 'Unknown'): 'Ignoto',
    (4256, 'Hospital'): 'Ospedale',

    # --- :4294-:4312 l'avventuriero a cui si affida un messaggio.
    # 「冷やかしか」: l'inglese dice «You kidding?», il giapponese «vieni solo a
    # curiosare?». Restano tutt'e due un rifiuto seccato.
    (4294, ' You kidding?'): '" " + cnvtalk("Mi stai prendendo in giro?")',
    (4309, ' Well noted!'): '" " + cnvtalk("Ricevuto!")',
    (4312, " I'll make sure that your message is delivered!"):
        '" " + cnvtalk("Uso la mia rete di contatti: il messaggio arriverà di sicuro!")',

    # --- :4334-:4336 *wish_fix, che NON è testo da leggere: sono le parole che
    #     il giocatore digita nella finestra del desiderio.
    #     ⚠️⚠️ «abilita» è senza accento di proposito: in CP932 la à non esiste,
    #        quindi nessuno può batterla, e un del_str su «abilita'» non
    #        aggancerebbe mai niente. Vedi il docstring.
    #     ⚠️ :4335, la variante con lo spazio, è RINVIATA: la rete 4 pretende una
    #        resa sola per lo stesso giapponese. La scrive la toppa.
    (4334, 'item'): 'oggetto',
    (4336, 'skill'): 'abilita',

    # --- :4350-:4374 la scelta del nome d'arte.
    (4350, 'Alias Selection'): 'Scelta del nome',
    (4356, 'Alias List'): 'Nomi possibili',
    (4374, 'Reroll'): 'Pensane un altro',
}
