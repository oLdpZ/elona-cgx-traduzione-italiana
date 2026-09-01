# -*- coding: utf-8 -*-
"""121a - Lotto 059 di `db_item.hsp`: I LIBRI, e la categoria CHIUDE.

`FILTER_ITEM_BOOK`, righe da `:47220` a `:129580`: **23 righe** — 21
dell'indice 0 e 2 dell'indice 2 — su 23 oggetti. Con questo lotto
`FILTER_ITEM_BOOK` va a **0 da fare su 23 vive**, ed e' la **quattordicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 059`: **+24 per 23 rese**. C'e'
una **gemella**, la prima da sei lotti: `:129580` (`ITEM_ID_RED_BOOK`) e
`:129651` (`ITEM_ID_BOOK`) hanno giapponese e inglese identici byte per byte —
due oggetti che si chiamano tutt'e due 本, «libro» — e una resa li copre
tutt'e due. ⓘ `:129651` **non e' nel lotto e non e' nel dossier**: la sua
esistenza la dice solo lo strumento, contando il sorgente (lezione della 116a).

### ⭐⭐⭐ QUATTRO DIARI CHE DEVONO RESTARE UGUALI, E UNO CHE DEVE RESTARE DIVERSO

Quattro righe aprono con la stessa formula, parola per parola:

    ◯がしたためたとされる日記。

    :56055  執事    -> il maggiordomo
    :71100  誰か    -> qualcuno
    :76935  姉      -> la sorella maggiore
    :89284  お嬢様  -> la signorina

La resa e' **«Un diario che si dice vergato da ◯.»** in tutte e quattro, e
cambia solo il nome. E tre di loro chiudono anche con la stessa seconda meta'
— 中には … が事細かに書かれているという — resa «Dentro, a quanto pare, … per
filo e per segno.» ⓘ したためる non e' 書く: e' il verbo formale del
*mettere per iscritto*, e «vergare» e' il suo pari in italiano.

⚠️⚠️ **E `:97200` NON e' della serie.** Il diario della sorella minore dice
妹が**書いた**日記 — il verbo comune — e la resa dice «Il diario che ha scritto
la sorella minore». A distinguerlo e' l'originale, e appiattirlo sui suoi
quattro fratelli sarebbe stato «migliorare» il testo cancellando una
differenza che l'autore ha scritto. ⭐ E' la lezione della 119a al rovescio:
li' l'inglese aveva ricopiato righe che dovevano differire, qui il rischio era
uniformare righe che l'inglese tiene distinte per caso e il giapponese per
scelta.

⭐ **I due diari segreti** — `:76791` la sorella cane maggiore, `:89356` la
sorella gatta minore — hanno la seconda meta' **identica byte per byte** in
giapponese. Le due rese cambiano «maggiore»/«minore» e nient'altro: i due
oggetti stanno uno accanto all'altro nell'inventario di chi li colleziona.

### ⭐⭐⭐ UN SEGMENTO CHE ESISTE SOLO IN INGLESE, E NON E' UNA RINVIATA

`:89358`, `description(2)` del diario segreto della sorella gatta.

    db_item.hsp:89352   description(2) = ""                       <- ramo jp
    db_item.hsp:89358   description(2) = "\\"Nyo reading!\\" ..."   <- ramo en

Il giapponese **non c'e'**: e' la stringa vuota, non una frase mancante.
⚠️ La tentazione e' trattarlo come `:129299`, la rinviata della 119a. **Non e'
lo stesso caso, e la differenza sta scritta nella rinviata stessa**: li' il
testo non ce l'aveva *nessuna delle due lingue* («la riga non ha testo in
nessuna delle due lingue»), e una resa avrebbe inventato. Qui l'inglese un
testo ce l'ha, e vale il precedente della 110a — *il giapponese vuoto e
l'inglese pieno: la riga si rende*.

⭐ E il bisticcio si puo' rendere perche' il gioco lo ha gia' reso altrove:
«Nyo reading!» e' il gatto che dice «no», e il tic della sorella gatta nel
dizionario e' **«miao»** in coda alla frase («E va bene, miao!», «Basta che tu
abbia capito, miao»). La resa e' «Vietato leggere, miao!».
ⓘ ⚠️ Altrove il progetto fa il contrario e **butta** il gatto inglese: le
battute di Mia («Nyobody knyows...») sono rese dal giapponese, che di gatto non
ha niente. Non e' incoerenza: e' che li' un giapponese c'era.

### ⭐⭐ CAIN NON ESISTE: SI CHIAMA CAIM

`:74101`, il diario del folle. Il giapponese dice 発狂したカイン, l'inglese
«a mad man named **Cain**» — e chi rende dall'inglese scrive Cain.

Il personaggio in gioco e' `<Caim> il riccone folle` (`<Caim> the mad rich`), e
il dizionario lo chiama **Caim** in tutte le sue voci. L'inglese di questa riga
e' l'unico posto dove compare la n.
⚠️ Nessuna rete lo vede: e' un nome plausibile, ed e' anche un nome vero.

### ⓘ Altri quattro punti dove il giapponese comanda

  - `:81064`, il libro di Bokonon: 真実であり、真っ赤な嘘である e' l'epigrafe
    dei *Libri di Bokonon* di Vonnegut, che in italiano suona «spudorate
    menzogne». ⚠️ L'inglese butta la seconda meta' e ci mette «granfalloon»,
    che il giapponese non nomina;
  - `:71100`, il diario di qualcuno: il giapponese dice **tre** cose (il nome
    non sta in copertina, non si sa di chi sia finche' non lo apri, e girano
    voci su un autore raro dopo una dozzina di letture); l'inglese ne tiene
    **una e mezza** e salta la seconda;
  - `:56201`: 開発主任 non e' «un capo progetto», e' `<Gavela> l'ingegnere
    capo`, un personaggio che il giocatore incontra;
  - `:86403`: レイチェル e' **Rachel**, ed e' una **donna** — «la scrittrice di
    favole Rachel», «una raccolta di fiabe che scaldano il cuore, firmata
    Rachel» — e i volumi sono quattro, come dice l'incarico di Renton.

### ⚠️⚠️ LA SPAZIATURA QUI NON E' UNIFORME IN NESSUNO DEI DUE PUNTI

Primo lotto della serie in cui `_forma.py` stampa due liste **diverse**:

    senza lo spazio prima del \\n : :47220  :57577  :71100  :93292
    senza lo spazio dopo il #    : :47220  :47222  :57577  :83697

⚠️⚠️ **E io ho letto «senza lo spazio prima del `\\n`» come «senza il `\\n`».**
Quattro rese sono uscite dal montaggio con la coda attaccata al punto finale, e
il segmento in meno. **`_preflight034.py` le ha prese tutte e quattro** —
«segmenti diversi: en 1, it 0» — prima del reimporta e prima della build.
⭐ E' il punto 3 del preflight, quello scritto nella 115a per un guasto
diverso, che qui ha pescato un errore di lettura di chi scrive le rese: la
riga di `_forma.py` dice due cose e io ne ho letta una.
"""
