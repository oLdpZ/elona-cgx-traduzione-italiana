"""Le 126 etichette del menu dei filtri, col nome italiano gia' deciso e la misura.

Il tetto non si stima: si legge dal sorgente. `tcg.hsp:3287` mette le
linguette a passo **63 px** (`x = basex + 180 + cnt * 63`), il testo parte da
`x + 1` (`:3302`) e la linguetta e' un ritaglio largo 63 (`gcopy 7, 360, 96,
63, 20`). Il carattere della build inglese e' `Courier New`, monospaziato, e
qui il corpo e' **9** (`:3283`, `font ..., 10 + en - en * 2` con `en == 1`):
6,6 px a corpo 11 e 7,2 a 12, cioe' 0,6 x corpo, quindi **5,4 px** a corpo 9.

    (63 - 2) / 5,4 = 11,3  ->  TETTO 11 CARATTERI

⭐ L'ancora e' di monte: l'etichetta inglese piu' lunga di tutt'e sedici le
pagine e' `largeanimal`, **11 caratteri esatti**.

⚠️ E il tetto si misura sulla forma **degradata** (`volonta'`, non `volontà`),
perche' e' quella che va a schermo.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from strumenti import accenti, percorsi  # noqa: E402

TETTO = 11

sorgente = (percorsi.SORGENTE_HSP / "tcg.hsp").read_bytes().decode("cp932")
righe = sorgente.split("\n")

# le etichette stanno nelle assegnazioni di `cfname@tcg` fra :3552 e :3632,
# dopo le due `lang()` di «List» e «Deck», che il dizionario gia' copre
etichette: list[str] = []
for numero in range(3552, 3633):
    riga = righe[numero - 1]
    if "cfname@tcg =" not in riga:
        continue
    coda = riga.split('lang("デッキ", "Deck"),', 1)[-1]
    for pezzo in re.findall(r'"((?:[^"\\]|\\.)*)"', coda):
        etichette.append(pezzo)

distinte = sorted(set(etichette))
print(f"etichette: {len(etichette)} siti, {len(distinte)} distinte\n")


def nomi(file_dizionario: str) -> dict[str, str]:
    voci = {}
    percorso = percorsi.PROGETTO / "dizionario" / file_dizionario
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it"):
            voci.setdefault(voce["en"], voce["it"])
    return voci


razze = nomi("db_race.hsp.jsonl")
classi = nomi("db_class.hsp.jsonl")

print(f"{'etichetta':<14}{'italiano gia deciso':<28}{'car.':>5}  fonte")
print("-" * 70)
senza = []
lunghe = []
for etichetta in distinte:
    reso = razze.get(etichetta) or classi.get(etichetta.capitalize()) \
        or classi.get(etichetta)
    fonte = "db_race" if etichetta in razze else (
        "db_class" if (etichetta.capitalize() in classi
                       or etichetta in classi) else "")
    if reso is None:
        senza.append(etichetta)
        continue
    degradato = accenti.degrada(reso)
    segno = "  <<< SFORA" if len(degradato) > TETTO else ""
    if segno:
        lunghe.append((etichetta, degradato, len(degradato)))
    print(f"{etichetta:<14}{degradato:<28}{len(degradato):>5}  {fonte}{segno}")

print(f"\nsenza un nome italiano gia' deciso ({len(senza)}):")
for etichetta in senza:
    print("   ", repr(etichetta))
print(f"\noltre il tetto di {TETTO}: {len(lunghe)}")
