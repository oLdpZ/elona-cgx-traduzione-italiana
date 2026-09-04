"""Le scene di storia: estrae da `scene2.hsp`, valida, riscrive l'albero di build.

`scene2.hsp` non e' un file di `lang()`: **e' il ramo inglese**, e il giapponese
e' un secondo file accanto (`scene.hsp:31`, `:49` fanno
`noteload lang("scene1.hsp", "scene2.hsp")`). Quindi la catena
`estrai -> reimporta -> applica` non lo vede, e serve una catena sua.

⚠️ Il file sta **dentro l'eseguibile** (`main.hsp:1`-`:2`, `#pack`): la
traduzione si inietta in `build/scene2.hsp` e vale solo dopo una
ricompilazione. `sorgente/` non si scrive mai.

## Il modello del gioco, che questo modulo imita riga per riga

`scene.hsp:56-108` scorre i marcatori `{...}`. Solo tre di loro **aprono** un
testo da disegnare -- `{txt}`, `{chat_N}`, `{wait}` -- e il marcatore successivo,
quale che sia, lo **chiude** e lo manda a schermo
(`scene.hsp:64-67` e `:408`). Ne discende la regola che governa tutto questo
modulo:

    la prosa che non segue un marcatore che apre NON ARRIVA A SCHERMO.

Nel file ce ne sono **quattro righe** (le didascalie di luogo delle scene 132,
133, 381 e 385): l'autore le ha scritte dopo un `{pic}`, un `{fade}` e un
`{actor_2}`, e il gioco le salta. Sono morte per flusso, come le famiglie che il
progetto ha gia' trovato dentro le `lang()`; qui si riconoscono da sole, perche'
`blocchi()` le lascia senza blocco che le contenga.

## I due modi di finire a schermo

`{txt}`     `scene.hsp:452-473`. Ogni riga si disegna **verbatim** e centrata:
            nessun a capo automatico, l'italiano si impagina a mano. Il budget
            e' la targa, `80 + strlen*8`, dentro la finestra **minima** che
            `config.txt` dichiara di reggere (800 px) -> `LARGHEZZA_TXT`.
            ⚠️ `windoww` e' configurazione: chi gioca a 2560 non vede sforare
            niente, e non per questo la riga ci sta.
            ⭐ Le righe **vuote** dentro un `{txt}` il gioco le cancella prima
            di disegnare (`scene.hsp:410-415`): un capoverso non si separa.

`{chat_N}`  `scene.hsp:427-436` -> `*chat_scene` -> `chatMore buff`. Il blocco e'
            **una riga sola** e a capo ci va il gioco, a `56 - en*3` = 53
            caratteri sugli spazi (`init.hsp:1329-1368`). Il vincolo qui e'
            **l'altezza**: `SOFFITTO_CHAT` righe nel riquadro, e il riquadro e'
            fisso a 600x380 quale che sia `windoww` (`chat.hsp:25230`).

`{actor_N}` `scene.hsp:400-404`. `"<Nome> Epiteto,54"`: si traduce **solo** cio'
            che sta prima dell'ultima virgola; il numero e' il ritratto.

## Il cancello

Con il dizionario vuoto, `applica_a_righe` deve restituire il file **identico
byte per byte**. E' la `prova_identita` di questa fase, e vale come cancello
d'ingresso: finche' non passa, nessuna resa e' credibile.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

FILE = "scene2.hsp"

# `config.txt`: «min 800 dots». Il budget della targa si tara sul minimo che il
# gioco dichiara di reggere, non sulla finestra di chi traduce.
FINESTRA_MINIMA = 800
LARGHEZZA_TXT = (FINESTRA_MINIMA - 80) // 8          # 90

# ⭐⭐ E L'ALTEZZA, tarata su uno screenshot il 2026-09-03 (134a). Fino a quel
# giorno il `{txt}` aveva un cancello in larghezza e **nessuno in altezza**:
# una resa da 16 righe passava, quando la piu' alta che il progetto disegni ne
# fa 11 e nessuno sapeva dove fosse il soffitto.
#
# `scene.hsp:451`-`:472`, il ciclo che disegna un `{txt}`:
#
#     y1 = 60                                  la banda dell'immagine parte qui
#     y3 = windowh/2 - (n*20)/2 - y1
#     y  = y3 + 28 + cnt*20                    riga cnt, passo 20 px
#     x  = windoww/2 - strlen(s)*4             CENTRATA, 8 px per carattere
#
# Il blocco e' centrato sulla finestra e **spostato in su di y1**: piu' righe ci
# sono, piu' la prima sale. Il vincolo che morde per primo e' quindi il bordo
# ALTO, non il basso.
#
#     prima riga = windowh//2 - 10n - 60 + 28  deve restare dentro la banda,
#                                              cioe' >= y1 = 60
#     -> 10n <= windowh//2 - 92
#
# ⭐ Il modello e' tarato, non dedotto: sulla foto della scena 0 blocco 3 (11
# righe, finestra 2560x1440) prevede la prima riga a 578 e l'ultima a 778, con
# passo 20; a schermo, riscalate, danno 451,6 e 607,8 con passo 15,62 — e le
# misure sulla foto dicono ~458, ~615 e 15,7. Vedi
# [[un-modello-del-rendering-va-tarato-su-un-pixel]].
FINESTRA_MINIMA_ALTA = 600                           # `config.txt`: «min 600 dots»
ALTEZZA_TXT = (FINESTRA_MINIMA_ALTA // 2 - 92) // 10                 # 20

# ⚠️ Due blocchi dei titoli di coda (`400.23` e `400.29`) fanno 24 e 22 righe, e
# le fanno **gia' in inglese**: sono elenchi di nomi, e accorciarli vorrebbe
# dire togliere qualcuno dai crediti. Il cancello non chiede quindi «stai sotto
# 20», ma «non essere piu' alta di monte»: sotto il soffitto sempre, e sopra il
# soffitto solo dove l'inglese ci era gia'.

# init.hsp:1279 -- talk_conv buff, 56 - en*3
COLONNA_CHAT = 53

# ⚠️ 53 NON e' la larghezza massima di una riga a schermo, ed e' un errore che
# la 132a ha fatto prima di misurarlo. `talk_conv` manda a capo **prima** di
# una parola che sforerebbe, ma l'ultimo pezzo -- quello senza piu' spazi
# dentro -- lo attacca alla riga corrente **senza controllare**
# (`init.hsp:1368`, l'`arg1 += msgtemp` fuori dai due cicli). Quindi ogni
# blocco puo' finire con una coda piu' lunga della colonna, e nell'inglese di
# monte succede in **125 blocchi su 1.181**, fino a 66 caratteri.
#
# Il tetto e' quindi la coda inglese piu' lunga dello stesso file -- la regola
# della 44a, «il budget di una schermata che nessuna guardia misura e'
# l'inglese di monte». ⚠️ Non e' una misura in pixel: quanto sia larga
# davvero quella riga nel riquadro non si ricava dal codice, e l'unico modo di
# saperlo e' guardarla. Finche' non la si guarda, non si sfora piu' di quanto
# gia' sfori il monte.
CODA_MASSIMA = 66

# ⚠️⚠️ IL SOFFITTO DEL RIQUADRO E' 13, E NON E' UN NUMERO NUOVO.
#
# `chat.hsp:25728` disegna il corpo a `wy + 43 + cnt*19`; `chat.hsp:25161` mette
# la voce «continua» a `wy + wh - 56 - keyrange*19 + 2`, con `wh = 380`. Il
# progetto ha gia' questo conto in `scratchpad/chat-lotto-misura.py` dalla 70a:
#
#     (324 - n*19 - 43) // 19        con n = 1  ->  13
#
# cioe' si pretende che la **fascia** di 19 px di ogni riga stia tutta sopra la
# fascia della voce di menu. Rifacendo il conto sul solo punto di partenza del
# testo (`43 + 19*cnt < 307`) ne verrebbero 14, e la 132a per un momento ha
# creduto che il 13 fosse un errore d'indice. Non lo e': sono due letture
# diverse di quanto sia alta una riga, e **differiscono di una riga sola**.
#
# Si tiene il 13, per tre ragioni:
#  - e' il numero gia' in forza nel progetto, e un cancello condiviso non si
#    allenta su un ricalcolo (la 112a: un numero che MIGLIORA va guardato con
#    lo stesso sospetto di uno che peggiora);
#  - l'asimmetria degli errori: un tetto troppo basso fa riscrivere una resa
#    che ci stava, un tetto troppo alto lascia a schermo un difetto che nessuno
#    guarda piu';
#  - nessuna delle due letture e' stata vista a schermo. Finche' non lo e', si
#    sceglie quella che non puo' far danno.
#
# ⓘ L'inglese di monte lo supera in un blocco (scena 11, 14 righe), come lo
# supera `chat.hsp:7289` -- notato dalla 70a. Non e' un permesso: e' l'inglese
# che sfora, e non lo si imita.
SOFFITTO_CHAT = (380 - 56 - 1 * 19 - 43) // 19          # 13

# ⚠️⚠️ LE GRAFIE INGLESI CHE IN ITALIANO IL PROGETTO NON SCRIVE COSI'.
#
# Non e' una lista di gusti: ogni riga porta il conto misurato sul dizionario
# il 2026-09-03, e ognuna nasce da una resa che aveva gia' la grafia sbagliata.
# La regola e' quella del progetto dalla 79a -- dove l'inglese di monte e'
# incoerente si segue il giapponese -- applicata ai nomi propri.
#
#   Ylva        -> Irva            イルヴァ: 1.058 «Irva» nelle rese, e le sole
#                                  due «Ylva» erano le scene della 132a
#   North Tyris -> Tyris del Nord  164 rese su 165, zero eccezioni
#   Port Kapul  -> Porto Kapul     24 rese contro 1 rimasta in inglese
#   Sierre Terre-> Sierra Terre    シエラ・テール. ⚠️ L'INGLESE SI CONTRADDICE DA
#                                  SOLO: `scene2.hsp` scrive «Sierra» 8 volte,
#                                  `chat.hsp` «Sierre» 7. Il giapponese ne ha
#                                  una sola, e le 10 rese col refuso lo
#                                  copiavano
#   Rosura      -> Lothria         ロスリア. Un refuso dell'inglese, in
#                                  `scene2.hsp:1139` e solo li': nello stesso
#                                  file «Lothria» compare 29 volte
#
# ⚠️ Nessuna delle forme di destra contiene quella di sinistra, quindi la
# sostituzione non si morde la coda. Chi aggiunge una riga lo verifichi.
GRAFIE = {
    "Ylva": "Irva",
    "North Tyris": "Tyris del Nord",
    "Port Kapul": "Porto Kapul",
    "Sierre Terre": "Sierra Terre",
    "Rosura": "Lothria",
}

# i soli marcatori che aprono un testo da disegnare (scene.hsp:70-105)
_APRONO = ("txt", "wait")

_MARCATORE = re.compile(r"^\{([A-Za-z0-9_]+)\}")
_ARGOMENTO = re.compile(r'^(\{[A-Za-z0-9_]+\}[^"]*")(.*)("[^"]*)$')


def _apre(tipo: str) -> bool:
    return tipo in _APRONO or tipo.startswith("chat_")


def leggi(percorso: Path | None = None) -> list[str]:
    """Le righe del file, senza terminatore. `'\\r\\n'.join(...)` le ricompone."""
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    return percorso.read_bytes().decode("cp932").split("\r\n")


def scrivi(righe: list[str], percorso: Path) -> None:
    percorso.write_bytes("\r\n".join(righe).encode("cp932"))


def firma(carico) -> str:
    """L'impronta dell'inglese, per accorgersi che il monte si e' mosso."""
    testo = "\n".join(carico) if isinstance(carico, list) else carico
    return hashlib.sha1(testo.encode("utf-8")).hexdigest()


