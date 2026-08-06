# strumenti/tests/test_funzioni.py
from strumenti.funzioni import (
    MORFOLOGIA_INGLESE, PRONOMI_PER_SITO, funzioni_di_contenuto, morfologia_residua,
)


def test_la_morfologia_inglese_non_e_contenuto():
    espressione = 'name(tc) + " attack" + _s(tc) + " " + itemname(ci)'
    assert funzioni_di_contenuto(espressione) == ["itemname", "name"]


def test_le_due_classi_non_si_sovrappongono():
    assert not (MORFOLOGIA_INGLESE & PRONOMI_PER_SITO)


def test_una_espressione_senza_chiamate_non_ha_contenuto():
    assert funzioni_di_contenuto('" and "') == []


def test_le_varianti_di_morfologia_trovate_nel_sorgente_non_sono_contenuto():
    # _s2/_s3/him2 sono verificate su init.hsp (task-1-report.md): restituiscono
    # sempre stringhe inglesi nude, mai lang(), e compaiono davvero nel corpus
    # (lavoro/controllo-text.jsonl). Se restassero fuori da MORFOLOGIA_INGLESE
    # il difetto che questo task chiude resterebbe aperto per queste voci.
    espressione = 'gdata(GDATA_GUEST) + " guest" + _s2(gdata(GDATA_GUEST))'
    assert funzioni_di_contenuto(espressione) == ["gdata", "gdata"]
    assert funzioni_di_contenuto('"beat " + him2(tc)') == []


# --- he/his/him: pronome per sito di chiamata, non per nome -----------------
#
# Giro di correzione 1: he/his/him NON sono sempre pronomi. Il loro corpo in
# init.hsp e' `if (arg2) { ...lang()... } ... stringhe inglesi nude ...`: con
# due argomenti passano da lang() (contenuto), con uno restano inglese per
# sempre (morfologia). Le due espressioni sotto sono prese cosi' come sono da
# `command.hsp:6667` e `action.hsp:9631` (sorgente in
# C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\), non inventate.

def test_his_con_due_argomenti_e_contenuto():
    # action.hsp:9631 — his(tc, 1) passa da lang(): si localizzera' con
    # init.hsp in Fase 4, va conservata come name() o itemname()
    espressione = 'name(tc) + " changed " + his(tc, 1) + " elemental affinity."'
    assert funzioni_di_contenuto(espressione) == ["his", "name"]


def test_his_con_un_argomento_e_morfologia():
    # command.hsp:6667 — his(tc) non ha un ramo lang() raggiungibile: scrive
    # "his"/"her" in inglese per sempre, anche dentro una frase italiana
    espressione = 'name(tc) + " puffs out " + his(tc) + " chest with pride."'
    assert funzioni_di_contenuto(espressione) == ["name"]
    assert morfologia_residua(espressione) == ["his"]


def test_he_con_due_argomenti_e_contenuto_ma_con_un_argomento_e_morfologia():
    # stessa funzione, stesso nome, due siti diversi nella stessa espressione
    espressione = 'he(tc, 1) + " vs. " + he(tc)'
    assert funzioni_di_contenuto(espressione) == ["he"]
    assert morfologia_residua(espressione) == ["he"]


def test_una_chiamata_annidata_non_conta_come_secondo_argomento():
    # his(cdatan(CDATAN_NAME, tc)) ha UN argomento (una chiamata annidata),
    # non due: la virgola dentro cdatan(...) non e' di his(...). Se contata
    # per errore, un his() sempre morfologia sfuggirebbe come "contenuto".
    espressione = 'his(cdatan(CDATAN_NAME, tc)) + " wallet."'
    assert funzioni_di_contenuto(espressione) == ["cdatan"]
    assert morfologia_residua(espressione) == ["his"]
