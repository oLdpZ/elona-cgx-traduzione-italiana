# strumenti/tests/test_toppe.py
"""Le toppe: le sostituzioni fuori da `lang()`, che il dizionario non raggiunge."""
import json

import pytest

from strumenti import percorsi
from strumenti.applica import (SorgenteCorrotto, applica_toppe, carica_toppe,
                               letterali_di_lang, righe_di_toppa)

RIGA_NAME = '\t\treturn "the " + cdatan(CDATAN_NAME, name_arg1)'


def toppa(**sovrascritture):
    base = {
        "file": "init.hsp",
        "cerca": RIGA_NAME,
        "sostituisci": '\t\treturn cdatan(CDATAN_NAME, name_arg1)',
        "motivo": "prova",
    }
    base.update(sovrascritture)
    return base


def sorgente(*righe):
    return "\r\n".join(righe) + "\r\n"


def test_una_toppa_sostituisce_la_riga_esatta():
    testo = sorgente("#defcfunc name int name_arg1", RIGA_NAME, "\treturn 0")
    nuovo, quante = applica_toppe("init.hsp", testo, [toppa()])
    assert quante == 1
    assert '"the "' not in nuovo
    assert "return cdatan(CDATAN_NAME, name_arg1)" in nuovo
    # il resto del file non si tocca, terminatori compresi
    assert nuovo.startswith("#defcfunc name int name_arg1\r\n")
    assert nuovo.endswith("\treturn 0\r\n")


def test_una_toppa_per_un_altro_file_non_si_applica():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("text.hsp", testo, [toppa()])
    assert quante == 0
    assert nuovo == testo


