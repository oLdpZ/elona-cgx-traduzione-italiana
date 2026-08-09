# strumenti/tests/test_toppe.py
"""Le toppe: le sostituzioni fuori da `lang()`, che il dizionario non raggiunge."""
import json

import pytest

from strumenti import percorsi
from strumenti.applica import (SorgenteCorrotto, applica_toppe, carica_toppe,
                               righe_di_toppa)

RIGA_NAME = '\t\treturn "the " + cdatan(CDATAN_NAME, name_arg1)'


def toppa(**sovrascritture):
    base = {
        "file": "init.hsp",
        "cerca": RIGA_NAME,
        "sostituisci": '\t\treturn cdatan(CDATAN_NAME, name_arg1)',
        "motivo": "prova",
    }
    base.update(sovrascritture)
    return base


def sorgente(*righe):
    return "\r\n".join(righe) + "\r\n"


def test_una_toppa_sostituisce_la_riga_esatta():
    testo = sorgente("#defcfunc name int name_arg1", RIGA_NAME, "\treturn 0")
    nuovo, quante = applica_toppe("init.hsp", testo, [toppa()])
    assert quante == 1
    assert '"the "' not in nuovo
    assert "return cdatan(CDATAN_NAME, name_arg1)" in nuovo
    # il resto del file non si tocca, terminatori compresi
    assert nuovo.startswith("#defcfunc name int name_arg1\r\n")
    assert nuovo.endswith("\treturn 0\r\n")


def test_una_toppa_per_un_altro_file_non_si_applica():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("text.hsp", testo, [toppa()])
    assert quante == 0
    assert nuovo == testo


