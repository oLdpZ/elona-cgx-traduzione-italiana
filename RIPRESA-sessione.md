# Ripresa sessione

Aggiornato: 2026-08-07, fine della quinta sessione.

## La prima cosa da fare domani

**Implementare il secondo tipo di sito in `siti()`** — la decisione di
`contratto-nomi.md` §2. È il cambiamento più grosso alla catena dalla Fase 0, e
sblocca tutte e 157 le voci di `rinviate.jsonl`.

`siti()` oggi scandisce solo `lang(jp, en)`. Deve imparare anche questa forma,
che in `db_item.hsp` compare **1.321 volte e sempre uguale** (verificato con una
regex sola, zero eccezioni):

```
if ( jp ) {
    ioriginalnameref(ITEM_ID_BANANA) = "バナナ"
}
else {
    ioriginalnameref(ITEM_ID_BANANA) = "banana"
    ioriginalnameref2(ITEM_ID_BANANA) = ""
}
```

**Il giudice è la prova d'identità.** Un dizionario che traduce ogni nome in sé
stesso deve riprodurre `db_item.hsp` byte per byte, esattamente come già fa per i
26.206 siti `lang()`. Con quella verde, i 1.321 nomi hanno le stesse garanzie di
tutto il resto: firma, `verifica`, coda di ritraduzione di SPEC 3.1.

Attenzione: gli `if ( jp )` in `db_item.hsp` sono **2.902**, ma solo 1.321
riguardano i nomi. Gli altri 1.581 non vanno toccati.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 180 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 26.206, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
```

## Dove siamo

**Il Task 7 è partito e `text.hsp` è al 37%** — 643 firme su 1.740. Quattro
lotti, catena verde a ogni giro, **180 test**. La Fase 1 è per il resto chiusa:
i task 1-6 sono fatti, e il Task 5 (glossario) è stato completato oggi.

- Branch `fase-0`, 13 commit oggi, **niente pushato**
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) sempre
  aperta verso `master`, mai unita
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`), manifesto **72/72 concordi**

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 643 | 1.740 | 37% |
| gli altri cinque | 0 | 4.948 | 0% |

**157 voci rinviate** in `rinviate.jsonl`, ciascuna col suo motivo. Non sono
debito di traduzione: sono la dipendenza dai nomi, che il contratto risolve.

## La scoperta che ha cambiato il piano

**I nomi non sono una conseguenza, sono una premessa.**

Il conteggio delle rinviate è passato da 0 a 35 a 68 a 157 in quattro lotti, e
sempre per lo stesso motivo: la voce citava un nome di creatura o di oggetto.
Quando il motivo del rinvio è sempre lo stesso, non stai accumulando eccezioni —
stai scoprendo una dipendenza che il piano non aveva.

È già successo in questo progetto, con `init.hsp` promosso da Fase 4 a Fase 1. E
il segnale d'allarme più chiaro era una **metrica che stava per mentire**:
`avanzamento.md` avrebbe finito per dire `text.hsp 100%` mentre il giocatore
leggeva nomi inglesi ovunque.

**SPEC §2 è chiuso.** I nomi degli oggetti non erano «altrove»: erano in
`db_item.hsp`, fuori da `lang()`. Vedi `contratto-nomi.md`, che è il documento
nuovo da leggere prima di riprendere.

## Il prezzo dei nomi di creatura — da non dimenticare

`db_creature.hsp` fa `cdatan(CDATAN_NAME, rc) = lang(…)`: **scrive i nomi nel
salvataggio**. Sono la stessa classe di `CDATAN_NEWSEX`, e sono ciò contro cui si
confrontano i **424 `evold`/`evname`** di `action.hsp`.

Vanno quindi tradotti **nello stesso momento** di quelli, mai prima e mai dopo, o
il confronto fallisce **in silenzio**. I nomi delle creature sono un lavoro
atomico, non incrementale.

