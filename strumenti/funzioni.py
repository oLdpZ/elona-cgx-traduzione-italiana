# strumenti/funzioni.py
"""Classificazione delle funzioni HSP che compaiono nelle espressioni dinamiche.

Non tutte le chiamate dentro un'espressione dinamica sono contenuto. Alcune sono
grammatica **inglese**, e in italiano vanno tolte: `_s(tc)` restituisce la `s`
della terza persona, `your(tc)` il suffisso possessivo `'s`. Conservarle
significherebbe scrivere inglese dentro una frase italiana.

La distinzione, verificata leggendo `init.hsp` (Fase 1, task 1 — vedi
`.superpowers/sdd/2026-08-06-fase-1-ui-e-messaggi/task-1-report.md` per
l'elenco completo delle prove, incluso il giro di correzione):

- **morfologia**: restituisce sempre una stringa inglese nuda, mai passata da
  `lang()`, qualunque siano gli argomenti. Non si localizzera' mai. In
  italiano va tolta.
- **pronome per sito di chiamata**: `he`, `his`, `him` hanno *la stessa
  funzione* che si comporta diversamente a seconda del numero di argomenti
  con cui viene chiamata — non e' una proprieta' del nome, e' una proprieta'
  del sito. Il corpo di ciascuna (letto per intero in `init.hsp`) e':

      if ( <nome>_arg2 ) {
          ... return lang("...", "...") ...   # con secondo argomento
      }
      ... return "it" / "you" / "he" / ...    # senza: inglese nudo per sempre

  Una prima versione di questo modulo classificava `he/his/him` per nome
  (sempre "pronome facoltativo"), ignorando questa biforcazione: `his(tc)`
  (un argomento, MAI lang()) veniva trattata come i suoi rispettivi
  `his(tc, 1)` (due argomenti, sempre lang()), e la verifica non avrebbe
  segnalato un `his(tc)` a un argomento lasciato per sempre in inglese dentro
  una frase italiana. Sul sorgente intero (72 file) `his` compare 111 volte a
  un argomento contro 12 a due; `he` 22 contro 17; `him` 36 contro 0 — il caso
  "morfologia nuda" e' la maggioranza, non l'eccezione.
  Regola: **due argomenti -> contenuto** (si localizzera' con `init.hsp` in
  Fase 4, va conservata); **un argomento -> morfologia** (resta inglese per
  sempre, va tolta).

Tutto il resto e' contenuto e va conservato: perdere `name(tc)` significa
perdere il nome del personaggio dalla frase.

Casi verificati e lasciati fuori da entrambe le classi:

- `his2(EntityID)`: `if (EntityID==CHARA_PLAYER) return "your"` altrimenti
  `return name(EntityID)` — nel ramo non-giocatore restituisce il nome vero
  del personaggio, cioe' contenuto, non morfologia ne' pronome. A differenza
  di `he/his/him` non ha un secondo argomento con cui distinguere i siti (la
  sua firma e' `his2(EntityID)`, un solo parametro): non c'e' un sito "con
  lang()" da riconoscere, quindi la regola per sito non si applica. Resta
  contenuto per esclusione (comportamento di default). Non e' usata nei sei
  file di Fase 1 con l'argomento che farebbe restituire `name(...)`.
- `him2(EntityID)`, `his3(EntityID)`: firma a un solo parametro, nessun ramo
  `lang()` in nessun caso (letti per intero) — morfologia incondizionata,
  senza distinzione di sito perche' il sito non varia mai.
"""
import re

from strumenti.estrai import argomenti_di

