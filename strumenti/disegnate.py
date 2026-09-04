"""La rete che parte da CHI DISEGNA, su tutto il sorgente.

⚠️⚠️ **Perche' esiste.** `copertura._PROSA` cerca «due parole alfabetiche
separate da uno spazio», cioe' riconosce la **prosa**. Ma un'interfaccia e'
fatta di **etichette**, e un'etichetta di solito e' una parola sola:

    "Regeneration "     una parola sola     -> INVISIBILE a _PROSA
    "Filter: Attack "   due, coi due punti  -> INVISIBILE
    "One!"  "AIEEE!!!"  "Cheapskate."       -> INVISIBILI
    "Sort by: Attack "  due parole vere     -> vista

La 137a ne ha trovate **58 in un file solo** (`tcg.hsp`), a schermo, dentro un
fronte dichiarato e contato — e il conto non le comprendeva. La 138a ne ha
trovate altre **25** fra le battute del gioco di carte. Tutt'e due le volte il
buco e' stato misurato **su un file per volta**, e la domanda vera e' rimasta
aperta: *quante ce ne sono negli altri novanta?*

⭐ **La risposta non puo' venire da un'euristica sulla forma della stringa.**
Allargare `_PROSA` alla parola sola non si puo': in HSP quasi tutti i letterali
di una parola sono identificatori (`"male"`, `"bg3"`, `"ITEM_ID_BANANA"`), e il
referto annegherebbe. Serve partire dall'altra parte: da **chi manda un testo
allo schermo**. Se un letterale finisce dentro `txt`, `mes`, `chatList` o
`cardhelp`, allora e' testo — comunque sia fatto, una parola o venti.

## Che cosa questa rete vede, e che cosa NON vede

Vede i letterali che stanno **sulla riga** di un comando che disegna, fuori da
`lang()`.

⚠️ **NON vede il salto per variabile:** `s = "Fatto."` su una riga e `txt s`
sulla riga dopo. Modellare quel salto vuol dire seguire il flusso dei dati in
HSP, e questa rete non lo fa: e' un limite **dichiarato**, non una svista, e
misurarlo e' il gradino dopo. Per la stessa ragione non e' un cancello che
pretende zero: e' un **censimento** che dice dove guardare.

⚠️ `noteadd` resta fuori dai comandi. Non perche' non disegni — la lista delle
carte e il diario passano di li' — ma perche' scrive anche i **file di dato**
(i mazzi, la configurazione), e un censimento che li mescolasse al testo
direbbe «da tradurre» a righe che tradotte romperebbero un salvataggio. Chi
lo affronta lo fara' con la sua decisione, non dentro questa misura.

## Uso

    python -m strumenti.disegnate              # il censimento, per file
    python -m strumenti.disegnate --file X.hsp # un file solo, riga per riga
    python -m strumenti.disegnate --confronto  # quante ne perde `_PROSA`
"""
import argparse
import re
from collections import defaultdict
from dataclasses import dataclass

from strumenti import copertura, percorsi
from strumenti.commenti import righe_in_commento
from strumenti.estrai import siti

# I comandi che mandano un testo a schermo, e perche'. Una riga qui e' una
# dichiarazione: se il comando non disegna, il censimento gonfia; se manca, il
# censimento tace -- ed e' il modo in cui 58 etichette sono state invisibili
# per centotrentasei sessioni.
COMANDI = {
    "txt": "il registro dei messaggi in basso: la via principale del testo",
    "txtmore": "il registro, con l'attesa di un tasto",
    "mes": "disegno diretto, comando di HSP",
    "bmes": "`mes` col bordo scuro (custom-gx): nuvolette, schede, numeri",
    "mesbox": "la scatola di testo scorrevole (guida, libri)",
    "HIGHDPI_mesbox": "la stessa, nella versione ad alta risoluzione",
    "chatList": "una voce del menu di dialogo",
    "chatMore": "una battuta del dialogo, con l'attesa",
    "cardhelp": "il riquadro d'aiuto del gioco di carte",
    "dialog": "la finestra di sistema di Windows",
    "objprm": "il testo dentro un controllo Win32 (campo di immissione)",
    "poptext": "il testo che salta fuori sopra una creatura",
}

