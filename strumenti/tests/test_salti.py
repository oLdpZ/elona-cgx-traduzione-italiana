"""Le prove della rete del salto.

⚠️⚠️ La prova che conta di piu' e' quella al contrario: **il caso vero che la
140a ha trovato a mano deve accendere questa rete**. Se le tredici etichette
della riga di stato dell'editor di mazzo non si vedessero da qui, il modulo
sarebbe una misura in piu' da mantenere che non trova quel che e' stato scritto
per trovare — ed e' esattamente il modo in cui `disegnate` e' stata cieca su
`s@tcg` per due sessioni senza che nessuno se ne accorgesse.
"""
from strumenti import copertura, disegnate, percorsi, salti
from strumenti.commenti import righe_in_commento
from strumenti.salti import (DICHIARATI, blocchi, misti_di, problemi,
                             scoperte_di, specifiche_disegnate)


def _testo(*righe: str) -> str:
    return "\n".join(righe)


def _valori(testo: str) -> list[str]:
    return [t[3] for t in scoperte_di("x.hsp", testo)]


# --- l'ambito: i blocchi ---------------------------------------------------

def test_i_blocchi_si_tagliano_sulle_etichette():
    righe = ["\tmes s", "*primo", "\ts = \"a\"", "*secondo", "\ts = \"b\""].copy()
    assert blocchi(righe) == [("<testa>", 1, 1), ("primo", 2, 3),
                              ("secondo", 4, 5)]


def test_quel_che_sta_prima_della_prima_etichetta_e_un_blocco():
    """Non e' un dettaglio: in `command.hsp` le cinque sigle della riga di
    stato del personaggio (`Lv:`, ` DV:`, ` PV:`, ` HP: `, ` MP: `) stanno
    tutte nella testa del file, prima di qualunque `*etichetta`."""
    assert blocchi(["\ts = \"Lv:\"", "\tmes s"])[0] == ("<testa>", 1, 2)


# --- il primo limite tolto: l'assegnazione dentro le graffe ----------------

def test_vede_l_assegnazione_dentro_un_if_a_graffe():
    """⭐⭐ IL CASO VERO, ed e' il motivo per cui la rete esiste.
    `tcg.hsp:3348` e' `if ( sortmode@tcg == 0 ) { s@tcg += "Sort by: DBID   " }`
    e `tcg.hsp:3363` e' `mes s@tcg`: un salto solo, che `disegnate` non vede
    perche' la sua `_ASSEGNAZIONE` e' ancorata a inizio riga."""
    testo = _testo('\tif ( sortmode@tcg == 0 ) { s@tcg += "Sort by: DBID   " }',
                   '\tmes s@tcg')
    assert _valori(testo) == ["Sort by: DBID   "]
    assert disegnate.per_variabile(
        testo, disegnate.variabili_disegnate(testo)) == []


def test_vede_l_assegnazione_dopo_i_due_punti():
    """HSP separa due comandi sulla stessa riga con `:`."""
    testo = _testo('\tcolor 255, 255, 255 : s@tcg = "Fatto."',
                   '\tmes s@tcg')
    assert _valori(testo) == ["Fatto."]


def test_un_confronto_non_e_un_assegnazione():
    """⚠️ `==` non e' `=`. Senza questa distinzione ogni `if ( x == "male" )`
    diventerebbe testo a schermo, e il referto annegherebbe negli
    identificatori — che e' la ragione per cui `_PROSA` non guarda le parole
    sole."""
    testo = _testo('\tif ( s@tcg == "warrior" ) { color 0, 0, 0 }',
                   '\tmes s@tcg')
    assert _valori(testo) == []


# --- il secondo limite tolto: il nome generico, con l'ambito del blocco ----

def test_un_nome_generico_vale_dentro_il_suo_blocco():
    """⭐⭐ L'ALTRO CASO VERO. `help.hsp:387` mette le etichette dei tasti in
    `s`, e `help.hsp:393` disegna `mes s(cnt * 2)`: `disegnate` butta via `s`
    su tutto il file, e cosi' non ne vedeva nessuna."""
    testo = _testo("*com_help",
                   '\ts = "Pick Up", key_get, "Drop", key_drop',
                   "\tmes s(cnt * 2)")
    assert _valori(testo) == ["Pick Up", "Drop"]
    assert disegnate.variabili_disegnate(testo) == set()


