# Ripresa sessione

Aggiornato: 2026-08-09, fine dell'undicesima sessione.

## La prima cosa da fare

**Il collaudo in gioco** di tutto ciò che è entrato oggi, che è molto e di cui
si è visto a schermo solo il primo pezzo. La build è pronta:
`C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

| cosa guardare | dove | cosa deve uscire |
|---|---|---|
| ego degli oggetti | arma o armatura non identificata di qualità alta | «un paio di scarpe **di vetro di fuoco**» — materiale attaccato al nome, ego dopo |
| pesci | canna da pesca, poi l'inventario | «**una** carpa», «**uno** scorfano», su pila «**2 carpe**» |
| spazzatura pescata | idem | «una lattina vuota», «**degli** stivali bucati» |
| incantamenti | scheda di un oggetto identificato (`i`) | «**Infligge danni ingenti ai draghi.**» — maiuscola, **senza** «It» davanti |
| nomi di abilità | lista abilità (`a`) | «Corazza», «Intuito», «Spada», «Daga» in italiano; descrizioni ancora inglesi |
| **il campo da 6** | traccia **Corazza** e **Maglia** sull'HUD | devono distinguersi: è il campo che ha deciso tutto il lotto |
| incantamenti + abilità | scheda di un oggetto incantato | «**Aumenta Forza di 3.**», che stamattina era «increases your Strength by 3» |

Le due correzioni della mattina sono già state collaudate e sono uscite giuste:
«uno shuriken», «stivali pesanti **d'osso**», «cintura **d'argento**».

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 318 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
```

## Dove siamo

**Due file completi.** `db_item.hsp` 1.605/1.606 (l'unica mancante è
`<Pants of Ogre>`, **rinviata**), e da oggi `item_data.hsp` **318/318, senza
nemmeno un rinvio**. `skill.hsp` è entrato oggi: 111 su 885.

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.605 | 1.606 | **100%** |
| `item_data.hsp` | **318** | 318 | **100%** |
| `skill.hsp` | 111 | 885 | 13% |
| `text.hsp` | 681 | 1.740 | 39% |
| gli altri quattro | 0 | 4.063 | 0% |
| **totale** | **2.715** | **8.612** | **32%** |

Otto commit oggi, tutti verdi, **tutti pushati**. Branch `fase-0` allineato con
`origin`, [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1)
sempre aperta. Sorgente pinnato al tag `2.31.2.0`, manifesto 72/72.

**318 test** (erano 297), prova d'identità **72/72, 27.813 sostituzioni**,
**2.851 sostituzioni nella build** (erano 2.505), **40 toppe**, il compilatore
non dice nulla.

## Le due cose imparate oggi che valgono più di tutte

### Il posto decide se il dato arriva in tempo

`ioriginalnameref(ITEM_ID_FISH)` è la **stringa vuota**. Il nome della specie
non è un pezzo del nome dell'oggetto: è *tutto* il nome, e arriva da
`itemNameSub` (`item_func.hsp:997`), che gira a riga 1936 — cioè **dopo** che
l'articolo è stato messo davanti e dopo che il plurale è stato scelto.

Tradurre i 113 nomi e basta avrebbe dato «**a salmone**». E nessun test lo
avrebbe visto: `verifica` chiede genere e plurale solo alle voci che
**dichiarano un array**, e i pesci non lo dichiaravano.

> Prima di tradurre un nome si guarda **dove** il gioco lo mette. Il posto
> decide se i dati che porta arrivano in tempo.

Concetto: [[il-posto-decide-quando-arriva-il-dato]].

### Il budget di un campo si calcola, non si indovina

Prima di tradurre `skillname` ho misurato i campi invece di dedurli:

| campo | dove | larghezza |
|---|---|---|
| tracciatore HUD | `screen.hsp:2002` | **6 caratteri** |
| razza e classe | `chara.hsp:4679` | **3 caratteri** |
| lista abilità, nome | `command.hsp:5383` | ~29 caratteri |
| lista abilità, descrizione | `command.hsp:5389` | 34 caratteri |

Il 6 non è arbitrario: nome a `pos 16`, valore a `pos 66` = 50 px, e il sorgente
stesso assume 7 px/carattere (`command.hsp:5385` fa `288 - strlen(s) * 7`).
50/7 = 7,14.

⚠️ **In italiano il rischio è strutturale**: l'inglese antepone il
qualificatore, l'italiano lo posticipa, e in un campo stretto la parte che
distingue esce dalla finestra. Quattro famiglie collidevano. La cura è **testa
diversa invece di nome + aggettivo**, e due volte su quattro la testa diversa
era anche più fedele al giapponese.

Concetto: [[larghezza-per-campo]], aggiornato oggi.

## Le altre quattro, più corte

### Prima di scegliere la forma di una frase si contano i posti da cui esce

La descrizione d'incantamento esce da **quattro** siti e solo uno le mette un
soggetto davanti (`command.hsp:16405`, `lang("それは", "It ") + s`). Le rese sono
quindi **verbi alla terza persona senza soggetto**, e il prefisso si spegne con
una toppa a mano — `command.hsp` non è fra i file estratti.

