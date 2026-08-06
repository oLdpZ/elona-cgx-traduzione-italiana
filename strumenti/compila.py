# strumenti/compila.py
"""Compila il sorgente HSP senza la GUI dell'editor, e ne costruisce l'eseguibile.

Il cancello della Fase 0 - «il sorgente ricompila» - era dato per manuale perche'
l'SDK HSP si guida dall'editor. Non e' vero: `hspcmp.dll` espone tutta l'API del
compilatore. L'unico ostacolo e' che la DLL e' a 32 bit, e un Python a 64 bit non
la puo' caricare. Windows ha pero' gia' un host a 32 bit installato di serie,
`SysWOW64\\WindowsPowerShell`, e da li' la si pilota: il lavoro vero sta in
`compila.ps1`, questo modulo lo invoca e ne legge l'esito.

Regola non negoziabile: SORGENTE non riceve scritture. L'oggetto va sempre altrove,
e l'eseguibile si costruisce solo dentro BUILD, perche' `#pack` scrive il file
`packfile` nella cartella corrente.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from strumenti import percorsi

SCRIPT = Path(__file__).resolve().parent / "compila.ps1"

# I messaggi del compilatore HSP sono in CP932: il sorgente e' giapponese e lo
# sono anche i nomi che il compilatore cita negli avvisi.
CODIFICA_MESSAGGI = "cp932"

FIRMA_SUCCESSO = "#No error detected."


class CompilazioneImpossibile(RuntimeError):
    """Manca un presupposto: l'host a 32 bit, l'SDK, o il sorgente."""


class SorgenteInScrittura(ValueError):
    """Qualcuno ha chiesto di scrivere dentro SORGENTE. Non succede."""


@dataclass
class Esito:
    ok: bool
    comp: int
    messaggi: str
    runtime: str = ""
    make: str = ""
    oggetto: Path | None = None
    eseguibile: Path | None = None
    avvisi: list[str] = field(default_factory=list)

    def errori(self) -> list[str]:
        """Le righe che il compilatore ha emesso quando si e' fermato.

        Gli avvisi iniziano con `#-`, l'intestazione e le statistiche con `#`.
        Quel che resta, se la compilazione fallisce, e' il motivo.
        """
        if self.ok:
            return []
        return [r for r in self.messaggi.splitlines()
                if r.strip() and not r.startswith("#-")]


def host_32bit() -> Path:
    """Il PowerShell a 32 bit. Su Windows x64 c'e' sempre; altrove non serve."""
    radice = Path(os.environ.get("SystemRoot", r"C:\Windows"))
    for sotto in ("SysWOW64", "System32"):  # System32 e' il caso di un Windows a 32 bit
        candidato = radice / sotto / "WindowsPowerShell" / "v1.0" / "powershell.exe"
        if candidato.exists():
            return candidato
    raise CompilazioneImpossibile(
        "Nessun PowerShell trovato per ospitare hspcmp.dll, che e' a 32 bit."
    )


def _controlla_destinazione(percorso: Path) -> None:
    sorgente = percorsi.SORGENTE.resolve()
    percorso = percorso.resolve()
    if percorso == sorgente or sorgente in percorso.parents:
        raise SorgenteInScrittura(
            f"{percorso} sta dentro SORGENTE. Il sorgente upstream non si scrive: "
            "l'oggetto va in una cartella temporanea, l'eseguibile in BUILD."
        )


def _leggi_esito(stdout: str) -> dict[str, str]:
    campi = {}
    for riga in stdout.splitlines():
        if "=" in riga:
            chiave, _, valore = riga.partition("=")
            campi[chiave.strip()] = valore.strip()
    return campi


def compila(sorgente: Path, oggetto: Path, *, eseguibile: bool = False,
            sdk: Path | None = None, principale: str = "main.hsp",
            debug: int = 0) -> Esito:
    """Compila `sorgente/principale` producendo `oggetto`. Con `eseguibile`, anche l'exe.

    `eseguibile` implica la creazione del packfile, che scrive nella cartella del
    sorgente: per questo e' ammesso solo fuori da SORGENTE.
    """
    sdk = Path(sdk) if sdk else percorsi.HSP
    sorgente = Path(sorgente)
    oggetto = Path(oggetto)

    if not (sdk / "hspcmp.dll").exists():
        raise CompilazioneImpossibile(
            f"hspcmp.dll non e' in {sdk}. L'SDK HSP 3.4 va estratto li' "
            "(vedi RIPRESA-sessione.md)."
        )
    if not (sorgente / principale).exists():
        raise CompilazioneImpossibile(f"{principale} non e' in {sorgente}.")

    _controlla_destinazione(oggetto)
    if eseguibile:
        _controlla_destinazione(sorgente)

    oggetto.parent.mkdir(parents=True, exist_ok=True)
    # bit2 di p2 accende la creazione del packfile a partire da #pack/#packopt
    p2 = 4 if eseguibile else 0

    with tempfile.TemporaryDirectory() as tmp:
        messaggi_grezzi = Path(tmp) / "messaggi.txt"
        comando = [
            str(host_32bit()), "-NoProfile", "-NonInteractive",
            "-ExecutionPolicy", "Bypass", "-File", str(SCRIPT),
            "-Sdk", str(sdk), "-SrcDir", str(sorgente),
            "-ObjOut", str(oggetto), "-MesOut", str(messaggi_grezzi),
            "-Main", principale, "-P1", str(debug), "-P2", str(p2),
        ]
        if eseguibile:
            comando.append("-MakeExe")
        finito = subprocess.run(comando, capture_output=True, text=True)
        if finito.returncode != 0:
            raise CompilazioneImpossibile(
                f"L'host a 32 bit e' uscito con {finito.returncode}: "
                f"{finito.stderr.strip() or finito.stdout.strip()}"
            )
        testo = messaggi_grezzi.read_bytes().decode(CODIFICA_MESSAGGI, errors="replace") \
            if messaggi_grezzi.exists() else ""

    campi = _leggi_esito(finito.stdout)
    comp = int(campi.get("comp", "-1"))
    esito = Esito(
        ok=(comp == 0),
        comp=comp,
        messaggi=testo,
        runtime=campi.get("runtime", ""),
        make=campi.get("make", ""),
        oggetto=oggetto if comp == 0 and oggetto.exists() else None,
        avvisi=[r for r in testo.splitlines() if r.startswith("#-")],
    )
    if eseguibile and esito.ok:
        prodotti = sorted(sorgente.glob("*.exe"), key=lambda p: p.stat().st_mtime)
        esito.eseguibile = prodotti[-1] if prodotti else None
    return esito


def cancello(sdk: Path | None = None) -> Esito:
    """Il cancello: SORGENTE, non modificato, deve compilare senza errori.

    L'oggetto finisce in una cartella temporanea che sparisce subito: qui non
    interessa il prodotto, interessa il verdetto.
    """
    with tempfile.TemporaryDirectory() as tmp:
        return compila(percorsi.SORGENTE_HSP, Path(tmp) / "start.ax", sdk=sdk)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--sorgente", type=Path, default=None,
                    help="cartella da compilare (default: SORGENTE per --cancello, BUILD altrimenti)")
    ap.add_argument("--oggetto", type=Path, default=None, help="percorso del .ax da produrre")
    ap.add_argument("--eseguibile", action="store_true", help="costruisci anche l'exe (solo fuori da SORGENTE)")
    ap.add_argument("--cancello", action="store_true", help="verifica che SORGENTE ricompili, senza produrre nulla")
    ap.add_argument("--avvisi", action="store_true", help="stampa anche gli avvisi del compilatore")
    argomenti = ap.parse_args(argv)

    if argomenti.cancello:
        esito = cancello()
    else:
        sorgente = argomenti.sorgente or percorsi.BUILD_HSP
        oggetto = argomenti.oggetto or (sorgente / "start.ax")
        esito = compila(sorgente, oggetto, eseguibile=argomenti.eseguibile)

    if argomenti.avvisi:
        for riga in esito.avvisi:
            print(riga)
    if esito.ok:
        print(FIRMA_SUCCESSO if FIRMA_SUCCESSO in esito.messaggi else "compilato")
        if esito.eseguibile:
            print(f"eseguibile: {esito.eseguibile} ({esito.eseguibile.stat().st_size} byte)")
        return 0
    print("COMPILAZIONE FALLITA", file=sys.stderr)
    for riga in esito.errori():
        print(riga, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
