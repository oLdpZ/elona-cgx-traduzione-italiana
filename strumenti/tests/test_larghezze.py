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
    FILE, MARGINE, PIXEL_PER_CARATTERE, budget, campi, fuori_misura, larghezza_inglese,
    larghezze, menu_diretti,
    menu_per_riga, menu_senza_larghezza, reso, siti_senza_larghezza,
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


def test_ogni_menu_ha_un_chiamante():
    """Un menu che smette di essere trovato smette di essere controllato.

    Oggi li trova tutti. Se un domani ne restasse fuori uno, va capito perche'
    prima di scrivere qui il suo nome come eccezione.
    """
    assert menu_senza_larghezza() == set()


def test_il_menu_del_corpo_si_trova_anche_se_non_si_chiama_txtset():
    """`txtplusbody` non segue la convenzione `txtset*`/`txtselect*`.

    La prima versione della guardia cercava le chiamate per quel prefisso, e
    questo menu — la parte del corpo da farsi crescere, action.hsp:12510 —
    restava l'unico non misurato, con l'aria di essere codice morto. I nomi si
    prendono da `menu_per_riga`, che li legge dal sorgente.
    """
    assert larghezze()["txtplusbody"] == 200


# --- la seconda strada: i menu che non passano da text.hsp -------------------
#
# Un menu si puo' scrivere anche senza `#deffunc`: una corsa di `promptAdd
# lang(...)` chiusa da `gosub *prompt_key`. Stesso riquadro, stesso carattere,
# stesso taglio. Sono 95 siti contro i 20 della prima strada.

def test_la_larghezza_e_il_terzo_campo_comunque_siano_scritti_i_primi_due():
    """`system.hsp:4275` fa `gfini val(2) - 17`: la larghezza e` il terzo campo.

    Cercare `promptx, prompty, N` ne trova venti su novantacinque: `chara.hsp`
    scrive `promptx, 240, 160` e `tcg.hsp` `basex@tcg + 420, basey@tcg + 230,
    200`. Il metro sta in *prompt_key, non nel nome dei parametri.
    """
    assert campi("basex@tcg + 420, basey@tcg + 230, 200, 1")[2].strip() == "200"
    assert campi("promptx, 240, 160, 1")[2].strip() == "160"


def test_la_lingua_allarga_il_riquadro_in_tutti_e_due_i_versi():
    """La rete conosceva solo `450 - 50 * en`, e non basta.

    `action.hsp:2242` scrive `180 + ( en * 50 )`: il menu del voto e` piu` largo
    in inglese, non piu` stretto. Chi leggesse il primo numero direbbe che «Vota
    per l'esecuzione» sfora un tetto da 17 — ed e` un falso positivo, perche' il
    tetto vero e` 23. La build e` quella inglese, cioe` `en = 1`.
    """
    assert larghezza_inglese("180 + ( en * 50 )") == 230
    assert larghezza_inglese("450 - 50 * en") == 400
    assert larghezza_inglese("300") == 300


def test_un_campo_che_non_e_un_numero_non_e_una_larghezza():
    """`val = (windoww - 220) / 2 + inf_screenx, winposy(90), 12, 1, 0` non e`
    un riquadro di menu: il 12 e` il numero di cifre di un campo d'immissione.
    Fidarsi della forma del `val =` inventa menu che non esistono.
    """
    assert larghezza_inglese("winposy(90)") is None
    assert larghezza_inglese("promptx") is None


DIRETTI = """\
#define global promptOk(%1=200,%2=1,%3=prompty) promptl(0,0)=lang("オッケー","Ok"),"y","0"\\
	:promptmax=1:val=promptx,%3,%1,%2:gosub *prompt_key

*un_menu_vero
	promptAdd lang("はい", "Yes"), "null", 0
	promptAdd lang("いいえ", "A very long English answer"), "null", 1
	val = promptx, 240, 160, 1
	gosub *prompt_key

*un_menu_senza_riquadro
	promptAdd lang("はい", "Yes"), "null", 0
	val = 0
	gosub *prompt_key
"""


@pytest.fixture
def diretti(tmp_path):
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / "diretto.hsp").write_bytes(DIRETTI.encode("cp932"))
    (cartella / FILE).write_bytes(b"")  # la prima strada non ha niente da dire
    return cartella


def test_una_corsa_di_promptadd_e_un_menu_col_riquadro_che_la_chiude(diretti):
    """La seconda strada: nessun `#deffunc`, nessun `s(cnt)`, solo promptAdd.

    Sono 95 siti contro i 20 di `text.hsp`, e ci vivono 151 voci con `lang()`.
    """
    misurati = menu_diretti(diretti)
    assert misurati[("diretto.hsp", 5)] == 160
    assert misurati[("diretto.hsp", 6)] == 160


def test_il_riquadro_dichiarato_dentro_una_macro_non_e_un_menu(diretti):
    """`init.hsp:19`-`:33` definisce `promptYesNo`, `promptOk`, `promptTagTeam`.

    Sono `#define`: il `gosub *prompt_key` che portano dentro non e` un sito, e
    il `%1=200` non e` una larghezza. Contarli fa nascere tre menu che non
    esistono, con dentro una voce che nessuno disegna li`.
    """
    assert not [riga for (_, riga) in menu_diretti(diretti) if riga <= 2]


def test_un_sito_senza_riquadro_non_si_misura_col_val_di_qualcun_altro(diretti):
    """`val = 0` compare 65 volte nel sorgente, e non e` mai una larghezza.

    Se la ricerca all'indietro tirasse su il primo `val =` che trova senza
    guardare quanti campi ha, questo menu si misurerebbe con un numero preso da
    un'altra istruzione. Meglio non misurato che misurato male: un sito che
    resta fuori lo dice il referto, un sito misurato male tace.
    """
    assert ("diretto.hsp", 11) not in menu_diretti(diretti)
    assert siti_senza_larghezza(diretti) == [("diretto.hsp", 13)]


