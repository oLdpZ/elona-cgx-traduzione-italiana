# strumenti/tests/test_intestazioni_larghezze.py
"""RETE 20: il tetto di `display_topic`, e i quattro modi di sbagliarlo.

La rete e' nata nella 66a guardando solo le coppie di intestazioni vicine, e
nella 68a il collaudo ha trovato due difetti proprio dove non guardava:
l'**ultima** intestazione di ogni riga, il cui limite non e' il bordo della
finestra ma la prima cosa che le viene disegnata a destra.

I quattro test centrali fissano le quattro cose che, sbagliate, la rendevano
cieca o bugiarda:

1. l'ostacolo puo' stare **trecento righe piu' in la'**, purche' dentro la
   stessa etichetta HSP (`command.hsp:10429` e la sua `mes` a `:10733`);
2. la sua `x` puo' essere un'**espressione** con `en` (`wx + 564 - en * 22`);
3. la fascia verticale dell'intestazione e' alta **12** px, non 15: con 15
   toccava la riga di valori sotto e inventava colonne dal tetto zero;
4. un `pos` seguito da una `line` **non disegna niente** e non e' un ostacolo.
"""
import pytest

from strumenti import intestazioni_larghezze as rete20
from strumenti.intestazioni_larghezze import (
    ALTO, BASSO, DI_MONTE, ICONA, PASSO, ascissa, blocchi, ostacoli, tetto,
)

# ⚠️ `testo_di` NON si importa per nome: comincia per «test» e pytest se lo
# raccoglie come funzione di prova, chiedendo una fixture «argomento» che non
# esiste. Si chiama per modulo.


def righe(testo):
    return testo.split("\n")


# ---------------------------------------------------------------- il tetto


def test_il_tetto_e_lo_spazio_diviso_il_passo():
    # il testo comincia a x + 26 e ogni carattere avanza di 7
    assert tetto(400, 557) == (557 - 400 - ICONA) // PASSO == 18
    assert tetto(400, 542) == 16


def test_i_due_tetti_veri_della_scheda_del_personaggio():
    """⭐ Misurati a schermo nella 68a, non dedotti.

    Il ritratto (`window2 wx + 557`) taglia «Benedizioni e malocchi» a 18
    caratteri: sullo schermo si leggeva «Benedizioni e maloc». La `mes` di
    «Pot. magia» (`wx + 542`) ne lascia 16 a «Tiri di combattimento», che
    infatti ci finiva sopra.
    """
    assert tetto(400, 557) == 18
    assert tetto(400, 542) == 16
    # e l'inglese di monte ci sta in tutt'e due, come vuole la regola della 63a
    assert len("Blessing and Hex") <= 18
    assert len("Combat Rolls") <= 16


# ------------------------------------------------------- l'ascissa con `en`


@pytest.mark.parametrize("base, segno, termine, atteso", [
    ("400", None, None, 400),
    ("564", "-", "22", 542),   # pos wx + 564 - en * 22  ->  «Pot. magia»
    ("460", "+", "8", 468),
])
def test_ascissa_risolve_il_termine_en(base, segno, termine, atteso):
    assert ascissa(base, segno, termine) == atteso


# ------------------------------------------------------ il confine: l'etichetta


BLOCCHI = """\
*prima_schermata
\tdisplay_topic lang("あ", "Alpha"), wx + 28, wy + 100
\tpos wx + 300, wy + 100
\tmes "valore"
*seconda_schermata
\tpos wx + 60, wy + 100
\tmes "un'altra finestra"
"""


def test_l_etichetta_separa_due_schermate():
    r = righe(BLOCCHI)
    tagli = blocchi(r)
    assert len(tagli) == 2
    prima, ultima = tagli[0]
    trovati = ostacoli(r, prima, ultima)
    # dentro la prima etichetta c'e' solo l'ostacolo a 300: quello a 60 e'
    # un'altra schermata e non deve stringere il tetto a zero
    assert [x for x, _a, _b in trovati] == [300]


