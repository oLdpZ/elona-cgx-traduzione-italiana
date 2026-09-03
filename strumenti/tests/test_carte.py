"""Le prove della catena di `tcg_mod.hsp`, le descrizioni d'effetto delle carte.

⚠️ Come per `scene2.hsp`, la prova che conta di piu' non e' l'identita': e' la
sua **prova al contrario**. Un `applica_a_righe` che non toccasse mai niente
supererebbe l'identita' a occhi chiusi. Ogni cancello qui sotto ha la sua
coppia: uno che pretende che non succeda niente, e uno che pretende che succeda.

⚠️⚠️ E la prova piu' importante di tutte non guarda una resa: guarda la
**partizione**. `tcg_skill.hsp:618` copia un effetto solo se la carta e'
marcata `TCG_SKILL_TYPE_BATTLECRY` **e** la parola compare nel testo. Le due
cose non coincidono di monte (491 marcate, 19 senza la parola, due delle quali
sono refusi), e l'italiano deve riprodurre quella partizione esatta -- non
ripararla.
"""
import pytest

from strumenti.carte import (ATTESE, COLONNA_SCHEDA, GRAFIE, INNESTI,
                             PAROLE_CHIAVE, PREFISSO,
                             SOFFITTO_AVVISO, applica_a_righe,
                             avvisi, carica_dizionario, partizione_battlecry,
                             problemi, righe_a_capo, voci)


def _righe(*testo: str) -> list[str]:
    return list(testo)


UN_FILE = _righe(
    "\tsdim effdesc@tcg, 30, 3000",
    '\teffdesc@tcg(TCG_EFF_NONE) = "No Effect."',
    '\teffdesc@tcg(TCG_EFF_ZEOME) = "Battlecry: Draw 1 Card."',
    "\tif ( x == 1 ) {",
    '\t\teffdesc@tcg(TCG_EFF_MARKA) = "She is a \\"bear\\" card."',
    "\t}",
    '\tcardhelp lang("test", "Test")',
)


def _diz(*voci_piene) -> dict:
    return {v["costante"]: v for v in voci_piene}


# --- il riconoscitore -----------------------------------------------------

def test_riconosce_solo_le_assegnazioni_di_effdesc():
    trovate = voci(UN_FILE)
    assert [v["costante"] for v in trovate] == [
        "TCG_EFF_NONE", "TCG_EFF_ZEOME", "TCG_EFF_MARKA"]


def test_sdim_non_e_una_descrizione():
    """`sdim effdesc@tcg, 30, 3000` dichiara l'array, non assegna un testo."""
    assert all(v["costante"] != "effdesc@tcg" for v in voci(UN_FILE))


def test_il_letterale_con_le_virgolette_dentro_arriva_intero():
    marka = next(v for v in voci(UN_FILE) if v["costante"] == "TCG_EFF_MARKA")
    assert marka["en"] == 'She is a \\"bear\\" card.'


def test_la_chiave_e_il_nome_della_costante_e_porta_la_riga():
    zeome = next(v for v in voci(UN_FILE) if v["costante"] == "TCG_EFF_ZEOME")
    assert zeome["riga"] == 3


def test_il_sorgente_vero_ha_il_numero_atteso_di_descrizioni():
    """⚠️ Il numero atteso batte l'avviso: non chiede a nessuno di ricordarsi."""
    from strumenti.carte import leggi
    assert len(voci(leggi())) == ATTESE


def test_due_descrizioni_hanno_l_inglese_vuoto_e_il_bersaglio_e_833():
    """⚠️ `TCG_EFF_PROJETP1` e `P2`, i moduli del PRO-JET, hanno `""` come
    testo: non c'e' niente da tradurre e non ci sara' mai. Un contatore che
    punta a 835 non arriverebbe mai in fondo, e un cancello che non chiude mai
    si impara a ignorare."""
    from strumenti.carte import TRADUCIBILI, leggi
    piene = [v for v in voci(leggi()) if v["en"].strip()]
    assert len(piene) == TRADUCIBILI == ATTESE - 2


