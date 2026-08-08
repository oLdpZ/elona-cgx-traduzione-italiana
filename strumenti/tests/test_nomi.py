# strumenti/tests/test_nomi.py
"""Il secondo tipo di sito: i nomi degli oggetti di `db_item.hsp`.

Vedi `contratto-nomi.md` §1-2. I nomi degli oggetti non stanno dentro `lang()`
ma in un blocco `if ( jp ) … else …` con una forma canonica sola, misurata sul
sorgente pinnato: 1.321 su 1.321, zero eccezioni.

Il giudice vero di questo lavoro non e' qui: e' la prova d'identita', che
attraversa il file intero e pretende di riprodurlo byte per byte. Questi test
coprono la forma, i bordi e cio' che **non** deve essere agganciato.
"""
import pytest

from strumenti import percorsi
from strumenti.applica import applica_a_testo
from strumenti.estrai import avvio_nome, estrai_da_testo, siti, spezza_righe
from strumenti.prova_identita import dizionario_identita

BLOCCO = (
    "\tif ( jp ) {\n"
    '\t\tioriginalnameref(ITEM_ID_BANANA) = "バナナ"\n'
    "\t}\n"
    "\telse {\n"
    '\t\tioriginalnameref(ITEM_ID_BANANA) = "banana"\n'
    '\t\tioriginalnameref2(ITEM_ID_BANANA) = ""\n'
    "\t}\n"
)

BLOCCO_COMPOSTO = (
    "\tif ( jp ) {\n"
    '\t\tioriginalnameref(ITEM_ID_SCROLL_HARVEST) = "収穫の巻物"\n'
    "\t}\n"
    "\telse {\n"
    '\t\tioriginalnameref(ITEM_ID_SCROLL_HARVEST) = "harvest"\n'
    '\t\tioriginalnameref2(ITEM_ID_SCROLL_HARVEST) = "scroll"\n'
    "\t}\n"
)


def _nomi(testo):
    """(jp, en) dei soli siti che la scansione emette, in ordine."""
    return [(sito[3], sito[5]) for sito in siti(testo)]


def test_il_nome_inglese_e_un_sito():
    assert _nomi(BLOCCO) == [("バナナ", "banana")]


def test_il_secondo_riferimento_e_un_sito_a_se():
    """`deed of camp` si compone di due letterali, e sono due voci di dizionario.

    Il `" of "` sta fuori: lo risolve una toppa (contratto-nomi.md §3).
    """
    assert _nomi(BLOCCO_COMPOSTO) == [
        ("収穫の巻物", "harvest"),
        ("収穫の巻物", "scroll"),
    ]


def test_il_ramo_giapponese_non_e_un_sito():
    """Tradurre la riga giapponese cancellerebbe il gioco in giapponese."""
    for _, inglese in _nomi(BLOCCO):
        assert inglese != "バナナ"
    assert len(list(siti(BLOCCO))) == 1


def test_un_nome_inglese_vuoto_non_e_lavoro():
    """Come per `lang()`: senza inglese non c'e' niente da tradurre.

    Sul sorgente pinnato sono 12 su 1.321.
    """
    vuoto = BLOCCO.replace('= "banana"', '= ""')
    assert _nomi(vuoto) == []


def test_le_posizioni_ritagliano_il_letterale_sulla_riga_giusta():
    """Lo span e' cio' che `applica.py` sostituisce: deve tagliare esatto."""
    righe, _, _ = spezza_righe(BLOCCO_COMPOSTO)
    for sito in siti(BLOCCO_COMPOSTO):
        numero_riga, _, _, _, _, _, grezzo_en, inizio, fine = sito
        assert righe[numero_riga - 1][inizio:fine] == grezzo_en


def test_i_nomi_sono_statiche():
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    assert [v["tipo"] for v in voci] == ["statica"]
    assert voci[0]["en_grezzo"] == '"banana"'
    assert voci[0]["jp_grezzo"] == '"バナナ"'
    assert voci[0]["contesto"] == ""


def test_un_if_jp_che_non_e_un_nome_non_si_aggancia():
    """Gli `if ( jp )` di `db_item.hsp` sono 2.902, i nomi 1.321.

    Gli altri 1.581 non vanno toccati: agganciarli per analogia e' esattamente
    il modo di corrompere il sorgente in silenzio.
    """
    descrizione = (
        "\tif ( jp ) {\n"
        '\t\tdescription(0) = "説明"\n'
        "\t}\n"
        "\telse {\n"
        '\t\tdescription(0) = "a description"\n'
        '\t\tdescription(1) = ""\n'
        "\t}\n"
    )
    assert _nomi(descrizione) == []


def test_un_blocco_con_identificatori_diversi_non_si_aggancia():
    """Se i due rami parlano di oggetti diversi non e' la forma canonica.

    Non esiste nel sorgente pinnato, e se comparisse va guardata, non indovinata.
    """
    disallineato = BLOCCO.replace(
        'ioriginalnameref2(ITEM_ID_BANANA)', 'ioriginalnameref2(ITEM_ID_MELA)')
    assert _nomi(disallineato) == []


def test_un_blocco_senza_secondo_riferimento_non_si_aggancia():
    """La forma canonica ha sempre le due righe nel ramo `else`."""
    monco = BLOCCO.replace('\t\tioriginalnameref2(ITEM_ID_BANANA) = ""\n', "")
    assert _nomi(monco) == []


