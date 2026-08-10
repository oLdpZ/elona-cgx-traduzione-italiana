# strumenti/tests/test_larghezze.py
"""Il tetto dei menu: la misura, il criterio, e il dizionario che ci sta dentro.

La misura sta in `strumenti/larghezze.py` e viene da due letture a schermo del
2026-08-10. I due test che la fissano vanno letti come una **prova con data**:
se un giorno una voce dentro il tetto uscisse tagliata, sono loro a dover
fallire per primi, prima che qualcuno cominci ad accorciare frasi a caso.
"""
import json

import pytest

from strumenti import percorsi
from strumenti.larghezze import (
    FILE, MARGINE, PIXEL_PER_CARATTERE, budget, fuori_misura, larghezze,
    menu_per_riga, menu_senza_larghezza, reso,
)

SORGENTE = """\
#deffunc txtsetfinto int txtsetfinto_arg1
	repeat txtsetfinto_arg1
		if ( p(cnt) == 0 ) {
			s(cnt) = lang("キャンセル", "Cancel")
		}
	loop
	txt lang("問題", "A question, not a menu entry")
	return

#deffunc txtsetaltro int txtsetaltro_arg1
	s(cnt) = lang("はい", "Yes")
	return
"""

CHIAMANTE = """\
	txtsetfinto 2
	repeat 2
		promptAdd s(cnt), key_select(cnt)
	loop
	val = promptx, prompty, 300, 1
	gosub *prompt_key
"""

CHIAMANTE_CON_EN = """\
	txtsetaltro 2
	repeat 2
		promptAdd s(cnt), key_select(cnt)
	loop
	val = promptx, prompty, 450 - 50 * en, 1
	gosub *prompt_key
"""


@pytest.fixture
def finto(tmp_path):
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / FILE).write_bytes(SORGENTE.encode("cp932"))
    (cartella / "chiamante.hsp").write_bytes(
        (CHIAMANTE + "\n" + CHIAMANTE_CON_EN).encode("cp932"))
    return cartella


# --- la misura, con la sua data ---------------------------------------------

def test_il_riquadro_da_300_pixel_tiene_32_caratteri():
    """Misurato il 2026-08-10 sul menu della frusta da domatore.

    A schermo il taglio cadeva dopo il 33esimo carattere; il tetto e` 32 perche'
    l'ultimo visibile e` gia' contro il bordo e non si spende.
    """
    assert budget(300) == 32


def test_il_riquadro_da_500_pixel_tiene_la_riga_inglese_piu_lunga_dell_abisso():
    """L'altra lettura dello stesso giorno, sul libro dell'abisso in inglese.

    `[Abyss Leading]    SAN10 /Convert items into abyss power` e` 55 caratteri e
    a schermo aveva ancora margine: il tetto deve stare sopra, non sotto.
    """
    assert budget(500) >= 55


def test_la_misura_e_una_retta_fra_i_due_punti():
    """Se qualcuno cambia una delle due costanti senza rimisurare, si vede qui."""
    assert PIXEL_PER_CARATTERE == pytest.approx(7.7)
    assert MARGINE == 46


# --- che cosa e` una voce di menu -------------------------------------------

def test_solo_le_assegnazioni_a_s_cnt_sono_voci_di_menu(finto):
    """Un `txt lang(...)` dentro lo stesso #deffunc e` un messaggio, non una voce.

    E' il caso vero di `text.hsp:1310`, la domanda del quiz: contarla faceva
    gridare al difetto su una riga che nessun riquadro tocca.
    """
    mappa = menu_per_riga(finto / FILE)
    assert list(mappa.values()) == ["txtsetfinto", "txtsetaltro"]
    righe = sorted(mappa)
    assert SORGENTE.split("\n")[righe[0] - 1].strip().startswith("s(cnt)")


def test_la_domanda_del_quiz_vero_non_e_una_voce_di_menu():
    """`text.hsp:1310` e` un `txt`, e non deve comparire fra le voci misurate."""
    assert 1310 not in menu_per_riga()


# --- la larghezza, letta dal chiamante --------------------------------------

def test_la_larghezza_si_legge_dal_chiamante(finto):
    assert larghezze(finto)["txtsetfinto"] == 300


def test_una_larghezza_che_dipende_dalla_lingua_vale_quella_inglese(finto):
    """`450 - 50 * en`: nella build inglese, che e` la nostra, sono 400.

    Chi leggesse il primo numero si darebbe 50 pixel che non ha.
    """
    assert larghezze(finto)["txtsetaltro"] == 400


def test_il_menu_del_quiz_trova_il_suo_prompt_cento_righe_piu_sotto():
    """I 35 menu del quiz condividono un solo `prompt_key` (chat.hsp:13055).

    Una ricerca che si fermasse dopo poche righe li lascerebbe tutti fuori dal
    controllo, in silenzio.
    """
    misurate = larghezze()
    assert misurate["txtsetquiz0"] == 310
    assert misurate["txtsetquiz34"] == 310


# --- la forma misurata e` quella degradata ----------------------------------

def test_un_accento_degradato_vale_due_caratteri():
    assert reso("città") == "citta'"
    assert len(reso("città")) == 6


def test_una_dinamica_si_misura_col_numero_dentro():
    assert reso('"Ti offro " + kane + " monete"') == "Ti offro 999 monete"


# --- la rete vera ------------------------------------------------------------

def test_nessuna_voce_di_menu_sfora_il_suo_riquadro():
    """La regressione che questo file esiste per impedire.

    Il 2026-08-10 ne sforavano 41, in venti menu, e otto stavano nello stesso
    riquadro da 300px: il difetto non si vedeva perche' nessuno lo misurava.
    """
    sfori = fuori_misura()
    assert sfori == [], "\n".join(
        "%s (%dpx, tetto %d): riga %d, %d caratteri: %s" % s for s in sfori)


def test_ogni_menu_ha_un_chiamante_tranne_quello_noto():
    """Un menu che smette di essere trovato smette di essere controllato.

    `txtplusbody` e` l'unico senza chiamante nel sorgente pinnato: se ne
    comparisse un altro, va capito prima perche', non aggiunto qui.
    """
    assert menu_senza_larghezza() == {"txtplusbody"}
