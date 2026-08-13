# strumenti/tests/test_riquadri.py
"""I riquadri che non sono menu: le piastrelle dell'HUD e la colonna tattiche.

`larghezze.py` misura i menu che passano da `*prompt_key`, e quei due siti non
ci passano: nessuno li guardava. Il 2026-08-13 li ha guardati uno schermo, e
sfondavano tutti e due.

I test che fissano le misure vanno letti come **prove con data**: se un giorno
una resa dentro il tetto uscisse tagliata, o una fuori tetto uscisse intera,
sono loro a dover fallire per primi. Vedi `decisioni.md`, «Due tetti che
nessuno aveva misurato».
"""
import json

import pytest

from strumenti.riquadri import (
    COLONNA_TATTICHE, CORPO_HUD, CORPO_TATTICHE, INSET, RAPPORTO_COURIER,
    budget_colonna, budget_piastrella, colonna_dal_sorgente,
    etichette_senza_piastrella, fuori_misura_stati, fuori_misura_tattiche,
    piastrella_per_riga, piastrelle, righe_buffname,
)

FINTO_SCREEN = """\
	if ( cdata(CDATA_CONDITION_DRUNK, CHARA_PLAYER) != 0 ) {
		color 100, 0, 100
		pos sx, sy
		gcopy 3, 0, 416, 65 + en * 15, 15
		pos sx + 6, sy + 1
		mes _condrunk
		sy -= 20
	}
	if ( cbit(CHARA_BIT_DEATH_CREST, CHARA_PLAYER) ) {
		color 220, 0, 0
		pos sx, sy
		gcopy BUFFER_INF, 0 + en * 84, 416, 65 + en * 30, 15
		pos sx + 6, sy + 1
		mes _conkokusi
		sy -= 20
	}
	mes _consenzapiastrella
"""

FINTO_TEXT = """\
	_condrunk = lang("酔　い", "Ubriachezza")
	_conkokusi = lang("刻死紋", "Segno letale")
"""

FINTO_BUFF = """\
	buffname(BUFF_SPEED) = lang("加速", "Accelerazione")
	bufftxt(0, BUFF_SPEED) = lang("は機敏になった。", " diventa piu' agile."), " up."
"""

FINTO_TATTICHE = """\
*AIAbilityLearnMenu
	repeat NumActions+1
		cs_list listn(0, cnt), wx + 44 + (150 * (cnt/15)), (wy + 60 + cnt * 19 - 1) - (284 * (cnt/15)), 19
	loop

*AIValueSetMenu
	if ( CAIComparator(CurrentTactic, tc) == 4 ) {
		repeat MAX_BUFF-1, 1
			listn(0, NumActions) = buffname(cnt)
			NumActions++
		loop
	}
	font lang(cfg_font1, cfg_font2), 14 - en * 2, 0

	repeat NumActions+1
		keyrange = cnt + 1
		pos wx + 18 + (145 * (cnt/22)), (wy + 25 + cnt * 19 - 2) - (416 * (cnt/22))
		cs_list listn(0, cnt), wx + 18 + (145 * (cnt/22)), (wy + 25 + cnt * 19 - 1) - (417 * (cnt/22)), 19
	loop
"""


@pytest.fixture
def finto(tmp_path):
    cartella = tmp_path / "sorgente"
    cartella.mkdir()
    (cartella / "screen.hsp").write_bytes(FINTO_SCREEN.encode("cp932"))
    (cartella / "text.hsp").write_bytes(FINTO_TEXT.encode("cp932"))
    (cartella / "buff.hsp").write_bytes(FINTO_BUFF.encode("cp932"))
    (cartella / "custom_ai.hsp").write_bytes(FINTO_TATTICHE.encode("cp932"))
    return cartella


# --- le misure, con la loro data ---------------------------------------------

def test_la_piastrella_da_95_pixel_tiene_13_caratteri():
    """Misurato a schermo il 2026-08-13, ed e' la lettura che ha aperto tutto.

    «Marchio letale» e' 14 caratteri e usciva **«Marchio letal»**: esattamente
    13. Il tetto deve cadere li', non a 12 e non a 14.
    """
    assert budget_piastrella(95) == 13


def test_la_piastrella_da_80_pixel_tiene_11_caratteri():
    """L'altra piastrella, quella dei `gcopy 65 + en * 15`.

    L'ancora e' «Autopickup», 10 caratteri, che a schermo esce intera con un
    filo di margine.
    """
    assert budget_piastrella(80) == 11


