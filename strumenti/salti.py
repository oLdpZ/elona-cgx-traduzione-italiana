"""La rete del SALTO: il testo che arriva a schermo passando per una variabile.

⚠️⚠️ **Perche' esiste, e che cosa la 141a ha scoperto scrivendola.** La 139a e
la 140a hanno lasciato scritto che `disegnate.py` «fa un salto solo», e che il
gradino dopo era **il secondo salto** — una stringa messa in una variabile,
passata a un'altra e disegnata li'. Le due sonde a mano della 140a hanno
trovato 51 stringhe a schermo che nessuna rete vedeva, e il motivo scritto
accanto diceva: manca il secondo salto.

⭐ **Il motivo era prosa, e la prosa sbagliava.** Andando a guardare il
sorgente, nessuno dei due casi era un secondo salto:

    tcg.hsp:3348   if ( sortmode@tcg == 0 ) { s@tcg += "Sort by: DBID   " }
    tcg.hsp:3363   mes s@tcg

E' **un salto solo**, e `disegnate` conosce sia la variabile che il comando.
Non la vedeva perche' `_ASSEGNAZIONE` e' ancorata a `^\\s*`, e li' l'assegnazione
sta **dentro un `if` a graffe sulla stessa riga**. Un'ancora, non un salto.

    help.hsp:387   s      = "アイテムを拾う(get)", key_get, ...
    help.hsp:393   mes s(cnt * 2)

Anche questo e' un salto solo. Non lo vedeva perche' `s` sta in
`disegnate._TROPPO_GENERICHE`, ed e' escluso **su tutto il file**.

💡 Cosi' questa rete non aggiunge un salto: toglie i due limiti che
nascondevano il primo, e **poi** segue la catena quanto serve.

## Le tre cose che fa, e perche' ognuna

1. **L'assegnazione si legge dovunque stia sulla riga**, non solo in testa:
   dopo un `{`, dopo un `:`. E' il caso della riga di stato dell'editor di
   mazzo, tredici etichette dentro tredici `if` a graffe.

2. **La lista dei nomi generici diventa un AMBITO, non un'esclusione.** `s`,
   `buff`, `tmp` portano di tutto, e come chiave su tutto il file direbbero
   «da tradurre» a mezzo gioco: e' la ragione per cui `disegnate` li butta
   via. Ma dentro **un sottoprogramma solo** — fra un `*etichetta` e la
   successiva — `s` vuol dire una cosa sola, e se in quel blocco qualcuno
   disegna `s` allora i letterali che ci finiscono dentro sono testo. Un nome
   specifico (`s@tcg`, `cfname@tcg`, `locvar_equipinfo_s`) vale invece su
   tutto il file, come prima.

3. **La catena si segue oltre il primo passo.** `a = "..."`, `b = a`,
   `mes b`: chi assegna a una variabile che finisce a schermo, finisce a
   schermo. E' la chiusura transitiva degli alias dentro il blocco, ed e'
   l'unico pezzo che merita davvero il nome di «secondo salto». ⚠️ Nel
   sorgente di oggi **non trova niente da sola**: i 36 ritrovamenti vengono
   tutti dai due punti di sopra. Sta qui lo stesso perche' costa sei righe e
   perche' la prossima volta la domanda non si riapra.

## Che cosa NON vede, e resta dichiarato

⚠️ **Il salto fra due blocchi per un nome generico.** `s` riempito in
`*apparecchia` e disegnato in `*mostra` non lo vede nessuno, ed e' voluto: e'
il prezzo dell'ambito che rende usabile `s`.

⚠️ **Il passaggio per un sottoprogramma che riscrive il valore.**
`*convertHelp` (`help.hsp:284`) prende `s(cnt)` e ci lascia dentro solo quel
che stava fra le parentesi. Qui il letterale e il disegno stanno nello stesso
blocco, quindi il caso si vede lo stesso — ma il **valore** che questa rete
riporta e' quello prima della riscrittura.

⚠️⚠️ **E il letterale MISTO resta fuori dal conto principale.** Le 38
etichette dei tasti di F1 portano giapponese e inglese **insieme, nella stessa
stringa, fuori da `lang()`**, e `_giapponese` le scarta come scarta ogni ramo
giapponese — giustamente, per le altre undicimila. `--misti` le conta a parte:
sono un asse diverso dal salto, e mescolarle renderebbe illeggibili tutt'e due
i numeri.

## Uso

    python -m strumenti.salti              # il censimento, per file
    python -m strumenti.salti --file X.hsp # un file solo, riga per riga
    python -m strumenti.salti --confronto  # quante ne aggiunge a `disegnate`
    python -m strumenti.salti --misti      # l'altro asse: i letterali misti
"""
import argparse
import re
from collections import defaultdict
from dataclasses import dataclass

