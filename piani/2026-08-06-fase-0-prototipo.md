# Fase 0 — Prototipo tecnico — Piano di implementazione

> **Per esecutori agentici:** SUB-SKILL RICHIESTA: usare `superpowers:subagent-driven-development` (consigliata) oppure `superpowers:executing-plans` per implementare questo piano compito per compito. I passi usano caselle (`- [ ]`) per il tracciamento.

**Obiettivo:** dimostrare che il ciclo completo `estrai → traduci → applica → compila → installa → verifica` produce un Elona+ Custom-GX giocabile con ~50 stringhe in italiano, e individuare dove risiedono i nomi degli oggetti.

**Architettura:** il sorgente upstream non viene mai modificato. Il dizionario JSONL vive nel vault e viene iniettato da `applica.py` su una copia del clone, producendo un albero di build che il compilatore HSP trasforma in `elonapluscgx-it.exe`. Il dizionario conserva l'italiano con gli accenti veri; la degradazione in forma con apostrofo (`perché` → `perche'`) avviene solo in fase di build, perché CP932 cancellerebbe gli accenti in silenzio.

**Stack:** Python 3.14.3, pytest 9.0.3, git 2.53.0, HSP 3.4 SDK, PowerShell 7.

**Spec di riferimento:** `../SPEC.md` (approvato 2026-08-06).

## Vincoli globali

- **Progetto:** `C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana` — d'ora in poi `$PROGETTO`. Contiene **solo testo**.
- **Radice di lavoro:** `C:\Games\Elona\_traduzione` — d'ora in poi `$LAVORO`. Contiene `hsp34/`, `sorgente/`, `build/`, `dist/`. Mai versionata nel vault.
- **Gioco installato:** `C:\Games\Elona\elonaplus2.31`.
- **Upstream:** `https://github.com/JianmengYu/ElonaPlusCustom-GX`, branch `work`, sorgente in `2.05-custom-gx/`.
- **Encoding:** i `.hsp` si leggono e si scrivono in **CP932**. Il dizionario e i lotti JSONL sono **UTF-8**.
- **Nessuno script scrive mai dentro `$LAVORO\sorgente\`.** È di sola lettura per costruzione.
- **Vocali da degradare:** `à è é ì ò ù À È É Ì Ò Ù` → `a' e' e' i' o' u' A' E' E' I' O' U'`. Nient'altro.
- **Lingua:** codice e commenti in italiano, coerente con il progetto gemello Elin.
- I test stanno in `$PROGETTO\strumenti\tests\` e si eseguono con `python -m pytest strumenti/tests -v` da `$PROGETTO`.

---

## Struttura dei file

| file | responsabilità |
|---|---|
| `strumenti/percorsi.py` | unico posto che conosce i percorsi d'ambiente; tutti gli altri script lo importano |
| `strumenti/accenti.py` | degradazione accenti → apostrofo, e rilevamento di forme con apostrofo scritte a mano |
| `strumenti/estrai.py` | dal sorgente produce lotti JSONL, classificando statiche e dinamiche |
| `strumenti/reimporta.py` | valida un lotto tradotto e lo scrive nel dizionario |
| `strumenti/verifica.py` | regole di blocco su lotto e su dizionario |
| `strumenti/applica.py` | costruisce l'albero di build iniettando il dizionario |
| `strumenti/compila.py` | invoca il compilatore HSP sull'albero di build |
| `strumenti/installa.py` | copia la build nel gioco preservando inglese e salvataggi |

Ogni file ha una responsabilità sola, ingresso e uscita su file, ed è invocabile e testabile isolatamente.

---

## Task 1: Ambiente e prova del cancello

Il vero rischio del progetto: se l'eseguibile non si ricompila da sorgente **non modificato**, tutto il resto è teoria. Questo compito non traduce niente — dimostra soltanto che si può ricostruire ciò che già esiste.

**File:**
- Creare: `$LAVORO\sorgente\` (clone), `$LAVORO\hsp34\` (già presente)
- Creare: `$PROGETTO\decisioni.md`

- [ ] **Passo 1: Verificare che l'SDK sia a posto**

```powershell
$LAVORO = "C:\Games\Elona\_traduzione"
foreach ($f in 'hsp34\hsed3.exe','hsp34\hsp3.exe','hsp34\hspcmp.dll','hsp34\common\hspcmp.as') {
  "{0,-28} {1}" -f $f, (Test-Path (Join-Path $LAVORO $f))
}
```

Atteso: quattro `True`. Se no, riestrarre `$LAVORO\hsp34a.zip` **specificando CP932 per i nomi delle voci** — `Expand-Archive` corrompe i nomi giapponesi e fallisce.

- [ ] **Passo 2: Clonare il sorgente upstream**

```powershell
$LAVORO = "C:\Games\Elona\_traduzione"
git clone --depth 1 --branch work https://github.com/JianmengYu/ElonaPlusCustom-GX.git "$LAVORO\sorgente"
git -C "$LAVORO\sorgente" rev-parse HEAD
```

Annotare l'hash del commit: è la base a cui il dizionario si riferisce.

- [ ] **Passo 3: Piazzare `hsplua.dll` nella cartella dell'SDK**

Il gioco fallisce all'avvio senza questa DLL quando è lanciato dall'editor.

```powershell
$LAVORO = "C:\Games\Elona\_traduzione"
Copy-Item "$LAVORO\sorgente\2.05-custom-gx\hsplua.dll" "$LAVORO\hsp34\hsplua.dll"
Test-Path "$LAVORO\hsp34\hsplua.dll"
```

Atteso: `True`.

- [ ] **Passo 4: Compilare da sorgente non modificato**

Passo manuale e da fare una volta sola: serve a scoprire la ricetta, che poi il Task 2 automatizza.

1. Avviare `$LAVORO\hsp34\hsed3.exe`
2. Aprire `$LAVORO\sorgente\2.05-custom-gx\main.hsp`
3. Premere `Ctrl+F9` (crea eseguibile)

Atteso: viene prodotto `elonapluscgx.exe` dentro `2.05-custom-gx\`.

Se compare un errore di compilazione, **fermarsi e riportarlo**: è il cancello, e non si prosegue aggirandolo.

- [ ] **Passo 5: Verificare che l'eseguibile prodotto funzioni**

```powershell
$LAVORO = "C:\Games\Elona\_traduzione"
$src = "$LAVORO\sorgente\2.05-custom-gx"
Get-Item "$src\elonapluscgx.exe" | Select-Object Name, Length, LastWriteTime
$p = Start-Process "$src\elonapluscgx.exe" -WorkingDirectory $src -PassThru
Start-Sleep 8
if ($p.HasExited) { "USCITO codice $($p.ExitCode)" } else { "IN ESECUZIONE titolo='$($p.MainWindowTitle)'"; $p.CloseMainWindow() | Out-Null }
```

Atteso: `IN ESECUZIONE` con titolo `Elona+ Custom-GX 2.31.2.0`. Dimensione confrontabile con i 16.895.548 byte dell'eseguibile ufficiale — non necessariamente identica (il compilatore incorpora percorsi e timestamp), ma dello stesso ordine.

- [ ] **Passo 6: Registrare la ricetta**

Creare `$PROGETTO\decisioni.md` annotando: hash del commit upstream, versione dell'SDK, sequenza esatta che ha prodotto l'eseguibile, dimensione ottenuta, ed eventuali intoppi incontrati e come sono stati risolti.

- [ ] **Passo 7: Commit**

```bash
cd "$PROGETTO"
git add decisioni.md
git commit -m "Fase 0: il cancello passa, l'exe si ricompila da sorgente non modificato"
```

---

## Task 2: `percorsi.py` — i percorsi in un posto solo

**File:**
- Creare: `strumenti/percorsi.py`
- Test: `strumenti/tests/test_percorsi.py`

**Interfacce:**
- Consuma: niente
- Produce: `RADICE_LAVORO: Path`, `SORGENTE: Path`, `BUILD: Path`, `DIST: Path`, `HSP: Path`, `GIOCO: Path`, `PROGETTO: Path`, `DIZIONARIO: Path`, `LAVORO_LOTTI: Path`

- [ ] **Passo 1: Scrivere il test che fallisce**

```python
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
```

- [ ] **Passo 2: Eseguire il test e verificare che fallisca**

```
python -m pytest strumenti/tests/test_percorsi.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.percorsi'`.