def test_nel_sorgente_vero_le_costanti_sono_tutte_distinte():
    from strumenti.carte import leggi
    nomi = [v["costante"] for v in voci(leggi())]
    assert len(set(nomi)) == len(nomi)


# --- l'identita' e la sua prova al contrario ------------------------------

def test_col_dizionario_vuoto_il_file_torna_identico():
    rifatte, fatte = applica_a_righe(UN_FILE, {})
    assert rifatte == UN_FILE
    assert fatte == 0


def test_una_resa_viene_davvero_iniettata():
    """La prova al contrario dell'identita': se questa passa a vuoto, l'altra
    non prova niente."""
    diz = _diz({"costante": "TCG_EFF_ZEOME", "en": "Battlecry: Draw 1 Card.",
                "it": "Grido di battaglia: pesca 1 carta."})
    rifatte, fatte = applica_a_righe(UN_FILE, diz)
    assert fatte == 1
    assert rifatte[2] == ('\teffdesc@tcg(TCG_EFF_ZEOME) = "Grido di battaglia:'
                          ' pesca 1 carta."')


def test_la_resa_viene_scritta_senza_accenti_veri():
    """CP932 non contiene nessuna vocale accentata italiana: `accenti.degrada`
    scrive `a'` al posto di `à`, e l'iniezione deve passare di li'."""
    diz = _diz({"costante": "TCG_EFF_NONE", "en": "No Effect.",
                "it": "Nessuna abilità."})
    rifatte, _ = applica_a_righe(UN_FILE, diz)
    assert "abilita'" in rifatte[1]
    assert "à" not in rifatte[1]


def test_una_resa_su_un_monte_cambiato_si_rifiuta():
    """Se l'inglese non e' piu' quello su cui la resa fu scritta, la voce va
    rifatta, non riagganciata."""
    diz = _diz({"costante": "TCG_EFF_ZEOME", "en": "Battlecry: Draw 2 Cards.",
                "it": "Grido di battaglia: pesca 2 carte."})
    with pytest.raises(ValueError, match="monte"):
        applica_a_righe(UN_FILE, diz)


def test_una_costante_che_non_esiste_piu_si_rifiuta():
    diz = _diz({"costante": "TCG_EFF_SPARITA", "en": "x", "it": "y"})
    with pytest.raises(ValueError, match="TCG_EFF_SPARITA"):
        applica_a_righe(UN_FILE, diz)


# --- `talk_conv` a 65, il ramo non giapponese -----------------------------

def test_l_a_capo_cade_prima_della_parola_che_sfora():
    """⚠️ La parola che fa sforare dev'essere seguita da uno spazio: `talk_conv`
    guarda il **prossimo spazio**, quindi l'ultima parola non provoca mai un a
    capo, per lunga che sia. Vedi la prova qui sotto sulla coda."""
    assert righe_a_capo("a" * 60 + " parola ancora", 65) == [
        "a" * 60 + " ", "parola ancora"]


def test_una_coda_senza_spazi_resta_lunga_quanto_viene():
    """`talk_conv` non spezza mai dentro una parola: e' l'unico modo in cui una
    riga puo' sforare in larghezza invece che in altezza."""
    assert righe_a_capo("x" * 90, 65) == ["x" * 90]


def test_il_prefisso_della_scheda_entra_nel_conto():
    """`tcg.hsp:1473` manda a capo `"Effect: " + effdesc`, non `effdesc`."""
    assert PREFISSO == "Effetto: "


# --- i cancelli sulla resa ------------------------------------------------

def test_le_caporali_non_passano():
    """CP932 non le sa scrivere: e' la trappola su cui sono inciampate la 133a
    e la 135a. Il cancello va dove si scrive la resa."""
    guai = problemi({"costante": "X", "en": "a", "it": "Costa «poco»."})
    assert any("CP932" in g for g in guai)


