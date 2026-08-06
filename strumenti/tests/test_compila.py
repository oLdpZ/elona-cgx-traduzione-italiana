# strumenti/tests/test_compila.py
import os
import re
from pathlib import Path

import pytest

from strumenti import compila, percorsi


def test_l_host_a_32_bit_esiste():
    host = compila.host_32bit()
    assert host.exists()
    assert host.name.lower() == "powershell.exe"


def test_lo_script_powershell_e_accanto_al_modulo():
    assert compila.SCRIPT.exists()


# --- l'ABI, che e' la cosa costata di piu' a trovare -------------------------
# Ogni export di hspcmp.dll e' decorato @16 e prende quattro slot. Le funzioni
# che ricevono una stringa la leggono dal SECONDO slot: passarla nel primo non
# fallisce con un errore, fa saltare il processo con una access violation.
# Se qualcuno "semplifica" le firme, questi test lo fermano prima del crash.

DICHIARAZIONI = compila.SCRIPT.read_text(encoding="utf-8")


@pytest.mark.parametrize("funzione", ["hsc_ini", "hsc_refname", "hsc_objname",
                                      "hsc_compath", "hsc3_make"])
def test_le_funzioni_con_stringa_la_prendono_nel_secondo_slot(funzione):
    riga = next(r for r in DICHIARAZIONI.splitlines() if f" {funzione}(" in r)
    firma = riga.split(f"{funzione}(", 1)[1].split(")", 1)[0]
    assert firma.split(",")[0].strip().startswith("int"), funzione
    assert firma.split(",")[1].strip().startswith("string"), funzione


@pytest.mark.parametrize("funzione", ["hsc_getmes", "hsc3_messize"])
def test_le_funzioni_con_buffer_lo_prendono_nel_primo_slot(funzione):
    riga = next(r for r in DICHIARAZIONI.splitlines() if f" {funzione}(" in r)
    firma = riga.split(f"{funzione}(", 1)[1].split(")", 1)[0]
    primo = firma.split(",")[0].strip()
    assert primo.startswith("IntPtr") or primo.startswith("ref int"), funzione


def test_ogni_import_usa_il_nome_decorato():
    punti = re.findall(r'EntryPoint="([^"]+)"', DICHIARAZIONI)
    assert punti, "nessun EntryPoint dichiarato"
    for punto in punti:
        # i nomi puliti che hspcmp.as mostra non esistono nella tabella di export
        assert punto.startswith("_") and punto.endswith("@16"), punto


def test_ogni_import_dichiara_quattro_parametri():
    for firma in re.findall(r"extern int \w+\(([^)]*)\)", DICHIARAZIONI):
        assert len(firma.split(",")) == 4, firma


# --- la guardia sul sorgente upstream ----------------------------------------

def test_rifiuta_di_scrivere_l_oggetto_dentro_il_sorgente():
    with pytest.raises(compila.SorgenteInScrittura):
        compila._controlla_destinazione(percorsi.SORGENTE_HSP / "start.ax")


def test_rifiuta_anche_una_sottocartella_del_sorgente():
    with pytest.raises(compila.SorgenteInScrittura):
        compila._controlla_destinazione(percorsi.SORGENTE_HSP / "defines" / "x.ax")


def test_accetta_una_destinazione_fuori_dal_sorgente(tmp_path):
    compila._controlla_destinazione(tmp_path / "start.ax")
    compila._controlla_destinazione(percorsi.BUILD_HSP / "start.ax")


def test_l_eseguibile_non_si_costruisce_dentro_il_sorgente(tmp_path):
    # #pack scrive il file `packfile` nella cartella corrente: costruire l'exe
    # dentro SORGENTE lo sporcherebbe
    with pytest.raises(compila.SorgenteInScrittura):
        compila.compila(percorsi.SORGENTE_HSP, tmp_path / "start.ax", eseguibile=True)


# --- presupposti mancanti ----------------------------------------------------

def test_senza_sdk_lo_dice_invece_di_lanciare_powershell(tmp_path):
    with pytest.raises(compila.CompilazioneImpossibile, match="hspcmp.dll"):
        compila.compila(tmp_path, tmp_path / "out.ax", sdk=tmp_path)


def test_senza_il_file_principale_lo_dice(tmp_path):
    finto_sdk = tmp_path / "sdk"
    finto_sdk.mkdir()
    (finto_sdk / "hspcmp.dll").write_bytes(b"")
    with pytest.raises(compila.CompilazioneImpossibile, match="main.hsp"):
        compila.compila(tmp_path, tmp_path / "out.ax", sdk=finto_sdk)


# --- lettura dell'esito ------------------------------------------------------

def test_legge_i_campi_dallo_stdout_dell_host():
    campi = compila._leggi_esito("ini=0\ncomp=0\nruntime=\nmake=0\n")
    assert campi == {"ini": "0", "comp": "0", "runtime": "", "make": "0"}


def test_una_riga_senza_uguale_non_disturba():
    assert compila._leggi_esito("rumore\ncomp=-1") == {"comp": "-1"}


def test_gli_errori_escludono_gli_avvisi():
    esito = compila.Esito(
        ok=False, comp=-1,
        messaggi="#-avviso su una variabile\n#Error 12 in line 40 [chat.hsp]\n",
    )
    assert esito.errori() == ["#Error 12 in line 40 [chat.hsp]"]


def test_quando_compila_non_ci_sono_errori_da_mostrare():
    esito = compila.Esito(ok=True, comp=0, messaggi="#No error detected.")
    assert esito.errori() == []


# --- il cancello vero, contro il sorgente reale ------------------------------
# Costa una decina di secondi e pretende SDK e sorgente sul disco, quindi non
# gira nella suite normale. Il comando equivalente e':
#     python -m strumenti.compila --cancello

@pytest.mark.skipif(os.environ.get("ELONA_IT_CANCELLO") != "1",
                    reason="cancello lento: si accende con ELONA_IT_CANCELLO=1")
def test_il_sorgente_non_modificato_ricompila():
    esito = compila.cancello()
    assert esito.ok, esito.errori()
    assert compila.FIRMA_SUCCESSO in esito.messaggi


@pytest.mark.skipif(os.environ.get("ELONA_IT_CANCELLO") != "1",
                    reason="cancello lento: si accende con ELONA_IT_CANCELLO=1")
def test_il_cancello_non_lascia_tracce_nel_sorgente():
    prima = {p.name for p in percorsi.SORGENTE_HSP.iterdir()}
    compila.cancello()
    assert {p.name for p in percorsi.SORGENTE_HSP.iterdir()} == prima