def test_avvio_nome_riconosce_la_riga_di_assegnazione():
    """Il riconoscitore per riga serve al riscontro di `applica.py`."""
    riga = '\t\tioriginalnameref(ITEM_ID_BANANA) = "banana"'
    assert avvio_nome(riga) == ('"banana"', 37, 45)
    assert riga[37:45] == '"banana"'
    assert avvio_nome('\tif ( jp ) {') is None
    assert avvio_nome('\t\tiorgweight(ITEM_ID_BANANA) = 3200') is None


def test_applica_sostituisce_il_nome_e_non_tocca_il_giapponese():
    voci = estrai_da_testo("db_item.hsp", BLOCCO_COMPOSTO)
    dizionario = {v["firma"]: {**v, "it": {"harvest": "raccolto", "scroll": "pergamena"}[v["en"]]}
                  for v in voci}
    nuovo, sostituzioni = applica_a_testo("db_item.hsp", BLOCCO_COMPOSTO, dizionario)
    assert sostituzioni == 2
    assert '"収穫の巻物"' in nuovo
    assert 'ioriginalnameref(ITEM_ID_SCROLL_HARVEST) = "raccolto"' in nuovo
    assert 'ioriginalnameref2(ITEM_ID_SCROLL_HARVEST) = "pergamena"' in nuovo


def test_la_prova_di_identita_attraversa_i_nomi():
    """Un dizionario che traduce ogni nome in se' stesso riproduce il testo."""
    testo = BLOCCO + BLOCCO_COMPOSTO
    dizionario, ambigue = dizionario_identita("db_item.hsp", testo)
    nuovo, sostituzioni = applica_a_testo("db_item.hsp", testo, dizionario)
    assert (nuovo, sostituzioni, ambigue) == (testo, 3, 0)


def test_una_traduzione_che_rompe_la_riga_si_ferma():
    """La virgoletta dentro l'italiano chiuderebbe la stringa in anticipo.

    `verifica.py` la rifiuta gia' nel lotto; qui si pretende che nemmeno un
    dizionario ritoccato a mano riesca a scrivere sorgente non rileggibile.
    """
    from strumenti.applica import SorgenteCorrotto

    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: {**v, "it": 'ba"nana'} for v in voci}
    with pytest.raises(SorgenteCorrotto):
        applica_a_testo("db_item.hsp", BLOCCO, dizionario)


def test_i_conteggi_sul_sorgente_vero():
    """1.321 blocchi, meno 12 nomi vuoti, piu' 298 secondi riferimenti.

    I numeri sono misurati sul sorgente pinnato al tag 2.31.2.0. Se calano
    senza che nessuno abbia cambiato il contratto, la scansione sta vedendo
    meno di prima e nessun altro test lo direbbe.
    """
    percorso = percorsi.SORGENTE_HSP / "db_item.hsp"
    if not percorso.exists():
        pytest.skip("il clone del sorgente non e' disponibile")
    testo = percorso.read_bytes().decode("cp932")

    voci = estrai_da_testo("db_item.hsp", testo)
    assert len(voci) == 1309 + 298
    righe, _, _ = spezza_righe(testo)
    for voce in voci:
        assert righe[voce["riga"] - 1].lstrip().startswith("ioriginalnameref")


# ---------------------------------------------------------------------------
# Il plurale dei nomi, che in `item_func.hsp` l'inglese fa col suffisso.
#
# Decisione del 2026-08-07: il plurale sta nel dizionario, una forma per nome,
# e viaggia fino al gioco in due array HSP nuovi (`ioriginalnamerefplur` e
# `ioriginalnameref2plur`) che `applica.py` popola accanto al singolare.
#
# La regola italiana non basta: «paio → paia», «asse → assi», e l'aggettivo si
# accorda col nome («spada lunga → spade lunghe»). Scritto a mano si sbaglia una
# volta; dedotto si sbaglia per sempre e in silenzio.
# ---------------------------------------------------------------------------
from strumenti.applica import applica_dati_nome


def test_le_voci_dei_nomi_portano_il_campo_plurale():
    voce = estrai_da_testo("db_item.hsp", BLOCCO)[0]
    assert voce["plurale"] == ""
    assert voce["oggetto"] == "ITEM_ID_BANANA"
    assert voce["array"] == "ioriginalnameref"


def test_le_voci_di_lang_non_lo_portano():
    """Solo i nomi hanno un array del plurale: aggiungerlo altrove sarebbe rumore."""
    voce = estrai_da_testo("text.hsp", 'a = lang("はい", "Yes")')[0]
    assert "plurale" not in voce
    assert "oggetto" not in voce


def test_il_secondo_riferimento_dichiara_il_suo_array():
    voci = estrai_da_testo("db_item.hsp", BLOCCO_COMPOSTO)
    assert [v["array"] for v in voci] == ["ioriginalnameref", "ioriginalnameref2"]


def _dizionario(testo, **plurali):
    voci = estrai_da_testo("db_item.hsp", testo)
    return {v["firma"]: {**v, "it": v["en"], "plurale": plurali.get(v["en"], "")}
            for v in voci}


def test_il_plurale_si_scrive_accanto_al_singolare():
    dizionario = _dizionario(BLOCCO, banana="banane")
    nuovo, quanti = applica_dati_nome("db_item.hsp", BLOCCO, dizionario)
    assert quanti == 1
    righe = nuovo.split("\n")
    assert righe[4] == '\t\tioriginalnameref(ITEM_ID_BANANA) = "banana"'
    assert righe[5] == '\t\tioriginalnamerefplur(ITEM_ID_BANANA) = "banane"'
    # la riga che seguiva non si perde
    assert righe[6] == '\t\tioriginalnameref2(ITEM_ID_BANANA) = ""'


