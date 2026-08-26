# strumenti/tests/test_descrizioni.py
"""Il TERZO tipo di sito: le descrizioni degli oggetti di `db_item.hsp`.

Vedi `contratto-nomi.md` §1 (che le aveva gia' segnate come aperte) e la
sezione della 107a in `decisioni.md`. Come i nomi, stanno fuori da `lang()` in
un `if ( jp ) … else …`; a differenza dei nomi, il blocco e' **indicizzato** —
`description(0)` … `description(3)` — e la coppia (giapponese, inglese) si fa
per **indice**, non per posizione nel blocco.

⚠️⚠️ La cosa che non si vede, e senza la quale il riconoscitore sarebbe
plausibile e sbagliato: se il ramo giapponese e quello inglese non portano gli
**stessi** indici, accoppiarli per posizione darebbe a ogni descrizione il
giapponese di un'altra — una firma valida su una coppia falsa, cioe' un guasto
silenzioso che nessuna verifica successiva puo' vedere. Sul sorgente pinnato
gli asimmetrici sono zero, ma il riconoscitore non ci fa affidamento: pretende
che i due insiemi di indici coincidano, e se no lascia stare il blocco.

Il giudice vero non e' qui: e' la prova d'identita', che attraversa il file
intero e pretende di riprodurlo byte per byte.
"""
import pytest

from strumenti import percorsi
from strumenti.applica import applica_a_testo
from strumenti.estrai import (avvio_descrizione, estrai_da_testo, siti,
                              spezza_righe)
from strumenti.prova_identita import dizionario_identita

BLOCCO = (
    "\t\tif ( dbmode == DBMODE_DESC ) {\n"
    "\t\t\tif ( jp ) {\n"
    '\t\t\t\tdescription(0) = "麻酔銃。"\n'
    '\t\t\t\tdescription(1) = "射手の言葉。"\n'
    '\t\t\t\tdescription(2) = ""\n'
    '\t\t\t\tdescription(3) = "鑑定報告書。"\n'
    "\t\t\t}\n"
    "\t\t\telse {\n"
    '\t\t\t\tdescription(0) = "A tranquilizer rifle."\n'
    '\t\t\t\tdescription(1) = "Words of a marksman."\n'
    '\t\t\t\tdescription(2) = ""\n'
    '\t\t\t\tdescription(3) = "(Reusable) Dart rifle."\n'
    "\t\t\t}\n"
    "\t\t\treturn\n"
    "\t\t}\n"
)


def _coppie(testo):
    return [(s[3], s[5]) for s in siti(testo)]


# ---------------------------------------------------------------------------
# la forma
# ---------------------------------------------------------------------------

def test_le_descrizioni_inglesi_sono_siti():
    assert _coppie(BLOCCO) == [
        ("麻酔銃。", "A tranquilizer rifle."),
        ("射手の言葉。", "Words of a marksman."),
        ("鑑定報告書。", "(Reusable) Dart rifle."),
    ]


def test_il_ramo_giapponese_non_e_un_sito():
    """Quattro righe per ramo, ma i siti sono tre: le vuote non contano e il
    giapponese non si traduce."""
    assert len(list(siti(BLOCCO))) == 3


def test_la_descrizione_vuota_non_e_un_sito():
    """2.452 righe su 5.284 sono la stringa vuota: `emetti` le scarta gia', e
    questo test dice che il riconoscitore non ci si mette di traverso."""
    assert all(en for _, en in _coppie(BLOCCO))


def test_l_accoppiamento_e_per_indice_non_per_posizione():
    """⚠️ Il test che conta. Se il ramo giapponese salta un indice, accoppiare
    per posizione darebbe a `description(2)` il giapponese di `description(1)`.
    """
    storto = (
        "\t\tif ( dbmode == DBMODE_DESC ) {\n"
        "\t\t\tif ( jp ) {\n"
        '\t\t\t\tdescription(0) = "ゼロ"\n'
        '\t\t\t\tdescription(2) = "ドゥエ"\n'
        "\t\t\t}\n"
        "\t\t\telse {\n"
        '\t\t\t\tdescription(0) = "zero"\n'
        '\t\t\t\tdescription(2) = "due"\n'
        "\t\t\t}\n"
        "\t\t\treturn\n"
        "\t\t}\n"
    )
    assert _coppie(storto) == [("ゼロ", "zero"), ("ドゥエ", "due")]


