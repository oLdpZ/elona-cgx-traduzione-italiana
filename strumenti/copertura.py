# strumenti/copertura.py
"""Quale testo inglese del sorgente non lo raggiunge nessuno.

⚠️⚠️ IL BUCO CHE QUESTO MODULO CHIUDE. Tutte le reti del progetto partono da
cio' che qualcuno ha gia' deciso di coprire:

    verifica --dizionario           scorre DIZIONARIO/*.jsonl
    applica                         scorre DIZIONARIO/*.jsonl e toppe.jsonl
    perimetro.py                    conta firme lang(), nomi db_item, file dati
    _123-file-senza-dizionario.py   i file CON lang() e SENZA dizionario

Nessuna di queste puo' trovare una stringa che nessuno ha mai chiesto. Il
perimetro diceva **100,0%** alla fine della 134a, e sotto quel numero stavano
`tcg_mod.hsp` (809 stringhe inglesi distinte a schermo) e `tcg_skill.hsp` (142):
il testo del gioco di carte, cioe' quasi tutto quello che il minigioco dice.
Trovati alla 135a partendo dall'elenco dei file del SORGENTE.

⭐ **Come applicarlo:** una rete che parte dall'elenco delle cose coperte non
puo' trovare le cose scoperte.

⚠️⚠️ E LA COPERTURA E' UNA PROPRIETA' DELLA STRINGA, NON DEL FILE. Il primo
censimento della 135a chiedeva «questo file ha un dizionario o una toppa?», e
per questo dava `tcg_mod.hsp` per **coperto**: ha un dizionario (8 voci) e una
toppa (le fasi del turno), contro 809 stringhe che non raggiunge nessuno. Un
file coperto per un ottavo di percento risultava indistinguibile da uno coperto
davvero. Qui una stringa e' raggiunta solo se lo e' **lei**:

    - sta dentro una `lang()`      -> la prende `estrai`, e quindi il dizionario
    - la sua riga la riscrive una toppa
    - il suo file ha un meccanismo proprio, dichiarato in MECCANISMI

LA FORMA DEL CANCELLO. Non «ogni stringa dev'essere coperta»: sarebbe un
cancello che chiede l'impossibile, e quelli vengono disattivati, non rispettati
(lezione della 134a sul soffitto dei `{txt}`). Chiede una cosa piu' debole e
piu' utile: **ogni file con stringhe scoperte e' DICHIARATO, e il suo conto
torna**. Si accende su:

  - un file scoperto che nessuno ha dichiarato   <- il caso di tcg_skill
  - un conto dichiarato che non torna piu'       <- monte mosso in silenzio
  - una dichiarazione diventata inutile          <- il file ora e' coperto

Il terzo caso e' quello che impedisce alla lista di marcire: quando un fronte
dichiarato viene lavorato, la sua riga va tolta, e il cancello lo ricorda.
"""
import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass

from strumenti import percorsi
from strumenti.commenti import righe_in_commento
from strumenti.estrai import siti

# Un letterale HSP, con la regola del backslash del progetto: `\"` non chiude
# la stringa (vedi `estrai.py`, ESCAPE).
_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')

# «Prosa»: due parole alfabetiche separate da spazio, la prima lunga almeno
# tre lettere. Separa una frase da un identificatore, che nessuna lingua tocca:
# tace su `"dragon"`, `"bg3"`, `"ITEM_ID_BANANA"`, `"\t"`, `"male"`.
#
# ⚠️ E' un riconoscitore GROSSOLANO, ed e' voluto: deve sbagliare per eccesso.
# Un falso positivo costa una riga di dichiarazione con scritto perche'; un
# falso negativo costa un'altra Fase 4 chiusa al 100% con 951 stringhe inglesi
# dentro.
# ⚠️⚠️ QUESTA EURISTICA NON VEDE LE ETICHETTE, E UN'INTERFACCIA E' FATTA DI
# ETICHETTE. Pretende DUE parole: `"Regeneration "` e' una parola sola seguita
# da uno spazio, e dopo lo spazio non c'e' nessuna lettera, quindi non aggancia.
# La 137a ne ha trovate **32 a schermo** cosi' -- le 31 etichette dei bit di
# `tcg.hsp:1522-1605` piu' `"Bits:  "` -- dentro un file che questo modulo
# dichiarava e contava. Non erano un fronte non dichiarato: erano dentro un
# fronte dichiarato, e il numero del fronte non le comprendeva.
#
# ⚠️ Il buco vale per TUTTO il sorgente, non solo per `tcg.hsp`. Quante siano
# altrove nessuno l'ha misurato, ed e' una cosa aperta scritta in
# `RIPRESA-sessione.md`, non un lavoro fatto a meta' in silenzio. Allargare
# l'euristica alla parola sola qui dentro pero' non si puo': in HSP la
# stragrande maggioranza dei letterali di una parola sono identificatori, e il
# referto annegherebbe. Serve una rete che parta da CHI DISEGNA, non dalla forma
# della stringa.
_PROSA = re.compile(r"[A-Za-z]{3}[a-z]*\s+[A-Za-z]")