def test_una_resa_pulita_non_da_problemi():
    """La prova al contrario del cancello di sopra."""
    assert problemi({"costante": "X", "en": "a",
                     "it": "Grido di battaglia: pesca 1 carta."}) == []


def test_un_innesto_reso_fuori_glossario_si_accende():
    """`carte.GRAFIE` nasce con il cancello che la legge -- a differenza di
    `scene.GRAFIE`, pronta dalla 133a e mai letta da nessuno.

    ⚠️ E la rete non e' quella di `scene.py`, che cerca inglese rimasto dentro
    l'italiano: qui «Grido di guerra» di inglese non ne ha. La rete guarda
    l'inglese di monte, e pretende il traducente canonico nella resa.
    """
    guai = problemi({"costante": "X", "en": "Battlecry: Draw.",
                     "it": "Grido di guerra: pesca."})
    assert any("Grido di battaglia" in g for g in guai), guai


def test_l_innesto_si_controlla_solo_in_testa():
    """`Sacrifice` in testa e' «Sacrificio:», ma a meta' frase e' il verbo
    «sacrifica». Un cancello che lo cercasse ovunque direbbe rosso su una resa
    giusta, e chi traduce imparerebbe a non guardarlo."""
    assert problemi({"costante": "X", "en": "Battlecry: Sacrifice a Card.",
                     "it": "Grido di battaglia: sacrifica una carta."}) == []


def test_i_refusi_di_monte_sono_esentati_dal_cancello():
    """`TCG_EFF_NAPLUS` dichiara `BattleCry` e deve NON portare il traducente
    canonico, o si accenderebbe una carta che oggi il gioco non copia."""
    assert problemi({"costante": "TCG_EFF_NAPLUS",
                     "en": "BattleCry/InHand: Make you 1 thing.",
                     "it": "Grido di Battaglia/In mano: ti fa 1 cosa."}) == []


def test_una_parola_chiave_gia_a_schermo_si_controlla_ovunque():
    """`Windfury` e' «Raffica» nelle toppe di `tcg.hsp` da fasi: una seconda
    resa sarebbe una seconda traduzione della stessa parola, e le due si vedono
    nella stessa schermata."""
    guai = problemi({"costante": "X", "en": "Ongoing: Gain Windfury.",
                     "it": "Continuo: ottieni Furia del vento."})
    assert any("Raffica" in g for g in guai), guai


def test_la_tabella_delle_grafie_copre_gli_innesti_scritti_in_piu_modi():
    for scritto in ["BeginPhase", "In Hand", "On Draw", "AfterCombat"]:
        assert scritto in GRAFIE


def test_nessun_traducente_delle_tabelle_e_gia_degradato():
    """⚠️ `problemi()` confronta con la resa del DIZIONARIO, dove l'accento e'
    vero: `degrada` interviene dopo, scrivendo l'albero di build. Un traducente
    scritto gia' degradato -- `Gravita'` invece di `Gravità` -- non troverebbe
    mai la resa giusta e il cancello direbbe rosso su una resa corretta.

    Era proprio il caso di `Gravity`, e il difetto non l'ha trovato nessuna
    prova: l'ho visto scrivendo il lotto dopo. Da qui in poi lo trova questa.
    """
    import re

    degradato = re.compile(r"[aeiou]'(?![A-Za-zÀ-ÿ])")
    for tabella, nome in [(INNESTI, "INNESTI"), (PAROLE_CHIAVE, "PAROLE_CHIAVE")]:
        for chiave, italiano in tabella.items():
            assert not degradato.search(italiano), (
                "%s[%r] = %r sembra gia' degradato" % (nome, chiave, italiano))