def test_un_nome_generico_riempito_in_un_ALTRO_blocco_resta_fuori():
    """⚠️ Il prezzo dichiarato dell'ambito. `s` vuol dire una cosa diversa in
    ogni sottoprogramma, e seguirlo da un blocco all'altro direbbe «da
    tradurre» ai percorsi dei file e ai pezzi di salvataggio."""
    testo = _testo("*apparecchia",
                   '\ts = "Ciao a tutti"',
                   "*mostra",
                   "\tmes s")
    assert _valori(testo) == []


def test_un_nome_specifico_vale_invece_su_tutto_il_file():
    """`s@tcg`, `cfname@tcg`, `locvar_equipinfo_s`: un nome cosi' vuol dire la
    stessa cosa ovunque, e il `mes` puo' stare mille righe piu' in la'."""
    testo = _testo("*riempi",
                   '\tcfname@tcg = "All", "Blue"',
                   "*disegna",
                   "\tmes cfname@tcg(cnt)")
    assert _valori(testo) == ["All", "Blue"]


def test_specifiche_disegnate_non_raccoglie_i_nomi_generici():
    assert specifiche_disegnate(_testo("\tmes s@tcg", "\tmes s")) == {"s@tcg"}


# --- il salto vero: la catena oltre il primo passo -------------------------

def test_segue_la_catena_oltre_il_primo_passo():
    """⭐ Il pezzo che merita davvero il nome di «secondo salto»: `a = "..."`,
    `b = a`, `mes b`. ⚠️ Nel sorgente di oggi non trova niente da solo — i 50
    ritrovamenti vengono dai due limiti tolti sopra — e sta qui lo stesso
    perche' costa sei righe."""
    testo = _testo("*mostra",
                   '\ttesta = "Benvenuto"',
                   "\triga = testa",
                   "\tmes riga")
    assert _valori(testo) == ["Benvenuto"]


def test_una_variabile_che_nessuno_disegna_non_porta_niente():
    """La rete parte da chi disegna: un array che non finisce a schermo non e'
    testo, e contarlo sarebbe l'errore opposto."""
    testo = _testo("*salva", '\tsavedata@tcg = "deck1", "deck2"')
    assert _valori(testo) == []


# --- i filtri, che devono restare gli stessi delle altre reti -------------

def test_non_vede_il_ramo_giapponese_di_una_lang():
    testo = _testo("*mostra", '\ts@tcg = lang("こんにちは", "Hello there")',
                   "\tmes s@tcg")
    assert _valori(testo) == []


def test_non_vede_una_cornice_senza_lettere_ne_una_riga_commentata():
    assert _valori(_testo("*m", '\ts@tcg = " (" + n + ")"', "\tmes s@tcg")) == []
    assert _valori(_testo("*m", '\t;s@tcg = "Ciao qui"', "\tmes s@tcg")) == []


# --- l'altro asse: i letterali misti --------------------------------------

def test_un_letterale_misto_fuori_da_lang_porta_la_parte_inglese():
    """⚠️⚠️ `help.hsp:387` scrive giapponese e inglese INSIEME nella stessa
    stringa, fuori da `lang()`, e in inglese `*convertHelp` tiene solo quel che
    sta fra le parentesi. `_giapponese` lo scarta — giustamente, per le altre
    undicimila — e le 38 etichette di F1 erano invisibili per questo, non per
    il salto."""
    riga = '\ts = "アイテムを拾う(get)", key_get'
    assert [t[2] for t in misti_di("help.hsp", riga)] == ["get"]


def test_il_ramo_giapponese_di_una_lang_non_e_un_letterale_misto():
    """Dentro `lang()` il giapponese ha gia' il suo inglese accanto: contarlo
    fra i misti direbbe scoperto un lavoro che il dizionario copre."""
    riga = '\tmes lang("拾う(get)", "Pick up")'
    assert misti_di("x.hsp", riga) == []


# --- il sorgente vero ------------------------------------------------------

def _sorgente(nome: str):
    percorso = percorsi.SORGENTE_HSP / nome
    return (percorso.read_bytes().decode("cp932"),
            righe_in_commento(percorso))


def test_la_riga_di_stato_dell_editor_di_mazzo_si_vede_da_qui():
    """L'ancora della 140a: le tredici etichette trovate a mano. Sono gia'
    tradotte con le toppe, quindi non stanno fra le scoperte — ma la rete deve
    **vederle**, altrimenti non ha trovato il caso per cui e' stata scritta."""
    testo, morte = _sorgente("tcg.hsp")
    valori = {t[3] for t in scoperte_di("tcg.hsp", testo, morte)}
    for etichetta in ("Sort by: DBID   ", "Filter: Domain   ",
                      "Filter: Class2 & Sex   "):
        assert etichetta in valori


