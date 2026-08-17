import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4520-:4541 la festa a tempo.
    (4520, 'Your final score is  points!'):
        '"Il punteggio finale è " '
        '+ qdata(QDATA_PARAM2, gdata(GDATA_QUEST_REF)) + " punti!"',
    (4536, 'People had a hell of a good time!'):
        'La festa è stata un successone!',
    (4541, 'The party turned out to be a big flop...'):
        'La festa è finita in un mezzo disastro...',

    # --- :4549-:4554 la consegna (QUEST_TYPE_HARVEST). «consegna» viene da
    # command.hsp:15499, che e' la riga di questo stesso incarico.
    (4549, 'You complete the task!'):
        'Consegna completata!',
    (4554, 'You fail to fulfill your task...'):
        'La consegna non è arrivata in tempo...',

    # --- :4562-:4567 il campo minato (QUEST_TYPE_MINEFIELD). ⚠️ Stesso inglese
    # delle due qui sopra, giapponese diverso: 撤去 e' la rimozione delle mine.
    (4562, 'You complete the task!'):
        'Bonifica completata!',
    (4567, 'You fail to fulfill your task...'):
        'La bonifica non è finita in tempo...',

    # --- :4572 la caccia (QUEST_TYPE_CONQUER). ⚠️ Impersonale come il
    # giapponese: «non sei riuscito» porterebbe un participio col genere.
    (4572, 'You failed to slay the target...'):
        'La caccia è fallita...',

    # --- :4616 la citazione da BioShock. I due nomi stanno gia' cosi', fra
    # parentesi angolari, e «Mr Bubbles» si scrive senza il punto
    # (db_creature.hsp:124283, :124289, :124385).
    (4616, 'The Little Sister slips from the Big Daddy\'s shoulder. \\"Mr. Bubbles!\\"'):
        '<Little Sister> scivola dalla spalla di <Big Daddy>. \\"Mr Bubbles!\\"',

    # --- :4622-:4712 le sette battute degli dèi prima del Ragnarok, una per
    # divinita': Lulwy, Ehekatl, Opatos, Kumiromi, Mani, Jure, Itzpalt.
    (4622, 'Fool... Prepare to die!!!'):
        'Che sciocchezza... preparati a morire!!!',
    # Ehekatl e' la dea gatta: e' un verso, non una frase.
    (4652, 'memememw...MEMEMEM...MEWWWWWW!'):
        'mimimi... MIMIMI... MIAAAAAO!',
    (4664, '...Muwahahaha...wahahahaha!'):
        '...Muahahaha... uahahahahah!',
    (4676, "I absolutely... can't forgive...!!!"):
        'Non ti perdono... mai e poi mai...!!!',
    (4688, 'Come, let us bring this farce to a close!!!'):
        'Su, facciamo calare il sipario!!!',
    # Jure e' la dea che guarisce, e la battuta e' sua: la stupidita' non si cura.
    (4700, "I-if you won't die, then my only choice is to heal your foolishness!!!"):
        'S-se proprio non vuoi morire, allora ti curo io la stupidità!!!',
    # ⚠️ `he(cc)` con un argomento e' morfologia e sparisce: la chiusa segue il
    # giapponese, 「今こそ、あるべき姿へと還るのだ！」, che quel pronome non ce l'ha.
    # ⚠️⚠️ Ma la voce resta DINAMICA, perche' e' il ramo inglese a dirlo: la resa
    # va scritta come espressione HSP, fra virgolette, anche se di funzioni non
    # ne resta nessuna. Senza, `applica.py` la scriverebbe come codice (37ª).
    (4712, 'Roaring flames! Biting cold! Savage lightning! Return this fool to the dust from whence  came!'):
        '"Fiamme, turbinate! Gelo, avvolgi! Folgore, guizza! '
        'È ora di tornare alla forma che ti spetta!"',
}