@dataclass(frozen=True)
class Dichiarazione:
    tipo: str        # "fronte" | "esente"
    scoperte: int    # stringhe DISTINTE disegnate e non coperte
    motivo: str


# ⚠️ Come in `copertura`: o un file e' dichiarato, o il cancello si accende.
# La differenza e' che qui il metro e' «chi disegna», quindi questi numeri NON
# sono quelli di la' e non vanno confrontati riga per riga: `--confronto` dice
# quanto le due reti si scoprono a vicenda.
DICHIARATI: dict[str, Dichiarazione] = {
    "tcg.hsp": Dichiarazione(
        "fronte", 129,
        "⭐⭐ IL RITROVAMENTO DELLA 138ª, e il fronte piu' grosso che resta nel "
        "gioco di carte: il **menu dei filtri dell'editor di mazzo** "
        "(`cfname@tcg`, `:3552-:3632`). Sono 126 etichette a schermo — «All», "
        "«Blue», «Cost 0», «1 HP», «2 Atk», e l'elenco intero di razze e "
        "classi — che NESSUN censimento ha mai contato: `_PROSA` pretende due "
        "parole alfabetiche e queste ne hanno una. "
        "⚠️ Vanno guardate a schermo prima di tradurle: stanno negli stessi "
        "slot a larghezza fissa degli 8 «Filter:» del lotto B2, e l'italiano "
        "e' piu' lungo. ⚠️ E le razze/classi vanno decise **insieme** ai nomi "
        "che il progetto usa altrove (`db_class.hsp`, `db_race.hsp`), o il "
        "filtro chiamerebbe «dragon» quel che la carta chiama «drago». "
        "ⓘ Dentro il 129 ci sono anche 3 sparsi dello stesso file, che col "
        "menu non c'entrano: `bmes \"Immune\"` (`:969`), `mes \"Mana \"` "
        "(`:3480`) e un `\"Effect: \"` appeso a `s@tcg` (`:1610`). 126 + 3."),
    "action.hsp": Dichiarazione(
        "fronte", 12,
        "Le dodici classi che il comando dei desideri **scrive dentro il nome "
        "della creatura** (`cdatan(CDATAN_CLASS, tc) = \"warrior\"`, "
        "`:13670-:13703`). ⚠️ Sulla stessa riga c'e' l'OPERANDO — `if "
        "inputlog == \"warrior\"` — che e' quel che il giocatore digita e "
        "**non si tocca**: e' la trappola di `module.hsp`, dove otto "
        "`cnv_str` tolgono prefissi inglesi da quel che il giocatore scrive. "
        "La resa deve essere quella di `db_class.hsp`, non una nuova."),
    "command.hsp": Dichiarazione(
        "fronte", 2,
        "✅ `\"Dv:\"` e `\" Pv:\"` (`:14191`, `:14205`) sono uscite di qui "
        "nella 138ª: erano gia' decise dal glossario, e quel che mancava era "
        "la riga in `invariati.md` — che ora c'e'. Restano `\",Tab \"` "
        "(`:14077`, il suggerimento di tasto, che compare uguale in "
        "`module.hsp` e va deciso una volta per tutt'e due) e `\"d\"`, che "
        "non e' testo: e' la «d» dei dadi (`3d5`)."),
    "screen.hsp": Dichiarazione(
        "esente", 3,
        "✅ `\"Sp\"` (`:417`) e' uscita di qui nella 138ª, dentro "
        "`invariati.md` insieme alle altre sigle del glossario. Restano "
        "`\"Lv\"` (`:423`), che NON e' esente ma va deciso insieme al "
        "` liv.` del dizionario e al `lv:` di `main.hsp` — oggi il progetto "
        "ne ha tre grafie — e `\"*debug*\"` e `\"loop\"` (`:1125`, `:1128`), "
        "che escono solo col debug acceso."),
    "system.hsp": Dichiarazione(
        "esente", 3,
        "Tre finestre d'errore del sistema: «invalid version», «Failed to get "
        "WINDOW ID», «Failed to get OBJECT ID». Le legge chi installa male il "
        "gioco o chi lo sviluppa, e nominano oggetti di Windows. Sono la "
        "stessa famiglia dei comandi MCI di `sound.hsp`."),
    "net.hsp": Dichiarazione(
        "esente", 2,
        "«OPEN '» e «SERVER » dentro `dialog`: sono il diario della "
        "connessione di rete, non testo di gioco. Il file e' gia' esente in "
        "`copertura` per la stessa ragione."),
    "main.hsp": Dichiarazione(
        "fronte", 2,
        "«Invalid defLoadFolder. name» e' un errore di sviluppo (esente per "
        "la stessa ragione di `system.hsp`). «lv:» (`:3258`) invece e' a "
        "schermo, ed e' l'unica del gruppo che vada decisa insieme al «Lv» "
        "della barra e al « liv.» che il dizionario usa in `command.hsp`: "
        "**oggi il progetto ne ha due grafie**, e questa e' la terza."),
    # ✅ `proc.hsp` NON sta piu' qui: la sua unica stringa — «Omae wa mou
    # shindeiru.», la citazione di Ken il guerriero — e' entrata in
    # `invariati.md` nella 138ª, e la riga di dichiarazione va tolta INSIEME al
    # lavoro. Lasciarla direbbe aperto un fronte che e' chiuso: e' la lezione
    # che alla 136ª e' costata un referto sbagliato di 800 stringhe.
    "etc.hsp": Dichiarazione(
        "esente", 2,
        "«Jo» (`:95`) e' la sigla del **Jolly** sulla carta da poker, e «X » "
        "(`:127`) e' il segno di moltiplicazione davanti al numero di carte "
        "nella pila. Nessuno dei due e' una parola."),
    "config.hsp": Dichiarazione(
        "esente", 1,
        "«%.1f» e' un formato di `strf`, non testo."),
    "module.hsp": Dichiarazione(
        "fronte", 1,
        "«,Tab » (`:5195`), il suggerimento di tasto che compare uguale in "
        "`command.hsp:14077`. Va deciso una volta per tutt'e due: «Tab» e' il "
        "nome del tasto sulla tastiera e non si traduce, ma la virgola e lo "
        "spazio sono la cornice di un elenco di tasti."),
    "helloworld.hsp": Dichiarazione(
        "esente", 1,
        "File di prova di HSP, 6 righe, che nessuno `#include`: non entra "
        "nell'eseguibile. Gia' esente in `copertura` per la stessa ragione."),
}


