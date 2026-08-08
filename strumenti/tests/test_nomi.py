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
from strumenti.applica import applica_plurali


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
    nuovo, quanti = applica_plurali("db_item.hsp", BLOCCO, dizionario)
    assert quanti == 1
    righe = nuovo.split("\n")
    assert righe[4] == '\t\tioriginalnameref(ITEM_ID_BANANA) = "banana"'
    assert righe[5] == '\t\tioriginalnamerefplur(ITEM_ID_BANANA) = "banane"'
    # la riga che seguiva non si perde
    assert righe[6] == '\t\tioriginalnameref2(ITEM_ID_BANANA) = ""'


def test_senza_plurale_non_si_scrive_niente():
    """Lo stato intermedio e' leggibile: il gioco ripiega sul singolare."""
    nuovo, quanti = applica_plurali("db_item.hsp", BLOCCO, _dizionario(BLOCCO))
    assert (nuovo, quanti) == (BLOCCO, 0)


def test_ogni_array_prende_il_suo_plurale():
    dizionario = _dizionario(BLOCCO_COMPOSTO, harvest="raccolti", scroll="pergamene")
    nuovo, quanti = applica_plurali("db_item.hsp", BLOCCO_COMPOSTO, dizionario)
    assert quanti == 2
    assert 'ioriginalnamerefplur(ITEM_ID_SCROLL_HARVEST) = "raccolti"' in nuovo
    assert 'ioriginalnameref2plur(ITEM_ID_SCROLL_HARVEST) = "pergamene"' in nuovo


def test_piu_blocchi_non_si_sfalsano():
    """L'inserimento sposta le righe: se si lavora dall'alto ci si perde."""
    testo = BLOCCO + BLOCCO_COMPOSTO
    dizionario = _dizionario(testo, banana="banane", harvest="raccolti", scroll="pergamene")
    nuovo, quanti = applica_plurali("db_item.hsp", testo, dizionario)
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
    nuovo, _ = applica_plurali("db_item.hsp", BLOCCO, dizionario)
    assert 'ioriginalnamerefplur(ITEM_ID_BANANA) = "virtu\'"' in nuovo


def test_il_plurale_si_inserisce_nel_testo_gia_tradotto():
    """L'ordine vero della catena: prima si sostituisce, poi si inserisce.

    Le firme si leggono dal sorgente, perche' nel tradotto non ci sono piu'.
    """
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: {**v, "it": "banana", "plurale": "banane"} for v in voci}
    tradotto, _ = applica_a_testo("db_item.hsp", BLOCCO, dizionario)
    nuovo, quanti = applica_plurali("db_item.hsp", BLOCCO, dizionario, tradotto)
    assert quanti == 1
    assert 'ioriginalnameref(ITEM_ID_BANANA) = "banana"' in nuovo
    assert 'ioriginalnamerefplur(ITEM_ID_BANANA) = "banane"' in nuovo


def test_due_testi_sfalsati_fermano_la_catena():
    from strumenti.applica import SorgenteCorrotto

    dizionario = _dizionario(BLOCCO, banana="banane")
    with pytest.raises(SorgenteCorrotto, match="sfalsati"):
        applica_plurali("db_item.hsp", BLOCCO, dizionario, BLOCCO + "\tx = 1\n")


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
