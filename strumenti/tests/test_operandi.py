"""Le prove della rete dell'operando.

⚠️⚠️ La prova che conta di piu' e' quella al contrario: **i casi veri che la
142a ha trovato a mano devono accendere questa rete, e la rete deve dire
QUALI**. Un `assert problemi() == []` direbbe solo che le dichiarazioni
tornano, e tornerebbero anche se la rete non trovasse piu' niente.
"""
import pytest

from strumenti import operandi, percorsi
from strumenti.commenti import righe_in_ramo_spento
from strumenti.operandi import (DICHIARATI, TIPI, candidati_di,
                                chiavi_da_espressione, censimento, problemi)


def _chiavi(riga: str) -> list[str]:
    return [c for caso in candidati_di("x.hsp", [(1, riga)])
            for c in caso["chiavi"]]


def _pagliai(riga: str) -> list[str]:
    return [caso["radice"] for caso in candidati_di("x.hsp", [(1, riga)])]


# --- dove sta la chiave in ogni costrutto ----------------------------------

def test_di_un_instr_si_prende_il_terzo_argomento():
    assert _chiavi('if ( instr(evact, 0, "gohos") != (-1) ) {') == ["gohos"]


def test_di_un_cnv_str_si_prende_il_secondo_e_non_il_sostituto():
    """⭐ IL CASO CHE DISTINGUE UNA RETE DA UN `grep`.
    `cnv_str fix_input_chat_arg1, "%", "per"` non ha nessuna chiave italiana:
    `"per"` e' quel che ci si SCRIVE al posto del segno di percentuale."""
    assert _chiavi('cnv_str fix_input_chat_arg1, "%", "per"') == []


def test_di_uno_sreplace_si_prende_il_terzo_argomento():
    """`sreplace destinazione, sorgente, cerca, sostituto`: quattro argomenti,
    e la chiave e' il terzo."""
    assert _chiavi('sreplace s, s, "coffin ", "bara "') == ["coffin "]


def test_una_riga_puo_portare_due_chiavi():
    """Le due battute del desiderio stanno in `or` sulla stessa riga."""
    riga = ('if ( instr(inputlog, 0, "god inside") != (-1) | '
            'instr(inputlog, 0, "dio dentro") != (-1) ) {')
    assert _chiavi(riga) == ["god inside", "dio dentro"]


def test_l_instr_annidato_non_sposta_gli_argomenti():
    """`instr(a, instr(b, 0, "x"), "y")` ha tre argomenti, non cinque: la
    chiave di fuori e' `"y"`, e quella di dentro resta la sua. ⓘ Escono
    nell'ordine in cui i due `instr` cominciano, cioe' prima quello esterno."""
    assert _chiavi('p = instr(s, instr(t, 0, "x"), "y")') == ["y", "x"]
    assert _pagliai('p = instr(s, instr(t, 0, "x"), "y")') == ["s", "t"]


def test_lo_strmid_non_e_un_costrutto():
    """Prende posizione e lunghezza: non ha mai un letterale come chiave. Le
    sue righe entravano nel conto solo per l'`instr` che ci sta dentro."""
    assert _chiavi('evact = strmid(tmpbuff(cnt), 0, 100)') == []


# --- che cosa non e' una chiave --------------------------------------------

def test_il_marcatore_non_e_una_chiave():
    for marcatore in ('%txt', '{ev}', '/neg/', ':sound', '_tmp_', 'JP'):
        assert _chiavi('if ( instr(buff, 0, "%s") != (-1) ) {' % marcatore) == []


def test_il_giapponese_non_e_una_chiave():
    """Una chiave giapponese in un ramo `jp` e' al suo posto."""
    assert _chiavi('if ( instr(s, 0, "錬金術師") != (-1) ) {') == []


def test_la_chiave_costruita_da_una_lang_non_e_un_candidato():
    """⭐ E' la FORMA GIUSTA, non un buco: e' cosi' che il progetto si porta
    dietro una chiave, ed e' il caso delle 75 parole del filtro automatico."""
    assert _chiavi('if ( instr(s, 0, lang("すべての", " ogni ")) != (-1) ) {') == []


# --- il pagliaio ------------------------------------------------------------

def test_il_pagliaio_perde_l_indice_ma_non_il_nome():
    assert _pagliai('if ( instr(cdatan(CDATAN_NAME, tc), 0, "Alhaz") ) {') \
        == ["cdatan"]


# --- le due famiglie di riga morta ------------------------------------------

def test_il_blocco_spento_dal_mod_non_si_conta():
    """`command.hsp:2554`-`:2555` sta in un `/* ORIGINAL … */`: due righe che
    non girano, e che senza questo taglio raddoppierebbero il fronte di
    `listn`."""
    casi = candidati_di("command.hsp")
    righe = {c["riga"] for c in casi if c["radice"] == "listn"}
    assert righe == {2561, 2562, 2563, 2564}


