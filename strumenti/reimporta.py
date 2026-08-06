"""Scrive un lotto tradotto nel dizionario, ma solo se l'intero lotto e' pulito.

Tutto o niente vale sull'**intero lotto**, non file per file: `main()` valida
tutti i gruppi prima di scrivere qualunque cosa. Un lotto che tocca due file con
una voce sporca nel secondo lasciava altrimenti il primo gia' scritto su disco.

La scrittura del dizionario e' atomica (file temporaneo piu' `os.replace`):
lo SPEC ne fa la sorgente di verita' e vive in un vault sincronizzato, dove
un'interruzione a meta' `open("w")` lo troncherebbe.
"""
import argparse
import json
import os
import tempfile
from pathlib import Path

from strumenti import percorsi
from strumenti.verifica import controlla_lotto


def reimporta(voci: list[dict], dizionario: dict) -> dict:
    """Valida il lotto e lo fonde **in-place** nel dizionario ricevuto.

    Tutto o niente: se anche una sola voce e' sporca solleva `ValueError` e il
    dizionario ricevuto **non viene toccato**. Se il lotto e' pulito le voci ci
    finiscono dentro modificando l'oggetto passato, che viene anche restituito
    per comodita': il chiamante non deve aspettarsi una copia.
    """
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
    """Scrive il dizionario in modo atomico: temporaneo piu' os.replace.

    Il dizionario e' la sorgente di verita' del progetto e vive in un vault
    sincronizzato: un `open("w")` interrotto a meta' lo troncherebbe. Con
    `os.replace` il file di destinazione o e' quello vecchio o e' quello
    nuovo, mai una via di mezzo.
    """
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    percorso.parent.mkdir(parents=True, exist_ok=True)
    ordinate = sorted(dizionario.values(), key=lambda v: (v["riga"], v["occorrenza"]))

    descrittore, temporaneo = tempfile.mkstemp(
        dir=percorso.parent, prefix=f".{nome_file}.", suffix=".tmp"
    )
    try:
        with os.fdopen(descrittore, "w", encoding="utf-8") as scrittura:
            for voce in ordinate:
                scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
            scrittura.flush()
            os.fsync(scrittura.fileno())
        os.replace(temporaneo, percorso)
    except BaseException:
        Path(temporaneo).unlink(missing_ok=True)
        raise
    return percorso


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Reimporta un lotto tradotto nel dizionario.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL tradotto")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    per_file: dict[str, list[dict]] = {}
    for voce in voci:
        per_file.setdefault(voce["file"], []).append(voce)

    # prima si valida tutto, poi si scrive: altrimenti un lotto che tocca due
    # file con una voce sporca nel secondo lascia il primo gia' su disco.
    pronti: list[tuple[str, dict, int]] = []
    try:
        for nome_file, gruppo in per_file.items():
            dizionario = reimporta(gruppo, carica_dizionario(nome_file))
            pronti.append((nome_file, dizionario, len(gruppo)))
    except ValueError as errore:
        raise SystemExit(
            f"lotto rifiutato, niente e' stato scritto nel dizionario: {errore}"
        )

    for nome_file, dizionario, quante in pronti:
        percorso = salva_dizionario(nome_file, dizionario)
        print(f"{quante} voci in {percorso}")


if __name__ == "__main__":
    main()
