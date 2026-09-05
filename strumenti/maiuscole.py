# strumenti/maiuscole.py
"""`cnven()` mette la maiuscola in ogni lingua che non sia il giapponese.

## Che cosa fa davvero

`init.hsp:191`. In build giapponese restituisce la stringa tale e quale; in
ogni altra **alza la prima lettera**. E' il modo in cui Elona ottiene gratis la
maiuscola d'inizio frase per un valore che arriva da una tabella:

    txt cnven(cdatan(CDATAN_NAME, rc)) + " torna in vita!"   ->  «Gwen torna in vita!»

⚠️⚠️ **Ma in italiano lo stesso trucco produce una maiuscola in mezzo a una
frase**, perche' la nostra lingua compone diversamente da quella inglese:

    chat.hsp:25573   s += cnven(gendername(tc))   ->  «Tomdecker il cittadino Femmina»

`text.hsp:124` rende `strfemale` con la minuscola giusta, «femmina»; e' `cnven`
che gliela alza, dieci file piu' in la', in un sito che nessun dizionario
raggiunge perche' li' non c'e' nessuna `lang()`.

💡 **E' la stessa forma di difetto delle gronde** (`strumenti/gronde.py`): il
danno non sta nella stringa, sta in **come il codice la monta insieme a
un'altra**, e nessuna rete che guardi le stringhe una per una lo puo' vedere.

## Il criterio

Non e' «cnven e' sbagliato»: dipende da **dove sta nell'espressione**.

- **in testa** — `cnven(...)` e' la prima cosa che finisce nella stringa
  disegnata. La maiuscola e' giusta: e' inizio frase, o e' un'etichetta che sta
  per conto suo in una casella (`s(3) = cnven(strfemale)`, la riga «Sesso»
  della scheda). ✅
- **appeso** — prima di `cnven(...)`, nella stessa espressione, c'e' gia'
  dell'altro testo unito con `+`. La maiuscola cade in mezzo a una frase. ❌
- **accumulato** — la riga fa `x += cnven(...)`. Se l'accumulatore era vuoto
  siamo nel primo caso, se no nel secondo, e **il sorgente da solo non lo dice**:
  va guardato a mano. ⚠️

⚠️ Il conto degli «appesi» non e' il conto dei difetti: e' il conto delle righe
da guardare. Un `+` dopo i due punti o dopo un trattino («Res. » + cnven(s))
regge la maiuscola meglio che dentro un sintagma.
"""
import re
import sys
from pathlib import Path

from strumenti import estrai
from strumenti import percorsi

IN_TESTA = "in testa"
APPESO = "appeso"
ACCUMULATO = "accumulato"