# Verificate su init.hsp: restituiscono SEMPRE una stringa inglese nuda,
# mai attraverso lang(), qualunque siano gli argomenti. _s/_s2/_s3/_s4 sono
# varianti della stessa desinenza di terza persona ("s"/"es"/""); him2/his3/
# its/its2/your2/yourself sono varianti di possessivi e riflessivi inglesi
# che, a differenza di he/his/him, non hanno alcun ramo che passa da lang().
# have/does sono coniugazioni verbali (has/have, do/does), stesso discorso.
# is2 e' la copula accordata al NUMERO invece che alla persona (are/is,
# init.hsp:1768): mancava, e la guardia pretendeva che una frase italiana
# conservasse un "is". L'elenco e' ora verificato da un test contro init.hsp.
#
# ⚠️⚠️ **cnvrank e' morfologia, e la sonda del test non poteva vederla** (85a).
# `init.hsp:149` e' la desinenza ordinale inglese: `if ( jp ) { return "" +
# rank }`, e fuori di li' appende `st`/`nd`/`rd`/`th` al numero. E' lo stesso
# mestiere di `_s`, ma la sonda cercava funzioni i cui `return` fossero
# **letterali nudi** — e qui i return CONCATENANO l'argomento col suffisso,
# quindi le sfuggiva. Il prezzo era gia' a schermo: quattro rese italiane
# scrivevano «Rango del museo: 2nd» e «Livello di sotterraneo piu' profondo:
# 25th». La resa giusta concatena l'argomento nudo, e quando l'argomento e'
# un'espressione va fra PARENTESI — HSP valuta senza precedenza (provato al
# banco, `scratchpad/_85-banco-cnvrank.py`).
MORFOLOGIA_INGLESE = frozenset({
    "_s", "_s2", "_s3", "_s4",
    "is", "is2", "was", "your", "your2",
    "have", "does",
    "him2", "his3", "its", "its2", "yourself",
    "cnvrank",
})

# Pronomi il cui esito dipende dal sito di chiamata, non dal nome: con un
# secondo argomento passano da lang() (contenuto), senza restano per sempre
# inglese nudo (morfologia). Vedi la spiegazione estesa sopra.
PRONOMI_PER_SITO = frozenset({"he", "his", "him"})

# ⚠️ Chiamate che non portano NESSUN dato: aggiungono solo punteggiatura
# intorno a quello che ricevono. `cnvtalk` (`module.hsp`) fa esattamente
# `return "\"" + s + "\" "`, cioe' mette le virgolette al discorso diretto.
#
# Vanno attraversate invece che registrate. Registrarle e' un difetto vero,
# trovato nella 72a su `screen.hsp:1442`: il giapponese saluta il giocatore per
# nome — 「共に戦うぞ、" + cdatan(CDATAN_NAME, CHARA_PLAYER) + "！」 — e l'inglese
# quel nome l'aveva perso. Rimettendolo in italiano, che vuol dire metterlo
# **dentro** le virgolette, cambiava il testo dell'argomento di `cnvtalk`, e la
# guardia degli argomenti leggeva l'intera `cnvtalk(...)` come una chiamata che
# «non viene da monte» — mentre l'unica chiamata di contenuto, `cdatan`, da
# monte ci veniva eccome, dal ramo giapponese.
#
# 💡 Il difetto non era nella regola ma nella **classificazione**: una funzione
# che non porta dati non e' una chiamata di contenuto, e trattarla come tale
# rende invisibile il contenuto che ha dentro.
#
# ⭐ **`cnven` e' della stessa famiglia, ed e' entrata nella 82a.** `init.hsp:191`:
# in build giapponese restituisce l'argomento tale e quale, altrimenti ne alza
# la prima lettera. Non porta nessun dato — porta una maiuscola.
#
# Il difetto che ha corretto sta in `chat.hsp:18813`, `"(" + cnven(he(tc)) +
# " nodded shyly.)"`. Li' dentro **non c'e' niente da conservare**: `he(tc)` a
# un argomento e' morfologia inglese e va tolta, e con lei se ne va la
# maiuscola che le stava sopra, perche' in italiano la frase comincia con un
# verbo scritto per esteso. Ma `funzioni_di_contenuto` registrava `cnven` fra
# le attese, e nessuna resa italiana poteva soddisfarla: la voce era
# intraducibile, come «Manuscript production» prima della maschera dei
# letterali. Sul sorgente pinnato `cnven(he(...))` compare **16 volte**: non e'
# un caso limite.
#
# ⚠️ E lasciar cadere `cnven` non allenta nessuna guardia, perche' la maiuscola
# ha una rete tutta sua: `strumenti/maiuscole.py` legge la **build** e giudica
# ogni sito per posizione (in testa / appeso / accumulato). Le due misure non
# si sovrappongono — una guarda che il DATO sopravviva alla traduzione, l'altra
# che la MAIUSCOLA cada nel posto giusto — e pretenderle tutt'e due dalla stessa
# lista rendeva impossibile la resa giusta.
TRASPARENTI = frozenset({"cnvtalk", "cnven"})