def test_una_riga_che_non_c_e_piu_ferma_la_catena():
    # e' il caso del riallineamento a una nuova versione CGX (SPEC 3.1): se
    # upstream ha riscritto quella riga, applicare la toppa alla cieca non ha
    # senso. Meglio fermarsi e rifarla che produrre un eseguibile diverso da
    # quello che si crede.
    testo = sorgente("#defcfunc name int name_arg1", "\treturn 0")
    with pytest.raises(SorgenteCorrotto, match="non esiste"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_riga_ambigua_ferma_la_catena():
    # due righe identiche: quale delle due? Indovinare significa avere una
    # probabilita' su due di toppare quella sbagliata, in silenzio.
    testo = sorgente(RIGA_NAME, "\tx = 1", RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="due volte|2 volte|piu' di una"):
        applica_toppe("init.hsp", testo, [toppa()])


def test_una_toppa_che_non_cambia_niente_e_un_errore():
    # cerca == sostituisci e' quasi sempre un refuso, e resterebbe muta
    testo = sorgente(RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="identica"):
        applica_toppe("init.hsp", testo, [toppa(sostituisci=RIGA_NAME)])


def test_senza_toppe_il_testo_non_si_tocca():
    testo = sorgente(RIGA_NAME)
    nuovo, quante = applica_toppe("init.hsp", testo, [])
    assert quante == 0
    assert nuovo == testo


def test_carica_toppe_legge_il_jsonl(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa(), ensure_ascii=False) + "\n", encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert len(caricate) == 1
    assert caricate[0]["file"] == "init.hsp"


def test_senza_il_file_non_si_rompe_niente(tmp_path):
    assert carica_toppe(tmp_path / "assente.jsonl") == []


def test_ogni_toppa_deve_avere_un_motivo(tmp_path):
    # una toppa senza motivo e' una modifica al sorgente di cui fra sei mesi
    # nessuno sa piu' il perche'
    percorso = tmp_path / "toppe.jsonl"
    voce = toppa()
    del voce["motivo"]
    percorso.write_text(json.dumps(voce, ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="motivo"):
        carica_toppe(percorso)


# --- il file vero, contro il sorgente vero ----------------------------------

def test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato():
    """La prova che conta: ogni toppa trova la sua riga, una volta sola.

    Se upstream cambia una di quelle righe, questo test diventa rosso prima che
    la build produca qualcosa di sbagliato.
    """
    toppe = carica_toppe()
    assert toppe, "toppe.jsonl e' vuoto: se non serve piu', va tolto il file"
    for t in toppe:
        percorso = percorsi.SORGENTE_HSP / t["file"]
        assert percorso.exists(), f"{t['file']} non esiste nel sorgente"
        testo = percorso.read_bytes().decode("cp932")
        nuovo, quante = applica_toppe(t["file"], testo, [t])
        assert quante == 1
        assert nuovo != testo


def test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere():
    """Ogni toppa deve poter essere scritta nell'albero di build.

    Le toppe sono l'unica strada per cui un testo italiano arriva al sorgente
    **senza passare da `applica.py`**, che degrada gli accenti a ogni punto in
    cui un dato del dizionario diventa codice. Una toppa che porti una vocale
    accentata vera fa esplodere la scrittura del file — «bambù», 2026-08-09 —
    e lo fa in fondo alla catena, dopo che tutto il resto e' gia' andato bene.

    Qui si rompe subito, e per tutte le toppe: quella che c'e' oggi e quella
    che qualcuno scrivera' domani.
    """
    for t in carica_toppe():
        for chiave in ("cerca", "sostituisci"):
            for riga in righe_di_toppa(t[chiave]):
                try:
                    riga.encode("cp932")
                except UnicodeEncodeError as e:
                    raise AssertionError(
                        f"la toppa «{t['motivo'][:50]}…» porta in `{chiave}` un "
                        f"carattere che CP932 non ha: {riga[e.start:e.end]!r}. "
                        "Va degradato con accenti.degrada() da chi genera la "
                        f"toppa.\n  {riga.strip()}") from None


# I caratteri che `scratchpad/guardie.py` rifiuta da sempre nelle voci di
# dizionario. L'elenco si tiene qui uguale a quello: due reti che cercano la
# stessa cosa con due elenchi diversi sono due numeri incomparabili, ed e' la
# lezione che `_126-referti-toppe.py` ha gia' scritto per i participi.
PROIBITI_ITALIANI = "…“”～«»"

# Gli intervalli del giapponese: kana (hiragana + katakana) e kanji.
_GIAPPONESE = (("぀", "ヿ"), ("一", "鿿"))


def _ha_giapponese(riga: str) -> bool:
    return any(a <= c <= b for c in riga for a, b in _GIAPPONESE)


def proibiti_in_italiano(riga: str) -> list[str]:
    """I caratteri proibiti che la riga scrive, se la riga e' italiana.

    Una riga che contiene kana o kanji e' il ramo `if ( jp )` che una toppa a
    blocco si porta dietro: li' `…` e 《 》 sono scritti giusti, e non sono roba
    nostra. Ritorna una lista ordinata, cosi' il messaggio d'errore e' stabile.
    """
    if _ha_giapponese(riga):
        return []
    return sorted({c for c in riga if c in PROIBITI_ITALIANI})


def test_nessuna_toppa_scrive_in_italiano_un_carattere_a_doppia_larghezza():
    """I caratteri proibiti nel dizionario sono proibiti anche nelle toppe.

    ⚠️ **La rete qui sopra non basta, e per otto sessioni non e' bastata.**
    `…` (U+2026) in CP932 esiste — e' 0x81 0x63 — quindi `encode("cp932")` non
    solleva e quella prova resta verde. Ma e' un carattere a **doppia
    larghezza**, e il ramo che la build italiana esegue disegna col carattere
    latino dichiarato in `config.txt` (`font2. "Courier New"`): i due byte
    diventano due glifi latini a caso. E' la stessa ragione per cui
    `invariati.md` tiene 《 》 e 【 】 fuori dalle rese.

    Il progetto lo sapeva: `…` sta in cima all'elenco `PROIBITI` di
    `scratchpad/guardie.py` dalla 33a. Ma `guardie.py` legge i JSONL di lotto,
    cioe' il **dizionario**, e una toppa una firma non ce l'ha: nella 127a se ne
    sono trovate **cinque** nelle battute delle mosse speciali, scritte nella
    126a — lo stesso giorno in cui erano nati i due referti sulle toppe, che
    pero' cercavano participi ed elisioni, non caratteri.

    ⚠️ Si giudica **riga per riga**, e le righe col giapponese si saltano: una
    toppa a blocco porta dentro anche il ramo `if ( jp )`, dove 「疲れた…」 e'
    scritta giusta — li' il carattere a doppia larghezza sta in una riga a
    doppia larghezza, ed e' quel che quella lingua vuole. Il `cerca` si salta
    per la stessa ragione al contrario: e' il sorgente di monte, e non e' roba
    nostra.
    """
    for t in carica_toppe():
        for riga in righe_di_toppa(t["sostituisci"]):
            cattivi = proibiti_in_italiano(riga)
            assert not cattivi, (
                f"la toppa «{t['motivo'][:50]}…» scrive in italiano "
                f"{cattivi!r}, che CP932 codifica a due byte e il carattere "
                "latino della build disegna come due glifi a caso. I puntini "
                "di sospensione si scrivono `...`, le virgolette `\"`.\n"
                f"  {riga.strip()}")


def test_la_rete_dei_caratteri_proibiti_vede_e_non_vede_quel_che_deve():
    """La rete qui sopra su una riga inventata, nei due versi.

    ⚠️ Una prova che gira su un corpus tutto sano non dimostra niente: resta
    verde anche se la regola non guarda nessuno. Qui la regola si esercita su
    una riga scritta apposta — quella vera che la 127a ha trovato — e sul caso
    che deve invece lasciar passare.
    """
    italiana = '\t\t\ttxt cnvtalk("Clemenza… Clementia!")'
    assert proibiti_in_italiano(italiana) == ["…"]

    # la stessa riga scritta bene non accusa piu' niente
    assert proibiti_in_italiano(italiana.replace("…", "...")) == []

    # e il ramo giapponese di una toppa a blocco porta `…` a ragione: si salta
    giapponese = '\t\t\ttxt name(tc) + "「疲れた…」"'
    assert proibiti_in_italiano(giapponese) == []

    # le altre quattro dell'elenco, per non lasciare la regola provata su uno solo
    assert proibiti_in_italiano('mes "«ciao»"') == ["«", "»"]
    assert proibiti_in_italiano('mes "“ciao”"') == ["“", "”"]


# ---------------------------------------------------------------------------
# Toppe a blocco: piu' righe consecutive al posto di una sola.
#
# Nate il 2026-08-07 per la composizione del nome degli oggetti
# (`item_func.hsp:1259-1285`), dove il plurale della parola-contatore si fa col
# suffisso inglese (`scroll` + `"s "`). In italiano il plurale e' irregolare per
# parola: la riscrittura corretta vuole uno `switch`, cioe' un blocco, e una
# toppa di riga non ci arriva.
# ---------------------------------------------------------------------------

BLOCCO_CERCA = [
    "\tif ( n > 1 ) {",
    '\t\ts = "" + n + " " + tipo + "s of "',
    "\t}",
]
BLOCCO_SOSTITUISCI = [
    "\tif ( n > 1 ) {",
    "\t\tswitch tipo",
    '\t\t\tcase "pergamena"',
    '\t\t\t\ts = "" + n + " pergamene di "',
    "\t\t\t\tswbreak",
    "\t\tswend",
    "\t}",
]


def toppa_blocco(**sovrascritture):
    base = {
        "file": "item_func.hsp",
        "cerca": BLOCCO_CERCA,
        "sostituisci": BLOCCO_SOSTITUISCI,
        "motivo": "prova a blocco",
    }
    base.update(sovrascritture)
    return base


def test_una_toppa_a_blocco_sostituisce_le_righe_consecutive():
    testo = sorgente("*itemname", *BLOCCO_CERCA, "\treturn s")
    nuovo, quante = applica_toppe("item_func.hsp", testo, [toppa_blocco()])
    assert quante == 1
    assert nuovo == sorgente("*itemname", *BLOCCO_SOSTITUISCI, "\treturn s")


def test_una_toppa_a_blocco_puo_cambiare_il_numero_di_righe():
    """Le toppe girano dopo il dizionario, quindi lo scivolamento non fa danni."""
    testo = sorgente("*itemname", *BLOCCO_CERCA, "\treturn s")
    nuovo, _ = applica_toppe("item_func.hsp", testo, [toppa_blocco()])
    righe = nuovo.split("\r\n")[:-1]
    assert len(righe) == 2 + len(BLOCCO_SOSTITUISCI)


def test_un_blocco_che_non_esiste_piu_ferma_la_catena():
    """Stessa regola delle toppe di riga: upstream l'ha riscritto, non si indovina."""
    testo = sorgente("*itemname", BLOCCO_CERCA[0], "\ts = 0", "\t}")
    with pytest.raises(SorgenteCorrotto, match="non esiste piu'"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco()])


def test_un_blocco_ambiguo_ferma_la_catena():
    testo = sorgente("*itemname", *BLOCCO_CERCA, "*altro", *BLOCCO_CERCA)
    with pytest.raises(SorgenteCorrotto, match="ambigu"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco()])


