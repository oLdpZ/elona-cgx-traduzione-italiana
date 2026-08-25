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
    assert problemi(voce(it="x" * 24 + ":corpo {reward}")) == []


def test_un_titolo_oltre_il_tetto_e_un_problema():
    assert "titolo largo" in problemi(voce(it="x" * 25 + ":corpo {reward}"))


def test_il_tetto_e_le_stellette_non_la_scadenza():
    # ⚠️ misurato a schermo nella 70a: le stellette del livello stanno a
    # wx+270 (command.hsp:3391) e si disegnano DOPO il titolo, mentre la
    # scadenza - il primo pos successivo leggendo il sorgente - sta a wx+344.
    # Col tetto sbagliato (34) un titolo da 25 passava e finiva sotto le stelle.
    assert dati_verifica.TETTO_TITOLO == 24
    assert "titolo largo" in problemi(voce(it="Un rinfresco coi fiocchi!:corpo {reward}"))


def test_il_titolo_si_misura_degradato():
    # «perche'» a schermo e' 7 caratteri, non 6: l'apostrofo e' un carattere
    ventiquattro = "perché" + "x" * 18          # 24 nel dizionario, 25 a schermo
    assert "titolo largo" in problemi(voce(it=ventiquattro + ":corpo {reward}"))


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


# ------------------------------------------------ l'accento e la degradazione

def test_un_accento_vero_non_e_un_problema():
    # nel lotto va «perché», non «perche'»: la degradazione la fa
    # l'applicazione, e la rete guarda quel che resta DOPO
    assert problemi(voce(it="Perché no:il corpo con {reward}.")) == []


def test_un_apostrofo_scritto_a_mano_e_un_problema():
    assert "apostrofo" in problemi(voce(it="Perche' no:il corpo con {reward}."))


def test_l_elisione_non_e_un_apostrofo_scritto_a_mano():
    assert problemi(voce(it="L'affare:un po' di {reward} per l'incarico.")) == []


# -------------------------------------------------------------- l'altezza

def test_senza_tetto_la_rete_dell_altezza_e_spenta():
    lunghissima = "T:" + "parola " * 60
    assert "altezza" not in problemi(voce(en="T:corto {reward}", it=lunghissima))


def test_una_resa_piu_alta_del_piu_lungo_di_monte_e_un_problema():
    lotto = [voce(en="A:" + "x " * 5, it="A:{reward}", blocco="A"),
             voce(en="B:" + "y " * 5, it="B:" + "parola " * 30, blocco="B")]
    generi = [p.genere for p in dati_verifica.controlla(lotto, tetto_a_capo=20)]
    assert "altezza" in generi


def test_il_tetto_dell_altezza_lo_fissa_la_riga_inglese_piu_lunga():
    # una resa alta quanto la piu' alta di monte passa: il tetto e' il corpus
    lungo = "parola " * 12
    lotto = [voce(en="A:" + lungo, it="A:" + lungo.replace("parola", "vocabo"), blocco="A")]
    assert dati_verifica.controlla(lotto, tetto_a_capo=20) == []


def test_i_segnaposto_non_si_espandono_per_contare_le_righe():
    # en e it hanno lo stesso insieme di segnaposto, quindi crescono uguale:
    # contare sul testo grezzo e' onesto e non chiede di indovinare l'oggetto
    assert dati_verifica.righe_del_corpo("T:{objective} e {reward}", 70) == 1


# ------------------------------------------------- il profilo per file

def test_ogni_file_ha_il_suo_espansore():
    # ⚠️ board.txt passa da talktxt_conv, talk.txt da convert_word, e NON
    # conoscono gli stessi nomi: {nptc} e {npcc} sono validi solo nel secondo
    assert dati_verifica.profilo("board.txt")["espansore"].nome == "talktxt_conv"
    assert dati_verifica.profilo("talk.txt")["espansore"].nome == "convert_word"
    assert "nptc" not in dati_verifica.TALKTXT_CONV.noti
    assert "nptc" in dati_verifica.CONVERT_WORD.contenuto