def test_il_ramo_if_zero_non_si_conta_ed_e_il_progetto_a_scriverlo():
    """⭐⭐ La trappola di leggere la build. Il pluralizzatore inglese di
    `item_func.hsp` — `"coffins"`, `"ves"`, `"ies"` — sta dentro un
    `if ( 0 ) { … }` che ci ha messo `genera_toppe_nomi.py`, perche' il plurale
    italiano arriva da `ioriginalnamerefplur`. Contarlo vorrebbe dire aprire un
    fronte su codice che il progetto ha appena spento."""
    spente = righe_in_ramo_spento(percorsi.BUILD_HSP / "item_func.hsp")
    assert 2103 in spente and 2117 in spente
    chiavi = {c["chiavi"][0] for c in candidati_di("item_func.hsp")}
    assert "coffins" not in chiavi and "ves" not in chiavi


# --- la prova al contrario: i casi veri, e QUALI sono -----------------------

def test_trova_il_difetto_di_ragon_e_dice_dove():
    """⭐⭐ Il punto 9 della lista della 138a, e questa rete e' il primo
    strumento del progetto che l'ha misurato invece di ricordarselo.

    ⚠️ Le tre righe sono le stesse di prima della cura; quel che e' cambiato e'
    che adesso ognuna porta anche le chiavi italiane. Se un giorno «drago»
    sparisse di qui, la cacciatrice di draghi tornerebbe ad agganciare i soli
    quattro «dragonewt» e nessun altro cancello se ne accorgerebbe."""
    casi = [c for c in candidati_di("tcg_skill.hsp")
            if c["radice"] == "carddetailneff@tcg"]
    assert sorted({c["riga"] for c in casi}) == [4960, 4972, 5003]
    assert {c["chiavi"][0] for c in casi} == {"ragon", "drago", "Drago",
                                              "draghi"}


def test_trova_le_battute_dell_alchimista():
    """La professione finta la digita il giocatore, e in italiano scrivera'
    «alchimista»: `lchemist` da solo non agganciava."""
    casi = [c for c in candidati_di("command.hsp") if c["radice"] == "cdatan"]
    assert sorted({c["riga"] for c in casi}) == [52, 57, 62, 67, 72]
    assert {c["chiavi"][0] for c in casi} == {"lchemist", "lchimista"}


def test_il_fronte_e_di_tre_righe_su_un_pagliaio_solo():
    """⚠️ Il conto non si eredita: se cambia, o si e' chiuso un fronte o se
    n'e' aperto uno, e in tutt'e due i casi va scritto perche'.

    ⓘ Era di 12 righe su 4 pagliai quando la 143a l'ha misurato la prima
    volta: l'alchimista e la cacciatrice di draghi si sono chiusi nella stessa
    sessione, e quel che resta e' la giuntura inglese del nome composto, che
    vuole `contratto-nomi.md` e non una toppa per riga."""
    fronti = {n: d for n, d in DICHIARATI.items() if d.tipo == "fronte"}
    assert set(fronti) == {"custom_dmgpop.hsp:s@DP"}
    assert sum(d.casi for d in fronti.values()) == 3


def test_le_chiavi_gia_a_posto_sono_il_margine():
    """⚠️ Un cancello booleano non dice il margine: 144 chiavi passano gia' da
    una `lang()`, e senza questo numero il «12» sembrerebbe tutto il mondo."""
    conti = chiavi_da_espressione()
    assert conti["lang"] > 100


# --- il cancello -------------------------------------------------------------

def test_ogni_pagliaio_della_build_e_dichiarato_col_suo_conto():
    assert problemi() == []


def test_ogni_dichiarazione_ha_un_tipo_conosciuto_e_un_motivo():
    for nome, dichiarata in DICHIARATI.items():
        assert dichiarata.tipo in TIPI, nome
        assert len(dichiarata.motivo) > 20, nome


def test_il_cancello_si_accende_se_un_pagliaio_nuovo_compare():
    """La prova al contrario del cancello: senza una dichiarazione, il
    censimento non tace."""
    finto = [{"chiave": "x.hsp:nuovo", "file": "x.hsp", "pagliaio": "nuovo",
              "quanti": 1,
              "casi": [{"file": "x.hsp", "riga": 7, "chiavi": ["dragon"]}]}]
    # ⓘ `problemi` su un censimento finto lamenta anche tutte le
    # dichiarazioni che li' dentro non trovano piu' niente: si guarda la voce
    # del pagliaio nuovo, che e' quel che questa prova misura.
    sue = [g for g in problemi(finto) if g.startswith("x.hsp:nuovo")]
    assert len(sue) == 1
    assert "dragon" in sue[0] and "riga 7" in sue[0]


def test_il_cancello_si_accende_se_il_conto_si_muove():
    """⭐ E' successo davvero, ed e' servito: le quattro toppe della 143a hanno
    mosso tre conti, e la rete se n'e' accorta da sola."""
    dichiarata = DICHIARATI["tcg_skill.hsp:carddetailneff@tcg"]
    finto = [{"chiave": "tcg_skill.hsp:carddetailneff@tcg",
              "file": "tcg_skill.hsp", "pagliaio": "carddetailneff@tcg",
              "quanti": dichiarata.casi + 1,
              "casi": [{"file": "tcg_skill.hsp", "riga": 4960,
                        "chiavi": ["ragon"]}]}]
    sue = [g for g in problemi(finto)
           if g.startswith("tcg_skill.hsp:carddetailneff@tcg")]
    assert len(sue) == 1
    assert ("dichiarate %d righe, nella build ne sono %d"
            % (dichiarata.casi, dichiarata.casi + 1)) in sue[0]
