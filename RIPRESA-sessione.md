# Ripresa sessione

Aggiornato: 2026-08-10, fine della diciassettesima sessione.

## La prima cosa da fare

**I 1.131 nomi di creatura sono finiti.** `--razze` dice «restano 0 firme in 0
razze». Il lavoro dei nomi è chiuso e il prossimo passo è **una scelta**, non
una continuazione:

1. **le 320 firme di voce** di `db_creature.hsp` — stessa catena, stesso
   strumento, `python -m strumenti.creature --classe voce`;
2. **le 59 rinviate del quiz**, che i nomi hanno appena sbloccato e che si
   chiudono col loro lotto di `text.hsp`, non una alla volta;
3. **le 915 dinamiche di `action.hsp`**, che riparano anche «mordes».

⚠️ **Ma prima conviene il collaudo**, ed è la cosa che questa sessione lascia
più scoperta: **1.131 nomi nuovi non sono mai stati visti a schermo**. Vedi
«Per rifare la prova in gioco» più sotto. Serve un salvataggio nuovo.

### Le quattro verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 336 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 373 | 1.288 | 29% |
| `text.hsp` | 721 | 1.740 | 41% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **3.915** | **8.624** | **45%** |

Fuori dalla Fase 1: `db_creature.hsp` a **1.132 firme su 3.655** — **tutti e
1.131 i nomi** più l'epiteto — e le 2.555 descrizioni d'oggetto di
`db_item.hsp`.

**336 test**, prova d'identità **72/72 e 27.813**, **5.646 sostituzioni** nella
build, il compilatore non dice nulla.

### Rimasto aperto di proposito

- **Il collaudo dei nomi**: nessuno dei 1.131 è stato visto in gioco. È il
  debito più grosso, ed è il tipo di debito che il collaudo di Norfor ha già
  dimostrato saper ripagare — quella prova trovò un difetto latente che due
  sessioni di lettura non avevano visto.
- **«draco» è una decisione revisionabile.** Vedi sotto: se non convince,
  si rifà in un giro solo.

## Il metodo, ormai rodato

Un lotto è una razza. Il giro completo:

```powershell
python -m strumenti.creature --razza <razza> --uscita lavoro/fase2-<razza>-001.jsonl
# ... si traduce ...
python -m strumenti.verifica lavoro/<lotto>.jsonl   # prima di reimportare
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita        # 72/72, 27.813, ambigue 0
python -m strumenti.genera_toppe_nomi     # 32 generate, tutte «ok»
python -m strumenti.genera_toppe_casuali  # 213 generate, tutte «ok»
```

### Prima di tradurre un nome opaco, leggi la sua carta

Scoperta della sedicesima sessione, confermata cinquantasei volte nella
diciassettesima. Il blocco della creatura in `db_creature.hsp` dice cosa la
creatura **è nel sistema**; `db_card.hsp` dice cosa **rappresenta**: due o tre
frasi di prosa in `cardrefskill`, poche righe sopra il `cardrefn` che ne porta
il nome.

⚠️ **La carta dà anche il sesso**, ed è spesso l'unica fonte. `<Spipha>` è una
donna solo perché la carta dice «più di metà del suo corpo è trasformata dalla
maledizione del drago e sceglie vestiti che la coprano».

⚠️ **La carta tiene insieme le famiglie.** I tre lich sono una storia sola —
`シズル` diventa non morta e scrive il **codice Ssil**, il 冒涜の魔導亡者 ne
decifra un pezzo e sbaglia la fusione, `イスシズル` sorveglia gli appunti.
Tradotti uno per uno sarebbero stati tre epiteti scollegati.

⚠️ **Tre carte inglesi sono sbagliate nel sorgente**: `マンドレザッパー`
(`db_card.hsp:4131`), `世界樹` (`9643`), `ガイドの『ノルン』` (`7017`) hanno la
prosa inglese di un'altra creatura. Il giapponese è sempre corretto.

## Le sette cose da non riscoprire

### 1. Un nome già preso non si può riusare

Due creature diverse non possono uscire a schermo con lo stesso nome. È
successo tre volte, e ogni volta la seconda ha dovuto cambiare: `メイド` →
«la domestica» perché `メイドさん` era già «la cameriera»; `沙羅曼蛇` →
«la salamandra d'oriente» perché `メガサラマンダー` era già «la salamandra»;
`ローパー` → «il tentacolare» perché `スライムローパー` era già «la melma
tentacolare». **Cercare in dizionario prima di scegliere**, non dopo.

Vedi [[una-chiave-che-collide-non-e-una-chiave]].

### 2. `ドレイク` è «draco», e questo chiude il refuso di `action.hsp:17390`

