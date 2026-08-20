# strumenti/tests/test_maiuscole.py
"""`cnven()` e la maiuscola in mezzo alla frase.

Nata nella 72a da una schermata: «Tomdecker il cittadino **F**emmina», dove
`text.hsp:124` aveva reso `strfemale` con la minuscola giusta e `cnven`
(`init.hsp:191`) gliela alzava dieci file piu' in la'.
"""
import pytest

from strumenti import percorsi
from strumenti.maiuscole import (
    ACCUMULATO,
    APPESO,
    GIUDICATI,
    IN_TESTA,
    _posizione,
    accumulati,
    appesi,
    da_guardare,
    siti,
)


def test_nessun_sito_nuovo_da_giudicare():
    """La guardia.

    ⚠️ **Non chiede zero appesi.** Nove dei dieci giudicati reggono la
    maiuscola — dopo i due punti di «Ricetta: », dopo il punto abbreviativo di
    «Res. », dopo il trattino della lapide — e quattro stanno in `chat.hsp`,
    che non e' ancora tradotto e va giudicato quando ci arriva il lotto. Quel
    che la guardia ferma e' un sito **nuovo**: una riga che nessuno ha ancora
    letto.
    """
    nuovi = da_guardare()
    assert nuovi == [], "\n".join(
        "%s:%d  %s" % (s["file"], s["riga"], s["testo"]) for s in nuovi)


def test_cnven_alza_davvero_la_prima_lettera():
    """Il fatto da cui dipende tutto il resto, letto in `init.hsp`.

    Il corpo fa `poke ..., locvar_cnven_p - 32`, cioe' la sottrazione che porta
    una minuscola ASCII sulla sua maiuscola, e ci arriva solo dopo `if ( jp )
    return`. ⚠️ In build giapponese non succede niente: e' un difetto che
    **esiste solo nelle build tradotte**.
    """
    testo = (percorsi.SORGENTE_HSP / "init.hsp").read_bytes().decode("cp932")
    corpo = testo.split("#defcfunc cnven str cnven_str", 1)[1][:900]
    assert "if ( jp ) {" in corpo
    assert "- 32" in corpo


@pytest.mark.parametrize("riga, atteso", [
    ('\ttxt cnven(name(rc)) + " torna in vita!"', IN_TESTA),
    ('\ts(3) = cnven(strfemale)', IN_TESTA),
    ('\tlistn(0, 0) = cnven(strmale)', IN_TESTA),
    ('\tracename = lang("コボルト", cnven("Coboldo"))', IN_TESTA),
    ('\ts = "Res. " + cnven(s)', APPESO),
    ('\tbuff = lang("x", "(" + cnven(he(tc)) + " nodded.)")', APPESO),
    ('\ts += cnven(gendername(tc))', ACCUMULATO),
])
def test_la_posizione_si_legge_dalla_forma_dell_espressione(riga, atteso):
    inizio = riga.index("cnven(")
    assert _posizione(riga, inizio) == atteso


def test_un_piu_dentro_le_virgolette_non_e_una_concatenazione():
    """⚠️ Senza questo, ogni battuta che contiene un `+` risulterebbe appesa."""
    riga = '\ttxt lang("x", "1+1 fa 2. " + cnven(s))'
    assert _posizione(riga, riga.index("cnven(")) == APPESO
    riga = '\ttxt cnven(lang("+3 di forza", "+3 di forza"))'
    assert _posizione(riga, riga.index("cnven(")) == IN_TESTA


def test_le_quattro_toppe_della_72a_hanno_tolto_i_loro_cnven():
    """I quattro siti curati non devono tornare fra gli appesi.

    `chat.hsp:25573` era il difetto fotografato; `item_func.hsp` quello piu'
    frequente — il suffisso di qualita' su **ogni** oggetto identificato, dove
    `text.hsp:106` rende le sei qualita' in minuscolo apposta; le due di
    `command.hsp` erano anche incoerenti con le quattro righe sopra, che
    appendono la stessa famiglia di etichette senza `cnven`.
    """
    dove = {(s["file"], s["riga"]) for s in appesi() + accumulati()}
    build = (percorsi.BUILD_HSP / "item_func.hsp").read_bytes().decode("cp932")
    assert "cnven(_quality(" not in build
    build = (percorsi.BUILD_HSP / "chat.hsp").read_bytes().decode("cp932")
    assert "cnven(gendername(" not in build
    build = (percorsi.BUILD_HSP / "command.hsp").read_bytes().decode("cp932")
    assert "s += cnven(strmale)" not in build
    assert "s += cnven(strfemale)" not in build
    assert not any(f == "item_func.hsp" and r < 2321 for f, r in dove)


def test_ogni_giudicato_porta_il_suo_motivo():
    """Una riga in `GIUDICATI` e' una decisione: senza motivo e' una svista
    zittita. Stessa regola di `invariati.md`."""
    for chiave, motivo in GIUDICATI.items():
        assert len(motivo) > 30, chiave


def test_i_giudicati_esistono_ancora():
    """Se upstream sposta una riga, il permesso non deve restare appeso al
    vuoto: sarebbe un sito nuovo zittito da una decisione presa su un altro."""
    vivi = {(s["file"], s["riga"]) for s in appesi() + accumulati()}
    morti = sorted(set(GIUDICATI) - vivi)
    assert morti == [], morti


def test_la_grande_maggioranza_dei_siti_sta_in_testa():
    """134 su 144: `cnven` fa il suo mestiere quasi sempre, ed e' il motivo per
    cui non si toglie in blocco ma sito per sito."""
    tutti = siti()
    in_testa = [s for s in tutti if s["dove"] == IN_TESTA]
    assert len(in_testa) > len(tutti) * 0.9
