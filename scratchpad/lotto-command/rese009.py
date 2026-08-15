import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1196-:1273 gli undici usi della lista. Per ognuno: la domanda (`txt`),
    #     il titolo della finestra e le due intestazioni di colonna.
    (1196, 'Imprison who?'):
        'Chi vuoi rinchiudere?',
    (1197, 'Prisoner List'):
        'Prigionieri da rinchiudere',
    # ⭐ copiata: «Nome» sta gia' a :453, :456 e :14120
    (1197, 'Name'):
        'Nome',
    (1197, 'Status'):
        'Stato',

    (1201, 'Who to recall?'):
        'Chi vuoi richiamare?',
    (1202, 'Ally List'):
        'Alleati da richiamare',
    (1202, 'Name'):
        'Nome',

    (1206, 'Who to sell off?'):
        'Chi vuoi vendere?',
    (1207, 'Ally List'):
        'Alleati da vendere',
    # ⭐ copiata: 「値段」 e' gia' «Prezzo» a :14101
    (1207, 'Value'):
        'Prezzo',

    # ⚠️ 「試合の規定人数: 」 e' il numero regolamentare, e lo spazio in coda serve
    (1221, 'Participant: '):
        'Partecipanti: ',
    (1222, 'Ally List'):
        'Alleati in gara',

    (1227, 'Whose power will you awaken?'):
        'A chi vuoi risvegliare il potere?',
    (1228, 'Ally List'):
        'Candidati',
    # ⚠️ 「必要AP/所持AP」 dice due cose, «Cost/AP» una e mezza
    (1228, 'Cost/AP'):
        'AP necessari/AP',
    # ⭐ copiata: «AP» e' invariato dalla 43a (:10504)
    (1232, 'AP'):
        'AP',

    (1235, 'Who will you add body parts to?'):
        'A chi vuoi aggiungere una parte?',
    # ⭐ copiata: 「生命力」 e' gia' «Vita» a :10517 e a skill.hsp:9
    (1236, 'Life'):
        'Vita',

    (1239, 'Who will help?'):
        'Chi vuoi che dia una mano?',
    (1243, 'Whose story?'):
        'La storia di chi?',

    (1247, 'Who will train here?'):
        'Chi vuoi iscrivere?',
    (1248, 'Ally List'):
        'Aspiranti',

    (1251, 'Who do you want to leave here?'):
        'Chi vuoi lasciare al pascolo?',
    (1252, 'Ally List'):
        'Candidati al pascolo',

    (1255, 'Who will be the shopkeeper?'):
        'Chi vuoi come negoziante?',
    (1256, 'Ally List'):
        'Candidati al negozio',
    # ⭐ «Trattativa» viene da skill.hsp:222; CAR e' la sigla della scheda
    (1256, 'CHR/Negotiation'):
        'CAR/Trattativa',

    # ⚠️ «allevatore» concorderebbe col compagno: si nomina l'attivita'
    (1259, 'Who will be the breeder?'):
        'Chi vuoi alla riproduzione?',
    (1260, 'Ally List'):
        'Candidati alla riproduzione',
    (1260, 'Breed Power'):
        'Fertilità',

    (1263, 'Who should stay in your home?'):
        'Chi vuoi che resti qui?',
    (1264, 'Ally List'):
        'Chi resta e chi no',

    (1269, 'Who is the subject?'):
        'Chi è il soggetto?',
    (1270, 'Ally List'):
        'Alleati',
    (1273, 'Body/Skill'):
        'Parti/Abilità',

    # --- :1319 il bottone in fondo alla lista.
    (1319, 'Proceed'):
        'Conferma',

    # --- :1328-:1361 quel che si legge accanto al nome. Il giapponese chiude le
    #     parentesi e usa le BARRE per i quattro ordini: la resa fa uguale.
    (1328, '(Riding'):
        '(in sella)',
    (1332, ' *In* '):
        ' *in gara* ',
    (1345, '(OutRange'):
        '(fuori vista)',
    (1350, '(offensive'):
        '/assalto/',
    (1353, '(defensive'):
        '/difesa/',
    (1356, '(intercept'):
        '/contrasto/',
    (1359, '(talking'):
        '/dialogo/',
    (1361, ' PGauge:%'):
        '" Carica:" + cdata(CDATA_POWER_GAUGE, i) + "%"',

    # --- :1368-:1398 gli stati. ⚠️ «morto» e «disperso» concorderebbero col
    #     compagno: si dice lo stato, non la persona.
    (1368, '(revival impossible until you switch area)'):
        '(rinasce solo cambiando mappa)',
    (1371, '(Dead'):
        '(senza vita)',
    (1376, '(Waiting)'):
        '(in attesa)',
    (1379, 'Waiting'):
        'Attesa',
    (1384, '(Alive)'):
        '(in vita)',
    (1393, '(Ash)'):
        '(in cenere)',
    (1398, '(Stray)'):
        '(chissà dove)',

    # ⭐ copiata: 「なし」 e' gia' «Nessuna» a init.hsp:371, e qui il nome che
    #    sostituisce e' una parte del corpo
    (1445, 'None'):
        'Nessuna',

    # --- :1498-:1536 i quattro rifiuti.
    # ⭐ «Ingegneria genetica» viene da skill.hsp:197
    (1498, 'You need to be a better gene engineer.'):
        "L'ingegneria genetica non basta.",
    (1511, 'You need at least 1 pet to start the battle.'):
        'Serve almeno un partecipante.',
    # ⚠️ dinamiche: `he` e `is` sono morfologia e spariscono, quindi niente
    #    soggetto e niente participio — «è morto» concorderebbe
    (1519, '  dead.'):
        '"Non è più in vita."',
    (1524, '  waiting.'):
        '"È in attesa."',
    (1529, '  working.'):
        '"È al lavoro."',
    (1536, 'Too many participants.'):
        'Troppi partecipanti.',
}
