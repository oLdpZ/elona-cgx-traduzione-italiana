import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :13 la congiunzione della lista di oggetti sulla casella.
    # ⚠️ rete 3: text.hsp:11685 rende 「と」 «, più », ma li' e' la ricompensa di
    #    una missione, qui e' una lista. Vedi il docstring.
    (13, ' and '):
        ' e ',

    # --- :23-:30 le tre righe che partono a ogni passo su un oggetto.
    # ⚠️ «Vedi» e non «Si vede»: rtvaln puo' essere una pila («3 pozioni»).
    (23, 'You see  here.'):
        '"Vedi " + rtvaln + " per terra."',
    # ⚠️ «installato» concorderebbe col genere dell'oggetto: nome di genere fisso
    (27, ' is constructed here.'):
        '"Vedi qui una costruzione: " + rtvaln + "."',
    (30, 'You see  placed here.()'):
        '"Vedi " + rtvaln + " qui.(" + cnvweight(inv(INV_ITEM_WEIGHT, rtval(1))) + ")"',

    # --- :34-:49 i sei giudizi sul letto, che si saldano alla riga di sopra.
    # ⚠️ l'impersonale «ci si dorme»: l'accordo cade sul «si», non sul letto
    (34, " It looks uncomfortable to sleep on, but I'm sure I'll have good dreams."):
        ' Non ci si dorme comodi, ma i sogni saranno belli.',
    (37, " It wouldn't be much different from sleeping on the ground."):
        ' Non è molto diverso dal dormire per terra.',
    (40, " It's better than sleeping on the ground."):
        ' Meglio che dormire per terra, ma...',
    (43, ' I think I can rest to some extent.'):
        ' Ci si riposa discretamente.',
    (46, " I think I'll be able to sleep comfortably."):
        ' Ci si dorme bene.',
    (49, " I think I'll be able to sleep very comfortably!"):
        ' Ci si dorme benissimo!',

    # --- :53-:73 i cinque barili dell'alchimista. db_item.hsp:136634 fissa
    #     «barile», e il giapponese e' sempre la stessa parola allungata.
    (53, ' \\"Baaarrel...\\"'):
        ' \\"Baaarile...\\"',
    (58, ' \\"It\'s a Barrel~\\"'):
        ' \\"Bariiile~\\"',
    (63, ' \\"A barrel.\\"'):
        ' \\"Un barile.\\"',
    (68, ' \\"Barrel!\\"'):
        ' \\"Barile!\\"',
    (73, ' \\"Barrel.\\"'):
        ' \\"Baarile.\\"',

    # --- :78 ⚠️ il giapponese conta i TIPI, l'inglese i pezzi.
    (78, 'There are  items lying here.'):
        '"Qui ci sono " + rtval + " tipi di oggetti."',

    # --- :127 ⚠️ « stacks » in inglese, ﾀｰﾝ in giapponese, e il cdata conta turni.
    (127, ' stacks '):
        ' turni ',

    # --- :160-:169 la scheda del bersaglio (il gemello :265/:271 e' rinviato).
    (160, 'SpriteID:  / ColorID:  '):
        '"ID sprite: " + cdata(CDATA_PIC, txttargetnpc_arg_tc) + " / ID colore: " + '
        'refchara(cdata(CDATA_ID, txttargetnpc_arg_tc), DBSPEC_CHARA_COL) * 1000 + " "',
    (169, 'Gender:  / Age:  / Religion: '):
        '"Sesso: " + s + " / Età: " + calcage(txttargetnpc_arg_tc) + " anni / Fede: " + '
        'godname(cdata(CDATA_GOD, txttargetnpc_arg_tc)) + ""',

    (231, 'This location is out of sight.'):
        'Fuori dal campo visivo.',

    # --- :282 il bersaglio e il suo compagno di coppia.
    # 💡 « + » e' un invariato nuovo: il giapponese ha il ＋ a larghezza intera
    (282, 'You are targeting '):
        'Il bersaglio è ',
    (282, ' + '):
        ' + ',
    (282, '.(Distance '):
        ' (distanza ',

    # --- :433-:456 la finestra delle stanze e delle squadre scaricate.
    (433, 'Which room do you want to visit? '):
        'Quale stanza vuoi visitare? ',
    (436, 'Which team do you want to play a match? '):
        'Contro quale squadra vuoi giocare? ',
    (445, 'Room List'):
        'Elenco delle stanze',
    (448, 'Team List'):
        'Elenco delle squadre',
    (450, 'BackSpace [Delete]  '):
        'BackSpace [Cancella]  ',
    # ⚠️ rete 13: lo stesso «Name» per 「ルームの名称」 e 「チームの名称」
    (453, 'Name'):
        'Nome',
    (456, 'Name'):
        'Nome',

    (510, 'Selected item is incompatible.'):
        'Il file è di una versione incompatibile.',
    (524, 'Failed to retrieve designated files.'):
        'Recupero del file non riuscito.',
    (566, 'Do you really want to delete ? '):
        '"Vuoi davvero cancellare " + userfile + "? "',

    # --- :602-:993 il bersaglio. ⭐ :602 e' parola per parola proc.hsp:20200,
    #     :858 e :993 prendono la forma di proc.hsp:3681.
    (602, 'You look around and find nothing.'):
        "Non c'è nessun bersaglio in vista.",
    (858, 'You target .'):
        '"Prendi di mira " + name(rc) + "."',
    (864, 'You target the ground.'):
        'Prendi di mira il terreno.',
    (993, 'You target .'):
        '"Prendi di mira " + name(p) + "."',
}
