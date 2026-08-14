# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-004: l'equipaggiamento che si rovina e i sei modi
buffi di morire (chara_func.hsp 4000-4999).

33 rese e **due rinviate**, su 35 voci. Due blocchi che non si somigliano:
`:4200`-`:4520` e' l'equipaggiamento aggredito dagli elementi (acido, fuoco,
gelo), `:4761`-`:4848` e' `txteledmg`, cioe' il verso che accompagna **ogni
danno elementale** del gioco.

⭐ **`txteledmg` ha tre gradini, e il secondo e' una CODA.** `txteledmg_arg1`
vale 0, 1 o 2: **ferito**, **ucciso da chi attacca**, **morto**. Il gradino 1 e'
scritto in giapponese **senza soggetto** — 「殺した。」, 「千切りにした。」,
「内部から崩壊させて殺した。」 — perche' si attacca in coda alla riga di sopra,
esattamente come le teste «… e» della 35ª ma dall'altro lato. ✅ La forma era
gia' decisa e sta nel dizionario: `chara_func.hsp:6843` rende 「殺した。」
«uccide sul colpo.», senza soggetto e senza pronome. Le altre code seguono:
«taglia a listarelle.», «fa crollare il corpo dall'interno.»
⚠️ **E una coda italiana non puo' portare il clitico**, che l'inglese invece si
concede (`him(txteledmg_arg3)`): «lo fa a listarelle» concorderebbe col
personaggio, «le» pure. Il possesso e l'oggetto restano impliciti, come fa il
giapponese.

⚠️ **Ma il gradino 1 non e' sempre una coda, e a deciderlo e' l'INGLESE.** A
`:4786` e `:4823` il giapponese e' senza soggetto («栗で抉り殺した。», 「人形に
変えて事実上殺した。」) ma l'inglese ha rimesso dentro un `name()`, e la rete 11
pretende che ci sia. Quindi la resa **nomina** — «Le castagne crivellano X a
morte», «trasforma X in una bambola» — e le due frasi convivono nello stesso
blocco con quelle che non nominano. Non e' un'incoerenza della traduzione: e'
l'inglese di monte che non e' coerente con se stesso, e la rete 11 la propaga.
💡 A `:4800` la strada e' il **`-ne` enclitico** della 37ª: l'inglese dice
`name(arg2) + " burst " + his(arg3) + " brain."` e in italiano «il cervello di
X» fonderebbe — «X **ne** fa scoppiare il cervello» tiene il nome di chi
attacca, l'invariabilita' e il possesso.

⚠️⚠️ **`:4520` e' la QUARTA riga del progetto che il dizionario non puo'
aggiustare, e la causa e' nuova: una `lang()` che `estrai.py` NON VEDE.**
`:4491` fa `locvar_item_cold_s = name(item_cold_arg1) + lang("の",
your(item_cold_arg1))`, e `:4520` usa quella variabile come **prefisso**. Il
ramo inglese di quella `lang()` e' **una sola chiamata di funzione, senza
letterale**, quindi non e' una firma: le firme di `chara_func.hsp` sono 342 e
`:4491` non e' fra loro. ⚠️ `your()` restituisce `"'s"` o `"r"`
(`init.hsp:2045`), fuori da `lang()`, e a schermo la riga italiana leggerebbe
«il putit**'s** …». ⚠️ E la resa non puo' rimediare **nemmeno nominando il
proprietario**, perche' il `name()` sta dentro la variabile e
`funzioni_di_contenuto` non lo vede: l'inglese dichiara `['itemname']` e una
resa che aggiungesse `name()` verrebbe bocciata dalla rete 11. E' la stessa
strettoia di `:3037` e di `proc.hsp:24107`, per una ragione terza.
✅ **Rinviata, e toppata in due punti**: `:4491` costruisce adesso un
**suffisso** («, che X porta addosso») invece di un prefisso possessivo, e
`:4520` lo mette in fondo. A schermo: «Il gelo manda in frantumi la spada, che
il putit porta addosso.», e «Il gelo manda in frantumi la spada.» quando
l'oggetto e' per terra e la variabile e' vuota. Il ramo giapponese di tutt'e due
le righe resta **identico**.
💡 **E' il rovescio del genitivo**: la strada di sempre — mai «di » davanti a
`name()` — qui non bastava a scriverla, perche' il pezzo da girare stava trenta
righe piu' su e in un'altra istruzione.

⚠️ **`:4369` e' commentata nel sorgente** (`; txt lang(...)`, dentro il blocco
del tag-team che il mod ha spento riga per riga col `;`). Rinviata come le
quattro di `db_creature.hsp` e `proc.hsp:4958`. 💡 La resa esisteva gia'
comunque — `proc.hsp:6481` e `text.hsp:13` dicono «X protegge Y.» — quindi non
si perde niente.

💡 **E l'equipaggiamento vuole il soggetto ELEMENTO, non il partitivo.**
`:4274`-`:4520` dicono tutte 「name の itemname は…」, e `itemname()` puo' essere
**plurale** («tre frecce»): una resa come «X si vede ridurre in cenere Y»
dovrebbe accordare il verbo col numero, che non si conosce. ✅ Il fuoco, il gelo
e l'acido diventano **soggetti** — «Il fuoco riduce in cenere Y», «Il gelo manda
in frantumi Y» — cosi' il verbo resta singolare e l'oggetto puo' essere quello
che vuole. E il possesso si attacca in coda con «che X porta addosso», che e'
la forma di `proc.hsp` gia' vista a schermo nel collaudo della 39ª.
"""
