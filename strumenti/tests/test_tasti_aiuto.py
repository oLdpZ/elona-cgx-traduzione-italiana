"""Le prove delle 38 etichette dei tasti nella schermata di aiuto.

⚠️⚠️ Come per la riga di stato dell'editor di mazzo, la prova che spiega il
modulo e' `test_queste_etichette_sono_un_punto_cieco_delle_due_reti`: senza
quella, un domani in cui una delle due reti imparasse a vederle nessuno se ne
accorgerebbe, e questo generatore resterebbe per inerzia.
"""
import pytest

from strumenti import accenti, copertura, disegnate, percorsi
from strumenti import genera_toppe_tasti_aiuto as tasti
from strumenti.commenti import righe_in_commento
from strumenti.genera_toppe_tasti_aiuto import (DAL_DIZIONARIO, MonteMosso,
                                                NUOVE, comandi_sorgente,
                                                dal_dizionario, problemi,
                                                rese, toppe)


def test_sono_trentotto_su_sette_righe():
    comandi = comandi_sorgente()
    assert len(comandi) == 38
    assert len({n for n, _p, _c in comandi}) == 7


def test_ogni_comando_della_schermata_ha_la_sua_parola():
    assert problemi() == []


def test_le_parole_della_barra_si_leggono_e_non_si_riscrivono():
    """⭐ Il rinvio e' il punto: se la schermata di aiuto chiamasse un comando
    con una parola e la barra con un'altra, il giocatore imparerebbe il nome
    sbagliato."""
    lette = dal_dizionario()
    assert lette["get"] == "Raccogli"
    assert lette["Wide apply"] == "Ab. ampia"
    assert lette["apply"] == accenti.degrada("Abilità")
    assert set(lette) == set(DAL_DIZIONARIO)


def test_una_voce_sparita_dalla_barra_ferma_tutto(monkeypatch):
    """⭐ La prova al contrario: se il dizionario smettesse di rendere la voce
    a cui il rinvio punta, la parola va ridecisa, non indovinata."""
    monkeypatch.setitem(DAL_DIZIONARIO, "get", "Non Esiste")
    with pytest.raises(KeyError):
        dal_dizionario()


def test_un_comando_nuovo_di_monte_ferma_tutto(monkeypatch):
    senza = {k: v for k, v in NUOVE.items() if k != "quaff"}
    monkeypatch.setattr(tasti, "NUOVE", senza)
    assert any("nessuno gli ha dato una parola italiana" in g
               for g in problemi())


def test_una_riga_di_tabella_che_non_serve_piu_si_accende(monkeypatch):
    monkeypatch.setattr(tasti, "NUOVE", dict(NUOVE, dormiente="Dormiente"))
    assert any("non compare piu'" in g for g in problemi())


def test_una_parola_con_due_sorgenti_ferma_tutto(monkeypatch):
    monkeypatch.setattr(tasti, "NUOVE", dict(NUOVE, get="Prendi"))
    assert any("due sorgenti" in g for g in problemi())


# --- le misure -------------------------------------------------------------

def test_l_accento_si_degrada_da_se():
    """⚠️ Queste sono toppe: scrivono nel CP932, dove la vocale accentata non
    esiste. Il generatore degrada, cosi' la tabella puo' portare l'italiano
    giusto e la build la forma che si puo' scrivere."""
    assert rese()["apply"] == "Abilita'"


def test_un_carattere_che_CP932_non_sa_scrivere_e_un_guaio(monkeypatch):
    """`degrada` conosce le vocali accentate e basta: tutto il resto — un
    trattino lungo, una virgoletta a caporale — passerebbe."""
    monkeypatch.setattr(tasti, "NUOVE", dict(NUOVE, quaff="Bevi—"))
    assert any("non e' ASCII" in g for g in problemi())


def test_una_resa_troppo_lunga_e_un_guaio(monkeypatch):
    monkeypatch.setattr(tasti, "NUOVE",
                        dict(NUOVE, quaff="B" * (tasti.TETTO + 1)))
    assert any("il tetto e'" in g for g in problemi())


def test_una_parentesi_nella_resa_e_un_guaio(monkeypatch):
    """`*convertHelp` taglia sulla PRIMA parentesi: una in piu' gli farebbe
    tagliare il pezzo sbagliato."""
    monkeypatch.setattr(tasti, "NUOVE", dict(NUOVE, quaff="Bevi (pozione)"))
    assert any("PRIMA parentesi" in g or "prima parentesi" in g.lower()
               for g in problemi())


def test_la_geometria_viene_dal_sorgente(monkeypatch):
    tasti._controlla_geometria()
    monkeypatch.setattr(tasti, "GEOMETRIA",
                        [("help.hsp", 393, "pos x + 999", "dove parte")])
    with pytest.raises(MonteMosso):
        tasti._controlla_geometria()


def test_il_blocco_spostato_ferma_tutto(monkeypatch):
    monkeypatch.setattr(tasti, "RIGHE", (380,))
    with pytest.raises(MonteMosso):
        comandi_sorgente()


# --- le toppe --------------------------------------------------------------

def test_le_toppe_cambiano_solo_quel_che_sta_fra_le_parentesi():
    """Il giapponese davanti resta: e' quel che legge chi gioca in giapponese,
    ed e' l'altra meta' di ogni riga."""
    for toppa in toppe():
        prima = toppa["cerca"]
        dopo = toppa["sostituisci"]
        assert prima.count('"') == dopo.count('"')
        for pezzo_a, pezzo_b in zip(prima.split('"'), dopo.split('"')):
            if "(" in pezzo_a:
                assert pezzo_a.split("(")[0] == pezzo_b.split("(")[0]
            else:
                assert pezzo_a == pezzo_b


def test_nella_build_la_schermata_di_aiuto_parla_italiano():
    testo = (percorsi.BUILD_HSP / "help.hsp").read_bytes().decode("cp932")
    tabella = rese()
    for _numero, _pezzo, comando in comandi_sorgente():
        assert "(%s)" % tabella[comando] in testo, (
            "il tasto %r non ha la sua etichetta italiana" % comando)
    for comando in ("get", "quaff", "hi jump"):
        assert "(%s)" % comando not in testo, "e' rimasto %r" % comando


# --- perche' questo modulo esiste ------------------------------------------

def test_queste_etichette_sono_un_punto_cieco_delle_due_reti():
    """⚠️⚠️ Sul SORGENTE pinnato — senza le toppe — `copertura` ne vede una
    sola su 38 e `disegnate` nessuna."""
    percorso = percorsi.SORGENTE_HSP / "help.hsp"
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso)
    numeri = {n for n, _p, _c in comandi_sorgente()}

    scoperte = set(copertura.scoperte_di("help.hsp", testo, set(), morte,
                                         set()))
    # ⚠️ Si cerca «(comando)» con le parentesi, non il comando nudo: «apply»
    #    e «help» sono SOTTOSTRINGHE di «Wide apply» e di «help index not
    #    found», e un `in` nudo direbbe che la rete li vede.
    viste = {c for _n, _p, c in comandi_sorgente()
             if any("(%s)" % c in s for s in scoperte)}
    assert viste == {"Wide apply"}

    disegnate_qui = [t for t in disegnate.disegnate_di("help.hsp", testo)
                     if t[0] in numeri]
    assert disegnate_qui == []