def blocchi(righe: list[str]) -> tuple[list[dict], list[int]]:
    """I blocchi del file, e gli indici delle righe che il gioco non disegna.

    Imita `scene.hsp:56-108`: un marcatore che apre raccoglie la prosa che lo
    segue, e il marcatore dopo la chiude. La prosa che non ha sopra di se' un
    marcatore che apre non finisce in nessun blocco -- e non finisce a schermo.
    """
    trovati: list[dict] = []
    morte: list[int] = []
    scena: str | None = None
    per_scena = 0
    aperto: dict | None = None
    for indice, riga in enumerate(righe):
        spoglia = riga.strip()
        marcatore = _MARCATORE.match(spoglia)
        if marcatore is not None:
            nome = marcatore.group(1)
            aperto = None
            if nome.isdigit():
                scena, per_scena = nome, 0
                continue
            blocco = {
                "scena": scena,
                "blocco": per_scena,
                "tipo": nome,
                "riga": indice + 1,
                "argomento": spoglia[marcatore.end():].strip().strip('"'),
                "prosa": [],
            }
            per_scena += 1
            trovati.append(blocco)
            if _apre(nome):
                aperto = blocco
            continue
        if spoglia == "" or spoglia.startswith(";"):
            continue
        if aperto is None:
            morte.append(indice)
        else:
            aperto["prosa"].append(indice)
    return trovati, morte