# I file che hanno una catena tutta loro, che non passa ne' dal dizionario di
# `estrai` ne' dalle toppe. Non sono esenzioni: sono coperture che questo
# modulo non sa leggere, e il cancello di ciascuno sta altrove.
MECCANISMI = {
    "scene2.hsp": "i blocchi di scena, iniettati da `strumenti.scene --applica` "
                  "e sorvegliati da `scene --referto` (1701 su 1701). Le "
                  "stringhe che questo modulo vede sono le etichette "
                  "`{actor_N}` — `\"<Saimore> The Crown Prince of Zanan,54\"` — "
                  "che `scene.py:45` tratta come un tipo di blocco suo.",
    "tcg_mod.hsp": "le descrizioni d'effetto delle carte, iniettate da "
                   "`strumenti.carte --applica` e sorvegliate da "
                   "`carte --referto` (833 su 833, piu' 8 battute su 8). "
                   "Chiuso nella 136a. ⚠️ UNA stringa resta fuori e non e' "
                   "dimenticata: `efftalk@tcg(TCG_EFF_LITTLESISTER)` "
                   "(`tcg_mod.hsp:2354`) e' `cnvtalk(\"\" + _onii(...) + \"!\")`, "
                   "una concatenazione e non un letterale. Il riconoscitore la "
                   "rifiuta apposta -- meglio una riga in meno tradotta che una "
                   "riga sbagliata iniettata -- e va guardata a mano insieme a "
                   "`_onii()`, che decide come il fratellino chiama chi gioca.",
}


@dataclass(frozen=True)
class Dichiarazione:
    tipo: str        # "esente" | "fronte" | "da_triare"
    scoperte: int    # stringhe DISTINTE non raggiunte, sul sorgente pinnato
    motivo: str