def test_un_blocco_identico_alla_sostituzione_e_un_errore():
    testo = sorgente("*itemname", *BLOCCO_CERCA)
    with pytest.raises(SorgenteCorrotto, match="cerca identica"):
        applica_toppe("item_func.hsp", testo, [toppa_blocco(sostituisci=BLOCCO_CERCA)])


def test_un_blocco_vuoto_e_un_errore(tmp_path):
    """`carica_toppe` pretende i campi non vuoti: una lista vuota e' vuota."""
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_blocco(cerca=[]), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="campi mancanti o vuoti"):
        carica_toppe(percorso)


def test_riga_e_blocco_convivono_nello_stesso_file():
    testo = sorgente("*itemname", RIGA_NAME, *BLOCCO_CERCA)
    toppe = [toppa(file="item_func.hsp"), toppa_blocco()]
    nuovo, quante = applica_toppe("item_func.hsp", testo, toppe)
    assert quante == 2
    assert '"the "' not in nuovo
    assert '"s of "' not in nuovo


def test_carica_toppe_conserva_i_blocchi(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_blocco(), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert caricate[0]["cerca"] == BLOCCO_CERCA


# ---------------------------------------------------------------------------
# Toppe `tutte`: la stessa riga ripetuta, tradotta ovunque.
#
# Nate il 2026-08-16 (50a) misurando il quinto punto cieco: **125 righe su 717**
# di testo inglese nudo non erano raggiungibili da nessuna toppa, non perche'
# mancasse la resa ma perche' la riga compare piu' volte identica e
# `applica_toppe` — giustamente — si ferma sull'ambiguita'.
#
# Sono schermate che ripetono se' stesse: gli otto menu di `custom_tweaks.hsp`
# hanno lo stesso titolo («Tweak Setup» x6, «Configure Tweaks» x8, «Return to
# the previous menu.» x9), le dodici schermate di creazione del personaggio
# ripetono «Press F1 to show help.» (`chara.hsp`), e `command.hsp:2901` (« Rank.»)
# compare due volte, nel diario e nella scheda.
#
# ⚠️ L'ambiguita' resta un ERRORE per difetto: `tutte` va scritto a mano, una
# toppa alla volta, e vale solo dove chi la scrive ha guardato tutte le
# occorrenze e ha deciso che vogliono la stessa resa. Il caso pericoloso —
# stessa riga, rese diverse a seconda del posto — deve continuare a fermarsi.
# ---------------------------------------------------------------------------

def test_una_toppa_tutte_sostituisce_ogni_occorrenza():
    testo = sorgente(RIGA_NAME, "\tx = 1", RIGA_NAME, "\ty = 2", RIGA_NAME)
    nuovo, quante = applica_toppe("init.hsp", testo, [toppa(tutte=True)])
    assert quante == 1                      # una toppa, non tre
    assert '"the "' not in nuovo            # nessuna occorrenza sopravvissuta
    assert nuovo.count("return cdatan(CDATAN_NAME, name_arg1)") == 3
    assert "\tx = 1" in nuovo and "\ty = 2" in nuovo


def test_una_toppa_tutte_va_bene_anche_con_una_sola_occorrenza():
    testo = sorgente(RIGA_NAME)
    nuovo, _ = applica_toppe("init.hsp", testo, [toppa(tutte=True)])
    assert '"the "' not in nuovo


def test_una_toppa_tutte_vuole_almeno_un_occorrenza():
    """`tutte` allarga l'ambiguita', non il non-esiste: se sparisce, ci si ferma."""
    testo = sorgente("#defcfunc name int name_arg1", "\treturn 0")
    with pytest.raises(SorgenteCorrotto, match="non esiste"):
        applica_toppe("init.hsp", testo, [toppa(tutte=True)])


def test_senza_tutte_l_ambiguita_resta_un_errore():
    """La rete che conta: `tutte` e' una scelta esplicita, non il nuovo difetto."""
    testo = sorgente(RIGA_NAME, RIGA_NAME)
    with pytest.raises(SorgenteCorrotto, match="ambigu"):
        applica_toppe("init.hsp", testo, [toppa()])
    with pytest.raises(SorgenteCorrotto, match="ambigu"):
        applica_toppe("init.hsp", testo, [toppa(tutte=False)])


def test_una_toppa_tutte_a_blocco_sostituisce_ogni_blocco():
    testo = sorgente("*itemname", *BLOCCO_CERCA, "*altro", *BLOCCO_CERCA)
    nuovo, _ = applica_toppe("item_func.hsp", testo, [toppa_blocco(tutte=True)])
    assert '"s of "' not in nuovo
    assert nuovo.count('s = "" + n + " pergamene di "') == 2
    assert "*altro" in nuovo


def test_una_toppa_tutte_non_si_mangia_le_occorrenze_sovrapposte():
    """Blocchi che si accavallano: si prende il primo e si riparte DOPO di lui.

    Con `cerca` di due righe uguali fra loro e tre righe uguali nel file, gli
    inizi possibili sono due (0 e 1) ma i blocchi veri sono uno solo: contarli
    tutt'e due vorrebbe dire sostituire dentro un pezzo gia' sostituito.
    """
    doppia = ["\tmes a", "\tmes a"]
    testo = sorgente("*x", "\tmes a", "\tmes a", "\tmes a")
    t = toppa_blocco(cerca=doppia, sostituisci=["\tmes b"], tutte=True)
    nuovo, _ = applica_toppe("item_func.hsp", testo, [t])
    assert nuovo == sorgente("*x", "\tmes b", "\tmes a")


def test_carica_toppe_conserva_tutte(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa(tutte=True), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert caricate[0]["tutte"] is True


def test_tutte_deve_essere_un_booleano(tmp_path):
    """Un `"si"` o un `1` letti come veri sarebbero una decisione presa per caso."""
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa(tutte="si"), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="tutte"):
        carica_toppe(percorso)


# --- `prima`: la toppa che gira PRIMA del dizionario -------------------------
#
# Nata nella 61a per `config.hsp:618`, dove due voci di menu sono letterali
# inglesi nudi sulla stessa riga di quattro che invece stanno dentro una
# `lang()`. Il dizionario riscrive le quattro, quindi dopo di lui quella riga
# non e' piu' quella del sorgente pinnato e una toppa scritta sul sorgente non
# la trova. Girando prima, il `cerca` resta la riga del sorgente — e cosi' resta
# vera anche la guardia contro la deriva di upstream.

RIGA_MISTA = '\t\ts = lang("ログ", "Log"), "  Display log instead*", ""'
RIGA_MISTA_IT = '\t\ts = lang("ログ", "Log"), "  Registro invece*", ""'


def toppa_prima(**sovrascritture):
    base = {
        "file": "config.hsp",
        "cerca": RIGA_MISTA,
        "sostituisci": RIGA_MISTA_IT,
        "motivo": "prova",
        "prima": True,
    }
    base.update(sovrascritture)
    return base


def test_carica_toppe_conserva_prima(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_prima(), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    caricate = carica_toppe(percorso)
    assert caricate[0]["prima"] is True


def test_prima_deve_essere_un_booleano(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_prima(prima="si"), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="prima"):
        carica_toppe(percorso)


def test_una_toppa_prima_non_puo_cambiare_il_contenuto_di_una_lang(tmp_path):
    """E' la ragione per cui `prima` non e' il modo normale di toppare.

    Il dizionario gira dopo e cerca i siti per contenuto: se la toppa gli
    cambia l'inglese sotto i piedi, quel sito diventa orfano e la riga torna in
    inglese senza che nessuna guardia se ne accorga.
    """
    percorso = tmp_path / "toppe.jsonl"
    rotta = toppa_prima(sostituisci='\t\ts = lang("ログ", "Registro"), "  Registro invece*", ""')
    percorso.write_text(json.dumps(rotta, ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(SorgenteCorrotto, match="lang"):
        carica_toppe(percorso)


def test_una_toppa_prima_che_tocca_solo_il_nudo_passa(tmp_path):
    percorso = tmp_path / "toppe.jsonl"
    percorso.write_text(json.dumps(toppa_prima(), ensure_ascii=False) + "\n",
                        encoding="utf-8")
    assert len(carica_toppe(percorso)) == 1


def test_letterali_di_lang_prende_solo_quel_che_sta_dentro():
    dentro = letterali_di_lang([RIGA_MISTA])
    assert dentro == ['"ログ"', '"Log"']
    # il nudo di fuori non c'e', ed e' tutto il punto
    assert '"  Display log instead*"' not in dentro


def test_letterali_di_lang_regge_le_virgolette_protette():
    riga = '\ttxt lang("a", "dice \\"si\\" e basta"), "fuori"'
    assert letterali_di_lang([riga]) == ['"a"', '"dice \\"si\\" e basta"']
