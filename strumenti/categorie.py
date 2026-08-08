# strumenti/categorie.py
"""La categoria che il sorgente dichiara per ogni oggetto di `db_item.hsp`.

I primi sei lotti della Fase 1 sono stati scelti con `filter_item`, e ha
funzionato ogni volta: una classe raccoglie oggetti che pongono la **stessa
domanda**. Poi `filter_item` si e' esaurito, e cio' che restava si chiamava «il
gruppo senza filtro» — un residuo, non una classe.

Il residuo non esisteva: la categoria c'e', solo che non sta in `filter_item`.
Ogni oggetto la dichiara **dentro il proprio blocco**:

    if ( dbid == ITEM_ID_HAMBURGER ) {
        ...
        reftype = FILTER_ITEM_FOOD

Sono 1.320 oggetti classificati dal sorgente, e con quella chiave il residuo
torna a essere fatto di classi: FILTER_ITEM_TOOL, FILTER_FURNITURE,
FILTER_JUNK, FILTER_ITEM_FOOD, FILTER_CONTAINER...

⚠️ **E' un dato del sorgente, non una lettura del dizionario.** La lezione di
`stessa-forma-va-verificata-nel-codice` vale anche al contrario: dove il codice
dichiara una classe, quella e' la classe, e non serve dedurla dai nomi.

Un blocco puo' assegnare `reftype` piu' volte (una per `dbmode`): vince la
prima, e le altre sono uguali. Un oggetto che non assegna mai `reftype` non
compare nella mappa — non e' un errore, e chi lo chiede se lo trova assente
invece che classificato per sbaglio.
"""
import argparse
import collections
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.estrai import (
    carica_rinviate, da_tradurre, estrai_da_file, firme_tradotte,
)

FILE = "db_item.hsp"

_INIZIO_BLOCCO = re.compile(r"if\s*\(\s*dbid\s*==\s*(ITEM_ID_[A-Z_0-9]+)\s*\)")
_CATEGORIA = re.compile(r"reftype\s*=\s*(FILTER_[A-Z_0-9]+)")


def categorie_da_testo(testo: str) -> dict[str, str]:
    """ITEM_ID -> FILTER_..., leggendo i blocchi `if ( dbid == ITEM_ID_X )`."""
    trovate: dict[str, str] = {}
    corrente: str | None = None
    for riga in testo.splitlines():
        avvio = _INIZIO_BLOCCO.search(riga)
        if avvio:
            corrente = avvio.group(1)
            continue
        if corrente is None:
            continue
        categoria = _CATEGORIA.search(riga)
        if categoria:
            trovate.setdefault(corrente, categoria.group(1))
            corrente = None
    return trovate


def categorie(percorso: Path | None = None) -> dict[str, str]:
    """La mappa letta dal sorgente vero. CP932 come tutto il resto del sorgente."""
    percorso = percorso or percorsi.SORGENTE_HSP / FILE
    return categorie_da_testo(percorso.read_bytes().decode("cp932"))


def voci_di_categoria(categoria: str, solo_da_tradurre: bool = True) -> list[dict]:
    """Le voci di `db_item.hsp` che il sorgente dichiara di quella categoria."""
    mappa = categorie()
    voci = estrai_da_file(percorsi.SORGENTE_HSP / FILE)
    if solo_da_tradurre:
        voci = da_tradurre(voci, firme_tradotte(FILE), carica_rinviate(None, FILE))
    return [v for v in voci if mappa.get(v.get("oggetto")) == categoria]


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Le categorie che db_item.hsp dichiara, e i lotti che ne escono.",
    )
    analizzatore.add_argument(
        "--categoria",
        help="scrive il lotto di questa categoria, es. FILTER_ITEM_TOOL",
    )
    analizzatore.add_argument("--uscita", help="percorso del lotto JSONL da scrivere")
    analizzatore.add_argument(
        "--tutte", action="store_true",
        help="conta tutti gli oggetti, non solo quelli ancora da tradurre",
    )
    argomenti = analizzatore.parse_args()

    if argomenti.categoria:
        voci = voci_di_categoria(argomenti.categoria, not argomenti.tutte)
        if not argomenti.uscita:
            for voce in voci:
                print(f"{voce['en']}\t{voce['jp']}")
            print(f"-- {len(voci)} voci")
            return
        uscita = Path(argomenti.uscita)
        uscita.parent.mkdir(parents=True, exist_ok=True)
        with uscita.open("w", encoding="utf-8") as scrittura:
            for voce in voci:
                scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
        print(f"{len(voci)} voci in {uscita}")
        return

    mappa = categorie()
    voci = estrai_da_file(percorsi.SORGENTE_HSP / FILE)
    if not argomenti.tutte:
        voci = da_tradurre(voci, firme_tradotte(FILE), carica_rinviate(None, FILE))
    conteggio = collections.Counter(
        mappa.get(v.get("oggetto"), "(nessuna)") for v in voci
    )
    quali = "in tutto" if argomenti.tutte else "ancora da tradurre"
    print(f"{len(voci)} voci {quali}, {len(mappa)} oggetti classificati dal sorgente")
    for nome, quante in conteggio.most_common():
        print(f"  {quante:5d}  {nome}")


if __name__ == "__main__":
    main()