def test_le_38_etichette_dei_tasti_di_F1_si_contano_fra_i_MISTI():
    """L'altra ancora della 140a. ⚠️ Non sta fra le scoperte del salto ed e'
    giusto cosi': `help.hsp` e' un fronte dell'altro asse."""
    testo, morte = _sorgente("help.hsp")
    inglesi = [t[2] for t in misti_di("help.hsp", testo, morte)]
    assert len(inglesi) == 38
    for parola in ("get", "drop", "quaff", "zap", "Wide apply"):
        assert parola in inglesi


def test_del_fronte_di_50_ne_restano_6_e_sono_dichiarate():
    """⚠️⚠️ IL CONTO E' MISURATO, e questa prova esiste per farlo muovere solo
    insieme al lavoro. Il fronte che la rete ha aperto era di **50** stringhe
    su sette file, e la 141a lo ha chiuso quasi tutto nella stessa sessione:

        item_func.hsp  15  ->  0   le sigle del pannello, 14 toppe + `Trap`
        tcg.hsp        12  ->  0   erano gia' decise in `glossario.md`
        command.hsp    18  ->  4   14 sigle nude in `invariati.md`
        custom_ai.hsp   1  ->  0   il marcatore `(P)` diventa `(T)`
        config.hsp      1  ->  0   `GuruGuruSMF4`, nome di driver
        custom_tweaks   1  ->  0   `Nani?!`, l'altra meta' di una citazione
        map_func.hsp    2  ->  2   servono a schermo, non a tavolino

    ⚠️ Le sei che restano sono **dichiarate**, non dimenticate: tre pezzi di
    percorso che non sono testo, e tre che si decidono guardando la larghezza
    a schermo. Il numero qui non e' una soglia da tenere: e' la fotografia di
    quel che resta.
    """
    per_file = {r["file"]: r["distinte"] for r in salti.censimento()
                if r["distinte"]}
    assert per_file == {"command.hsp": 4, "map_func.hsp": 2}
    assert sum(per_file.values()) == 6
    for nome in ("item_func.hsp", "tcg.hsp", "custom_ai.hsp", "config.hsp",
                 "custom_tweaks.hsp"):
        assert nome not in per_file


def test_il_cancello_e_verde_e_le_due_dichiarazioni_dicono_perche():
    """⚠️⚠️ **Questa rete e' nata rossa**, ed e' stata l'unica del progetto a
    nascere cosi': un censimento nuovo che nascesse verde vorrebbe dire che non
    ha trovato niente. Adesso e' verde perche' ogni file e' o lavorato o
    dichiarato — non perche' la rete abbia smesso di guardare, e le due cose si
    distinguono da `test_del_fronte_di_50_ne_restano_6_e_sono_dichiarate`.
    """
    assert problemi() == []
    assert set(DICHIARATI) == {"command.hsp", "map_func.hsp"}


def test_quel_che_disegnate_vede_gia_non_si_dichiara_due_volte():
    """⚠️ Le dodici chiavi di classe di `action.hsp` e la «Jo» del jolly di
    `etc.hsp` rimbalzano a schermo e sono gia' dichiarate in `disegnate`:
    contarle anche qui vorrebbe dire due dichiarazioni della stessa cosa, che
    prima o poi divergono. E' la 136a, dove un file contato due volte ha
    sbagliato un referto di 800 stringhe."""
    per_file = {r["file"]: r for r in salti.censimento()}
    assert per_file["action.hsp"]["viste"] == 12
    assert per_file["action.hsp"]["distinte"] == 0
    assert "action.hsp" in disegnate.DICHIARATI


def test_le_due_reti_si_scoprono_a_vicenda():
    """La prova che dice se il modulo serve. ⚠️ Se `solo_qui` arrivasse a zero
    vorrebbe dire che `disegnate` da sola basta, e allora o il modulo va tolto
    o la rete ha smesso di guardare dove guardava."""
    confronto = salti.confronto()
    assert sum(len(r["solo_mie"]) for r in confronto) == 6
    assert sum(len(r["solo_sue"]) for r in confronto) > 0


def test_una_dichiarazione_col_conto_sbagliato_si_accende(monkeypatch):
    finto = {"command.hsp": salti.Dichiarazione("fronte", 3, "conto vecchio"),
             "map_func.hsp": DICHIARATI["map_func.hsp"]}
    monkeypatch.setattr(salti, "DICHIARATI", finto)
    guai = problemi()
    assert any("dichiarate 3 stringhe che saltano a schermo, nel sorgente ne "
               "sono 4" in g for g in guai)


