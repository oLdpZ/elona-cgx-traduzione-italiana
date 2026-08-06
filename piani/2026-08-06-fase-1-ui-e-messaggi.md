# Piano Fase 1 — UI e messaggi

> **Per chi esegue:** i passi hanno la casella `- [ ]` per essere spuntati.
> Ogni task finisce con un commit e lascia la suite verde. Non si passa al task
> successivo con la suite rossa.

**Obiettivo:** portare in italiano interfaccia e messaggistica di Elona+ Custom-GX
— i sei file `text` `command` `action` `proc` `skill` `trait`, **6.688 stringhe
uniche su 7.737 occorrenze** — e chiudere i cinque buchi della catena che oggi
renderebbero quel lavoro impossibile o insicuro.

**Architettura:** invariata rispetto alla Fase 0. Dizionario esterno per file,
applicato a una copia del sorgente al momento della build. Questa fase non cambia
l'architettura: ne completa i pezzi che lo SPEC promette e che non esistono.

**Stack:** Python 3.14 (nessuna dipendenza esterna), pytest, HSP 3.4 via
`strumenti/compila.py`.

---

## Vincoli globali

Valgono per ogni task, senza ripeterli ogni volta.

- **Il sorgente upstream non si scrive mai.** Verifica con il manifesto, mai con
  `git status` (SPEC §2). Gli strumenti hanno già la guardia: non aggirarla.
- **La prova d'identità deve restare a 72/72** dopo ogni task che tocchi
  `estrai.py` o `applica.py`: `python -m strumenti.prova_identita`.
- **Il cancello deve restare verde:** `python -m strumenti.compila --cancello`.
- **Nel dizionario si scrivono gli accenti veri** (`perché`). La degradazione ad
  apostrofo la fa `applica.py` in build. `verifica.py` segnala l'apostrofo scritto
  a mano.
- **Mai `"` in una traduzione statica:** romperebbe il letterale HSP. Si usano le
  virgolette tipografiche `“ ”`. Mai `«»`: CP932 non le codifica.
- **Sorgente pinnato al tag `2.31.2.0`.** Nessun task fa `git pull` nel clone.
- Nomi in italiano per funzioni, variabili e test, come nel resto del progetto.

---

## Perché questi task, e in quest'ordine

Cinque cose sbarrano la strada alla traduzione. Le prime due sono state misurate
scrivendo questo piano, non stimate:

1. **Il 33% delle dinamiche di Fase 1 verrebbe rifiutato da `verifica.py`.** Sono
   510 stringhe su 1.522 che contengono funzioni di grammatica inglese. La regola
   sulle interpolazioni pretende che l'insieme delle chiamate sia identico fra
   inglese e italiano, ma `_s(tc)` — che restituisce la `s` della terza persona
   inglese — **in italiano va tolta**. Senza Task 1 un traduttore onesto viene
   respinto e uno frettoloso lascia `s` nel testo.
2. **425 statiche di Fase 1 non sono traducibili affatto.** Sono avvolte in
   `cnvtalk(`, e `applica.py` le rifiuta per non far sparire la chiamata. Sul
   corpus intero sono 3.466, in due sole forme: `cnvtalk` (3.390) e `cnven` (76).
3. **La regola «traduzione identica all'inglese» non ha via d'uscita.** `Vernis`
   in italiano è `Vernis`. `invariati.md` è promesso dallo SPEC §7 e non esiste,
   quindi oggi l'unico modo di far passare un nome proprio è falsificarlo.
4. **La coda di ritraduzione non esiste.** Lo SPEC §3.1 ci fonda l'intera
   architettura — «al riallineamento si riapplica il dizionario e le firme
   sparite diventano la coda» — ma `verifica --dizionario` non è implementato.
   Finché il dizionario è vuoto non si vede; con 6.688 voci è troppo tardi.
5. **Glossario e guida di stile non esistono.** Tradurre 6.688 stringhe senza
   glossario significa tradurre `Blessed` in quattro modi diversi.

I task 1-5 chiudono questi buchi. I task 6-7 traducono.

**Un punto dell'elenco in `decisioni.md` sparisce invece di essere fatto.** Era
«spostare a monte il rilevamento delle statiche avvolte, perché oggi il
traduttore lo scopre solo a build abortito». Il Task 2 le rende traducibili,
quindi non c'è più niente da segnalare a monte: il caso non esiste. Va tolto da
`decisioni.md` alla chiusura della fase, non lasciato lì a sembrare arretrato.

---

## Mappa dei file

| file | responsabilità | task |
|---|---|---|
| `strumenti/funzioni.py` | **nuovo** — classifica le funzioni HSP che compaiono nelle dinamiche: contenuto, morfologia inglese, pronome | 1 |
| `strumenti/verifica.py` | usa la classificazione invece del confronto secco; legge `invariati.md`; nuovo modo `--dizionario` | 1, 3, 4 |
| `strumenti/applica.py` | sostituisce dentro `cnvtalk(`/`cnven(` invece di rifiutare | 2 |
| `strumenti/prova_identita.py` | l'esclusione delle statiche avvolte sparisce | 2 |
| `invariati.md` | **nuovo** — stringhe che restano in inglese per scelta | 3 |
| `glossario.md` | **nuovo** — termine EN → IT, vincolante | 5 |
| `guida-stile.md` | **nuovo** — registro, segnaposto, accordo di genere | 5 |
| `avanzamento.md` | **nuovo** — tradotte/totali per file | 7 |

---

## Task 1 — Le funzioni grammaticali inglesi

Oggi `verifica.py` confronta l'insieme delle chiamate fra inglese e italiano e
pretende che coincida. Per il contenuto è giusto: perdere `name(tc)` significa
perdere il nome del personaggio. Per la grammatica inglese è sbagliato.

Le tre classi, **verificate leggendo `init.hsp`**, non dedotte dal nome:

| classe | funzioni | cosa restituiscono | in italiano |
|---|---|---|---|
| morfologia inglese | `_s`, `is`, `was`, `your` | `"s"`, `"es"`, `"is"`, `"are"`, `"was"`, `"were"`, `"'s"` — stringhe inglesi nude, mai passate da `lang()` | **vanno tolte** |
| pronome | `he`, `his`, `him` | `lang("彼", "he")`, `lang("彼の", "his")` — passano da `lang()`, quindi si localizzeranno con `init.hsp` | **facoltative** |
| contenuto | tutto il resto: `name`, `itemname`, `cdatan`, `skillname`, `gdata`… | il testo vero | **vanno conservate** |

La distinzione fra le prime due è la ragione per cui questo task esiste e non è
una riga di codice: `is(tc)` produce inglese per sempre, `he(tc, 1)` produrrà
italiano appena si traduce `init.hsp` in Fase 4. Trattarle uguali sarebbe
sbagliato in un verso o nell'altro.

**File:**
- Crea: `strumenti/funzioni.py`
- Crea: `strumenti/tests/test_funzioni.py`
- Modifica: `strumenti/verifica.py` (la sezione `if tipo == "dinamica"`)
- Modifica: `strumenti/tests/test_verifica.py`

**Interfacce prodotte:**
- `MORFOLOGIA_INGLESE: frozenset[str]`
- `PRONOMI: frozenset[str]`
- `funzioni_di_contenuto(espressione: str) -> list[str]` — le chiamate che
  contano, ordinate, con morfologia e pronomi tolti

- [ ] **Passo 1: verificare l'elenco sul sorgente, non fidarsi di questo piano**

La funzione `s` compare 28 volte e non è stata verificata. Prima di scrivere
codice, guarda cosa restituiscono davvero:

```powershell
cd "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
python -c "
import re
t=open('init.hsp','rb').read().decode('cp932')
righe=re.split(r'\r\n|\n', t)
for i,r in enumerate(righe):
    m=re.match(r'#defcfunc\s+([A-Za-z_][A-Za-z0-9_]*)', r)
    if m and m.group(1) in ['s','are','have','does','name_s']:
        print(m.group(1), [x.strip() for x in righe[i:i+14] if 'return' in x][:4])
"
```

Regola per classificare: **se il valore restituito passa da `lang()` è un
pronome (facoltativo), se è una stringa inglese nuda è morfologia (da togliere).**
Aggiungi al set giusto quello che trovi. Se una funzione non è definita in
`init.hsp`, cercala con `grep -rn "#defcfunc\s\+nome" *.hsp`.

- [ ] **Passo 2: scrivere il test che fallisce**

```python
# strumenti/tests/test_funzioni.py
from strumenti.funzioni import MORFOLOGIA_INGLESE, PRONOMI, funzioni_di_contenuto


def test_la_morfologia_inglese_non_e_contenuto():
    espressione = 'name(tc) + " attack" + _s(tc) + " " + itemname(ci)'
    assert funzioni_di_contenuto(espressione) == ["itemname", "name"]


def test_i_pronomi_non_sono_contenuto():
    # he() passa da lang(), quindi si localizzera' con init.hsp: che l'italiano
    # lo tenga o lo tolga sono due scelte entrambe valide, e la verifica non
    # deve imporne nessuna
    assert funzioni_di_contenuto('cnven(he(tc, 1)) + " is here."') == ["cnven"]


def test_le_due_classi_non_si_sovrappongono():
    assert not (MORFOLOGIA_INGLESE & PRONOMI)


def test_una_espressione_senza_chiamate_non_ha_contenuto():
    assert funzioni_di_contenuto('" and "') == []
```

- [ ] **Passo 3: verificare che fallisca**

Esegui: `python -m pytest strumenti/tests/test_funzioni.py -v`
Atteso: FAIL con `ModuleNotFoundError: No module named 'strumenti.funzioni'`

- [ ] **Passo 4: scrivere `strumenti/funzioni.py`**

```python
# strumenti/funzioni.py
"""Classificazione delle funzioni HSP che compaiono nelle espressioni dinamiche.

Non tutte le chiamate dentro un `lang()` dinamico sono contenuto. Alcune sono
grammatica **inglese**, e in italiano vanno tolte: `_s(tc)` restituisce la `s`
della terza persona, `your(tc)` il suffisso possessivo `'s`. Conservarle
significherebbe scrivere inglese dentro una frase italiana.

La distinzione fra le due classi non ovvie sta nel valore restituito, verificato
leggendo `init.hsp`:

- **morfologia**: restituisce una stringa inglese nuda, mai passata da `lang()`.
  Non si localizzera' mai. In italiano va tolta.
- **pronome**: restituisce `lang("彼", "he")`, quindi si localizzera' insieme a
  `init.hsp` in Fase 4. Tenerla o toglierla sono due scelte entrambe legittime,
  e la verifica non deve imporne nessuna.

