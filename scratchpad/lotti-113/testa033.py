# -*- coding: utf-8 -*-
"""114a - Lotto 033 di `db_item.hsp`: GLI ATTREZZI, prima parte.

`FILTER_ITEM_TOOL`, righe 0-48.000: **50 righe** su 31 oggetti — 31 dell'indice
0, 6 dell'indice 1 e 13 dell'indice 2. E' il primo lotto del corpo fuori dal
mobilio, e non somiglia a nessuno dei precedenti: sono oggetti **aggiunti dal
CGX**, con prosa lunga, tecnica, e piena di termini che il gioco usa altrove.

### ⭐⭐⭐ QUI UNA RESA NON COPRE UNA RIGA SOLA

I quattro fucili anestetici (`:42415`, `:42491`, `:42567`, `:42643`) hanno
descrizioni di indice 0 diverse solo nella **fascia di peso**, ma le loro righe
di indice 1 e 2 sono **identiche parola per parola in tutti e quattro**: una
firma sola, `:42416` e `:42417`, che copre otto righe del sorgente. E' il
moltiplicatore che il mobilio non aveva e il cibo si', e vuol dire che
`applica` sale di **piu'** di 50.

⚠️ Il numero atteso, quindi, **non e' il numero delle rese**: si guarda quanto
sale `applica` e si controlla che sia coerente con le firme gemelle, non che
faccia 50.

### ⭐⭐⭐ LE QUATTRO CARTE HANNO IL GIAPPONESE IDENTICO, E L'INGLESE NO

`:46547`, `:46615`, `:46683` e `:46751` — i quattro «signori» di quadri, cuori,
fiori e picche — hanno **lo stesso identico giapponese**, che dice «tutti gli
spiriti delle carte **corrispondenti al seme dell'oggetto**». L'inglese invece
nomina lo spirito preciso di ciascun seme (Diamond Eyes, Heart Witch, Club
Feathers, Spade Warrior).

Le quattro rese sono **identiche**, come il giapponese: il seme il giocatore lo
legge nel **nome** della carta, che e' gia' reso («signore di quadri»…), e una
resa generica e' vera per tutt'e quattro. ⓘ Cosi' `_coerenza.py` — che si
accende quando lo stesso giapponese ha rese diverse — resta a zero senza che si
sia dovuto forzare niente.

### ⭐⭐⭐ IL CODICE SMENTISCE IL GIAPPONESE, E VINCE IL CODICE

Il giapponese di `:46950` (l'estensore di sopravvivenza Y) comincia con
**（未実装）**, «non implementato». Ma l'oggetto **funziona**:
`action.hsp:8721` ha il suo ramo di effetto e `:8782` mette
`CDATA_PREGNANCY_MALE_CHILD`, esattamente come la X fa con
`CDATA_PREGNANCY_FEMALE_CHILD`. Il giapponese e' fermo a una versione vecchia.

E' la quinta fonte della 110a — *il codice vince quando il giapponese e' in
disaccordo su un fatto di gioco* — e qui non e' un'ambiguita': e' una riga che
direbbe al giocatore di non usare un oggetto che funziona. Il marcatore non si
rende, e le due rese restano identiche come lo sono i due inglesi.

### ⭐⭐ L'INGLESE SBAGLIA UN ATTRIBUTO, E TAGLIA TRE VOLTE

- **`:46952` e' attribuito alla persona SBAGLIATA.** L'inglese firma
  `# Lead Developer <Dr. Gavela>`, la stessa firma di `:46886`; il giapponese
  dice 生化学者『イコール』, **il biochimico <Icolle>**. Se ne accorge
  `lotti-113/_code.py`, che passa dal giapponese e non dall'inglese.
- **`:46403` cita il LIBRO sbagliato.** L'inglese scrive
  `#~Thousands of pieces of Junk I love~`, il giapponese `～ゴミの山に光るもの～`
  — sono due libri diversi, e la coda giusta e'
  `~Quel che Brilla nel Mucchio dei Rifiuti~`. Stessa rete, stessa ragione.
- **`:45745` (il Res upper) butta via che fine facevano le fate**: 鱗粉を奪われ
  翅がハゲてスカスカになる妖精が続出した — a molte fate strapparono la polvere
  delle ali, e le ali restarono spelacchiate. L'inglese al suo posto **aggiunge**
  una «Elea misinformation» che il giapponese non ha.
- **`:47016` (la fibra stellare) perde これだけでは何の役にも立たない**, «da sola
  non serve a niente», che e' la frase che dice a che cosa serve l'oggetto.
- **`:45811` e `:45877` perdono la terza frase**, quella che dice che il farmaco
  da' il meglio quando e' un buon equipaggiamento ad amplificarlo.

### ⚠️⚠️ LA SPAZIATURA PRIMA DEL `\\n` QUI NON E' UNIFORME

Nel mobilio era quasi sempre uno spazio. Qui l'inglese ne mette **uno**, **zero**
o **due** (`:45549`, `:45615`, `:45681`), e `:45944` porta perfino un `\\n` **in
coda** che nessun'altra riga del lotto ha. Ogni riga copia il suo, verbatim.

### ⚠️⚠️ DUE RIGHE HANNO PERSO IL `#` DAVANTI ALLA FONTE, E NON GLIELO RIMETTIAMO

`:47287` e `:47288` (le due battute sui calzini) hanno in giapponese
`#～…の言葉～` col cancelletto, e in inglese `~Bandit Leader~` **senza**. Senza
il `#` il gioco non la disegna come riga-fonte (`command.hsp:16758`): cade
nell'impaginatore e va a sinistra.

Il `#` **non** si aggiunge, per due ragioni:

1. il cancello di `_112-corpo-descrizioni.py` conta i `#` **contro l'inglese**
   (`en.count('#') != it.count('#')`), e aggiungerlo lo accenderebbe su due
   righe;
2. e' un difetto di **monte**, come i 110 inglesi oltre il tetto dell'indice 3:
   non si contano contro di noi e non si riparano di nascosto.

ⓘ Per questo `lotti-113/_code.py` esce con **1** su questo lotto, dicendo «2
righe senza resa in tabella»: cerca il segmento che comincia per `#`, e qui non
c'e'. Non e' un guasto della rete — e' la rete che vede il difetto di monte. Le
due code sono state scritte a mano nella forma della famiglia, cosi' che se
l'upstream un giorno rimette il `#` il testo sia gia' giusto.

### ⭐ I TERMINI CERCATI A MANO

    カード精霊   -> spiriti delle carte    (`db_creature.hsp`, i quattro semi)
    深淵魔力     -> potere abissale        (`action.hsp`)
    魔道具(abilita') -> Dispositivi magici (`skill.hsp`)
    暗記         -> Memoria                (`skill.hsp`)
    罠の知識     -> Disarmo trappole       (`skill.hsp`)
    ポーショマン -> potioman               (`chat.hsp`)
    モンスターボール -> sfera dei mostri   (`chat.hsp`)
    変装セット   -> set da travestimento   (`db_item.hsp`)
    姉波動       -> Onda Sororale          (`chat.hsp`)
    魔石         -> pietra magica          (`chat.hsp`)
    パワーゲージ -> barra di potenza       (`chat.hsp`)
    防御態勢     -> difesa                 (`text.hsp`)
    エウダーナ / ザナン -> Eulderna / Zanan  (nomi propri)

⚠️ **魔導体 non e' nel dizionario**: e' l'organo che conduce la magia, e
l'inglese lo chiama ora «magical conductors» ora «Conductive Cells». Reso
**«conduttore magico»**, e la scelta va nel glossario.
⚠️ **電磁波 non e' nel dizionario**, e «elettromagnetiche» e' di **17
caratteri**: sopra la soglia dei 14, l'impaginatore la spezzerebbe. Reso
«radiazioni», che nel contesto — la reclame truffaldina contro le onde e la
lettura del pensiero — dice la stessa cosa e ci sta.
"""