def carico_inglese(blocco: dict, righe: list[str]):
    """Che cosa, di questo blocco, e' testo da tradurre. `None` se niente."""
    tipo = blocco["tipo"]
    if tipo == "txt":
        if not blocco["prosa"]:
            return None
        # ⚠️ UNA STRINGA, non una lista, con le righe separate da un a capo.
        # Ogni altro strumento del progetto (`accenti`, `bilingui`, `verifica`,
        # i referti) legge `it` ed `en` come stringhe e chiama `.strip()` o una
        # regex: il primo giro della 132a le scriveva come liste e ha acceso
        # due reti in file che non c'entravano niente. L'impaginazione e' un
        # dettaglio di disegno, non un tipo di dato diverso.
        return "\n".join(righe[i] for i in blocco["prosa"])
    if tipo.startswith("chat_"):
        if not blocco["prosa"]:
            return None
        return righe[blocco["prosa"][0]]
    if tipo.startswith("actor_"):
        nome, virgola, _ = blocco["argomento"].rpartition(",")
        return nome if virgola else None
    return None


def giapponese(righe_jp: list[str] | None = None) -> dict:
    """Il carico di `scene1.hsp` per chiave, quando la scena e' appaiabile.

    ⭐⭐ **Il giapponese c'e' anche per questo file**, e serve. La 132a stava
    per rendere «the Vindale Forest» con «foresta di Vindale» in un punto dove
    il giapponese scrive `異形の森`, che il progetto rende **Foresta Eretica**
    da diciassette voci: l'inglese di monte chiama con lo stesso nome due cose
    che il giapponese tiene separate (`ヴィンデールの森` e `異形の森`), e il
    nome inglese da solo non basta a decidere.

    ⚠️ Si appaia **solo dove la struttura combacia**. Otto scene su 89 hanno un
    numero di blocchi diverso nei due rami (l'inglese ha tagliato dei `{txt}`),
    e li' un appaiamento per ordinale accosterebbe blocchi che non si
    corrispondono -- che e' peggio di nessun giapponese, perche' sembra un
    dato. Su quelle scene la voce esce senza `jp`.
    """
    if righe_jp is None:
        righe_jp = leggi(percorsi.SORGENTE_HSP / "scene1.hsp")
    blocchi_jp, _ = blocchi(righe_jp)
    per_scena: dict = {}
    for blocco in blocchi_jp:
        per_scena.setdefault(blocco["scena"], []).append(blocco)
    return {"per_scena": per_scena, "righe": righe_jp}


