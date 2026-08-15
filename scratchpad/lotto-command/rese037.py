import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Le cinque etichette della finestra dell'inventario (:14211-:14325)
    # ================================================================
    # ⚠️ Tetto 9 caratteri: 60 px fra `:14208` e `:14212`, corpo 11 (`:14203`,
    #    `12 + en - en * 2` con `en = 1`), cioe' 6,6 px a carattere.
    # ⭐ 「部位」 e' gia' «Parte» in :12620 e «Parti» in :1273.
    (14211, 'Equip:'):
        'Parti:',

    # ⚠️⚠️ Il giapponese e' lo STESSO 「 枚」 nei due rami — un puro classificatore
    #    — e la rete 4 pretende una resa sola. Ha ragione: a distinguere e'
    #    `invctrl(1)`, non il testo, e la distinzione la porta gia'
    #    l'INTESTAZIONE della colonna, che :14105 rende «Medagliette» e :14108
    #    «Biglietti». L'inglese, mettendo «Coins» e «Tickets», la ripete due
    #    volte. ✅ «pz.» e' il classificatore italiano e regge anche l'1, che
    #    «pezzi» non reggerebbe.
    (14272, ' Coins'):
        ' pz.',
    (14275, ' Tickets'):
        ' pz.',

    # ⭐ 「足元」 e' «per terra» in :6703, :6707 e map.hsp:9914.
    (14280, ' (Ground)'):
        ' (per terra)',
    # ⭐ 「遠隔」 e' «Tiro» in text.hsp:136, e :15309/:15312 dicono gia' «da Tiro»
    #    e «nel Tiro» parlando di questo stesso slot.
    (14325, ' (Range)'):
        ' (tiro)',

    # ================================================================
    # Piantare i semi (:14487)
    # ================================================================
    # ⚠️ `name_of_seed_planted` (`:14455`, ioriginalnameref) e' SINGOLARE e
    #    `number_of_seeds_planted` puo' valere 1: il numero non puo' stargli
    #    davanti. L'etichetta non concorda con niente e regge tutt'e due i casi.
    (14487, "You've planted  ."):
        '"Semi piantati: " + number_of_seeds_planted + " (" + name_of_seed_planted + ")."',

    # ================================================================
    # Lasciare per terra, i contenitori, il cimitero (:14517-:14595)
    # ================================================================
    # ⚠️ Il ramo e' `inv_getspace(-1) == 0`: e' il TERRENO che non ne prende piu'.
    (14517, "You can't drop items any more."):
        "Non c'è più spazio per terra.",
    (14569, 'The container is full.'):
        'Non ci entra altro.',
    # ⭐ 「霊園」 e' «Cimitero» in text.hsp:50.
    (14576, 'The cemetery is full.'):
        'Il cimitero è pieno.',
    # 💡 Stesso inglese di :14569 su un giapponese diverso (置けない contro
    #    入らない): due contenitori, stesso evento. Resa identica di proposito.
    (14583, 'The container is full.'):
        'Non ci entra altro.',
    # ⚠️ Il giapponese dice 以上, «da tanto in su»; l'inglese lo gira in «less
    #    than». Si segue il giapponese, che e' quello che il codice controlla
    #    (`inv(INV_ITEM_WEIGHT, ci) >= efp * 100`).
    (14590, 'The container can only hold items weighing less than .'):
        '"Non ci entra niente che pesi " + cnvweight(efp * 100) + " o più."',
    # ⭐ 「荷物」 e' la roba del carretto: :15923 dice «Le cose sul carretto».
    (14595, 'The container cannot hold cargos'):
        'Le cose del carretto non ci entrano.',

    # ================================================================
    # L'eredita' (:14616, :14717)
    # ================================================================
    (14616, "You don't have a claim."):
        'Non hai nessun diritto di eredità.',
    # ⭐ Stesso giapponese di action.hsp:3386, ricopiata parola per parola.
    # ⚠️ `_s3(...)` e' morfologia e sparisce col suo argomento: il contratto e'
    #    il solo `gdata` di testa.
    (14717, 'You can claim  more heirloom.'):
        '"Puoi ancora reclamare " + gdata(GDATA_HEIR_DEED) + " oggetti in eredità."',

    # ================================================================
    # Il banco del negozio (:14643-:14692)
    # ================================================================
    # ⚠️⚠️ Tre inglesi identici su tre giapponesi diversi. Il giapponese
    #    distingue nominando l'oggetto con `itemname(ci, 1)`, che la rete 11 non
    #    lascia aggiungere; il VERBO pero' non e' una funzione, e la
    #    distinzione torna con quello. Contratto: `['inv']` in tutt'e tre.
    (14531, 'How many? (1 to )'):
        '"Quanti ne lasci? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',
    (14643, 'How many? (1 to )'):
        '"Quanti ne compri? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',
    (14646, 'How many? (1 to )'):
        '"Quanti ne vendi? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',

    (14668, 'Do you really want to buy  for gp?'):
        '"Vuoi davvero comprare " + itemname(ci, in) + " per " + '
        'in * calcitemvalue(ci, 0) + " gp?"',
    (14671, 'Do you really want to sell  for gp?'):
        '"Vuoi davvero vendere " + itemname(ci, in) + " per " + '
        'in * calcitemvalue(ci, 1) + " gp?"',

    # ⭐ «portafogli»: proc.hsp lo scrive cosi' in :3389, :9474, :9482, :21991
    #    e :21994. La seconda meta' segue l'inglese, che china la testa; il
    #    giapponese dice 「がっかりした」, che e' la stessa cosa detta d'umore.
    (14683, 'You check your wallet and shake your head.'):
        'Apri il portafogli e chini la testa...',
    (14683, 'You need to earn more money!'):
        'Devi guadagnare di più!',
    # ⚠️ `his(tc)` a un argomento e' morfologia e sparisce: resta il solo `name`.
    # 💡 Stessa frase di :14683 in terza persona, perche' qui c'e' `name(tc)`.
    (14692, ' checks  wallet and shakes  head.'):
        'name(tc) + " apre il portafogli e china la testa..."',
}