def test_un_blocco_asimmetrico_non_si_aggancia():
    """Indici diversi nei due rami: il blocco si lascia stare **intero**.

    Tradurre la meta' che combacia e' peggio che non tradurre niente: la parte
    agganciata sembrerebbe a posto e nessuno andrebbe piu' a guardare l'altra.
    """
    asimmetrico = (
        "\t\tif ( dbmode == DBMODE_DESC ) {\n"
        "\t\t\tif ( jp ) {\n"
        '\t\t\t\tdescription(0) = "ゼロ"\n'
        "\t\t\t}\n"
        "\t\t\telse {\n"
        '\t\t\t\tdescription(0) = "zero"\n'
        '\t\t\t\tdescription(1) = "uno"\n'
        "\t\t\t}\n"
        "\t\t\treturn\n"
        "\t\t}\n"
    )
    assert _coppie(asimmetrico) == []


def test_fuori_da_dbmode_desc_non_si_aggancia():
    """`db_item.hsp` ha 2.902 `if ( jp )` e solo 1.321 sono descrizioni.

    Un `description()` fuori da `DBMODE_DESC` oggi non esiste — 10.568 righe su
    10.568 stanno dentro — e proprio per questo agganciarlo per analogia sarebbe
    il modo di corrompere il sorgente in silenzio il giorno che ne comparisse uno.
    """
    fuori = (
        "\t\tif ( jp ) {\n"
        '\t\t\tdescription(0) = "ゼロ"\n'
        "\t\t}\n"
        "\t\telse {\n"
        '\t\t\tdescription(0) = "zero"\n'
        "\t\t}\n"
    )
    assert _coppie(fuori) == []


# ---------------------------------------------------------------------------
# l'oggetto a cui la descrizione appartiene
#
# ⭐ Non e' una comodita' per scegliere i lotti: e' la chiave che lega la
# descrizione al NOME ITALIANO gia' reso dello stesso oggetto. E' la stessa
# dipendenza per cui esiste `_102-dossier.py` sulle carte — la prosa e il nome
# sono l'unico posto in cui il giocatore vede le due cose vicine, e se la prosa
# nomina l'oggetto deve nominarlo con quel nome.
# ---------------------------------------------------------------------------

DENTRO_OGGETTO = (
    "\tif ( dbid == ITEM_ID_TZ500_K ) {\n"
    "\t\tif ( dbmode == DBMODE_REF ) {\n"
    "\t\t\treturn\n"
    "\t\t}\n"
    + BLOCCO +
    "\t}\n"
)


def test_la_descrizione_porta_il_suo_oggetto():
    voci = estrai_da_testo("db_item.hsp", DENTRO_OGGETTO)
    assert {v["oggetto"] for v in voci} == {"ITEM_ID_TZ500_K"}


def test_l_oggetto_non_fa_della_descrizione_un_nome():
    """`oggetto` sì, `array` no: senza array non c'e' plurale ne' articolo, e
    `_teste()` non la puo' scambiare per la testa di un nome composto."""
    voce = estrai_da_testo("db_item.hsp", DENTRO_OGGETTO)[0]
    assert voce["oggetto"] == "ITEM_ID_TZ500_K"
    assert "array" not in voce
    assert "plurale" not in voce
    assert "genere" not in voce


def test_un_oggetto_gia_chiuso_non_deborda():
    """⚠️ Il difetto plausibile: prendere l'ultimo `if ( dbid == … )` VISTO
    invece di quello che ci sta ancora INTORNO. Le graffe si seguono come le
    seguirebbe il compilatore, o la descrizione finisce attribuita all'oggetto
    di prima — e un dossier che pesca il nome sbagliato non si vede.
    """
    testo = (
        "\tif ( dbid == ITEM_ID_PRIMO ) {\n"
        "\t\treturn\n"
        "\t}\n"
        + BLOCCO
    )
    voci = estrai_da_testo("db_item.hsp", testo)
    assert voci, "le descrizioni ci sono lo stesso"
    assert all("oggetto" not in v for v in voci)


def test_l_oggetto_e_il_piu_interno():
    annidato = (
        "\tif ( dbid == ITEM_ID_FUORI ) {\n"
        "\t\tif ( dbid == ITEM_ID_DENTRO ) {\n"
        + BLOCCO +
        "\t\t}\n"
        "\t}\n"
    )
    voci = estrai_da_testo("db_item.hsp", annidato)
    assert {v["oggetto"] for v in voci} == {"ITEM_ID_DENTRO"}


