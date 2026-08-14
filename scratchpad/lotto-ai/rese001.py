import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il bambino del caos che dimentica, e il nemico che implora pieta'.
    # ⚠️ l'inglese ha DUE name(): la rete 11 li pretende tutt'e due, e in
    #    italiano il nome si ripete come si ripete in inglese
    (79, ' was frightened and began to ask for forgiveness. Maybe you could talk to  now.'):
        '"La paura travolge " + name(cc) + ", che si mette a implorare pietà. '
        'Vuoi ascoltare " + name(cc) + "?"',
    # ⚠️ he(cc, 1) e' CONTENUTO (due argomenti, init.hsp:1819): dice «lui»/«lei»
    #    e va conservato dentro la frase
    (381, ' forgot the reason why   fighting.'):
        'name(cc) + " non ricorda più perché " + he(cc, 1) + " combatte."',
    (387, ' forgot how to walk.'):
        'name(cc) + " ha dimenticato come si cammina."',
    (393, ' forgot how to breathe.'):
        'name(cc) + " ha dimenticato come si respira."',
    (399, ' forgot  fighting instincts.'):
        'name(cc) + " ha dimenticato l\'istinto della lotta."',
    # ⚠️ personaggio sbagliato: l'inglese dice name(tc), il giapponese e il
    #    codice dicono cc (animeload 8, cc; le quattro sorelle qui sopra)
    (406, ' forgot everything and completely stopped moving....'):
        'name(cc) + " ha dimenticato ogni cosa e non si muove più..."',

    # --- il sacco da pugni (CHARA_BIT_SANDBAG). ⚠️ l'inglese ha rimescolato:
    #     «Release me now.» e' la battuta del prigioniero di :482
    (472, 'Release me now.'):
        'Colpiscimi ancora!',
    (472, "I won't forget this."):
        'Questa non te la perdono!',
    (472, 'Hit me!'):
        'Ma che fai?!',

    # --- il prigioniero in gabbia (CHARA_BIT_LOCKED_UP). ⚠️ la seconda ha lo
    #     stesso giapponese di :472: la rete 4 pretende la stessa resa
    (482, 'Release me now!'):
        'Fammi uscire di qui!',
    (482, "I won't forget this!"):
        'Questa non te la perdono!',
    (482, 'Where are you taking me?'):
        'Dove mi porti?',

    # --- chi si tira dietro al guinzaglio e non ci sta.
    # ⚠️ divergenza dichiarata: action.hsp:8778 ha lo stesso giapponese ma e'
    #    una dinamica che descrive da fuori, qui e' il grido del personaggio
    (522, 'Ouch!'):
        'Ahi!',
    (522, 'Stop it!'):
        'Smettila!',
    (528, ' untangle the leash.'):
        'name(cc) + " si libera dal guinzaglio."',

    # --- il pubblico dell'arena delle bestie.
    # ⚠️ divergenza dichiarata: proc.hsp:850 rende lo stesso giapponese «Bel
    #    pezzo!», ma li' e' il pubblico di un concerto
    (658, 'Come on!'):
        'Così si fa!',
    (658, 'More blood!'):
        'Dagliele!',
    (658, "Beat'em!"):
        'Fallo sanguinare!',
    # ⚠️ le due qui sotto sono scambiate di monte: 頑張って e' «forza!» e
    #    頭を使えよ e' «usa la testa». Rese sul giapponese
    (658, 'Use your brain!'):
        'Forza!',
    (658, 'Wooooo!'):
        'Uooooh!',
    (658, 'Go go!'):
        'Vai!',
    (658, 'Good fighting.'):
        'Usa la testa!',
    (658, 'Yeeee!'):
        'Iiiih!',
    # le due degli evocati, che guardano e basta
    (670, 'Come on!'):
        'Sembra divertente!',
    (670, 'More blood!'):
        'Forza tutti e due!',

    # --- il pronto soccorso. ⭐ copiata da action.hsp:11146, stesso giapponese
    (865, ' used a first aid kit.'):
        'name(cc) + " ha usato il kit di pronto soccorso."',

    # --- i compagni che mangiano e bevono.
    (1009, ' consults your expression and cautiously touches the food.'):
        'name(cc) + " ti scruta in faccia e prende il cibo con timore."',
    # ⚠️ genitivo: «lo zaino di X» non si scrive. Il possesso resta implicito
    (1100, ' searched  bag and find nothing to eat!'):
        'name(cc) + " fruga nello zaino e non trova niente da mangiare!"',
    (1129, ' searched  bag and find nothing to drink!'):
        'name(cc) + " fruga nello zaino e non trova niente da bere!"',
    # ふかふかパン e' il «pane soffice» di db_item.hsp:141763
    (1163, '  frightned by the puff puff bread at  feet.'):
        'name(cc) + " ha paura del pane soffice che ha ai piedi..."',
    # パートナー e' il «compagno di coppia» di action.hsp:1024
    (1191, ' silently watches  partner have a meal.'):
        'name(cc) + " guarda in silenzio il compagno di coppia che mangia..."',
    (1207, " couldn't endure and approached the food."):
        'name(cc) + " non resiste e si avvicina al cibo."',
    (1224, '  gazing at the food with a pained expression.'):
        'name(cc) + " fissa il cibo con occhi struggenti..."',
    (1241, ' salivates to moisten  throat, but remembers something and jumps up trembling.'):
        'name(cc) + " sta per bere, poi si ricorda di qualcosa e trasalisce."',
    (1252, " couldn't endure and approached the water."):
        'name(cc) + " non resiste e si avvicina all\'acqua."',
    # ⚠️ senza kit, ed e' un'altra frase: qui il codice cura hp, mp e sp da solo
    (1326, ' administered first aid.'):
        'name(cc) + " si medica alla meglio."',

    # --- Dragostea din tei, primo gradino: la forma con cui la canzone e'
    #     conosciuta in Italia. ⚠️ il verso rumeno resta invariato
    (1452, 'Vrei sa pleci dar♪'):
        'Vrei sa pleci dar♪',
    (1452, 'Numa numa yay!!'):
        'Numa numa iei!!',
    (1452, 'Numa numa numa yay!!'):
        'Numa numa numa iei!!',

    # --- secondo gradino: il soramimi, parole italiane vere che suonano come
    #     il rumeno, come fa il giapponese
    (1456, 'Vrei sa pleci dar♪'):
        'Brie♪ sale♪ pece♪ dai♪',
    (1456, 'Numa numa yay!!'):
        'Numera♪ numera♪ ehi!♪',
    (1456, 'Numa numa numa yay!!'):
        'Numera♪ numera♪ numera♪ ehi!♪',

    # --- terzo gradino, il piu' scemo dei tre
    (1460, 'Numa numa yay!!'):
        'Una mano♪ una mano♪ ehi!♪',
    (1460, 'Numa numa numa yay!!'):
        'Una mano♪ una mano♪ una mano♪ ehi!♪',

    # --- il fischiettio e il ritornello vero.
    (1465, ' *whistle-whistle* '):
        ' *fiuu-fiuu* ',
    (1468, 'Mai-Ya-Hi♪'):
        'Mai-a-hi♪',
    (1468, 'Mai-Ya-Hoo♪'):
        'Mai-a-hu♪',
    (1468, 'Mai-Ya-Ha Ma Mi A♪'):
        'Mai-a-ho♪',
}