def test_senza_plurale_non_si_scrive_niente():
    """Lo stato intermedio e' leggibile: il gioco ripiega sul singolare."""
    nuovo, quanti = applica_dati_nome("db_item.hsp", BLOCCO, _dizionario(BLOCCO))
    assert (nuovo, quanti) == (BLOCCO, 0)


def test_ogni_array_prende_il_suo_plurale():
    dizionario = _dizionario(BLOCCO_COMPOSTO, harvest="raccolti", scroll="pergamene")
    nuovo, quanti = applica_dati_nome("db_item.hsp", BLOCCO_COMPOSTO, dizionario)
    assert quanti == 2
    assert 'ioriginalnamerefplur(ITEM_ID_SCROLL_HARVEST) = "raccolti"' in nuovo
    assert 'ioriginalnameref2plur(ITEM_ID_SCROLL_HARVEST) = "pergamene"' in nuovo


def test_piu_blocchi_non_si_sfalsano():
    """L'inserimento sposta le righe: se si lavora dall'alto ci si perde."""
    testo = BLOCCO + BLOCCO_COMPOSTO
    dizionario = _dizionario(testo, banana="banane", harvest="raccolti", scroll="pergamene")
    nuovo, quanti = applica_dati_nome("db_item.hsp", testo, dizionario)
    assert quanti == 3
    assert 'ioriginalnamerefplur(ITEM_ID_BANANA) = "banane"' in nuovo
    assert 'ioriginalnamerefplur(ITEM_ID_SCROLL_HARVEST) = "raccolti"' in nuovo
    # nessuna riga originale persa
    for riga in testo.split("\n"):
        if riga.strip():
            assert riga in nuovo


def test_il_plurale_passa_dalla_degradazione_degli_accenti():
    """Come `it`: nel dizionario c'e' l'accento vero, nel sorgente CP932 no."""
    dizionario = _dizionario(BLOCCO, banana="virtù")
    nuovo, _ = applica_dati_nome("db_item.hsp", BLOCCO, dizionario)
    assert 'ioriginalnamerefplur(ITEM_ID_BANANA) = "virtu\'"' in nuovo


def test_il_plurale_si_inserisce_nel_testo_gia_tradotto():
    """L'ordine vero della catena: prima si sostituisce, poi si inserisce.

    Le firme si leggono dal sorgente, perche' nel tradotto non ci sono piu'.
    """
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: {**v, "it": "banana", "plurale": "banane"} for v in voci}
    tradotto, _ = applica_a_testo("db_item.hsp", BLOCCO, dizionario)
    nuovo, quanti = applica_dati_nome("db_item.hsp", BLOCCO, dizionario, tradotto)
    assert quanti == 1
    assert 'ioriginalnameref(ITEM_ID_BANANA) = "banana"' in nuovo
    assert 'ioriginalnamerefplur(ITEM_ID_BANANA) = "banane"' in nuovo


def test_due_testi_sfalsati_fermano_la_catena():
    from strumenti.applica import SorgenteCorrotto

    dizionario = _dizionario(BLOCCO, banana="banane")
    with pytest.raises(SorgenteCorrotto, match="sfalsati"):
        applica_dati_nome("db_item.hsp", BLOCCO, dizionario, BLOCCO + "\tx = 1\n")


# ---------------------------------------------------------------------------
# La guardia del plurale del nome: solo quando NON c'e' parola-contatore.
#
# Trovata il 2026-08-08, leggendo il sorgente prima del primo lotto di nomi.
# Il pluralizzatore inglese che le toppe spengono (`item_func.hsp:1842`) era
# protetto da `if ( locvar_itemname_s2 == "" )`: in inglese si flette la
# parola-contatore **oppure** il nome, mai tutti e due. «3 scrolls of identify»,
# non «3 scrolls of identifies».
#
# In italiano vale lo stesso, e per la stessa ragione grammaticale: la testa del
# sintagma e' il contatore, e il complemento dopo «di» resta al singolare —
# «3 pergamene di identificazione». Le tre toppe dei siti di concatenazione
# avevano perso quella guardia: con `plurale` pieno su entrambe le voci del
# blocco composto avrebbero scritto «3 pergamene di identificazioni».
#
# La difesa e' nel codice e non nel dato: `verifica.py` pretende il `plurale` su
# ogni nome tradotto, quindi la coda di un composto un plurale ce l'ha per forza.
# ---------------------------------------------------------------------------

def test_il_plurale_del_nome_si_usa_solo_senza_parola_contatore():
    from strumenti.applica import carica_toppe

    # solo le toppe che **leggono** il plurale: la dichiarazione degli array e
    # il commento della toppa che spegne il pluralizzatore inglese lo nominano
    # soltanto
    interessate = [t for t in carica_toppe()
                   if "= ioriginalnamerefplur(" in "\n".join(
                       t["sostituisci"] if isinstance(t["sostituisci"], list)
                       else [t["sostituisci"]])]
    assert len(interessate) == 3, (
        "i siti di concatenazione del nome sono tre (item_func.hsp:1731, 1747,"
        f" 1770): trovate {len(interessate)} toppe che leggono il plurale")
    for toppa in interessate:
        testo = "\n".join(toppa["sostituisci"])
        assert 'locvar_itemname_s2 == ""' in testo, (
            "il plurale del nome va usato solo quando non c'e' parola-contatore,"
            " come faceva il pluralizzatore inglese spento a item_func.hsp:1842."
            " Senza la guardia esce «3 pergamene di identificazioni»")


