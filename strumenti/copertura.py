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
    "tcg_mod.hsp": Dichiarazione(
        "fronte", 809,
        "IL FRONTE PIU' GROSSO TROVATO DALLA 135a. 813 delle 820 stringhe sono "
        "`effdesc@tcg(...)`, cioe' il testo dell'effetto di ogni carta, "
        "disegnato da `cardhelp effdesc@tcg(eff@tcg), 10` (`tcg.hsp:3935` e "
        "`:4170`) e ricomposto in `\"Effect: \" + effdesc@tcg(...)` a "
        "`tcg.hsp:1473`. Le altre 6 sono `efftalk@tcg`, battute. Il file HA un "
        "dizionario, di **8** voci, e una toppa: e' quello che lo faceva "
        "sembrare coperto."),
    "tcg_skill.hsp": Dichiarazione(
        "fronte", 142,
        "L'ALTRA META' DEL GIOCO DI CARTE. 7.686 righe, `#include` da "
        "`tcg.hsp:3`, zero byte non-ASCII: non c'e' nessun ramo giapponese, "
        "l'inglese e' cablato e il giocatore lo legge qualunque lingua scelga. "
        "76 schede di carta (`carddetailneff@tcg(...)`, disegnate da `cardhelp` "
        "a `tcg.hsp:691`), 35 battute (`efllistaddchat`, `cnvtalk`), 17 "
        "`randomchat@tcg`, 2 `markerwords`. ⚠️ Tre `instr(carddetailneff@tcg"
        "(...), 0, \"ragon\")` (`:4960`, `:4972`, `:5003`) CERCANO dentro il "
        "testo della carta: la resa di «dragon» deve contenere «ragon» — "
        "«dragone» va, «drago» no."),

    # ---- fronti piccoli, triati alla 135a ---------------------------------
    "map_func.hsp": Dichiarazione(
        "fronte", 13,
        "L'editor di mappe: menu Win32 (`AppendMenuA ... \"Map Mode\"`, "
        ":1921-:1933), un `dialog` di conferma (:1857), la sua guida (:1896), "
        "la casella `chkbox \"Auto Coast\"` (:2513) e il filtro a tendina delle "
        "categorie (:2517). E' testo a schermo, ma di un'altra specie dal resto "
        "del gioco — widget del sistema operativo, non finestre di Elona — e "
        "le larghezze le decide Windows, non le reti del progetto."),
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
        "fronte", 52,
        "IL TERZO PEZZO DEL GIOCO DI CARTE, in un file che ha gia' 102 toppe e "
        "un dizionario: e' il contorno a essere stato lavorato, non le carte. "
        "Le 26 righe `if` di :1568-:1605 sono le ETICHETTE che si appendono al "
        "testo della carta — `[Command Card]`, `[Illegal Card]`, `<Mage "
        "Guild>` — e le cinque di :3348-:3352 sono il menu «Sort by:». "
        "Aggiungi tre `carddetailneff@tcg`, tre `efllistaddchat` e i "
        "segnaposto delle schede (:4632-:4658, «race dependent», «[Random "
        "AKA] [Random Name]»). ⚠️ Restano fuori 10 `proctcg`, che sono tracce "
        "di debug. Vanno lavorate INSIEME a `tcg_mod` e `tcg_skill`: le "
        "etichette entrano nella stessa stringa delle schede."),
    "tcg_custom.hsp": Dichiarazione(
        "fronte", 4,
        "Tre tracce di debug (`proc`, `proctcg`, `poptext@tcg`) e una cosa "
        "che al fronte TCG appartiene davvero: `sreplace ..., \"the The\"` "
        "(:4566), cioe' la pezza che l'inglese mette per non scrivere «the "
        "The» quando compone un nome di carta. In italiano quella pezza o "
        "cambia o sparisce, e la decisione si prende con le carte in mano."),

    # ---- fronti veri, piccoli, trovati dal triage della 135a ---------------
    "buff.hsp": Dichiarazione(
        "fronte", 48,
        "I TESTI DEI BUFF, e sono un costrutto SPEZZATO A META' dal dizionario. "
        "La forma e' `bufftxt(0, BUFF_X) = lang(jp, \" get\"), \" surrounded "
        "by a hazy mist.\"`: l'assegnazione riempie DUE celle dell'array, la "
        "prima con una `lang()` — che il dizionario prende — e la seconda con "
        "il resto della frase, nudo. Il giapponese tiene tutto nella prima. "
        "Li ricompone `chara_func.hsp:2310` e `:2377`. Quindi il file risulta "
        "coperto per il verbo e scoperto per la frase, e le 48 sono tutte "
        "testo che il giocatore legge a ogni buff."),
    "system.hsp": Dichiarazione(
        "fronte", 83,
        "MISTO, e la parte grossa NON e' testo: 54 `noteadd` e 11 `proc` sono "
        "la CONSOLE DI DEBUG, che si annuncia da sola a :4400 («Debug Console  "
        "Type \\\"?\\\" for help»). Il testo vero e' il resto: 11 `dialog` "
        "(«The name is too long.», «The first letter of the name must be "
        "alphabetic.», :1924-:1934, quando si crea un oggetto o un PNG "
        "personalizzato), il menu di :3537 («Restore an adventurer», "
        "«Generate an adventurer», «Incarnate an adventurer», «View the "
        "homepage»), un `mes` a :3521 e 4 `filedsc`, che sono le descrizioni "
        "nelle finestre Apri/Salva di Windows. ⚠️ `%Elona Custom Item` (:1869) "
        "e `%Elona Custom Npc` (:1972) NON si toccano: sono la firma dei file "
        "che il gioco scrive e rilegge."),
    "command.hsp": Dichiarazione(
        "fronte", 16,
        "MISTO, e qui la parte da NON tradurre e' la piu' insidiosa: le 7 "
        "righe `if` di :4481-:4763 confrontano quel che il giocatore ha "
        "scritto o il nome di un oggetto — «god inside», «dog whistle», «happy "
        "new year», «merry christmas» — e sono innesti di uova di Pasqua. "
        "Tradurle senza tradurre l'altro capo del confronto spegne l'evento in "
        "silenzio. Il testo vero e': `display_topic \"Level(Piety Cost)\"` "
        "(:7625, un'intestazione a schermo), due `dialog` a :13240, due "
        "`description` a :16039-:16041, due `filedsc` e un `noteadd`."),
    "main.hsp": Dichiarazione(
        "fronte", 8,
        "Sette `dialog` e una stringa di versione. I `dialog` sono i messaggi "
        "d'avvio e di caricamento: «Could not find an installation of Elona+. "
        "Please follow the install instructions…» (:61), e soprattutto "
        "«Perform a quickload? You are playing in a mode where no-save "
        "penalties apply.» (:3176) e «Perform a quickload?» (:3178), che un "
        "giocatore vede spesso. ⚠️ `ElonaPlus Custom-GX 2.31.1.0` (:21) e' la "
        "versione: non si tocca."),
    "custom_ai.hsp": Dichiarazione(
        "fronte", 8,
        "Il menu dell'IA dei famigli: quattro `ActionName` («Throw Salt», "
        "«Throw Greater Potion», «Throw Major Potion», «Throw Potion», "
        ":3077-:3086) che si leggono nella lista delle azioni, un `ValueName` "
        "(«Not Set», :3214), un `dialog` di conferma («Re-Initialize this "
        "pet's spells and abilities?», :1663) e due `filedsc`. ⚠️ `\"not "
        "set\"` a :71 sta in un `if`: e' l'operando, e va lasciato."),
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
        "fronte", 8,
        "Tre `gain_ap` che sono testo a schermo (« of your mount», « "
        "tag-team partner», « of your minion», :8536-:8546, la coda della "
        "frase che dice a chi vanno i punti), tre `title` che scrivono nella "
        "barra della finestra un messaggio diagnostico, un `proc`. ⚠️ E "
        "`:8640` e' un caso a se': un `txt` in GIAPPONESE nudo "
        "(«[SURVIVABILITY EXTENSION！]　フェイズ1が完了した…»), cioe' testo che "
        "l'inglese non ha mai tradotto. Vedi il gemello in `item.hsp:4324`."),
    "action.hsp": Dichiarazione(
        "fronte", 11,
        "Dieci `proc` sono tracce di debug del regalo di capodanno "
        "(:3809-:3959). L'undicesima e' testo: `txt \"Potion-charge Lv\"` "
        "(:6545), che il giocatore legge sulla pozione. Ha un gemello esatto "
        "in `proc.hsp:13471`, e le due rese devono coincidere."),
    "proc.hsp": Dichiarazione(
        "fronte", 3,
        "`txt \"Potion-charge Lv\"` (:13471), gemello di `action.hsp:6545`; "
        "`studybuddy \"your friends\"` (:16980); e `txt \"Omae wa mou "
        "shindeiru.\"` (:14392), che e' una citazione e va lasciata com'e' — "
        "ma la decisione va scritta, non lasciata all'inerzia."),
    "screen.hsp": Dichiarazione(
        "fronte", 3,
        "Un `dialog` che il giocatore puo' vedere davvero all'avvio "
        "(«Invalid screen resolution detected. Custom-GX will attempt to reset "
        "to a sane default.», :22) e due `title` diagnostici a :8288, che "
        "scrivono nella barra della finestra."),
    "db_creature.hsp": Dichiarazione(
        "fronte", 4,
        "Quattro grida di battaglia dei boss, nude fuori da `lang()` in un "
        "file che ne ha 5.718: 「Last Danceが最後の行程に入った」 (:51263), "
        "「HAPPY END！！」 (:53276), 「Target Acquired.」 e 「Resistance is "
        "futile!」 (:99788). Le prime due sono giapponesi anche nel ramo "
        "inglese; le altre due sono inglesi in tutt'e due i rami. Sono le "
        "quattro righe di questo file che il dizionario non puo' vedere."),
    "trait.hsp": Dichiarazione(
        "fronte", 2,
        "Un solo messaggio, spezzato in due letterali attorno al numero: "
        "`\"This is an UNKNOWN_TRAIT[\" + ... + \"], report it.\"` (:1268). "
        "Lo legge il giocatore nella lista dei tratti quando il gioco ne "
        "incontra uno che non conosce, ed e' un invito a segnalare: la resa "
        "italiana deve restare riconoscibile a chi riceve la segnalazione."),
    "help.hsp": Dichiarazione(
        "fronte", 2,
        "`dialog \"help index not found \"` (:230) e — piu' interessante — "
        "`s \"広域能力を使う(Wide apply)\"` (:409), una voce di menu che porta "
        "il giapponese e l'inglese INSIEME nella stessa stringa, fuori da "
        "`lang()`. Il dizionario non puo' prenderla, e in italiano va decisa "
        "come una voce sola."),
    "item.hsp": Dichiarazione(
        "fronte", 1,
        "`txt \"[HAPPY BIRTHDAY！！]　フェイズ2が完了した。\"` (:4324): "
        "giapponese nudo che il ramo inglese non ha mai tradotto. Gemello di "
        "`chara_func.hsp:8640`, e le due rese vanno decise insieme perche' "
        "sono le due fasi della stessa catena."),
    "db_card.hsp": Dichiarazione(
        "fronte", 1,
        "`cardrefskill` a :2695: una descrizione di carta lunga, in "
        "giapponese, nuda fuori da `lang()` in un file che ne ha 2.326. "
        "Appartiene al fronte TCG per contenuto, a `db_card` per posizione."),
    "text.hsp": Dichiarazione(
        "fronte", 2,
        "`sg \"Unknown Code\"` (:9351), che il giocatore puo' leggere quando "
        "il gioco incontra un codice che non conosce, e un `proc \"god text\"` "
        "(:12150) che e' una traccia di debug."),

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


def scoperte_di(nome_file: str, testo: str, toppe: set[str],
                righe_morte: set[int] | None = None) -> list[str]:
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
            dentro_lang = any(inizio <= trovato.start(1) and trovato.end(1) <= fine
                              for inizio, fine in span_per_riga.get(numero, []))
            if not dentro_lang and riga.strip() not in toppe:
                scoperte.append(trovato.group(1))
    return scoperte


def censimento() -> list[dict]:
    """Una riga per ogni `.hsp` del sorgente che ha stringhe scoperte."""
    toppe = _righe_con_toppa()
    righe = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        prosa = letterali_di_prosa(testo, morte)
        if not prosa:
            continue
        scoperte = scoperte_di(percorso.name, testo,
                               toppe.get(percorso.name, set()), morte)
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
