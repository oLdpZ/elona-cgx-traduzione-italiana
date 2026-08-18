# strumenti/tests/test_commenti.py
"""Le righe spente da un commento di blocco.

La funzione viveva in `scratchpad/commenti-blocco.py` dalla 37a, cioe' fuori
dalla catena delle verifiche e senza test. Dalla 60a la usa una **rete**
(`larghezze.py`, per non prendere la larghezza di un riquadro da codice morto),
e una rete non puo' dipendere da uno scratch: la funzione e' passata in
`strumenti/` e questi test sono il prezzo del passaggio.
"""
from strumenti import percorsi
from strumenti.commenti import righe_in_commento

SPENTO = """\
\tval = promptx, prompty, 999, 1
\t/********** ORIGINAL - BEGINNING **********

\tval = promptx, prompty, 280, 1

\t ********** ORIGINAL - ENDING **********/

\tval = promptx, prompty, 330, 1
"""

CON_STRINGA = """\
\ttxt lang("a/*b", "a/*b")
\tval = promptx, prompty, 280, 1
"""


def test_le_righe_fra_i_delimitatori_sono_spente(tmp_path):
    """E' il caso vero di `map_user.hsp:522`: upstream tiene la sua riga in
    commento accanto a quella del mod, e sono tutt'e due dei `val =`.
    """
    percorso = tmp_path / "finto.hsp"
    percorso.write_bytes(SPENTO.encode("cp932"))

    spente = righe_in_commento(percorso)

    assert 1 not in spente          # il val vivo di sopra
    assert 4 in spente              # il val dentro il blocco
    assert 8 not in spente          # il val vivo di sotto


def test_un_delimitatore_dentro_una_stringa_non_spegne_niente(tmp_path):
    """Se no un `/*` scritto in un letterale spegnerebbe meta' file."""
    percorso = tmp_path / "finto.hsp"
    percorso.write_bytes(CON_STRINGA.encode("cp932"))

    assert righe_in_commento(percorso) == set()


def test_il_val_di_map_user_e_davvero_dentro_un_blocco_spento():
    """Il punto misurato nel sorgente vero, che ha fatto nascere la funzione qui.

    `map_user.hsp:522` e' la riga di upstream tenuta in commento dal mod
    BLOODYSHADE, che poco sotto riscrive lo stesso `val` in due rami.
    """
    spente = righe_in_commento(percorsi.SORGENTE_HSP / "map_user.hsp")
    assert 522 in spente
    assert 529 not in spente
    assert 532 not in spente
