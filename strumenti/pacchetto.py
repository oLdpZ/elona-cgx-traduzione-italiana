"""Costruisce l'archivio che si pubblica: quel che serve a compilare in casa.

⚠️⚠️ **Quel che NON ci va dentro, ed e' il punto di tutto.** Nell'archivio non
entra un solo byte del gioco: ne' l'eseguibile, ne' il sorgente di Custom-GX,
ne' i file di `data\\`. Il sorgente non ha licenza, e finche' non c'e' un
permesso non si ridistribuisce. Dentro ci va **il dizionario, che e' nostro**,
e gli strumenti che lo applicano; tutto il resto se lo prende `costruisci.py`
sul computer di chi installa, dalle sorgenti pubbliche di chi lo ha fatto.

ⓘ Il dizionario contiene anche le stringhe inglesi di monte, perche' una
traduzione e' fatta di coppie: quella e' la norma delle traduzioni amatoriali
ed e' un'altra cosa dal distribuire il gioco.

## Uso

    python -m strumenti.pacchetto            # scrive dist/elona-cgx-ita-<ver>.zip
    python -m strumenti.pacchetto --elenco   # dice solo cosa ci metterebbe
"""
import argparse
import zipfile
from pathlib import Path

from strumenti import percorsi

VERSIONE = "2.31.2.0"

# ⚠️ Ogni voce e' roba nostra. Chi aggiunge una riga qui si chieda prima di chi
# e' il file che sta mettendo in un archivio pubblico.
RADICE = [
    "costruisci.py",
    "costruisci.bat",
    "LEGGIMI.txt",
    "toppe.jsonl",
]
CARTELLE = [
    ("dizionario", "*.jsonl"),
    ("dati", "manifesto-sorgente.txt"),
]
# gli strumenti che la catena tocca davvero, piu' quelli che loro importano
STRUMENTI_FUORI = {"tests", "__pycache__"}


def contenuto() -> list[tuple[Path, str]]:
    """(percorso sul disco, nome dentro l'archivio)."""
    dentro: list[tuple[Path, str]] = []
    for nome in RADICE:
        percorso = percorsi.PROGETTO / nome
        if not percorso.exists():
            raise SystemExit("manca %s: l'archivio sarebbe monco" % nome)
        dentro.append((percorso, nome))

    for cartella, modello in CARTELLE:
        base = percorsi.PROGETTO / cartella
        for percorso in sorted(base.rglob(modello)):
            dentro.append((percorso, str(percorso.relative_to(percorsi.PROGETTO))))

    strumenti = percorsi.PROGETTO / "strumenti"
    for percorso in sorted(strumenti.iterdir()):
        if percorso.name in STRUMENTI_FUORI or percorso.is_dir():
            continue
        if percorso.suffix in (".py", ".ps1"):
            dentro.append((percorso, "strumenti/" + percorso.name))
    return dentro


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--elenco", action="store_true",
                              help="dice cosa ci metterebbe, senza scrivere")
    argomenti = analizzatore.parse_args()

    dentro = contenuto()
    byte = sum(p.stat().st_size for p, _ in dentro)
    if argomenti.elenco:
        for percorso, nome in dentro:
            print("%9d  %s" % (percorso.stat().st_size, nome))
        print()
        print("%d file, %.1f MB non compressi" % (len(dentro), byte / 1e6))
        return

    percorsi.DIST.mkdir(parents=True, exist_ok=True)
    archivio = percorsi.DIST / ("elona-cgx-ita-%s.zip" % VERSIONE)
    with zipfile.ZipFile(archivio, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for percorso, nome in dentro:
            z.write(percorso, nome)

    print("%s" % archivio)
    print("  %d file, %.1f MB non compressi -> %.1f MB"
          % (len(dentro), byte / 1e6, archivio.stat().st_size / 1e6))
    print()
    print("  ⓘ Dentro non c'e' nessun byte del gioco: ne' l'eseguibile, ne' il")
    print("    sorgente di Custom-GX, ne' i file di data\\. Se li' dentro un")
    print("    giorno ci finissero, questa riga sarebbe una bugia.")


if __name__ == "__main__":
    main()