- [ ] **Passo 3: Scrivere l'implementazione minima**

```python
# strumenti/percorsi.py
"""Unico punto che conosce i percorsi d'ambiente. Tutti gli altri script importano da qui."""
import os
from pathlib import Path

PROGETTO = Path(__file__).resolve().parent.parent

RADICE_LAVORO = Path(os.environ.get("ELONA_IT_LAVORO", r"C:\Games\Elona\_traduzione"))
SORGENTE = RADICE_LAVORO / "sorgente"
BUILD = RADICE_LAVORO / "build"
DIST = RADICE_LAVORO / "dist"
HSP = RADICE_LAVORO / "hsp34"

GIOCO = Path(os.environ.get("ELONA_IT_GIOCO", r"C:\Games\Elona\elonaplus2.31"))

DIZIONARIO = PROGETTO / "dizionario"
LAVORO_LOTTI = PROGETTO / "lavoro"

# sottocartella del sorgente che contiene gli .hsp
SORGENTE_HSP = SORGENTE / "2.05-custom-gx"
BUILD_HSP = BUILD / "2.05-custom-gx"
```

Creare anche `strumenti/__init__.py` e `strumenti/tests/__init__.py` vuoti.

- [ ] **Passo 4: Eseguire il test e verificare che passi**

```
python -m pytest strumenti/tests/test_percorsi.py -v
```

Atteso: 4 passed.

- [ ] **Passo 5: Commit**

```bash
git add strumenti/__init__.py strumenti/percorsi.py strumenti/tests/
git commit -m "percorsi.py: i percorsi d'ambiente in un posto solo"
```

---

## Task 3: `accenti.py` — la degradazione

Il punto unico in cui l'italiano corretto diventa italiano compatibile con CP932. Se sbaglia qui, sbaglia ovunque, silenziosamente.

**File:**
- Creare: `strumenti/accenti.py`
- Test: `strumenti/tests/test_accenti.py`

**Interfacce:**
- Consuma: niente
- Produce: `degrada(testo: str) -> str`, `ha_apostrofo_scritto_a_mano(testo: str) -> bool`, `non_ascii_residuo(testo: str) -> list[str]`

- [ ] **Passo 1: Scrivere i test che falliscono**

```python
# strumenti/tests/test_accenti.py
import pytest
from strumenti.accenti import degrada, ha_apostrofo_scritto_a_mano, non_ascii_residuo


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


def test_non_ascii_residuo_elenca_cio_che_cp932_cancellerebbe():
    assert non_ascii_residuo("perche' tutto ok") == []
    assert non_ascii_residuo("perché") == ["é"]
    # il giapponese preesistente non e' un residuo: CP932 lo rappresenta
    assert non_ascii_residuo("バックパック") == []
```

- [ ] **Passo 2: Eseguire i test e verificare che falliscano**

```
python -m pytest strumenti/tests/test_accenti.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.accenti'`.

- [ ] **Passo 3: Scrivere l'implementazione**

```python
# strumenti/accenti.py
"""Conversione fra italiano corretto (dizionario) e italiano CP932 (albero di build).

CP932 non contiene le vocali accentate italiane e le sostituisce silenziosamente
con la vocale nuda. La forma con apostrofo e' l'unica affidabile, ma il dizionario
conserva sempre l'accento vero: la degradazione avviene solo qui.
"""
import re

TABELLA = {
    "à": "a'", "è": "e'", "é": "e'", "ì": "i'", "ò": "o'", "ù": "u'",
    "À": "A'", "È": "E'", "É": "E'", "Ì": "I'", "Ò": "O'", "Ù": "U'",
}

# vocale nuda + apostrofo a fine parola: la forma che il traduttore non deve scrivere.
# L'elisione italiana (l'oggetto, dell'acqua) ha l'apostrofo dopo consonante.
# Le eccezioni legittime con vocale + apostrofo si escludono per elenco:
# "un'" (elisione) e "po'" (troncamento di "poco").
_ELISIONI = {"un'", "Un'", "po'", "Po'"}
_APOSTROFO_A_MANO = re.compile(r"[aeiouAEIOU]'(?![a-zA-Zà-ùÀ-Ù])")


def degrada(testo: str) -> str:
    """Sostituisce le vocali accentate italiane con la forma vocale + apostrofo."""
    for accentata, piana in TABELLA.items():
        testo = testo.replace(accentata, piana)
    return testo


def ha_apostrofo_scritto_a_mano(testo: str) -> bool:
    """Vero se il testo contiene una forma con apostrofo che doveva essere un accento.

    Distingue dall'elisione italiana, in cui l'apostrofo e' seguito da una lettera.
    """
    for elisione in _ELISIONI:
        testo = testo.replace(elisione, "")
    return _APOSTROFO_A_MANO.search(testo) is not None


def non_ascii_residuo(testo: str) -> list[str]:
    """Caratteri che CP932 non sa rappresentare: sarebbero cancellati in silenzio.

    Il giapponese preesistente non e' un residuo, perche' CP932 lo codifica.
    """
    residui = []
    for carattere in testo:
        if ord(carattere) < 128:
            continue
        try:
            ritorno = carattere.encode("cp932").decode("cp932")
        except (UnicodeEncodeError, UnicodeDecodeError):
            residui.append(carattere)
            continue
        if ritorno != carattere:
            residui.append(carattere)
    return residui
```

- [ ] **Passo 4: Eseguire i test e verificare che passino**

```
python -m pytest strumenti/tests/test_accenti.py -v
```

