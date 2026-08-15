import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :10495 la colonna di destra in cima. Budget 60 px.
    (10495, 'Next Lv'):
        'Prossimo',
    # ⭐ copiata: skill.hsp:347 rende 「信仰」 «Fede»
    (10495, 'God'):
        'Fede',
    (10495, 'Guild'):
        'Gilda',
    (10495, 'Growth'):
        'Crescita',

    # --- :10504 la prima colonna. Budget 38 px: al massimo sei caratteri.
    (10504, 'Aka'):
        'Alias',
    (10504, 'Race'):
        'Razza',
    # ⚠️ rete 3: text.hsp:191 scrive «sesso» minuscolo, ma li' e' dentro una
    #    frase. Qui e' l'intestazione di una colonna.
    (10504, 'Sex'):
        'Sesso',
    (10504, 'Class'):
        'Classe',

    # --- :10504 la seconda colonna. Budget 50 px.
    (10504, 'Age'):
        'Età',
    (10504, 'Height'):
        'Altezza',
    (10504, 'Weight'):
        'Peso',
    # 💡 INIT sono i tiri iniziali: :10657 somma CDATA_INIT_LIFEMANA e _ATTR
    (10504, 'INI'):
        'Iniz.',
    # 💡 invariato dichiarato in invariati.md: il giapponese e' 「ＡＰ」
    (10504, 'AP'):
        'AP',

    # --- :10517 la colonna centrale. Budget 55 px.
    # 💡 invariato dichiarato in invariati.md: il giapponese scrive HP/MP uguale
    (10517, 'HP/MP'):
        'HP/MP',
    # ⭐ copiate: skill.hsp:9, :14, :59
    (10517, 'Life'):
        'Vita',
    (10517, 'Mana'):
        'Mana',
    (10517, 'InSAN'):
        'Follia',
    (10517, 'Speed'):
        'Velocità',
    (10517, 'Fame'):
        'Fama',
    (10517, 'Karma'):
        'Karma',
    (10517, 'Rating'):
        'Potenza',
    (10517, 'Melee'):
        'Mischia',
    # ⭐ copiata: text.hsp:136 rende `Shoot` «Tiro»
    (10517, 'Shoot'):
        'Tiro',

    # --- :10526 la colonna in basso a sinistra. Budget 57 px.
    (10526, 'Cargo Wt'):
        'Carico',
    (10526, 'Cargo Lmt'):
        'Limite',
    # ⭐ stessa sigla di :14193 nel lotto 002
    (10526, 'Equip Wt'):
        'Peso eq.',
    # ⚠️ rete 4: stesso giapponese 「ターン」 di :10754, e la resa dev'essere una
    #    sola. Lo spazio serve li' e qui e' un rientro di tre pixel.
    (10526, 'Turns'):
        ' Turni',
    (10526, 'Time'):
        'Tempo',

    # --- :10609 il segno di percentuale della crescita.
    # 💡 attaccato al numero come nel giapponese: cosi' non coincide con
    #    l'inglese, che ci mette uno spazio davanti
    (10609, ' %'):
        '%',

    # --- :10621-:10627 le tre gilde. ⭐ parola per parola init.hsp:373-:379.
    (10621, 'Mages Guild'):
        'Gilda dei Maghi',
    (10624, 'Fighters Guild'):
        'Gilda dei Guerrieri',
    (10627, 'Thieves Guild'):
        'Gilda dei Ladri',

    # --- :10730-:10734 le tre sigle del riquadro di destra.
    # ⚠️ abbreviate perche' il riquadro e' stretto, non perche' la resa cambi:
    #    «Schivata» e' skill.hsp:307 e vuole 46 px dove ce ne sono 43
    (10730, 'Prot'):
        'Prot.',
    (10732, 'Evade'):
        'Schiv.',
    (10734, 'SpellPow'):
        'Pot. magia',

    # --- :10754 il contatore dei turni. ⚠️ vedi :10526.
    (10754, ' Turns'):
        ' Turni',

    # --- :10814-:10847 il piede della scheda e le intestazioni della lista.
    (10814, "This character isn't currently blessed or hexed."):
        'Adesso non ha nessun effetto attivo.',
    # ⚠️ 33 px soli: «Spiegazione:» ne vorrebbe settanta
    (10837, 'Desc:'):
        'Info:',
    (10845, 'Lv(Potential)'):
        'Lv(potenziale)',
    (10847, 'Detail'):
        'Effetto',

    # --- :10948 il prefisso delle resistenze nella lista abilita'.
    (10948, 'Resist '):
        'Res. ',
}
