# -*- coding: utf-8 -*-
"""Il menu dei ritocchi di comodita' (`*ConvenienceTweakMenu_loop`, :560-:787).

Diciotto voci e diciotto descrizioni: **36 righe**. Titolo, riga di testa e voce
di ritorno erano gia' chiusi dalle toppe `tutte` del menu principale.

## Il vocabolario, e quattro voci di menu che il gioco ha gia'

⭐ **Quattro di queste righe nominano comandi che il giocatore usa gia'**, e
vanno chiamati con la parola esatta che sta nel menu, non con un sinonimo:

    Feed             -> «Dai da mangiare»    command.hsp:5976
    Give             -> «Dai qualcosa»       command.hsp:5970
    Pickpocket       -> Borseggio            action.hsp:7302
    Mining           -> Scavo                action.hsp:7224
    Undead return    -> «Ritira i non-morti» text.hsp:2089
    Necro Force      -> «Forza necromantica» skill.hsp:1492
    Necro Fusion     -> «Fusione dei morti»  action.hsp:11702

E il resto, verificato uno per uno:

    ranch            -> allevamento          db_item.hsp:139803, action.hsp:2714
    deed             -> atto                 db_item.hsp:134277 e altre dodici
    furniture        -> mobilio              text.hsp:9671
    register         -> registratore di cassa  db_item.hsp:145097
    shop strongbox   -> cassaforte del negozio db_item.hsp:145110
    fruit tree       -> albero da frutto     db_item.hsp:145586
    chest            -> baule                db_item.hsp:148684
    leash            -> guinzaglio           action.hsp:10787, :10822
    Ensemble         -> Ensemble             skill.hsp:1172 (non si traduce)
    DD cemetery key  -> chiave del cimitero DD  db_item.hsp:138639
    Garok            -> Garok                db_creature.hsp:118328
    Yes              -> Si'                  text.hsp:196
    bash             -> caricare             command.hsp:5279, action.hsp:1732

⭐ **«red book» non e' un libro rosso.** `ITEM_ID_RED_BOOK` ha
`ioriginalnameref = "book"` (`db_item.hsp:152478`), reso **«libro»**: il
«red» e' il colore dello sprite nel nome interno, non una parola che il
giocatore legga. Tradurlo «libri rossi» avrebbe inventato un oggetto che non
esiste.

## ⚠️⚠️ La terza incoerenza della giornata: negromanzia / necromantica

Il dizionario ha **tutt'e due le radici**, una volta per uno:
- `db_item.hsp:139896` «coffin of necromancy» -> «bara della **negro**manzia»
- `skill.hsp:1492` «Necro Force» -> «Forza **necro**mantica»

⚠️ E i lotti di oggi hanno spostato il conteggio: il menu dell'IA e quello di
difficolta' hanno scritto «negromanzia» altre due volte, quindi adesso e' 3 a 1.
✅ «Negromanzia» e' la forma italiana tradizionale (come «negromante») ed e' la
scelta giusta; ⚠️ ma qui `:654` deve dire **«Forza necromantica»** lo stesso,
perche' e' il nome che il giocatore legge nella lista delle abilita'. Come per
fattura/bolletta: si nomina la cosa col nome che porta a schermo, e si segna il
debito invece di nasconderlo.

## Due battute che in italiano non esistono

⭐ `:660` «if you don't want to be the cool-aid man don't enable this» cita il
**Kool-Aid Man**, il pupazzo della pubblicita' americana che sfonda i muri. In
Italia non lo conosce nessuno e non c'e' un gemello: la resa tiene l'immagine
(«sfondare i muri come un ariete») e lascia cadere il nome, che da solo non
direbbe niente.
⭐ `:574` «Everything must go!» e' il grido dei saldi di liquidazione: «Tutto
deve sparire!» e' la formula italiana corrispondente.

## La larghezza

Voci a `wx + 64` (576 px, **74** caratteri col metro prudente); qui sono tutti
interruttori, quindi il suffisso e' sempre « (Ora: acceso)», 14 caratteri.
Descrizioni a `wx + 38` (602 px, **78** per riga).
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

TETTO_DESCRIZIONE = 78
SUFFISSO = ' (Ora: acceso)'   # in questo menu sono tutti interruttori
TETTO_VOCE = 74 - len(SUFFISSO)

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_COMODITA = (
    "Sta nel menu dei ritocchi di comodita' (`*ConvenienceTweakMenu_loop`), uno dei "
    "sette menu di dettaglio del pannello dei ritocchi di Custom-GX — la categoria di "
    "quelli che tolgono attriti (custom_tweaks.hsp:105). La finestra e' 640: le voci "
    "hanno 74 caratteri col metro prudente, suffisso di stato compreso (qui sempre "
    "« (Ora: acceso)», perche' sono tutti interruttori), e le descrizioni 78 per riga. "
)

# (riga, tipo, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = [
    # ── le diciotto voci ────────────────────────────────────────────────────
    (567, 'voce', [('"Add Feed Option For Pets."', '"Aggiungi \'Dai da mangiare\' per gli alleati."')], 1,
     "⭐ «Feed» non si traduce a orecchio: e' una voce del menu degli alleati che il "
     "gioco chiama gia' «Dai da mangiare» (command.hsp:5976), e va citata con quella "
     "parola. ⚠️ Apici semplici e non virgolette a caporale: CP932 non ha «». "),
    (568, 'voce', [('"Can Change Item Sprites In Home."', '"Cambia lo sprite degli oggetti in casa."')], 1,
     "⚠️ «sprite» resta: il progetto lo lascia cosi' anche altrove (command.hsp:160 «ID "
     "sprite: »), ed e' la parola con cui chi gioca a Elona chiama l'immaginetta. "),
    (569, 'voce', [('"Display Pickpocket shortcut."', '"Mostra la scorciatoia per il borseggio."')], 1,
     "«Pickpocket» e' l'abilita' «Borseggio» (action.hsp:7302). "),
    (570, 'voce', [('"Gather Items At End Of Party Time."', '"Raccogli gli oggetti a fine festa."')], 1,
     "«Party Time!» e' l'evento «Si balla!» (text.hsp:131); qui la voce dice solo «a "
     "fine festa» perche' il nome per esteso lo da' la descrizione di :618. "),
    (571, 'voce', [('"Share Gold For Group Performance."', '"Dividi l\'oro guadagnato suonando insieme."')], 1,
     "proc.hsp:1035 dice gia' «Il pubblico lascia al gruppo N monete d'oro in tutto: … "
     "il resto va agli alleati», che e' esattamente quel che questo ritocco cambia. "),
    (572, 'voce', [('"Bash all fruit."', '"Fai cadere tutta la frutta."')], 1,
     "⚠️ «bash» il gioco lo rende «caricare» (command.hsp:5279 «In che direzione vuoi "
     "caricare?»), ma qui il punto non e' il colpo, e' la frutta che viene giu': la "
     "voce dice il risultato e la descrizione di :624 nomina la carica. "),
    (573, 'voce', [('"Organize ranch produce."', '"Metti in ordine i prodotti dell\'allevamento."')], 1,
     "«ranch» -> «allevamento» (db_item.hsp:139803, action.hsp:2714 «funziona solo negli "
     "allevamenti di tua proprieta'»). "),
    (574, 'voce', [('"Everything must go!"', '"Tutto deve sparire!"')], 1,
     "⭐ E' il grido dei saldi di liquidazione, e l'italiano ne ha uno suo: «Tutto deve "
     "sparire!». Tradurlo alla lettera («Tutto deve andare») avrebbe perso il modo di "
     "dire, che qui e' tutto il contenuto della riga. "),
    (575, 'voce', [('"Throw potion at self with [t]."', '"Tirati addosso una pozione con [t]."')], 1,
     "⚠️ La lettera fra parentesi quadre e' il tasto e resta `[t]`. "),
    (576, 'voce', [('"Allow running in world map."', '"Permetti di correre sulla mappa del mondo."')], 1, ""),
    (577, 'voce', [('"Skip skill training confirmation."', '"Salta la conferma per allenare le abilita\'."')], 1, ""),
    (578, 'voce', [('"Auto-drop opened chests."', '"Lascia a terra i bauli gia\' aperti."')], 1,
     "«chest» -> «baule» (db_item.hsp:148684). "),
    (579, 'voce', [('"Remove spell over-cast confirmation."', '"Togli la conferma per lanciare senza mana."')], 1,
     "⭐ La conferma di cui parla la riga e' proc.hsp:6636, che l'italiano rende gia' "
     "«Non hai abbastanza mana. Vuoi tentare il lancio lo stesso?»: «over-cast» in "
     "italiano non e' una parola, e la voce dice la cosa — lanciare senza mana. "),
    (580, 'voce', [('"Auto Hand-in quests."', '"Consegna da solo gli incarichi."')], 1, ""),
    (581, 'voce', [('"Sort spells by spell type."', '"Ordina le magie per tipo."')], 1,
     "⚠️ L'inglese ripete «spell» due volte; l'italiano lo dice una volta sola perche' "
     "«per tipo» dopo «le magie» non puo' voler dire altro. "),
    (582, 'voce', [('"Necromancy zombies goes inside DD-Cemetry when they die."',
                    '"Gli zombi della negromanzia vanno nel cimitero DD da morti."')], 1,
     "«DD cemetery key» e' gia' «chiave del cimitero DD» (db_item.hsp:138639), quindi il "
     "posto e' «il cimitero DD». ⚠️ L'inglese scrive «DD-Cemetry», con un refuso; "
     "l'italiano no. "),
    (583, 'voce', [('"Allow leashing temporary allies."', '"Permetti il guinzaglio sugli alleati temporanei."')], 1,
     "«leash» -> «guinzaglio» (action.hsp:10787 «Chi metti al guinzaglio?», :10822). "),
    (584, 'voce', [('"Auto dig walls when running into them."', '"Scava i muri da solo andandoci addosso."')], 1, ""),

    # ── le diciotto descrizioni ─────────────────────────────────────────────
    (609, 'descrizione',
     [('"Adds a Feed option that works like Give but that filters out non-food items '
       'when\\ninteracting with pets. Also allows for feeding pets raw equipment."',
       '"Aggiunge \'Dai da mangiare\', che funziona come \'Dai qualcosa\' ma con '
       'gli\\nalleati mostra solo il cibo.\\nE permette di dar loro anche '
       'equipaggiamento crudo."')], 1,
     "⭐ Le due voci di menu si chiamano col loro nome: «Dai da mangiare» "
     "(command.hsp:5976) e «Dai qualcosa» (command.hsp:5970). ⚠️ L'inglese sta su due "
     "righe e l'italiano su tre, perche' la seconda frase e' una cosa a se'. "),
    (612, 'descrizione',
     [('"Adds a new menu item to blacksmiths in your home that allows you to '
       'change\\nitem sprites like at Garok."',
       '"Aggiunge una voce all\'armeria di casa tua per cambiare lo sprite\\ndegli '
       'oggetti, come si fa da Garok."')], 1,
     "«Blacksmith» -> «Armeria» (text.hsp:1618), Garok resta (db_creature.hsp:118328 "
     "«<Garok> il fabbro leggendario»). "),
    (615, 'descrizione',
     [('"Adds a \\"Yes/No\\" dialogue box when attempting to pick up items that '
       'do\\nnot belong to you outside of quests and moongates."',
       '"Aggiunge una domanda \\"Si\'/No\\" quando provi a raccogliere roba che\\nnon '
       'e\' tua, fuori dagli incarichi e dai cancelli lunari."')], 1,
     "⚠️ Le virgolette dentro la stringa sono protette con la barra rovesciata e restano "
     "protette. «Yes» -> «Si'» (text.hsp:196; l'accento vero non si puo' scrivere "
     "perche' le toppe non passano da `accenti.py`). «moongate» -> «cancello lunare» "
     "(db_item.hsp:144121). "),
    (618, 'descrizione',
     [('"When a Party Time! quest ends, you will be presented with a list of items on '
       'the\\nfloor that you can take."',
       '"Quando finisce l\'incarico \'Si balla!\', ti compare l\'elenco delle '
       'cose\\nrimaste a terra che puoi prendere."')], 1,
     "⭐ «Party Time!» e' il nome dell'evento e il progetto lo rende «Si balla!» "
     "(text.hsp:131). "),
    (621, 'descrizione',
     [('"When performing an ensemble with pets, your pets will receive a portion\\nof '
       'all gold earned."',
       '"Quando suoni un ensemble con gli alleati, a loro va una parte\\ndi tutto l\'oro '
       'guadagnato."')], 1,
     "⚠️ «Ensemble» NON si traduce: e' il nome dell'abilita' (skill.hsp:1172) e "
     "proc.hsp:19178 dice gia' «Tu e i tuoi compagni cominciate l'ensemble». "),
    (624, 'descrizione',
     [('"Bash all fruit out of fruit trees in one go."',
       '"Carica l\'albero da frutto e fai cadere tutta la frutta in una volta."')], 1,
     "«fruit tree» -> «albero da frutto» (db_item.hsp:145586); «bash» -> «caricare», il "
     "verbo che il gioco usa gia' (action.hsp:1732 «Carichi la porta e la sfondi»). "),
    (627, 'descrizione',
     [('"Better organize the ranch by collecting all ranch produce in one spot (x17 y14)."',
       '"Mette in ordine l\'allevamento: i prodotti vanno tutti in un punto (x17 y14)."')], 1,
     "⚠️ Le coordinate restano come sono: servono a chi va a cercare la roba. "),
    (630, 'descrizione',
     [('"Allows shops to sell furniture, red books, and deeds. Registers,\\nshop '
       'strongboxes, shelters, and unique items still won\'t be sold."',
       '"Permette ai negozi di vendere mobilio, libri e atti. Restano fuori\\ni '
       'registratori di cassa, le casseforti, i rifugi e i pezzi unici."')], 1,
     "⭐⭐ **«red book» e' semplicemente «libro»**: `ITEM_ID_RED_BOOK` ha "
     "`ioriginalnameref = \"book\"` (db_item.hsp:152478, reso «libro»), e il «red» e' il "
     "colore dello sprite nel nome interno — non una parola che il giocatore legga. "
     "«furniture» -> «mobilio» (text.hsp:9671), «deed» -> «atto» (db_item.hsp:134277 e "
     "altre dodici), «register» -> «registratore di cassa» (:145097), «shop strongbox» "
     "-> «cassaforte del negozio» (:145110), «shelter» -> «rifugio» (:145197). "),
    (633, 'descrizione',
     [('"Adds potions to the [t]ool menu.\\nUsing a potion with this tweak enabled '
       'throws it at your tile."',
       '"Aggiunge le pozioni al menu degli attrezzi, il tasto [t].\\nCon questo ritocco, '
       'usare una pozione la tira sulla tua casella."')], 1,
     "⚠️ L'inglese segna il tasto dentro la parola («[t]ool»), che in italiano non si "
     "puo' fare con «attrezzi»: il tasto si dice a parte, «il tasto [t]». «casella» e' "
     "la parola fissata nel menu dei ritocchi vari (:1694). "),
    (636, 'descrizione',
     [('"Allows running in the world map by holding Shift."',
       '"Permette di correre sulla mappa del mondo tenendo premuto Shift."')], 1, ""),
    (639, 'descrizione',
     [('"Skips the confirmation when spending platinum coins on skill training."',
       '"Salta la conferma quando spendi monete di platino per allenarti."')], 1,
     "«platinum coin» -> «moneta di platino» (db_item.hsp:152046). "),
    (642, 'descrizione',
     [('"Automatically drops empty chests after they\'ve been opened."',
       '"Lascia a terra da solo i bauli vuoti dopo che li hai aperti."')], 1, ""),
    (645, 'descrizione',
     [('"Removes confirmation window when over-casting spells."',
       '"Toglie la conferma quando lanci una magia senza mana a sufficienza."')], 1,
     "⭐ La finestra e' proc.hsp:6636, gia' resa «Non hai abbastanza mana. Vuoi tentare "
     "il lancio lo stesso?». "),
    (648, 'descrizione',
     [('"Automatically hand-in quests after you complete them.\\nThis applies to '
       'harvest/hunt/trap/party/panic/challenge quests."',
       '"Consegna da solo gli incarichi appena li hai completati.\\nVale per raccolto, '
       'caccia, trappole, festa, panico e sfida."')], 1,
     "⚠️ I sei tipi di incarico non hanno un elenco reso in dizionario, ma il gioco li "
     "descrive uno per uno e da li' vengono le parole: il raccolto (map.hsp:12223 "
     "«raccogliere prodotti agricoli»), le trappole (:12227 «disinnescare N trappole»), "
     "la festa (:12215 «scaldare la festa»), la caccia (:12231 «abbattere»). "),
    (651, 'descrizione',
     [('"Sort spells by spell type."', '"Ordina le magie per tipo."')], 1,
     "⚠️ In inglese la descrizione e' identica alla voce; in italiano pure, ed e' giusto "
     "cosi': sono due righe diverse del sorgente con lo stesso testo, non un errore. "),
    (654, 'descrizione',
     [('"Necromancy zombies goes into DD-Cemetery when they return.\\nThis only '
       'activates if you are holding a DD-Cemetery Key.\\nThis includes: '
       'Pushback/Undead-Return/Killed/Necro-Fusion/Placement-Failure.\\nAlso gives '
       'Necro-Force a Summon-From-DD-Cemetery option."',
       '"Gli zombi della negromanzia rientrano nel cimitero DD.\\nVale solo se hai in '
       'mano la chiave del cimitero DD.\\nComprende: respinta, Ritira i non-morti, '
       'morte,\\nFusione dei morti e posa fallita.\\nE aggiunge a Forza necromantica '
       'l\'evocazione dal cimitero DD."')], 1,
     "⭐⭐ **Tre nomi vanno presi dal gioco, non tradotti**: «Undead-Return» e' «Ritira i "
     "non-morti» (text.hsp:2089), «Necro-Fusion» e' «Fusione dei morti» "
     "(action.hsp:11702) e «Necro-Force» e' «Forza necromantica» (skill.hsp:1492). "
     "⚠️⚠️ E qui casca l'incoerenza: il resto della riga dice «negromanzia» (la forma "
     "italiana tradizionale, gia' in db_item.hsp:139896), ma l'abilita' si chiama "
     "«Forza NECROmantica» nella lista delle abilita', e va nominata come il giocatore "
     "la legge. Il debito e' segnato, non nascosto. ⚠️ E' l'unica descrizione del "
     "pannello su CINQUE righe invece di quattro: i tre nomi presi dal gioco sono piu' "
     "lunghi delle abbreviazioni inglesi («Undead-Return», «Necro-Fusion») e la terza "
     "riga sfondava i 78 caratteri. La finestra regge — `mes` parte da `wy + 343` su "
     "448 di altezza, cioe' 105 px, e a corpo 13 ci stanno sei righe. "),
    (657, 'descrizione',
     [('"Allow leashing temporary allies."',
       '"Permette di mettere al guinzaglio gli alleati temporanei."')], 1, ""),
    (660, 'descrizione',
     [('"Autodig walls when running into them (with shift).\\nEnable with caution if you '
       'have low mining.\\nANd if you don\'t want to be the cool-aid man don\'t enable this."',
       '"Scava i muri da solo quando ci vai addosso (con Shift).\\nAccendilo con prudenza '
       'se hai poco Scavo.\\nE se non vuoi sfondare i muri come un ariete, lascialo '
       'spento."')], 1,
     "⭐⭐ L'ultima riga cita il **Kool-Aid Man**, il pupazzo della pubblicita' americana "
     "che entra sfondando i muri. In Italia non lo conosce nessuno e non ha un gemello: "
     "la resa tiene l'immagine («sfondare i muri come un ariete») e lascia cadere il "
     "nome, che da solo non direbbe niente. «Mining» -> «Scavo» (action.hsp:7224). "
     "⚠️ Il refuso dell'inglese («ANd») non si riporta. "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')


def _letterale(pezzo: str) -> str:
    """Il testo come lo vede il giocatore: senza virgolette esterne, senza le
    barre rovesciate di protezione, e con i `\\n` resi a capo veri."""
    return pezzo.strip('"').replace('\\"', '"').replace('\\n', '\n')


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
    toppa['motivo'] = motivo + MENU_COMODITA + CLASSE
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
    for t in da_scrivere:
        print(f"  :{t['_riga']}  (largo {t['_largo']})")
        print(f"    + {t['sostituisci'].strip()[:120]}")