from strumenti import copertura, disegnate, percorsi
from strumenti.commenti import righe_in_commento

# Il nome di una variabile HSP, con o senza modulo. Uguale a quello di
# `disegnate`: due grafie diverse dello stesso nome sarebbero due reti che non
# si possono confrontare.
_NOME = r"[A-Za-z_][A-Za-z0-9_]*(?:@[A-Za-z0-9_]+)?"

# L'etichetta che apre un sottoprogramma: e' il confine dell'ambito.
_ETICHETTA = re.compile(r"^\s*\*(%s)" % _NOME)

# ⚠️ Un'assegnazione OVUNQUE sulla riga: a inizio riga, dopo `{` (il caso della
# riga di stato dell'editor di mazzo) e dopo `:` (HSP separa cosi' due comandi
# sulla stessa riga). `(?!=)` tiene fuori `==`, che e' un confronto; il resto
# dei confronti (`!=`, `>=`, `<=`) non puo' arrivare qui, perche' prima del
# segno c'e' il nome e prima del nome c'e' `^`, `{` o `:`.
_ASSEGNA = re.compile(r"(?:^|[{:])\s*(%s)\s*(?:\([^)]*\))?\s*\+?=(?!=)\s*"
                      % _NOME)

# Il primo argomento di un comando che disegna: `mes s`, `mes s(cnt * 2)`.
_ARGOMENTO = re.compile(r"^(%s)\s*(?:\([^)]*\))?\s*(?:$|[,)+\s])" % _NOME)

_LETTERALE = disegnate._LETTERALE
_COMANDO = disegnate._COMANDO

# ⚠️ Non e' una lista di esclusione: e' la lista dei nomi il cui AMBITO e' il
# blocco invece del file. Sta in `disegnate` e si legge di li' — averne due
# copie vorrebbe dire che un giorno una delle due impara un nome e l'altra no.
GENERICHE = disegnate._TROPPO_GENERICHE

# La parentesi ASCII dentro un letterale che porta anche il giapponese: e' quel
# che `*convertHelp` tiene quando il gioco e' in inglese.
_PARENTESI = re.compile(r"\(([\x20-\x7e]*[A-Za-z][\x20-\x7e]*)\)")


@dataclass(frozen=True)
class Dichiarazione:
    tipo: str        # "fronte" | "esente"
    scoperte: int    # stringhe DISTINTE che arrivano a schermo di rimbalzo
    motivo: str


# ⚠️⚠️ Come in `copertura` e in `disegnate`: o un file e' dichiarato, o il
# cancello si accende. Il conto e' misurato e non puo' sbagliare; **il motivo
# scritto accanto e' prosa, e nessun cancello legge la prosa** — la lezione
# della 140a, dove quattro motivi su sette dicevano una cosa falsa. Chi tocca
# una di queste righe verifichi il motivo prima di ereditarlo.
DICHIARATI: dict[str, Dichiarazione] = {}


