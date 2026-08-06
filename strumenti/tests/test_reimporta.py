import json

import pytest

from strumenti.reimporta import reimporta


def voce(firma, it, **extra):
    # i campi sono quelli che estrai.py produce davvero: en_grezzo compreso.
    # Senza, la voce non e' una voce di dizionario valida e verifica.py la
    # segnala (giustamente) come incompleta.
    base = {
        "firma": firma, "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "はい", "jp_grezzo": '"はい"',
        "en": "Yes", "en_grezzo": '"Yes"',
        "tipo": "statica", "contesto": "", "it": it,
    }
    base.update(extra)
    return base


def test_scrive_le_voci_pulite():
    esito = reimporta([voce("a", "Sì")], {})
    assert esito["a"]["it"] == "Sì"


def test_rifiuta_l_intero_lotto_se_una_voce_e_sporca():
    with pytest.raises(ValueError, match="1 voci con problemi"):
        reimporta([voce("a", "Sì"), voce("b", "")], {})


def test_un_lotto_sporco_non_scrive_niente():
    dizionario = {}
    with pytest.raises(ValueError):
        reimporta([voce("a", "Sì"), voce("b", "")], dizionario)
    assert dizionario == {}


def test_sovrascrive_una_voce_gia_presente():
    dizionario = {"a": voce("a", "Si")}
    esito = reimporta([voce("a", "Sì")], dizionario)
    assert esito["a"]["it"] == "Sì"


def test_un_lotto_sporco_non_tocca_un_dizionario_gia_popolato():
    # il caso avverso che mancava: dizionario gia' popolato, voce sporca
    # IN MEZZO a voci valide. Il test con dizionario vuoto e voce sporca in
    # coda passerebbe anche con scritture incrementali.
    preesistente = {
        "vecchia1": voce("vecchia1", "Prima", riga=1),
        "vecchia2": voce("vecchia2", "Seconda", riga=2),
    }
    dizionario = dict(preesistente)
    istantanea = json.dumps(dizionario, sort_keys=True, ensure_ascii=False)

    with pytest.raises(ValueError):
        reimporta([voce("a", "Sì"), voce("b", ""), voce("c", "No")], dizionario)

    assert dizionario == preesistente
    assert json.dumps(dizionario, sort_keys=True, ensure_ascii=False) == istantanea
    assert "a" not in dizionario and "c" not in dizionario


def test_reimporta_fonde_in_place_nel_dizionario_ricevuto():
    dizionario = {}
    esito = reimporta([voce("a", "Sì")], dizionario)
    assert esito is dizionario
    assert dizionario["a"]["it"] == "Sì"


def test_main_valida_tutti_i_gruppi_prima_di_scrivere(monkeypatch, tmp_path, capsys):
    # un lotto che tocca due file, con la voce sporca nel secondo: il primo
    # file non deve arrivare su disco.
    import importlib
    monkeypatch.setenv("ELONA_IT_DIZIONARIO", str(tmp_path / "diz"))
    from strumenti import percorsi
    importlib.reload(percorsi)
    import strumenti.reimporta as modulo
    importlib.reload(modulo)

    lotto = tmp_path / "lotto.jsonl"
    lotto.write_text(
        json.dumps(voce("a", "Sì", file="text.hsp"), ensure_ascii=False) + "\n"
        + json.dumps(voce("b", "", file="proc.hsp"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr("sys.argv", ["reimporta", str(lotto)])

    with pytest.raises(SystemExit) as uscita:
        modulo.main()
    # messaggio leggibile, non un traceback nudo
    assert "lotto rifiutato" in str(uscita.value)
    assert not (tmp_path / "diz" / "text.hsp.jsonl").exists()

    monkeypatch.delenv("ELONA_IT_DIZIONARIO")
    importlib.reload(percorsi)
    importlib.reload(modulo)


def test_la_scrittura_del_dizionario_e_atomica(monkeypatch, tmp_path):
    # un'interruzione a meta' non deve troncare il dizionario preesistente
    import importlib
    monkeypatch.setenv("ELONA_IT_DIZIONARIO", str(tmp_path / "diz"))
    from strumenti import percorsi
    importlib.reload(percorsi)
    import strumenti.reimporta as modulo
    importlib.reload(modulo)

    modulo.salva_dizionario("text.hsp", {"a": voce("a", "Prima")})
    percorso = tmp_path / "diz" / "text.hsp.jsonl"
    intatto = percorso.read_bytes()

    vero_dumps = json.dumps

    def esplode(*args, **kwargs):
        raise KeyboardInterrupt("interruzione a meta' scrittura")

    monkeypatch.setattr(modulo.json, "dumps", esplode)
    with pytest.raises(KeyboardInterrupt):
        modulo.salva_dizionario("text.hsp", {"b": voce("b", "Seconda")})
    monkeypatch.setattr(modulo.json, "dumps", vero_dumps)

    assert percorso.read_bytes() == intatto
    assert not list((tmp_path / "diz").glob("*.tmp"))

    monkeypatch.delenv("ELONA_IT_DIZIONARIO")
    importlib.reload(percorsi)
    importlib.reload(modulo)
