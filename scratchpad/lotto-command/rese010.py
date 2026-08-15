import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1575-:1623 i diciassette pensieri di sempre, `rnd(17)`.
    (1575, 'Not thinking anything in particular'):
        'Non sto pensando a niente in particolare',
    (1578, 'Want more stimulation'):
        'Voglio più emozioni',
    (1581, 'Remember old things'):
        'Sto ripensando ai vecchi tempi',
    (1584, 'Am I OK?'):
        'Ma vado bene così come sono?',
    # ⚠️ il giapponese e' la barzelletta: PENSA di non pensare a niente
    (1587, 'Do not think about anything!'):
        'Sto pensando di non pensare a niente',
    (1590, 'I know that you are looking into my heart!'):
        'Lo so che mi stai leggendo nel pensiero!',
    # ⚠️ «vorrei essere capito» concorderebbe col compagno
    (1593, 'Want you to understand more about myself'):
        'Vorrei che mi capissi di più',
    (1596, 'Concerned about the weather!'):
        'Mi preoccupa il tempo',
    (1599, 'Worried about my family'):
        'Sono in pensiero per la famiglia',
    (1602, 'Very bored'):
        'Che noia mortale',
    (1605, 'Forgetting something...'):
        'Ho la sensazione di scordare qualcosa...',
    (1608, 'Eyes slightly itchy'):
        'Mi prudono gli occhi',
    (1611, 'Why will the gaps not disappear?'):
        'Perché le disuguaglianze non spariscono?',
    (1614, 'Thinking about the meaning of living'):
        'Sto pensando al senso della vita',
    (1617, 'Absolutely want it...'):
        'Voglio quella cosa, a tutti i costi...',
    # ⚠️ «vorrei sentirmi amato» concorderebbe col compagno
    (1620, 'Want to feel love'):
        "Ho bisogno di sentire l'amore",
    (1623, 'What was the dream last time?'):
        'Che voleva dire quel sogno?',

    # --- :1626-:1638 la fame. ⚠️ l'inglese passa alla terza persona a meta'
    #     blocco («Wants to eat a lot»), il giapponese no.
    (1626, 'Hungry and has no strength.'):
        'Ho fame, non ho più forze',
    (1629, 'Want to eat anything'):
        'Qualunque cosa, purché sia cibo',
    (1632, 'Wants to eat a lot'):
        'Voglio mangiare qualcosa di sostanzioso',
    (1635, 'Wants a sweet one'):
        'Voglio qualcosa di dolce',
    (1638, 'Want to eat delicious home cooking'):
        'Voglio un piatto fatto in casa, e buono',

    # --- :1643-:1652 la sete.
    (1643, 'Looks completely dried up'):
        'Sto per seccarmi',
    # ⚠️ 「喉がカラカラ」 e' la gola secca, non la gola che fa male
    (1646, 'My throat hurts'):
        'Ho la gola secca',
    (1649, 'Seems disoriented from the lack of water'):
        'Mi gira la testa dalla sete',
    (1652, 'W-Water...'):
        'A-Acqua...',

    # --- :1657-:1673 l'affetto: tre pensieri se ti vuole bene, tre se e' al
    #     massimo (`EVOCHAT_POINTS == 10`).
    (1657, 'I can work hard today'):
        'Oggi mi sento di dare il massimo',
    (1660, 'Happy'):
        'Non sto più nella pelle',
    (1663, 'Such a life is not bad either'):
        'Anche una vita così non è male',
    # ⚠️ 「のろけたい」 e' vantarsi del proprio amore, non di una persona
    (1667, 'Want to brag about someone'):
        'Vorrei raccontare a tutti il mio amore',
    (1670, 'Very happy!'):
        'Sono al settimo cielo!',
    (1673, 'I am glad that I am alive'):
        'Ne è valsa la pena, di vivere fin qui',

    # --- :1678-:1696 i sette caratteri in combattimento, uno per `CDATA_TONE`.
    #     ⚠️ vanno tenuti distinti fra loro: vedi il docstring.
    (1678, 'I will never lose'):
        'Non perderò mai',
    (1681, 'Only enemies are beaten'):
        'I nemici si abbattono e basta',
    (1684, 'I will fight as usual'):
        'Faccio come sempre e andrà bene',
    (1687, 'Anxious about defeat'):
        'E se non ce la faccio?',
    (1690, 'No possibility of lose'):
        'Non posso perdere',
    # ⚠️ 「いざ尋常に勝負！」 e' lingua da duello antico
    (1693, "Let's fight squarely"):
        'E ora, un duello leale!',
    (1696, 'Sure works well'):
        'Qualcosa si risolverà',
}
