"""Le prove delle battute della nuvoletta del gioco di carte (lotto D).

⚠️⚠️ La prova che conta di piu' non e' l'identita': e' la sua **prova al
contrario**. Un `applica_a_righe` che non toccasse mai niente supererebbe
l'identita' a occhi chiusi, e la 136a ha imparato che un cancello si prova
iniettando il guasto che dovrebbe accendere.

⚠️⚠️ E la seconda che conta e' quella sui **siti multipli**: lo stesso
letterale sta su due righe, e una resa che ne serva una sola fa dire al gioco
due cose diverse nello stesso momento. Nel sorgente vero i casi sono tre.
"""
import json

import pytest

from strumenti import percorsi
from strumenti.dialoghi import (ARRAY_ESENTI, ATTESE, applica_a_righe,
                                array_parlanti, avvisi, carica_dizionario,
                                decise, leggi, problemi, tutte, voci_da_array,
                                voci_dirette)

DIRETTA = '\t\t\t\tefllistaddchat "Totally not my fault.", c@tcg'
CNVTALK = '\t\t\tefllistaddchat cnvtalk("I tire of this."), ac@tcg'
DA_ARRAY = '\t\t\t\tefllistaddchat randomchat@tcg(rnd(3)), ac@tcg'
ASSEGNA = '\t\t\trandomchat@tcg = "Uno!", "Due!", "Tre!"'


def _righe(*testo: str) -> list[str]:
    return list(testo)


# --- il riconoscitore: chi parla, non che forma ha la stringa --------------

def test_riconosce_il_letterale_passato_a_mano():
    trovate = voci_dirette(_righe(DIRETTA), "tcg.hsp")
    assert len(trovate) == 1
    assert trovate[0]["en"] == "Totally not my fault."
    assert trovate[0]["riga"] == 1


def test_riconosce_il_letterale_dentro_cnvtalk():
    trovate = voci_dirette(_righe(CNVTALK), "tcg_skill.hsp")
    assert [v["en"] for v in trovate] == ["I tire of this."]


def test_riconosce_una_battuta_di_una_parola_sola():
    """⭐ E' il motivo per cui questo strumento esiste. `copertura._PROSA`
    pretende **due parole alfabetiche**: `"Cheapskate."` non ne ha due, e per
    il censimento non esisteva. Ma sta a schermo come tutte le altre."""
    riga = '\t\t\t\t\tefllistaddchat "Cheapskate.", manytia@tcg'
    assert [v["en"] for v in voci_dirette(_righe(riga), "tcg_skill.hsp")] \
        == ["Cheapskate."]


def test_una_riga_commentata_non_e_una_battuta():
    """In HSP il commento e' `;` **oppure** `//`: guardare solo il `;` e' il
    guasto che le rinviate chiamano «la quarta volta»."""
    assert voci_dirette(_righe("\t//" + DIRETTA.lstrip()), "tcg.hsp") == []
    assert voci_dirette(_righe("\t;" + DIRETTA.lstrip()), "tcg.hsp") == []


def test_la_dichiarazione_della_funzione_non_e_una_chiamata():
    """`#deffunc efllistaddchat str efllistadd_argstr, ...` (`tcg.hsp:1362`)
    contiene il nome ma non fa parlare nessuno."""
    riga = "#deffunc efllistaddchat str efllistadd_argstr, int a, int b"
    assert voci_dirette(_righe(riga), "tcg.hsp") == []


def test_un_array_che_parla_viene_trovato_dal_sito_che_lo_legge():
    assert list(array_parlanti({"tcg_skill.hsp": _righe(DA_ARRAY)})) \
        == ["randomchat@tcg"]


def test_l_array_gia_reso_da_un_altro_meccanismo_e_esente_e_dichiarato():
    """⚠️ Due meccanismi che scrivono la stessa riga sono il modo in cui una
    resa sparisce senza che nessuno lo veda: `efftalk@tcg` lo rende
    `carte.battute()` dalla Fase 5, e qui resta **dichiarato**, non sparito."""
    riga = "\t\t\tefllistaddchat efftalk@tcg(eff@tcg), effac@tcg"
    assert array_parlanti({"tcg_custom.hsp": _righe(riga)}) == {}
    assert "efftalk@tcg" in ARRAY_ESENTI


def test_una_assegnazione_porta_piu_battute_sulla_stessa_riga():
    """⚠️ E' la forma che la chiave-letterale di `schede.py` non sapeva
    reggere: li' una riga = una scheda, qui una riga = tre battute."""
    trovate = voci_da_array(_righe(ASSEGNA), "tcg_skill.hsp", ["randomchat@tcg"])
    assert [v["en"] for v in trovate] == ["Uno!", "Due!", "Tre!"]
    assert {v["riga"] for v in trovate} == {1}


