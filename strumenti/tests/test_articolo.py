"""L'articolo derivato dal genere. Vedi `strumenti/articolo.py`.

I casi non sono inventati: quasi tutti sono nomi che stanno davvero nel
dizionario di `db_item.hsp`, cosi' il test si rompe se la regola smette di
reggere il corpus vero invece di un corpus di comodo.
"""
import pytest

from strumenti.articolo import articoli, preposizione_di


@pytest.mark.parametrize("genere, nome, atteso", [
    # femminile: «una» normale, «un'» davanti a vocale
    ("f", "pozione", ("una ", "la ")),
    ("f", "pergamena", ("una ", "la ")),
    ("f", "bacchetta", ("una ", "la ")),
    ("f", "spada lunga", ("una ", "la ")),
    ("f", "incudine", ("un'", "l'")),
    ("f", "accetta", ("un'", "l'")),
    ("f", "armatura decorata", ("un'", "l'")),
    # femminile con s impura: resta «una», non «uno»
    ("f", "scheggia di legno", ("una ", "la ")),
    ("f", "stoffa di seta", ("una ", "la ")),
    # maschile: «un» normale, «uno» sulla s impura e sui digrammi
    ("m", "mantello leggero", ("un ", "il ")),
    ("m", "grimorio", ("un ", "il ")),
    ("m", "pugnale", ("un ", "il ")),
    ("m", "scudo da cavaliere", ("uno ", "lo ")),
    ("m", "sgabello tondo", ("uno ", "lo ")),
    ("m", "scrittoio", ("uno ", "lo ")),
    ("m", "zaino", ("uno ", "lo ")),
    ("m", "gnomo", ("uno ", "lo ")),
    # maschile davanti a vocale: «un» senza apostrofo, ma «l'»
    ("m", "anello decorativo", ("un ", "l'")),
    ("m", "altare", ("un ", "l'")),
    ("m", "oracolo", ("un ", "l'")),
    # plurali soli: il partitivo, che e' cio' che l'inglese sbaglia con «a goods»
    ("fp", "cianfrusaglie", ("delle ", "le ")),
    ("fp", "armi", ("delle ", "le ")),
    ("mp", "libri", ("dei ", "i ")),
    ("mp", "vestiti", ("dei ", "i ")),
    ("mp", "attrezzi", ("degli ", "gli ")),
    ("mp", "stivali pesanti", ("degli ", "gli ")),
    ("mp", "accessori variopinti", ("degli ", "gli ")),
])
def test_casi_del_dizionario(genere, nome, atteso):
    assert articoli(genere, nome) == atteso


def test_h_muta_si_comporta_da_vocale():
    """«l'hotel», non «lo hotel»: la h italiana non si pronuncia."""
    assert articoli("m", "hotel") == ("un ", "l'")


@pytest.mark.parametrize("nome, atteso", [
    ("ferro", "di "),
    ("seta", "di "),
    ("materia grezza", "di "),
    ("scaglie di drago", "di "),
    ("bambù", "di "),
    ("argento", "d'"),
    ("oro", "d'"),
    ("osso", "d'"),
    ("ossidiana", "d'"),
    ("acciaio", "d'"),
    ("etere", "d'"),
    ("adamantio", "d'"),
])
def test_la_preposizione_elide_davanti_a_vocale(nome, atteso):
    """«d'argento», non «di argento»; ma «di ferro»."""
    assert preposizione_di(nome) == atteso


def test_la_preposizione_non_elide_davanti_a_semiconsonante():
    """«di iato», non «d'iato»: la i seguita da vocale fa consonante.

    E' la stessa domanda dell'articolo — «questa parola comincia per vocale?» —
    e deve dare la stessa risposta, o il gioco direbbe «uno iato» e «d'iato»
    nella stessa riga.
    """
    assert preposizione_di("iato") == "di "


def test_la_preposizione_non_si_applica_al_nulla():
    """Un materiale senza resa non deve produrre una preposizione orfana."""
    assert preposizione_di("") == ""


def test_la_h_muta_non_rende_pura_la_s_impura():
    """«uno shuriken», non «un shuriken».

    La `h` sta fra le vocali perche' a inizio di parola e' muta e chiede
    l'elisione («l'hotel»). Ma in seconda posizione, dopo la `s`, non e' una
    vocale: `sh` e' `s` impura come `sc` e `st`. Le due domande — «elide?» e
    «e' consonante?» — si somigliano e non sono la stessa, e questo caso e' il
    posto dove si separano. Visto a schermo nel collaudo del 2026-08-09.
    """
    assert articoli("m", "shuriken") == ("uno ", "lo ")


def test_i_semiconsonante_chiede_uno():
    """«uno iato»: la i seguita da vocale fa consonante, e non elide."""
    assert articoli("m", "iato") == ("uno ", "lo ")


def test_i_vocale_piena_non_la_chiede():
    """«un'identificazione»: qui la i e' vocale, e la regola non deve scattare."""
    assert articoli("f", "identificazione") == ("un'", "l'")


def test_le_parentesi_angolari_non_contano():
    """Un artefatto si giudica sulla lettera, non sul segno che lo racchiude."""
    assert articoli("f", "<Falce del Vuoto>") == ("una ", "la ")
    assert articoli("m", "<Zantetsuken>") == ("uno ", "lo ")


def test_genere_non_valido_si_rompe():
    with pytest.raises(ValueError, match="non valido"):
        articoli("maschile", "mantello")


def test_nome_vuoto_non_produce_articolo():
    """Meglio niente che un articolo appeso al nulla."""
    assert articoli("m", "   ") == ("", "")
