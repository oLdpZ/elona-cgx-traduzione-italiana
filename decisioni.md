# Decisioni

Scelte non ovvie e il perché. Le decisioni numerate stanno in `SPEC.md` §10;
qui c'è il ragionamento che non ci stava in una riga di tabella, e le domande
ancora aperte.

---

## Come è andata la Fase 0

La catena `estrai → verifica → reimporta → applica` esiste, è coperta da **83
test** ed è stata provata end-to-end sul sorgente vero. Ma il **cancello vero
della Fase 0 non è ancora passato**: ricompilare l'eseguibile da sorgente non
modificato richiede la GUI dell'SDK HSP 3.4. Finché non passa, quella che
abbiamo è una *catena verificata*, non un *gioco verificato*.

### La prova che conta più di tutti i test

Un **dizionario identità** — ogni stringa tradotta in sé stessa — deve
riprodurre i file byte per byte. È la verifica più forte disponibile su questa
catena, perché non dipende da quali casi qualcuno si è ricordato di scrivere:
copre ogni sito del corpus reale.

Esito: **73 file su 73 identici**, con 22.602 sostituzioni eseguite.

È stata questa prova, e non i test, a trovare i due difetti più gravi del
progetto.

### I quattro difetti che i test non hanno visto

Tutti e quattro producevano **corruzione silenziosa**: virgolette pari,
parentesi bilanciate, nessun errore, sorgente rotto.

1. **Il parser era cieco all'escape `\"`.** 195 righe del sorgente lo usano.
   Costo misurato: 11 `lang()` perse, 295 voci con l'inglese mutilato, e 5 span
   sbagliati su cui `applica.py` sostituiva facendo **sparire dal sorgente** una
   chiamata `_onii(cdata(...))` e un'intera coppia `lang()`. Perdita di logica di
   gioco, non di testo.
2. **`e_dinamica` cercava il `+` anche dentro il testo.** 163 stringhe statiche
   contengono un `+` (`"Enchantment Bonus + 4"`, `"RES+ magic"`) e venivano
   classificate dinamiche, il che faceva finire l'italiano **nudo** nel sorgente.
   86 in file di Fase 1.
3. **Statiche avvolte in una chiamata.** `lang("…", cnvtalk("Urchinn!"))` non ha
   un `+` di primo livello, quindi è statica — ma sostituire l'intero span fa
   sparire `cnvtalk`. Sono **3.499**, in due sole forme: `cnvtalk(` (3.423) e
   `cnven(` (76).
4. **Firme che collidono su espressioni diverse.** La firma si calcola sui soli
   letterali, quindi `name(gdata(GDATA_RIDER)) + " glare"` e
   `cdatan(CDATAN_NAME, ttc) + " glare"` condividono la chiave: la traduzione
   dell'una finirebbe sull'altra portandosi dietro **le variabili sbagliate**.
   Sono **77 firme**, 334 occorrenze.

I primi due sono corretti. Il terzo e il quarto sono **rifiutati con un errore
esplicito** che nomina file, riga, firma e causa: la catena si ferma invece di
corrompere. Non è la soluzione definitiva, è il rifiuto onesto.

### Perché rifiutare invece di risolvere

Il cancello della Fase 0 è «la catena non corrompe il sorgente», e rifiutare lo
soddisfa in modo dimostrabile. Il caso 4 in particolare è una modifica allo
schema della chiave, cioè a `SPEC.md` §3.2: va decisa a mente fredda, non
improvvisata dentro una correzione.

---

## Domande aperte, da decidere prima della Fase 1

### 1. La firma delle dinamiche deve includere l'espressione? — DA DECIDERE

Oggi `firma = sha1(giapponese + NUL + inglese)` usa i **soli letterali**. Per le
dinamiche questo fa collidere espressioni diverse che condividono il testo (77
casi).

Includere `en_grezzo` nella firma risolverebbe la collisione, ma renderebbe la
chiave più fragile ai cambiamenti a monte: qualunque ritocco all'espressione,
anche il rinominare una variabile, romperebbe la firma e manderebbe la stringa
in coda di ritraduzione anche se il testo non è cambiato.

**Va decisa adesso**, perché `dizionario/` è ancora vuoto e non c'è debito di
migrazione. Dopo la prima ondata di traduzioni la finestra si chiude.

### 2. Il rifiuto arriva troppo tardi nel ciclo

`estrai.py` emette comunque le 3.833 occorrenze dei casi 3 e 4 nei lotti, e
`verifica.py` non le segnala. Un traduttore le traduce, `reimporta` le accetta, e
solo `applica` esplode — abortendo l'intero build su un caso alla volta.

Il rilevamento va spostato a monte, in `estrai`/`verifica`, o le voci vanno
marcate nel lotto. Altrimenti si scopre il problema dopo aver tradotto.

---

## Rilievi parcheggiati

Reali ma non bloccanti, valutati e lasciati:

- `applica.py` importa ancora il privato `estrai._argomenti` per `_profilo`.
- `applica.main()` scrive i file uno alla volta: un errore lascia l'albero di
  build a metà. Innocuo perché `build/` è usa e getta, ma incoerente col rigore
  tutto-o-niente applicato a `reimporta`.
- Il controllo del caso 4 è saltato in silenzio se una voce di dizionario
  ritoccata a mano è priva di `en_grezzo`: `verifica.py` lo pretende, ma
  `applica.main()` legge i `.jsonl` senza passare da `verifica`.
- `_letterali` conserva gli escape come `\"` invece che `"`: fedele e
  reversibile, ma chi traduce lo vede nel campo `en`. Da fissare nella guida di
  stile.

---

## Da portare nel piano della Fase 1

In quest'ordine:

1. Sostituzione dentro `cnvtalk(` / `cnven(` — **bloccante per la Fase 2**, ma è
   lavoro di poche righe: non è una famiglia aperta di involucri, sono due forme
   sole.
2. La decisione sulla firma delle dinamiche, §3.2 — **prima** che il dizionario
   si riempia.
3. Spostare a monte il rilevamento dei casi 3 e 4.
4. La whitelist `invariati.md` per la regola «identica all'inglese»: `SPEC.md` §7
   la promette ma non è implementata, e senza di essa i nomi propri e le sigle
   non hanno via d'uscita — il rischio concreto è che si aggiri la regola
   scrivendo traduzioni finte.
5. Il modo `verifica --dizionario` che confronta dizionario e sorgente e produce
   la coda di ritraduzione. `SPEC.md` §3.1 ne fa il cardine dell'architettura, ma
   non esiste: oggi una firma orfana viene solo contata da `applica`.
