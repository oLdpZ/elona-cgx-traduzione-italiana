# -*- coding: utf-8 -*-
"""116a - Lotto 041 di `db_item.hsp`: LE ARMI, il primo lotto della categoria.

`FILTER_WEAPON`, righe da `:43558` a `:66910`: **41 righe** su 39 oggetti — 39
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. La categoria e' la piu'
grossa fra quelle intatte, **110 su 110**, e come gli scarti non ha
moltiplicatore: «da fare» e «vive» coincidono, quindi `applica` deve salire di
**41 esatte**.

⚠️ L'intervallo si e' scelto in due tentativi, come vuole la 115a: `0 200000`
ha detto 110 righe da `:43558` a `:131182` (la categoria intera), e `0 67000`
ne ha dato 41. Le armi **non sono distribuite in modo uniforme**: fra `:43558`
e `:51779` c'e' un vuoto di ottomila righe, e poi trentotto righe stanno
addensate in quindicimila.

### ⭐⭐⭐ IL TITOLO-FONTE DICEVA UN TERZO NOME, E IL GLOSSARIO SI SMENTIVA DA SOLO

`:53420` porta la coda ～ソックスソードマンの評価～, che la tabella della 112a
rendeva `~Il Giudizio del Sockswordman~`. Ma ソックスソードマン e' gia' a
schermo, in `chat.hsp:12731`, come **«lo Spadaccino dei Calzini»**: e' il nome
da eroe che Kuroya si da' quando passa alle maniere forti.

⚠️⚠️ Le due forme stavano **nello stesso file**: `glossario.md:482` diceva
«lo Spadaccino dei Calzini» e `glossario.md:2221` diceva «Sockswordman». Un
documento che si contraddice da solo a millesettecento righe di distanza.

**Come si e' trovato:** non da una rete. `_113-fonti-gia-rese.py` cerca il
titolo **intero** e questo giapponese intero non e' reso altrove, quindi dice 0
su 41 con serenita'. L'ha trovato la ricerca a mano nel glossario, che la 111a
ha reso uno strumento (`lotti-111/_cerca.py`): e' la regola «le reti del lotto
non leggono il glossario», applicata e ripagata.

⭐ **La famiglia e' di una riga sola**, e si e' misurato prima di toccare:
ソックスソードマン compare **1 volta** in tutto `db_item.hsp`, ed e' questa. La
correzione della tabella non tocca nessuna resa gia' fatta. E' la lezione della
115a sulla tilde («la prima domanda e' quanto e' grande la famiglia»)
applicata a un difetto nostro invece che di monte.

Corretti `scratchpad/lotti-112/titoli_fonte.py` e `glossario.md:2221`.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, CIOE' INVARIATO

Le cinque code di questo lotto, e perche' nessuna ne aggiunge una settima:

    ~Irva Fantasy Encyclopedia~   26 righe  -> Dizionario Fantastico di Irva
                                  ⓘ e' gia' uno dei sei: l'altro giapponese,
                                    ～イムウエル幻想辞典～, va in «Aimwell».
                                    Qui il giapponese e' sempre ～イルヴァ～
    ~Collection of Armaments...~  12 righe  -> Raccolta di Armi e Armature...
    ~Book of Wisdom~               1 riga   -> Il Libro della Sapienza
    ~words of <Loyter>...~         1 riga   -> Parole di <Loyter>...
    ~words of a sockswordman~      1 riga   -> Il Giudizio dello Spadaccino...

Nessuno di questi inglesi copre due giapponesi diversi (controllato nella
tabella del glossario, righe 2116-2221), quindi **il cancello resta a 6**.
⭐ Il numero e' scritto qui **prima** del montaggio, come vuole la 115a: una
previsione, non una scusa.

### ⭐⭐ L'INGLESE LASCIA CADERE TRE FRASI INTERE

Non appiattimenti: frasi che nel giapponese ci sono e nell'inglese no.

  - `:53206` (<Engoku>): 見た目によらずかなりのハイテク武装で —
    «a dispetto dell'aspetto e' un'arma di alta tecnologia». L'inglese scrive
    «Pewter staff discovered in the ruins.» e salta diritto alla lama;
  - `:54316` (falce d'ossa): 一般的に見かけよりも軽く、鋭い —
    «di solito e' piu' leggera e piu' affilata di quel che sembra». L'inglese
    attacca con «However», che senza la frase prima non regge;
  - `:65879` (<Ivy Spine>): 下手に触れると死にたくなるような痛みと激しい吐き気
    に襲われる — il dolore da farsi venir voglia di morire e la nausea violenta.

⚠️ **Nessun cancello le vede**: l'inglese e' coerente con se' stesso e la resa
nostra e' piu' lunga, che non e' un difetto. Le vede solo chi legge il
giapponese accanto.

### ⭐ E DUE VOLTE L'INGLESE APPIATTISCE

  - `:52717` (<ANNINDOFU TIPO SPADA LASER>): il giapponese scrive **tre volte**
    杏仁豆腐 — l'oggetto e' budino di mandorle, l'elsa e' budino di mandorle, la
    lama e' budino di mandorle — ed e' tutta la battuta. L'inglese ne perde uno
    e scrive «Tofu attached to an Annin», che sono due cose diverse;
  - `:52996` (<Gouten>): 水中潜航や飛行 sono **due** capacita', immergersi e
    volare. L'inglese le fonde in «dive and fly underwater», che ne dice una
    sola e sbagliata.

### ⚠️ E UNA VOLTA CAMBIA LA RISORSA, COME I GLOBI OSCURI DEL 034

`:52857` (<Go-Renge>): il giapponese dice ＳＰ, l'inglese scrive «stamina». Si
segue il giapponese e si scrive **SP**, che e' la forma che il dizionario usa
gia' (`chat.hsp`, il consiglio sul recupero).

### ⭐ IL NOME DEL SOLDATO NON E' IL NOME DELLA SPADA

`:63723` (<The White Hawk>): l'oggetto e' **invariato**, perche' il giapponese
lo scrive in katakana (ウィーテハウク). Ma il soprannome del soldato di Zanan,
tre frasi dopo, e' 「白き鷹」 — giapponese vero, non katakana — e allora si
rende: **«il Falco Bianco»**.

ⓘ Il giapponese fa la stessa distinzione che facciamo noi: nome dell'oggetto
traslitterato, soprannome della persona in lingua. Non e' una scelta nostra, e'
la struttura della riga.

### ⚠️ LA RIGA DI GIOCO: <Necromantis> E QUATTRO TERMINI DEL DIZIONARIO

`:60786` e' l'unica riga del lotto che descrive un **effetto vero**, e i suoi
quattro termini si sono cercati invece di inventarli:

    パワーゲージ    -> la barra di potenza    (`chat.hsp`, il consiglio sulle gemme)
    使役           -> soggiogare             («Se ne puo' soggiogare uno solo»)
    棺             -> la bara                («Rimetti nella bara»)
    アンデッド      -> i non morti

⚠️ 融合アンデッド nel dizionario **non c'e'**. Si e' scritto «un non morto di
fusione», sulla forma dell'abilita' *Fusione dei morti* (`*死者融合*`), che e'
il nome che il giocatore vede per la stessa meccanica.

### ⚠️ TRE ECCEZIONI DI SPAZIATURA, TUTTE DICHIARATE PRIMA DEL MONTAGGIO

    :43558   la coda e' `#~` SENZA spazio; le altre venticinque di Irva l'hanno
    :63723   il corpo NON ha lo spazio prima del `\\n`
    :65265   idem

ⓘ Non si vedono leggendo il dossier: le da' `_scheda034.py 041` col `repr()`,
ed e' l'unica ragione per cui quello strumento esiste.

### ⓘ Il preflight ha detto una cosa sola, e aveva ragione

«dell'indipendenza», 17 caratteri, oltre la finestra di rinculo di 15. Riscritto
in «il simbolo di libertà e indipendenza» (12). Non si e' discusso se la parola
fosse lontana dal confine: costava una parola cambiarla.
"""
