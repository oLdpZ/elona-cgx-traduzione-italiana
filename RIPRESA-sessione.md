# Ripresa sessione

Aggiornato: 2026-08-10, fine della diciottesima sessione.

## La prima cosa da fare

**Il collaudo dei nomi è stato fatto** e ha trovato due difetti, entrambi
riparati. Il debito grosso della sessione scorsa è chiuso. Il prossimo passo non
è una scelta: è **finire `action.hsp`**, dove restano 889 firme (292 dinamiche +
597 statiche) e il modello è ormai fissato.

⚠️ **Una cosa resta non provata in gioco**, ed è la più importante: le **379
rinomine all'evoluzione riparate**. La lettura del sorgente dice che ora il
confronto combacia, ma è una deduzione, non una prova — e questo progetto ha già
visto una deduzione ribaltarsi a schermo. Vedi «Per rifare la prova in gioco».

### Le quattro verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 338 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
```

I test sono **338**, non più 336: due nuovi sulla regola della morfologia
annidata, vedi sotto.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `text.hsp` | 780 | 1.740 | 45% |
| `action.hsp` | 399 | 1.288 | 31% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **4.000** | **8.624** | **46%** |

Fuori dalla Fase 1: `db_creature.hsp` a **1.452 firme su 3.655** — i 1.131 nomi,
l'epiteto e le 320 stringhe di voce.

⚠️ **Tre file sono entrati nel perimetro** il 2026-08-10, e non erano nel piano:
`custom_enemyevolution.hsp` (368 firme, **chiuso al 100%**), `ai.hsp` (6 su 100),
`event.hsp` (5 su 654). Perché, sta qui sotto.

**338 test**, prova d'identità **72/72 e 27.813**, **7.596 sostituzioni** nella
build, il compilatore non dice nulla.

## Le tre cose che questa sessione ha cambiato nel metodo

### 1. Un difetto può stare **fra** due file, e nessuna guardia lo vede

La rinomina all'evoluzione confronta il nome memorizzato con un letterale del
sorgente. In `action.hsp` quel letterale è tradotto; in
`custom_enemyevolution.hsp`, `ai.hsp` ed `event.hsp` — **fuori dal perimetro** —
era rimasto inglese. Il confronto non combaciava più: **440 rinomine morte**, in
silenzio, con tutte le guardie verdi. Il nemico evolve e tiene il nome di prima.

Riparato: 379 firme uniche, **tutte risolte cercando il giapponese** nel
dizionario esistente, zero ambigue. Concetto:
[[coerenza-fra-due-file-uno-solo-tracciato]].

> La domanda da rifare a ogni lotto: **chi altro, fuori dal perimetro, dipende
> da un valore che dentro ho cambiato?** Si risponde con una ricerca per
> contenuto su tutto il sorgente, non per nome di file.

### 2. Il testo giusto non basta: conta **dove viene stampato**

`custom_dmgpop.hsp:237` applicava il *title case* inglese agli epiteti —
`L'investigatrice Della Gilda Dei Guerrieri` — con una chiamata cablata a mano
che scavalcava l'opzione del gioco. Il dizionario era corretto; la deformazione
avveniva a valle, dove nessuna guardia sul testo può guardare. Toppa 255ª.

Sospetti abituali da controllare: `capitalize`, `strmid` a larghezza fissa,
suffissi di plurale, articoli, allineamenti.

### 3. Una guardia che nessuna resa può soddisfare è **la guardia** a essere rotta

`verifica.py` contava come contenuto anche ciò che sta **dentro** una chiamata di
morfologia inglese. In `name(gdata(R)) + is(gdata(R)) + " using it."` il secondo
`gdata` serve solo alla copula; togliere `is()` — obbligatorio — lo porta via, e
nessuna traduzione italiana corretta poteva passare.

Corretto `strumenti/funzioni.py` (`_classifica` salta gli argomenti della
morfologia) sul criterio verificato che **una funzione di grammatica non stampa
mai ciò che riceve**. ⚠️ Ha fatto cadere **due test esistenti**, riletti per il
loro obiettivo dichiarato e corretti nelle asserzioni incidentali; due test nuovi
per la regola. Se la decisione non convince, si torna indietro in un commit — ma
allora quelle voci restano intraducibili. Vedi [[guardia-troppo-severa]].