## Cosa ha insegnato il collaudo in gioco

Fatto il 2026-08-07 con 643 firme tradotte. Il salvataggio esistente carica, e
`Sex Maschio` compare su un personaggio **già creato**: le sei toppe che separano
l'etichetta dall'operando di `CDATAN_NEWSEX` reggono sul caso rischioso.

Due difetti che nessun test poteva prendere:

- **la colonna degli slot taglia a 6 caratteri**, contro un tetto di 13 che avevo
  *dedotto* dalla stringa più lunga del file invece che *misurato* sul campo. La
  regola giusta è in `guida-stile.md`, con una tabella dei tetti misurati;
- **le qualità dell'oggetto escono attaccate al nome** (`a light cloak (Ottima)`),
  non nella frase su cui avevo scelto il femminile. Ora sono invariabili.

Vale la pena averlo fatto adesso: le correzioni hanno toccato 9 voci, a fine file
ne avrebbero toccate centinaia. È la terza volta che il collaudo cambia una regola
in questo progetto.

## I meccanismi, e cosa protegge cosa

| file | cosa dichiara | chi lo legge |
|---|---|---|
| `glossario.md` | rese vincolanti + la regola dei nomi propri | umani |
| `invariati.md` | stringhe che restano inglesi, per sezione classificata | `verifica.py` |
| `rinviate.jsonl` | voci rinviate, con motivo obbligatorio | `estrai --da-tradurre` |
| `toppe.jsonl` | sostituzioni fuori dal dizionario (7 oggi) | `applica.py` |
| `avanzamento.md` | firme tradotte per file, e i rinvii | umani |
| `contratto-nomi.md` | dove stanno i nomi e come si compongono | umani |

⚠️ `carica_invariati` ora **classifica le sezioni e non ha default**: aggiungere
una sezione con valori senza classificarla alza `ValueError`. È voluto — il
difetto che ha corretto nasceva proprio da un'esclusione silenziosa.

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa tutti i 26.206 siti e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 26.206, ambigue 0
```

**Ma non prende tutto.** Le stringhe-dato le attraversa senza accorgersene: lì la
forma resta giusta ed è il significato che si rompe. Contro quelle serve la
lettura, e la ricerca da fare **prima di tradurre un file nuovo** è in
`avanzamento.md` — quella del piano è troppo larga, su `text.hsp` dà 1.187 righe.
La misura che conta è **per firma**: una firma condivisa fra un sito-dato e un
sito-display non si può separare traducendo.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostra **2.31.1.0**: è la costante di versione che il tag non ha
aggiornato al rilascio, non un errore di build. Copia dei salvataggi in
`C:\Games\Elona\save-backup\`.

Artefatto atteso dello stato intermedio: **«colpisces»** nei messaggi di mischia.
`action.hsp:4887` concatena ancora `_s(cc)` dopo il verbo, e quel file non è
tradotto. Sparisce con `action.hsp`.

## Cosa deve esistere fuori dal repo

| percorso | come ottenerlo |
|---|---|
| `C:\Games\Elona\_traduzione\hsp34\` | `hsp34a.zip` da <https://www.onionsoft.net/hsp/file/hsp34a.zip>, estratto **specificando CP932 per i nomi delle voci** |
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch 2.31.2.0 https://github.com/JianmengYu/ElonaPlusCustom-GX.git sorgente` — **il tag, non il branch `work`** |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | SHA-256 dei 72 `.hsp`, una riga `HASH  nome.hsp` per file. ⚠️ **gli hash sono in MAIUSCOLO**: confrontarli case-sensitive dà 0/72 e sembra un disastro |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco.** Per l'integrità
si usa il manifesto, mai `git status`. Vedi `SPEC.md` §2.

Vedi [[terminologia-prima-del-testo]], [[larghezza-per-campo]],
[[stringhe-che-sono-dati]], [[toppe-fuori-dal-dizionario]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
