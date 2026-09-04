"""Le prove delle schede di carta scritte a mano (`tcg_skill.hsp`, `tcg.hsp`).

⚠️ La prova che conta di piu' non e' l'identita': e' la sua **prova al
contrario**. Un `applica_a_righe` che non toccasse mai niente supererebbe
l'identita' a occhi chiusi.

⚠️⚠️ E la prova piu' importante non guarda una resa: guarda il **vocabolario**.
Il ramo dinamico della scheda e' italiano da fasi (`N.`, `Rarita':`,
`Effetto:`) e queste 72 sono scritte a mano: se non lo seguono, meta' gioco
dice una cosa e meta' l'altra, e non lo vedrebbe nessun cancello che guardi la
resa per conto suo.
"""
import pytest

from strumenti.schede import (ATTESE, GIUNTURE, VOCABOLARIO, applica_a_righe,
                              avvisi, carica_dizionario, disegnate, leggi,
                              problemi, tutte, voci)


def _righe(*testo: str) -> list[str]:
    return list(testo)


UNA_RIGA = ('\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "Cure Crystal  No.???'
            '   overpriced heal potion  Rare:None\\nEffect: Heal 2 Damage."')


# --- il riconoscitore ------------------------------------------------------

def test_riconosce_l_assegnazione_a_carddetailneff():
    trovate = voci(_righe(UNA_RIGA), "tcg_skill.hsp")
    assert len(trovate) == 1
    assert trovate[0]["riga"] == 1
    assert trovate[0]["en"].startswith("Cure Crystal")


def test_una_riga_commentata_non_e_una_scheda():
    """In HSP il commento e' `;` **oppure** `//`: guardare solo il `;` e' il
    guasto che le rinviate chiamano «la quarta volta»."""
    assert voci(_righe("\t//" + UNA_RIGA.lstrip()), "tcg_skill.hsp") == []
    assert voci(_righe("\t;" + UNA_RIGA.lstrip()), "tcg_skill.hsp") == []


def test_una_giuntura_dichiarata_non_e_una_scheda():
    """«ace of » e' un pezzo di nome che il gioco del poker concatena, non una
    scheda. Sta in `GIUNTURE` con la sua ragione invece di sparire."""
    riga = '\t\tcarddetailneff@tcg(aeft@tcg) = "ace of " + carddetailneff@tcg(x)'
    assert voci(_righe(riga), "tcg_skill.hsp") == []
    assert "ace of " in GIUNTURE


def test_il_sorgente_vero_ha_il_numero_atteso_di_schede():
    """⚠️ Il numero atteso batte l'avviso, perche' non chiede a nessuno di
    ricordarsi. 72, non le 76 del censimento della 135ª: la differenza sono le
    giunture piu' una traccia di debug, e sta rifatta in
    `scratchpad/_137-schede-riconcilia.py`."""
    assert len(tutte()) == ATTESE


def test_nel_sorgente_vero_i_letterali_sono_tutti_distinti():
    """E' l'unica cosa che rende il letterale una chiave usabile: qui non c'e'
    un nome di costante come nella Fase 5, e `file:riga` si sposta sotto una
    resa."""
    letterali = [v["en"] for v in tutte()]
    assert len(set(letterali)) == len(letterali)


# --- l'iniezione e la sua prova al contrario -------------------------------

def test_col_dizionario_vuoto_il_file_torna_identico():
    righe = _righe("prima", UNA_RIGA, "dopo")
    rifatte, fatte = applica_a_righe(righe, "tcg_skill.hsp", {})
    assert (rifatte, fatte) == (righe, 0)


def test_una_resa_viene_davvero_iniettata():
    """La prova al contrario dell'identita': col dizionario pieno il file
    DEVE cambiare, o l'identita' qui sopra non prova niente."""
    righe = _righe(UNA_RIGA)
    monte = voci(righe, "tcg_skill.hsp")[0]["en"]
    diz = {monte: {"it": "Cristallo  N.???   pozione  Rarita':Nessuna"
                         "\\nEffetto: cura 2 danni."}}
    rifatte, fatte = applica_a_righe(righe, "tcg_skill.hsp", diz)
    assert fatte == 1
    assert "Cristallo" in rifatte[0]
    assert "Cure Crystal" not in rifatte[0]


def test_la_resa_viene_scritta_senza_accenti_veri():
    """CP932 non contiene nessuna vocale accentata italiana: «Rarità» a schermo
    e' «Rarita'», e degradare va fatto **prima** di scrivere."""
    righe = _righe(UNA_RIGA)
    monte = voci(righe, "tcg_skill.hsp")[0]["en"]
    rifatte, _ = applica_a_righe(righe, "tcg_skill.hsp",
                                 {monte: {"it": "Città N.??? Rarità: Effetto:"}})
    assert "Citta'" in rifatte[0]
    assert "Città" not in rifatte[0]


