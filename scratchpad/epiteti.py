# -*- coding: utf-8 -*-
"""Gli epiteti generati: il QUINDICESIMO punto cieco, e il primo fuori dai sorgenti.

`etc.hsp:335` carica il vocabolario degli epiteti da un **file dati esterno**:

    noteload exedir + lang("data\\ndata.csv", "data\\ndata-e.csv")

cioe' da `C:\\Games\\Elona\\elonaplus2.31\\data\\ndata-e.csv`, che non sta nei
sorgenti HSP e che **nessuno strumento del progetto puo' vedere**: leggono tutti
`.hsp`. Sono 365 righe e **950 parole distinte** di inglese vivo.

⚠️ **Non e' solo l'epiteto del giocatore.** `random_title()` genera anche:

    adv.hsp:225                   il nome di OGNI avventuriero PNG
    command.hsp:17527             il nome della squadra
    chat.hsp:22497                il nome di certe mappe
    custom_nefiatypes.hsp:505     i PNG delle nefia speciali
    action.hsp:4589, :5206        e altri due siti

## La griglia

Ogni riga e' una famiglia di sinonimi. Le colonne hanno ruoli diversi:

    colonne 0-1    SOSTANTIVI    prince/duke, danger/risk, sadness/sorrow
    colonne 2-9    MODIFICATORI  dangerous, risky, unsafe, sword wielding
    colonna 14     la CATEGORIA  (人 persona, 形 aggettivo, 具 arnese, 万能 jolly)

La categoria serve a non accoppiare due parole della stessa famiglia
(`etc.hsp:473`), tranne quando una delle due e' 万能.

## La grammatica (etc.hsp:399-505, ramo `else` cioe' non giapponese)

    1. parola1 = una colonna a caso (rnd(14)) di una riga a caso
    2. se parola1 viene dalle colonne 0-1, cioe' e' un sostantivo:
         1 su 6  ->  parola1 + " of"           «Dusk of Copper»
         se no, 1 su 6  ->  "the " + parola1   e FINISCE   «The infinity»
    3. parola2 = colonna 0 o 1 (sempre un sostantivo) di un'altra riga,
       di categoria diversa
    4. risultato = parola1 + " " + parola2     «Corrupted Wolf»
    5. se il risultato arriva a 28 caratteri, si ributta tutto e si rifa'

⭐ **La prova che questa lettura e' giusta non e' un ragionamento: sono i 16
epiteti veri** della schermata di collaudo della 64a, che si scompongono tutti
nella griglia. Vedi `prova_sulla_schermata()`, che e' la regola della 61a --
gli strumenti si provano dove si sa gia' che cosa deve venire fuori.

## Perche' in italiano non basta tradurre le parole

La forma inglese e' **modificatore + testa**; l'italiano vuole **testa +
modificatore**, con l'accordo di genere:

    Corrupted Wolf        ->  Lupo corrotto      (agg. accordato al maschile)
    Elegance Fairy        ->  Fata dell'eleganza (nome + preposizione articolata)
    Dusk of Copper        ->  Crepuscolo di rame (qui l'ordine e' gia' giusto)
    The infinity          ->  L'infinito         (articolo, non «the»)

Quindi il vocabolario italiano deve portare, per ogni parola, piu' di una forma
-- il genere del sostantivo, le due desinenze dell'aggettivo, la forma
preposizionale -- e `etc.hsp` va toppato perche' componga all'italiana. Vedi
`decisioni.md`.
"""
import csv
import io
import sys
from pathlib import Path

DATI = Path(r"C:\Games\Elona\elonaplus2.31\data\ndata-e.csv")

# I sedici epiteti della schermata di collaudo della 64a, letti a schermo.
SCHERMATA = [
    "Retard Tank",
    "Corrupted Wolf",
    "Dusk of Copper",
    "Abhorrent Thief",
    "Axe wielding Serpent",
    "Champion Destiny",
    "The infinity",
    "Coolness of Curse",
    "Dreaming Summoner",
    "Loved Priest",
    "Fire of Rapier",
    "Dagger Ring",
    "Patient of Dead",
    "Soul Mate",
    "Modern Judgment",
    "Elegance Fairy",
]


