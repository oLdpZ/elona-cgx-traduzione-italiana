# strumenti/tests/test_estrai.py
from strumenti.estrai import estrai_da_testo, firma, e_dinamica

STATICA = '#define global txt_invfull txt lang("バックパックが一杯だ。", "Your inventory is full.")'
DINAMICA = '#define global txt_guard txt lang(name(tc) + "は" + name(x) + "をかばった！", name(tc) + " guarded " + name(x) + ".")'
DUE_SULLA_STESSA_RIGA = 'a = lang("はい", "Yes"), lang("いいえ", "No")'


def test_estrae_una_statica():
    voci = estrai_da_testo("text.hsp", STATICA)
    assert len(voci) == 1
    voce = voci[0]
    assert voce["jp"] == "バックパックが一杯だ。"
    assert voce["en"] == "Your inventory is full."
    assert voce["tipo"] == "statica"
    assert voce["it"] == ""
    assert voce["file"] == "text.hsp"
    assert voce["riga"] == 1


def test_riconosce_una_dinamica_e_ne_conserva_il_contesto():
    voci = estrai_da_testo("text.hsp", DINAMICA)
    assert len(voci) == 1
    assert voci[0]["tipo"] == "dinamica"
    assert voci[0]["contesto"] == DINAMICA


def test_conserva_l_espressione_grezza():
    # per le dinamiche si traduce l'espressione intera, non i soli letterali:
    # in italiano l'ordine dei pezzi cambia
    voce = estrai_da_testo("text.hsp", DINAMICA)[0]
    assert voce["en_grezzo"] == 'name(tc) + " guarded " + name(x) + "."'
    assert voce["en"] == " guarded ."

    statica = estrai_da_testo("text.hsp", STATICA)[0]
    assert statica["en_grezzo"] == '"Your inventory is full."'
    assert statica["en"] == "Your inventory is full."


def test_le_statiche_non_portano_contesto():
    assert estrai_da_testo("text.hsp", STATICA)[0]["contesto"] == ""


def test_estrae_piu_occorrenze_dalla_stessa_riga():
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    assert [v["en"] for v in voci] == ["Yes", "No"]


def test_le_firme_sono_stabili_e_distinte():
    assert firma("はい", "Yes") == firma("はい", "Yes")
    assert firma("はい", "Yes") != firma("はい", "No")
    assert firma("いいえ", "Yes") != firma("はい", "Yes")


def test_i_duplicati_esatti_si_distinguono_per_occorrenza():
    testo = 'a = lang("はい", "Yes")\nb = lang("はい", "Yes")'
    voci = estrai_da_testo("text.hsp", testo)
    assert len(voci) == 2
    assert voci[0]["occorrenza"] == 0
    assert voci[1]["occorrenza"] == 1
    assert voci[0]["firma"] == voci[1]["firma"]


def test_e_dinamica_distingue_concatenazioni():
    assert e_dinamica('"Your inventory is full."') is False
    assert e_dinamica('name(tc) + " guarded " + name(x) + "."') is True
    assert e_dinamica('"You create " + itemname(ci, 1) + "!"') is True


def test_ignora_le_righe_senza_lang():
    assert estrai_da_testo("text.hsp", "	sdim bodyn, 4, 15") == []


def test_ignora_le_stringhe_con_inglese_vuoto():
    # particelle giapponesi che in inglese non esistono: niente da tradurre.
    # In text.hsp sono 6 casi reali, es. lang("層", "")
    assert estrai_da_testo("text.hsp", 'buff += lang("残り", "")') == []
