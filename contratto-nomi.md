# Il contratto dei nomi

Scritto il 2026-08-07, dopo il quarto lotto del Task 7 e il primo collaudo in
gioco. Non è un piano di traduzione: è il **contratto** che i nomi di creature e
oggetti devono rispettare, e senza il quale ogni frase che li cita è un debito.

## Perché esiste

Al quarto lotto le voci rinviate erano passate da 0 a 157, e quasi tutte per la
stessa ragione: citavano un nome di creatura o di oggetto. Il quiz è fatto di
nomi; i modificatori di qualità pure; `elename()` pure.

La pratica dice che lo strato dei nomi viene **prima** del testo che li cita —
altrimenti ogni frase tradotta è una dipendenza in avanti. Il progetto l'aveva
già fatto bene una volta, col Task 5: sei termini fissati prima dei lotti che li
contenevano. I nomi sono la stessa categoria, ma erano finiti in Fase 2 perché
stanno in **file** diversi. Le fasi sono ordinate per visibilità, e la visibilità
non coincide con le dipendenze.

C'era anche un secondo argomento, più concreto: tirando avanti così,
`avanzamento.md` avrebbe finito per dire `text.hsp 100%` mentre il giocatore
legge nomi di mostri e oggetti in inglese ovunque — cioè ciò che in un roguelike
si legge più spesso. Una metrica che mente è peggio di una che manca.

## 1. Dove stanno i nomi — misurato

| | dove | forma | il dizionario li vede? |
|---|---|---|---|
| **creature** | `db_creature.hsp` | dentro `lang()` | **sì** |
| **oggetti** | `db_item.hsp` | dentro `if ( jp ) … else …` | **no** |

I nomi degli oggetti sono **1.321**, tutti in una sola forma canonica:

```
if ( jp ) {
    ioriginalnameref(ITEM_ID_BANANA) = "バナナ"
}
else {
    ioriginalnameref(ITEM_ID_BANANA) = "banana"
    ioriginalnameref2(ITEM_ID_BANANA) = ""
}
```

Verificato con una espressione regolare sola: **1.321 su 1.321, zero eccezioni**.
Gli altri 1.581 `if ( jp )` del file non riguardano i nomi.

**298 si compongono** come `ioriginalnameref2 + " of " + ioriginalnameref`
(`init.hsp:186-189`): `deed of camp`, `scroll of harvest`, `high potion of agony`.
Il `" of "` è cablato **fuori da `lang()`**.

## 2. Come li raggiungiamo — un secondo tipo di sito

**Decisione presa.** `siti()` impara a riconoscere la forma canonica dei nomi
oltre a `lang()`. I 1.321 nomi diventano voci di dizionario **normali**: firma,
`verifica`, coda di ritraduzione di SPEC 3.1, e soprattutto **la prova d'identità
li attraversa**.

Le alternative e perché no:

- **1.321 toppe.** Le toppe agganciano la riga intera e sono nate per una decina
  di casi eccezionali. La prova d'identità non ci passa: metterebbe 1.321 nomi
  fuori dalla garanzia byte per byte, che è la cosa che tiene in piedi il
  progetto. E nessuna coda di ritraduzione.
- **Un dizionario separato.** Due catene, due formati, due verifiche, e la prova
  d'identità da riscrivere. Isolato sì, ma il costo si paga per sempre.

È il cambiamento più grosso alla catena dalla Fase 0, e **vuole i suoi test**:
la scansione nuova deve essere sicura quanto quella di `lang()`, e la prova
d'identità è il giudice — un dizionario che traduce ogni nome in sé stesso deve
riprodurre `db_item.hsp` byte per byte.

**Fatto il 2026-08-07.** `siti()` riconosce le sette righe del blocco e ne emette
due siti, uno per `ioriginalnameref` e uno per `ioriginalnameref2`, entrambi col
giapponese del blocco. Il riconoscimento è tollerante sull'indentazione e severo
sulla struttura: pretende l'ordine delle righe e **lo stesso identificatore** in
tutte e quattro le assegnazioni, così i 1.581 `if ( jp )` che non sono nomi non
si agganciano.

