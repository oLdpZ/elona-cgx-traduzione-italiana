# -*- coding: utf-8 -*-
"""Il menu dei ritocchi vari (`*MiscTweakMenu_loop`, :1624-:1829).

Quindici voci e quindici descrizioni: **30 righe**, di cui qui se ne toccano
**29**. Titolo, riga di testa e voce di ritorno erano gia' chiusi dalle toppe
`tutte` del menu principale.

## ⚠️ La riga che si lascia in inglese apposta: `:1679` «Nani?!»

E' la descrizione della «Fist of the North Star Mode», e **non si traduce**.
Il motivo e' lo stesso per cui la 50a ha lasciato «Sp 12/23» dentro la
descrizione della barra: **l'inglese non l'ha tradotta neanche lui**. Chi ha
scritto il mod aveva a disposizione «What?!» e ha scelto di lasciare il
giapponese, perche' la battuta e' la citazione — e in italiano la serie si
chiama «Ken il guerriero», quindi la voce di menu il riferimento lo da' gia'.
Tradurre «Nani?!» con «Cosa?!» avrebbe tolto la citazione e non aggiunto
niente.
⚠️ Percio' `triage_nudi` continuera' a contare questa riga fra le «da fare»:
**e' voluto**, non e' una dimenticanza.

## Il vocabolario

    Tachi-E          -> ritratto           custom_tweaks.hsp:462 (50a)
    tag-team         -> coppia             action.hsp:10861, proc.hsp:10793, skill.hsp:1477
    bolt / ball / arrow -> saetta / sfera / freccia   skill.hsp:504-549, db_item.hsp:138050, :149300
    super lure       -> super esca         db_item.hsp:140140, proc.hsp:5082
    Dimension Fishing -> Pesca dimensionale  skill.hsp:1608, proc.hsp:19307
    Devil's Cape     -> Capo del Diavolo   text.hsp:2845
    map (oggetto)    -> mappa              db_item.hsp:150869
    NPC              -> PNG                custom_tweaks.hsp:133
    pet arena        -> arena delle bestie db_creature.hsp:118259, map.hsp:5478

⭐ **«Fist of the North Star» si traduce, e non alla lettera**: in Italia la
serie si chiama **«Ken il guerriero»**, ed e' con quel nome che il giocatore la
riconosce. «Il pugno della stella del nord» sarebbe stato fedele e illeggibile.

⚠️ **«casella» e' una parola nuova nel progetto** — nessuna resa in dizionario
usa «casella» ne' «tessera» per il quadretto di mappa — e serviva due volte
(`:1694` le caselle non esplorate, `:1703` lo spostamento di tre caselle). E' la
parola italiana normale per un quadretto di griglia e non ha alternative migliori:
si fissa qui.

⚠️ **`(MMA)`, `(MMAH)`, `Custom-GX` e i nomi di file restano**: sono rami di
codice e file veri che il giocatore deve trovare sul disco
(`graphic/custom_animation`, `face4_B1.bmp`, `face_B.bmp`).

## La larghezza

Voci a `wx + 64` (576 px, **74** caratteri col metro prudente), suffisso di
stato compreso — qui sono tutti interruttori, quindi al massimo « (Ora:
acceso)», 14 caratteri. Descrizioni a `wx + 38` (602 px, **78** per riga).
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

TETTO_VOCE = 74 - len(' (Ora: acceso)')
TETTO_DESCRIZIONE = 78

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_VARI = (
    "Sta nel menu dei ritocchi vari (`*MiscTweakMenu_loop`), uno dei sette menu di "
    "dettaglio del pannello dei ritocchi di Custom-GX. «ritratto» per «Tachi-E» e "
    "«PNG» per «NPC» sono le rese gia' fissate nella 50a (custom_tweaks.hsp:462 e :133). "
    "La finestra e' 640: le voci hanno 74 caratteri col metro prudente, suffisso di "
    "stato compreso, e le descrizioni 78 per riga. "
)

# (riga, tipo, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = [
    # ── le quindici voci ────────────────────────────────────────────────────
    (1631, 'voce', [('"Enable Random Start For MP3."', '"Fai partire gli MP3 da un punto a caso."')], 1,
     "«Random start» non e' l'ordine casuale dei brani ma il punto di partenza dentro il "
     "brano — lo dice la descrizione di :1670 («from a random point»). "),
    (1632, 'voce', [('"Display Weather Everywhere."', '"Mostra il tempo dappertutto."')], 1,
     "«Weather» e' il tempo atmosferico, quello di cui text.hsp:46 elenca i valori "
     "(«Vento d'etere», «Neve», «Pioggia», «Temporale»). "),
    (1633, 'voce', [('"Prevent bump attack."', '"Impedisci l\'attacco per contatto."')], 1,
     "⚠️ Il «bump attack» e' l'attacco che parte camminando addosso a qualcuno, e in "
     "dizionario non c'era: le uniche voci con «bump» sono onomatopee («*tonf*», "
     "action.hsp:2269). «per contatto» dice come si fa partire, che e' quel che il "
     "ritocco impedisce. "),
    (1634, 'voce', [('"Fist of the North Star Mode."', '"Modalita\' Ken il guerriero."')], 1,
     "⭐⭐ In Italia la serie si chiama **«Ken il guerriero»**, ed e' con quel nome che il "
     "giocatore la riconosce: «Il pugno della stella del nord» sarebbe stato fedele e "
     "illeggibile. E' il caso in cui tradurre alla lettera perde proprio la cosa che la "
     "riga vuole dire. "),
    (1635, 'voce', [('"Disable cicada noises."', '"Togli il frinire delle cicale."')], 1,
     "«cicada» -> «cicala» (db_item.hsp:135237 «cicala morente»). «frinire» e' il verbo "
     "italiano proprio per il verso della cicala. "),
    (1636, 'voce', [('"Faster Fishing Animation."', '"Animazione della pesca piu\' veloce."')], 1,
     "«fishing» -> «pesca» (skill.hsp:367). "),
    (1637, 'voce', [('"Use CGX Arrow/Bolt/Ball Spell Animation."',
                     '"Usa le animazioni CGX di freccia, saetta e sfera."')], 1,
     "⭐ I tre tipi di magia hanno gia' un nome in italiano e sono decine di voci: «bolt» "
     "-> «saetta» (skill.hsp:504-:549, «Saetta di gelo», «Saetta di fuoco»…), «ball» -> "
     "«sfera» (db_item.hsp:138050 «sfera di bolle», :139922 «sfera di fulmine»), «arrow» "
     "-> «freccia» (db_item.hsp:149300 «freccia magica»). ⚠️ E la barra dell'inglese e' "
     "un elenco, non una scelta: l'italiano scrive la virgola e la «e». "),
    (1638, 'voce', [('"Display Day/Night Cycle Everywhere."',
                     '"Mostra il ciclo giorno-notte dappertutto."')], 1, ""),
    (1639, 'voce', [('"Draw Local/World map when using \'map\' item."',
                     '"Disegna la mappa locale o del mondo con la \'mappa\'."')], 1,
     "⚠️ L'oggetto si chiama «mappa» (db_item.hsp:150869) e l'inglese lo cita fra apici "
     "perche' e' il nome dell'oggetto: l'italiano fa uguale. "),
    (1640, 'voce', [('"(MMA) Use Melee-Weapon-Swing Animation."',
                     '"(MMA) Usa l\'animazione del colpo di mischia."')], 1,
     "⚠️ `(MMA)` e' il nome di un ramo di codice e resta. "),
    (1641, 'voce', [('"Load Animated Tachi-E."', '"Carica i ritratti animati."')], 1,
     "«Tachi-E» (立ち絵) e' il disegno a figura intera del personaggio, che la 50a ha "
     "gia' reso «ritratto» (custom_tweaks.hsp:462). "),
    (1642, 'voce', [('"Always draw Tachi-E on Main Screen."',
                     '"Disegna sempre il ritratto sullo schermo di gioco."')], 1,
     "«Main Screen» e' la schermata di gioco vera e propria, non un menu: «schermo di "
     "gioco». "),
    (1643, 'voce', [('"Draw items with translucency when overlapped with something."',
                     '"Disegna semitrasparenti gli oggetti coperti da qualcosa."')], 1, ""),
    (1644, 'voce', [('"Draw Tag-Team character with X-offset."',
                     '"Sposta di lato il personaggio in coppia."')], 1,
     "⭐ «tag-team» e' «coppia» in tutto il progetto (action.hsp:10861 «Chi e' in coppia "
     "non si puo' appendere», proc.hsp:10793, skill.hsp:1477 «Rafforza la coppia»): non "
     "si inventa un termine tecnico per l'occasione. «X-offset» e' uno spostamento "
     "orizzontale, cioe' «di lato». "),
    (1645, 'voce', [('"(MMA) Use ASync animations."', '"(MMA) Usa le animazioni asincrone."')], 1, ""),

    # ── le quattordici descrizioni che si traducono ─────────────────────────
    #    (la quindicesima, :1679 «Nani?!», si lascia: vedi in cima)
    (1670, 'descrizione',
     [('"Will make MP3s start playback from a random point.\\nCould cause compatability issues."',
       '"Gli MP3 partono da un punto a caso invece che dall\'inizio.\\nPuo\' dare '
       'problemi di compatibilita\'."')], 1, ""),
    (1673, 'descrizione',
     [('"Weather effects will display in all areas."',
       '"Gli effetti del tempo si vedono in tutte le zone."')], 1, ""),
    (1676, 'descrizione',
     [('"Prevents you from performing a melee attack when bumping into others."',
       '"Impedisce di attaccare corpo a corpo camminando addosso agli altri."')], 1, ""),
    (1682, 'descrizione',
     [('"Prevents cicada noises from playing during the summer months."',
       '"Toglie il frinire delle cicale nei mesi d\'estate."')], 1, ""),
    (1685, 'descrizione',
     [('"Makes fishing animations much faster. \\nAnd instant dimensional fishing with a super lure."',
       '"Rende molto piu\' veloci le animazioni della pesca.\\nE con la super esca la '
       'pesca dimensionale e\' immediata."')], 1,
     "⭐ «dimensional fishing» e' l'abilita' «Pesca dimensionale» (skill.hsp:1608, e "
     "proc.hsp:19307 «Cominci la pesca dimensionale»), «super lure» e' la «super esca» "
     "(db_item.hsp:140140, proc.hsp:5082): tutt'e due gia' rese, e la riga le nomina "
     "come il giocatore le legge. "),
    (1688, 'descrizione',
     [('"Use Custom Animation for Arrow/Bolt/Ball spell animations. \\nIf it causes '
       'crashes, make sure you have the files in \'graphic/custom_animation\' folder."',
       '"Usa le animazioni di Custom-GX per freccia, saetta e sfera.\\nSe il gioco va in '
       'crash, controlla che i file siano nella cartella\\n\'graphic/custom_animation\'."')], 1,
     "⚠️ Il percorso della cartella e' un percorso vero sul disco e non si traduce. "
     "⚠️ L'inglese sta su due righe e l'italiano su tre: l'a capo in piu' serve a "
     "staccare il percorso, che altrimenti spezzerebbe la riga in un punto qualunque. "),
    (1691, 'descrizione',
     [('"Day/Night will display in all areas.\\nSome area will be unnavigably dark like Devil\'s Cape."',
       '"Il ciclo giorno-notte si vede in tutte le zone.\\nIn certe sara\' buio pesto, '
       'come al Capo del Diavolo."')], 1,
     "⭐ «Devil Cape» e' gia' «Capo del Diavolo» (text.hsp:2845): e' un posto sulla "
     "mappa del mondo, e va chiamato col nome che porta li'. "),
    (1694, 'descrizione',
     [('"Draw a local map / world map when using the \'map\' item.\\nTiles undiscovered are not shown."',
       '"Disegna la mappa della zona o del mondo quando usi l\'oggetto mappa.\\nLe '
       'caselle non ancora esplorate non si vedono."')], 1,
     "⚠️ **«casella» e' una parola nuova**: nessuna resa del progetto aveva mai avuto "
     "bisogno di nominare il quadretto di mappa. E' la parola italiana normale per un "
     "quadretto di griglia, e serve anche a :1703. "),
    (1697, 'descrizione',
     [('"Use Melee-Weapon-Swing attack animation from MMA branch."',
       '"Usa l\'animazione del colpo di mischia del ramo MMA."')], 1, ""),
    (1700, 'descrizione',
     [('"Load Animated Tachi-E.\\nUse Frames like face4_B1.bmp~face4_B100.bmp.\\nUses '
       'default face_B.bmp when there\'s no animation.\\n(Heavy Disc Reading)"',
       '"Carica i ritratti animati.\\nI fotogrammi vanno da face4_B1.bmp a '
       'face4_B100.bmp.\\nSenza animazione usa il face_B.bmp normale.\\n(Legge molto dal '
       'disco.)"')], 1,
     "⚠️ I nomi dei file restano: sono file veri che il giocatore deve creare col nome "
     "giusto. «frame» -> «fotogramma». "),
    (1703, 'descrizione',
     [('"Draw Tachi-E of destinated character for RP purposes.\\nThis will also shift '
       'screen center 3 tiles left.\\nDoes not work in pet arena."',
       '"Disegna il ritratto del personaggio scelto, per il gioco di ruolo.\\nSposta '
       'anche il centro dello schermo di tre caselle a sinistra.\\nNon funziona '
       'nell\'arena delle bestie."')], 1,
     "⭐ «pet arena» e' «l'arena delle bestie» (db_creature.hsp:118259 «l'organizzatore "
     "dell'arena delle bestie», map.hsp:5478). «RP» -> «gioco di ruolo», per esteso "
     "perche' la sigla inglese in italiano non si legge. "),
    (1706, 'descrizione',
     [('"Draw items with 50% transparency when an NPC is behind it."',
       '"Disegna gli oggetti al 50% di trasparenza quando coprono un PNG."')], 1,
     "⚠️ L'inglese dice «when an NPC is behind it» e l'italiano gira la frase — «quando "
     "coprono un PNG» — perche' il soggetto della riga sono gli oggetti, che sono anche "
     "quel che il ritocco disegna. "),
    (1709, 'descrizione',
     [('"Adjust the positioning of tag-team leader 12-px to the left.\\nEnsuring they '
       'are not centered exclusively on the tag-leader,\\n but rather equally spaced '
       'between the two members of the team."',
       '"Sposta di 12 px a sinistra il capo della coppia.\\nCosi\' lo schermo non e\' '
       'centrato solo su di lui,\\n ma a meta\' strada fra i due della coppia."')], 1,
     "⚠️ Lo spazio a inizio terza riga c'e' anche nell'inglese e si conserva: e' un "
     "rientro voluto. «tag-leader» e «tag-team leader» sono la stessa cosa e l'italiano "
     "li dice tutt'e due «il capo della coppia». "),
    (1712, 'descrizione',
     [('"(MMAH) Render queued animations in ASync mode. \\n  E.g. Death animations will '
       'all play at the same time, instead of one by one."',
       '"(MMAH) Disegna le animazioni in coda in modo asincrono.\\n  Per esempio le '
       'morti si vedono tutte insieme, non una per volta."')], 1,
     "⚠️ I due spazi a inizio seconda riga sono un rientro dell'inglese e restano. "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')


def _letterale(pezzo: str) -> str:
    return pezzo.strip('"').replace('\\n', '\n')


nuove = []
for riga, tipo, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != attese:
            raise SystemExit(
                f'{NOME}:{riga} compare {quante} volte nel {eti}, non {attese}')

    nuova = originale
    for cerca, metti in sostituzioni:
        if nuova.count(cerca) != 1:
            raise SystemExit(
                f'{NOME}:{riga}: `{cerca[:60]}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)

    tetto = TETTO_VOCE if tipo == 'voce' else TETTO_DESCRIZIONE
    pezzi = _letterale(sostituzioni[0][1]).split('\n')
    for pezzo in pezzi:
        if len(pezzo) > tetto:
            raise SystemExit(
                f'{NOME}:{riga}: {len(pezzo)} caratteri, tetto {tetto} — {pezzo!r}')
    largo = max(len(p) for p in pezzi)

    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + MENU_VARI + CLASSE
    toppa['_riga'] = riga
    toppa['_quante'] = attese
    toppa['_largo'] = largo
    nuove.append(toppa)

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
da_scrivere = [t for t in nuove if _chiave(t) not in gia]

if not da_scrivere:
    print('toppe gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = ''.join(
        json.dumps({k: v for k, v in t.items() if not k.startswith('_')},
                   ensure_ascii=False) + '\n'
        for t in da_scrivere
    ).encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    coperte = sum(t['_quante'] for t in da_scrivere)
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)}), '
          f'{coperte} righe coperte')
    print('⚠️ :1679 «Nani?!» lasciata in inglese apposta: la citazione e\' il punto.')
    for t in da_scrivere:
        print(f"  :{t['_riga']}  (largo {t['_largo']})")
        print(f"    + {t['sostituisci'].strip()[:120]}")
