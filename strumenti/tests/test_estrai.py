# strumenti/tests/test_estrai.py
from strumenti.estrai import (
    _argomenti, _letterali, avvii, e_dinamica, estrai_da_testo, firma,
    normalizza_espressione, siti, spezza_righe,
)

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


# --- escape \" nei letterali (revisione finale, rilievo CRITICAL 1) -----------
# Nel sorgente HSP \" e' una virgoletta dentro un letterale. Il parser che
# faceva toggle su ogni virgoletta scartava 11 lang(), sbagliava 5 span e
# mutilava 295 voci. La riga qui sotto e' db_creature.hsp:50728, ridotta.

RIGA_CON_ESCAPE = (
    '\t\t\ttxt lang("「なに？", "\\"Oh, my ") + _onii(cdata(CDATA_SEX, CHARA_PLAYER))'
    ' + lang("さんも味わいたいの？」", " want to taste it too?\\"")'
)


def test_l_escape_non_chiude_il_letterale():
    voci = estrai_da_testo("db_creature.hsp", RIGA_CON_ESCAPE)
    assert [v["en"] for v in voci] == ['\\"Oh, my ', ' want to taste it too?\\"']


def test_lo_span_non_inghiotte_il_codice_fra_due_lang():
    # il difetto grave: lo span del secondo argomento arrivava fino alla
    # virgoletta successiva, e applica.py sostituendolo faceva sparire dal
    # sorgente sia _onii(...) sia l'intera coppia lang() seguente.
    elenco = list(siti(RIGA_CON_ESCAPE))
    assert len(elenco) == 2
    _, _, _, _, _, _, grezzo_en, inizio, fine = elenco[0]
    assert RIGA_CON_ESCAPE[inizio:fine] == grezzo_en
    assert "_onii" not in grezzo_en
    assert "lang(" not in grezzo_en


def test_un_lang_dentro_un_letterale_non_e_un_sito():
    # 'lang(' che compare dentro una stringa e' testo, non codice
    riga = 'txt lang("説明: lang(a, b) と書く", "write lang(a, b) here")'
    assert len(avvii(riga)) == 1
    voci = estrai_da_testo("text.hsp", riga)
    assert len(voci) == 1
    assert voci[0]["en"] == "write lang(a, b) here"


def test_letterali_onora_gli_escape():
    assert _letterali('"say \\"hi\\" now"') == 'say \\"hi\\" now'
    assert _letterali('"a" + f() + "b"') == "ab"
    # il backslash raddoppiato non si mangia la virgoletta di chiusura
    assert _letterali('"finisce con \\\\" + x') == "finisce con \\\\"


def test_argomenti_non_si_ferma_su_una_parentesi_dentro_un_letterale():
    riga = 'lang("jp)", "en)")'
    assert _argomenti(riga, 4) == ('"jp)"', '"en)"', 12, 17)
    assert riga[12:17] == '"en)"'


# --- il + va cercato fuori dai letterali (rilievo CRITICAL 2) ----------------

def test_un_piu_dentro_il_testo_non_rende_dinamica_la_stringa():
    # 163 stringhe reali contengono un + nel testo. Classificarle dinamiche
    # fa finire l'italiano nudo, senza virgolette, nel sorgente HSP.
    assert e_dinamica('"Enchantment Bonus + 4"') is False
    assert e_dinamica('"RES+ magic"') is False
    voce = estrai_da_testo("trait.hsp", 'txt lang("jp", "Enchantment Bonus + 4")')[0]
    assert voce["tipo"] == "statica"


def test_un_piu_di_concatenazione_resta_dinamico():
    assert e_dinamica('"Bonus + " + str(n)') is True
    assert e_dinamica('name(tc) + " guarded " + name(x) + "."') is True


# --- fine riga: split() sul terminatore, mai splitlines() -------------------

def test_le_righe_si_spezzano_solo_sul_terminatore_effettivo():
    # \x0c e U+2028 sono fine riga per splitlines() ma non per il file:
    # spezzarli sfalserebbe i numeri di riga rispetto al sorgente reale.
    testo = 'a = lang("jp", "en1")\x0c ancora\r\nb = lang("jp2", "en2")\r\n'
    righe, fine_riga, coda = spezza_righe(testo)
    assert fine_riga == "\r\n"
    assert coda is True
    assert len(righe) == 2
    assert [v["riga"] for v in estrai_da_testo("text.hsp", testo)] == [1, 2]


# --- la firma: cosa vi entra e cosa no (SPEC 3.2) ----------------------------

QUI = 'name(gdata(GDATA_RIDER)) + " glare"'
ALTROVE = 'cdatan(CDATAN_NAME, ttc) + " glare"'


def test_senza_espressione_la_firma_e_quella_dei_soli_letterali():
    # e' il caso delle statiche: l'involucro non entra nella chiave
    assert firma("jp", "en") == firma("jp", "en", None)


def test_l_espressione_cambia_la_firma():
    assert firma("jp", " glare", QUI) != firma("jp", " glare")


def test_due_espressioni_diverse_con_gli_stessi_letterali_hanno_firme_diverse():
    # erano 77 firme collidenti: la traduzione dell'una finiva sull'altra
    # portandosi le variabili sbagliate
    assert firma("jp", " glare", QUI) != firma("jp", " glare", ALTROVE)


def test_gli_spazi_non_contano_nella_firma():
    # reindentare a monte non deve mandare la stringa in coda di ritraduzione
    assert firma("jp", " glare", QUI) == firma("jp", " glare", QUI.replace(" + ", "\t+  "))


def test_normalizza_riduce_ogni_sequenza_di_spazi_a_uno():
    assert normalizza_espressione('  a  +\t\t"b"  ') == 'a + "b"'


def test_una_dinamica_del_sorgente_porta_l_espressione_nella_chiave():
    voce = estrai_da_testo("proc.hsp", DINAMICA)[0]
    assert voce["tipo"] == "dinamica"
    assert voce["firma"] == firma(voce["jp"], voce["en"], voce["en_grezzo"])
    assert voce["firma"] != firma(voce["jp"], voce["en"])


def test_una_statica_del_sorgente_non_la_porta():
    voce = estrai_da_testo("text.hsp", STATICA)[0]
    assert voce["tipo"] == "statica"
    assert voce["firma"] == firma(voce["jp"], voce["en"])
