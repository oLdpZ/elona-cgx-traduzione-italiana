# -*- coding: utf-8 -*-
"""116a - Lotto 043 di `db_item.hsp`: LE ARMI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_WEAPON`, righe da `:82945` a `:131182`: **34 righe** su 33 oggetti — 32
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. Con questo lotto
`FILTER_WEAPON` passa a **0 da fare su 110 vive**: e' la **quarta categoria
chiusa** del corpo dopo il mobilio (114a), gli attrezzi e gli scarti (115a), e
ci sono voluti tre lotti, dal 041 al 043, tutti nella stessa sessione.

⚠️ Come per il 037 e il 040, la coda di una categoria **non e' un intervallo
stretto**: le ultime 34 righe stanno sparse fra `:82945` e `:131182`, e ci e'
voluto `82000 200000`.

### ⭐⭐⭐ LA PREVISIONE DI `applica` SI E' FATTA CONTANDO, NON SPERANDO

Il 042 aveva chiuso con «previsione +35, misurato +36», e il colpevole era una
riga gemella che nessuna tabella nomina. La lezione si e' applicata **subito**,
prima di scrivere una sola resa: per ognuna delle 34 righe si e' contato quante
volte il suo giapponese compare nel sorgente pinnato.

    righe del lotto: 34   righe in piu' che applica tocchera': 0
    PREVISIONE applica: +34

⭐ E' una riga di script, e trasforma la previsione da speranza in misura. Va
fatta **ogni volta**, perche' la riga gemella non si vede ne' nel dossier ne'
nella tabella delle categorie: si vede solo nel sorgente.

### ⭐⭐⭐ LA GEMELLA DEL 042 SI E' RIEMPITA DA SOLA, E IL DOSSIER LO MOSTRA

`:126849` e' **Mournblade**, ed e' la riga che nel 042 aveva fatto salire
`applica` di uno in piu'. Nel dossier di questo lotto compare **gia' tradotta**,
con la resa scritta ieri per <Stormbringer>, e **non** e' fra le 34 righe da
fare: `_corpo.py` non la vede perche' non e' in `lavoro/_107-daitem.jsonl`.

⭐ E la coppia si legge tutta: l'indice 3 di Stormbringer dice «ha per gemella
Mournblade», quello di Mournblade dice «ha per gemella Stormbringer». Le due
prose sono la stessa perche' il giapponese e' lo stesso; i due indici 3 restano
distinti perche' il giapponese e' diverso. La firma ha fatto la cosa giusta.

### ⭐⭐⭐ L'INGLESE DELLA LANCIA E' QUELLO DEL BASTONE, COPIATO

`:116982` (長槍, la lancia) e `:117051` (杖, il bastone) portano lo **stesso
inglese, byte per byte**:

    A stick born to assist magic. Despite its everyday look, if you hit with
    it with all your might, your opponent will probably fall unconscious.

che e' la descrizione del **bastone**. Il giapponese della lancia dice tutt'altro
— 長い柄の先に尖った切っ先を持つ武器 — e l'indice 3 inglese della lancia e'
invece giusto («a polearm with a sharp point»). Quindi il difetto e' in una
riga sola del ramo inglese di monte, non in tutta la voce.

⭐ **Due giapponesi diversi fanno due firme diverse** (lezione della 115a):
le rese sono **due**, ciascuna scritta dal proprio giapponese, e chi gioca in
italiano vede la lancia descritta come una lancia — cosa che chi gioca in
inglese non vede.

⚠️⚠️ **PREVISIONE: `_coerenza` dira' «lo stesso INGLESE, rese diverse: 1».**
Non e' un guasto, e' il referto che si accende su questa coppia, ed e' atteso.
Se dicesse 0, vorrebbe dire che le due rese sono uguali, cioe' che abbiamo
copiato l'errore di monte.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, ANCORA INVARIATO

    ~Collection of Armaments...~   17 righe
    ~Irva Fantasy Encyclopedia~    15 righe  (gia' uno dei sei, per Aimwell)
    ~words of <Renton> the suffering wizard~   1 riga
    ~words of <Loyter> the crimson of Zanan~   1 riga

Nessuno di questi inglesi copre due giapponesi. E la domanda della 116a —
*questo titolo contraddice un nome gia' a schermo?* — e' stata fatta su tutt'e
quattro: <Renton> e <Loyter> sono nomi invariati, e «mago» e' la forma che il
dizionario usa per 魔術士.

### ⚠️ L'INGLESE ROVESCIA UNA FRASE, E STAVOLTA E' UNA PAROLA SOLA

`:127421` (<Diablos>): il giapponese dice che la lama nera scombina la mente di
**斬られた者**, «chi viene tagliato». L'inglese scrive «the spirit of the
cutter», cioe' **chi taglia** — il contrario. E' un rovesciamento come quelli
della 114a, e nessun cancello lo puo' vedere.

### ⓘ I CINQUE DONI DEGLI DEI, E PERCHE' NON C'ERA NIENTE DA DECIDERE

`:85642`, `:85714`, `:85785`, `:85857` e `:85927` sono i doni di Opatos, Ehekatl,
Jure, Itzpalt e Kumiromi, e ciascuna prosa nomina il proprio dio. I nomi **non
si sono scelti**: i cinque indici 3 di quegli stessi oggetti sono resi da tempo
e dicono gia' «il dio della terra», «la dea della fortuna», «la dea della
guarigione», «il dio degli elementi», «il dio del raccolto». Si sono copiati.

### ⓘ Due parole riscritte dal preflight, e una era la meno ovvia

    dell'oltretomba   15  -> «le fiamme che l'oltretomba manda» (12)
    un'organizzazione 17  -> «un gruppo di spie»

⚠️ La prima e' istruttiva: `dell'oltretomba` **esiste gia'** nel dizionario,
nell'indice 3 di quest'arma. Non e' un errore li': l'indice 3 **non si
impagina**, e la finestra di rinculo non lo riguarda. La stessa parola e'
legittima in un campo e troppo lunga nell'altro, e a saperlo e' il cancello,
non l'occhio.

### ⚠️ Un heredoc vuoto ha bloccato il terminale, per la settima volta

Scritto `python - << 'FINE'` con il corpo vuoto per saltare un passo. Due minuti
di terminale fermo, chiuso con `TaskStop`. E' esattamente il caso che i
documenti descrivono dalla 104a e che la 115a aveva gia' ripetuto. Le due
correzioni sono state fatte con lo strumento di modifica, che e' quello che la
regola dice di usare.
"""
