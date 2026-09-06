# Elona+ Custom-GX — Traduzione italiana

Traduzione italiana di Elona+ Custom-GX 2.31.2.0.

Copre i nomi degli oggetti e delle creature, le descrizioni, i dialoghi, le
missioni, il gioco di carte, i menù, i messaggi di combattimento e i file di
testo in `data/`.

Traduzione amatoriale, non ufficiale, non affiliata agli autori del gioco.

## Installazione

Requisiti: Windows, Python 3.11 o successivo, una connessione a Internet.

1. Scaricare e scompattare l'archivio.
2. Eseguire `costruisci.bat`.
3. Indicare la cartella di Elona+ Custom-GX quando viene richiesta.

Il primo avvio scarica circa 60 MB e richiede qualche minuto. Al termine la
cartella del gioco contiene `cgx-ita.exe` accanto a `elonapluscgx.exe`, che non
viene modificato. I salvataggi sono compatibili con entrambi gli eseguibili.

Vengono aggiunti anche sei file `data/*_it.txt`, che il gioco carica solo se
presenti.

Istruzioni estese e risoluzione dei problemi: [`LEGGIMI.txt`](LEGGIMI.txt).

### Disinstallazione

`disinstalla-italiano.bat` rimuove i sette file aggiunti. L'installazione
originale resta invariata.

## Perché la distribuzione non include un eseguibile già compilato

Il sorgente di Custom-GX non specifica una licenza, quindi non esiste un
permesso esplicito per ridistribuire il gioco compilato. Il permesso è stato
richiesto agli autori nella
[issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37) e la
richiesta è tuttora aperta.

Nel frattempo la compilazione avviene sulla macchina di chi installa.
`costruisci.py` scarica il sorgente dal repository di Custom-GX e l'SDK HSP 3.4
dal sito di Onion Software, e legge i file di testo dall'installazione locale.
Questo repository fornisce soltanto il dizionario.

L'eseguibile prodotto da HSP non è riproducibile: due compilazioni dello stesso
albero, eseguite a un minuto di distanza, differiscono nel 96,56% dei byte. Le
impronte di due installazioni non coincidono, e il confronto non è un indicatore
utile.

## Come funziona

La traduzione è un dizionario esterno applicato a un clone pulito del sorgente
al momento della compilazione. Il sorgente originale non viene mai modificato in
sede: la sua integrità è verificata con un manifesto SHA-256 di 72 file, e la
revisione è fissata a un tag anziché a un ramo, perché un ramo in movimento
invaliderebbe manifesto e conteggi senza segnalarlo.

Il testo del gioco richiede due meccanismi distinti:

- le stringhe contenute in `lang("giapponese", "inglese")` sono gestite dal
  **dizionario**: 64 file JSONL, 32.782 voci, indicizzate per contenuto;
- il resto — testo inglese non incapsulato, ordine delle parole, larghezze dei
  riquadri, letterali che il codice cerca a runtime — è gestito da **1.431
  toppe** al sorgente, ciascuna con la motivazione registrata.

`rinviate.jsonl` elenca 113 stringhe che non vengono tradotte, ciascuna con la
propria condizione: riga non raggiungibile, già risolta da una toppa, resa
inutile dal flusso del programma, in attesa di una modifica a monte. Nessuna è
in attesa di lavoro.

### Controlli automatici

Il rischio principale di una traduzione di queste dimensioni è che una porzione
di testo resti indietro senza che nessuno se ne accorga. Cinque controlli
misurano ciascuno una domanda diversa, e ognuno impone che ogni file sia coperto
oppure dichiarato tale con il relativo conteggio e la motivazione.

| controllo | domanda |
|---|---|
| `copertura` | ogni `lang()` del sorgente è raggiunta dal dizionario? |
| `disegnate` | ogni stringa che arriva a un comando di disegno è coperta? |
| `salti` | e quelle che ci arrivano attraverso una variabile? |
| `operandi` | e i letterali che il codice cerca all'interno di una stringa? |
| `prova_identita` | il sorgente non tradotto si riproduce byte per byte? |

L'ultimo controllo aggiunto è `operandi`. I primi tre esaminano il testo
visualizzato; nessuno esaminava i letterali che `instr` e `sreplace` cercano
dentro una stringa. Una battuta tradotta può restare inattiva perché la parola
che la attiva è ancora in inglese.

