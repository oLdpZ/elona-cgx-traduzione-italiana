import pytest
from strumenti.reimporta import reimporta


def voce(firma, it, **extra):
    base = {
        "firma": firma, "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "はい", "en": "Yes", "tipo": "statica", "contesto": "", "it": it,
    }
    base.update(extra)
    return base


def test_scrive_le_voci_pulite():
    esito = reimporta([voce("a", "Sì")], {})
    assert esito["a"]["it"] == "Sì"


def test_rifiuta_l_intero_lotto_se_una_voce_e_sporca():
    with pytest.raises(ValueError, match="1 voci con problemi"):
        reimporta([voce("a", "Sì"), voce("b", "")], {})


def test_un_lotto_sporco_non_scrive_niente():
    dizionario = {}
    with pytest.raises(ValueError):
        reimporta([voce("a", "Sì"), voce("b", "")], dizionario)
    assert dizionario == {}


def test_sovrascrive_una_voce_gia_presente():
    dizionario = {"a": voce("a", "Si")}
    esito = reimporta([voce("a", "Sì")], dizionario)
    assert esito["a"]["it"] == "Sì"