def test_gli_array_del_plurale_sono_dimensionati():
    """Un array **sparso** va dimensionato: leggerlo oltre e' un overflow.

    Crash del 2026-08-08, in gioco, aprendo la lista di un negoziante:
    `HspError 7 — Array overflow`, in `itemName`. La toppa dichiarava
    `sdim ioriginalnamerefplur` senza dimensione, com'e' dichiarato
    `ioriginalnameref` che affianca, e il motivo diceva «si autoespande
    all'assegnazione». E' vero, ma l'autoespansione vale **in scrittura**:
    in lettura un indice mai assegnato e' fuori dall'array e il gioco muore.

    La differenza fra i due array e' che `ioriginalnameref` lo assegna
    `db_item.hsp` per **ogni** oggetto, quindi arriva sempre in fondo; il
    plurale ce l'hanno solo i nomi tradotti — 86 su 1.606 — e gli ID degli
    oggetti vanilla sono bassi. Bastava un oggetto con ID alto in una pila da
    due (il negozio ne e' pieno) per leggere oltre la fine.

    La regola generale: un array dichiarato senza dimensione e' sicuro solo se
    chi lo riempie lo riempie tutto. Il nostro e' sparso per costruzione.
    """
    from strumenti.applica import carica_toppe

    dichiarazioni = [t for t in carica_toppe()
                     if any("sdim ioriginalnamerefplur" in r
                            for r in t["sostituisci"])]
    assert len(dichiarazioni) == 1, "la dichiarazione degli array del plurale e' una sola"
    righe = [r for r in dichiarazioni[0]["sostituisci"] if "plur" in r]
    assert len(righe) == 2, righe
    for riga in righe:
        assert "MAX_DB" in riga, (
            f"{riga!r}: l'array del plurale e' sparso (solo i nomi tradotti ne"
            " hanno uno) e va dimensionato a MAX_DB, o leggere l'ID di un"
            " oggetto non tradotto e' un Array overflow — crash in negozio")


# ---------------------------------------------------------------------------
# Le sei parole-contatore cablate in `item_func.hsp` (2026-08-08).
#
# Viste a schermo: «2 bottle di juice». Non stanno in `db_item.hsp` e non
# passano da `lang()`: sono letterali inglesi dentro `itemname()`, assegnati per
# classe di oggetto — succo, caffe', te', merce pesante, guanti e stivali, cibo
# cucinato. Il dizionario non le raggiunge, e il loro plurale inglese lo faceva
# proprio il pluralizzatore che la toppa 8 spegne: senza toppa hanno perso anche
# quello, e «2 bottles of juice» era diventato «2 bottle di juice» — una
# regressione rispetto all'inglese.
#
# Le rese sono gia' decise in `contatori.jsonl` (paio/paia, piatto/piatti): il
# dato c'era, mancava il codice che lo legge.
# ---------------------------------------------------------------------------

CABLATE = (("bottle", "bottiglia", "bottiglie"), ("cup", "tazza", "tazze"),
           ("cargo", "carico", "carichi"), ("pair", "paio", "paia"),
           ("dish", "piatto", "piatti"))


def _item_func_toppato():
    from strumenti.applica import applica_toppe, carica_toppe
    percorso = percorsi.SORGENTE_HSP / "item_func.hsp"
    if not percorso.exists():
        pytest.skip("il clone del sorgente non e' disponibile")
    testo = percorso.read_bytes().decode("cp932")
    toppe = [t for t in carica_toppe() if t["file"] == "item_func.hsp"]
    nuovo, _ = applica_toppe("item_func.hsp", testo, toppe)
    return nuovo


def test_le_parole_contatore_cablate_diventano_italiane():
    nuovo = _item_func_toppato()
    for inglese, italiano, _ in CABLATE:
        assert f'locvar_itemname_s2 += "{inglese}"' not in nuovo, inglese
        assert f'locvar_itemname_s2 = "{inglese}"' not in nuovo, inglese
        assert f'"{italiano}"' in nuovo, italiano


def test_le_parole_contatore_cablate_hanno_il_loro_plurale():
    # non ce l'hanno dal dizionario -- non sono nomi di `db_item.hsp` -- quindi
    # il ripiego sul singolare le lascerebbe a «2 bottiglia di succo»
    nuovo = _item_func_toppato()
    for _, italiano, plurale in CABLATE:
        assert f'"{plurale}"' in nuovo, plurale


# ---------------------------------------------------------------------------
# Il materiale: si mette da parte e si riversa dopo il nome (2026-08-08).
#
# Visto a schermo: «bronze corazza», «silk veste», «raw cintura» — 12 righe su
# 16 nella lista di un negoziante. In inglese il materiale precede; in italiano
# e' un complemento che segue, ed e' gia' la regola di `guida-stile.md`:
# «spada d'acciaio», mai «spada acciaiosa».
#
# I nomi dei materiali stanno in `item_data.hsp` dentro normali `lang()`, quindi
# la catena li raggiunge senza inventare niente. Due vincoli, misurati:
#
# - **il materiale resta un sostantivo nudo**, perche' `command.hsp:16289` dice
#   «It is made of » + mtname(...): col «di» cotto nel dato uscirebbe «fatto di
#   di cuoio». Il giunto va nella toppa. E' la seconda volta che questo progetto
#   impara la stessa cosa, dopo il `" of "` dei nomi composti;
# - **il buffer e' di 18 byte** (`sdim mtname, 18, 2, ITEM_MATERIAL_MAX`), e in
#   italiano non ci si sta: «scaglia di grifone» sono 18 esatti, e un accento
#   vero ne vale due dopo la degradazione. Si allarga la dichiarazione, come per
#   gli array del plurale: e' lo stesso difetto visto dal lato del buffer.
# ---------------------------------------------------------------------------

