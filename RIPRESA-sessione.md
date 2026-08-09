# Ripresa sessione

Aggiornato: 2026-08-09, fine della quattordicesima sessione.

## La prima cosa da fare

**Il lotto dei ~930 nomi di creatura che restano**, a lotti per **razza**. Il
nucleo atomico è dentro e collaudato a schermo: da qui in poi non c'è più
niente di atomico, si va per lotti normali.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m strumenti.creature --classe nome --uscita lavoro/fase2-nomi-grezzo.jsonl
```

⚠️ Quel comando dà **tutti** i 1.131 nomi, nucleo compreso: va filtrato su chi
ha già una resa in `dizionario/db_creature.hsp.jsonl`. `--classe` era rotto
fino a ieri (passava una `str` dove serve un `Path`) ed è stato riparato in
questa sessione: se si comporta in modo strano, è la prima volta che lo si usa
davvero.

Il taglio per razza si fa con `dbidn` prima di `*db_race`: 76 razze, da
`norland` con 91 a quelle da una.

### Le quattro verifiche d'apertura

```powershell
python -m pytest strumenti/tests -q        # atteso: 331 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, in due classi 0
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** ← chiuso oggi |
| `item_data.hsp` | 318 | 318 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `action.hsp` | **373** | 1.288 | 29% |
| `text.hsp` | 721 | 1.740 | 41% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **3.915** | **8.624** | **45%** |

Fuori dalla Fase 1: `db_creature.hsp`, **204 firme su 3.655** (203 nomi del
nucleo più l'epiteto), e le 2.555 descrizioni d'oggetto di `db_item.hsp`.

Sei commit oggi, tutti verdi e pushati. **331 test** (erano 325), prova
d'identità **72/72 e 27.813**, **4.684 sostituzioni** nella build, il
compilatore non dice nulla. **Rinviate: da 80 a 79** — restano le 59 risposte
del quiz, che aspettano gli altri ~930 nomi, e le 20 `elename()` che aspettano
`proc.hsp`.

## Il lavoro di oggi, in cinque pezzi

1. **Il nucleo atomico tradotto**: 576 voci in due dizionari insieme, 378
   stringhe, 380 firme, 372 rese. L'articolo sta dentro il nome.
2. **`<Pants of Ogre>` chiuso** → «`<Mutande dell'Ogre>`», e con lui
   `db_item.hsp` a 1.606 su 1.606.
3. **Il giapponese arbitra** dove la colonna inglese sbaglia: otto collisioni,
   quattro catene di evoluzione riparate.
4. **L'epiteto perde il `the`**: 152 siti con una voce sola, trovato guardando
   lo schermo.
5. **Una correzione a una mia conclusione sbagliata**, trovata dallo stesso
   screenshot. È il pezzo più importante e sta qui sotto.

## Le tre cose da non riscoprire

### Il giapponese arbitra dove le due colonne divergono

La colonna inglese di upstream **non è una chiave**. Sbaglia in due direzioni:

- `フレアチック` è `Flare Chick` in un punto e `Flare chick` nell'altro (idem
  `イノブタ`, `ヤドナシ`, `デュラハン`): il confronto distingue le maiuscole,
  quindi quelle **quattro evoluzioni di secondo stadio in inglese non scattano
  mai**, in giapponese sì;
- `サラブレッド` (*purosangue*) è `wild horse` in `action.hsp` ma
  `thoroughbred` in `db_creature.hsp`; `野うさぎ` è `rabbit` di là e
  `wild rabbit` di qua.

**Dove divergono si traduce il giapponese**, che è l'originale. Non per
correggere upstream: perché rendere `サラブレッド` con «cavallo selvatico»
sarebbe un nome falso a prescindere dal codice.

⚠️ **Conseguenza sulle guardie: la chiave è la firma, non l'inglese.** Le
funzioni `evoluzioni_con_jp`, `nomi_per_creatura_con_jp` e
`nomi_visibili_con_jp` esistono per questo. Una mappa `{en: it}` di due rese ne
tiene una sola, in silenzio — è il difetto che c'era.

### ⚠️ Il ramo del suffisso è la strada normale, non quella morta

**Ho scritto il contrario a metà sessione ed era falso.** Il conto guardava il
nome nudo della specie, dove `evold` sta in testa. Ma il nome che il
**salvataggio** conserva per un alleato con nome proprio è l'epiteto —
«Lazrof il cavallo zoppo» — e lì `evold` sta in coda, sempre.

Simulato il taglio con un epiteto davanti: **245 su 245 dal suffisso, zero dal
prefisso.** E i personaggi con epiteto sono i 152 con `CHARA_BIT_HAS_NAME`,
cioè quelli che si tengono in squadra, cioè **quelli che evolvono**.

