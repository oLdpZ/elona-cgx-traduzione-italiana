# strumenti/tests/test_commenti.py
"""Le righe spente da un commento di blocco.

La funzione viveva in `scratchpad/commenti-blocco.py` dalla 37a, cioe' fuori
dalla catena delle verifiche e senza test. Dalla 60a la usa una **rete**
(`larghezze.py`, per non prendere la larghezza di un riquadro da codice morto),
e una rete non puo' dipendere da uno scratch: la funzione e' passata in
`strumenti/` e questi test sono il prezzo del passaggio.
"""
from strumenti import percorsi
from strumenti.commenti import (colonna_commento_riga, lang_spenta_da_barre,
                                righe_in_commento)

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


# --------------------------------------------------- il commento di riga `//`

def test_le_due_barre_spengono_solo_quel_che_viene_dopo():
    """Una riga viva con un commento in coda **non** e' una riga morta."""
    assert colonna_commento_riga('\ttxt lang("a", "b")') is None
    assert colonna_commento_riga('// txt lang("a", "b")') == 0
    assert colonna_commento_riga('\tx = 1 // nota') == 7
    assert lang_spenta_da_barre('\tx = 1 // nota') is False


def test_le_barre_dentro_una_stringa_o_dopo_un_punto_e_virgola_non_contano():
    """L'indirizzo del wiki sta in un letterale, e un `//` dopo un `;` e' gia'
    dentro il commento di riga che il progetto guardava da sempre.
    """
    assert colonna_commento_riga('\ts = "https://elona.fandom.com"') is None
    assert colonna_commento_riga('\tx = 1 ; // finto') is None


def test_i_due_selettori_di_autopick_sono_davvero_spenti():
    """Il caso vero che ha fatto nascere la funzione, nella 100a.

    `custom_autopick.hsp:200`-`:217` tiene spenti con `//` i due selettori
    ` zombie ` e ` dragon's `, e `estrai` li estraeva come se fossero vivi.
    """
    righe = (percorsi.SORGENTE_HSP / "custom_autopick.hsp").read_bytes() \
        .decode("cp932").split("\r\n")

    assert lang_spenta_da_barre(righe[199]) is True     # :200  ` zombie `
    assert lang_spenta_da_barre(righe[216]) is True     # :217  ` dragon's `
    # ⚠️ la prova al contrario: il selettore vivo che viene subito dopo
    assert lang_spenta_da_barre(righe[219]) is False    # :220  ` empty `
