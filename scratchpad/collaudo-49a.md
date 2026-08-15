# Collaudo 49ª — 2026-08-16

Eseguibile: `elonaplus2.31\cgx-test.exe` (16/08 01:40, dopo tutti i lotti della 48ª).
Salvataggio al sicuro in `save-backup\pre-collaudo-20260816-49a` (202 file).
`config.txt`: `language. "1"`, `fontSfix1. "1"` → **sizefix = 1**, corpo 11, **6,6 px** a carattere.

Segna accanto a ogni riga: ✅ come atteso · ⚠️ tagliata/saldata/storta · ❓ non raggiunta.

---

## 1 — `i` su un alleato (menu di interazione)

Tetto **29 caratteri** (`:6172`, riquadro da 275 px). La voce più lunga già spedita ne fa 28.

Undici voci nuove in cima:

| riga | testo atteso | car. |
|---|---|---|
| `:5952` | `Parla` | 5 |
| `:5955` | `Attacca` | 7 |
| `:5963` | `Di' quello che provi` | 20 |
| `:5967` | `Dai/Ricevi qualcosa` | 19 |
| `:5970` | `Dai qualcosa` | 12 |
| `:5976` | `Dai da mangiare` | 15 |
| `:6002` | `Rimetti nella bara` | 18 |
| `:6009` | `Porta fuori` | 11 |
| `:6144` | `Mostra le capacita'` | 19 |
| `:6147` | `Informazioni` | 12 |

⚠️ Se una riga esce tagliata, il posto dove guardare è la voce già spedita da 28.

## 2 — `i` su una creatura-carta

Guerriero di picche, piuma di fiori, occhi di quadri, strega di cuori, o un Jolly Variabile.

- `:5985` `<Cambia valore>`
- `:5987` `[Cambia in picche]`
- `:5990` `[Cambia in fiori]`
- `:5993` `[Cambia in quadri]`
- `:5996` `[Cambia in cuori]`
- ⭐ premendo la prima deve uscire **`Quale valore?`** (`:6770`), **non** «Quale rango?».
  È la correzione della 48ª: «rango» in questo file è già il grado dell'avventuriero.

## 3 — Inventario

- `:14211` `Parti:` nel riquadro dell'equipaggiamento
- `:14280` ` (per terra)` in coda al nome (guarda un oggetto per terra)
- `:14325` ` (tiro)` in coda al nome (arma da lancio equipaggiata)
- `:14272` / `:14275` ` pz.` al banco delle medagliette e dei biglietti musicali
  💡 resa unica per due rami: a distinguerli è l'intestazione di colonna sopra
  (`:14105` «Medagliette», `:14108` «Biglietti»). Verifica che regga anche col valore **1**.

## 4 — Menu delle capacità ⭐ la misura più a rischio

Riquadro da **600 px** → tetto `(600 − 58 − 40) / 6,6` = **76 caratteri**.

- `:5342` titolo `Capacita'`
- `:5344` `Nome` · `:5345` `Costo` · `:5346` `Effetto`
- ⭐⭐ **riga di aiuto in fondo**, composta da `strhint2+3+7+8` (`text.hsp:114`-`122`):

  `+,- [Pagina]  Shift,Esc [Chiudi]  0~9 [Scorciatoia]  * [NASC.] / [MOSTRA]`

  = **73 caratteri su 76**. Tre di margine. Se sfora, si vede qui.
- `:5552` variante ad area: `Capacita' ad area` — stessa riga di aiuto, stesso tetto.
- `:5470` `[Mostrate tutte le capacita']` · `:5673` `[Mostrate tutte le capacita' ad area]`

## 5 — Elenco dei PNG (dalla scheda alleati, col tasto che cambia colonna)

Riquadro da 700 px. Colonne: nome `wx+84`, informazioni `wx+372`, terza `wx+512`.
→ la colonna informazioni ha **140 px ≈ 21 caratteri**.

- `:3565`/`:3568` `Nome` · `:3570` `Informazioni` · `:3546` `Elenco dei candidati`
- intestazioni della terza colonna: `:3550` `Paga` · `:3553` `Assunzione (paga)` ·
  `:3556` `Livello` · `:3559` `Rottura guardia` · `:3562` `Sanguinamento`
- `:3631`-`:3634` la riga `Lv.10 male(25)` — vive nei 21 caratteri della colonna informazioni
- `:3611` `(fuori vista)` · `:3616` `/assalto/` · `:3619` `/difesa/` ·
  `:3622` `/contrasto/` · `:3625` `/dialogo/`
- `:3677` ` oro` in coda al costo

⚠️⚠️ **`:3627` è il sospetto numero uno.** Con la colonna su «Rottura guardia» la riga è
`Hp:100%/assalto/ Rottura guardia:0%` = **35 caratteri in 21**. L'inglese ne fa 29 e sfora
già lui (`" GuardBreak:"`), ma noi peggioriamo di **6**. Da guardare per primo: se il
numero finisce sotto la colonna accanto, serve una resa corta — p.es. ` Guardia:`.

⚠️ **Il sesso resta in inglese ed è atteso** (`male`, `female`, `male?`, `female?`,
`none`, `hermaphrodite`): è una decisione di `invariati.md`, quel valore è salvato nel
personaggio e riletto come operando in `init.hsp:1813`-`:2008`. **Non «aggiustarlo».**

## 6 — Bacheca degli incarichi e jukebox

- `:3320` `Incarichi in bacheca` (+ i simboli `$`)
- `:3843` `Elenco dei brani` · `:3845` `Titolo`
- `:7513` `Titolo` (altro riquadro)

---

## Debiti vecchi, se avanza tempo

- ⚠️ **Da rifare con l'eseguibile nuovo** (toppa della 47ª): riquadro «Combat Rolls»
  della scheda personaggio (`c`). Deve leggersi `Mira 64%` e `Pot. magia 100%`, **con lo
  spazio**. La toppa sposta l'etichetta a sinistra in modo inglese
  (`:12427` `wx + 590 - en * 6`, `:10733` `wx + 564 - en * 22`).
- **Le cinque schermate mai aperte** (47ª): ritratto/PCC (`c` poi `p`, e «Su misura»
  compare solo su un alleato), specchio (`Mantello Off` o `MantelloOff`?), cambio di
  immagine (`usa:Pic_ 123`), tono di voce (riga di aiuto da 54 su 55), evocazione dei PNG.
- **Gli 88 ranghi della 41ª** — il debito più vecchio.
- 💡 Le righe d'attacco della scheda **non** compaiono aprendola: le disegna
  `*show_weaponStat`, che gira solo equipaggiando o togliendo qualcosa in uno slot
  **mano**. Riequipaggiare l'arma prova in un gesto le righe d'attacco, il messaggio
  «Ti togli …» e gli avvisi sul peso.