def test_ogni_parola_chiave_gia_a_schermo_sta_nel_cancello_o_e_esentata():
    """⚠️⚠️ La prima `PAROLE_CHIAVE` ne aveva sette invece di ventisei, e il
    buco non l'ha trovato nessun test: l'ha trovato la prova al contrario,
    perche' «Ricarica» al posto di «Rigenerazione» passava indisturbata. Una
    tabella incompleta non sbaglia, **tace**.

    Questa prova non fissa un numero -- lo leggerebbe da se' stessa. Legge le
    toppe VERE di `tcg.hsp`, cioe' quel che il gioco scrive a schermo, e
    pretende che ogni parola chiave sia decisa: o nel cancello, o esentata con
    la sua ragione.
    """
    import json
    import re

    from strumenti import percorsi
    from strumenti.carte import FUORI_DAL_CANCELLO, PAROLE_CHIAVE

    letterale = re.compile(r'"((?:[^"\\]|\\.)*)"')
    chiavi = set()
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        toppa = json.loads(riga)
        if toppa.get("file") != "tcg.hsp":
            continue
        cerca, sostituisci = toppa.get("cerca"), toppa.get("sostituisci")
        if not isinstance(cerca, str) or not isinstance(sostituisci, str):
            continue
        # le parole chiave sono le toppe su `bmes "<parola>", 235, 125, 125`
        if "bmes" not in cerca:
            continue
        for prima, dopo in zip(letterale.findall(cerca),
                               letterale.findall(sostituisci)):
            if prima != dopo and prima.isascii() and len(prima.split()) <= 2:
                chiavi.add(prima)

    assert chiavi, "nessuna parola chiave letta dalle toppe: la prova e' cieca"
    decise = set(PAROLE_CHIAVE) | set(FUORI_DAL_CANCELLO)
    assert chiavi <= decise, sorted(chiavi - decise)


def test_l_avviso_conta_le_righe_sulla_forma_degradata():
    """Un accento costa un carattere a schermo: `Rarità` diventa `Rarita'`.

    ⚠️ La lunghezza qui non e' scelta a caso, e' **cercata**: nove «Città» col
    prefisso fanno 63 caratteri e stanno su una riga; degradate in «Citta'» ne
    fanno 72 e vanno a capo. Una prova che non attraversa quel confine
    passerebbe anche contando sulla resa non degradata, cioe' non proverebbe
    niente (lezione della 107a).
    """
    nove = "Città " * 9
    assert len(PREFISSO + nove) <= COLONNA_SCHEDA          # senza degradare: 1 riga
    guai = avvisi({"costante": "X", "en": "short", "it": nove})
    assert any("2 righe" in g for g in guai), guai


def test_una_resa_corta_non_avvisa():
    assert avvisi({"costante": "X", "en": "short",
                   "it": "Grido di battaglia: pesca 1 carta."}) == []


def test_il_soffitto_e_un_avviso_non_un_rifiuto():
    """Finche' nessuno ha visto il riquadro a schermo, il cancello avvisa e non
    rifiuta: un cancello che chiede l'impossibile viene disattivato (134a)."""
    lunga = "parola " * 60
    assert problemi({"costante": "X", "en": "short", "it": lunga}) == []
    assert avvisi({"costante": "X", "en": "short", "it": lunga}) != []


# --- l'invariante che protegge il comportamento ---------------------------

def test_la_partizione_battlecry_del_sorgente_e_quella_attesa():
    """491 marcate `TCG_SKILL_TYPE_BATTLECRY`, 472 delle quali portano la
    parola nel testo. Le altre 19 sono le carte degli dei e due refusi di
    monte, e devono restare fuori."""
    from strumenti.carte import leggi
    con, senza = partizione_battlecry(leggi())
    assert (len(con), len(senza)) == (472, 19)


def test_i_due_refusi_di_monte_sono_fra_i_diciannove():
    from strumenti.carte import leggi
    _, senza = partizione_battlecry(leggi())
    assert "TCG_EFF_CARAVAN" in senza
    assert "TCG_EFF_NAPLUS" in senza


