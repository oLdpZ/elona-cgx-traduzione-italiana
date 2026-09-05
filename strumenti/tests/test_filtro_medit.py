"""Le prove del filtro oggetti dell'editor di mappe.

⚠️ La prova che conta di piu' e' `test_le_voci_e_le_costanti_stanno_in_fila`:
le due righe si leggono **per posizione**, e una voce in piu' o in meno
sposterebbe tutti i filtri di uno senza che niente si accenda — l'editor
mostrerebbe le pozioni scegliendo «Pergamena», e nessun cancello del progetto
misura quello.
"""
import pytest

from strumenti import percorsi
from strumenti import genera_toppe_filtro_medit as medit
from strumenti.genera_toppe_filtro_medit import (DALL_AUTOPICK, MonteMosso,
                                                 NUOVE, costanti,
                                                 dall_autopick, problemi,
                                                 rese, toppe, voci)


def test_le_voci_e_le_costanti_stanno_in_fila():
    assert len(voci()) == 26
    assert len(costanti()) == 26
    assert voci()[0] == "All items"
    assert costanti()[0] == "FILTER_NOTHING"


def test_ogni_voce_ha_la_sua_parola():
    assert problemi() == []


def test_le_parole_vengono_dall_autopick_e_non_da_qui():
    """⭐ Sono le categorie che il GIOCATORE filtra: se l'editor ne usasse
    altre, il progetto avrebbe due vocabolari per la stessa cosa."""
    lette = dall_autopick()
    assert lette["Helm"] == "Elmo"
    assert lette["Ore"] == "Minerale"
    assert lette["Staff"] == "Bacchetta"   # FILTER_ITEM_ROD, non un bastone
    assert lette["Amulet"] == "Collana"    # l'autopick la chiama `necklace`
    assert set(lette) == set(DALL_AUTOPICK)


def test_una_categoria_sparita_dall_autopick_ferma_tutto(monkeypatch):
    """⭐ La prova al contrario."""
    monkeypatch.setitem(DALL_AUTOPICK, "Helm", "non_esiste")
    with pytest.raises(KeyError):
        dall_autopick()


def test_una_voce_nuova_di_monte_ferma_tutto(monkeypatch):
    monkeypatch.setattr(medit, "NUOVE",
                        {k: v for k, v in NUOVE.items() if k != "Trade"})
    assert any("non ha una parola italiana" in g for g in problemi())


def test_una_riga_di_tabella_che_non_serve_piu_si_accende(monkeypatch):
    monkeypatch.setattr(medit, "NUOVE", dict(NUOVE, Dormiente="Dormiente"))
    assert any("non compare piu'" in g for g in problemi())


def test_una_resa_troppo_lunga_e_un_guaio(monkeypatch):
    monkeypatch.setattr(medit, "NUOVE",
                        dict(NUOVE, Trade="M" * (medit.TETTO + 1)))
    assert any("una tredicina" in g for g in problemi())


def test_un_a_capo_dentro_una_voce_e_un_guaio(monkeypatch):
    """`\\n` separa le voci: una voce che ne porta uno ne diventerebbe due, e
    le costanti scivolerebbero tutte di uno."""
    monkeypatch.setattr(medit, "NUOVE", dict(NUOVE, Trade="Mer\\nce"))
    assert any("ne diventerebbe due" in g for g in problemi())


def test_la_larghezza_viene_dal_sorgente(monkeypatch):
    medit._controlla_geometria()
    monkeypatch.setattr(medit, "RIGA_LARGHEZZA", 2534)
    with pytest.raises(MonteMosso):
        medit._controlla_geometria()


def test_la_toppa_non_cambia_il_numero_di_voci():
    """⚠️ Le due liste si leggono per posizione: il conto e' il vincolo."""
    toppa = toppe()[0]
    prima = medit._LETTERALE.findall(toppa["cerca"])[0].split("\\n")
    dopo = medit._LETTERALE.findall(toppa["sostituisci"])[0].split("\\n")
    assert len(prima) == len(dopo) == 26
    tabella = rese()
    assert dopo == [tabella[v] for v in prima]


def test_nella_build_il_filtro_parla_italiano():
    testo = (percorsi.BUILD_HSP / "map_func.hsp").read_bytes().decode("cp932")
    assert "Cianfrusaglie\\nCommestibile" in testo
    assert "All items\\nFurniture" not in testo


def test_l_editor_di_mappe_non_e_una_schermata_del_gioco():
    """⚠️ Il fatto che regge la decisione di tradurlo con calma: ci si entra
    solo se l'eseguibile si CHIAMA `medit`. Se un domani monte cambiasse quel
    cancello, la stessa riga diventerebbe interfaccia vera."""
    main = (percorsi.SORGENTE_HSP / "main.hsp").read_bytes().decode("cp932")
    assert 'if ( dirinfo(4) == "medit" ) {' in main