def _carico_appaiato(indice: dict, scena_en: list[dict], blocco: dict):
    """Il carico giapponese del blocco, se le due scene hanno la stessa forma."""
    if indice is None:
        return None
    gemelli = indice["per_scena"].get(blocco["scena"])
    if gemelli is None or len(gemelli) != len(scena_en):
        return None
    gemello = gemelli[blocco["blocco"]]
    if gemello["tipo"] != blocco["tipo"]:
        return None
    return carico_inglese(gemello, indice["righe"])


def voci(righe: list[str], scene: set[str] | None = None,
         indice_jp: dict | None = None) -> list[dict]:
    """Una voce per ogni blocco con del testo, nell'ordine del file."""
    trovati, _ = blocchi(righe)
    per_scena_en: dict = {}
    for blocco in trovati:
        per_scena_en.setdefault(blocco["scena"], []).append(blocco)
    fuori = []
    for blocco in trovati:
        if scene is not None and blocco["scena"] not in scene:
            continue
        carico = carico_inglese(blocco, righe)
        if carico is None:
            continue
        voce = {
            "firma": firma(carico),
            "file": FILE,
            "riga": blocco["riga"],
            "scena": blocco["scena"],
            "blocco": blocco["blocco"],
            "tipo": blocco["tipo"],
            "en": carico,
            "it": "",
        }
        gemello = _carico_appaiato(indice_jp, per_scena_en[blocco["scena"]], blocco)
        if gemello is not None:
            voce["jp"] = gemello
        fuori.append(voce)
    return fuori


def _chiave(voce: dict) -> tuple:
    return (voce["scena"], voce["blocco"])


