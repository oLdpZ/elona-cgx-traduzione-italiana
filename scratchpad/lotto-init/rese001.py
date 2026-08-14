import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- i due sparsi.
    # ⚠️ invariato: parola italiana identica all'inglese, come «bonus»
    (23, 'Ok'):
        'Ok',
    (76, 'Error:'):
        'Errore:',

    # --- :355 l'arena. Dieci gradini piu' il nome della categoria.
    (355, 'Arena champion'):
        "Campione dell'arena",
    (355, 'Super elite gladiator'):
        'Gladiatore invitto',
    (355, 'Star gladiator'):
        "Stella dell'arena",
    # ⚠️ «d'élite» darebbe «d'e'lite» a schermo: accenti.py degrada anche gli
    #    accenti dentro la parola
    (355, 'Elite gladiator'):
        'Gladiatore scelto',
    (355, 'Veteran gladiator'):
        'Gladiatore esperto',
    (355, 'Popular gladiator'):
        'Gladiatore affermato',
    (355, 'New hope'):
        "Promessa dell'arena",
    (355, 'Darkhorse'):
        'Mina vagante',
    (355, 'Low class fighter'):
        'Gladiatore di bassa lega',
    (355, 'Unknown fighter'):
        'Gladiatore senza nome',
    # ⚠️ invariato: il nome della categoria, e l'italiano ha la stessa parola
    (355, 'Arena'):
        'Arena',

    # --- :356 l'arena delle bestie.
    (356, 'King of tamer'):
        'Sovrano di tutte le bestie',
    (356, 'Super elite tamer'):
        'Domatore impareggiabile',
    (356, 'Prince of animals'):
        'Principe delle bestie',
    (356, 'Chief of animals'):
        'Idolo delle bestie',
    (356, 'Elite tamer'):
        'Domatore scelto',
    (356, 'Notorious tamer'):
        'Domatore rinomato',
    # ⚠️ il giapponese dice ペットの母, e «madre» sarebbe sbagliato per meta' dei
    #    giocatori: «balia» e' un nome di RUOLO, buono per chiunque
    (356, 'New hope'):
        'Balia delle bestie',
    (356, 'Average tamer'):
        'Discreto domatore',
    (356, 'Petty tamer'):
        'Domatore alle prime armi',
    (356, 'Unknown tamer'):
        'Domatore senza nome',
    (356, 'Pet Arena'):
        'Arena delle bestie',

    # --- :357 Nefia e i sotterranei.
    (357, 'King of Nefia'):
        'Signore di Nefia',
    (357, 'Champion of labyrinth'):
        'Dominatore dei labirinti',
    (357, 'Dungeon master'):
        'Padrone dei sotterranei',
    (357, 'Famous adventurer'):
        'Esploratore illustre',
    (357, "Children's star"):
        'Idolo dei bambini',
    (357, 'Guide of Nefia'):
        'Guida dei sotterranei',
    (357, 'Notorious tomb robber'):
        'Famoso predone di rovine',
    (357, 'Tomb robber'):
        'Esploratore',
    # ⚠️ il giapponese dice ちんけな遺跡荒らし, uno sfottò: l'inglese ci ha messo
    #    un complimento («Famous tourist»)
    (357, 'Famous tourist'):
        'Predone di rovine da strapazzo',
    (357, 'Tourist'):
        'Turista',
    (357, 'Crawler'):
        'Esploratore di Nefia',

    # --- :358 il museo. ⚠️ «Great museum» sta su DUE gradini: chiave lunga
    (358, 'Tyris\' greatest museum'):
        'Il museo più grande di Tyris',
    (358, 'Royal museum'):
        'Museo famosissimo',
    (358, 'Great museum', '大人気の博物館'):
        'Museo amatissimo',
    (358, 'Top museum'):
        'Museo famoso',
    (358, 'Great museum', '来客の絶えない博物館'):
        'Museo sempre affollato',
    (358, 'Good museum'):
        'Museo che piace',
    (358, 'Average museum'):
        'Museo conosciuto',
    (358, 'Small museum'):
        'Museo passabile',
    (358, 'Unknown museum'):
        'Museo poco visitato',
    # ⚠️ l'inglese dice «Ruin», il giapponese 無名の博物館: e' un museo
    (358, 'Unknown Ruin'):
        'Museo senza nome',
    (358, 'Museum'):
        'Museo',
}
