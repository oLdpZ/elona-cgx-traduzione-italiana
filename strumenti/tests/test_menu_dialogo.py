# strumenti/tests/test_menu_dialogo.py
"""Il tetto delle voci del menu del dialogo: la misura, il criterio, la rete.

La misura sta in `strumenti/menu_dialogo.py` e viene dal collaudo del
2026-08-17, dove una voce del negozio delle carte e' stata vista **tagliata**.
I test che la fissano vanno letti come una **prova con data**: se un domani una
voce dentro il tetto uscisse tagliata, sono loro a dover fallire per primi.
"""
import json

import pytest

from strumenti.menu_dialogo import (
    INIZIO_TESTO, PIXEL_PER_CARATTERE, PIXEL_UTILI, TETTO,
    fuori_misura, fuori_misura_inglese, menu_non_ancora_tradotti, reso,
    righe_di_menu, voci_di_menu,
)

# una voce di menu statica, una dinamica, e un `chatMore` che NON e' una voce
SORGENTE = """\
*finto_negozio
\tchatList 1, lang("引き受ける", "Sure thing.")
\tchatList currentthing@tcg, lang("[チケット"+prezzo+"枚]カード", "["+prezzo+" Tickets] A card.")
\tchatMore lang("ながいはなし", "A long body of text that chatMore draws as the message"), strbye
\treturn
"""


def _voce(riga, it, en_grezzo, tipo="statica"):
    return {
        "firma": "f%d" % riga, "file": "finto.hsp", "riga": riga, "occorrenza": 0,
        "jp": "", "jp_grezzo": "", "en": "", "en_grezzo": en_grezzo,
        "tipo": tipo, "contesto": "", "it": it,
    }


@pytest.fixture
def finto(tmp_path):
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "finto.hsp").write_bytes(SORGENTE.encode("cp932"))

    dizionario = tmp_path / "dizionario"
    dizionario.mkdir()
    voci = [
        _voce(2, '"Vada per il si\'."', '"Sure thing."'),
        _voce(3, '"[" + prezzo + " biglietti] Una carta."',
              '"[" + prezzo + " Tickets] A card."', tipo="dinamica"),
        _voce(4, '"Un corpo di testo lungo che chatMore disegna come messaggio"',
              '"A long body of text that chatMore draws as the message"'),
    ]
    (dizionario / "finto.hsp.jsonl").write_text(
        "\n".join(json.dumps(v, ensure_ascii=False) for v in voci) + "\n",
        encoding="utf-8")
    return dizionario, sorgente


# --- la misura, con la sua data ---------------------------------------------

def test_il_tetto_e_la_misura_del_2026_08_17():
    """407 px utili diviso 7,7 px per carattere.

    I 407 sono `wx + 577` (bordo interno della pergamena, misurato sulla
    schermata a finestra intera) meno `wx + 170` (dove `cs_list` mette il testo,
    letto dal sorgente). Se qualcuno tocca una delle due costanti senza
    rimisurare, si vede qui.
    """
    assert INIZIO_TESTO == 170
    assert PIXEL_UTILI == 407
    assert PIXEL_PER_CARATTERE == pytest.approx(7.7)
    assert TETTO == 52


def test_la_voce_piu_lunga_che_ci_stava_e_dentro_il_tetto():
    """«[4000 biglietti] Carta delle <Nove Code Dorate>.» — 47 caratteri, 357 px.

    Vista intera a schermo il 2026-08-17, con una cinquantina di pixel di
    margine prima del bordo. Il tetto deve stare sopra, non sotto.
    """
    assert TETTO >= 47


def test_la_voce_tagliata_a_schermo_e_fuori_dal_tetto():
    """«…Carta del dio-di-carta-piegata-segretissimo <Kamikakushi>.» — 75.

    A schermo si fermava su «segretissimo». Se un giorno il tetto salisse fino a
    coprirla, la misura sarebbe sbagliata: quella riga NON ci stava.
    """
    assert TETTO < 75


# --- che cosa e` una voce di menu, e che cosa no -----------------------------

def test_solo_chatlist_e_una_voce_di_menu(finto):
    """`chatMore` disegna il CORPO del messaggio, che ha un'altra geometria.

    Il corpo lo misura la rete 14 (dodici righe, a capo a 53 caratteri): contarlo
    qui farebbe gridare al difetto su ogni battuta un po' lunga del gioco.
    """
    _, sorgente = finto
    assert righe_di_menu(sorgente) == {"finto.hsp": {2, 3}}


def test_anche_le_voci_STATICHE_entrano_nel_conto(finto):
    """La regressione per cui questa rete e' stata riscritta il giorno stesso.

    La prima versione riconosceva le voci dal campo `contesto`, che `estrai.py`
    riempie **solo per le dinamiche**: vedeva 31 voci su 150, e tutte le opzioni
    di conversazione — che sono quasi tutte statiche — le lasciava fuori.
    """
    dizionario, sorgente = finto
    righe = sorted(v["riga"] for v in voci_di_menu(dizionario, sorgente))
    assert righe == [2, 3], "la statica di riga 2 non deve sparire"


def test_il_denominatore_dice_quanto_resta_scoperto():
    """«Zero fuori misura» non vuol dire «tutto controllato».

    Nel sorgente le righe di menu sono oltre millecinquecento e il dizionario ne
    copre poche decine: il conto sta nel referto apposta per non farlo dimenticare.
    """
    assert menu_non_ancora_tradotti() > 1000


# --- la forma misurata e` quella che arriva a schermo ------------------------

def test_una_dinamica_si_misura_col_prezzo_dentro():
    """Quattro cifre, non tre: il set piu' caro del negozio costa 5500."""
    assert reso('"[" + prezzo + " biglietti] Carta."') == "[9999 biglietti] Carta."


def test_le_virgolette_di_hsp_non_si_contano():
    """`\\"` e' una virgoletta sola a schermo, non due caratteri."""
    assert reso('\\"Miao?\\"') == '"Miao?"'
    assert len(reso('\\"Miao?\\"')) == 7  # le virgolette si vedono, la barra no


def test_un_accento_degradato_vale_due_caratteri():
    assert reso("città") == "citta'"
    assert len(reso("città")) == 6


# --- la rete vera ------------------------------------------------------------

def test_nessuna_voce_di_menu_sfora_il_riquadro():
    """La regressione che questo file esiste per impedire.

    Il 2026-08-17 ne sforavano quattro, tutte nel negozio delle carte, e due
    erano nostre: l'inglese ci stava e la resa italiana no. Il difetto non si
    vedeva perche' nessuno misurava questa larghezza.
    """
    sfori = fuori_misura()
    assert sfori == [], "\n".join(
        "%s:%d  %d caratteri: %s" % s for s in sfori)


def test_le_due_voci_rotte_a_monte_restano_note():
    """Due voci del negozio sforano **anche in inglese** (`:1968`, `:2108`).

    Non e' un permesso: la resa italiana le ha comunque accorciate dentro il
    tetto. Serve a ricordare che il riquadro e' il tetto anche dove upstream lo
    sfonda — e che se un domani questo elenco si allunga, e' arrivata una voce
    nuova rotta di suo, non una nostra svista.
    """
    monte = {(f, r) for f, r, _, _ in fuori_misura_inglese()}
    assert monte == {("tcg_custom.hsp", 1968), ("tcg_custom.hsp", 2108)}