### La stessa cura, tre cose ignote diverse

«Non accordarsi con ciò che non si conosce» ha scelto la forma tre volte oggi, e
ogni volta l'ignoto era un altro: il genere dell'**oggetto** (ego), quello
dell'**abilità** (`"deals X damage."`), quello del **giocatore**
(`skillencdesc`, dove «ti rende letterato» si accorderebbe con chi gioca).

### La `h` muta non rende pura la `s` impura

`articolo.py` teneva la `h` fra le vocali — giusto, per «l'hotel» — ma la stessa
costante rispondeva anche a «la lettera dopo la `s` è una consonante?». Per `sh`
le due domande danno risposte opposte: usciva «un shuriken».

> Due domande che si somigliano non sono la stessa domanda. Il caso dove si
> separano è raro per costruzione, e lo trova il collaudo, non i test.

Concetto: [[una-parola-due-domande]].

### Il giunto del materiale non è uno solo: sette elidono

« di » era cablato nella toppa, e lì deve restare (`command.hsp` legge `mtname`
nudo). Ma una preposizione sola non copre 38 materiali: sette cominciano per
vocale. Terza via, già usata per plurale e articolo: **`mtcomplemento`**, array
italiano accanto a quello inglese col complemento già montato.

## Cosa resta, in ordine

1. **il collaudo in gioco** di oggi (tabella in cima)
2. **`skill.hsp`**, 774 voci in tre blocchi:
   - `skilldesc` **415** — finestra di 34 caratteri, e 41 originali la sforano
     già: non è un tetto, è la finestra, e i primi 34 devono portare il senso
   - incantesimi **90** e mosse speciali **271** — questi ultimi a larghezza
     compressa, vedi `decisioni.md` §quinta sessione
3. le **119 voci rinviate** di `text.hsp`, di cui 30 sono i nomi casuali
4. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
   di `action.hsp`, mai prima e mai dopo (§5 di `contratto-nomi.md`)

⚠️ Prima di attaccare gli incantesimi e le mosse speciali: **misurare i loro
campi**, come fatto oggi per `skillname`. Il taglio a 6 è quello del
tracciatore; le mosse speciali escono altrove e hanno vincoli loro.

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

L'ordine in cui il nome si monta, dopo oggi:

```
articolo + nome + s6 (materiale) + s10 (ego) + s7 (stato)
→ «un paio di scarpe di vetro di fuoco con benedizione»
```

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa tutti i 27.813 siti e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 27.813, ambigue 0
```

⚠️ **Non giudica le toppe**, che girano dopo in un giro loro. Il loro guardiano è
la regola «esiste esatto e una volta sola», più il compilatore, **più il collaudo
in gioco**.

**Il generatore delle toppe** è il primo comando da rilanciare quando arriva una
versione CGX nuova:

```powershell
python -m strumenti.genera_toppe_nomi   # atteso: 32 generate, tutte «ok»
```

⚠️ Da oggi le toppe **degradano gli accenti da sole**: sono l'unica strada per
cui un testo italiano arriva al sorgente senza passare da `applica.py`. Un test
lo pretende per tutte — «bambù» faceva esplodere la scrittura dell'albero di
build, in fondo alla catena.

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

### Il personaggio che cammina da solo — risolto il 2026-08-09

`config.txt` del gioco aveva `joypad. "1"`, e nella macchina ci sono pad
virtuali. **Cura: `joypad. "0"`** in `C:\Games\Elona\elonaplus2.31\config.txt`,
già applicata. Backup in `config.txt.bak-prima-joypad0`.

### Il gioco si può pilotare da qui

`collaudo/schermo.ps1`. ⚠️ È **lento**, e l'utente preferisce una lista di passi
da eseguire lui. Conviene solo se non c'è nessuno a giocare.

## Cosa deve esistere fuori dal repo

| percorso | come ottenerlo |
|---|---|
| `C:\Games\Elona\_traduzione\hsp34\` | `hsp34a.zip` da <https://www.onionsoft.net/hsp/file/hsp34a.zip>, estratto **specificando CP932 per i nomi delle voci** |
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch 2.31.2.0 https://github.com/JianmengYu/ElonaPlusCustom-GX.git sorgente` — **il tag, non il branch `work`** |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | SHA-256 dei 72 `.hsp`. ⚠️ **gli hash sono in MAIUSCOLO**: confrontarli case-sensitive dà 0/72 e sembra un disastro |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco.** Per l'integrità
si usa il manifesto, mai `git status`. Vedi `SPEC.md` §2.

Vedi [[terminologia-prima-del-testo]], [[larghezza-per-campo]],
[[stringhe-che-sono-dati]], [[toppe-fuori-dal-dizionario]],
[[dato-o-derivata]], [[plurale-e-un-dato-non-una-regola]],
[[toppe-generate-dal-sorgente]], [[genere-ignoto-si-risolve-col-complemento]],
[[stessa-forma-va-verificata-nel-codice]],
[[la-categoria-che-il-sorgente-dichiara]], [[registro-e-segmento]],
[[una-procura-non-e-una-proprieta]], [[il-posto-decide-quando-arriva-il-dato]],
[[una-parola-due-domande]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
