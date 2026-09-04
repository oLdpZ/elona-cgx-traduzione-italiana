# Fase 6 — l'altra metà del gioco di carte: schede, etichette, battute

Aperta nella **centotrentasettesima** sessione, 2026-09-04.

## STATO: quattro lotti su cinque chiusi, 233 rese

    lotto A   ✅  32 etichette dei bit + "Bits:  " -> "Tratti:  "      toppe
    lotto B   ✅  21 etichette della scheda                             toppe
    lotto C   ✅  72 schede di carta scritte a mano   strumenti/schede.py
    lotto D   ✅  74 battute della nuvoletta       strumenti/dialoghi.py
                  (68 rese + 6 invariate, su 77 SITI — non le 52 di questo
                   piano: vedi qui sotto)
    lotto B2  ⬜  8 `Filter:` (+ 5 `Sort by:`) — vuole lo SCHERMO prima
    lotto E   🔶  24 toppe fatte; restano la pezza «the The» e
                  db_card.hsp:2695

    strumenti/schede.py + 19 prove   --estrai/--reimporta/--applica/--referto
    strumenti/dialoghi.py + 25 prove idem, piu' `--referto` sui siti
    dizionario/carte/schede.jsonl    72 rese
    dizionario/carte/dialoghi.jsonl  68 rese + 6 invariate
    toppe                            1.230 -> 1.293 -> **1.317** (24 del
                                     lotto E; il lotto D non ne usa nessuna)
    copertura                        7 fronti / 211 -> 118 -> 62 -> **31**
                                     scoperte, e i fronti sono **6**:
                                     `tcg_skill.hsp` e' passato a ESENTE,
                                     gli 8 che restano sono tracce di debug
    pytest                           921 -> 952 -> **982**
    in gioco                         eseguibile delle 18:10 del 04/09

⚠️⚠️ **Il lotto D non era 52: erano 77 siti.** Le 25 di differenza —
`"One!"`, `"AIEEE!!!"`, `"Cheapskate."`, `"Rent-free!"` — `copertura._PROSA`
non le vedeva, ed è lo stesso buco delle 58 etichette della 137ª. Il
riconoscitore nuovo parte da **chi parla** (`efllistaddchat`, e gli array che
qualcuno gli passa), non dalla forma della stringa. ⭐ Per questo `copertura`
cala di 56 e non di 77: il conto del fronte e quello del lavoro sono due misure
diverse, e vanno lette separate.

⚠️ **Tre cose sono andate diversamente da come le prevedeva questo piano**, e
stanno scritte in `decisioni.md` (137ª):

1. **Il perimetro era sbagliato in tutt'e due i versi.** Le 231 di questo piano
   erano 199 dichiarate + 32 invisibili; le invisibili vere sono **58**, e le
   schede sono **72**, non 76. Il conto è stato rifatto due volte, mai
   aggiustato.
2. **`carte --applica` e `scene --applica` cancellavano le toppe** che
   `applica.py` aveva appena messo. Non era nel piano perché nessuno lo
   sapeva: l'ha trovato il lotto C, che stava per introdurre lo stesso difetto
   su un file con 165 toppe.
3. **Il lotto B non si poteva rimandare dopo il C.** Il piano lo diceva ma per
   il motivo sbagliato: non è che le etichette «entrano nella stessa stringa»,
   è che 61 schede su 72 **contengono** `Rare:` e 23 contengono
   `[Command Card]`, quindi senza le decisioni di B il lotto C non aveva un
   vocabolario a cui obbedire.

---

## Il perimetro non è 198: è 231 (e neanche quello)

Il censimento della 135ª contava **198 stringhe scoperte** su quattro file.
Sono giuste, ma non sono tutte: `copertura.py` non può vederne altre **58** nel
solo `tcg.hsp`.

    tcg_skill.hsp   142 -> 72   72 schede rese dal lotto C
    tcg.hsp          52 -> 29   21 etichette rese dal lotto B, 2 schede dal C
    tcg_custom.hsp    4         3 tracce e la pezza «the The»
    db_card.hsp       1         una descrizione rimasta giapponese
    + 58 etichette invisibili al censimento (37 rese, 13 invariate, 8 da fare)

### ⚠️⚠️ Perché 58 stringhe a schermo non le contava nessuno

`copertura._PROSA` è `[A-Za-z]{3}[a-z]*\s+[A-Za-z]`: pretende **due parole**.
`"Regeneration "` ne ha una sola, e `"Filter: Attack   "` ne ha due ma coi due
punti attaccati alla prima — mentre `"Sort by: Attack   "`, una riga sotto
nello stesso menu, si vedeva.

⭐ **La lezione è più larga di queste 58.** Un'euristica che cerca la prosa non
vede le **etichette**, e un'interfaccia è fatta di etichette. Il buco vale per
tutto il sorgente: quante siano altrove **questa fase non lo misura**, e resta
una cosa aperta dichiarata, non un lavoro fatto a metà in silenzio.

---

## L'ordine dei lotti lo decide il comportamento, non la dimensione

La 136ª ha imparato che le toppe che proteggono un comportamento vanno **prima**
delle rese, e che proteggere l'inizio e la fine non basta. Qui i vincoli sono
stati censiti **prima di tradurre una riga**, ed è servito.

| stringa | scritta da | **cercata da** | esito |
|---|---|---|---|
| `"Bits:  "` | `tcg.hsp:1522` | `:1470`, `:4625`, `:4630` | ✅ tutt'e quattro insieme, con cancello |
| `"Effect: "` | toppa 1230 | `tcg.hsp:4628` | ✅ toppato |
| `"\nEffect: "` | `tcg_skill.hsp:2003` | — | ✅ toppato ⚠️ ma lì non c'è `talk_conv` |
| `"ragon"` | `db_card.hsp` | `tcg_skill.hsp:4960/:4972/:5003` | ⬜ fuori perimetro |
| `"the The"` | — | `tcg_custom.hsp:4566` | ⬜ lotto E |
| nome creatura | `db_card.hsp` | `tcg_custom.hsp:208/:209/:1516/:1519` | ✅ regge |

⚠️ `"Bits:  "` ha **due spazi** e sono portanti: chi la cerca la cerca esatta.

---

## La chiave: il letterale, non la costante e non la riga

La Fase 5 aveva una chiave naturale — il nome della costante di `effdesc@tcg`.
Qui non c'è: `carddetailneff@tcg(cextra@tcg)` ha l'indice **variabile**, e il
valore a volte è concatenato.

E non può essere `file:riga`, che la Fase 4 ha imparato a proprie spese: la
riga **si sposta sotto una resa**.

⭐ Resta il letterale inglese, che su questi file è distinto: **72 su 72**.

---

## Come si saprà che è finita

    copertura            7 fronti / 118 -> 3 fronti / ~12
    schede --referto     72 su 72, vocabolario che combacia col ramo dinamico
    toppe                1.293 -> ~1.310, tutte agganciate
    "Tratti:  "          4 siti su 4 concordi, con la prova al contrario
    pytest               verde DOPO i documenti, non prima

⚠️ Nessuno di questi numeri si eredita da qui: si rilanciano.
