# -*- coding: utf-8 -*-
"""117a - Lotto 046 di `db_item.hsp`: I CIBI, il lotto che CHIUDE la categoria.

`FILTER_ITEM_FOOD`, righe da `:113749` a `:119461`: **31 righe** su 30 oggetti —
30 dell'indice 0 e **1** dell'indice 2. Con questo lotto `FILTER_ITEM_FOOD` va a
**0 da fare su 148 vive**: e' la **quinta** categoria del corpo che si chiude,
dopo mobilio, attrezzi, scarti e armi.

⚠️⚠️ Previsione di `applica`: **+32** per 31 rese.

### ⭐⭐⭐ LA RETE NUOVA HA TROVATO LA SECONDA GEMELLA DEL PROGETTO, SUBITO

`_previsione.py 046`, nata nel lotto 045 di questa stessa sessione, si e'
accesa al primo lotto in cui c'era qualcosa da trovare:

    :113814  ->  anche :113879   ⚠️ FUORI DAL LOTTO
    previsione di `applica`: +32 sostituzioni per 31 rese

`:113814` (il sacco di farina) e `:113879` (la pasta fresca) sono tutt'e due
l'**indice 2**, hanno il giapponese **vuoto** e lo stesso identico inglese:
`estrai.firma()` e' `sha1(jp + \\x00 + en)`, quindi una firma sola e una resa
che copre due righe.

⚠️ `:113879` **non e' nel lotto e non poteva esserci**: l'estrazione tiene una
voce per firma, quindi `_107-chiavi-item.py` non la emette. E' una delle **64
righe** che nessun lotto potra' mai scegliere (la differenza fra le 1.513 righe
di `_107-descrizioni-item` e le 1.449 firme di `_114-corpo-da-fare`), e si
riempie da sola quando si rende la gemella.

⭐ **Il valore della rete non e' aver detto 32.** E' che il 32 e' stato scritto
**prima** di lanciare `applica`, dove nel 042 lo stesso fatto era stato scoperto
dopo, guardando un numero che non tornava.

### ⭐⭐ LA QUARTA FIRMA GENERICA DELL'INDICE 2, E LA FAMIGLIA ERA GIA' SCRITTA

`:113814` e' la quarta e ultima delle firme generiche dell'indice 2 dei cibi —
il **moltiplicatore** che la 114a aveva annunciato leggendo «98 da fare su 148
vive». Le altre tre erano gia' rese, e la resa nuova le segue parola per parola:

    A type of vegetable that restores satiety...  Una verdura che sazia, e che
                                                  entra in molte ricette.
    A type of seafood  ...                        Un cibo di mare che sazia...
    A type of fruit    ...                        Un frutto che sazia...
    Food that restores satiety...     <- QUESTA    Un cibo che sazia, e che
                                                  entra in molte ricette.

ⓘ Le prime tre dicono «A type of X», questa dice «Food» e basta: e' la voce
generica per i cibi che non sono ne' verdura, ne' pesce, ne' frutta — la farina
e la pasta fresca.

### ⭐⭐ TRE ORTAGGI SI GUARDANO L'UN L'ALTRO, E L'INGLESE NE ROMPE DUE RIMANDI

Il giapponese incatena tre righe **dello stesso lotto**:

    :117978  la zucca      «parente della ウリ»          -> il MELONE, :117905
    :118787  la patata d.  «meno adatta della カボチ»     -> la ZUCCA,  :117978
    :118581  l'imo         «più piccolo della さつまいも» -> la PATATA DOLCE, :118787

L'inglese rompe i primi due: scrive «cucumber family» dove il giapponese dice
melone, e sostituisce il paragone con la zucca con un generico «It tastes
terrible when eaten wrong». In italiano i tre nomi sono quelli gia' a schermo —
melone, zucca, patata dolce — e i tre rimandi restano veri.

⚠️ **Nessuna rete puo' vederlo**: sono tre stringhe diverse, con tre inglesi
diversi, e il legame sta in una parola dentro la prosa. E' la lezione della
111a — «le altre righe della stessa famiglia» — applicata dentro un lotto solo.

### ⭐⭐ IL MOSTRO SI CHIAMA GIA' COME L'ORTAGGIO, E LA BATTUTA CI GUADAGNA

`:117978` chiude dicendo che c'e' chi sostiene che la カボチャ abbia a che fare
col mostro chiamato パンプキン. In giapponese sono **due parole diverse**, e la
battuta e' che qualcuno ci veda una parentela.

In italiano il mostro e' gia' **«zucca»** (`db_creature.hsp`, cercato con
`_cerca.py`), esattamente come l'ortaggio. Reso alla lettera, «il mostro
chiamato zucca» sarebbe una tautologia; reso **sul nome** — «il mostro che porta
il suo stesso nome» — la battuta funziona meglio che in giapponese, perche' in
italiano i due nomi coincidono davvero.

### ⚠️⚠️ L'INGLESE SOSTITUISCE DUE VOLTE, E UNA VOLTA INVENTA

  - `:113812` (la farina) e `:113877` (la pasta fresca): l'inglese scrive per
    **tutt'e due** la stessa frase — «Taste a lot better when cooked, but some
    prefer to ate it raw.» — e il giapponese dice due cose diverse, nessuna
    delle quali e' quella: nella farina «ci sara' pure una ragione, lasciamolo
    in pace», nella pasta la citazione di chi la mangia cruda;
  - `:118860` (il ravanello): il giapponese dice che da bambini ci si giocava a
    duello con questi in mano e ci si prendeva la sgridata **in due**;
    l'inglese scrive «It is often used in food fights by the childrens of
    Noyel». Ne' la battaglia di cibo ne' **Noyel** stanno nel giapponese;
  - `:115652` (la razione): l'inglese lascia cadere
    それに比例してか味の方は絶望的な出来栄えである, cioe' la battuta su cui la
    riga si chiude — si conserva benissimo, e il sapore e' disperato.

### ⚠️ UN ROVESCIAMENTO, UNA PAROLA LETTA MALE E UN'AGGIUNTA

  - `:118116` (il limone) — 大凡の果実のように…止めておいた方がよい dice che
    con **questo** non si fa quel che si fa con quasi tutti gli altri frutti.
    L'inglese scrive «like most fruits, should not be eaten directly», cioe'
    che a non doversi mangiare sono anche gli altri: il contrario;
  - `:119461` (la quwapana) — もいで e' «staccare, cogliere». L'inglese legge
    «wriggling», dimenare: le foglie si colgono, non si agitano;
  - `:113749` (il pesce bomba) — はじける e' «scoppiare». L'inglese scrive
    «burst into flames», e le fiamme nel giapponese non ci sono.

E due tagli piu' piccoli: `:119193` (l'uva) perde il chicco che sta nella bocca
di un bambino, e `:119258` (la mela) perde i modi di cucinarla nati lungo la
storia — che e' proprio la premessa della battuta sulla torta di mele.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono tre, tutte gia' in tabella con una sola resa italiana:
`~Il Cibo Mutevole di Tyris~` (29 righe), `~Rapporto di Identificazione:
categoria <Cibo>~` (1) e `~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~`
(1). Il cancello «titoli resi in PIU' modi» resta a **7**.

⚠️ La forma e' quasi uniforme, all'opposto del 044 e del 045: **2** righe su 31
hanno lo spazio prima del `\\n` (`:113940` e `:115652`) e **1** sola ha la coda
`# ~` (`:115652`). Uniforme non vuol dire deducibile: si legge lo stesso
`scratchpad/lotti-113/_forma.py 046`.
"""
