# -*- coding: utf-8 -*-
"""116a - Lotto 042 di `db_item.hsp`: LE ARMI, seconda parte.

`FILTER_WEAPON`, righe da `:67045` a `:81879`: **35 righe** su 33 oggetti — 33
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. L'intervallo scelto e'
`67000 82000`, che lascia **34 righe** al lotto 043: due meta' pari invece di
un 42 e un 27.

⚠️⚠️⚠️ **LA PREVISIONE ERA «+35 ESATTE» ED E' USCITO +36.** Si scrive qui com'e'
andata, non com'era stata detta: la sezione in fondo racconta perche', e la
ragione e' piu' utile del numero.

### ⭐⭐⭐ DUE FAMIGLIE, E UNA ATTRAVERSA I LOTTI

**La prima e' dentro il lotto, ed e' di cinque righe.** `:75445` (<Libro
Distruttore>), `:77005` (<Kindness Blade>), `:77215` (<Distruttore di Dei>),
`:77285` (<Falce della Bestia>) e `:81606` (<Coda di Frisia>) portano in
giapponese la **stessa identica frase**:

    人では振るえない程の重さだが、使いこなす者が現れた時この武器は
    使用者に<X>を授けるだろう。それと少しばかりの気まぐれを。

e cambia solo l'attributo donato. ⭐ Misurato con uno script prima di scrivere:
la frase compare **5 volte in tutto `db_item.hsp`**, e sono tutte e cinque qui.
La famiglia e' chiusa dentro il lotto, quindi non puo' rompersi dopo.

⚠️ **L'inglese la riscrive cinque volte in modo diverso** — «so heavy that it
cannot be wielded by a single person», «too heavy for a man to wield», «so
heavy that no man can wield it», «It is too heavy for a man to wield», «It is
so heavy that it cannot be wielded by a human being» — dove il giapponese ha
una formula sola. Nessun cancello lo vede: l'inglese e' cinque stringhe
diverse, quindi per la rete 4 sono cinque cose diverse.

⭐ **La forma italiana e' senza genere apposta.** I cinque oggetti sono un
libro, una spada, un'ascia, una falce e un bastone: qualunque clitico («la
possa brandire») avrebbe costretto a cambiare la frase, e la famiglia si
sarebbe rotta sulla grammatica. La forma scelta gira intorno al problema:

    E' di un peso che un uomo non regge, ma quando comparira' chi sa
    servirsene, quest'arma gli donera' <X>. E, insieme, un pizzico di capriccio.

I cinque attributi sono i **nomi del dizionario**, non inventati:
習得 → apprendimento, 意志 → volontà, パワー → forza, 耐久 → costituzione,
魔力 → magia (tutti da `chara.hsp`, «Ottiene +11 in ...»).

**La seconda famiglia attraversa i lotti**, ed e' la sola ragione per cui va
scritta qui. `:76863` (<Stormbringer>) apre con la **stessa prima frase** di
`:51779` (<Ravenbrand>), che sta nel **lotto 041**, chiuso stamattina:
邪を祓う為に更に強大な邪を用いる、という考えから生み出された黒の剣。
Confrontate byte per byte: identiche. La resa e' copiata parola per parola.
⭐ Sono **2 in tutto il file**, e la seconda cambia: `:51779` dice 分身
(«sdoppiamenti»), `:76863` dice 兄弟剣 («gemella», come gia' scrive l'indice 3
di Mournblade). Uguale dove il giapponese e' uguale, diversa dove e' diverso.

⚠️ E l'inglese aggiunge «surrounded with an aura of dread» a **tutt'e due**:
nel giapponese non c'e' ne' qui ne' la'. Un'invenzione ripetuta e' comunque
un'invenzione.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, CIOE' ANCORA INVARIATO

Le sei code del lotto, e nessuna copre due giapponesi:

    ~Irva Fantasy Encyclopedia~      27 righe  (gia' uno dei sei, per Aimwell)
    ~Collection of Armaments...~      4 righe
    ~Book of Wisdom~                  1 riga
    ~words of a God of Destruction~   1 riga
    ~words of a younger sister~       1 riga
    ~Supporting Roles in Kitchen~     1 riga

⭐ E stavolta si e' anche fatta la domanda della 116a — *questo titolo
contraddice un nome gia' a schermo?* — su tutt'e sei, invece di aspettare che
saltasse fuori: «il dio della distruzione» e «sorella minore» sono le forme che
il dizionario usa gia'. Nessuna terza forma. Il numero e' scritto qui **prima**
del montaggio.

### ⭐⭐ L'INGLESE SBAGLIA IN GROSSO TRE VOLTE, E DUE SONO PAROLE SOSTITUITE

  - `:73631` (<Scorticatore Vitale>): **lascia cadere la seconda frase
    intera**, cioe' da dove viene il bastone — le ossa e gli occhi di una
    bestia magica leggendaria, abbattuta al prezzo di migliaia di vite di
    maghi. L'inglese e' una riga sola e la storia sparisce;
  - `:78052` (<Battipalo>): il giapponese dice che a usarlo di gusto e' «un
    fedele accanito di Mani o un **romantico**» (ロマンチスト). L'inglese
    scrive «maniac», che e' un'altra parola e rovescia il senso della battuta:
    il giapponese prende in giro chi ama le macchine, non chi e' pazzo;
  - `:77706` (<Sciabola Dinamica>): 振るうと力が湧いてくる vuol dire «a
    girarla, ti monta dentro la forza» — l'effetto e' su **chi la impugna**.
    L'inglese scrive «it produces a shockwave of power», che e' un'onda d'urto
    e non esiste nel giapponese.

⚠️ La seconda e la terza **nessun cancello le puo' vedere**: l'inglese e'
grammaticale, coerente e plausibile. Solo il giapponese accanto le smaschera.

### ⚠️ E DUE VOLTE APPIATTISCE, NELLA STESSA RIGA

`:67530` (<Housenka>): il giapponese dice che il capo dello sviluppo la
**destino' alle armi pesanti** (大型兵器用にした), e l'inglese scrive «larger
and more powerful», che e' un'altra cosa; e la balsamina del paragone
**sputa i semi** (種を放つ), che e' tutto il punto dell'immagine — l'inglese
scrive «explodes like a rose balsam» e il seme non c'e' piu'.

E `:67181` (falce a catena) perde la frase del 護拳, la guardia sul manico che
serve perche' il contraccolpo della catena non ti faccia ferire la mano sulla
lama.

### ⓘ Il lotto e' uniforme, e la cosa si e' misurata

Tutte e trentacinque le righe hanno lo spazio prima del `\\n` e tutte e
trentacinque la coda `# ~` con lo spazio. Nel 041 c'erano **tre** eccezioni.
Non e' una regola: e' una proprieta' di questo intervallo, e si legge con
`_scheda034.py 042`.

ⓘ Il preflight e' passato al primo colpo: 0 guasti di struttura, nessuna parola
oltre i 14 caratteri, nessun carattere respinto.

### ⭐⭐⭐ IL MOLTIPLICATORE NON ERA NELLA TABELLA, PERCHE' LA RIGA GEMELLA NON C'E'

`applica` e' passato da 29.571 a **29.607**: **+36** per **35 rese**. Le altre
tre misure dicevano tutte 35 (`verifica --dizionario` 769 -> 734,
`_114-corpo-da-fare` 769 -> 734, `FILTER_WEAPON` 69 -> 34), e solo
`_107-descrizioni-item` diceva 36 (735 -> **771** rese del corpo).

**Che cosa e' successo.** Il giapponese di `:76863` (<Stormbringer>) compare
**due volte** nel sorgente: a `:76857` e a `:126843`. La seconda e'
**Mournblade**, la spada gemella — e si riconosce dal suo indice 3, che dice
«ストームブリンガーという兄弟剣が存在する». Le due righe hanno il giapponese
**e** l'inglese identici byte per byte, quindi la stessa firma, quindi una resa
sola le copre tutt'e due. E' una riga viva: sta nel normale `if ( jp ) … else`.

⚠️⚠️ **Ma Mournblade non e' in `lavoro/_107-daitem.jsonl`.** L'estrazione tiene
**una voce per firma**, e il conto lo dimostra: 2.580 voci, 2.580 firme
distinte. La riga di Mournblade non e' stata scartata per un difetto: e' stata
*accorpata*, e da quel momento nessuna tabella di lotto puo' offrirla.

⭐ **Quanto e' grande la famiglia**, perche' la prima domanda e' sempre quella:
`_107-descrizioni-item` conta il corpo **per riga** e dice 1.513 vive;
`_114-corpo-da-fare` lo conta **per firma** e dice 1.449. La differenza,
**64 righe**, e' esattamente l'insieme di quelle che nessun lotto potra' mai
scegliere perche' un'altra riga porta gia' la loro firma. Non sono perse: si
riempiono da sole quando si rende la gemella.

**Come applicarlo.** La lezione della 115a diceva «la differenza fra da fare e
vive in una categoria dice che da qualche parte c'e' un moltiplicatore». Qui la
categoria diceva 110 e 110 — nessuna differenza — e il moltiplicatore c'era lo
stesso, perche' **la riga gemella e' in un'altra categoria e non e' nella
tabella affatto**. La previsione giusta non si legge nella riga della tabella e
nemmeno nel lotto: si legge **contando il giapponese nel sorgente**, che e' una
riga di script.

ⓘ E qui il difetto non c'e': la resa di <Stormbringer> descrive la spada nera,
che e' la stessa cosa per tutt'e due, e i due indici 3 — quello che dice
«Mournblade» e quello che dice «Stormbringer» — sono resi da tempo e restano
distinti. Trentasei righe italiane per trentacinque rese, tutte giuste.
"""
