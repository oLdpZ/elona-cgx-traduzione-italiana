import json
import pytest
from strumenti.accenti import (
    accenti_interni,
    degrada,
    ha_apostrofo_scritto_a_mano,
    non_ascii_residuo,
)


@pytest.mark.parametrize("dentro,fuori", [
    ("perché", "perche'"),
    ("città", "citta'"),
    ("più", "piu'"),
    ("così", "cosi'"),
    ("però", "pero'"),
    ("È vero", "E' vero"),
    ("Perù", "Peru'"),
    ("nessun accento", "nessun accento"),
    ("", ""),
])
def test_degrada_le_vocali_accentate(dentro, fuori):
    assert degrada(dentro) == fuori


def test_degrada_non_tocca_il_giapponese():
    giapponese = "バックパックが一杯だ。"
    assert degrada(giapponese) == giapponese


def test_degrada_e_idempotente():
    una_volta = degrada("perché è così")
    assert degrada(una_volta) == una_volta


def test_rileva_apostrofo_scritto_a_mano():
    assert ha_apostrofo_scritto_a_mano("perche' e' cosi'") is True
    assert ha_apostrofo_scritto_a_mano("citta'") is True
    assert ha_apostrofo_scritto_a_mano("perché è così") is False


def test_apostrofo_legittimo_non_e_un_falso_positivo():
    # elisione italiana: l'oggetto, un'arma, dell'acqua
    assert ha_apostrofo_scritto_a_mano("l'oggetto") is False
    assert ha_apostrofo_scritto_a_mano("un'arma magica") is False
    assert ha_apostrofo_scritto_a_mano("dell'acqua") is False
    # troncamento: "po'" e' vocale + apostrofo, ma e' italiano corretto
    assert ha_apostrofo_scritto_a_mano("un po' di acqua") is False
    assert ha_apostrofo_scritto_a_mano("Aspetta un po'") is False


def test_imperativi_monosillabici_non_sono_falsi_positivi():
    # elenco chiuso degli imperativi monosillabici italiani: apostrofo legittimo
    assert ha_apostrofo_scritto_a_mano("va' via") is False
    assert ha_apostrofo_scritto_a_mano("fa' silenzio") is False
    assert ha_apostrofo_scritto_a_mano("da' il libro") is False
    assert ha_apostrofo_scritto_a_mano("di' quello che pensi") is False
    assert ha_apostrofo_scritto_a_mano("sta' fermo") is False
    assert ha_apostrofo_scritto_a_mano("be' non lo so") is False


def test_imperativi_monosillabici_maiuscoli_non_sono_falsi_positivi():
    assert ha_apostrofo_scritto_a_mano("Va' via subito") is False
    assert ha_apostrofo_scritto_a_mano("Fa' silenzio") is False


def test_apostrofo_davvero_sbagliato_resta_segnalato():
    # questo e' il test che conta: l'estensione dei troncamenti non deve
    # spegnere il rilevatore per gli errori veri
    assert ha_apostrofo_scritto_a_mano("sara' domani") is True
    assert ha_apostrofo_scritto_a_mano("perche' non lo so") is True
    assert ha_apostrofo_scritto_a_mano("la citta' e' grande") is True
    assert ha_apostrofo_scritto_a_mano("e' piu' veloce") is True
    assert ha_apostrofo_scritto_a_mano("l'ho gia' fatto") is True


