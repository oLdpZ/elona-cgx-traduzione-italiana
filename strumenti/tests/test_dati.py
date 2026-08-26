# strumenti/tests/test_dati.py
"""Il formato a blocchi dei file di `elonaplus2.31\\data\\`.

La prova che conta e' il **round-trip sui file veri**: un caso costruito prova
che la funzione fa quel che il test dice, non che il corpus e' fatto come il
test crede. Le sei forme qui sotto sono state contate sul corpus, non
immaginate:

    %END          board, book, exhelp, talk
    %END%         talk, 48 volte
    %DEFINE       book: un blocco SENZA lingua
    %AREA,5,EN\t\t\t/Vernis     intestazione con un commento dopo le tabulazioni
    %%SKILLTRAINER,JP           talk: due percento, un refuso di monte che
                                funziona solo perche' il gioco cerca una
                                sottostringa (`instr(buff, 0, "%" + s + ",EN")`)
    %COOK,GENERAL,EN            la chiave puo' contenere virgole

⚠️ I file dati vogliono i CRLF: `noteinfo(0)` conta le righe sui CRLF, e un file
a LF soltanto per HSP e' una riga sola (lezione della 65a). Per questo il
round-trip si misura sui **byte**, non sulle righe.
"""
import pytest

from strumenti import dati, percorsi

FILE_A_BLOCCHI = ("board.txt", "book.txt", "exhelp.txt", "talk.txt")


def _cartella_dati():
    for cartella in (percorsi.DATI_SORGENTE, percorsi.GIOCO / "data"):
        if cartella.is_dir():
            return cartella
    return None


def _testo_vero(nome):
    cartella = _cartella_dati()
    if cartella is None:
        pytest.skip("ne' dati-sorgente ne' la cartella data del gioco sono disponibili")
    percorso = cartella / nome
    if not percorso.exists():
        pytest.skip(f"{nome} non e' disponibile")
    return percorso.read_bytes()


# ---------------------------------------------------------------- il corpus

@pytest.mark.parametrize("nome", FILE_A_BLOCCHI)
def test_il_round_trip_e_esatto_sui_file_veri(nome):
    grezzo = _testo_vero(nome)
    testo = grezzo.decode("cp932")
    assert dati.serializza(dati.analizza(testo)) == testo
    # e la prova vera e' sui byte, perche' e' li' che vivono i CRLF
    assert dati.serializza(dati.analizza(testo)).encode("cp932") == grezzo


@pytest.mark.parametrize("nome", FILE_A_BLOCCHI)
def test_ogni_blocco_del_corpus_e_chiuso(nome):
    documento = dati.analizza(_testo_vero(nome).decode("cp932"))
    assert documento.blocchi, f"{nome}: nessun blocco trovato"
    for blocco in documento.blocchi:
        assert blocco.chiusura is not None, f"{nome}: {blocco.chiave} non e' chiuso"


def test_board_ha_i_venticinque_blocchi_inglesi_attesi():
    # se questo conto cambia, e' monte che ha cambiato il file: va visto, non
    # inseguito con una modifica al parser
    documento = dati.analizza(_testo_vero("board.txt").decode("cp932"))
    inglesi = [b for b in documento.blocchi if b.lingua == "EN"]
    giapponesi = [b for b in documento.blocchi if b.lingua == "JP"]
    assert len(inglesi) == 25
    assert len(giapponesi) == 25
    assert sum(len(b.righe_piene()) for b in inglesi) == 25
    assert sum(len(b.righe_piene()) for b in giapponesi) == 63


def test_ogni_blocco_inglese_di_board_ha_il_suo_giapponese():
    documento = dati.analizza(_testo_vero("board.txt").decode("cp932"))
    for blocco in documento.blocchi:
        if blocco.lingua == "EN":
            assert documento.blocco(blocco.chiave, "JP") is not None, blocco.chiave


# ---------------------------------------------- le forme dell'intestazione