CHIAMATA = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def _fine_chiamata(espressione: str, apertura: int) -> int:
    """L'indice subito dopo la parentesi che chiude quella aperta in `apertura`.

    Se le parentesi non si chiudono (espressione troncata), ritorna la fine
    della stringa: meglio sovrastimare la porzione da saltare che classificare
    come contenuto la coda di una chiamata di morfologia.
    """
    livello = 0
    for i in range(apertura, len(espressione)):
        if espressione[i] == "(":
            livello += 1
        elif espressione[i] == ")":
            livello -= 1
            if livello == 0:
                return i + 1
    return len(espressione)


def _maschera_letterali(espressione: str) -> str:
    """La stessa espressione con il **testo dentro le stringhe** ridotto a spazi.

    ⚠️ Serve perche' `CHIAMATA` non sa distinguere il codice dal testo, e una
    parola seguita da una parentesi **dentro una stringa** le sembra una
    chiamata. `"Manuscript production (" + gdata(...) + " inspiration) "`
    faceva contare una funzione `production`, e la resa italiana — «Scrittura
    di manoscritti (» — ne faceva contare una di nome `manoscritti`: due
    elenchi diversi, e la voce era intraducibile. Qualunque resa con una
    parentesi dopo una parola sarebbe stata rifiutata.

    Le posizioni non cambiano (ogni carattere mascherato diventa uno spazio),
    quindi gli indici valgono ancora sull'originale. Sparisce anche la
    punteggiatura dentro le stringhe, ed e' voluto: una parentesi o una virgola
    scritte nel testo non aprono un argomento.
    """
    fuori = []
    dentro = False
    scappa = False
    for carattere in espressione:
        if scappa:
            fuori.append(" ")
            scappa = False
            continue
        if carattere == "\\" and dentro:
            fuori.append(" ")
            scappa = True
            continue
        if carattere == '"':
            fuori.append('"')
            dentro = not dentro
            continue
        fuori.append(" " if dentro else carattere)
    return "".join(fuori)


def _classifica(espressione: str) -> tuple[list[str], list[str]]:
    """Per ogni chiamata dell'espressione, decide se e' contenuto o morfologia.

    Ritorna (contenuto, morfologia): i nomi delle chiamate, non ordinati e con
    ripetizioni, nell'ordine in cui compaiono. Le chiamate a `he/his/him`
    guardano il numero di argomenti al sito, non il solo nome.

    ⚠️ Gli **argomenti di una chiamata di morfologia non sono contenuto**, e non
    entrano nel conteggio. Una funzione di morfologia non stampa mai cio' che
    riceve: `is`, `was`, `_s`, `your`, `have`, `does`, `yourself` e le altre
    restituiscono una parola inglese fissa, scelta guardando l'argomento e
    basta. Quindi in `name(gdata(R)) + is(gdata(R)) + " using it."` il secondo
    `gdata` non arriva a schermo: e' l'impianto idraulico della copula inglese.
    Toglierlo e' obbligatorio insieme a `is()`, e pretenderlo nell'italiano
    rendeva la voce intraducibile — nessuna resa corretta poteva passare.
    Trovato traducendo le dinamiche di `action.hsp`, dove la morfologia annidata
    compare per la prima volta in quantita'.
    """
    contenuto: list[str] = []
    morfologia: list[str] = []
    salta_fino_a = 0
    # il testo dentro le stringhe non e' codice: vedi _maschera_letterali
    espressione = _maschera_letterali(espressione)
    for corrispondenza in CHIAMATA.finditer(espressione):
        if corrispondenza.start() < salta_fino_a:
            continue
        nome = corrispondenza.group(1)
        apertura = corrispondenza.end() - 1
        if nome in MORFOLOGIA_INGLESE:
            morfologia.append(nome)
            salta_fino_a = _fine_chiamata(espressione, apertura)
        elif nome in TRASPARENTI:
            # ⚠️ Attraversata, non registrata, e **non** si salta il suo interno:
            # e' la differenza con la morfologia qui sopra. Vedi TRASPARENTI.
            # Fino alla 82a questa classe la conosceva solo
            # `chiamate_di_contenuto`, e le due funzioni dello stesso modulo
            # davano risposte diverse sulla stessa espressione.
            continue
        elif nome in PRONOMI_PER_SITO:
            argomenti = argomenti_di(espressione, apertura)
            if argomenti is not None and len(argomenti) >= 2:
                contenuto.append(nome)
            else:
                morfologia.append(nome)
                salta_fino_a = _fine_chiamata(espressione, apertura)
        else:
            contenuto.append(nome)
    return contenuto, morfologia