# I siti «appesi» o «accumulati» gia' guardati, con il motivo per cui la
# maiuscola li' regge. ⚠️ La guardia non chiede zero appesi — chiede che questo
# elenco non si allunghi da solo: un sito nuovo e' una riga da giudicare, non
# per forza un difetto. E' la stessa forma di `fuori_misura_inglese` in
# `menu_dialogo`: il conto non e' il verdetto, e' l'elenco da leggere.
GIUDICATI = {
    ("blend.hsp", 1299): "il nome della ricetta dopo «Ricetta: »: dopo i due "
                         "punti la maiuscola regge, ed e' un nome",
    # ⚠️ :18813 NON e' piu' qui, ed e' la terza volta che succede per la stessa
    # ragione. Il permesso diceva «chat.hsp non e' ancora tradotto: si giudica
    # quando ci arriva il lotto». Il lotto e' arrivato nella 82a, la resa e'
    # «(Annuisce, con aria imbarazzata)» — la maiuscola sta nel letterale, e
    # `cnven(he(tc))` e' sparita del tutto insieme al pronome inglese che
    # avvolgeva. Il sito non e' piu' appeso perche' **non esiste piu'**.
    # ⚠️ :22375 e :24739 NON sono piu' qui, e il motivo vale piu' della riga:
    # questa rete legge la BUILD, non il sorgente pinnato. Le due rese della 77a
    # («La gattina passa di mano.», «La gattina entra al tuo servizio.») mettono
    # il nome IN TESTA, quindi i due siti sono usciti dagli appesi da soli e il
    # loro permesso sarebbe rimasto appeso al vuoto. L'ha detto
    # `test_i_giudicati_esistono_ancora`, che esiste apposta.
    ("chat.hsp", 24713): "il prezzo dello schiavo, dopo «vediamo nella "
                         "stalla...»: dopo i puntini la maiuscola regge (77a)",
    ("command.hsp", 4436): "cnven(txtcopy), la nota che segue la frase "
                           "gridata: apre una frase sua",
    # ⚠️ Era :10948 fino alla 97a, ed e' sempre la stessa riga, riletta nella
    # build: a spostarla di **6** e' la toppa di `book.txt` della 98a, che a
    # `command.hsp:8371` sostituisce un `noteload` con sette righe (il ramo
    # `exist` + il ripiego). Terza volta che questa coordinata si muove per una
    # toppa che cresce sopra di lei — 83a, 96a, 98a — e il test ha ragione a
    # scattare tutt'e tre. ⭐ E adesso la regolarita' e' visibile: le toppe dei
    # **file dati** sono le uniche multiriga del progetto, quindi ognuna che
    # tocchi un file con un permesso appeso sposta il pavimento di 6. Le prime
    # tre (board -> init.hsp, talk -> text.hsp, exhelp -> help.hsp) non lo
    # avevano fatto solo perche' non c'erano permessi in quei file.
    ("command.hsp", 10954): "«Res. » piu' il nome dell'elemento: dopo il punto "
                            "abbreviativo la maiuscola regge",
    # ⚠️ Era :2321 fino alla 82a, ed e' la stessa identica riga: a spostarla di
    # 31 righe sono state le TOPPE della 83a, che infilano il plurale e la spia
    # del nome non identificato piu' su nello stesso file. E' una causa nuova —
    # le tre volte precedenti un permesso era morto perche' il sito era
    # cambiato, qui il sito e' intatto e si e' mosso il pavimento. 💡 La chiave
    # di questa tabella e' una coordinata nella BUILD, e la build la muoviamo
    # noi: ogni toppa che aggiunge righe sopra un sito appeso fa scattare
    # `test_i_giudicati_esistono_ancora`. Il test ha ragione a scattare — un
    # permesso appeso al vuoto e' peggio di nessun permesso — e il rimedio e'
    # rileggere la riga, non allentare il test.
    # ⚠️ Era :2321 fino alla 82a, :2352 fino alla 96a e :2366 fino alla 130a, ed
    # e' sempre la stessa riga: nella 96a a spostarla di 14 sono state le righe
    # che la toppa dell'articolo si e' presa per dare a ciascuno dei tredici
    # **fiori selvatici** il suo («un rosa» -> «una rosa»); nella 131a a
    # spostarla di 2 e' stata la guardia che impedisce all'articolo del nome
    # ignoto di scavalcare quello del nome vero quando e' vuoto («a borraccia
    # filtrante» -> «una borraccia filtrante»). Terza volta che questa coordinata
    # si muove per una toppa che cresce sopra di lei, e il test ha ragione a
    # scattare tutt'e tre le volte: la riga si rilegge, il permesso regge, e la
    # coordinata si aggiorna.
    # ⭐ 131a: e proprio scattando ha trovato un guasto che non era suo. Il
    # primo giro spostava la riga di **-12**, non di +2, perche' rigenerando le
    # toppe erano spariti i tredici articoli dei fiori: stavano scritti a mano
    # dentro una toppa `generata`, e `genera_toppe_nomi.py` sostituisce le
    # proprie a ogni giro. Adesso i fiori stanno nel generatore
    # (`articolo_del_fiore`). Il test dei giudicati e' l'unica cosa che se ne
    # e' accorta.
    # ⚠️ 142a: era :2366 fino alla 130a, :2368 fino alla 141a, ed e' sempre la
    # stessa riga — riletta nella build, dice ancora `lang("[" + mtname(...) +
    # "製]", "[" + cnven(mtname(...)) + "]")`. A spostarla di **6** sono le
    # quattro toppe che sciolgono i rinvii di questo file: quella del succo
    # cresce di 5 righe (16 -> 21, la testa italiana va davanti e il frutto la
    # segue) e quella della taglia del pesce di 1 (il conto in centimetri esce
    # in una riga sua). Quarta volta che questa coordinata si muove per una
    # toppa che cresce sopra di lei, e il test ha ragione a scattare tutt'e
    # quattro.
    ("item_func.hsp", 2374): "il tassello del materiale, «[Mithril]». Fa parte "
                             "del muro del materiale, che vuole il suo giro: "
                             "la postposizione italiana («spada DI mithril») "
                             "sposta il sito, non solo la maiuscola",
    ("main.hsp", 4296): "la lapide, «Vernis - Ucciso da ...»: dopo il trattino "
                        "comincia una frase",
    ("init.hsp", 289): "e' la funzione che serve a mettere la maiuscola: "
                       "cap_out la vuole",
}

