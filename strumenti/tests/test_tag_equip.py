"""Le prove delle 15 sigle del pannello dell'equipaggiamento.

⚠️⚠️ La prova che spiega il modulo e' `test_queste_sigle_sono_un_punto_cieco`:
senza quella, un domani in cui `copertura` o `disegnate` imparassero a vederle
nessuno se ne accorgerebbe, e questo generatore resterebbe per inerzia.

⚠️ E quella che pesa di piu' e' `test_il_tetto_e_un_TAGLIO_non_un_bordo`: una
sigla di cinque caratteri qui non sborda dal pannello — `item_func.hsp:2629`
la **taglia**, e il giocatore legge un troncone senza che niente si accorga di
niente.
"""
import pytest

from strumenti import copertura, disegnate, percorsi, salti
from strumenti import genera_toppe_tag_equip as tag
from strumenti.commenti import righe_in_commento
from strumenti.genera_toppe_tag_equip import (MonteMosso, SIGLE, TETTO,
                                              nomi_italiani, problemi,
                                              sorgente, toppe)
from strumenti.verifica import carica_invariati


def test_sono_quindici_e_la_tabella_le_copre_tutte():
    nel_sorgente = sorgente()
    assert len(nel_sorgente) == 15
    assert set(nel_sorgente) == set(SIGLE)


def test_ogni_abilita_del_pannello_ha_la_sua_sigla():
    assert problemi() == []


def test_le_sigle_si_leggono_tutte_in_quattro_caratteri():
    for costante, (_n, _e, _nome, sigla) in SIGLE.items():
        assert len(sigla) <= TETTO, costante
        assert sigla.isascii(), costante


def test_nessuna_sigla_si_ripete():
    """Nella fila si leggono una accanto all'altra: due uguali sono due che il
    giocatore non puo' distinguere."""
    sigle = [v[3] for v in SIGLE.values()]
    assert len(set(sigle)) == len(sigle)


# --- il tetto --------------------------------------------------------------

def test_il_tetto_e_un_TAGLIO_non_un_bordo():
    """⭐ Non e' geometria e non e' una stima in pixel: `item_func.hsp:2629` fa
    `strmid(locvar_equipinfo_s, 0, 4)`. Una sigla piu' lunga non sborda dal
    pannello: viene tagliata, e il giocatore legge un troncone."""
    righe = tag._righe_file("item_func.hsp")
    assert righe[2628].strip() == \
        "locvar_equipinfo_s = strmid(locvar_equipinfo_s, 0, 4)"
    assert TETTO == 4


def test_quattro_caratteri_lasciano_la_fila_dove_stava():
    """`:2651` fa avanzare la x con `strlen(s) * 8`: sigle lunghe quanto le
    inglesi lasciano la geometria della riga identica a com'era."""
    righe = tag._righe_file("item_func.hsp")
    assert righe[2650].strip() == \
        "locvar_equipinfo_x += strlen(locvar_equipinfo_s) * 8"
    for costante, (_n, inglese, _nome, sigla) in SIGLE.items():
        assert len(sigla) == len(inglese), costante


