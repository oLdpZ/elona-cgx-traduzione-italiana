# strumenti/tests/test_dati_estrai.py
"""L'estrazione di un lotto da un file dati.

La voce e' **una riga inglese**, non un blocco e non una coppia col giapponese:
in `board.txt` l'inglese e il giapponese non sono appaiati (misurato: 25 righe
contro 63, e `COOK,1` rende la seconda giapponese, non la prima). Il giapponese
si porta dietro come **contesto del blocco**, ed e' per questo che non entra
nella firma: cambiarlo non cambia quale riga si sta traducendo.
"""
import json

import pytest

from strumenti import dati, dati_estrai, percorsi

DUE_LINGUE = (
    "%COOK,GENERAL,JP\n"
    "primo:giapponese uno\n"
    "secondo:giapponese due\n"
    "%END\n"
    "\n"
    "%COOK,GENERAL,EN\n"
    "A new recipe!:Bring me {objective}.\n"
    "%END\n"
)


def _voci(testo, nome="board.txt"):
    return dati_estrai.voci(nome, dati.analizza(testo))


# ------------------------------------------------------------- la forma

def test_una_voce_per_riga_piena_del_blocco_inglese():
    (voce,) = _voci(DUE_LINGUE)
    assert voce["file"] == "board.txt"
    assert voce["blocco"] == "COOK,GENERAL"
    assert voce["riga"] == 1
    assert voce["en"] == "A new recipe!:Bring me {objective}."
    assert voce["it"] == ""


def test_il_giapponese_del_blocco_e_tutto_nel_contesto():
    (voce,) = _voci(DUE_LINGUE)
    assert voce["jp_contesto"] == ["primo:giapponese uno", "secondo:giapponese due"]


def test_un_blocco_inglese_senza_giapponese_ha_contesto_vuoto():
    (voce,) = _voci("%SOLO,EN\nuno:due\n%END\n")
    assert voce["jp_contesto"] == []


def test_i_blocchi_giapponesi_non_generano_voci():
    voci = _voci("%A,JP\nuno:due\n%END\n")
    assert voci == []


def test_un_blocco_senza_lingua_non_genera_voci():
    # %DEFINE di book.txt: non e' testo da leggere, e' una tabella di sostituzioni
    voci = _voci("%DEFINE\nqualcosa\n%END\n")
    assert voci == []


def test_le_righe_si_numerano_fra_le_piene_non_fra_tutte():
    # una riga vuota in mezzo non deve spostare il numero delle righe dopo:
    # se monte ne aggiunge una, le firme non devono cambiare tutte
    voci = _voci("%A,EN\nuno:x\n\ndue:y\n%END\n")
    assert [v["riga"] for v in voci] == [1, 2]
    assert [v["en"] for v in voci] == ["uno:x", "due:y"]


# -------------------------------------------------------------- la firma

def test_la_firma_cambia_se_cambia_l_inglese():
    prima = _voci("%A,EN\nuno:x\n%END\n")[0]["firma"]
    dopo = _voci("%A,EN\nuno:y\n%END\n")[0]["firma"]
    assert prima != dopo


def test_la_firma_cambia_se_cambia_il_blocco():
    prima = _voci("%A,EN\nuno:x\n%END\n")[0]["firma"]
    dopo = _voci("%B,EN\nuno:x\n%END\n")[0]["firma"]
    assert prima != dopo


def test_la_firma_cambia_se_cambia_il_file():
    prima = _voci("%A,EN\nuno:x\n%END\n", "board.txt")[0]["firma"]
    dopo = _voci("%A,EN\nuno:x\n%END\n", "talk.txt")[0]["firma"]
    assert prima != dopo


def test_la_firma_non_cambia_se_cambia_il_giapponese_accanto():
    # il contesto serve a chi traduce, non a identificare la riga: se monte
    # riscrivesse il giapponese, le rese italiane non andrebbero buttate
    prima = _voci("%A,JP\njp uno\n%END\n%A,EN\nuno:x\n%END\n")[0]["firma"]
    dopo = _voci("%A,JP\njp DUE\n%END\n%A,EN\nuno:x\n%END\n")[0]["firma"]
    assert prima == dopo


def test_le_firme_di_un_lotto_sono_tutte_diverse():
    voci = _voci("%A,EN\nuno:x\ndue:y\n%END\n%B,EN\nuno:x\n%END\n")
    assert len({v["firma"] for v in voci}) == len(voci) == 3


# ------------------------------------------------------------ il file vero

def _board():
    percorso = percorsi.DATI_SORGENTE / "board.txt"
    if not percorso.exists():
        pytest.skip("board.txt non e' ancora stato pinnato")
    return dati_estrai.voci("board.txt", dati.analizza(percorso.read_bytes().decode("cp932")))


def test_board_da_venticinque_voci():
    voci = _board()
    assert len(voci) == 25
    assert all(v["it"] == "" for v in voci)
    assert len({v["blocco"] for v in voci}) == 25, "un blocco, una riga: e' cosi' che sta il file"


def test_ogni_voce_di_board_ha_il_giapponese_del_suo_blocco():
    voci = _board()
    assert all(v["jp_contesto"] for v in voci)
    assert sum(len(v["jp_contesto"]) for v in voci) == 63


def test_ogni_voce_di_board_ha_un_titolo_e_un_corpo():
    for voce in _board():
        assert ":" in voce["en"], voce["blocco"]
        titolo = voce["en"].split(":")[0]
        assert titolo.strip(), voce["blocco"]


# --------------------------------------------------------------- il lotto

def test_il_lotto_si_scrive_e_si_rilegge(tmp_path):
    percorso = tmp_path / "board-001.jsonl"
    dati_estrai.scrivi_lotto(percorso, _voci(DUE_LINGUE))
    riletto = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    assert riletto == _voci(DUE_LINGUE)
