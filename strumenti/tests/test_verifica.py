# strumenti/tests/test_verifica.py
from strumenti.verifica import controlla_voce, controlla_lotto


def voce(**sovrascritture):
    base = {
        "firma": "abc", "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "バックパックが一杯だ。", "jp_grezzo": '"バックパックが一杯だ。"',
        "en": "Your inventory is full.", "en_grezzo": '"Your inventory is full."',
        "tipo": "statica", "contesto": "", "it": "Il tuo zaino e' pieno.",
    }
    base.update(sovrascritture)
    return base


def test_una_voce_valida_non_ha_problemi():
    assert controlla_voce(voce(it="Il tuo zaino è pieno.")) == []


def test_blocca_la_traduzione_vuota():
    problemi = controlla_voce(voce(it=""))
    assert any("vuota" in p for p in problemi)


def test_blocca_la_traduzione_identica_all_inglese():
    problemi = controlla_voce(voce(it="Your inventory is full."))
    assert any("identica" in p for p in problemi)


def test_blocca_l_apostrofo_scritto_a_mano():
    problemi = controlla_voce(voce(it="Il tuo zaino e' pieno."))
    assert any("apostrofo" in p for p in problemi)


def test_blocca_i_caratteri_che_cp932_cancellerebbe():
    problemi = controlla_voce(voce(it="Zaino pieno — davvero"))  # trattino lungo
    assert any("cp932" in p.lower() for p in problemi)


def test_le_dinamiche_devono_conservare_le_stesse_chiamate():
    pulita = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='name(tc) + " ha protetto " + name(x) + "."',
    )
    assert controlla_voce(pulita) == []

    rotta = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='"ha protetto"',
    )
    problemi = controlla_voce(rotta)
    assert any("interpolazion" in p for p in problemi)


def test_blocca_la_virgoletta_doppia_nelle_statiche():
    problemi = controlla_voce(voce(it='Ha detto "ciao".'))
    assert any('"' in p and "«" in p and "“" in p for p in problemi)


def test_non_blocca_la_virgoletta_doppia_nelle_dinamiche():
    pulita = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='name(tc) + " ha protetto " + name(x) + "."',
    )
    problemi = controlla_voce(pulita)
    assert not any("virgolette" in p for p in problemi)


def test_le_virgolette_tipografiche_alte_passano_nelle_statiche():
    assert controlla_voce(voce(it="Ha detto “ciao”.")) == []


def test_controlla_lotto_indicizza_per_firma():
    esito = controlla_lotto([voce(firma="uno", it=""), voce(firma="due", it="Zaino pieno.")])
    assert "uno" in esito
    assert "due" not in esito


# --- accessi coerenti (rilievo IMPORTANT 7) ---------------------------------

def test_una_voce_senza_tipo_non_solleva_un_keyerror_nudo():
    # un dizionario ritoccato a mano non deve far esplodere la validazione
    # di un lotto intero con un KeyError senza contesto
    problemi = controlla_voce({"file": "text.hsp", "riga": 42, "en": "Yes", "it": "Sì"})
    assert problemi
    assert "text.hsp:42" in problemi[0]
    assert "tipo" in problemi[0]


def test_un_tipo_non_valido_viene_segnalato_con_file_e_riga():
    problemi = controlla_voce({
        "file": "proc.hsp", "riga": 7, "tipo": "boh",
        "en": "Yes", "en_grezzo": '"Yes"', "it": "Sì",
    })
    assert problemi and "proc.hsp:7" in problemi[0] and "boh" in problemi[0]


# --- morfologia inglese vs contenuto (task 1, Fase 1) -----------------------

def test_togliere_la_morfologia_inglese_non_e_un_problema():
    # _s(tc) e' la desinenza della terza persona inglese: in italiano non
    # esiste. Sul sorgente vero (non sul file di lavoro, che e' un residuo):
    # i sei file di Fase 1 (text, command, action, proc, skill, trait) hanno
    # 1.522 dinamiche in tutto, di cui almeno 477 contengono una chiamata di
    # morfologia inglese pura (_s/_s2/_s3/_s4/is/was/your/your2/have/does/
    # him2/his3/its/its2/yourself) — verificato con
    # `strumenti.estrai.estrai_da_file` su
    # `C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\`. Il conteggio
    # esatto delle sole voci che il difetto rifiutava (serve la traduzione
    # italiana per saperlo, non disponibile in questa cartella) resta da
    # misurare quando il corpus tradotto di Fase 1 sara' pronto.
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": 'name(tc) + " attacca."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert controlla_voce(voce) == []


def test_perdere_una_funzione_di_contenuto_resta_un_problema():
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": '"Attacca."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert any("interpolazioni" in p for p in controlla_voce(voce))


def test_lasciare_la_morfologia_inglese_nell_italiano_e_un_problema():
    # scriverebbe "attacca s" a schermo
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": 'name(tc) + " attacca" + _s(tc) + "."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert any("morfologia inglese" in p for p in controlla_voce(voce))


def test_un_pronome_con_due_argomenti_va_conservato_come_contenuto():
    # giro di correzione 1: he/his/him NON sono piu' facoltativi. Con due
    # argomenti passano da lang() (action.hsp:9631, sorgente vero) e vanno
    # trattati come name() o itemname(): perderli e' un problema come
    # perdere qualunque altro contenuto.
    grezzo = 'name(tc) + " changed " + his(tc, 1) + " elemental affinity."'
    conservato = {
        "tipo": "dinamica", "en": " changed  elemental affinity.",
        "it": 'name(tc) + " ha cambiato " + his(tc, 1) + " affinità elementale."',
        "en_grezzo": grezzo,
    }
    perso = {
        "tipo": "dinamica", "en": " changed  elemental affinity.",
        "it": 'name(tc) + " ha cambiato la sua affinità elementale."',
        "en_grezzo": grezzo,
    }
    assert controlla_voce(conservato) == []
    assert any("interpolazioni" in p for p in controlla_voce(perso))


def test_un_pronome_con_un_argomento_deve_sparire():
    # command.hsp:6667 (sorgente vero) — his(tc) non ha mai un ramo lang()
    # raggiungibile: se resta nell'italiano scrive "his"/"her" per sempre,
    # esattamente come _s(tc) scriverebbe "s"
    grezzo = 'name(tc) + " puffs out " + his(tc) + " chest with pride."'
    corretto = {
        "tipo": "dinamica", "en": " puffs out  chest with pride.",
        "it": 'name(tc) + " gonfia il petto con orgoglio."', "en_grezzo": grezzo,
    }
    lasciato = {
        "tipo": "dinamica", "en": " puffs out  chest with pride.",
        "it": 'name(tc) + " gonfia " + his(tc) + " petto con orgoglio."',
        "en_grezzo": grezzo,
    }
    assert controlla_voce(corretto) == []
    assert any("morfologia inglese" in p for p in controlla_voce(lasciato))
