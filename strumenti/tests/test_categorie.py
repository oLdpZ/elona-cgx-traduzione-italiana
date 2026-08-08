# strumenti/tests/test_categorie.py
import pytest

from strumenti import percorsi
from strumenti.categorie import FILE, categorie, categorie_da_testo

BLOCCO = """\
	if ( dbid == ITEM_ID_HAMBURGER ) {
		if ( dbmode == DBMODE_SET ) {
			inv(INV_ITEM_PIC, ci) = xy2pic(22, 29)
			reftype = FILTER_ITEM_FOOD
			return
		}
	}
"""


def test_legge_la_categoria_dal_blocco():
    assert categorie_da_testo(BLOCCO) == {"ITEM_ID_HAMBURGER": "FILTER_ITEM_FOOD"}


def test_dentro_un_blocco_vince_la_prima_assegnazione():
    # un oggetto assegna reftype una volta per dbmode: SET, REF, REF_SPEC. Sono
    # uguali, ma se un giorno divergessero il test dice quale si e' scelta
    testo = BLOCCO + """\
	if ( dbid == ITEM_ID_TABLE ) {
		reftype = FILTER_FURNITURE
		reftype = FILTER_JUNK
	}
"""
    assert categorie_da_testo(testo)["ITEM_ID_TABLE"] == "FILTER_FURNITURE"


def test_un_oggetto_senza_reftype_non_compare():
    # assente e' meglio di classificato per sbaglio: chi lo chiede se ne
    # accorge, invece di ereditare la categoria del blocco precedente
    testo = """\
	if ( dbid == ITEM_ID_SENZA ) {
		inv(INV_ITEM_VALUE, ci) = 10
	}
	if ( dbid == ITEM_ID_TABLE ) {
		reftype = FILTER_FURNITURE
	}
"""
    mappa = categorie_da_testo(testo)
    assert "ITEM_ID_SENZA" not in mappa
    assert mappa["ITEM_ID_TABLE"] == "FILTER_FURNITURE"


def test_un_reftype_fuori_da_ogni_blocco_e_ignorato():
    assert categorie_da_testo("\treftype = FILTER_ITEM_FOOD\n") == {}


def test_il_sorgente_vero_classifica_i_nomi_che_restano():
    # la rete sul file vero: il classificatore serve a scegliere i lotti, e se
    # una parte dei nomi restasse senza categoria il criterio tornerebbe a
    # essere il mio occhio senza che nessuno lo dica
    if not (percorsi.SORGENTE_HSP / FILE).exists():
        pytest.skip("sorgente non disponibile")

    from strumenti.estrai import (
        carica_rinviate, da_tradurre, estrai_da_file, firme_tradotte,
    )

    mappa = categorie()
    resta = da_tradurre(
        estrai_da_file(percorsi.SORGENTE_HSP / FILE),
        firme_tradotte(FILE),
        carica_rinviate(None, FILE),
    )
    senza = [v["en"] for v in resta if v.get("oggetto") not in mappa]
    assert senza == []
