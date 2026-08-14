import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # copiata da text.hsp:2969, stesso giapponese e stesso inglese
    (172, 'Unknown'):
        'Ignoto',
    # ⚠️ NON e' testo: e' la chiave di ricerca dentro instr(), sul file dei
    #    dialoghi. action.hsp:4816 e text.hsp:9361 la lasciano gia' cosi'
    (748, 'EN'):
        'EN',

    # --- i rapporti con i PNG. Il giapponese usa 「と」, il complemento di
    #     compagnia: «con» non si fonde con l'articolo che cdatan porta dentro.
    (1080, 'Your relation with  becomes <>...'):
        '"Il rapporto con " + cdatan(CDATAN_NAME, modimp_charid) + " diventa <" + locvar_modimp_pp + ">..."',
    (1086, 'Your relation with  becomes <>!'):
        '"Il rapporto con " + cdatan(CDATAN_NAME, modimp_charid) + " diventa <" + locvar_modimp_pp + ">!"',
    # 媚赤蝋燭 e' <Candela di Lulwy> in db_item.hsp:138261
    (1169, 'You drip wax on  from the Candle of Lulwy. \\"Hot hot hot~\\"'):
        '"Fai colare la cera della <Candela di Lulwy> sopra " + cdatan(CDATAN_NAME, modimp2_charid) + ". \\"Ahi ahi ahi~\\""',
    # :1183 e' il rapporto che peggiora, :1189 quello che migliora: lo dice il ramo
    (1183, 'Your master/servant relation with  becomes <>.'):
        '"Il rapporto di servizio con " + cdatan(CDATAN_NAME, modimp2_charid) + " diventa <" + locvar_modimp2_pp + ">."',
    (1189, 'Your master/servant relationship with  becomes <>.'):
        '"Il rapporto di servizio con " + cdatan(CDATAN_NAME, modimp2_charid) + " diventa <" + locvar_modimp2_pp + ">!"',

    # --- tre righe di trama.
    # ⚠️ March e' un nome proprio: girato per non doverne indovinare il genere
    (1294, 'March was destroyed.'):
        'March non esiste più.',
    # ⚠️ il giapponese parla del giocatore in TERZA persona (「あいつ」), quindi
    #    niente participio da accordare. E le virgolette vanno protette
    (1323, '??? says: \\"You.. you really made it this far, huh. We\'re going to have to get serious.\\"'):
        '???: \\"Quello lì... fa sul serio, allora. Tocca usare le maniere forti.\\"',
    (1380, 'Time starts to run again.'):
        'Il tempo riprende a scorrere.',
    (1392, ' more to go.'):
        '"[Sterminio] ne restano " + locvar_check_quest_p + ". "',

    # --- la squadra. 「と」 di nuovo, e «con» di nuovo.
    (1627, ' and  form a tag-team.'):
        'cdatan(CDATAN_NAME, tag_begin_arg1) + " fa squadra con " + cdatan(CDATAN_NAME, tag_begin_arg2) + "."',
    (1641, 'You were disbanded  with .'):
        'cdatan(CDATAN_NAME, tag_end_arg1) + " e " + cdatan(CDATAN_NAME, locvar_tag_end_ttc) + " sciolgono la squadra."',

    # --- la sella. ⚠️ TESTA di frase: la parentesi si chiude a :1665, fuori da
    #     qualunque lang(). La resa finisce con la freccia e lo spazio, come
    #     l'inglese. E il nome sta fra parentesi come ETICHETTA, per non dover
    #     scrivere «la velocita' di X».
    (1654, "You ride . ('s speed: ->"):
        '"Cavalchi " + name(ride_begin_arg1) + ". (" + name(ride_begin_arg1) + ", velocità: " + cdata(CDATA_SPEED, ride_begin_arg1) + " -> "',
    (1657, " rides you. ('s speed: ->"):
        'name(ride_begin_arg1) + " ti sale in groppa. (" + name(ride_begin_arg1) + ", velocità: " + cdata(CDATA_SPEED, ride_begin_arg1) + " -> "',
    # ⚠️ il giapponese giudica la CAVALCATURA, l'inglese parla di te. Il ramo
    #    guarda CHARA_BIT_SUPERIOR_RIDING, cioe' una proprieta' della bestia
    (1668, 'You feel comfortable.'):
        'Questa creatura è perfetta da cavalcare!',
    (1673, 'This creature is too weak to carry you.'):
        'Questa creatura è troppo debole per portarti.',

    # --- il rumore che sveglia, e chi perde la pazienza.
    (1736, ' notice the sound and wake up.'):
        'name(cnt) + " sente il rumore e si sveglia."',
    (1744, ' can no longer put up with it.'):
        'name(cnt) + " perde le staffe."',
    (1746, "That's it."):
        'Adesso basta.',

    # --- le due sparse in fondo. ⚠️ genitivo: «il patto di X»
    (5479, ' lost the effect of contingency.'):
        'name(dmghp_charid) + " vede scadere il patto."',
    # 絶対防衛 e' «Difesa assoluta» in buff.hsp:159
    (5864, '*Absolute protect*'):
        '*Difesa assoluta*',
}
