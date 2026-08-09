# Ripresa sessione

Aggiornato: 2026-08-09, fine della dodicesima sessione.

## La prima cosa da fare

**Il collaudo in gioco delle 519 stringhe entrate oggi.** Nessuna è stata vista
a schermo. Non è prudenza generica: **due dei tre difetti trovati oggi li ha
trovati il collaudo**, e nessuno dei due sarebbe mai uscito dai test.

La build è pronta: `C:\Games\Elona\elonaplus2.31\cgx-test.exe`, delle 17:07.

| cosa guardare | dove | cosa deve uscire |
|---|---|---|
| **gradi di resistenza** | `a` → pagina delle resistenze | `Scarsa`, `Debolezza` **staccati** dal nome. Era il difetto di stamattina, già collaudato una volta e passato: serve la controprova dopo gli altri lotti |
| descrizioni delle abilità | `a`, pagine 1-3 | «Abilità con le asce.», «Rimargina le ferite col tempo.» — italiano, non più inglese |
| **le quattro resistenze riscritte** | `a`, resistenze | ⚠️ `Fulmine`, `Mente`, `Nervi`, `Caos` passano da `custom_tweaks.hsp`. Se **queste quattro** sono inglesi e le altre italiane, la toppa non ha preso |
| nomi d'incantesimo | `Z` o il libro degli incantesimi | «Saetta di gelo», «Dardo magico», «Tasca quadridimensionale» |
| **larghezza dei nomi** | lista incantesimi, colonna `Cost` | ⚠️ nessun nome deve toccare il costo. «Tasca quadridimensionale» è **esattamente** al tetto di 24: è la riga da guardare |
| mosse speciali | il menù delle mosse | descrizioni in italiano, **nomi ancora inglesi** (sono i 276 che restano) |
| `<Serba/libera la forza>` | menù mosse speciali | il nome della mossa della barra, se il tweak è attivo |

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 318 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.605 | 1.606 | **100%** ⚠️ vedi sotto |
| `item_data.hsp` | 318 | 318 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `skill.hsp` | **618** | 885 | **70%** |
| `text.hsp` | 681 | 1.740 | 39% |
| gli altri quattro | 0 | 4.063 | 0% |
| **totale** | **3.234** | **8.612** | **37,6%** |

Cinque commit oggi, tutti verdi, **tutti pushati**. Branch `fase-0` allineato con
`origin`, [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1)
sempre aperta. Sorgente pinnato al tag `2.31.2.0`, manifesto 72/72.

**318 test**, prova d'identità **72/72, 27.813 sostituzioni**, **3.370
sostituzioni nella build** (erano 2.851 stamattina), **40 toppe**, il compilatore
non dice nulla.

⚠️ **`db_item.hsp` al 100% è il 100% dei suoi siti di nome.** Il file contiene
anche **2.555 descrizioni d'oggetto**, ~64.000 parole, che non stanno nelle
8.612 e **si vedono in gioco**. Sono Fase 3, con un conteggio proprio: vedi
`SPEC.md` §2.1.

## Le tre cose imparate oggi

### Un campo ancorato a destra non tronca: invade

```hsp
command.hsp:11002   pos wx + 280 - strlen(s) * 7    ; i gradi di resistenza
command.hsp:10893   x = 54                          ; da dove parte il nome
```

Non ha un tetto: cresce verso sinistra finché non copre il vicino.

> Il difetto **non appare nel campo lungo, appare in quello di fianco** — e
> nessun controllo che guardi una stringa alla volta può vederlo.

Concetto: [[larghezza-per-campo]], aggiornato.

### Una traduzione giusta che non si vede mai

`custom_tweaks.hsp` riassegna sei chiavi di `skill.hsp` dopo di lui, per
applicare le opzioni. **Vince l'ultima scrittura.**

> Una firma garantisce **dove** hai scritto, non **cosa** legge il gioco.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`. Oggi è solo `custom_tweaks.hsp`, ma è un file
di *tweak* e cresce a ogni rilascio. La ricerca è meccanica — una regex
sull'assegnazione su tutti i file, e un confronto d'insiemi.

Concetto: [[ultima-scrittura-vince]], nuovo.

### Una percentuale senza denominatore

L'indizio delle 2.555 descrizioni era scritto da giorni: «gli altri 1.581
`if ( jp )` non riguardano i nomi». Nessuno aveva guardato **cosa** fossero.

> «Gli altri N non ci interessano» è una frase che chiude un'indagine senza
> concluderla. Va trattata come debito.

Concetto: [[percentuale-senza-denominatore]], nuovo.

## Le regole nuove per tradurre

**Gli atomi vincono sulle voci.** Le 348 etichette di `skilldesc` si traducono
per famiglia, non una per una — `Surround` compare quattordici volte. Gli atomi
stanno in `glossario.md`, sezione «Gli atomi delle etichette di `skilldesc`».

**Il lotto si chiava sull'indice, non sull'inglese.** Sette stringhe inglesi si
ripetono con un giapponese diverso (due `Create mist` sono «nebbia fitta» e
«nebbia abbagliante»). Una mappa `en → it` le fonde **in silenzio**, e ogni
firma risulta comunque tradotta.

**Il giapponese scioglie le sigle.** `CON`/`END` sono entrambe 耐久, `CHA`/`CHR`
entrambe 魅力: in italiano una resa sola, **Cos** e **Car**. E tre `skilldesc`
inglesi sono letteralmente `?` — buchi mai chiusi a monte, resi dal giapponese.

**L'accento a metà parola degrada male.** «dèi» → `de'i`, apostrofo dentro la
parola. Quelli finali («Abilità» → `Abilita'`) sono invisibili.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

