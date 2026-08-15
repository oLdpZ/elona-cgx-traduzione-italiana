import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Le interazioni di base (:5952-:5976). Riquadro da 275 px (`:6172`),
    # tetto 29 caratteri: la voce piu' lunga qui ne fa 20.
    # ================================================================
    # 💡 Governa anche :6085, che e' il secondo `promptAdd` della stessa firma.
    (5952, 'Talk'):
        'Parla',
    (5955, 'Attack'):
        'Attacca',
    # ⚠️ Non e' una dichiarazione d'amore: porta a txtselectkimoti (`:6842`),
    #    undici battute che vanno da «Ti amo.» a «Fai schifo.»
    #    (text.hsp:1756-:1790, gia' rese).
    (5963, 'Confess feelings'):
        "Di' quello che provi",
    # 💡 I due rami sono «渡す/もらう» e «渡す»: le due rese restano in coppia.
    (5967, 'Give/Take'):
        'Dai/Ricevi qualcosa',
    (5970, 'Give'):
        'Dai qualcosa',
    # ⚠️ Il giapponese dice 「所持品」, l'inventario; ma :6229 mette `Filter_Food = 1`
    #    prima di aprirlo, e l'inglese dice «Feed». Si da' da mangiare.
    (5976, 'Feed'):
        'Dai da mangiare',

    # ================================================================
    # Le carte (:5985-:5996)
    # ================================================================
    # ⚠️⚠️ 「ランク」 e' il NUMERO della carta (`:6772` chiede 1-13). «rango» in
    #    questo file e' gia' il grado dell'avventuriero (:4192, :4194), e
    #    proc.hsp:20184 — la frase che insegna la cosa — dice gia' «seme e
    #    valore». Va insieme a scratchpad/correzione-rango-carta.py, che porta
    #    :6770 da «Quale rango?» a «Quale valore?».
    (5985, '<Rank Change>'):
        '<Cambia valore>',
    # ⭐ I quattro semi erano gia' decisi: db_creature.hsp:38006, :37943, :37880
    #    e :37816, e i messaggi :6790-:6811 dicono gia' «conta come il guerriero
    #    di picche».
    (5987, '[Spade Change]'):
        '[Cambia in picche]',
    (5990, '[Club Change]'):
        '[Cambia in fiori]',
    (5993, '[Diamond Change]'):
        '[Cambia in quadri]',
    (5996, '[Heart Change]'):
        '[Cambia in cuori]',
}