def test_in_talk_un_nptc_e_legittimo_e_in_board_no():
    di_talk = {"firma": "f", "file": "talk.txt", "blocco": "A", "riga": 1,
               "en": "Hello {nptc}.", "jp_contesto": [], "it": "Ciao {nptc}."}
    assert dati_verifica.controlla([di_talk]) == []
    di_board = dict(di_talk, file="board.txt", it="T:Ciao {nptc}.", en="T:Hello {nptc}.")
    generi = [p.genere for p in dati_verifica.controlla([di_board])]
    assert "segnaposto" in generi


def test_in_talk_non_si_chiede_il_due_punti():
    di_talk = {"firma": "f", "file": "talk.txt", "blocco": "A", "riga": 1,
               "en": "Nice weather today.", "jp_contesto": [], "it": "Che bel tempo oggi."}
    assert dati_verifica.controlla([di_talk]) == []


def test_i_codici_di_faccia_e_di_suono_si_conservano():
    di_talk = {"firma": "f", "file": "talk.txt", "blocco": "A", "riga": 1,
               "en": "{Happy}Hi!{seGet}", "jp_contesto": [], "it": "{Happy}Ciao!{seGet}"}
    assert dati_verifica.controlla([di_talk]) == []
    perso = dict(di_talk, it="{Happy}Ciao!")
    assert "segnaposto" in [p.genere for p in dati_verifica.controlla([perso])]


def test_la_rete_di_monte_girata_su_talk_non_trova_niente():
    # e col profilo sbagliato ne troverebbe uno: e' la prova che il profilo conta
    voce_talk = {"firma": "f", "file": "talk.txt", "blocco": "A", "riga": 1,
                 "en": "Hello {nptc}.", "jp_contesto": [], "it": ""}
    assert dati_verifica.segnaposto_ignoti_di_monte([voce_talk]) == []
    sbagliato = dati_verifica.segnaposto_ignoti_di_monte(
        [voce_talk], espansore=dati_verifica.TALKTXT_CONV)
    assert len(sbagliato) == 1


# ⚠️⚠️ `{you}` e `{me}` escono in giapponese anche nella build inglese: `_kimi`
# e `_ore` (text.hsp:5329 e :5851) non hanno nessun `lang()`. La resa italiana
# giusta e' quella che NON li porta, quindi il confronto li sottrae all'inglese.

def _voce_talk(en, it):
    return {"firma": "x", "file": "talk.txt", "blocco": "AAREA,30", "riga": 4,
            "en": en, "jp_contesto": [], "it": it}


def test_you_va_tolto_dalla_resa():
    voce = _voce_talk("We're almost out of food. {you}, share some.",
                      "Siamo quasi senza provviste: dividi le tue con noi.")
    assert dati_verifica.controlla([voce]) == []


def test_you_tenuto_nella_resa_e_un_problema():
    voce = _voce_talk("We're almost out of food. {you}, share some.",
                      "Siamo senza provviste. {you}, dividi le tue con noi.")
    problemi = dati_verifica.controlla([voce])
    assert len(problemi) == 1
    assert problemi[0].genere == "segnaposto"
    assert "you" in problemi[0].dettaglio


def test_gli_altri_segnaposto_restano_obbligatori():
    voce = _voce_talk("({nptc} looks at you.)", "(ti guarda.)")
    problemi = dati_verifica.controlla([voce])
    assert len(problemi) == 1
    assert "nptc" in problemi[0].dettaglio


def test_da_togliere_non_e_fra_gli_ammessi():
    assert "you" not in dati_verifica.CONVERT_WORD.ammessi()
    assert "me" not in dati_verifica.TALKTXT_CONV.ammessi()
    # ma restano NOTI: non devono essere segnalati come nomi sconosciuti
    assert "you" in dati_verifica.CONVERT_WORD.noti


# ⚠️ Tre nomi latini erano classificati male fino alla 71a. Il sito li separa:
#   {sex}     text.hsp:7057   lang("男", "boy")            -> contenuto
#   {onii}    text.hsp:7030   ramo else: "brother"/"sister" -> inglese nudo
#   {syujin}  text.hsp:7050   ramo else: "master"           -> inglese nudo

