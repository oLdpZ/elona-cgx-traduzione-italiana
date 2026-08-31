# -*- coding: utf-8 -*-
"""117a - Lotto 045 di `db_item.hsp`: I CIBI, il secondo lotto della categoria.

`FILTER_ITEM_FOOD`, righe da `:92585` a `:108257`: **28 righe** su 28 oggetti,
tutte dell'indice 0. Restano **31 righe** per il lotto 046, e con quello la
categoria si chiude.

⚠️ Previsione di `applica`: **+28**, e stavolta non e' contata a mano — la
stampa `scratchpad/lotti-113/_previsione.py 045`, nuovo. Zero righe gemelle.

### ⭐⭐⭐ LA PREVISIONE DI `applica` DIVENTA UNO STRUMENTO

La 116a ha imparato che una riga puo' avere una **gemella** con giapponese e
inglese identici byte per byte — stessa firma, una resa che copre due righe — e
che la gemella **non sta in nessuna tabella**, perche' l'estrazione tiene una
voce per firma. La lezione finiva li': «il conto e' una riga di script», e la
riga di script si riscriveva a mano ogni lotto.

Adesso e' `_previsione.py NNN`: raggruppa per firma **tutte** le voci del file e
dice quante righe del sorgente porta ciascuna firma del lotto.

⭐ **Provata al contrario, e non su un lotto qualunque**: puntata sul **042**,
dove la gemella c'e' di sicuro, si accende e stampa la coppia giusta —

    :76863  ->  anche :126849   ⚠️ FUORI DAL LOTTO
    previsione di `applica`: +36 sostituzioni per 35 rese

che e' **esattamente** quello che `applica` disse nella 116a, scoperto allora
dopo il fatto. Sul 043 e sul 044 dice +34 su 34 e +39 su 39, cioe' le due
previsioni che allora furono esatte. La rete riproduce tre casi noti, due
spenti e uno acceso, prima di essere creduta su un caso nuovo.

### ⭐⭐ DUE PESCI SPIEGANO IL PROPRIO NOME, E IN ITALIANO IL NOME E' UN ALTRO

Il giapponese di quattro pesci contiene l'etimologia del nome. Due reggono la
traduzione e due no, e la differenza non e' di stile: e' se la frase resti
**vera davanti al nome che il giocatore legge**.

  - `:107673`, **pesce sciabola**: 舶刀「カトラス」 e' la sciabola, e il nostro
    nome la porta gia'. Regge, e si scrive senza nominare la parola inglese;
  - `:108111`, **pesce piatto**: 名の通り平坦で四角い, «come dice il nome».
    Regge;
  - `:107819`, **pesce palla**: グローブ e' il **guanto**, e il giapponese lo
    dice esplicito (手に装着するグローブ). Con «pesce palla» a schermo, «il
    nome viene da un guanto» e' una frase falsa;
  - `:108257`, **pesce re**: il nome viene dal 三日月, la falce di luna presa a
    forza. Con «pesce re» a schermo, la luna non spiega niente.

**La decisione** e' quella che il progetto ha gia' preso altrove: *si rende il
gioco, non le sillabe* — le fusioni delle razze, e la battuta della formica di
`chat.hsp:9942`, dove il precedente e' dell'inglese stesso. Il gioco di parole
si **rifa' sul nome che il progetto ha scelto**:

    pesce palla   il guanto resta, ma e' il guanto IMBOTTITO, che e' tondo:
                  «tonda come un guanto imbottito da infilare in mano»
    pesce re      resta il PRENDERE A FORZA, che e' il cuore dell'immagine:
                  «pare di star prendendo a forza un re che non vuole
                  saperne di arrendersi»

⚠️ Il nome **non si tocca**: `ムーンフィッシュ -> pesce re` e
`グローブフィッシュ -> pesce palla` sono gia' a schermo, e «pesce luna» e' preso
da マンボー (`:108038`), che e' il pesce luna vero. Cambiare un nome per far
tornare una descrizione sposterebbe il difetto su tre righe invece di una.
ⓘ Cercati in `_cerca.py`: nessuna delle due etimologie e' resa altrove.

### ⭐⭐ I SETTE SEMI: L'INGLESE NE APPIATTISCE TRE

Tutti e sette condividono la seconda frase parola per parola, e la terza si
sdoppia:

    杖 / 鉱石 / 果物 / 野菜   食べることができるが、そうするくらいなら少し
                              成長を待ってあげてほしい。今日よりも明日なんだ。
    アーティファクト / 謎 / ハーブ
                              食べることができるが、種の持つ可能性につりあう
                              満腹度は得られないだろう。

L'inglese scrive per **tutti e sette** la prima — «You can eat them, but you
should wait for them to grow a little longer.» — e per giunta lascia cadere
今日よりも明日なんだ, che e' la chiusa della prima variante. Quattro frasi
perse e tre righe appiattite, in un gruppo di sette.

⭐ E il **codice ha confermato il giapponese**: 杖 qui e' la **bacchetta**, non
il bastone. `action.hsp:19811` fa cadere `ITEM_ID_ROD_HEALING_HANDS`,
`..._UNCURSE`, `..._MANA` e gli altri dall'albero magico. Il dizionario ha le
due rese di 杖 gia' distinte — «bastone» per l'arma, «bacchetta» per l'oggetto
che si agita — e a scegliere non e' stato il senso comune: e' stata la fonte.

### ⚠️⚠️ UN ROVESCIAMENTO DELL'INGLESE, SU MORGIA

`:102836`: 食欲減退に効果があるとされ — l'erba fa effetto **contro** il calo
dell'appetito, che e' il sintomo. L'inglese scrive «effective in reducing
appetite», cioe' che l'appetito lo toglie: il contrario.

⭐ A dirlo non e' la grammatica ma la **frase dopo**, che il giapponese e
l'inglese hanno tutt'e due: 軽病の際には薬膳料理として食される, la si mangia
come piatto medicinale quando il male e' leggero. Un'erba che si mangia da
malati non e' un'erba che leva la fame.

### ⚠️ L'INGLESE LASCIA CADERE, RIPETE E SBAGLIA UN NOME

  - `:97601` (lo snack cibernetico): l'inglese **ripete la stessa frase due
    volte** — «But it is delicious! But it is really tasty!» — dove il
    giapponese dice でもおいしい！ una volta sola;
  - `:107746` (il tonno): perde 一尾で二度おいしい, «un pesce solo e buono due
    volte», che e' la battuta su cui la riga si chiude;
  - `:102584` (alraunia): appiattisce 舞踏会, il **ballo**, in «social
    occasions», e perde l'orto delle erbe delle gran dame;
  - `:102710` (spenseweed): perde 奮発して, cioe' che il cittadino ci si
    **sforza**, a comprarla;
  - `:102773` (mareilon): appiattisce 他の香辛料にも劣らぬ («non ha niente da
    invidiare alle altre spezie») in «for it's kick»;
  - `:108111` (il pesce piatto): scrive **«Palmyre»** dove il giapponese dice
    パルミア. E' Palmia, e nel dizionario e' Palmia da sempre.

### ⚠️⚠️ UNA `é` PERSA A MONTE, DENTRO IL CORPO — E LA FAMIGLIA E' DI UNA

`:92585` (l'uovo) scrive in inglese `our home d?cor`: la `é` di «décor» e' un
punto interrogativo **vero**, 0x3F, letto byte per byte nel sorgente pinnato.

E' lo stesso guasto delle sette code storpiate di `_115-fonti-storpiate`, ma
nel **corpo** invece che nella coda, dove nessuna rete lo cercava. Misurata la
famiglia col criterio «un `?` in mezzo a due lettere»:

    db_item.hsp     1 occorrenza     d?c        <- questa
    tutto il resto  0                (i tre di `net.hsp` sono query di URL)

Un'occorrenza in tutto il sorgente. Non serve una rete nuova per una riga sola,
e l'italiano non ci passa: «un pezzo d'arredo di casa tua» non ha accenti.
ⓘ E 我が家 lo scrive l'inglese «our home», ma il soggetto della frase e' あなた:
e' la casa di chi legge.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le due code del lotto sono `~Il Cibo Mutevole di Tyris~` (15 righe) e
`~Atlante Illustrato del Giardinaggio di Tyris~` (13), tutt'e due gia' in
tabella con **una sola** resa italiana ciascuna. Il cancello «titoli resi in
PIU' modi» resta a **7**: un 8 sarebbe un difetto nuovo.

⚠️ La forma e' di nuovo disomogenea, e le due disomogeneita' **non
coincidono**: 11 righe hanno lo spazio prima del `\\n` e 17 no; 7 code sono
`# ~` e 21 sono `#~`. I sette `# ~` sono i sette semi, che hanno anche lo
spazio; ma la carne secca e i tre snack hanno lo spazio e la coda **senza**.
Si legge `scratchpad/lotti-113/_forma.py 045` riga per riga.
"""
