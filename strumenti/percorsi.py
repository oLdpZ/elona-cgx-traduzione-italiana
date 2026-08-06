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

DIZIONARIO = PROGETTO / "dizionario"
LAVORO_LOTTI = PROGETTO / "lavoro"

# sottocartella del sorgente che contiene gli .hsp
SORGENTE_HSP = SORGENTE / "2.05-custom-gx"
BUILD_HSP = BUILD / "2.05-custom-gx"