Il giudice ha risposto: **72/72 byte per byte, 27.813 sostituzioni** contro le
26.206 di prima — esattamente i 1.607 siti nuovi, senza toccarne uno dei vecchi.
I test sono 194 (erano 180), e quelli nuovi stanno in `strumenti/tests/test_nomi.py`.

Il riconoscitore **per riga** (`avvio_nome`) aggancia anche il ramo giapponese,
perché le due righe hanno la stessa forma. È voluto: serve solo al riscontro
strutturale di `applica.py`, che confronta la riga prodotta con quella di
partenza e non ha bisogno di sapere quale sia — la riga giapponese non viene mai
toccata e si rilegge identica. Chi deve sapere **quale** letterale è traducibile
guarda il blocco intero, e quello lo fa `siti()`.

## 3. Ordine di aggettivo e nome — si riordina dove si compone

**Decisione presa.** In inglese l'aggettivo precede (`clear potion`), in italiano
segue (`pozione trasparente`). Non si piega il lessico all'ordine inglese: si
sposta la concatenazione, perché **dove i pezzi si uniscono è codice nostro**.

Due casi, due strumenti:

- **dentro una dinamica** l'espressione italiana la scriviamo noi, quindi basta
  scriverla nell'ordine giusto:

  ```
  EN  his(cc) + " " + elename(ele) + " " + _melee(2, …)
  IT  "il suo " + _melee(2, …) + " " + elename(ele)
      → «il suo artiglio ardente»
  ```

- **fuori da `lang()`** serve una toppa, come già per `"the "`:

  ```
  init.hsp:189   ref2 + " of " + ref   →   ref2 + " di " + ref
  ```