def applica_a_righe(righe: list[str], dizionario: dict) -> tuple[list[str], int]:
    """Inietta le rese. Dizionario vuoto -> le righe tornano identiche.

    Si lavora **all'indietro**, dall'ultimo blocco al primo, perche' un `{txt}`
    italiano puo' avere un numero di righe diverso dall'inglese e cambierebbe
    gli indici di tutto cio' che sta sotto.
    """
    trovati, _ = blocchi(righe)
    fuori = list(righe)
    fatte = 0
    for blocco in reversed(trovati):
        voce = dizionario.get((blocco["scena"], blocco["blocco"]))
        if voce is None:
            continue
        reso = voce.get("it")
        if not reso:
            continue
        atteso = carico_inglese(blocco, righe)
        if atteso is None or firma(atteso) != voce["firma"]:
            raise ValueError(
                "%s scena %s blocco %s: il monte non e' piu' quello su cui la"
                " resa fu scritta. La voce va rifatta, non riagganciata."
                % (FILE, blocco["scena"], blocco["blocco"])
            )
        tipo = blocco["tipo"]
        if tipo == "txt":
            primo, ultimo = blocco["prosa"][0], blocco["prosa"][-1]
            fuori[primo:ultimo + 1] = [degrada(r) for r in reso.split("\n")]
        elif tipo.startswith("chat_"):
            fuori[blocco["prosa"][0]] = degrada(reso)
        elif tipo.startswith("actor_"):
            indice = blocco["riga"] - 1
            pezzi = _ARGOMENTO.match(fuori[indice].strip())
            if pezzi is None:
                raise ValueError(
                    "%s:%d: la riga dell'attore non ha la forma attesa"
                    % (FILE, blocco["riga"])
                )
            _, virgola, coda = pezzi.group(2).rpartition(",")
            fuori[indice] = pezzi.group(1) + degrada(reso) + virgola + coda + pezzi.group(3)
        fatte += 1
    return fuori, fatte


def carica_dizionario(percorso: Path | None = None) -> dict:
    percorso = percorso or (percorsi.DIZIONARIO / (FILE + ".jsonl"))
    if not percorso.exists():
        return {}
    fuori = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        fuori[_chiave(voce)] = voce
    return fuori


def righe_a_capo(testo: str, colonna: int = COLONNA_CHAT) -> list[str]:
    """`talk_conv` nel ramo non giapponese (`init.hsp:1331-1363`).

    Si guarda il **prossimo spazio**: se la riga corrente piu' quella parola
    supera la colonna, si va a capo prima della parola. La coda senza spazi
    finisce tutta sull'ultima riga, lunga quanto viene -- ed e' l'unico modo in
    cui una riga puo' sforare in larghezza invece che in altezza.
    """
    resto, fuori, corrente = testo, [], ""
    while True:
        taglio = resto.find(" ")
        if taglio == -1:
            break
        parola = resto[:taglio + 1]
        if len(corrente) + len(parola) > colonna:
            fuori.append(corrente)
            corrente = ""
        corrente += parola
        resto = resto[taglio + 1:]
    fuori.append(corrente + resto)
    return fuori


def avvisi(voce: dict) -> list[str]:
    """Cio' che va **guardato**, non cio' che va rifiutato.

    ⚠️ La distinzione e' quella che `scratchpad/chat-lotto-misura.py` fa dalla
    70a, e non e' pedanteria: li' `fuori` conta le rese che sforano il tetto e
    `peggiorate` quelle che fanno una riga in piu' dell'inglese, e sono due
    numeri separati. L'italiano e' piu' lungo dell'inglese quasi sempre; se
    «una riga in piu'» fosse un rifiuto, il cancello direbbe rosso su una resa
    corretta e chi traduce imparerebbe a non guardarlo.
    """
    reso = voce.get("it")
    inglese = voce.get("en")
    if not reso or not voce["tipo"].startswith("chat_"):
        return []
    if not isinstance(reso, str) or not isinstance(inglese, str):
        return []
    dopo = len(righe_a_capo(degrada(reso)))
    prima = len(righe_a_capo(inglese))
    if dopo > prima:
        return ["%d righe contro le %d dell'inglese" % (dopo, prima)]
    return []


