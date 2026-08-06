# strumenti/tests/test_funzioni.py
from strumenti.funzioni import MORFOLOGIA_INGLESE, PRONOMI, funzioni_di_contenuto


def test_la_morfologia_inglese_non_e_contenuto():
    espressione = 'name(tc) + " attack" + _s(tc) + " " + itemname(ci)'
    assert funzioni_di_contenuto(espressione) == ["itemname", "name"]


def test_i_pronomi_non_sono_contenuto():
    # he() passa da lang(), quindi si localizzera' con init.hsp: che l'italiano
    # lo tenga o lo tolga sono due scelte entrambe valide, e la verifica non
    # deve imporne nessuna
    assert funzioni_di_contenuto('cnven(he(tc, 1)) + " is here."') == ["cnven"]


def test_le_due_classi_non_si_sovrappongono():
    assert not (MORFOLOGIA_INGLESE & PRONOMI)


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
