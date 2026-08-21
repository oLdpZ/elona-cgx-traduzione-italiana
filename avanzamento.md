# Avanzamento

Aggiornato a mano dopo ogni reimportazione. I numeri si rifanno con:

```powershell
python -m strumenti.verifica --dizionario
```

**L'unità è la firma, non l'occorrenza.** Il piano della Fase 1 contava le
occorrenze (2.127 per `text.hsp`), ma il dizionario è indicizzato per contenuto:
una stringa che compare tre volte è **una** voce da tradurre e tre sostituzioni
in fase di build. Tradurre si conta in firme; l'effetto a schermo si vede nelle
occorrenze. Le due colonne stanno qui entrambe perché servono a cose diverse.

| file | tradotte | firme | % | occorrenze |
|---|---|---|---|---|
| `text.hsp` | **1.718** | 1.720 | **100%** | 2.127 |
| `command.hsp` | **795** | 1.304 | 61% | 1.481 |
| `action.hsp` | **1.286** | 1.288 | **100%** | 1.502 |
| `proc.hsp` | **127** | 1.098 | 12% | 1.327 |
| `skill.hsp` | **885** | 885 | **100%** | 894 |
| `trait.hsp` | 0 | 373 | 0% | 406 |
| `db_item.hsp` | **1.606** | 1.606 | **100%** | 1.607 |
| `item_data.hsp` | **318** | 318 | **100%** | 318 |
| `custom_tweaks.hsp` | **12** | 12 | **100%** | 28 |
| **totale** | **5.952** | **8.604** | **69%** | **9.690** |

⚠️ **Questa tabella è ferma, e la riga di `command.hsp` è l'unica riaggiornata
(2026-08-15, 45ª: 795 su 1.304, più 20 rinviate).** `proc.hsp` dice 12% ed è chiuso dalla 39ª; il totale in
fondo somma valori di sessioni diverse. Il conto vivo lo danno
`python -m strumenti.verifica --dizionario` per il perimetro `lang()` e
`python scratchpad/perimetro.py` per il totale vero, descrizioni degli oggetti e
file di `data/` compresi. Finché nessuno rifà la tabella intera, **si guardano
quelli**.

## Fuori dalla Fase 1

`db_creature.hsp` non è in Fase 1, ma dal 2026-08-11 è il file su cui si lavora
insieme a `proc.hsp`: le sue **battute** sono le stringhe a frequenza più alta di
tutto il gioco. Vedi `decisioni.md`, 2026-08-11.

Le 3.655 firme del file, misurate con `strumenti/creature.py` più il dizionario:

| classe | rese | da fare |
|---|---|---|
| nome | **1.131** | 0 ⭐ chiusi |
| battuta (`voce`) | **2.519** | 0 ⭐ chiuse |
| senza classe | 1 | 0 |
| rinviate (righe commentate) | — | 4 |
| **totale** | **3.651** | **4** |

⭐ **Aggiornato a fine trentunesima sessione (2026-08-13): il file è chiuso.**
Le quattro voci che restano sono le righe commentate rinviate apposta, e
`verifica --dizionario` continuerà a contarle per sempre. Fuori conto resta
`86293`, la battuta col ramo inglese vuoto, che `estrai.py` non vede nemmeno.

Le battute si sono chiuse in tre tappe: i lotti `015`-`026` della 27ª coprono i
livelli **6-45** — le creature di citta', i PNG di trama e i primi sotterranei;
i dieci lotti `027`-`036` della 30ª i livelli **45-157**, cioè i PNG delle
gilde, i boss di trama e i mostri di Nefia profonda; i sei lotti `037`-`042`
della 31ª tutto il resto, **159-1200**: i demoni, gli dèi del Patto Eterno, gli
otto dèi di Elona e le loro forme potenziate.

⚠️ **Il file è chiuso nel dizionario, non a schermo.** Delle 2.519 battute rese
ne sono state viste in gioco poche decine. Vedi `RIPRESA-sessione.md`, «Il
collaudo, punto per punto».

⚠️ **I nomi risultano chiusi solo dopo la 27ª**, e l'ultimo che i conteggi
mostravano da fare **non esisteva**: stava su una riga commentata
(`db_creature.hsp:105060`), e la riga viva sotto era gia' tradotta. Le 4
rinviate sono tutte righe commentate senza nessuna occorrenza viva: `estrai` le
toglie dai lotti, `verifica --dizionario` continua a contarle fra le non
tradotte. Vedi `decisioni.md`, 2026-08-12.

Quanto segue vale da fine ventiseiesima sessione (2026-08-11). Le battute rese
sono passate da 546 a 960 in un giorno — quattordici lotti, `fase2-battute-001`
… `-014` — e sono **tutte su creature di livello 1-6**, cioe' gli abitanti delle
citta'. Non e' un caso: da questa sessione i lotti si compongono in **ordine di
livello crescente** e non piu' in ordine di riga. Vedi `decisioni.md`, la
sezione sull'ordine dei lotti.

⚠️ **Il conto delle battute è cambiato di significato il 2026-08-11.**
`strumenti.creature` ne dichiarava **320** e il numero era sbagliato: il ramo
inglese di una battuta sta dentro `cnvtalk()`, e la classificazione ne vedeva un
ottavo. Ora sono **2.465** firme in tutto. Un confronto con un numero scritto qui
prima di quella data non ha senso.

⚠️ `strumenti.creature` stampa **2.466** e non 2.465: conta le **coppie
(giapponese, inglese)** delle righe, e una di esse non diventa una firma a sé.
I due numeri misurano cose diverse e non vanno sommati fra loro.

⚠️ **Il denominatore di `text.hsp` è sceso da 1.740 a 1.720** il 2026-08-11: le
20 firme di `elename()` non erano arretrato ma **rinviate**, e ora che sono
tradotte sono passate dal fuori-conto al numeratore. Le 2 che restano aspettano
`data/talk.txt`, e il file è **chiuso**.

⚠️ **Due di questi 100% sono falsi, e il 2026-08-10 si è misurato di quanto.**
`db_item.hsp` ha **261** `iknownnameref` — i nomi che il gioco mostra prima
dell'identificazione, tipo `colorful eyes` — e `custom_tweaks.hsp` ha **77**
etichette del menu opzioni: nessuna delle due classi passa da `lang()` né
dall'estrattore, quindi non sta né al numeratore né al denominatore. In tutto
sono **391 stringhe visibili** sparse su nove file. Non è un errore di calcolo:
il denominatore conta solo ciò che l'estrattore sa vedere. Il dettaglio, il
censimento e l'ordine con cui affrontarle stanno in `decisioni.md`, 2026-08-10.

⚠️ Le 2 firme che mancano ad `action.hsp` **non sono arretrato**: sono le due
righe rinviate a toppa (`:4584`, l'articolo inglese davanti a un'arma unica, e
`:9631`, il possessivo `his(tc, 1)` che in italiano si omette). Il file è
chiuso; il conto le porterà per sempre. Vedi `decisioni.md`, 2026-08-10.

Fuori dalla Fase 1, con conteggio proprio: `db_creature.hsp`, **1.452 firme su
3.655** — tutti e 1.131 i nomi, l'epiteto e le **320 stringhe di voce**, chiuse
il 2026-08-10. Le 2.203 righe rimanenti del file sono dialoghi e descrizioni.

⚠️ **Tre file nuovi nel perimetro dal 2026-08-10**, entrati per riparare le
rinomine all'evoluzione (vedi `decisioni.md`, diciottesima sessione). Non erano
nel piano della Fase 1 e hanno un conteggio proprio:

| file | tradotte | resta | perché è entrato |
|---|---|---|---|
| `custom_enemyevolution.hsp` | **368** | **0 — chiuso** | 418 letterali `evold`/`evname` rimasti inglesi |
| `ai.hsp` | 6 | 94 | 16 letterali, stessa causa |
| `event.hsp` | 5 | 649 | 6 letterali, stessa causa |
| `init.hsp` | 6 | 133 | già nel perimetro da prima |
| `chara_func.hsp` | **45** | 286 | 2026-08-11: chiude la frase di combattimento, vedi sotto |
| `buff.hsp` | **136** | 63 | 2026-08-13: `buffname` (29ª) e `bufftxt` (31ª) chiusi; restano i `buffdesc` |

## `*chat_default` chiuso, le gilde e il tutorial — 2026-08-21, settantottesima sessione

Tre lotti grossi invece di nove piccoli, e ognuno chiude una cosa intera.
**270 rese**, nessuna toppa, nessuna rete nuova.

| lotto | rese | esito |
|---|---|---|
| `*chat_default` | 81 | **CHIUSO** salvo la famiglia evochat, dichiarata fuori |
| il sistema delle gilde | 97 | tre maestri, tre guardiani, tre investigatori |
| l'inizio della storia e il tutorial | 92 | Larnneire, Rianna, Lomias, il tutorial intero |

`chat.hsp` scende da 3.147 a **2.877**. `menu_dialogo` misura **731** voci
(erano 675), `bilingui` resta a **0** — e in tutt'e tre i lotti ha dato zero al
**primo** giro, che non era mai successo.

### ⚠️⚠️⚠️ Il conteggio `--da-tradurre` mente sul perimetro di un blocco