_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
_COMANDO = re.compile(r"(?:^|[\s{:])(%s)\s+(?=[^\s=])"
                      % "|".join(sorted(COMANDI, key=len, reverse=True)))

# Un letterale che non e' testo per costruzione: e' una chiave, un formato, un
# separatore. Restano fuori dal censimento senza bisogno di una riga per uno.
_NON_TESTO = re.compile(r"^[\s\\ntr]*$|^[A-Z_][A-Z_0-9]*$|^%[a-z0-9]*$")

# ⚠️⚠️ Il RAMO GIAPPONESE non e' lavoro che manca: e' l'altra meta' di ogni
# `lang()`, e il progetto traduce l'inglese. Gli span che `estrai.siti()`
# restituisce coprono il letterale **inglese**, non la chiamata intera, quindi
# senza questo filtro il censimento conterebbe come «scoperta» ogni stringa
# giapponese del gioco -- e il primo giro ne ha contate undicimila.
#
# Il sorgente e' CP932: un letterale con un byte fuori dall'ASCII e' giapponese
# (l'inglese di monte e l'italiano del progetto stanno tutt'e due in ASCII, che
# e' la ragione per cui `accenti.degrada` esiste).
def _giapponese(letterale: str) -> bool:
    return any(ord(c) > 127 for c in letterale)


