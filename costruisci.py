#!/usr/bin/env python3
"""Costruisce sul TUO computer l'eseguibile italiano di Elona+ Custom-GX.

⭐ **Perche' si compila in casa invece di scaricare un eseguibile pronto.** Il
sorgente di Custom-GX non ha una licenza, quindi nessuno ci ha dato il permesso
di ridistribuire il gioco compilato. Questo programma non ridistribuisce niente
di nessuno: il **sorgente** se lo prende da GitHub, l'**SDK HSP** dal sito di
Onion Software, i **file di dato** dalla tua installazione, e da noi arriva solo
il **dizionario**, che e' l'unica cosa nostra.

⚠️ **Non tocca niente di quel che hai.** L'eseguibile italiano si chiama
`cgx-ita.exe` e si mette ACCANTO al tuo `elonapluscgx.exe`, che resta dov'e' e
continua a funzionare. I file di testo italiani si chiamano `*_it.txt` e il
gioco li legge solo se ci sono. I salvataggi non vengono aperti nemmeno per
sbaglio. Per tornare indietro si cancellano sette file, e c'e' `disinstalla.bat`
che lo fa.

## Uso

    costruisci.bat                          (doppio clic: cerca il gioco da se')
    python costruisci.py --gioco "C:\\Games\\Elona\\elonaplus2.31"

La prima volta scarica circa 60 MB e ci mette qualche minuto. Le volte dopo
riusa quel che ha gia' scaricato.
"""
import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

QUI = Path(__file__).resolve().parent

# ⚠️ La versione di Custom-GX a cui questa traduzione si riferisce. Cambiarla
# senza rifare il dizionario vuol dire agganciare righe che non esistono piu':
# la catena si ferma da sola, ma e' bene saperlo prima.
VERSIONE_CGX = "2.31.2.0"

SORGENTE_URL = ("https://codeload.github.com/JianmengYu/ElonaPlusCustom-GX/"
                "zip/refs/tags/" + VERSIONE_CGX)

# ⚠️ L'SDK HSP 3.4 non e' piu' nell'elenco dei download di hsp.tv, che oggi
# mostra solo la 3.6 e la 3.7. Il file pero' e' ancora servito dal sito di
# Onion Software a questo indirizzo, ed e' quello che Custom-GX vuole.
SDK_URL = "http://www.onionsoft.net/hsp/file/hsp34a.zip"
SDK_SHA256 = "2b841c71bbe4efad0dce1bed88bdd72bfd4ebe5e5671689b4a5833c105b278cf"
SDK_BYTE = 37016153

# ⚠️ L'eseguibile ufficiale di Custom-GX 2.31.2.0. Serve solo a dire «hai la
# versione giusta»: non lo apriamo e non lo tocchiamo.
GIOCO_EXE = "elonapluscgx.exe"
GIOCO_SHA256 = "60eda5f7ed44ddfe9e02318955a5169f2cbe29c0891117a902af1973a27a14c8"

NOSTRO_EXE = "cgx-ita.exe"

# I sei file di testo italiani, che si aggiungono senza sostituire niente
DATI_IT = ["autopick_it.txt", "board_it.txt", "book_it.txt", "exhelp_it.txt",
           "manual_ENG_it.txt", "talk_it.txt"]

CERCA_GIOCO = [
    Path(r"C:\Games\Elona\elonaplus2.31"),
    Path(r"C:\Elona\elonaplus2.31"),
    Path(r"C:\elonaplus2.31"),
    Path.home() / "elonaplus2.31",
    Path.home() / "Games" / "elonaplus2.31",
]


class NonSiPuo(SystemExit):
    """Un presupposto non c'e'. Si dice quale, e come si rimedia."""


def passo(n, quanti, testo):
    print()
    print("[%d/%d] %s" % (n, quanti, testo))


def impronta(percorso: Path) -> str:
    h = hashlib.sha256()
    with percorso.open("rb") as f:
        for pezzo in iter(lambda: f.read(1 << 20), b""):
            h.update(pezzo)
    return h.hexdigest()