# ⚠️ Il conto accanto a ogni riga non e' decorazione: e' il motivo per cui il
# sorgente sta pinnato a un tag e non a un branch. Se monte si muove e il
# numero cambia, la dichiarazione non vale piu' per il file che descriveva, e
# il cancello lo dice invece di lasciarla passare per inerzia.
DICHIARATI: dict[str, Dichiarazione] = {
    # ---- i due fronti veri trovati dalla 135a: il gioco di carte -----------
    # ✅ `tcg_mod.hsp` NON sta piu' qui: la 136a l'ha chiuso, e ora e' in
    # MECCANISMI. La sua riga di dichiarazione andava tolta insieme al lavoro,
    # non lasciata: un file dichiarato E coperto veniva contato due volte, e il
    # totale in fondo al referto diceva 1.020 scoperte quando ne restavano 211.
    "tcg_skill.hsp": Dichiarazione(
        "esente", 8,
        "✅ CHIUSO NELLA 138ª, ed erano 142. La 137ª ne ha rese 70 (le schede "
        "di carta scritte a mano, `strumenti/schede.py`), la 138ª le battute "
        "della nuvoletta (`strumenti/dialoghi.py`) e gli sparsi del lotto E "
        "come toppe. Quel che resta sono **8 tracce di debug** — `proctcg "
        "\"tcg attacking: \"` e compagne, che escono solo con `dbg_tcg` — e "
        "per questo la riga e' passata da `fronte` a `esente`. "
        "⚠️⚠️ «Esente» vale per quel che questo modulo VEDE. Delle 77 battute "
        "vere `_PROSA` ne vedeva 52: le altre 25 — `\"One!\"`, "
        "`\"AIEEE!!!\"`, `\"Cheapskate.\"` — erano a schermo dentro un file "
        "dichiarato, e nessun conto le comprendeva. Sono rese, ma la domanda "
        "«quante altre ce ne sono negli altri 90 file» resta aperta ed e' "
        "scritta in `RIPRESA-sessione.md`: il conto del fronte e quello del "
        "lavoro sono due misure diverse. "
        "⚠️ Tre `instr(carddetailneff@tcg(...), 0, \"ragon\")` (`:4960`, "
        "`:4972`, `:5003`) CERCANO dentro il testo della carta: la resa di "
        "«dragon» deve contenere «ragon» — «dragone» va, «drago» no. E' un "
        "difetto preesistente, non lo ha introdotto la traduzione, e la "
        "decisione di glossario non e' ancora presa."),

    # ---- fronti piccoli, triati alla 135a ---------------------------------
    "map_func.hsp": Dichiarazione(
        "fronte", 1,
        "Resta il filtro a tendina delle categorie di oggetto (:2517): 26 voci "
        "in una stringa sola, «All items\nFurniture\nJunk\n...». Non e' "
        "lasciata indietro per fatica — quella lista FISSEREBBE i nomi italiani "
        "delle categorie, e il progetto non ce li ha: `categorie.py` legge la "
        "classe che il sorgente DICHIARA (`FILTER_ITEM_FOOD`...), che e' una "
        "chiave, non un nome da mostrare. Deciderli in un attrezzo laterale "
        "vorrebbe dire ritrovarseli addosso nell'interfaccia del gioco. "
        "ⓘ Rese alla 135a: le quattro modalita' e i quattro comandi del menu "
        "Win32, la conferma della mappa nuova, la guida (:1896) e la casella "
        "«Costa automatica» — guida e casella insieme, perche' la prima nomina "
        "la seconda."),
    # ---- esenzioni: sembrano prosa e non sono testo ------------------------
    "custom_itemlist.hsp": Dichiarazione(
        "esente", 1,
        "Quel che resta dopo la toppa della 135a: `\"ID\\tType\\tJName\\t"
        "EName\\tValue\"` (:49), l'intestazione del TSV che questo stesso file "
        "scrive con `noteadd` e poi rilegge per sapere quali oggetti "
        "evidenziare. Tradurla non cambierebbe una parola a schermo: "
        "romperebbe il formato. L'altra stringa del file — la finestra di "
        "errore di :10 — e' stata resa e ora e' coperta da una toppa."),
    "sound.hsp": Dichiarazione(
        "esente", 7,
        "Comandi MCI di Windows, non testo: `mci \"close music\"` (:998), "
        "`mci \"play music repeat\"` (:1052), `\"set music time format "
        "milliseconds\"`. Sono l'API del sistema operativo. Tradurli non "
        "cambierebbe una parola a schermo: spegnerebbe la musica."),
    "lua.hsp": Dichiarazione(
        "esente", 9,
        "Due famiglie, tutt'e due fuori dallo schermo. `luaError(...)` e' "
        "`#define ctype luaError(%1) hl_pushnil : hl_pushstring %1 : return 2` "
        "(:13): la stringa torna all'interprete Lua come valore d'errore, e la "
        "legge chi scrive un mod, non chi gioca. `proc \"Lua init\"` (:16) e' "
        "una traccia di debug."),
    "helloworld.hsp": Dichiarazione(
        "esente", 1,
        "File di prova di HSP, 6 righe. Nessuno lo `#include`: l'unica "
        "occorrenza di «helloworld» nel sorgente e' il suo `#packopt`. Non "
        "entra nell'eseguibile."),

    # ---- il resto della famiglia TCG: appartiene al fronte del minigioco ---
    "tcg.hsp": Dichiarazione(
        "fronte", 14,
        "⭐ ERANO 52: la 137ª ne ha rese 23 — le 21 etichette della scheda "
        "(`[Carta comando]`, `<Gilda dei Maghi>`) come toppe del lotto B, e le "
        "2 schede scritte a mano con `schede.py` — e la 138ª altre 15: le 4 "
        "battute della nuvoletta (`dialoghi.py`: <Rianna> che perde, "
        "`imaritsuka@tcg` che sfotte, «Sia la luce...») piu' gli 11 sparsi "
        "del lotto E come toppe — i 9 segnaposto della tabella che "
        "`TCG_card_list.txt` esporta e il nome del tipo di file nella "
        "finestra di dialogo del mazzo. "
        "⚠️ **Restano 14, e 5 sono un lotto vero**: i «Sort by:» del menu "
        "mazzo (`:3348-:3352`), che stanno in slot a larghezza fissa insieme "
        "agli 8 «Filter:» — il lotto B2, che vuole essere GUARDATO a schermo "
        "prima di essere tradotto perche' l'italiano e' piu' lungo. Gli altri "
        "9 sono `proctcg` di debug. "
        "IL TERZO PEZZO DEL GIOCO DI CARTE, in un file che ha gia' 102 toppe e "
        "un dizionario: e' il contorno a essere stato lavorato, non le carte. "
        "Le 26 righe `if` di :1568-:1605 sono le ETICHETTE che si appendono al "
        "testo della carta — `[Command Card]`, `[Illegal Card]`, `<Mage "
        "Guild>` — e le cinque di :3348-:3352 sono il menu «Sort by:». "
        "Aggiungi tre `carddetailneff@tcg`, tre `efllistaddchat` e i "
        "segnaposto delle schede (:4632-:4658, «race dependent», «[Random "
        "AKA] [Random Name]»). ⚠️ Restano fuori 10 `proctcg`, che sono tracce "
        "di debug. Vanno lavorate INSIEME a `tcg_mod` e `tcg_skill`: le "
        "etichette entrano nella stessa stringa delle schede. "
        "⚠️⚠️ E QUESTO 52 NON E' TUTTO: la 137ª ha reso **32 stringhe a "
        "schermo di questo stesso file** che il conto non comprende — le 31 "
        "etichette dei bit (`\"Flying \"`, `\"Haste \"`...) e `\"Bits:  \"` — "
        "perché `_PROSA` pretende due parole. Il 52 resta 52: quelle 32 non "
        "c'erano dentro nemmeno prima."),
    "tcg_custom.hsp": Dichiarazione(
        "fronte", 4,
        "Tre tracce di debug (`proc`, `proctcg`, `poptext@tcg`) e una cosa "
        "che al fronte TCG appartiene davvero: `sreplace ..., \"the The\"` "
        "(:4566), cioe' la pezza che l'inglese mette per non scrivere «the "
        "The» quando compone un nome di carta. In italiano quella pezza o "
        "cambia o sparisce, e la decisione si prende con le carte in mano."),

    # ---- fronti veri, piccoli, trovati dal triage della 135a ---------------
    "buff.hsp": Dichiarazione(
        "esente", 48,
        "⭐ MORTE PER TOPPA — la QUARTA specie di copertura, dopo il dizionario, "
        "la toppa che riscrive e il meccanismo proprio. La forma e' "
        "`bufftxt(0, BUFF_X) = lang(jp, \" get\"), \" surrounded by a hazy "
        "mist.\"`: l'assegnazione riempie DUE celle, la prima con una `lang()` "
        "e la seconda col resto della frase, nudo. L'inglese le ricomponeva in "
        "`nome + bufftxt(0) + _s(...) + bufftxt(1)`, e quel `_s()` e' la "
        "desinenza inglese di terza persona, che in italiano cadrebbe in mezzo "
        "alla frase. ⚠️ Il progetto l'aveva GIA' risolto: una toppa sostituisce "
        "tutto il blocco `if ( en )` di `chara_func.hsp` con "
        "`txt name(addbuff_charid) + bufftxt(0, addbuff_buffid)`, cioe' la "
        "composizione a una parte sola. Da allora la frase italiana sta INTERA "
        "nella `lang()`, e `bufftxt(1)` non lo legge piu' nessuno. Verificato "
        "sull'albero di build: l'unica occorrenza di `bufftxt(1` che resta e' "
        "`chara_func.hsp:2310`, dentro il `/* ORIGINAL */`. "
        "⚠️ Questo modulo non puo' dedurlo — non sa che una toppa ha tolto il "
        "lettore — e senza qualcuno che vada a guardare le avrebbe tenute per "
        "un fronte da 48."),
    "system.hsp": Dichiarazione(
        "esente", 74,
        "Quel che resta dopo le nove rese della 135a: NON e' testo. 54 `noteadd` "
        "e 11 `proc` sono la CONSOLE DI DEBUG, che si annuncia da sola a :4400 "
        "(«Debug Console  Type \\\"?\\\" for help»); `%Elona Custom Item` (:1869) e "
        "`%Elona Custom Npc` (:1972) sono la firma dei file che il gioco scrive "
        "e rilegge; il `s = ...` di :3537 e' il ramo `if ( jp )` del menu del "
        "titolo, e il ramo inglese e' gia' reso da una toppa di sessioni fa; "
        "due `dialog` a :3995 e :4002 dicono «Failed to get WINDOW ID» e restano "
        "diagnostici. ⓘ Rese alla 135a: le tre regole sul nome (:1924-:1934, "
        "gemelle a :2060-:2068), i quattro `filedsc`, il filtro BMP|JPG, "
        "l'avviso di migrazione dei Tweak (:72) e la riga dei crediti di :3521."),
    "command.hsp": Dichiarazione(
        "esente", 10,
        "Quel che resta dopo le cinque rese della 135a non si traduce, e sette "
        "decimi sono la trappola: le righe `if` di :4481-:4763 confrontano quel "
        "che il giocatore ha scritto o il nome di un oggetto — «god inside», "
        "«man inside», «dog whistle», «happy new year», «merry christmas», "
        "«small coin», «small medal» — e sono innesti di uova di Pasqua. "
        "Tradurle senza l'altro capo del confronto spegne l'evento in silenzio. "
        "Le altre tre: `\"ElonaPlus Custom-GX \"` e' l'operando di uno "
        "`sreplace` (:413), e «Elona Version » (:17658) e «Level(Piety Cost)» "
        "(:7625) sono gli argomenti GIAPPONESI di due `lang()`, che non si "
        "traducono per costruzione. ⓘ Rese alla 135a: i due `dialog` di :13240, "
        "le due `description` dell'oggetto Omake e i due `filedsc`."),
    "main.hsp": Dichiarazione(
        "esente", 2,
        "Quel che resta dopo le cinque rese della 135a: "
        "`ElonaPlus Custom-GX 2.31.1.0` (:21) e' la stringa di VERSIONE, e "
        "`Invalid defLoadFolder. name` (:212) e' un errore che scatta solo con "
        "un albero di sviluppo rotto — chi lo vede sta compilando, non "
        "giocando. ⓘ Rese alla 135a: le due finestre d'avvio (:61 e :73 "
        "insieme, :66), l'avviso di posizione non valida (:1987) e le due "
        "conferme di caricamento rapido (:3176, :3178)."),
    "custom_ai.hsp": Dichiarazione(
        "esente", 1,
        "Resta `\"not set\"` minuscolo a :71, che sta dentro un `if`: e' "
        "l'operando del confronto, non l'etichetta. L'etichetta e' il `Not Set` "
        "maiuscolo di :3214, ed e' resa. ⓘ Rese alla 135a: le quattro azioni "
        "dell'IA dei famigli (:3077-:3086), il valore vuoto del menu, la "
        "conferma di reimpostazione (:1663) e la descrizione del file "
        "(:3483, gemella a :3501)."),
    "module.hsp": Dichiarazione(
        "fronte", 10,
        "⚠️ QUI LA DOMANDA E' PIU' GROSSA DELLE DIECI STRINGHE. Otto sono "
        "`cnv_str fix_wish_arg1, \"card of \", \"\"` (:4815-:4825): sono i "
        "prefissi che il gioco TOGLIE da quel che il giocatore scrive quando "
        "esprime un desiderio, per capire che oggetto vuole. Non sono testo a "
        "schermo, ma sono operandi tarati sui nomi INGLESI degli oggetti — e "
        "i nostri nomi ora sono italiani, quindi con ogni probabilita' non "
        "agganciano piu' niente. Vanno decisi col contratto dei nomi in mano, "
        "non da soli. Le altre due: un `proc` di debug e il filtro «ALL files "
        "(*.*)» di una finestra di Windows."),
    "chara_func.hsp": Dichiarazione(
        "esente", 8,
        "Nessuna delle otto e' lavoro, per tre ragioni diverse. Tre `title` e "
        "un `proc` scrivono nella barra della finestra o nel log un messaggio "
        "diagnostico. Il `txt` di :8640 e' l'argomento GIAPPONESE di una "
        "`lang()` — l'inglese, «[SURVIVABILITY EXTENSION !] Phase 1 "
        "completed...», sta nel dizionario; gemello di `item.hsp:4324`. "
        "⚠️ E i tre `gain_ap (gain_ap_source + \" of your mount\")` "
        "(:8536-:8546) sono MORTI PER RESA: due toppe di sessioni fa hanno "
        "sostituito `gain_ap_source` con frasi fisse («dalla trattativa», "
        "«dall'uccisione», «dalla pietra del risveglio»), e nella build quella "
        "variabile non arriva piu' a nessun `txt` — resta solo negli `==`. "
        "Verificato sull'albero di build."),
    "action.hsp": Dichiarazione(
        "esente", 11,
        "Dieci `proc` sono tracce di debug del regalo di capodanno "
        "(:3809-:3959). L'undicesima, `Potion-charge Lv` (:6545), e' "
        "l'argomento GIAPPONESE di una `lang()` in cui i due rami portano la "
        "stessa stringa: l'inglese sta nel dizionario, e il gemello e' "
        "`proc.hsp:13471`. Nessuna delle undici e' lavoro."),
    "proc.hsp": Dichiarazione(
        "esente", 2,
        "`Omae wa mou shindeiru.` (:14392) e' una citazione e resta com'e': "
        "tradurla la spegnerebbe. `Potion-charge Lv` (:13471) e' l'argomento "
        "GIAPPONESE di una `lang()` in cui i due rami portano la stessa "
        "stringa; l'inglese sta nel dizionario. ⓘ Rese alla 135a: «your "
        "friends» due volte (:16980 e :19167), e con loro il difetto che le "
        "teneva nascoste — due rese avevano inghiottito la variabile col nome "
        "del compagno. Vedi il motivo delle due toppe."),
    "screen.hsp": Dichiarazione(
        "esente", 2,
        "Restano i due letterali di :8288, che scrivono nella BARRA DEL TITOLO "
        "della finestra un messaggio diagnostico («Invalid race id detected on "
        "map [...], removing race id from ...»): non e' testo di gioco, e chi "
        "lo legge lo sta segnalando. ⓘ Resa alla 135a: la finestra della "
        "risoluzione non valida (:22), che il giocatore vede all'avvio."),
    "db_creature.hsp": Dichiarazione(
        "esente", 4,
        "Le quattro grida dei boss — 「Last Danceが最後の行程に入った」 (:51263), "
        "「HAPPY END！！」 (:53276), 「Target Acquired.」 e 「Resistance is "
        "futile!」 (:99788) — sono gli argomenti GIAPPONESI di altrettante "
        "`lang(jp, cnvtalk(en))`. L'inglese sta DENTRO la `cnvtalk` "
        "nell'argomento `en`, quindi il dizionario lo copre gia'; il "
        "giapponese non si traduce per costruzione. Sembravano scoperte perche' "
        "il ramo giapponese di queste quattro e' scritto mezzo in latino."),
    "help.hsp": Dichiarazione(
        "fronte", 1,
        "Resta `s \"広域能力を使う(Wide apply)\"` (:409): una voce di menu che "
        "porta il giapponese e l'inglese INSIEME nella stessa stringa, fuori da "
        "`lang()`. Il dizionario non puo' prenderla, e in italiano va decisa "
        "come una voce sola — cioe' bisogna prima sapere che cosa fa quel "
        "comando, e nessuno l'ha ancora guardato in gioco. ⓘ Resa alla 135a: "
        "il `dialog` dell'indice della guida mancante (:230)."),
    "item.hsp": Dichiarazione(
        "esente", 1,
        "`txt lang(\"[HAPPY BIRTHDAY！！]　フェイズ2が完了した。\", "
        "\"[HAPPY BIRTHDAY!!] Phase 2 completed.\")` (:4324): e' l'argomento "
        "GIAPPONESE, e l'inglese sta nel dizionario. Gemello di "
        "`chara_func.hsp:8640`, che e' la fase 1 della stessa catena."),
    "db_card.hsp": Dichiarazione(
        "fronte", 1,
        "`cardrefskill` a :2695: una descrizione di carta lunga, in "
        "giapponese, nuda fuori da `lang()` in un file che ne ha 2.326. "
        "Appartiene al fronte TCG per contenuto, a `db_card` per posizione."),
    "text.hsp": Dichiarazione(
        "esente", 1,
        "Resta `proc \"god text\"` (:12150), una traccia di debug. ⓘ Resa alla "
        "135a: `sg \"Unknown Code\"` (:9351), che il giocatore legge al posto "
        "di un codice che il gioco non riconosce."),

    # ---- esenzioni trovate dal triage della 135a ---------------------------
    "init.hsp": Dichiarazione(
        "esente", 61,
        "E' IL RAPPORTO DI ERRORE, tutto quanto. 41 `ErrorMsg` sono i nomi "
        "degli errori dell'interprete HSP («Stack overflow», «Divided by "
        "zero», «Array overflow», :2671-:2711), 14 `buf` sono le righe che il "
        "gioco scrive nel rapporto quando crolla («* error in "
        "function:chara_create:#», :2751-:2871), 5 sono `proc` di debug. "
        "⚠️ Vanno lasciati in inglese di proposito: chi riceve un rapporto di "
        "crash deve poterlo confrontare con quelli di monte, e un «Overflow "
        "del buffer» in mezzo a una segnalazione la rende inutile. "
        "`\"unknown user\"` (:549) e' per giunta un operando di confronto."),
    "map.hsp": Dichiarazione(
        "esente", 11,
        "Undici `proc`, tutti tracce di debug del ciclo della mappa "
        "(«Map:Check renew», «Map:Init music», «Map:Quest message», "
        ":9616-:12211). Nessuna arriva a schermo."),
    "config.hsp": Dichiarazione(
        "esente", 4,
        "Due `proc` di debug, e due falsi positivi di una specie che vale la "
        "pena registrare: `s = lang(\"なし\", \"None\"), lang(\"direct "
        "sound\", \"Direct sound\"), \"MCI\"` (:805 e :809). «direct sound» e' "
        "l'argomento GIAPPONESE della `lang()` — il ramo giapponese scrive in "
        "inglese il nome del driver — e il lato giapponese non si traduce per "
        "costruzione, quindi `siti()` non lo copre e non deve coprirlo. "
        "L'inglese, «Direct sound», sta gia' nel dizionario."),
    "map_rand.hsp": Dichiarazione(
        "esente", 1,
        "`if ( ... == \"hobbit caves\" )` (:273): operando di confronto sul "
        "nome interno di un tipo di nefia, non testo a schermo."),
    "chat.hsp": Dichiarazione(
        "esente", 1,
        "Un solo `proc \"cnpc event start\"` (:952), traccia di debug, in un "
        "file che per il resto e' coperto da 4.328 stringhe raggiunte."),
    "event.hsp": Dichiarazione(
        "esente", 1,
        "Un solo `proc \"Random event\"` (:2), traccia di debug del generatore "
        "di eventi casuali. Il resto del file — 693 stringhe — lo raggiunge il "
        "dizionario: e' l'unica riga che gli sfugge."),
    "net.hsp": Dichiarazione(
        "esente", 1,
        "`sockput \" HTTP/1.0\\nHost:???\\nUser-Agent: HSP ver3.0\\n\\n\"` "
        "(:94): e' la richiesta HTTP che il gioco manda in rete. Non e' "
        "testo, e' protocollo."),
}