def test_una_intestazione_dichiara_chiave_e_lingua():
    documento = dati.analizza("%COOK,GENERAL,EN\nuno\n%END\n")
    (blocco,) = documento.blocchi
    assert blocco.chiave == "COOK,GENERAL"
    assert blocco.lingua == "EN"


def test_una_intestazione_puo_portare_un_commento_dopo_le_tabulazioni():
    documento = dati.analizza("%AREA,5,EN\t\t\t/Vernis\nuno\n%END\n")
    (blocco,) = documento.blocchi
    assert blocco.chiave == "AREA,5"
    assert blocco.lingua == "EN"


def test_un_blocco_puo_non_avere_lingua():
    documento = dati.analizza("%DEFINE\nuno\n%END\n")
    (blocco,) = documento.blocchi
    assert blocco.chiave == "DEFINE"
    assert blocco.lingua == ""


def test_i_percento_di_troppo_non_entrano_nella_chiave():
    # %%SKILLTRAINER,JP e' un refuso di talk.txt: il gioco lo aggancia lo stesso
    # perche' cerca una sottostringa. Il parser non deve inventarci una chiave
    # che comincia per percento.
    documento = dati.analizza("%%SKILLTRAINER,JP\nuno\n%END\n")
    (blocco,) = documento.blocchi
    assert blocco.chiave == "SKILLTRAINER"


def test_end_con_percento_finale_chiude_il_blocco():
    documento = dati.analizza("%A,EN\nuno\n%END%\n%B,EN\ndue\n%END\n")
    assert [b.chiave for b in documento.blocchi] == ["A", "B"]
    assert [b.righe_piene() for b in documento.blocchi] == [["uno"], ["due"]]


def test_una_intestazione_nuova_chiude_un_blocco_rimasto_aperto():
    # non succede nel corpus, ma un file scritto a mano puo' dimenticare %END:
    # meglio un blocco chiuso d'ufficio che tutto il resto del file dentro
    documento = dati.analizza("%A,EN\nuno\n%B,EN\ndue\n%END\n")
    assert [b.chiave for b in documento.blocchi] == ["A", "B"]
    assert documento.blocchi[0].chiusura is None
    assert documento.blocchi[0].righe_piene() == ["uno"]


# ------------------------------------------------------- le righe e il testo

def test_le_righe_del_blocco_escludono_intestazione_e_chiusura():
    documento = dati.analizza("prima\n%A,EN\nuno\ndue\n%END\ndopo\n")
    (blocco,) = documento.blocchi
    assert blocco.righe_piene() == ["uno", "due"]


def test_le_righe_vuote_dentro_un_blocco_ci_sono_ma_non_sono_piene():
    documento = dati.analizza("%A,EN\nuno\n\ndue\n%END\n")
    (blocco,) = documento.blocchi
    assert blocco.righe_piene() == ["uno", "due"]
    assert len(blocco.indici) == 3


def test_il_testo_fuori_dai_blocchi_si_conserva():
    testo = "### commento ###\n\n%A,EN\nuno\n%END\n\n# coda\n"
    assert dati.serializza(dati.analizza(testo)) == testo


def test_un_file_senza_a_capo_finale_torna_uguale():
    testo = "%A,EN\nuno\n%END"
    assert dati.serializza(dati.analizza(testo)) == testo


def test_il_crlf_si_conserva():
    testo = "%A,EN\r\nuno\r\n%END\r\n"
    documento = dati.analizza(testo)
    assert documento.blocchi[0].righe_piene() == ["uno"]
    assert dati.serializza(documento) == testo


# ------------------------------------------------------------ la sostituzione

def test_sostituire_una_riga_conserva_il_fine_riga():
    testo = "%A,EN\r\nuno\r\ndue\r\n%END\r\n"
    documento = dati.analizza(testo)
    blocco = documento.blocchi[0]
    documento.sostituisci(blocco.indici[0], "UNO")
    assert dati.serializza(documento) == "%A,EN\r\nUNO\r\ndue\r\n%END\r\n"


