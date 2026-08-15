import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4758-:4768 le tre feste.
    (4758, 'I wish you a Happy New Year!'): 'Auguri anche a te.',
    # ⭐⭐ l'inglese butta via la battuta: il giapponese chiede se il Natale non
    #    sia stato annullato anche quest'anno. È una statica, nessun contratto di
    #    funzioni: la resa segue il giapponese. Vedi il docstring.
    (4764, 'Merry Christmas!'):
        'Eh? Ma il Natale non è stato annullato anche quest\'anno?',
    (4768, 'Here you are.'): 'E va bene, non si può proprio dirti di no...',

    # --- :4778-:4785 il personaggio segreto e il rimpatrio.
    (4778, "T-there's no such thing!"):
        'M-ma figurati se esiste una cosa del genere!',
    (4785, 'Please calm. Here, we return.'): 'Su, su, calma. Tutti a casa.',

    # --- :4798-:4826 i sette dèi maggiori che spariscono.
    #     ⭐ il registro è quello riscosso in :4497-:4540 (lotto 028).
    (4798, 'Haa! What you did unto me, turned you into my destined opponent...'):
        'Ha! Che io mi metta a fare sul serio contro un mortale...',
    # ⚠️ 「はなさんかいボケェ！」 è «mollami, deficiente!»: l'inglese dice un'altra cosa.
    (4802, 'Count your days, stupid!'): 'Mollami, deficiente!',
    # ⭐ «idiota» non ha genere in italiano, e action.hsp:14058 lo mette già in
    #    bocca a Jure. Il giocatore può essere uomo o donna.
    (4806, 'I HATE YOU!... Idiot!'): 'Ti odio! ...idiota.',
    (4810, 'The joy, it fades...'): '...Mi hai fatto passare il divertimento.',
    (4814, 'Muhan! Muha...!'): 'Muahaan! Muah!',
    (4818, "It can't end like this..."): 'Così non mi basta...',
    (4822, 'Oh, are you putting an end to it?'): 'Oh, cala il sipario qui?',
    # 「フシャーッ！」 è il soffio di un gatto: db_creature.hsp:91012 ha lo stesso
    # inglese per un fruscio, e sono due cose diverse. Gli spazi sono dell'inglese.
    (4826, ' *Hiss* '): ' *fsss* ',

    # --- :4832-:4855 le parole chiave: `instr` sul desiderio digitato.
    #     ⭐ ognuna è il nome dell'oggetto come sta in db_item.hsp, perché è quello
    #        che il giocatore legge sullo schermo prima di ricopiarlo.
    (4832, 'skill ticket'): "biglietto d'abilità",
    (4837, 'A  appears at your feet.'):
        'itemname(ci) + " rotola fino ai tuoi piedi."',
    (4846, 'card'): 'carta',
    (4849, 'figure'): 'statuetta',
    (4852, 'golden doll'): 'bambola dorata',
    (4855, 'flesh doll'): 'bambola di carne',

    # --- :4941-:4949 il negozio della dea.
    (4941, 'It does not come out now, please be patient with this.'):
        'Uhm. Adesso non ne escono, accontentati di questo.',
    (4949, "It's sold out."): 'Ah, quello è esaurito.',
}
