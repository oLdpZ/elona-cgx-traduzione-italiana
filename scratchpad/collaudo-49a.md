# Collaudo 49ª — 2026-08-16

## ESITO (scritto a fine sessione)

✅ **Verificato a schermo e a posto** — menu delle capacità (titolo, colonne, e la
riga di aiuto da **73 su 76**, che era la misura più a rischio della 48ª); menu
`i` su un alleato (venti voci, la più lunga «Metti fra gli indispensabili» = **28
su 29**, nessuna tagliata); «Combat Rolls» con `c` (la toppa della 47ª tiene:
`Mira 64%` con lo spazio); `Unisce le forze sulla serratura`; `Parti:` coi nomi
degli slot (`Mano Mano Tiro Dardi`); ` (per terra)`; ` (tiro)` e il menu
«Mano o Tiro?»; la bacheca degli incarichi.

❓ **Non raggiunte, ognuna col suo motivo** — la colonna «Rottura guardia» (serve
la capacità «Istruzione individuale», che il personaggio non ha); la
creatura-carta (il `<Cambia valore>` vuole il ritratto `xy2pic(18, 35)`, che
assegna solo `proc.hsp:20179` — «Forza del poker» a 50 di barra: **non è una
schermata da un tasto**); il jukebox (è un oggetto, non un arredo di città); il
` pz.` dei due banchi.

⚠️ **Il sospetto della colonna informazioni (`:3627`, 35 caratteri in 21) resta
APERTO**, perché quella schermata non si è potuta aprire.

💡 **Quel che si vede in inglese e NON è un difetto**: `(Light)` (`cnveqweight` in
`screen.hsp`, file senza dizionario), `You change your equipment.`
(`main.hsp:3089`, dentro una `lang()` regolare — `main.hsp` non ha dizionario),
`Autopickup` (`screen.hsp:1004`, idem), `un black claws` (già censito il
2026-08-10: 261 `iknownnameref`), gli incarichi (`event.hsp`, 649 voci), e la
**voce vuota in cima al menu delle capacità** (fuori-di-uno di monte: il ciclo
parte da `cnt = 0`, cioè dallo slot 600, che non ha costante né nome; le 276
`SKILL_SPACT_*` vanno da 601 a 876).

---


Eseguibile: `elonaplus2.31\cgx-test.exe` (16/08 01:40, dopo tutti i lotti della 48ª).
Salvataggio al sicuro in `save-backup\pre-collaudo-20260816-49a` (202 file).
`config.txt`: `language. "1"`, `fontSfix1. "1"` → **sizefix = 1**, corpo 11, **6,6 px** a carattere.

Segna accanto a ogni riga: ✅ come atteso · ⚠️ tagliata/saldata/storta · ❓ non raggiunta.

