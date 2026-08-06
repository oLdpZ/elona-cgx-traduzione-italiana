# Elona+ Custom-GX — Traduzione Italiana

Traduzione italiana di **Elona+ Custom-GX 2.31.2.0**, installato in
`C:\Games\Elona\elonaplus2.31\`.

La traduzione è un **dizionario esterno** applicato a un clone pulito del
sorgente CGX al momento della build. Il sorgente upstream non viene mai
modificato.

Stato: **design approvato (`SPEC.md`), Fase 0 non ancora eseguita.**

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
| `strumenti/` | `estrai.py`, `applica.py`, `reimporta.py`, `verifica.py`, `compila.py`, `installa.py` |
| `sorgente/` | clone upstream CGX — git-ignored, ricreabile |
| `dist/` | build italiana installabile |

## Flusso di lavoro

1. `estrai.py` produce un lotto **JSONL** da un intervallo di file del sorgente,
   classificando le stringhe in statiche e dinamiche
2. si traduce il campo `it` di ogni riga del lotto
3. `reimporta.py` valida il lotto e, solo se pulito, lo scrive nel dizionario
4. `verifica.py` controlla interpolazioni, glossario, accenti persi, larghezza UI
5. `applica.py` inietta il dizionario su un clone pulito → albero di build
6. `compila.py` produce `elonapluscgx-it.exe` con l'SDK HSP 3.4
7. `installa.py` copia la build nel gioco, preservando eseguibile inglese e salvataggi
8. prova in gioco, poi aggiornamento di `avanzamento.md` e `RIPRESA-sessione.md`

## Attenzione

**CP932 cancella silenziosamente le vocali accentate** (`perché` → `perche`). È
il rischio primario del progetto e la prima cosa che la Fase 0 deve risolvere.
Vedi `SPEC.md` §4.

## Note

Progetto gemello: [[Elin - Traduzione Italiana]], da cui derivano metodo e
glossario di partenza.

Questa cartella è anche una nota del vault Obsidian *progetto second brain*: i
documenti sono pensati per essere letti da lì e versionati da qui.