def test_troncamento_ancorato_a_confine_di_parola():
    # il troncamento va escluso solo come parola a se stante: se e' la coda
    # di una parola piu' lunga, l'apostrofo resta un errore vero.
    # "rida'" e' la forma sbagliata di "ridà" (terza persona di "ridare").
    assert ha_apostrofo_scritto_a_mano("rida' domani") is True
    assert ha_apostrofo_scritto_a_mano("grida' forte") is True
    assert ha_apostrofo_scritto_a_mano("trova' la strada") is True
    assert ha_apostrofo_scritto_a_mano("leva' la mano") is True
    assert ha_apostrofo_scritto_a_mano("guarda' li") is True
    # gli stessi troncamenti come parola isolata restano legittimi,
    # sia a inizio frase sia a meta' frase, minuscoli e maiuscoli
    assert ha_apostrofo_scritto_a_mano("va' via") is False
    assert ha_apostrofo_scritto_a_mano("Va' via") is False
    assert ha_apostrofo_scritto_a_mano("presto, fa' silenzio") is False
    assert ha_apostrofo_scritto_a_mano("Fa' silenzio") is False
    assert ha_apostrofo_scritto_a_mano("adesso da' il libro") is False
    assert ha_apostrofo_scritto_a_mano("Da' il libro") is False
    assert ha_apostrofo_scritto_a_mano("resta li, sta' fermo") is False
    assert ha_apostrofo_scritto_a_mano("Sta' fermo") is False
    assert ha_apostrofo_scritto_a_mano("ora di' la verita") is False
    assert ha_apostrofo_scritto_a_mano("Di' la verita") is False
    assert ha_apostrofo_scritto_a_mano("prendine un po'") is False
    assert ha_apostrofo_scritto_a_mano("Po' di pazienza") is False
    assert ha_apostrofo_scritto_a_mano("mah, be' non lo so") is False
    assert ha_apostrofo_scritto_a_mano("Be' non lo so") is False
    # elisione: l'apostrofo deve restare non segnalato anche vicino ai troncamenti
    assert ha_apostrofo_scritto_a_mano("l'oggetto") is False
    assert ha_apostrofo_scritto_a_mano("un'arma") is False
    assert ha_apostrofo_scritto_a_mano("dell'acqua") is False


def test_non_ascii_residuo_elenca_cio_che_cp932_cancellerebbe():
    assert non_ascii_residuo("perche' tutto ok") == []
    assert non_ascii_residuo("perché") == ["é"]
    # il giapponese preesistente non e' un residuo: CP932 lo rappresenta
    assert non_ascii_residuo("バックパック") == []


# ⚠️ La degradazione ad apostrofo regge SOLO se l'accento sta sull'ultima
# lettera. «dei» e «elite» lo portano dentro e a schermo diventano «de'i» e
# «e'lite»: la lezione della 41a, che fino alla 71a non era una rete.

@pytest.mark.parametrize("testo,attese", [
    ("gli dèi del caos", ["dèi"]),
    ("un gladiatore d'élite", ["élite"]),
    ("perché più città però così", []),
    ("Sé stesso è qui", []),
    ("È vero", []),
    ("", []),
    ("バックパック", []),
])
def test_accenti_interni(testo, attese):
    assert accenti_interni(testo) == attese


def test_accento_interno_solo_se_seguito_da_LETTERE():
    # un accento finale seguito da punteggiatura o da un trattino non e' interno:
    # l'apostrofo resta in fondo alla parola, dove l'italiano lo scrive comunque
    assert accenti_interni("Perché?") == []
    assert accenti_interni("così-così") == []
    assert accenti_interni("città, e poi") == []
    # ma dentro una parola composta si', perche' li' l'apostrofo spezza
    assert accenti_interni("dèi-guerrieri") == ["dèi"]


def test_nessun_accento_interno_in_tutto_il_dizionario():
    """La rete gira sul corpus vero, non su un caso costruito (regola della 56a)."""
    from pathlib import Path
    from strumenti import percorsi
    colpite = []
    for percorso in sorted(Path(percorsi.DIZIONARIO).rglob("*.jsonl")):
        for riga in percorso.read_text(encoding="utf-8").splitlines():
            if not riga.strip():
                continue
            voce = json.loads(riga)
            for parola in accenti_interni(voce.get("it") or ""):
                colpite.append(f"{percorso.name}:{voce.get('riga') or voce.get('blocco')} {parola}")
    assert colpite == [], f"{len(colpite)} rese con l'accento dentro la parola: {colpite[:10]}"
