# Fase 6 — l'altra metà del gioco di carte: schede, etichette, battute

Aperta nella **centotrentasettesima** sessione, 2026-09-03.

## Il perimetro non è 198: è 231

Il censimento della 135ª contava **198 stringhe scoperte** su quattro file. Sono
giuste, ma non sono tutte: `copertura.py` ne ha **32 che non può vedere**, e
stanno tutte in mezzo a queste.

    tcg_skill.hsp   142   76 schede di carta, 35 battute, 17 randomchat, 8 tracce, 4 sparsi, 2 markerword
    tcg.hsp          52   27 etichette e menu, 12 sparsi, 10 tracce, 3 schede
    tcg_custom.hsp    4   3 tracce e la pezza «the The»
    db_card.hsp       1   una descrizione di sapore rimasta giapponese
    ─────────────────────
                    199   dichiarate
    + 31 etichette dei bit  ⚠️ invisibili al censimento
    +  1 «Bits:  »          ⚠️ invisibile al censimento
    ─────────────────────
                    231

### ⚠️⚠️ Perché 32 stringhe a schermo non le contava nessuno

`copertura._PROSA` è `[A-Za-z]{3}[a-z]*\s+[A-Za-z]`: pretende **due parole**.
`"Regeneration "` è una parola sola seguita da uno spazio, e dopo lo spazio non
c'è nessuna lettera — quindi non aggancia. Lo stesso per `"Flying "`,
`"Haste "`, `"Immune "` e le altre ventotto, e per `"Bits:  "`.

Non sono identificatori: `tcg.hsp:1522-1560` le **appende** alla riga dei bit
della scheda di ogni carta, che il giocatore legge premendo `c`. Il glossario
della 136ª le aveva già decise quasi tutte, e la ripresa le dava per «Fase 6» —
ma il numero che il progetto usa per sapere quanto manca non le contava.

⭐ **La lezione è più larga di queste 32.** Un'euristica che cerca la prosa non
vede le **etichette**, e un'interfaccia è fatta di etichette. Il buco vale per
tutto il sorgente, non solo per `tcg.hsp`: quante siano altrove **questa fase
non lo misura**, e resta una cosa aperta dichiarata, non un lavoro fatto a metà
in silenzio.

---

## L'ordine dei lotti lo decide il comportamento, non la dimensione

La 136ª ha imparato che le toppe che proteggono un comportamento vanno **prima**
delle rese, e che proteggere l'inizio e la fine non basta: in una fase lunga il
mezzo dura sessioni. Qui i vincoli sono censiti **prima di tradurre una riga**.

### I vincoli trovati, e chi li scrive

| stringa | scritta da | **cercata da** | effetto se si traduce solo la scrittura |
|---|---|---|---|
| `"Bits:  "` | `tcg.hsp:1522` | `:1470`, `:4625`, `:4630` | ⚠️⚠️ **la riga dei bit sparisce da ogni scheda** |
| `"Effect: "` | già reso (toppa 1230) | `tcg.hsp:4628` | l'export `TCG_card_list.txt` non toglie più il prefisso |
| `"ragon"` | `db_card.hsp` (nomi) | `tcg_skill.hsp:4960/:4972/:5003` | ⚠️ già spento da fasi precedenti — fuori perimetro |
| `"the The"` | — | `tcg_custom.hsp:4566` | non aggancia più: i nomi sono italiani |
| nome creatura | `db_card.hsp` | `tcg_custom.hsp:208/:209/:1516/:1519` | regge: la scheda porta il nome reso |

⚠️ `"Bits:  "` ha **due spazi**, e i due spazi sono portanti: chi la cerca la
cerca esatta. La resa deve avere la stessa forma in tutt'e quattro i siti, e un
cancello lo pretende.

### I lotti

- **A — i vincoli e le 32 invisibili.** `"Bits:  "` in tutt'e quattro i siti, le
  31 etichette dei bit, e la toppa dell'operando di `:4628`. Sono toppe, non
  voci di dizionario: sono letterali nudi dentro il codice, come le altre 103
  di `tcg.hsp`.
- **B — le 27 etichette e i menu di `tcg.hsp`.** `[Command Card]`,
  `<Mage Guild>`, `Sort by: Cost`. Si **appendono alla stessa stringa** delle
  schede, quindi il loro glossario è quello del lotto C.
- **C — le 76 schede di `tcg_skill.hsp`.** Schede intere scritte a mano dentro
  il codice: nome, `No.???`, sapore, `Rare:`, etichette, `Effect:`.
  ⚠️⚠️ **Il vocabolario della scheda è già italiano** nel ramo dinamico, e le 76
  devono combaciare, o metà gioco dirà `Rare:` e metà `Rarità:`:

      "  No."    -> "  N."          " <Land>"  -> " <Terreno>"
      "  Rare:"  -> "  Rarità:"     " <Spell>" -> " <Magia>"
      "Data: "   -> "Dati: "        "Effect: " -> "Effetto: "

- **D — 35 battute e 17 randomchat.** Prosa, la parte facile.
- **E — gli sparsi**: 12 di `tcg.hsp`, la pezza `the The`, la descrizione
  giapponese di `db_card.hsp:2695`.
- **Esenti — 18 tracce di debug** (`proctcg`, `proc`, `poptext@tcg`): non
  arrivano a schermo.

---

## La chiave: il letterale, non la costante e non la riga

La Fase 5 aveva una chiave naturale — il nome della costante di `effdesc@tcg`.
Qui non c'è: `carddetailneff@tcg(cextra@tcg)` ha l'indice **variabile**, e il
valore a volte è concatenato (`tcg_skill.hsp:931`).

E non può essere `file:riga`, che è quel che la Fase 4 ha imparato a proprie
spese: la riga **si sposta sotto una resa**.

⭐ Resta il letterale inglese stesso, che su questi quattro file è distinto
(76 schede su 76 siti). È la stessa `firma` che il dizionario generale usa da
sempre, applicata a letterali che non stanno dentro `lang()`.

---

## Come si saprà che è finita

    copertura            7 fronti / 211 -> 3 fronti / 12
    schede --referto     76 su 76, vocabolario che combacia col ramo dinamico
    toppe                1.230 -> ~1.265, tutte agganciate
    "Bits:  "            4 siti su 4 concordi, con la prova al contrario
    pytest               verde DOPO i documenti, non prima

⚠️ Nessuno di questi numeri si eredita da qui: si rilanciano.
