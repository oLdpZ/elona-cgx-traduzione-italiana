import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- le ultime cinque morti. Log al presente, epigrafe al passato remoto.
    # 闇のゲーム e' il Gioco delle Ombre di Yu-Gi-Oh, non «a card game».
    # ⚠️ «contro» non si fonde con l'articolo che cdatan porta dentro
    (7002, ' was sent to Amur-cage by .'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " perde il Gioco delle Ombre contro " + cdatan(CDATAN_NAME, (DAMAGE_FROM_CARD_GAME - dmghp_source)) + "."',
    (7004, 'lost a card game against  and was sent to Amur-cage'):
        '"perse il Gioco delle Ombre contro " + cdatan(CDATAN_NAME, (DAMAGE_FROM_CARD_GAME - dmghp_source))',
    (7009, ' hang self.'):
        'name(dmghp_charid) + " si impicca."',
    (7011, 'committed suicide by hanging'):
        'si impiccò',
    (7015, ' choke to death.'):
        'name(dmghp_charid) + " muore per soffocamento."',
    (7017, 'choked to death'):
        'morì per soffocamento',
    # rtvaln vale itemname() oppure questo letterale: porta l'articolo dentro
    (7032, 'backpack'):
        'il carico',
    # ⚠️ «schiacciato da lo zaino»: il carico diventa soggetto, come valn nella 36ª
    (7037, '  squashed by .'):
        'rtvaln + " schiaccia " + name(dmghp_charid) + " sotto il peso."',
    # ⚠️ qui il carico NON puo' fare da soggetto (e' il predicato del morto):
    #    «sotto» e' una delle preposizioni che non si fondono
    (7039, 'was squashed by '):
        '"si accasciò sotto " + rtvaln',

    # --- gli eventi che seguono la morte di qualcuno di importante.
    # ネヘルタード e' <Amurdad> in db_creature.hsp:75293
    (7139, 'Amurdad: Alas... It was in vain...'):
        '"<Amurdad>: " + cnvtalk("Non c\'è più niente da fare... che peccato...")',
    # copiate da proc.hsp:241, stesso giapponese
    (7247, 'Removal Point '):
        'Punti ',
    (7247, 'Quota '):
        'Obiettivo ',
    (7279, 'This will likely reduce bear visits a little.'):
        'Così gli orsi si vedranno un poco meno in giro.',
    (7283, 'This will likely reduce bear visits in the future.'):
        'Così in futuro gli orsi si vedranno molto meno in giro.',
    # 神殺し e' «flagello degli dei» in item_data.hsp:1361
    (7319, 'You are the godslayer!'):
        'Ormai sei il flagello degli dèi.',
    # copiata da action.hsp:18728, stesso giapponese
    (7330, '*Duel-Over!*'):
        '*Duello finito!*',

    # --- i sette premi di trama. I nomi fra parentesi quadre stanno gia'
    #     in text.hsp:11576-11630: si copiano, non si ridecidono.
    (7347, "You obtain the [Fool's Magic Stone]!"):
        'Ottieni la [pietra magica del folle]!',
    (7353, "You obtain the [King's Magic Stone]!"):
        'Ottieni la [pietra magica del conquistatore]!',
    (7359, "You obtain the [Sage's Magic Stone]!"):
        'Ottieni la [pietra magica del saggio]!',
    (7448, 'You obtain the [Ankh of The Sun]!'):
        'Ottieni l\'[ankh del sole]!',
    (7454, 'You obtain the [Data Chip]!'):
        'Ottieni il [chip di dati]!',
    (7460, 'You obtain the [Chaos Wings]!'):
        'Ottieni le [ali del caos]!',
    (7473, 'You obtain the [Data Register]!'):
        'Ottieni il [registro di dati]!',
    (7605, 'You obtain the [Rusted Bell]!'):
        'Ottieni il [campanello arrugginito]!',

    # --- la Little Sister, la capsula, le pulizie, l'allarme.
    (7423, 'The Big Daddy had already evacuated the Little Sister somewhere.'):
        '<Big Daddy> aveva già messo al sicuro la <Little Sister> da qualche parte.',
    (7430, 'You have saved Little Sisters  times and killed them  times.'):
        '"<Little Sister> salvate: " + gdata(GDATA_SISTER_SAVED) + ", uccise: " + gdata(GDATA_SISTER_KILLED) + "."',
    (7496, 'You place the lump of purified ether into the recovery capsule.'):
        'Metti il blocco di etere purissimo nella capsula di recupero.',
    # copiata da db_creature.hsp:95327, stesso inglese e stesso senso
    (7512, 'Cleaning completed!'):
        'Pulizie completate!',
    (7644, '*beeeeeep!* An alarm sounds loudly!'):
        '*biiiiip!* Un allarme squilla assordante!',
    (7765, 'You feel sad for a moment.'):
        'Ti prende la tristezza per un istante.',

    # --- il cadavere da cui si scende.
    # ⚠️ «dal cadavere di X» sono due fusioni in una riga, e la rete 11 vuole
    #    tutt'e due i name(). La strada e' l'apposizione.
    (7787, ' get off the corpse of .'):
        'name(CHARA_PLAYER) + " scende di sella e lascia a terra " + name(dmghp_charid) + ", ormai cadavere."',
    (7796, ' took down the corpse of .'):
        'name(CHARA_PLAYER) + " depone a terra con delicatezza " + name(dmghp_charid) + ", ormai cadavere."',
    # 死の宣告 e' «Sentenza di morte» in buff.hsp:71
    (7878, 'The death word breaks.'):
        'La sentenza di morte si annulla.',

    # --- la parodia di Dragon Quest: tutto in hiragana, con gli spazi larghi.
    (7915, ' stood up and offered to join you! Would you like to join ?'):
        '"Incredibile! " + cdatan(0, dmghp_charid) + " si rialza e ti guarda come se volesse unirsi a te! Vuoi accogliere " + cdatan(0, dmghp_charid) + " nel gruppo?"',
    (7934, ' vanish.'):
        '"" + cdatan(0, dmghp_charid) + " se ne va con aria mesta"',
}