⚠️ **Il 24 corregge il «~29» scritto ieri.** A `wx+288` arriva **il costo**, non
il nome: `"12 Sp"` sono 35 px. Misurare due `pos` non basta — bisogna sapere chi
occupa lo spazio in mezzo.

## Cosa resta, in ordine

1. **il collaudo in gioco** delle 519 di oggi (tabella in cima)
2. **le 276 mosse speciali** di `skill.hsp`, ultimo blocco del file. Tetto **24**,
   già misurato, e sono il blocco più rischioso: nomi inventati, sigle, e
   l'inglese arriva già a 24 (`Critical Particle Cannon`)
3. le **119 voci rinviate** di `text.hsp`, di cui 30 sono i nomi casuali
4. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
   di `action.hsp`, mai prima e mai dopo (§5 di `contratto-nomi.md`)
5. la **Fase 3**: le 2.555 descrizioni d'oggetto, non prima di aver chiuso
   `skill.hsp`

## Il prezzo dei nomi di creatura — da non dimenticare

`db_creature.hsp` fa `cdatan(CDATAN_NAME, rc) = lang(…)`: **scrive i nomi nel
salvataggio**. Sono la stessa classe di `CDATAN_NEWSEX`, e sono ciò contro cui
si confrontano i **424 `evold`/`evname`** di `action.hsp`. Vanno tradotti nello
stesso momento di quelli, o il confronto fallisce **in silenzio**.

⚠️ `<Pants of Ogre>` aspetta quella decisione: in `db_creature.hsp` **`orc` e
`ogre` convivono**, quindi «orco» non può coprirle entrambe.

## Il disegno dei nomi, in una riga

> Il **plurale** e il **genere** sono dati, perché l'italiano non li deduce.
> L'**articolo** no: è una derivata del genere, e la calcola `strumenti/articolo.py`.

I quattro generi sono `m`, `f`, `mp`, `fp`: il **numero fa parte del dato**.

⚠️ **Le parole-contatore cablate vincono sull'articolo dell'array**: «un paio di
stivali pesanti», non «degli stivali pesanti».

⚠️ **I due campi possono dire cose diverse, ed è voluto.** `unicorn horn` è `m`
con plurale «corna»; `bone` è `m` con «ossa»; `egg` è `m` con «uova».

```
articolo + nome + s6 (materiale) + s10 (ego) + s7 (stato)
→ «un paio di scarpe di vetro di fuoco con benedizione»
```

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa **tutti e 72 i file** — non quelli che
traduciamo (`prova_identita.py:84` fa `radice.glob("*.hsp")`) — e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 27.813, ambigue 0
```

⚠️ **Non giudica le toppe**, che girano dopo in un giro loro. Il loro guardiano è
la regola «esiste esatto e una volta sola», più il compilatore, **più il collaudo
in gioco**. E non giudica **chi riscrive dopo**: quello è un controllo a parte,
vedi [[ultima-scrittura-vince]].

**Il generatore delle toppe** è il primo comando da rilanciare quando arriva una
versione CGX nuova:

```powershell
python -m strumenti.genera_toppe_nomi   # atteso: 32 generate, tutte «ok»
```

⚠️ Le toppe **degradano gli accenti da sole**: sono l'unica strada per cui un
testo italiano arriva al sorgente senza passare da `applica.py`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ **La copia fallisce con «Device or resource busy» se il gioco è aperto.**
Chiuderlo prima.

Il titolo mostra **2.31.1.0**: è la costante di versione che il tag non ha
aggiornato al rilascio, non un errore di build. Al primo avvio esce «Invalid
screen resolution»: si dà OK e si prosegue.

Il personaggio che cammina da solo era `joypad. "1"` nel `config.txt` del gioco.
Cura già applicata: `joypad. "0"`, backup in `config.txt.bak-prima-joypad0`.

⚠️ L'utente **preferisce una lista di passi da eseguire lui** al collaudo
pilotato da qui (`collaudo/schermo.ps1`, che è lento). Dargli la tabella, con
l'esito atteso di ogni riga.

## Cosa deve esistere fuori dal repo

| percorso | come ottenerlo |
|---|---|
| `C:\Games\Elona\_traduzione\hsp34\` | `hsp34a.zip` da <https://www.onionsoft.net/hsp/file/hsp34a.zip>, estratto **specificando CP932 per i nomi delle voci** |
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch 2.31.2.0 https://github.com/JianmengYu/ElonaPlusCustom-GX.git sorgente` — **il tag, non il branch `work`** |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | SHA-256 dei 72 `.hsp`. ⚠️ **gli hash sono in MAIUSCOLO**: confrontarli case-sensitive dà 0/72 e sembra un disastro |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

⚠️ I file `.hsp` stanno in `sorgente\2.05-custom-gx\`, non nella radice del clone.

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco.** Per l'integrità
si usa il manifesto, mai `git status`. Vedi `SPEC.md` §2.

Vedi [[terminologia-prima-del-testo]], [[larghezza-per-campo]],
[[ultima-scrittura-vince]], [[percentuale-senza-denominatore]],
[[stringhe-che-sono-dati]], [[toppe-fuori-dal-dizionario]],
[[dato-o-derivata]], [[plurale-e-un-dato-non-una-regola]],
[[toppe-generate-dal-sorgente]], [[genere-ignoto-si-risolve-col-complemento]],
[[stessa-forma-va-verificata-nel-codice]],
[[la-categoria-che-il-sorgente-dichiara]], [[registro-e-segmento]],
[[una-procura-non-e-una-proprieta]], [[il-posto-decide-quando-arriva-il-dato]],
[[una-parola-due-domande]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