Tutto il resto e' contenuto e va conservato: perdere `name(tc)` significa perdere
il nome del personaggio dalla frase.
"""
import re

# restituiscono stringhe inglesi nude: "s", "es", "is", "are", "was", "were", "'s"
MORFOLOGIA_INGLESE = frozenset({"_s", "is", "was", "your"})

# restituiscono lang("彼", "he") e simili: si localizzeranno con init.hsp
PRONOMI = frozenset({"he", "his", "him"})

_CHIAMATA = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def funzioni_di_contenuto(espressione: str) -> list[str]:
    """Le chiamate che devono sopravvivere alla traduzione, ordinate."""
    return sorted(
        nome for nome in _CHIAMATA.findall(espressione)
        if nome not in MORFOLOGIA_INGLESE and nome not in PRONOMI
    )
```

- [ ] **Passo 5: verificare che passi**

Esegui: `python -m pytest strumenti/tests/test_funzioni.py -v`
Atteso: PASS, 4 test

- [ ] **Passo 6: il test che fallisce su `verifica.py`**

Aggiungi in `strumenti/tests/test_verifica.py`:

```python
def test_togliere_la_morfologia_inglese_non_e_un_problema():
    # _s(tc) e' la desinenza della terza persona inglese: in italiano non
    # esiste. Sono 510 dinamiche su 1.522 in Fase 1.
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


def test_un_pronome_puo_restare_o_sparire():
    grezzo = 'cnven(he(tc, 1)) + " is a citizen."'
    con = {"tipo": "dinamica", "en": " is a citizen.",
           "it": 'cnven(he(tc, 1)) + " e\' un cittadino."', "en_grezzo": grezzo}
    senza = {"tipo": "dinamica", "en": " is a citizen.",
             "it": 'cnven("E\'") + " un cittadino."', "en_grezzo": grezzo}
    assert controlla_voce(con) == []
    assert controlla_voce(senza) == []
```

- [ ] **Passo 7: verificare che falliscano**

Esegui: `python -m pytest strumenti/tests/test_verifica.py -v -k "morfologia or contenuto or pronome"`
Atteso: FAIL — la regola attuale confronta gli insiemi interi

- [ ] **Passo 8: cambiare la regola in `verifica.py`**

Sostituisci il blocco `if tipo == "dinamica":` in `controlla_voce` con:

```python
    if tipo == "dinamica":
        attese = funzioni_di_contenuto(voce["en_grezzo"])
        trovate = funzioni_di_contenuto(italiano)
        if attese != trovate:
            problemi.append(f"interpolazioni non conservate: attese {attese}, trovate {trovate}")

        # la morfologia inglese non si localizza mai: _s(tc) scrive "s" a
        # schermo anche dentro una frase italiana
        residue = sorted(set(_CHIAMATE.findall(italiano)) & MORFOLOGIA_INGLESE)
        if residue:
            problemi.append(
                f"morfologia inglese rimasta nella traduzione: {residue}. "
                "Sono desinenze e possessivi inglesi (\"s\", \"is\", \"'s\"): "
                "in italiano vanno tolti e la frase va riscritta."
            )
```

e in cima al file:

```python
from strumenti.funzioni import MORFOLOGIA_INGLESE, funzioni_di_contenuto
```

- [ ] **Passo 9: suite intera**

Esegui: `python -m pytest strumenti/tests -q`
Atteso: tutti verdi. Se qualche test preesistente sulle interpolazioni si rompe,
**leggilo prima di cambiarlo**: se pretendeva la conservazione di `_s` era il
test a codificare il difetto.

- [ ] **Passo 10: commit**

```bash
git add strumenti/funzioni.py strumenti/verifica.py strumenti/tests/test_funzioni.py strumenti/tests/test_verifica.py
git commit -m "verifica: la morfologia inglese non e' contenuto da conservare"
```

---

## Task 2 — Sostituzione dentro `cnvtalk(` e `cnven(`

3.466 statiche del corpus, **425 in Fase 1**, hanno l'argomento inglese avvolto in
una chiamata: `lang("「うにーっ！」", cnvtalk("Urchinn!"))`. Sostituire l'intero
span farebbe sparire `cnvtalk` dal sorgente, quindi `applica.py` rifiuta. Il
risultato è che quelle stringhe **non sono traducibili**.

Gli involucri sono due soli, misurati sul sorgente pinnato: `cnvtalk` 3.390,
`cnven` 76. Non è una famiglia aperta.

**La soluzione sta nel prendere l'involucro dal sito, non dal dizionario.** La
voce di dizionario contiene solo il testo italiano; `applica.py` ricostruisce
l'involucro leggendolo dall'espressione che ha davanti. Così la stessa voce serve
sia il sito nudo sia quello avvolto — che è esattamente il caso delle 3 firme
ambigue residue in `db_creature.hsp`, che spariscono da sole.

**File:**
- Modifica: `strumenti/applica.py:150-161` (il blocco che solleva `SorgenteCorrotto`)
- Modifica: `strumenti/prova_identita.py` (l'esclusione delle avvolte)
- Modifica: `strumenti/tests/test_applica.py`
- Modifica: `strumenti/tests/test_prova_identita.py`

**Interfacce prodotte:**
- `applica.INVOLUCRI: frozenset[str]` — `{"cnvtalk", "cnven"}`
- `applica.riscrivi_statica(grezzo_en: str, italiano: str) -> str | None` — l'HSP
  da mettere al posto di `grezzo_en`; `None` se la forma non è riconosciuta

- [ ] **Passo 1: il test che fallisce**

```python
def test_sostituisce_dentro_cnvtalk_conservando_l_involucro():
    sorgente = '\ttxt lang("「うにーっ！」", cnvtalk("Urchinn!"))'
    diz = dizionario_con("「うにーっ！」", "Urchinn!", "Ricciooo!",
                         en_grezzo='cnvtalk("Urchinn!")')
    testo, sostituzioni = applica_a_testo("action.hsp", sorgente, diz)
    assert sostituzioni == 1
    assert 'cnvtalk("Ricciooo!")' in testo
    assert "Urchinn!" not in testo


def test_sostituisce_dentro_cnven():
    sorgente = '\ttxt lang("jp", cnven("Hello."))'
    diz = dizionario_con("jp", "Hello.", "Ciao.", en_grezzo='cnven("Hello.")')
    testo, _ = applica_a_testo("chat.hsp", sorgente, diz)
    assert 'cnven("Ciao.")' in testo


def test_la_stessa_voce_serve_il_sito_nudo_e_quello_avvolto():
    # l'involucro si prende dal sito, non dal dizionario: e' il caso delle 3
    # firme ambigue di db_creature.hsp
    sorgente = '\ttxt lang("jp", "Ciao.")\r\n\ttxt lang("jp", cnvtalk("Ciao."))'
    diz = dizionario_con("jp", "Ciao.", "Salve.")
    testo, sostituzioni = applica_a_testo("db_creature.hsp", sorgente, diz)
    assert sostituzioni == 2
    assert '"Salve."' in testo
    assert 'cnvtalk("Salve.")' in testo


def test_un_involucro_sconosciuto_viene_ancora_rifiutato():
    # la famiglia e' chiusa: due forme. Una terza va vista, non indovinata
    sorgente = '\ttxt lang("jp", qualcosaDiNuovo("Hello."))'
    diz = dizionario_con("jp", "Hello.", "Ciao.", en_grezzo='qualcosaDiNuovo("Hello.")')
    with pytest.raises(SorgenteCorrotto, match="involucro non riconosciuto"):
        applica_a_testo("chat.hsp", sorgente, diz)
```

- [ ] **Passo 2: verificare che falliscano**

Esegui: `python -m pytest strumenti/tests/test_applica.py -v -k "cnvtalk or cnven or involucro or avvolto"`
Atteso: FAIL con `SorgenteCorrotto: ... non e' un letterale nudo`

- [ ] **Passo 3: implementare**

In `strumenti/applica.py`, prima di `applica_a_testo`:

```python
# Gli involucri sono due, misurati sul sorgente pinnato: cnvtalk 3.390,
# cnven 76. Non e' una famiglia aperta, ed e' giusto che un terzo involucro
# faccia fermare la catena invece di essere gestito per analogia.
INVOLUCRI = frozenset({"cnvtalk", "cnven"})

_AVVOLTA = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(\s*(".*")\s*\)\s*$', re.DOTALL)


def riscrivi_statica(grezzo_en: str, italiano: str) -> str | None:
    """L'HSP da mettere al posto di `grezzo_en`, con l'italiano al posto dell'inglese.

    L'involucro si prende **dal sito**, non dalla voce di dizionario: cosi' la
    stessa traduzione serve sia `"Ciao."` sia `cnvtalk("Ciao.")`, che nel
    sorgente convivono e condividono la firma.

    `None` se la forma non e' riconosciuta: il chiamante rifiuta.
    """
    letterale = '"' + italiano + '"'
    trovato = _AVVOLTA.match(grezzo_en)
    if trovato:
        return f"{trovato.group(1)}({letterale})" if trovato.group(1) in INVOLUCRI else None
    # una statica senza involucro e' per definizione un letterale nudo: non ha
    # un `+` di primo livello, altrimenti sarebbe classificata dinamica
    nudo = grezzo_en.strip()
    if nudo.startswith('"') and nudo.endswith('"') and len(nudo) >= 2:
        return letterale
    return None
```

e sostituisci il blocco che rifiutava (oggi `if tipo == "statica" and grezzo_en != '"' + inglese + '"'`) con:

```python
            if tipo == "statica":
                nuovo = riscrivi_statica(grezzo_en, degrada(voce["it"]))
                if nuovo is None:
                    raise SorgenteCorrotto(
                        f"{nome_file}:{numero_riga} firma {chiave}: involucro non "
                        f"riconosciuto in {grezzo_en!r}. Gli involucri gestiti sono "
                        f"{sorted(INVOLUCRI)}: se il sorgente ne ha introdotto un "
                        "altro va guardato, non gestito per analogia."
                    )
```

e più sotto, dove oggi si costruisce `nuovo`, lascia solo il ramo dinamico:

```python
            if tipo == "dinamica":
                # per le dinamiche l'italiano e' gia' un'espressione HSP completa
                nuovo = degrada(voce["it"])
```

- [ ] **Passo 4: verificare che passino**

Esegui: `python -m pytest strumenti/tests/test_applica.py -v`
Atteso: PASS

- [ ] **Passo 5: togliere l'esclusione dalla prova d'identità**

In `strumenti/prova_identita.py`, il ramo `if voce["en_grezzo"] != '"' + voce["en"] + '"'`
non deve più escludere: le avvolte ora si sostituiscono. Il contatore
`esclusi_avvolti` va tolto dalla dataclass, dalla stampa e dai test che lo
leggono. Aggiorna `test_una_statica_avvolta_e_esclusa_e_contata` a pretendere
l'opposto e rinominalo `test_una_statica_avvolta_ora_entra_nel_dizionario`.

- [ ] **Passo 6: la prova d'identità sul corpus vero**

Esegui: `python -m strumenti.prova_identita`
Atteso: **72/72**, sostituzioni salite da 22.738 a circa **26.200**, `escluse,
firme ambigue: 0`, `escluse, statiche avvolte` sparito.

Se un file non torna byte per byte, **fermati**: la ricostruzione dell'involucro
non è fedele. L'indiziato più probabile è uno spazio dentro `cnvtalk( "…" )`,
che il round-trip non riproduce.

- [ ] **Passo 7: il cancello**

Esegui: `python -m strumenti.compila --cancello`
Atteso: `#No error detected.`

- [ ] **Passo 8: commit**

```bash
git add strumenti/applica.py strumenti/prova_identita.py strumenti/tests/
git commit -m "applica: sostituisce dentro cnvtalk( e cnven( invece di rifiutare"
```

---

## Task 3 — `invariati.md` e la regola «identica all'inglese»

`verifica.py` segnala come problema una traduzione identica all'inglese. È una
regola giusta — quasi sempre indica una riga dimenticata — ma senza eccezioni
`Vernis` non ha via d'uscita, e il rischio concreto è che si aggiri la regola
scrivendo traduzioni finte.

Il progetto gemello Elin ha già questo file e questa soluzione: si eredita la
forma, non il contenuto (i luoghi Elona valgono per entrambi, i termini d'interfaccia no).

**File:**
- Crea: `invariati.md`
- Modifica: `strumenti/verifica.py`
- Modifica: `strumenti/tests/test_verifica.py`

**Interfacce prodotte:**
- `verifica.carica_invariati(percorso: Path | None = None) -> set[str]`
- `controlla_voce(voce, invariati: set[str] | None = None)` — parametro nuovo,
  con default che non cambia il comportamento dei chiamanti esistenti

- [ ] **Passo 1: scrivere `invariati.md`**

```markdown
# Invariati

Stringhe che restano identiche all'inglese **per scelta esplicita**, non perche'
la traduzione e' stata dimenticata. `verifica.py` legge questo file e non le
segnala.

Una riga qui e' una decisione: va motivata. Se il motivo non si riesce a
scrivere, probabilmente la stringa va tradotta.

| valore | motivo |
|---|---|
| Vernis | nome proprio di citta', canone Elona |
| Palmia | nome proprio di citta', canone Elona |
| Derphy | nome proprio di citta', canone Elona |
| Noyel | nome proprio di citta', canone Elona |
| Yowyn | nome proprio di citta', canone Elona |
| Lumiest | nome proprio di citta', canone Elona |
| Melugas | nome proprio di luogo, canone Elona |
| Karma | termine acquisito in italiano |
| Mana | termine acquisito nei giochi di ruolo |
```

- [ ] **Passo 2: il test che fallisce**

```python
def test_una_stringa_negli_invariati_non_e_segnalata():
    voce = {"tipo": "statica", "en": "Vernis", "en_grezzo": '"Vernis"', "it": "Vernis"}
    assert controlla_voce(voce, invariati={"Vernis"}) == []


def test_senza_gli_invariati_resta_segnalata():
    voce = {"tipo": "statica", "en": "Vernis", "en_grezzo": '"Vernis"', "it": "Vernis"}
    assert any("identica all'inglese" in p for p in controlla_voce(voce))


def test_carica_invariati_legge_la_tabella(tmp_path):
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "# Invariati\n\n| valore | motivo |\n|---|---|\n"
        "| Vernis | nome proprio |\n| Karma | termine acquisito |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"Vernis", "Karma"}


def test_carica_invariati_ignora_l_intestazione_e_i_separatori(tmp_path):
    percorso = tmp_path / "invariati.md"
    percorso.write_text("| valore | motivo |\n|---|---|\n| Vernis | x |\n", encoding="utf-8")
    assert carica_invariati(percorso) == {"Vernis"}


def test_senza_il_file_non_si_rompe_niente(tmp_path):
    assert carica_invariati(tmp_path / "assente.md") == set()
```

- [ ] **Passo 3: verificare che falliscano**

Esegui: `python -m pytest strumenti/tests/test_verifica.py -v -k invariat`
Atteso: FAIL con `TypeError: controlla_voce() got an unexpected keyword argument`

- [ ] **Passo 4: implementare**

In `strumenti/verifica.py`:

```python
def carica_invariati(percorso: Path | None = None) -> set[str]:
    """I valori della tabella di `invariati.md`, prima colonna.

    Il file e' un'aggiunta, non un requisito: se manca, la regola si comporta
    come prima. Un progetto senza eccezioni e' un progetto senza il file.
    """
    percorso = percorso or (percorsi.PROGETTO / "invariati.md")
    if not percorso.exists():
        return set()
    valori = set()
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip().startswith("|"):
            continue
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) < 2 or not celle[0] or celle[0] == "valore":
            continue
        if set(celle[0]) <= {"-", ":"}:  # riga separatrice
            continue
        valori.add(celle[0])
    return valori
```

e nella firma di `controlla_voce`:

```python
def controlla_voce(voce: dict, invariati: set[str] | None = None) -> list[str]:
```

e nella regola:

```python
    if italiano == originale and italiano not in (invariati or set()):
        problemi.append("traduzione identica all'inglese")
```

`controlla_lotto` carica il file una volta sola e lo passa:

```python
def controlla_lotto(voci: list[dict], invariati: set[str] | None = None) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema.

    Gli invariati si caricano una volta sola qui, non a ogni voce: leggere il
    file 6.688 volte per un lotto sarebbe assurdo, e i test lo passano gia'
    risolto per non toccare il disco.
    """
    invariati = carica_invariati() if invariati is None else invariati
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce, invariati)
        if problemi:
            esito[voce.get("firma", _dove(voce))] = problemi
    return esito
