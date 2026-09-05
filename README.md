# Elona+ Custom-GX — Traduzione Italiana

Traduzione italiana di **Elona+ Custom-GX**, alla versione **2.31.2.0**.

Non è una traduzione parziale dell'interfaccia: sono tradotti i nomi degli
oggetti e delle creature, le descrizioni, i dialoghi, le missioni, il gioco di
carte, i menù, i messaggi di combattimento e i file di testo di `data/`.

---

## Come si installa

Doppio clic su **`costruisci.bat`**. Serve Python 3.11 o più nuovo e una
connessione; la prima volta scarica circa 60 MB e ci mette qualche minuto.

Alla fine, nella cartella del gioco, trovi **`cgx-ita.exe`** accanto al tuo
`elonapluscgx.exe`, che resta dov'è e continua a funzionare. Gli stessi
salvataggi vanno bene per tutt'e due. Per tornare indietro c'è
`disinstalla-italiano.bat`, che cancella i sette file aggiunti.

I dettagli, i casi storti e cosa fare se qualcosa non va stanno in
[`LEGGIMI.txt`](LEGGIMI.txt).

### Perché non c'è un eseguibile già pronto

Perché non è nostro da regalare. Il sorgente di Custom-GX **non ha una
licenza**, quindi nessuno ci ha dato il permesso di distribuire il gioco
compilato, e non ce lo prendiamo da soli. Il permesso è stato chiesto
([issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37)); nel
frattempo l'italiano lo mette insieme il tuo computer.

`costruisci.py` non distribuisce niente di nessuno: prende il **sorgente** da
GitHub dagli autori di Custom-GX, l'**SDK HSP** dal sito di Onion Software, i
**file di testo** dalla tua installazione. Da qui arriva solo il **dizionario**,
che è l'unica cosa nostra.

⚠️ **L'eseguibile HSP non è riproducibile**: due compilazioni dello stesso
identico albero, a un minuto di distanza, differiscono nel 96,56% dei byte. Il
tuo `cgx-ita.exe` avrà un'impronta diversa da quella di chiunque altro, ed è
normale. Non confrontarla con nessuno.

---

## Com'è fatta

La traduzione è un **dizionario esterno** applicato a un clone pulito del
sorgente al momento della build. ⚠️ **Il sorgente di monte non viene mai
scritto**: la sua integrità si verifica col manifesto SHA-256, e il pin è a un
**tag**, non a un ramo — un ramo che si muove invaliderebbe manifesto e conteggi
in silenzio.

Il testo del gioco sta in due posti, e vogliono due macchine diverse:

- le stringhe dentro `lang("giapponese", "inglese")` → il **dizionario**, 64
  file JSONL, 32.782 voci, indicizzato per contenuto;
- tutto il resto — testo inglese nudo, ordini di parole, larghezze dei riquadri,
  chiavi che il codice cerca — → le **toppe**, 1.431, ognuna con scritto il
  *perché* e non solo il *cosa*.

Poi c'è quel che si è deciso di **non** rendere: 113 voci in `rinviate.jsonl`,
ognuna con la sua condizione (riga morta, risolta da toppa, morta per flusso,
aspetta il monte). Nessuna aspetta lavoro.

### Le cinque reti

Il rischio vero di una traduzione grossa non è tradurre male: è **non
accorgersi** che qualcosa è rimasto indietro. Perciò ogni domanda ha una rete
che la misura, e ognuna ha un cancello: o un file è coperto, o è **dichiarato**
col suo conto e col motivo.

| rete | la domanda a cui risponde |
|---|---|
| `copertura` | ogni `lang()` del sorgente è raggiunta dal dizionario? |
| `disegnate` | ogni stringa che arriva a un comando che disegna è coperta? |
| `salti` | …e quelle che ci arrivano passando per una variabile? |
| `operandi` | e la **chiave** che il codice *cerca*, non quella che stampa? |
| `prova_identita` | il sorgente non toccato si riproduce byte per byte? |

⭐ L'ultima è la più giovane e dice perché servono tutte: le prime tre guardano
il testo che il giocatore **legge**, e nessuna guardava il letterale che
`instr` o `sreplace` vanno a cercare *dentro* una stringa. Una battuta può
essere italiana da sessioni e restare spenta perché la parola che l'accende è
ancora inglese.

