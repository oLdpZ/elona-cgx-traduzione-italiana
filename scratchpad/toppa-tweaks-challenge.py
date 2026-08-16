# -*- coding: utf-8 -*-
"""Il menu dei ritocchi di difficolta' (`*ChallengeTweakMenu_loop`, :1838-:1966).

Sette voci e sette descrizioni: **14 righe**. Titolo, riga di testa, «Indietro.»
e «Torna al menu precedente.» erano gia' chiusi dalle toppe `tutte` del menu
principale — verificato leggendo la build.

## ⚠️ Qui le voci portano DUE letterali, non uno

Al contrario del menu dell'IA, queste voci non chiamano `GetTStatus` ma
**`GetTStatusProgress`** (:502-:512), che ha un terzo argomento: l'etichetta del
contatore. `listn(0, 0) = "Permanent Etherwind." + GetTStatusProgress(…, "Days
Survived")` diventa a schermo « (Ora: 12 giorni di sopravvivenza)». Tradotta la
voce e lasciata l'etichetta, ogni riga di questo menu resterebbe mezza inglese —
ed e' il tipo di riga che nessun conteggio per riga vede, perche' le due
stringhe stanno sulla stessa riga.

⚠️ Percio' il tetto di larghezza qui si misura sulla **somma**: testo della voce
piu' il suffisso completo col contatore a quattro cifre. Il controllo qui sotto
lo fa da solo (`_larghezza_voce`).

## Il vocabolario, ancora tutto preso da fuori

    Etherwind        -> vento d'etere      text.hsp:46, item_data.hsp:662
    vindale cloak    -> mantello di Vindale  db_item.hsp:145171
    shelter          -> rifugio            db_item.hsp:145197, text.hsp:2827
    Elea (plurale)   -> gli Elea           map.hsp:770, db_creature.hsp:76550
    nuke             -> far saltare in aria  action.hsp:15396 (proprio questo evento)
    beggar           -> accattone          init.hsp:359 («Tugurio da accattone»)
    Impress          -> amicizia           command.hsp:4196 («Fama(amicizia)»)
    figurine         -> statuetta          db_item.hsp:145913
    HP               -> HP                 buff.hsp:530, skill.hsp:949 (non si traduce)
    fame             -> punti fama         action.hsp:1207, command.hsp:10517
    Vanilla          -> l'originale        init.hsp:2873 («la versione originale»)
    Big sis          -> Sorellona          text.hsp:111
    split            -> sdoppiarsi         chara_func.hsp:8751 («si sdoppia!»)

⭐ **«Wind God» e' una dea, non un dio.** E' Lulwy, che il progetto tratta al
femminile dappertutto (`db_creature.hsp:75097` «Sorella Lulwy», `:63022` «somma
Lulwy»): «che la dea del vento abbia pieta' di te». Ricalcare l'inglese avrebbe
cambiato sesso a un personaggio che il giocatore conosce.

⭐ **«Split Monsters» non e' il nome di una creatura** — nessuna voce di
dizionario lo porta. Sono le creature col bit `CHARA_BIT_SPLIT_*`, e il gioco
annuncia quel che fanno con «si sdoppia!» (`chara_func.hsp:8751`): la voce dice
«i mostri si sdoppiano», che e' la stessa parola che il giocatore legge in
combattimento. ⚠️ E l'inglese qui e' ridondante apposta («Split Monsters
split»); l'italiano non ha modo di ripetere la parola due volte senza sembrare
un errore, e non ci prova.

⚠️ **«challenge» qui e' «sfida», e non contraddice «Ritocchi di difficolta'».**
La categoria e' il livello di durezza (per questo la 50a la rese
«difficolta'»), ma `:1880` parla della **singola** partita a regole dure che si
vince o si perde: «la sfida e' persa».

## ⚠️⚠️ Un'incoerenza vecchia trovata per strada: fattura / bolletta

`db_item.hsp:144367` chiama l'oggetto **«fattura»**, ma le toppe del diario
della 50a scrivono **«bollette»** («Bollette (emesse il 1 del mese)», «Hai N
bollette da pagare»). E' **lo stesso oggetto**: quello che arriva ogni mese e
che si paga. Il giocatore legge «bollette» nel diario e poi cerca «fattura»
nell'inventario.
✅ Qui la descrizione parla dell'oggetto che si impugna, quindi dice **fattura**,
che e' il nome sotto cui il giocatore ce l'ha in mano.
⚠️ **Ma la scelta vera resta da fare**, ed e' della stessa famiglia di
«borraccia/bottiglia filtrante» gia' in elenco: non si risolve con una toppa,
perche' «fattura» sta nel dizionario di `db_item.hsp` con plurale e articolo
attaccati.

## La larghezza

Finestra 640: voci a `wx + 64` (576 px, **74** caratteri col metro prudente da
7,7), descrizioni a `wx + 38` (602 px, **78**). Le descrizioni vanno a capo sui
`\\n` del sorgente; quella di :1877 ne ha tre e qui ne ha quattro, che entrano
lo stesso — `mes` parte da `wy + 343` su una finestra alta 448.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

TETTO_VOCE = 74
TETTO_DESCRIZIONE = 78
# " (Ora: " + il contatore a quattro cifre + " " + l'etichetta + ")"
CORNICE_PROGRESSO = len(' (Ora: 9999 ') + len(')')

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_SFIDE = (
    "Sta nel menu dei ritocchi di difficolta' (`*ChallengeTweakMenu_loop`), uno dei "
    "sette menu di dettaglio del pannello dei ritocchi di Custom-GX. ⚠️ Le voci di "
    "QUESTO menu portano DUE letterali inglesi ciascuna, perche' chiamano "
    "`GetTStatusProgress` (:502-:512) e le passano l'etichetta del contatore: a schermo "
    "esce « (Ora: 12 <etichetta>)». Tradotta la voce e lasciata l'etichetta, la riga "
    "resterebbe mezza inglese, e nessun conteggio per riga se ne accorgerebbe perche' "
    "le due stringhe stanno sulla stessa riga. La finestra e' 640: le voci hanno 74 "
    "caratteri col metro prudente, contando anche il suffisso col contatore, e le "
    "descrizioni 78 per riga. "
)

# (riga, tipo, [(cerca, metti), …], occorrenze_attese, motivo)
#   tipo 'progresso' => la seconda sostituzione e' l'etichetta del contatore
VOCI = [
    # ── le sette voci ───────────────────────────────────────────────────────
    (1846, 'progresso',
     [('"Permanent Etherwind."', '"Vento d\'etere perenne."'),
      ('"Days Survived"', '"giorni di sopravvivenza"')], 1,
     "⭐ «Etherwind» e' «Vento d'etere» (text.hsp:46, item_data.hsp:662 «Protegge dal "
     "Vento d'etere»): il nome del tempo atmosferico, non una parola comune. "
     "⚠️ L'etichetta del contatore e' «giorni di sopravvivenza» e non «giorni "
     "sopravvissuti»: «sopravvivere» in italiano e' intransitivo e non regge un "
     "partecipio passato attributivo, per quanto l'inglese lo faccia. "),
    (1847, 'progresso',
     [('"Double your tax each month."', '"Raddoppia le tasse ogni mese."'),
      ('"Months Paid"', '"mesi pagati"')], 1,
     "⭐ La stessa sfida ha gia' un nome reso altrove: command.hsp:15560 «Double Tax "
     "Each Month» -> «Tasse doppie ogni mese», e :15562 «Hai pagato le tasse per N "
     "mesi!». La voce di menu e' all'imperativo come l'inglese, ma usa le stesse parole "
     "(«tasse», «ogni mese», «mesi pagati») perche' il giocatore deve riconoscere che e' "
     "la stessa cosa. "),
    (1848, 'progresso',
     [('"Nuke the beggar-cave."', '"Fai saltare la grotta da accattone."'),
      ('"Eleas Obliterated"', '"Elea polverizzati"')], 1,
     "⭐ «nuke» qui non e' una metafora: e' l'evento della bomba atomica, che "
     "action.hsp:15396 rende gia' «Hai piazzato la bomba atomica... e adesso scappa!!». "
     "«beggar» -> «accattone» viene da init.hsp:359 («Tugurio da accattone»), che e' la "
     "stessa presa in giro sulla catapecchia da cui si parte. ⭐ «Elea» resta «Elea» al "
     "plurale invariabile, come map.hsp:770 («gli Elea che stanno a casa tua», e proprio "
     "a proposito di Vernis) e db_creature.hsp:76550. "),
    (1849, 'voce',
     [('"(DISABLED) Make travelling harder."', '"(DISATTIVATO) Rendi piu\' duri i viaggi."')], 1,
     "⚠️ «Disabled» -> «disattivato» e' la resa gia' fissata dal suffisso di stato "
     "(custom_tweaks.hsp:457), dove l'inglese distingue «Off» da «Disabled»: qui in "
     "maiuscolo perche' l'inglese lo urla. ⚠️ Questa e' l'unica voce del menu SENZA "
     "suffisso di stato — il ritocco e' spento da monte e la riga non chiama nessuna "
     "`GetTStatus`. "),
    (1850, 'progresso',
     [('"Pets die permanently."', '"Gli alleati muoiono per sempre."'),
      ('"Friends Buried"', '"amici sepolti"')], 1,
     "«alleato» e' la resa gia' in uso per pet e follower (custom_tweaks.hsp:471). "
     "⭐ L'inglese cambia parola apposta nel contatore — non «Pets Buried» ma «Friends "
     "Buried» — e l'italiano lo segue con «amici»: e' la battuta della riga. "),
    (1851, 'progresso',
     [('"Split Monsters split (like in Vanilla)."', '"I mostri si sdoppiano come nell\'originale."'),
      ('"Copies Summoned"', '"copie evocate"')], 1,
     "⭐ «Split Monsters» non e' il nome di una creatura: nessuna voce di dizionario lo "
     "porta, e nel codice sono le creature col bit `CHARA_BIT_SPLIT_*` "
     "(chara_func.hsp:8759-:8795). Il gioco annuncia quel che fanno con «si sdoppia!» "
     "(chara_func.hsp:8751), e la voce usa quella stessa parola. ⚠️ L'inglese ripete la "
     "parola apposta («Split Monsters split»); in italiano ripeterla sembrerebbe un "
     "refuso, e non si ripete. ⭐ «Vanilla» -> «l'originale», come init.hsp:2873 rende "
     "«the vanilla version» con «la versione originale». "),
    (1852, 'progresso',
     [('"Powerful ambush spawns (like during Etherwind)."',
       '"Imboscate piu\' dure (come col vento d\'etere)."'),
      ('"Godly Encounters"', '"incontri divini"')], 1,
     "«Ambush!» e' gia' «Imboscata!» (action.hsp:2612). ⚠️ La resa diretta di «Powerful "
     "ambush spawns» sarebbe stata «Imboscate con nemici potenti», e col suffisso del "
     "contatore («(Ora: 999 incontri divini)») avrebbe sfondato i 74 caratteri: "
     "«piu' dure» dice la stessa cosa e ci sta. La descrizione di :1895 recupera i "
     "«nemici divini» per esteso. "),

    # ── le sette descrizioni ────────────────────────────────────────────────
    (1877, 'descrizione',
     [('"Weather will change into etherwind 100%, but hey, at least it\'s not raining. '
       '\\nShelters are closed. Vindale cloaks are sold out. Training time-skips are '
       'disabled. \\nHead to Lumiest, seek Renton, may the Wind God have mercy on your '
       'soul. "',
       '"Il tempo sara\' vento d\'etere al 100%, ma almeno non piove.\\nI rifugi sono '
       'chiusi. I mantelli di Vindale sono esauriti.\\nNon si puo\' piu\' saltare il '
       'tempo allenandosi.\\nVa\' a Lumiest, cerca Renton, e che la dea del vento abbia '
       'pieta\' di te."')], 1,
     "⭐⭐ **«Wind God» e' una DEA.** E' Lulwy, che il progetto tratta al femminile "
     "dappertutto (db_creature.hsp:75097 «Sorella Lulwy», :63022 «somma Lulwy», "
     "action.hsp:14207 dove parla in prima persona): «il dio del vento» avrebbe cambiato "
     "sesso a un personaggio che il giocatore conosce. «shelter» -> «rifugio» "
     "(db_item.hsp:145197), «vindale cloak» -> «mantello di Vindale» (db_item.hsp:145171), "
     "Lumiest e Renton restano (text.hsp:744, db_creature.hsp:121405). ⚠️ L'inglese "
     "spalma tre cose su una riga sola e sfonderebbe: l'italiano usa un a capo in piu' "
     "(quattro righe invece di tre), che la finestra regge — `mes` parte da `wy + 343` "
     "su 448 di altezza. "),
    (1880, 'descrizione',
     [('"You taxes will double each month. You building/hiring cost remain unchanged. '
       '\\nNot paying tax or using a empty bill will fail the challenge. \\nYou tax '
       'immunities will be lifted. \\nWorry not, your big sister Goddess may help you '
       'pay (some) your bills."',
       '"Le tasse raddoppiano ogni mese. Costruire e assumere costa come prima.\\nSe non '
       'paghi, o se usi una fattura vuota, la sfida e\' persa.\\nLe esenzioni dalle '
       'tasse non valgono piu\'.\\nTranquillo: la dea sorellona potrebbe pagarne '
       '(qualcuna) per te."')], 1,
     "⚠️⚠️ **«bill» qui e' l'OGGETTO, e il progetto lo chiama in due modi.** "
     "db_item.hsp:144367 lo rende «fattura», ma le toppe del diario della 50a scrivono "
     "«bollette» («Bollette (emesse il 1 del mese)», «Hai N bollette da pagare»): e' lo "
     "stesso oggetto e il giocatore lo incontra con due nomi. Qui si dice «fattura» "
     "perche' la frase parla di quel che si ha in mano, cioe' del nome che l'oggetto "
     "porta nell'inventario — ma **l'incoerenza resta da sciogliere**, ed e' della "
     "stessa famiglia di «borraccia/bottiglia filtrante». ⚠️ «challenge» qui e' la "
     "singola partita a regole dure, quindi «sfida»: non contraddice «Ritocchi di "
     "difficolta'» della categoria, che e' il livello di durezza. ⭐ «big sister» -> "
     "«sorellona» e' la resa di text.hsp:111 («Big sis»). "),
    (1883, 'descrizione',
     [('"You can nuke your home again. \\nThis will prevent you from entering Vernis '
       'until you nuked your cave. \\nYou can leave home without triggering main quest. '
       '\\nNoel quest no longer require 7000 fame."',
       '"Puoi di nuovo far saltare in aria casa tua.\\nNon potrai entrare a Vernis '
       'finche\' non hai fatto saltare la grotta.\\nPuoi uscire di casa senza far '
       'partire la trama principale.\\nL\'incarico di Noel non chiede piu\' 7000 punti '
       'fama."')], 1,
     "⭐ Il giro di parole non e' inventato: map.hsp:770 dice gia' «Non hai ancora "
     "salutato gli Elea che stanno a casa tua. Vuoi davvero entrare a Vernis?», che e' "
     "esattamente il blocco di cui parla questa riga. «fame» -> «punti fama» "
     "(action.hsp:1207, command.hsp:10517), «quest» -> «incarico», Noel resta "
     "(db_creature.hsp:121592 «<Noel> la dinamitarda», ed e' proprio lei quella delle "
     "bombe). "),
    (1886, 'descrizione',
     [('"Traveling is revamped in 2.27. This tweak is now disabled."',
       '"I viaggi sono stati rifatti nella 2.27. Questo ritocco e\' disattivato."')], 1,
     "La descrizione della voce spenta da monte. «disattivato» come la voce. "),
    (1889, 'descrizione',
     [('"Pets now have permadeath.\\nOn the bright side, they now drop figurine and '
       'corpses!\\n(Only if they have high impression.)"',
       '"Gli alleati muoiono per sempre.\\nIn compenso adesso lasciano statuette e '
       'cadaveri!\\n(Solo se hanno molta amicizia.)"')], 1,
     "⭐ «impression» e' il valore di affetto che il gioco chiama gia' «amicizia» "
     "(command.hsp:4196 «Fame(Impress)» -> «Fama(amicizia)», :4199 «Messaggio(amic.)»): "
     "non «impressione», che in italiano non vuol dire niente qui. «figurine» -> "
     "«statuetta» (db_item.hsp:145913), «corpse» -> «cadavere» (db_item.hsp:150042). "),
    (1892, 'descrizione',
     [('"Split Monsters no longer has a HP threshold handicap.\\nExpect things to get '
       'out of hand fast.\\nThis applies to your allies too."',
       '"I mostri che si sdoppiano non hanno piu\' una soglia di HP.\\nAspettati che la '
       'cosa sfugga di mano in fretta.\\nVale anche per i tuoi alleati."')], 1,
     "⚠️ «HP» NON si traduce: il progetto lo lascia cosi' (buff.hsp:530 «Consuma HP e "
     "MP», skill.hsp:949 «Cura gli HP»). ⭐ «get out of hand» -> «sfuggire di mano» e' "
     "l'idioma italiano gemello, non una traduzione parola per parola. "),
    (1895, 'descrizione',
     [('"Ambush spawn godly enemies like during Etherwinds.\\nVery deadly for new '
       'characters, free loot for end game."',
       '"Le imboscate mandano nemici divini come col vento d\'etere.\\nMicidiali per un '
       'personaggio nuovo, bottino gratis a fine partita."')], 1,
     "⚠️ «godly» ha due rese in dizionario (text.hsp:56 «senza pari al mondo», :106 "
     "«celestiale») ma tutt'e due sono la QUALITA' di un oggetto, non la forza di un "
     "nemico: qui non si riusano, e «divini» dice quel che l'inglese dice. "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')


def _letterale(pezzo: str) -> str:
    return pezzo.strip('"').replace('\\n', '\n')


def _larghezza_voce(tipo: str, sostituzioni: list) -> int:
    """Quanto e' larga a schermo la voce, suffisso di stato compreso."""
    testo = _letterale(sostituzioni[0][1])
    if tipo != 'progresso':
        return len(testo)
    etichetta = _letterale(sostituzioni[1][1])
    return len(testo) + CORNICE_PROGRESSO + len(etichetta)


nuove = []
for riga, tipo, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    # ⚠️ regola della 50a: il `cerca` deve agganciare il sorgente pinnato E la build.
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
        for pezzo in _letterale(sostituzioni[0][1]).split('\n'):
            if len(pezzo) > TETTO_DESCRIZIONE:
                raise SystemExit(
                    f'{NOME}:{riga}: {len(pezzo)} caratteri, tetto {TETTO_DESCRIZIONE} '
                    f'— {pezzo!r}')
        largo = max(len(p) for p in _letterale(sostituzioni[0][1]).split('\n'))
    else:
        largo = _larghezza_voce(tipo, sostituzioni)
        if largo > TETTO_VOCE:
            raise SystemExit(
                f'{NOME}:{riga}: la voce col suffisso e\' larga {largo}, tetto {TETTO_VOCE}')

    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    # ⚠️ le toppe non passano da `accenti.py`: l'apostrofo e' scritto a mano.
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + MENU_SFIDE + CLASSE
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
