# strumenti/battute.py
"""Il repertorio di battute di ogni creatura, per comporre un lotto.

`db_creature.hsp` mescola due corpora — vedi `creature.py` — e le **battute**
sono il piu' grosso: 2.465 firme, di cui 1.919 ancora da rendere al 2026-08-11.
Sono anche le stringhe a **frequenza piu' alta di tutto il gioco**: `ai.hsp:766`
le fa uscire ogni 5 turni con probabilita' 1 su 4 per ogni creatura entro dieci
caselle dal giocatore. Un nome si legge una volta, quando incontri la creatura;
una battuta oziosa a ogni turno in cui ti sta accanto.

## Perche' il lotto prende creature intere

Ogni creatura ha fino a cinque classi di battuta, e il database le dichiara col
suo `dbmode`:

| `dbmode` | quando esce |
|---|---|
| `DBMODE_FLAVOR_PASSIVE` | sta lì tranquilla e chiacchiera |
| `DBMODE_FLAVOR_ANGERED` | l'hai fatta arrabbiare |
| `DBMODE_FLAVOR_DEATH` | muore |
| `DBMODE_FLAVOR_KILL` | ha ucciso qualcuno |
| `DBMODE_FLAVOR_WELCOME` | torni a casa e lei ti sta aspettando |

⚠️ **Il registro di un mostro e' uno**, e scriverne una situazione per volta lo
spezza: la stessa creatura direbbe «Che daffare! Che FELICITÀ!» da tranquilla e
poi qualcosa di tono diverso in punto di morte, scritto in un altro giorno da
un'altra mano. Quindi il lotto prende **creature intere in ordine di riga**, non
una classe alla volta su tutto il file.

⚠️ **E il nome italiano della creatura va tenuto sotto gli occhi**, perche' le
battute lo citano: chi parla di se' come «sorella maggiore» ha un nome che porta
il bisticcio 「修道姉」, e la parentela in prosa segue `glossario.md`, non il nome.
I nomi sono tutti in dizionario dalla Fase 2: qui si leggono e non si reinventano.

## Perche' l'ordine e' per livello e non per riga

⚠️ **L'ordine di riga e' cieco alla frequenza.** `db_creature.hsp` elenca le
creature nell'ordine in cui sono state aggiunte al gioco, che non ha niente a
che vedere con quante volte il giocatore le incontra: mette l'accattone di
livello 2, che sta in ogni citta', accanto a `<Jure la Benedetta>` di livello
1200, che come creatura non si incontra mai. Misurato l'11/08: delle 1.975 voci
che restano, **605 stanno su creature di livello 1-10** — quasi tutte `/man/`,
gli abitanti delle citta' che ti camminano accanto per decine di turni — e
**528 su creature oltre il livello 100**.

Il livello e' il metro perche' decide in quale fascia di Nefia la creatura puo'
comparire, e le creature di citta' lo hanno bassissimo. A parita' di livello
viene prima chi ha piu' battute: una creatura con quindici rese rende piu' di
una con una sola.

⚠️ **Non e' una misura esatta della frequenza, ed e' apposta.** Non esiste nel
sorgente un campo «quanto spesso esce» — `DBSPEC_CHARA_RARE` non lo e', lo
leggono solo il valore del cadavere (`item_func.hsp:2295`) e la mappa utente. Il
livello e' una **procura**: sbaglia sui casi singoli, ma sposta il lavoro dalla
coda verso la testa, che e' quello che serve. `--per-riga` rimette l'ordine
vecchio.

## Uso

    python -m strumenti.battute                 # il primo lotto da fare, ~60 voci
    python -m strumenti.battute --da 10         # salta le prime 10 creature
    python -m strumenti.battute --tetto 100     # un lotto piu' grosso
    python -m strumenti.battute --conto         # solo il totale per classe
    python -m strumenti.battute --per-riga      # l'ordine vecchio, di riga

Legge `lavoro/_c.jsonl`, che si rigenera con

    python -m strumenti.estrai db_creature.hsp --da-tradurre --uscita lavoro/_c.jsonl
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from strumenti import percorsi

FILE = "db_creature.hsp"
ESTRAZIONE = percorsi.LAVORO_LOTTI / "_c.jsonl"

_DBMODE = re.compile(r"dbmode == (DBMODE_\w+)")
_DBID = re.compile(r"dbid == (CREATURE_ID_\w+)")
_LIVELLO = re.compile(r"cdata\(CDATA_LEVEL, rc\)\s*=\s*(\d+)")

# a una creatura che non dichiara il livello si da' il piu' alto, cosi' finisce
# in coda invece di scavalcare per un dato mancante
LIVELLO_IGNOTO = 10**6

# come si chiamano le cinque classi in italiano, per il referto
ETICHETTA = {
    "DBMODE_FLAVOR_PASSIVE": "oziosa",
    "DBMODE_FLAVOR_ANGERED": "offesa",
    "DBMODE_FLAVOR_DEATH": "morte",
    "DBMODE_FLAVOR_KILL": "uccide",
    "DBMODE_FLAVOR_WELCOME": "torni",
    "DBMODE_REF_SPEC": "nome",
}


def contesto_per_riga(testo: str) -> tuple[dict[int, str], dict[int, str]]:
    """Per ogni riga del sorgente: il suo `dbmode` e il suo `dbid`.

    ⚠️ **Un blocco nuovo riparte senza `dbmode`.** `dbid` apre la creatura e i
    `dbmode` si susseguono dentro; se il modo non si azzerasse sul `dbid`, la
    prima classe di una creatura erediterebbe l'ultima della precedente — e i
    referti sarebbero plausibili e sbagliati.
    """
    modo, ident = "?", "?"
    modo_di: dict[int, str] = {}
    ident_di: dict[int, str] = {}
    for i, riga in enumerate(testo.split("\n")):
        trovato = _DBID.search(riga)
        if trovato:
            ident, modo = trovato.group(1), "?"
        trovato = _DBMODE.search(riga)
        if trovato:
            modo = trovato.group(1)
        modo_di[i + 1] = modo
        ident_di[i + 1] = ident
    return modo_di, ident_di


def rese_gia_decise() -> dict[str, set[str]]:
    """`jp` -> le rese italiane che quel giapponese ha gia' ricevuto altrove.

    ⚠️ **Lo stesso giapponese puo' avere due firme.** Il dizionario e'
    indicizzato per contenuto, e il contenuto di una voce comprende l'inglese:
    due creature che dicono la stessa identica frase giapponese ma che hanno
    ricevuto due inglesi diversi da monte sono **due voci da tradurre**, non
    una. Il punk (`db_creature.hsp:104157`) e il teppista (`:121xxx`) hanno
    tredici battute giapponesi in comune e nessuna in comune in inglese.

    Se le due rese divergono, la stessa frase esce in due modi da due creature,
    e **nessuna guardia lo vede**: sono entrambe italiano valido, entrambe
    diverse dal loro inglese, entrambe senza morfologia residua. Si vede solo
    incrociando il giapponese, che e' quello che fa questa funzione.

    Misurato l'11/08: 88 giapponesi compaiono piu' di una volta, 10 avevano gia'
    rese divergenti e 37 avevano una resa decisa e una voce ancora da fare.
    """
    fuori: dict[str, set[str]] = defaultdict(set)
    percorso = percorsi.DIZIONARIO / f"{FILE}.jsonl"
    if not percorso.exists():
        return fuori
    for riga in percorso.open(encoding="utf-8"):
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if voce.get("it") and voce.get("jp"):
            fuori[voce["jp"]].add(voce["it"])
    return fuori


def nomi_italiani(modo_di: dict[int, str], ident_di: dict[int, str]) -> dict[str, str]:
    """`CREATURE_ID_X` -> il nome italiano deciso in Fase 2, dove c'e'."""
    fuori: dict[str, str] = {}
    percorso = percorsi.DIZIONARIO / f"{FILE}.jsonl"
    if not percorso.exists():
        return fuori
    for riga in percorso.open(encoding="utf-8"):
        voce = json.loads(riga)
        if modo_di.get(voce["riga"]) == "DBMODE_REF_SPEC" and voce.get("it"):
            fuori[ident_di.get(voce["riga"], "?")] = voce["it"]
    return fuori


def livelli(testo: str, modo_di: dict[int, str], ident_di: dict[int, str]) -> dict[str, int]:
    """`CREATURE_ID_X` -> il livello che il database le assegna alla nascita.

    ⚠️ **Conta solo la prima assegnazione dentro `DBMODE_SET`**, che e' il
    livello base. Le altre due forme che il sorgente usa lì sono
    `cdata(CDATA_LEVEL, rc) = initlv`, che ripete un livello imposto da chi
    chiama, e la riscalatura per `voidlv`: nessuna delle due porta una cifra, e
    prenderle direbbe il livello di una generazione particolare invece di quello
    della creatura.
    """
    fuori: dict[str, int] = {}
    for i, riga in enumerate(testo.split("\n"), 1):
        if modo_di.get(i) != "DBMODE_SET":
            continue
        trovato = _LIVELLO.search(riga)
        if trovato:
            fuori.setdefault(ident_di.get(i, "?"), int(trovato.group(1)))
    return fuori


def repertori(
    estrazione: Path | None = None,
    sorgente: Path | None = None,
    per_riga: bool = False,
) -> tuple[list[tuple[str, list[dict]]], dict[str, str], dict[int, str]]:
    """Le creature da fare col loro repertorio completo.

    In testa quelle che il giocatore incontra di piu' — livello crescente, e a
    parita' di livello chi ha piu' battute. Con `per_riga` torna l'ordine in cui
    il sorgente le elenca, che e' cieco alla frequenza: vedi la testa del file.
    """
    sorgente = sorgente or (percorsi.SORGENTE_HSP / FILE)
    testo = sorgente.read_bytes().decode("cp932")
    modo_di, ident_di = contesto_per_riga(testo)

    estrazione = estrazione or ESTRAZIONE
    per_creatura: dict[str, list[dict]] = defaultdict(list)
    for riga in estrazione.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        per_creatura[ident_di.get(voce["riga"], "?")].append(voce)

    if per_riga:
        chiave = lambda kv: (min(v["riga"] for v in kv[1]),)
    else:
        livello_di = livelli(testo, modo_di, ident_di)
        # la riga in coda alla chiave tiene l'ordine stabile fra due creature
        # che hanno lo stesso livello e lo stesso numero di battute
        chiave = lambda kv: (
            livello_di.get(kv[0], LIVELLO_IGNOTO),
            -len(kv[1]),
            min(v["riga"] for v in kv[1]),
        )

    return sorted(per_creatura.items(), key=chiave), nomi_italiani(modo_di, ident_di), modo_di


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--da", type=int, default=0,
                        help="salta le prime N creature (per riprendere un lotto)")
    parser.add_argument("--tetto", type=int, default=60,
                        help="quante voci al massimo nel lotto (default 60)")
    parser.add_argument("--conto", action="store_true",
                        help="stampa solo il totale per classe, senza il repertorio")
    parser.add_argument("--per-riga", action="store_true",
                        help="l'ordine vecchio, in cui il sorgente elenca le creature")
    parser.add_argument("--divergenti", action="store_true",
                        help="i giapponesi gia' resi in due modi diversi nel dizionario")
    argomenti = parser.parse_args(argv)

    if argomenti.divergenti:
        # ⚠️ un referto, non una guardia: la divergenza puo' essere legittima.
        # `あなたは誰かに見つめられている感じがした。` ha due voci con inglese al
        # passato e al presente, e le due rese seguono l'inglese come devono;
        # `*ドスン*` ne ha una con gli spazi di giuntura e una senza. Chi guarda
        # decide — una regola automatica qui rifiuterebbe lavoro giusto.
        divergenti = {jp: rese for jp, rese in rese_gia_decise().items() if len(rese) > 1}
        for jp, rese in sorted(divergenti.items()):
            print(f"{jp}")
            for resa in sorted(rese):
                print(f"    {resa!r}")
        print(f"\n{len(divergenti)} giapponesi resi in piu' di un modo")
        return 0

    if not ESTRAZIONE.exists():
        print(f"manca {ESTRAZIONE}. Rigenerala con:\n"
              f"  python -m strumenti.estrai {FILE} --da-tradurre --uscita lavoro/_c.jsonl")
        return 1

    ordinate, nomi, modo_di = repertori(per_riga=argomenti.per_riga)
    testo = (percorsi.SORGENTE_HSP / FILE).read_bytes().decode("cp932")
    livello_di = livelli(testo, *contesto_per_riga(testo))
    gia_deciso = rese_gia_decise()

    if argomenti.conto:
        conto = Counter(
            ETICHETTA.get(modo_di.get(v["riga"], "?"), modo_di.get(v["riga"], "?"))
            for _, voci in ordinate for v in voci
        )
        for classe, n in conto.most_common():
            print(f"  {n:5}  {classe}")
        print(f"\n{sum(conto.values())} voci da fare su {len(ordinate)} creature")
        return 0

    totale, ultimo = 0, argomenti.da - 1
    for indice, (ident, voci) in enumerate(ordinate):
        if indice < argomenti.da:
            continue
        if totale and totale + len(voci) > argomenti.tetto:
            break
        totale += len(voci)
        ultimo = indice
        nome = nomi.get(ident, "⚠️ NOME NON TRADOTTO")
        livello = livello_di.get(ident)
        quanto = f"lv {livello}" if livello is not None else "lv ignoto"
        print(f"--- [{indice}] {ident}  «{nome}»  ({quanto})")
        for voce in sorted(voci, key=lambda x: x["riga"]):
            classe = ETICHETTA.get(modo_di.get(voce["riga"], "?"), "?")
            atteso = f'cnvtalk("{voce["en"]}")'
            nota = "" if voce["en_grezzo"] == atteso else f"   [grezzo {voce['en_grezzo']}]"
            print(f"  {voce['riga']:6} {classe:7} {voce['en']!r}{nota}")
            # ⚠️ lo stesso giapponese puo' avere gia' una resa sotto un'altra
            # firma: si copia, non si reinventa. Vedi rese_gia_decise()
            gia = gia_deciso.get(voce.get("jp", ""))
            if gia:
                for resa in sorted(gia):
                    print(f"         ⚠️ GIA' RESO ALTROVE: {resa!r}")

    print(f"\n{totale} voci, creature da [{argomenti.da}] a [{ultimo}]"
          f", su {len(ordinate)} creature da fare")
    print("il prossimo lotto: --da", ultimo + 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