# Senza nemmeno una lettera non c'e' niente da tradurre: sono cornici,
# separatori e numeri (`" ("`, `"/"`, `" - "`). ⚠️ NON e' la regola delle
# «due parole» di `_PROSA` travestita: `"One!"` e `"Cheapskate."` la passano,
# ed e' tutta la differenza.
_SENZA_LETTERE = re.compile(r"^[^A-Za-z]*$")


def _viva(riga: str) -> bool:
    spoglia = riga.lstrip()
    return not (spoglia.startswith(";") or spoglia.startswith("//")
                or spoglia.startswith("#"))


def _spazio_lang(testo: str) -> tuple[dict[int, list[tuple[int, int]]],
                                      dict[int, set[str]]]:
    """Per ogni riga: gli span dell'inglese, e i letterali del GIAPPONESE.

    ⚠️⚠️ `estrai.siti()` da' lo span del solo letterale **inglese**, perche' e'
    quello che il dizionario riscrive. Il giapponese resta fuori, e di solito
    si riconosce da se' — ha byte fuori dall'ASCII. Ma non sempre:
    `chat.hsp:6711` e' `lang("Yes", "Yes.")`, con il ramo giapponese scritto in
    lettere latine. Senza questa seconda mappa il censimento chiamerebbe
    «scoperta» la meta' giapponese di una riga tradotta — cioe' direbbe che
    manca del lavoro che c'e'.
    """
    span: dict[int, list[tuple[int, int]]] = defaultdict(list)
    giapponesi: dict[int, set[str]] = defaultdict(set)
    for sito in siti(testo):
        span[sito[0]].append((sito[7], sito[8]))
        giapponesi[sito[0]].update(_LETTERALE.findall(sito[4] or ""))
    return span, giapponesi


def disegnate_di(nome: str, testo: str,
                 morte: set[int] | None = None) -> list[tuple[int, str, str]]:
    """(riga, comando, letterale) per ogni testo che finisce a schermo.

    Comprende quelli gia' coperti: chi chiama sottrae quel che vuole. Tenerli
    dentro qui e' voluto — il totale «quanto testo disegna questo file» e' una
    misura utile per conto suo, e il numero che si sottrae si vede.
    """
    morte = morte or set()
    span_lang, giapponesi = _spazio_lang(testo)

    fuori = []
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte or not _viva(riga):
            continue
        for trovato in _COMANDO.finditer(riga):
            comando = trovato.group(1)
            coda_da = trovato.end()
            for letterale in _LETTERALE.finditer(riga, coda_da):
                dentro_lang = any(
                    inizio <= letterale.start(1) and letterale.end(1) <= fine
                    for inizio, fine in span_lang.get(numero, []))
                if dentro_lang:
                    continue
                testo_del_letterale = letterale.group(1)
                if (_NON_TESTO.match(testo_del_letterale)
                        or _giapponese(testo_del_letterale)
                        or _SENZA_LETTERE.match(testo_del_letterale)
                        or testo_del_letterale in giapponesi.get(numero, set())):
                    continue
                fuori.append((numero, comando, letterale.group(1)))
    return fuori


# Il nome di una variabile HSP, con o senza modulo (`s`, `s@tcg`, `buff`).
_NOME = r"[A-Za-z_][A-Za-z0-9_]*(?:@[A-Za-z0-9_]+)?"
_ARGOMENTO = re.compile(r"^(%s)\s*(?:\([^)]*\))?\s*(?:$|[,)+\s])" % _NOME)
_ASSEGNAZIONE = re.compile(r"^\s*(%s)\s*(?:\([^)]*\))?\s*\+?=\s*(.*)$" % _NOME)