def problemi(voce: dict) -> list[str]:
    """Che cosa non va in una resa. Elenco vuoto = va bene."""
    reso = voce.get("it")
    if not reso:
        return []
    guai = []
    tipo = voce["tipo"]
    # ⚠️ prima di tutto il resto, e per ogni tipo: una grafia inglese dentro
    # una resa italiana. Costa niente e la 133a ne ha trovate due gia' scritte
    # dalla sessione prima -- che senza questo cancello avrei imitato lotto
    # dopo lotto, perche' il modo in cui si sbaglia un nome proprio e'
    # guardare come l'ha reso chi ha tradotto prima.
    testo = reso if isinstance(reso, str) else "\n".join(reso)
    for inglese, italiano in GRAFIE.items():
        if inglese in testo:
            guai.append("la resa scrive «%s»: in italiano il progetto scrive"
                        " «%s»" % (inglese, italiano))
    # ⚠️⚠️ E il carattere che CP932 non sa scrivere. `degrada` toglie gli
    # accenti, non tutto: le virgolette caporali «» passavano di qui indenni e
    # scoppiavano dopo, dentro `--applica`, a lotto gia' reimportato. Il
    # cancello va dove si scrive la resa, non dove si costruisce l'albero.
    # ⓘ Le virgolette curve “” invece CP932 le scrive -- a doppia larghezza,
    # che a schermo e' un'altra cosa: quelle le vede l'occhio, non il codice.
    try:
        degrada(testo).encode("cp932")
    except UnicodeEncodeError as errore:
        fuori = degrada(testo)[errore.start:errore.end]
        guai.append("il carattere %r non esiste in CP932: il gioco non puo'"
                    " scriverlo" % fuori)
    if tipo == "txt":
        if not isinstance(reso, str):
            return ["una resa di {txt} e' una stringa sola, con le righe"
                    " separate da un a capo"]
        disegnate = reso.split("\n")
        soffitto = max(ALTEZZA_TXT, len((voce.get("en") or "").split("\n")))
        if len(disegnate) > soffitto:
            guai.append("%d righe, oltre le %d che la targa regge alla finestra"
                        " minima (%d x %d)"
                        % (len(disegnate), soffitto, FINESTRA_MINIMA,
                           FINESTRA_MINIMA_ALTA))
        for numero, riga in enumerate(reso.split("\n"), 1):
            if riga.strip() == "":
                guai.append("riga %d vuota: il gioco la cancella prima di"
                            " disegnare, non separa niente" % numero)
            lunga = len(degrada(riga))
            if lunga > LARGHEZZA_TXT:
                guai.append("riga %d di %d caratteri, oltre i %d della targa"
                            % (numero, lunga, LARGHEZZA_TXT))
    elif tipo.startswith("chat_"):
        if not isinstance(reso, str):
            return ["una resa di {chat_N} e' UNA riga sola: a capo ci va il gioco"]
        if "\n" in reso:
            return ["una resa di {chat_N} non porta a capo: li mette il gioco"]
        disegnate = righe_a_capo(degrada(reso))
        if len(disegnate) > SOFFITTO_CHAT:
            guai.append("%d righe una volta mandate a capo, il riquadro ne"
                        " tiene %d" % (len(disegnate), SOFFITTO_CHAT))
        lunga = max(len(r) for r in disegnate)
        if lunga > CODA_MASSIMA:
            guai.append("una riga arriva a %d caratteri, oltre i %d della coda"
                        " piu' lunga dell'inglese" % (lunga, CODA_MASSIMA))
    elif tipo.startswith("actor_"):
        if "," in str(reso):
            guai.append("una virgola nel nome dell'attore sposta il taglio di"
                        " csvsort e si porta via il ritratto")
    return guai


def _prova_identita(righe: list[str]) -> None:
    rifatte, fatte = applica_a_righe(righe, {})
    if rifatte != righe or fatte != 0:
        raise SystemExit("identita' ROTTA: col dizionario vuoto il file cambia")
    print("identita'                : il file torna identico, 0 sostituzioni")