`estrai --da-tradurre` ancora una voce per **firma** alla **prima**
occorrenza. Chi legge quell'elenco per sapere «che cosa manca in questo
blocco» prende un numero sbagliato per difetto, e non se ne accorge: in
`*chat_default` le firme erano **89**, non le 77 che l'elenco mostrava. Le
dodici mancanti avevano la prima occorrenza altrove.

E due delle dodici erano **voci di menu**: «Sorry.» vive anche nel menu della
gatta Sinaha (`:10880`), «Hold on.» in quello della barca di Regulus
(`:13590`). Tradurre le 77 dell'elenco avrebbe lasciato **due menu a meta'** in
posti che nessuno stava guardando.

💡 La regola: *per sapere che cosa manca in una zona si guardano tutte le
occorrenze di tutte le firme, non l'elenco del lavoro che resta.* Il conto
giusto e' «firme non tradotte con **almeno un'occorrenza** nella zona».

⭐ Nel lotto del tutorial la stessa cosa e' successa in grande: 「わかった」 vive
in **sette** menu lontani (`:9575`, `:9588`, `:10671`, `:11830`, `:15186` per
«Alright.», `:2210` e `:2215` per «Will do.»), ognuno con la sorella ancora
inglese. Otto sorelle aggiunte al lotto, e `bilingui` a zero al primo giro.

### ⭐⭐ In `*chat_unique` si prende un SISTEMA, non un parlante

`*chat_unique` e' uno smistamento `_switch_val == CREATURE_ID_x`, quindi la
tentazione e' il lotto per personaggio. Ma le tre gilde sono **sei blocchi
quasi identici fra loro** piu' tre investigatori a Tyris del Sud: prese
insieme, il glossario si decide una volta e le sei schermate parallele dicono
le stesse parole.

⭐ **E il glossario non si e' deciso: si e' ripreso.** Gilda dei Maghi /
Guerrieri / Ladri e «il maestro della gilda» stavano gia' in `command.hsp` e
`text.hsp`; «il guardiano» e «l'investigatrice» nelle domande del quiz; «punti
gilda», «obiettivo» (per la ノルマ), «grimorio», «refurtiva», «Nefia casuali di
tipo X di livello Y o piu'» nelle voci di diario che annotano le stesse prove.
Le tre prove d'ingresso adesso dicono **le parole del diario che le annota**.

Lo stesso nel tutorial: `<Mangia>`, `<Leggi>`, `<Scava>`, `<Equipaggia>`,
`Tiro` e i tasti `g` e `d` si copiano da `text.hsp`, che il progetto ha gia'
tradotto. Un tutorial che nomina i menu con parole sue sarebbe peggio che
inglese.

### ⚠️⚠️ Il perimetro si taglia dove il menu di monte e' ancora inglese

Le tredici rese della famiglia **evochat** — le dieci «route», i due esiti del
cuore, il potere di scasso — sono rimaste fuori da `*chat_default` apposta: il
menu che le accende (`:19250`-`:19278`) e' ancora tutto inglese, e tradurne il
solo esito produce la meta' **peggiore**, menu inglese e risposta italiana.

💡 *La direzione conta.* Menu italiano e risposta inglese e' il difetto che la
73a ha corretto in massa; il rovescio — risposta italiana sotto un menu inglese
— e' lo stesso difetto girato, e nessuna rete lo misura perche' `bilingui`
guarda i gruppi di `chatList`, non i percorsi.

### ⭐ Un referto che nessuno leggeva aveva ragione

`scratchpad/referti.py` segnalava da sessioni tre participi. Due sono falsi
positivi legittimi («te lo sei preso» concorda con l'extraterrestre, «te la sei
cavata» e' l'idioma), il terzo no: `chat.hsp:18483` diceva **«non sei
riuscito»** al giocatore. Corretto; il referto scende da 3 a 2.

## `*chat_default` svuotato a meta', e la firma condivisa come regola — 2026-08-21, settantasettesima sessione

Nove lotti dentro `*chat_default` e nei blocchi che le firme si sono tirati
dietro. **152 rese e una toppa**, senza reti nuove: le quindici c'erano gia' e
hanno lavorato tutte.

| pezzo | rese | esito |
|---|---|---|
| le due arene | 17 | duello, rissa, animali, squadre, EX, punteggio |
| l'informatore | 12 | la lista, il messaggio, la sequenza del compleanno |
| il dojo di Nazuna | 37 | il blocco `:8812`-`:9186` chiuso intero, piu' cinque menu lontani |
| l'ingaggio e il reclutamento | 11 | `chatval` 50 e 51 |
| il mercante di schiavi | 9 | vendere, comprare, la madre di Pael |
| quel che i PNG rispondono | 21 | confessione, sfratto, portafogli, spostati |
| il nome della casa | 12 + toppa | l'ordine girato, provato sul banco HSP |
| il dio e l'indulgenza | 14 | il numero nuovo, l'offerta, il prete |
| i servizi che si pagano | 19 | identificare, curare, il rifugio, il veicolo |

`chat.hsp` scende da 3.299 a **3.147**. `menu_dialogo` misura **675** voci (erano
629), `bilingui` resta a **0** e `maiuscole` passa da 9 appesi a **7**.

### ⚠️⚠️⚠️ La firma condivisa non e' un caso limite: e' la forma normale del file

Tre volte su nove lotti una resa ha acceso menu che non stavo guardando, e ogni
volta l'ha detto `bilingui` **dopo** la reimportazione, mai una lettura del
codice — perche' finche' un menu e' tutto inglese non c'e' niente da vedere.

| firma | rappresentante | menu accesi |
|---|---|---|
| 「やめる」/«No way!» | `:9051` | il blocco 47 dell'informatore |
| 「断る」/«I refuse.» | `:2351` | Erystia, le monete di bronzo, la droga in capsula, la tartaruga |
| 「いいよ」/«Sure.» | `:8197` | la lettera di Siraha, la tartaruga della principessa |

💡 E chiuderne uno ne apre un altro: la resa delle **monete di bronzo**, scritta
per chiudere il menu di `:2996`, ha acceso il menu del potioman a `:3029`. Tre
giri di rete per arrivare a zero. *La rete va rilanciata dopo ogni giro, non una
volta sola.*

⭐ **E l'altra faccia paga**: `:20576` e' la firma di **tutti** i «Thanks!» del
file (`_thanks(2)`), quindi una resa sola ne ha resi una decina.

### ⭐⭐⭐ Il nome della casa: la soluzione non era una resa, era l'ordine

`chat.hsp:22500` **appende** all'epiteto uno degli undici suffissi di `:22498`
(«Silver Spectre Hovel»). In italiano l'epiteto e' gia' un sintagma intero —
«fragore della dipendenza» (64a) — e il suffisso in coda non e' italiano. Il
giapponese ha la struttura **nostra**, 「<epiteto>の家」 = «casa DI <epiteto>»:
la toppa 1017 gira la concatenazione nel solo ramo inglese e i suffissi
diventano prefissi che finiscono in «di».

⚠️ «di» e' la sola preposizione che regge: qualunque articolo si accorderebbe
col primo nome dell'epiteto, che cambia a ogni tiro. ✅ Provato sul **banco HSP**
fuori dal gioco: «Castello di Quiete del figlio», «Tana di Dea dell'uccello»,
dodici tiri, nessuno storto.

### ⚠️⚠️ E un test ha corretto una cosa che avevo scritto in un commit

`strumenti/maiuscole.py` legge la **build**, non il sorgente pinnato. Le due
rese di `:22375` e `:24739` mettono il nome in testa, quindi quei due siti sono
usciti dagli «appesi» da soli e i loro permessi in `GIUDICATI` restavano
attaccati al vuoto: l'ha detto `test_i_giudicati_esistono_ancora`, che esiste
apposta.

## I menu bilingui, e la rete che li conta — 2026-08-21, settantaseiesima sessione

Nata da un difetto trovato traducendo: il dizionario è per **firma**, quindi una
voce di menu resa in un punto del file ne rende un'altra in una schermata
lontana, che resta metà italiana. **121 rese, una rete nuova, 11 test.**

| pezzo | rese | esito |
|---|---|---|
| `chat.hsp`, l'oste | 18 | i cinque `chatval` della taverna e il kiseru |
| `chat.hsp`, il figlio | 11 | il menu dell'istruzione, sette voci |
| `chat.hsp`, il lupo mannaro | 13 | i sette toni dell'accusa e l'indagine |
| `chat.hsp`, le indicazioni | 21 | le direzioni, la guida, e la scena di Jure per forza |
| `chat.hsp`, i menu bilingui | 58 | quindici schermate chiuse, in tre lotti |
| `strumenti/bilingui.py` | — | rete nuova, quindicesima verifica, 6 test |
| `strumenti/menu_dialogo.py` | — | due difetti nella misura delle dinamiche, 5 test |

`chat.hsp` scende da 3.420 a **3.299**. `menu_dialogo` misura **629** voci (erano
572) e `bilingui` ne trova **0** a metà, su tutti i file con dizionario.

⚠️ `rinviate.jsonl` sale a **75**: le due righe **commentate** di `chat.hsp:19327`
e `:19334`, che erano state tradotte e per questo erano entrate nelle misure.

## Le gemelle, e i quattordici menu di `chat.hsp` — 2026-08-20, settantatreesima sessione

