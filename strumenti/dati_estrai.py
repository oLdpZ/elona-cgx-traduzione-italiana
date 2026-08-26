# strumenti/dati_estrai.py
"""Da un file dati a un lotto JSONL da tradurre.

L'unita' e' **una riga inglese**. Non un blocco, e non una coppia col
giapponese: in `board.txt` le due lingue non sono appaiate — 25 righe inglesi
contro 63 giapponesi, `COOK,1` rende la seconda giapponese e non la prima,
`COOK,3` non ne rende nessuna, e `COOK,8` ha un giapponese identico a quello di
`COOK,GENERAL` con un inglese tutto suo. Non e' sciatteria: il file lo dichiara
alle righe 22-24 («*The translation doesn't have to be precise. You can even add
your own sentences if you like to.*»).

Quindi il giapponese si porta dietro come **contesto del blocco**, e per la
stessa ragione **non entra nella firma**: se monte riscrivesse il giapponese, le
rese italiane non andrebbero buttate.

    python -m strumenti.dati_estrai board.txt --lotto lavoro/board-001.jsonl

⚠️ La firma si fa su `(file, blocco, riga, inglese)`. Sull'**inglese** e non
solo sulla posizione: se monte riscrive una riga la voce resta **orfana** e il
referto lo dice, invece di lasciar scivolare una resa su un testo che non e'
piu' quello.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from strumenti import dati, percorsi


def firma(nome_file: str, blocco: str, riga: int, en: str) -> str:
    crudo = f"{nome_file}|{blocco}|{riga}|{en}"
    return hashlib.sha1(crudo.encode("utf-8")).hexdigest()


def voci(nome_file: str, documento: dati.Documento) -> list[dict]:
    """Una voce per riga piena di ogni blocco inglese.

    ⚠️ Dove il blocco e' una **CSV** (`dati.COLONNE_CSV`) l'unita' non e' la
    riga ma una **colonna**: l'inglese e' quel che c'e' nella sua, il
    giapponese sta nella colonna accanto ed e' contesto come sempre.
    """
    estratte: list[dict] = []
    for blocco in documento.blocchi:
        colonne = dati.colonne_csv(nome_file, blocco.chiave)
        if colonne is not None:
            for numero, testo in enumerate(blocco.righe_piene(), 1):
                estratte.append({
                    "firma": firma(nome_file, blocco.chiave, numero,
                                   dati.campo_csv(testo, colonne["en"])),
                    "file": nome_file,
                    "blocco": blocco.chiave,
                    "riga": numero,
                    "en": dati.campo_csv(testo, colonne["en"]),
                    "jp_contesto": [dati.campo_csv(testo, colonne["jp"])],
                    "it": "",
                })
            continue
        if blocco.lingua != "EN":
            continue
        giapponese = documento.blocco(blocco.chiave, "JP")
        contesto = giapponese.righe_piene() if giapponese is not None else []
        # numerate fra le righe **piene**: una riga vuota aggiunta da monte non
        # deve spostare la firma di tutte quelle che vengono dopo
        for numero, testo in enumerate(blocco.righe_piene(), 1):
            estratte.append({
                "firma": firma(nome_file, blocco.chiave, numero, testo),
                "file": nome_file,
                "blocco": blocco.chiave,
                "riga": numero,
                "en": testo,
                "jp_contesto": contesto,
                "it": "",
            })
    return estratte


def scrivi_lotto(percorso: Path, elenco: list[dict]) -> None:
    percorso.parent.mkdir(parents=True, exist_ok=True)
    percorso.write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in elenco),
        encoding="utf-8",
    )


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Estrae un lotto da un file dati di data\\.")
    analizzatore.add_argument("file", help="es. board.txt")
    analizzatore.add_argument("--lotto", help="dove scrivere il lotto JSONL")
    argomenti = analizzatore.parse_args()

    origine = percorsi.DATI_SORGENTE / argomenti.file
    if not origine.exists():
        raise SystemExit(f"{origine} non c'e': i file dati si pinnano con "
                         "`python -m strumenti.dati_sorgente --pinna`")

    documento = dati.analizza_file(argomenti.file,
                                   dati.leggi(origine, argomenti.file))
    elenco = voci(argomenti.file, documento)

    percorso = Path(argomenti.lotto) if argomenti.lotto else (
        percorsi.LAVORO_LOTTI / f"{Path(argomenti.file).stem}-001.jsonl")
    scrivi_lotto(percorso, elenco)

    blocchi = len({v["blocco"] for v in elenco})
    print(f"{argomenti.file}: {len(elenco)} righe inglesi in {blocchi} blocchi")
    print(f"lotto: {percorso}")


if __name__ == "__main__":
    main()
