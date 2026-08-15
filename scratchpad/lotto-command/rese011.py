import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1700-:1709 la stamina a terra, `rnd(4)`.
    (1700, 'Want to rest'):
        'Voglio riposare',
    # ⚠️ errore di monte: il giapponese e' l'apatia, non la fatica
    (1703, 'It keeps getting more difficult...'):
        'Comincia a non importarmi più niente',
    (1706, 'Do I really need to work this hard?'):
        'Devo per forza sforzarmi ancora?',
    (1709, 'Well, that was unpleasant'):
        'Ecco perché non volevo',

    # --- :1713-:1725 la vita sotto un quarto. ⚠️ le ultime due non dipendono
    #     dal `rnd(3)` ma da `CDATA_MASTER_SERVANT2`: il panico e il piacere.
    (1713, 'I may die'):
        'Potrei morire',
    (1716, 'I can not afford to fall down yet'):
        'Non posso cadere adesso',
    (1719, 'I am not going to die here'):
        'Non è qui che voglio morire',
    (1722, 'I do not want to die...'):
        'Ahi ahi no non voglio morire',
    (1725, 'I am excited'):
        'Che brivido...',

    # --- :1729-:1780 le tredici condizioni, una riga per condizione.
    (1729, 'Anxious that can not see anything'):
        'Non vedo niente, che angoscia',
    # 💡 la croma la porta il giapponese, e l'inglese la butta via
    (1732, 'Somewhat funny'):
        'Che allegria♪',
    (1735, 'Wants to escape by some means'):
        'Devo trovare il modo di scappare!',
    (1738, 'Regret that can not move'):
        'Non riesco a muovermi, che frustrazione',
    (1741, 'Can not stop anger'):
        'La rabbia non passa!',
    (1744, 'Scattered in head'):
        'Mi gira tutto in testa',
    (1747, 'Misty on head'):
        'Ho come una nebbia in testa',
    # ⭐ il katakana e' la voce di chi non decide piu': il maiuscolo fa lo stesso
    (1750, 'Trying to execute the order'):
        "ESEGUO L'ORDINE",
    (1753, 'In a bad mood'):
        'Mi sento male',
    (1756, 'Painful a poor physical condition'):
        'Sto poco bene, che fatica',
    # ⚠️ il giapponese la dice due volte, ed e' il panico: si tiene
    (1759, 'Have to run away'):
        'Devo scappare devo scappare',
    (1762, 'Painful that can not breathe'):
        'Non respiro! Che agonia...',
    (1765, 'Playing with the sheep in dream'):
        'Nel sogno gioco con le pecore',
    (1768, 'Obsession'):
        'Un pensiero fisso non mi lascia',
    (1771, 'Scared with fear'):
        'Il terrore mi confonde tutto',
    (1774, 'Suffering from trauma.'):
        'Un vecchio trauma mi tormenta',
    # ⚠️ 「あなたに殺される」: l'allucinazione e' che a ucciderlo sia TU
    (1777, 'Looking at the hallucination killed by you'):
        'Ti vedo uccidermi, e non è vero',
    (1780, 'Suffers from a suicide impulse.'):
        'Resisto alla voglia di farla finita',

    # --- :1784 quando il bersaglio sei tu: sovrascrive tutte le altre.
    (1784, "It's a strange feeling looking into one's own heart."):
        'Guardarsi dentro fa un effetto strano',
}