def test_una_descrizione_non_e_un_nome():
    """Niente plurale, niente genere, niente array: non e' un sostantivo che il
    gioco mette dietro a un articolo, e' prosa."""
    voce = estrai_da_testo("db_item.hsp", BLOCCO)[0]
    assert voce["tipo"] == "statica"
    assert "plurale" not in voce
    assert "genere" not in voce
    assert "array" not in voce


def test_il_riconoscitore_per_riga_vede_il_letterale():
    """`avvio_descrizione` serve al riscontro strutturale di `applica`, che
    confronta la riga prodotta con quella di partenza."""
    riga = '\t\t\t\tdescription(3) = "(Reusable) Dart rifle."'
    grezzo, inizio, fine = avvio_descrizione(riga)
    assert grezzo == '"(Reusable) Dart rifle."'
    assert riga[inizio:fine] == grezzo
    assert avvio_descrizione('\tioriginalnameref(ITEM_ID_BANANA) = "banana"') is None


# ---------------------------------------------------------------------------
# l'applicazione
# ---------------------------------------------------------------------------

def test_la_traduzione_si_scrive_nel_ramo_inglese():
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: dict(v, it="Un fucile anestetico.")
                  for v in voci if v["en"] == "A tranquilizer rifle."}
    nuovo, quante = applica_a_testo("db_item.hsp", BLOCCO, dizionario)
    assert quante == 1
    assert 'description(0) = "Un fucile anestetico."' in nuovo
    # il ramo giapponese resta intatto
    assert 'description(0) = "麻酔銃。"' in nuovo


def test_gli_accenti_si_degradano_come_ovunque():
    """CP932 non ha le accentate: `degrada()` vale anche qui."""
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: dict(v, it="Perché è così.")
                  for v in voci if v["en"] == "Words of a marksman."}
    nuovo, _ = applica_a_testo("db_item.hsp", BLOCCO, dizionario)
    assert 'description(1) = "Perche\' e\' cosi\'."' in nuovo


def test_una_traduzione_che_rompe_la_riga_si_ferma():
    """La virgoletta non chiusa produce sorgente non rileggibile: il riscontro
    strutturale la deve prendere qui come la prende sulle `lang()`."""
    from strumenti.applica import SorgenteCorrotto
    voci = estrai_da_testo("db_item.hsp", BLOCCO)
    dizionario = {v["firma"]: dict(v, it="rotta\\")
                  for v in voci if v["en"] == "A tranquilizer rifle."}
    with pytest.raises(SorgenteCorrotto):
        applica_a_testo("db_item.hsp", BLOCCO, dizionario)


# ---------------------------------------------------------------------------
# il sorgente vero
# ---------------------------------------------------------------------------

def _sorgente():
    percorso = percorsi.SORGENTE_HSP / "db_item.hsp"
    if not percorso.exists():
        pytest.skip("il sorgente pinnato non c'e' su questa macchina")
    return percorso.read_bytes().decode("cp932")


def test_i_numeri_del_sorgente_pinnato():
    """I valori attesi, misurati il 2026-08-26 da `_107-struttura-db-item.py`.

    Se cambiano, il sorgente pinnato e' cambiato o il riconoscitore ha
    allargato la presa: in tutt'e due i casi si guarda, non si aggiorna.
    """
    testo = _sorgente()
    righe, _, _ = spezza_righe(testo)
    from strumenti.estrai import descrizioni_per_riga
    trovate = descrizioni_per_riga(righe)
    assert len(trovate) == 5284, "4 descrizioni per ciascuno dei 1.321 oggetti"

    voci = [v for v in estrai_da_testo("db_item.hsp", testo)
            if "array" not in v]
    assert len(voci) == 2832, "le vive: le altre 2.452 sono la stringa vuota"


def test_la_prova_d_identita_regge_sulle_descrizioni():
    """Il giudice vero: un dizionario che traduce ogni voce in se' stessa deve
    riprodurre il file byte per byte."""
    testo = _sorgente()
    dizionario, _ = dizionario_identita("db_item.hsp", testo)
    nuovo, quante = applica_a_testo("db_item.hsp", testo, dizionario)
    assert quante > 2832
    assert nuovo == testo