def griglia(percorso=DATI):
    """[(parole per colonna, categoria)] -- una voce per riga del CSV."""
    fuori = []
    with io.open(percorso, encoding="cp932", errors="replace", newline="") as f:
        for r in csv.reader(f):
            parole = [p.strip() for p in r[:14]]
            categoria = r[14].strip() if len(r) > 14 else ""
            fuori.append((parole, categoria))
    return fuori


def indice(g):
    """{parola minuscola: [(riga, colonna)]} su tutta la griglia."""
    fuori = {}
    for n, (parole, _) in enumerate(g):
        for c, p in enumerate(parole):
            if p:
                fuori.setdefault(p.lower(), []).append((n, c))
    return fuori


def scomponi(epiteto, idx):
    """Le scomposizioni dell'epiteto secondo la grammatica di `random_title`."""
    e = epiteto.strip()
    basso = e.lower()

    # forma «the X»: X e' un sostantivo (colonne 0-1)
    if basso.startswith("the "):
        resto = basso[4:]
        siti = [s for s in idx.get(resto, []) if s[1] < 2]
        if siti:
            return [("the", resto, siti)]
        return []

    # forma «A of B»: A sostantivo, B sostantivo
    if " of " in basso:
        a, b = basso.split(" of ", 1)
        sa = [s for s in idx.get(a, []) if s[1] < 2]
        sb = [s for s in idx.get(b, []) if s[1] < 2]
        if sa and sb:
            return [("of", (a, b), (sa, sb))]
        return []

    # forma «A B»: A qualsiasi colonna, B sostantivo. Il taglio fra le due
    # parole non e' per forza l'ultimo spazio -- «Axe wielding Serpent» ha un
    # modificatore di due parole -- quindi si provano tutti i tagli.
    fuori = []
    pezzi = basso.split(" ")
    for i in range(1, len(pezzi)):
        a = " ".join(pezzi[:i])
        b = " ".join(pezzi[i:])
        sa = idx.get(a, [])
        sb = [s for s in idx.get(b, []) if s[1] < 2]
        if sa and sb:
            fuori.append(("coppia", (a, b), (sa, sb)))
    return fuori


def prova_sulla_schermata():
    """⭐ La prova della 61a: la grammatica deve spiegare i 16 epiteti veri."""
    g = griglia()
    idx = indice(g)
    spiegati = 0
    print("--- i sedici epiteti della schermata della 64a")
    for e in SCHERMATA:
        letture = scomponi(e, idx)
        if letture:
            spiegati += 1
            forma = letture[0][0]
            pezzi = letture[0][1]
            print(f"   ok   [{forma:6s}]  {e:24s}  {pezzi}")
        else:
            print(f"   ⚠️    [       ]  {e:24s}  NON spiegato dalla griglia")
    print(f"\n   spiegati {spiegati} su {len(SCHERMATA)}")
    return spiegati == len(SCHERMATA)


def referto():
    g = griglia()
    parole = [p for parole, _ in g for p in parole if p]
    sostantivi = {p for parole, _ in g for p in parole[:2] if p}
    modificatori = {p for parole, _ in g for p in parole[2:] if p}
    categorie = {}
    for _, c in g:
        categorie[c] = categorie.get(c, 0) + 1

    print(f"vocabolario: {DATI}")
    print(f"  righe (famiglie di sinonimi) : {len(g)}")
    print(f"  parole                       : {len(parole)}  ({len(set(parole))} distinte)")
    print(f"  di cui sostantivi (col. 0-1) : {len(sostantivi)}")
    print(f"  di cui modificatori (col. 2+): {len(modificatori)}")
    print(f"  categorie                    : {len(categorie)}")
    print()
    ok = prova_sulla_schermata()
    if not ok:
        print("\n⚠️ la lettura della grammatica non regge: non fidarsi del resto")
    return ok


if __name__ == "__main__":
    sys.exit(0 if referto() else 1)
