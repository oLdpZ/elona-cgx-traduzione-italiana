"""Le prove della rete che parte da chi disegna.

⚠️⚠️ La prova che conta di piu' e' quella che dice **che cosa questa rete vede
e `_PROSA` no**: se le due vedessero le stesse cose, questo modulo non
servirebbe a niente e nessuno se ne accorgerebbe, perche' un censimento in
piu' che non trova niente somiglia molto a un censimento pulito.
"""
import pytest

from strumenti import copertura, disegnate, percorsi
from strumenti.commenti import righe_in_commento
from strumenti.disegnate import (COMANDI, DICHIARATI, disegnate_di, per_variabile,
                                 problemi, tutte_di, variabili_disegnate)


def _testo(*righe: str) -> str:
    return "\n".join(righe)


# --- livello 0: il letterale sulla riga che disegna ------------------------

def test_vede_un_letterale_passato_a_un_comando_che_disegna():
    trovate = disegnate_di("x.hsp", _testo('\tmes "Dv:" + dvr1'))
    assert trovate == [(1, "mes", "Dv:")]


def test_vede_una_parola_sola_che_PROSA_non_vedrebbe():
    """⭐ E' la ragione per cui questo modulo esiste. `_PROSA` pretende due
    parole alfabetiche separate da uno spazio: «Immune» ne ha una, e stava a
    schermo dentro un file dichiarato e contato."""
    riga = '\t\t\tbmes "Immune", 255, 255, 255'
    assert [t[2] for t in disegnate_di("tcg.hsp", _testo(riga))] == ["Immune"]
    assert copertura._PROSA.search("Immune") is None


def test_non_vede_il_ramo_giapponese_di_una_lang():
    """Il giapponese non e' lavoro che manca: e' l'altra meta' di ogni
    `lang()`, e il progetto traduce l'inglese."""
    riga = '\tmes lang("こんにちは", "Hello there")'
    assert disegnate_di("x.hsp", _testo(riga)) == []


def test_non_vede_il_giapponese_scritto_in_LETTERE_LATINE():
    """⚠️⚠️ Il caso vero: `chat.hsp:6711` e' `lang("Yes", "Yes.")` — il ramo
    giapponese in lettere latine. Il filtro sui byte non-ASCII non lo prende,
    e senza la seconda mappa il censimento direbbe «scoperta» la meta'
    giapponese di una riga tradotta."""
    riga = '\t\t\tchatList 0, lang("Yes", "Yes.")'
    assert disegnate_di("chat.hsp", _testo(riga)) == []


def test_non_vede_una_cornice_senza_lettere():
    assert disegnate_di("x.hsp", _testo('\tmes " (" + n + ")"')) == []


def test_non_vede_una_riga_commentata_ne_una_direttiva():
    assert disegnate_di("x.hsp", _testo('\t//mes "Ciao qui"')) == []
    assert disegnate_di("x.hsp", _testo('\t;mes "Ciao qui"')) == []
    assert disegnate_di("x.hsp", _testo('#deffunc mes str s')) == []


def test_ogni_comando_dichiarato_ha_una_ragione():
    """Una riga in `COMANDI` e' una dichiarazione: se il comando non disegna,
    il censimento gonfia; se manca, il censimento tace."""
    assert all(motivo.strip() for motivo in COMANDI.values())


# --- livello 1: il salto per variabile -------------------------------------

def test_trova_la_variabile_che_qualcuno_disegna():
    assert variabili_disegnate(_testo("\tmes s@tcg")) == {"s@tcg"}


def test_una_variabile_troppo_generica_non_fa_da_chiave():
    """⚠️ `s`, `buff`, `tmp` portano di tutto — numeri, percorsi, pezzi di
    salvataggio — e come chiave del salto direbbero «da tradurre» a mezzo
    gioco."""
    assert variabili_disegnate(_testo("\tmes s")) == set()
    assert variabili_disegnate(_testo("\ttxt buff")) == set()


def test_vede_il_letterale_che_arriva_a_schermo_di_rimbalzo():
    """⭐⭐ IL CASO CHE E' COSTATO DUE VOLTE. Le 58 etichette della 137a non
    stavano sulla riga di `mes`: stavano in `s@tcg += "[Command Card] "`, e
    `s@tcg` finiva a schermo venti righe piu' giu'."""
    testo = _testo('\t\ts@tcg += "[Command Card] "',
                   '\t\tmes s@tcg')
    nomi = variabili_disegnate(testo)
    assert [t[2] for t in per_variabile(testo, nomi)] == ["[Command Card] "]


def test_un_array_di_etichette_porta_piu_voci_sulla_stessa_riga():
    """Il menu dei filtri dell'editor mazzo, che e' il ritrovamento della
    138a: undici etichette su una riga sola."""
    testo = _testo('\t\tcfname@tcg = "All", "Blue", "Green", "White"',
                   '\t\tmes cfname@tcg(cnt)')
    nomi = variabili_disegnate(testo)
    assert [t[2] for t in per_variabile(testo, nomi)] \
        == ["All", "Blue", "Green", "White"]


