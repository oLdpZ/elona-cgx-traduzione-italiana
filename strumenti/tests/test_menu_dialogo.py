# strumenti/tests/test_menu_dialogo.py
"""Il tetto delle voci del menu del dialogo: la misura, il criterio, la rete.

La misura sta in `strumenti/menu_dialogo.py` e viene dal collaudo del
2026-08-17, dove una voce del negozio delle carte e' stata vista **tagliata**.
I test che la fissano vanno letti come una **prova con data**: se un domani una
voce dentro il tetto uscisse tagliata, sono loro a dover fallire per primi.
"""
import json
import re

import pytest

from strumenti import percorsi

from strumenti.menu_dialogo import (
    TETTO_DUE_COLONNE,
    tagliate_a_due_colonne,
    CORNICE_RE_SELECT, FINE_VOCE_LEGGI, FINESTRA_EVENTO, INIZIO_TESTO,
    INIZIO_VOCE_GOD, INIZIO_VOCE_LEGGI, INIZIO_VOCE_RE_SELECT, LARGHEZZA_GOD,
    LEGGI_CITTA, MARGINE_GOD, MARGINE_RE_SELECT,
    NON_DISEGNANO, PANNELLO_DEI, PERGAMENA, PIXEL_PER_CARATTERE, PIXEL_UTILI,
    SFONDO_A_MANO,
    TETTO, contenitore_di_menu, fuori_misura, fuori_misura_inglese,
    menu_non_ancora_tradotti, non_misurate, reso, righe_di_menu,
    sfondi_a_mano_da_togliere, tetto_di, voci_di_menu,
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


SORGENTE_MINUSCOLO = """\
*finto_minuscolo
\tfile = "bg_finto"
\tchatlist 1, lang("いぬだ！", "a dog!")
\tchatList 2, lang("ねこだ！", "a cat!")
\tgosub *re_select
\treturn
"""


def test_chatlist_minuscolo_e_la_stessa_cosa(tmp_path):
    """⚠️⚠️ HSP non distingue maiuscole e minuscole, e monte scrive in due modi.

    Nel sorgente pinnato ci sono 1.626 `chatList` e 31 `chatlist`, e il gioco li
    disegna uguali. Fino alla 74a questa rete cercava la sola forma con la L
    grande: quelle 31 righe non erano «dentro il tetto», erano **fuori dal
    perimetro**. 💡 Nessun referto poteva dirlo — un buco nel perimetro non
    produce un numero sbagliato, produce un numero che non c'e'.
    """
    (tmp_path / "finto.hsp").write_bytes(SORGENTE_MINUSCOLO.encode("cp932"))
    assert righe_di_menu(tmp_path) == {"finto.hsp": {3, 4}}


def test_le_due_scritture_di_chatlist_stanno_tutte_nel_perimetro():
    """Il censimento sul sorgente pinnato, che e' quel che la rete deve coprire.

    ⚠️ Il numero e' fissato apposta: se un aggiornamento CGX porta una terza
    scrittura (`CHATLIST`, `ChatList`) questo test resta verde ma il totale
    cambia, e il confronto col censimento lo fa vedere.
    """
    trovate = righe_di_menu()
    censimento = 0
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        for riga in percorso.read_bytes().decode("cp932", "replace").split("\n"):
            censimento += len(re.findall(r"(?i)\bchatlist\b", riga))
    assert censimento == 1626 + 31, "le scritture nel sorgente sono cambiate"
    assert sum(len(r) for r in trovate.values()) == censimento
    # le quindici minuscole di event.hsp: tredici sono i menu degli eventi di mare
    assert {3655, 3658, 3881, 3883, 3886} <= trovate["event.hsp"]


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


def test_le_voci_rotte_a_monte_restano_note():
    """Due voci sforano **anche in inglese**, e una l'ha vista lo schermo.

    Non e' un permesso: la resa italiana l'ha comunque accorciata dentro il
    tetto. Serve a ricordare che il riquadro e' il tetto anche dove upstream lo
    sfonda — e che se un domani questo elenco si allunga, e' arrivata una voce
    nuova rotta di suo, non una nostra svista.

    ⚠️ **Fino al 2026-08-18 qui ce n'erano due.** La seconda, `:2108`, ha 54
    caratteri in inglese: era rotta solo per il tetto sbagliato da 52, e col
    tetto vero da 58 non lo e' mai stata. Un tetto troppo stretto non produce
    solo rese accorciate: produce anche **difetti di monte che non esistono**.

    ⚠️⚠️ **E dalla 72a sono quattro.** Le due nuove non sono difetti nuovi: sono
    due voci del menu comune del dialogo (`chat.hsp:19527` da 59 caratteri e
    `:19563` da 60) che stavano in questo elenco da sempre e che nessuno vedeva,
    perche' fino alla 72a l'intero menu di `*talk_main` finiva fra le «non
    misurate» — attribuito a `*talk_quest`, che non disegna. 💡 Una rete che non
    misura un contenitore non tace solo sulle NOSTRE rese: tace anche sui
    difetti di monte che ci vivono dentro.

    ⚠️⚠️ **E dalla 73a sono SEI.** Le due nuove — `chat.hsp:17710` (60 caratteri)
    e `:17713` (76) — sono le azioni AP del compagno, rotte di loro da sempre:
    sono comparse qui il giorno in cui le abbiamo **tradotte**, perche'
    `voci_di_menu()` legge il DIZIONARIO e una voce non ancora resa non entra in
    nessuna misura. 💡 E' la lezione della 72a nella sua forma di tutti i giorni:
    *una rete tace sui difetti di monte che vivono dove noi non siamo ancora
    arrivati*, quindi questo elenco cresce mentre il progetto avanza, e la
    guardia serve a farlo crescere **con un motivo scritto** invece che da solo.
    Le due rese italiane stanno dentro il tetto (47 e 50 caratteri).

    ⭐ **E `event.hsp:521` non e' una deduzione: e' una fotografia.** La voce
    inglese dell'attacco del lupo mannaro ha 48 caratteri in un riquadro da 40
    (`bg_re9`, 280 px utili), e il 2026-08-18 il collaudo l'ha vista uscire
    dalla pergamena e finire stampata sopra la mappa. La resa italiana ne usa
    34. E' la prima voce di questo elenco che qualcuno ha guardato invece di
    calcolarla.

    ⚠️ **E dalla 75a sono SETTE.** `chat.hsp:22937` — «Not even the God of
    Machine would allow this workplace to exist!», 64 caratteri in un riquadro da
    58 — e' una delle due voci con cui il giocatore risponde al capo del Dock, ed
    e' comparsa qui il giorno in cui l'abbiamo tradotta, esattamente come le due
    della 73a: `voci_di_menu()` legge il DIZIONARIO, e una voce non ancora resa
    non entra in nessuna misura. 💡 Terza volta di fila che questo elenco cresce
    non perche' sia arrivato un difetto nuovo, ma perche' il progetto e' arrivato
    dov'era. La resa italiana ne usa 53.
    """
    monte = {(f, r) for f, r, _, _ in fuori_misura_inglese()}
    assert monte == {("tcg_custom.hsp", 1968), ("event.hsp", 521),
                    ("chat.hsp", 19527), ("chat.hsp", 19563),
                    ("chat.hsp", 17710), ("chat.hsp", 17713),
                    ("chat.hsp", 22937)}


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


# --- il terzo contenitore: il pannello degli dei ------------------------------
#
# Nato nella 61a, quando `god.hsp` e' entrato nel dizionario: le sue tre voci
# (`:345`-`:350`) risultavano dentro `*screen_drawStatus`, cioe' dentro un
# contenitore che non esiste. La regola «a disegnarla e' il gosub che segue» e'
# giusta e resta; quel che mancava e' che fra la voce e il ciclo che disegna
# davvero puo' esserci un gosub che ridisegna l'HUD.

SORGENTE_DEI = """\
*god_select
\tchatList 0, lang("信仰する", "Believe in a god")
\tchatList 2, lang("やめる", "Cancel")
\tgosub *screen_drawStatus
*god_select_WHILE1
\tdx = 650
\treturn
"""


@pytest.fixture
def finto_pannello_dei(tmp_path):
    (tmp_path / "god.hsp").write_bytes(SORGENTE_DEI.encode("cp932"))
    return tmp_path


def test_un_gosub_che_ridisegna_l_hud_non_e_il_contenitore(finto_pannello_dei):
    """`*screen_drawStatus` non apre nessuna finestra: si tira dritto."""
    trovate = contenitore_di_menu(finto_pannello_dei)["god.hsp"]
    assert trovate[2][0] == PANNELLO_DEI
    assert trovate[3][0] == PANNELLO_DEI


def test_screen_drawStatus_e_dichiarato_fra_quelli_che_non_disegnano():
    # se un domani qualcuno lo toglie da qui, il test sopra diventa rosso e si
    # capisce subito perche'
    assert "screen_drawStatus" in NON_DISEGNANO


def test_il_tetto_del_pannello_dei_viene_dal_dx_scritto_a_mano():
    """`god.hsp:382` scrive `dx = 650`, e non c'e' nessun bitmap di mezzo."""
    atteso = (LARGHEZZA_GOD - INIZIO_VOCE_GOD - MARGINE_GOD) // PIXEL_PER_CARATTERE
    assert tetto_di(PANNELLO_DEI, "?") == atteso
    assert atteso == 79


def test_le_voci_del_pannello_dei_ci_stanno_tutte():
    """La piu' lunga e' «Convertiti a Kumiromi della Messe»: 33 su 79."""
    voci = [v for v in voci_di_menu() if v["file"] == "god.hsp"]
    assert voci, "god.hsp non ha piu' voci di menu: e' cambiato il sorgente?"
    for v in voci:
        assert v["_contenitore"] == PANNELLO_DEI
    assert [v for v in fuori_misura() if v["file"] == "god.hsp"] == []


# --- il quarto contenitore: l'elenco delle leggi della citta' -----------------
#
# `economy.hsp:440`-`:441`. Il confine non e' il bordo della finestra
# (`ww = 480`, :458) ma la **striscia** che il gioco disegna sotto le righe pari:
# `gfini 365, 18` a partire da wx+74 (:494-:495). Sono 41 px in meno, cioe' sei
# caratteri, e su una frase intera sei caratteri si vedono.


def test_il_tetto_delle_leggi_viene_dalla_striscia_non_dalla_finestra():
    atteso = (FINE_VOCE_LEGGI - INIZIO_VOCE_LEGGI) // PIXEL_PER_CARATTERE
    assert tetto_di(LEGGI_CITTA, "?") == atteso
    assert atteso == 47
    # il bordo della finestra darebbe sei caratteri in piu': e' la differenza
    # che questo contenitore esiste per non regalare
    assert (480 - INIZIO_VOCE_LEGGI) // PIXEL_PER_CARATTERE > atteso


def test_le_due_leggi_della_citta_ci_stanno():
    voci = [v for v in voci_di_menu() if v["file"] == "economy.hsp"]
    assert voci, "economy.hsp non ha piu' voci di menu: e' cambiato il sorgente?"
    for v in voci:
        assert v["_contenitore"] == LEGGI_CITTA
    assert [v for v in fuori_misura() if v["file"] == "economy.hsp"] == []


# --- il secondo tetto della pergamena: le due colonne (nato nella 72a)

def test_il_tetto_delle_due_colonne_viene_dal_sorgente():
    """24 non e' una stima: e' l'argomento di `strmid` a `chat.hsp:25166`."""
    righe = (percorsi.SORGENTE_HSP / "chat.hsp").read_bytes().decode("cp932").splitlines()
    taglio = [r for r in righe if "strmid(listn(0, cnt), 0," in r]
    assert taglio, "la riga che taglia le voci a due colonne non c'e' piu'"
    assert str(TETTO_DUE_COLONNE) in taglio[0]


def test_nessuna_resa_peggiora_a_due_colonne():
    """Se l'inglese ci sta in 24, l'italiano ci deve stare.

    ⚠️ **Non e' «≤ 24 per tutti».** Quante voci abbia il menu dipende dal PNG —
    ruolo, trama, compagni — e non e' decidibile dal sorgente: un negoziante ne
    mostra sette e resta a una colonna, un compagno passa le dieci. Chiedere 24
    a tutte vorrebbe dire mutilare anche le voci che upstream stesso lascia
    tagliare. Il metro e' il confronto con l'inglese, come in
    `fuori_misura_inglese`.

    ⭐ Alla nascita ne ha trovate **dieci**, e nove erano di sessioni
    precedenti: fra queste i quattro «Il boss di ...», dove la cura non e' stata
    accorciare il nome del luogo — canonico e usato in `map.hsp` e `text.hsp` —
    ma l'apposizione che gli sta davanti: «Boss: Torre Rovente».
    """
    peggiorate = tagliate_a_due_colonne()
    assert peggiorate == [], "\n".join(
        "%s:%d  en %d -> it %d  %s" % (f, r, e, i, s) for f, r, e, i, s in peggiorate)


def test_le_due_colonne_valgono_solo_nella_pergamena():
    """Gli altri tre contenitori non hanno la seconda colonna: `chat.hsp:25164`
    e' dentro `if ( evochat == 0 )`, cioe' solo il menu del dialogo normale."""
    fuori = {f for f, _, _, _, _ in tagliate_a_due_colonne()}
    assert fuori <= {"chat.hsp", "tcg_custom.hsp"}


# --- il quarto gosub che non disegna, e lo sfondo letto a mano (nati nella 74a)
#
# Le sette voci che la guardia dei contenitori dichiarava «non misurate» a fine
# 73a erano due difetti diversi, e nessuno dei due era una resa sbagliata:
# `*convert_word` scambiato per una finestra, e uno sfondo scritto in un ramo di
# `if` che la ricerca all'indietro non raggiunge.

SORGENTE_SONNO = """\
*finto_sonno
\ts = lang("そいね", "Force Sleep Sharing")
\tfile = "bg_finto"
\tbuff = lang("ほんぶん", "What do you try...")
\tchatList 1, lang("ほうち", "(Leave them alone)")
\tgosub *convert_word
\tgosub *re_select
\treturn
"""


@pytest.fixture
def finto_sonno(tmp_path):
    (tmp_path / "event.hsp").write_bytes(SORGENTE_SONNO.encode("cp932"))
    return tmp_path


def test_un_gosub_che_scioglie_i_segnaposto_non_e_il_contenitore(finto_sonno):
    """A disegnare e' `*re_select`, che viene dopo: `*convert_word` sta in mezzo.

    E' la stessa forma di `*screen_drawStatus` e `*talk_quest`: un
    `gosub *etichetta` come tutti gli altri, che pero' non apre nessuna finestra.
    """
    trovate = contenitore_di_menu(finto_sonno)["event.hsp"]
    assert trovate[5] == (FINESTRA_EVENTO, "bg_finto")


def test_convert_word_e_dichiarato_fra_quelli_che_non_disegnano():
    # se un domani qualcuno lo toglie da qui, il test sopra diventa rosso e si
    # capisce subito perche'
    assert "convert_word" in NON_DISEGNANO


def test_convert_word_non_disegna_nessuna_voce_di_menu():
    """La prova che non e' una finestra: nel suo corpo non c'e' nessun `cs_list`.

    E' la stessa prova usata per `*talk_quest` nella 72a, e va rifatta sul
    sorgente invece che ricordata: `*convert_word` (`text.hsp:6899`) e' lungo
    1.266 righe e non fa altro che sciogliere i segnaposto `{...}` dentro `buff`.
    """
    righe = (percorsi.SORGENTE_HSP / "text.hsp").read_bytes().decode("cp932").split("\n")
    inizio = [i for i, r in enumerate(righe) if r.startswith("*convert_word")]
    assert len(inizio) == 1, "l'etichetta non c'e' piu' o e' raddoppiata"
    corpo = []
    for riga in righe[inizio[0] + 1:]:
        if riga.startswith("*"):
            break
        corpo.append(riga)
        if riga.strip() == "return":
            break
    assert corpo, "il corpo e' vuoto"
    assert [r for r in corpo if "cs_list" in r] == []
    assert [r for r in corpo if "chatList" in r] == []


def test_lo_sfondo_a_mano_vale_solo_dove_la_ricerca_non_trova_niente(finto_sonno):
    """⚠️ Il registro non SOVRASCRIVE: riempie un buco.

    Due risposte per lo stesso sito sarebbero un modo di litigare in silenzio, e
    quella scritta a mano invecchierebbe senza che nessuno se ne accorga. Qui la
    ricerca automatica trova `bg_finto` due righe sopra: il registro non conta, e
    `sfondi_a_mano_da_togliere` dice di levarlo.
    """
    bugia = {("event.hsp", 5): "bg_altro"}
    trovate = contenitore_di_menu(finto_sonno, a_mano=bugia)["event.hsp"]
    assert trovate[5][1] == "bg_finto"
    stantii = sfondi_a_mano_da_togliere(finto_sonno, a_mano=bugia)
    assert [(f, r) for f, r, _ in stantii] == [("event.hsp", 5)]


def test_il_registro_a_mano_e_ancora_tutto_valido():
    """Ogni voce del registro deve continuare a valere per le quattro ragioni
    per cui e' stata scritta: vedi `sfondi_a_mano_da_togliere`. ⚠️ Un elenco a
    mano che nessuno ricontrolla e' un permesso nascosto — la 68a."""
    stantii = sfondi_a_mano_da_togliere()
    assert stantii == [], "\n".join(
        "%s:%d  %s" % (f, r, motivo) for f, r, motivo in stantii)


def test_allargare_la_finestra_all_indietro_prenderebbe_il_ramo_sbagliato():
    """⭐⭐ Perche' il registro e' a mano e la ricerca resta corta.

    `event.hsp:3633`-`:3638` mette le due voci in due rami dello stesso `if`, e
    `:3512`-`:3519` sceglie il bitmap con la **stessa guardia**, 116 righe piu'
    su. Tornando indietro dalla voce del mare il primo `file =` che si incontra
    e' quello dell'**altro** ramo: la rete misurerebbe la voce stretta (tetto 33)
    col riquadro largo (45) e direbbe «dentro» per costruzione.

    💡 Il difetto che ne verrebbe fuori non e' un falso allarme — e' un permesso,
    cioe' la categoria che non si vede finche' qualcuno non guarda lo schermo.
    """
    righe = (percorsi.SORGENTE_HSP / "event.hsp").read_bytes().decode("cp932").split("\n")
    guardia = "if ( gdata(GDATA_AREA) == AREA_OCEAN ) {"
    assert righe[3512 - 1].strip() == guardia
    assert righe[3633 - 1].strip() == guardia

    prima = [r.strip() for r in righe[:3634 - 1] if r.strip().startswith("file = ")]
    assert prima[-1] == 'file = "bg_re13"', "il ramo della strada, non quello del mare"
    assert SFONDO_A_MANO[("event.hsp", 3634)] == "bg_re25"

    stretto = tetto_di(FINESTRA_EVENTO, "bg_re25")
    largo = tetto_di(FINESTRA_EVENTO, "bg_re13")
    assert (stretto, largo) == (33, 45)


def test_le_voci_del_sonno_condiviso_ci_stanno_tutte():
    """Le cinque voci di `event.hsp:2586`-`:2590`, sfondo `bg_re16`, tetto 45.

    Sono le voci per cui la guardia era rossa: la piu' lunga e' «(Lasciare stare
    e dormire)», 26 caratteri. Erano dentro anche prima — quel che mancava era
    che qualcuno le misurasse invece di dichiararle non misurabili.
    """
    voci = {v["riga"]: v for v in voci_di_menu()
            if v["file"] == "event.hsp" and 2586 <= v["riga"] <= 2590}
    assert sorted(voci) == [2586, 2587, 2588, 2589, 2590]
    tetto = tetto_di(FINESTRA_EVENTO, "bg_re16")
    assert tetto == 45
    for riga, voce in sorted(voci.items()):
        assert voce["_contenitore"] == FINESTRA_EVENTO
        assert voce["_sfondo"] == "bg_re16"
        assert len(reso(voce["it"])) <= tetto, (riga, voce["it"])