def test_la_colonna_del_menu_tattiche_tiene_20_caratteri():
    """Misurato sullo stesso schermo, e con due ancore che si toccano.

    «Crescita della magia» e' 20 caratteri e **non** tocca la colonna dopo;
    «Crescita della destrezza», che e' 24, ci si sovrapponeva sopra.
    """
    assert budget_colonna() == 20


def test_il_passo_del_courier_e_sei_decimi_del_corpo():
    """Le due misure del 13/08 tornano tutte e due con lo stesso rapporto.

    Il carattere della build inglese e' `Courier New` (`config.txt`, `font2.`),
    che e' monospaziato: 12 px di corpo danno 7,2 px di passo e 11 ne danno
    6,6. Chi cambiasse una delle due misure senza toccare l'altra si accorge
    qui che ha rotto la relazione.
    """
    assert RAPPORTO_COURIER == pytest.approx(0.6)
    assert CORPO_TATTICHE * RAPPORTO_COURIER == pytest.approx(7.2)
    assert CORPO_HUD * RAPPORTO_COURIER == pytest.approx(6.6)
    assert INSET == 6


# --- la larghezza, letta dal sorgente ----------------------------------------

def test_la_piastrella_si_legge_dal_gcopy_che_la_precede(finto):
    """`65 + en * 15` nella build inglese sono 80 pixel, `65 + en * 30` sono 95.

    Chi leggesse il primo numero e basta si darebbe una piastrella da 65.
    """
    misurate = piastrelle(finto)
    assert misurate["_condrunk"] == 80
    assert misurate["_conkokusi"] == 95


def test_un_etichetta_disegnata_senza_piastrella_si_nota(finto):
    """Una `mes _conX` senza `gcopy` sopra non e' misurabile, e va detto.

    E' [[una-guardia-vale-solo-dove-guarda]]: un'etichetta che smette di
    trovare la sua piastrella smette di essere controllata, in silenzio.
    """
    assert etichette_senza_piastrella(finto) == {"_consenzapiastrella"}


def test_la_colonna_si_legge_dal_sorgente_non_si_ricorda(finto):
    """Il 145 sta in `custom_ai.hsp`, e se upstream lo cambia il tetto cambia.

    ⚠️ **E non e' l'unico elenco a colonne del file.** Prima di quello dei
    potenziamenti ce n'e' un altro, con un passo di **150**: una guardia che
    prendesse la prima `cs_list` misurerebbe un menu che non e' quello che sta
    controllando. Si parte dalla riga che elenca i `buffname` e si scende.
    """
    assert colonna_dal_sorgente(finto) == 145


def test_la_colonna_vera_del_menu_dei_potenziamenti_e_145():
    """Sul sorgente vero, dove gli elenchi a colonne sono quattro.

    Tre hanno passo 150 (`custom_ai.hsp:1263`, `:1337`, `:1821`) e solo quello
    dei potenziamenti ha 145 (`:3174`). Il verdetto per caso non cambierebbe —
    150 / 7,2 fa comunque 20 — ma una guardia giusta per sbaglio non e' una
    guardia.
    """
    assert colonna_dal_sorgente() == 145
    assert COLONNA_TATTICHE == 145


# --- che cosa e' una voce misurata -------------------------------------------

def test_solo_i_buffname_stanno_nella_colonna_tattiche(finto):
    """Un `bufftxt` e' un pezzo di frase, non una voce di elenco.

    Il menu tattiche elenca `buffname(cnt)` (`custom_ai.hsp:3138`) e nient'altro:
    misurare anche i `bufftxt` farebbe gridare al difetto su righe che nessuna
    colonna tocca.
    """
    assert righe_buffname(finto) == {1}


def test_ogni_voce_di_una_riga_di_stato_eredita_la_sua_piastrella(finto):
    """Le etichette stanno in array: piu' voci del dizionario sulla stessa riga.

    ⚠️ `occorrenza` e' 0 per tutte, quindi non distingue niente: l'unica cosa
    che le accomuna, ed e' quella che conta, e' la piastrella su cui finiscono.
    """
    per_riga = piastrella_per_riga(finto)
    assert per_riga == {1: 80, 2: 95}


# --- la forma misurata e' quella degradata -----------------------------------

def test_il_tetto_si_misura_sulla_forma_degradata():
    """`volonta'` e' 15 caratteri, `volontà` 14, e a schermo ci va la prima.

    Il dizionario tiene l'accento vero e lo degrada `applica`: chi misurasse la
    forma del dizionario si darebbe un carattere che non ha.
    """
    assert budget_colonna() == 20
    assert len("Cresce volontà") == 14
    assert len("Cresce volonta'") == 15