# ⚠️ Il debito misurato e non guardato. Alla 135a e' stato svuotato: ogni file
# con stringhe scoperte ha ora una Dichiarazione con scritto perche'. Resta qui
# perche' e' la casella giusta dove mettere un file nuovo mentre lo si misura,
# PRIMA di averlo guardato una stringa per volta — e perche' il cancello lo
# tratta come una dichiarazione debole, che tiene il conto e non pretende una
# ragione. Una riga qui NON vuol dire «va bene cosi'»: vuol dire «misurato,
# mai guardato».
DA_TRIARE: dict[str, int] = {}


def letterali_di_prosa(testo: str, righe_morte: set[int] | None = None) -> list[str]:
    """I letterali del file che somigliano a una frase, righe morte escluse.

    `righe_morte` sono le righe dentro un `/* */`, che le chiama chi ha il
    percorso del file (`commenti.righe_in_commento()` legge dal disco).
    """
    fuori = []
    morte = righe_morte or set()
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte:
            continue
        spoglia = riga.lstrip()
        # In HSP il commento e' `;` **oppure** `//`. Guardare solo il `;` e' il
        # guasto che le rinviate chiamano «la quarta volta»: `tcg.hsp:1505` e'
        # una `lang()` spenta da `//` che una rete ha contato come viva.
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        for trovato in _LETTERALE.finditer(riga):
            if _PROSA.search(trovato.group(1)):
                fuori.append(trovato.group(1))
    return fuori


