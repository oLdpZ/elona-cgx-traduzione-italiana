# Ripresa sessione

Aggiornato: 2026-08-09, fine della tredicesima sessione.

## La prima cosa da fare

**Il primo lotto della Fase 2: le 378 stringhe del nucleo atomico.** È tutto
pronto — misurato, delimitato, con le guardie in piedi — e non è stata tradotta
nessuna riga. Il lotto è in
`C:\Users\old_p\AppData\Local\Temp\…\scratchpad\nucleo.txt` ma si rigenera in un
comando (vedi «Come si rifà il lotto» più sotto): **non fidarsi dello
scratchpad, che è di sessione.**

⚠️ **Le 378 non entrano in dizionario finché non sono tutte pronte.** Sono
atomiche: 203 vivono in `db_creature.hsp` e 373 in `action.hsp`, e chi entra da
solo rompe la rinomina in silenzio. Si lavora in `lavoro/`, si reimporta alla
fine.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 325 passed, 4 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, in due classi 0
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.605 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `skill.hsp` | **885** | 885 | **100%** ← chiuso oggi |
| `text.hsp` | 721 | 1.740 | 41% |
| gli altri quattro | 0 | 4.063 | 0% |
| **totale Fase 1** | **3.541** | **8.624** | **41%** |

Fuori dalla Fase 1, con conteggio proprio: `db_creature.hsp` (**1.131 nomi** +
320 di voce) e le **2.555 descrizioni d'oggetto** di `db_item.hsp`.

Sette commit oggi, tutti verdi e pushati. **325 test** (erano 318), **254
toppe** (erano 40), prova d'identità **72/72 e 27.813**, **3.694 sostituzioni**
nella build, il compilatore non dice nulla.

**Rinviate: da 120 a 80.** Restano solo i tre motivi vivi — 59 risposte di quiz
che aspettano i nomi di creatura, 20 `elename()` che aspettano `proc.hsp`, e
`<Pants of Ogre>`, che però **oggi si sblocca** (vedi `orc`/`ogre` più sotto).

## Il lavoro di oggi, in quattro pezzi

1. **`skill.hsp` chiuso**, 276 mosse speciali, tetto 24. Collaudato a schermo.
2. **Dieci rinviate riaperte**: quattro risposte del quiz sui grimori (il rinvio
   era a `skill.hsp`) e sei parti meccaniche, la cui dipendenza dichiarata **non
   esisteva**.
3. **I nomi casuali degli oggetti**, 30 voci più **213 toppe generate** che
   ribaltano «aggettivo + nome» in `db_item.hsp`. Collaudato a schermo.
4. **La Fase 2 misurata e disegnata**, senza tradurre niente: è il pezzo lungo
   di questo documento.

## Fase 2 — tutto ciò che serve per cominciare

### La misura

| cosa | dove | quante |
|---|---|---|
| nomi di creatura | `db_creature.hsp` | **1.131** |
| voce delle creature | `db_creature.hsp` | 320 |
| stringhe di evoluzione | `action.hsp`, `evold`/`evname` | **373** |
| **il nucleo atomico, primo lotto** | i due insieme | **378** |

### Le tre cose decise, e perché

**L'articolo sta dentro il nome.** Un array parallelo per `CREATURE_ID` non
funziona: l'id **non cambia** quando la creatura evolve, il nome sì, e
l'articolo resterebbe quello di prima. Perciò lo portano anche `evold` e
`evname`, e il taglio lo sostituisce insieme alla specie.

**La chirurgia si tiene, i nomi si traducono.** Le altre due strade pagavano in
qualità: lasciare i nomi inglesi rinuncia alla superficie più visibile del
gioco, riscrivere il nome intero perde `<Momalaria>` all'evoluzione.

**`orc` → «orco», `ogre` invariato.** Forzata dal lotto, che contiene `orc`,
`king orc`, `orc warrior`. ⚠️ **Sblocca `<Pants of Ogre>`**, l'ultima firma
rinviata di `db_item.hsp` — da chiudere insieme al lotto.

### Le guardie, e cosa hanno già evitato

Quattro test in `strumenti/tests/test_creature.py`, **armati prima del lavoro**.
Due sono reti sotto gli altri due, e sono servite tutte e due:

| guardia | cosa difende |
|---|---|
| `evold` resta agganciato | la rinomina deve continuare ad attaccare in testa **o** in coda |
| ogni nome porta l'articolo | se una sola metà lo dimentica esce un nome senza articolo o con due |
| l'accoppiamento trova tutti gli `evold` | rete: se sbagliasse forma, i due sopra guarderebbero il vuoto |
| il campo è delimitato dal cancello | rete: senza, la prima guardia è impossibile da soddisfare |

