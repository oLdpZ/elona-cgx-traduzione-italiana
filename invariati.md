# Invariati

Stringhe che restano identiche all'inglese **per scelta esplicita**, non perché
la traduzione è stata dimenticata. `verifica.py` legge questo file e non le
segnala.

Senza il file `verifica.py` si comporta come prima: è un'aggiunta, non un
requisito. Un progetto senza eccezioni è un progetto senza il file.

Il confronto è sulla **stringa intera** e sensibile alle maiuscole: una riga
qui copre `Vernis` come valore completo di `en`, non la parola `Vernis` dentro
una frase più lunga. Una frase che contiene un nome proprio si traduce
normalmente.

Una riga qui è una decisione: va motivata. Se il motivo non si riesce a
scrivere, probabilmente la stringa va tradotta.

| valore | motivo |
|---|---|
| Vernis | nome proprio di città, canone Elona |
| Palmia | nome proprio di città, canone Elona |
| Derphy | nome proprio di città, canone Elona |
| Noyel | nome proprio di città, canone Elona |
| Yowyn | nome proprio di città, canone Elona |
| Lumiest | nome proprio di città, canone Elona |
| Melugas | nome proprio di luogo, canone Elona |
| Larna | nome proprio di città, canone Elona; nome opaco, vedi «la regola dei nomi propri» in `glossario.md` |
| Arcbelc | nome proprio di luogo Elona+; nome opaco |
| Lesimas | nome proprio del dungeon sotto Vernis; nome opaco |
| Karma | termine acquisito in italiano |
| Mana | termine acquisito nei giochi di ruolo |
| * | simbolo, non testo: `text.hsp:12` lo stampa come marcatore. Non c'è niente da tradurre |

## Valori di dato, non testo — tradurli rompe i salvataggi

⚠️ Queste `lang()` non finiscono a schermo: sono i valori del campo
`CDATAN_NEWSEX`, **scritti** nei dati del personaggio (`chara.hsp:2790`,
`chara.hsp:4390`) e **riletti** come operandi di confronto (`init.hsp:1813-1823`,
dentro `he()`/`his()`/`him()`).

Tradurle sembra innocuo e non lo è: un salvataggio esistente contiene la stringa
inglese, il confronto col valore italiano fallisce, e il gioco sbaglia il genere
di ogni personaggio già creato. Il cancello della Fase 0 ha verificato proprio
che i salvataggi esistenti si carichino: questo lo vanificherebbe in silenzio.

| valore | motivo |
|---|---|
| male | valore di `CDATAN_NEWSEX`, non testo a schermo |
| female | valore di `CDATAN_NEWSEX` |
| none | valore di `CDATAN_NEWSEX` |
| hermaphrodite | valore di `CDATAN_NEWSEX` |
| male? | valore di `CDATAN_NEWSEX` |
| female? | valore di `CDATAN_NEWSEX` |
| trans-male | valore di `CDATAN_NEWSEX` |
| trans-female | valore di `CDATAN_NEWSEX` |

## Nomi di creatura riscritti nel salvataggio — non decidibili qui

⚠️ Trovate il 2026-08-07 misurando `Sister`. In `action.hsp` (Fase 1) ci sono
**424 assegnazioni** di `evname`/`evold`, il sistema di evoluzione dei nemici:
**232 valori `evold` distinti, 203 dei quali sono nomi di creatura letterali di
`db_creature.hsp`**, che è Fase 2.

Non sono testo e non sono nemmeno solo dati. Il codice fa chirurgia di stringa
sul nome memorizzato del personaggio:

```
if ( strmid(cdatan(CDATAN_NAME, cc), 0, strlen(evold)) == evold ) {
    cdatan(CDATAN_NAME, cc) = evname + strmid(cdatan(CDATAN_NAME, cc), ...)
```

`evold` è l'**operando** confrontato col nome che sta nel salvataggio; `evname`
è il pezzo che lo **sostituisce**, e quindi finisce a schermo come nuovo nome
della creatura evoluta. In inglese `evname` non è mai stampato direttamente:
l'unico `txt` che lo contiene (`action.hsp:18632`) lo ha solo nel ramo
giapponese.

Le conseguenze, nessuna delle quali si vede provandolo su una partita nuova:

- **vanno tradotti in blocco con `db_creature.hsp`**, mai prima: se `evold`
  diventa italiano e il nome della creatura no (o viceversa), il confronto
  fallisce e l'evoluzione smette di rinominare **in silenzio**;
- **rompono i salvataggi esistenti comunque li si tratti**, perché lì il nome
  memorizzato è già in inglese;
- la **prova d'identità non li prende**: come per `CDATAN_NEWSEX`, la forma
  resta giusta ed è il significato a rompersi.

Non li metto nella tabella sopra: dichiararli invariati deciderebbe di lasciare
i nomi delle creature in inglese per sempre, che è una decisione di Fase 2 e
non è stata presa. Restano segnalati da `verifica.py` come non tradotti, che è
il comportamento voluto finché la Fase 2 non li affronta.

Vedi [[stringhe-che-sono-dati]].

## Da decidere nel glossario

*Vuota dal 2026-08-07.* I cinque toponimi che stavano qui sono stati decisi con
«la regola dei nomi propri» di `glossario.md`: `Larna`, `Arcbelc` e `Lesimas`
sono saliti nella tabella degli invariati; `Port Kapul` → «Porto Kapul» e
`Cyber Dome` → «Cupola Cibernetica» si traducono e quindi qui non ci vanno.

La sezione resta perché il meccanismo serve: un candidato messo qui è segnalato
da `verifica.py`, così la decisione non passa inosservata.
