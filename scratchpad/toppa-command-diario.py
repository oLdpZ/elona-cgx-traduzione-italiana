# -*- coding: utf-8 -*-
"""Il diario (`j`): 54 righe inglesi nude in una schermata sola.

`command.hsp:*com_journal` e' la seconda routine del quinto punto cieco per
numero di righe (53 di testo secondo `triage_nudi.py`, piu' due che il triage non
contava — vedi sotto). Le intestazioni erano gia' toppate da sessioni passate
(«- Notizie -», «- Missioni -», «- Entrate e uscite -»): qui si chiude tutto il
resto, cioe' il conto delle bollette e le quaranta voci della «Cronaca delle
avventure».

## Il giapponese e' l'originale, e due volte l'inglese ha sbagliato

⭐⭐ **`Bandits Killed` non conta i banditi, conta le bande.** Il giapponese dice
潰した盗賊団**の数** («numero di bande di ladri sgominate») e il sito di
assegnazione gli da' ragione: `GDATA_FLAG_BANDITS_KILLED` cresce di uno per
**scontro** — `action.hsp:2514` quando travolgi dei predoni con la nave,
`quest.hsp:718` quando respingi un incarico dei ladri — non per nemico ucciso.
✅ «Bande di banditi sgominate».

⭐⭐ **`Max Arena Streak` non e' una serie.** Il giapponese dice アリーナ**総勝数**
(«totale delle vittorie») e `quest.hsp:675` incrementa il contatore a ogni
vittoria senza azzerarlo mai: non c'e' nessuna serie da interrompere. Il nome
della costante (`HIGHEST_ARENA_STREAK`) e' d'accordo con l'inglese e sbagliato
quanto lui — la solita lezione, **i nomi del decompilatore non sono
un'autorita'**. ✅ «Vittorie in arena» e «Vittorie all'Arena delle Bestie».

💡 Il metodo che le ha trovate e' lo stesso di sempre e costa una ricerca: **si
guarda chi assegna il campo**. Le altre voci dubbie sono state controllate allo
stesso modo — `YOUNGER_SISTERS` cresce in `chara.hsp:2602` quando arriva una
sorellina, `HOUSE_VISITORS` in `chat.hsp:23372` con l'evento visita,
`TIMES_EATEN_IN_SECRET` in `proc.hsp:5804` quando un alleato mangia di nascosto,
`MELGET_HISCORE` in `chat.hsp:13076` col punteggio del quiz — e li' l'inglese era
giusto.

## Le colonne del conto restano allineate

Il riquadro delle bollette allinea i due punti con degli spazi, e l'inglese
riempie l'etichetta fino a sette caratteri (`"Sum    : About "`). L'italiano fa
lo stesso a **nove**, che e' la lunghezza di «Personale»:

    @BL  Totale   : circa <n> oro
    @RE  Personale: circa <n> oro
    @RE  Immobili : circa <n> oro
    @RE  Tasse    : circa <n> oro
    @RE  Totale   : circa <n> oro

⚠️ «Immobili» e non «Manutenz.»: il valore e' `calccostbuilding()`, cioe' quel che
costano le proprieta', e una voce di bolletta italiana si chiama cosi'. Sta in
otto caratteri e non porta un punto che si confonda coi due punti della colonna.

## La larghezza: due colonne da 306 px, ~46 caratteri per riga

Il diario e' un libro da 736x448 con due colonne di venti righe
(`command.hsp:3140`, `x = wx + 80 + cnt / 20 * 306`). Il carattere delle righe
`@BL`/`@RE` e' a corpo 10 (`12 + sizefix - en * 2`), cioe' fra 46 e 51 caratteri
per riga secondo i due metri del progetto. La voce italiana piu' lunga e'
«Vittorie all'Arena delle Bestie: » a 33 caratteri piu' il numero: sotto il tetto
con tutt'e due i metri, e l'inglese piu' lungo ne occupava 30.

## Due righe che nessun conteggio contava

⚠️⚠️ **`command.hsp:3095` («Cats/Dogs Killed») e' un DIFETTO di `nudi_en.py`.**
La regola `_PERCORSO` scarta ogni letterale che contenga una barra, perche' una
barra e' il segno di un percorso di file — ma «Cats/Dogs Killed: » e' una frase,
e la barra ci sta in mezzo come congiunzione. La riga e' nuda come le altre e
nessun referto l'ha mai vista. Entra qui, e il filtro va corretto a parte.

💡 **`command.hsp:3186` («(more)») sta in `*com_journal_loop`**, non in
`*com_journal`: e' la stessa schermata ma un'altra routine, quindi nel referto
per routine compare altrove. Tradurla con le sue sorelle e' l'unica cosa
sensata: e' la scritta in fondo alla pagina del libro.

## Quel che resta fuori, e perche'

⚠️⚠️ **`command.hsp:2901` (` Rank.`) non si puo' toppare, ed e' un limite NUOVO
del meccanismo.** La riga compare due volte identiche — nel diario e nella scheda
di `*dump_chara` (`:17848`) — quindi una toppa a riga singola e' ambigua. E il
blocco non salva: le quattro righe sopra e sotto sono identiche nei due siti, e
la prima che li distingue (`:2897`, `noteadd lang("名声: ", "Fame: ")`) porta una
**resa**, che nella build il dizionario ha gia' riscritto. Un blocco che la
raggiunge aggancia il sorgente pinnato — come `test_toppe.py:104` pretende — ma
non aggancia piu' la build, dove le toppe girano davvero.
💡 **La regola che ne esce: una toppa puo' disambiguare solo con righe che il
dizionario non tocca.** Due siti identici separati da righe tradotte sono
irraggiungibili finche' il formato non impara a dire «tutte le occorrenze».

⚠️ **`command.hsp:3067` («Total Platinum») esce di qui apposta**: e' l'unica riga
della schermata che porta un letterale nudo **e** una `lang()` non ancora
tradotta (`lang("枚", " Plat")`). La regola della 46ª vieta toppa e resa sulla
stessa riga: vuole prima un rinvio della firma, e si fa in un passo suo.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'command.hsp'

# La coda comune a ogni motivo: che classe e' e perche' solo una toppa la tocca.
CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca "
    "solo con una toppa. Quinto punto cieco, misurato da `scratchpad/nudi_en.py` "
    "(49a) e classificato da `scratchpad/triage_nudi.py` (50a). La riga e' unica per "
    "giapponese e inglese, quindi la toppa vale per tutt'e due i rami."
)
DIARIO = (
    "Sta nel DIARIO (`command.hsp:*com_journal`, tasto `j`), che il triage della 50a "
    "ha misurato come la seconda routine del punto cieco per numero di righe. Il "
    "libro e' 736x448 con due colonne da 306 px e venti righe (`:3140`), carattere a "
    "corpo 10: fra 46 e 51 caratteri per riga secondo i due metri del progetto. "
)
CONTO = (
    "Nel riquadro delle bollette i due punti sono allineati con degli spazi: "
    "l'inglese riempie l'etichetta fino a sette caratteri, l'italiano fino a NOVE, "
    "che e' la lunghezza di «Personale». Le cinque voci restano incolonnate. "
)

# (riga, [(cerca, metti), ...], motivo specifico)
VOCI = [
    (2851, [('"No news"', '"Nessuna notizia"')],
     "Il testo che il diario mostra al posto delle notizie quando non ce n'e' nessuna."),

    (2934, [('"Salary (Paid every 1st and 15th day)"',
             '"Paga (versata il 1 e il 15 del mese)"')],
     "L'intestazione della paga nel conto del diario. Il giapponese (:2919) dice "
     "「給料(毎月1日と15日に支給)」, cioe' proprio «versata il 1 e il 15 di ogni mese». "
     "⚠️ Niente «1o» con l'ordinale: CP932 non ha il carattere, e il test "
     "`test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere` lo fermerebbe."),
    (2935, [('"@BL  Sum    : About "', '"@BL  Totale   : circa "'), ('" GP"', '" oro"')],
     "Il totale della paga. " + CONTO +
     "⭐ ` GP` -> ` oro` e' la resa di sempre: command.hsp:3677 e text.hsp:193 "
     "(`strgold`) hanno gia' `lang(\" gold\", \" oro\")`, e il ramo giapponese di questa "
     "stessa schermata (:2920) usa proprio `strgold`."),
    (2937, [('"Bills  (Issued every 1st day)"', '"Bollette (emesse il 1 del mese)"')],
     "L'intestazione delle bollette. Il giapponese (:2922) dice 「請求書内訳(毎月1日に発行)」."),
    (2938, [('"@RE  Labor  : About "', '"@RE  Personale: circa "'), ('" GP"', '" oro"')],
     "Il costo del personale (`GDATA_COST_HIRE`, quel che costano gli assunti). Il "
     "giapponese dice 「人件費」, spese di personale. " + CONTO),
    (2939, [('"@RE  Maint. : About "', '"@RE  Immobili : circa "'), ('" GP"', '" oro"')],
     "Il costo degli immobili (`calccostbuilding()`). ⚠️ «Immobili» e non "
     "«Manutenz.»: il valore e' quel che costano le proprieta', una voce di bolletta "
     "italiana si chiama cosi', e sta in otto caratteri senza portare un punto che si "
     "confonda coi due punti della colonna. Il giapponese dice 「維持費」. " + CONTO),
    (2940, [('"@RE  Tax    : About "', '"@RE  Tasse    : circa "'), ('" GP"', '" oro"')],
     "Le tasse (`calccosttax()`, giapponese 「税金」). " + CONTO),
    (2941, [('"@RE  Sum    : About "', '"@RE  Totale   : circa "'), ('" GP"', '" oro"')],
     "Il totale delle bollette. " + CONTO),
    (2943, [('"Prepaid Balance "', '"Anticipo residuo "'), ('" GP"', '" oro"')],
     "Il residuo di quel che si e' pagato in anticipo. Il giapponese (:2928) dice "
     "「現在先払いの残額は」, «l'anticipo che resta adesso e' di»."),
    (2946, [('"You have "', '"Hai "'), ('" unpaid bills."', '" bollette da pagare."')],
     "Le bollette non pagate. Il giapponese (:2931) dice 「現在未払いの請求書は<n>枚」."),

    (3040, [('"Your stats so far:"', '"Come sei andato finora:"')],
     "L'intestazione della «Cronaca delle avventure». Il giapponese (:2955) dice "
     "「これまでのあなた」, cioe' «tu fino a qui»: e' un bilancio della partita, non un "
     "elenco di statistiche di sistema."),
    (3041, [('"@BL   Deepest Lvl : "', '"@BL   Livello piu\' profondo: "')],
     "Il piano piu' profondo raggiunto (giapponese 「最深攻略階層」). ⚠️ L'inglese ha uno "
     "spazio di troppo prima dei due punti — e' l'unica riga dell'elenco che ce l'ha, "
     "e l'italiano non lo eredita."),
    (3042, [('Nefia Conquered: "', 'Nefie conquistate: "')],
     "Le Nefia conquistate (giapponese 「ネフィア制覇数」). «Nefia» resta il nome proprio "
     "che il dizionario usa gia' (db_item.hsp:138961 «nucleo di Nefia»), al plurale "
     "italiano «Nefie»."),
    (3043, [('"@BL   Kills: "', '"@BL   Uccisioni: "')],
     "Le uccisioni (giapponese 「殺害数」)."),
    (3044, [('Total Duels Experienced: "', 'Duelli combattuti: "')],
     "I duelli (giapponese 「決闘の経験」)."),
    (3045, [('Jobs Completed: "', 'Incarichi completati: "')],
     "Gli incarichi completati (giapponese 「依頼達成数」). «Incarico» e' il termine che "
     "la bacheca usa gia'."),
    (3047, [('Miles Traveled: "', 'Miglia percorse: "')],
     "La distanza sulla mappa del mondo (giapponese 「世界移動距離」 + 「マイル」)."),
    (3048, [('Items Made (Alchemy): "', 'Oggetti creati (alchimia): "')],
     "Gli oggetti prodotti con l'alchimia (giapponese 「生産数(錬金術)」)."),
    (3049, [('Items Made (Carpenter): "', 'Oggetti creati (falegnameria): "')],
     "Gli oggetti prodotti dal falegname (giapponese 「生産数(大工)」). ⚠️ Il giapponese "
     "nomina il MESTIERE, l'italiano nomina l'arte come nelle altre tre voci: "
     "alchimia, falegnameria, oreficeria, sartoria stanno insieme."),
    (3050, [('Items Made (Jeweler): "', 'Oggetti creati (oreficeria): "')],
     "Gli oggetti prodotti col taglio delle gemme (giapponese 「生産数(宝石細工)」)."),
    (3051, [('Items Made (Tailor): "', 'Oggetti creati (sartoria): "')],
     "Gli oggetti prodotti col cucito (giapponese 「生産数(裁縫)」)."),
    (3053, [('Highest Normal Dmg: "', 'Danno normale massimo: "')],
     "Il danno normale piu' alto inflitto (giapponese 「最大通常ダメージ」)."),
    (3054, [('Walls Mined: "', 'Muri abbattuti: "')],
     "I muri scavati (giapponese 「掘り壊した壁の数」)."),
    (3055, [('Hours Slept: "', 'Ore di sonno: "')],
     "Il sonno totale (giapponese 「総睡眠時間」 + 「時間」)."),
    (3056, [('Elapsed Days: "', 'Giorni trascorsi: "')],
     "I giorni passati (giapponese 「経過日」 + 「日」)."),
    (3057, [('Wishes Made: "', 'Desideri espressi: "')],
     "I desideri (giapponese 「願い発生回数」)."),
    (3061, [('House Visitors: "', 'Visitatori in casa: "')],
     "I visitatori di casa (giapponese 「わが家への訪問客」 + 「人」). Controllato il sito "
     "d'assegnazione: `chat.hsp:23372` incrementa il contatore insieme all'evento "
     "`EVENT_VISITOR`, quindi conta le visite ricevute."),
    (3062, [('Treasure Found: "', 'Tesori dissotterrati: "')],
     "I tesori scavati (giapponese 「宝発掘回数」, dove 発掘 e' proprio lo scavo)."),
    (3063, [('Bandits Killed: "', 'Bande di banditi sgominate: "')],
     "⭐⭐ L'inglese qui SBAGLIA e il giapponese ha ragione: 「潰した盗賊団の数」 conta le "
     "BANDE sgominate, non i banditi uccisi. Il sito d'assegnazione conferma — "
     "`GDATA_FLAG_BANDITS_KILLED` cresce di uno per scontro (`action.hsp:2514`, i "
     "predoni travolti con la nave; `quest.hsp:718`, l'incarico contro i ladri "
     "respinto), non per nemico morto. 💡 Trovato guardando chi assegna il campo, che "
     "e' l'unica prova che vale."),
    (3064, [('Max Arena Streak: "', 'Vittorie in arena: "')],
     "⭐⭐ Anche qui l'inglese sbaglia: non e' una «serie». Il giapponese dice "
     "「アリーナ総勝数」, cioe' il TOTALE delle vittorie, e `quest.hsp:675` incrementa il "
     "contatore a ogni vittoria senza azzerarlo mai — non c'e' nessuna serie da "
     "interrompere. ⚠️ Il nome della costante (`HIGHEST_ARENA_STREAK`) e' d'accordo "
     "con l'inglese ed e' sbagliato quanto lui: i nomi del decompilatore non sono "
     "un'autorita' (lezione n. 2 della 49a)."),
    (3065, [('Max Pet Arena Streak: "', 'Vittorie all\'Arena delle Bestie: "')],
     "Come :3064, per l'arena degli alleati (giapponese 「Ｐアリーナ総勝数」). ⭐ «Arena "
     "delle Bestie» e' il nome che il progetto usa gia': text.hsp:2803 e init.hsp:356. "
     "33 caratteri piu' il numero, sotto il tetto della colonna con tutt'e due i metri."),
    (3068, [('Player Skill Bonus Earned: "', 'Bonus abilita\' ottenuti: "')],
     "I bonus di abilita' ottenuti dal personaggio (giapponese 「PCｽｷﾙﾎﾞｰﾅｽ入手数」)."),
    (3069, [('Total Spell Bonus Earned: "', 'Bonus magia ottenuti: "')],
     "I bonus di magia ottenuti (giapponese 「ｽﾍﾟﾙﾎﾞｰﾅｽ入手数」)."),
    (3071, [('Melget Hiscore: "', 'Record al quiz di Melget: "'), ('" points"', '" punti"')],
     "Il record al quiz. ⚠️ L'inglese dice solo «Melget Hiscore» e il giapponese solo "
     "「クイズ最高記録」 («record del quiz»): l'italiano tiene tutt'e due i pezzi perche' "
     "senza il quiz il nome non dice di che record si tratta. Il sito d'assegnazione "
     "conferma: `chat.hsp:13076` alza `GDATA_FLAG_MELGET_HISCORE` col punteggio del "
     "quiz, e db_creature.hsp:69199 rende «<Melget> l'informatrice»."),
    (3079, [('Bread Eaten: "', 'Pagnotte mangiate: "')],
     "Il pane mangiato (giapponese 「食ったパンの数」)."),
    (3080, [('Panties Eaten: "', 'Mutandine mangiate: "')],
     "Le mutandine mangiate (giapponese 「食ったパンツの数」)."),
    (3081, [('Humans Eaten: "', 'Umani mangiati: "')],
     "Il cannibalismo (giapponese 「人肉食の回数」)."),
    (3082, [('Times Eaten in Secret: "', 'Pasti di nascosto: "')],
     "I bocconi rubati (giapponese 「盗み食いの回数」). Il sito d'assegnazione "
     "(`proc.hsp:5804`) scatta quando un alleato mangia di nascosto un oggetto altrui."),
    (3083, [('Goods Stolen: "', 'Oggetti rubati: "')],
     "La refurtiva (giapponese 「盗んだ品物数」)."),
    (3087, [('Jobs Failed: "', 'Incarichi falliti: "')],
     "Gli incarichi falliti (giapponese 「依頼失敗数」)."),
    (3088, [('Younger Sisters: "', 'Sorelline: "')],
     "Le sorelline (giapponese 「血の繋がらない妹」, «sorelline non di sangue»). Il sito "
     "d'assegnazione e' `chara.hsp:2602`, che scatta sull'ID della sorellina."),
    (3089, [('Times Converted: "', 'Cambi di fede: "')],
     "Le conversioni PROPRIE (giapponese 「改宗した回数」): `god.hsp:580` le incrementa "
     "quando sei tu a cambiare divinita'. ⚠️ Da non confondere con :3100, che conta le "
     "persone convertite da te."),
    (3090, [('Times Married: "', 'Matrimoni: "')],
     "I matrimoni (giapponese 「結婚した回数」)."),
    (3091, [('Prostitution Encounters: "', 'Incontri a pagamento: "')],
     "Il giapponese e' un eufemismo (「気持ちいい事回数」) e l'inglese e' esplicito; "
     "l'italiano sta in mezzo, come fa il resto della traduzione con questa materia."),
    (3093, [('Nuclear Explosions: "', 'Esplosioni nucleari: "')],
     "Le esplosioni nucleari (giapponese 「核爆発の発生回数」)."),
    (3094, [('Ragnaroks Started: "', 'Ragnarok scatenati: "')],
     "I ragnarok (giapponese 「終末の発生回数」). «Ragnarok» resta invariato al plurale, "
     "come db_item.hsp:151775."),
    (3095, [('Cats/Dogs Killed: "', 'Cani e gatti uccisi: "')],
     "⚠️⚠️ Questa riga e' un DIFETTO di `nudi_en.py`, non una voce come le altre: la "
     "regola `_PERCORSO` scarta ogni letterale che contenga una barra perche' una "
     "barra e' il segno di un percorso di file, ma «Cats/Dogs Killed: » e' una frase e "
     "la barra ci sta come congiunzione. Nessun referto l'aveva mai vista. "
     "Il giapponese dice 「犬猫殺害数」, cani e gatti."),
    (3096, [('Gwen Killed: "', 'Morti di Gwen: "')],
     "Le morti di Gwen (giapponese 「グウェン死亡数」). Il nome resta invariato, come in "
     "db_creature.hsp:86024 («<Gwen> la guerriera spietata»). ⚠️ Il giapponese dice "
     "死亡数, «numero di morti», non «uccisa da te»: l'italiano tiene la forma neutra."),
    (3097, [('Lomias Killed: "', 'Morti di Lomias: "')],
     "Come :3096 (giapponese 「ロミアス死亡数」). «Lomias» invariato, db_creature.hsp:100005."),
    (3099, [('Trees Felled: "', 'Alberi abbattuti: "')],
     "Gli alberi tagliati (giapponese 「伐採した樹木」 + 「本」)."),
    (3100, [('People Converted: "', 'Persone convertite: "')],
     "Le persone convertite DA TE (giapponese 「改宗させた人数」, col causativo させた). "
     "⚠️ Il paio con :3089, che conta invece i tuoi cambi di fede."),
    (3101, [('Alcohol Consumed: "', 'Alcol bevuto: "')],
     "L'alcol bevuto (giapponese 「飲んだお酒」). ⚠️ Il giapponese aggiunge il "
     "contatore 「本」 (bottiglie) e l'inglese no: «Alcol bevuto» non si sbilancia "
     "sull'unita', che sarebbe una supposizione."),
    (3102, [('Smoking Frequency: "', 'Sigarette fumate: "')],
     "Le fumate (giapponese 「喫煙回数」)."),

    (3186, [('"(more)"', '"(segue)"')],
     "La scritta in fondo alla pagina del libro quando ce n'e' un'altra. "
     "💡 Sta in `*com_journal_loop` e non in `*com_journal`, quindi nel referto per "
     "routine compare staccata dalle sue sorelle: e' la stessa schermata."),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')

nuove = []
for riga, sostituzioni, motivo in VOCI:
    originale = sorg[riga - 1]
    # ⚠️ La toppa aggancia il SORGENTE pinnato (test_toppe.py:104) ma gira sulla
    #    BUILD: se il dizionario ha gia' riscritto la riga, la catena si spezza.
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != 1:
            raise SystemExit(f'{NOME}:{riga} compare {quante} volte nel {eti}: toppa ambigua')

    nuova = originale
    for cerca, metti in sostituzioni:
        if nuova.count(cerca) != 1:
            raise SystemExit(f'{NOME}:{riga}: `{cerca}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    # ⚠️ CP932 non sa scrivere le lettere accentate: nelle toppe l'apostrofo si
    #    scrive a mano, perche' `accenti.py` non passa di qui.
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    nuove.append({'file': NOME, 'cerca': originale, 'sostituisci': nuova,
                  'motivo': motivo + ' ' + DIARIO + CLASSE, '_riga': riga})

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
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)})')
    for t in da_scrivere:
        print(f"  :{t['_riga']}")
        print(f"    - {t['cerca'].strip()[:110]}")
        print(f"    + {t['sostituisci'].strip()[:110]}")
