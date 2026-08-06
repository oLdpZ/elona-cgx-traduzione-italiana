# strumenti/tests/test_percorsi.py
from pathlib import Path
from strumenti import percorsi


def test_i_percorsi_sono_assoluti():
    for nome in ("RADICE_LAVORO", "SORGENTE", "BUILD", "DIST", "HSP", "GIOCO", "PROGETTO"):
        valore = getattr(percorsi, nome)
        assert isinstance(valore, Path), f"{nome} non e' un Path"
        assert valore.is_absolute(), f"{nome} non e' assoluto"


def test_sorgente_e_dentro_la_radice_di_lavoro():
    assert percorsi.SORGENTE.parent == percorsi.RADICE_LAVORO
    assert percorsi.BUILD.parent == percorsi.RADICE_LAVORO
    assert percorsi.DIST.parent == percorsi.RADICE_LAVORO


def test_il_dizionario_sta_nel_vault_non_nella_radice_di_lavoro():
    assert percorsi.RADICE_LAVORO not in percorsi.DIZIONARIO.parents


def test_la_radice_di_lavoro_si_puo_ridefinire(monkeypatch):
    monkeypatch.setenv("ELONA_IT_LAVORO", r"D:\altrove")
    import importlib
    ricaricato = importlib.reload(percorsi)
    assert ricaricato.RADICE_LAVORO == Path(r"D:\altrove")
    assert ricaricato.SORGENTE == Path(r"D:\altrove\sorgente")
    monkeypatch.delenv("ELONA_IT_LAVORO")
    importlib.reload(percorsi)


def test_il_dizionario_si_puo_ridefinire(monkeypatch, tmp_path):
    # senza questa variabile ogni prova d'integrazione scriverebbe nel
    # dizionario vero del vault
    monkeypatch.setenv("ELONA_IT_DIZIONARIO", str(tmp_path / "diz"))
    import importlib
    ricaricato = importlib.reload(percorsi)
    assert ricaricato.DIZIONARIO == tmp_path / "diz"
    monkeypatch.delenv("ELONA_IT_DIZIONARIO")
    importlib.reload(percorsi)
