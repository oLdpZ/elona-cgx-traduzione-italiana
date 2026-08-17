import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1174-:1187 la febbre delle Nefie casuali, le due meta' della stessa
    # cosa: :1187 accende GDATA_FLAG_NEFIA_FEVER_ACTIVE, :1174 lo rimette a zero.
    # Il plurale «Nefie» lo ha gia' scelto il pannello dei ritocchi.
    (1174, 'Nefia got quiet.'):
        'Le Nefie si sono calmate.',
    (1187, 'Nefia have entered fever!'):
        'Le Nefie casuali sono entrate in fermento!',

    # --- :1213-:1229 il vento d'etere. L'etichetta fra parentesi e' il nome
    # della sfida, e lo dice gia' il pannello: «Vento d'etere perenne».
    (1213, '(Permanent Etherwind) Etherwind will start in a few days, brace yourselves.'):
        "(Vento d'etere perenne) Fra pochi giorni arriva il vento d'etere: preparati.",
    (1217, "(Permanent Etherwind) Etherwind starts to blow. There's no escape."):
        "(Vento d'etere perenne) Il vento d'etere comincia a soffiare. Non c'è scampo.",
    # «rifugio» e' la resa fissata di `shelter` (text.hsp:2827, db_item.hsp:145197).
    (1229, 'Etherwind starts to blow. You need to find a shelter!'):
        "Il vento d'etere comincia a soffiare. Devi trovare un rifugio!",

    # --- :1242-:1307 il meteo. Le parole sono quelle dell'HUD (text.hsp:46):
    # «Pioggia», «Temporale», «Neve».
    (1242, 'You draw a rain cloud.'):
        'Attiri a te una nube di pioggia.',
    (1249, 'It starts to snow.'):
        'Comincia a nevicare.',
    (1256, 'It starts to rain.'):
        'Comincia a piovere.',
    # Il ramo mette WEATHER_HARD_RAIN, che nell'HUD si chiama «Temporale».
    (1261, 'Suddenly, rain begins to pour down from the sky.'):
        "All'improvviso scoppia un temporale.",
    (1274, 'It stops raining.'):
        'Ha smesso di piovere.',
    (1279, 'The rain becomes heavier.'):
        'La pioggia diventa un temporale.',
    (1286, 'The rain becomes lighter.'):
        'Il temporale si attenua in pioggia.',
    (1294, '(Permanent Etherwind) The Etherwind is restless.'):
        "(Vento d'etere perenne) Il vento d'etere non si placa.",
    (1300, 'The Etherwind dissipates.'):
        "Il vento d'etere si è dissolto.",
    # ⚠️ Il giapponese e' 「雪は止んだ」 e il ramo e' `p == WEATHER_SNOW`: l'inglese
    # ha copiato qui la stringa della pioggia di :1274. La resa segue il codice.
    (1307, 'It stops raining.'):
        'Ha smesso di nevicare.',

    # --- :1365-:1462 il ciclo del giorno.
    # «pisolino» e' gia' la resa di `nap` (command.hsp:10068).
    (1365, 'You take a nap.'):
        'Fai un pisolino.',
    (1373, 'You endure your sleepiness.'):
        'Resisti al sonno.',
    # Scatta a `gdata(GDATA_HOUR) == 6`, cioe' nell'ora che text.hsp:60 chiama «Alba».
    (1399, 'Day breaks.'):
        "Spunta l'alba.",
    (1453, 'A day passes and a new day begins.'):
        'Il giorno finisce e ne comincia uno nuovo.',
    # Gia' reso identico in sei file: la rete 3 lo confermera'.
    (1462, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',

    # --- :1524-:1540 le cinque giornate bonus. Il sostantivo e' quello con cui
    # text.hsp:48 nomina la giornata nella barra.
    (1524, "It's a perfect day for training today."):
        "Oggi è una giornata perfetta per l'allenamento.",
    (1528, "It's a perfect day for combat today."):
        'Oggi è una giornata perfetta per la battaglia.',
    (1532, "It's a perfect day for work today."):
        'Oggi è una giornata perfetta per il lavoro.',
    (1536, "It's a perfect day for exploring today."):
        "Oggi è una giornata perfetta per l'esplorazione.",
    (1540, "It's a perfect day for studying today."):
        'Oggi è una giornata perfetta per lo studio.',

    # --- :1589 il detective. Il nome della creatura e' «il detective»
    # (db_creature.hsp:70308) e «*Snif*» e' la resa gia' usata per lo sniffare
    # (db_creature.hsp:96610). `cnvtalk` e' contenuto e resta.
    (1589, 'A detective seems to have come.*Sniff*... I smell a case!!'):
        '"Pare che sia arrivato un detective." '
        '+ cnvtalk("*Snif*... qui sento odore di un caso!!")',

    # --- :1626-:1635 la finestra della sfida, gemella di command.hsp:15560.
    (1626, 'Permanent Etherwind'):
        "Vento d'etere perenne",
    # ⚠️ «Hai resistito» e non «Sei sopravvissuto»: il participio con `essere`
    # accorderebbe col genere del giocatore, che non si conosce.
    (1628, 'Unbelievable! You survived Etherwind for  days!'):
        '"Incredibile! Hai resistito al vento d\'etere per " '
        '+ (TweakData(TWEAK_CHALLENGE_ALWAYS_ETHERWIND, TWEAK_CATEGORY_CHALLENGE) - 1) '
        '+ " giorni!"',
    # Le sei battute sono le stesse `lang()` di command.hsp:15564-15569, gia'
    # rese li' e in text.hsp: si ricopiano.
    (1630, 'Finally!'):
        'Finalmente!',
    (1631, 'Just the natural outcome.'):
        'Era il risultato naturale.',
    (1632, 'Woooooo!'):
        'Uooooooh!',
    (1633, 'Heh.'):
        'Hmpf.',
    (1634, "I can't sleep tonight."):
        'Stanotte non chiudo occhio.',
    (1635, "You're kidding."):
        'Stai scherzando.',
}