SITI_MATERIALE = ("mtname(0, inv(INV_ITEM_MATERIAL, itemname_itemid))",
                  "mtname(1, inv(INV_ITEM_MATERIAL, itemname_itemid))")


def test_il_materiale_non_si_antepone_piu_al_nome():
    # solo **prima** di `*skipName`: dopo, il nome c'e' gia' e un `+=` con
    # mtname e' un suffisso legittimo -- la targhetta `[Bronzo]` di riga 2175,
    # che era gia' al posto giusto e non va spostata
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    for spoglia in righe[:righe.index("*skipName")]:
        if "mtname(" in spoglia and spoglia.startswith("locvar_itemowner_s +="):
            raise AssertionError(
                f"{spoglia!r}: il materiale si antepone ancora. In italiano segue"
                " il nome, quindi va messo da parte in locvar_itemname_s6 e"
                " riversato dopo")


def test_il_materiale_si_riversa_dopo_il_nome_una_volta_sola():
    # il riversamento sta dopo `*skipName`, che e' il punto in cui **tutti** i
    # rami del nome convergono: metterlo sui singoli rami significherebbe
    # dimenticarne uno e perdere il materiale in silenzio
    nuovo = _item_func_toppato()
    righe = [r.strip() for r in nuovo.split("\r\n")]
    flussi = [i for i, r in enumerate(righe)
              if r == "locvar_itemowner_s += locvar_itemname_s6"]
    assert len(flussi) == 1, f"riversamenti trovati: {len(flussi)}"
    etichetta = righe.index("*skipName")
    assert etichetta < flussi[0] < etichetta + 4, (
        "il riversamento va subito dopo *skipName, dove tutti i rami del nome"
        " sono gia' passati e l'articolo non e' ancora stato anteposto")


def test_il_materiale_si_azzera_a_ogni_chiamata():
    nuovo = _item_func_toppato()
    righe = [r.strip() for r in nuovo.split("\r\n")]
    assert righe.count('locvar_itemname_s6 = ""') == 1
    assert righe.index('locvar_itemname_s6 = ""') < righe.index("*skipName")


def test_il_buffer_dei_materiali_sta_largo_per_l_italiano():
    from strumenti.applica import applica_toppe, carica_toppe
    percorso = percorsi.SORGENTE_HSP / "item_data.hsp"
    if not percorso.exists():
        pytest.skip("il clone del sorgente non e' disponibile")
    testo = percorso.read_bytes().decode("cp932")
    toppe = [t for t in carica_toppe() if t["file"] == "item_data.hsp"]
    nuovo, _ = applica_toppe("item_data.hsp", testo, toppe)
    assert "sdim mtname, 18, 2, ITEM_MATERIAL_MAX" not in nuovo
    assert "sdim mtname, 48, 2, ITEM_MATERIAL_MAX" in nuovo


# ---------------------------------------------------------------------------
# Benedizione e maledizione: complementi, come gli epiteti (2026-08-08).
#
# `strblessed`/`strcursed`/`strdoomed` si antepongono al nome
# (`item_func.hsp:1204, 1207, 1210`, ramo inglese). In italiano «benedetto»
# segue il nome **e si accorda**: «mantello benedetto», «pozione benedetta».
# Il genere non si conosce, come per gli epiteti del materiale, e la soluzione
# e' la stessa: un complemento che non chiede accordo a nessuno.
#
# Erano in `rinviate.jsonl` dal 2026-08-07, e il motivo diceva «va deciso
# insieme ai nomi di db_item.hsp, che la Fase 1 dichiara di non risolvere».
# Quella premessa e' caduta il 2026-08-08, quando i nomi sono entrati nella
# catena. L'altra meta' del motivo -- il sistema dei nomi casuali -- resta.
# ---------------------------------------------------------------------------

def test_lo_stato_dell_oggetto_non_si_antepone_piu():
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    prima_del_nome = righe[:righe.index("*skipName")]
    for stato in ("strblessed", "strcursed", "strdoomed"):
        anteposti = [r for r in prima_del_nome
                     if r.startswith("locvar_itemowner_s") and stato in r]
        # nel ramo `jp` resta al suo posto: li' l'ordine e' quello giusto
        assert len(anteposti) == 1, f"{stato}: {anteposti}"
        assert "locvar_itemname_s2 = " not in anteposti[0]


def test_lo_stato_si_riversa_dopo_il_materiale():
    # «mantello leggero di platino con benedizione»: prima il materiale, poi
    # lo stato. Sono due code distinte proprio per questo -- una sola le
    # metterebbe nell'ordine in cui l'inglese le scrive, che e' l'inverso
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    materiale = righe.index("locvar_itemowner_s += locvar_itemname_s6")
    stato = righe.index("locvar_itemowner_s += locvar_itemname_s7")
    assert materiale < stato
    assert righe.count('locvar_itemname_s7 = ""') == 1


# ---------------------------------------------------------------------------
# L'articolo: derivato dal genere, e scritto SOLO sulla testa del nome.
#
# Decisione del 2026-08-08. L'inglese sceglie `a`/`an` guardando la prima
# lettera della stringa composta (`item_func.hsp:1816`), che e' una regola di
# fonetica. In italiano l'articolo dipende dal **genere del sostantivo testa**,
# che sta in mezzo alla stringa e non si deduce da nessuna lettera. Il genere e'
# quindi un dato, come il plurale; l'articolo no, perche' una volta noto il
# genere la scelta fra «un» e «uno» e' meccanica.
# ---------------------------------------------------------------------------