# ⚠️ Variabili che portano di tutto, e che come chiave direbbero «tradotto» a
# meta' del gioco: sono i nomi generici che il sorgente riusa per i numeri, i
# percorsi e i pezzi di salvataggio. Restano fuori dal SALTO (livello 1), non
# dal livello 0: li' il letterale sta sulla riga che disegna e si vede da se'.
_TROPPO_GENERICHE = {"s", "buff", "txt", "p", "q", "a", "b", "c", "n", "t",
                     "x", "y", "z", "i", "j", "k", "tmp", "temp", "str",
                     "name", "sql", "line", "lines", "notebuf", "mes"}


def variabili_disegnate(testo: str, morte: set[int] | None = None) -> set[str]:
    """I nomi che qualcuno passa a un comando che disegna.

    ⭐ E' il gradino che mancava. Le 58 etichette della 137a non stavano sulla
    riga di `mes`: stavano in `s@tcg += "[Command Card] "`, e `s@tcg` finiva a
    schermo venti righe piu' giu'. Una rete che guardi solo la riga del
    comando non le vede — ed e' quello che il primo giro di questo modulo ha
    fatto vedere, contandone 34 in tutto il sorgente.
    """
    morte = morte or set()
    fuori = set()
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte or not _viva(riga):
            continue
        for trovato in _COMANDO.finditer(riga):
            coda = riga[trovato.end():].lstrip()
            nome = _ARGOMENTO.match(coda)
            if nome and nome.group(1) not in _TROPPO_GENERICHE:
                fuori.add(nome.group(1))
    return fuori


def per_variabile(testo: str, nomi: set[str],
                  morte: set[int] | None = None) -> list[tuple[int, str, str]]:
    """(riga, variabile, letterale): il testo che arriva a schermo di rimbalzo.

    ⚠️ Sono i letterali **assegnati o appesi** a una variabile che qualcuno
    disegna. Non e' un'analisi del flusso dei dati: e' un salto solo, e nello
    stesso file. Basta per il caso che ci e' costato due volte — l'etichetta
    composta a pezzi — e non basta per tutto.
    """
    morte = morte or set()
    span_lang, giapponesi = _spazio_lang(testo)

    fuori = []
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte or not _viva(riga):
            continue
        trovato = _ASSEGNAZIONE.match(riga)
        if trovato is None or trovato.group(1) not in nomi:
            continue
        for letterale in _LETTERALE.finditer(riga, trovato.start(2)):
            testo_del_letterale = letterale.group(1)
            dentro_lang = any(
                inizio <= letterale.start(1) and letterale.end(1) <= fine
                for inizio, fine in span_lang.get(numero, []))
            if (dentro_lang or _NON_TESTO.match(testo_del_letterale)
                    or _giapponese(testo_del_letterale)
                    or _SENZA_LETTERE.match(testo_del_letterale)
                    or testo_del_letterale in giapponesi.get(numero, set())):
                continue
            fuori.append((numero, trovato.group(1), testo_del_letterale))
    return fuori


def tutte_di(nome: str, testo: str,
             morte: set[int] | None = None) -> list[tuple[int, str, str]]:
    """I due livelli insieme: sulla riga che disegna, e di rimbalzo."""
    diretti = disegnate_di(nome, testo, morte)
    nomi = variabili_disegnate(testo, morte)
    return diretti + per_variabile(testo, nomi, morte)


def _rese_note() -> dict[str, set[str]]:
    """Quel che un meccanismo del progetto copre gia', per file."""
    fuori: dict[str, set[str]] = defaultdict(set)
    for nome, chiavi in copertura.rese_da_meccanismo().items():
        fuori[nome] |= chiavi
    return fuori