def blocchi(righe: list[str]) -> list[tuple[str, int, int]]:
    """(etichetta, prima riga, ultima riga) per ogni sottoprogramma.

    Quel che sta prima della prima etichetta e' un blocco anche lui, e si
    chiama `<testa>`: in `command.hsp` ci stanno le cinque sigle della riga di
    stato del personaggio.
    """
    tagli: list[tuple[int, str]] = [(0, "<testa>")]
    for numero, riga in enumerate(righe, 1):
        trovato = _ETICHETTA.match(riga)
        if trovato:
            tagli.append((numero, trovato.group(1)))
    fuori = []
    for indice, (numero, nome) in enumerate(tagli):
        fine = tagli[indice + 1][0] - 1 if indice + 1 < len(tagli) else len(righe)
        if fine >= numero:
            fuori.append((nome, max(numero, 1), fine))
    return fuori


def _disegnate_sulla_riga(riga: str) -> set[str]:
    """I nomi passati come primo argomento a un comando che disegna."""
    fuori = set()
    for trovato in _COMANDO.finditer(riga):
        nome = _ARGOMENTO.match(riga[trovato.end():].lstrip())
        if nome:
            fuori.add(nome.group(1))
    return fuori


def specifiche_disegnate(testo: str, morte: set[int] | None = None) -> set[str]:
    """I nomi NON generici che qualcuno disegna, su tutto il file.

    E' l'ambito largo: `s@tcg` vuol dire la stessa cosa in ogni blocco, e un
    letterale che ci finisce dentro arriva a schermo anche se il `mes` sta
    mille righe piu' in la'.
    """
    morte = morte or set()
    fuori = set()
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte or not disegnate._viva(riga):
            continue
        fuori |= {n for n in _disegnate_sulla_riga(riga) if n not in GENERICHE}
    return fuori


def _catena(disegnati: set[str], alias: dict[str, set[str]]) -> set[str]:
    """Chi finisce a schermo di rimbalzo: la chiusura transitiva degli alias.

    `b = a` e `mes b` vogliono dire che anche `a` finisce a schermo. E' il
    pezzo che merita il nome di «secondo salto», ed e' anche l'unico che nel
    sorgente di oggi non trova niente da solo.
    """
    vive = set(disegnati)
    cambiato = True
    while cambiato:
        cambiato = False
        for bersaglio, sorgenti in alias.items():
            if bersaglio in vive and not sorgenti <= vive:
                vive |= sorgenti
                cambiato = True
    return vive


def scoperte_di(nome: str, testo: str,
                morte: set[int] | None = None) -> list[tuple[int, str, str, str]]:
    """(riga, blocco, variabile, letterale) per il testo che salta a schermo.

    ⚠️ Comprende quel che e' gia' coperto dal dizionario o da una toppa: chi
    chiama sottrae quel che vuole, come in `disegnate`.
    """
    morte = morte or set()
    righe = testo.split("\n")
    span_lang, giapponesi = disegnate._spazio_lang(testo)
    larghe = specifiche_disegnate(testo, morte)

    fuori = []
    for etichetta, prima, ultima in blocchi(righe):
        disegnati = set(larghe)
        assegnazioni: dict[str, list[tuple[int, int]]] = defaultdict(list)
        alias: dict[str, set[str]] = defaultdict(set)
        for numero in range(prima, ultima + 1):
            riga = righe[numero - 1]
            if numero in morte or not disegnate._viva(riga):
                continue
            disegnati |= _disegnate_sulla_riga(riga)
            for trovato in _ASSEGNA.finditer(riga):
                bersaglio = trovato.group(1)
                assegnazioni[bersaglio].append((numero, trovato.end()))
                sorgente = _ARGOMENTO.match(riga[trovato.end():].lstrip())
                if sorgente:
                    alias[bersaglio].add(sorgente.group(1))

        for bersaglio in sorted(_catena(disegnati, alias)):
            for numero, coda_da in assegnazioni.get(bersaglio, []):
                riga = righe[numero - 1]
                for letterale in _LETTERALE.finditer(riga, coda_da):
                    valore = letterale.group(1)
                    dentro_lang = any(
                        inizio <= letterale.start(1) and letterale.end(1) <= fine
                        for inizio, fine in span_lang.get(numero, []))
                    if (dentro_lang
                            or disegnate._NON_TESTO.match(valore)
                            or disegnate._giapponese(valore)
                            or disegnate._SENZA_LETTERE.match(valore)
                            or valore in giapponesi.get(numero, set())):
                        continue
                    fuori.append((numero, etichetta, bersaglio, valore))
    return fuori


