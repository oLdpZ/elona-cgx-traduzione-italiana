# strumenti/tests/test_menu_dialogo.py
"""Il tetto delle voci del menu del dialogo: la misura, il criterio, la rete.

La misura sta in `strumenti/menu_dialogo.py` e viene dal collaudo del
2026-08-17, dove una voce del negozio delle carte e' stata vista **tagliata**.
I test che la fissano vanno letti come una **prova con data**: se un domani una
voce dentro il tetto uscisse tagliata, sono loro a dover fallire per primi.
"""
import json

import pytest

from strumenti import percorsi

from strumenti.menu_dialogo import (
    CORNICE_RE_SELECT, FINESTRA_EVENTO, INIZIO_TESTO, INIZIO_VOCE_RE_SELECT,
    MARGINE_RE_SELECT, PERGAMENA, PIXEL_PER_CARATTERE, PIXEL_UTILI, TETTO,
    contenitore_di_menu, fuori_misura, fuori_misura_inglese,
    menu_non_ancora_tradotti, non_misurate, reso, righe_di_menu, tetto_di,
    voci_di_menu,
)

# una voce di menu statica, una dinamica, e un `chatMore` che NON e' una voce
SORGENTE = """\
*finto_negozio
\tchatList 1, lang("引き受ける", "Sure thing.")
\tchatList currentthing@tcg, lang("[チケット"+prezzo+"枚]カード", "["+prezzo+" Tickets] A card.")
\tchatMore lang("ながいはなし", "A long body of text that chatMore draws as the message"), strbye
\tgosub *chat_select
\treturn
"""

# lo stesso menu, ma disegnato dalla finestra dell'evento invece che dalla
# pergamena: e' la distinzione che questa rete non faceva
SORGENTE_EVENTO = """\
*finto_evento
\ts = lang("さいかい", "Reunion")
\tfile = "bg_finto"
\tbuff = lang("ほんぶん", "The body of the event text")
\tchatList 1, lang("いぬだ！", "a dog!")
\tgosub *re_select
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
    """407 px utili diviso 7 px per carattere.

    I 407 sono `wx + 577` (bordo interno della pergamena, misurato sulla
    schermata a finestra intera) meno `wx + 170` (dove `cs_list` mette il testo,
    letto dal sorgente). Se qualcuno tocca una delle due costanti senza
    rimisurare, si vede qui.
    """
    assert INIZIO_TESTO == 170
    assert PIXEL_UTILI == 407
    assert PIXEL_PER_CARATTERE == 7
    assert TETTO == 58


def test_il_passo_del_carattere_e_quello_che_usa_il_gioco():
    """⚠️ Il 2026-08-17 qui c'era 7,7, preso da `larghezze.py` senza verificare.

    Non e' lo stesso carattere: `*prompt_key` disegna con `font ..., 15 - en * 2`
    (13), questa finestra con `font ..., 14 - en * 2` (12). E il numero giusto
    non e' una stima: sta scritto nel sorgente, in `cs_list`, dove il gioco
    dimensiona la barra evidenziata.

        module.hsp:70
        locvar_cs_list_tx = limit(strlen(arg1) * 7 + 32 + arg5, 10, 480)

    Se un aggiornamento di CGX cambia quel 7, questo test cade e il tetto va
    rifatto. Il 32 e' il contorno: e' lui che, spalmato sui caratteri, faceva
    sembrare 7,7 un passo di carattere.
    """
    sorgente = percorsi.SORGENTE_HSP / "module.hsp"
    testo = sorgente.read_bytes().decode("cp932", "replace")
    riga = next(r for r in testo.splitlines()
                if "locvar_cs_list_tx = limit(" in r)
    assert f"* {PIXEL_PER_CARATTERE} + 32" in riga or f"*{PIXEL_PER_CARATTERE}+32" in riga, riga


def test_la_barra_evidenziata_del_lupo_mannaro_finisce_dove_il_passo_dice():
    """La misura del 2026-08-18, ridotta a un conto che si puo' rifare.

    `event.hsp:521`, sfondo `bg_re9`: la voce inglese ha 48 caratteri, la barra
    comincia a `wx + 60` con `wx = 783`, e a schermo finisce a 1210.
    Con 7 il conto torna al pixel; con 7,7 sarebbe finita 34 px piu' in la'.
    """
    voce = "The werewolf had murdered someone in cold blood!"
    assert len(voce) == 48
    assert 783 + 60 + (len(voce) * PIXEL_PER_CARATTERE + 32) - 1 == 1210


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


def test_la_voce_rotta_a_monte_resta_nota():
    """Una voce del negozio sfora **anche in inglese**: `:1968`, 77 caratteri.

    Non e' un permesso: la resa italiana l'ha comunque accorciata dentro il
    tetto. Serve a ricordare che il riquadro e' il tetto anche dove upstream lo
    sfonda — e che se un domani questo elenco si allunga, e' arrivata una voce
    nuova rotta di suo, non una nostra svista.

    ⚠️ **Fino al 2026-08-18 qui ce n'erano due.** La seconda, `:2108`, ha 54
    caratteri in inglese: era rotta solo per il tetto sbagliato da 52, e col
    tetto vero da 58 non lo e' mai stata. Un tetto troppo stretto non produce
    solo rese accorciate: produce anche **difetti di monte che non esistono**.
    """
    monte = {(f, r) for f, r, _, _ in fuori_misura_inglese()}
    assert monte == {("tcg_custom.hsp", 1968)}


# --- un chatList non e` sempre nella pergamena (corretto il 2026-08-18) ------

@pytest.fixture
def finto_evento(tmp_path):
    """Un menu dentro `*re_select`, con uno sfondo largo 200 px."""
    import struct

    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "evento.hsp").write_bytes(SORGENTE_EVENTO.encode("cp932"))

    grafica = tmp_path / "graphic"
    grafica.mkdir()
    # basta una testa di BMP: la rete legge solo i quattro byte a offset 18
    testa = bytearray(b"BM" + bytes(52))
    struct.pack_into("<ii", testa, 18, 200, 150)
    (grafica / "bg_finto.bmp").write_bytes(bytes(testa))

    dizionario = tmp_path / "dizionario"
    dizionario.mkdir()
    voci = [
        _voce(5, '"Un cane!"', '"a dog!"'),
        _voce(5, '"Una voce lunga quarantacinque caratteri!!!!"', '"a dog!"'),
    ]
    voci[1]["riga"] = 5
    (dizionario / "evento.hsp.jsonl").write_text(
        "\n".join(json.dumps(v, ensure_ascii=False) for v in voci) + "\n",
        encoding="utf-8")
    return dizionario, sorgente, grafica


def test_il_contenitore_dice_chi_disegna_il_menu(finto_evento):
    """`chatList` riempie la lista; a disegnarla e' il `gosub` che segue."""
    _, sorgente, _ = finto_evento
    assert contenitore_di_menu(sorgente) == {"evento.hsp": {5: ("re_select", "bg_finto")}}