def _invarianti() -> set[str]:
    """Le stringhe che restano inglesi **per scelta scritta**.

    ⚠️ Un censimento che le contasse fra le scoperte chiederebbe per sempre un
    lavoro gia' deciso, ed e' esattamente il motivo per cui `invariati.md`
    esiste. `Info`, `t `, `Direct sound`, `Qy@`: decise, non dimenticate.
    """
    from strumenti.verifica import carica_invariati

    return set(carica_invariati())


def censimento() -> list[dict]:
    toppe = copertura._righe_con_toppa()
    rese = _rese_note()
    invarianti = _invarianti()
    righe = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        nome = percorso.name
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        tutte = tutte_di(nome, testo, morte)
        if not tutte:
            continue
        righe_del_file = testo.split("\n")
        scoperte = []
        for numero, comando, letterale in tutte:
            if letterale in rese.get(nome, set()) or letterale in invarianti:
                continue
            if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
                continue
            scoperte.append((numero, comando, letterale))
        # ⚠️ `scene2.hsp` e `tcg_mod.hsp` hanno una catena tutta loro che
        # questo modulo non sa leggere: sta scritto in `copertura.MECCANISMI`,
        # e si legge di li' invece di riscriverlo.
        righe.append({
            "file": nome,
            "disegnate": len(tutte),
            "scoperte": 0 if nome in copertura.MECCANISMI else len(scoperte),
            "distinte": 0 if nome in copertura.MECCANISMI
                        else len({s[2] for s in scoperte}),
            "meccanismo": nome in copertura.MECCANISMI,
            "campioni": sorted({s[2] for s in scoperte})[:3],
        })
    return righe


def confronto() -> list[dict]:
    """Quante ne perde `_PROSA`: la domanda che la 137a ha lasciato aperta.

    ⚠️ Sottrae le **stesse** cose del censimento, `invariati.md` compreso: due
    misure della stessa cosa che tolgono liste diverse sono due numeri che non
    si possono confrontare, e la prossima sessione ne troverebbe due e non
    saprebbe quale credere.
    """
    toppe = copertura._righe_con_toppa()
    rese = _rese_note()
    invarianti = _invarianti()
    fuori = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        nome = percorso.name
        if nome in copertura.MECCANISMI:
            continue
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        righe_del_file = testo.split("\n")

        mie = set()
        for numero, _comando, letterale in tutte_di(nome, testo, morte):
            if letterale in rese.get(nome, set()) or letterale in invarianti:
                continue
            if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
                continue
            mie.add(letterale)
        sue = {s for s in copertura.scoperte_di(nome, testo,
                                                toppe.get(nome, set()), morte,
                                                rese.get(nome, set()))
               if s not in invarianti}
        if mie or sue:
            fuori.append({"file": nome, "disegnate": mie, "prosa": sue,
                          "solo_mie": mie - sue, "solo_sue": sue - mie})
    return fuori