def _dizionario_genere(testo, **generi):
    """Come `_dizionario`, ma riempie `genere` invece del plurale."""
    voci = estrai_da_testo("db_item.hsp", testo)
    return {v["firma"]: {**v, "it": v["en"], "plurale": v["en"],
                         "genere": generi.get(v["en"], "")}
            for v in voci}


def test_le_voci_dei_nomi_portano_il_campo_genere():
    voce = estrai_da_testo("db_item.hsp", BLOCCO)[0]
    assert voce["genere"] == ""


def test_le_voci_di_lang_non_portano_il_genere():
    """Nessuna `lang()` finisce dietro un articolo scelto dal codice."""
    voce = estrai_da_testo("text.hsp", 'a = lang("はい", "Yes")')[0]
    assert "genere" not in voce


def test_l_articolo_si_scrive_sul_nome_semplice():
    dizionario = _dizionario_genere(BLOCCO, banana="f")
    nuovo, _ = applica_dati_nome("db_item.hsp", BLOCCO, dizionario)
    assert 'ioriginalnamearticolo(ITEM_ID_BANANA) = "una "' in nuovo
    assert 'ioriginalnamearticolodet(ITEM_ID_BANANA) = "la "' in nuovo


def test_sul_composto_l_articolo_lo_regge_la_testa_e_non_il_complemento():
    """«una pergamena di raccolto», non «un raccolto»: davanti sta `ref2`."""
    dizionario = _dizionario_genere(BLOCCO_COMPOSTO, scroll="f", harvest="m")
    nuovo, _ = applica_dati_nome("db_item.hsp", BLOCCO_COMPOSTO, dizionario)
    assert 'ioriginalnamearticolo(ITEM_ID_SCROLL_HARVEST) = "una "' in nuovo
    # il complemento non ne scrive uno suo: ce n'e' uno solo per oggetto
    assert nuovo.count("ioriginalnamearticolo(ITEM_ID_SCROLL_HARVEST)") == 1


def test_senza_genere_non_si_scrive_niente():
    """Ripiego leggibile, come per il plurale: resta l'articolo inglese."""
    nuovo, _ = applica_dati_nome("db_item.hsp", BLOCCO, _dizionario_genere(BLOCCO))
    assert "ioriginalnamearticolo" not in nuovo


def test_l_elisione_arriva_fino_al_sorgente():
    """«un'incudine» senza spazio, «uno scudo» con: la stringa e' gia' pronta."""
    dizionario = _dizionario_genere(BLOCCO, banana="f")
    dizionario = {k: {**v, "it": "incudine"} for k, v in dizionario.items()}
    nuovo, _ = applica_dati_nome("db_item.hsp", BLOCCO, dizionario)
    assert 'ioriginalnamearticolo(ITEM_ID_BANANA) = "un\'"' in nuovo
    assert 'ioriginalnamearticolodet(ITEM_ID_BANANA) = "l\'"' in nuovo


def test_plurale_e_articolo_stanno_nello_stesso_blocco():
    """Le due righe gemelle si inseriscono insieme, senza sfalsare le altre."""
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: {**v, "it": "banana", "plurale": "banane",
                               "genere": "f"} for v in voci}
    nuovo, quante = applica_dati_nome("db_item.hsp", BLOCCO, dizionario)
    assert quante == 3
    righe = nuovo.split("\n")
    assert righe[4] == '\t\tioriginalnameref(ITEM_ID_BANANA) = "banana"'
    assert righe[5] == '\t\tioriginalnamerefplur(ITEM_ID_BANANA) = "banane"'
    assert righe[6] == '\t\tioriginalnamearticolo(ITEM_ID_BANANA) = "una "'
    assert righe[7] == '\t\tioriginalnamearticolodet(ITEM_ID_BANANA) = "la "'
    assert righe[8] == '\t\tioriginalnameref2(ITEM_ID_BANANA) = ""'


# ---------------------------------------------------------------------------
# La qualita' dell'arredo: complementi, come materiale ed epiteti (2026-08-08).
#
# `_furniture` (`text.hsp:56`) sono undici gradini che l'inglese antepone al
# nome (`item_func.hsp:1324`). E' la sesta volta che si presenta la stessa
# forma -- un prefisso a un nome di **genere ignoto** -- e la cura non cambia:
# spostarli in coda e renderli con complementi che non chiedono accordo.
#
# Qui il vincolo e' piu' stretto che altrove: l'arredamento comprende nomi che
# esistono solo al plurale («dei libri sparsi»), quindi la resa deve essere
# invariante per genere **e** per numero. «malandato» fallirebbe su entrambi.
# ---------------------------------------------------------------------------

def test_la_qualita_dell_arredo_non_si_antepone_piu():
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    for spoglia in righe[:righe.index("*skipName")]:
        if "_furniture(" in spoglia and spoglia.startswith("locvar_itemowner_s +="):
            assert "itemowner_itemid" in spoglia, (
                f"{spoglia!r}: la qualita' dell'arredo si antepone ancora nel"
                " ramo inglese. In italiano segue il nome, quindi va messa da"
                " parte in locvar_itemname_s6 e riversata dopo")