def test_una_sigla_troppo_lunga_e_un_guaio(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_SHIELD"] = (2618, "Shld", "Scudo", "Scudo")
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("verrebbe TAGLIATA" in g for g in problemi())


def test_una_sigla_non_ASCII_e_un_guaio(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_MAGIC_CAPACITY"] = (2615, "M-Cp", "Capacita' magica",
                                            "C-Mà")
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("non e' ASCII" in g for g in problemi())


def test_due_sigle_uguali_sono_un_guaio(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_CONTROL_MAGIC"] = (2626, "Ct-M", "Controllo magia",
                                           "C-Mg")
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("sta su 2 abilita'" in g for g in problemi())


# --- il rinvio al dizionario ----------------------------------------------

def test_ogni_sigla_abbrevia_un_nome_che_il_dizionario_da_davvero():
    """⭐ Il rinvio e' il punto: la sigla e la lista delle abilita' devono dire
    la stessa parola. Se `Greater Evasion` smettesse di essere «Intuito»,
    `Intu` andrebbe ridecisa e non indovinata."""
    italiani = nomi_italiani()
    assert italiani["SKILL_NORMAL_GREATER_EVASION"] == "Intuito"
    assert italiani["SKILL_NORMAL_TWO_HAND"] == "Due mani"
    for costante, (_n, _e, nome, _s) in SIGLE.items():
        assert italiani[costante] == nome, costante


def test_un_nome_cambiato_nel_dizionario_ferma_tutto(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_GREATER_EVASION"] = (2625, "G-Ev", "Schivata", "Schi")
    monkeypatch.setattr(tag, "SIGLE", finto)
    guai = problemi()
    assert any("era ricavata da 'Schivata'" in g and "'Intuito'" in g
               for g in guai)


def test_un_abilita_nuova_nel_pannello_ferma_tutto(monkeypatch):
    finto = {k: v for k, v in SIGLE.items() if k != "SKILL_NORMAL_MINING"}
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("nessuno gli ha dato una sigla italiana" in g
               for g in problemi())


def test_una_riga_di_tabella_che_non_serve_piu_si_accende(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_FISHING"] = (2627, "Fish", "Pesca", "Pesc")
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("nel pannello non compare piu'" in g for g in problemi())


def test_il_monte_spostato_ferma_tutto(monkeypatch):
    def finto(_nome):
        return ["", "riga cambiata"] * 3000
    monkeypatch.setattr(tag, "_righe_file", finto)
    with pytest.raises(MonteMosso):
        tag._controlla_geometria()


# --- la sigla che coincide -------------------------------------------------

def test_la_sigla_che_coincide_non_genera_una_toppa():
    """`Trap` abbrevia «trappole» con le stesse quattro lettere di `trap`: la
    toppa sarebbe una riga uguale a se stessa."""
    assert len(toppe()) == 14
    assert all("Trap" not in t["sostituisci"] for t in toppe())


def test_la_sigla_che_coincide_sta_in_invariati():
    """⚠️ Senza la riga in `invariati.md` le reti chiederebbero per sempre un
    lavoro gia' deciso: e' il motivo per cui quel file esiste."""
    assert "Trap" in carica_invariati()


def test_una_sigla_coincidente_e_non_dichiarata_si_accende(monkeypatch):
    finto = dict(SIGLE)
    finto["SKILL_NORMAL_SHIELD"] = (2618, "Shld", "Scudo", "Shld")
    monkeypatch.setattr(tag, "SIGLE", finto)
    assert any("deve stare in `invariati.md`" in g for g in problemi())


# --- le toppe e la build ---------------------------------------------------

def test_le_toppe_cambiano_solo_la_sigla():
    """Il resto della riga — la costante, le graffe, il nome della variabile —
    non si tocca: una toppa che cambiasse la condizione cambierebbe il gioco."""
    for toppa in toppe():
        prima, dopo = toppa["cerca"], toppa["sostituisci"]
        assert prima.count('"') == dopo.count('"') == 2
        assert prima.split('"')[0] == dopo.split('"')[0]
        assert prima.split('"')[2] == dopo.split('"')[2]


def test_nella_build_il_pannello_parla_italiano():
    testo = (percorsi.BUILD_HSP / "item_func.hsp").read_bytes().decode("cp932")
    for costante, (_n, inglese, _nome, sigla) in SIGLE.items():
        assert '"%s"' % sigla in testo, (
            "%s non ha la sua sigla italiana" % costante)
        if sigla != inglese:
            assert '"%s"' % inglese not in testo, "e' rimasta %r" % inglese


# --- perche' questo modulo esiste ------------------------------------------

def test_queste_sigle_sono_un_punto_cieco_delle_DUE_reti_vecchie():
    """⚠️⚠️ Sul SORGENTE pinnato, `copertura` non ne vede nessuna — `2Hnd` non
    ha nemmeno una parola alfabetica — e `disegnate` nemmeno: l'assegnazione
    sta dentro un `if` a graffe e la sua `_ASSEGNAZIONE` e' ancorata a inizio
    riga. Le vede solo `salti`."""
    percorso = percorsi.SORGENTE_HSP / "item_func.hsp"
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso)
    sigle = {v[1] for v in SIGLE.values()}

    da_prosa = set(copertura.scoperte_di("item_func.hsp", testo, set(), morte,
                                         set()))
    da_disegnate = {t[2] for t in disegnate.tutte_di("item_func.hsp", testo,
                                                     morte)}
    da_salti = {t[3] for t in salti.scoperte_di("item_func.hsp", testo, morte)}

    assert sigle & da_prosa == set()
    assert sigle & da_disegnate == set()
    assert sigle <= da_salti