def problemi(righe: list[dict] | None = None) -> list[str]:
    """Le tre cose che accendono il cancello. Lista vuota = tutto dichiarato.

    ⚠️ E' lo stesso cancello di `copertura.problemi`, sull'altro metro: un
    censimento senza cancello e' una misura che invecchia. Le 58 etichette
    della 137a e le 25 della 138a sono state trovate a mano tutte e due le
    volte, e il modo di non trovarle una terza e' che il numero si accenda da
    solo quando il sorgente si muove.
    """
    if righe is None:
        righe = censimento()
    per_nome = {r["file"]: r for r in righe}
    guai = []
    for riga in righe:
        nome = riga["file"]
        if riga["meccanismo"] or riga["distinte"] == 0:
            continue
        dichiarata = DICHIARATI.get(nome)
        if dichiarata is None:
            guai.append(
                "%s: %d stringhe disegnate a schermo che non raggiunge ne' il "
                "dizionario ne' una toppa, e nessuna dichiarazione in "
                "disegnate.py. Esempio: %r"
                % (nome, riga["distinte"], riga["campioni"][0][:60]))
        elif dichiarata.scoperte != riga["distinte"]:
            guai.append(
                "%s: dichiarate %d stringhe disegnate e scoperte, nel sorgente "
                "ne sono %d. Il monte si e' mosso sotto la dichiarazione, "
                "oppure il conto era sbagliato."
                % (nome, dichiarata.scoperte, riga["distinte"]))
    for nome in DICHIARATI:
        riga = per_nome.get(nome)
        if riga is None or riga["distinte"] == 0:
            guai.append("%s: dichiarato in disegnate.py ma nel sorgente non ha "
                        "piu' nessuna stringa disegnata e scoperta. La riga va "
                        "tolta." % nome)
    return guai


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--file", metavar="NOME")
    analizzatore.add_argument("--confronto", action="store_true")
    argomenti = analizzatore.parse_args()

    if argomenti.file:
        percorso = percorsi.SORGENTE_HSP / argomenti.file
        testo = percorso.read_bytes().decode("cp932")
        toppe = copertura._righe_con_toppa().get(argomenti.file, set())
        rese = _rese_note().get(argomenti.file, set())
        righe_del_file = testo.split("\n")
        for numero, comando, letterale in tutte_di(
                argomenti.file, testo, righe_in_commento(percorso)):
            stato = "  "
            if letterale in rese:
                stato = "✅"
            elif righe_del_file[numero - 1].strip() in toppe:
                stato = "🩹"
            print("%s %5d  %-10s %r" % (stato, numero, comando, letterale))
        return

    if argomenti.confronto:
        print("  quel che DISEGNA vede e `_PROSA` no, e viceversa\n")
        print("  %-26s %9s %9s %9s %9s" % ("file", "disegna", "prosa",
                                           "solo qui", "solo la'"))
        print("  " + "-" * 68)
        totale_mie = totale_sue = totale_solo = 0
        for riga in sorted(confronto(), key=lambda r: -len(r["solo_mie"])):
            totale_mie += len(riga["disegnate"])
            totale_sue += len(riga["prosa"])
            totale_solo += len(riga["solo_mie"])
            if not (riga["solo_mie"] or riga["solo_sue"]):
                continue
            print("  %-26s %9d %9d %9d %9d"
                  % (riga["file"], len(riga["disegnate"]), len(riga["prosa"]),
                     len(riga["solo_mie"]), len(riga["solo_sue"])))
        print("\n  totale: %d disegnate scoperte, %d viste da `_PROSA`,"
              " **%d invisibili al censimento**"
              % (totale_mie, totale_sue, totale_solo))
        return

    righe = censimento()
    print("  %-26s %10s %10s %10s" % ("file", "disegnate", "scoperte",
                                      "distinte"))
    guai = problemi(righe)
    print("  " + "-" * 62)
    for riga in sorted(righe, key=lambda r: -r["distinte"]):
        if not riga["distinte"]:
            continue
        print("  %-26s %10d %10d %10d   %s"
              % (riga["file"], riga["disegnate"], riga["scoperte"],
                 riga["distinte"], riga["campioni"][0][:40] if riga["campioni"] else ""))
    print("\n  testo disegnato in tutto : %d siti"
          % sum(r["disegnate"] for r in righe))
    print("  scoperto                 : %d siti, %d stringhe distinte,"
          " su %d file"
          % (sum(r["scoperte"] for r in righe),
             sum(r["distinte"] for r in righe),
             sum(1 for r in righe if r["distinte"])))
    print("\n  ⚠️ Il salto per variabile e' UN SOLO salto, e nello stesso file:"
          "\n     `s = \"...\"` passato a una funzione e disegnato altrove resta"
          " fuori.\n     E' un limite dichiarato, non una svista.")
    for guaio in guai:
        print("\n  ⚠️ %s" % guaio)
    if not guai:
        print("\n  disegnate: ogni stringa a schermo o e' coperta, o e'"
              " dichiarata")
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
