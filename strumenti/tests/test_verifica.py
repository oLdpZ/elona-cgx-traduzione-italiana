# strumenti/tests/test_verifica.py
from strumenti.verifica import controlla_voce, controlla_lotto


def voce(**sovrascritture):
    base = {
        "firma": "abc", "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "バックパックが一杯だ。", "jp_grezzo": '"バックパックが一杯だ。"',
        "en": "Your inventory is full.", "en_grezzo": '"Your inventory is full."',
        "tipo": "statica", "contesto": "", "it": "Il tuo zaino e' pieno.",
    }
    base.update(sovrascritture)
    return base


def test_una_voce_valida_non_ha_problemi():
    assert controlla_voce(voce(it="Il tuo zaino è pieno.")) == []


def test_blocca_la_traduzione_vuota():
    problemi = controlla_voce(voce(it=""))
    assert any("vuota" in p for p in problemi)


def test_blocca_la_traduzione_identica_all_inglese():
    problemi = controlla_voce(voce(it="Your inventory is full."))
    assert any("identica" in p for p in problemi)


def test_blocca_l_apostrofo_scritto_a_mano():
    problemi = controlla_voce(voce(it="Il tuo zaino e' pieno."))
    assert any("apostrofo" in p for p in problemi)


def test_blocca_i_caratteri_che_cp932_cancellerebbe():
    problemi = controlla_voce(voce(it="Zaino pieno — davvero"))  # trattino lungo
    assert any("cp932" in p.lower() for p in problemi)


def test_le_dinamiche_devono_conservare_le_stesse_chiamate():
    pulita = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='name(tc) + " ha protetto " + name(x) + "."',
    )
    assert controlla_voce(pulita) == []

    rotta = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='"ha protetto"',
    )
    problemi = controlla_voce(rotta)
    assert any("interpolazion" in p for p in problemi)


def test_controlla_lotto_indicizza_per_firma():
    esito = controlla_lotto([voce(firma="uno", it=""), voce(firma="due", it="Zaino pieno.")])
    assert "uno" in esito
    assert "due" not in esito