La razza `drake` è **亜竜**, sub-drago, e le carte lo dicono di tutti
(`viashivan` è «mezza lucertola», `mass monster` «una sottospecie di drago»).
Serviva un gradino sotto «drago» e l'italiano ce l'ha: **«draco»**, che è il
nome del *Draco volans*, la lucertola che plana.

⚠️ **Da qui viene che il preteso refuso non era un refuso.** `Electric Drake`
(電気竜, l'evoluzione di 電気羊) è «il draco elettrico», e chiamarlo «il drago
elettrico» lo farebbe collidere con エレキドラゴン. La voce resta com'è.

⚠️ **È la decisione più revisionabile della sessione**: «draco» e «drago»
differiscono di una lettera, ed è per questo che la sedicesima sessione l'aveva
letta come un errore di battitura. L'alternativa seria è «dragonetto». Se si
cambia, sono tre nomi del lotto `drake` più quella voce di `action.hsp`.

### 3. L'articolo lo porta il nome, **anche** un nome proprio

`name()` riconosce i nomi propri **dalla prima lettera** (`init.hsp:1713-1716`),
cioè da `<` o da `"`. Gli dèi stanno fra `<>` e non prendono articolo; i quattro
nomi del ciclo di Cthulhu no, e l'inglese infatti scrive `the cthugha`. Vanno
con l'articolo: «il Cthugha», «la Shub-Niggurath». Criterio completo in
`guida-stile.md`.

⚠️ **Il test dell'articolo ha avuto ragione due volte su due.** Quando cade,
ha ragione lui.

### 4. Il giapponese arbitra, e il registro si è allungato

Su 1.131 nomi l'inglese ha sbagliato molte decine di volte, e non per
abbreviazione. Oltre ai casi già noti:

| giapponese | inglese | cosa dice davvero |
|---|---|---|
| 機甲将軍 | `iron colonel` | è un **generale**, la carta lo ripete |
| 生化学者 | `biologist` | **biochimico** |
| 剣客 | `the cosmic sword` | uno **spadaccino**: perde la persona |
| ネザーマッドゴーレム | `mad mud golem` | è **mud**, 地獄の泥 |
| マルチプルゴーレム | `ultimate golem` | è **multiplo** |
| ファラオの呪い | `cursed coffin` | la **maledizione del faraone** |
| デビルコボルト | `dark kobold` | **diabolico** |
| 自走雷撃砲 | `electric tank` | un **semovente**, e a fulmini |

⚠️ **Ma non sempre.** `胡瓜の怪物` l'inglese lo chiama `cucumber horse` e ha
ragione: la carta descrive il 精霊馬 di Obon, il cavallo di cetriolo che porta
i morti. Si distingue chiedendo alla carta.

### 5. Le fusioni si rifanno, e a volte l'italiano vince

Il principio era già fissato; questa sessione ha aggiunto i casi in cui
l'incastro italiano è **migliore** dell'inglese:

- `アロマカリス` = アノマロカリス + アロマ → «l'aromalocaris», identico;
- `ヒノキオ` = ヒノキ + ピノキオ, e Pinocchio è italiano → «il Pinocipresso»;
- `魔女王蜂` sovrappone 魔女 e 女王蜂 → «l'ape stregina»;
- `コンバット` = com + bat → «il combattistrello»;
- `Ｅ・スケープゴート` = escape + scapegoat → «il capro espatriatorio»;
- `ガジュマルの怪` la carta lo chiama 絞め殺しの木 → «il fico strangolatore».

### 6. Il precedente decide più spesso di quanto sembri

Prima di inventare, cercare: `db_item.hsp` aveva già fissato i tre 魔神石
(«globo oscuro verde/blu/cremisi») e quindi i tre 魔神兵; `action.hsp` aveva
già «il Meshera Soldado» e quindi tutta la famiglia; `<Neres> la smemorata`
ha dato il genere a `<Ryutye> lo smemorato`; il **quiz** di `text.hsp` chiede
già «il nome esatto della tartaruga di Valm» e ha vincolato `玄武の『レイキ』`.

Lo strumento è banale — una ricerca per sottostringa su `dizionario/*.jsonl` —
e va fatta **prima** di scegliere.

### 7. L'articolo sta sulla testa del sintagma, non sulla persona

Invariato dalla sedicesima sessione, e ha retto su tutti i lotti di persone.
Sesso dichiarato (`cdata(CDATA_SEX, rc)`) → si concorda; sesso casuale →
sostantivo il cui articolo non dipende dalla persona («la guardia»,
«l'abitante», «l'agente di commercio»); maschile non marcato solo dove
l'italiano non offre altro. ⚠️ `/man/` non è il sesso: è
`DBSPEC_CHARA_FILTER`.

## L'ordine che resta

1. **il collaudo dei 1.131 nomi**, con un salvataggio nuovo;
2. le **320 firme di voce** di `db_creature.hsp`;
3. le **59 rinviate** del quiz, ora sbloccate;
4. le **915 dinamiche di `action.hsp`**, che riparano anche «mordes»;
5. `text.hsp` dal 41% in su, `command.hsp`, `proc.hsp`, `trait.hsp`;
6. le **2.555 descrizioni d'oggetto** di `db_item.hsp`.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è
permanentemente sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp` — oggi è solo `custom_tweaks.hsp`, ma è un
file di *tweak* e cresce a ogni rilascio.

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono
`/man/` letto come percorso: passare il testo con `git commit -F <file>`.

⚠️ **CP932 non codifica tutto.** Niente `«»`, niente dieresi tedesche
(`Konigskatze`, non `Königskatze`), niente `å` — `verifica.py` blocca i primi,
gli altri vanno evitati a mano.

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

⚠️ **Serve un salvataggio nuovo** per i nomi, e un **personaggio nuovo** per
l'epiteto. La ragione è più forte di «i nomi sono memorizzati»: la rinomina
all'evoluzione è una **sostituzione di stringa** sul nome nel salvataggio
(`action.hsp:18640-18646`), quindi un alleato reclutato con l'exe non tradotto
non combacia più con `evold` e **non viene rinominato affatto**. Un alleato
generato dalla console dopo la patch va bene lo stesso.

### La console di debug, per scrivere i campi che il gioco non espone

`cgx-lua.exe` in `elonaplus2.31\` è la build della traduzione con
`CUSTOM_GX_LUA` attiva — la define sta commentata a monte (`main.hsp:9`) e
senza di lei **la console Lua non esiste nell'eseguibile**. La modifica si fa
in BUILD e si ripristina subito; serve anche `hsplua.dll`, già copiata.

```powershell
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-lua.exe" -ArgumentList "--develop" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Senza `--develop` la console parte in modalità HSP. **F12** apre la console; la
sintassi è `dim[attributo][indice]`:

```lua
return cdata[17][2]                 -- impressione dell'alleato 2 (serve >= 150)
cdata[17][2] = 150
return cdata[214][2]                -- stadio d'evoluzione, dev'essere 0
return itemcreate(869, 0, 0, 0, 0)  -- gemma in inventario, torna l'indice
inv[25][17] = 14                    -- PARAM1 = EVITEM_HEART_ANOTHER
```

⚠️ L'oggetto va usato su una delle **otto caselle adiacenti**
(`*prompt_direction`, `system.hsp:4105`), e il bersaglio dev'essere in uno slot
alleato — indice **< 16** (`action.hsp:16626`). `cgx-lua.exe` è uno strumento
di collaudo: quello che si spedisce resta `cgx-test.exe`.

⚠️ L'utente **preferisce una lista di passi da eseguire lui** al collaudo
pilotato da qui. Dargli la tabella, con l'esito atteso di ogni riga.

### Il collaudo, punto per punto

- ✅ **L'evoluzione vera è stata provata** il 2026-08-10:
  `Norfor il cavallo zoppo` → **`Norfor l'unicorno`**. È scattato il **ramo
  suffisso** (`action.hsp:18643-18644`), quello con l'indice sbagliato
  (`rc` invece di `tc`): ha dato il risultato giusto perché lì `rc` valeva
  `tc`, quindi il difetto è **latente**, non attivo.
- ⚠️ **Il non tradotto esce in inglese, non in giapponese.** `applica`
  sostituisce nello slot **inglese** di `lang(jp, en)` (`applica.py:305`) e il
  gioco gira in inglese. Atteso fino a che non si chiudono le 915 dinamiche.
- ❌ **I 1.131 nomi non sono mai stati visti**, tranne i 351 della quindicesima
  sessione sui passanti delle città. È il debito da pagare per primo.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

⚠️ Alcuni nomi di questa sessione sono lunghi — «la principessa ibrida
<roccia e macchina>», «<Melugast AO-I> la macchina da combattimento» — e i
tetti qui sopra non li coprono: il nome di creatura compare in messaggi senza
limite. Se il collaudo mostra troncamenti, il posto dove guardare è questa
tabella, non il dizionario.

Vedi [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[guardia-troppo-severa]], [[larghezza-per-campo]], [[ultima-scrittura-vince]],
[[percentuale-senza-denominatore]], [[una-procura-non-e-una-proprieta]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