def test_una_variabile_che_nessuno_disegna_non_porta_niente():
    """La rete parte da chi disegna: un array che non finisce a schermo non e'
    testo, e contarlo sarebbe l'errore opposto."""
    testo = _testo('\t\tsavedata@tcg = "deck1", "deck2"')
    assert per_variabile(testo, variabili_disegnate(testo)) == []


# --- il sorgente vero ------------------------------------------------------

def test_il_menu_dei_filtri_del_mazzo_e_dentro_il_censimento():
    """Il caso vero, nominato: se un giorno sparisce dal censimento, o e'
    stato tradotto o la rete si e' rotta — e la differenza si vede da qui."""
    percorso = percorsi.SORGENTE_HSP / "tcg.hsp"
    testo = percorso.read_bytes().decode("cp932")
    trovate = {t[2] for t in tutte_di("tcg.hsp", testo,
                                      righe_in_commento(percorso))}
    for etichetta in ("Cost 0", "1 HP", "2 Atk", "Legendary", "seamonster"):
        assert etichetta in trovate


def test_il_cancello_del_sorgente_vero_e_verde():
    """Verde = ogni stringa che finisce a schermo o e' coperta da un
    meccanismo, o ha una riga in `DICHIARATI` con scritto perche'."""
    assert problemi() == []


def test_il_caso_vero_si_accende_senza_la_sua_riga(monkeypatch):
    """⭐ LA PROVA AL CONTRARIO. Tolta la dichiarazione di `action.hsp`, il
    cancello deve accendersi **sul file vero**.

    ⚠️ L'ancora era `tcg.hsp` fino alla 138a, ed e' stata spostata quando la
    139a ha tradotto le 129 etichette del menu dei filtri: quel file non ha
    piu' nessuna stringa scoperta, e una prova al contrario ancorata a un
    fronte chiuso non prova piu' niente. **L'ancora si sposta insieme al
    lavoro**, come la dichiarazione.
    """
    senza = {n: d for n, d in DICHIARATI.items() if n != "action.hsp"}
    monkeypatch.setattr(disegnate, "DICHIARATI", senza)
    guai = problemi()
    assert len(guai) == 1
    assert guai[0].startswith("action.hsp: 12 stringhe disegnate")


def test_un_conto_dichiarato_che_non_torna_si_accende(monkeypatch):
    finto = dict(DICHIARATI)
    finto["action.hsp"] = disegnate.Dichiarazione("fronte", 11, "conto vecchio")
    monkeypatch.setattr(disegnate, "DICHIARATI", finto)
    guai = problemi()
    assert len(guai) == 1
    assert "dichiarate 11 stringhe disegnate e scoperte, nel sorgente ne sono 12" \
        in guai[0]


def test_una_dichiarazione_diventata_inutile_si_accende(monkeypatch):
    """Quando un fronte viene lavorato, la sua riga va tolta: una
    dichiarazione che non serve piu' dice aperto un fronte chiuso. E' la
    lezione della 136a, dove un file dichiarato E coperto veniva contato due
    volte e il referto sbagliava di 800."""
    finto = dict(DICHIARATI)
    finto["db_race.hsp"] = disegnate.Dichiarazione("fronte", 3, "non esiste")
    monkeypatch.setattr(disegnate, "DICHIARATI", finto)
    assert any("db_race.hsp" in g and "va tolta" in g for g in problemi())


def test_le_due_reti_si_scoprono_a_vicenda_e_nessuna_basta():
    """⚠️⚠️ La prova che dice se il modulo serve, **nei due versi**.

    Il numero da solo non basta a dire niente: era 153 nella 138a ed e' 20
    dopo che la 139a ha tradotto le 129 etichette del menu dei filtri. Sceso
    perche' il lavoro e' stato fatto, non perche' la rete abbia smesso di
    cercare — e le due cose si distinguono guardando `--confronto`, non un
    numero. Per questo la soglia non e' un conto ma la **proprieta'**: ognuna
    delle due reti vede ancora qualcosa che l'altra non vede.

    ⚠️ Se un giorno `solo_qui` arrivasse a zero, questa prova si accende ed e'
    giusto che si accenda: vorra' dire che `copertura` da sola basta, e allora
    o il modulo va tolto, o la rete ha smesso di guardare dove guardava.
    """
    confronto = disegnate.confronto()
    solo_qui = sum(len(r["solo_mie"]) for r in confronto)
    solo_prosa = sum(len(r["solo_sue"]) for r in confronto)
    assert solo_qui > 0, "chi disegna non vede piu' niente che _PROSA non veda"
    assert solo_prosa > solo_qui, "_PROSA vede tracce di debug e stringhe di dato"


def test_ogni_dichiarazione_dice_perche():
    for nome, dichiarata in DICHIARATI.items():
        assert dichiarata.tipo in ("fronte", "esente"), nome
        assert len(dichiarata.motivo) > 40, nome