def test_la_rete_misura_anche_i_menu_fuori_da_text_hsp(diretti, tmp_path):
    """Il punto cieco che la 57a, la 58a e la 59a avevano segnalato senza chiudere.

    La rete leggeva un dizionario solo, `text.hsp.jsonl`, e una voce resa in un
    menu di `command.hsp` non aveva nessuno che la guardasse. Il riquadro pero'
    e' lo stesso, e taglia lo stesso.
    """
    dizionario = tmp_path / "dizionario"
    dizionario.mkdir()
    voce = {"file": "diretto.hsp", "riga": 6, "en": "A very long English answer",
            "it": "Una risposta italiana molto molto piu' lunga del riquadro"}
    (dizionario / "diretto.hsp.jsonl").write_text(
        json.dumps(voce, ensure_ascii=False) + "\n", encoding="utf-8")

    sfori = fuori_misura(dizionario, diretti)

    assert [(sito, riga) for sito, _, _, riga, _, _ in sfori] == [("diretto.hsp:8", 6)]


def test_anche_i_menu_di_text_hsp_usano_lo_stesso_metro(tmp_path):
    """Le due strade devono misurare con lo stesso righello.

    La prima leggeva la larghezza con una regex sua, che conosceva solo
    `N - M * en`: davanti a `300 + (en * 25)` prendeva il 300 e buttava via i
    25 pixel che in inglese ci sono. Due misure diverse dello stesso riquadro
    sono la lezione della 59a — una rete che prende una costante dall'altra.
    """
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / FILE).write_bytes(
        '#deffunc txtsetlargo int a\n\ts(cnt) = lang("はい", "Yes")\n\treturn\n'
        .encode("cp932"))
    (cartella / "chiamante.hsp").write_bytes(
        "\ttxtsetlargo 1\n\tval = 0\n\tval = promptx, prompty, 300 + (en * 25), 0\n"
        "\tgosub *prompt_key\n".encode("cp932"))

    assert larghezze(cartella)["txtsetlargo"] == 325


def test_le_tre_forme_del_riquadro_nel_sorgente_vero():
    """Un punto misurato per ciascuna delle tre scritture che il gioco usa.

    Se un aggiornamento CGX cambiasse uno di questi numeri, la voce che ci sta
    dentro smetterebbe di essere misurata giusta senza che nessuno lo dica.
    """
    misurati = menu_diretti()
    assert misurati[("action.hsp", 2238)] == 230   # 180 + ( en * 50 )
    assert misurati[("chara.hsp", 3555)] == 160    # promptx, 240, 160
    assert misurati[("tcg.hsp", 2487)] == 300      # basex@tcg + 400, basey@tcg + 230, 300


def test_ogni_sito_di_prompt_key_ha_il_suo_riquadro():
    """Il fratello di `test_ogni_menu_ha_un_chiamante`, per la seconda strada.

    Sono 91 siti e 258 voci: se un domani ne restasse fuori uno, va capito
    perche' prima di scriverlo qui come eccezione.

    Il novantaduesimo sito e' `command.hsp:17287`, che sta **dentro un commento
    di blocco** insieme alle sue tre voci: e' il menu di uscita di upstream,
    spento dal mod. Una delle tre e' persino gia' resa (`:17285`,
    «Impostazioni»), ed e' materia di `misura-blocchi-spenti.py`, non di questa
    rete.
    """
    assert siti_senza_larghezza() == []
    assert len(menu_diretti()) == 258


MORTO = """\
*un_menu_con_un_val_spento
	promptAdd lang("はい", "Yes"), "null", 0
	val = promptx, prompty, 280, 1
	/********** ORIGINAL - BEGINNING **********
	val = promptx, prompty, 100, 1
	 ********** ORIGINAL - ENDING **********/
	gosub *prompt_key
"""

DUE_RAMI = """\
*un_menu_con_due_riquadri
	promptAdd lang("はい", "Yes"), "null", 0
	if ( negozio ) {
		val = promptx, prompty, 280, 1
	}
	else {
		val = promptx, prompty, 330, 1
	}
	gosub *prompt_key
"""


def test_un_val_dentro_un_commento_di_blocco_non_dichiara_niente(tmp_path):
    """`map_user.hsp:522` e` la riga di upstream tenuta in commento dal mod.

    Sta piu` vicina al `gosub` di quella viva, e una ricerca all'indietro che
    non guardi i commenti misura il menu con un numero che il gioco non usa.
    """
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / "morto.hsp").write_bytes(MORTO.encode("cp932"))
    (cartella / FILE).write_bytes(b"")

    assert menu_diretti(cartella)[("morto.hsp", 2)] == 280


def test_quando_un_menu_ha_piu_riquadri_vale_il_piu_stretto(tmp_path):
    """`map_user.hsp:529` allarga la finestra a 330 **solo dentro un negozio**.

    E` la stessa regola della prima strada — «se piu` chiamanti costruiscono lo
    stesso menu si tiene il piu` stretto» — perche' una voce deve stare in tutti
    i posti in cui il menu compare. ⚠️ Il piu` stretto non e` il piu` vicino: qui
    il ramo largo e` l'ultimo prima del `gosub`.
    """
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / "rami.hsp").write_bytes(DUE_RAMI.encode("cp932"))
    (cartella / FILE).write_bytes(b"")

    assert menu_diretti(cartella)[("rami.hsp", 2)] == 280
