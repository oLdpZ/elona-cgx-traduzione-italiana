"""La toppa che fa leggere board_it.txt, con il ripiego su board.txt.

Sostituisce anche la versione a riga sola se e' gia' stata scritta.
"""
import json
from pathlib import Path

from strumenti import percorsi

RIGA = '\tnoteload exedir + "data\\\\board.txt"'

NUOVE = [
    '\texist exedir + "data\\\\board_it.txt"',
    '\tif ( strsize != (-1) ) {',
    '\t\tnoteload exedir + "data\\\\board_it.txt"',
    '\t}',
    '\telse {',
    '\t\tnoteload exedir + "data\\\\board.txt"',
    '\t}',
]

MOTIVO = (
    "Il nome del file dati e' un letterale nudo, fuori da ogni lang(): il dizionario "
    "non lo raggiunge. La toppa fa leggere board_it.txt, che applica costruisce in "
    "build\\dati\\ dal dizionario dei file dati (dizionario/dati/board.txt.jsonl). "
    "Il file italiano si posa ACCANTO a quello di monte invece che al posto suo: e' "
    "la disciplina di cgx-test.exe, che non sovrascrive elonapluscgx.exe, cosi' "
    "l'eseguibile inglese continua a girare col suo file e il riferimento pulito "
    "resta sul disco. "
    "Il ramo `exist` NON e' prudenza generica: la riga di monte fa noteload senza "
    "guardia, e un noteload su un file assente e' un errore di esecuzione, cioe' il "
    "gioco che muore all'avvio. Senza ripiego, chi copiasse l'eseguibile senza il "
    "file dati non vedrebbe una bacheca inglese: non vedrebbe il gioco. L'idioma "
    "`exist` + `strsize != (-1)` e' quello che custom_autopick.hsp usa gia' per i "
    "propri file. Vedi piani/2026-08-20-fase-3-file-dati.md."
)


def main() -> None:
    sorgente = (percorsi.SORGENTE_HSP / "init.hsp").read_bytes().decode("cp932").splitlines()
    quante = sorgente.count(RIGA)
    print("la riga cercata:", repr(RIGA))
    print("aggancia il sorgente pinnato:", quante, "volte")
    if quante != 1:
        raise SystemExit("la toppa deve agganciare esattamente una riga")

    percorso = Path("toppe.jsonl")
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]

    toppa = {"file": "init.hsp", "cerca": RIGA, "sostituisci": NUOVE, "motivo": MOTIVO}
    rimpiazzate = 0
    tenute = []
    for vecchia in esistenti:
        if vecchia["file"] == "init.hsp" and vecchia["cerca"] == RIGA:
            rimpiazzate += 1
            continue
        tenute.append(vecchia)
    tenute.append(toppa)

    percorso.write_text(
        "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tenute),
        encoding="utf-8", newline="\n")
    print(f"toppe: {len(tenute)} (rimpiazzate {rimpiazzate})")


if __name__ == "__main__":
    main()