Nata dalla misura della 72ª: 417 rese che esistevano già in un altro file di
dizionario e che nessun referto nominava. **296 rese, una rete nuova, 22 test.**

| pezzo | rese | esito |
|---|---|---|
| `strumenti/gemelle.py` | — | rete nuova, tre classi, 22 test |
| `chat.hsp` fuori dai menu | 120 | la finestra delle modalità, i materiali del compagno |
| `chat.hsp`, i quattordici menu | 152 | 76 gemelle + 78 sorelle + 2 correzioni di misura |
| `event.hsp` fuori dal generatore | 24 | e il menu `4504-4509` chiuso intero |
| `event.hsp:1070` | 1 | la sorella mancante di un menu da due voci |
| il generatore di `event.hsp` | 193 | 158 pezzi e 35 cornici, con la grammatica nuova |
| intorno al generatore | 16 | dal collaudo: titoli, bottoni, registro, la paga |

`chat.hsp` scende da 3.920 a **3.648** e `event.hsp` da 622 a **394**: nessuno
dei due ha più gemelle. **505 rese in tutto, in dieci spinte.**

### ⭐⭐⭐ La schermata di collaudo che ha trovato una cornice mancante

La frase del generatore era arrivata e stava in piedi; **intorno** c'erano il
titolo inglese di ogni evento, l'unico bottone della finestra, le due righe di
registro che escono sempre — e una riga **mezza italiana** fatta da noi la
mattina stessa: «As a salary, 215 monete d'oro e 2 oggetti have been sent to
your house.» I pezzi erano fra le 24 gemelle importate, la cornice di
`event.hsp:4467` no. 💡 *Una resa può essere giusta e fare danno perché la
cornice che la incornicia non è arrivata.*

### Le tre classi, misurate su tutto il progetto

    gemelle      392 -> 59     la firma combacia: valida per costruzione
    divergenti    13 ->  2     già resa in due modi: sceglie chi legge
    quasi        201 -> 162    solo il giapponese: da leggere, mai da travasare

Delle 59 che restano, **21 sono `custom_autopick.hsp`**, che è delicato: il
resto è pulviscolo su quindici file. La famiglia è, in pratica, chiusa.

### ⭐⭐ Il generatore degli eventi di viaggio

Le 116 gemelle ferme in `event.hsp` erano i **pezzi di un generatore**: `hito`,
`mon`, `tori`, `item`, `drink`, `tree` più i due modificatori `donna` e
`nagara`, montati a caso in 35 cornici (`3523-3629`). La grammatica — articolo
dentro il pezzo, `donna` invariabile e postposto, cornici senza participi che si
accordino — sta in `decisioni.md`.