La conseguenza sul lessico è che **l'aggettivo torna libero**: non serve più
sceglierlo invariabile per forza. Resta però la regola imparata al collaudo — un
aggettivo che esce attaccato a un nome di genere ignoto va invariabile lo stesso
(vedi `guida-stile.md`, «l'etichetta si legge dove esce»).

## 4. Articolo e genere — chi li porta

Confermata ed estesa la decisione della quarta sessione: **l'articolo lo porta il
nome**, perché in italiano dipende da genere ed elisione — «il putit», «lo
gnomo», «l'orco» — e questo si sa per nome, non per regola.

- `init.hsp:1718` toglie già il `"the "` inglese davanti ai nomi dei PNG (toppa
  esistente);
- lo stesso vale per gli oggetti: gli articoli e i contatori inglesi si compongono
  in `item_func.hsp` (`itemname()`), che ha un ramo `if ( jp )` proprio — quindi
  il ramo inglese è il posto dove va l'italiano.

## 4-bis. Il plurale — due macchine, non una

Scoperto il 2026-08-07 leggendo `item_func.hsp`, e non previsto da questo
documento. Il plurale in inglese si fa **col suffisso**, e il file lo fa in due
punti diversi:

| | dove | su cosa | quanti oggetti |
|---|---|---|---|
| parola-contatore | `1259-1285` | `scroll` + `"s "`, `dish` + `"es "` | i **298** composti |
| nome dell'oggetto | `1840-1932`, 91 righe, 47 `case ITEM_ID` | `long sword` + `"s"` | i **1.023** semplici |

**In italiano il plurale non si deduce**: paio/paia, asse/assi, e l'aggettivo si
accorda col nome (spada lunga → spade lunghe). Quindi è un **dato**, scritto una
volta per nome nel campo `plurale` del dizionario, e portato fino al gioco da
due array nuovi che `applica_plurali` popola accanto al singolare:

```
ioriginalnameref(ITEM_ID_SCROLL_HARVEST)      = "raccolto"
ioriginalnamerefplur(ITEM_ID_SCROLL_HARVEST)  = "raccolti"
ioriginalnameref2(ITEM_ID_SCROLL_HARVEST)     = "pergamena"
ioriginalnameref2plur(ITEM_ID_SCROLL_HARVEST) = "pergamene"
```

⚠️ **Il nome si flette dove si concatena, non dopo.** Il primo disegno voleva
sostituire il pluralizzatore di riga 1842, ma lì `locvar_itemowner_s` non è il
nome: è la stringa già composta — benedizione, materiale, nome dell'ego, il nome
vero, e in coda i titoli fra `<>`. L'inglese può appiccicare la `s` in fondo
perché il sostantivo testa sta alla fine; in italiano sta **in mezzo**.

I punti dove il nome si concatena sembrano sei, ma **tre sono morti**: due stanno
dentro blocchi `/* ORIGINAL */`, cioè in commento, e uno è nel ramo `jp`. I vivi
sono `item_func.hsp:1731, 1747, 1770`.

Un plurale che manca **non è un errore a valle**: `applica_plurali` lo salta e il
gioco ripiega sul singolare. Serve perché i 1.023 plurali arrivano a lotti, e lo
stato intermedio deve restare leggibile.

⚠️ Ma il ripiego è per i nomi **non ancora tradotti**. Su un nome già tradotto
scriverebbe «2 spada lunga» per sempre, in silenzio, e il momento della
traduzione è il solo in cui qualcuno sta guardando quel nome. Perciò
`verifica.py` **pretende** il `plurale` su ogni nome con `it` pieno (dal
2026-08-07: prima non guardava il campo, e un lotto a metà passava senza un
fiato). Se plurale e singolare coincidono, si riscrive uguale: la coincidenza si
dichiara, non si indovina.

Le otto toppe sono generate prendendo `cerca` dal sorgente pinnato, non scritte a
mano, e lo strumento rifiuta di emetterne una il cui blocco non compaia
**esattamente una volta**. Ha già impedito un errore: la riga da spegnere a 1842
compare due volte, perché upstream tiene la versione originale in commento poco
sopra.

## 5. Il prezzo dei nomi di creatura: i salvataggi

⚠️ `db_creature.hsp` non si limita a dichiarare i nomi: fa
`cdatan(CDATAN_NAME, rc) = lang(…)`, cioè li **scrive nei dati del personaggio**,
che finiscono nel salvataggio.

Sono quindi la **stessa classe** di `CDATAN_NEWSEX`, e sono esattamente ciò
contro cui si confrontano i **424 `evold`/`evname`** di `action.hsp` (vedi
`invariati.md`). Le conseguenze:

- un salvataggio esistente contiene i nomi **inglesi**: tradurre `db_creature.hsp`
  non li rinomina, e l'evoluzione dei nemici smette di riconoscerli;
- `evold`/`evname` vanno tradotti **nello stesso momento** di `db_creature.hsp`,
  mai prima e mai dopo, o il confronto fallisce **in silenzio**.

Questo non è un dettaglio di implementazione: è il motivo per cui i nomi delle
creature sono un lavoro atomico e non incrementale.

## 6. Cosa si sblocca

Le 157 voci rinviate di `rinviate.jsonl`, per gruppo:

| gruppo | voci | sbloccato da |
|---|---|---|
| modificatori di qualità (`_bookself`, `_furniture`, `_weight`) | 35 | §3 e §4 |
| nomi casuali degli oggetti (`_namepotion` e fratelli) | 33 | §3 e §4 |
| `elename()` | 20 | §3 (con `proc.hsp`) |
| nomi di creatura e oggetto nel quiz | 59 | §1 e §2 |
| nomi di magia nel quiz | 4 | con `skill.hsp` |
| parti meccaniche | 6 | §1 e §2 |

## 7. Cosa questo contratto **non** decide

- **Non traduce nessun nome.** Il termbase vero è lavoro suo.
- **Non decide l'ordine delle fasi.** Dice solo che i nomi sono una premessa di
  ciò che li cita, non una conseguenza — come `init.hsp` si è rivelato una
  premessa del registro nella quarta sessione.
- **Non tocca `data/*.txt`**, che restano Fase 4 e vogliono una catena diversa.
