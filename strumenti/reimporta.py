"""Scrive un lotto tradotto nel dizionario, ma solo se l'intero lotto e' pulito."""
import argparse
import json
from pathlib import Path

from strumenti import percorsi
from strumenti.verifica import controlla_lotto


def reimporta(voci: list[dict], dizionario: dict) -> dict:
    """Valida il lotto e lo fonde nel dizionario. Tutto o niente."""
    problemi = controlla_lotto(voci)
    if problemi:
        dettaglio = "; ".join(f"{k}: {', '.join(v)}" for k, v in list(problemi.items())[:5])
        raise ValueError(f"{len(problemi)} voci con problemi — {dettaglio}")
    for voce in voci:
        dizionario[voce["firma"]] = voce
    return dizionario


def carica_dizionario(nome_file: str) -> dict:
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    if not percorso.exists():
        return {}
    voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    return {v["firma"]: v for v in voci}


def salva_dizionario(nome_file: str, dizionario: dict) -> Path:
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    percorso.parent.mkdir(parents=True, exist_ok=True)
    ordinate = sorted(dizionario.values(), key=lambda v: (v["riga"], v["occorrenza"]))
    with percorso.open("w", encoding="utf-8") as scrittura:
        for voce in ordinate:
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    return percorso


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Reimporta un lotto tradotto nel dizionario.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL tradotto")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    per_file: dict[str, list[dict]] = {}
    for voce in voci:
        per_file.setdefault(voce["file"], []).append(voce)

    for nome_file, gruppo in per_file.items():
        dizionario = reimporta(gruppo, carica_dizionario(nome_file))
        percorso = salva_dizionario(nome_file, dizionario)
        print(f"{len(gruppo)} voci in {percorso}")


if __name__ == "__main__":
    main()