def funzioni_di_contenuto(espressione: str) -> list[str]:
    """Le chiamate che devono sopravvivere alla traduzione, ordinate."""
    contenuto, _ = _classifica(espressione)
    return sorted(contenuto)


def chiamate_di_contenuto(espressione: str) -> list[str]:
    """Le chiamate di contenuto **con i loro argomenti**, ordinate.

    `funzioni_di_contenuto` confronta i soli **nomi**: `name(cc)` e `name(tc)`
    le sembrano la stessa cosa, e una resa che scambia i due personaggi passa
    ogni guardia. E' un difetto trovato il 2026-08-11 in `proc.hsp:763`: il
    sorgente dice `name(tc)` — lo spettatore che tira il sasso all'artista — e
    la resa diceva `name(cc)`, cioe' l'artista che tira il sasso a se stesso.
    Il compilatore non ha niente da dire, la prova d'identita' nemmeno: `cc` e
    `tc` sono due variabili valide, e il messaggio esce a schermo col nome
    sbagliato.

    Il testo **dentro** le stringhe non conta come argomento: `cnvtalk("Ciao")`
    e `cnvtalk("Hi")` sono la stessa chiamata, con il contenuto tradotto. Si
    confronta la forma mascherata, dove i letterali sono spazi, e gli spazi si
    togliono perche' `name(tc)` e `name( tc )` sono la stessa chiamata.
    """
    mascherata = _maschera_letterali(espressione)
    fuori: list[str] = []
    salta_fino_a = 0
    for corrispondenza in CHIAMATA.finditer(mascherata):
        if corrispondenza.start() < salta_fino_a:
            continue
        nome = corrispondenza.group(1)
        apertura = corrispondenza.end() - 1
        fine = _fine_chiamata(mascherata, apertura)
        if nome in MORFOLOGIA_INGLESE:
            salta_fino_a = fine
            continue
        # ⚠️ Trasparente: NON si registra e NON si salta il suo interno. La
        # differenza con la morfologia qui sopra e' tutta li' — quella nasconde
        # anche quel che contiene, questa lascia vedere dentro.
        if nome in TRASPARENTI:
            continue
        if nome in PRONOMI_PER_SITO:
            argomenti = argomenti_di(mascherata, apertura)
            if argomenti is None or len(argomenti) < 2:
                salta_fino_a = fine
                continue
        fuori.append(re.sub(r"\s+", "", mascherata[corrispondenza.start():fine]))
    return sorted(fuori)


def morfologia_residua(espressione: str) -> list[str]:
    """I nomi di morfologia inglese presenti nell'espressione, ordinati e senza
    ripetizioni: se compaiono nell'italiano tradotto e' un problema, non una
    scelta stilistica (a differenza dei pronomi, che sono facoltativi)."""
    _, morfologia = _classifica(espressione)
    return sorted(set(morfologia))
