import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1702-:1738 i tre incarichi di livello 150. I nomi stanno gia' cosi',
    # fra parentesi angolari, in db_card.hsp e in text.hsp.
    (1702, 'It seems that the mind of <Arasiel> has changed.'):
        'Pare che <Arasiel> abbia cambiato idea.',
    (1718, 'You have received a request for help from <Garziem>.'):
        'È arrivata una richiesta di aiuto da <Garziem>.',
    # Il giapponese dice 電波, un segnale radio: il messaggio arriva da lontano.
    (1738, 'You have received a rescue request from <Amurdad>.'):
        'È arrivata una chiamata di soccorso da <Amurdad>.',

    # --- :1867-:1893 le due coppie del rientro impedito. La variabile che le
    # separa e' GDATA_FLAG_SHIP_LAST_PORT: 0 = rientro, altro = imbarco.
    (1867, 'Strange power prevents you from returning.'):
        'Una forza misteriosa impedisce il rientro.',
    (1871, 'Strange power prevents you from sailing.'):
        'Una forza misteriosa impedisce di salpare.',
    (1889, 'One of your allies prevents you from returning.'):
        'Hai con te un alleato che adesso non può rientrare.',
    (1893, 'One of your allies prevents you from sailing.'):
        'Hai con te un alleato che adesso non può salpare.',

    # --- :1898 «Sovraccarico» e' il nome che text.hsp:66 da' a questo stato
    # nella barra: la voce ripete la parola invece di inventarne un'altra.
    (1898, 'Someone shouts, \\"Sorry, overweight.\\"'):
        'Da qualche parte si sente una voce: \\"Spiacente, sovraccarico.\\"',

    # --- :1910-:1919 il Ritorno che riesce.
    (1910, 'You commit a crime.'):
        'Hai infranto la legge.',
    # ⚠️ Stesso inglese di calculation.hsp:1556, ma altro giapponese e altro
    # evento: qui e' l'arrivo del Ritorno, con SOUNDLIST_TELEPORT1.
    (1915, 'A dimensional door opens in front of you.'):
        'Hai aperto una porta dimensionale.',
    (1919, 'Your ship has arrived.'):
        'La tua nave è arrivata.',

    # --- :1928-:1932 il carretto troppo pesante. «carretto» e' la parola della
    # barra dell'inventario (command.hsp:14176).
    (1928, 'Return failed because your cargo is too heavy.'):
        'Ma il carretto è troppo pesante: il rientro è fallito.',
    (1932, 'Sailing failed because your cargo is too heavy.'):
        "Ma il carretto è troppo pesante: l'imbarco è fallito.",

    # --- :1937 il Ritorno che ti scarica in prigione. 管理者 e' insieme chi
    # amministra e chi sorveglia: «custode» tiene le due cose.
    (1937, 'The capricious controller of time has changed your destination!'):
        'Il capriccioso custode del tempo ha stravolto la tua destinazione!',
}
