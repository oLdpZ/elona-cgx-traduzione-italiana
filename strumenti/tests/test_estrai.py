# strumenti/tests/test_estrai.py
from strumenti.estrai import (
    _argomenti, _letterali, avvii, e_dinamica, estrai_da_testo, firma,
    normalizza_espressione, siti, spezza_righe,
)

STATICA = '#define global txt_invfull txt lang("バックパックが一杯だ。", "Your inventory is full.")'
DINAMICA = '#define global txt_guard txt lang(name(tc) + "は" + name(x) + "をかばった！", name(tc) + " guarded " + name(x) + ".")'
DUE_SULLA_STESSA_RIGA = 'a = lang("はい", "Yes"), lang("いいえ", "No")'


def test_estrae_una_statica():
    voci = estrai_da_testo("text.hsp", STATICA)
    assert len(voci) == 1
    voce = voci[0]
    assert voce["jp"] == "バックパックが一杯だ。"
    assert voce["en"] == "Your inventory is full."
    assert voce["tipo"] == "statica"
    assert voce["it"] == ""
    assert voce["file"] == "text.hsp"
    assert voce["riga"] == 1


def test_riconosce_una_dinamica_e_ne_conserva_il_contesto():
    voci = estrai_da_testo("text.hsp", DINAMICA)
    assert len(voci) == 1
    assert voci[0]["tipo"] == "dinamica"
    assert voci[0]["contesto"] == DINAMICA


def test_conserva_l_espressione_grezza():
    # per le dinamiche si traduce l'espressione intera, non i soli letterali:
    # in italiano l'ordine dei pezzi cambia
    voce = estrai_da_testo("text.hsp", DINAMICA)[0]
    assert voce["en_grezzo"] == 'name(tc) + " guarded " + name(x) + "."'
    assert voce["en"] == " guarded ."

    statica = estrai_da_testo("text.hsp", STATICA)[0]
    assert statica["en_grezzo"] == '"Your inventory is full."'
    assert statica["en"] == "Your inventory is full."


def test_le_statiche_non_portano_contesto():
    assert estrai_da_testo("text.hsp", STATICA)[0]["contesto"] == ""


def test_estrae_piu_occorrenze_dalla_stessa_riga():
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    assert [v["en"] for v in voci] == ["Yes", "No"]


def test_le_firme_sono_stabili_e_distinte():
    assert firma("はい", "Yes") == firma("はい", "Yes")
    assert firma("はい", "Yes") != firma("はい", "No")
    assert firma("いいえ", "Yes") != firma("はい", "Yes")


def test_i_duplicati_esatti_si_distinguono_per_occorrenza():
    testo = 'a = lang("はい", "Yes")\nb = lang("はい", "Yes")'
    voci = estrai_da_testo("text.hsp", testo)
    assert len(voci) == 2
    assert voci[0]["occorrenza"] == 0
    assert voci[1]["occorrenza"] == 1
    assert voci[0]["firma"] == voci[1]["firma"]


def test_e_dinamica_distingue_concatenazioni():
    assert e_dinamica('"Your inventory is full."') is False
    assert e_dinamica('name(tc) + " guarded " + name(x) + "."') is True
    assert e_dinamica('"You create " + itemname(ci, 1) + "!"') is True


def test_ignora_le_righe_senza_lang():
    assert estrai_da_testo("text.hsp", "	sdim bodyn, 4, 15") == []


def test_ignora_le_stringhe_con_inglese_vuoto():
    # particelle giapponesi che in inglese non esistono: niente da tradurre.
    # In text.hsp sono 6 casi reali, es. lang("層", "")
    assert estrai_da_testo("text.hsp", 'buff += lang("残り", "")') == []


# --- escape \" nei letterali (revisione finale, rilievo CRITICAL 1) -----------
# Nel sorgente HSP \" e' una virgoletta dentro un letterale. Il parser che
# faceva toggle su ogni virgoletta scartava 11 lang(), sbagliava 5 span e
# mutilava 295 voci. La riga qui sotto e' db_creature.hsp:50728, ridotta.

RIGA_CON_ESCAPE = (
    '\t\t\ttxt lang("「なに？", "\\"Oh, my ") + _onii(cdata(CDATA_SEX, CHARA_PLAYER))'
    ' + lang("さんも味わいたいの？」", " want to taste it too?\\"")'
)


def test_l_escape_non_chiude_il_letterale():
    voci = estrai_da_testo("db_creature.hsp", RIGA_CON_ESCAPE)
    assert [v["en"] for v in voci] == ['\\"Oh, my ', ' want to taste it too?\\"']


