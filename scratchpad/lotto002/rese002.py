import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- l'azione ostile: due righe che partono a ogni colpo dato in citta'.
    # ⚠️ il giapponese dice solo 「嫌な顔をした」: l'inglese ci aggiunge «at you»,
    #    ma il ramo non sa chi sia la sorgente. Reso sul giapponese.
    (2021, ' glares at you.'):
        'name(hostileaction_target) + " storce il naso."',
    (2047, ' gets furious!'):
        'name(hostileaction_target) + " va su tutte le furie!"',
    # 家畜 e' «bestiame», come in db_item.hsp:137486
    (2067, 'The livestock got excited!'):
        'Il bestiame si agita!',
    # copiata da adv.hsp:18, stesso giapponese e stesso inglese
    (2101, ' cancel  action.'):
        'name(cnt) + " interrompe l\'azione."',
    # ⚠️ l'inglese dice «Incognito» (il buff), il giapponese 「変装」 (la cosa):
    #    buff.hsp:1020 la rende gia' «Travestimento»
    (2122, 'Incognito does not work for the duel opponent.'):
        'Durante un duello il travestimento non funziona.',

    # --- l'aggiunta di un buff: cosa lo ferma, cosa lo attenua, cosa lo chiude.
    (2248, 'But it produces no effect.'):
        'Ma non produce alcun effetto.',
    # riga di debug: stampa un numero
    (2260, 'Buff Power:.'):
        '"Potenza: " + locvar_addbuff_bpower + "."',
    # ホーリーヴェイル e' <Velo sacro> in buff.hsp:47
    # ⚠️ rete 13: :2280 e :2298 hanno lo STESSO inglese e due giapponesi diversi.
    #    防いだ = respinta (il codice fa `return`); 弱めた = attenuata (il codice
    #    accorcia la durata). Vedi il docstring.
    (2280, 'The holy veil repels the hex.'):
        'Il velo sacro respinge la maledizione.',
    # copiata da action.hsp:8844 e proc.hsp:9322, stesso giapponese
    (2288, ' resist the hex.'):
        'name(addbuff_charid) + " resiste."',
    (2298, 'The holy veil repels the hex.'):
        'Il velo sacro attenua la maledizione.',
    # ⚠️ :2310 e' RINVIATA: sta dentro un blocco /* ORIGINAL */ spento dal mod,
    #    ed e' testo che il giocatore non legge mai. Vedi il docstring.
    (2404, 'The effect of  ends.'):
        '"L\'effetto di " + buffname(delbuff_buffid) + " svanisce."',

    # --- le undici resistenze che SALGONO (resistmod, txtef COLOR_GREEN).
    #     ⚠️ il giapponese dice 「name の身体は…」, 「name の魂は…」: il genitivo
    #     davanti a name() non esiste. La strada e' il dativo riflessivo, che
    #     lascia il possesso implicito e sposta l'accordo su un nome di genere
    #     fisso. Le stesse ventidue rese tornano identiche in resistmodh.
    (2675, 'Suddenly,  feel very hot.'):
        '"D\'improvviso " + name(resistmod_charid) + " si sente il corpo in fiamme."',
    (2678, 'Suddenly,  feel cool.'):
        '"D\'improvviso " + name(resistmod_charid) + " si sente il corpo di ghiaccio."',
    (2681, '  struck by an electric shock.'):
        '"Una scarica elettrica percorre " + name(resistmod_charid) + "."',
    (2684, 'Suddenly,  mind becomes very clear.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha la mente limpida."',
    (2687, ' nerve is sharpened.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha i nervi saldi."',
    (2690, ' no longer fear darkness.'):
        '"D\'improvviso " + name(resistmod_charid) + " non teme più il buio."',
    (2693, ' eardrums get thick.'):
        'name(resistmod_charid) + " non bada più al frastuono."',
    (2696, 'Suddenly,  understand chaos.'):
        '"D\'improvviso " + name(resistmod_charid) + " comprende il caos."',
    (2699, ' now  antibodies to poisons.'):
        'name(resistmod_charid) + " regge meglio i veleni."',
    (2702, '  no longer afraid of hell.'):
        'name(resistmod_charid) + " sente l\'anima avvicinarsi all\'inferno."',
    (2705, ' body is covered by a magical aura.'):
        'name(resistmod_charid) + " si sente la pelle avvolta in un\'aura magica."',

    # --- le undici resistenze che SCENDONO (resistmod, txtef COLOR_PURPLE).
    (2711, ' sweat.'):
        '"D\'improvviso " + name(resistmod_charid) + " comincia a sudare."',
    (2714, ' shiver.'):
        '"D\'improvviso " + name(resistmod_charid) + " sente un brivido di freddo."',
    (2717, '  shocked.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha la pelle sensibile all\'elettricità."',
    (2720, ' mind becomes slippery.'):
        'name(resistmod_charid) + " non ha più la mente limpida di prima."',
    (2723, ' become dull.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha i nervi a pezzi."',
    (2726, 'Suddenly,  fear darkness.'):
        '"D\'improvviso " + name(resistmod_charid) + " teme il buio."',
    (2729, ' become very sensitive to noises.'):
        '"D\'improvviso " + name(resistmod_charid) + " trova assordante ogni rumore."',
    (2732, ' no longer understand chaos.'):
        'name(resistmod_charid) + " non comprende più il caos."',
    (2735, ' lose antibodies to poisons.'):
        'name(resistmod_charid) + " regge peggio i veleni."',
    (2738, '  afraid of hell.'):
        'name(resistmod_charid) + " sente l\'anima allontanarsi dall\'inferno."',
    (2741, 'The magical aura disappears from  body.'):
        'name(resistmod_charid) + " si sente svanire l\'aura magica dalla pelle."',

    # --- resistmodh: le stesse ventidue righe, ricopiate parola per parola da
    #     upstream con l'unica differenza del nome della variabile. Le rese
    #     devono coincidere nei letterali, e la rete 4 lo pretende.
    (2769, 'Suddenly,  feel very hot.'):
        '"D\'improvviso " + name(resistmodh_charid) + " si sente il corpo in fiamme."',
    (2772, 'Suddenly,  feel cool.'):
        '"D\'improvviso " + name(resistmodh_charid) + " si sente il corpo di ghiaccio."',
    (2775, '  struck by an electric shock.'):
        '"Una scarica elettrica percorre " + name(resistmodh_charid) + "."',
    (2778, 'Suddenly,  mind becomes very clear.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha la mente limpida."',
    (2781, ' nerve is sharpened.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha i nervi saldi."',
    (2784, ' no longer fear darkness.'):
        '"D\'improvviso " + name(resistmodh_charid) + " non teme più il buio."',
    (2787, ' eardrums get thick.'):
        'name(resistmodh_charid) + " non bada più al frastuono."',
    (2790, 'Suddenly,  understand chaos.'):
        '"D\'improvviso " + name(resistmodh_charid) + " comprende il caos."',
    (2793, ' now  antibodies to poisons.'):
        'name(resistmodh_charid) + " regge meglio i veleni."',
    (2796, '  no longer afraid of hell.'):
        'name(resistmodh_charid) + " sente l\'anima avvicinarsi all\'inferno."',
    (2799, ' body is covered by a magical aura.'):
        'name(resistmodh_charid) + " si sente la pelle avvolta in un\'aura magica."',
    (2805, ' sweat.'):
        '"D\'improvviso " + name(resistmodh_charid) + " comincia a sudare."',
    (2808, ' shiver.'):
        '"D\'improvviso " + name(resistmodh_charid) + " sente un brivido di freddo."',
    (2811, '  shocked.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha la pelle sensibile all\'elettricità."',
    (2814, ' mind becomes slippery.'):
        'name(resistmodh_charid) + " non ha più la mente limpida di prima."',
    (2817, ' become dull.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha i nervi a pezzi."',
    (2820, 'Suddenly,  fear darkness.'):
        '"D\'improvviso " + name(resistmodh_charid) + " teme il buio."',
    (2823, ' become very sensitive to noises.'):
        '"D\'improvviso " + name(resistmodh_charid) + " trova assordante ogni rumore."',
    (2826, ' no longer understand chaos.'):
        'name(resistmodh_charid) + " non comprende più il caos."',
    (2829, ' lose antibodies to poisons.'):
        'name(resistmodh_charid) + " regge peggio i veleni."',
    (2832, '  afraid of hell.'):
        'name(resistmodh_charid) + " sente l\'anima allontanarsi dall\'inferno."',
    (2835, 'The magical aura disappears from  body.'):
        'name(resistmodh_charid) + " si sente svanire l\'aura magica dalla pelle."',

    # --- la malattia dell'etere. 「エーテル病」 e' «malattia dell'etere»
    #     in text.hsp:10113.
    (2864, 'You show signs of Ether Disease.'):
        'Compaiono i primi sintomi della malattia dell\'etere.',
    # copiata da proc.hsp:25789: stesso giapponese, identico
    (2903, 'Your disease is getting worse.'):
        'L\'etere ti corrode il corpo.',
    (2991, 'The symptoms of the Ether Disease seem to calm down.'):
        'La corrosione dell\'etere si attenua.',
}
