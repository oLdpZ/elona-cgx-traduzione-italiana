# strumenti/tests/test_toppe.py
"""Le toppe: le sostituzioni fuori da `lang()`, che il dizionario non raggiunge."""
import json

import pytest

from strumenti import percorsi
from strumenti.applica import (SorgenteCorrotto, applica_toppe, carica_toppe)

RIGA_NAME = '\t\treturn "the " + cdatan(CDATAN_NAME, name_arg1)'


def toppa(**sovrascritture):
    base = {
        "file": "init.hsp",
        "cerca": RIGA_NAME,
        "sostituisci": '\t\treturn cdatan(CDATAN_NAME, name_arg1)',
        "motivo": "prova",
    }
    base.update(sovrascritture)
    return base


def sorgente(*righe):
    return "\r\n".join(righe) + "\r\n"


def test_una_toppa_sostituisce_la_riga_esatta():
    testo = sorgente("#defcfunc name int name_arg1", RIGA_NAME, "\treturn 0")
    nuovo, quante = applica_toppe("init.hsp", testo, [toppa()])
    assert quante == 1
    assert '"the "' not in nuovo
    assert "return cdatan(CDATAN_NAME, name_arg1)" in nuovo
    # il resto del file non si tocca, terminatori compresi
    assert nuovo.startswith("#defcfunc name int name_arg1\r\n")
    assert nuovo.endswith("\treturn 0\r\n")


def test_una_toppa_per_un_altro_file_non_si_applica():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("text.hsp", testo, [toppa()])
    assert quante == 0
    assert nuovo == testo


def test_una_riga_che_non_c_e_piu_ferma_la_catena():
    # e' il caso del riallineamento a una nuova versione CGX (SPEC 3.1): se
    # upstream ha riscritto quella riga, applicare la toppa alla cieca non ha
    # senso. Meglio fermarsi e rifarla che produrre un eseguibile diverso da
    # quello che si crede.
    testo = sorgente("#defcfunc name int name_arg1", "\treturn 0")
    with pytest.raises(SorgenteCorrotto, match="non esiste"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_riga_ambigua_ferma_la_catena():
    # due righe identiche: quale delle due? Indovinare significa avere una
    # probabilita' su due di toppare quella sbagliata, in silenzio.
    testo = sorgente(RIGA_NAME, "\tx = 1", RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="due volte|2 volte|piu' di una"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_toppa_che_non_cambia_niente_e_un_errore():
    # cerca == sostituisci e' quasi sempre un refuso, e resterebbe muta
    testo = sorgente(RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="identica"):
        applica_toppe("init.hsp", testo, [toppa(sostituisci=RIGA_NAME)])


def test_senza_toppe_il_testo_non_si_tocca():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("init.hsp", testo, [])
    assert quante == 0
    assert nuovo == testo


def test_carica_toppe_legge_il_jsonl(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa(), ensure_ascii=False) + "\n", encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert len(caricate) == 1
    assert caricate[0]["file"] == "init.hsp"


def test_senza_il_file_non_si_rompe_niente(tmp_path):
    assert carica_toppe(tmp_path / "assente.jsonl") == []


def test_ogni_toppa_deve_avere_un_motivo(tmp_path):
    # una toppa senza motivo e' una modifica al sorgente di cui fra sei mesi
    # nessuno sa piu' il perche'
    percorso = tmp_path / "toppe.jsonl"
    voce = toppa()
    del voce["motivo"]
    percorso.write_text(json.dumps(voce, ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="motivo"):
        carica_toppe(percorso)


# --- il file vero, contro il sorgente vero ----------------------------------

def test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato():
    """La prova che conta: ogni toppa trova la sua riga, una volta sola.

    Se upstream cambia una di quelle righe, questo test diventa rosso prima che
    la build produca qualcosa di sbagliato.
    """
    toppe = carica_toppe()
    assert toppe, "toppe.jsonl e' vuoto: se non serve piu', va tolto il file"
    for t in toppe:
        percorso = percorsi.SORGENTE_HSP / t["file"]
        assert percorso.exists(), f"{t['file']} non esiste nel sorgente"
        testo = percorso.read_bytes().decode("cp932")
        nuovo, quante = applica_toppe(t["file"], testo, [t])
        assert quante == 1
        assert nuovo != testo