def _righe_con_toppa() -> dict[str, set[str]]:
    per_file: dict[str, set[str]] = defaultdict(set)
    for riga in (percorsi.PROGETTO / "toppe.jsonl").read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        toppa = json.loads(riga)
        cerca = toppa["cerca"]
        # `cerca` e' quasi sempre una riga sola; alcune toppe ne portano un
        # elenco, perche' riscrivono un blocco
        pezzi = cerca if isinstance(cerca, list) else [cerca]
        per_file[toppa["file"]].update(p.strip() for p in pezzi)
    return per_file


def rese_da_meccanismo() -> dict[str, set[str]]:
    """I letterali che un meccanismo proprio del progetto copre gia'.

    ⚠️ `MECCANISMI` marca un file INTERO come coperto, e per `scene2.hsp` e
    `tcg_mod.hsp` va bene: li' la catena prende tutto. `tcg_skill.hsp` no --
    `schede.py` ne copre le 70 schede di carta e non le battute, le
    `randomchat` e le tracce. Senza questo, `copertura` continuerebbe a
    contare come scoperte settantadue stringhe **gia' tradotte**, cioe' a
    dire che manca del lavoro che c'e'.

    ⚠️⚠️ Di `dialoghi.py` entrano anche le **invariate**, e le schede non ne
    hanno: una battuta come `"AIEEE!!!"` e' stata **decisa** — sta in
    `invariati.md` con la sua ragione — e contarla ancora fra le scoperte
    vorrebbe dire chiedere per sempre un lavoro che non c'e'. E' la stessa
    regola che `verifica.py` applica leggendo `invariati.md`.
    """
    from strumenti import dialoghi, schede

    fuori: dict[str, set[str]] = defaultdict(set)
    for chiave, voce in schede.carica_dizionario().items():
        if voce.get("it"):
            fuori[voce["file"]].add(chiave)
    diz_dialoghi = dialoghi.carica_dizionario()
    for chiave in dialoghi.decise(diz_dialoghi):
        for sito in diz_dialoghi[chiave].get("siti", []):
            fuori[sito["file"]].add(chiave)
    return fuori