```

Aggiungi `from pathlib import Path` e `from strumenti import percorsi` se non ci sono.

- [ ] **Passo 5: verificare che passino, e la suite**

Esegui: `python -m pytest strumenti/tests -q`
Atteso: tutti verdi

- [ ] **Passo 6: commit**

```bash
git add invariati.md strumenti/verifica.py strumenti/tests/test_verifica.py
git commit -m "verifica: invariati.md come via d'uscita alla regola identica-all-inglese"
```

---

## Task 4 — `verifica --dizionario`: la coda di ritraduzione

Lo SPEC §3.1 fonda l'architettura su questa promessa: «a ogni nuova versione CGX
si fa `git pull` e si riapplica il dizionario; le firme sparite diventano la coda
di ritraduzione». Oggi la promessa non è implementata: `applica.py` conta le voci
orfane mentre costruisce l'albero, e basta.

Serve prima che il dizionario si riempia, non dopo: con 6.688 voci una coda
inesistente si traduce in stringhe che tornano inglesi a macchia di leopardo
senza che nessuno se ne accorga.

**File:**
- Modifica: `strumenti/verifica.py` (`main`)
- Modifica: `strumenti/tests/test_verifica.py`

**Interfacce prodotte:**
- `verifica.confronta_col_sorgente(nome_file: str) -> tuple[list[dict], int]` —
  le voci orfane e il numero di firme del sorgente non ancora tradotte

- [ ] **Passo 1: il test che fallisce**

```python
def test_una_firma_sparita_dal_sorgente_finisce_in_coda(tmp_path, monkeypatch):
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "text.hsp").write_bytes('\ttxt lang("jp", "Ciao.")\r\n'.encode("cp932"))
    diz = tmp_path / "diz"
    diz.mkdir()
    (diz / "text.hsp.jsonl").write_text(
        json.dumps({"firma": "sparita", "jp": "vecchio", "en": "Old.", "it": "Vecchio.",
                    "tipo": "statica", "en_grezzo": '"Old."', "riga": 1, "occorrenza": 0},
                   ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(percorsi, "SORGENTE_HSP", sorgente)
    monkeypatch.setattr(percorsi, "DIZIONARIO", diz)

    orfane, non_tradotte = confronta_col_sorgente("text.hsp")
    assert [v["firma"] for v in orfane] == ["sparita"]
    assert non_tradotte == 1


def test_un_dizionario_allineato_non_ha_coda(tmp_path, monkeypatch):
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "text.hsp").write_bytes('\ttxt lang("jp", "Ciao.")\r\n'.encode("cp932"))
    voci = estrai_da_testo("text.hsp", '\ttxt lang("jp", "Ciao.")\r\n')
    diz = tmp_path / "diz"
    diz.mkdir()
    (diz / "text.hsp.jsonl").write_text(
        json.dumps({**voci[0], "it": "Salve."}, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(percorsi, "SORGENTE_HSP", sorgente)
    monkeypatch.setattr(percorsi, "DIZIONARIO", diz)

    orfane, non_tradotte = confronta_col_sorgente("text.hsp")
    assert orfane == []
    assert non_tradotte == 0
```

- [ ] **Passo 2: verificare che falliscano**

Esegui: `python -m pytest strumenti/tests/test_verifica.py -v -k "coda or allineato"`
Atteso: FAIL con `ImportError: cannot import name 'confronta_col_sorgente'`

- [ ] **Passo 3: implementare**

```python
def confronta_col_sorgente(nome_file: str) -> tuple[list[dict], int]:
    """Coda di ritraduzione per un file: SPEC 3.1.

    Ritorna le voci tradotte la cui firma **non esiste piu'** nel sorgente — la
    stringa e' cambiata o sparita a monte, e la traduzione va rifatta — e quante
    firme del sorgente non hanno ancora una traduzione.

    Sono due domande diverse e vanno lette insieme: un dizionario puo' essere
    completo e tutto da ritradurre.
    """
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    voci = []
    if percorso.exists():
        voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    tradotte = {v["firma"]: v for v in voci if v.get("it")}

    testo = (percorsi.SORGENTE_HSP / nome_file).read_bytes().decode("cp932")
    nel_sorgente = {v["firma"] for v in estrai_da_testo(nome_file, testo)}

    orfane = [v for f, v in tradotte.items() if f not in nel_sorgente]
    non_tradotte = len(nel_sorgente - set(tradotte))
    return sorted(orfane, key=lambda v: v.get("riga", 0)), non_tradotte
```

Import necessari: `from strumenti.estrai import estrai_da_testo`.

Poi il modo da riga di comando, in `main()`:

```python
    analizzatore.add_argument("--dizionario", action="store_true",
                              help="confronta il dizionario col sorgente invece di validare un lotto")
    analizzatore.add_argument("lotto", nargs="?", help="percorso del lotto JSONL")
```

```python
    if argomenti.dizionario:
        totale_orfane = 0
        for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
            orfane, non_tradotte = confronta_col_sorgente(percorso.stem)
            totale_orfane += len(orfane)
            print(f"{percorso.stem}: {len(orfane)} da ritradurre, {non_tradotte} non ancora tradotte")
            for voce in orfane[:5]:
                print(f"    {voce['firma'][:10]} (riga {voce.get('riga', '?')}): {voce.get('en', '')[:60]!r}")
            if len(orfane) > 5:
                print(f"    ... e altre {len(orfane) - 5}")
        raise SystemExit(1 if totale_orfane else 0)
```

- [ ] **Passo 4: verificare, poi provare sul dizionario vero**

Esegui: `python -m pytest strumenti/tests -q` → verdi
Esegui: `python -m strumenti.verifica --dizionario`
Atteso: nessuna riga (il dizionario è vuoto), uscita 0

- [ ] **Passo 5: commit**

```bash
git add strumenti/verifica.py strumenti/tests/test_verifica.py
git commit -m "verifica --dizionario: la coda di ritraduzione promessa da SPEC 3.1"
```

---

## Task 5 — `glossario.md` e `guida-stile.md`

Senza glossario, `Blessed` diventa «benedetto», «consacrato» e «santo» nello
stesso file. Senza guida di stile, metà delle dinamiche useranno il «tu» e metà
la terza persona.

Il progetto gemello Elin ha entrambi
(`C:\Users\old_p\Documents\progetto second brain\Elin - Traduzione Italiana\`).
**Si eredita quello che è di universo, non quello che è di motore:** i nomi
Elona valgono per entrambi, le regole sui segnaposto `#1` e sui tag Unity no —
qui i segnaposto sono espressioni HSP.

Questo task **non è TDD**: sono documenti. La verifica è che le regole siano
applicabili e non contraddicano `verifica.py`.

**File:**
- Crea: `glossario.md`
- Crea: `guida-stile.md`

- [ ] **Passo 1: estrarre i termini ricorrenti da tradurre**

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -c "
from collections import Counter
from strumenti import percorsi
from strumenti.estrai import estrai_da_file
import re
c = Counter()
for n in ['text','command','action','proc','skill','trait']:
    for v in estrai_da_file(percorsi.SORGENTE_HSP / (n + '.hsp')):
        for p in re.findall(r\"[A-Za-z][a-z]+\", v['en']):
            if len(p) > 3: c[p.lower()] += 1
for p, k in c.most_common(80): print(f'{k:5d}  {p}')
"
```

I termini con più occorrenze sono quelli che una resa incoerente rende più
visibile. Mettili in glossario per primi.

- [ ] **Passo 2: scrivere `glossario.md`**

Struttura a tabelle per area, ereditata da Elin:

```markdown
# Glossario EN → IT

Vincolante: un termine tradotto qui si riusa ovunque. Se una resa non funziona
in un contesto, si cambia **qui** e si ritraduce, non si deroga nel lotto.

## Interfaccia e comandi

| EN | IT | note |
|---|---|---|
| Inventory | Inventario | |
| Equipment | Equipaggiamento | |

## Statistiche e abilità

| EN | IT | note |
|---|---|---|
| Strength | Forza | |
| Constitution | Costituzione | |

## Stati e incantesimi

| EN | IT | note |
|---|---|---|
| Blessed | Benedetto | mai «consacrato»: il gioco lo contrappone a Cursed |
| Cursed | Maledetto | |

## Nomi propri

Vedi `invariati.md`: restano in inglese e non vanno in questa tabella.
```

Riempi le tabelle con i termini del passo 1. Non inventare voci per termini che
non compaiono: un glossario gonfio non si consulta.

- [ ] **Passo 3: scrivere `guida-stile.md`**

Le regole **specifiche di questo gioco**, non ereditabili da Elin:

```markdown
# Guida di stile

## Registro

- **Il gioco parla a te: si usa il «tu».** «Non hai abbastanza oro», «Sei sicuro?».
  Elona+ si rivolge al giocatore in seconda persona e non c'e' il problema del
  registro misto che ha Elin: qui le righe del giocatore e quelle dei PNG sono
  chiamate `lang()` diverse.
- **Mai un aggettivo o un participio riferito al giocatore**: il genere non si
  conosce. `You are too full` → «Non riesci a mangiare altro», non «Sei sazio».

## Espressioni dinamiche

- **`name(tc)`, `itemname(ci)`, `cdatan(...)` sono contenuto: vanno conservate.**
  Perderle significa perdere il nome dal messaggio. `verifica.py` lo blocca.
- **`_s(...)`, `is(...)`, `was(...)`, `your(...)` sono grammatica inglese e vanno
  tolte.** Restituiscono `"s"`, `"is"`, `"'s"`: scriverebbero inglese dentro la
  frase italiana. Riscrivi la frase in italiano corretto e concatena solo il
  contenuto. `verifica.py` le blocca se restano.
- **`he(...)`, `his(...)`, `him(...)` sono pronomi e passano da `lang()`:** si
  localizzeranno quando si tradurra' `init.hsp` in Fase 4. Puoi tenerle o
  toglierle. Toglierle e' quasi sempre meglio: l'italiano il pronome lo sottintende.
- **L'ordine dei pezzi si puo' cambiare.** `name(tc) + " drops " + itemname(ci)`
  → `name(tc) + " lascia cadere " + itemname(ci)`. E' il vantaggio di tradurre
  l'espressione intera invece del solo testo.
- **Attenzione alle preposizioni davanti a un nome**: `name(tc)` puo' restituire
  un nome proprio o «qualcosa», e l'articolo non si fonde. Preferisci costruzioni
  che non richiedano `del`/`al`.

## Ortografia

- **Nel dizionario si scrivono gli accenti veri**: `perché`, `più`, `è`. La
  degradazione ad apostrofo la fa `applica.py`. Scrivere `perche'` a mano e' un
  errore che `verifica.py` segnala.
- **Mai il carattere `"` in una traduzione statica.** Usa `“ ”`. Mai `«»`.
- Le maiuscole dei nomi di abilita' e oggetti seguono l'inglese solo dove il
  gioco le usa come nomi propri.

## Prima di reimportare

```powershell
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
```

Entrambi verdi, sempre.
```

- [ ] **Passo 4: commit**

```bash
git add glossario.md guida-stile.md
git commit -m "glossario e guida di stile per la Fase 1"
```

---

## Task 6 — Il primo lotto: `text.hsp`, con collaudo in gioco

`text.hsp` è il file giusto per primo: 2.127 stringhe traducibili, di cui 1.896
statiche — la quota più alta di testo semplice — ed è **quello che si vede subito
a schermo**. Se qualcosa nella catena è ancora rotto, qui si vede in un minuto.

Non si traduce tutto il file in un colpo. **Primo lotto: 50 stringhe**, scelte
per coprire i casi difficili, esattamente come la prova 2 della Fase 0 (SPEC §6).

**File:**
- Crea: `lavoro/fase1-text-001.jsonl`
- Crea: `dizionario/text.hsp.jsonl`

- [ ] **Passo 1: estrarre il primo lotto**

```powershell
python -m strumenti.estrai text.hsp --uscita lavoro/fase1-text-001.jsonl --max 50
```

- [ ] **Passo 2: controllare che il lotto contenga i casi difficili**

```powershell
python -c "
import json
voci = [json.loads(r) for r in open('lavoro/fase1-text-001.jsonl', encoding='utf-8')]
din = [v for v in voci if v['tipo'] == 'dinamica']
print(f'{len(voci)} voci, {len(din)} dinamiche')
print('con morfologia inglese:', sum(1 for v in din if any(f in v['en_grezzo'] for f in ['_s(', 'is(', 'was(', 'your('])))
print('avvolte in cnvtalk   :', sum(1 for v in voci if 'cnvtalk(' in v['en_grezzo']))
"
```

Servono **almeno cinque dinamiche con morfologia inglese** e **almeno cinque
stringhe con vocali accentate nella traduzione**. Se il lotto non le contiene,
alza `--max` finché non ci sono: è il lotto che deve provare la catena, non il
contrario.

- [ ] **Passo 3: tradurre**

Compila il campo `it` di ogni riga, seguendo `glossario.md` e `guida-stile.md`.
Per le dinamiche l'italiano è **l'espressione HSP intera**, non il solo testo.

- [ ] **Passo 4: verificare il lotto**

```powershell
python -m strumenti.verifica lavoro/fase1-text-001.jsonl
```
Atteso: `50 voci, nessun problema`. Se segnala qualcosa, **correggi la traduzione,
non la regola.**

- [ ] **Passo 5: reimportare**

```powershell
python -m strumenti.reimporta lavoro/fase1-text-001.jsonl
```

- [ ] **Passo 6: costruire e compilare**

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
```
Atteso: `#No error detected.` e l'eseguibile prodotto.

- [ ] **Passo 7: vedere le stringhe a schermo — il collaudo che nessun test sostituisce**

```powershell
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe"
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Da guardare, in quest'ordine:

1. le stringhe tradotte compaiono in italiano;
2. **le accentate si leggono `perche'`**, non `perche` né come carattere rotto.
   È il rischio numero uno del progetto (SPEC §4);
3. le dinamiche non mostrano una `s` inglese appiccicata a un verbo italiano;
4. nessuna riga esce dal riquadro dell'interfaccia.

Se una accentata è sparita, **fermati e non tradurre altro**: la degradazione non
funziona e ogni lotto tradotto da qui in poi andrebbe rifatto.

- [ ] **Passo 8: commit**

```bash
git add dizionario/text.hsp.jsonl lavoro/fase1-text-001.jsonl
git commit -m "Fase 1: primo lotto di text.hsp, 50 stringhe, viste a schermo"
```

---

## Task 7 — I lotti restanti e `avanzamento.md`

Chiuso il collaudo, il resto è ripetizione dello stesso ciclo. L'ordine è per
visibilità decrescente: quello che si vede di più si traduce prima, così ogni
lotto ha valore anche se il progetto si ferma lì.

| ordine | file | da tradurre |
|---|---|---|
| 1 | `text.hsp` (resto) | 2.127 occorrenze |
| 2 | `command.hsp` | 1.481 |
| 3 | `action.hsp` | 1.502 |
| 4 | `proc.hsp` | 1.327 |
| 5 | `skill.hsp` | 894 |
| 6 | `trait.hsp` | 406 |

**Lotti da 200-300 voci.** Più piccoli fanno perdere tempo in cicli, più grandi
rendono doloroso scartare un lotto sporco — e `reimporta` è tutto-o-niente.

- [ ] **Passo 1: creare `avanzamento.md`**

```markdown
# Avanzamento

Aggiornato a mano dopo ogni reimportazione.

| file | tradotte | totali | % |
|---|---|---|---|
| `text.hsp` | 50 | 2.127 | 2% |
| `command.hsp` | 0 | 1.481 | 0% |
| `action.hsp` | 0 | 1.502 | 0% |
| `proc.hsp` | 0 | 1.327 | 0% |
| `skill.hsp` | 0 | 894 | 0% |
| `trait.hsp` | 0 | 406 | 0% |
```

Il conteggio si ottiene con:

```powershell
python -m strumenti.verifica --dizionario
```

- [ ] **Passo 2: per ogni lotto, il ciclo**

Ripeti finché il file non è finito:

```powershell
python -m strumenti.estrai <file>.hsp --uscita lavoro/fase1-<file>-NNN.jsonl --max 250
# tradurre il campo it
python -m strumenti.verifica lavoro/fase1-<file>-NNN.jsonl
python -m strumenti.reimporta lavoro/fase1-<file>-NNN.jsonl
python -m pytest strumenti/tests -q
git add dizionario/ lavoro/ ; git commit -m "Fase 1: <file> lotto NNN"
```

- [ ] **Passo 3: ogni due lotti, la prova d'identità e il cancello**

```powershell
python -m strumenti.prova_identita
python -m strumenti.compila --cancello
```

Non serve dopo ogni lotto — il dizionario non tocca il sorgente — ma serve
**prima di ogni collaudo in gioco**, perché un build abortito a metà si scopre
altrimenti dopo venti minuti di traduzione.

- [ ] **Passo 4: a fine file, collaudo in gioco**

Stessa procedura del Task 6, passo 7. Aggiorna `avanzamento.md` e committa.

- [ ] **Passo 5: chiusura della fase**

Quando i sei file sono a 100%:

```powershell
python -m strumenti.verifica --dizionario   # atteso: 0 da ritradurre, 0 non tradotte
python -m strumenti.prova_identita          # atteso: 72/72
python -m strumenti.compila --eseguibile
python -m pytest strumenti/tests -q
```

Poi aggiorna `SPEC.md` (stato), `RIPRESA-sessione.md` e `decisioni.md` con quello
che la fase ha insegnato, e apri il piano della Fase 2.

---

## Cosa questo piano **non** fa

Detto esplicitamente, perché non venga scoperto a metà:

- **Non traduce i 250 KB di testi esterni** (`book.txt`, `talk.txt`, `exhelp.txt`,
  `board.txt`). Non passano da `lang()` e vogliono una catena diversa: sono Fase 4.
- **Non risolve dove stanno i nomi degli oggetti.** `db_item.hsp` contiene zero
  `lang()` e il punto è ancora aperto (SPEC §2). Condiziona la Fase 2, non questa.
- **Non implementa `installa.py`.** Il collaudo si fa copiando l'eseguibile a mano
  con un nome distinto, che è più sicuro finché il gioco installato è l'unica
  copia funzionante.
- **Non tocca la larghezza dell'interfaccia.** `verifica.py` non misura quanto una
  stringa è lunga a schermo: se in Fase 1 si vedono righe tagliate, quello diventa
  un task suo, con una misura vera invece di una soglia inventata.
