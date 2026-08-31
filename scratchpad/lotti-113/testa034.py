# -*- coding: utf-8 -*-
"""115a - Lotto 034 di `db_item.hsp`: GLI ATTREZZI, seconda parte.

`FILTER_ITEM_TOOL`, righe 48.000-62.000: **44 righe** su 39 oggetti — 39
dell'indice 0, 1 dell'indice 1 e 4 dell'indice 2. Segue il 033, che aveva preso
le prime 50 righe della categoria fino a `:47288`.

La taglia e' stata scelta guardando il numero che `_corpo.py` stampa: `0 48000`
dava 38, `0 62000` ne da' 44, `0 64000` 55, `0 70000` 73. Un lotto sano sta fra
le 30 e le 55.

### ⭐⭐⭐ L'INGLESE E' SLITTATO DI UNA POSIZIONE, E LO DICONO LE CODE

Tre righe di due oggetti diversi portano un inglese che appartiene alla riga
**precedente della catena**:

    :50410  (convertitore, indice 2)  jp VUOTO      en «if the skill is too low…»
    :51288  (detriti, indice 0)       jp enciclopedia  en «treasures that provide
                                                          experience…»
    :51289  (detriti, indice 1)       jp «tesoro che da' esperienza»
                                      en «if the skill is too low…»

Il giapponese di `:51289` e' quello che l'inglese mette a `:51288`; l'inglese di
`:51289` e' quello che appartiene a `:50410`, dove il giapponese **non c'e'**.

⭐ **A dirlo con certezza sono le code, che invece sono al posto giusto**:
`:51288` ha ～イルヴァ幻想辞典～ / `~Irva Fantasy Encyclopedia~` in tutt'e due le
lingue, `:51289` ha ～遺跡荒らしのメモ～ / `~memo of a grave robber~` in tutt'e
due. La coda dice a quale fonte appartiene il testo, e il corpo inglese non le
corrisponde. Senza le code sarebbero state due prose plausibili e nessuno
avrebbe visto niente.

Si segue il giapponese (109a), e a `:50410` — che un giapponese non ce l'ha —
si segue l'inglese, che li' e' quello giusto: parla davvero del convertitore.

### ⚠️⚠️ E LE DUE RIGHE HANNO L'INGLESE IDENTICO, MA NON LA STESSA FIRMA

`:50410` e `:51289` portano lo **stesso identico inglese**, 229 caratteri. E'
l'unica coppia del lotto che condivide un testo, e sembrava il moltiplicatore
del 033 — una resa sola per due righe, con l'obbligo di scegliere quale dei due
sensi sacrificare.

Non lo e': `estrai.firma()` e' `sha1(giapponese + \\x00 + inglese)`, e il
giapponese qui e' diverso (uno e' la stringa **vuota**). Due firme, due voci,
due rese indipendenti. ⭐ Il difetto di monte si puo' riparare **su tutt'e due i
siti**, senza toppe e senza scegliere.

⚠️ La lezione: prima di dare per gemelle due righe con l'inglese uguale si
guarda il **giapponese**, perche' e' meta' della chiave. Un inglese uguale non
basta a fondere due firme.

### ⭐⭐⭐ I QUATTRO POTIO-MAN: L'INGLESE APPIATTISCE QUATTRO FRASI IN UNA

`:50474`, `:50540`, `:50606`, `:50672` sono quattro modelli dello stesso
giocattolo. Il loro giapponese ha la stessa struttura e **due** frasi che
cambiano: la seconda e l'ultima. L'inglese copia l'ultima fedelmente, ma al
posto della seconda scrive in tutt'e quattro «Its wielder is called a Potioner»,
che e' la seconda frase del **solo** `:50474`.

    :50474  これの使い手はポーショナーと呼ばれる    (il nome di chi lo usa)
    :50540  時代に合わせて色々な飲み物の栓が…      (i tappi usati nel tempo)
    :50606  地域によってはコルクマンと呼ぶ…        (come lo chiamano altrove)
    :50672  使ったポーションの数だけ弾数が増える…  (quante cariche ha)

Quattro rese diverse dove l'inglese ne aveva una. E' il verso opposto della
lezione del 033 sulle quattro carte: li' il giapponese era identico e l'inglese
distingueva, e le rese erano **una sola** ripetuta.

⚠️ `ポーショナー` e `コルクマン` non stanno in nessun dizionario: sono nomi che
nascono qui. «pozionista» e «uomo di sughero» — il secondo e' un soprannome
locale, e va reso, non traslitterato.

### ⭐⭐ I TRE GLOBI OSCURI: L'INGLESE DICE «SP» TRE VOLTE, IL GIAPPONESE NO

`:50945` (verde), `:51012` (blu), `:51079` (cremisi) hanno lo stesso testo a
meno del colore e della risorsa consumata. Il giapponese dice **ＳＰ, ＭＰ,
ＨＰ**; l'inglese scrive «SP» in tutt'e tre. E' un fatto di gioco, e la quinta
fonte (110a) e' il codice: si segue il giapponese.

⭐ **Il （未実装） qui regge, e lo conferma il codice.** Nel 033 il giapponese
diceva «non implementato» di un oggetto che funzionava, e aveva vinto il codice.
Qui e' il contrario: `action.hsp:15047-15059` ha i tre rami dei globi, e il
verde arriva a `txt lang("開発中。", "Under development.")`; gli altri due non
fanno **niente**. Il giapponese e il codice dicono la stessa cosa.

⚠️ La resa e' modellata sul **fratello bianco** `:45481`, gia' reso nel 033
(111a: la famiglia batte il lotto). «Per classificazione» resta com'e' li',
anche se e' di 15 caratteri e la finestra di rinculo e' 15: il cancello delle
parole spezzate misura la **posizione**, non la lunghezza, e nel 033 quella
stessa parola e' passata. Se si accende, si riscrive.

### ⚠️⚠️ IL DIZIONARIO FANTASTICO E' DI DUE CITTA', E L'INGLESE NE CONOSCE UNA

`:52380` (il Moku-Jin) porta la coda ～イムウエル幻想辞典～, cioe' **Aimwell**;
tutte le altre dodici del lotto portano ～イルヴァ幻想辞典～, Irva. L'inglese
scrive `~Irva Fantasy Encyclopedia~` per tutt'e due.

イムウエル e' gia' reso «Aimwell» altrove nel dizionario (due erbe di Tyris del
Nord e una mappa), e la tabella della 112a gli da' gia' `~Dizionario Fantastico
di Aimwell~`. Non c'e' niente da decidere: c'e' da non appiattire.

⚠️⚠️ **CONSEGUENZA ANNUNCIATA PRIMA DI MISURARLA**: il cancello «titoli resi in
PIU' modi» di `_112-corpo-descrizioni` chiava sull'**inglese**, quindi dopo
questo lotto passa da **2 a 3**, e il terzo e' `Irva Fantasy Encyclopedia` ->
Irva / Aimwell. E' il terzo appiattimento dell'inglese, non una nostra
divergenza. Un **4** sarebbe un difetto nuovo.

### ⚠️ LA FONTE CHE L'INGLESE SCRIVE SENZA TILDE

`:52047` e' l'unica riga del lotto la cui coda inglese e'
`# Words of the Goddess of Wealth`: il `#` c'e', le tilde no. Il giapponese le
ha (～富の女神の言葉～), e tutte le altre 233 fonti della famiglia le hanno.

Si conserva il `#` **col suo spazio**, come vuole la regola del 033 sui `#`
perduti, e si rimettono le tilde, che sono la forma della fonte e non un vezzo
dell'inglese. ⓘ `_code.py` da solo qui sbaglia: la sua `marca` e' il prefisso
dell'inglese fino alla prima tilde, e senza tilde ripiega su `#` perdendo lo
spazio. Il file `_traduzioni034.py` lo corregge a mano.

### ⭐ L'INGLESE DEL KISERU DICE «PELLE» DOVE IL GIAPPONESE DICE CARISMA

I quattro oggetti da fumo (`:60914` kiseru, `:60980` pipa, `:61046` hamaki,
`:61112` sigaretta) crescono quattro attributi diversi: 魅力 Carisma, 習得
Apprendimento, 器用 Destrezza, 感覚 Percezione. Sul kiseru l'inglese scrive
«ingredients thats beneficial to the skin»: la pelle non c'entra niente, e non
e' un fatto di gioco vago — e' l'attributo che l'oggetto alza.

I nomi dei quattro attributi si copiano da `skill.hsp`, dove sono gia' resi
(Carisma, Apprendimento, Destrezza, Percezione), e la formula e' la stessa per
tutt'e quattro: «fanno crescere l'attributo X». ⓘ «l'attributo» non e'
un'aggiunta gratuita: `l'Apprendimento` misura 15 caratteri e la finestra di
rinculo e' 15. Serviva un confine, e il gioco quella parola la usa gia'
(«Attributi base», `command.hsp:10416`).

### ⓘ Gli altri termini cercati a mano nel dizionario

Le reti non leggono il glossario (regola della 111a), quindi: 富の女神 «la dea
della ricchezza» in prosa e «Yacatect» come nome; ヤカポイント «YacaPoint»
invariato; 龍脈 «la vena del drago» (`chat.hsp`); 決戦因子 «Fattore Decisivo»;
はく製 «statuetta»; アーティファクト «artefatto»; ケサランパサラン
«kesaranpasaran»; 雑貨店 «merceria»; テスカトリポカ «Tezcatlipoca»; ゼーム
«Zeome»; 魔石 «pietra magica»; 生化学文明 «civilta' biochimica»; スタミナ
«resistenza» in prosa.

⚠️ `:52380` obbedisce al nome **non identificato** dell'oggetto («bambola di
legno»), non a quello identificato (`<Moku-Jin>`): la prosa del pannello si
legge anche prima di identificare.
"""
