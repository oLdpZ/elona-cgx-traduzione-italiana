# strumenti/dati_sorgente.py
"""La copia pinnata dei file di `elonaplus2.31\\data\\`, e il manifesto che la
sorveglia.

I file dati **non stanno nel clone di monte**: `sorgente/` li ha cancellati dal
working tree, e per `talk.txt` e `autopick.txt` il gioco installato e' piu'
recente del commit pinnato. Il riferimento e' quindi una copia presa **una volta
sola dal gioco** — che e' anche il file che l'eseguibile legge davvero.

Una copia senza sorveglianza pero' non e' un riferimento, e' solo un file
vecchio. Il manifesto (`dati/manifesto.json`, nel vault) dice quali byte ci si
aspetta di trovare, e serve a tre cose distinte:

1. l'altra macchina verifica di avere gli stessi byte prima di lavorare;
2. un aggiornamento del gioco si vede **subito**, invece di far scivolare le
   rese su un testo che non e' piu' quello;
3. i fine riga si **misurano**: un file dati a LF soltanto per HSP e' una riga
   sola, perche' `noteinfo(0)` conta i CRLF (lezione della 65a).

Uso:

    python -m strumenti.dati_sorgente            # verifica
    python -m strumenti.dati_sorgente --pinna    # la prima volta

⚠️ Il ripinnamento vuole `--forza` se il manifesto c'e' gia': assorbire un
aggiornamento di monte in silenzio e' esattamente il difetto che il manifesto
esiste per impedire.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
from dataclasses import dataclass, field
from pathlib import Path

from strumenti import percorsi

# I sette file di `data\` che contengono testo per il giocatore. `board`,
# `book`, `exhelp` e `talk` sono a blocchi (vedi `strumenti/dati.py`); i due
# `manual_*` sono prosa impaginata a mano; `autopick.txt` e' il file che il
# giocatore riscrive, e semina la sua copia nel salvataggio.
FILE_PINNATI = (
    "board.txt",
    "book.txt",
    "exhelp.txt",
    "talk.txt",
    "manual_ENG.txt",
    "manual_JP.txt",
    "autopick.txt",
)


def impronta(grezzo: bytes) -> dict:
    """Byte, md5 e **fine riga** — questi ultimi contati apposta."""
    return {
        "byte": len(grezzo),
        "md5": hashlib.md5(grezzo).hexdigest(),
        "righe_crlf": grezzo.count(b"\r\n"),
        "lf_soli": grezzo.count(b"\n") - grezzo.count(b"\r\n"),
    }


@dataclass
class Esito:
    mancanti: list[str] = field(default_factory=list)
    difformi: list[str] = field(default_factory=list)
    gioco_difformi: list[str] = field(default_factory=list)
    gioco_visto: bool = False

    @property
    def ok(self) -> bool:
        # il gioco che cambia non rompe la copia pinnata: rompe il presupposto
        # che la copia pinnata sia ancora quel che l'eseguibile legge. Va detto,
        # e va deciso da una persona - non fa fallire una verifica d'apertura.
        return not self.mancanti and not self.difformi


def _sola_lettura(percorso: Path) -> None:
    percorso.chmod(percorso.stat().st_mode & ~stat.S_IWRITE)


def _scrivibile(percorso: Path) -> None:
    if percorso.exists():
        percorso.chmod(percorso.stat().st_mode | stat.S_IWRITE)


def pinna(cartella_gioco: Path, destinazione: Path, manifesto: Path,
          nomi: tuple[str, ...] = FILE_PINNATI, forza: bool = False) -> dict:
    """Copia i file dal gioco e scrive il manifesto. Una volta sola."""
    if manifesto.exists() and not forza:
        raise SystemExit(
            f"{manifesto} esiste gia'. Ripinnare vuol dire accettare un testo di monte "
            "diverso da quello su cui sono state scritte le rese: se e' quel che vuoi, "
            "usa --forza, e poi controlla le voci orfane."
        )

    destinazione.mkdir(parents=True, exist_ok=True)
    manifesto.parent.mkdir(parents=True, exist_ok=True)

    impronte: dict[str, dict] = {}
    assenti: list[str] = []
    for nome in nomi:
        origine = cartella_gioco / nome
        if not origine.exists():
            assenti.append(nome)
            continue
        grezzo = origine.read_bytes()
        bersaglio = destinazione / nome
        _scrivibile(bersaglio)
        shutil.copyfile(origine, bersaglio)
        _sola_lettura(bersaglio)
        impronte[nome] = impronta(grezzo)

    manifesto.write_text(
        json.dumps({"origine": str(cartella_gioco), "file": impronte},
                   indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return {"pinnati": sorted(impronte), "assenti": assenti}


def verifica(destinazione: Path, manifesto: Path,
             cartella_gioco: Path | None = None) -> Esito:
    """La copia pinnata combacia ancora col manifesto? E il gioco con lei?"""
    atteso = json.loads(manifesto.read_text(encoding="utf-8"))["file"]
    esito = Esito()

    for nome, impronta_attesa in sorted(atteso.items()):
        percorso = destinazione / nome
        if not percorso.exists():
            esito.mancanti.append(nome)
            continue
        if impronta(percorso.read_bytes()) != impronta_attesa:
            esito.difformi.append(nome)

    if cartella_gioco is not None and cartella_gioco.is_dir():
        esito.gioco_visto = True
        for nome, impronta_attesa in sorted(atteso.items()):
            nel_gioco = cartella_gioco / nome
            if nel_gioco.exists() and impronta(nel_gioco.read_bytes()) != impronta_attesa:
                esito.gioco_difformi.append(nome)

    return esito


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="La copia pinnata dei file di data\\ e il suo manifesto.")
    analizzatore.add_argument("--pinna", action="store_true",
                              help="prende i file dal gioco e scrive il manifesto")
    analizzatore.add_argument("--forza", action="store_true",
                              help="ripinna sopra un manifesto esistente")
    argomenti = analizzatore.parse_args()

    cartella_gioco = percorsi.GIOCO / "data"

    if argomenti.pinna:
        esito = pinna(cartella_gioco, percorsi.DATI_SORGENTE, percorsi.MANIFESTO_DATI,
                      forza=argomenti.forza)
        for nome in esito["pinnati"]:
            print(f"  pinnato  {nome}")
        for nome in esito["assenti"]:
            print(f"  ASSENTE  {nome}  (il gioco non ce l'ha)")
        print(f"\nmanifesto: {percorsi.MANIFESTO_DATI}")
        return

    if not percorsi.MANIFESTO_DATI.exists():
        raise SystemExit("nessun manifesto: la prima volta si lancia con --pinna")

    esito = verifica(percorsi.DATI_SORGENTE, percorsi.MANIFESTO_DATI, cartella_gioco)
    for nome in esito.mancanti:
        print(f"  MANCA     {nome}  nella copia pinnata")
    for nome in esito.difformi:
        print(f"  DIFFORME  {nome}  la copia pinnata non e' piu' quella del manifesto")
    for nome in esito.gioco_difformi:
        print(f"  aggiornato {nome}  il GIOCO non combacia piu' col manifesto: "
              "monte ha cambiato il file, le rese vanno riviste")
    quanti = len(json.loads(percorsi.MANIFESTO_DATI.read_text(encoding='utf-8'))["file"])
    print(f"\ncopia pinnata: {quanti - len(esito.mancanti) - len(esito.difformi)} / {quanti} "
          f"intatti; gioco difforme su {len(esito.gioco_difformi)}")
    if not esito.ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
