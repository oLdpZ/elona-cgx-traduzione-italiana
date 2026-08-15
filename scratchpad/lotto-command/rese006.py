import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9735-:9867 i quarantacinque pregi. Ognuno chiude in «, ma» perche' la
    #     riga dopo e' un difetto tirato a sorte a parte: vedi il docstring.
    (9735, 'Though you are gentle and merciful,'):
        'Mitezza e generosità, ma',
    (9738, 'Though you are a genius,'):
        'Un cervello geniale, ma',
    (9741, 'Though you are friends with everyone,'):
        'Amicizia con tutti, ma',
    (9744, 'Though you are always polite,'):
        'Buone maniere e precisione, ma',
    (9747, 'Though you know many things,'):
        'Un sapere vasto, ma',
    (9750, 'Though you have a keen eye,'):
        'Occhio acuto, ma',
    (9753, 'Though you are calm and collected,'):
        'Sangue freddo e buon giudizio, ma',
    # ⚠️ 「ムードメーカー」 e' chi tira su gli altri, non chi fa festa
    (9756, 'Though you are the life of the party,'):
        'Allegria che contagia gli altri, ma',
    (9759, 'Though you are ordinary,'):
        'Una normalità di fondo, ma',
    (9762, 'Though you are bold and daring,'):
        'Ambizione e voglia di sfide, ma',
    (9765, 'Though you never give up,'):
        'Mai una resa, ma',
    (9768, 'Though you are always strict with yourself,'):
        'Serietà e severità con se stessi, ma',
    (9771, 'Though you are passionate,'):
        'Un carattere schietto e caldo, ma',
    (9774, 'Though highly proactive,'):
        "Una gran capacità di agire, ma",
    (9777, 'Though bold and courageous,'):
        'Audacia e fegato, ma',
    (9780, 'Though good at supporting others,'):
        'Un gran talento nel dare una mano, ma',
    (9783, 'Though enduring hardships,'):
        'Tempra da resistere alle sventure, ma',
    (9786, 'Though curious and sociable,'):
        'Curiosità e simpatia, ma',
    (9789, 'Though have an excellent memory,'):
        'Una memoria formidabile, ma',
    (9792, 'Though adapt to different environments,'):
        'Adattamento rapido a ogni ambiente, ma',
    (9795, 'Though have extraordinary imagination,'):
        "Un'inventiva fuori dal comune, ma",
    (9798, "Though doesn't leave people in trouble alone,"):
        'Mai un occhio chiuso su chi è nei guai, ma',
    (9801, 'Though remains confident even in times of crisis,'):
        'Portamento saldo anche nei momenti neri, ma',
    (9804, 'Though have a strong sense of responsibility,'):
        'Un senso di responsabilità come nessuno, ma',
    (9807, 'Though have the ability to bring everyone together,'):
        'Il polso per tenere insieme tutti, ma',
    (9810, 'Though have virtue and is loved by everyone,'):
        "Virtù, e l'affetto di tutti, ma",
    (9813, 'Though have strong loyalty and kindness,'):
        'Lealtà e cuore, ma',
    (9816, 'Though think flexibly according to the situation,'):
        'Pensiero elastico secondo il momento, ma',
    (9819, 'Though always easygoing,'):
        'Una leggerezza costante, ma',
    (9822, 'Though have a strong resolve,'):
        'Una determinazione nascosta, ma',
    (9825, 'Though have no ulterior motives and are straightforward,'):
        'Nessun doppio fine, tutto alla luce del sole, ma',
    (9828, 'Though good at gathering information,'):
        'Un fiuto per le notizie, ma',
    (9831, 'Though never get depressed even when worst things happen,'):
        'Nessuno scoramento, per male che vada, ma',
    (9834, 'Though good at identifying the good points of others,'):
        'Un occhio per i pregi degli altri, ma',
    # ⚠️ «leader» ha un genere addosso: «guida» e' il nome di genere fisso
    (9837, 'Though possesses strong leadership,'):
        'Una guida forte per gli altri, ma',
    (9840, "Though doesn't sweat the small stuff,"):
        'Nessun pensiero per le piccolezze, ma',
    (9843, 'Though good at taking care of others,'):
        'Alla fine, cura per gli altri, ma',
    # ⚠️ 「格下相手にも」: la guardia non cala nemmeno contro i piu' deboli
    (9846, 'Though never let guard down,'):
        'Mai la guardia bassa, nemmeno coi deboli, ma',
    (9849, 'Though show true worth in times of crisis,'):
        'Il vero valore esce nei guai, ma',
    (9852, 'Though kind and tolerant,'):
        'Dolcezza e larghezza di vedute, ma',
    (9855, 'Though good at paying attention to small details,'):
        'Attenzioni minute per chiunque, ma',
    (9858, 'Though work hard for others,'):
        'Ogni sforzo, se è per qualcuno, ma',
    (9861, 'Though have the ability to see the big picture,'):
        'Uno sguardo che abbraccia tutto, ma',
    (9864, 'Though value bonds with others,'):
        'I legami con gli altri contano, ma',
    (9867, 'Though have the strength to not rely on anyone,'):
        'La forza di non dipendere da nessuno, ma',
}
