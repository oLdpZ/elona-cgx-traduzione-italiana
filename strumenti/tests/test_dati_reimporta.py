# strumenti/tests/test_dati_reimporta.py
"""La promozione di un lotto a dizionario dei file dati.

Il lotto e il dizionario hanno la **stessa forma**, quindi promuovere e' fondere
per firma. Quel che il passo aggiunge non e' una conversione: e' il **rifiuto**.
Un lotto con problemi non entra nel dizionario, perche' il dizionario e' la
sorgente di verita' del progetto e ci si arriva solo passando dalle reti.
"""
import json

import pytest

from strumenti import dati_reimporta


def voce(blocco, it, riga=1, en=None):
    return {"firma": f"{blocco}-{riga}", "file": "board.txt", "blocco": blocco,
            "riga": riga, "en": en or f"{blocco} titolo:corpo {{reward}}",
            "jp_contesto": [], "it": it}


def test_un_lotto_pulito_entra_nel_dizionario(tmp_path):
    lotto = [voce("A", "Titolo:corpo {reward}")]
    destinazione = tmp_path / "board.txt.jsonl"
    quante = dati_reimporta.reimporta(lotto, destinazione)
    assert quante == 1
    scritte = [json.loads(r) for r in destinazione.read_text(encoding="utf-8").splitlines()]
    assert scritte[0]["it"] == "Titolo:corpo {reward}"


def test_un_lotto_con_problemi_e_rifiutato(tmp_path):
    lotto = [voce("A", "senza due punti {reward}")]
    destinazione = tmp_path / "board.txt.jsonl"
    with pytest.raises(SystemExit):
        dati_reimporta.reimporta(lotto, destinazione)
    assert not destinazione.exists(), "un lotto rifiutato non lascia niente"


def test_fondere_aggiorna_le_voci_esistenti_e_aggiunge_le_nuove(tmp_path):
    destinazione = tmp_path / "board.txt.jsonl"
    dati_reimporta.reimporta([voce("A", "Prima:corpo {reward}")], destinazione)
    dati_reimporta.reimporta(
        [voce("A", "Dopo:corpo {reward}"), voce("B", "Nuova:corpo {reward}")],
        destinazione)
    scritte = {v["blocco"]: v["it"] for v in
               (json.loads(r) for r in destinazione.read_text(encoding="utf-8").splitlines())}
    assert scritte == {"A": "Dopo:corpo {reward}", "B": "Nuova:corpo {reward}"}


def test_le_voci_restano_in_ordine_stabile(tmp_path):
    destinazione = tmp_path / "board.txt.jsonl"
    dati_reimporta.reimporta(
        [voce("Z", "Zeta:corpo {reward}"), voce("A", "Alfa:corpo {reward}"),
         voce("A", "Alfa due:corpo {reward}", riga=2)], destinazione)
    ordine = [(v["blocco"], v["riga"]) for v in
              (json.loads(r) for r in destinazione.read_text(encoding="utf-8").splitlines())]
    assert ordine == [("A", 1), ("A", 2), ("Z", 1)]
