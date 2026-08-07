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
