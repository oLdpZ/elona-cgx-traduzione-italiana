# strumenti/tests/test_dati_verifica.py
"""Le reti di un lotto di file dati.

Ognuna nasce da un sito preciso, non da una prudenza generica:

    segnaposto   text.hsp:11922 *talktxt_conv sostituisce solo i nomi che
                 conosce; uno inventato resta a schermo fra graffe. E la
                 famiglia grammaticale giapponese ({だ}, {のだ}, {くれ}...) in
                 italiano non deve comparire mai.
    due punti    text.hsp:11656 spacca la riga al PRIMO due punti: davanti il
                 titolo dell'incarico, dietro il corpo.
    titolo largo command.hsp:3357 disegna il titolo a wx+100 (module.hsp:129:
                 arg2 + 4 + arg5) con font corpo 12, cioe' 7 px per carattere;
                 la scadenza gli sta davanti a wx+344. 244 px, 34 caratteri.
    struttura    dati.py rifiuta a-capo e percento, ma il lotto va fermato
                 prima di arrivarci: l'errore si legge meglio col numero di
                 riga del lotto accanto.
    doppi byte   la regola di ogni lotto (accenti.doppi_byte_cp932).
    identica     una resa uguale all'inglese e' quasi sempre una dimenticanza.

⚠️ Il tetto si misura sulla forma **degradata**: «perché» sta in 6 caratteri nel
dizionario e in 7 a schermo (64a).
"""
import pytest

from strumenti import dati_verifica


def voce(en="Titolo:corpo {reward}.", it="", jp=None, blocco="A", riga=1):
    return {"firma": "f" * 40, "file": "board.txt", "blocco": blocco, "riga": riga,
            "en": en, "jp_contesto": jp if jp is not None else ["giapponese:{reward}"],
            "it": it}


def problemi(v):
    return [p.genere for p in dati_verifica.controlla([v])]


# ------------------------------------------------------------- segnaposto

def test_una_resa_che_conserva_i_segnaposto_passa():
    assert problemi(voce(it="Titolo:il corpo, con {reward}.")) == []


def test_un_segnaposto_perso_e_un_problema():
    assert "segnaposto" in problemi(voce(it="Titolo:corpo senza niente."))


def test_un_segnaposto_aggiunto_e_un_problema():
    assert "segnaposto" in problemi(voce(it="Titolo:corpo {reward} da {client}."))


def test_un_segnaposto_inventato_e_un_problema():
    # talktxt_conv non lo conosce: resterebbe a schermo fra graffe
    v = voce(en="Titolo:corpo {reward}.", it="Titolo:corpo {ricompensa}.")
    assert "segnaposto" in problemi(v)


def test_un_codice_grammaticale_giapponese_nella_resa_e_un_problema():
    v = voce(en="Titolo:corpo {reward}.", it="Titolo:corpo {reward}{のだ}.")
    assert "segnaposto" in problemi(v)


def test_i_segnaposto_si_possono_riordinare():
    v = voce(en="Titolo:{objective} per {reward}.", it="Titolo:per {reward} vuole {objective}.")
    assert problemi(v) == []


def test_lo_stesso_segnaposto_due_volte_conta_due_volte():
    v = voce(en="Titolo:{reward} e {reward}.", it="Titolo:solo {reward}.")
    assert "segnaposto" in problemi(v)


# -------------------------------------------------------------- due punti

def test_una_resa_senza_due_punti_e_un_problema():
    assert "due punti" in problemi(voce(it="Titolo corpo {reward}"))


def test_una_resa_col_titolo_vuoto_e_un_problema():
    assert "due punti" in problemi(voce(it=":corpo {reward}"))


def test_un_secondo_due_punti_nel_corpo_va_bene():
    # il gioco spacca al primo: quelli dopo restano nel corpo
    assert problemi(voce(it="Titolo:ecco: corpo {reward}")) == []


# ----------------------------------------------------------- il titolo largo

def test_un_titolo_lungo_ma_dentro_il_tetto_passa():
    assert problemi(voce(it="x" * 34 + ":corpo {reward}")) == []


def test_un_titolo_oltre_il_tetto_e_un_problema():
    assert "titolo largo" in problemi(voce(it="x" * 35 + ":corpo {reward}"))