def test_il_ramo_giapponese_dell_arredo_resta_intatto():
    """Riga 1077: sta dentro `if ( jp )`, dove l'ordine e' gia' quello giusto."""
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    intatte = [r for r in righe
               if r == "locvar_itemowner_s += _furniture("
                       "inv(INV_ITEM_SUB_NAME, itemowner_itemid))"]
    assert len(intatte) == 1, intatte


def test_la_qualita_dell_arredo_precede_il_materiale_nella_coda():
    """Nella stessa coda s6, e prima: «tavolo di buona fattura di seta».

    Non e' una convenzione ma una conseguenza: il sito dell'arredo (1324) gira
    prima di quelli del materiale (1386+), quindi due `+=` sulla stessa coda
    bastano e non serve una terza coda da azzerare.
    """
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    arredo = [i for i, r in enumerate(righe)
              if r.startswith("locvar_itemname_s6 +=") and "_furniture(" in r]
    materiale = [i for i, r in enumerate(righe)
                 if r.startswith("locvar_itemname_s6 +=") and "mtname(" in r]
    assert len(arredo) == 1, arredo
    assert materiale, "nessun materiale in coda: la toppa del materiale e' sparita"
    assert arredo[0] < min(materiale)


def test_le_rese_dell_arredo_sono_complementi_non_aggettivi():
    """Un aggettivo si accorderebbe; questi undici non possono permetterselo."""
    from strumenti.reimporta import carica_dizionario

    voci = [v for v in carica_dizionario("text.hsp").values()
            if v.get("riga") == 56 and v.get("it")]
    assert len(voci) == 11, f"attese 11 rese di _furniture, trovate {len(voci)}"
    teste = {"di", "da", "dal", "che", "senza", "con", "in", "a"}
    for v in voci:
        prima = v["it"].split()[0]
        assert prima in teste, (
            f"{v['en']} -> {v['it']!r}: comincia per {prima!r}, che non e' una"
            " testa di complemento. Un aggettivo si accorderebbe con un nome"
            " di genere e numero ignoti -- l'arredamento ha anche plurali")


# ---------------------------------------------------------------------------
# La taglia e la qualita' del manoscritto (2026-08-08).
#
# Questi due NON sono la forma di `_furniture`, per quanto il documento di
# ripresa li desse per identici. Sono gia' suffissi anche in inglese, quindi
# non c'e' niente da spostare -- e la cura e' un'altra per ciascuno:
#
# `_weight` (text.hsp:57) esce come « grown huge » (item_func.hsp:974). Un
# aggettivo italiano in coda si accorderebbe lo stesso col nome. La leva e' il
# **giunto**: « di taglia » introduce una testa femminile e fissa, e da li' in
# poi l'accordo e' con «taglia», non con l'oggetto.
#
# `_bookself` (text.hsp:54) esce gia' fra parentesi (item_func.hsp:988), dove
# sta da sola e non si accorda con niente. Non chiede nessuna toppa: e' solo
# dato, ed e' l'unico caso di questa famiglia in cui il codice andava bene.
# ---------------------------------------------------------------------------

def test_il_giunto_della_taglia_diventa_di_taglia():
    nuovo = _item_func_toppato()
    assert 'lang("", " grown ")' not in nuovo, (
        "il giunto inglese e' ancora li': le rese di _weight si accorderebbero"
        " con l'oggetto invece che con «taglia»")
    assert 'lang("", " di taglia ")' in nuovo


def test_le_rese_della_taglia_si_accordano_con_taglia():
    """Femminili singolari, perche' seguono «di taglia»."""
    from strumenti.reimporta import carica_dizionario

    voci = [v for v in carica_dizionario("text.hsp").values()
            if v.get("riga") == 57 and v.get("it")]
    assert len(voci) == 10, f"attese 10 rese di _weight, trovate {len(voci)}"
    for v in voci:
        ultima = v["it"].split()[-1]
        assert not ultima.endswith(("o", "i")), (
            f"{v['en']} -> {v['it']!r}: {ultima!r} finisce da maschile o da"
            " plurale, ma segue «di taglia», che e' femminile singolare")


def test_la_qualita_del_manoscritto_resta_dov_e():
    """Riga 988: l'inglese la mette gia' fra parentesi. Niente da spostare."""
    righe = [r.strip() for r in _item_func_toppato().split("\r\n")]
    parentesi = [r for r in righe if "_bookself(" in r and '" ("' in r]
    assert len(parentesi) == 1, (
        f"il sito fra parentesi non e' piu' uno solo: {parentesi}")


# ---------------------------------------------------------------------------
# Il libro prodotto dal giocatore: una testa, non un prefisso (2026-08-08).
#
# `_bookselfs` (text.hsp:55) finisce in `locvar_itemname_s2`
# (item_func.hsp:1233), lo slot della **parola-contatore**. E' percio' la forma
# di `contatori.jsonl` e non quella di `_furniture`: niente da spostare, ma
# singolare, plurale, genere e un `case` in **entrambi** gli switch.
#
# Il legame fra i due file e' per stringa: il `case` confronta la resa di
# `contatori.jsonl` con quella che l'array porta a runtime, che viene dal
# dizionario. Se divergono, il case non aggancia mai -- e non lo dice nessuno,
# ne' il compilatore ne' la prova d'identita'. Da qui il primo test.
# ---------------------------------------------------------------------------

def _teste_da_text():
    """Le teste di s2 che arrivano da un array di text.hsp, da contatori.jsonl."""
    import json

    righe = (percorsi.PROGETTO / "contatori.jsonl").read_text(encoding="utf-8")
    return [json.loads(r) for r in righe.splitlines()
            if r.strip() and json.loads(r).get("fonte") == "text"]


