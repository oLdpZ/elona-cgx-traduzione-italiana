# strumenti/tests/test_dati_applica.py
"""L'applicazione del dizionario a un file dati.

La prova che conta e' la **prova d'identita'**: un dizionario che traduce ogni
riga in se' stessa deve riprodurre il file **byte per byte**. E' la stessa
verifica che sugli `.hsp` ha trovato i due difetti peggiori del progetto mentre
83 test erano verdi, e non dipende da quali casi qualcuno si e' ricordato di
coprire: attraversa ogni riga del corpus vero.

⚠️ Byte per byte, non riga per riga: i CRLF sono il punto (65a).
"""
import pytest

from strumenti import dati, dati_applica, dati_estrai, percorsi

TESTO = (
    "### commento ###\r\n"
    "\r\n"
    "%A,JP\r\n"
    "giapponese\r\n"
    "%END\r\n"
    "\r\n"
    "%A,EN\r\n"
    "Titolo:corpo\r\n"
    "Secondo:altro corpo\r\n"
    "%END\r\n"
)


def _dizionario(testo, nome="board.txt", rese=None):
    voci = dati_estrai.voci(nome, dati.analizza(testo))
    for voce in voci:
        voce["it"] = (rese or {}).get(voce["en"], "")
    return {v["firma"]: v for v in voci}


# ------------------------------------------------------------ il nome del file

def test_il_file_italiano_si_chiama_col_suffisso():
    # accanto a quello di monte, non al posto suo: e' la disciplina di
    # cgx-test.exe, che non sovrascrive elonapluscgx.exe
    assert dati_applica.nome_italiano("board.txt") == "board_it.txt"
    assert dati_applica.nome_italiano("talk.txt") == "talk_it.txt"


# ------------------------------------------------------------ la sostituzione

def test_una_resa_sostituisce_solo_la_sua_riga():
    diz = _dizionario(TESTO, rese={"Titolo:corpo": "Titolo:tradotto"})
    nuovo, quante, orfane = dati_applica.applica_a_testo("board.txt", TESTO, diz)
    assert quante == 1 and orfane == []
    assert "Titolo:tradotto\r\n" in nuovo
    assert "Secondo:altro corpo\r\n" in nuovo
    assert "giapponese\r\n" in nuovo


def test_una_voce_non_tradotta_lascia_la_riga_com_era():
    diz = _dizionario(TESTO)
    nuovo, quante, _ = dati_applica.applica_a_testo("board.txt", TESTO, diz)
    assert quante == 0
    assert nuovo == TESTO


def test_i_crlf_restano_crlf():
    diz = _dizionario(TESTO, rese={"Titolo:corpo": "Titolo:tradotto"})
    nuovo, _, _ = dati_applica.applica_a_testo("board.txt", TESTO, diz)
    assert nuovo.count("\r\n") == TESTO.count("\r\n")
    assert "\n" not in nuovo.replace("\r\n", "")


def test_l_accento_si_degrada_applicando():
    # nel dizionario va «perché», a schermo esce «perche'»: CP932 la é non la
    # codifica, e la degradazione e' compito di chi applica
    diz = _dizionario(TESTO, rese={"Titolo:corpo": "Perché no:è così"})
    nuovo, _, _ = dati_applica.applica_a_testo("board.txt", TESTO, diz)
    assert "Perche' no:e' cosi'\r\n" in nuovo
    nuovo.encode("cp932")          # e il risultato dev'essere scrivibile


def test_una_voce_che_non_aggancia_niente_e_orfana():
    # monte ha riscritto la riga: la resa non va applicata a un testo che non e'
    # piu' quello, e il referto deve dirlo
    diz = _dizionario(TESTO, rese={"Titolo:corpo": "Titolo:tradotto"})
    cambiato = TESTO.replace("Titolo:corpo", "Titolo:corpo cambiato da monte")
    nuovo, quante, orfane = dati_applica.applica_a_testo("board.txt", cambiato, diz)
    assert quante == 0
    assert len(orfane) == 1