def test_lo_span_non_inghiotte_il_codice_fra_due_lang():
    # il difetto grave: lo span del secondo argomento arrivava fino alla
    # virgoletta successiva, e applica.py sostituendolo faceva sparire dal
    # sorgente sia _onii(...) sia l'intera coppia lang() seguente.
    elenco = list(siti(RIGA_CON_ESCAPE))
    assert len(elenco) == 2
    _, _, _, _, _, _, grezzo_en, inizio, fine = elenco[0]
    assert RIGA_CON_ESCAPE[inizio:fine] == grezzo_en
    assert "_onii" not in grezzo_en
    assert "lang(" not in grezzo_en


def test_un_lang_dentro_un_letterale_non_e_un_sito():
    # 'lang(' che compare dentro una stringa e' testo, non codice
    riga = 'txt lang("説明: lang(a, b) と書く", "write lang(a, b) here")'
    assert len(avvii(riga)) == 1
    voci = estrai_da_testo("text.hsp", riga)
    assert len(voci) == 1
    assert voci[0]["en"] == "write lang(a, b) here"


def test_letterali_onora_gli_escape():
    assert _letterali('"say \\"hi\\" now"') == 'say \\"hi\\" now'
    assert _letterali('"a" + f() + "b"') == "ab"
    # il backslash raddoppiato non si mangia la virgoletta di chiusura
    assert _letterali('"finisce con \\\\" + x') == "finisce con \\\\"


def test_argomenti_non_si_ferma_su_una_parentesi_dentro_un_letterale():
    riga = 'lang("jp)", "en)")'
    assert _argomenti(riga, 4) == ('"jp)"', '"en)"', 12, 17)
    assert riga[12:17] == '"en)"'


# --- il + va cercato fuori dai letterali (rilievo CRITICAL 2) ----------------

def test_un_piu_dentro_il_testo_non_rende_dinamica_la_stringa():
    # 163 stringhe reali contengono un + nel testo. Classificarle dinamiche
    # fa finire l'italiano nudo, senza virgolette, nel sorgente HSP.
    assert e_dinamica('"Enchantment Bonus + 4"') is False
    assert e_dinamica('"RES+ magic"') is False
    voce = estrai_da_testo("trait.hsp", 'txt lang("jp", "Enchantment Bonus + 4")')[0]
    assert voce["tipo"] == "statica"


def test_un_piu_di_concatenazione_resta_dinamico():
    assert e_dinamica('"Bonus + " + str(n)') is True
    assert e_dinamica('name(tc) + " guarded " + name(x) + "."') is True


# --- fine riga: split() sul terminatore, mai splitlines() -------------------

def test_le_righe_si_spezzano_solo_sul_terminatore_effettivo():
    # \x0c e U+2028 sono fine riga per splitlines() ma non per il file:
    # spezzarli sfalserebbe i numeri di riga rispetto al sorgente reale.
    testo = 'a = lang("jp", "en1")\x0c ancora\r\nb = lang("jp2", "en2")\r\n'
    righe, fine_riga, coda = spezza_righe(testo)
    assert fine_riga == "\r\n"
    assert coda is True
    assert len(righe) == 2
    assert [v["riga"] for v in estrai_da_testo("text.hsp", testo)] == [1, 2]


# --- la firma: cosa vi entra e cosa no (SPEC 3.2) ----------------------------

QUI = 'name(gdata(GDATA_RIDER)) + " glare"'
ALTROVE = 'cdatan(CDATAN_NAME, ttc) + " glare"'


def test_senza_espressione_la_firma_e_quella_dei_soli_letterali():
    # e' il caso delle statiche: l'involucro non entra nella chiave
    assert firma("jp", "en") == firma("jp", "en", None)


def test_l_espressione_cambia_la_firma():
    assert firma("jp", " glare", QUI) != firma("jp", " glare")


def test_due_espressioni_diverse_con_gli_stessi_letterali_hanno_firme_diverse():
    # erano 77 firme collidenti: la traduzione dell'una finiva sull'altra
    # portandosi le variabili sbagliate
    assert firma("jp", " glare", QUI) != firma("jp", " glare", ALTROVE)


def test_gli_spazi_non_contano_nella_firma():
    # reindentare a monte non deve mandare la stringa in coda di ritraduzione
    assert firma("jp", " glare", QUI) == firma("jp", " glare", QUI.replace(" + ", "\t+  "))


def test_normalizza_riduce_ogni_sequenza_di_spazi_a_uno():
    assert normalizza_espressione('  a  +\t\t"b"  ') == 'a + "b"'