def test_l_ostacolo_vale_anche_a_trecento_righe_di_distanza():
    r = righe("*una\n"
              + '\tdisplay_topic lang("あ", "Combat Rolls"), wx + 400, wy + 253\n'
              + "\tmes \"riempitivo\"\n" * 300
              + "\tpos wx + 564 - en * 22, wy + 263\n\tmes \"Pot. magia\"\n")
    prima, ultima = blocchi(r)[0]
    trovati = ostacoli(r, prima, ultima)
    assert (542, 263, 263 + 16) in trovati


# ---------------------------------------------------- la fascia verticale


def _fascia_incrocia(y_intestazione, alto, basso):
    """La stessa condizione che usa `misure`, isolata per poterla provare."""
    return not (basso <= y_intestazione + ALTO or alto >= y_intestazione + BASSO)


def test_una_mes_appena_sotto_non_e_un_ostacolo():
    """⚠️ `chat.hsp:25513`: intestazione a wy+225, valori a wy+245.

    Con la fascia alta 15 le due si sfioravano di tre px e la rete dichiarava
    tre colonne dal tetto **zero** — tre falsi che facevano fallire il banco di
    monte. L'inchiostro misurato e' alto 12.
    """
    assert not _fascia_incrocia(225, 245, 245 + 16)
    assert not _fascia_incrocia(225, 198, 198 + 16)


def test_il_ritratto_incrocia_l_intestazione_che_copre():
    # window2 wx + 557, wy + 23, 87, 120 contro l'intestazione a wy + 122
    assert _fascia_incrocia(122, 23, 23 + 120)


def test_la_mes_di_pot_magia_incrocia_i_tiri_di_combattimento():
    assert _fascia_incrocia(253, 263, 263 + 16)


# ------------------------------------------------- che cosa disegna davvero


NON_DISEGNA = """\
*una
\tpos wx + 100, wy + 50
\tline wx + 100, wy + 50, wx + 200, wy + 50
\tpos wx + 300, wy + 50
\tcolor 0, 0, 0
\tmes "questo si'"
"""


def test_un_pos_seguito_da_line_non_e_un_ostacolo():
    r = righe(NON_DISEGNA)
    prima, ultima = blocchi(r)[0]
    assert [x for x, _a, _b in ostacoli(r, prima, ultima)] == [300]


def test_color_e_font_non_interrompono_la_lettura_del_disegno():
    """`pos` / `color` / `mes` e' la forma piu' comune: la `mes` va vista."""
    r = righe(NON_DISEGNA)
    prima, ultima = blocchi(r)[0]
    assert (300, 50, 50 + 16) in ostacoli(r, prima, ultima)


NON_TESTO = """\
*una
\twindow2 wx + 557, wy + 23, 87, 120
\tpos wx + 560, wy + 27
\tgzoom 80, 112, 4, 0, 0, 48, 72
"""


def test_una_finestra_e_un_immagine_sono_ostacoli():
    r = righe(NON_TESTO)
    prima, ultima = blocchi(r)[0]
    trovati = ostacoli(r, prima, ultima)
    assert (557, 23, 143) in trovati       # la cornice del ritratto
    assert (560, 27, 27 + 112) in trovati  # il ritratto stesso


# -------------------------------------------------------------- il testo


@pytest.mark.parametrize("argomento, atteso", [
    ('lang("神経", "Blessing and Hex")', "Blessing and Hex"),
    ('"Ver"', "Ver"),
    ('s', None),
    ('s(2)', None),
])
def test_legge_solo_i_letterali(argomento, atteso):
    assert rete20.testo_di(argomento) == atteso


# --------------------------------------------------------- il banco di monte


def test_i_siti_dove_monte_sfora_sono_dichiarati():
    """Non e' «zero fuori misura»: col passo vero l'inglese sfora davvero.

    Se questo insieme cambia, o e' cambiato il sorgente CGX o e' sbagliata la
    rete — e in tutt'e due i casi va guardato prima di toccare una resa.
    """
    assert DI_MONTE == {("command.hsp", 4199), ("command.hsp", 10410)}