def test_una_resa_che_spaccherebbe_il_blocco_e_rifiutata():
    diz = _dizionario(TESTO, rese={"Titolo:corpo": "Titolo:uno\ndue"})
    with pytest.raises(ValueError):
        dati_applica.applica_a_testo("board.txt", TESTO, diz)


# ------------------------------------------------------- la prova d'identita'

def test_l_identita_riproduce_il_testo_costruito():
    diz = dati_applica.dizionario_identita("board.txt", TESTO)
    nuovo, quante, orfane = dati_applica.applica_a_testo("board.txt", TESTO, diz)
    assert nuovo == TESTO
    assert quante == 2 and orfane == []


@pytest.mark.parametrize("nome", ("autopick.txt", "board.txt", "book.txt",
                                  "exhelp.txt", "manual_ENG.txt", "talk.txt"))
def test_l_identita_riproduce_i_file_veri_byte_per_byte(nome):
    percorso = percorsi.DATI_SORGENTE / nome
    if not percorso.exists():
        pytest.skip(f"{nome} non e' ancora stato pinnato")
    grezzo = percorso.read_bytes()
    testo = grezzo.decode(dati.codifica(nome))
    diz = dati_applica.dizionario_identita(nome, testo)
    nuovo, quante, orfane = dati_applica.applica_a_testo(nome, testo, diz)
    assert orfane == []
    assert quante == len(diz), "l'identita' deve toccare ogni riga che dichiara"
    assert nuovo.encode(dati.codifica(nome)) == grezzo


# ---------------------------------------------------- il blocco CSV (%DEFINE)

DEFINE = (
    "%DEFINE\r\n"
    "0,日記,My Diary,\t\t\t\t1\r\n"
    "1,迷子の兵士に送るマニュアル,Beginner's Guide,\t0\r\n"
    "%END\r\n"
)


def test_la_resa_entra_nella_colonna_e_il_resto_della_riga_non_si_muove():
    diz = _dizionario(DEFINE, "book.txt", {"My Diary": "Il mio diario"})
    nuovo, quante, orfane = dati_applica.applica_a_testo("book.txt", DEFINE, diz)
    assert quante == 1 and orfane == []
    assert "0,日記,Il mio diario,\t\t\t\t1\r\n" in nuovo
    assert "1,迷子の兵士に送るマニュアル,Beginner's Guide,\t0\r\n" in nuovo


def test_una_resa_con_la_virgola_non_arriva_mai_al_file():
    """⚠️ Meglio fermarsi che scrivere una CSV con una colonna in piu'."""
    diz = _dizionario(DEFINE, "book.txt", {"My Diary": "Il diario, mio"})
    with pytest.raises(ValueError, match="virgola"):
        dati_applica.applica_a_testo("book.txt", DEFINE, diz)


def test_gli_accenti_si_degradano_anche_dentro_la_colonna():
    diz = _dizionario(DEFINE, "book.txt", {"My Diary": "Il diario perché"})
    nuovo, _, _ = dati_applica.applica_a_testo("book.txt", DEFINE, diz)
    assert "0,日記,Il diario perche',\t\t\t\t1\r\n" in nuovo


def test_l_identita_riproduce_il_blocco_csv():
    diz = dati_applica.dizionario_identita("book.txt", DEFINE)
    nuovo, quante, orfane = dati_applica.applica_a_testo("book.txt", DEFINE, diz)
    assert nuovo == DEFINE
    assert quante == 2 and orfane == []


def test_l_identita_dichiara_quante_righe_misura():
    percorso = percorsi.DATI_SORGENTE / "board.txt"
    if not percorso.exists():
        pytest.skip("board.txt non e' ancora stato pinnato")
    diz = dati_applica.dizionario_identita("board.txt", percorso.read_bytes().decode("cp932"))
    # se questo conto cala senza che nessuno abbia toccato niente, la prova sta
    # misurando meno di prima e nessun altro test lo direbbe
    assert len(diz) == 25