Atteso: 14 passed. Se `test_apostrofo_legittimo_non_e_un_falso_positivo` fallisce, correggere `_APOSTROFO_A_MANO` — **non** indebolire il test: i falsi positivi su `l'oggetto` renderebbero `verifica.py` inutilizzabile.

- [ ] **Passo 5: Commit**

```bash
git add strumenti/accenti.py strumenti/tests/test_accenti.py
git commit -m "accenti.py: degradazione accenti e rilevamento di apostrofi scritti a mano"
```

---

## Task 4: `estrai.py` — dal sorgente ai lotti

**File:**
- Creare: `strumenti/estrai.py`
- Test: `strumenti/tests/test_estrai.py`

**Interfacce:**
- Consuma: `percorsi.SORGENTE_HSP`
- Produce: `estrai_da_testo(nome_file: str, testo: str) -> list[dict]`, `firma(giapponese: str, inglese: str) -> str`, `e_dinamica(inglese_grezzo: str) -> bool`

Ogni voce estratta è un dizionario con: `firma`, `file`, `riga`, `occorrenza`, `jp`, `en`, `tipo` (`"statica"` o `"dinamica"`), `contesto` (la riga sorgente intera, solo per le dinamiche), `it` (vuoto).

- [ ] **Passo 1: Scrivere i test che falliscono**

```python
# strumenti/tests/test_estrai.py
from strumenti.estrai import estrai_da_testo, firma, e_dinamica

STATICA = '#define global txt_invfull txt lang("バックパックが一杯だ。", "Your inventory is full.")'
DINAMICA = '#define global txt_guard txt lang(name(tc) + "は" + name(x) + "をかばった！", name(tc) + " guarded " + name(x) + ".")'
DUE_SULLA_STESSA_RIGA = 'a = lang("はい", "Yes"), lang("いいえ", "No")'


def test_estrae_una_statica():
    voci = estrai_da_testo("text.hsp", STATICA)
    assert len(voci) == 1
    voce = voci[0]
    assert voce["jp"] == "バックパックが一杯だ。"
    assert voce["en"] == "Your inventory is full."
    assert voce["tipo"] == "statica"
    assert voce["it"] == ""
    assert voce["file"] == "text.hsp"
    assert voce["riga"] == 1


def test_riconosce_una_dinamica_e_ne_conserva_il_contesto():
    voci = estrai_da_testo("text.hsp", DINAMICA)
    assert len(voci) == 1
    assert voci[0]["tipo"] == "dinamica"
    assert voci[0]["contesto"] == DINAMICA


def test_conserva_l_espressione_grezza():
    # per le dinamiche si traduce l'espressione intera, non i soli letterali:
    # in italiano l'ordine dei pezzi cambia
    voce = estrai_da_testo("text.hsp", DINAMICA)[0]
    assert voce["en_grezzo"] == 'name(tc) + " guarded " + name(x) + "."'
    assert voce["en"] == " guarded ."

    statica = estrai_da_testo("text.hsp", STATICA)[0]
    assert statica["en_grezzo"] == '"Your inventory is full."'
    assert statica["en"] == "Your inventory is full."


def test_le_statiche_non_portano_contesto():
    assert estrai_da_testo("text.hsp", STATICA)[0]["contesto"] == ""


def test_estrae_piu_occorrenze_dalla_stessa_riga():
    voci = estrai_da_testo("text.hsp", DUE_SULLA_STESSA_RIGA)
    assert [v["en"] for v in voci] == ["Yes", "No"]


def test_le_firme_sono_stabili_e_distinte():
    assert firma("はい", "Yes") == firma("はい", "Yes")
    assert firma("はい", "Yes") != firma("はい", "No")
    assert firma("いいえ", "Yes") != firma("はい", "Yes")


def test_i_duplicati_esatti_si_distinguono_per_occorrenza():
    testo = 'a = lang("はい", "Yes")\nb = lang("はい", "Yes")'
    voci = estrai_da_testo("text.hsp", testo)
    assert len(voci) == 2
    assert voci[0]["occorrenza"] == 0
    assert voci[1]["occorrenza"] == 1
    assert voci[0]["firma"] == voci[1]["firma"]


def test_e_dinamica_distingue_concatenazioni():
    assert e_dinamica('"Your inventory is full."') is False
    assert e_dinamica('name(tc) + " guarded " + name(x) + "."') is True
    assert e_dinamica('"You create " + itemname(ci, 1) + "!"') is True


def test_ignora_le_righe_senza_lang():
    assert estrai_da_testo("text.hsp", "	sdim bodyn, 4, 15") == []


def test_ignora_le_stringhe_con_inglese_vuoto():
    # particelle giapponesi che in inglese non esistono: niente da tradurre.
    # In text.hsp sono 6 casi reali, es. lang("層", "")
    assert estrai_da_testo("text.hsp", 'buff += lang("残り", "")') == []
```

- [ ] **Passo 2: Eseguire i test e verificare che falliscano**

```
python -m pytest strumenti/tests/test_estrai.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.estrai'`.

- [ ] **Passo 3: Scrivere l'implementazione**