def referto() -> None:
    righe = leggi()
    trovati, morte = blocchi(righe)
    tutte = voci(righe)
    diz = carica_dizionario()
    rese = [v for v in tutte if diz.get(_chiave(v), {}).get("it")]
    print("%s: %d righe, %d blocchi, %d con testo"
          % (FILE, len(righe) - 1, len(trovati), len(tutte)))
    print("tradotte                 : %d su %d" % (len(rese), len(tutte)))
    print("righe che il gioco NON disegna: %d   (atteso: 4)" % len(morte))
    for indice in morte:
        print("    %s:%d  %s" % (FILE, indice + 1, righe[indice].strip()))
    _prova_identita(righe)
    guasti = 0
    for voce in tutte:
        piena = diz.get(_chiave(voce))
        if piena is None:
            continue
        for guaio in problemi(piena):
            print("  scena %s blocco %s (%s): %s"
                  % (voce["scena"], voce["blocco"], voce["tipo"], guaio))
            guasti += 1
    print("rese fuori misura        : %d   (atteso: 0)" % guasti)
    if guasti:
        raise SystemExit(1)


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--estrai", metavar="SCENE",
                              help="lotto JSONL per le scene indicate, es. 0-5 o 0,1,11")
    analizzatore.add_argument("--applica", action="store_true",
                              help="riscrive build/scene2.hsp col dizionario")
    analizzatore.add_argument("--reimporta", metavar="LOTTO",
                              help="valida un lotto e lo scrive nel dizionario")
    analizzatore.add_argument("--referto", action="store_true")
    argomenti = analizzatore.parse_args()

    if argomenti.estrai:
        scene = set()
        for pezzo in argomenti.estrai.split(","):
            if "-" in pezzo:
                da, a = pezzo.split("-")
                scene.update(str(n) for n in range(int(da), int(a) + 1))
            else:
                scene.add(pezzo)
        righe = leggi()
        trovate = voci(righe, scene, giapponese())
        bersaglio = percorsi.LAVORO_LOTTI / ("scene2-%s.jsonl" % argomenti.estrai)
        bersaglio.write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in trovate),
            encoding="utf-8")
        print("%d voci in %s" % (len(trovate), bersaglio))
        return

    if argomenti.reimporta:
        # ⚠️ si valida **tutto il lotto** e solo se e' pulito si scrive: e' la
        # regola di `reimporta.py` per il dizionario delle `lang()`, e vale qui
        # per lo stesso motivo. Un lotto scritto a meta' e' peggio di un lotto
        # rifiutato, perche' nessuno sa dove si era fermato.
        arrivo = Path(argomenti.reimporta)
        lotto = [json.loads(r) for r in arrivo.read_text(encoding="utf-8").splitlines() if r.strip()]
        guasti = [(v, p) for v in lotto for p in problemi(v)]
        for voce, guaio in guasti:
            print("  FUORI %s.%s %s: %s" % (voce["scena"], voce["blocco"],
                                            voce["tipo"], guaio))
        if guasti:
            raise SystemExit("lotto rifiutato: %d rese fuori misura" % len(guasti))
        # e la firma deve ancora agganciare il monte, non solo essere presente
        righe = leggi()
        attese = {_chiave(v): v["firma"] for v in voci(righe)}
        slegate = [_chiave(v) for v in lotto if attese.get(_chiave(v)) != v["firma"]]
        if slegate:
            raise SystemExit("lotto rifiutato: %d voci non agganciano piu' il"
                             " monte: %s" % (len(slegate), slegate[:5]))
        diz = carica_dizionario()
        piene = 0
        for voce in lotto:
            if voce.get("it"):
                diz[_chiave(voce)] = voce
                piene += 1
        bersaglio = percorsi.DIZIONARIO / (FILE + ".jsonl")
        ordinate = sorted(diz.values(), key=lambda v: v["riga"])
        bersaglio.write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in ordinate),
            encoding="utf-8")
        print("%d rese nel lotto, %d voci nel dizionario -> %s"
              % (piene, len(ordinate), bersaglio))
        return

    if argomenti.applica:
        # ⚠️⚠️ Si legge dalla BUILD: leggendo dal sorgente questo passo rifa il
        # file da capo e butta via le toppe che `applica.py` ci ha appena messo.
        # Su `scene2.hsp` oggi non ce n'e' nessuna, quindi non si perdeva
        # niente -- ma su `tcg_mod.hsp` il gemello di questa riga ha fatto
        # sparire i nomi delle fasi del turno da ogni eseguibile dalla 136a in
        # poi. Un difetto che non fa danno solo perche' il file e' vuoto e'
        # comunque un difetto.
        bersaglio = percorsi.BUILD_HSP / FILE
        if not bersaglio.exists():
            raise SystemExit("albero di build assente: lancia prima `applica.py`")
        righe, fatte = applica_a_righe(leggi(bersaglio), carica_dizionario())
        scrivi(righe, bersaglio)
        print("%s: %d blocchi iniettati" % (bersaglio, fatte))
        return

    referto()


if __name__ == "__main__":
    main()
