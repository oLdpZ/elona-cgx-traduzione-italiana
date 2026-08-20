"""Unico punto che conosce i percorsi d'ambiente. Tutti gli altri script importano da qui."""
import os
from pathlib import Path

PROGETTO = Path(__file__).resolve().parent.parent

RADICE_LAVORO = Path(os.environ.get("ELONA_IT_LAVORO", r"C:\Games\Elona\_traduzione"))
SORGENTE = RADICE_LAVORO / "sorgente"
BUILD = RADICE_LAVORO / "build"
DIST = RADICE_LAVORO / "dist"
HSP = RADICE_LAVORO / "hsp34"

GIOCO = Path(os.environ.get("ELONA_IT_GIOCO", r"C:\Games\Elona\elonaplus2.31"))

# ridefinibile perche' altrimenti ogni prova d'integrazione scriverebbe nel
# dizionario vero del vault, che e' la sorgente di verita' del progetto
DIZIONARIO = Path(os.environ.get("ELONA_IT_DIZIONARIO", PROGETTO / "dizionario"))
LAVORO_LOTTI = PROGETTO / "lavoro"

# I file dati di `data\` (board.txt, book.txt, exhelp.txt, talk.txt, manual_*)
# non stanno nel clone di monte: `sorgente/` li ha cancellati dal working tree,
# e per talk.txt e autopick.txt il gioco installato e' piu' recente del commit
# pinnato. Il riferimento e' una copia presa **una volta** dal gioco: e' il file
# che l'eseguibile legge davvero. Il manifesto in `dati/manifesto.json` dice
# quali byte ci si aspetta di trovarci.
DATI_SORGENTE = RADICE_LAVORO / "dati-sorgente"
BUILD_DATI = BUILD / "dati"

# sottocartella del sorgente che contiene gli .hsp
SORGENTE_HSP = SORGENTE / "2.05-custom-gx"
BUILD_HSP = BUILD / "2.05-custom-gx"
