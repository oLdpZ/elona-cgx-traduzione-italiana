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


def test_la_dinamica_non_viene_messa_fra_virgolette():
    # per le dinamiche l'italiano e' gia' un'espressione HSP completa: se viene
    # avvolta fra virgolette come una statica, il codice HSP finisce a schermo.
    sorgente = (
        '	txt lang(name(tc) + "を守った。" + name(x) + "。", '
        'name(tc) + " guarded " + name(x) + ".")'
    )
    espressione = 'name(tc) + " ha protetto " + name(x) + "."'
    diz = dizionario_con("を守った。。", " guarded .", espressione, tipo="dinamica")
    testo, sostituzioni = applica_a_testo("text.hsp", sorgente, diz)
    assert sostituzioni == 1
    assert espressione in testo
    assert '"' + espressione + '"' not in testo


def test_due_lang_sulla_stessa_riga_con_lunghezze_diverse():
    # due lang() sulla stessa riga, con traduzioni di lunghezza diversa
    # dall'inglese originale (una piu' lunga, una piu' corta): verifica che
    # le posizioni di sostituzione non si sfalsino tra la prima e la seconda.
    sorgente = '	txt lang("jp1", "en1") + "  " + lang("jp2", "en2")'
    diz = {}
    diz.update(dizionario_con("jp1", "en1", "Una traduzione molto piu' lunga dell'originale"))
    diz.update(dizionario_con("jp2", "en2", "corta"))
    testo, sostituzioni = applica_a_testo("text.hsp", sorgente, diz)
    assert sostituzioni == 2
    atteso = (
        '	txt lang("jp1", "Una traduzione molto piu\' lunga dell\'originale") + "  " '
        '+ lang("jp2", "corta")'
    )
    assert testo == atteso