def test_il_titolo_si_misura_degradato():
    # «perche'» a schermo e' 7 caratteri, non 6: l'apostrofo e' un carattere
    trentaquattro = "perché" + "x" * 28          # 34 nel dizionario, 35 a schermo
    assert "titolo largo" in problemi(voce(it=trentaquattro + ":corpo {reward}"))


# ------------------------------------------------------------- la struttura

def test_una_resa_con_un_a_capo_e_un_problema():
    assert "struttura" in problemi(voce(it="Titolo:corpo {reward}\naltro"))


def test_una_resa_che_comincia_per_percento_e_un_problema():
    assert "struttura" in problemi(voce(it="%END:corpo {reward}"))


def test_una_resa_vuota_non_e_un_problema_e_solo_da_fare():
    assert problemi(voce(it="")) == []


# ------------------------------------------------------- gli altri controlli

def test_un_doppio_byte_cp932_e_un_problema():
    # U+2015 CP932 lo codifica su DUE byte, e la build inglese disegna un glifo
    # per byte: a schermo escono due caratteri sbagliati
    assert "doppi byte" in problemi(voce(it="Titolo:corpo ― {reward}"))


def test_un_carattere_che_cp932_non_sa_codificare_e_un_problema():
    # ⚠️ il trattino lungo che si scrive per abitudine e' U+2014, e CP932 non lo
    # codifica AFFATTO: e' un'altra famiglia, e serve l'altro controllo.
    # Le virgolette caporali sono nella stessa famiglia.
    assert "fuori cp932" in problemi(voce(it="Titolo:corpo — {reward}"))
    assert "fuori cp932" in problemi(voce(it="Titolo:corpo «{reward}»"))


def test_una_resa_identica_all_inglese_e_un_problema():
    v = voce(en="Titolo:corpo {reward}.", it="Titolo:corpo {reward}.")
    assert "identica" in problemi(v)


def test_una_resa_identica_dichiarata_invariata_non_e_un_problema():
    v = voce(en="Titolo:corpo {reward}.", it="Titolo:corpo {reward}.")
    assert dati_verifica.controlla([v], invariati={v["en"]}) == []


# ------------------------------------------------------------ il referto

def test_il_referto_porta_blocco_e_riga():
    (problema,) = dati_verifica.controlla([voce(it="Titolo corpo {reward}", blocco="COOK,1", riga=2)])
    assert problema.blocco == "COOK,1"
    assert problema.riga == 2
    assert "due punti" == problema.genere


def test_un_lotto_pulito_non_da_problemi():
    lotto = [voce(it="Uno:corpo {reward}", blocco="A"),
             voce(it="Due:altro {reward}", blocco="B")]
    assert dati_verifica.controlla(lotto) == []


# ------------------------------------------------- il conto delle righe a capo

def test_il_corpo_si_manda_a_capo_come_fa_talk_conv():
    # talk_conv nel ramo non giapponese spezza sulle spaziature (init.hsp:1326),
    # e conta ogni parola INSIEME allo spazio che la segue: "uno " e' 4, e
    # aggiungere "due " farebbe 8, che sfora il tetto di 7
    assert dati_verifica.righe_a_capo("uno due tre", 7) == ["uno ", "due tre"]


def test_l_ultimo_pezzo_si_appende_senza_controllo():
    # dopo l'ultima spaziatura non c'e' nessun controllo (init.hsp:1368): la
    # coda si appende alla riga corrente per lunga che sia, e non manda a capo
    assert dati_verifica.righe_a_capo("uno tre-lunghissima-parola", 7) == [
        "uno tre-lunghissima-parola"]


def test_una_parola_piu_lunga_del_tetto_manda_a_capo_mille_volte():
    # ⚠️ difetto di monte, riprodotto apposta: se la prima parola con lo spazio
    # dietro sfora il tetto, il ciclo esterno non consuma niente e va avanti
    # fino alle sue mille iterazioni. Al tetto di board (70) non si raggiunge;
    # a `talk_conv s, 32` (command.hsp:10540) una parola italiana lunga si'.
    righe = dati_verifica.righe_a_capo("incomprensibilmente si", 8)
    assert len(righe) == 1001
    assert righe[:3] == ["", "", ""]
    assert righe[-1] == "incomprensibilmente si"