def test_sostituire_non_tocca_le_altre_righe():
    testo = "prima\n%A,EN\nuno\ndue\n%END\ndopo\n"
    documento = dati.analizza(testo)
    documento.sostituisci(documento.blocchi[0].indici[1], "DUE")
    assert dati.serializza(documento) == "prima\n%A,EN\nuno\nDUE\n%END\ndopo\n"


def test_una_resa_con_un_a_capo_dentro_e_rifiutata():
    # spaccherebbe il blocco in due righe, e il gioco ne pesca una a caso:
    # meta' incarico. Vedi text.hsp:11654.
    documento = dati.analizza("%A,EN\nuno\n%END\n")
    with pytest.raises(ValueError):
        documento.sostituisci(documento.blocchi[0].indici[0], "uno\ndue")


def test_una_resa_che_comincia_per_percento_e_rifiutata():
    documento = dati.analizza("%A,EN\nuno\n%END\n")
    with pytest.raises(ValueError):
        documento.sostituisci(documento.blocchi[0].indici[0], "%END")


# ------------------------------------------------------------- la ricerca

def test_si_trova_un_blocco_per_chiave_e_lingua():
    documento = dati.analizza("%A,JP\njp\n%END\n%A,EN\nen\n%END\n")
    assert documento.blocco("A", "EN").righe_piene() == ["en"]
    assert documento.blocco("A", "JP").righe_piene() == ["jp"]
    assert documento.blocco("A", "IT") is None


# ------------------------------------------- il file piatto, e la codifica

def test_un_file_senza_blocchi_e_un_blocco_solo():
    """`autopick.txt` non ha `%CHIAVE,LINGUA`: e' un file di configurazione."""
    testo = "# commento\n\nregola\n"
    documento = dati.analizza_piatto(testo)

    assert len(documento.blocchi) == 1
    assert documento.blocchi[0].lingua == "EN"
    assert documento.blocchi[0].righe_piene() == ["# commento", "regola"]
    assert dati.serializza(documento) == testo


def test_il_lettore_piatto_si_sceglie_dal_nome_del_file():
    """⚠️ La prova al contrario: gli altri quattro NON vanno letti piatti."""
    testo = "%A,EN\nuno\n%END\n"

    assert dati.e_piatto("autopick.txt") is True
    assert dati.e_piatto("board.txt") is False
    # letto a blocchi ne trova uno con dentro una riga; letto piatto, tre righe
    assert dati.analizza_file("board.txt", testo).blocchi[0].righe_piene() == ["uno"]
    assert dati.analizza_file("autopick.txt", testo).blocchi[0].righe_piene() \
        == ["%A,EN", "uno", "%END"]


def test_autopick_e_l_unico_file_dati_in_utf8():
    assert dati.codifica("autopick.txt") == "utf-8"
    for nome in ("board.txt", "book.txt", "exhelp.txt", "manual_ENG.txt", "talk.txt"):
        assert dati.codifica(nome) == "cp932"


def test_i_file_senza_blocchi_sono_due_e_per_ragioni_diverse():
    """`autopick.txt` non ha blocchi; il manuale ce li ha in un altro file."""
    assert dati.e_piatto("manual_ENG.txt") is True
    assert dati.e_piatto("autopick.txt") is True
    for nome in ("board.txt", "book.txt", "exhelp.txt", "talk.txt"):
        assert dati.e_piatto(nome) is False


def test_il_manuale_vero_e_ascii_puro(tmp_path):
    """⚠️ Se un giorno monte ci mettesse un accento, il CP932 lo cancellerebbe."""
    from strumenti import percorsi
    percorso = percorsi.DATI_SORGENTE / "manual_ENG.txt"
    if not percorso.exists():
        pytest.skip("manual_ENG.txt non e' ancora stato pinnato")
    grezzo = percorso.read_bytes()
    assert all(byte < 128 for byte in grezzo), "non e' piu' ASCII puro"