def test_una_dichiarazione_diventata_inutile_si_accende(monkeypatch):
    """Quando un fronte viene lavorato, la sua riga va tolta: una
    dichiarazione che non serve piu' dice aperto un fronte chiuso."""
    finto = {"db_race.hsp": salti.Dichiarazione("fronte", 3, "non esiste")}
    monkeypatch.setattr(salti, "DICHIARATI", finto)
    assert any("db_race.hsp" in g and "va tolta" in g for g in problemi())


def test_ogni_dichiarazione_dice_perche():
    for nome, dichiarata in DICHIARATI.items():
        assert dichiarata.tipo in ("fronte", "esente"), nome
        assert len(dichiarata.motivo) > 40, nome


def test_i_nomi_generici_si_leggono_da_disegnate():
    """⚠️ Due copie della stessa lista sono due liste che un giorno divergono:
    una impara un nome e l'altra no."""
    assert salti.GENERICHE is disegnate._TROPPO_GENERICHE


def test_le_liste_sottratte_sono_le_stesse_delle_altre_reti():
    """Due misure della stessa cosa che tolgono liste diverse sono due numeri
    che non si possono confrontare."""
    toppe, rese, invarianti = salti._da_sottrarre()
    assert toppe == copertura._righe_con_toppa()
    assert rese == disegnate._rese_note()
    assert invarianti == disegnate._invarianti()


# --- quel che la 141a ha deciso a partire da questa rete -------------------

def test_le_dodici_parole_chiave_delle_carte_sono_dichiarate():
    """⚠️⚠️ Erano gia' decise **in `glossario.md`**, e nessuno strumento legge
    un paragrafo: e' la terza volta che il progetto lo impara (138a su `Dv:`,
    139a su `Immune`). ⚠️ Lo spazio in coda fa parte del valore: i tratti si
    concatenano in `s@tcg` e lo spazio e' quel che li separa a schermo."""
    from strumenti.verifica import carica_invariati

    invarianti = carica_invariati()
    for tratto in ("<Yerles> ", "<Xeren> ", "<Zanan> ", "<Lothrian> ",
                   "<Eulderna> ", "<Elea> ", "<Juere> ", "<Zaile> ",
                   "<Ninja> ", "<CNPC> ", "Immune ", "Kamikaze "):
        assert tratto in invarianti, tratto
    # ⭐ E il confine passa in mezzo alla colonna: i nomi comuni si traducono.
    for tradotto in ("<Bandit> ", "<Citizen> ", "<Teacher> "):
        assert tradotto not in invarianti, tradotto


def test_le_quattordici_sigle_nude_sono_dichiarate():
    """Stesso criterio di `Dv:` e `Lv`: una sigla latina **nuda**, fuori da
    `lang()`, la legge anche chi gioca in giapponese."""
    from strumenti.verifica import carica_invariati

    invarianti = carica_invariati()
    for sigla in ("Lv:", " DV:", " PV:", " HP: ", " MP: ", "Hp:", "Lv.",
                  "(Hp: ", " Lv.", "(MAX)", " cm", " kg", "p ", " x",
                  "GuruGuruSMF4", "Nani?!"):
        assert sigla in invarianti, repr(sigla)


def test_lo_spazio_in_coda_fa_parte_del_valore():
    """⚠️ ` Lv.` e `Lv.` sono due stringhe diverse, e tutt'e due esistono nel
    sorgente: se `invariati.md` le confondesse, una delle due resterebbe
    scoperta per sempre senza che niente lo dicesse."""
    from strumenti.verifica import carica_invariati

    invarianti = carica_invariati()
    assert "Lv." in invarianti and " Lv." in invarianti
    assert "p " in invarianti and "p" not in invarianti


def test_nella_build_il_marcatore_dell_IA_e_italiano():
    """⭐ `(P)` sta per *Preserve*, e la voce di menu che accende quel
    comportamento il progetto la rende «**Tieni** il soggetto come bersaglio»:
    se il marcatore restasse `P`, nella lingua del giocatore non ci sarebbe
    piu' nessuna parola a cui agganciarlo."""
    testo = (percorsi.BUILD_HSP / "custom_ai.hsp").read_bytes().decode("cp932")
    assert testo.count('s += "(T)"') == 2
    assert '"(P)"' not in testo
    assert "Tieni il soggetto come bersaglio" in testo