def misti_di(nome: str, testo: str,
             morte: set[int] | None = None) -> list[tuple[int, str, str]]:
    """(riga, letterale, la parte inglese) dei letterali BILINGUI fuori da `lang()`.

    ⚠️⚠️ L'altro asse, e non e' il salto. Un letterale con byte non-ASCII di
    solito e' il ramo giapponese di una `lang()`, e il progetto traduce
    l'inglese: scartarlo e' giusto undicimila volte. Ma `help.hsp:387` scrive
    `"アイテムを拾う(get)"` **fuori** da `lang()`, e in inglese `*convertHelp`
    tiene solo `get`: quella parentesi e' testo a schermo. Le 38 etichette di
    F1 erano invisibili a tutt'e due le reti per questo, non per il salto.
    """
    morte = morte or set()
    span_lang, giapponesi = disegnate._spazio_lang(testo)
    fuori = []
    for numero, riga in enumerate(testo.split("\n"), 1):
        if numero in morte or not disegnate._viva(riga):
            continue
        for letterale in _LETTERALE.finditer(riga):
            valore = letterale.group(1)
            if not disegnate._giapponese(valore):
                continue
            # ⚠️⚠️ Lo span di `estrai.siti()` copre il solo ramo INGLESE, e il
            # ramo giapponese ci resta fuori: senza la seconda mappa ogni
            # `lang("拾う(get)", "Pick up")` del gioco finirebbe fra i misti,
            # cioe' la rete direbbe scoperto un lavoro che il dizionario copre.
            if valore in giapponesi.get(numero, set()):
                continue
            if any(inizio <= letterale.start(1) and letterale.end(1) <= fine
                   for inizio, fine in span_lang.get(numero, [])):
                continue
            dentro = _PARENTESI.search(valore)
            if dentro:
                fuori.append((numero, valore, dentro.group(1)))
    return fuori


def _da_sottrarre() -> tuple[dict[str, set[str]], dict[str, set[str]], set[str]]:
    """Le tre liste che ogni rete del progetto toglie, prese da dove stanno.

    ⚠️ Devono essere **le stesse** di `disegnate` e `copertura`: due misure
    della stessa cosa che sottraggono liste diverse sono due numeri che non si
    possono confrontare, e la prossima sessione non saprebbe a quale credere.
    """
    return (copertura._righe_con_toppa(), disegnate._rese_note(),
            disegnate._invarianti())


def censimento() -> list[dict]:
    toppe, rese, invarianti = _da_sottrarre()
    righe = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        nome = percorso.name
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        righe_del_file = testo.split("\n")
        tutte = scoperte_di(nome, testo, morte)
        if not tutte:
            continue
        gia = {t[2] for t in disegnate.tutte_di(nome, testo, morte)}
        scoperte = []
        for numero, etichetta, bersaglio, valore in tutte:
            if valore in rese.get(nome, set()) or valore in invarianti:
                continue
            if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
                continue
            scoperte.append((numero, etichetta, bersaglio, valore))
        meccanismo = nome in copertura.MECCANISMI
        viste = set() if meccanismo else {s[3] for s in scoperte}
        # ⚠️⚠️ Il conto che il cancello guarda e' quello delle stringhe che
        # **nessun'altra rete vede**, non di tutte quelle che rimbalzano. Una
        # stringa gia' dichiarata in `disegnate` — le 12 chiavi di classe di
        # `action.hsp`, la «Jo» del jolly — dovrebbe altrimenti essere
        # dichiarata due volte, e due dichiarazioni della stessa cosa
        # divergono: e' la 136a, dove un file contato due volte ha sbagliato
        # un referto di 800 stringhe.
        distinte = viste - gia
        righe.append({
            "file": nome,
            "saltate": len(tutte),
            "scoperte": 0 if meccanismo else len(scoperte),
            "viste": len(viste),
            "distinte": len(distinte),
            "meccanismo": meccanismo,
            "campioni": sorted(distinte)[:3],
        })
    return righe