def test_un_array_non_letto_da_nessuno_non_porta_battute():
    """La rete parte da chi parla: un array che nessuno passa a
    `efllistaddchat` non e' un repertorio di battute."""
    assert voci_da_array(_righe(ASSEGNA), "tcg_skill.hsp", []) == []


# --- il sorgente vero ------------------------------------------------------

def test_il_sorgente_vero_ha_il_numero_atteso_di_siti():
    """⚠️ Il numero atteso batte l'avviso, perche' non chiede a nessuno di
    ricordarsi. 77, non le 52 del piano della Fase 6: il conto e' stato
    **rifatto** partendo da chi parla, e le 25 di differenza sono battute che
    `_PROSA` non poteva vedere."""
    assert len(tutte()) == ATTESE


def test_nel_sorgente_vero_una_battuta_sta_su_piu_righe():
    """⚠️ La ragione per cui una voce ha una LISTA di siti."""
    siti = tutte()
    ripetuti = {v["en"] for v in siti
                if len([x for x in siti if x["en"] == v["en"]]) > 1}
    assert "H means HIGHLANDER!" in ripetuti
    assert "I tire of this stupid card game." in ripetuti


def test_col_dizionario_vuoto_il_sorgente_vero_torna_identico():
    for nome in ("tcg.hsp", "tcg_skill.hsp"):
        righe = leggi(nome)
        rifatte, fatte = applica_a_righe(righe, nome, {})
        assert fatte == 0
        assert rifatte == righe


# --- l'iniezione, e la sua prova al contrario ------------------------------

def test_l_iniezione_cambia_davvero_la_riga():
    """La prova al contrario dell'identita': se questa passa **e** passa
    l'identita', allora l'identita' vuol dire qualcosa."""
    righe = _righe(DIRETTA)
    diz = {"Totally not my fault.": {"en": "Totally not my fault.",
                                     "it": "Non e' mica colpa mia."}}
    fuori, fatte = applica_a_righe(righe, "tcg.hsp", diz)
    assert fatte == 1
    assert '"Non e\' mica colpa mia."' in fuori[0]
    assert "Totally not my fault." not in fuori[0]


def test_l_iniezione_serve_TUTTI_i_siti_di_una_chiave():
    """⚠️⚠️ Il caso vero: `"H means HIGHLANDER!"` sta a `:1716` e a `:7187`.
    Rendere un sito solo vuol dire un gioco che dice due cose diverse."""
    righe = _righe(DIRETTA, "\tmes 1", DIRETTA)
    diz = {"Totally not my fault.": {"en": "Totally not my fault.",
                                     "it": "Non e' colpa mia."}}
    fuori, fatte = applica_a_righe(righe, "tcg.hsp", diz)
    assert fatte == 2
    assert "Totally not my fault." not in "\n".join(fuori)


def test_l_iniezione_degrada_gli_accenti():
    """⚠️ CP932 non scrive nessuna vocale accentata italiana."""
    diz = {"Totally not my fault.": {"en": "Totally not my fault.",
                                     "it": "Non è colpa mia, città!"}}
    fuori, _ = applica_a_righe(_righe(DIRETTA), "tcg.hsp", diz)
    assert "citta'" in fuori[0]
    assert "è" not in fuori[0]


def test_una_resa_il_cui_monte_e_sparito_grida():
    """⚠️⚠️ Si cammina sul DIZIONARIO, non sui letterali del file: al contrario
    una voce col monte cambiato sparirebbe in silenzio, e la guardia che la
    proteggeva non potrebbe accendersi mai (la 137a l'ha trovato in
    `schede.py`, e l'ha trovato la prova, non una rilettura)."""
    diz = {"Una battuta che non c'e' piu'": {
        "en": "Una battuta che non c'e' piu'", "it": "x",
        "siti": [{"file": "tcg.hsp", "riga": 1}]}}
    with pytest.raises(ValueError):
        applica_a_righe(_righe(DIRETTA), "tcg.hsp", diz)


def test_una_battuta_da_array_si_inietta_come_le_altre():
    righe = _righe(DA_ARRAY, ASSEGNA)
    diz = {"Due!": {"en": "Due!", "it": "Twee!"}}
    fuori, fatte = applica_a_righe(righe, "tcg_skill.hsp", diz)
    assert fatte == 1
    assert fuori[1] == '\t\t\trandomchat@tcg = "Uno!", "Twee!", "Tre!"'


# --- il cancello -----------------------------------------------------------

def test_rifiuta_un_carattere_che_cp932_non_scrive():
    guai = problemi({"en": "x", "it": "«così»"}, 100)
    assert any("CP932" in g for g in guai)


