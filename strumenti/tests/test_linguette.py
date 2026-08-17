# strumenti/tests/test_linguette.py
"""Il tetto delle linguette di `drawmenu`: la misura, il criterio, la rete.

La misura sta in `strumenti/linguette.py` e viene dalla schermata della scheda
del personaggio del 2026-08-17. I test che la fissano vanno letti come una
**prova con data**: se un domani una linguetta dentro il tetto uscisse
sovrapposta alla sua vicina, sono loro a dover fallire per primi.
"""
import json

import pytest

from strumenti.linguette import (
    CENTRAGGIO, PASSO, PIXEL_PER_CARATTERE, SCOSTAMENTO, TETTO_COPPIA,
    TETTO_ULTIMA, costo, file_di_linguette, fuori_misura, rese,
)

# due file di linguette dentro `drawmenu`, piu' una riga `s = lang(` che sta
# FUORI dalla funzione e non e' una linguetta
SORGENTE = """\
#deffunc altracosa
\ts = lang("見出し", "Heading")
\treturn

#deffunc drawmenu int drawmenu_arg1
\tif ( drawmenu_arg1 == 0 ) {
\t\ts = lang("情報", "Chara"), lang("装備", "Wear"), ""
\t}
\tif ( drawmenu_arg1 == 1 ) {
\t\ts = lang("魔法", "Spell"), lang("技能", "Skill"), lang("広域技能", "Wide Skill"), ""
\t}
\treturn

#deffunc fillbg
\ts = lang("べつ", "Other")
\treturn
"""


def _voce(firma, riga, en, it):
    return {
        "firma": firma, "file": "module.hsp", "riga": riga, "occorrenza": 0,
        "jp": "", "jp_grezzo": "", "en": en, "en_grezzo": '"%s"' % en,
        "tipo": "statica", "contesto": "", "it": it,
    }


@pytest.fixture
def finto(tmp_path):
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "module.hsp").write_bytes(SORGENTE.encode("cp932"))
    dizionario = tmp_path / "dizionario"
    dizionario.mkdir()
    return dizionario, sorgente


def _scrivi(dizionario, sorgente, rese_per_inglese):
    """Il dizionario finto, con le firme prese dal sorgente finto."""
    voci = []
    for riga, elenco in file_di_linguette(sorgente).items():
        for firma, inglese in elenco:
            if inglese in rese_per_inglese:
                voci.append(_voce(firma, riga, inglese, rese_per_inglese[inglese]))
    (dizionario / "module.hsp.jsonl").write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci), encoding="utf-8")


# --- la misura, con la sua data ---------------------------------------------

def test_il_tetto_e_la_misura_del_2026_08_17():
    """Sette px per carattere, contro i sei che il gioco suppone.

    I sette vengono da quattro etichette misurate a schermo (da 6,80 a 7,25); i
    tre di `CENTRAGGIO` sono la meta' dei sei che `module.hsp:5184` usa per
    centrare. La differenza fra i due e' tutto il motivo per cui esiste questa
    rete: se fossero uguali, il testo resterebbe dentro la sua cella per
    costruzione.
    """
    assert PIXEL_PER_CARATTERE == 7
    assert CENTRAGGIO == 3
    assert PASSO == 50
    assert SCOSTAMENTO == 46
    assert TETTO_COPPIA == 50


def test_il_tetto_della_coppia_e_il_passo_e_non_una_costante_a_mano():
    """Lo scostamento si semplifica: le due celle partono dallo stesso punto.

    Scritto come `96 - 46` il numero sarebbe giusto e muto; scritto come il
    passo, segue il sorgente se un aggiornamento CGX allarga le celle.
    """
    assert TETTO_COPPIA == PASSO


def test_la_coppia_inglese_peggiore_tocca_il_limite_esatto():
    """`Skill`(5) + `Wide Skill`(10) fa `4*5 + 3*10 = 50`.

    ⭐ E' la prova della formula: la coppia piu' larga che upstream ha scritto
    arriva **esattamente** al tetto e non lo supera. Se il conto fosse sbagliato
    di poco, questa uguaglianza non ci sarebbe.
    """
    assert costo("Skill", "Wide Skill") == TETTO_COPPIA


def test_wide_skill_e_lunga_dieci_come_il_tetto_dell_ultima():
    """Il bordo destro della barra, misurato a 1897, da' dieci caratteri netti.

    E `Wide Skill` ne ha dieci: la fila piu' stretta del gioco tocca tutt'e due
    i limiti insieme, quello della coppia e quello del bordo.
    """
    assert TETTO_ULTIMA == len("Wide Skill")


