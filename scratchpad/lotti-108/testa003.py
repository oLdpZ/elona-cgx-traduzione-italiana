# -*- coding: utf-8 -*-
"""108a - Lotto 003 di `db_item.hsp`: il rapporto delle PERGAMENE e degli ATTI.

`FILTER_ITEM_SCROLL`, `description(3)`: **66 righe del sorgente, 65 firme**.
Dentro la categoria ci sono **due famiglie** che il giapponese tiene separate
con due parole diverse, e la resa le segue:

    巻物   → **una pergamena** (紙片, «foglio», nella riga di categoria)
    権利書 → **un atto**       (証書, «certificato»)

⚠️ **L'inglese apre venticinque righe con «It is a scroll that when read, …»**,
e in italiano quella testa costa: «Una pergamena che, letta, …» sono venti
caratteri su 69 spesi per dire due volte quel che il nome dell'oggetto dice già.
Il giapponese non ha quella testa — dice 「…する巻物だ。」, con la parola in
fondo — quindi la resa mette il **fatto** davanti quando il fatto è lungo, e
tiene «Una pergamena che …» quando ci sta. È la stessa scelta del lotto 002.

### ⚠️⚠️ Dieci atti, un solo giapponese, e dieci inglesi diversi

`:45063`-`:45418` e `:51362`-`:51575` sono i mezzi di trasporto: zattera,
peschereccio, nave pirata, nave da crociera, nave da guerra, sottomarino,
corazzata, locomotiva, autocarro, carrozza. **Il giapponese scrive la stessa
frase per tutti e dieci** — 「海マップでの乗り物の権利書だ。」 e
「ワールドマップでの乗り物の権利書だ。」, *un atto per un mezzo della mappa del
mare* / *della mappa del mondo* — e l'inglese ci mette il nome del mezzo.

**Il nome del mezzo è già il nome dell'oggetto**, dieci righe più su nella
stessa scheda: ripeterlo nel referto lo spreca. E la distinzione che il
giapponese fa — mare contro terra — è quella che al giocatore serve, perché dice
**dove** il mezzo si può usare. Due rese per dieci firme.

### ⚠️ Tre righe dove l'inglese aggiunge, e si tace

- **`:52520`**, la stregoneria: l'inglese dice «5 spell bonus points», il
  giapponese solo スペルボーナス. Il numero non è nel giapponese, e `text.hsp`
  ha già una riga che lo dice quando succede.
- **`:81402`**, la licenza del Vuoto: l'inglese dice **dove** sta il Vuoto
  («at South-West North Tyris»), il giapponese no.
- **`:89493`**, la mappa del tesoro: «from sources unknown» è dell'inglese.

### ⚠️ Le stelle non si scrivono

Il giapponese di `:81743` dice 「☆のついた武器防具」 e quello di `:130246`
parla degli oggetti col ★. **`☆` e `★` sono a doppia larghezza in CP932** e li
boccia `guardie`; nel dizionario non ce n'è **nemmeno uno** su 23.469 rese. Si
scrive quel che la stella significa, e in tutt'e due i casi lo dice l'inglese:
le due qualità che ☆ marca sono `_quality` 4 e 5, «eccezionale» e «celestiale»
(`glossario.md`), e ★ marca gli **artefatti**.

ⓘ **I termini già fissati altrove, e qui si ubbidisce:** 巻物 → «pergamena» e
権利書 → «atto» (i nomi degli oggetti in `db_item.hsp`), 呪い → «la maledizione»,
信仰 → «la Fede» (`chat.hsp`), 潜在能力 → «il potenziale», マテリアル →
«materiale», スペルボーナス → «punti bonus per gli incantesimi»
(`proc.hsp`), 収容所 → «accampamento», e `MP` è **invariato**
(`invariati.md:79`, che tiene `HP/MP` insieme).
"""