def test_rifiuta_un_a_capo_che_l_inglese_non_ha():
    """`bmes` onora l'a capo, e la nuvoletta finisce sulla carta di sopra."""
    guai = problemi({"en": "One line.", "it": "Prima riga\\nseconda"}, 100)
    assert any("a capo" in g for g in guai)
    assert problemi({"en": "a\\nb", "it": "a\\nb"}, 100) == []


def test_rifiuta_una_resa_piu_lunga_del_massimo_inglese():
    """⚠️ Non c'e' un riquadro: c'e' `elax = 36 - strlen * 3`
    (`tcg.hsp:1366`). Il soffitto e' il punto oltre il quale la nuvoletta
    scorre a sinistra piu' di quanto il gioco abbia mai fatto."""
    assert problemi({"en": "corta", "it": "x" * 21}, 20) != []
    assert problemi({"en": "corta", "it": "x" * 20}, 20) == []


def test_rifiuta_un_kamui_che_non_dice_quel_che_la_scheda_dice_gia():
    """⚠️⚠️ `tcg_skill.hsp:7302-7308` ANNUNCIA i sette kamui, `effdesc@tcg`
    li DESCRIVE, e l'inglese di monte usa due nomi diversi per la stessa cosa.
    Una resa che nominasse gli dei in un altro modo farebbe annunciare un
    potere e descriverne un altro — e non lo vedrebbe nessun cancello che
    guardi la resa per conto suo."""
    buona = {"en": "<Grudge of the Abominable Gods>",
             "it": "<Rancore degli dei abominevoli>"}
    assert problemi(buona, 100) == []
    cattiva = dict(buona, it="<Rancore degli dei ripugnanti>")
    assert any("meta'" in g for g in problemi(cattiva, 100))


def test_il_vocabolario_del_gioco_di_carte_e_un_rifiuto():
    """`Deck` e' «mazzo» da 162 toppe: una battuta che dicesse «deck» sarebbe
    l'unico punto del gioco a dirlo."""
    assert problemi({"en": "Bethel in your Deck?", "it": "Bethel nel deck?"},
                    100) != []
    assert problemi({"en": "Bethel in your Deck?", "it": "Bethel nel mazzo?"},
                    100) == []


def test_una_resa_molto_piu_lunga_e_un_avviso_non_un_rifiuto():
    assert avvisi({"en": "corta", "it": "corta"}) == []
    assert avvisi({"en": "corta", "it": "corta" + "x" * 11}) != []


def test_una_invariata_e_decisa_quanto_una_resa():
    """⚠️ «Deciso» non vuol dire «tradotto»: `"AIEEE!!!"` e' un verso, e la
    decisione di lasciarlo sta scritta con la sua ragione. Un conto che le
    contasse come da fare chiederebbe per sempre un lavoro che non c'e'."""
    diz = {"a": {"en": "a", "it": "b"},
           "AIEEE!!!": {"en": "AIEEE!!!", "invariata": "verso"},
           "c": {"en": "c", "it": ""}}
    assert decise(diz) == {"a", "AIEEE!!!"}


def test_una_invariata_non_viene_iniettata():
    """Non ha una resa: se `applica` provasse a scriverla, la sostituzione non
    cambierebbe niente e il guasto uscirebbe li' invece che qui."""
    diz = {"Totally not my fault.": {"en": "Totally not my fault.",
                                     "invariata": "citazione"}}
    fuori, fatte = applica_a_righe(_righe(DIRETTA), "tcg.hsp", diz)
    assert fatte == 0
    assert fuori == _righe(DIRETTA)


# --- il dizionario vero ----------------------------------------------------

def test_ogni_voce_del_dizionario_vero_ha_ancora_il_suo_monte():
    """Il dizionario non puo' portare una chiave che il sorgente non ha piu':
    sarebbe una resa che non arriva a schermo e che nessuno conta come persa."""
    diz = carica_dizionario()
    if not diz:
        pytest.skip("il lotto D non e' ancora stato reimportato")
    monte = {v["en"] for v in tutte()}
    assert set(diz) <= monte


def test_ogni_voce_del_dizionario_vero_passa_il_cancello():
    diz = carica_dizionario()
    if not diz:
        pytest.skip("il lotto D non e' ancora stato reimportato")
    guai = {c: problemi(v) for c, v in diz.items() if problemi(v)}
    assert guai == {}


def test_il_dizionario_vero_e_scritto_una_voce_per_riga():
    percorso = percorsi.DIZIONARIO / "carte" / "dialoghi.jsonl"
    if not percorso.exists():
        pytest.skip("il lotto D non e' ancora stato reimportato")
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if riga.strip():
            assert "en" in json.loads(riga)
