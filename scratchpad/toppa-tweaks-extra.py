# -*- coding: utf-8 -*-
"""Il menu dei ritocchi extra al gioco (`*GameplayExtraTweakMenu_loop`, :1274-:1476).

Quattordici voci e quattordici descrizioni: **28 righe**. Titolo, riga di testa
e voce di ritorno erano gia' chiusi dalle toppe `tutte` del menu principale.

## ⚠️ Tre voci hanno un letterale ANCHE DOPO il suffisso di stato

`:1283` e `:1284` mettono la percentuale a cavallo del suffisso —
`"…Nefias:" + GetTStatus(…) + "% increase."` — e a schermo diventa «Piu' mostri
nelle Nefie casuali: (Ora: 30)% in piu'.». Sono due letterali sulla stessa riga
come nel menu di difficolta', ma stavolta il secondo sta **in coda**, non dentro
la cornice: se si traducesse solo il primo resterebbe un «% increase» inglese
attaccato a una frase italiana.

`:1288` invece ha il suffisso a piu' valori (`" (Ora: ovunque)"`, `" (Ora: solo
il giocatore)"`…), che la 50a ha gia' tradotto a :434-:454: qui basta la voce.

## Il vocabolario, tutto verificato nel dizionario

    Pet Arena        -> arena delle bestie   db_creature.hsp:118259, map.hsp:5478
    Random Nefia     -> Nefia casuale        custom_tweaks.hsp:434 (50a)
    Custom NPC/CNPC  -> PNG personalizzato   («PNG» da custom_tweaks.hsp:133)
    summoning crystal -> cristallo di evocazione   db_item.hsp:142315
    socks            -> calzini              db_item.hsp:134939
    craft repair kit -> kit di riparazione di pregio   db_item.hsp:137649
    material kit     -> kit di materiali     db_item.hsp:144134
    moon gate        -> cancello lunare      db_item.hsp:144121
    Show House       -> Cupola delle Case    text.hsp:2848
    music ticket     -> biglietto per il concerto   db_item.hsp:142700
    pot for fusion   -> vaso della fusione   db_item.hsp:141737
    artifact         -> artefatto            proc.hsp:15167, skill.hsp:475
    Blacksmith       -> Armeria              text.hsp:1618
    ore              -> minerale             text.hsp:9668
    deck             -> mazzo di carte       db_item.hsp:143069
    boss             -> capo                 db_creature.hsp:96717, init.hsp:361
    enchantment      -> incantamento         action.hsp:7716
    PP               -> platino              text.hsp:194, item_data.hsp:1387

⭐ **L'incarico di Urcaguary era gia' tradotto nella sua versione alternativa.**
`text.hsp:11220` dice gia' «<Urcaguary>, a Ol-dran, mi ha chiesto di procurarle
30 kit di riparazione»: e' esattamente il ritocco di `:1289`, e la voce di menu
usa le stesse parole. ⚠️ E Urcaguary e' **femmina** («procurarle»,
«<Urcaguary> la gemma tenace»).

⭐ **«Party Quest» e' l'incarico della festa**, quello in cui si suona:
`map.hsp:12215` dice gia' «Devi scaldare la festa entro N minuti», e i biglietti
che vola­no sono i «biglietti per il concerto» (`db_item.hsp:142700`).

## ⚠️⚠️ Una seconda incoerenza trovata per strada: Tenebre / Ombre

Il gioco delle carte mortale ha **due nomi italiani** gia' in dizionario:
- `command.hsp:6166` «Play TCG (Lethal)!» -> «**Gioco delle Tenebre**!»
- `chara_func.hsp:7004` «lost a card game against …» -> «perse il **Gioco delle
  Ombre** contro …»

E' la stessa partita: la prima e' la voce con cui la si comincia, la seconda e'
la causa di morte che finisce nel necrologio. ✅ Qui si e' scelto «Gioco delle
Tenebre», perche' e' il nome che il giocatore legge **prima**, nel menu, e
perche' questa riga di menu sta accanto a quella. ⚠️ Ma l'incoerenza resta, ed
e' la seconda della giornata dopo fattura/bolletta.

## La larghezza

Voci a `wx + 64` (576 px, **74** caratteri col metro prudente, suffisso di stato
compreso), descrizioni a `wx + 38` (602 px, **78** per riga).
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

TETTO_VOCE = 74
TETTO_DESCRIZIONE = 78

# ⚠️ Il suffisso di stato NON e' uguale per tutte le voci: `GetTStatus`
#    (:417-:500) ha un ramo dedicato per certi ritocchi e per tutti gli altri
#    cade sul generico « (Ora: acceso)». Qui si scrive il ramo PIU' LUNGO che
#    ogni voce puo' davvero prendere — misurarle tutte col peggiore in assoluto
#    avrebbe bocciato voci larghe la meta'.
SUFFISSO_NORMALE = ' (Ora: acceso)'
SUFFISSI = {
    1283: ' (Ora: 100)',                       # percentuale, ramo :498
    1284: ' (Ora: 100)',                       # percentuale, ramo :498
    1288: ' (Ora: Nefie casuali risvegliate)',  # ramo GAMEPLAY 77, :434
    1293: ' (Ora: tutte le armi indossate)',    # ramo SPELL_PROCS, :488
}

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_EXTRA = (
    "Sta nel menu dei ritocchi extra al gioco (`*GameplayExtraTweakMenu_loop`), uno dei "
    "sette menu di dettaglio del pannello dei ritocchi di Custom-GX — la categoria di "
    "quelli che aggiungono roba nuova invece di riportare indietro (custom_tweaks.hsp:108). "
    "«PNG» per «NPC» e «Nefie casuali» sono le rese gia' fissate nella 50a (:133, :434). "
    "La finestra e' 640: le voci hanno 74 caratteri col metro prudente, suffisso di "
    "stato compreso, e le descrizioni 78 per riga. "
)

# (riga, tipo, [(cerca, metti), …], occorrenze_attese, motivo)
#   tipo 'voce'  -> il primo letterale e' la voce; gli altri le stanno in coda
VOCI = [
    # ── le quattordici voci ─────────────────────────────────────────────────
    (1281, 'voce', [('"Increased daily Pet Arena attempts. "',
                     '"Piu\' incontri al giorno nell\'arena delle bestie. "')], 1,
     "⭐ «Pet Arena» e' «l'arena delle bestie» (db_creature.hsp:118259 «l'organizzatore "
     "dell'arena delle bestie», map.hsp:5478): non si inventa un nome nuovo per un posto "
     "che ce l'ha. Lo spazio in coda c'e' anche nell'inglese e resta. "),
    (1282, 'voce', [('"Increased variety of hireable home servants."',
                     '"Piu\' varieta\' di domestici da assumere."')], 1,
     "«home servant» e' chi si assume per farlo lavorare a casa propria: «domestico». "),
    (1283, 'voce', [('"Increase mob density in Random Nefias:"', '"Piu\' mostri nelle Nefie casuali:"'),
                    ('"% increase."', '"% in piu\'."')], 1,
     "⚠️⚠️ **Due letterali sulla stessa riga, e il secondo sta in CODA al suffisso di "
     "stato**: a schermo esce «Piu' mostri nelle Nefie casuali: (Ora: 30)% in piu'.». "
     "Tradotto solo il primo, sarebbe rimasto un «% increase» inglese attaccato a una "
     "frase italiana. ⭐ «Nefia» e' il nome proprio del dizionario (db_item.hsp:138961), "
     "al plurale italiano «Nefie», come gia' a :434. "),
    (1284, 'voce', [('"Use CGX Map Layouts in Random Nefia."', '"Usa le mappe CGX nelle Nefie casuali."'),
                    ('"% Chance."', '"% di probabilita\'."')], 1,
     "⚠️ Stesso caso di :1283: il secondo letterale sta in coda al suffisso. "),
    (1285, 'voce', [('"Use CGX Job Quests."', '"Usa gli incarichi CGX."')], 1,
     "«quest» -> «incarico» in tutto il progetto. «Job quest» sono gli incarichi comuni "
     "delle citta' — consegne, sterminii, raccolti, feste — che la descrizione di :1331 "
     "elenca uno per uno. "),
    (1286, 'voce', [('"Disable Random Custom NPC spawns."', '"Niente PNG personalizzati a caso."')], 1,
     "«Custom NPC» (CNPC) e' il personaggio che il giocatore si scrive da se': «PNG "
     "personalizzato». «PNG» e' la resa gia' in uso per NPC (custom_tweaks.hsp:133). "),
    (1287, 'voce', [('"Use summoning crystals to summon Custom NPCs."',
                     '"Evoca i PNG personalizzati coi cristalli di evocazione."')], 1,
     "⭐ «summoning crystal» e' il «cristallo di evocazione» (db_item.hsp:142315): e' un "
     "oggetto vero e va chiamato col suo nome. "),
    (1288, 'voce', [('"Spawn evolved enemies in: "', '"Nemici evoluti in: "')], 1,
     "⚠️ Il suffisso di stato di questa voce e' quello a piu' valori (« (Ora: ovunque)», "
     "« (Ora: solo il giocatore)»…), gia' tradotto dalla 50a a :434-:454: qui basta la "
     "voce. Lo spazio in coda c'e' anche nell'inglese e resta — con quello del suffisso "
     "fa due spazi, esattamente come in inglese. "),
    (1289, 'voce', [('"Collect kits instead of socks in Urcaguary quest."',
                     '"Raccogli kit invece di calzini per Urcaguary."')], 1,
     "⭐ **Questo incarico era gia' tradotto nella sua versione alternativa**: "
     "text.hsp:11220 dice «<Urcaguary>, a Ol-dran, mi ha chiesto di procurarle 30 kit di "
     "riparazione», che e' proprio quel che questo ritocco accende. «socks» -> «calzini» "
     "(db_item.hsp:134939). ⚠️ Urcaguary e' femmina («procurarle», text.hsp:11199 "
     "«<Urcaguary> la gemma tenace»). "),
    (1290, 'voce', [('"Enable loot in Moongate/Rune maps."',
                     '"Bottino nelle mappe da cancello lunare e rune."')], 1,
     "«moon gate» -> «cancello lunare» (db_item.hsp:144121). ⚠️ La barra dell'inglese e' "
     "una congiunzione, non una scelta: l'italiano scrive «e». "),
    (1291, 'voce', [('"Enable Noa\'s unused gathering text adventure."',
                     '"Attiva l\'avventura testuale di Noa, mai usata."')], 1,
     "Noa e' l'autore di Elona e il nome resta. ⚠️ «unused» va spostato in fondo perche' "
     "in italiano davanti al nome («la mai usata avventura di Noa») non si dice. "),
    (1292, 'voce', [('"Allow playing Termination Card Game (TCG) against anyone."',
                     '"Permetti il Gioco delle Tenebre (TCG) contro chiunque."')], 1,
     "⚠️⚠️ **Il gioco di carte mortale ha DUE nomi italiani gia' in dizionario**: "
     "command.hsp:6166 «Play TCG (Lethal)!» -> «Gioco delle Tenebre!» e chara_func.hsp:7004 "
     "«lost a card game against …» -> «perse il Gioco delle Ombre contro …», che e' la "
     "causa di morte nel necrologio. E' la stessa partita. ✅ Qui si usa «Gioco delle "
     "Tenebre» perche' e' il nome che il giocatore legge PRIMA, nel menu, e perche' "
     "questa riga di menu sta accanto a quella. ⚠️ Ma l'incoerenza resta da sciogliere. "),
    (1293, 'voce', [('"Allow spells to activate weapon enchantment."',
                     '"Le magie attivano l\'incantamento dell\'arma."')], 1,
     "«enchantment» -> «incantamento» (action.hsp:7716), la stessa resa usata a :252 "
     "nella 50a, e al singolare come l'inglese. ⚠️ **E' la voce piu' stretta del menu**: "
     "il suo suffisso di stato non e' il generico « (Ora: acceso)» ma quello a piu' "
     "valori di `TWEAK_GAMEPLAY_SPELL_PROCS`, che arriva a « (Ora: tutte le armi "
     "indossate)» — 31 caratteri. Con l'inglese la riga fa gia' 75 caratteri sui 74 del "
     "metro prudente: qui la resa e' stata accorciata fino a 74, cioe' **meno** "
     "dell'inglese. "),
    (1294, 'voce', [('"Allow (weaker) artifact fusion at blacksmiths."',
                     '"Fusione di artefatti (piu\' debole) in armeria."')], 1,
     "«artifact» -> «artefatto» (proc.hsp:15167 «Che nome vuoi dare a questo "
     "artefatto?»), «Blacksmith» -> «Armeria» (text.hsp:1618), che e' il nome del negozio "
     "sulla mappa. "),

    # ── le quattordici descrizioni ──────────────────────────────────────────
    (1319, 'descrizione',
     [('"Increases the daily limit of Pet Arena match attempts\\nin intervals of 10 and '
       'maxing out at 100 a day."',
       '"Alza il limite giornaliero di incontri nell\'arena delle bestie,\\na passi di 10 '
       'e fino a un massimo di 100 al giorno."')], 1, ""),
    (1322, 'descrizione',
     [('"Adds more hireable home servants.\\nIncludes the baker, fisher, and food '
       'vendor.\\nAlso increases the number of servants generated."',
       '"Aggiunge altri domestici da assumere.\\nFra cui il panettiere, il pescivendolo e '
       'il droghiere.\\nE aumenta anche quanti se ne generano."')], 1,
     "⚠️ In dizionario i tre mestieri compaiono col negozio attaccato («della "
     "panetteria», text.hsp:436; «del negozio di pesca», :452; «della drogheria», :460), "
     "perche' li' sono nomi composti con quello del personaggio. In un elenco secco "
     "servono le persone: «il panettiere, il pescivendolo e il droghiere». "),
    (1325, 'descrizione',
     [('"Increase density in random Nefia, result may vary due to mob-room/pack.\\n  '
       'Default population of low density dungeon (rdtype1): 5~60 average: 23\\n  '
       'Default population of high density dungeon (rdtype5): 25~110 average: 59\\nThis '
       'also enforces a 1/64 mob density, +10~30 from mob-room/pack."',
       '"Piu\' mostri nelle Nefie casuali; stanze e branchi possono variare il '
       'conto.\\n  Sotterraneo poco popolato (rdtype1): da 5 a 60, in media 23\\n  '
       'Sotterraneo molto popolato (rdtype5): da 25 a 110, in media 59\\nImpone anche 1 '
       'mostro ogni 64 caselle, +10~30 da stanze e branchi."')], 1,
     "⚠️ I rientri di due spazi e i codici `rdtype1`/`rdtype5` sono dell'inglese e "
     "restano: sono nomi interni che chi legge questa riga sta cercando. «casella» e' la "
     "parola fissata nel menu dei ritocchi vari (:1694). "),
    (1328, 'descrizione',
     [('"Uses Custom Map Layouts in Nefia. \\nThis replaces the existing mapgen '
       'algorithm with the given percentage chance. \\nLayouts with no clear path to '
       'exit may be generated, you might need to dig walls. \\nMob density is 1 mob '
       'every 64 tile, +10~20 per monster-room/packs"',
       '"Usa le mappe di Custom-GX nelle Nefie.\\nSostituisce l\'algoritmo che genera le '
       'mappe, con la probabilita\' data.\\nPuo\' uscire una mappa senza via d\'uscita: '
       'potrebbe servire scavare i muri.\\nLa densita\' e\' 1 mostro ogni 64 caselle, '
       '+10~20 per stanze e branchi."')], 1, ""),
    (1331, 'descrizione',
     [('"Delivery quests now marks the item and makes it heavier, but rewards more '
       'PP.\\nEliminate quests now spawn targets in a group, civilians will also be '
       'spawned.\\nHarvest quests now reward seeds based on your performance '
       'instead.\\nPeople throw more music tickets at you during Party Quest."',
       '"Le consegne segnano l\'oggetto e lo appesantiscono, ma danno piu\' '
       'platino.\\nGli sterminii fanno comparire i bersagli in gruppo, e anche dei '
       'civili.\\nI raccolti premiano con semi in base a come sei andato.\\nAlle feste '
       'ti tirano piu\' biglietti per il concerto."')], 1,
     "⭐ I quattro tipi di incarico hanno gia' un nome italiano nel gioco: le consegne "
     "(map.hsp:12223 «la cassa delle consegne»), gli sterminii (text.hsp:10713 "
     "«sterminare l'esercito juere»), i raccolti (map.hsp:12223 «raccogliere prodotti "
     "agricoli») e le feste (map.hsp:12215 «Devi scaldare la festa entro N minuti»). "
     "⭐ «PP» sono le monete di platino, che il progetto chiama «platino» "
     "(text.hsp:194, command.hsp:17669 «Platino   : »), e i «music ticket» sono i "
     "«biglietti per il concerto» (db_item.hsp:142700). "),
    (1334, 'descrizione',
     [('"This will disable Random CNPC spawn in all areas except Derphy and Melkawn."',
       '"Niente PNG personalizzati a caso, tranne che a Derphy e Melkawn."')], 1,
     "Derphy e Melkawn restano (text.hsp:747, :1128). "),
    (1337, 'descrizione',
     [('"Play as a summoner. Summon CNPCS and monsters to help you in battle. \\nYou can '
       'summon allied CNPCS in dungeons using god\'s favor, or at Home using PP. \\nThis '
       'will also change player summoned monsters in dungeons to be allied."',
       '"Gioca da evocatore: chiami PNG personalizzati e mostri a darti man '
       'forte.\\nNei sotterranei ti costano il favore degli dei, a casa il '
       'platino.\\nE i mostri che evochi nei sotterranei diventano alleati."')], 1,
     "⚠️ L'inglese e' spezzato in due frasi («Play as a summoner. Summon CNPCS…») e "
     "l'italiano le lega coi due punti, perche' la seconda spiega la prima. "),
    (1340, 'descrizione',
     [('"Spawn evolved enemies at given locations. \\nChance start at 1/1800 chance, '
       'caps at area lvl 301 with 1/6 chance.\\nEvolution branches chance stack. '
       '\\nEvolution stages are calculated independently."',
       '"Fa comparire nemici evoluti nei posti scelti.\\nSi parte da 1 su 1800 e si '
       'arriva a 1 su 6 al livello d\'area 301.\\nLe probabilita\' dei rami di '
       'evoluzione si sommano.\\nGli stadi di evoluzione si calcolano uno per uno."')], 1,
     "«evolution» -> «evoluzione» (db_item.hsp:142914, action.hsp:18632 «la tua creatura "
     "si e' evoluta»), che e' anche il tema di tutto `custom_enemyevolution.hsp`. "),
    (1343, 'descrizione',
     [('"Urcaguary now accept craft repair kits and material kits instead of '
       'socks.\\nCraft repair kit count as 1 and material kit count as 2.\\nYou still '
       'need to find the sock-thief for the first time.\\nBut he will drop enough socks '
       'for you complete the quest."',
       '"Urcaguary accetta kit di riparazione e kit di materiali, non calzini.\\nUn kit '
       'di riparazione vale 1, un kit di materiali vale 2.\\nLa prima volta devi ancora '
       'trovare il ladro di calzini,\\nma lascera\' calzini a sufficienza per chiudere '
       'l\'incarico."')], 1,
     "⭐ «craft repair kit» -> «kit di riparazione di pregio» (db_item.hsp:137649) e "
     "«material kit» -> «kit di materiali» (db_item.hsp:144134). ⚠️ Qui si dice solo "
     "«kit di riparazione», senza «di pregio», perche' la riga li conta e il nome intero "
     "la farebbe sfondare — ed e' comunque il nome che text.hsp:11220 usa nel diario "
     "dell'incarico. "),
    (1346, 'descrizione',
     [('"Custom maps entered via Moongate/Runes now contains loot.\\nEnemies drop gold '
       'and ores depend on their level.\\nContainers can be opened.\\nThis won\'t enable '
       'if you enter the Custom Map using Show House."',
       '"Le mappe raggiunte da cancello lunare o rune hanno del bottino.\\nI nemici '
       'lasciano oro e minerali secondo il loro livello.\\nI contenitori si possono '
       'aprire.\\nNon vale se entri nella mappa dalla Cupola delle Case."')], 1,
     "⭐ «Show House» e' «la Cupola delle Case» (text.hsp:2848), un posto sulla mappa del "
     "mondo. «ore» -> «minerale» (text.hsp:9668). "),
    (1349, 'descrizione',
     [('"Enable the unused text adventure made by Noa. \\nThis affects the material-spot '
       'gathering mechanics. \\nMaterial/EXP gain is increased compare to Vanilla. '
       '\\nBut lowered compared to Plus (If your skill is insufficient.)"',
       '"Attiva l\'avventura testuale di Noa, rimasta inutilizzata.\\nCambia il modo in '
       'cui si raccolgono i materiali.\\nMateriali ed esperienza resi sono di piu\' che '
       'nell\'originale,\\nma meno che in Plus, se l\'abilita\' non basta."')], 1,
     "«Vanilla» -> «l'originale» (init.hsp:2873), «Plus» resta perche' e' il nome della "
     "versione. La raccolta ai giacimenti il gioco la chiama gia' cosi' "
     "(action.hsp:2890 «Qui puoi cercare materiali», command.hsp:6155 «Raccogli i "
     "materiali»). "),
    (1352, 'descrizione',
     [('"Enable a lethal round of TCG against any NPC.\\nThe winner gets a card of '
       'loser. And the loser DIES.\\nBoss decks are still WIP."',
       '"Permette una partita mortale a TCG contro qualunque PNG.\\nChi vince prende una '
       'carta di chi perde. E chi perde MUORE.\\nI mazzi dei capi sono ancora in '
       'lavorazione."')], 1,
     "«deck» -> «mazzo di carte» (db_item.hsp:143069), «boss» -> «capo» "
     "(db_creature.hsp:96717 «il capo dei pirati», :115450 «il capo della banda»). "
     "⚠️ Il maiuscolo di «DIES» resta: e' l'inglese che alza la voce, non un caso. "),
    (1355, 'descrizione',
     [('"Allow spells to activate weapon enchantments.\\nHighly unbalanced, as spells '
       'are balanced towards not having procs."',
       '"Le magie possono attivare gli incantamenti dell\'arma.\\nSbilanciatissimo: le '
       'magie sono calibrate per non farlo."')], 1,
     "«proc» e' il gergo per «l'incantamento scatta»: l'italiano non ha la parola e dice "
     "la cosa («per non farlo»), che e' quel che serve a capire perche' e' sbilanciato. "),
    (1358, 'descrizione',
     [('"Allows a weaker version artifact fusion at blacksmiths without Irma.\\n  '
       'Blacksmiths only accepts pot of fusion items.\\nAnd also allows strengthening '
       'and removal of enchantments.\\n  For those who don\'t want to savescum hours for '
       'a perfect blank slate item."',
       '"Permette una fusione di artefatti piu\' debole in armeria, senza Irma.\\n  '
       'L\'armeria accetta solo gli oggetti del vaso della fusione.\\nE permette anche '
       'di rafforzare e togliere gli incantamenti.\\n  Per chi non vuole ricaricare per '
       'ore in cerca dell\'oggetto perfetto."')], 1,
     "⭐ «pot for fusion» e' il «vaso della fusione» (db_item.hsp:141737), Irma resta "
     "(db_creature.hsp:74027 «<Irma> la forgiatrice straniera»). «savescum» e' gergo "
     "senza equivalente: «ricaricare per ore» dice la stessa cosa in italiano corrente. "
     "⚠️ I rientri di due spazi sono dell'inglese e restano. "),
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

    if tipo == 'descrizione':
        pezzi = _letterale(sostituzioni[0][1]).split('\n')
        for pezzo in pezzi:
            if len(pezzo) > TETTO_DESCRIZIONE:
                raise SystemExit(
                    f'{NOME}:{riga}: {len(pezzo)} caratteri, tetto {TETTO_DESCRIZIONE} '
                    f'— {pezzo!r}')
        largo = max(len(p) for p in pezzi)
    else:
        # la voce e' il primo letterale, il suffisso di stato, poi la coda
        suffisso = SUFFISSI.get(riga, SUFFISSO_NORMALE)
        largo = sum(len(_letterale(m)) for _, m in sostituzioni) + len(suffisso)
        # ⚠️ La regola non e' «stare sotto il tetto», e' **non peggiorare
        #    l'inglese**: se la riga inglese sfondava gia' di suo (misurato
        #    col suffisso italiano, che e' comune alle due), l'italiano puo'
        #    arrivare fin li' e non oltre. Vedi la 50a, screen.hsp:1811.
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
    toppa['motivo'] = motivo + MENU_EXTRA + CLASSE
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
