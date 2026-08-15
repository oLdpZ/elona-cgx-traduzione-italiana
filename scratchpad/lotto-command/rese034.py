import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Il congedo degli otto dèi (:7015-:7050)
    # ⭐ Registro riscosso dal lotto 028 (:4490-:4547), l'arrivo degli stessi.
    #    Vedi la tabella nel docstring.
    # ================================================================
    # ITZPALT — solenne, 「我が」. Come :4526, «anche questo è destino tessuto
    #    dall'Elemento».
    (7015, 'Then I shall return to the world where I belong.'):
        'È tempo che io torni al mondo cui appartengo.',
    # YACATECT — il Kansai di 「ほなさいならー！」, cioè la popolana. Come :4533,
    #    «Se mi chiami, arrivo subito!».
    (7020, 'See ya!'): 'E allora ciao, eh!',
    # ⭐ JURE — il giapponese RIPETE la costruzione dell'arrivo,
    #    「べ、別に…んだからね！」 / 「ベ、別に…んだから！」, e la resa la ripete con lui.
    #    :4540 era «N-non è mica che volessi venire, sai! Per niente!».
    (7025, "I-I'm not lonely at all!"):
        'N-non è mica che mi senta sola, sai! Per niente!',
    # LULWY — arrogante, e chiama il giocatore 「子猫ちゃん」. Come :4497,
    #    «Che sfacciataggine, convocarmi così.».
    (7030, "I'll let you off the hook this time, kitty."):
        'Per stavolta ti lascio andare, gattino.',
    # EHEKATL — la gatta bambina che raddoppia le parole. Come :4490,
    #    «Miaomiaomiaaa!».
    (7035, "I'm going home! Home!"): 'Torno a casa! A casa!',
    # OPATOS — la risata. Come :4504, «Muahahahah! Eccomi qua!».
    (7040, 'Muwahahahahahahahahaha! Farewell.'):
        'Muahahahahahah! Addio.',
    # KUMIROMI — i puntini. Come :4511, «Mi hai chiamato... che gioia...».
    (7045, 'Do not forget... I will always be watching over you...'):
        'Non dimenticare... veglierò sempre su di te...',
    # MANI — il dio della macchina, altezzoso. Come :4518, «Ti concedo il
    #    diritto di adorarmi.». 「空間転移装置」 non ha un termine gia' deciso.
    (7050, 'Allow me to demonstrate one last time what this spatial shifter can do!'):
        "Per l'ultima volta, guarda di che cosa è capace questo trasferitore "
        'spaziale!',
    # ⚠️ Non «… è tornato a casa»: tc puo' essere di qualunque genere.
    (7056, 'You ask  to return to heaven.'):
        '"Hai rimandato a casa " + name(tc) + "."',

    # ================================================================
    # I cioccolatini di San Valentino (:7072)
    # ⚠️ Cinque varianti della stessa scena: `txt` ne sceglie una a caso.
    # ================================================================
    (7072, 'Please take it. These are my true feelings.'):
        'Tieni... sono i miei veri sentimenti.',
    # ⚠️ L'inglese di monte ha perso lo spazio dopo name(tc): «Annafidgeted».
    #    La resa e' il letterale, quindi lo spazio ce lo rimette.
    (7072, 'fidgeted a bit before taking out a package from  pocket.'):
        'name(tc) + " tentenna un po\', poi tira fuori un pacchetto dalla tasca."',
    (7072, ' hastily takes out some chocolate and shoves it in your face, blushing.'):
        'name(tc) + " arrossisce, tira fuori in fretta un cioccolatino e te lo '
        'mette sotto il naso."',
    (7072, ' smiles and shows you the chocolate  hid behind  back.'):
        'name(tc) + " sorride e mostra il cioccolatino che teneva nascosto '
        'dietro la schiena."',
    # ⚠️ «da una persona come me» e non «da uno come me»: chi parla puo' essere
    #    di qualunque genere.
    (7072, 'Are you really okay with someone like me...?'):
        '...Davvero ti va bene, da una persona come me?',

    # ================================================================
    # La gabbia (:7094-:7098)
    # ================================================================
    # ⚠️ L'inglese porta `name` DUE volte e la rete 11 conta le occorrenze.
    #    「連行対象」 e' chi va consegnato a qualcuno.
    (7094, 'You let  out of the cage.  is now free...'):
        '"Fai uscire " + name(tc) + " dalla gabbia. Ormai " + name(tc) + '
        '" non è più da consegnare."',
    # ⚠️ «riprende» e non «è tornato»: nessun accordo da indovinare.
    (7098, ' changed to their original shape.'):
        'cdatan(CDATAN_NAME, tc) + " riprende l\'aspetto di prima."',
}
