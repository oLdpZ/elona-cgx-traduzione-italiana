# Elona+ Custom-GX — Traduzione Italiana

Traduzione italiana di **Elona+ Custom-GX**, sorgente pinnato al tag `2.31.2.0`,
gioco di riferimento installato in `C:\Games\Elona\elonaplus2.31\`.

La traduzione è un **dizionario esterno** applicato a un clone pulito del
sorgente CGX al momento della build. Il sorgente upstream non viene mai
modificato.

Stato: **design approvato (`SPEC.md`); il cancello della Fase 0 è passato per intero.**

Fatto: la catena `estrai → verifica → reimporta → applica` esiste, è sotto test
(122 test verdi) ed è stata provata end-to-end sul sorgente vero — round-trip
CP932, CRLF conservati, manifesto di `sorgente/` intatto. Il sorgente non
modificato **ricompila, e l'eseguibile prodotto si avvia e carica un salvataggio
esistente**:

```
python -m strumenti.compila --cancello
```

Non ancora fatto: `installa.py`, vedere le stringhe tradotte a schermo, e
individuare dove risiedono i nomi degli oggetti.

## Struttura

| percorso | contenuto |
|---|---|
| `SPEC.md` | design approvato: architettura, rischi, fasi, QA |
| `glossario.md` | termine EN → IT, vincolante |
| `guida-stile.md` | registro, marcatori da conservare, accordo di genere |
| `invariati.md` | stringhe che restano in inglese per scelta, non per dimenticanza |
| `decisioni.md` | scelte non ovvie e il perché |
| `avanzamento.md` | tradotte / totali per file e per fase |
| `RIPRESA-sessione.md` | punto di ripresa per la sessione successiva |
| `piani/` | piani di fase |
| `dizionario/` | la traduzione — sorgente di verità |
| `lavoro/` | lotti JSONL in lavorazione |
| `strumenti/` | `estrai.py`, `applica.py`, `reimporta.py`, `verifica.py`, `compila.py`, `prova_identita.py`, `installa.py` |

Nel vault sta solo testo. Gli artefatti pesanti e rigenerabili vivono in
`C:\Games\Elona\_traduzione\`: `hsp34/` (SDK), `sorgente/` (clone upstream),
`build/` (albero di build), `dist/` (eseguibile italiano).

## Flusso di lavoro

1. `estrai.py` produce un lotto **JSONL** da un intervallo di file del sorgente,
   classificando le stringhe in statiche e dinamiche
2. si traduce il campo `it` di ogni riga del lotto
3. `reimporta.py` valida il lotto e, solo se pulito, lo scrive nel dizionario
4. `verifica.py` controlla interpolazioni, glossario, accenti persi, larghezza UI
5. `applica.py` inietta il dizionario su un clone pulito → albero di build
6. `compila.py` produce l'eseguibile italiano pilotando `hspcmp.dll` senza GUI
7. `installa.py` copia la build nel gioco, preservando eseguibile inglese e salvataggi
8. prova in gioco, poi aggiornamento di `avanzamento.md` e `RIPRESA-sessione.md`

## Accenti

**CP932 cancella silenziosamente le vocali accentate** (`perché` → `perche`).
Soluzione adottata: forma con apostrofo, `perche'`.

Ma **nel dizionario si scrive sempre l'italiano corretto, con gli accenti veri**.
La degradazione ad apostrofo la fa `applica.py` durante la build. Chi traduce non
deve mai scrivere `perche'` a mano — `verifica.py` lo segnala come errore.

Vedi `SPEC.md` §4.

## Note

Progetto gemello: [[Elin - Traduzione Italiana]], da cui derivano metodo e
glossario di partenza.

Questa cartella è anche una nota del vault Obsidian *progetto second brain*: i
documenti sono pensati per essere letti da lì e versionati da qui.