### I numeri di oggi

    prove                  1.148 verdi, 6 saltate
    dizionario             32.782 voci, 0 da ritradurre
    perimetro              28.028 su 28.028 = 100% (31.795 coi file di dato)
    toppe                  1.431
    reti                   copertura, salti, disegnate, operandi: tutte verdi

⚠️ **Quel 100% è il perimetro, non il progetto.** Dice che le stringhe che
qualcuno ha *chiesto* sono rese; non dice che non esistano fronti che nessuno ha
ancora chiesto. È già successo più volte che una rete nuova, o una sonda a mano,
ne trovasse uno mentre tutto era verde — l'ultima è `operandi`, che ha trovato
dodici righe in un progetto che non aveva un solo cancello rosso.

### Quel che manca

**Il collaudo a schermo.** Nessuna misura dice che una resa sia stata *vista*.
È l'unico debito grosso rimasto, ed è la differenza fra «tutto verde» e
«funziona».

---

## Struttura

| percorso | contenuto |
|---|---|
| `costruisci.py`, `costruisci.bat` | quel che compila l'italiano in casa |
| `LEGGIMI.txt` | istruzioni per chi installa |
| `dizionario/` | la traduzione — sorgente di verità |
| `toppe.jsonl` | le modifiche al codice, col perché |
| `rinviate.jsonl` | quel che si è deciso di non rendere, e a che condizione |
| `strumenti/` | 48 moduli: estrazione, applicazione, reti, build, pacchetto |
| `strumenti/tests/` | 48 file di prove |
| `glossario.md` | termine EN → IT, vincolante |
| `contratto-nomi.md` | dove stanno i nomi, chi porta l'articolo, il plurale |
| `guida-stile.md` | registro, marcatori da conservare, accordo di genere |
| `invariati.md` | stringhe che restano in inglese per scelta, non per svista |
| `decisioni.md` | le scelte non ovvie e il perché |
| `SPEC.md` | il design |

Gli artefatti pesanti e rigenerabili (SDK, clone del sorgente, albero di build)
vivono fuori dal repo.

## La catena, per chi vuole lavorarci

    estrai      →  un lotto JSONL da un intervallo di file
    (si traduce il campo `it` di ogni riga)
    reimporta   →  valida il lotto e, solo se pulito, lo scrive nel dizionario
    verifica    →  interpolazioni, glossario, accenti persi, larghezze
    applica     →  inietta dizionario e toppe su un clone pulito
    scene, carte, schede, dialoghi --applica   ←  ⚠️ NON facoltativi
    compila     →  pilota `hspcmp.dll` senza la GUI dell'editor

⚠️ I quattro `--applica` vanno **dopo** `applica` e prima di `compila`: un
`applica` lanciato da solo lascia l'albero in uno stato che nessun documento
descrive, e le prove che leggono la build cadono.

## Accenti

**CP932 cancella silenziosamente le vocali accentate** (`perché` → `perche`).
La forma adottata a schermo è quella con l'apostrofo, `perche'`.

Ma **nel dizionario si scrive sempre l'italiano corretto, con gli accenti
veri**: la degradazione la fa `applica` durante la build. Chi traduce non deve
mai scrivere `perche'` a mano — `verifica` lo segnala come errore.

---

## Grazie a

**JianmengYu**, che mantiene Elona+ Custom-GX. **Ruin0x11**, che l'ha creato.
**Glyphy**, per Elona+ Custom-G. **AnnaBannana** e **BloodyShade**, per Elona+
Custom. **Ano**, per Elona+. **Noa**, per Elona.

Traduzione amatoriale e non ufficiale. Non affiliata a nessuno di loro.

---

### In English

This is an unofficial Italian translation of **Elona+ Custom-GX 2.31.2.0**.

It ships **no game code**: the translation lives here as an external dictionary
plus a set of documented source patches, and `costruisci.py` builds the Italian
executable on the player's own machine — pulling Custom-GX's source from its
GitHub repository and the HSP SDK from Onion Software. The result is installed
as `cgx-ita.exe` *next to* the original executable, which is never modified, and
six additive `data/*_it.txt` files the game loads only if present.

Since Custom-GX carries no license, permission to distribute a prebuilt binary
has been asked for in
[issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37) rather
than assumed.
