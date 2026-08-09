# Fase 2 — i nomi di creatura

Scritto il 2026-08-09, tredicesima sessione, **prima di tradurre una riga**.
Il blocco era descritto in `contratto-nomi.md` §5 come atomico e costoso.
Misurandolo si è scoperto che è atomico per una ragione **diversa** da quella
scritta, e che costa **meno** su un fronte e **molto di più** su un altro.

## La misura

| cosa | dove | quante |
|---|---|---|
| nomi di creatura | `db_creature.hsp`, `cdatan(CDATAN_NAME, rc) = lang(…)` | **1.131 firme** |
| stringhe di evoluzione | `action.hsp`, `evold` / `evname` | **373 firme** (424 assegnazioni) |
| voce delle creature | `db_creature.hsp`, il resto delle `lang()` | ~270 firme, vengono col file |
| **totale del file** | `db_creature.hsp` | **1.405 firme**, 2.744 occorrenze |

⚠️ `db_creature.hsp` **non è nella catena**: non sta nelle 8.624 firme di
Fase 1, e come le 2.555 descrizioni d'oggetto vuole un **conteggio proprio**.
Sommarlo al totale di oggi produrrebbe una percentuale che non serve a nessuna
decisione — vedi [[percentuale-senza-denominatore]].

## Correzione a `contratto-nomi.md` §5

Il contratto dice:

> un salvataggio esistente contiene i nomi **inglesi**: tradurre
> `db_creature.hsp` non li rinomina, e **l'evoluzione dei nemici smette di
> riconoscerli**.

**La seconda metà è troppo forte.** L'idoneità all'evoluzione non passa dal
nome: `action.hsp:16604` e i suoi fratelli la decidono su
`cdata(CDATA_ID, tc)`, su `cdata(CDATA_EVOLUTION_STAGE, tc)` e sull'oggetto
usato. Il nome non entra da nessuna parte in quella catena.

`evold` e `evname` servono a una cosa sola: **riscrivere la stringa del nome**
già salvata (`action.hsp:18640-18646`), cercando `evold` come prefisso o come
suffisso e sostituendolo con `evname`.

> Su un salvataggio esistente l'evoluzione **funziona**: statistiche, stadio e
> grafica cambiano. Fallisce **solo la rinomina**, e il compagno resta col nome
> inglese. È un difetto estetico e permanente, non un sistema rotto.

Questo non toglie l'atomicità, la sposta: se si traduce `db_creature.hsp` e non
`evold`/`evname`, **le creature nuove** smettono di essere rinominate, e
falliscono in silenzio. L'atomicità serve a proteggere le partite future, non
quelle passate.

## Il vero prezzo: la chirurgia sulla stringa

Ecco cosa fa davvero la rinomina (`action.hsp:18640`):

```hsp
if ( strmid(cdatan(CDATAN_NAME, tc), 0, strlen(evold)) == evold ) {
    cdatan(CDATAN_NAME, tc) = evname + strmid(cdatan(CDATAN_NAME, tc), strlen(evold), …)
} else {
    if ( strmid(cdatan(CDATAN_NAME, tc), strlen(…) - strlen(evold), strlen(evold)) == evold ) {
        cdatan(CDATAN_NAME, tc) = strmid(cdatan(CDATAN_NAME, tc), 0, strlen(cdatan(CDATAN_NAME, rc)) - strlen(evold)) + evname
    }
}
```

Due rami: **prefisso**, e se non attacca, **suffisso**. In inglese il
qualificatore sta davanti, quindi in pratica gira quasi sempre il ramo del
prefisso.

⚠️ **In italiano il qualificatore sta dietro, quindi il ramo comune diventa
quello del suffisso — ed è il ramo che ha un difetto.** Alla riga 18644 la
lunghezza da tagliare si calcola su `cdatan(CDATAN_NAME, **rc**)`, non su `tc`.
Verificato: in tutta `*act_use` (che comincia a `action.hsp:6680`) `rc` non
viene mai assegnato, e nemmeno `*charaRefresh` (`screen.hsp:8208`) lo assegna:
al momento del taglio `rc` porta il valore lasciato da un'operazione
precedente, cioè **la lunghezza del nome di un'altra creatura**.

> È un difetto di upstream che l'inglese quasi non incontra, e che l'italiano
> incontrerebbe come caso normale. Non è un rischio della traduzione: è un
> rischio che la traduzione **sveglia**.

Cura prevista: una **toppa** su quella riga, `rc` → `tc`. È fuori da `lang()`,
sta in un file del sorgente pinnato e ha aggancio unico: esattamente la forma
che il generatore delle toppe pretende.

## La seconda difficoltà: i tagli non cadono dove serve

La chirurgia taglia sul **confine della stringa**, non sul confine sintattico.
La coppia d'esempio (`action.hsp:16657`):

```
evold  = "younger cat sister"   →  evname = "Cat Princess"
```

in inglese sostituisce tutta la testa e il risultato è pulito. In italiano
«sorella gatta minore» e «principessa gatta» non condividono né un prefisso né
un suffisso utile: la sostituzione o non attacca, o produce un ibrido.

Va deciso **prima di tradurre**, e la decisione è di disegno, non di lessico:

1. **rendere le coppie sostituibili**, cioè scegliere le rese italiane in modo
   che `evold` sia davvero un suffisso di ogni nome che lo contiene. Vincola il
   lessico dei nomi, e va verificato a macchina su tutti i 1.131;
2. **spegnere la chirurgia con una toppa** e riscrivere il nome intero, il che
   vuole una mappa `evold → nome nuovo completo` che oggi non esiste;
3. **lasciare i nomi di creatura invariati**, come già si fa per gli artefatti
   opachi, e tradurre solo la voce e le descrizioni.

⚠️ Nessuna delle tre è ovvia, e la seconda e la terza cambiano lo scopo della
Fase 2. Questa è la prima domanda da sciogliere alla prossima sessione, e
**non è una domanda di traduzione**.

## Cosa questo piano non decide

- `orc` contro `ogre`, che tiene in ostaggio `<Pants of Ogre>`;
- il genere e il plurale dei 1.131 nomi, che la macchina di Fase 1 sa già
  portare (`ioriginalnamearticolo` e fratelli) ma che qui vanno su un campo
  diverso, `cdatan`;
- le 59 risposte del quiz rinviate, che si sbloccano **dopo**, non insieme.

## L'ordine consigliato

1. sciogliere la domanda della chirurgia (le tre strade qui sopra);
2. toppa `rc` → `tc`, **prima** di tradurre: è una correzione che vale anche
   per il gioco inglese, e va collaudata da sola;
3. mettere `db_creature.hsp` nella catena, con conteggio proprio;
4. tradurre i 1.131 nomi e i 373 di `action.hsp` **nello stesso commit**;
5. collaudo in gioco **su un salvataggio nuovo**, perché è l'unico dove la
   rinomina può attaccare;
6. solo dopo, le 59 rinviate del quiz.