### Stato

| | |
|---|---|
| test | 1.148 superati, 6 saltati |
| dizionario | 32.782 voci, 0 da ritradurre |
| perimetro tradotto | 28.028 su 28.028 (31.795 includendo i file di dato) |
| toppe | 1.431 |
| controlli | copertura, salti, disegnate, operandi: tutti superati |

Il perimetro misura le stringhe individuate finora, non la totalità del gioco.
Più volte un controllo nuovo ha individuato un insieme di stringhe scoperte
mentre tutti i controlli esistenti risultavano superati; l'ultimo caso è
`operandi`, che ha individuato dodici righe in un progetto senza controlli
falliti.

### Limitazione nota

La traduzione non è ancora stata verificata schermata per schermata all'interno
del gioco. I controlli automatici misurano la copertura e la coerenza del testo,
non il suo aspetto una volta disegnato. Le segnalazioni sono benvenute,
in particolare da installazioni diverse da quella di sviluppo.

## Struttura del repository

| percorso | contenuto |
|---|---|
| `costruisci.py`, `costruisci.bat` | compilazione locale dell'eseguibile italiano |
| `LEGGIMI.txt` | istruzioni per l'installazione |
| `dizionario/` | la traduzione |
| `toppe.jsonl` | modifiche al sorgente, con motivazione |
| `rinviate.jsonl` | stringhe non tradotte, con la relativa condizione |
| `strumenti/` | 48 moduli: estrazione, applicazione, controlli, build, pacchetto |
| `strumenti/tests/` | 48 file di test |
| `glossario.md` | corrispondenze EN → IT vincolanti |
| `contratto-nomi.md` | composizione dei nomi, articoli, plurali |
| `guida-stile.md` | registro, marcatori da preservare, accordo di genere |
| `invariati.md` | stringhe mantenute in inglese per scelta |
| `decisioni.md` | scelte non ovvie e relative motivazioni |
| `SPEC.md` | progettazione |

SDK, clone del sorgente e albero di compilazione sono rigenerabili e restano
fuori dal repository.

## Lavorare alla traduzione

    estrai      genera un lotto JSONL da un intervallo di file
                (si compila il campo `it` di ogni riga)
    reimporta   valida il lotto e lo scrive nel dizionario solo se privo di errori
    verifica    controlla interpolazioni, glossario, accenti, larghezze
    applica     inietta dizionario e toppe in un clone pulito
    scene, carte, schede, dialoghi --applica
    compila     invoca `hspcmp.dll` senza l'interfaccia dell'editor

I quattro comandi `--applica` vanno eseguiti dopo `applica` e prima di
`compila`. Eseguire `applica` da solo lascia l'albero in uno stato intermedio, e
i test che leggono la build falliscono.

### Accenti e CP932

CP932 non rappresenta le vocali accentate e le rimuove senza segnalarlo
(`perché` diventa `perche`). A schermo si adotta la forma con l'apostrofo:
`perche'`.

Nel dizionario si scrive sempre l'italiano corretto con gli accenti. La
conversione avviene in fase di compilazione, dentro `applica`. Le forme con
apostrofo scritte a mano vengono segnalate come errore da `verifica`.

## Crediti

Elona è stato creato da **Noa**. Elona+ è di **Ano**. Elona+ Custom è di
**AnnaBannana** e **BloodyShade**; Elona+ Custom-G di **Glyphy**; Elona+
Custom-GX è stato creato da **Ruin0x11** ed è mantenuto da **JianmengYu**.

Questa traduzione non è affiliata a nessuno di loro.

## English

Unofficial Italian translation of Elona+ Custom-GX 2.31.2.0.

The repository contains no game code. The translation is an external dictionary
plus a set of documented source patches, and `costruisci.py` builds the Italian
executable on the user's own machine, downloading Custom-GX's source from its
GitHub repository and the HSP SDK from Onion Software. The result is installed
as `cgx-ita.exe` alongside the original executable, which is never modified,
together with six additive `data/*_it.txt` files the game loads only if present.
`disinstalla-italiano.bat` removes them.

Custom-GX specifies no license, so permission to distribute a prebuilt binary
was requested in
[issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37) rather
than assumed.

Requirements: Windows, Python 3.11 or later. Bug reports are welcome.
