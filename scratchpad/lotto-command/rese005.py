import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- 「旅に出る」: si parte per un viaggio. Ventidue voci.
    (9597, 'You left on adventure to find yourself.'):
        'In viaggio per ritrovare se stessi.',
    (9600, 'You left on adventure lightheartedly.'):
        'In viaggio così, senza un vero perché.',
    (9612, 'You left on adventure to find a missing person.'):
        'In viaggio sulle tracce di uno scomparso.',
    (9627, 'You left on adventure to distract yourself from broken heart.'):
        'In viaggio per dimenticare un amore finito.',
    (9630, 'You left on adventure to work towards world peace.'):
        'In viaggio per la pace nel mondo.',
    (9633, 'You left on adventure to work towards global domination.'):
        'In viaggio per conquistare il mondo.',
    (9642, 'You left on adventure due to a revelation from god.'):
        'In viaggio dopo una rivelazione divina.',
    (9660, 'You left on adventure to flee from your past.'):
        'In viaggio per fuggire dal passato.',
    (9669, 'You left on adventure in search of atonement.'):
        'In viaggio per espiare una colpa.',
    (9678, 'You left on adventure to pursue the mysteries of old era.'):
        'In viaggio dietro ai misteri degli antichi.',
    (9690, 'You set out on a journey to find a way to lift a curse.'):
        'In viaggio per sciogliere una maledizione.',
    (9693, 'You set out on a journey to seek avenging on some person .'):
        'In viaggio sulle tracce di una vendetta.',
    (9708, 'You set out on a journey to change a terrible future.'):
        'In viaggio per cambiare un futuro pessimo.',
    (9711, 'You set out on a journey in search of someone to marry.'):
        'In viaggio in cerca di chi sposare.',
    (9723, 'You set out on a journey to restore your clan.'):
        'In viaggio per far risorgere il casato.',
    (9729, 'You went on a journey to show yourself off.'):
        'In viaggio per farsi ammirare.',
    # ⚠️ 「修行の旅」 e' l'allenamento, non il vagabondaggio. «forti» al plurale
    #    perche' l'impersonale «farsi» non ha genere.
    (9621, 'You left on adventure to become stronger.'):
        'In viaggio per allenarsi e diventare più forti.',
    # ⚠️ 「出稼ぎ」 e' andare a guadagnare fuori, non l'avventura
    (9618, 'You left on adventure to find better work.'):
        'Fuori a guadagnarsi il pane.',
    # ⚠️ 「命令されて」: l'ordine viene da altri. «ricevuto» concorda con `ordine`.
    (9624, 'You left on adventure to travel the world.'):
        'Per ordine altrui, un giro fra i vari paesi.',
    # ⚠️ 「逃亡する」 e' la fuga, non la partenza. «morto» concorderebbe.
    (9639, 'You left on adventure because you feared for your life.'):
        'In fuga da chi ti vuole uccidere.',
    (9714, 'You are traveling around, wanting to see a wider world.'):
        'In giro per il mondo, per vederlo tutto.',
    (9696, 'You are investigating the world to gather intelligence.'):
        'Indagini in giro per il mondo, a caccia di notizie.',

    # --- 「冒険に出る」: si parte per l'avventura. Nove voci.
    (9603, 'You left on adventure to fulfill an important promise.'):
        "All'avventura per tenere fede a una promessa.",
    (9609, 'You left on adventure for the excitement.'):
        "All'avventura in cerca di emozioni.",
    # ⚠️ 「ロマン」 e' la meraviglia, il sogno d'avventura: l'inglese legge «romance»
    (9615, 'You left on adventure to find romance.'):
        "All'avventura in cerca di meraviglie.",
    # ⚠️ «guidati dal destino» concorderebbe: il destino agisce, non chi lo segue
    (9636, 'You left on adventure because it was your destiny.'):
        "All'avventura, per mano del destino.",
    (9663, 'You left on adventure to protect something precious.'):
        "All'avventura per difendere ciò che conta.",
    (9675, 'You left on adventure to seek undiscovered treasures.'):
        "All'avventura in cerca di tesori mai visti.",
    (9720, 'You set out on an adventure, dreaming of passive income.'):
        "All'avventura, col sogno di una rendita.",
    (9699, 'You have failed in life and can only became a adventurer.'):
        "Una vita fallita, e nessun'altra strada.",

    # --- 「冒険者になる」: si diventa avventurieri. Sei voci, e il nome del mestiere
    #     un genere ce l'ha: si dice il MESTIERE, non chi lo fa.
    (9606, 'You left on adventure to better your situation.'):
        'Avventura, per cambiare aria.',
    (9648, 'You left on adventure because you admired adventurers.'):
        'Il sogno di fare come gli avventurieri.',
    (9654, 'You left on adventure to become rich.'):
        'Avventura, perché si dice che renda.',
    (9666, 'You left on adventure to seek fame.'):
        'Avventura in cerca di gloria.',
    (9687, 'You become an adventurer at the recommendation of friends.'):
        'Avventura, su consiglio di un conoscente.',
    (9726, 'You became an adventurer, dreaming of a sudden turnaround.'):
        'Avventura, col sogno del colpo di fortuna.',

    # --- le otto che non partono per scelta: qualcosa e' successo.
    (9645, 'You left on adventure after becoming a criminal.'):
        'Un delitto, e la cacciata dal paese natale.',
    (9651, 'One day you were summoned to this world.'):
        'Un giorno, la chiamata in questo mondo.',
    (9657, 'You left on adventure for getting involved in a conspiracy.'):
        "Un complotto, e poi l'esilio.",
    # ⚠️ 「役立たずと判断されて」: «giudicato» concorderebbe, il giudizio no
    (9717, 'You were deemed useless and banished.'):
        'Il giudizio di inutilità, e poi il bando.',
    # ⚠️ il giapponese non nomina nessuna nave: la Queen Sedona la mette l'inglese
    (9672, 'You were loaded onto the Queen Sedona while you slept.'):
        'Un sonno profondo, e il risveglio in una stiva.',
    (9684, 'You suddenly find yourself on a ship before you die.'):
        'La fine della vita, e il ritorno in sé su una nave.',
    (9702, 'You have walked through a mysterious gate.'):
        'Il passaggio attraverso un portale misterioso.',
    # ⚠️ «inghiottito» concorderebbe: la piega agisce, chi ci cade si smarrisce
    (9705, 'You got swallowed into a distortion in time-space.'):
        'Una piega dello spaziotempo, e lo smarrimento.',
    (9681, 'You can not remember the reason of your travel.'):
        'Nemmeno il motivo del viaggio è chiaro.',
}