def test_contatori_e_dizionario_concordano_sulle_teste_di_s2():
    from strumenti.reimporta import carica_dizionario

    rese = {v["en"]: v.get("it")
            for v in carica_dizionario("text.hsp").values() if v.get("riga") == 55}
    teste = _teste_da_text()
    assert len(teste) == 7, f"attese 7 teste da text.hsp, trovate {len(teste)}"
    for testa in teste:
        assert rese.get(testa["en"]) == testa["it"], (
            f"{testa['en']}: contatori.jsonl dice {testa['it']!r}, il dizionario"
            f" {rese.get(testa['en'])!r}. Il `case` confronta le due stringhe:"
            " se divergono non aggancia mai, in silenzio")


def test_le_due_scale_del_libro_sono_la_stessa_scala():
    """`_bookself` e `_bookselfs` differiscono solo per la testa «libro»."""
    from strumenti.reimporta import carica_dizionario

    voci = carica_dizionario("text.hsp").values()
    manoscritto = {v["en"]: v["it"] for v in voci if v.get("riga") == 54 and v.get("it")}
    libro = {v["en"]: v["it"] for v in voci if v.get("riga") == 55 and v.get("it")}
    assert len(manoscritto) == 7 and len(libro) == 7, (manoscritto, libro)
    for en, resa in manoscritto.items():
        assert libro[f"{en} book"] == f"libro {resa}", (
            f"{en}: «{resa}» contro «{libro[f'{en} book']}». Sono la stessa"
            " qualita' vista in due punti: due scale diverse si leggerebbero"
            " come due cose diverse")


# ---------------------------------------------------------------------------
# Le 39 teste che vengono da db_item.hsp (2026-08-09).
#
# `contatori.jsonl` ha tre fonti: `text` (le sette del libro prodotto),
# `item_func` (le sei cablate) e `db_item` (39). Le prime due alimentano
# `genera_toppe_nomi.py` ed erano gia' difese. Le 39 no: sono un **registro**
# di cio' che il dizionario dice per lo slot `ioriginalnameref2`, e su di esse
# non guardava nessuno.
#
# Il confronto non e' l'uguaglianza, ed e' `grave` a insegnarlo. Il nome si
# monta come `s2 + " " + s3 + " " + s1`, e la toppa 3 fissa il giunto a «di».
# Per ITEM_ID_GRAVE_ORNAMENTED_WITH_FLOWERS le due parti sono «tomba ornata» e
# «fiori», che danno «tomba ornata di fiori». L'aggettivo sta in `s2` perche'
# **e' li' che puo' accordarsi con la testa**: con «tomba» in `s2` uscirebbe
# «tomba di ornata di fiori», e con «tomba» piu' «fiori» si perderebbe del
# tutto l'«ornamented».
#
# Quindi il registro dice il **termine** e il dizionario dice il **segmento**,
# che porta l'accordo. Sono due livelli, non due verita' in conflitto. Il test
# vive al livello che li tiene insieme: la resa del dizionario **comincia con**
# il termine del registro. Cosi' prende i 38 casi identici e accetta la
# variante contestuale senza costringere a dichiarare un'eccezione falsa.
#
# Se un domani una variante non fosse un prefisso, allora si' che andrebbe
# dichiarata: sarebbe una testa diversa, non la stessa testa accordata.
# ---------------------------------------------------------------------------

def _teste_da_db_item():
    """Le teste di s2 che vengono dallo slot ioriginalnameref2 di db_item.hsp."""
    import json

    righe = (percorsi.PROGETTO / "contatori.jsonl").read_text(encoding="utf-8")
    return [json.loads(r) for r in righe.splitlines()
            if r.strip() and json.loads(r).get("fonte") == "db_item"]


def test_il_dizionario_non_contraddice_il_registro_delle_teste_di_db_item():
    from strumenti.reimporta import carica_dizionario

    rese: dict[str, set[str]] = {}
    for voce in carica_dizionario("db_item.hsp").values():
        if voce.get("array") == "ioriginalnameref2" and voce.get("it"):
            rese.setdefault(voce["en"], set()).add(voce["it"])

    teste = _teste_da_db_item()
    assert len(teste) == 39, f"attese 39 teste da db_item.hsp, trovate {len(teste)}"
    for testa in teste:
        varianti = rese.get(testa["en"])
        assert varianti, (
            f"{testa['en']}: contatori.jsonl lo registra come testa di"
            " ioriginalnameref2, ma il dizionario non ha nessuna voce tradotta"
            " in quello slot. O il registro e' vecchio, o la voce e' sfuggita")
        for variante in sorted(varianti):
            assert variante.startswith(testa["it"]), (
                f"{testa['en']}: il registro dice {testa['it']!r}, il dizionario"
                f" {variante!r}, che non ne e' una specificazione. Se e' voluto"
                " e' una testa diversa, e va dichiarata invece che divergere in"
                " silenzio")


def test_il_libro_prodotto_ha_un_case_in_entrambi_gli_switch():
    """Senza, cadrebbe nel default: «2 libro sublime» e l'articolo dell'array."""
    nuovo = _item_func_toppato()
    for testa in _teste_da_text():
        assert nuovo.count(f'case "{testa["it"]}"') == 2, (
            f"{testa['it']}: servono due case, uno per il plurale e uno per"
            " l'articolo")
        assert f'locvar_itemname_s5 = "{testa["plurale"]}"' in nuovo
