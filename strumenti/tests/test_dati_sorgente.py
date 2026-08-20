# strumenti/tests/test_dati_sorgente.py
"""La copia pinnata dei file di `data\\` e il manifesto che la sorveglia.

I file dati non stanno nel clone di monte, quindi il riferimento e' una copia
presa **una volta** dal gioco. Una copia senza sorveglianza pero' non e' un
riferimento: e' solo un file vecchio. Il manifesto nel vault dice quali byte ci
si aspetta di trovarci, e serve a tre cose distinte:

1. l'altra macchina verifica di avere gli stessi byte prima di lavorare
   (vedi la memoria `elona-due-macchine`);
2. un aggiornamento del gioco si vede subito, invece di far scivolare le rese
   su un testo che non e' piu' quello;
3. i **fine riga** si misurano, perche' un file dati a LF soltanto per HSP e'
   una riga sola (lezione della 65a: due CSV a LF piantarono il gioco).

⚠️ E il ripinnamento **non e' automatico**: assorbire un aggiornamento di monte
in silenzio e' esattamente il difetto che il manifesto esiste per impedire.
"""
import json
import stat

import pytest

from strumenti import dati_sorgente

CRLF = b"%A,EN\r\nuno\r\n%END\r\n"


def _manomettibile(percorso):
    percorso.chmod(percorso.stat().st_mode | stat.S_IWRITE)


def _cartella_finta(tmp_path, contenuti):
    cartella = tmp_path / "gioco"
    cartella.mkdir()
    for nome, byte in contenuti.items():
        (cartella / nome).write_bytes(byte)
    return cartella


# ------------------------------------------------------------- l'impronta

def test_l_impronta_conta_byte_md5_e_fine_riga():
    impronta = dati_sorgente.impronta(CRLF)
    assert impronta["byte"] == len(CRLF)
    assert len(impronta["md5"]) == 32
    assert impronta["righe_crlf"] == 3
    assert impronta["lf_soli"] == 0


def test_l_impronta_vede_un_file_degradato_a_lf():
    impronta = dati_sorgente.impronta(CRLF.replace(b"\r\n", b"\n"))
    assert impronta["righe_crlf"] == 0
    assert impronta["lf_soli"] == 3


# ------------------------------------------------------------ il pinnaggio

def test_pinnare_copia_i_file_e_scrive_il_manifesto(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF, "talk.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"

    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt", "talk.txt"))

    assert (destinazione / "board.txt").read_bytes() == CRLF
    scritto = json.loads(manifesto.read_text(encoding="utf-8"))
    assert sorted(scritto["file"]) == ["board.txt", "talk.txt"]
    assert scritto["file"]["board.txt"]["byte"] == len(CRLF)


def test_pinnare_salta_i_file_che_il_gioco_non_ha(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"

    esito = dati_sorgente.pinna(gioco, destinazione, manifesto,
                                nomi=("board.txt", "manca.txt"))

    assert esito["assenti"] == ["manca.txt"]
    assert "manca.txt" not in json.loads(manifesto.read_text(encoding="utf-8"))["file"]


def test_ripinnare_sopra_un_manifesto_esistente_e_rifiutato(tmp_path):
    # assorbire un aggiornamento di monte in silenzio e' il difetto che il
    # manifesto esiste per impedire
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    with pytest.raises(SystemExit):
        dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",), forza=True)


# ------------------------------------------------------------ la verifica

def test_la_verifica_e_pulita_subito_dopo_il_pinnaggio(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    esito = dati_sorgente.verifica(destinazione, manifesto, gioco)
    assert esito.ok
    assert esito.difformi == [] and esito.mancanti == [] and esito.gioco_difformi == []


def test_la_verifica_vede_la_copia_pinnata_cambiata(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    # la copia pinnata e' marcata di sola lettura apposta: per manometterla
    # bisogna volerlo, e il test lo vuole
    _manomettibile(destinazione / "board.txt")
    (destinazione / "board.txt").write_bytes(CRLF + b"in piu'\r\n")

    esito = dati_sorgente.verifica(destinazione, manifesto, gioco)
    assert not esito.ok
    assert esito.difformi == ["board.txt"]


def test_la_verifica_vede_la_copia_pinnata_sparita(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    _manomettibile(destinazione / "board.txt")
    (destinazione / "board.txt").unlink()

    esito = dati_sorgente.verifica(destinazione, manifesto, gioco)
    assert not esito.ok
    assert esito.mancanti == ["board.txt"]


def test_un_aggiornamento_del_gioco_si_segnala_ma_non_e_un_guasto(tmp_path):
    # il gioco che cambia non rompe la copia pinnata: rompe il presupposto che
    # la copia pinnata sia ancora quel che l'eseguibile legge. Va detto, e va
    # deciso da una persona.
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    (gioco / "board.txt").write_bytes(CRLF.replace(b"uno", b"due"))

    esito = dati_sorgente.verifica(destinazione, manifesto, gioco)
    assert esito.gioco_difformi == ["board.txt"]
    assert esito.ok, "la copia pinnata e' intatta: il referto avverte, non fallisce"


def test_senza_la_cartella_del_gioco_la_verifica_guarda_solo_la_copia(tmp_path):
    gioco = _cartella_finta(tmp_path, {"board.txt": CRLF})
    destinazione = tmp_path / "dati-sorgente"
    manifesto = tmp_path / "manifesto.json"
    dati_sorgente.pinna(gioco, destinazione, manifesto, nomi=("board.txt",))

    esito = dati_sorgente.verifica(destinazione, manifesto, tmp_path / "non-c-e")
    assert esito.ok
    assert esito.gioco_difformi == []


# ------------------------------------------------- il manifesto vero, in repo

def test_il_manifesto_del_progetto_e_leggibile_e_coerente():
    from strumenti import percorsi
    if not percorsi.MANIFESTO_DATI.exists():
        pytest.skip("il manifesto dei file dati non e' ancora stato pinnato")
    manifesto = json.loads(percorsi.MANIFESTO_DATI.read_text(encoding="utf-8"))
    assert manifesto["file"], "un manifesto vuoto non sorveglia niente"
    for nome, impronta in manifesto["file"].items():
        assert impronta["byte"] > 0, nome
        assert len(impronta["md5"]) == 32, nome
        assert impronta["lf_soli"] == 0, (
            f"{nome}: il file pinnato ha dei fine riga a LF soltanto. "
            "Per HSP un file cosi' e' una riga sola (lezione della 65a)."
        )


def test_la_copia_pinnata_combacia_col_manifesto():
    from strumenti import percorsi
    if not percorsi.MANIFESTO_DATI.exists() or not percorsi.DATI_SORGENTE.is_dir():
        pytest.skip("i file dati non sono ancora stati pinnati")
    esito = dati_sorgente.verifica(percorsi.DATI_SORGENTE, percorsi.MANIFESTO_DATI,
                                   percorsi.GIOCO / "data")
    assert esito.ok, f"mancanti {esito.mancanti}, difformi {esito.difformi}"
