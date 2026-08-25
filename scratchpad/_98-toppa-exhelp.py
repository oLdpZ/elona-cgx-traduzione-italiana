"""La toppa che fa leggere exhelp_it.txt, con il ripiego su exhelp.txt.

La terza della famiglia, dopo board.txt (init.hsp) e talk.txt (text.hsp).
"""
import json
from pathlib import Path

from strumenti import percorsi

FILE = "help.hsp"
RIGA = '\tnoteload exedir + "data\\\\exhelp.txt"'

NUOVE = [
    '\texist exedir + "data\\\\exhelp_it.txt"',
    '\tif ( strsize != (-1) ) {',
    '\t\tnoteload exedir + "data\\\\exhelp_it.txt"',
    '\t}',
    '\telse {',
    '\t\tnoteload exedir + "data\\\\exhelp.txt"',
    '\t}',
]

MOTIVO = (
    "Il nome del file dati e' un letterale nudo, fuori da ogni lang(): il dizionario "
    "non lo raggiunge. La toppa fa leggere exhelp_it.txt, che applica costruisce in "
    "build\\dati\\ dal dizionario dei file dati (dizionario/dati/exhelp.txt.jsonl). "
    "E' la terza della famiglia, identica a quelle di board.txt (init.hsp:2574) e "
    "talk.txt (text.hsp): il file italiano si posa ACCANTO a quello di monte invece "
    "che al posto suo, come cgx-test.exe accanto a elonapluscgx.exe. "
    "Il ramo `exist` non e' prudenza generica: la riga di monte fa noteload senza "
    "guardia, e un noteload su un file assente e' un errore di esecuzione. Qui pero' "
    "il danno sarebbe piu' stretto che per board.txt, e vale la pena dirlo: "
    "*elona_help e' un gosub chiamato da diciotto siti (cfg_extrahelp), non "
    "dall'avvio, quindi senza ripiego a morire non sarebbe il gioco ma il primo "
    "consiglio di Norne — cioe' la prima volta che il giocatore entra in casa. "
    "Il ripiego resta perche' un guasto che aspetta il primo consiglio e' peggio di "
    "uno che si vede subito, non perche' sia meno grave. "
    "Vedi piani/2026-08-20-fase-3-file-dati.md."
)


def main() -> None:
    sorgente = (percorsi.SORGENTE_HSP / FILE).read_bytes().decode("cp932").splitlines()
    quante = sorgente.count(RIGA)
    print("la riga cercata:", repr(RIGA))
    print("aggancia il sorgente pinnato:", quante, "volte")
    if quante != 1:
        raise SystemExit("la toppa deve agganciare esattamente una riga")

    percorso = Path("toppe.jsonl")
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]

    toppa = {"file": FILE, "cerca": RIGA, "sostituisci": NUOVE, "motivo": MOTIVO}
    rimpiazzate = 0
    tenute = []
    for vecchia in esistenti:
        if vecchia["file"] == FILE and vecchia["cerca"] == RIGA:
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