⭐ **Provata componendo tutte e 35 le cornici due volte**, una con i pezzi tutti
femminili e una con tutti maschili, e **leggendole**: tre riscritte, e nessuna
delle tre per un accordo (una reggenza, una ripetizione, un'ambiguità).

⭐ **La geometria misurata, non stimata**: `talk_conv` va a capo a 34 caratteri
in mare (`bg_re25`) e 48 in viaggio (`bg_re13`), e la finestra **cresce di 15 px
a riga**. Caso peggiore: una riga più dell'inglese, cinque in tutto.

### ⭐⭐⭐ 82 gemelle su 194 stavano dentro un menu, e nessun menu si chiudeva

È il pezzo che vale più della rete, e non era nel piano. Il menu dello stile di
combattimento (`8991-9004`) aveva **tre** gemelle su quattordici voci:
importarle sole avrebbe portato la schermata da inglese e coerente a metà
italiano e incoerente. I quattordici menu sono stati chiusi **interi**, con 78
sorelle scritte a mano:

    2630-2745   i materiali del fabbro            40 voci
    20318-20351 che cosa pensi del compagno       30 voci   (due colonne)
    8991-9004   lo stile a mani nude              14 voci
    20296-20307 le regole del compagno            12 voci   (due colonne)
    11253-11263 l'elemento da imparare            11 voci
    16737-16746 la parte del corpo da far crescere 10 voci
    13650-13658 quale dio                          9 voci
    7012-7021   il sindaco                         7 voci
    17702-17716 le azioni AP del compagno          6 voci
    9195-9209   i biglietti del casinò             4 voci
    13772-13775 il mercante di scorte              4 voci
    + 1376, 7370, 10997, 22111                     4 menu da due voci

⚠️ **Sei gemelle scartate**: `claw`, `spore` e `branch` perché in `text.hsp`
sono il **verbo** del colpo e qui serve il nome dello stile; tre perché
`text.hsp:1523-1556` è lo stesso elenco visto da un pannello con la colonna più
larga, e qui il tetto delle due colonne è 24.

`menu_dialogo`: 0 fuori misura su **417** misurate (erano 257) e 0 peggiorate a
due colonne — e la rete ha preso due righe nostre troppo lunghe prima che
arrivassero a schermo.

### Altre decisioni prese leggendo il sito, non la stringa

- 腰 nella lista delle parti del corpo diventa **«Fianchi»**, non «Vita»: la voce
  dice già «(Vita -3)», e due «Vita» nella stessa riga sono illeggibili.
- le azioni AP prendono il nome che `skill.hsp` ha già («Sincronia delle anime»,
  «Guardia metallica»): un'azione non può chiamarsi in due modi fra il menu che
  la compra e la barra che la usa.
- `準備中` è **«In preparazione»**, non «Cancel»: nessun ramo raccoglie quella
  scelta, e l'inglese di monte lo nasconde.

---

## Due file chiusi e il menu del dialogo — 2026-08-20, settantaduesima sessione

Nata da un collaudo di quattro schermate. 289 rese, due file chiusi, tre reti
toccate (due nuove), otto toppe.

| pezzo | rese | esito |
|---|---|---|
| i quattro inglesi del collaudo | 4 | `displace`, i due `gp`, «Premi un tasto per chiudere» |
| il menu del dialogo di `chat.hsp` | 125 | 100 voci di `*talk_main` più 19 del pannello |
| le dieci tagliate a due colonne | 10 | correzioni, **nove di sessioni precedenti** |
| `help.hsp` | 46 | ⭐ **CHIUSO**, 0 / 0 |
| `screen.hsp` | 98 | ⭐ **CHIUSO**, 0 / 0 (20 di combattimento + 78 cori) |

`chat.hsp` scende da 4.046 a **3.920**. I file con `lang()` e senza dizionario
passano da dodici a **dieci**.

### ⭐ Il menu del dialogo: 125 voci, raggruppate per SCHERMATA e non per file

Il perimetro non si sceglie per riga ma per **quello che si apre insieme**: le
100 voci di `*talk_main` (`chat.hsp:19340`-`19876`) e le 19 del pannello che
sta a sinistra (`:25480`-`:25610`) sono la stessa schermata, e il registro si
decide una volta sola.

⚠️ **E l'elenco per riga ne perdeva sei.** `estrai` raccoglie per **firma** e
riporta il **primo sito**: «Let's talk.» risultava a `chat.hsp:1326`, non a
`:19348`, e un filtro sul numero di riga non la vedeva. Il perimetro si prende
per firma, calcolando i siti.

### ⭐ `help.hsp` chiuso — 46 rese

Il più piccolo dei dodici file senza dizionario, e dentro ci sono due schermate
che si aprono il primo giorno: la ruota dei comandi e l'elenco dei tasti.

⚠️ Il tetto è **10 caratteri**, e non viene da un `sdim`: il testo è **centrato**
su piastrelle da 48 px (`help.hsp:105`, `x(cnt) + tx + 25 - strlen(s) * 3`) e
gli slot 0, 4 e 8 — i nomi delle quattro pagine — hanno passo 75 px.

Tre valori restano inglesi e sono in `invariati.md`, sezione nuova **«Chiavi e
nomi di file — non sono testo, sono indirizzi»**: `EN` è la chiave del blocco che
`:228` cerca dentro `manual_ENG.txt` con `instr`; `manual_ENG.txt` e
`scene2.hsp` sono argomenti di `noteload`. ⚠️ Il giorno che il manuale si
traduce, quella riga non diventa una resa ma una **toppa** con `manual_IT.txt` e
il ramo `exist` di ripiego — la disciplina di `board_it.txt` e `talk_it.txt`.

### ⭐ `screen.hsp` chiuso — il decimo punto cieco della 55ª

⚠️ **Non è l'HUD, come diceva l'elenco: sono due cose sotto un nome solo.**

    20 righe   combattimento e livello: « have gained a level.» era ancora
               inglese, ed è una delle righe più lette del gioco
    78 righe   i cori della battaglia finale, una voce per personaggio — gli
               otto dei, i compagni, i negozianti, la sorella, il cane poliziotto

La forma dei cori è `"<Nome> <verbo>, " + cnvtalk("<battuta>")`, e il
**giapponese non ha nessun verbo**: scrive 名前「battuta」 e basta. I verbi sono
un'aggiunta inglese ma sono caratterizzanti e si tengono, con i **due punti** al
posto della virgola — la punteggiatura italiana del discorso diretto, e lo stile
che il progetto usa già in `action.hsp:14051`.

I nomi restano quelli di monte, che il dizionario ha già da altri file. Si
traducono i quattro parlanti senza nome (la scienziata misteriosa, il cane
poliziotto, il guerriero leopardo, la sorella) e i due che un nome reso ce
l'hanno: «la principessa dell'abisso» (`db_creature.hsp:86765`) e il «vento
d'etere» (`chat.hsp:9500`).

### ⭐ Tre volte l'inglese aveva buttato via quel che il giapponese ha

    screen.hsp:6759   「はレベルNになった！」 dice a QUALE livello si sale
    screen.hsp:8076   シャキーン e ズバシュッ sono due onomatopee diverse — il lampo
    e :8099           della lama e il taglio — appiattite su un « *vorpal* »
    screen.hsp:1442   il giapponese saluta il giocatore per nome nella battuta
    help.hsp:866      il giapponese ha una seconda riga che l'inglese non ha

Tutte e quattro sono tornate. È lo stesso fenomeno dei 38 blocchi giapponesi che
`board.txt` ha perso e delle 13 righe di `ZAILE` in `talk.txt`: **l'inglese di
monte non è una copia del giapponese, è una riduzione.**

### Le otto toppe: 1009 → **1016**

    1010a-1012a   la gronda della scheda: wx+68 -> 79, wx+310 -> 325,
                  wx+410 -> 418. Curano ClasseGuerriero, Altezza157 cm,
                  Velocita70(70), AliasGiustizia del sole e Prossimo 3024
    1013a-1016a   i quattro cnven() appesi: chat.hsp:25573 («il cittadino
                  Femmina»), item_func.hsp (il suffisso di qualità di OGNI
                  oggetto identificato) e le due dell'elenco dei compagni

### Le reti

    menu_dialogo   +*talk_quest fra i gosub che NON disegnano: da 156 a 257
                   voci misurate, e dentro c'erano due difetti DI MONTE
                   +tagliate_a_due_colonne(): il secondo tetto, 24 caratteri
    gronde.py      NUOVA: lo spazio fra etichetta e valore. Legge la BUILD
    maiuscole.py   NUOVA: cnven() e la maiuscola in mezzo alla frase
    verifica.py    il metro delle interpolazioni è inglese PIÙ giapponese
    funzioni.py    cnvtalk è trasparente, non è una chiamata di contenuto

`pytest` da 653 a **684**.

---

## `item.hsp` chiuso — 2026-08-20, sessantanovesima sessione

**244 `lang()`, 242 rese, 2 rinviate.** Il file era il **quindicesimo punto
cieco**: aveva `lang()` e nessun file di dizionario, quindi non compariva in
`verifica --dizionario` e nessun conteggio lo guardava — la lezione della 54ª,
*un file senza file di dizionario non è un file finito, è un file che nessun
conteggio guarda*.

Otto lotti, in ordine di quel che il giocatore legge più spesso:

| lotto | righe | rese | che cos'è |
|---|---|---|---|
| `fase4-item-001` | `:3304`-`:3397` | 31 | che sapore ha quel che mangi |
| `fase4-item-002` | `:3471`-`:3888` | 22 | le erbe, la carne umana, i cibi speciali |
| `fase4-item-003` | `:3925`-`:4046` | 17 | il cioccolato, la mesugaki, la fortuna |
| `fase4-item-004` | `:4066`-`:4217` | 17 | i cibi che cambiano il corpo (6 invariati) |
| `fase4-item-005` | `:4258`-`:4324` | 7 | le abilità e la «Fase 2» (+ 2 toppe) |
| `fase4-item-006` | `:4335`-`:4648` | 36 | le carni e gli effetti |
| `fase4-item-007` | `:107`-`:127` | 42 | le cinque tabelle in testa al file |
| `fase4-item-008` | sparse | 32 | il parassita, la stima, la cronaca, la cucina |

Le due che il conto porterà per sempre sono `:4291` e `:4294`, terzo esemplare
della famiglia di `his2()` dopo `proc.hsp:11481` (36ª) e `proc.hsp:24107` (39ª):
risolte da toppa, come le altre due.

⚠️ **I file senza dizionario scendono da 13 a 12, e le `lang()` fuori da ogni
conteggio da 811 a 567.** Restano `txtadv.hsp` 170, `material_data.hsp` 118,
`custom_autopick.hsp` 90, `help.hsp` 52, `net.hsp` 37.

## `item_func.hsp` — gli stati del nome, 2026-08-20, sessantanovesima sessione

Non un lotto: **tre toppe e una resa**, nate da un collaudo che ha letto «un
piatto di **rotten** pasta fresca».

`item_func.hsp` è il compositore dei nomi degli oggetti: incolla una sessantina
di pezzi attorno al nome vero, quasi tutti **suffissi fra parentesi**
(`(Scary)`, `(Empty)`, `(Herb)`, `(Antiseptic)`, `(Poisoned)`…) e pochi
**prefissi**. I prefissi sono il problema: l'aggettivo italiano prima del nome
concorda col genere, e `rotten ` serve *ogni cibo del gioco*.

| pezzo | esito | perché |
|---|---|---|
| `rotten ` | **toppa** → ` (marcio)` in coda | nessun genere sicuro: serve ogni cibo |
| `sample ` | **toppa** → ` (campione)` in coda | idem |
| `[Growable] ` | **resa normale** → `[Coltivabile] ` | «coltivabile» è in **-e**, invariabile al singolare |

💡 La differenza fra i tre non è il posto in cui stanno: è **se l'italiano ha o
no una forma che non concorda**.

⚠️ **Lo stesso muro aspetta il prefisso del materiale** — `mtname(…) + lang("製の", " ")`
in tre siti, più le 118 righe di `material_data.hsp`: `mithril sword` in
italiano è «spada **di** mithril», postposta.

Restano **240** righe di `item_func.hsp`.

## I 71 `bufftxt` di `buff.hsp` — 2026-08-13, trentunesima sessione

**65 firme distinte coprono i 71 siti**: i tre 「装備の力を引き出した」 e i
cinque cambi di forma condividono la firma.

Non erano un lotto di rese ma **lavoro strutturale**, e sono servite due toppe:
una riporta il ramo inglese di `chara_func.hsp:2316-2375` alla forma giapponese
(63 righe diventano una, e `bufftxt(1)` — letterale nudo fuori da `lang()` in
tutte e 71 le righe — smette di essere letto); l'altra allarga
`sdim bufftxt, 30, 2, MAX_BUFF` a 128, perché l'italiano porta la frase intera e
arriva a 59 byte dove il giapponese si fermava a 28. Il ragionamento sta in
`RIPRESA-sessione.md`, «Le due toppe di `buff.hsp`».

⚠️ **Dei 71, zero erano già resi altrove** — l'opposto dei `buffname`, dove 44
su 71 si copiavano da `skill.hsp`. La differenza è che un nome di status è
anche il nome di un incantesimo, mentre il messaggio che lo annuncia non
compare da nessun'altra parte.

## I 71 `buffname` di `buff.hsp` — 2026-08-13, ventinovesima sessione

Prima fetta del blocco di Fase 4 anticipato dalla decisione 0. **71 voci, tutte
`statica`, tutte dentro `lang()` e autonome**: nessuna dipendenza strutturale,
che era il motivo per cui erano state scelte.

⚠️ **La ripresa diceva «~90 `buffname`»: sono 71.** Le 199 voci del file si
dividono in **71 `buffname`**, **65 `bufftxt`** (quelle spezzate in due, lavoro
strutturale) e **63 `buffdesc`**, che nessun documento nominava. La variabile
non sta nel JSONL: si legge rileggendo la riga del sorgente.

💡 **Solo 27 delle 71 sono state decise qui.** Le altre **44 avevano gia' una
resa**, quasi tutte in `skill.hsp`: un buff e l'incantesimo che lo concede sono
la stessa cosa per chi gioca, e il giapponese e' identico. Copiate dal
dizionario, non ridecise — vedi `decisioni.md`, «Un buff e' l'incantesimo che lo
concede».

Le 27 nuove, per gruppo:

- **i dieci `Grow X`** prendono il nome d'attributo gia' chiuso in `skill.hsp`
  (`Crescita della forza`, `… della costituzione`, `… dell'apprendimento`);
- **le cinque `Form Shift`**, `Cambio di forma (A)`/`(B)`/`(G)`/`(D)` e
  `Cambio di forma finale`;
- **dodici sparse**, fra cui `Punizione divina`, `Fortuna`, `Sfortuna`,
  `Distrazione`, `Malinconia`, `Maledizione della fame`.

Le tre etichette di stato pure — `Distracted`, `Melancholy`, `Unlucky` — sono
rese **sostantivi** e non aggettivi, come impone la guida di stile: `Distrazione`
e non `Distratto`, che vorrebbe il genere di chi lo subisce.

Catena verde: `verifica` 0 problemi al primo colpo, **398 test**, prova
d'identita' **72/72 e 27.813**, larghezze 0/75, diario 0/214.

## `chara_func.hsp` entra per 45 firme — 2026-08-11, diciannovesima sessione

Quarto file fuori piano, ed entrato per la stessa ragione dei tre della
sessione prima: un valore che il perimetro produce e che qualcuno fuori
consuma. Qui però non è un confronto, è **una frase**.

`action.hsp` scrive la prima metà del messaggio d'attacco — «il putit morde il
viandante e» — e imposta `gdata(GDATA_DMG_TYPE) = 2`; `chara_func.hsp:6323`
legge quel flag e stampa la seconda metà, «infligge una lieve ferita.», con
`txtcontinue` che sopprime la maiuscola. Sono 45 firme su 331: **solo la zona
del danno**, non il file intero.

Il criterio del taglio è quello che vale la pena tenere: si allarga il
perimetro alla **zona che chiude la frase**, non al file che la contiene. Le
altre 286 firme di `chara_func.hsp` restano fuori finché non serviranno.

⚠️ La causa di morte (`chara_func.hsp:6850`) è rimasta fuori di proposito: la
frase la compone `main.hsp:4409`, che non è nel perimetro. Tradurla darebbe
«<epiteto> <nome> per mano di il putit in Vernis» — metà italiano, metà
inglese, e una preposizione che non si fonde.

## Il perimetro si allarga di tre file — 2026-08-10, diciottesima sessione

Sessione aperta per collaudare i nomi, chiusa con **464 firme in più** e un
difetto sistemico riparato.

**379 rinomine all'evoluzione, in tre file che non erano nel perimetro.** Il
dettaglio sta in `decisioni.md`. Qui conta il precedente di metodo: un file
entra nel dizionario **anche se non è nel piano**, quando il piano lo esclude
per una ragione che nel frattempo è caduta. `custom_enemyevolution.hsp` non era
in Fase 1 perché non contiene interfaccia né messaggi — contiene solo copie di
nomi di creatura. Ed era proprio quello il problema: erano copie **da tenere
allineate**, e nessuno le teneva.

Le 379 sono state risolte automaticamente cercando il **giapponese** nel
dizionario esistente: zero ambigue, zero mancanti su 379. Vale la pena tenerlo
come tecnica: quando un file duplica valori di un altro file già tradotto, la
traduzione non si scrive, si **risolve**, e la chiave è il campo che i due
condividono per costruzione — qui il giapponese, non l'inglese.

**320 stringhe di voce** (`db_creature.hsp`, classe `voce`): chiuse tutte.

**59 rinviate del quiz**: chiuse. `rinviate.jsonl` scende da 79 a **20**, e le
20 che restano aspettano tutte `proc.hsp`.

**26 dinamiche di `action.hsp`** su 318. Poche perché la strada era bloccata da
una guardia che rendeva certe voci intraducibili; sbloccarla ha richiesto di
correggere `strumenti/funzioni.py` e due test. Il modello per le restanti 292 è
ora fissato:

- terza persona, mai `_s()`, `is()`, `was()`, `your()`, `have()`, `does()`:
  non passano da `lang()` e resterebbero inglesi;
- mai una preposizione davanti a `name()` o `itemname()`, che portano già
  l'articolo (`guida-stile.md:212`) — il controllo va rifatto a ogni lotto;
- `name(giocatore)` è «il viandante», quindi la terza persona regge per tutti.

### Il debito che questa sessione lascia

- **292 dinamiche + 597 statiche** in `action.hsp`.
- `chara_func.hsp` **non è nel perimetro** ma il quiz ne ha già fissato quattro
  nomi (`glossario.md`): finché non entra, il giocatore riceve le pietre di
  Lesimas in inglese e le ritrova in italiano nel quiz.
- Le rinomine riparate **non sono state viste in gioco**: la lettura del
  sorgente dice che ora combaciano, ma è una deduzione.

## Cinquantasei lotti, e i nomi finiti — 2026-08-10, diciassettesima sessione

I 455 nomi rimasti sono stati chiusi tutti, a lotti per razza, in dieci commit.
Il metodo era quello della sedicesima sessione e non è cambiato: `--razza` per
il taglio, la carta di `db_card.hsp` per i nomi opachi e per il sesso, il
blocco della creatura per ciò che il sistema dichiara, e le quattro verifiche a
ogni giro.

### Il test dell'articolo ha avuto ragione due volte

La prima sui quattro nomi del ciclo di Cthulhu (`クトゥグア`, `ツァトゥグァ`,
`ナイアーラトテップ`, `シュブ＝ニグラス`), scritti nudi come gli dèi. Ma gli
dèi stanno fra `<>` e questi no, e `name()` riconosce i nomi propri **dalla
prima lettera** (`init.hsp:1713-1716`): per il motore sono specie, e l'inglese
infatti scrive `the cthugha`. Vanno con l'articolo. Regola in `guida-stile.md`.

### `ドレイク` è un gradino sotto `ドラゴン`, e questo chiude il preteso refuso

La razza è **亜竜**, sub-drago, e le carte lo ripetono per tutti. L'italiano ha
la parola: **«draco»**, il nome del *Draco volans*. Da qui viene che
`action.hsp:17390` non era un errore di battitura: `Electric Drake` (電気竜) è
«il draco elettrico», e renderlo «drago» lo farebbe **collidere** con
エレキドラゴン, che quel nome ce l'ha già. La voce esce dalle cose in sospeso.

### Un nome già preso non si può riusare, ed è successo tre volte

| nome | prima scelta | perché no | resa |
|---|---|---|---|
| `メイド` | «la cameriera» | è già di `メイドさん` | «la domestica» |
| `沙羅曼蛇` | «la salamandra» | è già di `メガサラマンダー` | «la salamandra d'oriente» |
| `ローパー` | «la melma tentacolare» | è già di `スライムローパー` | «il tentacolare» |

⚠️ E una collisione la crea **l'inglese**, non noi: `<Orphe> the chaos child`
è il 混沌の**寵児**, ma `<The Chaos Child>` è già il 混沌の**超児** del lotto
`god`, «<Il Figlio del Caos>». Un carattere li separa in giapponese —
寵 «prediletto» contro 超 «oltre» — e si segue quello.

### Due giochi di parole che solo la carta rivela

- `先生きのこ` sembra «fungo insegnante»; la carta finisce con
  「この先生きのこれないだろう」, cioè 「この先 生きのこれる」 «sopravvivere»
  letto come 「この先生 きのこれる」. Il nome **è** la battuta →
  **«il professore champignon»**;
- `闘駐火草` si legge *tochukaso* ed è **冬虫夏草**, il cordiceps, scritto con
  ateji. Vale la regola degli omofoni: si traduce la base → **«il cordiceps»**.
- `邪拳王` la carta lo dichiara origine di じゃんけん, e in italiano il gioco ha
  il suo nome → **«il re della morra»**.

### Tre carte inglesi sono sbagliate nel sorgente

`マンドレザッパー` (`db_card.hsp:4131`) ha la prosa di `胡瓜の怪物`, `世界樹`
(`9643`) quella di `ヘブンズビートル`, e `ガイドの『ノルン』` (`7017`) quella
di `メルガスト`. Il **giapponese è sempre corretto** ed è da lì che si è
tradotto. Non toccate: sono upstream.

### Il registro dei nomi che l'inglese sbaglia si è allungato

| giapponese | inglese | cosa dice davvero |
|---|---|---|
| 機甲将軍 | `iron colonel` | è un **generale**, e la carta lo ripete |
| 生化学者 | `biologist` | **biochimico**, la carta dice 生化学専門 |
| 剣客 | `the cosmic sword` | uno **spadaccino**: perde la persona |
| ネザーマッドゴーレム | `mad mud golem` | è **mud**, 地獄の泥から作られた |
| マルチプルゴーレム | `ultimate golem` | è **multiplo**, 多数の素材を複合 |
| ファラオの呪い | `cursed coffin` | la **maledizione del faraone** |
| デビルコボルト | `dark kobold` | **diabolico** |
| 暗黒宇宙蟹 | `dark dome` | un granchio spaziale nato in un buco nero |
| 自走雷撃砲 | `electric tank` | un **semovente**, e a fulmini |

## Otto lotti, e un arbitro nuovo — 2026-08-10, sedicesima sessione

**122 nomi**, da 577 a 455: `karune` 18, `ghost` 17, `roran` 17, `worm` 15,
`dragon` 15, `cat` 14, `metal` 14, `largeanimal` 13. La macchina del taglio per
razza non è cambiata; è cambiato **dove si va a chiedere**.

### `db_card.hsp` descrive in prosa ogni creatura, e decide i nomi opachi

Ogni creatura ha una carta del gioco di carte con `cardrefskill`, due o tre
frasi che dicono **cos'è**. Dal blocco della creatura non si ricavano: il blocco
dà razza, classe, sesso, azioni. La carta dà l'intenzione.

```powershell
# la descrizione sta poche righe sopra il cardrefn che porta il nome
python -c "..."   # vedi strumenti/, oppure cerca cardrefn e risali a cardrefskill
```

Cosa ha sciolto, che altrimenti sarebbe rimasto opaco o sbagliato:

| nome | senza la carta | con la carta |
|---|---|---|
| `シュイド` | katakana senza significato, l'inglese dice `shadow` | «più `シェイド` fusi insieme, e per questo chiamato così» → un collettivo coniato sul nome base → **«l'ombrame»** |
| `アークレイス` | `アーク` = arch, e poi? | «gli individui più forti si distinguono come rango sovrano e prendono il prefisso `アーク`» — la **regola**, non il caso → «l'arcispettro» |
| `ヴォルガーファントム` | l'inglese si arrende a `vol phantom` | fulmini, energia accumulata, scoppio → `ヴォル` è **volt** → «il fantasma voltaico» |
| `黒お嬢様` | l'inglese dice `white young lady` | «i vestiti sono bianchi ma la sua sostanza è nera senza fine» → «la signorina dal cuore nero» |
| `『Ｈな妹』` | uguale a `えっちな妹`, e l'inglese le rende entrambe `H sister` | «**ヒットマン**な妹», con la motosega → «la sorella minore **sicaria**» |
| `シン・ゴリラ` | l'inglese legge `sin` | generatore nucleare in corpo, sigillato, distrugge per sfogare energia: è `シン・ゴジラ` → «lo Shin Gorilla» |
| `バレットワーム` | l'inglese dice `rock worm` | ingoia minerali, fabbrica pallottole e le sputa → «il verme proiettile» |

⚠️ **La carta non sostituisce il blocco: risponde a un'altra domanda.** Il
blocco dice cosa la creatura *è nel sistema* (razza, sesso, classe, azioni), la
carta cosa *rappresenta*. Su `病兄` servono tutti e due: `CDATA_SEX = 0` dal
blocco, e dalla carta il fatto che i maschi di Roran siano malati sul serio —
che è la ragione per cui **non** segue `病妹` → «la sorella yandere».

### La guardia dell'articolo ha fermato un nome, e aveva ragione

`シルバースカル陛下` era diventato «sua maestà il teschio d'argento», e
`test_ogni_nome_e_ogni_stringa_di_evoluzione_porta_il_proprio_articolo` l'ha
bocciato: non comincia con un articolo. Non è formalismo — la rinomina
all'evoluzione sostituisce la stringa intera e `name()` non antepone più nulla,
quindi il nome sarebbe uscito nudo. Corretto in «la maestà del teschio
d'argento». **È lo stesso meccanismo che il collaudo di questa sessione ha visto
funzionare dal lato buono.**

### Un refuso nel già tradotto, lasciato lì apposta

`action.hsp:17390`, `電気竜` → «il **draco** elettrico»: unica occorrenza di
«draco» contro decine di «drago». Non è una distinzione voluta, è una lettera.
Non corretto perché sta fuori dai lotti e una voce chiusa che si ritocca va
vista in un commit suo.

## Dodici lotti per razza — 2026-08-10, quindicesima sessione

**351 nomi in un giorno**, da 928 a 577. Il nucleo atomico si era preso da sé;
tutto il resto si taglia per **razza**, che è un campo che il sorgente dichiara
— `dbidn`, subito prima di `gosub *db_race` — e non una proprietà che qualcuno
legge nel nome. È la terza volta che il criterio giusto è un campo del sorgente
invece di un giudizio: `reftype` per `db_item.hsp`, l'array che dichiara la voce
per `item_data.hsp`, `dbidn` qui.

```powershell
python -m strumenti.creature --razze              # quanto resta, razza per razza
python -m strumenti.creature --razza dog --uscita lavoro/fase2-dog-001.jsonl
```

⚠️ `--classe nome` da solo emette tutti i 1.131, nucleo compreso: `--razza`
toglie da sé le firme già in dizionario, o ogni lotto sovrascriverebbe il
precedente. La rete del criterio è `firme_senza_razza()`, oggi vuota: se un
domani non lo fosse, «un lotto è una razza» coprirebbe novecento nomi meno uno
**senza dirlo**.

| lotto | nomi | cosa ha insegnato |
|---|---|---|
| `dog` | 27 | i dieci segugi elementali li dichiara `FILTER_RACE_HOUND_<X>` |
| `norland` | 90 | il sesso è dichiarato solo su 52 su 90 → il criterio dell'articolo |
| `god` | 36 | l'inglese tiene il nome proprio e lascia cadere l'epiteto |
| `juere` | 33 | `rogue` copre due giapponesi diversi |
| `zanan` | 25 | la razza sta in `dbidn`, non nel nome |
| `bird` | 24 | due uccelli sbagliati e uno abbandonato dall'inglese |
| `spirit` | 21 | la stessa prova non dà la stessa conclusione |
| `rat` | 21 | una famiglia di giochi di parole che l'inglese aveva spezzato |
| `elea` | 19 | i nomi della trama, già vincolati dal quiz |
| `seamonster` | 19 | una razza fatta di fusioni |
| `machine` | 18 | l'inglese incoerente dove il giapponese non lo è |
| `imp` | 18 | sei fusioni da rifare, non da leggere |

### L'articolo di un nome di persona

Il problema che il nucleo non poneva e che vale per tutti i 577 che restano: un
nome di mestiere descrive una **persona**, e in italiano l'articolo di
«negoziante» dipende da chi lo porta. Il sorgente dichiara `cdata(CDATA_SEX,
rc)` **solo per una parte** — 52 su 90 in `norland`. Il criterio completo sta in
`guida-stile.md`; qui basta la conseguenza pratica, scoperta col lotto `imp`:

⚠️ **l'articolo sta sulla testa del sintagma, non sulla persona.** I cinque
demoni di `imp` hanno sessi diversi e la stessa forma italiana — «il demone di
X» — perché il genere lo dà «demone». `CDATA_SEX` conta solo quando la testa
**è** la persona (`<Neres> la smemorata`). I casi difficili sono meno di quanti
sembrassero.

### Due deroghe alla regola dell'articolo, e nessuna di più

`SENZA_ARTICOLO` in `test_creature.py` ha due voci, e un test pretende che
restino esattamente quelle: `＠`, che è il simbolo del giocatore fatto creatura
e parla «Qy@», e `user`, che non è un nome ma lo **slot** dei PNG definiti dal
giocatore. Il secondo lo firma il sorgente: `lang("user", "user")`, col
giapponese identico all'inglese in un file dove ogni nome vero ha la sua forma
giapponese.

### Un aggancio riparato all'indietro

`text.hsp` chiedeva «Come si chiama l'**investigatore** della Gilda dei Maghi?»,
ma la risposta è `<Lenas>` e `db_creature.hsp` le dà `SEX=1`. Il maschile era
un'ipotesi presa quando i nomi di creatura non c'erano ancora: ora ci sono e
dicono il contrario. **Le domande del quiz sono già a schermo, i nomi no** —
quindi sono i nomi a doversi adeguare, tranne dove è la domanda a essere
sbagliata.

## Il nucleo atomico è dentro — 2026-08-09, quattordicesima sessione

**Il primo lotto della Fase 2**, e il primo che entra in **due dizionari
insieme**: 203 nomi di `db_creature.hsp` più 373 stringhe di evoluzione di
`action.hsp`, 576 voci per 380 firme e 372 rese distinte. 378 stringhe
inglesi, e le firme sono 380 perché due inglesi ne coprono due creature.

Si rifà in un comando:

```powershell
python -m strumenti.creature --nucleo --uscita lavoro/fase2-nucleo-001.jsonl
```

**Le firme sono 380 e le rese 372** perché otto giapponesi compaiono con due
inglesi diversi. Non è rumore: è il motivo per cui il giapponese arbitra (vedi
`decisioni.md`, quattordicesima sessione).

`<Pants of Ogre>` → «`<Mutande dell'Ogre>`» chiude `db_item.hsp` a **1.606 su
1.606**. Rinviate da 80 a **79**: restano le 59 risposte del quiz, che aspettano
gli altri ~930 nomi, e le 20 `elename()` che aspettano `proc.hsp`.

⚠️ **Cinque delle 59 sono già sbloccate nel merito** — `steel golem`, `spider`,
`scorpion`, `black widow`, `paralyzer` sono nel nucleo — ma restano rinviate
perché il motivo dice «insieme a quelli», e «quelli» sono 203 su 1.131. Si
sciolgono col resto.

## `skill.hsp` è chiuso — 2026-08-09, tredicesima sessione

**Quarto file completo**, 885 su 885, e il più grosso dei quattro dopo
`db_item.hsp`. L'ultimo blocco erano le **276 mosse speciali**, tetto 24
caratteri già misurato il giorno prima.

Quindici nomi restano inglesi per scelta, dichiarati in `invariati.md`.
⚠️ **La regola della marca 《》 degli artefatti non si applica alle mosse**: il
nome di un artefatto è un nome proprio, quello di una mossa è un'etichetta
funzionale che si sceglie da un elenco. Vedi `decisioni.md`.

## Le rinviate scendono da 120 a 80 — 2026-08-09, tredicesima sessione

Tre dei cinque motivi erano scaduti o falsi.

| gruppo | voci | esito |
|---|---|---|
| risposte del quiz sui grimori | 4 | il rinvio era a `skill.hsp`, che oggi è chiuso |
| parti meccaniche `Change …` | 6 | ⚠️ **la dipendenza dichiarata non esisteva**: in `db_item.hsp` non ce n'è nessuna |
| nomi casuali degli oggetti | 30 | risolti con 213 toppe generate, vedi sotto |
| risposte del quiz su creature | 59 | rinvio **vivo**: aspettano i nomi di creatura |
| `elename()` | 20 | rinvio **vivo**: aspettano `proc.hsp` |
| `<Pants of Ogre>` | 1 | rinvio **vivo**: aspetta `orc`/`ogre` |

I nomi casuali hanno chiesto il primo ribaltamento d'ordine del progetto:
`db_item.hsp` compone «aggettivo + nome» in **213 siti**, e in italiano
l'aggettivo segue il nome. L'ordine sta nel codice, non nelle stringhe, quindi
il dizionario non lo raggiunge: le toppe le genera
`strumenti/genera_toppe_casuali.py`, una per sito, ognuna con l'aggancio unico
del proprio `ITEM_ID`.

⚠️ **Il genere è una proprietà dell'array, non della riga**, come l'articolo dei
pesci: le rese si accordano una volta per famiglia. Le sei firme condivise fra
due famiglie prendono la **forma invariabile** — quattro sono materiali e lo
sono già, due l'hanno presa apposta.

## `item_data.hsp` è chiuso — 2026-08-09, undicesima sessione

**Secondo file completo**, e a differenza del primo senza nemmeno un rinvio:
318 su 318.

I 235 rimasti a inizio sessione non erano un mucchio. La classe qui non è
`reftype` come in `db_item.hsp` ma **l'array che dichiara la voce**, e con
quella chiave si sciolgono in cinque discipline diverse, chiuse in tre lotti:

| lotto | criterio | voci |
|---|---|---|
| ego | `egoname` + `egominorn` | 29 |
| pesci | `fishdatan` | 113 (10 invariati) |
| incantamenti | `encDisp`, le dinamiche di `*item_encdetail`, `ammoname` | 93 (2 invariati) |

Le tre cose che il file ha insegnato, in ordine di prezzo:

1. **Il posto decide se i dati arrivano in tempo.**
   `ioriginalnameref(ITEM_ID_FISH)` è la stringa vuota: il nome della specie è
   *tutto* il nome e arriva da `itemNameSub`, che gira **dopo** l'articolo.
   Tradurre i 113 nomi e basta avrebbe dato «a salmone», e nessun test lo
   avrebbe visto.
2. **L'ego va dopo il materiale**, il che vuole una coda propria (`s10`)
   riversata fra materiale e stato.
3. **Il soggetto sta fuori dai file estratti.** `lang("それは", "It ")` è in
   `command.hsp`, e `s` compare in quattro siti di cui tre senza soggetto: le
   rese sono verbi alla terza persona senza soggetto, e il prefisso si spegne
   con una toppa.

## `db_item.hsp` è chiuso — 2026-08-09, decima sessione

**Primo file completo del progetto**: 1.605 firme su 1.606. L'unica mancante è
`<Pants of Ogre>`, che è **rinviata** e non dimenticata (vedi più sotto).

Il file è passato da 599 nomi da guardare a zero in una sessione, con sei lotti.
Il criterio non è stato la forma del nome, che era il candidato scritto qui
ieri, ma **la categoria che il sorgente dichiara**.

I lotti dal terzo al sesto erano stati scelti per `filter_item`. Quando quel
criterio si è esaurito, ciò che restava si chiamava «il gruppo senza filtro»: un
residuo da affrontare a occhio. Non era un residuo. La categoria c'è, solo che
sta **dentro il blocco di ogni oggetto** — `reftype = FILTER_ITEM_...` — e
classifica **1.320 oggetti**.

Lo strumento è `strumenti/categorie.py`, con cinque test:

```powershell
python -m strumenti.categorie                                 # il resto, per categoria
python -m strumenti.categorie --categoria FILTER_ITEM_TOOL --uscita lavoro/x.jsonl
```

⚠️ **Vale anche per gli altri file.** `item_data.hsp` e i cinque mai guardati
non sono stati letti con questa chiave: prima di dichiararli senza struttura,
si cerca dove il codice li struttura.

| lotto | criterio | voci |
|---|---|---|
| artefatti fra `<>` | forma del nome più la marca 《》 | 169 (105 invariati, 63 tradotti, 1 rinviato) |
| arredamento da `map_fur_*` | array del generatore di mappe | 46 |
| cibo | `FILTER_ITEM_FOOD` | 51 |
| arredamento | `FILTER_FURNITURE` | 100 |
| attrezzi | `FILTER_ITEM_TOOL` | 107 |
| scarto | `FILTER_JUNK` | 59 |
| code corte | nove categorie insieme | 67 |

**Sui 169 artefatti la domanda era di invarianza, non di resa**, e la regola sta
in `decisioni.md`: l'inglese romanizzato o siglato resta; il giapponese fra
《》 e traslitterato resta; il giapponese descrittivo si traduce. La prova che
non è stata cucita addosso al lotto è che riproduce tutti e otto i precedenti
già presi.

`item_data.hsp` è entrato il 2026-08-08, e non era nel piano: ci sono i **45
materiali** (`mtname`), che il primo collaudo ha mostrato anteposti al nome in
ordine inglese — «bronze corazza». Le 83 voci fatte sono i 38 materiali, i 38
epiteti e le 7 piante dei semi; le altre 235 sono altri dati degli oggetti,
ancora da guardare.

L'ordine è quello del piano, per visibilità decrescente: quello che si vede di
più si traduce prima, così ogni lotto ha valore anche se il progetto si ferma lì.

`db_item.hsp` è entrato in coda il 2026-08-07, quando `siti()` ha imparato il
**secondo tipo di sito** (`contratto-nomi.md` §2). La percentuale totale è scesa
dal 10% all'8% senza che nessuno abbia disfatto niente: il denominatore era
incompleto, e i nomi degli oggetti erano lavoro che il conteggio non vedeva.
Una metrica che scende perché ha smesso di mentire è una metrica migliore.

I 1.607 siti sono 1.321 blocchi canonici meno 12 nomi inglesi vuoti, più i 298
`ioriginalnameref2` non vuoti — i nomi che si compongono (`deed of camp`). Le
firme sono **1.606**, una sola in meno dei siti: una coppia giapponese-inglese
ripetuta.

⚠️ **Corretto il 2026-08-08: qui c'era scritto 1.591, e la differenza erano
esattamente le 15 firme che `estrai --da-tradurre` non offriva.** Il numero era
stato preso dall'uscita dell'estrazione invece che dalla scansione, e portava
dentro il suo difetto: `rinviate.jsonl` è indicizzato per firma, e 15 voci
rinviate su `text.hsp` (risposte del quiz, nomi casuali) hanno lo stesso
contenuto di 15 nomi di oggetto. Quei nomi sparivano da ogni lotto, e la
metrica li aveva già dimenticati.

**La regola che ne resta: il denominatore si misura sul sorgente, mai
sull'uscita di uno strumento.** Uno strumento che filtra fa passare il suo
filtro dentro il numero, e una metrica costruita così non può segnalare il
difetto che la produce. Le due misure vanno tenute separate e confrontate: se
`verifica --dizionario` e `estrai --da-tradurre` non tornano, è un difetto, non
un arrotondamento.

## Prima di cominciare un file nuovo

La ricerca delle stringhe che sono dati. Quella scritta nel piano
(`grep -nE '(=|==|!=|instr\().*lang\('`) è **troppo larga**: su `text.hsp`
restituisce 1.187 righe, quasi tutte array di etichette. Le due che servono:

```powershell
# confronti veri e scritture nei campi del salvataggio
grep -nE '(==|!=|instr\()[^=]*lang\(|cdatan?\([^)]*\) *= *.*lang\(' <file>.hsp
```

E soprattutto la misura **per firma**, che è quella che conta, perché una firma
condivisa fra un sito-dato e un sito-display non si può separare traducendo:
vedi `invariati.md`, sezione «valori di dato», e le sei toppe di `text.hsp`.

Su `text.hsp`: 7 firme su 1.740 toccavano un sito-dato. Trovarle prima è costato
mezz'ora; trovarle dopo sarebbe costato un salvataggio rotto.

## Rinviato alla Fase 2

Voci estratte, **non** tradotte, e non dimenticate: `verifica.py` continua a
segnalarle. Non sono un debito di traduzione ma una dipendenza da una decisione
che questa fase non prende.

L'elenco vero è `rinviate.jsonl`, che `estrai --da-tradurre` legge: senza di
esso queste voci tornerebbero in testa a ogni estrazione e andrebbero riscartate
a mano. Il `motivo` è obbligatorio, come per le toppe.

| gruppo | voci | perché |
|---|---|---|
| nomi casuali degli oggetti (`text.hsp:176-192`) | 30 | `_namepotion`+`strpotion` costruiscono «clear potion». In italiano cambia **l'ordine** («pozione trasparente») oltre al genere, e gli aggettivi sono condivisi fra sei classi di sostantivo con generi diversi: «pozione chiara» ma «anello chiaro» |
| `elename()` (`text.hsp:203-271`) | 20 | → **con `proc.hsp`, in questa fase.** Aggettivo elementale che modifica la parte del corpo di `_melee(2,…)`: `proc.hsp:8797` compone `elename(ele) + " " + _melee(2,…)`. In italiano l'aggettivo segue il nome e ne prende il genere, e i nomi sono di generi misti (mano, artiglio, zanna, occhio). L'ordine si sistema traducendo `proc.hsp`, che è una dinamica e permette di riordinare la concatenazione |
| nomi di magia nel quiz (`text.hsp:978-987`) | 4 | → **con `skill.hsp`, in questa fase** |
| nomi di creatura e oggetto nel quiz | 59 | risposte del quiz che nominano creature e oggetti. Il nome vero sta in `db_creature.hsp`/`db_item.hsp`: tradurlo qui prima farebbe divergere la risposta dal nome che il giocatore legge |
| parti meccaniche (`text.hsp:1387-1402`) | 6 | verificato che compaiono anche in `db_item.hsp` |
| `<Pants of Ogre>` (`db_item.hsp`) | 1 | il nome contiene `ogre`, e in `db_creature.hsp` `orc` e `ogre` convivono come creature distinte (`orc warrior`, `black orc` contro `slash ogre`, `shine ogre`): «orco» non può coprirle entrambe. **Primo rinvio deciso da `db_item.hsp`**, e per questo `test_i_nomi_di_db_item_non_sono_rinviati_da_text` ha smesso di asserire `== set()` — era una procura — e adesso pretende la proprietà vera: ogni firma che esce per `db_item.hsp` viene da una riga **di** `db_item.hsp` |
| **totale** | **120** | |

## Le 35 uscite della nona sessione (2026-08-08)

Sono uscite dal rinvio `_furniture` (11), `_bookself` (7), `_bookselfs` (7) e
`_weight` (10). Il motivo del rinvio era corretto quando fu scritto — «aggettivi
prefissi a un nome di genere ignoto, che vive in `db_item.hsp`» — ed è caduto
quando i nomi sono entrati nella catena.

⚠️ **Ma il rinvio le trattava come un gruppo solo, e non lo erano.** Quattro
array che il documento dava per «la stessa identica forma» hanno chiesto
**quattro cure diverse**, e scoprirlo è stato il lavoro vero della sessione:

| array | dove esce in inglese | cura |
|---|---|---|
| `_furniture` | prefisso al nome | toppa: sposta in `locvar_itemname_s6`, rese a complemento invariante |
| `_bookself` | **già fra parentesi** (`item_func.hsp:988`) | **nessuna toppa**: solo dato. L'unico della famiglia in cui il sorgente andava bene |
| `_weight` | già suffisso, ma con giunto « grown » | toppa **sul giunto**: « di taglia » introduce una testa femminile fissa, e l'accordo smette di dipendere dall'oggetto |
| `_bookselfs` | slot della parola-contatore (`item_func.hsp:1233`) | trattamento di `contatori.jsonl`: singolare, plurale, genere, e un `case` in **entrambi** gli switch |

**La lezione, che vale oltre questi quattro: «stessa forma» è un'ipotesi, non un
fatto, e va verificata guardando il sito di concatenazione prima di scrivere la
toppa.** Il documento di ripresa li dava per identici in buona fede, sulla base
del fatto che sono tutti aggettivi prefissi in `text.hsp`. Lo sono nel
dizionario; non lo sono nel codice, ed è il codice che decide la cura.

⚠️ **Un legame fragile creato qui, da ricordare.** Fra `contatori.jsonl` e il
dizionario il legame è **per stringa**: il `case` dello switch confronta la resa
del primo con quella che l'array porta a runtime, che viene dal secondo. Se
divergono il `case` non aggancia mai — e restano verdi sia il compilatore sia la
prova d'identità. Ora lo pretendono `genera_toppe_nomi.py` (alla generazione) e
un test (a ogni giro).

**Coperte anche le altre 39, il 2026-08-09.** `contatori.jsonl` ha tre fonti:
`text` (le sette del libro prodotto) e `item_func` (le sei cablate) alimentano
il generatore ed erano già difese; le **39 con `fonte: "db_item"`** sono il
registro di ciò che il dizionario dice per lo slot `ioriginalnameref2`, e su di
esse non guardava nessuno.

Il confronto giusto **non è l'uguaglianza**, e a insegnarlo è `grave`: il
registro dice «tomba», il dizionario «tomba ornata», e ha ragione il dizionario,
perché il nome si monta `s2 + " " + s3 + " " + s1` col giunto fissato a «di» e
l'aggettivo deve stare in `s2` per accordarsi con la testa. A schermo esce
«tomba ornata di fiori». Il registro dice il **termine**, il dizionario il
**segmento**: due livelli, non due verità. Il test pretende quindi che la resa
del dizionario **cominci con** il termine del registro.

**Tre uscite precedenti, sempre il 2026-08-08: `blessed`, `cursed`, `doomed`.** Erano rinviate
perché si antepongono al nome e in italiano un participio si accorderebbe con
un oggetto di genere ignoto. La premessa del rinvio — «i nomi di `db_item.hsp`
non li risolviamo in questa fase» — è caduta quando i nomi sono entrati nella
catena, e la forma è la stessa degli epiteti del materiale: **complemento**,
«con benedizione», che non chiede accordo a nessuno. Le tre stringhe si
spostano in coda con `locvar_itemname_s7` (`item_func.hsp:1204, 1207, 1210`,
solo il ramo inglese).

Il resto del loro motivo **non** è caduto: il sistema dei nomi casuali resta
rinviato, ed è un problema suo.

⚠️ **Il conto è cresciuto da 68 a 157 in un lotto solo**, ed è quasi tutto la
stessa dipendenza: i nomi di creature e oggetti della Fase 2. Vale la pena
guardarlo prima di tirare avanti — la Fase 1 sta accumulando debito verso una
decisione che non ha preso, esattamente come `init.hsp` accumulava debito
verso il registro finché non è stato promosso da Fase 4 a Fase 1.

Sono **aggettivi prefissi al nome di un oggetto**, e in italiano un aggettivo
prefisso vuole il genere del nome che segue. Quel nome vive in `db_item.hsp`,
e il piano della Fase 1 dice esplicitamente di non risolvere dove stanno i nomi
degli oggetti (SPEC §2, punto ancora aperto). Tradurli ora significherebbe
scegliere un genere al posto di quella decisione, in 35 punti, in silenzio.

È lo stesso nodo dell'articolo di `name()`, risolto nella quarta sessione
rimandando la scelta a chi conosce il nome. Qui si rimanda allo stesso posto.


## Fase 3 — i file dati di `data\` (dalla 70a)

L'unita' e' la **riga inglese** dentro un blocco `%…,EN`. Il conto vivo:

```powershell
python -m strumenti.dati_verifica lavoro/<file>-001.jsonl
```

| file | tradotte | righe EN | % | famiglia |
|---|---|---|---|---|
| `board.txt` | **25** | 25 | **100%** | senso |
| `talk.txt` | **569** | 569 | **100%** | senso |
| `exhelp.txt` | 0 | 185 | 0% | impaginazione |
| `manual_ENG.txt` | 0 | 591 | 0% | impaginazione |
| `book.txt` | 0 | 2.208 | 0% | impaginazione |
| **totale** | **594** | **3.578** | **17%** | |

⭐ **La famiglia del senso e' CHIUSA** (71a): `board.txt` e `talk.txt` sono
tutt'e due al 100%. Quel che resta e' la famiglia dell'impaginazione, dove la
riga e' un'unita' di **disegno** e vuole prima una misura della colonna presa
dalla geometria (regola della 55a).

⚠️ **La famiglia decide l'unita' di traduzione.** Dove la riga e' un'unita' di
**senso** il gioco ne pesca una a caso (`rnd`) e si traduce riga per riga; dove
e' un'unita' di **disegno** l'inglese e' spezzato a mano a larghezza fissa
(`book.txt`: 33 righe giapponesi contro 224 inglesi) e l'unita' e' il blocco.

⚠️ **E ogni file ha il suo espansore di segnaposto**: `board.txt` passa da
`*talktxt_conv` (33 nomi), `talk.txt` da `*convert_word` (46). Stanno in
`PROFILI`, dentro `strumenti/dati_verifica.py`.

`talk.txt` e' stato chiuso in **otto lotti** (71a), raggruppati per *chi
parla* e non per posizione nel file:

| lotto | che cosa | righe |
|---|---|---|
| 001 (70a) | `DEFAULT` e le quattro `PERSONALITY` | 64 |
| 002 | chi ti parla addosso: compagni, mestieri, figure | 58 |
| 003 | le citta' della Tyris del Nord | 61 |
| 004 | il rifugio e le citta' della Tyris del Sud | 58 |
| 005 | voci sul bottino, feste, dei, campo di battaglia | 56 |
| 006 | Irva Perduta e i suoi presidi | 62 |
| 007 | la nave divina e i biscotti della fortuna | 68 |
| 008 | le varianti d'aprile dei luoghi | 81 |
| 009 | le varianti d'aprile di chi parla | 61 |

⚠️⚠️ **Il conto pari delle righe NON prova l'allineamento fra le due lingue.**
Quattro blocchi lo hanno smentito in modi diversi, e nessuna rete lo vede:

| blocco | forma | che cosa succede |
|---|---|---|
| `MOYER` | 2 contro 2 | **scambiato**: EN|1 rende JP2, EN|2 rende JP1 |
| `AREA,12` | 8 contro 8 | **sfalsato**: da EN|4 in poi scala di uno, JP4 buttata, EN|8 inventata |
| `BSHIP7` | 17 contro 30 | EN|13 e EN|14 scambiate fra loro |
| `AAREA,12` | 5 contro 6 | sfalsato, JP1 buttata |

💡 Uno **sfalsamento** e' piu' insidioso di uno scambio: le prime righe
combaciano e sembrano confermare l'allineamento.

⚠️ **I blocchi con la `A` davanti sono le varianti di APRILE**, non un'altra
famiglia di parlanti: `text.hsp:9609` e seguenti li scelgono con
`gdata(GDATA_MONTH) == 4`. E due sono **morti**: `%ABITCH` e `%AKASHIC` non
sono referenziati da nessuna parte.