def test_una_riga_che_non_c_e_piu_ferma_la_catena():
    # e' il caso del riallineamento a una nuova versione CGX (SPEC 3.1): se
    # upstream ha riscritto quella riga, applicare la toppa alla cieca non ha
    # senso. Meglio fermarsi e rifarla che produrre un eseguibile diverso da
    # quello che si crede.
    testo = sorgente("#defcfunc name int name_arg1", "\treturn 0")
    with pytest.raises(SorgenteCorrotto, match="non esiste"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_riga_ambigua_ferma_la_catena():
    # due righe identiche: quale delle due? Indovinare significa avere una
    # probabilita' su due di toppare quella sbagliata, in silenzio.
    testo = sorgente(RIGA_NAME, "\tx = 1", RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="due volte|2 volte|piu' di una"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_toppa_che_non_cambia_niente_e_un_errore():
    # cerca == sostituisci e' quasi sempre un refuso, e resterebbe muta
    testo = sorgente(RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="identica"):
        applica_toppe("init.hsp", testo, [toppa(sostituisci=RIGA_NAME)])


def test_senza_toppe_il_testo_non_si_tocca():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("init.hsp", testo, [])
    assert quante == 0
    assert nuovo == testo


def test_carica_toppe_legge_il_jsonl(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa(), ensure_ascii=False) + "\n", encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert len(caricate) == 1
    assert caricate[0]["file"] == "init.hsp"


def test_senza_il_file_non_si_rompe_niente(tmp_path):
    assert carica_toppe(tmp_path / "assente.jsonl") == []


def test_ogni_toppa_deve_avere_un_motivo(tmp_path):
    # una toppa senza motivo e' una modifica al sorgente di cui fra sei mesi
    # nessuno sa piu' il perche'
    percorso = tmp_path / "toppe.jsonl"
    voce = toppa()
    del voce["motivo"]
    percorso.write_text(json.dumps(voce, ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="motivo"):
        carica_toppe(percorso)


# --- il file vero, contro il sorgente vero ----------------------------------

def test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato():
    """La prova che conta: ogni toppa trova la sua riga, una volta sola.

    Se upstream cambia una di quelle righe, questo test diventa rosso prima che
    la build produca qualcosa di sbagliato.
    """
    toppe = carica_toppe()
    assert toppe, "toppe.jsonl e' vuoto: se non serve piu', va tolto il file"
    for t in toppe:
        percorso = percorsi.SORGENTE_HSP / t["file"]
        assert percorso.exists(), f"{t['file']} non esiste nel sorgente"
        testo = percorso.read_bytes().decode("cp932")
        nuovo, quante = applica_toppe(t["file"], testo, [t])
        assert quante == 1
        assert nuovo != testo


def test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere():
    """Ogni toppa deve poter essere scritta nell'albero di build.

    Le toppe sono l'unica strada per cui un testo italiano arriva al sorgente
    **senza passare da `applica.py`**, che degrada gli accenti a ogni punto in
    cui un dato del dizionario diventa codice. Una toppa che porti una vocale
    accentata vera fa esplodere la scrittura del file — «bambù», 2026-08-09 —
    e lo fa in fondo alla catena, dopo che tutto il resto e' gia' andato bene.

    Qui si rompe subito, e per tutte le toppe: quella che c'e' oggi e quella
    che qualcuno scrivera' domani.
    """
    for t in carica_toppe():
        for chiave in ("cerca", "sostituisci"):
            for riga in righe_di_toppa(t[chiave]):
                try:
                    riga.encode("cp932")
                except UnicodeEncodeError as e:
                    raise AssertionError(
                        f"la toppa «{t['motivo'][:50]}…» porta in `{chiave}` un "
                        f"carattere che CP932 non ha: {riga[e.start:e.end]!r}. "
                        "Va degradato con accenti.degrada() da chi genera la "
                        f"toppa.\n  {riga.strip()}") from None


# ---------------------------------------------------------------------------
# Toppe a blocco: piu' righe consecutive al posto di una sola.
#
# Nate il 2026-08-07 per la composizione del nome degli oggetti
# (`item_func.hsp:1259-1285`), dove il plurale della parola-contatore si fa col
# suffisso inglese (`scroll` + `"s "`). In italiano il plurale e' irregolare per
# parola: la riscrittura corretta vuole uno `switch`, cioe' un blocco, e una
# toppa di riga non ci arriva.
# ---------------------------------------------------------------------------

BLOCCO_CERCA = [
    "\tif ( n > 1 ) {",
    '\t\ts = "" + n + " " + tipo + "s of "',
    "\t}",
]
BLOCCO_SOSTITUISCI = [
    "\tif ( n > 1 ) {",
    "\t\tswitch tipo",
    '\t\t\tcase "pergamena"',
    '\t\t\t\ts = "" + n + " pergamene di "',
    "\t\t\t\tswbreak",
    "\t\tswend",
    "\t}",
]


def toppa_blocco(**sovrascritture):
    base = {
        "file": "item_func.hsp",
        "cerca": BLOCCO_CERCA,
        "sostituisci": BLOCCO_SOSTITUISCI,
        "motivo": "prova a blocco",
    }
    base.update(sovrascritture)
    return base


def test_una_toppa_a_blocco_sostituisce_le_righe_consecutive():
    testo = sorgente("*itemname", *BLOCCO_CERCA, "\treturn s")
    nuovo, quante = applica_toppe("item_func.hsp", testo, [toppa_blocco()])
    assert quante == 1
    assert nuovo == sorgente("*itemname", *BLOCCO_SOSTITUISCI, "\treturn s")


def test_una_toppa_a_blocco_puo_cambiare_il_numero_di_righe():
    """Le toppe girano dopo il dizionario, quindi lo scivolamento non fa danni."""
    testo = sorgente("*itemname", *BLOCCO_CERCA, "\treturn s")
    nuovo, _ = applica_toppe("item_func.hsp", testo, [toppa_blocco()])
    righe = nuovo.split("\r\n")[:-1]
    assert len(righe) == 2 + len(BLOCCO_SOSTITUISCI)


def test_un_blocco_che_non_esiste_piu_ferma_la_catena():
    """Stessa regola delle toppe di riga: upstream l'ha riscritto, non si indovina."""
    testo = sorgente("*itemname", BLOCCO_CERCA[0], "\ts = 0", "\t}")
    with pytest.raises(SorgenteCorrotto, match="non esiste piu'"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco()])


def test_un_blocco_ambiguo_ferma_la_catena():
    testo = sorgente("*itemname", *BLOCCO_CERCA, "*altro", *BLOCCO_CERCA)
    with pytest.raises(SorgenteCorrotto, match="ambigu"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco()])


def test_un_blocco_identico_alla_sostituzione_e_un_errore():
    testo = sorgente("*itemname", *BLOCCO_CERCA)
    with pytest.raises(SorgenteCorrotto, match="cerca identica"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco(sostituisci=BLOCCO_CERCA)])


def test_un_blocco_vuoto_e_un_errore(tmp_path):
    """`carica_toppe` pretende i campi non vuoti: una lista vuota e' vuota."""
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_blocco(cerca=[]), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="campi mancanti o vuoti"):
        carica_toppe(percorso)


def test_riga_e_blocco_convivono_nello_stesso_file():
    testo = sorgente("*itemname", RIGA_NAME, *BLOCCO_CERCA)
    toppe = [toppa(file="item_func.hsp"), toppa_blocco()]
    nuovo, quante = applica_toppe("item_func.hsp", testo, toppe)
    assert quante == 2
    assert '"the "' not in nuovo
    assert '"s of "' not in nuovo


def test_carica_toppe_conserva_i_blocchi(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_blocco(), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert caricate[0]["cerca"] == BLOCCO_CERCA
