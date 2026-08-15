import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6002 lo zombie del negromante.
    (6002, 'Return to the coffin'):
        'Rimetti nella bara',

    # --- :6009-:6019 il bestiame del ranch. 「皮を剥ぐ」 e' scuoiare, e in
    #     italiano c'e' il verbo apposta.
    (6009, 'Bring Out'):
        'Porta fuori',
    (6013, 'Take out bone'):
        'Estrai un osso',
    (6014, 'Take out heart'):
        'Estrai il cuore',
    (6015, 'Take out eye'):
        'Cava un occhio',
    # ⚠️ 「体液」 sono i fluidi, non il sangue
    (6016, 'Take out blood'):
        'Spremi i fluidi',
    (6017, 'Take out skin'):
        'Scuoia',
    (6019, 'Name'):
        'Dai un nome',

    # --- :6026-:6047 quel che si comanda a un alleato.
    # ⚠️ 「言葉を教える」 e' una frase per volta: :6631 chiede «quale frase?»
    (6026, 'Teach Words'):
        'Insegna una frase',
    (6027, 'Change Tone'):
        'Cambia parlata',
    (6031, 'Shut up'):
        'Fai tacere',
    (6034, 'You can speak now'):
        'Lascia parlare',
    # ⚠️ «prezioso» concorderebbe col compagno: «indispensabile» e' invariabile
    (6038, 'Designate as precious ally'):
        'Metti fra gli indispensabili',
    (6041, 'Cancel precious ally status'):
        'Togli dagli indispensabili',
    (6044, "Don't pick up items"):
        'Non raccogliere oggetti',
    (6047, 'Pick up items freely'):
        'Raccogli pure gli oggetti',
    (6053, 'Wait at the town'):
        'Fai aspettare in città',

    # --- :6062-:6076 l'aspetto. 「アイテム画像」 e' l'icona che si appiccica
    #     addosso al compagno, non un oggetto.
    (6062, 'Appearance'):
        'Cambia i vestiti',
    (6065, 'Shape change'):
        'Cambia aspetto',
    # ⚠️ 「立ち姿」 e' il ritratto a figura intera, non una posa
    (6067, 'Change Tachi-e'):
        'Cambia il ritratto',
    (6068, 'Item mark set'):
        "Assegna un'icona",
    # ⚠️ :6070 «Item mark adjust» e' commentata: rinviata, non resa
    (6073, 'Item mark move'):
        "Sposta l'icona",
    (6076, 'Item mark delete'):
        "Togli l'icona",

    # --- :6094-:6098 la coppia da tag-team.
    (6094, 'Tag organization'):
        'Forma una coppia',
    (6098, 'Tag dissolution'):
        'Sciogli la coppia',

    # --- :6110, :6116 due «Release» che sono due cose diverse.
    (6110, 'Release'):
        'Slega',
    (6116, 'Release'):
        'Libera dalla gabbia',

    # --- :6125-:6138 i casi speciali.
    (6125, 'Return home'):
        'Rimanda a casa',
    (6132, 'Ask for chocolate'):
        'Chiedi del cioccolato',
    (6138, 'Offer yourself as a gift'):
        'Offriti in regalo',

    # --- :6144, :6147 due «Information», e la seconda e' da sviluppo.
    (6144, 'Information'):
        'Mostra le capacità',
    (6147, 'Information'):
        'Informazioni',

    (6155, 'Collect materials'):
        'Raccogli i materiali',

    # --- :6163-:6166 il gioco di carte. ⭐ il giapponese cita Yu-Gi-Oh!, e la
    #     citazione in italiano esiste gia'.
    (6163, 'Play TCG!'):
        'Duello!',
    (6166, 'Play TCG (Lethal)!'):
        'Gioco delle Tenebre!',
}
