import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # La coppia da combattimento (:7178-:7218)
    # ⭐ 「タッグパートナー」 e' gia' «compagno di coppia»: action.hsp:1024 e
    #    :1877-:1889.
    # ================================================================
    # 「滞在中の仲間」 e' l'alleato assegnato a un'area (CDATA_AREA != AREA_NONE).
    (7178, 'The ally currently stays in this area.'):
        "Un compagno assegnato a un'area non può fare coppia.",
    # ⚠️⚠️ L'inglese dice un'altra cosa («There's no place.»), ma la voce e'
    #    tipata STATICA — l'inglese non ha funzioni dove il giapponese ha
    #    cdatan() — quindi la resa non puo' nominare nessuno. Vedi il docstring.
    (7191, "There's no place."): 'Ha già un compagno di coppia.',
    (7218, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + '
        'skillname(SKILL_SPACT_TAG_FORCE) + "."',

    # ================================================================
    # La raccolta dei pezzi (:7242-:7308)
    # ⚠️ name() non sta MAI dopo una preposizione: e' «il viandante», e «da il
    #    viandante» non si scrive. Vedi il docstring e la rete 8.
    # ================================================================
    # ⚠️ L'inglese parla di LATTE, ma il ramo copre p da 18 a 22. Il giapponese
    #    e' generico e la resa lo segue.
    (7242, 'If you squeeze more milk,  will die. Will you stop?'):
        '"Insistere potrebbe uccidere " + name(tc) + ". Vuoi lasciar perdere?"',

    # --- la serie 「無理やり」, quella dopo l'avvertimento di :7242.
    (7249, 'You take out a bone from .'):
        'name(tc) + " perde un osso, strappato via a forza."',
    # ⚠️ «il proprio cuore» e non «il cuore»: «perdere il cuore» vuol dire
    #    innamorarsi.
    (7255, 'You take out a heart from .'):
        'name(tc) + " perde il proprio cuore, strappato via a forza."',
    (7261, 'You take out an eye from .'):
        'name(tc) + " perde un occhio, cavato via a forza."',
    (7267, 'You take out blood from .'):
        'name(tc) + " perde sangue, spremuto via a forza."',
    # ⚠️ «tutta la pelle» e non «la pelle»: «rimetterci la pelle» vuol dire
    #    morire.
    (7273, 'You take out some skin from .'):
        'name(tc) + " perde tutta la pelle, strappata via a forza."',

    # --- la serie ordinaria, senza 「無理やり」.
    (7284, 'You take out a bone from .'):
        'name(tc) + " perde un osso."',
    (7290, 'You take out a heart from .'):
        'name(tc) + " perde il proprio cuore."',
    (7296, 'You take out an eye from .'):
        'name(tc) + " perde un occhio."',
    (7302, 'You take out blood from .'):
        'name(tc) + " perde sangue."',
    (7308, 'You take out some skin from .'):
        'name(tc) + " perde tutta la pelle."',

    # ================================================================
    # L'immagine del personaggio (:7332-:7340)
    # ================================================================
    # ⚠️ Il giapponese spiega anche che con 1 si torna alla predefinita, e
    #    l'inglese lo perde. Statica, nessun contratto: la resa lo tiene.
    (7332, 'Input the number of Pic_ . (48*48→2-16 48*96→17-32)'):
        "Numero dell'immagine? (48*48: da 2 a 16; 48*96: da 17 a 32. Con 1 "
        'torna quella predefinita.)',
    (7340, 'You put back the original graphic.'):
        "Rimetti l'immagine di prima.",
}