```python
# strumenti/estrai.py
"""Estrazione delle coppie lang(giapponese, inglese) dal sorgente HSP verso lotti JSONL."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from strumenti import percorsi

# lang( arg1 , arg2 ) con stringhe fra virgolette ed eventuali concatenazioni.
# Le parentesi annidate delle chiamate di funzione richiedono una scansione, non una regex sola.
_INIZIO = re.compile(r"\blang\(")


def firma(giapponese: str, inglese: str) -> str:
    """Chiave stabile della stringa. Se l'inglese cambia a monte, la firma si rompe di proposito."""
    grezzo = giapponese.encode("utf-8") + b"\x00" + inglese.encode("utf-8")
    return hashlib.sha1(grezzo).hexdigest()


def e_dinamica(argomento_grezzo: str) -> bool:
    """Vero se l'argomento concatena qualcosa oltre a una stringa letterale."""
    return "+" in argomento_grezzo


def _argomenti(testo: str, apertura: int) -> tuple[str, str, int, int] | None:
    """Argomenti grezzi di lang( ... ) piu' le posizioni del secondo.

    Ritorna (grezzo_jp, grezzo_en, inizio_en, fine_en) oppure None se malformata.
    Le posizioni servono ad applica.py per sostituire senza ricerche fragili.
    """
    profondita = 0
    dentro_stringa = False
    virgola = -1
    indice = apertura
    while indice < len(testo):
        carattere = testo[indice]
        if carattere == '"':
            dentro_stringa = not dentro_stringa
        elif not dentro_stringa:
            if carattere == "(":
                profondita += 1
            elif carattere == ")":
                profondita -= 1
                if profondita == 0:
                    if virgola == -1:
                        return None
                    grezzo_jp = testo[apertura + 1:virgola]
                    crudo_en = testo[virgola + 1:indice]
                    # scarta gli spazi attorno al secondo argomento, ma tieni le posizioni reali
                    scarto_sinistra = len(crudo_en) - len(crudo_en.lstrip())
                    scarto_destra = len(crudo_en) - len(crudo_en.rstrip())
                    inizio_en = virgola + 1 + scarto_sinistra
                    fine_en = indice - scarto_destra
                    return grezzo_jp.strip(), crudo_en.strip(), inizio_en, fine_en
            elif carattere == "," and profondita == 1 and virgola == -1:
                virgola = indice
        indice += 1
    return None


def _letterali(argomento_grezzo: str) -> str:
    """Concatena i letterali fra virgolette, che sono la parte traducibile."""
    return "".join(re.findall(r'"([^"]*)"', argomento_grezzo))


def estrai_da_testo(nome_file: str, testo: str) -> list[dict]:
    """Estrae tutte le coppie lang() da un sorgente gia' decodificato."""
    voci: list[dict] = []
    conteggio: dict[str, int] = {}
    for numero_riga, riga in enumerate(testo.splitlines(), start=1):
        for trovato in _INIZIO.finditer(riga):
            argomenti = _argomenti(riga, trovato.end() - 1)
            if argomenti is None:
                continue
            grezzo_jp, grezzo_en, _, _ = argomenti
            giapponese = _letterali(grezzo_jp)
            inglese = _letterali(grezzo_en)
            if not inglese:
                continue
            chiave = firma(giapponese, inglese)
            occorrenza = conteggio.get(chiave, 0)
            conteggio[chiave] = occorrenza + 1
            dinamica = e_dinamica(grezzo_en)
            voci.append({
                "firma": chiave,
                "file": nome_file,
                "riga": numero_riga,
                "occorrenza": occorrenza,
                "jp": giapponese,
                "jp_grezzo": grezzo_jp,
                "en": inglese,
                # per le dinamiche si traduce l'espressione intera: in italiano
                # l'ordine dei pezzi concatenati cambia
                "en_grezzo": grezzo_en,
                "tipo": "dinamica" if dinamica else "statica",
                "contesto": riga if dinamica else "",
                "it": "",
            })
    return voci


def estrai_da_file(percorso: Path) -> list[dict]:
    testo = percorso.read_bytes().decode("cp932")
    return estrai_da_testo(percorso.name, testo)


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Estrae un lotto JSONL dal sorgente HSP.")
    analizzatore.add_argument("file", nargs="+", help="nomi dei file .hsp, es. text.hsp")
    analizzatore.add_argument("--uscita", required=True, help="percorso del lotto JSONL da scrivere")
    analizzatore.add_argument("--max", type=int, default=0, help="numero massimo di voci (0 = tutte)")
    argomenti = analizzatore.parse_args()

    voci: list[dict] = []
    for nome in argomenti.file:
        voci.extend(estrai_da_file(percorsi.SORGENTE_HSP / nome))
    if argomenti.max:
        voci = voci[:argomenti.max]

    uscita = Path(argomenti.uscita)
    uscita.parent.mkdir(parents=True, exist_ok=True)
    with uscita.open("w", encoding="utf-8") as scrittura:
        for voce in voci:
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    print(f"{len(voci)} voci in {uscita}")


if __name__ == "__main__":
    main()
```

- [ ] **Passo 4: Eseguire i test e verificare che passino**

```
python -m pytest strumenti/tests/test_estrai.py -v
```

Atteso: 10 passed.

- [ ] **Passo 5: Confrontare con il conteggio noto**

```powershell
python -m strumenti.estrai text.hsp --uscita lavoro\controllo-text.jsonl
```

Atteso: **2146 voci** — di cui **1915 statiche e 231 dinamiche**.

(La ripartizione era 1909/237 prima della revisione finale della Fase 0: sei
stringhe statiche il cui testo contiene un `+` — `"Enchantment Bonus + 4"` e
simili — risultavano dinamiche. Vedi `SPEC.md` §2. Il totale non cambia.)

`text.hsp` contiene 2152 occorrenze di `lang(`, ma 6 hanno l'inglese **vuoto di
proposito**: sono particelle giapponesi che in inglese non esistono, come
`lang("層", "")` e `lang("まで護衛", "")`. Non c'è niente da tradurre e vanno
saltate. Verificato eseguendo l'algoritmo sul sorgente reale il 2026-08-06.

Se il conteggio differisce da 2146, l'estrattore sbaglia — indagare prima di
proseguire, non aggiustare il numero atteso.

- [ ] **Passo 6: Commit**

```bash
git add strumenti/estrai.py strumenti/tests/test_estrai.py
git commit -m "estrai.py: estrazione lang() con classificazione statiche/dinamiche"
```

---

## Task 5: `verifica.py` — le regole di blocco

**File:**
- Creare: `strumenti/verifica.py`
- Test: `strumenti/tests/test_verifica.py`

**Interfacce:**
- Consuma: `accenti.degrada`, `accenti.ha_apostrofo_scritto_a_mano`, `accenti.non_ascii_residuo`
- Produce: `controlla_voce(voce: dict) -> list[str]`, `controlla_lotto(voci: list[dict]) -> dict[str, list[str]]`

`controlla_voce` ritorna la lista dei problemi trovati; lista vuota significa voce pulita.

- [ ] **Passo 1: Scrivere i test che falliscono**

```python
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
    problemi = controlla_voce(voce(it="Zaino pieno \u2014 davvero"))  # trattino lungo
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


def test_controlla_lotto_indicizza_per_firma():
    esito = controlla_lotto([voce(firma="uno", it=""), voce(firma="due", it="Zaino pieno.")])
    assert "uno" in esito
    assert "due" not in esito
```

- [ ] **Passo 2: Eseguire i test e verificare che falliscano**

```
python -m pytest strumenti/tests/test_verifica.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.verifica'`.

- [ ] **Passo 3: Scrivere l'implementazione**

```python
# strumenti/verifica.py
"""Regole di blocco sui lotti e sul dizionario. Vedi SPEC.md paragrafo 7."""
import argparse
import json
import re
from pathlib import Path

from strumenti.accenti import ha_apostrofo_scritto_a_mano, non_ascii_residuo

_CHIAMATE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def _chiamate(testo: str) -> list[str]:
    return sorted(_CHIAMATE.findall(testo))


def controlla_voce(voce: dict) -> list[str]:
    """Ritorna la lista dei problemi. Lista vuota significa voce pulita."""
    problemi: list[str] = []
    italiano = voce.get("it", "")

    if not italiano.strip():
        problemi.append("traduzione vuota")
        return problemi

    # per le dinamiche il termine di paragone e' l'espressione intera
    originale = voce["en_grezzo"] if voce["tipo"] == "dinamica" else voce["en"]
    if italiano == originale:
        problemi.append("traduzione identica all'inglese")

    if ha_apostrofo_scritto_a_mano(italiano):
        problemi.append(
            "apostrofo scritto a mano: nel dizionario va l'accento vero, "
            "la degradazione la fa applica.py"
        )

    residui = non_ascii_residuo(italiano)
    if residui:
        problemi.append(f"caratteri che CP932 cancellerebbe: {residui}")

    if voce["tipo"] == "dinamica":
        attese = _chiamate(voce["en_grezzo"])
        trovate = _chiamate(italiano)
        if attese != trovate:
            problemi.append(f"interpolazioni non conservate: attese {attese}, trovate {trovate}")

    return problemi


def controlla_lotto(voci: list[dict]) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema."""
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce)
        if problemi:
            esito[voce["firma"]] = problemi
    return esito


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Verifica un lotto JSONL tradotto.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(riga) for riga in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if riga.strip()]
    esito = controlla_lotto(voci)
    if not esito:
        print(f"{len(voci)} voci, nessun problema")
        return
    for chiave, problemi in esito.items():
        print(f"{chiave}: " + "; ".join(problemi))
    raise SystemExit(f"{len(esito)} voci con problemi su {len(voci)}")


if __name__ == "__main__":
    main()
```

