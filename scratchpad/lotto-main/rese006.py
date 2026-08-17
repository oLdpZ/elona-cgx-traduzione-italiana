import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4128-:4151 il finale di Tyris del Sud. 「災厄」 e' «la calamità»
    # (text.hsp:9692, db_card.hsp:9227).
    (4128, "Blessing to , ! You've finally destroyed the source of disaster!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente distrutto la radice della calamità!"',
    (4150, 'In the year , /, you conquered Remido.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista delle Rovine di Remido."',
    # ⚠️ Stesso giapponese di :4232 e di :4071: a distinguerli e' il nome del
    # boss, che ce l'ha solo l'inglese. Vedi la correzione della rete 4.
    (4151, 'Upon killing Meshera Alpha, you said, '):
        '"Uccidendo Meshera Alpha hai detto: " + cnvtalk("" + wincomment)',

    # --- :4186-:4232 il finale del Sigillo Eterno. 「混沌の神」 e' «il dio del
    # caos» (text.hsp:9852).
    (4186, 'Unbelievable! You conquered the Eternal Seal!'):
        'Incredibile! Hai conquistato il Sigillo Eterno!',
    (4209, "Blessing to , ! You've finally beat the god of chaos!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente abbattuto il dio del caos!"',
    (4231, 'In the year , /, you conquered the Eternal Seal.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista del Sigillo Eterno."',
    (4232, 'Upon killing Enthumesis, you said, '):
        '"Uccidendo Enthumesis hai detto: " + cnvtalk("" + wincomment)',

    # --- :4272-:4274 le ultime parole. Lo spazio finale di :4272 c'e' anche
    # nell'inglese e serve a chi concatena.
    (4272, 'Good bye... '):
        'Addio... ',
    (4274, 'You leave a dying message.'):
        'Lasci un ultimo messaggio.',

    # --- :4282 ⚠️ CHIAVE LUNGA: due `lang()` sulla riga con lo stesso inglese.
    # Sono le virgolette che aprono e chiudono, non testo: gia' in invariati.md.
    (4282, '\\"', '「'):
        '\\"',
    (4282, '\\"', '」'):
        '\\"',

    # --- :4291-:4296 la lapide, tre righe di `noteadd`.
    (4291, ' '):
        ' ',
    # ⚠️ Ordine anno/mese/giorno come l'inglese: e' quello con cui init.hsp:2225
    # compone tutte le date del gioco, e li' il dizionario non puo' cambiarlo.
    (4293, '//'):
        '"" + gdata(GDATA_YEAR) + "/" + gdata(GDATA_MONTH) + "/" + gdata(GDATA_DAY)',
    # ⚠️ Nessuna preposizione davanti a mdatan: «a Vernis» ma «in Prigione».
    # `ndeathcause` arriva gia' reso come verbo al passato remoto senza soggetto.
    (4296, ' in .'):
        'mdatan(MDATAN_NAME) + " - " + cnven(ndeathcause) + "."',

    # --- :4349-:4353 la sepoltura.
    (4349, 'You are about to be buried...'):
        'Stanno per seppellirti...',
    (4353, 'You have been buried. Bye...(Hit any key to exit)'):
        'Sei sottoterra. Addio... (premi un tasto per uscire)',

    # --- :4361-:4371 il menu della morte. `val = promptx, 100, 400, 1`, cioe'
    # 400 px = 45 caratteri; la piu' lunga ne fa 28. Tutte all'imperativo, che
    # e' anche l'unica forma senza genere.
    (4361, 'Reload last save'):
        "Ricarica l'ultimo salvataggio",
    (4365, 'Crawl up'):
        'Rialzati',
    (4368, 'Crawl up from hell'):
        "Rialzati dall'inferno",
    (4371, 'Lie on your back'):
        'Lasciati seppellire',

    # --- :4409 la riga che va al tabellone in rete. Stessa forma della lapide.
    (4409, '   in  '):
        'cdatan(CDATAN_AKA, CHARA_PLAYER) + " " '
        '+ cdatan(CDATAN_NAME, CHARA_PLAYER) + " " + ndeathcause + " - " '
        '+ mdatan(MDATAN_NAME) + " " + lastword',
}