def scoperte_di(nome_file: str, testo: str, toppe: set[str],
                righe_morte: set[int] | None = None,
                rese: set[str] | None = None) -> list[str]:
    """Le stringhe di prosa che non raggiunge ne' il dizionario ne' una toppa.

    Il dizionario si consulta attraverso `estrai.siti()`, che e' l'unica
    scansione del sorgente del progetto: cosi' questo modulo e `applica`
    camminano sugli stessi siti per costruzione e non per disciplina.

    ⚠️ `righe_morte` sono le righe dentro un commento di blocco `/* */`, che
    `commenti.righe_in_commento()` sa trovare e che questo modulo NON sapeva
    saltare. Il caso vero: `custom_tweaks.hsp` apre con un `/*` a riga 1 e lo
    chiude a riga 85, e in mezzo tiene l'elenco documentativo delle 75 voci
    del menu Tweaks. Erano **tutte e 75** le «stringhe scoperte» del file, e
    per mezz'ora sono state il secondo fronte piu' grosso del progetto.
    """
    span_per_riga: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for sito in siti(testo):
        span_per_riga[sito[0]].append((sito[7], sito[8]))
    morte = righe_morte or set()

    scoperte = []
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte:
            continue
        spoglia = riga.lstrip()
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        for trovato in _LETTERALE.finditer(riga):
            if not _PROSA.search(trovato.group(1)):
                continue
            if trovato.group(1) in (rese or set()):
                continue
            dentro_lang = any(inizio <= trovato.start(1) and trovato.end(1) <= fine
                              for inizio, fine in span_per_riga.get(numero, []))
            if not dentro_lang and riga.strip() not in toppe:
                scoperte.append(trovato.group(1))
    return scoperte


