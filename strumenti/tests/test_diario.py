# strumenti/tests/test_diario.py
"""Il tetto delle righe che passano da `talk_conv`, e il difetto di monte.

`talk_conv` manda a capo da solo, e per questo per ventidue sessioni nessuno
l'ha misurato. Ma il ramo inglese (`init.hsp:1326-1369`) appende la coda dopo
l'ultimo spazio **senza controllo di larghezza**, e il riquadro del diario la
taglia: il 2026-08-11 la prima riga della trama e' uscita «…si trova qualco».

I test qui fissano due cose: che il simulatore riproduca il difetto — un
simulatore che lo corregge non troverebbe niente — e che il dizionario ci stia
dentro.
"""
from strumenti.diario import (
    EN, deffunc_che_mandano_a_capo, fuori_misura, manda_a_capo, reso, siti, tetto,
)


def test_il_tetto_della_build_inglese_e_36():
    # `talk_conv s, 40 - en * 4` con en = 1 (config.hsp:439)
    assert EN == 1
    assert tetto("40 - en * 4") == 36


def test_un_tetto_che_dipende_dalla_finestra_non_si_indovina():
    # event.hsp e help.hsp derivano la larghezza dalla dimensione della finestra
    assert tetto("(dx - 80) / (7 - en) - en * 4") is None
    assert tetto("(ww - 110 - en * 50) / 7") is None


def test_manda_a_capo_spezza_sugli_spazi():
    righe = manda_a_capo("uno due tre quattro cinque sei sette otto", 20)
    assert all(len(r.rstrip()) <= 20 for r in righe[:-1])
    assert "".join(righe) == "uno due tre quattro cinque sei sette otto"


def test_l_ultima_parola_entra_senza_controllo():
    """Il difetto di monte, riprodotto alla lettera.

    Sono 36 caratteri esatti di parole separate da spazio piu' una parola finale
    lunga: l'algoritmo accumula fino a 36, poi non trova piu' spazi, esce dai due
    cicli e fa `talk_conv_arg1 += msgtemp`. La coda entra intera.
    """
    testo = "Devo combattere fino in fondo senza arrendermi."
    righe = manda_a_capo(testo, 36)
    assert len(righe) == 1
    assert len(righe[0]) == 47


def test_una_coda_corta_invece_ci_sta():
    righe = manda_a_capo("Devo combattere fino in fondo, senza mai arrendermi.", 36)
    assert all(len(r.rstrip()) <= 36 for r in righe)


def test_reso_stima_le_interpolazioni_e_degrada_gli_accenti():
    assert reso('"ne mancano " + gdata(X) + " da consegnare."') == "ne mancano 999 da consegnare."
    assert reso("perché") == "perche'"


def test_reso_scioglie_la_virgoletta_protetta():
    # a schermo si vede una virgoletta sola, non il backslash che la protegge
    assert reso('Ha detto \\"ciao\\".') == 'Ha detto "ciao".'


def test_i_siti_del_diario_si_trovano():
    trovati = siti()
    assert "text.hsp" in trovati
    # le 139 chiamate di *quest_info / *daily_info / *quest_info2 e dintorni
    assert len(trovati["text.hsp"]) > 100
    assert set(trovati["text.hsp"].values()) == {36, 33}


def test_il_parametro_arriva_a_talk_conv_per_copia():
    """`addnews2` non manda a capo il parametro: ne manda a capo una copia.

    Cercare il nome del parametro e basta trovava zero `#deffunc`, e con essi
    spariva tutta la pagina delle notizie — che e' meta' del diario.
    """
    inoltrano = deffunc_che_mandano_a_capo()
    assert inoltrano.get("addnews2") == 33


def test_le_notizie_passate_come_argomento_sono_misurate():
    # text.hsp:12122 e' `addnews2 lang("…", "…"), 1`: nessuna assegnazione locale
    assert siti()["text.hsp"].get(12122) == 33


def test_nessuna_riga_di_diario_sfora_il_suo_tetto():
    """La regressione che questo file esiste per impedire.

    Il 2026-08-11 ne sforavano 24, tutte scritte lo stesso giorno, e nessuna si
    vedeva: il diario sembrava a posto perche' `talk_conv` manda a capo da solo.
    """
    sfori = fuori_misura()
    assert sfori == [], "\n".join(
        "%s:%d (tetto %d): riga di %d caratteri: %s" % s for s in sfori)