def scarica(url: str, destinazione: Path, atteso: str | None = None,
            byte_attesi: int | None = None) -> None:
    """Scarica se manca, e controlla l'impronta se la conosciamo."""
    if destinazione.exists():
        if atteso is None or impronta(destinazione) == atteso:
            print("   c'e' gia': %s" % destinazione.name)
            return
        print("   %s non e' quel che ci aspettavamo: lo riscarico"
              % destinazione.name)
        destinazione.unlink()

    destinazione.parent.mkdir(parents=True, exist_ok=True)
    print("   scarico %s" % url)
    parziale = destinazione.with_suffix(destinazione.suffix + ".parziale")
    with urllib.request.urlopen(url) as risposta, parziale.open("wb") as uscita:
        totale = int(risposta.headers.get("Content-Length") or 0)
        fatti = 0
        while pezzo := risposta.read(1 << 18):
            uscita.write(pezzo)
            fatti += len(pezzo)
            if totale:
                print("\r   %5.1f%%  (%d di %d MB)"
                      % (100.0 * fatti / totale, fatti >> 20, totale >> 20),
                      end="", flush=True)
        print()
    parziale.replace(destinazione)

    if byte_attesi is not None and destinazione.stat().st_size != byte_attesi:
        raise NonSiPuo(
            "Il file scaricato non ha la dimensione giusta (%d invece di %d).\n"
            "Riprova: puo' essere caduta la connessione."
            % (destinazione.stat().st_size, byte_attesi))
    if atteso is not None and impronta(destinazione) != atteso:
        raise NonSiPuo(
            "Il file scaricato non e' quello che ci aspettavamo.\n"
            "  atteso  %s\n  trovato %s\n"
            "Non lo uso: se il sito ha cambiato il file, la traduzione va "
            "rifatta apposta." % (atteso, impronta(destinazione)))


def estrai(archivio: Path, dentro: Path, nomi_cp932: bool = False) -> None:
    """Estrae, tenendo conto che i nomi giapponesi non sono UTF-8.

    ⚠️ L'SDK HSP e' un archivio giapponese e i nomi delle voci sono in CP932.
    Senza questa conversione i file finiscono con nomi storti e il compilatore
    non trova le sue librerie: e' una trappola nota, e costa un pomeriggio.
    """
    dentro.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archivio) as z:
        for voce in z.infolist():
            nome = voce.filename
            if nomi_cp932 and not (voce.flag_bits & 0x800):
                try:
                    nome = nome.encode("cp437").decode("cp932")
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass
            bersaglio = dentro / nome
            if voce.is_dir():
                bersaglio.mkdir(parents=True, exist_ok=True)
                continue
            bersaglio.parent.mkdir(parents=True, exist_ok=True)
            with z.open(voce) as dentro_zip, bersaglio.open("wb") as fuori:
                shutil.copyfileobj(dentro_zip, fuori)


def srotola(provvisoria: Path, bersaglio: Path, spia: str) -> None:
    """Sposta in `bersaglio` la cartella che contiene davvero `spia`.

    ⚠️ Sia l'archivio dell'SDK sia quello di GitHub avvolgono tutto in una
    cartella sola — `hsp34\\` l'uno, `ElonaPlusCustom-GX-2.31.2.0\\` l'altro — e
    chi estrae e basta si ritrova il compilatore un gradino piu' sotto di dove
    lo cerca. E' costato la prima prova di questo programma.
    """
    if (provvisoria / spia).exists():
        dentro = provvisoria
    else:
        candidate = [c for c in provvisoria.iterdir() if c.is_dir()]
        dentro = next((c for c in candidate if (c / spia).exists()),
                      candidate[0] if len(candidate) == 1 else None)
        if dentro is None:
            raise NonSiPuo(
                "Nell'archivio estratto non trovo %s: dentro %s ci sono %d "
                "cartelle." % (spia, provvisoria, len(candidate)))
    shutil.rmtree(bersaglio, ignore_errors=True)
    dentro.replace(bersaglio)
    shutil.rmtree(provvisoria, ignore_errors=True)


def trova_gioco(indicata: str | None) -> Path:
    if indicata:
        cartella = Path(indicata).expanduser().resolve()
        if not (cartella / GIOCO_EXE).exists():
            raise NonSiPuo(
                "In %s non c'e' %s.\nIndicami la cartella dove hai installato "
                "Elona+ con Custom-GX." % (cartella, GIOCO_EXE))
        return cartella
    for cartella in CERCA_GIOCO:
        if (cartella / GIOCO_EXE).exists():
            print("   trovato: %s" % cartella)
            return cartella
    raise NonSiPuo(
        "Non trovo la cartella del gioco da solo.\n"
        "Lanciami cosi', con la tua:\n"
        '    python costruisci.py --gioco "C:\\percorso\\a\\elonaplus2.31"')


