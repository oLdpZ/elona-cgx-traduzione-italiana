# SPEC — Elona+ Custom-GX, Traduzione Italiana

Design approvato il 2026-08-06. Questo documento è vincolante: le decisioni qui
dentro si cambiano modificando questo file, non improvvisando in sessione.

Stato: **design approvato, Fase 0 non ancora eseguita.**

---

## 1. Scopo

Tradurre in italiano il roguelike **Elona+ Custom-GX 2.31.2.0**, installato in
`C:\Games\Elona\elonaplus2.31\`.

Destinazione: uso personale, ma il progetto è strutturato fin dall'inizio come
pubblicabile (git, dizionario separabile, licenza da verificare prima di
pubblicare). La pubblicazione non è un obiettivo di questa fase.

Progetto gemello e modello di riferimento: [[Elin - Traduzione Italiana]], che
condivide universo, lessico e metodo di lavoro.

---

## 2. Contesto tecnico

Fatti verificati il 2026-08-06, non stime.

**Il gioco.** Elona+ Custom-GX è una variante di Elona+ mantenuta da
[JianmengYu](https://github.com/JianmengYu/ElonaPlusCustom-GX) (l'originale di
Ruin0x11 è fermo alla 2.15R). La release corrente è **2.31.2.0** (24/05/2026),
basata su Elona+ 2.31. Il `README` del branch `work` parla già di 2.32, ma quel
port non è ancora rilasciato.

**Dove sta il testo.**

| Collocazione | Volume | Note |
|---|---|---|
| Sorgente HSP (`2.05-custom-gx/*.hsp`, 72 file) | **26.817 coppie `lang()`** | Il grosso del gioco |
| File esterni in `data/` | ~250 KB | `book.txt` 115 KB, `talk.txt` 86 KB, `exhelp.txt` 17 KB, `board.txt` 15 KB |

Distribuzione delle `lang()` sui file principali:

| File | `lang()` |
|---|---|
| `db_creature.hsp` | 5.755 |
| `chat.hsp` | 4.828 |
| `db_card.hsp` | 2.340 |
| `text.hsp` | 2.152 |
| `command.hsp` | 1.590 |
| `action.hsp` | 1.502 |
| `proc.hsp` | 1.370 |
| `skill.hsp` | 917 |
| `event.hsp` | 756 |

**Forma delle stringhe.** Il sorgente usa ovunque la macro `lang(giapponese, inglese)`:

```hsp
#define global txt_invfull txt lang("バックパックが一杯だ。", "Your inventory is full.")
#define global txt_guard txt lang(name(tc) + "は" + name(...) + "をかばった！", name(tc) + " guarded " + name(...) + ".")
```

Estrazione e reinserimento sono quindi **meccanici e scriptabili**. È la
premessa che rende il progetto fattibile.

**Encoding.** Il repo salva i `.hsp` in UTF-8 e li estrae in CP932 tramite
`.gitattributes` (`working-tree-encoding=CP932`). Il compilatore HSP lavora in
CP932.

**Punto aperto.** `db_item.hsp` (4,6 MB) contiene **zero** `lang()`: i nomi degli
oggetti passano da `ioriginalnameref` e risiedono altrove. `ndata.csv` /
`ndata-e.csv` in `data/` sono liste di parole per la generazione di nomi casuali,
non il database dei nomi oggetto. **Individuare dove stanno i nomi degli oggetti
è un compito esplicito della Fase 0** e condiziona il dimensionamento della Fase 2.

---

## 3. Architettura

### 3.1 Il sorgente upstream non viene mai modificato

La traduzione **non** è un fork del sorgente CGX. È un **dizionario esterno**
applicato a un clone pulito solo al momento della build:

```
clone upstream (intatto)  +  dizionario/  --applica.py-->  albero di build  --HSP-->  elonapluscgx-it.exe
```

Motivazioni:

- **Riallineamento alle release.** A ogni nuova versione CGX si fa `git pull` sul
  clone e si riapplica il dizionario. Nessun conflitto di merge su 27.000 punti.
  `verifica.py` produce l'elenco delle stringhe cambiate o sparite a monte, che
  diventa la coda di ritraduzione.
- **Pubblicazione.** Si pubblicano dizionario e strumenti (pochi MB), non un fork
  di un progetto di terzi. Semplifica nettamente la questione licenza.
- **Coerenza col progetto gemello.** È lo stesso principio adottato su Elin: i
  file originali del gioco non vengono mai modificati.

### 3.2 Chiave di identificazione della stringa

`sha1(giapponese + "\x00" + inglese)`, con ambito **per-file** e contatore di
occorrenza progressivo a disambiguare i duplicati esatti dentro lo stesso file.

Il giapponese è la componente stabile: se a monte cambia solo la formulazione
inglese, la firma si rompe **di proposito** e la stringa entra in coda di
revisione invece di restare tradotta su un testo che non esiste più.

### 3.3 Dove finisce l'italiano

L'italiano **sostituisce il secondo argomento** di `lang()`, producendo un
eseguibile separato `elonapluscgx-it.exe`. La macro `lang()` non viene toccata e
i 26.817 siti di chiamata restano invariati. L'inglese resta disponibile nella
build ufficiale, che non viene sovrascritta.

### 3.4 Struttura della cartella

| percorso | contenuto |
|---|---|
| `SPEC.md` | questo documento |
| `README.md` | orientamento rapido e stato |
| `glossario.md` | termine EN → IT, vincolante |
| `guida-stile.md` | registro, marcatori da conservare, strategie per l'accordo di genere |
| `invariati.md` | stringhe che restano in inglese per scelta documentata |
| `decisioni.md` | scelte non ovvie e il perché |
| `avanzamento.md` | tradotte / totali per file e per fase |
| `RIPRESA-sessione.md` | punto di ripresa per la sessione successiva |
| `piani/` | piani di fase |
| `dizionario/` | **la traduzione — sorgente di verità** |
| `lavoro/` | lotti JSONL in lavorazione |
| `strumenti/` | script Python |
| `sorgente/` | clone upstream CGX — git-ignored, ricreabile |
| `dist/` | build italiana installabile |

`glossario.md` nasce come copia del glossario Elin (451 righe, in larga parte
interfaccia e termini generici) e da lì diverge.

---

## 4. Rischio primario: l'encoding uccide gli accenti

**CP932 non contiene le vocali accentate italiane, e non segnala l'errore.**
Verificato empiricamente: ogni accentata viene sostituita silenziosamente con la
vocale nuda.

| carattere | byte in CP932 | risultato |
|---|---|---|
| `è` `é` | `65` | `e` |
| `à` | `61` | `a` |
| `ì` | `69` | `i` |
| `ò` | `6F` | `o` |
| `ù` | `75` | `u` |

Siccome git fa checkout in CP932, la perdita avverrebbe **automaticamente e senza
un solo avviso**: `perché` → `perche`, `città` → `citta`.

Tre strade, da valutare in Fase 0 in quest'ordine:

| | Strada | Valutazione |
|---|---|---|
| **A** | Forma con apostrofo — `perche'`, `citta'`, `piu'` | Funziona con certezza. Estetica da localizzazione anni '90. **Piano di riserva garantito.** |
| **B** | Byte CP1252 diretti (`0xE8` = `è`) nel sorgente | `0xE8` è un lead byte Shift-JIS valido: il compilatore HSP può inglobare il carattere successivo. Da provare, non su cui contare. |
| **C** | Stringhe tradotte in tabella esterna caricata a runtime | Risolve accenti e manutenzione insieme; Elona legge già `book.txt`/`talk.txt` esterni. Ma è modifica al codice del gioco, non solo traduzione. |

L'esito determina se il risultato è "un Elona in italiano con gli apostrofi" o
"un Elona in italiano". **Va deciso prima di tradurre in volume**, non dopo.

---

## 5. Rischio secondario: l'accordo grammaticale

`estrai.py` classifica ogni stringa in due binari:

- **Statiche** — nessuna interpolazione (`"Your inventory is full."`). Traduzione
  ordinaria.
- **Dinamiche** — contengono concatenazioni
  (`name(tc) + " guarded " + name(...)`, `"You successfully create " + itemname(ci,1) + "!"`).
  Estratte **insieme al codice circostante come contesto** e lavorate a parte.

L'inglese non ha accordo di genere e numero; l'italiano sì. Tradurre le dinamiche
alla cieca produce sgrammaticature su scala industriale. `guida-stile.md` fissa
le strategie standard:

- costruzioni impersonali e neutre rispetto al genere;
- nessun articolo determinativo davanti a un nome interpolato;
- riordino della frase per spostare il segnaposto dove l'accordo non serve.

Ciò che resta irrisolvibile va in `invariati.md`: inglese **per scelta
documentata**, non per dimenticanza.

---

## 6. Fasi

Ogni fase termina con un gioco installabile e più italiano della precedente.
Interrompere il progetto dopo una qualsiasi di esse lascia un risultato usabile.

| Fase | Contenuto | Volume | Risultato |
|---|---|---|---|
| **0** | Prototipo tecnico | ~50 stringhe | Le tre prove passano, strada accenti decisa, posizione dei nomi oggetto individuata |
| **1** | UI e messaggi — `text` `command` `action` `proc` `skill` `trait` | 7.937 | Interfaccia e messaggistica in italiano |
| **2** | Nomi — `db_creature` `db_card`, più i nomi oggetto una volta localizzati | 8.095 + nomi oggetto | Gioco sostanzialmente italiano |
| **3** | Dialoghi — `chat.hsp` | 4.828 | Conversazioni con NPC in italiano |
| **4** | Coda — i restanti 60 file `.hsp` minori e i testi esterni | 5.957 + 250 KB | Copertura completa |

Somma verificata: 7.937 + 8.095 + 4.828 + 5.957 = **26.817**, il totale delle
`lang()` nel sorgente. I 250 KB di testi esterni (`book.txt`, `talk.txt`,
`exhelp.txt`, `board.txt`) sono aggiuntivi e non passano da `lang()`.

### Fase 0 — il cancello

Tre prove in ordine. Nessuna traduzione in volume inizia prima che passino tutte.

1. **Gli accenti arrivano a schermo?** Valutare A, B, C della §4 e fissare la
   scelta in `decisioni.md`.
2. **L'exe si ricompila?** SDK HSP 3.4 più `hsplua.dll`, build da sorgente **non
   modificato**; l'eseguibile prodotto deve avviarsi e caricare un salvataggio.
   Senza una build riproducibile dall'originale, il resto è teoria.
3. **Il ciclo gira end-to-end?** ~50 stringhe scelte apposta (metà statiche, metà
   dinamiche) attraverso `estrai → traduci → applica → compila → installa →
   verifica → visto a schermo`.

In parallelo: individuare dove risiedono i nomi degli oggetti (§2, punto aperto).

---

## 7. Controllo qualità

`verifica.py` **blocca** il reimport quando:

- le interpolazioni non combaciano con l'originale — stesso numero di `+` e
  stesse chiamate di funzione;
- una traduzione è identica all'inglese e non è in whitelist in `invariati.md`;
- il glossario è violato;
- **un accento è andato perso nella conversione di encoding** (confronto prima/dopo
  round-trip);
- una stringa di interfaccia supera la larghezza massima del suo riquadro;
- l'eseguibile non compila.

---

## 8. Strumenti

Contratti, non implementazione. Python, coerente con il progetto Elin.

| script | responsabilità |
|---|---|
| `estrai.py` | dal clone upstream produce un lotto JSONL per un intervallo di file/righe; classifica statica/dinamica; allega il contesto di codice alle dinamiche |
| `applica.py` | inietta il dizionario su un clone pulito producendo l'albero di build; non scrive mai dentro `sorgente/` |
| `reimporta.py` | valida un lotto tradotto (firma, campi presenti, controlli di contenuto) e solo se pulito lo scrive nel dizionario |
| `verifica.py` | esegue le regole della §7 su un lotto o sull'intero dizionario |
| `compila.py` | invoca l'SDK HSP 3.4 sull'albero di build e produce `elonapluscgx-it.exe` |
| `installa.py` | copia la build in `C:\Games\Elona\elonaplus2.31\`, preservando l'eseguibile inglese e i salvataggi |

Ogni script è indipendente, con ingresso e uscita su file, invocabile da solo e
testabile senza gli altri.

---

## 9. Fuori ambito

Deliberatamente esclusi, per non gonfiare il progetto:

- traduzione del giapponese (si traduce **dall'inglese**: è la versione mantenuta
  da CGX e quella che l'autore del progetto legge);
- supporto multi-lingua o selettore in gioco — la build italiana è un eseguibile
  separato;
- traduzione della documentazione del gioco (`manual_ENG.txt`, changelog);
- port alla 2.32 finché CGX non la rilascia;
- pubblicazione, packaging delle release e verifica della licenza — si affrontano
  quando il progetto sarà maturo, e la §3.1 è progettata per renderli possibili.

---

## 10. Decisioni prese

Registrate anche in `decisioni.md` man mano che se ne aggiungono.

| # | Decisione | Motivo |
|---|---|---|
| 1 | Dizionario esterno, non fork del sorgente | Riallineamento senza conflitti a ogni release CGX; pubblicabilità; coerenza con Elin |
| 2 | Chiave = `sha1(jp + \0 + en)` per-file | Il giapponese è stabile; una modifica dell'inglese a monte deve rompere la firma di proposito |
| 3 | L'italiano sostituisce l'argomento inglese di `lang()` | Nessuna modifica alla macro né ai 26.817 siti di chiamata |
| 4 | Traduzione dall'inglese, non dal giapponese | È la versione mantenuta da CGX |
| 5 | Copertura per priorità a fasi giocabili | Ogni fase ha valore autonomo; l'abbandono a metà lascia comunque un risultato |
| 6 | Prova encoding **prima** di ogni traduzione in volume | Il rischio più grave del progetto; costa ore, non settimane |
| 7 | Base 2.31, non 2.32 | CGX non ha ancora rilasciato il port alla 2.32 |