_CNVEN = re.compile(r"\bcnven\(")


def _posizione(riga: str, inizio: int) -> str:
    """Dove sta il `cnven(` che comincia a `inizio` dentro la sua espressione.

    Si cammina a ritroso dal `cnven(` fino al confine dell'espressione — un
    `=`, una virgola di argomento, la parentesi che apre la chiamata che ci
    contiene, o l'inizio della riga. Per strada:

    - un `+` a profondita' zero vuol dire che davanti c'e' gia' del testo
    - un `+=` vuol dire che il testo davanti c'e' **forse**, e non lo sappiamo

    ⚠️ Si salta quel che sta dentro le virgolette: un `+` dentro una battuta
    non e' una concatenazione.
    """
    dentro = estrai._dentro_stringa(riga)
    profondita = 0
    i = inizio - 1
    while i >= 0:
        c = riga[i]
        if dentro[i]:
            i -= 1
            continue
        if c == ")":
            profondita += 1
        elif c == "(":
            if profondita == 0:
                return IN_TESTA
            profondita -= 1
        elif profondita == 0:
            if c == "+":
                if i > 0 and riga[i - 1] == "+":   # l'incremento, non la somma
                    i -= 2
                    continue
                return APPESO
            if c == "=":
                return ACCUMULATO if i > 0 and riga[i - 1] == "+" else IN_TESTA
            if c == ",":
                return IN_TESTA
        i -= 1
    return IN_TESTA


def siti(radice: Path | None = None) -> list[dict]:
    """Tutti i `cnven(` dei sorgenti, classificati."""
    cartella = radice or percorsi.BUILD_HSP
    trovati = []
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = percorso.read_bytes().decode("cp932").splitlines()
        for numero, riga in enumerate(righe, 1):
            for trovato in _CNVEN.finditer(riga):
                trovati.append({
                    "file": percorso.name,
                    "riga": numero,
                    "dove": _posizione(riga, trovato.start()),
                    "testo": riga.strip(),
                })
    return trovati


def appesi(radice: Path | None = None) -> list[dict]:
    """I siti dove la maiuscola cade in mezzo a una frase italiana."""
    return [s for s in siti(radice) if s["dove"] == APPESO]


def accumulati(radice: Path | None = None) -> list[dict]:
    """I `+=`, che il sorgente da solo non sa classificare."""
    return [s for s in siti(radice) if s["dove"] == ACCUMULATO]


def da_guardare(radice: Path | None = None) -> list[dict]:
    """I siti appesi o accumulati che nessuno ha ancora giudicato."""
    return [s for s in siti(radice)
            if s["dove"] in (APPESO, ACCUMULATO)
            and (s["file"], s["riga"]) not in GIUDICATI]


def main(argv: list[str] | None = None) -> int:
    tutti = siti()
    per_dove: dict[str, int] = {}
    for s in tutti:
        per_dove[s["dove"]] = per_dove.get(s["dove"], 0) + 1

    for dove in (IN_TESTA, APPESO, ACCUMULATO):
        print("  %-12s %4d" % (dove, per_dove.get(dove, 0)))

    for titolo, elenco in (("APPESI — la maiuscola cade in mezzo alla frase", appesi()),
                           ("ACCUMULATI — da guardare a mano", accumulati())):
        if not elenco:
            continue
        print("\n%s" % titolo)
        for s in elenco:
            print("  %-22s %s" % ("%s:%d" % (s["file"], s["riga"]), s["testo"][:118]))

    nuovi = da_guardare()
    if nuovi:
        print("\n⚠️ SITI NUOVI, mai giudicati:")
        for s in nuovi:
            print("  %-22s %s" % ("%s:%d" % (s["file"], s["riga"]),
                                  s["testo"][:110]))
    print("\ncnven() in tutto: %d siti, di cui %d appesi e %d accumulati; "
          "%d gia' giudicati, %d da guardare"
          % (len(tutti), len(appesi()), len(accumulati()),
             len(GIUDICATI), len(nuovi)))
    return 1 if nuovi else 0


if __name__ == "__main__":
    sys.exit(main())