def controlla_versione(gioco: Path, forza: bool) -> None:
    trovata = impronta(gioco / GIOCO_EXE)
    if trovata == GIOCO_SHA256:
        print("   versione giusta: Custom-GX %s" % VERSIONE_CGX)
        return
    messaggio = (
        "Il tuo %s non e' la versione %s, che e' quella per cui questa\n"
        "traduzione e' stata fatta.\n"
        "  atteso  %s\n  trovato %s\n"
        "Con una versione diversa il dizionario aggancia righe che nel "
        "frattempo sono cambiate,\ne la costruzione si ferma a meta'. "
        "Scarica Custom-GX %s dalle sue release,\noppure rilanciami con "
        "--forza se sai quel che stai facendo."
        % (GIOCO_EXE, VERSIONE_CGX, GIOCO_SHA256, trovata, VERSIONE_CGX))
    if not forza:
        raise NonSiPuo(messaggio)
    print("   ⚠️ " + messaggio.replace("\n", "\n   "))


def esegui(comando: list[str], ambiente: dict, dove: Path) -> None:
    esito = subprocess.run(comando, cwd=dove, env=ambiente,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, encoding="utf-8", errors="replace")
    if esito.returncode != 0:
        print(esito.stdout)
        raise NonSiPuo(
            "Il passo «%s» si e' fermato. Il motivo e' nelle righe qui sopra."
            % " ".join(comando[2:]))
    return esito.stdout


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Costruisce l'eseguibile italiano di Elona+ Custom-GX.")
    analizzatore.add_argument("--gioco", help="la cartella dove sta il gioco")
    analizzatore.add_argument(
        "--lavoro", help="dove scaricare e compilare (default: _lavoro qui "
                         "accanto)")
    analizzatore.add_argument(
        "--forza", action="store_true",
        help="prosegui anche se la versione del gioco non combacia")
    argomenti = analizzatore.parse_args()

    if sys.version_info < (3, 11):
        raise NonSiPuo("Serve Python 3.11 o piu' nuovo; questo e' il %d.%d."
                       % sys.version_info[:2])
    if os.name != "nt":
        raise NonSiPuo("Il compilatore HSP gira solo su Windows.")

    lavoro = Path(argomenti.lavoro).resolve() if argomenti.lavoro \
        else QUI / "_lavoro"
    lavoro.mkdir(parents=True, exist_ok=True)

    print("Traduzione italiana di Elona+ Custom-GX %s" % VERSIONE_CGX)
    print("cartella di lavoro: %s" % lavoro)

    passo(1, 7, "Cerco il gioco e ne controllo la versione")
    gioco = trova_gioco(argomenti.gioco)
    controlla_versione(gioco, argomenti.forza)

    passo(2, 7, "Prendo il sorgente di Custom-GX da GitHub")
    zip_sorgente = lavoro / ("cgx-%s.zip" % VERSIONE_CGX)
    scarica(SORGENTE_URL, zip_sorgente)
    sorgente = lavoro / "sorgente"
    if not (sorgente / "2.05-custom-gx" / "main.hsp").exists():
        provvisoria = lavoro / "_estratto"
        shutil.rmtree(provvisoria, ignore_errors=True)
        estrai(zip_sorgente, provvisoria)
        srotola(provvisoria, sorgente, "2.05-custom-gx")
    print("   sorgente pronto: %s" % sorgente)
    controlla_sorgente(sorgente)

    passo(3, 7, "Prendo l'SDK HSP 3.4 da onionsoft.net")
    zip_sdk = lavoro / "hsp34a.zip"
    scarica(SDK_URL, zip_sdk, SDK_SHA256, SDK_BYTE)
    sdk = lavoro / "hsp34"
    if not (sdk / "hspcmp.dll").exists():
        shutil.rmtree(sdk, ignore_errors=True)
        provvisoria = lavoro / "_sdk"
        shutil.rmtree(provvisoria, ignore_errors=True)
        estrai(zip_sdk, provvisoria, nomi_cp932=True)
        # ⚠️ L'archivio dell'SDK porta una cartella `hsp34\` in testa, e quello
        # del sorgente una cartella col nome del tag: in tutt'e due i casi quel
        # che serve sta un gradino piu' sotto.
        srotola(provvisoria, sdk, "hspcmp.dll")
    if not (sdk / "hspcmp.dll").exists():
        raise NonSiPuo("L'SDK si e' estratto ma hspcmp.dll non c'e' in %s."
                       % sdk)
    shutil.copy2(sorgente / "2.05-custom-gx" / "hsplua.dll", sdk / "hsplua.dll")
    print("   SDK pronto: %s" % sdk)

    ambiente = dict(os.environ)
    ambiente["ELONA_IT_LAVORO"] = str(lavoro)
    ambiente["ELONA_IT_GIOCO"] = str(gioco)
    ambiente["PYTHONPATH"] = str(QUI)
    ambiente["PYTHONIOENCODING"] = "utf-8"
    py = [sys.executable, "-m"]

    passo(4, 7, "Prendo dalla TUA installazione i file di data\\")
    esegui(py + ["strumenti.dati_sorgente", "--pinna", "--forza"], ambiente, QUI)
    print("   fatto")

    passo(5, 7, "Applico la traduzione al sorgente (nessuna scrittura su di esso)")
    for modulo, argomento in [("strumenti.applica", None),
                              ("strumenti.scene", "--applica"),
                              ("strumenti.carte", "--applica"),
                              ("strumenti.schede", "--applica"),
                              ("strumenti.dialoghi", "--applica")]:
        comando = py + [modulo] + ([argomento] if argomento else [])
        esegui(comando, ambiente, QUI)
        print("   %s" % modulo.split(".")[-1])

    passo(6, 7, "Compilo (ci vuole un minuto)")
    esegui(py + ["strumenti.compila", "--eseguibile"], ambiente, QUI)
    costruito = lavoro / "build" / "2.05-custom-gx" / "elonapluscgx.exe"
    if not costruito.exists():
        raise NonSiPuo("La compilazione dice di essere andata bene ma "
                       "l'eseguibile non c'e': %s" % costruito)
    print("   %d byte" % costruito.stat().st_size)

    passo(7, 7, "Metto la traduzione accanto al gioco")
    shutil.copy2(costruito, gioco / NOSTRO_EXE)
    print("   %s" % (gioco / NOSTRO_EXE))
    costruiti_dati = lavoro / "build" / "dati"
    copiati = 0
    for nome in DATI_IT:
        sorgente_dato = costruiti_dati / nome
        if sorgente_dato.exists():
            shutil.copy2(sorgente_dato, gioco / "data" / nome)
            copiati += 1
    print("   %d file di testo italiani in data\\" % copiati)
    scrivi_disinstalla(gioco)

    print()
    print("FATTO. Per giocare in italiano lancia:")
    print("   %s" % (gioco / NOSTRO_EXE))
    print()
    print("Il tuo %s non e' stato toccato e funziona come prima." % GIOCO_EXE)
    print("Per tornare indietro: %s" % (gioco / "disinstalla-italiano.bat"))