# --- che la rete prenda davvero ----------------------------------------------

def _dizionario(tmp_path, nome, voci):
    cartella = tmp_path / "dizionario"
    cartella.mkdir(exist_ok=True)
    (cartella / (nome + ".jsonl")).write_text(
        "\n".join(json.dumps(v, ensure_ascii=False) for v in voci) + "\n",
        encoding="utf-8")
    return cartella


def test_l_etichetta_che_sfonda_la_piastrella_viene_presa(finto, tmp_path):
    """Il difetto vero del 13/08, rimesso dentro apposta.

    Senza questo test i tre `== []` piu' sotto passerebbero anche se la
    funzione non trovasse mai niente.
    """
    diz = _dizionario(tmp_path, "text.hsp", [
        {"riga": 2, "it": "Marchio letale"},
    ])
    assert fuori_misura_stati(diz, finto) == [
        ("_conkokusi", 95, 13, 2, 14, "Marchio letale")]


def test_l_etichetta_lunga_quanto_il_tetto_non_viene_presa(finto, tmp_path):
    """Il confine, dal lato giusto: 13 caratteri su 13 ci stanno.

    E' «Marchio letal», cioe' quello che si vedeva a schermo: la parte che
    entrava. Un tetto sbagliato di uno lo prenderebbe, e a quel punto si
    accorcerebbero rese che non ne hanno bisogno.
    """
    diz = _dizionario(tmp_path, "text.hsp", [{"riga": 2, "it": "Marchio letal"}])
    assert fuori_misura_stati(diz, finto) == []


def test_il_buffname_che_sconfina_nella_colonna_viene_preso(finto, tmp_path):
    """«Crescita della costituzione», 27 caratteri, e' la peggiore delle dieci."""
    diz = _dizionario(tmp_path, "buff.hsp", [
        {"riga": 1, "it": "Crescita della costituzione"},
    ])
    assert fuori_misura_tattiche(diz, finto) == [
        ("BUFF_SPEED", 20, 1, 27, "Crescita della costituzione")]


def test_un_accento_conta_per_due_perche_a_schermo_va_degradato(finto, tmp_path):
    """`Cresce volontà` e' 14 nel dizionario e **15** a schermo.

    Il tetto della colonna e' 20, quindi qui non cambia il verdetto; cambia su
    una resa al confine, ed e' per questo che si misura la forma degradata.
    """
    diz = _dizionario(tmp_path, "buff.hsp", [{"riga": 1, "it": "Cresce volontà"}])
    assert fuori_misura_tattiche(diz, finto) == []
    diz = _dizionario(tmp_path, "buff.hsp", [{"riga": 1, "it": "Cresce la volontà altrui"}])
    sfori = fuori_misura_tattiche(diz, finto)
    assert sfori and sfori[0][3] == 25


# --- le reti vere ------------------------------------------------------------

def test_nessuna_etichetta_di_stato_sfora_la_sua_piastrella():
    """La regressione che questo file esiste per impedire.

    Il 2026-08-13 ne sforavano **19 su 61**, e una si vedeva a schermo tagliata
    da chissa' quanto tempo.
    """
    sfori = fuori_misura_stati()
    assert sfori == [], "\n".join(
        "%s (%dpx, tetto %d): riga %d, %d caratteri: %s" % s for s in sfori)


def test_nessun_buffname_sfora_la_colonna_del_menu_tattiche():
    """Il 2026-08-13 ne sforavano **10 su 71**, e le colonne si sovrapponevano."""
    sfori = fuori_misura_tattiche()
    assert sfori == [], "\n".join(
        "%s (tetto %d): riga %d, %d caratteri: %s" % s for s in sfori)


def test_l_inglese_di_upstream_sta_nella_colonna_tattiche():
    """L'ancora del tetto: la colonna e' stata dimensionata sul set inglese.

    **0 su 71** lo sfondano, ed e' la ragione per cui il 20 e' un vincolo vero
    e non una cosa che il gioco accetta gia' rotta — al contrario dei
    `buffdesc`, dove 46 inglesi su 63 sfondano da sempre.
    """
    sfori = fuori_misura_tattiche(lingua="en")
    assert sfori == [], "\n".join(
        "%s (tetto %d): riga %d, %d caratteri: %s" % s for s in sfori)