def test_una_dinamica_del_sorgente_porta_l_espressione_nella_chiave():
    voce = estrai_da_testo("proc.hsp", DINAMICA)[0]
    assert voce["tipo"] == "dinamica"
    assert voce["firma"] == firma(voce["jp"], voce["en"], voce["en_grezzo"])
    assert voce["firma"] != firma(voce["jp"], voce["en"])


def test_una_statica_del_sorgente_non_la_porta():
    voce = estrai_da_testo("text.hsp", STATICA)[0]
    assert voce["tipo"] == "statica"
    assert voce["firma"] == firma(voce["jp"], voce["en"])


# --- il lavoro che resta (--da-tradurre, Task 7) -----------------------------

def test_da_tradurre_tiene_una_voce_per_firma():
    # estrai emette una voce per OCCORRENZA, perche' prova_identita e verifica
    # devono attraversare tutti i siti. Ma tradurre si conta in firme: il
    # dizionario e' indicizzato cosi', e una stringa che compare tre volte e'
    # una voce da tradurre e tre sostituzioni in fase di build
    from strumenti.estrai import da_tradurre
    voci = estrai_da_testo("text.hsp", 'a = lang("はい", "Yes")\nb = lang("はい", "Yes")')
    assert len(voci) == 2
    resta = da_tradurre(voci, gia_tradotte=set())
    assert len(resta) == 1
    assert resta[0]["en"] == "Yes"


def test_da_tradurre_esclude_le_firme_gia_tradotte():
    from strumenti.estrai import da_tradurre
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    assert len(voci) == 2
    fatta = voci[0]["firma"]
    resta = da_tradurre(voci, gia_tradotte={fatta})
    assert [v["en"] for v in resta] == ["No"]


def test_da_tradurre_conserva_l_ordine_del_sorgente():
    # i lotti si leggono in ordine di file: saltare avanti e indietro fa
    # perdere il contesto, che per le dinamiche e' l'unica cosa che c'e'
    from strumenti.estrai import da_tradurre
    testo = 'a = lang("いち", "One")\nb = lang("に", "Two")\nc = lang("さん", "Three")'
    resta = da_tradurre(estrai_da_testo("text.hsp", testo), gia_tradotte=set())
    assert [v["en"] for v in resta] == ["One", "Two", "Three"]


def test_da_tradurre_su_un_lotto_gia_finito_non_ritorna_niente():
    from strumenti.estrai import da_tradurre
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    assert da_tradurre(voci, gia_tradotte={v["firma"] for v in voci}) == []


def test_da_tradurre_salta_anche_le_rinviate():
    # una voce rinviata a una fase successiva non e' tradotta e non lo sara' in
    # questa fase: senza saltarla tornerebbe in testa a ogni estrazione, e
    # andrebbe riscartata a mano ogni volta
    from strumenti.estrai import da_tradurre
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    rinviata = voci[0]["firma"]
    resta = da_tradurre(voci, gia_tradotte=set(), rinviate={rinviata})
    assert [v["en"] for v in resta] == ["No"]


def test_le_rinviate_vogliono_un_motivo(tmp_path):
    # stessa regola delle toppe: una riga senza motivo e' un pezzo di lavoro
    # saltato di cui fra sei mesi nessuno sa il perche'
    import json, pytest
    from strumenti.estrai import carica_rinviate
    percorso = tmp_path / "rinviate.jsonl"
    percorso.write_text(json.dumps({"firma": "abc", "file": "text.hsp", "en": "x"}) + "\n",
                        encoding="utf-8")
    with pytest.raises(ValueError) as errore:
        carica_rinviate(percorso)
    assert "motivo" in str(errore.value)


def test_carica_rinviate_senza_file_non_rompe_niente(tmp_path):
    from strumenti.estrai import carica_rinviate
    assert carica_rinviate(tmp_path / "assente.jsonl") == set()


# --- il rinvio vale per il file che l'ha deciso (2026-08-08) -----------------
#
# `rinviate.jsonl` era indicizzato per **firma**, e la firma e' contenuto: non
# porta il file. Le 157 voci rinviate di `text.hsp` — risposte del quiz e nomi
# casuali — hanno per costruzione lo stesso contenuto dei nomi veri, e cosi'
# **15 nomi di `db_item.hsp` sparivano da ogni lotto**: `ring`, `lemon`,
# `strawberry`, `cherry`, `gold bar`, `broken sword`, `flag`, `earth crystal`...
#
# Non c'era nessun accoppiamento vero da rispettare: i dizionari sono per file
# (`dizionario/text.hsp.jsonl`, `dizionario/db_item.hsp.jsonl`), quindi tradurre
# il nome in `db_item` non tocca la risposta del quiz in `text.hsp`. Era solo
# una decisione presa su un file che toglieva lavoro alla coda di un altro, in
# silenzio e per sempre — la coda non si sarebbe mai svuotata e nessuno avrebbe
# saputo perche'.