- [ ] **Passo 4: Eseguire i test e verificare che passino**

```
python -m pytest strumenti/tests/test_verifica.py -v
```

Atteso: 7 passed.

- [ ] **Passo 5: Commit**

```bash
git add strumenti/verifica.py strumenti/tests/test_verifica.py
git commit -m "verifica.py: regole di blocco su vuoti, identiche, apostrofi, CP932 e interpolazioni"
```

---

## Task 6: `reimporta.py` — dal lotto al dizionario

**File:**
- Creare: `strumenti/reimporta.py`
- Test: `strumenti/tests/test_reimporta.py`

**Interfacce:**
- Consuma: `verifica.controlla_lotto`
- Produce: `reimporta(voci: list[dict], dizionario: dict) -> dict`, che solleva `ValueError` se il lotto non è pulito

Il dizionario su disco è `dizionario/<nome_file>.jsonl`, una voce per riga, ordinato per `riga` e `occorrenza`.

- [ ] **Passo 1: Scrivere i test che falliscono**

```python
# strumenti/tests/test_reimporta.py
import pytest
from strumenti.reimporta import reimporta


def voce(firma, it, **extra):
    base = {
        "firma": firma, "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "はい", "en": "Yes", "tipo": "statica", "contesto": "", "it": it,
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
```

- [ ] **Passo 2: Eseguire i test e verificare che falliscano**

```
python -m pytest strumenti/tests/test_reimporta.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.reimporta'`.

- [ ] **Passo 3: Scrivere l'implementazione**

```python
# strumenti/reimporta.py
"""Scrive un lotto tradotto nel dizionario, ma solo se l'intero lotto e' pulito."""
import argparse
import json
from pathlib import Path

from strumenti import percorsi
from strumenti.verifica import controlla_lotto


def reimporta(voci: list[dict], dizionario: dict) -> dict:
    """Valida il lotto e lo fonde nel dizionario. Tutto o niente."""
    problemi = controlla_lotto(voci)
    if problemi:
        dettaglio = "; ".join(f"{k}: {', '.join(v)}" for k, v in list(problemi.items())[:5])
        raise ValueError(f"{len(problemi)} voci con problemi — {dettaglio}")
    for voce in voci:
        dizionario[voce["firma"]] = voce
    return dizionario


def carica_dizionario(nome_file: str) -> dict:
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    if not percorso.exists():
        return {}
    voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    return {v["firma"]: v for v in voci}


def salva_dizionario(nome_file: str, dizionario: dict) -> Path:
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    percorso.parent.mkdir(parents=True, exist_ok=True)
    ordinate = sorted(dizionario.values(), key=lambda v: (v["riga"], v["occorrenza"]))
    with percorso.open("w", encoding="utf-8") as scrittura:
        for voce in ordinate:
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    return percorso


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Reimporta un lotto tradotto nel dizionario.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL tradotto")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    per_file: dict[str, list[dict]] = {}
    for voce in voci:
        per_file.setdefault(voce["file"], []).append(voce)

    for nome_file, gruppo in per_file.items():
        dizionario = reimporta(gruppo, carica_dizionario(nome_file))
        percorso = salva_dizionario(nome_file, dizionario)
        print(f"{len(gruppo)} voci in {percorso}")


if __name__ == "__main__":
    main()
```

- [ ] **Passo 4: Eseguire i test e verificare che passino**

```
python -m pytest strumenti/tests/test_reimporta.py -v
```

Atteso: 4 passed.

- [ ] **Passo 5: Commit**

```bash
git add strumenti/reimporta.py strumenti/tests/test_reimporta.py
git commit -m "reimporta.py: scrittura tutto-o-niente del lotto nel dizionario"
```

---

## Task 7: `applica.py` — l'albero di build

Il punto in cui il dizionario incontra il sorgente. **Non scrive mai dentro `SORGENTE`.**

**File:**
- Creare: `strumenti/applica.py`
- Test: `strumenti/tests/test_applica.py`

**Interfacce:**
- Consuma: `estrai.firma`, `accenti.degrada`, `percorsi.SORGENTE_HSP`, `percorsi.BUILD_HSP`
- Produce: `applica_a_testo(nome_file: str, testo: str, dizionario: dict) -> tuple[str, int]` che ritorna il testo modificato e il numero di sostituzioni

- [ ] **Passo 1: Scrivere i test che falliscono**

```python
# strumenti/tests/test_applica.py
from strumenti.applica import applica_a_testo
from strumenti.estrai import firma

STATICA = '	txt lang("バックパックが一杯だ。", "Your inventory is full.")'


def dizionario_con(jp, en, it, tipo="statica"):
    chiave = firma(jp, en)
    return {chiave: {
        "firma": chiave, "jp": jp, "jp_grezzo": f'"{jp}"',
        "en": en, "en_grezzo": f'"{en}"',
        "it": it, "tipo": tipo, "occorrenza": 0,
    }}


def test_sostituisce_l_inglese_con_l_italiano():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Il tuo zaino e' pieno.")
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, diz)
    assert sostituzioni == 1
    assert '"Il tuo zaino e\' pieno."' in testo
    assert "Your inventory is full." not in testo


def test_conserva_il_giapponese():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert "バックパックが一杯だ。" in testo


def test_degrada_gli_accenti_in_fase_di_applicazione():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "È già pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert '"E\' gia\' pieno."' in testo
    assert "È" not in testo


def test_lascia_intatte_le_stringhe_non_tradotte():
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, {})
    assert sostituzioni == 0
    assert testo == STATICA


def test_il_risultato_e_codificabile_in_cp932():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Perché è così")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    ritorno = testo.encode("cp932").decode("cp932")
    assert ritorno == testo


def test_conserva_i_fine_riga_crlf():
    sorgente = STATICA + "\r\n" + "	mes \"altro\"" + "\r\n"
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", sorgente, diz)
    assert "\r\n" in testo
    assert "\n" not in testo.replace("\r\n", "")
    assert testo.endswith("\r\n")
```