## Il metodo per `action.hsp`, ormai fissato

Le dinamiche sono espressioni HSP intere da riscrivere, non stringhe.

```powershell
python -m strumenti.estrai action.hsp --da-tradurre --uscita lavoro/<lotto>.jsonl
# ... si traduce ...
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

Le tre regole che governano ogni resa dinamica:

1. **Terza persona, sempre.** `name(giocatore)` è «il viandante» (toppa su
   `init.hsp`), quindi «perde la pazienza» regge per il giocatore e per il putit.
2. **Mai `_s()`, `is()`, `was()`, `your()`, `have()`, `does()`, `yourself()`.**
   Non passano da `lang()`: resterebbero inglesi dentro la frase italiana. La
   frase si riscrive, non si rattoppa.
3. **Mai una preposizione davanti a `name()` o `itemname()`** — portano già
   l'articolo, e HSP non fonde: `" di " + name(tc)` esce «di il putit». Criterio
   e ricerca da rifare a ogni lotto in `guida-stile.md:212`.

⚠️ **`«mordes»` è localizzato**: `action.hsp:4887`, dove `_melee(0, ...)` è già
tradotto «morde» in `text.hsp:164` e `_s(cc)` gli attacca la «s». Sparisce
quando si traduce quella riga. Il gemello è in `proc.hsp:8797`, lo stesso file su
cui puntano le **20 rinviate** rimaste: i due si chiudono insieme.

## Le cose da non riscoprire

### Un nome già preso non si può riusare — **e vale anche per le esche**

La regola era nota per i nomi di creatura. Questa sessione l'ha estesa: il quiz
«quale segugio ha il nome esatto» offre un vero e tre falsi, e il falso
`混沌ハウンド` sarebbe diventato «il segugio del caos» — che `カオスハウンド`
**ha già**. Due opzioni identiche, e la domanda non ha più risposta.

> Prima di scegliere una resa, cercarla in dizionario. Vale per i nomi veri e
> per quelli inventati.

### Il giapponese arbitra, e sulle voci l'inglese **inventa**

Sulle 320 stringhe di voce l'inglese non abbrevia: aggiunge frasi che nel
giapponese non esistono (`「ガルルル…」`, un ringhio, diventa «You hear the near
silent footfalls of a cat»). E due volte capovolge il senso: `あの男`
(*quell'uomo*) → «that girl»; `トドメを刺した` (*colpo di grazia*) → «tormented».

### La carta dice cosa la creatura rappresenta, il blocco cosa è

Invariato dalla sedicesima sessione. `db_card.hsp`, `cardrefskill`, poche righe
sopra il `cardrefn`. Dà anche il sesso, e tiene insieme le famiglie. ⚠️ Tre carte
inglesi sono sbagliate nel sorgente (`db_card.hsp:4131`, `9643`, `7017`): il
giapponese è sempre corretto.

### L'articolo sta sulla testa del sintagma, non sulla persona

Sesso dichiarato → si concorda; sesso casuale → sostantivo il cui articolo non
dipende dalla persona. ⚠️ `/man/` non è il sesso: è `DBSPEC_CHARA_FILTER`.

### `ドレイク` è «draco» — **confermato a schermo**

Non è più una decisione revisionabile: i tre draco sono stati guardati accanto a
`<Vansesda> il drago della fiamma primordiale` e non si confondono.

## L'ordine che resta

1. **`action.hsp`**: 292 dinamiche + 597 statiche;
2. `text.hsp` dal 45% in su;
3. `proc.hsp` — chiude le 20 rinviate e il gemello di «mordes»;
4. `command.hsp`, `trait.hsp`;
5. `ai.hsp` (94) ed `event.hsp` (649), ora nel perimetro;
6. le 2.203 righe rimanenti di `db_creature.hsp` e le 2.555 descrizioni
   d'oggetto di `db_item.hsp`.

⚠️ **`chara_func.hsp` non è nel perimetro, ma il quiz ne ha già fissato quattro
nomi.** Le tre pietre di Lesimas e l'ankh del sole si ottengono lì
(`chara_func.hsp:7347-7448`) e la tabella EN→IT è in `glossario.md`: quando il
file entrerà, quelle rese si copiano, non si reinventano. Finché non entra, il
giocatore riceve `[Sage's Magic Stone]` in inglese e la ritrova in italiano nel
quiz.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp` — oggi è solo `custom_tweaks.hsp`, ma è un file
di *tweak* e cresce a ogni rilascio. **E adesso anche**: cercare chi copia nomi
di creatura fuori da `db_creature.hsp`, che è il difetto delle 440 rinomine.

⚠️ **CP932 non codifica tutto.** Niente `«»` (si usano le tipografiche `“”`),
niente dieresi tedesche, niente `å`. Gli accenti veri si scrivono nel dizionario
e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine parola è
gratis, a metà no («dèi» → `de'i`). Il controllo copre ora **tutti** i campi di
testo, incluso `plurale`, che è separato dal singolare.

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce se il gioco è aperto. ⚠️ Se `applica` viene interrotta da un
blocco di file lascia l'albero di build **incompleto**, e `compila` poi dice
«main.hsp non è in ...»: si rilancia `applica` e basta.

### La console di debug — la nota che ha fatto perdere tempo

**La console parte in modalità HSP, non Lua.** `characreate` è il nome Lua e
risponde «comando sconosciuto» finché non si digita `lua` da solo. Ma non serve:

```
spawn_chara <id>
```

è il comando nativo (`system.hsp:4831`), sta **fuori** dall'`#ifdef
CUSTOM_GX_LUA` e quindi funziona anche in **`cgx-test.exe`**, che è
l'eseguibile che si spedisce — meglio collaudare quello. Genera la creatura
sulla casella del giocatore e risponde `Done. (<indice>)`.

`cgx-lua.exe` serve solo per scrivere i campi che il gioco non espone. Va
ricostruito quando cambia il dizionario (`main.hsp:9`, si scommenta in BUILD e
si ripristina subito); serve `hsplua.dll`, già copiata. Con `lua` attivo:

```lua
return cdata[27][N]   -- l'ID della creatura N (CDATA_ID)
return cdatan[0][N]   -- il suo nome (CDATAN_NAME)
return cdata[17][2]   -- impressione dell'alleato 2, serve >= 150
```

⚠️ **Un difetto riferito va verificato come uno trovato.** In questa sessione
`spawn_chara 659` sembrava produrre un ratto: le ID erano corrette e il ratto era
un mostro già sulla mappa. La lista di passi fa entrare prove che il codice non
sa dare, ma non tutto ciò che arriva da lì è un difetto.

⚠️ **Serve un salvataggio nuovo** per i nomi e un **personaggio nuovo** per
l'epiteto: la rinomina all'evoluzione è una sostituzione di stringa sul nome nel
salvataggio, quindi un alleato reclutato con l'exe non tradotto non combacia con
`evold` e non viene rinominato affatto.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati** (`action.hsp`): provata il 2026-08-10,
  `Norfor il cavallo zoppo` → `Norfor l'unicorno`.
- ✅ **I nomi a schermo**: provati, ed è così che è uscito il title case.
- ✅ **«draco»**: confermato guardandolo accanto a «drago».
- ❌ **L'evoluzione dei nemici** (`custom_enemyevolution.hsp`): **mai vista**.
  È la prova che manca. Si mette *Spawn evolved enemies* su **always** nelle
  opzioni Custom-GX e si entra in una Nefia: i nemici evoluti devono uscire col
  **nome evoluto**. Prima di questa sessione uscivano col nome base.
- ⚠️ **Il non tradotto esce in inglese, non in giapponese**: `applica` sostituisce
  nello slot inglese e il gioco gira in inglese. Atteso fino a `action.hsp`.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` (è `skillname`, non un nome di creatura) |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

⚠️ Il nome di creatura compare in messaggi **senza limite**, e i tetti qui sopra
non lo coprono. Il più lungo del dizionario è `<Ratin> l'investigatrice della
Gilda dei Guerrieri`, 50 caratteri: visto a schermo, non tronca.

Vedi [[coerenza-fra-due-file-uno-solo-tracciato]], [[guardia-troppo-severa]],
[[toppe-fuori-dal-dizionario]], [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[larghezza-per-campo]], [[ultima-scrittura-vince]],
[[percentuale-senza-denominatore]], [[una-procura-non-e-una-proprieta]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
