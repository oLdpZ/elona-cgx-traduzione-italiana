"""L'articolo derivato dal genere. Vedi `strumenti/articolo.py`.

I casi non sono inventati: quasi tutti sono nomi che stanno davvero nel
dizionario di `db_item.hsp`, cosi' il test si rompe se la regola smette di
reggere il corpus vero invece di un corpus di comodo.
"""
import pytest

from strumenti.articolo import articoli


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
