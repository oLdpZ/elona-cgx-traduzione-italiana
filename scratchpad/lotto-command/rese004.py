import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9456 il valore quando `ohanasi1 == 0`: la riga che si stampa al posto
    #     di tutte le altre quando il passato si tiene per se'. Il giapponese e'
    #     il sostantivo nudo 「内緒」.
    (9456, 'Secret'):
        'Segreto',

    # --- :9459-:9591 le quarantacinque origini, tirate a sorte da `rnd(45) + 1`.
    (9459, 'You had no family.'):
        'Nessuna famiglia, fin dalla nascita.',
    (9462, 'You grew up without any inconveniences.'):
        "Un'infanzia senza privazioni.",
    # ⚠️ «creato» concorderebbe: il participio passa al nome della cosa
    (9465, 'You were artificially created through an experiment.'):
        'Frutto artificiale di un esperimento.',
    # ⚠️ 「実験体にされていた」 e' il cavia, non l'esperimento: nome di genere fisso
    (9468, 'You were used for human experimentation.'):
        'Cavia in un centro di ricerca.',
    (9471, 'You have amnesia.'):
        'Amnesia: del passato nessun ricordo.',
    # ⚠️ «perduti» concorda con `genitori`, non con chi legge
    (9474, 'You lost your parents early.'):
        'Genitori perduti troppo presto.',
    (9477, 'You spent your days in peace.'):
        "Giorni sereni, uno dopo l'altro.",
    (9480, 'You have been abused since childhood.'):
        "Maltrattamenti fin dall'infanzia.",
    # ⚠️ il giapponese 「自分の出生を隠している」 e' attivo — le origini si NASCONDONO,
    #    non «furono tenute segrete». «tenute» concorda con `origini`.
    (9483, 'Your birth was kept secret.'):
        'Origini tenute nascoste.',
    (9486, 'You were a faithful servant.'):
        'Anni di servizio fedele.',
    (9489, 'You were raised by a different race.'):
        "Infanzia presso un'altra razza.",
    (9492, 'You were a slave.'):
        'Un passato di schiavitù.',
    (9495, 'You were poor but grew up well.'):
        'Povertà, ma una crescita robusta.',
    (9498, 'You had a normal life.'):
        'Famiglia normale, infanzia normale.',
    (9501, 'You were a member of a royal family.'):
        'Sangue reale in famiglia.',
    (9504, 'You were loved by everyone.'):
        "Un'infanzia circondata d'affetto.",
    (9507, 'You were bedridden with a disease for a long time.'):
        'Anni di malattia, a letto.',
    (9510, 'For some reason, you were asleep for a long time.'):
        'Un lunghissimo sonno, chissà perché.',
    # ⚠️ non «Vieni dal futuro»: la riga sta in colonna con le altre quarantaquattro,
    #    che sono tutte nominali. «Origine:» tiene la forma della lista.
    (9513, 'You actually come from the future.'):
        'Origine: il mondo del futuro.',
    (9516, 'You were a prisoner for a long time.'):
        'Anni di prigionia.',
    # ⭐ «criminale» e' invariabile in genere: qui il nome della persona si puo' dire
    (9519, 'You were a criminal.'):
        'Un passato da criminale.',
    (9522, 'For some reason, you destroyed your hometown.'):
        'Il proprio paese, distrutto per varie ragioni.',
    (9525, 'You lost your hometown in a war.'):
        'Il paese natale, perduto in guerra.',
    # ⚠️ «signore di provincia» ha un genere: si rende la CARICA, non chi la porta
    (9528, 'You were a local lord.'):
        'Un passato al comando di una provincia.',
    (9531, 'You were a powerful god.'):
        'Un passato di stirpe divina e potente.',
    # ⚠️ 「忌み子」 e' «figlio maledetto», che al femminile stona: «creatura» e' il
    #    nome di genere fisso che regge chiunque
    (9534, 'You were detested and abandoned as a child.'):
        "La nomea di creatura maledetta, e l'abbandono.",
    # --- :9537-:9549 i quattro 「家系」: la resa descrive la FAMIGLIA, che un genere
    #     ce l'ha, e non chi ne discende.
    (9537, 'You come from a family of adventurers.'):
        'Una famiglia di avventurieri da generazioni.',
    (9540, 'You come from a family of noble knights.'):
        'Una famiglia di cavalieri di nobile lignaggio.',
    (9543, 'You come from a prodigious family of mages.'):
        'Una famiglia di maghi di gran fama.',
    (9546, 'You were found and raised by thieves.'):
        "Un'infanzia in mano ai briganti.",
    (9549, 'Your family were impoverished warriors.'):
        'Una famiglia di guerrieri caduti in miseria.',
    # ⭐ «erede» e' invariabile in genere
    (9552, "You were raised as your family's heir."):
        "Un'educazione severa, da erede.",
    # ⭐ «militare» e' invariabile in genere; «ferita» concorda con se stessa
    (9555, 'You are a traumatized ex-soldier.'):
        "Un ex militare con una ferita nell'animo.",
    (9558, 'You are a minion of an evil organization.'):
        "Al soldo di un'organizzazione malvagia.",
    (9561, 'You are a clone of a certain person.'):
        'Il clone di una certa persona.',
    (9564, 'You are a weapon created with forbidden technology.'):
        "Un'arma nata da una tecnologia proibita.",
    (9567, 'You were discovered and rescued in ruins as a child.'):
        'Il ritrovamento fra le rovine, ancora in fasce.',
    (9570, 'You grew up in a village with horrific customs.'):
        'Infanzia in un villaggio dalle usanze atroci.',
    # ⚠️ «nato» concorderebbe: si nominano i due sangui, non chi li porta
    (9573, 'You were born between a monster and a human.'):
        'Sangue di mostro e sangue umano insieme.',
    # ⚠️ 「隠し子」 e' «figlio nascosto»: «frutto» e' la stessa manovra di :9465
    (9576, 'You are the illegitimate child of an affair.'):
        'Un frutto nascosto del tradimento.',
    (9579, "You were actually being raised by your parents' enemy."):
        'In casa del nemico dei genitori, senza saperlo.',
    (9582, 'You were isolated because of your hidden powers.'):
        "Un potere segreto, e per questo l'isolamento.",
    # --- :9585-:9591 le tre fini del paese natale: cambia la causa, non la forma.
    (9585, 'You lost your hometown in a great disaster.'):
        'Il paese natale, perduto in un cataclisma.',
    (9588, 'Your hometown was destroyed by monsters.'):
        'Il paese natale, distrutto dai mostri.',
    (9591, 'Your hometown was destroyed by an evil adventurer.'):
        'Il paese natale, distrutto da un pessimo avventuriero.',
}
