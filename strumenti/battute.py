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

## Uso

    python -m strumenti.battute                 # il primo lotto da fare, ~60 voci
    python -m strumenti.battute --da 10         # salta le prime 10 creature
    python -m strumenti.battute --tetto 100     # un lotto piu' grosso
    python -m strumenti.battute --conto         # solo il totale per classe

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


def repertori(
    estrazione: Path | None = None, sorgente: Path | None = None
) -> tuple[list[tuple[str, list[dict]]], dict[str, str], dict[int, str]]:
    """Le creature da fare, in ordine di riga, col loro repertorio completo."""
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

    ordinate = sorted(
        per_creatura.items(), key=lambda kv: min(v["riga"] for v in kv[1])
    )
    return ordinate, nomi_italiani(modo_di, ident_di), modo_di


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--da", type=int, default=0,
                        help="salta le prime N creature (per riprendere un lotto)")
    parser.add_argument("--tetto", type=int, default=60,
                        help="quante voci al massimo nel lotto (default 60)")
    parser.add_argument("--conto", action="store_true",
                        help="stampa solo il totale per classe, senza il repertorio")
    argomenti = parser.parse_args(argv)

    if not ESTRAZIONE.exists():
        print(f"manca {ESTRAZIONE}. Rigenerala con:\n"
              f"  python -m strumenti.estrai {FILE} --da-tradurre --uscita lavoro/_c.jsonl")
        return 1

    ordinate, nomi, modo_di = repertori()

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
        print(f"--- [{indice}] {ident}  «{nome}»")
        for voce in sorted(voci, key=lambda x: x["riga"]):
            classe = ETICHETTA.get(modo_di.get(voce["riga"], "?"), "?")
            atteso = f'cnvtalk("{voce["en"]}")'
            nota = "" if voce["en_grezzo"] == atteso else f"   [grezzo {voce['en_grezzo']}]"
            print(f"  {voce['riga']:6} {classe:7} {voce['en']!r}{nota}")

    print(f"\n{totale} voci, creature da [{argomenti.da}] a [{ultimo}]"
          f", su {len(ordinate)} creature da fare")
    print("il prossimo lotto: --da", ultimo + 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