def controlla_sorgente(sorgente: Path) -> None:
    """Il sorgente scaricato e' quello che il dizionario si aspetta?

    ⚠️ Non si controlla l'impronta dell'ARCHIVIO: GitHub rigenera i suoi zip e
    la stessa versione puo' avere impronte diverse in momenti diversi. Si
    controllano i file, che invece non cambiano.
    """
    manifesto = QUI / "dati" / "manifesto-sorgente.txt"
    if not manifesto.exists():
        print("   (nessun manifesto del sorgente: salto il controllo)")
        return
    hsp = sorgente / "2.05-custom-gx"
    difformi, mancanti = [], []
    for riga in manifesto.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        atteso, nome = riga.split(None, 1)
        percorso = hsp / nome.strip()
        if not percorso.exists():
            mancanti.append(nome.strip())
        elif impronta(percorso).lower() != atteso.strip().lower():
            difformi.append(nome.strip())
    if mancanti or difformi:
        raise NonSiPuo(
            "Il sorgente scaricato non e' quello atteso: %d file mancanti, "
            "%d diversi.\nPrimi: %s\nLa traduzione e' fatta sulla versione %s."
            % (len(mancanti), len(difformi),
               ", ".join((mancanti + difformi)[:5]), VERSIONE_CGX))
    print("   manifesto: tutti i file combaciano")


def scrivi_disinstalla(gioco: Path) -> None:
    righe = ["@echo off",
             "echo Tolgo la traduzione italiana. Il gioco resta com'era.",
             'del /q "%~dp0' + NOSTRO_EXE + '"']
    righe += ['del /q "%~dp0data\\' + nome + '"' for nome in DATI_IT]
    righe += ["echo Fatto.", "pause"]
    (gioco / "disinstalla-italiano.bat").write_text(
        "\r\n".join(righe) + "\r\n", encoding="ascii")


if __name__ == "__main__":
    try:
        main()
    except NonSiPuo as guaio:
        print()
        print("NON SI PUO' PROSEGUIRE")
        print(guaio)
        sys.exit(1)
