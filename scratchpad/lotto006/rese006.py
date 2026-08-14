import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- i sei versi di chi incassa un colpo. Stanno tutti sulla STESSA riga,
    #     dentro cnvtalk(): statiche, quindi la resa e' testo nudo.
    # ⚠️ l'inglese di 「くっ！」 dice «Kill me already!», che e' un'altra cosa:
    #    il giapponese e' un mugolio. Reso sul giapponese
    (8007, 'Kill me already!'):
        'Ngh!',
    (8007, 'No... not yet...!'):
        'Non ancora!',
    (8007, "I can't take it anymore..."):
        'Non ce la faccio più...',
    (8007, 'Argh!'):
        'Uuugh',
    (8007, 'Uhhh'):
        'Ah',
    (8007, 'Ugggg'):
        'Aaah',

    # ⚠️ genitivo: «la mente di X»
    (8039, 'Magic reaction hurts !'):
        '"Il contraccolpo del mana colpisce " + name(dmgmp_charid) + " nella mente!"',

    # --- il peso e la statura.
    # copiata da proc.hsp:10612, stesso giapponese. «pesante» non concorda
    (8178, ' gain weight.'):
        'name(modweight_charid) + " diventa più pesante."',
    # ⚠️ ma «più leggero» concorderebbe: girato col verbo
    (8181, ' lose weight.'):
        'name(modweight_charid) + " perde peso."',
    # ⚠️ genitivo: «la statura di X»
    (8197, ' grow taller.'):
        'name(modheight_charid) + " cresce un poco in altezza."',
    (8200, ' grow smaller.'):
        'name(modheight_charid) + " cala un poco in altezza."',

    # --- il vomito e l'anoressia. ⚠️ genitivo: «l'anoressia di X»
    (8211, ' manage to recover from anorexia.'):
        'name(cure_anorexia_charid) + " guarisce dall\'anoressia."',
    (8220, ' vomit.'):
        'name(chara_vomit_charid) + " vomita."',
    # ⚠️ il giapponese dice 異物, «corpo estraneo», non «children»
    (8225, ' spit children from  body!'):
        'name(chara_vomit_charid) + " sputa fuori quello che aveva in corpo!"',
    (8270, ' develop anorexia.'):
        'name(chara_vomit_charid) + " sviluppa l\'anoressia."',
    # stessa forma di chara_func:3543, 健康のお守り e' <Amuleto di Jure>
    (8280, 'But the Amulet of Jure shines brightly for a moment, instantly curing the anorexia.'):
        'Ma l\'<Amuleto di Jure> brilla per un istante e guarisce l\'anoressia sul colpo.',
    # copiata da chara_func:3377, stesso giapponese. E' una riga dello screenshot
    (8317, ' is incontinent.'):
        'name(chara_morasi_arg1) + " se la fa addosso."',

    # --- il nucleo vitale. ⚠️ l'inglese mette _s() dove andava name(): la rete
    #     11 concede un name() solo, quindi il donatore resta implicito
    (8629, ' get genes of .'):
        'name(gain_iden_charaid2) + " acquisisce i geni nel nucleo vitale."',
    (8634, '[Phase 1 progress  %]'):
        '"[Fase 1, avanzamento: " + locvar_gain_iden_sintyoku + "%]"',
    # in giapponese l'intestazione e' gia' in lettere latine: resta com'e'
    (8640, '[SURVIVABILITY EXTENSION !] Phase 1 completed. From now on, it need to grow with the nutrition of foods.'):
        '[SURVIVABILITY EXTENSION!] Fase 1 completata. D\'ora in poi deve crescere con il nutrimento del cibo.',

    # --- i presentimenti del cibo. Due blocchi ricopiati: quattro voci, due rese
    (8655, ' feel bad.'):
        'name(eatstatus_arg2) + " ha un brutto presentimento."',
    (8661, ' feel good.'):
        'name(eatstatus_arg2) + " ha un buon presentimento."',
    (8677, ' feel bad.'):
        'name(eatstatusfood_charaidx) + " ha un brutto presentimento."',
    (8683, ' feel good.'):
        'name(eatstatusfood_charaidx) + " ha un buon presentimento."',
    (8703, ' feel grumpy.'):
        'name(sickifcursed_arg2) + " si sente male."',

    # --- la scissione. ⚠️ un inglese per due giapponesi, e il codice decide:
    #     分身 e' l'ombra del ninja, 分裂 e' la melma che diventa due
    # «si sdoppia» e' gia' di action.hsp:12361, sotto lo stesso inglese
    (8751, ' split!'):
        'name(charaCanSplit_charidx) + " si sdoppia!"',
    (8754, ' split!'):
        'name(charaCanSplit_charidx) + " si divide in due!"',
}