def test_sex_e_contenuto_non_una_conversione_giapponese():
    voce = _voce_talk("what a nice {sex} you are", "{sex} mi piace proprio")
    assert dati_verifica.controlla([voce]) == []
    assert "sex" in dati_verifica.CONVERT_WORD.ammessi()
    assert "sex" in dati_verifica.TALKTXT_CONV.ammessi()
    assert "sex" not in dati_verifica.CONVERT_WORD.giapponesi


def test_onii_e_syujin_sono_inglese_nudo_non_giapponese():
    for nome in ("onii", "syujin"):
        assert nome in dati_verifica.CONVERT_WORD.inglesi_nudi
        assert nome not in dati_verifica.CONVERT_WORD.giapponesi
        assert nome not in dati_verifica.CONVERT_WORD.ammessi()
        # restano NOTI: il messaggio giusto e' «esce in inglese», non
        # «l'espansore non lo conosce»
        assert nome in dati_verifica.CONVERT_WORD.noti


def test_onii_nella_resa_segnalato_come_inglese():
    voce = _voce_talk("Hey {player}!", "Ehi {player}, {onii}!")
    problemi = dati_verifica.controlla([voce])
    generi = [p.genere for p in problemi]
    assert generi.count("segnaposto") >= 1
    assert any("inglese" in p.dettaglio for p in problemi)


def test_le_conversioni_giapponesi_restano_segnalate():
    voce = _voce_talk("Hey {player}!", "Ehi {player}{だ}!")
    problemi = dati_verifica.controlla([voce])
    assert any("giapponesi" in p.dettaglio for p in problemi)


# ------------------------------------------------------- il profilo di exhelp
#
# ⚠️⚠️ `exhelp.txt` non passa da nessun espansore: `help.hsp:227` lo carica con
# `noteload` e `:273` lo disegna con `gmes`, che di graffe non sa niente. E non
# e' `titolo:corpo`: i due punti dentro le frasi sono prosa. Senza un profilo
# suo cadrebbe nel PROFILO_IGNOTO, che e' quello di `board.txt` — e una rete
# giusta puntata sul file sbagliato non tace, mente.

def _voce_exhelp(en, it):
    return {"firma": "x", "file": "exhelp.txt", "blocco": "1", "riga": 1,
            "en": en, "jp_contesto": [], "it": it}


def test_exhelp_non_vuole_i_due_punti():
    voce = _voce_exhelp("Here's my first tip for you.",
                        "Ecco il mio primo consiglio.")
    assert dati_verifica.controlla([voce]) == []


def test_exhelp_coi_due_punti_nella_prosa_non_e_un_titolo():
    # su `board.txt` questo scatterebbe come «titolo largo»: 30 caratteri
    # davanti ai due punti contro un tetto di 24
    # ⚠️ l'accento vero, non «e'»: la degradazione la fa `dati_applica`, e la
    # rete dell'apostrofo scritto a mano scatta prima di questa
    voce = _voce_exhelp("Use your home as a safe storage since the items",
                        "Casa tua è un magazzino sicuro: quello che")
    assert dati_verifica.controlla([voce]) == []


def test_exhelp_una_graffa_qualsiasi_resterebbe_a_schermo():
    # nemmeno le conversioni giapponesi le mangia nessuno, qui
    for graffa in ("{reward}", "{だ}", "{you}"):
        voce = _voce_exhelp("Just ask the innkeepers.", f"Chiedilo al banco {graffa}.")
        problemi = dati_verifica.controlla([voce])
        assert any("resterebbero fra graffe" in p.dettaglio for p in problemi), graffa


def test_exhelp_ha_la_rete_dell_altezza_spenta_apposta():
    # il tetto vero e' in scratchpad/_98-exhelp-gmes.py: `gmes` manda a capo per
    # carattere e salta i marcatori, `righe_a_capo` fa l'opposto in tutt'e due
    assert dati_verifica.PROFILI["exhelp.txt"]["tetto_capo"] is None
    assert dati_verifica.PROFILI["exhelp.txt"]["titolo"] is False