def test_una_resa_su_un_monte_cambiato_si_rifiuta():
    """Se il letterale non c'e' piu', la voce va **rifatta**, non riagganciata
    alla riga che nel frattempo ci e' finita sopra."""
    righe = _righe(UNA_RIGA)
    monte = voci(righe, "tcg_skill.hsp")[0]["en"]
    diverse = _righe(UNA_RIGA.replace("Cure Crystal", "Cure Crystal MK2"))
    with pytest.raises(ValueError):
        applica_a_righe(diverse, "tcg_skill.hsp", {monte: {"it": "x N.??? y"}})


# --- il vocabolario, che e' un RIFIUTO ------------------------------------

def test_una_resa_che_non_segue_il_ramo_dinamico_si_rifiuta():
    """`tcg.hsp:1509` scrive gia' «Rarità:» dentro una `lang()`. Una scheda a
    mano che dicesse ancora «Rare:» spaccherebbe il gioco in due meta' che
    parlano lingue diverse."""
    guai = problemi({"en": "X  No.???  Rare:None\\nEffect: nothing.",
                     "it": "X  No.???  Rare:Nessuna\\nEffect: niente."})
    assert any("N.???" in g for g in guai)
    assert any("Rarita':" in g for g in guai)
    assert any("Effetto:" in g for g in guai)


def test_una_resa_che_lo_segue_passa():
    """Il confine si attraversa in tutt'e due i versi, o la prova non dice
    dove sta."""
    assert problemi({"en": "X  No.???  Rare:None\\nEffect: nothing.",
                     "it": "X  N.???  Rarita':Nessuna\\nEffetto: niente."}) == []


def test_il_vocabolario_copre_l_intestazione_e_non_la_inventa():
    """⚠️ Gli innesti NON stanno qui: li giudica `carte.problemi`, che sa che
    «Sacrifice» in testa e' «Sacrificio:» ma a meta' frase e' il verbo
    «sacrifica». Ricopiarli qui voleva dire ricopiarli peggio."""
    assert VOCABOLARIO["Bits:"] == "Tratti:"
    assert "Battlecry" not in VOCABOLARIO


def test_l_innesto_lo_giudica_il_cancello_delle_descrizioni():
    """La delega a `carte.problemi` non e' un dettaglio: e' il motivo per cui
    questo cancello conosce il glossario della 136ª senza averne una copia."""
    guai = problemi({"en": "X  Rare:None\\nEffect: Battlecry: draw a card.",
                     "it": "X  Rarita':Nessuna\\nEffetto: Urlo: pesca 1 carta."})
    assert any("Grido di battaglia" in g for g in guai), guai


# --- la larghezza, che qui non la limita nessuno --------------------------

def test_una_riga_piu_larga_dell_inglese_si_rifiuta():
    """⚠️ Queste schede NON passano da `talk_conv`: `cardhelp` le riceve gia'
    composte e `mes` le disegna verbatim. Il tetto e' il massimo che l'inglese
    di monte gia' disegna in queste stesse schede."""
    from strumenti.schede import _misura_inglese

    lunga = "x" * (_misura_inglese() + 1)
    guai = problemi({"en": "X  Rare:None\\nEffect: y.",
                     "it": lunga + "  Rarita':Nessuna\\nEffetto: y."})
    assert any("colonne" in g for g in guai), guai


def test_il_soffitto_di_larghezza_e_quello_dell_inglese_e_non_un_numero():
    """⭐ Il tetto non e' scelto: si **ricalcola dal file**. Se fosse una
    costante scritta a mano invecchierebbe in silenzio quando il sorgente si
    muove, ed e' esattamente il modo in cui un cancello smette di esserlo."""
    from strumenti.schede import _misura_inglese

    atteso = max(len(r) for v in tutte() for r in disegnate(v["en"]))
    assert _misura_inglese() == atteso


def test_l_a_capo_del_sorgente_e_due_caratteri_e_a_schermo_uno():
    """Nel file HSP `\\n` sono due caratteri; nell'eseguibile e' un ritorno a
    capo, e `mes` ci spezza la riga. Contare senza scioglierlo dice una riga
    sola dove il gioco ne disegna tre."""
    assert disegnate("uno\\ndue\\ntre") == ["uno", "due", "tre"]


# --- lo stato del lavoro ---------------------------------------------------

def test_tutte_le_schede_del_sorgente_sono_rese():
    diz = carica_dizionario()
    mancanti = [v["en"][:50] for v in tutte() if not diz.get(v["en"], {}).get("it")]
    assert mancanti == []


def test_nessuna_resa_del_dizionario_e_fuori_misura():
    diz = carica_dizionario()
    guai = [(v["file"], v["riga"], g)
            for v in tutte()
            for g in problemi(diz.get(v["en"], {}))]
    assert guai == []


def test_una_scheda_piu_alta_dell_inglese_e_un_avviso_non_un_rifiuto():
    """L'italiano e' piu' lungo dell'inglese quasi sempre; se «una riga in
    piu'» fosse un rifiuto, il cancello direbbe rosso su una resa corretta e
    chi traduce imparerebbe a non guardarlo (la distinzione della 70ª)."""
    voce = {"en": "X  Rare:None\\nEffect: y.",
            "it": "X  Rarita':Nessuna\\nEffetto: y.\\nancora."}
    assert problemi(voce) == []
    assert avvisi(voce) != []
