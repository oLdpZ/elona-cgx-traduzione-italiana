import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4575 il desiderio rinunciato. L'inglese sbuffa, il giapponese chiede.
    (4575, 'What a waste of a wish!'): 'Ah, ti sta bene così?',

    # --- :4581-:4627 il cambio di classe. ⭐ «Classe» è command.hsp:17663.
    (4581, "What's your new class?"): 'Qual è la tua nuova classe?',
    # ⭐ rete 3: action.hsp:9206 ha lo stesso giapponese.
    #    Vale anche per :4661, che è la stessa firma.
    (4587, 'You changed your mind.'): 'Hai cambiato idea.',
    (4627, 'You will be known as <>.'):
        '"La tua nuova classe è <" + cdatan(CDATAN_FAKE_CLASS, CHARA_PLAYER) + ">."',

    # --- :4633-:4643 il cambio di razza.
    (4633, "What's your new race?"): 'Qual è la tua nuova razza?',
    # ⚠️ «Sei rinato» accorderebbe col giocatore: la resa gira sul presente.
    (4643, 'You change your race to <>.'):
        '"Adesso la tua razza è <" + cdatan(CDATAN_CUSTOM_RACE, CHARA_PLAYER) + ">."',

    # --- :4649-:4709 il cambio di sesso.
    #     ⚠️ :4655 «hermaphrodite» è RINVIATA: la stessa lang() scrive
    #        CDATAN_NEWSEX a :4686, ed è un valore di dato. A schermo ci arriva
    #        per toppa. Vedi il docstring.
    (4649, 'Which gender would you like?'): 'Quale sesso vuoi?',
    (4693, 'Will you change name of gender?'): 'Vuoi cambiare il nome del sesso?',
    (4696, "What's a new name of gender?"): 'Come si chiama il nuovo sesso?',
    # ⭐ il giapponese aggiunge una chiusa che l'inglese non ha, e le funzioni di
    #    contenuto restano le stesse: la rete 11 lo permette.
    (4709, ' became !'):
        'name(CHARA_PLAYER) + " adesso è " + gendername(CHARA_PLAYER) '
        '+ "! ...E non si torna più indietro."',

    # --- :4714-:4722 il perdono e la morte.
    (4714, "You aren't a sinner."): '...Ma se non hai commesso nessun peccato.',
    (4718, 'What a convenient wish!'): 'Oh... che comodo, però.',
    (4722, 'If you wish so...'): 'Se è questo che desideri...',

    # --- :4732-:4752 quel che piove dal cielo.
    #     ⭐ i tre nomi sono già decisi: action.hsp:1245, command.hsp:14105,
    #        action.hsp:931.
    (4732, 'Lots of gold pieces appear.'): "Piovono monete d'oro!",
    (4739, 'Some small coins appear.'): 'Piovono medagliette!',
    (4746, 'Some platinum coins appear.'): 'Piovono monete di platino!',
    # il fischietto per cani: una faccia di cane che fa il verso del gatto.
    # ⚠️ l'emoticon è quella dell'inglese, perché il giapponese usa caratteri a
    #    doppia larghezza che le guardie del progetto vietano.
    (4752, 'U\'w\'U \\"Meow!\\"'): 'U\'w\'U \\"Miao!\\"',
}