def test_il_tetto_non_e_sette_caratteri_a_testa():
    """La lettura ingenua — `50 / 7` — direbbe che `Wide Skill` non ci sta.

    Ci sta, perche' e' l'ultima e la sua vicina di sinistra e' corta. Il vincolo
    e' sulla coppia, non sulla voce, e questo test esiste perche' nessuno lo
    riscriva «piu' semplice».
    """
    assert costo("Skill", "Wide Skill") <= TETTO_COPPIA
    assert TETTO_COPPIA // PIXEL_PER_CARATTERE == 7  # la lettura sbagliata
    assert len("Wide Skill") > 7                     # e la voce che smentisce


def test_il_tetto_e_asimmetrico():
    """La penalita' e' 4 a sinistra e 3 a destra, non 3,5 e 3,5.

    Il centraggio sbagliato spinge il testo verso destra, quindi la linguetta di
    sinistra costa piu' della sua vicina. Scambiare due rese puo' far passare
    una coppia che sforava, ed e' la cosa meno ovvia di questa geometria.
    """
    assert costo("aaaaaaaa", "aaa") != costo("aaa", "aaaaaaaa")
    assert costo("aaaaaaaa", "aaa") > costo("aaa", "aaaaaaaa")


# --- che cosa e` una linguetta, e che cosa no --------------------------------

def test_solo_le_righe_dentro_drawmenu_sono_linguette(finto):
    """Un `s = lang(` in un'altra funzione non ha questa geometria.

    Il riconoscimento e' sul corpo di `#deffunc drawmenu`, non sulla forma della
    riga: `module.hsp` ne ha altre due (`altracosa` e `fillbg` qui sopra), e
    misurarle col passo di 50 px griderebbe al difetto su un titolo qualsiasi.
    """
    _, sorgente = finto
    assert sorted(file_di_linguette(sorgente)) == [7, 10]


def test_le_file_si_leggono_dal_sorgente_e_non_da_un_elenco_a_mano(finto):
    """Una quinta fila aggiunta da un aggiornamento CGX deve entrare da sola.

    E' il difetto che ha tenuto fuori dai referti tutto questo pezzo di schermo
    fino alla 56a: quello che nessuno elenca, nessuno guarda.
    """
    _, sorgente = finto
    inglesi = [e for _, e in file_di_linguette(sorgente)[10]]
    assert inglesi == ["Spell", "Skill", "Wide Skill"]


def test_una_linguetta_non_tradotta_si_misura_sull_inglese(finto):
    """E' quel che il giocatore vede adesso.

    Se una fila non tradotta risultasse «a posto» perche' vuota, il referto
    direbbe «zero fuori misura» su una schermata che nessuno ha ancora toccato.
    """
    dizionario, sorgente = finto
    _scrivi(dizionario, sorgente, {})
    assert [t for _, t in rese(dizionario, sorgente)[7]] == ["Chara", "Wear"]


def test_l_accento_degradato_conta_due_caratteri(finto):
    """«Abilità» arriva a schermo come «Abilita'»: otto caratteri, non sette."""
    dizionario, sorgente = finto
    _scrivi(dizionario, sorgente, {"Skill": "Abilità"})
    assert ("Skill", "Abilita'") in rese(dizionario, sorgente)[10]


# --- la rete vera ------------------------------------------------------------

def test_una_coppia_troppo_larga_viene_presa(finto):
    """La regressione che questa rete esiste per impedire."""
    dizionario, sorgente = finto
    _scrivi(dizionario, sorgente, {"Skill": "Abilità", "Wide Skill": "Ad area"})
    guasti = fuori_misura(dizionario, sorgente)
    assert [(g[1], g[2]) for g in guasti] == [("Abilita'", "Ad area")]


def test_l_ultima_della_fila_ha_il_bordo_e_non_una_vicina(finto):
    """Oltre il bordo destro il testo esce dalla barra, senza toccare nessuno."""
    dizionario, sorgente = finto
    _scrivi(dizionario, sorgente, {"Wide Skill": "Capacità ad area"})
    guasti = fuori_misura(dizionario, sorgente)
    assert ("Capacita' ad area", "") in [(g[1], g[2]) for g in guasti]


def test_nessuna_linguetta_del_progetto_sfora():
    """Sul dizionario vero. Le tredici rese della 56a stanno tutte dentro."""
    guasti = fuori_misura()
    assert guasti == [], "\n".join("%s:%d %r + %r = %d" % (("module.hsp",) + g) for g in guasti)


def test_le_linguette_del_progetto_sono_tredici_in_quattro_file():
    """Se il conto cambia, un aggiornamento CGX ha toccato `drawmenu`."""
    tutte = rese()
    assert len(tutte) == 4
    assert sum(len(f) for f in tutte.values()) == 13
