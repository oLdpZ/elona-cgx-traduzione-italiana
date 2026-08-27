# -*- coding: utf-8 -*-
"""110a - Lotto 007 di `db_item.hsp`: il rapporto dei MINERALI.

`FILTER_ORE`, `description(3)`: **33 righe del sorgente, 21 firme**. E' la
categoria col rapporto piu' alto fra righe e rese di tutto l'indice 3, e la
ragione sta in una sola famiglia.

### ⭐ LE DODICI GEMME DEI MESI: dodici righe, un giapponese

`:48808`-`:49508` sono granato, ametista, acquamarina, diamante, smeraldo,
alessandrite, rubino, sardonice, zaffiro, opale, topazio e lapislazzuli — le
pietre dei dodici mesi. Il giapponese scrive per tutte
「贈り物に適した宝石だ。」, *una gemma adatta a un regalo*, e l'inglese fa lo
stesso («a gem that would make a great gift»). **Il nome della pietra e' gia' il
nome dell'oggetto**, dieci righe piu' su nella stessa scheda: e' la stessa specie
dei dieci atti dei mezzi (108a) e delle sette tombe (109a). Una resa, dodici
firme.

### ⓘ Le due formule dei minerali grezzi

    〜の要素が含まれる鉱石だ。 -> Un minerale che contiene tracce di ...  (3)
    〜色をした鉱石だ。         -> Un minerale di colore ...              (4)

⚠️ La seconda copre bianco, giallo, rosso e arancione — cioe' mica, cristallo di
sole, cristallo di mana e cristallo di terra. Il **colore non dice a che cosa
serva** il minerale, e il giapponese non lo dice apposta: non e' una lacuna da
riempire con l'inglese, che infatti dice la stessa cosa.

### ⭐ Due termini che il lotto NON ha dovuto decidere

- **`:66140`, 「合成用のアイテムだ。」 -> «Un oggetto per la sintesi.»** — e' la
  stessa firma del lotto 006 (dodici materiali fra gli scarti), e la resa e' la
  stessa perche' e' la stessa riga di dizionario. ⓘ `_coerenza.py` lo conferma
  guardando fuori dal lotto;
- **`:117321`, 「模造品だ。」 -> «Una riproduzione.»** — `db_item.hsp` ha gia'
  「剣の模造品だ。」 -> «La riproduzione di una spada.» e 「狂戦士の模造品だ。」
  -> «La riproduzione di un berserker.», rese in una sessione precedente. La
  parola c'era: si e' cercata invece di sceglierla.

### ⚠️ Una riga dove l'inglese racconta e il giapponese no

`:82613`, il biglietto per il concerto: l'inglese dice che sono biglietti dati ai
musicisti promettenti e che c'e' chi li colleziona; il giapponese dice che il
foglio **non ha alcun effetto** e che conviene cercare un collezionista. Il fatto
che l'inglese aggiunge — a chi vengono dati — non c'e' nella fonte. Regola di
`decisioni.md`.

### ⓘ I termini, verificati nel dizionario

宝石 → «gemma» (`skill.hsp`, «si avvolge nel bagliore di una gemma») ·
メダル → «medaglietta» (`chat.hsp`, «Trovi una medaglietta!») ·
模造品 → «riproduzione» (`db_item.hsp`) · ルビナス → «rubynus» (`invariati.md`) ·
武具 → «armi e armature» (il dizionario tiene i due separati) ·
合成用アイテム → «oggetti per la sintesi» (`chat.hsp`).
"""
