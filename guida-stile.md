# Guida di stile

Le regole specifiche di questo gioco. Quelle che valgono per l'universo Elona si
ereditano dal progetto gemello `Elin - Traduzione Italiana`; quelle che valgono
per il motore no — lì i segnaposto sono `#1` e i tag sono Unity, qui i
segnaposto sono espressioni HSP.

## Registro: terza persona, non «tu»

**Le righe che parlano di un personaggio vanno alla terza persona singolare del
presente indicativo.** Non è una preferenza: è l'unica forma che regge sia il
giocatore sia un PNG senza accordo di genere.

Il motivo sta in `init.hsp:1699`. `name()` risolve **da sé** chi è il soggetto:

```hsp
#defcfunc name int name_arg1
    if ( name_arg1 == CHARA_PLAYER ) {
        return lang("あなた", "you")              // il giocatore
    }
    ...
    return "the " + cdatan(CDATAN_NAME, name_arg1)  // un PNG
```

Quindi **una sola `lang()` serve entrambi**. Il caso canonico, `text.hsp:3137`:

```
name(X) + " lose" + _s(X) + " patience."
   →  "you lose patience."   /   "the putit loses patience."
```

L'inglese se la cava con `_s()`, che è morfologia. L'italiano non ha quel
trucco, e `_s()` va tolta (la blocca `verifica.py`): resta una forma sola, e la
seconda persona non regge.

- «perdi la pazienza» → *«il putit perdi la pazienza»* ✗
- «perde la pazienza» → «il viandante perde la pazienza», «il putit perde la
  pazienza» ✓

Sui sei file di Fase 1: 1.522 dinamiche, **901 usano `name()`**, **472
contengono un marcatore di morfologia inglese** — cioè sono dimostrabilmente
condivise. Non è un caso limite.

**La prova pratica:** se l'espressione contiene `name(...)`, `he(...)`,
`his(...)`, `him(...)` o una funzione di morfologia, la riga è condivisa e va in
terza persona. Se il gioco parla **a te** e basta — rifiuti, avvisi, domande,
interfaccia, menu — resta il «tu»: «Non hai abbastanza oro», «Sei sicuro?».
Quelle righe non hanno un gemello con un PNG al posto tuo, quindi non producono
nessuno stacco.

**Mai un aggettivo o un participio riferito al giocatore o a `name()`:** il
genere non si conosce. `You are too full` → «Non riesci a mangiare altro», non
«Sei sazio». `name(tc) + " has arrived"` → `name(tc) + " arriva"`, non «è
arrivato».

## Preposizioni davanti a un personaggio

`name()` restituisce un sintagma **con l'articolo** («il viandante», «il
putit»), e HSP non fonde la preposizione: `" a " + name(tc)` diventa «a il
viandante».

**Mai `a`, `di`, `da`, `in`, `su` davanti a `name(...)`.** Si rende il
personaggio complemento oggetto — `name(tc) + " kicks " + name(x)` → `name(tc) +
" prende a calci " + name(x)` — oppure si cambia soggetto alla frase. `per`,
`con` e `tra` non si fondono e vanno bene.

La ricerca da rifare a ogni lotto, sulla colonna italiana:

```
\b(a|di|da|in|su)\s*"\s*\+\s*name\s*\(
```

I nomi di oggetti (`itemname(...)`) e di zone non pongono lo stesso problema
solo quando la resa italiana non porta l'articolo: controllali caso per caso.

## Espressioni dinamiche

- **`name(...)`, `itemname(...)`, `cdatan(...)` sono contenuto: vanno
  conservate.** Perderle significa perdere il nome dal messaggio, e `verifica.py`
  lo blocca.
- **`_s(...)`, `is(...)`, `was(...)`, `your(...)`, `have(...)`, `does(...)` sono
  grammatica inglese e vanno tolte.** Restituiscono `"s"`, `"is"`, `"'s"`:
  scriverebbero inglese dentro la frase italiana. Riscrivi la frase in italiano
  corretto e concatena solo il contenuto. `verifica.py` le blocca se restano.
- **`he(...)`, `his(...)`, `him(...)` con due argomenti sono contenuto** (passano
  da `lang()`, `action.hsp:9631`) e vanno conservate; **con un argomento sono
  morfologia** e vanno tolte. La distinzione è per sito di chiamata, non per
  nome: `verifica.py` la applica già.
- **L'ordine dei pezzi si può cambiare.** `name(tc) + " drops " + itemname(ci)` →
  `name(tc) + " lascia cadere " + itemname(ci)`. È il vantaggio di tradurre
  l'espressione intera invece del solo testo.

## Ortografia

- **Nel dizionario si scrivono gli accenti veri**: `perché`, `più`, `è`. La
  degradazione ad apostrofo la fa `applica.py`. Scrivere `perche'` a mano è un
  errore, e `verifica.py` lo segnala. *(Qui la regola è l'opposto di Elin, che
  usa l'apostrofo tipografico `’`: là non c'è degradazione, qui sì.)*
- **Mai il carattere `"` in una traduzione statica**: chiuderebbe in anticipo la
  stringa HSP. Usa le virgolette tipografiche `“ ”`. **Mai `«»`**: CP932 non le
  sa codificare e `verifica.py` le rifiuta.
- Le maiuscole dei nomi di abilità e oggetti seguono l'inglese solo dove il gioco
  le usa come nomi propri.
- Materiali come complemento invariabile: «spada d'acciaio», mai «spada
  acciaiosa». Il motore compone i nomi a runtime e non sa accordare il genere.
- Nomi propri di luoghi e personaggi: vedi `invariati.md`. Una traduzione
  identica all'inglese fuori da quella lista `verifica.py` la segnala.

## Due dipendenze note, ancora aperte

1. **`init.hsp:1704` va tradotto prima delle dinamiche.** È il `lang("あなた",
   "you")` dentro `name()`: finché resta «you», nessuna forma verbale italiana
   regge entrambi i soggetti. Il piano lo collocava in Fase 4; è invece una
   premessa della Fase 1.

2. ~~L'articolo dei PNG non è raggiungibile dal dizionario.~~ **Risolto con una
   toppa** (`toppe.jsonl`). `init.hsp:1718` faceva `"the " + cdatan(...)`
   **fuori** da una `lang()`, dove il dizionario non arriva. Il prefisso ora si
   **toglie**, invece di sceglierne uno italiano: l'articolo italiano dipende da
   genere ed elisione, che si conoscono per nome e non per regola.

   **La conseguenza è una decisione di Fase 2:** l'articolo lo porta il nome
   della creatura in `db_creature.hsp` — «il putit», «lo gnomo», «l'orco».
   Vale per *ogni* uso di `cdatan()`, non solo per `name()`: prima di tradurre
   `db_creature.hsp` va guardato dove altro quei nomi compaiono (elenchi,
   negozi), perché lì l'articolo potrebbe non starci bene.

   `custom_dmgpop.hsp:224-231` *legge* la stringa `"the "` per toglierla dagli
   alias, ma è protetto da `instr(...) != -1`: senza `"the "` quel blocco è un
   no-op. Verificato: nessuna seconda toppa serve.

## Prima di reimportare

```powershell
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.verifica --dizionario
python -m pytest strumenti/tests -q
```

Tutti e tre verdi, sempre.
