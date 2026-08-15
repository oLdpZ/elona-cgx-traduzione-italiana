import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- le otto 「趣味は…」: il giapponese scrive «passatempo:», e la resa lo copia
    (10011, 'You like to tinker with machines.'):
        'Passatempo: armeggiare con le macchine.',
    (10017, 'You like to stalk people.'):
        'Passatempo: pedinare la gente.',
    (10023, 'You like to garden.'):
        'Passatempo: il giardinaggio.',
    (10026, 'You like to cultivate bonsai.'):
        'Passatempo: curare i bonsai.',
    (10038, 'You like to hunt.'):
        'Passatempo: la caccia.',
    (10068, 'You like to nap.'):
        'Passatempo: il pisolino.',
    (10074, 'You like to read.'):
        'Passatempo: la lettura.',
    (10104, 'You like making fun of others.'):
        'Passatempo: prendere in giro qualcuno.',

    # --- le altre trentacinque.
    # ⚠️ 「監禁」 e' la reclusione, non le catene
    (10014, 'You like being chained up.'):
        'Passatempo: farsi rinchiudere.',
    (10020, "You like to see pain on people's faces."):
        'Che piacere, una faccia stravolta dal dolore.',
    (10029, 'You like stuffed animals.'):
        'Un debole per i peluche.',
    # ⚠️ «sadico» ha un genere: si dice il vizio, non chi ce l'ha
    (10032, 'You are a self-proclaimed sadist.'):
        'Sadismo, per autodichiarazione.',
    (10035, 'You risk your life for creative activities.'):
        'La creazione vale una vita intera.',
    (10041, 'You like to wear clothes of the opposite sex.'):
        "Un interesse per i vestiti dell'altro sesso.",
    (10044, 'You love small animals.'):
        'Amore sviscerato per le bestioline.',
    (10047, 'You yearn for your master.'):
        "C'è un maestro da venerare.",
    (10050, 'You have memories of your past life.'):
        'Restano i ricordi di una vita precedente.',
    (10053, 'You like to exercise.'):
        'Il piacere di muovere il corpo.',
    (10056, 'Your body is branded by a mysterious coat of arms.'):
        'Uno stemma misterioso sulla pelle.',
    (10062, 'You have a sharp intuition.'):
        'Un intuito pronto, in ogni occasione.',
    # ⚠️ errore di monte: 「否定する」 e' dare torto, non privare di un piacere
    (10065, 'You enjoy denying pleasure to others.'):
        'Che gusto, dare torto agli altri.',
    (10071, 'You have a strong attachment to life.'):
        'Un attaccamento fortissimo alla vita.',
    (10077, 'You enjoy using violence.'):
        'Il piacere di menare le mani.',
    (10080, "You have a secret that you can't reveal."):
        "C'è un segreto che nessuno deve sapere.",
    (10083, 'You are good at singing.'):
        'Un gran talento nel canto.',
    (10086, 'You are gullible.'):
        'Una gran facilità a cascarci.',
    (10092, 'You are bad at lying.'):
        'Le bugie non riescono mai bene.',
    (10095, 'You easily fall in love.'):
        'Un cuore che si innamora in fretta.',
    (10098, 'You are a hard worker.'):
        'Un gran zelo sul lavoro.',
    (10101, 'You had a mission you failed to achieve.'):
        "C'è una missione rimasta incompiuta.",
    # ⚠️ 「弟子」 sono i discepoli, non i seguaci
    (10107, 'You have followers.'):
        "C'è qualche discepolo al seguito.",
    (10110, 'You hold a powerful grudge against someone.'):
        'Un rancore che dura più del previsto.',
    (10113, 'You fear betrayal above all else.'):
        'Il tradimento fa più paura di ogni altra cosa.',
    (10116, 'You like to collect junk.'):
        'Il gusto di raccogliere cianfrusaglie.',
    (10119, 'You actually want to live quietly.'):
        'In fondo, il sogno è una vita tranquilla.',
    (10122, 'You have a desire to be messed up.'):
        "C'è il desiderio di farsi ridurre a pezzi.",
    (10125, 'You have multiple hearts.'):
        'Più di un cuore in petto.',
    (10128, 'You sometimes have unnatural memory loss.'):
        'Ogni tanto la memoria sparisce, e non è normale.',
    (10131, 'You never forget food grudges.'):
        'I torti a tavola non si dimenticano mai.',
    (10134, "You are quick to covet other people's things."):
        'La roba altrui fa subito gola.',
    (10137, 'You think humanity should be destroyed.'):
        "L'umanità meriterebbe di sparire.",
    (10140, 'You prefer bamboo shoots to mushrooms.'):
        'Meglio i germogli di bambù dei funghi.',
    (10143, 'You are starving for motherhood.'):
        "Una fame d'affetto materno.",
}
