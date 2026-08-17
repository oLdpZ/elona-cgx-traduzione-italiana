import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4006-:4013 il Figlio del Caos compare. ⚠️ Niente participi riferiti
    # al giocatore: «doveva succedere» e non «saresti arrivato».
    (4006, 'Your arrival here was inevitable... sooner or later.'):
        'Era già scritto... prima o poi doveva succedere.',
    (4007, 'Space within the room distorts, and an elegant young man appears before you.'):
        'Lo spazio della stanza si deforma, e davanti a te compare un giovane di bell\'aspetto.',
    (4008, "For us, it's merely one facet of a vast, complex system, but I believe you humans know it as 'fate'?"):
        'Per noi è solo una faccia di un sistema immenso e intricato; ma voi umani, '
        'se non sbaglio, lo chiamate destino.',
    (4011, 'You earnestly attempt to suppress the shaking in your legs, but it proves difficult.'):
        'Cerchi con tutte le forze di fermare il tremito alle gambe, ma non ci riesci.',
    (4012, "The shadow of the young man with an elegant face is not a man's shadow."):
        "L'ombra di quel giovane dal viso gentile non è l'ombra di un uomo.",
    (4013, 'From the depths of his innocent eyes, you feel immeasurable strength and darkness.'):
        'In fondo a quegli occhi innocenti senti una forza e un buio senza fondo.',

    # --- :4016-:4031 il dono del tesoro. 「盟約」 e' il «Patto Eterno»
    # (db_creature.hsp:46255), 「秘宝」 il «tesoro segreto» (db_item.hsp:143525).
    (4016, 'The young man gestures at the corpse of Zeome with an ironic smile.'):
        'Il giovane indica il cadavere di Zeome con un sorriso ironico.',
    (4017, 'In accordance with the oath of the Eternal League of Nefia, the item that was guarded by this pathetic old man is now yours.'):
        'In virtù del Patto Eterno di Nefia, quel che questo povero vecchio custodiva '
        'da adesso è tuo.',
    (4020, 'You cast a suspicious gaze at the gorgeously adorned book resting on the pedestal as the man begins to speak to it...'):
        'Guardi con diffidenza il libro riccamente ornato posato sul piedistallo, '
        "mentre l'uomo comincia a parlargli...",
    (4025, 'The young man laughs and leans against the wall, wearing a mischievous smile.'):
        'Il giovane ride e si appoggia al muro, con un sorriso malizioso.',
    (4031, "...An unknown amount of time passes. The man with the terrifying eyes vanished while you weren't looking. You shake off your uncertainty, slowly reaching your hand out to the book..."):
        "...Chissà quanto tempo è passato. L'uomo dagli occhi di ghiaccio è sparito "
        "senza che te ne accorgessi. Scacci l'inquietudine e allunghi piano la mano "
        'verso il libro...',

    # --- :4048-:4050 lo striscione della vittoria. L'ordine dei due `cdatan` e'
    # quello inglese: la rete 11 confronta l'insieme, non la posizione.
    # ⚠️ «Benedizione a te, X» e non «Benedizione su X»: la rete 8 vieta una
    # preposizione che si fonde attaccata a `cdatan`, e ha ragione in generale —
    # per un PNG quel nome porta l'articolo. Il pronome scioglie il nodo.
    (4048, "Blessing to , ! You've finally acquired the codex!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente in mano il tesoro segreto di Lesimas!"',
    # Gli asterischi restano, come per *Sconfitta ai punti* di :3024.
    (4050, '*Win*'):
        '*Vittoria*',

    # --- :4060-:4073 il quadro del cammino: un tabellone, non un paragrafo.
    # Sei `mes` separati da righe vuote, dentro display_window 60,70,680,488.
    (4060, 'Trace'):
        'Il cammino verso la vittoria',
    (4065, 'In the year , /, you arrived at North Tyris.'):
        '"Anno " + 517 + ", " + 12 + "/" + 8 + ": arrivo a Tyris del Nord."',
    # ⚠️ Il `\n` c'e' anche nell'inglese, e serve: la riga non ci sta.
    (4067, "You've killed  creatures and reached\\nmaximum of  level of dungeons."):
        '"Creature uccise: " + gdata(GDATA_KILLED) '
        '+ ".\\nLivello di sotterraneo più profondo: " '
        '+ cnvrank(gdata(GDATA_DEEPEST)) + "."',
    (4068, 'Your score is  points now.'):
        '"Punteggio attuale: " + calcscore() + " punti."',
    (4070, 'In the year , /, you conquered Lesimas.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista di Lesimas."',
    (4071, 'Upon killing Zeome, you said, '):
        '"Uccidendo Zeome hai detto: " + cnvtalk("" + wincomment)',
    (4073, 'Your journey continues...'):
        'Il tuo viaggio non finisce qui...',

    (4092, 'Do you want to watch this event again?'):
        'Vuoi rivedere la scena?',
    # 「レミード」 e' «le Rovine di Remido» ovunque nel gioco (text.hsp:2979).
    (4105, 'Unbelievable! You conquered Remido!'):
        'Incredibile! Hai conquistato le Rovine di Remido!',
}
