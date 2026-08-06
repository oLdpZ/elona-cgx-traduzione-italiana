from strumenti.applica import applica_a_testo
from strumenti.estrai import firma

STATICA = '	txt lang("バックパックが一杯だ。", "Your inventory is full.")'


def dizionario_con(jp, en, it, tipo="statica"):
    chiave = firma(jp, en)
    return {chiave: {
        "firma": chiave, "jp": jp, "jp_grezzo": f'"{jp}"',
        "en": en, "en_grezzo": f'"{en}"',
        "it": it, "tipo": tipo, "occorrenza": 0,
    }}


def test_sostituisce_l_inglese_con_l_italiano():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Il tuo zaino e' pieno.")
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, diz)
    assert sostituzioni == 1
    assert '"Il tuo zaino e\' pieno."' in testo
    assert "Your inventory is full." not in testo


def test_conserva_il_giapponese():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert "バックパックが一杯だ。" in testo


def test_degrada_gli_accenti_in_fase_di_applicazione():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "È già pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert '"E\' gia\' pieno."' in testo
    assert "È" not in testo


def test_lascia_intatte_le_stringhe_non_tradotte():
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, {})
    assert sostituzioni == 0
    assert testo == STATICA


def test_il_risultato_e_codificabile_in_cp932():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Perché è così")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    ritorno = testo.encode("cp932").decode("cp932")
    assert ritorno == testo


def test_conserva_i_fine_riga_crlf():
    sorgente = STATICA + "\r\n" + "	mes \"altro\"" + "\r\n"
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", sorgente, diz)
    assert "\r\n" in testo
    assert "\n" not in testo.replace("\r\n", "")
    assert testo.endswith("\r\n")