- [ ] **Passo 2: Eseguire i test e verificare che falliscano**

```
python -m pytest strumenti/tests/test_applica.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.applica'`.

- [ ] **Passo 3: Scrivere l'implementazione**

```python
# strumenti/applica.py
"""Costruisce l'albero di build iniettando il dizionario su una copia del sorgente.

SORGENTE non viene mai toccata: si copia in BUILD e si modifica la copia.
"""
import argparse
import json
import shutil

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.estrai import _argomenti, _letterali, firma, _INIZIO


def applica_a_testo(nome_file: str, testo: str, dizionario: dict) -> tuple[str, int]:
    """Sostituisce l'argomento inglese di lang() con l'italiano degradato.

    Conserva i fine riga originali: i .hsp usano CRLF e riscriverli in LF
    produrrebbe un diff totale e potrebbe disturbare il compilatore.
    """
    sostituzioni = 0
    conteggio: dict[str, int] = {}
    righe_uscita = []

    fine_riga = "\r\n" if "\r\n" in testo else "\n"
    termina_con_a_capo = testo.endswith(("\r\n", "\n"))

    for riga in testo.splitlines():
        pezzi = []
        cursore = 0
        for trovato in _INIZIO.finditer(riga):
            argomenti = _argomenti(riga, trovato.end() - 1)
            if argomenti is None:
                continue
            grezzo_jp, grezzo_en, inizio_en, fine_en = argomenti
            giapponese = _letterali(grezzo_jp)
            inglese = _letterali(grezzo_en)
            if not inglese:
                continue
            chiave = firma(giapponese, inglese)
            occorrenza = conteggio.get(chiave, 0)
            conteggio[chiave] = occorrenza + 1

            voce = dizionario.get(chiave)
            if voce is None or not voce.get("it"):
                continue
            if inizio_en < cursore:  # sovrapposizione: salta, non corrompere
                continue

            if voce["tipo"] == "dinamica":
                # per le dinamiche l'italiano e' gia' un'espressione HSP completa
                nuovo = degrada(voce["it"])
            else:
                nuovo = '"' + degrada(voce["it"]) + '"'

            pezzi.append(riga[cursore:inizio_en])
            pezzi.append(nuovo)
            cursore = fine_en
            sostituzioni += 1
        pezzi.append(riga[cursore:])
        righe_uscita.append("".join(pezzi))

    risultato = fine_riga.join(righe_uscita)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, sostituzioni


def prepara_albero() -> None:
    """Copia SORGENTE in BUILD da zero. BUILD e' usa e getta."""
    if percorsi.BUILD.exists():
        shutil.rmtree(percorsi.BUILD)
    shutil.copytree(percorsi.SORGENTE, percorsi.BUILD, ignore=shutil.ignore_patterns(".git"))


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Costruisce l'albero di build col dizionario applicato.")
    analizzatore.add_argument("--salta-copia", action="store_true", help="riusa l'albero di build esistente")
    argomenti = analizzatore.parse_args()

    if not argomenti.salta_copia:
        prepara_albero()

    totale = 0
    for percorso_dizionario in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        nome_file = percorso_dizionario.stem
        voci = [json.loads(r) for r in percorso_dizionario.read_text(encoding="utf-8").splitlines() if r.strip()]
        dizionario = {v["firma"]: v for v in voci}

        bersaglio = percorsi.BUILD_HSP / nome_file
        testo = bersaglio.read_bytes().decode("cp932")
        nuovo, sostituzioni = applica_a_testo(nome_file, testo, dizionario)
        bersaglio.write_bytes(nuovo.encode("cp932"))
        totale += sostituzioni
        print(f"{nome_file}: {sostituzioni} sostituzioni")

    print(f"totale: {totale} sostituzioni in {percorsi.BUILD_HSP}")


if __name__ == "__main__":
    main()
```

- [ ] **Passo 4: Eseguire i test e verificare che passino**

```
python -m pytest strumenti/tests/test_applica.py -v
```

Atteso: 6 passed. Il test `test_il_risultato_e_codificabile_in_cp932` è il più importante: se fallisce, la degradazione ha lasciato passare qualcosa e il compilatore produrrebbe testo mutilato senza dirlo.

- [ ] **Passo 5: Verificare che il sorgente sia rimasto intatto**

⚠️ **`git status` non serve a questo scopo.** Su un clone appena fatto e mai toccato segnala già 1198 file modificati, fra cui `ai.hsp`, `command.hsp` e `main.hsp`, per via dell'asimmetria di iconv sul byte `0x8160` (`～` U+FF5E scritto, `〜` U+301C riletto). Vedi `SPEC.md` §2.

Serve un manifesto di hash. Crearlo **una volta sola**, subito dopo il clone:

```powershell
$src = "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
Get-ChildItem $src -Filter *.hsp | ForEach-Object {
  "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash, $_.Name
} | Set-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt"
(Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt" | Measure-Object -Line).Lines
```

Atteso: **72 righe**.

Poi, dopo ogni build, confrontare:

```powershell
$src = "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
$atteso = Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt"
$attuale = Get-ChildItem $src -Filter *.hsp | ForEach-Object {
  "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash, $_.Name
}
$diff = Compare-Object $atteso $attuale
if ($diff) { $diff | Format-Table -AutoSize } else { "sorgente intatto" }
```

Atteso: `sorgente intatto`. Qualsiasi differenza significa che uno strumento ha scritto dove non doveva; fermarsi e correggere prima di proseguire.

- [ ] **Passo 6: Commit**

```bash
git add strumenti/applica.py strumenti/tests/test_applica.py
git commit -m "applica.py: albero di build con dizionario iniettato e accenti degradati"
```

---

## Task 8: `compila.py` e `installa.py`

**File:**
- Creare: `strumenti/compila.py`, `strumenti/installa.py`
- Test: `strumenti/tests/test_installa.py`

