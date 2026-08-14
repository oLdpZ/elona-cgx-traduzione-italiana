import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- chi tira i sassi al gigante.
    (1525, 'Filthy monster!'):
        'Mostro schifoso!',
    (1525, 'Go to hell!'):
        'Crepa!',
    (1525, "I'll get rid of you."):
        'Adesso ti faccio fuori!',
    # ⭐ una firma copre due siti: 「くらえー！」 torna identica a :1570, e
    #    l'estrazione la conta una volta sola (lezione del lotto proc-017)
    (1525, 'Eat this!'):
        'Prendi questo!',

    # --- il pupazzo di neve.
    (1557, ' make !'):
        'name(cc) + " ha fatto " + itemname(ci) + "!"',

    # --- chi tira le cose per gioco. ⭐ la risatina e' gia' di db_creature:95622
    (1570, ' *grin* '):
        ' *risatina* ',
    (1570, 'Fire in the hole!'):
        'Toh!',
    (1570, 'Tee-hee-hee!'):
        'Alè!',
    (1570, 'Watch out!'):
        'Attenzione!',
    (1570, 'Scut!'):
        'Scansati!',

    # --- chi ha visto la lumaca.
    (1717, 'Snail!'):
        'Una lumaca!',
    (1717, 'Kill!'):
        'A morte!',

    # ⚠️ genitivo di monte: «mira a Y» si fonderebbe. «Puntare» regge diretto
    (1755, ' seems to be aiming at ...'):
        'cdatan(CDATAN_NAME, cc) + " punta " + cdatan(CDATAN_NAME, tc) + "..."',

    # --- il gioielliere che lavora e contratta. 店主 e' «il negoziante»
    (1830, ' processed the items in  possession!'):
        'name(cc) + " ha lavorato gli oggetti che portava addosso!"',
    (1834, '  negotiating prices with the shopkeeper...'):
        'name(cc) + " tratta sul prezzo con il negoziante..."',
    (1860, ' sells  items and earns  gold pieces.'):
        'name(cc) + " vende " + sell + " oggetti e guadagna " + sell(1) + " monete d\'oro."',
    # ⚠️ il giapponese dice 稼ぎ, i guadagni, non le monete di action.hsp:973
    (1866, ' shared coins with partner.'):
        'name(cc) + " ha diviso i guadagni con il compagno."',

    # --- l'allenamento. 訓練券 e' il «biglietto d'addestramento» (db_item:134224)
    (1893, ' used a training ticket at a trainer and developed  potential!'):
        'cdatan(CDATAN_NAME, cc) + " si allena con un biglietto d\'addestramento '
        'e accresce il potenziale!"',
    # ⚠️ l'inglese scrive «gp» attaccato: la resa scioglie l'abbreviazione
    (1939, ' spent gp to visit a trainer and develop  potential!'):
        'cdatan(CDATAN_NAME, cc) + " spende " + hiyou + " monete d\'oro '
        'dall\'allenatore e accresce il potenziale!"',

    # --- chi cavalca e travolge.
    (2039, ' ran over .'):
        'name(cc) + " travolge " + name(tc) + "."',
    # ⭐ copiata: quattro siti dicono gia' «esita.» (action:288, chara_func:3107,
    #    proc:8303, proc:13308)
    (2043, '  faltered.'):
        'name(tc) + " esita."',

    # --- chi spinge via chi sta mangiando, e le cinque reazioni.
    (2068, ' displace .'):
        'name(cc) + " spinge via " + name(tc) + "."',
    # ⚠️ «un'occhiataccia a X» si fonde: «verso» no. La resa di action.hsp:1986
    #    si tiene tale e quale
    (2074, ' glare at .'):
        'name(tc) + " lancia un\'occhiataccia verso " + name(cc) + "."',
    (2080, ' looked at  with dissatisfaction.'):
        'name(tc) + " guarda " + name(cc) + " con disappunto."',
    # ⭐ le tre qui sotto sono copiate da action.hsp:1992-:1998
    (2087, ' looked disappointed.'):
        'name(tc) + " china il capo per la delusione."',
    (2094, ' nodded slightly.'):
        'name(tc) + " fa un piccolo cenno del capo."',
    (2101, ' stepped back without a word.'):
        'name(tc) + " indietreggia di un passo senza dire nulla."',

    # --- le stesse cinque per il compagno di tag-team, con cdatan(ttc).
    # ⭐ le ultime tre sono copiate da action.hsp:2017-:2023, cdatan compreso
    (2113, ' glare at .'):
        'cdatan(CDATAN_NAME, ttc) + " lancia un\'occhiataccia verso " + name(cc) + "."',
    (2117, ' looked at  with dissatisfaction.'):
        'cdatan(CDATAN_NAME, ttc) + " guarda " + name(cc) + " con disappunto."',
    (2122, ' looked disappointed.'):
        'cdatan(CDATAN_NAME, ttc) + " china il capo per la delusione."',
    (2127, ' nodded slightly.'):
        'cdatan(CDATAN_NAME, ttc) + " fa un piccolo cenno del capo."',
    (2132, ' stepped back without a word.'):
        'cdatan(CDATAN_NAME, ttc) + " indietreggia di un passo senza dire nulla."',

    # --- chi sfonda quel che trova.
    (2157, ' crush the door!'):
        'name(cc) + " sfonda la porta!"',
    (2168, ' crush the wall!'):
        'name(cc) + " sfonda il muro!"',

    # --- il dolore che stende, e il ghepardo che bara.
    (2300, ' fainted after failing to endure the severe pain.'):
        'name(cc) + " non regge al dolore e perde i sensi."',
    # ⚠️ invariato: il giapponese e' inglese anche lui, e «ban» e' gergo di rete
    (2308, ' *BAN* '):
        ' *BAN* ',

    # --- i cinque versi dei figli che crescono.
    # ⚠️ l'accordo cade su «aria», che e' femminile per sempre
    (2317, '  rolling fine!'):
        'cdatan(CDATAN_NAME, cc) + " si scatena dalla gioia!"',
    (2323, '  hopping and playing!'):
        'cdatan(CDATAN_NAME, cc) + " gioca a saltelloni!"',
    (2329, '  looking away with interest!'):
        'cdatan(CDATAN_NAME, cc) + " guarda altrove con aria curiosa!"',
    (2335, '  thinking with a serious face!'):
        'cdatan(CDATAN_NAME, cc) + " riflette con aria seria!"',
    (2341, '  doubts about how  live!'):
        'cdatan(CDATAN_NAME, cc) + " si interroga su come vivere!"',

    # --- il suffisso della forma alterata. ⭐ copiato da action.hsp:11372
    (4525, '-altered'):
        '/Alter',
}
