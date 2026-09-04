"""Le prove della riga di stato dell'editor di mazzo.

⚠️⚠️ Questo modulo esiste per una cosa che le due reti del progetto non
vedevano: `copertura._PROSA` ne contava 5 su 13 e `disegnate.py` nessuna,
perche' il valore si monta con tredici `+=` e si disegna quindici righe piu'
giu'. La prova che conta di piu' e' percio'
`test_questa_riga_e_un_punto_cieco_delle_due_reti`: se un domani una delle due
imparasse a vederla, questo modulo diventerebbe superfluo, e senza quella prova
nessuno lo saprebbe.
"""
import pytest

from strumenti import copertura, disegnate, percorsi
from strumenti import genera_toppe_riga_stato as stato
from strumenti.commenti import righe_in_commento
from strumenti.genera_toppe_riga_stato import (MonteMosso, RESE,
                                               coppia_peggiore, problemi,
                                               righe_sorgente, toppe)


def test_sono_tredici_e_montano_tutte_la_stessa_variabile():
    righe = righe_sorgente()
    assert len(righe) == 13
    assert all("s@tcg +=" in r for _n, r in righe)


def test_ogni_letterale_con_lettere_ha_una_resa():
    assert problemi() == []


def test_una_parola_nuova_di_monte_ferma_tutto(monkeypatch):
    """⭐ La prova al contrario: se il monte aggiungesse un modo di ordinare,
    la sua etichetta resterebbe inglese e nessun altro cancello lo direbbe."""
    senza = {k: v for k, v in RESE.items() if k != "Sort by: Hp   "}
    monkeypatch.setattr(stato, "RESE", senza)
    guai = problemi()
    assert any("la tabella non lo ha" in g for g in guai)


def test_la_spaziatura_in_coda_non_si_tocca(monkeypatch):
    """Le tre spaziature separano l'ordinamento dal filtro: senza, la riga
    direbbe «Ordina per: CostoFiltro: Dominio»."""
    monkeypatch.setattr(stato, "RESE",
                        dict(RESE, **{"Sort by: Hp   ": "Ordina per: Vita"}))
    assert any("spaziatura in coda" in g for g in problemi())


# --- il tetto --------------------------------------------------------------

def test_il_tetto_si_misura_sulla_coppia_non_sulla_singola():
    """⚠️ La riga porta sempre un ordinamento E un filtro, concatenati."""
    ordine, filtro, misura = coppia_peggiore(RESE)
    assert misura == len(ordine) + len(filtro)
    assert misura <= stato.TETTO
    # e la coppia peggiore non e' la piu' lunga delle due da sola
    assert misura > max(len(ordine), len(filtro))


def test_la_razza_conta_col_numero_che_le_finisce_in_coda():
    """`"Filter: Race" + (filtertype@tcg - 4) + "   "`: la cifra e le tre
    spaziature arrivano dopo, e il tetto le deve vedere."""
    _o, filtro, _m = coppia_peggiore(
        {"Sort by: Hp   ": "Ordina   ",
         "Filter: Race": "Filtro: Razza"})
    assert filtro == "Filtro: RazzaN   "


def test_una_resa_troppo_lunga_e_un_guaio(monkeypatch):
    lunga = "F" * stato.TETTO + "   "
    monkeypatch.setattr(stato, "RESE",
                        dict(RESE, **{"Filter: Class1   ": lunga}))
    assert any("uscirebbe dal pannello" in g for g in problemi())


def test_la_geometria_viene_dal_sorgente_e_non_da_un_numero_a_mano(monkeypatch):
    """Il tetto e' un quoziente di tre numeri che stanno nel sorgente: se uno
    dei tre si muove, il cancello si accende invece di lasciar valere una
    misura che non vale piu'."""
    stato._controlla_geometria()
    monkeypatch.setattr(stato, "GEOMETRIA",
                        [("tcg_mod.hsp", 3490, "basew@tcg = 12345",
                          "la larghezza del pannello")])
    with pytest.raises(MonteMosso):
        stato._controlla_geometria()


def test_il_blocco_spostato_ferma_tutto(monkeypatch):
    """Se il monte sposta le tredici righe, i numeri qui non valgono piu'."""
    monkeypatch.setattr(stato, "PRIMA_RIGA", 3340)
    with pytest.raises(MonteMosso):
        righe_sorgente()


# --- le toppe --------------------------------------------------------------

def test_le_toppe_cambiano_solo_i_letterali():
    """Fuori dalle virgolette la riga resta identica: qui non si tocca la
    condizione, si traduce l'etichetta."""
    for toppa in toppe():
        assert (stato._LETTERALE.sub('""', toppa["cerca"])
                == stato._LETTERALE.sub('""', toppa["sostituisci"]))


def test_nella_build_la_riga_di_stato_parla_italiano():
    testo = (percorsi.BUILD_HSP / "tcg.hsp").read_bytes().decode("cp932")
    for inglese, italiano in RESE.items():
        assert '"%s"' % italiano in testo, "manca %r" % italiano
        assert '"%s"' % inglese not in testo, "e' rimasto %r" % inglese


# --- perche' questo modulo esiste ------------------------------------------

def test_questa_riga_e_un_punto_cieco_delle_due_reti():
    """⚠️⚠️ La prova che spiega il modulo. Sul SORGENTE pinnato — senza le
    toppe — `copertura` ne vede 5 su 13 e `disegnate` nessuna. Se un domani
    una delle due imparasse a vederle tutte, questa prova si accende e questo
    generatore va ripensato invece di restare per inerzia."""
    percorso = percorsi.SORGENTE_HSP / "tcg.hsp"
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso)
    numeri = {n for n, _r in righe_sorgente()}

    viste_da_copertura = {
        e for e in RESE
        if any(e in s for s in copertura.scoperte_di("tcg.hsp", testo, set(),
                                                     morte, set()))
    }
    assert 0 < len(viste_da_copertura) < len(RESE)

    viste_da_disegnate = [t for t in disegnate.disegnate_di("tcg.hsp", testo)
                          if t[0] in numeri]
    assert viste_da_disegnate == []
