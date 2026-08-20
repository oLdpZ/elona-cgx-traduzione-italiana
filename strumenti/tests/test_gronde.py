# strumenti/tests/test_gronde.py
"""La gronda fra etichetta e valore nella scheda del personaggio.

I numeri vengono dal collaudo della 72a, dove tre difetti dichiarati dalla 68a
si sono rivisti a schermo tali e quali — «ClasseGuerriero», «Altezza157 cm»,
«Velocita70(70)» — e un quarto, «AliasGiustizia del sole», non era mai stato
nominato. Un quinto, «Prossimo 3024», l'ha trovato la rete il giorno stesso in
cui e' nata.
"""
import pytest

from strumenti import percorsi
from strumenti.gronde import (
    GRONDE,
    PIXEL_PER_CARATTERE,
    RESPIRO,
    Gronda,
    etichette_di,
    fuori_misura,
    larghezza,
    misura,
)


def test_nessuna_etichetta_sovrastampa_il_suo_valore():
    """La guardia. Se fallisce, una resa nuova e' piu' larga della sua gronda:
    o si accorcia l'etichetta, o si sposta la colonna con una toppa."""
    sfori = fuori_misura()
    assert sfori == [], "\n".join(
        "%s:%d  <%s> %d px in una gronda da %d  (%s)" % (f, r, e, u, g, n)
        for f, r, n, e, u, g in sfori)


def test_le_cinque_gronde_sono_tutte_misurabili():
    """Ogni ancora deve trovarsi **una volta sola** nella build.

    ⚠️ E' la parte che vale piu' del conto: una rete che non trova la sua riga
    deve fermarsi, non misurare la riga accanto. Le toppe della 72a hanno gia'
    fatto scattare questo controllo — spostato `wx + 410` a `wx + 418`, la rete
    e' morta di `LookupError` invece di misurare una gronda vecchia.
    """
    for gronda in GRONDE:
        m = misura(gronda)
        assert m["gronda"] > 0
        assert m["etichette"], gronda.nome


def test_il_passo_e_quello_che_il_gioco_usa_per_conto_suo():
    """7 px non e' una stima nostra: sta in `module.hsp:70`, dentro `cs_list`.

    ⚠️ Ed e' lo **stesso** numero di `menu_dialogo`, che pero' disegna con un
    corpo diverso (12 contro 10). Il passo del glifo a larghezza fissa non
    segue il corpo, e questo e' il fatto che la 66a aveva sbagliato una volta:
    aveva preso il 7,7 di `larghezze.py` «perche' e' lo stesso carattere».
    """
    testo = (percorsi.SORGENTE_HSP / "module.hsp").read_bytes().decode("cp932")
    assert "strlen(cs_list_arg1) * %d + 32" % PIXEL_PER_CARATTERE in testo


def test_le_tre_toppe_della_scheda_sono_vive():
    """Le gronde stanno aperte per una toppa, non per grazia di monte.

    Se qualcuno togliesse le tre toppe, le ancore non si troverebbero piu' e
    `test_le_cinque_gronde_sono_tutte_misurabili` morirebbe: questo test dice
    **perche'**, cioe' che il sorgente pinnato ha ancora i valori stretti.
    """
    monte = (percorsi.SORGENTE_HSP / "command.hsp").read_bytes().decode("cp932")
    costruita = (percorsi.BUILD_HSP / "command.hsp").read_bytes().decode("cp932")
    for stretto, largo in (("pos wx + 68 + cnt / 5 * 190", "pos wx + 79 + cnt / 5 * 190"),
                           ("pos wx + 310, wy + 151", "pos wx + 325, wy + 151"),
                           ("pos wx + 410 + en * 5", "pos wx + 418 + en * 5")):
        assert stretto in monte, stretto
        assert largo not in monte, largo
        assert largo in costruita, largo
        assert stretto not in costruita, stretto


def test_i_quattro_difetti_del_collaudo_erano_veri():
    """Una prova con data: coi valori di MONTE le quattro etichette sforavano.

    ⚠️ Non e' una ripetizione della guardia: la guardia dice che **oggi** stanno
    dentro, questo dice che **prima** non ci stavano — cioe' che le toppe hanno
    curato qualcosa invece di spostare numeri a caso. «Alias» e «Altezza» ci
    stavano per un pelo (3 px e 1 px) e a schermo si leggevano attaccate:
    e' per loro che esiste `RESPIRO`.
    """
    gronde_di_monte = {"Classe": 38, "Alias": 38, "Altezza": 50, "Velocita'": 55}
    for etichetta, gronda in gronde_di_monte.items():
        assert larghezza(etichetta) > gronda, etichetta


def test_le_etichette_si_leggono_dal_s_uguale_sopra_il_pos():
    righe = [
        '\t\t\ts = lang("名前", "Nome"), lang("種族", "Razza")',
        "\t\t\trepeat 2",
        "\t\t\t\tpos wx + 30, wy + 47",
    ]
    assert etichette_di(righe, 2) == ["Nome", "Razza"]


def test_il_respiro_e_un_carattere_intero():
    """Un valore incollato all'etichetta non e' «dentro»: e' illeggibile.

    `Peso eq.` occupa 56 px in una gronda da 73 ed e' comodo; `Prossimo` ne
    occupava 56 in una da 60 e a schermo si leggeva «Prossimo3024».
    """
    assert larghezza("abc") == (3 + RESPIRO) * PIXEL_PER_CARATTERE


def test_un_ancora_ambigua_ferma_la_rete():
    finta = Gronda("finta", "command.hsp", "loop", "loop")
    with pytest.raises(LookupError):
        misura(finta)
