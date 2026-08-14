import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :359 la casa. ⚠️ il giapponese dice IRVA, non Tyris
    (359, 'Heaven of Tyris'):
        'Il paradiso di Irva',
    (359, 'Royal mansion'):
        'Villa da nababbi',
    (359, 'Celebrity mansion'):
        'Villa da primato',
    (359, 'Dream mansion'):
        'Casa da sogno',
    (359, 'Cozy mansion'):
        'Casa da rivista',
    (359, 'Attractive house'):
        'Casa che si fa notare',
    (359, 'Average house'):
        'Casa nella media',
    (359, 'Poor house'):
        "Casa un po' malandata",
    (359, "Peasant's shack"):
        'Casa nella miseria',
    # 乞食 e' l'«accattone» di db_creature.hsp:102544
    (359, "Beggar's shack"):
        'Tugurio da accattone',
    (359, 'Home'):
        'Casa',

    # --- :360 il negozio. ⚠️ anche qui il giapponese dice IRVA
    (360, "Tyris' greatest mall"):
        'Il negozio più grande di Irva',
    (360, 'Royal mall'):
        'Negozio da re',
    (360, 'Prosperous mall'):
        'Negozio che va a gonfie vele',
    (360, 'Celebrity shop'):
        'Negozio per gente famosa',
    (360, 'Prosperous shop'):
        'Negozio sempre pieno',
    # マダム e' la «dama» di db_item.hsp:145456
    (360, 'Popular shop'):
        'Negozio da dame',
    (360, 'Average shop'):
        'Negozio con clienti fissi',
    (360, 'Small shop'):
        'Bottega che si fa strada',
    (360, 'Souvenir shop'):
        'Bottega che non vende',
    (360, 'Unknown shop'):
        'Bottega senza nome',
    (360, 'Shop'):
        'Negozio',

    # --- :361 la comunita'.
    (361, 'Boss'):
        'Capo',
    (361, "King's advisor"):
        'Consigliere del re',
    (361, 'Elite consultant'):
        'Consulente scelto',
    (361, 'Famous consultant'):
        'Voce che conta',
    (361, 'Model voter'):
        'Elettore esemplare',
    (361, 'Nice voter'):
        'Elettore che piace alle dame',
    # ⚠️ il giapponese dice 名の知れた, «conosciuto»: l'inglese ci ha messo
    #    «Infamous», che e' il contrario
    (361, 'Infamous voter'):
        'Elettore conosciuto',
    (361, 'Average voter'):
        'Elettore qualunque',
    (361, 'Indifferent voter'):
        'Elettore disinteressato',
    (361, 'Almost voter'):
        'Elettore per un pelo',
    (361, 'Community'):
        'Comunità',

    # --- :362 la gilda, la sola scala che l'inglese ha rifatto da capo.
    (362, 'Future Guildmaster'):
        'Futuro maestro della gilda',
    (362, 'High Champion'):
        'Braccio destro del maestro',
    # ⚠️ 重役 e' il dirigente: l'inglese dice «Champion» e «Master»
    (362, 'Champion'):
        'Dirigente della gilda',
    (362, 'Master'):
        'Aspirante dirigente',
    (362, 'Adept'):
        'Adepto',
    (362, 'Expert'):
        'Esperto',
    (362, 'Journeyman'):
        'Lavorante',
    (362, 'Member'):
        'Membro effettivo',
    (362, 'Candidate'):
        'Aspirante membro',
    (362, 'Apprentice'):
        'Apprendista',
    # ⚠️ l'undicesima voce e' il NOME della categoria, non un grado: il
    #    giapponese dice 「ギルド」, l'inglese ci ha messo un rango
    (362, 'Novice'):
        'Gilda',

    # --- :371-:379 le tre gilde, come le dice gia' db_creature.hsp:79873.
    (371, 'None'):
        'Nessuna',
    (373, 'Mages Guild'):
        'Gilda dei Maghi',
    (376, 'Fighters Guild'):
        'Gilda dei Guerrieri',
    (379, 'Thieves Guild'):
        'Gilda dei Ladri',

    # --- :385-:390 le cariche cittadine, minuscole come in inglese.
    (385, 'mayor'):
        'sindaco',
    (386, 'chief'):
        'capovillaggio',
    (387, 'priest'):
        'sacerdote',
    (388, 'guard master'):
        'capo delle guardie',
    (389, 'tax master'):
        'esattore',
    (390, 'head architect'):
        'capomastro',
}
