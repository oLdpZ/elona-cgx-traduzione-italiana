# -*- coding: utf-8 -*-
"""Il menu dei ritocchi al gioco (`*GameplayTweakMenu_loop`, :796-:1211).

**69 righe** — 36 voci e 33 descrizioni — ed e' il piu' grosso dei sette menu
di dettaglio, l'ultimo che restava del pannello. Titolo, riga di testa e le due
voci di ritorno erano gia' chiusi dalle toppe del menu principale.

## Tre righe non sono voci: sono titoli di sezione

`:808`, `:826` e `:838` sono `=== … ===`, cioe' separatori dentro l'elenco. Non
hanno suffisso di stato e non hanno descrizione: sono le tre parti in cui il
menu si divide, e in italiano si accorciano perche' le cornici di uguali
rubano posto e il titolo deve stare in mezzo.

## Il vocabolario: quasi tutto nomi che il gioco ha gia'

Questo menu e' quasi solo rimandi a cose che esistono altrove, e il lavoro e'
stato andarle a prendere una per una invece di tradurle a orecchio:

    Curtain Call     -> Chiamata alla ribalta   proc.hsp:4650, db_creature.hsp:101104
    Gravity Sphere   -> Sfera di gravita'       skill.hsp:1232
    Graviton Buster  -> Colpo gravitonico       skill.hsp:1432
    Violent Garden   -> Giardino violento       skill.hsp:1704
    Shadow Step      -> Passo d'ombra           skill.hsp:932
    Gauge Release    -> Forza liberata          custom_tweaks.hsp:1255
    Deep-Sea Castle  -> Castello del Drago a Nove Teste   map.hsp:8408
    sandbag          -> sacco da botte          action.hsp:10916
    Wetting          -> Idratazione             text.hsp:64
    thirst           -> sete                    text.hsp:64, calculation.hsp:1697
    Dim              -> Stordimento             text.hsp:71
    burst / rapid ammo -> munizioni a raffica / rapide   text.hsp:2472, :2484
    stray cat        -> gatto randagio          action.hsp:16971
    town child       -> bambino di citta'       db_creature.hsp:104004
    Little Sister    -> <Little Sister>         db_creature.hsp:124417 (non si traduce)
    mega mole        -> talpa gigante           db_creature.hsp:79002
    talpidae         -> talpa oscura            db_creature.hsp:78930
    Aile             -> <Aile>                  db_creature.hsp:83196
    study day        -> giornata da studio      text.hsp:48
    Dojo             -> Dojo                    text.hsp:3036 (non si traduce)
    Abnormal         -> Abnormal                chara.hsp:4179 (nome di modalita')
    DV               -> DV                      command.hsp:17679 (non si traduce)
    godly (qualita') -> celestiale               text.hsp:106
    Blunt            -> Contundenti             skill.hsp:146
    gli elementi     -> fulmine, mente, oltretomba, suono, nervi, caos   skill.hsp:80-115

⭐ **«stamina» e' «SP»**, come deciso nella 50a (`buff.hsp:735`,
`item_data.hsp:613`): sei righe di questo menu la nominano e tutte dicono SP.

⭐ **«Abnormal» non si traduce, e non e' una scelta mia**: il sorgente
giapponese scrive «Abnormalモード» (`command.hsp:10415`), cioe' lascia la parola
inglese anche in giapponese. E' il nome della modalita'.

⚠️ **«<{enemy}>» resta com'e'** (`:915`): sono le parentesi angolari con cui il
gioco marca i nemici con nome proprio, e la riga parla di quella categoria.

⭐ **«Crush damage» -> «danno contundente»**: non c'e' un elemento «crush» nella
lista di `text.hsp:1951`-`:1981`, ma `skill.hsp:146` rende gia' «Blunt» con
«Contundenti», e questa e' la stessa famiglia di colpi.

## Le versioni non si toccano

Diciassette righe su 69 nominano un numero di versione («post-2.17»,
«post-1.90», «prima di CGX 2.21.2.0»). Sono riferimenti verificabili e restano
tali e quali: la formula italiana e' sempre «di prima della X.YZ», che e' la
piu' corta che dica la stessa cosa.

## La larghezza

Voci a `wx + 64` (576 px, **74** caratteri col metro prudente, suffisso di stato
compreso — qui e' sempre « (Ora: acceso)» tranne a :829, che porta un numero).
Descrizioni a `wx + 38` (602 px, **78** per riga).
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

TETTO_VOCE = 74
TETTO_DESCRIZIONE = 78
SUFFISSO_NORMALE = ' (Ora: acceso)'
SUFFISSI = {
    808: '', 826: '', 838: '',   # i tre separatori non chiamano GetTStatus
    829: ' (Ora: 100)',          # percentuale, ramo :498
}

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_GIOCO = (
    "Sta nel menu dei ritocchi al gioco (`*GameplayTweakMenu_loop`), il piu' grosso dei "
    "sette menu di dettaglio del pannello dei ritocchi di Custom-GX — la categoria di "
    "quelli che riportano indietro meccaniche cambiate da monte (custom_tweaks.hsp:107). "
    "⭐ «stamina» e' «SP», come fissato nella 50a (buff.hsp:735, item_data.hsp:613). "
    "La finestra e' 640: le voci hanno 74 caratteri col metro prudente, suffisso di "
    "stato compreso, e le descrizioni 78 per riga. "
)

# (riga, tipo, [(cerca, metti), …], occorrenze_attese, motivo)
VOCI = [
    # ── sezione 1: i salvataggi ─────────────────────────────────────────────
    (803, 'voce', [('"Re-enable save-scumming."', '"Riattiva il salva-e-ricarica."')], 1,
     "⚠️ «save-scumming» e' gergo inglese e non ha un traducente: «salva-e-ricarica» "
     "dice il gesto, che e' quel che il ritocco riabilita. "),
    (804, 'voce', [('"Enable rare-loot trigger permanently."', '"Bottino raro sempre attivo."')], 1, ""),
    (805, 'voce', [('"Confirm Reload With F2."', '"Chiedi conferma per F2."')], 1,
     "⚠️ Il tasto resta `F2`. La descrizione di :890 cita questa stessa voce fra "
     "virgolette, e le due devono dire la stessa cosa. "),
    (806, 'voce', [('"Option to reload last save after death."',
                    '"Puoi ricaricare l\'ultimo salvataggio dopo la morte."')], 1, ""),

    # ── sezione 2: le meccaniche ────────────────────────────────────────────
    (808, 'voce', [('"=== Gameplay Mechanics changes ==="', '"=== Meccaniche di gioco ==="')], 1,
     "⚠️ Non e' una voce ma un **titolo di sezione**: non chiama `GetTStatus` e non ha "
     "descrizione. In italiano si accorcia perche' le cornici di uguali rubano posto e "
     "il titolo deve restare in mezzo. "),
    (809, 'voce', [('"Disable Harvest Moon Mode for ranches."',
                    '"Niente modalita\' Harvest Moon negli allevamenti."')], 1,
     "⚠️ «Harvest Moon» e' il nome della serie di giochi di campagna a cui la meccanica "
     "si ispira, e in Italia esce con lo stesso nome: non si traduce. «ranch» -> "
     "«allevamento» (db_item.hsp:139803). "),
    (810, 'voce', [('"(Custom-G) Disable chain attacks."', '"(Custom-G) Niente attacchi a catena."')], 1,
     "⚠️ `(Custom-G)` e' il nome di un ramo del mod e resta. "),
    (811, 'voce', [('"(Custom-G) Disable thirst."', '"(Custom-G) Niente sete."')], 1, ""),
    (812, 'voce', [('"Disable urination from fear."', '"Niente pipi\' per la paura."')], 1,
     "⚠️ Il gioco su questo e' esplicito e l'italiano lo resta: girare la frase "
     "(«incontinenza») avrebbe alzato il registro dove l'inglese non lo alza. "),
    (813, 'voce', [('"Disable stamina depletion when attacking."', '"Attaccare non consuma SP."')], 1,
     "⭐ «stamina» -> «SP», la resa fissata nella 50a. ⚠️ E la frase si gira: l'inglese "
     "dice che cosa spegne il ritocco, l'italiano dice che cosa succede quando e' acceso, "
     "che e' piu' corto e piu' chiaro in una voce di menu. "),
    (814, 'voce', [('"Disable depletion when using stairs in Your Home."',
                    '"Le scale di casa tua non consumano SP."')], 1, ""),
    (815, 'voce', [('"Revert post-2.17 cooking result changes."',
                    '"Torna alla cucina di prima della 2.17."')], 1,
     "⚠️ I numeri di versione non si toccano: sono riferimenti verificabili. La formula "
     "«di prima della X.YZ» e' la piu' corta che dica quel che dice «revert post-». "),
    (816, 'voce', [('"Revert post-2.17 boss out-of-sight healing."',
                    '"Torna alle cure dei capi fuori vista di prima della 2.17."')], 1,
     "«boss» -> «capo» (db_creature.hsp:96717, :115450). "),
    (817, 'voce', [('"Revert post-2.08 elemental mechanics changes."',
                    '"Torna agli elementi di prima della 2.08."')], 1, ""),
    (818, 'voce', [('"Revert post-2.22 ranged ammo nerf."',
                    '"Torna alle munizioni di prima della 2.22."')], 1, ""),
    (821, 'voce', [('"Revert Gauge-Release Toggle post-2.24."',
                    '"Torna alla Forza liberata di prima della 2.24."')], 1,
     "⭐ «Gauge Release» e' «<Forza liberata>» (custom_tweaks.hsp:1255) e «Gauge "
     "Save/Release» e' «<Serba/libera la forza>» (skill.hsp:1528): e' un'abilita' vera "
     "e va nominata come il giocatore la legge. "),
    (822, 'voce', [('"Disable Mob begging-for-life System post-2.27."',
                    '"Niente mostri che implorano pieta\', come prima della 2.27."')], 1, ""),

    # ── sezione 3: esperienza e crescita ────────────────────────────────────
    (826, 'voce', [('"=== EXP/Progression related changes ==="', '"=== Esperienza e crescita ==="')], 1,
     "⚠️ Titolo di sezione, non voce. "),
    (827, 'voce', [('"Sandbag training."', '"Allenamento col sacco da botte."')], 1,
     "⭐ «sandbag» e' il «sacco da botte» (action.hsp:10916 «Il sacco da botte e' "
     "d'intralcio»). "),
    (828, 'voce', [('"Summoned monster training."', '"Allenamento sui mostri evocati."')], 1, ""),
    (829, 'voce', [('"Increase Dojo EXP gain: "', '"Piu\' esperienza al Dojo: "'),
                   ('"% increase."', '"% in piu\'."')], 1,
     "⚠️ **Due letterali sulla stessa riga**, col secondo in coda al suffisso di stato: "
     "a schermo esce «Piu' esperienza al Dojo:  (Ora: 30)% in piu'.». «Dojo» resta "
     "(text.hsp:3036). "),
    (830, 'voce', [('"Revert post-1.90 weapon skill exp formula changes."',
                    '"Torna all\'esperienza con le armi di prima della 1.90."')], 1, ""),
    (831, 'voce', [('"Disable study days (triple skill exp)"',
                    '"Niente giornate da studio (esperienza tripla)"')], 1,
     "⭐ «study day» e' «Giornata da studio» (text.hsp:48, dove sta l'elenco intero: "
     "allenamento, battaglia, lavoro, esplorazione, studio). ⚠️ La parentesi senza punto "
     "finale e' dell'inglese e resta. "),
    (832, 'voce', [('"Disable DESTINY."', '"Niente DESTINO."')], 1,
     "⚠️ Il maiuscolo e' dell'inglese, che grida il nome del sistema, e l'italiano lo "
     "tiene. La descrizione di :950 lo ripete. "),
    (833, 'voce', [('"Revert post-2.13 combat exp formula changes."',
                    '"Torna all\'esperienza in battaglia di prima della 2.13."')], 1, ""),
    (834, 'voce', [('"Revert post-2.17 skill exp formula changes."',
                    '"Torna all\'esperienza nelle abilita\' di prima della 2.17."')], 1, ""),
    (835, 'voce', [('"Revert post-2.31 4x exp bonus on low-level skills."',
                    '"Niente bonus x4 sulle abilita\' basse, come prima della 2.31."')], 1,
     "⚠️ E' la voce piu' lunga del menu: 74 caratteri col suffisso, esattamente il metro "
     "prudente. La resa diretta («Torna al bonus x4 sulle abilita' di basso livello di "
     "prima della 2.31») sfondava, e diceva anche il contrario — «revert» qui vuol dire "
     "TOGLIERE il bonus, non rimetterlo. "),

    # ── sezione 4: anti-abusi e varie ───────────────────────────────────────
    (838, 'voce', [('"=== Anti-powergaming/Misc changes ==="', '"=== Anti-abusi e varie ==="')], 1,
     "⚠️ Titolo di sezione, non voce. «powergaming» e' gergo inglese senza traducente: "
     "«abusi» e' quel che il gioco cerca di impedire, e la descrizione di :967 lo "
     "spiega per esteso. "),
    (839, 'voce', [('"(Custom-G) Disable Curtain Call."', '"(Custom-G) Niente Chiamata alla ribalta."')], 1,
     "⭐ «Curtain Call» e' «Chiamata alla ribalta» (proc.hsp:4650, db_creature.hsp:101104 "
     "«E' finita anche la chiamata alla ribalta»), la stessa resa che la 50a ha messo "
     "nella barra di stato. "),
    (840, 'voce', [('"(Custom-G) Disable skill SP cost nerfs."',
                    '"(Custom-G) Niente rincari di SP sulle abilita\'."')], 1,
     "⚠️ «nerf» e' gergo e non si traduce con una parola: qui sono aumenti di costo, "
     "cioe' «rincari», che e' italiano corrente e dice esattamente la cosa. "),
    (841, 'voce', [('"(Custom-G) Disable multi-attack-critical nerfs."',
                    '"(Custom-G) Niente tagli ai critici multipli."')], 1, ""),
    (842, 'voce', [('"(Custom-G) Disable sleep prevention."', '"(Custom-G) Niente antisonno."')], 1,
     "La descrizione di :976 dice di che si tratta: caffe' e tabacco. "),
    (843, 'voce', [('"(Custom-G) Disable naps while traveling."',
                    '"(Custom-G) Niente pisolini in viaggio."')], 1, ""),
    (844, 'voce', [('"Disable Deep-Sea Castle persistance."',
                    '"Niente persistenza al Castello del Drago a Nove Teste."')], 1,
     "⭐ «Deep-Sea Castle» e' «il Castello del Drago a Nove Teste» (map.hsp:8408): il "
     "nome italiano e' lungo ma e' quello che sta sulla mappa del mondo, e la voce ci "
     "sta lo stesso. ⚠️ L'inglese scrive «persistance» con un refuso. "),
    (845, 'voce', [('"Child, you must go!"', '"Va\' anche tu, bambino!"')], 1,
     "⭐ E' una battuta: il ritocco lascia consegnare gli incarichi usando gli alleati "
     "bambini, e la voce li manda a lavorare. L'italiano tiene lo scherzo e aggiunge "
     "«anche tu», che e' il senso — prima non potevano. "),
    (846, 'voce', [('"Disable Abnormal mode inventory limit"',
                    '"Niente limite d\'inventario in Abnormal"')], 1,
     "⭐ «Abnormal» NON si traduce, e non e' una scelta arbitraria: il sorgente "
     "giapponese scrive «Abnormalモード» (command.hsp:10415, chara.hsp:4179), cioe' "
     "lascia la parola inglese anche in giapponese. E' il nome della modalita'. "
     "⚠️ La riga senza punto finale e' dell'inglese e resta. "),

    # ── le 33 descrizioni ───────────────────────────────────────────────────
    (881, 'descrizione',
     [('"Disables autosaving, re-enables F2 save reloading.\\nThis also disables rare loot trigger."',
       '"Spegne il salvataggio automatico e riattiva il ricarico con F2.\\nE spegne '
       'anche l\'innesco del bottino raro."')], 1, ""),
    (884, 'descrizione',
     [('"Disables rare loot trigger system (Enable the trigger permanently).\\nThis '
       'allow rare items obtainable during first 10 minute of gameplay."',
       '"Spegne il sistema d\'innesco del bottino raro, cioe\' lo tiene sempre '
       'acceso.\\nCosi\' gli oggetti rari escono anche nei primi dieci minuti di gioco."')], 1,
     "⚠️ L'inglese e' contorto apposta («Disables … (Enable the trigger permanently)»): "
     "spegnere l'innesco vuol dire tenerlo sempre acceso. L'italiano lo scioglie con "
     "«cioe'», perche' altrimenti la riga si legge al contrario. "),
    (887, 'descrizione',
     [('"Causes a popup to appear when pressing the F2 key."',
       '"Fa comparire una domanda quando premi F2."')], 1, ""),
    (890, 'descrizione',
     [('"Adds an option to the death menu for reloading from the previous save.\\nIf '
       '\\"Confirm Reload With F2\\" is enabled, you will be warned when playing in a '
       'mode\\nwith a save penalty."',
       '"Aggiunge al menu della morte la voce per ricaricare il salvataggio '
       'prima.\\nCon \\"Chiedi conferma per F2\\" acceso, ti avvisa quando giochi in '
       'una\\nmodalita\' che punisce i salvataggi."')], 1,
     "⚠️ La riga **cita la voce di menu di :805** fra virgolette: le due rese devono "
     "essere identiche, ed e' il motivo per cui vanno nello stesso lotto. "),
    (894, 'descrizione',
     [('"Revert Ano\'s ranch content after version 1.89. Example: \\nLivestock can '
       'randomly become sick, are born unable to be milked, etc.\\n\\nIt is disabled by '
       'default before CGX 2.21.2.0."',
       '"Torna agli allevamenti di Ano di prima della 1.89. Per esempio:\\nil bestiame '
       'puo\' ammalarsi a caso, o nascere senza dare latte.\\n\\nPrima di CGX 2.21.2.0 '
       'era spento di suo."')], 1,
     "«Ano» e' l'autore di Elona+ e il nome resta. ⚠️ La riga vuota in mezzo c'e' anche "
     "nell'inglese e si conserva. "),
    (897, 'descrizione',
     [('"Disables the chain attacks mechanic.\\nThis reduces the damage dealt by '
       'sequential attacks within the attacker\'s turn."',
       '"Spegne gli attacchi a catena.\\nCala il danno dei colpi che si susseguono nello '
       'stesso turno."')], 1, ""),
    (900, 'descrizione',
     [('"Disables the thirst mechanic.\\nThis allows you to survive without drinking, '
       'and also disables the passive\\nstamina regeneration that the \\"Wetting\\" '
       'condition provides."',
       '"Spegne la sete.\\nSi sopravvive senza bere, ma sparisce anche il recupero di '
       'SP\\nche dava lo stato \\"Idratazione\\"."')], 1,
     "⭐ «Wetting» e' lo stato «Idratazione» (text.hsp:64, insieme a «Sete»): e' una "
     "spia che il giocatore vede nella barra, e va chiamata col suo nome. "),
    (903, 'descrizione',
     [('"Prevents characters from urinating when they are afflicted with fear."',
       '"Impedisce che i personaggi se la facciano addosso per la paura."')], 1, ""),
    (906, 'descrizione',
     [('"Disables stamina depletion when attacking or casting spells."',
       '"Attaccare e lanciare magie non consuma piu\' SP."')], 1, ""),
    (909, 'descrizione',
     [('"Using stairs in Your Home will not deplete stamina."',
       '"Prendere le scale di casa tua non consuma SP."')], 1, ""),
    (912, 'descrizione',
     [('"Reverts changes to the cooking product after version 2.17. \\nCooking will give '
       'extra product at cooking lvl 100 and lvl 200. \\nBut will no longer gave extra '
       'enchant or enhance values. \\nOn-eat changes to +enhance post 2.17 do not apply."',
       '"Torna ai risultati di cucina di prima della 2.17.\\nA Cucina 100 e 200 si '
       'ottiene piu\' roba,\\nma niente incantamenti o potenziamenti in piu\'.\\nE i '
       'potenziamenti al momento di mangiare della 2.17 non valgono."')], 1,
     "«enchant» -> «incantamento» (action.hsp:7716), «enhance» -> «potenziare» "
     "(skill.hsp:313 «Potenzia le bacchette», :333 «Potenzia le pozioni»). "),
    (915, 'descrizione',
     [('"Disable the <{enemy}> self-heal anti-cheese mechanics after version 2.17. '
       '\\nThis does not apply to creatures like Megamole/Talpidae/Aile."',
       '"Spegne l\'autocura anti-furbizia dei <{enemy}> introdotta con la '
       '2.17.\\nNon vale per creature come la talpa gigante, la talpa oscura o <Aile>."')], 1,
     "⚠️ **`<{enemy}>` resta com'e'**: sono le parentesi angolari con cui il gioco marca "
     "i nemici con nome proprio, e la riga parla di quella categoria. ⭐ I tre mostri "
     "hanno gia' un nome: «mega mole» -> «la talpa gigante» (db_creature.hsp:79002), "
     "«talpidae» -> «la talpa oscura» (:78930), «<Aile>» resta (:83196 «<Aile> "
     "l'assistente di volo»). «anti-cheese» -> «anti-furbizia»: e' gergo inglese e "
     "l'italiano dice la cosa. "),
    (918, 'descrizione',
     [('"Revert Post-2.08 elemental related changes, this '
       'includes:\\nLightning/Nerve/Mind/Sound/Chaos infliction changes. \\nNether drain '
       'nerf. cResEle bit nerf. Dim Nerf.\\nBreath/Touch skill element power buff. Crush '
       'damage DV resist buff. "',
       '"Torna agli elementi di prima della 2.08. Comprende:\\nle modifiche a fulmine, '
       'nervi, mente, suono e caos;\\nil taglio all\'assorbimento d\'oltretomba, ai bit '
       'cResEle e allo Stordimento;\\nil rinforzo a soffi e tocchi e alla resistenza DV '
       'al danno contundente."')], 1,
     "⭐ I sei elementi hanno gia' un nome (skill.hsp:80-:115 e text.hsp:1951-:1981): "
     "fulmine, nervi, mente, suono, caos, oltretomba. «Dim» e' lo stato «Stordimento» "
     "(text.hsp:71). «cResEle» e' un nome interno e resta. ⭐ «Crush damage» -> «danno "
     "contundente»: non c'e' un elemento «crush» nell'elenco, ma skill.hsp:146 rende "
     "gia' «Blunt» con «Contundenti» ed e' la stessa famiglia di colpi. «DV» non si "
     "traduce (command.hsp:17679). "),
    (921, 'descrizione',
     [('"Revert Post-2.22 ranged ammo nerf.\\nThis allows burst ammo to proc weapon '
       'enchants.\\nThis removes the 1/2 modifier for procs during rapid ammo.\\nNow you '
       'can out-damage every other build by ~1000% with this tweak active."',
       '"Torna alle munizioni di prima della 2.22.\\nLe munizioni a raffica fanno '
       'scattare gli incantamenti dell\'arma.\\nE sparisce il dimezzamento con le '
       'munizioni rapide.\\nCon questo acceso fai circa il 1000% di danni in piu\' di '
       'chiunque."')], 1,
     "⭐ «burst ammo» e «rapid ammo» sono «Munizioni a raffica» e «Munizioni rapide» "
     "(text.hsp:2472 e :2484, item_data.hsp:198). «proc» non ha traducente: «fanno "
     "scattare» dice la cosa. "),
    (929, 'descrizione',
     [('"Revert Post-2.24 Gauge Active method change.\\nBefore 2.24, You press gauge '
       'release before attacking to activate it.\\nAfter 2.24, it was changed to a '
       'toggle on/off.\\nIt also resets Gauge flag at the start of your turn to prevent '
       'misfire."',
       '"Torna al modo di attivare la barra di prima della 2.24.\\nPrima si premeva '
       'Forza liberata e poi si attaccava.\\nDalla 2.24 in poi e\' diventato un '
       'interruttore.\\nE azzera la barra a inizio turno, per non farla partire da '
       'sola."')], 1,
     "⭐ «Gauge Release» e' «Forza liberata» (custom_tweaks.hsp:1255). "),
    (932, 'descrizione',
     [('"Revert Post-2.27 Begging-for-life-Flag setting.\\nThis flag will change hostile '
       'mob NPCs into a pacified state.\\nWhere your bump melee is changed into dialog '
       'with the pacified mob."',
       '"Torna a prima della 2.27, quando i mostri non imploravano pieta\'.\\nCon quella '
       'regola un nemico puo\' passare a uno stato pacifico,\\ne allora andargli addosso '
       'apre un dialogo invece di colpirlo."')], 1,
     "«bump melee» e' l'attacco per contatto, la stessa cosa di custom_tweaks.hsp:1633. "),
    (935, 'descrizione',
     [('"Sandbagged monsters will give experience."',
       '"I mostri usati come sacco da botte danno esperienza."')], 1, ""),
    (938, 'descrizione',
     [('"Summoned monsters and monsters that split up will give experience."',
       '"I mostri evocati e quelli che si sdoppiano danno esperienza."')], 1,
     "«split» -> «sdoppiarsi», come nel menu di difficolta' (chara_func.hsp:8751 «si "
     "sdoppia!»). "),
    (941, 'descrizione',
     [('"Increase Dojo EXP gain. \\nDojo EXP is gained by traveling on world map, at '
       '~3.5 EXP per tile.\\nWhile slightly higher than travel EXP, it may be '
       'underwhelming for \\nthose who doesn\'t visit Dojo very often."',
       '"Alza l\'esperienza che si prende al Dojo.\\nQuell\'esperienza si accumula '
       'viaggiando: circa 3,5 per casella.\\nE\' poco piu\' di quella del viaggio, e chi '
       'al Dojo non ci va spesso\\nnon se ne accorgera\' granche\'."')], 1,
     "⚠️ «3.5» diventa «3,5»: il separatore decimale italiano e' la virgola. «casella» "
     "e' la parola fissata nel menu dei ritocchi vari (:1694). "),
    (944, 'descrizione',
     [('"Reverts changes to the weapon skill experience formula after version '
       '1.90.\\nThis mainly addresses the three-fold increase in player weapon skill exp '
       'gain.\\nIt does not change the study day triple exp bonus."',
       '"Torna alla formula dell\'esperienza con le armi di prima della '
       '1.90.\\nRiguarda soprattutto il triplo di esperienza che prende il '
       'giocatore.\\nNon tocca il bonus triplo delle giornate da studio."')], 1, ""),
    (947, 'descrizione',
     [('"Disables the \\"study day bonus\\" feature.\\nThis will prevent certain skills '
       'from gaining triple skill experience based on the\\nstudy day type."',
       '"Spegne il bonus delle \\"giornate da studio\\".\\nCosi\' certe abilita\' non '
       'prendono piu\' il triplo di esperienza\\na seconda del tipo di giornata."')], 1,
     "⭐ «study day» e' «Giornata da studio» (text.hsp:48). "),
    (950, 'descrizione',
     [('"Disables the \\"DESTINY\\" feature.\\nThis restores the chances of godly '
       'equipment being generated, regardless of\\nDESTINY triggers."',
       '"Spegne il \\"DESTINO\\".\\nRimette le probabilita\' normali per '
       'l\'equipaggiamento celestiale,\\nsenza guardare agli inneschi del DESTINO."')], 1,
     "⭐ «godly» qui e' la **qualita'** dell'oggetto, e li' il progetto la rende "
     "«celestiale» (text.hsp:106, l'elenco scadente/comune/eccellente/eccezionale/"
     "celestiale/speciale). ⚠️ Non e' la stessa cosa dei «nemici divini» del menu di "
     "difficolta': li' era la forza di un nemico, qui e' il grado di un oggetto. "),
    (953, 'descrizione',
     [('"Reverts changes to the killing experience formula after version '
       '2.13.\\nAddresses \\"increased EXP multipliers when defeating enemies above the '
       'PC\'s level\\".\\nToggling this also reverts the changes to the taxation mechanic."',
       '"Torna alla formula dell\'esperienza da uccisione di prima della '
       '2.13.\\nRiguarda i moltiplicatori in piu\' contro nemici di livello '
       'superiore.\\nAccenderlo riporta indietro anche il calcolo delle tasse."')], 1, ""),
    (956, 'descrizione',
     [('"Reverts changes to the skill experience formula after version 2.17.\\nThis will '
       'lock your growth rate at 400% (100% compared to growth in 2.17)."',
       '"Torna alla formula dell\'esperienza nelle abilita\' di prima della '
       '2.17.\\nBlocca la crescita al 400% (cioe\' il 100% di quella della 2.17)."')], 1, ""),
    (959, 'descrizione',
     [('"Reverts the 400% increase in EXP if (skill level < deepest level), in 2.31."',
       '"Toglie il +400% quando l\'abilita\' e\' sotto la profondita\' massima (2.31)."')], 1,
     "«deepest level» e' la «profondita' massima» del diario (command.hsp:17669 «Prof. "
     "max : »). "),
    (967, 'descrizione',
     [('"Disables the Curtain Call mechanic.\\nThis is an anti-AFK mechanism intended to '
       'prevent farming. It spawns instant-kill\\nenemies if you attack 10,000 times '
       'within the same map without leaving."',
       '"Spegne la Chiamata alla ribalta.\\nE\' una difesa contro chi lascia il gioco a '
       'macinare da solo: fa comparire\\nnemici che uccidono all\'istante dopo 10.000 '
       'colpi sulla stessa mappa."')], 1,
     "⚠️ «anti-AFK» e «farming» sono gergo inglese: l'italiano dice la cosa — «chi "
     "lascia il gioco a macinare da solo». ⚠️ «10,000» diventa «10.000»: il separatore "
     "delle migliaia italiano e' il punto. "),
    (970, 'descrizione',
     [('"Enables Custom-G\'s changes to certain skills.\\nThis affects Gravity Sphere, '
       'Graviton Buster, Violent Garden,\\nShadow Step, and some other skills."',
       '"Accende le modifiche di Custom-G a certe abilita\'.\\nRiguarda Sfera di '
       'gravita\', Colpo gravitonico, Giardino violento,\\nPasso d\'ombra e qualche '
       'altra."')], 1,
     "⭐ Quattro nomi di abilita', tutti gia' resi: «Gravity Sphere» -> «Sfera di "
     "gravita'» (skill.hsp:1232), «Graviton Buster» -> «Colpo gravitonico» (:1432), "
     "«Violent Garden» -> «Giardino violento» (:1704, la stessa che la 50a ha messo "
     "nella barra di stato), «Shadow Step» -> «Passo d'ombra» (:932). "),
    (973, 'descrizione',
     [('"Enables Custom-G\'s changes to damage calculation.\\nThis affects the damage '
       'and critical chance when multi-attacking."',
       '"Accende le modifiche di Custom-G al calcolo del danno.\\nRiguarda danno e '
       'probabilita\' di critico negli attacchi multipli."')], 1, ""),
    (976, 'descrizione',
     [('"Disables the sleep prevention effects caused by coffee and tobacco.\\nThey '
       'reduce your drowsiness directly as in Version 1.86."',
       '"Spegne l\'effetto antisonno di caffe\' e tabacco.\\nTornano a togliere '
       'sonnolenza diretta, come nella 1.86."')], 1,
     "«tobacco» -> «tabacco» (db_item.hsp:137880), «coffee» -> «caffe'». "),
    (979, 'descrizione',
     [('"Removes the chance to automatically take a nap when traveling while sleepy."',
       '"Toglie la possibilita\' di appisolarsi da soli viaggiando con sonno."')], 1, ""),
    (982, 'descrizione',
     [('"Visiting the Deep-Sea Castle only resets items with a cooldown period\\nwhile '
       'you\'re there, instead of continuously resetting them until you sleep."',
       '"Al Castello del Drago a Nove Teste gli oggetti a tempo si azzerano\\nsolo '
       'mentre sei li\', e non di continuo finche\' non dormi."')], 1, ""),
    (985, 'descrizione',
     [('"Allow you to turn in quests using pets with child-bit-flag.\\nNamely: Town '
       'Childs / Stray Cats / Little Sisters"',
       '"Permette di consegnare gli incarichi con gli alleati bambini.\\nCioe\': bambini '
       'di citta\', gatti randagi e <Little Sister>."')], 1,
     "⭐ I tre hanno gia' un nome: «town child» -> «il bambino di citta'» "
     "(db_creature.hsp:104004), «stray cat» -> «il gatto randagio» (action.hsp:16971), e "
     "**«<Little Sister>» NON si traduce** (db_creature.hsp:124417, chara_func.hsp:7430 "
     "«<Little Sister> salvate: N, uccise: N»): e' una citazione di BioShock e il "
     "progetto la lascia in inglese come fa col <Big Daddy>. "),
    (988, 'descrizione',
     [('"Disable the inventory limit of Abnormal Mode\\nThis includes: 20 inv limit, 4 '
       '4-dim mirror limit."',
       '"Toglie il limite d\'inventario della modalita\' Abnormal.\\nCioe\': 20 oggetti '
       'e 4 specchi quadridimensionali."')], 1,
     "«4-Dimensional mirror» -> «specchio quadridimensionale» (db_item.hsp:138600). "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')


def _letterale(pezzo: str) -> str:
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

    if tipo == 'descrizione':
        pezzi = _letterale(sostituzioni[0][1]).split('\n')
        for pezzo in pezzi:
            if len(pezzo) > TETTO_DESCRIZIONE:
                raise SystemExit(
                    f'{NOME}:{riga}: {len(pezzo)} caratteri, tetto {TETTO_DESCRIZIONE} '
                    f'— {pezzo!r}')
        largo = max(len(p) for p in pezzi)
    else:
        suffisso = SUFFISSI.get(riga, SUFFISSO_NORMALE)
        largo = sum(len(_letterale(m)) for _, m in sostituzioni) + len(suffisso)
        # ⚠️ la regola e' «non peggiorare l'inglese»: vedi il lotto dei ritocchi extra
        largo_en = sum(len(_letterale(c)) for c, _ in sostituzioni) + len(suffisso)
        tetto = max(TETTO_VOCE, largo_en)
        if largo > tetto:
            raise SystemExit(
                f"{NOME}:{riga}: la voce col suffisso e' larga {largo}, "
                f"tetto {tetto} (l'inglese e' {largo_en})")
        if largo > TETTO_VOCE:
            print(f"⚠️ {NOME}:{riga}: {largo} caratteri, oltre i {TETTO_VOCE} del metro "
                  f"prudente — ma l'inglese ne fa {largo_en}: non peggiora.")

    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + MENU_GIOCO + CLASSE
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
        print(f"  :{t['_riga']}  ({t['_largo']})  {t['sostituisci'].strip()[:100]}")
