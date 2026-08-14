import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il vortice di mana, che interrompe la lettura.
    # ⚠️ le virgolette dentro una statica vanno protette, come fa l'inglese
    (1505, '\\"Look out!\\" An ally notices a magical vortex and interrupts your reading.'):
        '\\"Attento!\\" Un compagno si accorge del vortice di mana e ti interrompe la lettura.',
    # ⚠️ genitivo: «il mana di X». Dativo riflessivo, come i ventidue del lotto 002
    (1511, ' mana is absorbed.'):
        'name(cc) + " si vede risucchiare il mana!"',
    (1524, '  even more confused now.'):
        'name(cc) + " si confonde ancora di più."',
    (1527, "It's too difficult!"):
        'Troppo difficile!',
    # ⚠️ il giapponese dice 「何かを」, «qualcosa»: l'inglese conta le creature
    (1536, 'Several creatures are summoned from a magical vortex.'):
        'Il vortice di mana evoca qualcosa!',
    # ⚠️ STATICA benche' il giapponese nomini cc: il tipo lo decide il ramo che
    #    la resa sostituisce, quindi niente nome. Il codice dice che e' un
    #    teletrasporto (efid = SKILL_SPELL_TELEPORT due righe sotto)
    (1556, 'A dimensional door opens in front of you.'):
        'Una forza strana distorce lo spazio!',

    # --- i tre gradini della sete, con le loro varianti.
    (1689, 'You are dehydrated!'):
        'Di questo passo la disidratazione ti stenderà!',
    (1689, 'You are almost a mummy.'):
        'Ancora un poco e diventi carne secca.',
    (1693, 'Your thirst makes you dizzy.'):
        'La sete ti fa girare la testa...',
    (1693, 'You have to drink something NOW.'):
        'Devi bere qualcosa, e subito...',
    (1697, 'You are getting thirsty.'):
        'Hai la gola arsa.',
    (1697, 'You feel thirsty.'):
        'Ti è venuta sete.',
    (1697, 'Now what shall I drink?'):
        'E adesso, che si beve?',

    # --- i tre gradini della fame, uguali e paralleli.
    (1732, 'You are starving!'):
        'Di questo passo muori di fame!',
    (1732, 'You are almost dead from hunger.'):
        'Hai una fame che ti uccide.',
    (1736, 'Your hunger makes you dizzy.'):
        'La fame ti fa girare la testa...',
    (1736, 'You have to eat something NOW.'):
        'Devi mangiare qualcosa, e subito...',
    (1740, 'You are getting hungry.'):
        'Ti sta venendo fame.',
    (1740, 'You feel hungry.'):
        'Hai fame.',
    (1740, 'Now what shall I eat?'):
        'E adesso, che si mangia?',

    # --- il sonno rotto dall'esplosione, e il miasma.
    (1764, '  hurt by the blast.'):
        '"L\'onda d\'urto travolge " + name(cnt) + "."',
    # ⚠️ rete 13: lo stesso inglese per il VELENO del miasma e per il miasma che
    #    CORRODE. Il codice li separa col colore (LIGHT_GREEN contro BLUE)
    (1821, '  weakened.'):
        '"Il veleno del miasma indebolisce " + name(r1) + "."',
    # ⚠️ «lo indebolisce» e «indebolirlo» portano un clitico che concorda:
    #    il -ne enclitico della 37ª
    (1854, '  weakened.'):
        '"Il miasma consuma " + name(r1) + " e ne fiacca le forze."',

    # --- il soffocamento.
    (1873, 'Ughh...!'):
        'Uuugh...!',
    (1879, ' stopped choking.'):
        'name(r1) + " riprende fiato. \\"Cof, cof!\\""',

    # --- i recuperi di stato. Tre erano gia' decisi altrove.
    (1895, ' break away from gravity.'):
        'name(r1) + " si libera dalla gravità."',
    (1906, ' calm down.'):
        'name(r1) + " si calma un poco."',
    (1917, ' stand up.'):
        'name(r1) + " si rimette in piedi."',
    # copiata da action.hsp:9515, stesso giapponese
    (1929, ' released from bind.'):
        'name(r1) + " si libera dalla costrizione."',
    # copiata da chara_func.hsp:3884, stesso giapponese
    (1948, ' recovered from brainwash.'):
        'name(r1) + " torna in sé."',
    (1964, ' recovered from atrophy.'):
        'name(r1) + " ritrova la voglia di combattere."',
    # ⚠️ genitivo: «la difesa di X»
    (1972, "'s protection vanishes."):
        'name(r1) + " allenta la guardia."',
    (2077, 'Your body is gradually falling apart...'):
        'Il corpo ti si sfalda a poco a poco...',
    (2095, ' recovered from incapacity.'):
        'name(r1) + " torna a muoversi."',
    (2107, ' became incapacitated.'):
        'name(r1) + " non riesce più a muoversi."',
    # stessa forma di chara_func.hsp:6182, che ha un giapponese gemello
    (2257, ' returned to their original form.'):
        'name(r1) + " ha ripreso l\'aspetto di prima."',

    # --- i quattro versi dello stimolo, tutti gia' resi a proc.hsp:6926-6935
    (2390, ' is extremely restless and fidgety...'):
        'name(r1) + " si agita senza sosta..."',
    (2393, ' is squirming and writhing in discomfort...'):
        'name(r1) + " si contorce dal disagio..."',
    (2396, ' is desperately holding back urine, trying not to go...'):
        'name(r1) + " si trattiene a fatica dal fare pipì..."',
    (2399, ' is trembling slightly, barely managing to endure the urge to urinate...'):
        'name(r1) + " trema appena e resiste allo stimolo..."',
    # copiata da chara_func.hsp:3377 e :8317, stesso giapponese
    (2408, ' wet .'):
        'name(r1) + " se la fa addosso."',

    # --- il sonno e il bonus della festa.
    (2473, 'You need to sleep.'):
        'Hai bisogno di dormire.',
    # ⚠️ «e' soddisfatto» concorderebbe col personaggio
    (2654, '  satisfied.'):
        'cdatan(CDATAN_NAME, cnt) + " ha avuto quel che voleva."',
    (2659, '(Total Bonus:%)'):
        '"(Bonus totale: " + ptp + "%)"',
}