def censimento() -> list[dict]:
    """Una riga per ogni `.hsp` del sorgente che ha stringhe scoperte."""
    toppe = _righe_con_toppa()
    rese = rese_da_meccanismo()
    righe = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        prosa = letterali_di_prosa(testo, morte)
        if not prosa:
            continue
        scoperte = scoperte_di(percorso.name, testo,
                               toppe.get(percorso.name, set()), morte,
                               rese.get(percorso.name, set()))
        righe.append({
            "file": percorso.name,
            "prosa": len(prosa),
            "scoperte": len(scoperte),
            "distinte": len(set(scoperte)),
            "campioni": sorted(set(scoperte))[:3],
        })
    return righe


def _dichiarazione(nome: str) -> Dichiarazione | None:
    if nome in DICHIARATI:
        return DICHIARATI[nome]
    if nome in DA_TRIARE:
        return Dichiarazione("da_triare", DA_TRIARE[nome],
                             "misurato alla 135a, mai guardato una stringa per volta")
    return None


def problemi(righe: list[dict] | None = None) -> list[str]:
    """Le tre cose che accendono il cancello. Lista vuota = tutto dichiarato."""
    if righe is None:
        righe = censimento()
    per_nome = {r["file"]: r for r in righe}
    guai = []

    for riga in righe:
        nome = riga["file"]
        if nome in MECCANISMI or riga["distinte"] == 0:
            continue
        dichiarata = _dichiarazione(nome)
        if dichiarata is None:
            guai.append(
                f"{nome}: {riga['distinte']} stringhe inglesi distinte che non "
                f"raggiunge ne' il dizionario ne' una toppa, e nessuna "
                f"dichiarazione in copertura.py. "
                f"Esempio: {riga['campioni'][0][:60]!r}")
        elif dichiarata.scoperte != riga["distinte"]:
            guai.append(
                f"{nome}: dichiarate {dichiarata.scoperte} stringhe scoperte, "
                f"nel sorgente ne sono {riga['distinte']}. Il monte si e' mosso "
                f"sotto la dichiarazione, oppure il conto era sbagliato.")

    # Una dichiarazione che non serve piu' e' peggio di nessuna dichiarazione:
    # dice che un fronte e' aperto quando e' stato chiuso.
    #
    # ⚠️ Le due condizioni sono diverse e servono tutt'e due. Il file puo'
    # sparire dal censimento (nessuna prosa) **oppure** restarci con zero
    # stringhe scoperte, che e' il caso normale quando un fronte viene
    # lavorato: `custom_lib.hsp` alla 135a, dopo la sua toppa, aveva ancora due
    # letterali di prosa e nessuno dei due scoperto. La prima versione di
    # questo ciclo guardava solo `is None` e lo lasciava passare.
    for nome in list(DICHIARATI) + list(DA_TRIARE):
        riga = per_nome.get(nome)
        if riga is None or riga["distinte"] == 0:
            guai.append(f"{nome}: dichiarato in copertura.py ma nel sorgente "
                        f"non ha piu' nessuna stringa scoperta. La riga va tolta.")
    for nome in MECCANISMI:
        if not (percorsi.SORGENTE_HSP / nome).exists():
            guai.append(f"{nome}: sta in MECCANISMI ma non esiste nel sorgente.")
    return guai


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Il testo inglese che non raggiunge nessuno. Cancello + referto.")
    analizzatore.add_argument(
        "--referto", action="store_true",
        help="stampa il censimento completo invece del solo cancello")
    argomenti = analizzatore.parse_args()

    righe = censimento()

    if argomenti.referto:
        print(f"  {'file':<28} {'prosa':>6} {'scoperte':>9} {'distinte':>9}  stato")
        print("  " + "-" * 74)
        for riga in sorted(righe, key=lambda r: -r["distinte"]):
            if riga["file"] in MECCANISMI:
                stato = "meccanismo proprio"
            elif riga["distinte"] == 0:
                stato = "coperto"
            else:
                dichiarata = _dichiarazione(riga["file"])
                stato = f"** {dichiarata.tipo.upper()}" if dichiarata else "** SCOPERTO"
            print(f"  {riga['file']:<28} {riga['prosa']:>6} {riga['scoperte']:>9} "
                  f"{riga['distinte']:>9}  {stato}")

        fronti = {n: d for n, d in DICHIARATI.items() if d.tipo == "fronte"}
        print(f"\n  fronti dichiarati e non lavorati: {len(fronti)}, "
              f"{sum(d.scoperte for d in fronti.values())} stringhe SCOPERTE")
        print("  ⚠️ «scoperte» non vuol dire «da tradurre»: nei file misti il "
              "conto include\n     le tracce di debug e gli operandi di "
              "confronto, che restano inglesi.\n     Quanto sia testo davvero "
              "sta scritto nel motivo di ciascuno.")
        for nome, d in sorted(fronti.items(), key=lambda kv: -kv[1].scoperte):
            print(f"      {d.scoperte:>5}  {nome}")
        print(f"  debito misurato e non triato: {len(DA_TRIARE)} file, "
              f"{sum(DA_TRIARE.values())} stringhe distinte")

    guai = problemi(righe)
    if not guai:
        print(f"\n  copertura: nessun file scoperto e non dichiarato")
        return
    print()
    for guaio in guai:
        print(f"  ⚠️ {guaio}")
    raise SystemExit(f"{len(guai)} problemi di copertura")


if __name__ == "__main__":
    main()