Quindi la riparazione di `action.hsp:18644` non è una precauzione: è la
condizione perché l'evoluzione di un alleato con nome funzioni. Vale anche in
inglese, dove `Lazrof the lame horse` finisce per `lame horse`.

> Il dato non è quello che il sorgente scrive: è quello che il salvataggio
> conserva.

La guardia nuova non controlla l'aggancio: monta il nome come lo monta il
gioco, esegue `18640-18646` col suffisso riparato e confronta il **risultato**.

### L'articolo va su tutto ciò che non comincia per `<` o `"`

`init.hsp:1712-1719` non guarda la maiuscola: guarda il primo carattere e
`CHARA_BIT_HAS_NAME`, che sta sul **personaggio** e non sulla stringa. Quindi
anche `Unicorn` e `Nekomata` prendono l'articolo: «l'unicorno», «la Nekomata».

⚠️ La guardia dell'articolo è filtrata su `classi()`: le dinamiche di
`db_creature.hsp` non sono nomi, e chiedere loro l'articolo vorrebbe dire
chiederlo **fuori** dal nome.

## Le sei guardie del nucleo, e cosa difendono

In `strumenti/tests/test_creature.py`:

| guardia | cosa difende |
|---|---|
| la misura del nucleo | 378 stringhe, 380 firme, 203 + 373 voci |
| stessa firma, stessa resa nei due dizionari | i dizionari sono per file e non si parlano |
| `evold` resta agganciato | la rinomina deve continuare ad attaccare, **per firma** |
| dove agganciava il giapponese aggancia l'italiano | le quattro catene riparate |
| il taglio su un alleato con epiteto | la chirurgia vera, simulata: 245 tagli |
| ogni nome porta l'articolo | solo le stringhe di classe `nome` |

`AGGANCI_SOLO_INGLESI` contiene **una** deroga, col motivo: `bisque doll` è
prefisso di `bisque dolls` solo per la `-s` del plurale inglese. Tutto ciò che
non è in quella lista deve agganciare.

## Il collaudo a schermo, com'è andato

Provato su partita nuova, due giri. **Funziona:** «il putit», «il coboldo»,
«il paguro», «l'occhio fluttuante», «Chinnba la bambina», «Lazrof il cavallo
zoppo». L'articolo dentro il nome non stona in nessuno dei posti guardati.

**Non ancora provato:** un'evoluzione vera. Serve impressione ≥ 150
(`action.hsp:16630`), stadio 0, e l'oggetto d'evoluzione usato sull'alleato.
Il soggetto giusto è a portata di mano: **Lazrof è un `lame horse`**, evmode 3.

> esito atteso: `Lazrof il cavallo zoppo` → **`Lazrof l'unicorno`**

**Non è un difetto** e non va inseguito: «Chinnba la bambina slashes il paguro»
e «mordes» sono lo stato intermedio previsto. Il verbo viene da `_melee` in
`text.hsp` (tradotto) e la frase che lo avvolge è `action.hsp:4887`, ancora fra
le 915 inglesi, che ci attacca `_s(cc)`. Si ricompone quando arriva quel lotto.

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
l'epiteto: quello vecchio ha la stringa sbagliata già scritta dentro.

⚠️ L'utente **preferisce una lista di passi da eseguire lui** al collaudo
pilotato da qui. Dargli la tabella, con l'esito atteso di ogni riga. Ha
funzionato: due screenshot hanno trovato un difetto vero e ribaltato una
conclusione sbagliata.

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
`skilldesc` fuori da `skill.hsp` — oggi è solo `custom_tweaks.hsp`, ma è un
file di *tweak* e cresce a ogni rilascio.

## L'ordine che resta

1. gli altri **~930 nomi**, a lotti per razza; poi le **320 di voce**;
2. le **59 rinviate** del quiz, che si sbloccano solo dopo (cinque lo sono già
   nel merito — `steel golem`, `spider`, `scorpion`, `black widow`,
   `paralyzer` — ma restano col resto);
3. le **915 dinamiche di `action.hsp`**, che riparano anche «mordes»;
4. `text.hsp` dal 41% in su, `command.hsp`, `proc.hsp`, `trait.hsp`;
5. le **2.555 descrizioni d'oggetto** di `db_item.hsp`.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

Vedi [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[guardia-troppo-severa]], [[larghezza-per-campo]], [[ultima-scrittura-vince]],
[[percentuale-senza-denominatore]], [[una-procura-non-e-una-proprieta]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]] e
[[cp932-perdite-silenziose]].