def confronto() -> list[dict]:
    """Quante ne aggiunge questa rete a `disegnate`, file per file.

    ⚠️ La domanda non e' «quante ne trova»: e' «quante ne trova **che l'altra
    non trovava**». Un censimento nuovo che ripete quel che c'era gia' e' un
    numero in piu' da mantenere e zero stringhe in piu' a schermo.
    """
    toppe, rese, invarianti = _da_sottrarre()
    fuori = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        nome = percorso.name
        if nome in copertura.MECCANISMI:
            continue
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        righe_del_file = testo.split("\n")

        mie = set()
        for numero, _etichetta, _bersaglio, valore in scoperte_di(nome, testo,
                                                                  morte):
            if valore in rese.get(nome, set()) or valore in invarianti:
                continue
            if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
                continue
            mie.add(valore)
        sue = set()
        for numero, _comando, valore in disegnate.tutte_di(nome, testo, morte):
            if valore in rese.get(nome, set()) or valore in invarianti:
                continue
            if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
                continue
            sue.add(valore)
        if mie or sue:
            fuori.append({"file": nome, "salti": mie, "disegnate": sue,
                          "solo_mie": mie - sue, "solo_sue": sue - mie})
    return fuori


def problemi(righe: list[dict] | None = None) -> list[str]:
    """Le tre cose che accendono il cancello. Lista vuota = tutto dichiarato.

    ⚠️ E' lo stesso cancello di `copertura.problemi` e `disegnate.problemi`,
    sul terzo metro. Un censimento senza cancello e' una misura che invecchia:
    le 58 etichette della 137a, le 25 della 138a e le 51 della 140a sono state
    trovate a mano tutte e tre le volte.
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
                "%s: %d stringhe che arrivano a schermo di rimbalzo e non "
                "raggiungono ne' il dizionario ne' una toppa, e nessuna "
                "dichiarazione in salti.py. Esempio: %r"
                % (nome, riga["distinte"], riga["campioni"][0][:60]))
        elif dichiarata.scoperte != riga["distinte"]:
            guai.append(
                "%s: dichiarate %d stringhe che saltano a schermo, nel "
                "sorgente ne sono %d. Il monte si e' mosso sotto la "
                "dichiarazione, oppure il conto era sbagliato."
                % (nome, dichiarata.scoperte, riga["distinte"]))
    for nome in DICHIARATI:
        riga = per_nome.get(nome)
        if riga is None or riga["distinte"] == 0:
            guai.append("%s: dichiarato in salti.py ma nel sorgente non ha "
                        "piu' nessuna stringa che salta a schermo. La riga va "
                        "tolta." % nome)
    return guai


def _referto_file(nome: str) -> None:
    percorso = percorsi.SORGENTE_HSP / nome
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso)
    toppe, rese, invarianti = _da_sottrarre()
    righe_del_file = testo.split("\n")
    gia = {t[2] for t in disegnate.tutte_di(nome, testo, morte)}
    for numero, etichetta, bersaglio, valore in scoperte_di(nome, testo, morte):
        stato = "  "
        if valore in rese.get(nome, set()) or valore in invarianti:
            stato = "✅"
        elif righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
            stato = "🩹"
        elif valore not in gia:
            stato = "⭐"
        print("%s %6d  *%-22s %-16s %r"
              % (stato, numero, etichetta[:22], bersaglio[:16], valore))
    print("\n  ⭐ = la vede questa rete e non `disegnate`")


def _referto_misti() -> None:
    print("  L'ALTRO ASSE: i letterali che portano giapponese e inglese"
          " INSIEME,\n  fuori da `lang()`. Non e' il salto, ed e' contato a"
          " parte apposta.\n")
    toppe, rese, invarianti = _da_sottrarre()
    totale = scoperti = 0
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        nome = percorso.name
        testo = percorso.read_bytes().decode("cp932")
        morte = righe_in_commento(percorso)
        righe_del_file = testo.split("\n")
        trovati = misti_di(nome, testo, morte)
        if not trovati:
            continue
        aperti = [t for t in trovati
                  if righe_del_file[t[0] - 1].strip() not in toppe.get(nome, set())
                  and t[2] not in rese.get(nome, set())
                  and t[2] not in invarianti]
        totale += len(trovati)
        scoperti += len(aperti)
        print("  %-24s %4d misti, %4d ancora scoperti   %s"
              % (nome, len(trovati), len(aperti),
                 [t[2] for t in aperti[:4]]))
    print("\n  totale: %d letterali misti, %d ancora scoperti" % (totale, scoperti))


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--file", metavar="NOME")
    analizzatore.add_argument("--confronto", action="store_true")
    analizzatore.add_argument("--misti", action="store_true")
    argomenti = analizzatore.parse_args()

    if argomenti.file:
        _referto_file(argomenti.file)
        return

    if argomenti.misti:
        _referto_misti()
        return

    if argomenti.confronto:
        print("  quel che il SALTO vede e `disegnate` no, e viceversa\n")
        print("  %-26s %8s %10s %9s %9s" % ("file", "salti", "disegnate",
                                            "solo qui", "solo la'"))
        print("  " + "-" * 68)
        totale_mie = totale_sue = totale_solo = 0
        for riga in sorted(confronto(), key=lambda r: -len(r["solo_mie"])):
            totale_mie += len(riga["salti"])
            totale_sue += len(riga["disegnate"])
            totale_solo += len(riga["solo_mie"])
            if not riga["solo_mie"]:
                continue
            print("  %-26s %8d %10d %9d %9d"
                  % (riga["file"], len(riga["salti"]), len(riga["disegnate"]),
                     len(riga["solo_mie"]), len(riga["solo_sue"])))
        print("\n  totale: %d scoperte dal salto, %d da `disegnate`,"
              " **%d che solo il salto vede**"
              % (totale_mie, totale_sue, totale_solo))
        return

    righe = censimento()
    guai = problemi(righe)
    print("  %-26s %9s %10s %8s %10s" % ("file", "saltate", "scoperte",
                                         "viste", "solo qui"))
    print("  " + "-" * 70)
    for riga in sorted(righe, key=lambda r: -r["distinte"]):
        if not riga["distinte"]:
            continue
        print("  %-26s %9d %10d %8d %10d   %s"
              % (riga["file"], riga["saltate"], riga["scoperte"],
                 riga["viste"], riga["distinte"],
                 riga["campioni"][0][:34] if riga["campioni"] else ""))
    print("\n  testo che salta a schermo : %d siti"
          % sum(r["saltate"] for r in righe))
    print("  scoperto                  : %d siti, %d stringhe distinte"
          % (sum(r["scoperte"] for r in righe),
             sum(r["viste"] for r in righe)))
    print("  che `disegnate` NON vede  : **%d stringhe distinte, su %d file**"
          % (sum(r["distinte"] for r in righe),
             sum(1 for r in righe if r["distinte"])))
    print("\n  ⚠️ L'ambito di un nome generico e' il BLOCCO: `s` riempito in un"
          "\n     sottoprogramma e disegnato in un altro resta fuori. E' il"
          " prezzo\n     dichiarato di poter guardare `s` invece di buttarlo"
          " via.\n  ⚠️ I letterali MISTI (giapponese e inglese nella stessa"
          " stringa)\n     sono un altro asse e si contano con `--misti`.")
    for guaio in guai:
        print("\n  ⚠️ %s" % guaio)
    if not guai:
        print("\n  salti: ogni stringa che rimbalza a schermo o e' coperta, o"
              " e' dichiarata")
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