def test_una_rinviata_di_un_file_non_toglie_lavoro_a_un_altro(tmp_path):
    import json
    from strumenti.estrai import carica_rinviate

    percorso = tmp_path / "rinviate.jsonl"
    percorso.write_text(json.dumps({
        "firma": "abc", "file": "text.hsp", "en": "gold bar",
        "motivo": "risposta del quiz, dipende dai nomi degli oggetti",
        "condizione": {"tipo": "attende_resa", "siti": ["db_item.hsp:1"]},
    }, ensure_ascii=False) + "\n", encoding="utf-8")

    assert carica_rinviate(percorso, "text.hsp") == {"abc"}
    assert carica_rinviate(percorso, "db_item.hsp") == set()


def test_senza_file_le_rinviate_si_leggono_tutte(tmp_path):
    # il comportamento storico resta disponibile: serve a chi vuole l'elenco
    # intero, per esempio per contarle
    import json
    from strumenti.estrai import carica_rinviate

    percorso = tmp_path / "rinviate.jsonl"
    percorso.write_text(json.dumps({
        "firma": "abc", "file": "text.hsp", "en": "x", "motivo": "y",
        "condizione": {"tipo": "riga_morta"},
    }) + "\n", encoding="utf-8")
    assert carica_rinviate(percorso) == {"abc"}


# --- la condizione e' un campo, non una frase (2026-09-02, 129a) -------------
#
# Nella 128a tre rinvii dicevano in prosa «va tradotta INSIEME a chi assegna il
# nome della mappa, non prima». Chi assegna e' stato tradotto in una sessione
# qualunque, e nessuno e' tornato a leggere il rinvio: **quattro rami del gioco
# erano morti** — il ballo nella sala delle feste durava 4 turni invece di 41.
#
# Il `motivo` resta obbligatorio per chi legge; `condizione.tipo` e'
# obbligatorio perche' qualcosa possa **misurare** se il rinvio e' scaduto.

def test_le_rinviate_vogliono_una_condizione(tmp_path):
    import json, pytest
    from strumenti.estrai import carica_rinviate
    percorso = tmp_path / "rinviate.jsonl"
    percorso.write_text(json.dumps({
        "firma": "abc", "file": "text.hsp", "en": "x",
        "motivo": "va tradotta INSIEME a map_rand.hsp: non prima",
    }) + "\n", encoding="utf-8")
    with pytest.raises(ValueError) as errore:
        carica_rinviate(percorso)
    assert "condizione" in str(errore.value)


def test_una_condizione_con_un_tipo_inventato_non_passa(tmp_path):
    # un tipo fuori vocabolario e' peggio di un campo assente: sembra
    # classificato, e nessun referto lo misura
    import json, pytest
    from strumenti.estrai import carica_rinviate
    percorso = tmp_path / "rinviate.jsonl"
    percorso.write_text(json.dumps({
        "firma": "abc", "file": "text.hsp", "en": "x", "motivo": "y",
        "condizione": {"tipo": "quando sara' il momento"},
    }, ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(ValueError) as errore:
        carica_rinviate(percorso)
    assert "tipo" in str(errore.value)


def test_i_nomi_di_db_item_non_sono_rinviati_da_text():
    # la rete di sicurezza sul file vero: se domani qualcuno rinvia una voce di
    # `text.hsp` che ha lo stesso contenuto di un nome, il nome deve restare
    # nella coda di `db_item.hsp`
    #
    # ⚠️ 2026-08-09. Qui c'era `== set()`: una **procura**, che reggeva solo
    # finche' `db_item.hsp` non aveva nessun rinvio suo. `<Pants of Ogre>` e' il
    # primo — il nome contiene `ogre`, e quale creatura si prenda «orco» e' una
    # decisione di Fase 2 — e la procura si e' rotta pur restando vera la
    # proprieta' che il test difende. Adesso la proprieta' e' scritta com'e':
    # ogni firma che esce per `db_item.hsp` viene da una riga **di**
    # `db_item.hsp`, mai da un altro file.
    import json

    from strumenti.estrai import carica_rinviate
    from strumenti.percorsi import PROGETTO

    percorso = PROGETTO / "rinviate.jsonl"
    if not percorso.exists():
        return

    righe = [
        json.loads(riga)
        for riga in percorso.read_text(encoding="utf-8").splitlines()
        if riga.strip()
    ]
    proprie = {r["firma"] for r in righe if r["file"] == "db_item.hsp"}
    assert carica_rinviate(None, "db_item.hsp") <= proprie
