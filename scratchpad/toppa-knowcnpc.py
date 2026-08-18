# -*- coding: utf-8 -*-
"""La scheda dell'avventuriero conosciuto: ottanta righe, una finestra intera.

`command.hsp:8001`-`:8215`, `*com_knowCNPC` — la sfera di cristallo che mostra
un avventuriero gia' incontrato, col suo livello, la razza, il rango, i
passatempi, le azioni dell'IA, le resistenze e i tratti.

⭐⭐⭐ **Nessun conteggio del progetto la nominava.** Le ottanta righe si
scrivono `buff += "..."`, cioe' la forma **a pezzi** dell'undicesimo punto cieco
(`scratchpad/buff_en.py`, 59a): niente `lang()`, niente firma, niente voce di
dizionario. `nudi_en.py` non le vede perche' guarda i letterali che *disegnano*
e questi stanno in un'assegnazione; `variabili_en.py` non le vede perche' guarda
le variabili *interpolate in una `lang()`* e `buff` non ci finisce mai.
Il referto che le ha trovate le ha viste solo alla **seconda** correzione, e
`:8073` solo alla terza.

## La geometria, e il passo del carattere che oggi ha una quarta conferma

    command.hsp:8016   ww = 380                  la finestra
    command.hsp:8186   gmesx = wx + 40           dove comincia la riga
    module.hsp:5014    gmesx += size / 2         quanto avanza per carattere

Il bordo interno destro sta a `wx + 380 - 12`, come in ogni finestra di questo
gioco. Restano **328 px**, e `gmes` avanza `size / 2` px per carattere
single-byte: con `size = 14` fa **7**, che e' il numero corretto oggi
(`strumenti/menu_dialogo.py`). Tetto: **46 caratteri**.
⭐ E' la quarta conferma indipendente dello stesso 7, dopo `module.hsp:70`, la
misura sulla schermata del lupo mannaro e la pendenza delle sei misure del
2026-08-17. Qui pero' e' scritto come **divisione**, non come costante: e' il
motore che dice quanto e' largo un carattere.
⚠️ Dentro `<title1>` la dimensione scende a 12 e il passo a 6: quelle righe
hanno tetto 54.
⚠️⚠️ **E `gmes` NON manda a capo dentro la finestra**: `gmesw` vale 600
(`:8188`), cioe' molto piu' dei 328 utili. Quel che sfora non va a capo e non
viene tagliato — finisce **stampato sopra la mappa**, fuori dalla cornice. Le
rese stanno tutte sotto i 46, e la piu' lunga per costruzione e' `:8175`, dove
il nome della classe e' interpolato.

## ⚠️⚠️ Il genere: qui non si sa, e la riga e' una sola per tutti

Il pannello dice se l'avventuriero e' maschio o femmina (`:8051`-`:8052`), ma
**i letterali sono gli stessi per tutti e due**. Ogni participio o aggettivo in
`-o` sbaglierebbe la meta' delle volte. Le rese usano solo forme invarianti:

    Stealthy.              «Passo felpato.»          e non «Furtivo»
    Blessed by Elements.   «Benedizione degli el.»   e non «Benedetto»
    Made of Metal.         «Corpo di metallo.»       e non «Fatto di metallo»
    Was not made of flesh. «Non aveva carne addosso» e non «Non era fatto»
    VERY ANGRY             «IN COLLERA NERA»         e non «MOLTO ARRABBIATO»
    Fastest X in the West. «Piu' veloce di ogni X»   perche' «veloce» e' in -e

⭐ **E i sei ranghi hanno lo stesso problema in forma peggiore**, perche' stanno
**davanti** al nome della classe: «Legendary Warmage» in italiano vorrebbe
l'aggettivo dopo, e messo davanti concorderebbe con una classe di cui non si
conosce il genere. Le rese li girano in **etichette col due punti** — «Leggenda:
Warmage» — che e' la forma che il resto del pannello usa gia' («Distanza
preferita: », «Passatempo: ») e che in una scheda di dati legge meglio
dell'aggettivo.

## Il vocabolario, preso dove il progetto lo aveva gia' deciso

    Do Nothing        «Non fare nulla»          toppa di custom_ai.hsp, 51a
    Melee Attack      «Attacca (mischia)»       toppa di custom_ai.hsp, 51a
    Ranged Attack     «Attacca (a distanza)»    toppa di custom_ai.hsp, 51a
    You can float.    «Levitazione»             command.hsp:2185
    Splits            «si sdoppia»              toppa del tavolo (tcg «Sdoppia»)
    Bleeding          «sanguinamento»           toppa del tavolo (tcg «Sangue»)

⚠️ **`Roam Around` non c'era**: `custom_ai.hsp` ha «Move (Away)» e «Move
(Forward)», che sono altre due azioni. Qui si fissa **«Gironzola»**.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'command.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO composto con `buff += \"...\"`: non passa da "
    "nessuna `lang()`, quindi non ha firma, non ha voce di dizionario e nessun lotto "
    "puo' raggiungerlo — si tocca solo con una toppa. E' l'UNDICESIMO punto cieco "
    "(`scratchpad/buff_en.py`, 59a), nella sua forma **a pezzi**: quella che il referto "
    "ha visto solo alla seconda correzione, la stessa che `variabili_en.py` aveva "
    "imparato nella 47a. "
)
PANNELLO = (
    "Sta nella scheda dell'avventuriero conosciuto (`*com_knowCNPC`, `command.hsp:8001`), "
    "la finestra della sfera di cristallo. ⚠️ La geometria: finestra 380, testo a "
    "`wx + 40`, bordo interno a `wx + 368` — **328 px**, e `gmes` avanza `size / 2` px "
    "per carattere (`module.hsp:5014`), cioe' 7 col corpo 14. Tetto **46 caratteri**, e "
    "`gmes` non manda a capo prima di 600 px: quel che sfora finisce stampato sopra la "
    "mappa. ⚠️ Il genere dell'avventuriero e' noto al gioco ma non alla riga, che e' una "
    "sola per maschi e femmine: le rese usano solo forme invarianti. "
)

# (riga, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = [
    # ── le tre righe d'intestazione ─────────────────────────────────────────
    (8050, [('"Level "', '"Livello "')], 1,
     "Il livello, sulla riga sua. "),
    (8051, [('"Male "', '"Maschio "')], 1,
     "Il sesso, che precede la razza sulla stessa riga: «Maschio Yerles». Sono due "
     "nomi in apposizione, e nessuno dei due concorda con l'altro. "),
    (8052, [('"Female "', '"Femmina "')], 1,
     "La gemella. "),

    # ── i sei ranghi, girati in etichette ───────────────────────────────────
    (8054, [('"Bad "', '"Principiante: "')], 1,
     "Il primo dei sei ranghi (`userdata(5)`), che precede il nome della classe. "
     "⭐ Girato in etichetta col due punti: l'aggettivo italiano andrebbe DOPO il nome, "
     "e messo davanti concorderebbe con una classe di genere ignoto. «Principiante» e' "
     "per giunta invariante. "),
    (8055, [('"Common "', '"Comune: "')], 1, "Il secondo rango. «Comune» e' in -e. "),
    (8056, [('"Skilled "', '"Abile: "')], 1, "Il terzo rango. «Abile» e' in -e. "),
    (8057, [('"Professional "', '"Professionista: "')], 1,
     "Il quarto rango. «Professionista» vale per tutt'e due i generi. "),
    (8058, [('"Legendary "', '"Leggenda: "')], 1,
     "Il quinto rango. ⚠️ «Leggendario» avrebbe concordato col nome della classe: il "
     "nome «Leggenda» no. "),
    (8059, [('"Well-Known "', '"Celebrita\': "')], 1,
     "Il sesto rango, che nel sorgente sta DOPO «Legendary» pur essendo un'altra scala. "
     "Anche qui un nome invece di un aggettivo. "),

    # ── il passatempo: l'etichetta e le tredici risposte ─────────────────────
    (8062, [('"Likes to: "', '"Passatempo: "')], 1,
     "L'etichetta, che si salda alla risposta sulla stessa riga. ⚠️ «Gli piace:» "
     "avrebbe portato il genere dell'avventuriero; «Passatempo:» no, ed e' la stessa "
     "forma delle altre due etichette del pannello. Le tredici risposte diventano "
     "quindi degli INFINITI, che e' anche lo stile delle voci di menu del progetto. "),
    (8063, [('"Do Nothing.\\n"', '"niente.\\n"')], 1,
     "«Passatempo: niente.» — la risposta si salda all'etichetta e comincia minuscola. "),
    (8064, [('"Walk Around.\\n"', '"gironzolare.\\n"')], 1, "Il vagabondaggio. "),
    (8065, [('"Walk in Circles.\\n"', '"girare in tondo.\\n"')], 1, "Il giro su se' stesso. "),
    (8066, [('"Do Nothing.\\n"', '"niente.\\n"')], 1,
     "⚠️ La gemella di :8063: stesso testo, condizione diversa (`userdata(7)` 3 invece "
     "di 0). Due righe distinte, due toppe. "),
    (8067, [('"Stalk People.\\n"', '"pedinare la gente.\\n"')], 1, "Il pedinamento. "),
    (8068, [('"Stalk Adventurers.\\n"', '"pedinare gli avventurieri.\\n"')], 1,
     "La riga piu' lunga del gruppo: con l'etichetta fa 38 caratteri su 46. "),
    (8069, [('"Sing.\\n"', '"cantare.\\n"')], 1, "Il canto. "),
    (8070, [('"Preach.\\n"', '"predicare.\\n"')], 1, "La predica. "),
    (8071, [('"Dance.\\n"', '"ballare.\\n"')], 1, "Il ballo. "),
    (8072, [('"Kill Snails.\\n"', '"ammazzare lumache.\\n"')], 1,
     "⭐ La lumaca e' una gag ricorrente di Elona e resta. "),
    (8073, [('"\\"It\'s a secret\\".\\n"', '"\\"e\' un segreto\\".\\n"')], 1,
     "⚠️ La riga con le VIRGOLETTE PROTETTE, che il referto `buff_en.py` non vedeva "
     "fino alla terza correzione: una regex che si ferma alla prima virgoletta la "
     "leggeva come stringa vuota e il filtro la buttava via. Lo escape resta. "),
    (8074, [('"Laze in Town.\\n"', '"oziare in citta\'.\\n"')], 1, "L'ozio in citta'. "),
    (8075, [('"Beg for Money.\\n"', '"chiedere l\'elemosina.\\n"')], 1, "L'accattonaggio. "),

    # ── i due numeri dell'IA ────────────────────────────────────────────────
    (8077, [('"Prefered Distance: "', '"Distanza preferita: "')], 1,
     "⚠️ «Prefered» e' un refuso di monte (si scrive «Preferred»): non lo si eredita. "),
    (8078, [('"Move Willingness: "', '"Voglia di muoversi: "')], 1,
     "La percentuale con cui l'avventuriero decide di spostarsi. "),

    # ── le tre intestazioni delle azioni ────────────────────────────────────
    (8079, [('"<title1>*Actions("', '"<title1>*Azioni("')], 1,
     "⚠️ `<title1>` e' un marcatore di `gmes` (`module.hsp:4964`) e NON si traduce: "
     "abbassa il corpo a 12 e cambia colore. Dentro quel marcatore il passo scende a "
     "6 px e il tetto sale a 54. "),
    (8094, [('"<title1>*Subactions("', '"<title1>*Azioni secondarie("')], 1,
     "Le azioni di riserva, con la loro percentuale. "),
    (8110, [('"<title1>*Emergency Action<def>\\n"',
             '"<title1>*Azione d\'emergenza<def>\\n"')], 1,
     "L'azione che scatta quando l'avventuriero e' in pericolo. `<def>` rimette il "
     "corpo a 14: e' l'altra meta' del marcatore e non si traduce. "),

    # ── le altre due intestazioni ───────────────────────────────────────────
    (8129, [('"<title1>*Resistance<def>\\n"', '"<title1>*Resistenze<def>\\n"')], 1,
     "⭐ Plurale: sotto ci sono fino a sedici righe, una per elemento. I nomi dei "
     "livelli («Nessuna», «Scarsa», «Ottima», «Suprema») vengono da `_resist` in "
     "`text.hsp:107`, che e' gia' tradotto. "),
    (8143, [('"<title1>*Quirks<def>\\n"', '"<title1>*Tratti<def>\\n"')], 1,
     "⚠️ Non «Stranezze»: sotto ci sono anche le immunita' e la levitazione, che "
     "stranezze non sono. «Tratti» copre tutta la lista. "),
]

# ── le venti azioni: tre blocchi che ripetono lo stesso repertorio ──────────
_AZIONI = {
    '"Do Nothing\\n"': ('"Non fare nulla\\n"',
                        "⭐ Presa dalla toppa di `custom_ai.hsp` (51a), dove «Do Nothing» "
                        "e' gia' «Non fare nulla»: il pannello dell'IA e questa scheda "
                        "mostrano lo stesso repertorio e devono chiamarlo uguale. "),
    '"Melee Attack\\n"': ('"Attacca (mischia)\\n"',
                          "⭐ Presa dalla toppa di `custom_ai.hsp`, dove «Attack (Melee)» "
                          "e' «Attacca (mischia)». "),
    '"Ranged Attack\\n"': ('"Attacca (a distanza)\\n"',
                           "⭐ Presa dalla toppa di `custom_ai.hsp`. Col costo davanti "
                           "(«[12]») fa 24 caratteri su 46. "),
    '"Roam Around\\n"': ('"Gironzola\\n"',
                         "⚠️ Questa NON c'era in `custom_ai.hsp`, che ha «Move (Away)» e "
                         "«Move (Forward)»: sono altre due azioni. «Gironzola» si fissa "
                         "qui. "),
    '"Throw Salt\\n"': ('"Lancia sale\\n"', "Il lancio del sale. "),
    '"Throw Potions\\n"': ('"Lancia pozioni\\n"', "Il lancio delle pozioni. "),
}
_BLOCCHI = [
    (range(8083, 8090), 'principale', 'userdata(15+cnt)'),
    (range(8098, 8105), 'secondario', 'userdata(20+cnt)'),
    (range(8113, 8119), "d'emergenza", 'userdata(10)'),
]
_sorg_azioni = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
for righe_blocco, quale, variabile in _BLOCCHI:
    for riga in righe_blocco:
        testo = _sorg_azioni[riga - 1]
        chiave = next((k for k in _AZIONI if k in testo), None)
        if chiave is None:
            raise SystemExit(f'{NOME}:{riga}: nessuna azione nota su questa riga')
        resa, nota = _AZIONI[chiave]
        VOCI.append((riga, [(chiave, resa)], 1,
                     f"L'azione nel blocco {quale} ({variabile}). " + nota))

# ── i trenta tratti ─────────────────────────────────────────────────────────
for riga, en, it, nota in [
    (8146, 'Can Float.', 'Levitazione.',
     "⭐ `command.hsp:2185` rende gia' «You can float.» con «Levitazione»: e' la stessa "
     "proprieta' vista da due finestre. "),
    (8147, 'Invisible.', 'Invisibile.', "In -e, quindi invariante. "),
    (8148, 'Keen Eyes.', 'Vista acuta.', "Un sintagma nominale, che non concorda. "),
    (8149, 'Immune to Confuse.', 'Immune alla confusione.',
     "⭐ «Immune» e' in -e: tutte e sette le immunita' sono invarianti per costruzione, "
     "ed e' un colpo di fortuna che qui vale molto. "),
    (8150, 'Immune to Blind.', 'Immune alla cecita\'.', "L'immunita' alla cecita'. "),
    (8151, 'Immune to Fear.', 'Immune alla paura.', "L'immunita' alla paura. "),
    (8152, 'Immune to Sleep.', 'Immune al sonno.', "L'immunita' al sonno. "),
    (8153, 'Immune to Paralyze.', 'Immune alla paralisi.', "L'immunita' alla paralisi. "),
    (8154, 'Immune to Poison.', 'Immune al veleno.', "L'immunita' al veleno. "),
    (8155, 'Iron Stomach.', 'Stomaco di ferro.',
     "L'idiotismo esiste identico in italiano. "),
    (8156, 'Hate Thieves.', 'Odia i ladri.',
     "⭐ Verbo alla terza persona: non concorda col soggetto, e vale per tutti. "),
    (8157, 'Stealthy.', 'Passo felpato.',
     "⚠️ «Furtivo» avrebbe portato il genere. Un sintagma nominale no. "),
    (8158, 'Loose Purse.', 'Borsa slacciata.',
     "Chi perde monete quando lo si colpisce. Il participio concorda con «borsa», che "
     "e' della frase e non del personaggio. "),
    (8159, 'Goes Kamikaze.', 'Si fa esplodere.',
     "⚠️ «Kamikaze» e' gia' nel progetto come nome di creatura (`action.hsp:17461`, «lo "
     "yeek kamikaze»), ma qui e' un comportamento e il verbo dice di piu'. "),
    (8160, 'Curses People.', 'Lancia maledizioni.', "Chi maledice chi lo colpisce. "),
    (8161, 'Master Blaster.', 'Artiglieria pesante.',
     "⚠️ «Maestro» avrebbe portato il genere. Il tratto vuol dire che l'avventuriero "
     "lancia magie d'attacco potenti, e un sintagma nominale lo dice senza concordare. "),
    (8162, 'Is a Defender.', 'Fa da scudo.',
     "⚠️ «E' un difensore» avrebbe portato il genere. ⚠️ E «Difensore» con la maiuscola "
     "e' gia' il nome di una carta (`db_card.hsp:14546`): qui e' un comportamento, non "
     "una creatura. "),
    (8163, 'Like Carrying Others.', 'Ama portare gli altri.',
     "Chi si carica in spalla i compagni caduti. "),
    (8164, 'Splits.', 'Si sdoppia.',
     "⭐ «Sdoppia» e' la resa gia' scelta per «Split» nella toppa del tavolo da gioco. "),
    (8165, 'Immune to Curse.', 'Immune alle maledizioni.',
     "Plurale, come le altre maledizioni del progetto. "),
    (8166, 'Hate Carrying Others.', 'Odia portare gli altri.', "Il rovescio di :8163. "),
    (8167, 'Blessed by Elements.', 'Benedizione degli elementi.',
     "⚠️ «Benedetto» avrebbe portato il genere. "),
    (8168, 'Splits Sometimes.', 'Ogni tanto si sdoppia.', "La versione saltuaria di :8164. "),
    (8169, 'Made of Metal.', 'Corpo di metallo.',
     "⚠️ «Fatto di metallo» avrebbe portato il genere. "),
    (8170, 'Immune to Bleeding.', 'Immune al sanguinamento.',
     "⭐ «Sangue» e' l'etichetta breve del tavolo da gioco; qui c'e' posto per la parola "
     "intera, ed e' la stessa cosa. "),
    (8171, 'Hate Walls.', 'Odia i muri.', "Chi non sa passare vicino a un muro. "),
    (8172, 'Think traps are okay.', 'Non teme le trappole.',
     "L'inglese e' colloquiale e l'italiano dice la stessa cosa in positivo. "),
    (8173, 'VERY ANGRY', 'IN COLLERA NERA',
     "⚠️ «MOLTO ARRABBIATO» avrebbe portato il genere. «In collera» e' invariante, e il "
     "maiuscolo dell'inglese resta perche' e' il tono. ⚠️ Ed e' l'unico tratto senza "
     "punto in coda, a monte: non gliene si aggiunge uno. "),
    (8174, 'Was not made of flesh.', 'Non aveva carne addosso.',
     "⚠️ «Non era fatto di carne» avrebbe portato il genere. ⭐ E il passato resta: "
     "l'inglese dice «was», ed e' un avventuriero che il giocatore ha gia' incontrato. "),
]:
    VOCI.append((riga, [(f'"{en}\\n"', f'"{it}\\n"')], 1, nota))

# ── l'ultimo tratto ha DUE letterali sulla stessa riga ──────────────────────
VOCI.append((8175, [('"Fastest "', '"Piu\' veloce di ogni "'),
                    ('" in the West.\\n"', '" a ovest.\\n"')], 1,
             "⭐ Il tratto con la battuta western, e l'unico con un pezzo interpolato in "
             "mezzo: `userdatan(3)`, il nome della classe. ⚠️ «Il piu' veloce» avrebbe "
             "portato l'articolo e quindi il genere della classe; «piu' veloce di ogni» "
             "no, perche' «veloce» e' in -e e «ogni» e' invariante. ⚠️ La coda si "
             "accorcia da «del West» a «a ovest» per lasciare posto: la riga vale 29 "
             "caratteri piu' il nome della classe, e il tetto e' 46. E' l'unica riga "
             "del pannello che puo' sforare, e solo con una classe da piu' di 17 "
             "caratteri. "))


sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')

nuove = []
for riga, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    if originale.lstrip().startswith(';'):
        raise SystemExit(f'{NOME}:{riga}: la riga e\' commentata nel sorgente')
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != attese:
            raise SystemExit(
                f'{NOME}:{riga} compare {quante} volte nel {eti}, non {attese}: '
                'la riga e\' cambiata, il conto va rifatto a mano'
            )

    nuova = originale
    for cerca, metti in sostituzioni:
        if nuova.count(cerca) != 1:
            raise SystemExit(
                f'{NOME}:{riga}: `{cerca}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + PANNELLO + CLASSE
    toppa['_riga'] = riga
    toppa['_quante'] = attese
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