def test_il_file_vero_non_si_decodifica_in_cp932(tmp_path):
    """La misura che ha fatto nascere la codifica per file, nella 100a.

    Se un giorno monte lo riscrivesse in CP932, questo test cade e la tabella
    delle codifiche va rivista invece di restare a mentire.
    """
    from strumenti import percorsi
    percorso = percorsi.DATI_SORGENTE / "autopick.txt"
    if not percorso.exists():
        pytest.skip("autopick.txt non e' ancora stato pinnato")

    grezzo = percorso.read_bytes()
    with pytest.raises(UnicodeDecodeError):
        grezzo.decode("cp932")
    assert dati.leggi(percorso).startswith("### Elona+ Custom-GX Autopickup")


# --------------------------------------------------- il blocco CSV (%DEFINE)

RIGA = "20,冒険暮らし,Adventurers Quarterly Spring '18,\t\t\t\t1"


def test_il_blocco_csv_si_dichiara_per_file_e_per_chiave():
    """Solo `book.txt`/`%DEFINE`: gli altri blocchi restano testo a righe."""
    assert dati.colonne_csv("book.txt", "DEFINE") == {"jp": 1, "en": 2}
    assert dati.colonne_csv("book.txt", "0") is None
    assert dati.colonne_csv("talk.txt", "DEFINE") is None
    assert dati.colonne_csv(None, "DEFINE") is None


def test_le_colonne_si_leggono_dove_le_legge_getstr():
    assert dati.campo_csv(RIGA, 0) == "20"
    assert dati.campo_csv(RIGA, 1) == "冒険暮らし"
    assert dati.campo_csv(RIGA, 2) == "Adventurers Quarterly Spring '18"
    assert dati.campo_csv(RIGA, 3) == "\t\t\t\t1"
    assert dati.campo_csv(RIGA, 9) == "", "una colonna che non c'e' non solleva"


def test_sostituire_una_colonna_lascia_le_altre_carattere_per_carattere():
    nuovo = dati.sostituisci_campo_csv(RIGA, 2, "L'avventuriero trimestrale")
    assert nuovo == ("20,冒険暮らし,"
                     "L'avventuriero trimestrale,\t\t\t\t1")
    # il numero del libro e il «1=generato a caso» sono dati del gioco
    assert dati.campo_csv(nuovo, 0) == "20"
    assert dati.campo_csv(nuovo, 3) == "\t\t\t\t1"


def test_la_virgola_nella_resa_si_rifiuta():
    """⚠️ Sposterebbe di uno tutti i campi dopo, e in silenzio."""
    with pytest.raises(ValueError, match="virgola"):
        dati.sostituisci_campo_csv(RIGA, 2, "Il trimestrale, primavera 518")


def test_la_tabulazione_e_il_campo_vuoto_si_rifiutano():
    with pytest.raises(ValueError, match="tabulazione"):
        dati.sostituisci_campo_csv(RIGA, 2, "Titolo\tcon tabulazione")
    # `getstr` esce dal giro appena `strsize == 0` (etc.hsp:322): un campo
    # vuoto fa sparire tutte le colonne che vengono dopo
    with pytest.raises(ValueError, match="vuota"):
        dati.sostituisci_campo_csv(RIGA, 2, "")


def test_il_define_del_file_vero_ha_trentatre_libri():
    """La misura sul corpus: se monte ne aggiunge uno, questo test lo dice."""
    from strumenti import percorsi
    percorso = percorsi.DATI_SORGENTE / "book.txt"
    if not percorso.exists():
        pytest.skip("book.txt non e' ancora stato pinnato")

    documento = dati.analizza_file("book.txt", dati.leggi(percorso))
    define = documento.blocco("DEFINE", "")
    assert define is not None
    righe = define.righe_piene()
    assert len(righe) == 33
    assert [dati.campo_csv(r, 0) for r in righe] == [str(n) for n in range(33)]
    assert dati.campo_csv(righe[0], 2) == "My Diary"