def test_il_contenitore_si_cerca_SENZA_limite_di_righe():
    """La regressione per cui la misura andava rifatta.

    Il negozio delle carte impagina **253** righe di menu prima del suo
    `gosub *chat_select` (`tcg_custom.hsp:1968` -> `:2221`). Con una finestra di
    sessanta righe restavano 208 voci senza contenitore, e una voce senza
    contenitore e' una voce che non si sa misurare.
    """
    assert contenitore_di_menu()["tcg_custom.hsp"][1968][0] == PERGAMENA


def test_il_tetto_di_re_select_viene_dal_bmp_di_sfondo(finto_evento):
    """`(tx + 36 - 12 - 64) / 7`, con tx letto dalla testa del bitmap.

    Con uno sfondo da 200 px: `(200 + 36 - 12 - 64) / 7 = 22` caratteri, cioe'
    meno della meta' del tetto della pergamena. Se qualcuno tocca una delle tre
    costanti senza rileggere `event.hsp`, si vede qui.
    """
    _, _, grafica = finto_evento
    assert CORNICE_RE_SELECT == 36        # dx = tx + 36        (event.hsp:4153)
    assert INIZIO_VOCE_RE_SELECT == 64    # wx+60 (:4195) + 4   (module.hsp:129)
    assert MARGINE_RE_SELECT == 12        # il bordo, simmetrico al gcopy di :4165
    assert tetto_di(FINESTRA_EVENTO, "bg_finto", grafica) == 22


def test_una_voce_larga_per_la_pergamena_sfora_nella_finestra_evento(finto_evento):
    """Il permesso che questa correzione toglie.

    Quarantatre caratteri: **dentro** il tetto della pergamena (58) e fuori da
    quello di questo evento (22). Prima della correzione passava e a schermo
    sfondava; adesso la rete la vede.
    """
    dizionario, sorgente, grafica = finto_evento
    sfori = fuori_misura(dizionario, sorgente, grafica)
    assert [s[2] for s in sfori] == [43]
    assert 43 < TETTO, "il punto del test e' che nella pergamena ci sarebbe stata"


def test_un_contenitore_di_cui_non_si_e_letta_la_geometria_non_si_misura():
    """⚠️ None vuol dire «non guardato», non «va bene».

    Le 148 voci di `*talk_quest` e le 46 di `*com_txtadv_loop` non hanno una
    geometria letta. Dar loro 52 «tanto per avere un numero» e' il filtro furbo
    di `custom_dmgpop.hsp`: non prova niente e fa credere di aver guardato.
    """
    assert tetto_di("talk_quest", "?") is None
    assert tetto_di(PERGAMENA, "?") == TETTO


def test_le_voci_tradotte_stanno_tutte_in_un_contenitore_misurabile():
    """Oggi le 68 voci sono tutte nella pergamena o nella finestra dell'evento.

    Se un domani questo elenco non e' piu' vuoto, e' arrivata una resa dentro un
    menu di cui nessuno ha misurato il riquadro: va misurato prima, non dopo.
    """
    scoperte = non_misurate()
    assert scoperte == [], "\n".join(
        "%s:%d in *%s" % (v["file"], v["riga"], v["_contenitore"]) for v in scoperte)
