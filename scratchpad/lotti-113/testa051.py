# -*- coding: utf-8 -*-
"""119a - Lotto 051 di `db_item.hsp`: LE PERGAMENE E GLI ATTI, prima meta'.

`FILTER_ITEM_SCROLL`, righe da `:44031` a `:99025`: **50 righe** su 43 oggetti —
42 dell'indice 0, **5 dell'indice 1** e 3 dell'indice 2. La categoria era intatta
(73 da fare su 73): dopo questo lotto ne restano **23**, e chiudono il 052.

⚠️⚠️ Previsione di `applica`: **+56** per 50 rese. Il moltiplicatore c'e', ed e'
la cosa che spiega tutto il lotto: quattro firme coprono sei righe in piu'.

### ⭐⭐⭐ LA NOTA DELLA NAVE E' UNA SCALA A QUATTRO GRADINI, E L'INGLESE LA APPIATTISCE

Sei mezzi di mare — zattera, peschereccio, nave pirata, nave da crociera, nave
da guerra, sottomarino — portano nell'indice 1 la stessa nota del manuale di
viaggio. In **inglese sono sei stringhe identiche**, tutte con «It is
tremendously vulnerable to thunderstorms and ether winds». In giapponese cambia
**una parola**, ed e' un fatto di gioco:

    :45061  zattera                   雷雨やエーテル風に **とてつもなく弱い**
    :45132  peschereccio, nave pirata                  **かなり弱い**
    :45274  nave da crociera                           **結構弱い**
    :45345  nave da guerra, sottomarino                **弱い**

Quattro gradini di fragilita', dal legno che affonda al sottomarino. La resa
tiene la scala con quattro avverbi e una parola sola, come la scala della
gittata della 110a: **debolissima / parecchio debole / abbastanza debole /
debole**.

⭐ **E la scala e' anche la ragione delle gemelle.** `estrai.firma()` e'
`sha1(giapponese + \\x00 + inglese)`: dove il giapponese coincide, coincide la
firma. Peschereccio e nave pirata dicono tutt'e due かなり弱い, nave da guerra e
sottomarino tutt'e due 弱い — quindi **due rese coprono quattro righe**. Non e'
un caso e non e' un difetto: e' il modo in cui l'autore ha raggruppato i mezzi
per fragilita'.

ⓘ Chi avesse reso le sei note dall'inglese avrebbe scritto sei volte
«debolissima», cioe' avrebbe cancellato una scala che il gioco usa. Nessuna rete
poteva vederlo: le sei righe inglesi sono uguali, e il dossier le mostra una per
volta.

⚠️ La nota dei mezzi di **terra** (`:51360`) e' invece davvero una sola per
quattro: corazzata, locomotiva, autocarro e carrozza hanno lo stesso giapponese
identico. Una resa, quattro righe.

### ⚠️⚠️ L'INGLESE È ROTTO ALTRE DUE VOLTE, E SEMPRE COPIANDO LA RIGA VICINA

Fa **quattro** in questa sessione: il te' nero (049), il liquido antiacido
(050), e qui:

    :96060  l'atto del MUSEO
      JP   博物館を建てる権利が得られる証書
      EN   «A deed gives the right to create a **shop**»
           (e' la riga del negozio, `:95990`; la seconda meta' dell'inglese
            parla poi di collezionisti, quindi la copia e' della prima frase)

    :97128  la pergamena di potenziamento dell'ARMA
      JP   武器の強度が増し (la robustezza dell'ARMA)
      EN   «increases the strength of the **armour**»
           (e' la riga dell'armatura, `:96986`)

⭐ **La forma del guasto e' sempre la stessa**: due righe gemelle per
costruzione, e monte ricopia l'una nell'altra senza cambiare la parola che le
distingue. Si vede solo mettendo le due righe **una accanto all'altra**, e in
tre casi su quattro le due righe stavano in lotti diversi.

### ⚠️ E UNA VOLTA L'INGLESE SBAGLIA IL CETO

`:51359`, la corazzata terrestre: ちょっとした金持ち程度では維持費を工面できない
e' «uno **appena benestante** non riesce a pagarne il mantenimento» — cioe'
serve essere ricchi sul serio. L'inglese scrive «even the richest person cannot
afford to maintain», che dice il contrario: che non se la puo' permettere
nessuno. Segue il giapponese.

### ⓘ I nomi che venivano da altre tabelle

    死神        -> **la Morte**, femminile e con la maiuscola (`item_func.hsp`,
                   «stringe un patto con la Morte»)
    ベルム家    -> **casa Bellum** (`chat.hsp`), non «Belm» come l'inglese
    エウダーナ  -> **Eulderna**
    すくつ      -> **il Vuoto** ⚠️ e' il refuso voluto di 巣窟; l'inglese scrive
                   «the sanctuary», che sarebbe un terzo nome per lo stesso
                   posto. Lo decide il rapporto di identificazione della
                   licenza stessa, che dice gia' «il Vuoto»
    形見のカバン -> **la borsa dei ricordi**
    魔具全典    -> `~Compendio Completo degli Oggetti Magici~` ⓘ l'inglese lo
                   scrive «Arcane Alamanac», col refuso, in tutte e diciotto

### ⓘ Le parole lunghe, e perche' restano

Il preflight segnala sei parole da 15 caratteri: `l'assicurazione` (quattro
volte, nella nota della nave) ed `equipaggiamento` (due). Sono dentro la
finestra di rinculo, che e' un **indizio** e non un vincolo (113a): a decidere
e' dove cade il taglio, e quello lo sa solo `_107-descrizioni-item`. Sciogliere
`equipaggiamento` vorrebbe dire scrivere un'altra parola per un termine che il
progetto usa dappertutto, compreso il nome degli oggetti. Misurate dopo il
reimport: parole spezzate introdotte **0**.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **undici**, tutte gia' in tabella (`_code.py 051`: righe
senza resa **0**). Il cancello «titoli resi in PIU' modi» resta a **7**.

⚠️ La forma: **37** righe su 50 hanno lo spazio prima del `\\n` e 13 no; **26**
code hanno lo spazio dopo il `#` e 24 no.
ⓘ `:52519` e' il caso in cui l'inglese la coda non la scrive nemmeno come coda —
`# Witch's words, written in the corner`, senza le tilde. La coda italiana la
decide la **tabella**, che ha le tilde: `#~Parole di una Strega Scritte in un
Angolo~`.
"""
