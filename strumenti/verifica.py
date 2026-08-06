# strumenti/verifica.py
"""Regole di blocco sui lotti e sul dizionario. Vedi SPEC.md paragrafo 7."""
import argparse
import json
import re
from pathlib import Path

from strumenti.accenti import degrada, ha_apostrofo_scritto_a_mano, non_ascii_residuo

_CHIAMATE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def _chiamate(testo: str) -> list[str]:
    return sorted(_CHIAMATE.findall(testo))


def controlla_voce(voce: dict) -> list[str]:
    """Ritorna la lista dei problemi. Lista vuota significa voce pulita."""
    problemi: list[str] = []
    italiano = voce.get("it", "")

    if not italiano.strip():
        problemi.append("traduzione vuota")
        return problemi

    # per le dinamiche il termine di paragone e' l'espressione intera
    originale = voce["en_grezzo"] if voce["tipo"] == "dinamica" else voce["en"]
    if italiano == originale:
        problemi.append("traduzione identica all'inglese")

    if ha_apostrofo_scritto_a_mano(italiano):
        problemi.append(
            "apostrofo scritto a mano: nel dizionario va l'accento vero, "
            "la degradazione la fa applica.py"
        )

    # gli accenti veri (perche') si degradano regolarmente in fase di build:
    # non sono un residuo. Il residuo vero e' cio' che resta non rappresentabile
    # anche dopo la degradazione (es. un trattino lungo, virgolette tipografiche).
    residui = non_ascii_residuo(degrada(italiano))
    if residui:
        problemi.append(f"caratteri che CP932 cancellerebbe: {residui}")

    if voce["tipo"] == "dinamica":
        attese = _chiamate(voce["en_grezzo"])
        trovate = _chiamate(italiano)
        if attese != trovate:
            problemi.append(f"interpolazioni non conservate: attese {attese}, trovate {trovate}")

    return problemi


def controlla_lotto(voci: list[dict]) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema."""
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce)
        if problemi:
            esito[voce["firma"]] = problemi
    return esito


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Verifica un lotto JSONL tradotto.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(riga) for riga in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if riga.strip()]
    esito = controlla_lotto(voci)
    if not esito:
        print(f"{len(voci)} voci, nessun problema")
        return
    for chiave, problemi in esito.items():
        print(f"{chiave}: " + "; ".join(problemi))
    raise SystemExit(f"{len(esito)} voci con problemi su {len(voci)}")


if __name__ == "__main__":
    main()