⚠️ **Due guardie sono nate sbagliate e le ha corrette la misura, non il
collaudo.** La prima pretendeva che ogni aggancio inglese si conservasse: ma il
taglio non ha controllo di confine di parola, `imp` è prefisso di `impure eye`,
e avrebbe chiesto che «occhio impuro» cominciasse per «folletto». La seconda
pretendeva la concordanza di genere fra `evold` e `evname`, che con l'articolo
dentro il nome **non serve** — e intanto non vedeva il difetto vero.

> Una guardia troppo severa non è prudente: è una guardia che verrà spenta.

### La riparazione già in build

`action.hsp:18644`, ramo del **suffisso** della rinomina: la lunghezza da
tagliare si calcolava su `cdatan(CDATAN_NAME, rc)` invece che su `tc`, mentre le
altre tre occorrenze della riga dicono `tc`. `rc` non è assegnato né in
`*act_use` né in `*charaRefresh`: portava la lunghezza del nome di un'**altra**
creatura. Difetto di upstream, non della traduzione — l'inglese quasi non lo
incontra perché usa il ramo del prefisso.

⚠️ **Va collaudato in gioco su un'evoluzione vera**, ed è l'unica cosa della
Fase 2 già nell'eseguibile.

⚠️ **Servono tutti e due i rami**, e il ramo che scatta cambia fra le lingue:
`lesser mummy` aggancia `mummy` in coda, «la mummia minore» lo aggancia in
testa, perché l'italiano mette la specie davanti.

### Come si rifà il lotto

```powershell
python -m strumenti.estrai db_creature.hsp --uscita lavoro/creature-grezzo.jsonl
python -m strumenti.estrai action.hsp --uscita lavoro/action-grezzo.jsonl
```

poi si filtra sull'unione di `evoluzioni()` e `nomi_visibili()` di
`strumenti/creature.py`, che è esattamente il nucleo atomico. `creature.py`
classifica anche nome contro voce, e `--classe nome --uscita …` scrive il lotto
degli altri ~750 nomi, quelli fuori dal nucleo.

### L'ordine che resta

1. tradurre le **378** del nucleo, con l'articolo dentro, in `lavoro/`;
2. reimportare **tutto insieme**, mai a metà;
3. chiudere `<Pants of Ogre>` con «orco»;
4. collaudo in gioco **su un salvataggio nuovo** — è l'unico dove la rinomina
   può attaccare, perché un salvataggio vecchio contiene i nomi inglesi;
5. gli altri ~750 nomi, a lotti per **razza** (`dbidn` prima di `*db_race`: 76
   razze, da `norland` con 91 a quelle da una); poi le 320 di voce;
6. le **59 rinviate** del quiz, che si sbloccano solo dopo.

⚠️ Su un salvataggio esistente l'evoluzione **funziona** — statistiche, stadio,
grafica — e fallisce **solo la rinomina**. È un difetto estetico permanente, non
un sistema rotto: il contratto diceva il contrario ed è stato corretto oggi.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce con «Device or resource busy» se il gioco è aperto.
Al primo avvio esce «Invalid screen resolution»: si dà OK e si prosegue.
Il titolo mostra 2.31.1.0: è la costante di versione, non un errore di build.

⚠️ L'utente **preferisce una lista di passi da eseguire lui** al collaudo
pilotato da qui. Dargli la tabella, con l'esito atteso di ogni riga.

## Cosa rifare a ogni giro

```powershell
python -m strumenti.prova_identita        # 72/72, 27.813, ambigue 0
python -m strumenti.genera_toppe_nomi     # 32 generate, tutte «ok»
python -m strumenti.genera_toppe_casuali  # 213 generate, tutte «ok»
```

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è
permanentemente sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp` — oggi è solo `custom_tweaks.hsp`, ma è un file
di *tweak* e cresce a ogni rilascio.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

Il 24 è stato **confermato a schermo** oggi: `<Serba/libera la forza>` è 23
caratteri e non tocca la colonna del costo.

Vedi [[una-guardia-agganciata-a-se-stessa]], [[larghezza-per-campo]],
[[ultima-scrittura-vince]], [[percentuale-senza-denominatore]],
[[una-procura-non-e-una-proprieta]], [[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]] e
[[cp932-perdite-silenziose]].
