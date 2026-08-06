import pytest
from strumenti.accenti import degrada, ha_apostrofo_scritto_a_mano, non_ascii_residuo


@pytest.mark.parametrize("dentro,fuori", [
    ("perché", "perche'"),
    ("città", "citta'"),
    ("più", "piu'"),
    ("così", "cosi'"),
    ("però", "pero'"),
    ("È vero", "E' vero"),
    ("Perù", "Peru'"),
    ("nessun accento", "nessun accento"),
    ("", ""),
])
def test_degrada_le_vocali_accentate(dentro, fuori):
    assert degrada(dentro) == fuori


def test_degrada_non_tocca_il_giapponese():
    giapponese = "バックパックが一杯だ。"
    assert degrada(giapponese) == giapponese


def test_degrada_e_idempotente():
    una_volta = degrada("perché è così")
    assert degrada(una_volta) == una_volta


def test_rileva_apostrofo_scritto_a_mano():
    assert ha_apostrofo_scritto_a_mano("perche' e' cosi'") is True
    assert ha_apostrofo_scritto_a_mano("citta'") is True
    assert ha_apostrofo_scritto_a_mano("perché è così") is False


def test_apostrofo_legittimo_non_e_un_falso_positivo():
    # elisione italiana: l'oggetto, un'arma, dell'acqua
    assert ha_apostrofo_scritto_a_mano("l'oggetto") is False
    assert ha_apostrofo_scritto_a_mano("un'arma magica") is False
    assert ha_apostrofo_scritto_a_mano("dell'acqua") is False
    # troncamento: "po'" e' vocale + apostrofo, ma e' italiano corretto
    assert ha_apostrofo_scritto_a_mano("un po' di acqua") is False
    assert ha_apostrofo_scritto_a_mano("Aspetta un po'") is False


def test_non_ascii_residuo_elenca_cio_che_cp932_cancellerebbe():
    assert non_ascii_residuo("perche' tutto ok") == []
    assert non_ascii_residuo("perché") == ["é"]
    # il giapponese preesistente non e' un residuo: CP932 lo rappresenta
    assert non_ascii_residuo("バックパック") == []