**Interfacce:**
- Consuma: `percorsi.BUILD_HSP`, `percorsi.HSP`, `percorsi.DIST`, `percorsi.GIOCO`
- Produce: `compila() -> Path` (percorso dell'exe prodotto), `installa(exe: Path) -> Path`

- [ ] **Passo 1: Automatizzare la compilazione a partire dalla ricetta del Task 1**

L'SDK non contiene un compilatore da riga di comando: `hspcmp.dll` va pilotata. La via certa, in ordine di preferenza:

1. **Driver HSP.** Scrivere `strumenti/build.hsp` sul modello di `$LAVORO\hsp34\sample\misc\hspcmp.hsp`, usando `hsc_ini` / `hsc_objname` / `hsc_comp` e poi `hsc3_make` più `pack_exe` per produrre l'eseguibile. Compilarlo **una volta** con `hsed3.exe` ottenendo `$LAVORO\hsp34\build.exe`; da lì in poi `compila.py` lo invoca e basta.
2. **Ripiego:** se il driver non produce un eseguibile funzionante, `compila.py` si ferma con un messaggio che istruisce a compilare a mano con `hsed3.exe` + `Ctrl+F9` sull'albero di build, e la Fase 0 prosegue lo stesso.

Il ripiego è accettabile: la Fase 0 deve dimostrare che il ciclo funziona, non che è comodo. L'automazione completa può slittare alla Fase 1.

- [ ] **Passo 2: Scrivere `compila.py`**

```python
# strumenti/compila.py
"""Invoca il compilatore HSP sull'albero di build e deposita l'eseguibile in DIST."""
import shutil
import subprocess
import sys
from pathlib import Path

from strumenti import percorsi

NOME_USCITA = "elonapluscgx-it.exe"


def compila() -> Path:
    driver = percorsi.HSP / "build.exe"
    principale = percorsi.BUILD_HSP / "main.hsp"

    if not principale.exists():
        raise SystemExit(f"albero di build assente: {principale} — eseguire prima applica.py")

    if not driver.exists():
        raise SystemExit(
            f"driver di compilazione assente: {driver}\n"
            f"Compilare strumenti/build.hsp una volta con {percorsi.HSP / 'hsed3.exe'} (Ctrl+F9),\n"
            f"oppure compilare a mano {principale} e copiare l'exe in {percorsi.DIST}."
        )

    esito = subprocess.run(
        [str(driver), str(principale)],
        cwd=str(percorsi.BUILD_HSP),
        capture_output=True,
        text=True,
    )
    if esito.returncode != 0:
        sys.stderr.write(esito.stdout + esito.stderr)
        raise SystemExit(f"compilazione fallita, codice {esito.returncode}")

    prodotto = percorsi.BUILD_HSP / "elonapluscgx.exe"
    if not prodotto.exists():
        raise SystemExit(f"la compilazione non ha prodotto {prodotto}")

    percorsi.DIST.mkdir(parents=True, exist_ok=True)
    destinazione = percorsi.DIST / NOME_USCITA
    shutil.copy2(prodotto, destinazione)
    print(f"{destinazione} ({destinazione.stat().st_size} byte)")
    return destinazione


if __name__ == "__main__":
    compila()
```

- [ ] **Passo 3: Scrivere il test di `installa.py`**

```python
# strumenti/tests/test_installa.py
import pytest
from strumenti.installa import installa


def test_installa_copia_l_exe_col_nome_italiano(tmp_path):
    exe = tmp_path / "elonapluscgx-it.exe"
    exe.write_bytes(b"finto eseguibile")
    gioco = tmp_path / "gioco"
    gioco.mkdir()
    (gioco / "elonapluscgx.exe").write_bytes(b"originale inglese")

    destinazione = installa(exe, gioco)

    assert destinazione == gioco / "elonapluscgx-it.exe"
    assert destinazione.read_bytes() == b"finto eseguibile"


def test_installa_non_tocca_l_eseguibile_inglese(tmp_path):
    exe = tmp_path / "elonapluscgx-it.exe"
    exe.write_bytes(b"finto eseguibile")
    gioco = tmp_path / "gioco"
    gioco.mkdir()
    inglese = gioco / "elonapluscgx.exe"
    inglese.write_bytes(b"originale inglese")

    installa(exe, gioco)

    assert inglese.read_bytes() == b"originale inglese"


def test_installa_non_tocca_i_salvataggi(tmp_path):
    exe = tmp_path / "elonapluscgx-it.exe"
    exe.write_bytes(b"finto eseguibile")
    gioco = tmp_path / "gioco"
    (gioco / "save").mkdir(parents=True)
    salvataggio = gioco / "save" / "sav_pippo"
    salvataggio.write_bytes(b"partita")

    installa(exe, gioco)

    assert salvataggio.read_bytes() == b"partita"


def test_installa_rifiuta_una_destinazione_che_non_e_il_gioco(tmp_path):
    exe = tmp_path / "elonapluscgx-it.exe"
    exe.write_bytes(b"finto eseguibile")
    with pytest.raises(SystemExit, match="non sembra"):
        installa(exe, tmp_path / "cartella_a_caso")
```

- [ ] **Passo 4: Eseguire il test e verificare che fallisca**

```
python -m pytest strumenti/tests/test_installa.py -v
```

Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.installa'`.

- [ ] **Passo 5: Scrivere `installa.py`**

```python
# strumenti/installa.py
"""Copia l'eseguibile italiano nel gioco, senza toccare inglese ne' salvataggi."""
import argparse
import shutil
from pathlib import Path

from strumenti import percorsi
from strumenti.compila import NOME_USCITA


def installa(exe: Path, gioco: Path | None = None) -> Path:
    gioco = Path(gioco) if gioco is not None else percorsi.GIOCO

    # una destinazione plausibile contiene l'eseguibile originale o la cartella dei salvataggi
    if not (gioco / "elonapluscgx.exe").exists() and not (gioco / "save").exists():
        raise SystemExit(f"{gioco} non sembra una installazione di Elona+ Custom-GX")

    destinazione = gioco / NOME_USCITA
    shutil.copy2(exe, destinazione)
    print(f"installato: {destinazione}")
    return destinazione


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Installa la build italiana nel gioco.")
    analizzatore.add_argument("--exe", default=None, help="percorso dell'eseguibile da installare")
    argomenti = analizzatore.parse_args()
    exe = Path(argomenti.exe) if argomenti.exe else percorsi.DIST / NOME_USCITA
    installa(exe)


if __name__ == "__main__":
    main()
```

- [ ] **Passo 6: Eseguire il test e verificare che passi**

```
python -m pytest strumenti/tests/test_installa.py -v
```

Atteso: 4 passed.

- [ ] **Passo 7: Commit**

```bash
git add strumenti/compila.py strumenti/installa.py strumenti/tests/test_installa.py strumenti/build.hsp
git commit -m "compila.py e installa.py: dalla build all'eseguibile italiano installato"
```

---

## Task 9: Il ciclo completo su 50 stringhe

La prova che tutta la catena regge. Le 50 stringhe si scelgono apposta: non le prime 50, ma un campione che stressa i casi difficili.

**File:**
- Creare: `lavoro/f0-campione.jsonl`, `dizionario/text.hsp.jsonl`
- Creare: `glossario.md`, `guida-stile.md`, `invariati.md`, `avanzamento.md`, `RIPRESA-sessione.md`

- [ ] **Passo 1: Portare glossario e guida di stile dal progetto gemello**

```powershell
$GEMELLO = "C:\Users\old_p\Documents\progetto second brain\Elin - Traduzione Italiana"
$PROGETTO = "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
Copy-Item "$GEMELLO\glossario.md" "$PROGETTO\glossario.md"
Copy-Item "$GEMELLO\guida-stile.md" "$PROGETTO\guida-stile.md"
```

Poi adattarli: in testa a `glossario.md` annotare che deriva dal glossario Elin e che i termini specifici di Elona lo estendono. In `guida-stile.md` aggiungere la sezione sulle **dinamiche** (SPEC §5): costruzioni impersonali, niente articolo determinativo davanti a nome interpolato, riordino della frase per evitare l'accordo. E la regola sugli accenti: **nel dizionario si scrive `perché`, mai `perche'`**.

- [ ] **Passo 2: Estrarre il campione**

```powershell
python -m strumenti.estrai text.hsp --uscita lavoro\f0-tutto-text.jsonl
```

Poi selezionare 50 voci a mano in `lavoro\f0-campione.jsonl`, con questa composizione:

- 25 statiche brevi e ad alta visibilità (`"Your inventory is full."`, `"It's impossible."`, `"You can't see the location."`, `"Nothing happens..."`) — si vedono subito in gioco;
- 20 dinamiche con interpolazione (quelle con `name(...)`, `itemname(...)`) — mettono alla prova sia `verifica.py` sia le regole di accordo;
- 5 che in italiano **richiedono un accento** (`"You have completed the quest!"` → `"Hai completato la missione!"` non basta: sceglierne che producano `perché`, `già`, `più`, `così`, `è`) — mettono alla prova la degradazione.

- [ ] **Passo 3: Tradurre le 50 voci**

Compilare il campo `it` di ogni riga di `lavoro\f0-campione.jsonl`, rispettando `glossario.md` e `guida-stile.md`. Accenti veri, mai apostrofi scritti a mano.

- [ ] **Passo 4: Verificare il lotto**

```powershell
python -m strumenti.verifica lavoro\f0-campione.jsonl
```

Atteso: `50 voci, nessun problema`. Se segnala problemi, correggere le traduzioni — **non** allentare le regole.

- [ ] **Passo 5: Reimportare nel dizionario**

```powershell
python -m strumenti.reimporta lavoro\f0-campione.jsonl
Get-Content dizionario\text.hsp.jsonl | Measure-Object -Line
```

Atteso: 50 righe.

- [ ] **Passo 6: Costruire e compilare**

```powershell
python -m strumenti.applica
python -m strumenti.compila
```

Atteso: `applica` riporta `text.hsp: 50 sostituzioni`; `compila` produce `C:\Games\Elona\_traduzione\dist\elonapluscgx-it.exe`.

- [ ] **Passo 7: Verificare che il sorgente sia ancora intatto**

Con il manifesto di hash creato al Task 7, passo 5 — **non** con `git status`, che nel clone del sorgente è permanentemente sporco:

```powershell
$src = "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
$atteso = Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt"
$attuale = Get-ChildItem $src -Filter *.hsp | ForEach-Object {
  "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash, $_.Name
}
$diff = Compare-Object $atteso $attuale
if ($diff) { $diff | Format-Table -AutoSize } else { "sorgente intatto" }
```

Atteso: `sorgente intatto`.

- [ ] **Passo 8: Installare e provare in gioco**

```powershell
python -m strumenti.installa
Start-Process "C:\Games\Elona\elonaplus2.31\elonapluscgx-it.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Controllare a schermo, con un personaggio di prova:

1. una statica appare in italiano — riempire lo zaino fino a `"Il tuo zaino è pieno."`;
2. una dinamica compone correttamente — creare un oggetto e leggere il messaggio con il nome interpolato;
3. **una stringa accentata appare come `perche'` e non come `perche`** — è la prova che la degradazione funziona e che CP932 non ha mangiato niente;
4. l'eseguibile inglese originale è ancora presente e funzionante.

- [ ] **Passo 9: Registrare lo stato**

Scrivere `avanzamento.md` (50 su 26.817, dettaglio per file), `RIPRESA-sessione.md` (punto di ripresa), `invariati.md` (vuoto, con la spiegazione del suo scopo), e aggiornare `decisioni.md` con quanto emerso.

- [ ] **Passo 10: Commit**

```bash
git add -A
git commit -m "Fase 0 completata: ciclo end-to-end verificato su 50 stringhe in gioco"
```

---

## Task 10: Dove stanno i nomi degli oggetti

Domanda aperta di `SPEC.md` §2: `db_item.hsp` pesa 4,6 MB e contiene **zero** `lang()`. Senza questa risposta la Fase 2 non è dimensionabile.

**File:**
- Modificare: `SPEC.md` §2 e §6, `decisioni.md`

- [ ] **Passo 1: Seguire `ioriginalnameref`**

```powershell
$src = "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
$enc = [Text.Encoding]::GetEncoding(932)
foreach ($f in Get-ChildItem $src -Filter *.hsp) {
  $s = $enc.GetString([IO.File]::ReadAllBytes($f.FullName))
  $n = ([regex]::Matches($s, 'ioriginalnameref')).Count
  if ($n -gt 0) { "{0,-28} {1}" -f $f.Name, $n }
}
```

Cercare il file che **assegna** i valori, non quelli che li leggono.

- [ ] **Passo 2: Trovare la tabella dei nomi**

Nel file individuato, cercare dove l'indice diventa testo: array di stringhe, `sdim` seguito da assegnazioni, oppure lettura da un file esterno in `data/`.

```powershell
$src = "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
$enc = [Text.Encoding]::GetEncoding(932)
$s = $enc.GetString([IO.File]::ReadAllBytes("$src\item.hsp"))
($s -split "`r?`n") | Select-String -Pattern 'ioriginalnameref|refitemname|itemname' | Select-Object -First 30
```

- [ ] **Passo 3: Contare quanti sono**

Una volta trovata la struttura, contare le voci traducibili. È il numero che manca alla Fase 2.

- [ ] **Passo 4: Aggiornare lo spec**

In `SPEC.md` §2 sostituire il "punto aperto" con la risposta. In §6 completare il volume della Fase 2. Annotare in `decisioni.md` come è stata trovata, così la prossima persona non rifà la ricerca.

- [ ] **Passo 5: Commit**

```bash
git add SPEC.md decisioni.md
git commit -m "Individuata la collocazione dei nomi degli oggetti, Fase 2 dimensionata"
```

---

## Criteri di uscita della Fase 0

La fase è conclusa quando tutte queste affermazioni sono vere:

- [ ] L'eseguibile si ricompila da sorgente **non modificato** e si avvia (Task 1)
- [ ] `python -m pytest strumenti/tests -v` passa interamente
- [ ] `strumenti.estrai text.hsp` conta esattamente **2146** voci (**1915** statiche, **231** dinamiche)
- [ ] 50 stringhe sono nel dizionario e `verifica.py` non segnala nulla
- [ ] Il manifesto di hash di `sorgente/` combacia dopo una build completa (**non** `git status`: nel clone del sorgente è permanentemente sporco, vedi `SPEC.md` §2)
- [ ] Le 50 stringhe si vedono in italiano in gioco, e una accentata appare come `perche'`
- [ ] L'eseguibile inglese e i salvataggi sono intatti
- [ ] La collocazione dei nomi degli oggetti è documentata in `SPEC.md`
