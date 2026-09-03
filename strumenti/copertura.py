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
}

# ⚠️⚠️ IL DEBITO NON ANCORA TRIATO, misurato alla 135a e non giudicato.
#
# Questi file hanno stringhe che nessuno raggiunge, e nessuno le ha ancora
# guardate una per una. Il numero e' una **misura**, non un verdetto: dentro
# ci sara' testo vero, tracce di debug (`system.hsp` ha una « Debug Console»),
# etichette di configurazione e falsi positivi del riconoscitore.
#
# ⚠️ Stanno qui, e non fuori da ogni lista, per una ragione sola: cosi' il
# cancello e' verde oggi e si accende domani, quando uno di questi conti si
# muove o quando compare un file nuovo. Una riga qui dentro NON vuol dire
# «va bene cosi'»: vuol dire «misurato il 2026-09-03, mai guardato».
# Triarne uno significa toglierlo di qui e dargli una Dichiarazione con
# scritto perche'.
DA_TRIARE: dict[str, int] = {
    "system.hsp": 83,
    "custom_tweaks.hsp": 75,
    "init.hsp": 61,
    "tcg.hsp": 52,
    "buff.hsp": 48,
    "command.hsp": 16,
    "action.hsp": 11,
    "map.hsp": 11,
    "module.hsp": 10,
    "chara_func.hsp": 8,
    "custom_ai.hsp": 8,
    "main.hsp": 8,
    "config.hsp": 4,
    "db_creature.hsp": 4,
    "tcg_custom.hsp": 4,
    "proc.hsp": 3,
    "screen.hsp": 3,
    "help.hsp": 2,
    "text.hsp": 2,
    "trait.hsp": 2,
    "chat.hsp": 1,
    "db_card.hsp": 1,
    "event.hsp": 1,
    "item.hsp": 1,
    "map_rand.hsp": 1,
    "material.hsp": 1,
    "net.hsp": 1,
}


def letterali_di_prosa(testo: str) -> list[str]:
    """I letterali del file che somigliano a una frase, righe morte escluse."""
    fuori = []
    for riga in testo.split("\n"):
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


def scoperte_di(nome_file: str, testo: str, toppe: set[str]) -> list[str]:
    """Le stringhe di prosa che non raggiunge ne' il dizionario ne' una toppa.

    Il dizionario si consulta attraverso `estrai.siti()`, che e' l'unica
    scansione del sorgente del progetto: cosi' questo modulo e `applica`
    camminano sugli stessi siti per costruzione e non per disciplina.
    """
    span_per_riga: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for sito in siti(testo):
        span_per_riga[sito[0]].append((sito[7], sito[8]))

    scoperte = []
    for numero, riga in enumerate(testo.split("\n"), 1):
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
        prosa = letterali_di_prosa(testo)
        if not prosa:
            continue
        scoperte = scoperte_di(percorso.name, testo, toppe.get(percorso.name, set()))
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
              f"{sum(d.scoperte for d in fronti.values())} stringhe distinte")
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
