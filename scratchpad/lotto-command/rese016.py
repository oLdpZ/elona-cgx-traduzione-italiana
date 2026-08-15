import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6790-:6811 le quattro carte. ⭐ i nomi vengono da db_creature.hsp,
    #     articolo compreso. ⚠️ «e' trattato come» concorderebbe con la creatura.
    (6790, ' is treated as a spade warrior.'):
        'cdatan(CDATAN_NAME, tc) + " conta come il guerriero di picche."',
    (6797, ' is treated as a club feather.'):
        'cdatan(CDATAN_NAME, tc) + " conta come la piuma di fiori."',
    (6804, ' is treated as a diamond eyes.'):
        'cdatan(CDATAN_NAME, tc) + " conta come gli occhi di quadri."',
    (6811, ' is treated as a heart witch.'):
        'cdatan(CDATAN_NAME, tc) + " conta come la strega di cuori."',

    # --- :6825 l'icona tolta. ⚠️ rete 8: «da » + name() darebbe «da il putit»,
    #     quindi il nome passa a soggetto e il verbo e' un composto con AVERE.
    (6825, 'You deleted the item mark on .'):
        'name(tc) + " ha perso l\'icona."',

    # --- :6863-:6921 le reazioni alla frase insegnata.
    #     ⚠️ `him(tc)` e `his(tc)` sono morfologia e spariscono.
    (6863, ' becomes very curious about what you were wanting to tell ...'):
        'cdatan(CDATAN_NAME, tc) + " si domanda con ansia che cosa volevi dire..."',
    # ⭐ copiata: la stessa riga sta in cinque file
    (6869, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',
    (6880, ' looks happy.'):
        'cdatan(CDATAN_NAME, tc) + " ha un\'aria felice."',
    (6883, ' seemed to think it was an exaggerated joke.'):
        'cdatan(CDATAN_NAME, tc) + " sembra averla presa per una battuta esagerata."',
    (6889, " is looking at you like you're some kind of creep."):
        'cdatan(CDATAN_NAME, tc) + " ti guarda come si guarda un tipo losco."',
    # ⚠️ errore di monte: 「まんざらでもない」 e' «non gli dispiace affatto»,
    #    cioe' il contrario di quel che dice l'inglese
    (6901, " doesn't seem to be very happy about that."):
        'cdatan(CDATAN_NAME, tc) + " non sembra dispiacersene affatto."',
    (6915, " couldn't believe  ears..."):
        'cdatan(CDATAN_NAME, tc) + " non crede alle proprie orecchie..."',
    (6918, ' gives you a look of pity.'):
        'cdatan(CDATAN_NAME, tc) + " ti guarda con pietà."',
    # ⚠️ 「やれやれ」 e' il sospiro di chi la scampa, non il sollievo del corpo
    (6921, ' shrugged  shoulders in relief.'):
        'cdatan(CDATAN_NAME, tc) + " alza le spalle con un sospiro."',

    # --- :6934-:6947 la notte con chi hai sposato, e i tre rifiuti del gioco.
    (6934, "You can't make a gene in this game mode."):
        'In questa modalità non si possono lasciare geni.',
    (6939, " isn't sleepy yet."):
        'cdatan(CDATAN_NAME, tc) + " non ha ancora sonno."',
    (6944, 'It seems that  wants to get out of here.'):
        '"Sembra che " + cdatan(CDATAN_NAME, tc) + " voglia andarsene da qui."',
    (6947, '*blush*'):
        '*arrossisce*',

    # --- :6955-:6978 le guardie di Jure. ⭐ 「ジュア」 e' «Jure» in quattro file.
    (6955, ': \\"Stop this at once! Lady Jua says she doesn\'t want to!\\"'):
        'cdatan(CDATAN_NAME, cnt) + ": \\"Smettila subito! Jure ha detto di no!\\""',
    (6978, ': \\"I won\'t forgive you for that.\\"'):
        'cdatan(CDATAN_NAME, cnt) + ": \\"Questo non te lo perdono!\\""',

    # --- :6987-:6998 le due risposte no e quella si'. Lo spazio in coda delle
    #     prime due e' dell'inglese.
    (6987, '... gently refuses your proposal. '):
        '"..." + cdatan(CDATAN_NAME, tc) + " rifiuta con garbo. "',
    (6993, '... sadly refuses your proposal. '):
        '"..." + cdatan(CDATAN_NAME, tc) + " rifiuta con dispiacere. "',
    (6998, '... blushed and nodded!'):
        '"..." + cdatan(CDATAN_NAME, tc) + " arrossisce e annuisce!"',
}