⚠️ **Due indicazioni della 48ª erano sbagliate e qui sono corrette:**
1. **Non esiste un tasto che cambia la colonna dell'elenco PNG.** `allyctrl` lo imposta chi
   apre la finestra (`command.hsp:1495`-`:1557`: nel ciclo non c'è nessun ramo che lo tocchi).
   Ogni colonna è una schermata diversa, raggiunta da un'azione diversa — vedi § 5.
2. **«Parti:» non sta nella scheda dell'equipaggiamento** (`w`): sta nel riquadro
   informativo di `INVCTRL_ALLYGET`, cioè `invctrl == 25` (`defines/mod.hsp:1908`), la
   finestra con cui si **prende** roba da un alleato. Vedi § 3.

I tasti sono letti dal `config.txt` di questa installazione.

---

## 1 — Menu delle capacità ⭐ la misura più a rischio

**Come arrivarci:** tasto **`a`** (`key_skill`, `main.hsp:3648`). La variante ad area è
**`W`** (maiuscola, `key_wipe`; `help.hsp:409` «広域能力を使う(Wide apply)»).

Riquadro da **600 px** → tetto `(600 − 58 − 40) / 6,6` = **76 caratteri**.

- `:5342` titolo `Capacita'` — con `W` diventa `:5552` `Capacita' ad area`
- `:5344` `Nome` · `:5345` `Costo` · `:5346` `Effetto`
- ⭐⭐ **riga di aiuto in fondo**, composta da `strhint2+3+7+8` (`text.hsp:114`-`122`,
  con `key_pageup` = `+` e `key_pagedown` = `-` presi dal tuo `config.txt`):

  `+,- [Pagina]  Shift,Esc [Chiudi]  0~9 [Scorciatoia]  * [NASC.] / [MOSTRA]`

  = **73 caratteri su 76**. Tre di margine. Se sfora, si vede qui: guarda che
  `[MOSTRA]` arrivi intero e non finisca sul bordo.
- premi **`*`** (`key_mode2`, `:5449`) → `:5470` `[Mostrate tutte le capacita']`
  (con `W`: `:5673` `[Mostrate tutte le capacita' ad area]`)
- prova a nascondere una capacità legata a un'abilità → `:5457`
  `Le capacita' legate a un'abilita' non si possono nascondere.`

## 2 — `i` su un alleato (menu di interazione)

**Come arrivarci:** tasto **`i`** (`key_interact`, `main.hsp:3708`), poi la direzione
dell'alleato. Serve un alleato **adiacente**.

Tetto **29 caratteri** (`:6172`, riquadro da 275 px). La voce più lunga già spedita ne fa 28.

| riga | testo atteso | car. | quando compare |
|---|---|---|---|
| `:5952` | `Parla` | 5 | sempre (se non sei confuso) |
| `:5955` | `Attacca` | 7 | non su un alleato in squadra, se `cfg_atk_select` lo consente |
| `:5963` | `Di' quello che provi` | 20 | interesse ≥ 80 |
| `:5967` | `Dai/Ricevi qualcosa` | 19 | alleato in squadra |
| `:5970` | `Dai qualcosa` | 12 | PNG **non** in squadra |
| `:5976` | `Dai da mangiare` | 15 | alleato o bestiame, con il tweak «feed» attivo |
| `:6002` | `Rimetti nella bara` | 18 | zombie da negromanzia |
| `:6009` | `Porta fuori` | 11 | bestiame nel ranch |
| `:6144` | `Mostra le capacita'` | 19 | alleato |
| `:6147` | `Informazioni` | 12 | sempre |

⚠️ Se una riga esce tagliata, il posto dove guardare è la voce già spedita da 28.

## 3 — «Parti:», « (per terra)», « (tiro)», « pz.»

- ⭐ **`Parti:`** (`:14211`) — `i` su un alleato → **«Dai/Ricevi qualcosa»** → scegli di
  **ricevere**. È il riquadrino in basso che elenca gli slot equipaggiati dell'alleato
  (`invctrl == INVCTRL_ALLYGET`). Nello stesso riquadro c'è anche `:14207` `Peso eq.:`.
- **` (per terra)`** (`:14280`) — si attacca al nome di un oggetto **che sta a terra**
  in qualunque menu che pesca anche da terra: `e` (mangia), `r` (leggi), `q` (bevi),
  `t` (usa)… Posa qualcosa con `d` e poi apri `e` o `t` sopra quella casella.
  ⚠️ **Non** compare in `g`, nel negozio, né al banco delle medagliette
  (`:14278` esclude `invctrl` 3, 11, 22, 27, 28).
- **` (tiro)`** (`:14325`) — equipaggia un'**arma da tiro identificata a fondo**
  (arco, fucile, fionda) e apri un elenco d'inventario: compare accanto al segno di
  equipaggiato.
- **` pz.`** (`:14272` / `:14275`) — è il banco di scambio `INVCTRL_METAL`:
  - **medagliette**: parla con **Miral, il fabbro leggendario** (`chat.hsp:2969`-`:2977`)
    e scegli «Ho delle medagliette» → colonna `:14105` **Medagliette**;
  - **biglietti musicali**: parla con **Stoke il ricco** (`chat.hsp:7742`-`:7748`)
    e scegli «Biglietti musicali» → colonna `:14108` **Biglietti**.
  💡 Resa unica per due rami: a distinguerli è l'intestazione di colonna, disegnata a
  `wx + 526` sopra quegli stessi numeri. **Verifica che regga anche col valore 1**
  («1 pz.»).

## 4 — `i` su una creatura-carta

**Come arrivarci:** tasto **`i`** su un **guerriero di picche, piuma di fiori, occhi di
quadri, strega di cuori** o un **Jolly Variabile** — il gioco riconosce la famiglia dal
ritratto (`:5983`, `cdata(CDATA_PIC, tc) == xy2pic(18, 35)`), e la creatura **non** dev'essere
già alleata (`:5984`).

- `:5985` `<Cambia valore>`
- `:5987` `[Cambia in picche]` · `:5990` `[Cambia in fiori]` ·
  `:5993` `[Cambia in quadri]` · `:5996` `[Cambia in cuori]`
  (compare solo il seme **diverso** da quello della creatura che hai davanti)
- ⭐ premendo **`<Cambia valore>`** deve uscire **`Quale valore?`** (`:6770`),
  **non** «Quale rango?». È la correzione della 48ª: «rango» in questo file è già il grado
  dell'avventuriero (`:4192`, `:4194`), e `proc.hsp:20184` dice già «seme e valore».

## 5 — Elenco dei PNG (`*com_listNpc`, `command.hsp:3451`)

Riquadro da 700 px. Colonne: nome `wx+84`, **informazioni `wx+372`**, terza `wx+512`.
→ la colonna informazioni ha **140 px ≈ 21 caratteri**.

Sempre visibili, qualunque sia l'entrata:
`:3565` `Nome` · `:3570` `Informazioni` · `:3631`-`:3634` la riga `Lv.10 male(25)` ·
`:3677` ` oro` in coda al costo.

**Ogni colonna è una schermata diversa.** Le entrate vere:

| colonna | `allyctrl` | come arrivarci |
|---|---|---|
| `:3550` `Paga` | 0 | in **casa tua**: usa (`t`) la **bacheca di casa** (`action.hsp:8222`, serve `MAP_TYPE_HOME`) → l'opzione che chiede «Chi vuoi spostare?» (`map_user.hsp:824`) |
| `:3553` `Assunzione (paga)` | 1 | stessa bacheca di casa → «Chi vuoi assumere?» (`map_user.hsp:1877`) |
| `:3556` `Livello` | 3 | da un dialogo (`chat.hsp:15515`, `:20403`) |
| `:3559` **`Rottura guardia`** | 4 | capacità speciale **«Istruzione individuale»** (`skill.hsp:1788`, `proc.hsp:26781`) — lanciala con `a` |
| `:3562` `Sanguinamento` + `:3546` `Elenco dei candidati` | 5 | capacità speciale **«Trasfusione diretta»** (`skill.hsp:1284`, `proc.hsp:19085`) — lanciala con `a` |
| `Rank.` | 6 | costa **5 di barra della potenza** (`proc.hsp:20052`-`:20058`) |

⚠️⚠️ **`:3627` è il sospetto numero uno — è la schermata di «Istruzione individuale».**
Con `allyctrl == 4` la riga informazioni è
`Hp:100%/assalto/ Rottura guardia:0%` = **35 caratteri in 21**.
L'inglese ne fa 29 e sfora già lui (`" GuardBreak:"`, `sorgente/command.hsp:3627`), ma la
resa italiana peggiora di **6**. Se il numero finisce sotto la colonna accanto, serve una
resa corta — p.es. ` Guardia:`.
💡 Nella stessa schermata guarda anche `:3611` `(fuori vista)` (bersaglio fuori dalla
linea di vista) e i modi: `:3616` `/assalto/` · `:3619` `/difesa/` · `:3622` `/contrasto/` ·
`:3625` `/dialogo/`.

⚠️ **Il sesso resta in inglese ed è atteso** (`male`, `female`, `male?`, `female?`,
`none`, `hermaphrodite`): è una decisione di `invariati.md`, quel valore è salvato nel
personaggio e riletto come operando in `init.hsp:1813`-`:2008`. **Non «aggiustarlo».**

## 6 — Bacheca degli incarichi e jukebox

- **Bacheca** (`:3320` `Incarichi in bacheca`, più i simboli `$`): in una **città**,
  cammina **sopra** la bacheca degli incarichi — è una casella speciale,
  `cellfeat == 23` (`action.hsp:2233`-`:2235`). Non serve nessun tasto.
- **Jukebox** (`:3843` `Elenco dei brani`, `:3845` `Titolo`, riquadro da 340 px):
  usa (**`t`**, `key_use`) un **jukebox** — `EFFECT_JUKE_BOX`, `action.hsp:13719`-`:13722`.
  Prima esce la domanda `Quale brano metti su?` (`action.hsp:13721`).

---

## Debiti vecchi, se avanza tempo

- ⚠️ **Da rifare con l'eseguibile nuovo** (toppa della 47ª): premi **`c`** (`key_charainfo`)
  → riquadro «Combat Rolls». Deve leggersi `Mira 64%` e `Pot. magia 100%`, **con lo
  spazio**. La toppa sposta l'etichetta a sinistra solo in inglese
  (`:12427` `wx + 590 - en * 6`, `:10733` `wx + 564 - en * 22`).
- **Le cinque schermate mai aperte** (47ª):
  - **ritratto/PCC**: `c` poi `p` — «Su misura» compare solo aprendo la scheda **su un alleato**;
  - **specchio**: usa (`t`) uno specchio su un alleato — «Parti da nascondere»: si legge
    se esce `Mantello Off` o `MantelloOff`;
  - **cambio di immagine**: la riga `usa:Pic_ 123`;
  - **tono di voce**: riga di aiuto da 54 caratteri su 55;
  - **evocazione dei PNG**.
- **Gli 88 ranghi della 41ª** — il debito più vecchio.
- 💡 Le righe d'attacco della scheda **non** compaiono aprendola: le disegna
  `*show_weaponStat`, che gira solo equipaggiando o togliendo qualcosa in uno slot
  **mano** (`:12806`, `:14781`). **Riequipaggiare l'arma con `w`** prova in un gesto solo
  le righe d'attacco, il messaggio «Ti togli …» e gli avvisi sul peso.