def test_la_partizione_si_misura_sulla_parola_che_l_operando_cerca():
    """La prova al contrario: cambiando la parola cercata la partizione DEVE
    muoversi. Se non si muove, la funzione non sta guardando il testo."""
    from strumenti.carte import leggi
    righe = leggi()
    con_it, _ = partizione_battlecry(righe, parola="Grido di battaglia")
    assert len(con_it) == 0


def test_il_soffitto_di_avviso_e_quello_dell_inglese():
    assert SOFFITTO_AVVISO == 4


def test_la_colonna_e_quella_di_tcg_hsp_1473():
    assert COLONNA_SCHEDA == 65


# --- le battute delle carte (`efftalk@tcg`) -------------------------------

UN_FILE_BATTUTE = _righe(
    "\tsdim efftalk@tcg, 30, 3000",
    '\tefftalk@tcg(TCG_EFF_CACY) = "*Hiss*"',
    '\tefftalk@tcg(TCG_EFF_BIGSISTER) = cnvtalk("Leave this to your big sis!")',
    '\tefftalk@tcg(TCG_EFF_LITTLESISTER) = cnvtalk("" + _onii(x) + "!")',
)


def test_una_battuta_si_riconosce_piana_e_dentro_cnvtalk():
    from strumenti.carte import battute
    trovate = battute(UN_FILE_BATTUTE)
    assert [(v["costante"], v["en"]) for v in trovate] == [
        ("TCG_EFF_CACY", "*Hiss*"),
        ("TCG_EFF_BIGSISTER", "Leave this to your big sis!"),
    ]


def test_una_battuta_concatenata_NON_si_riconosce():
    """`cnvtalk("" + _onii(...) + "!")` non e' un letterale: va guardata a mano,
    non indovinata. Resta dichiarata come scoperta invece di sparire."""
    from strumenti.carte import battute
    assert all(v["costante"] != "TCG_EFF_LITTLESISTER"
               for v in battute(UN_FILE_BATTUTE))


def test_il_sorgente_vero_ha_il_numero_atteso_di_battute():
    from strumenti.carte import BATTUTE_ATTESE, battute, leggi
    assert len(battute(leggi())) == BATTUTE_ATTESE


def test_una_battuta_dentro_cnvtalk_conserva_il_suo_involucro():
    from strumenti.carte import applica_battute_a_righe
    diz = {"TCG_EFF_BIGSISTER": {"costante": "TCG_EFF_BIGSISTER",
                                 "en": "Leave this to your big sis!",
                                 "it": "Ci pensa la sorellona!"}}
    rifatte, fatte = applica_battute_a_righe(UN_FILE_BATTUTE, diz)
    assert fatte == 1
    assert rifatte[2] == ('\tefftalk@tcg(TCG_EFF_BIGSISTER) ='
                          ' cnvtalk("Ci pensa la sorellona!")')


def test_col_dizionario_vuoto_le_battute_non_cambiano_niente():
    from strumenti.carte import applica_battute_a_righe
    rifatte, fatte = applica_battute_a_righe(UN_FILE_BATTUTE, {})
    assert rifatte == UN_FILE_BATTUTE
    assert fatte == 0


# --- il dizionario --------------------------------------------------------

def test_un_dizionario_che_non_esiste_e_vuoto_non_rotto(tmp_path):
    assert carica_dizionario(tmp_path / "manca.jsonl") == {}


def test_il_dizionario_si_indicizza_per_costante(tmp_path):
    percorso = tmp_path / "effdesc.jsonl"
    percorso.write_text(
        '{"costante": "TCG_EFF_NONE", "en": "No Effect.", "it": "Nessuno."}\n',
        encoding="utf-8")
    assert carica_dizionario(percorso)["TCG_EFF_NONE"]["it"] == "Nessuno."
