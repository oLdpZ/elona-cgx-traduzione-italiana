# Ripresa sessione

Aggiornato: 2026-09-02, fine della **centoventisettesima** sessione (**il fronte
delle righe nude scende da 141 a 45: 78 toppe, quattro famiglie che erano
toppate a metà — e una l'avevo lasciata a metà io, tre ore prima — cinque toppe
che scrivevano i puntini con un carattere a due byte, e una frase che cominciava
in italiano e finiva in inglese**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 16:25 DEL 02/09**, ricompilato e
ricopiato a mano dopo l'ultima toppa. Se la data e' quella, non c'e' niente da
rifare. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

⭐⭐⭐ **IL PERIMETRO `lang()` RESTA CHIUSO AL 100%.** Il conto **non si eredita
da qui** — si rilancia:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/perimetro.py

        firme rese                              26.326
        firme ancora da fare, contate                0
        --- fatto 26.326 su 26.326            = 100,0%

---

## ⭐⭐⭐ IL FRONTE DELLE RIGHE NUDE E' QUASI CHIUSO: NE RESTANO 45, E 44 SONO DICHIARATE

Il conto si rilancia in due comandi, e **non si eredita da qui**. ⚠️ **Le due
sottrazioni non si sommano a mano: la seconda parte dalla prima**, e la seconda
guarda **anche la build**, non solo il sorgente.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-nudi-nel-ramo-jp.py

        testo, dal triage                            62
        dentro un `if ( jp )`, che la build en non esegue   3
        --- vive secondo questo referto              59

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-spente-da-una-costante.py

        dentro un `if ( FALSE )`, che non gira mai   14
        --- VIVE DAVVERO                             45

⚠️⚠️⚠️ **MA QUELLE 45 NON SONO 45 COSE DA FARE.** Delle 45, **quarantaquattro
sono dichiarate in `invariati.md`** — sigle di colonne misurate, falsi positivi
del triage, roba da modo mago, `helloworld.hsp` che non fa nemmeno parte della
build — e restano nel conto solo perche' `nudi_en` e `triage_nudi` contano i
letterali **intatti**, e una riga che deve restare intatta e' indistinguibile da
una che nessuno ha guardato. E' la ragione gia' scritta per `net.hsp:263` nella
125a, ora vera per quasi tutto il residuo.

💡 **Il fronte come lo si contava dalla 125a in poi e' finito.** Chi riapre
questo documento e vede «45» non ha davanti un lotto: ha davanti la voce qui
sotto, e poi altri fronti.

### ⭐⭐⭐ L'UNICA COSA APERTA E MISURATA: GLI AP DI `chara_func.hsp`

`chara_func.hsp:8430` e `:8522`, `name(…) + " obtained " + N + " AP from the " +
gain_ap_source + "."`. A schermo esce **«X obtained 3 AP from the kill of your
minion.»**, ed e' testo di combattimento.

⚠️ **`gain_ap_source` e' operando e testo insieme**, come `male`/`female`: il
codice lo confronta con `"talk"`, `"kill"` e `"destone"` in **sette** punti
(`:8415`, `:8436`, `:8455`, `:8509`, `:8524`, `:8530`, `:8543`) per decidere
cosa fare, e la stessa variabile finisce dentro la frase. Tradurre l'operando
rompe le sette condizioni **in silenzio**.

⚠️⚠️ **E non e' una parola: e' una frase che si compone per ricorsione.**
`:8533`-`:8560` richiamano `gain_ap` passandogli `gain_ap_source + " of yours"`,
`+ " of your mount"`, `+ " of your minion"`, `+ " of " + his(…) + " tag-team
partner"` — altri quattro frammenti inglesi nudi, e `his()` a un argomento e'
**morfologia inglese** che in italiano va tolta.

✅ **La strada e' scritta e non e' stata percorsa**: separare l'operando dalla
resa con una tabella al **sito di stampa**, tre basi per cinque code. E' una
toppa a blocco di una certa dimensione e vuole una sessione sua. Il dettaglio
sta in `invariati.md`, sezione «Un fronte misurato e NON chiuso».

---

## ⚠️⚠️⚠️ QUATTRO FAMIGLIE ERANO TOPPATE A META', E UNA L'AVEVO LASCIATA IO

E' il difetto della giornata, ed e' uscito **quattro volte**, sempre nello
stesso modo: cercando *se questa stringa e' gia' resa altrove* prima di
decidere. Nessun referto lo vede, perche' non c'e' niente di malformato da
nessuna parte — c'e' solo una meta' fatta e una meta' no.

    la scala del potenziale     i sette gradini della scheda del personaggio
                                (command.hsp:10677-10700) erano italiani da
                                sessioni; i cinque minuscoli di *dump_chara no
    le suppliche di chi muore   il giapponese di ai.hsp:805/813/821 e' IDENTICO
                                parola per parola a proc.hsp:20596/20677/20756,
                                rese nella 126a. Si copiano, non si riscrivono
    l'evasione fiscale          event.hsp:4560 e' la gemella esatta di
                                command.hsp:15556 — ⚠️ TOPPATA DA ME LA MATTINA
                                DI QUESTA STESSA SESSIONE
    la spiegazione del          chat.hsp:14246 diceva «Supreme e' il massimo,
    potenziale                  Hopeless e' il minimo», cioe' mandava il
                                giocatore a cercare due parole che le toppe
                                avevano gia' tolto dallo schermo

⭐⭐⭐ **La terza e' quella che insegna qualcosa di nuovo.** Le prime due sono
debiti di sessioni vecchie; la terza l'ho creata io tre ore prima, dentro questa
sessione, con tutto il contesto in testa. Quindi **non e' un problema di
memoria: e' la forma di lavoro.** La cura e' una riga sola: prima di chiudere
una toppa si cerca la stringa **in tutto il sorgente**, non solo nel file che si
sta guardando.

    grep -n 'LA STRINGA' *.hsp     nella cartella del sorgente pinnato

💡 E la quarta dice l'altra meta': **una resa di dizionario puo' scadere per
colpa di una toppa**. Le etichette del potenziale sono toppe, la spiegazione che
le nomina e' dizionario, e **nessun referto mette a confronto i due mondi**. E'
la scoperta della 126a («le toppe erano l'unico italiano che nessuna rete avesse
mai letto») vista dal lato opposto: non l'italiano delle toppe che nessuno
legge, ma l'italiano del dizionario che una toppa ha reso falso.

---

## ⚠️⚠️ CINQUE TOPPE SCRIVEVANO I PUNTINI CON UN CARATTERE A DUE BYTE

Cinque toppe della 126a — le battute delle mosse speciali di `proc.hsp` —
portavano nell'italiano `…` (U+2026).

CP932 quel carattere **ce l'ha**: e' 0x81 0x63. Quindi
`test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere` restava verde, perche'
chiede che il carattere sia **scrivibile**, non che sia **leggibile**. Ma e' a
doppia larghezza, e il ramo che la build italiana esegue disegna col carattere
latino dichiarato in `config.txt` (`font2. "Courier New"`): i due byte diventano
due glifi latini a caso, per la stessa ragione che `invariati.md` scrive da
sempre per 《 》 e 【 】.

⚠️ **E il progetto lo sapeva.** `…` sta in cima all'elenco `PROIBITI` di
`scratchpad/guardie.py` dalla 33a — ma `guardie.py` legge i JSONL di **lotto**,
cioe' il dizionario, e una toppa una firma non ce l'ha.

✅ La rete nuova e'
`strumenti/tests/test_toppe.py::test_nessuna_toppa_scrive_in_italiano_un_carattere_a_doppia_larghezza`,
e ha due cose che vale la pena copiare:

⭐⭐ **Guarda i BYTE, non un elenco.** La prima stesura chiedeva se il carattere
stesse in `…“”～«»`; la versione buona chiede **quanti byte CP932 spende per
scriverlo**. Un elenco chiuso avrebbe lasciato passare `—`, `–`, `’`, `※`, che
sono a due byte esattamente come `…` e vengono a mano scrivendo in italiano — e
uno stavo per scriverlo davvero, mezz'ora dopo, traducendo Mikraanesis.
ⓘ `♪` resta l'unica deroga, ed e' vecchia.

⭐⭐ **E' stata ESERCITATA, non solo scritta.** Rimettendo il `toppe.jsonl` di
ieri la prova e' **rossa** e nomina la riga; con quello di oggi e' verde. Piu'
una seconda prova che la mette alla prova su righe inventate nei due versi:
l'italiano col `…` accusa, il ramo giapponese con lo stesso `…` no.

⚠️ **Si giudica riga per riga, e le righe col giapponese si saltano**: una toppa
a blocco si porta dentro il ramo `if ( jp )`, dove 「疲れた…」 e' scritta giusta.

---

## ⚠️⚠️ UNA FRASE COMINCIAVA IN ITALIANO E FINIVA IN INGLESE

`chat.hsp:17065` non era una riga nuda qualunque: era la **sesta e ultima** di
una frase spezzata su sei `mes`, e le prime cinque passano da `lang()` ed erano
italiane da sessioni. A schermo si leggeva:

    …Uscire senza salva ed esci option from the ESC menu will result in a
    penalty at load time.

⚠️ **Nessun conteggio poteva distinguerla**: per `nudi_en` era un letterale
intatto come gli altri. A vederla serve **leggere il blocco**, non l'elenco.

💡 Il caso ha un nome nel progetto — `code-virgolette.py`, «la frase spezzata fra
`if ( en )` e `lang()`» — ma nessuno strumento la cerca al contrario: *una
`lang()` gia' resa la cui coda e' nuda*. Sarebbe un referto da scrivere.

---

## LE 78 TOPPE DELLA 127a, IN NOVE LOTTI

    command.hsp    29   le scene del cioccolato, i menu, la scala del potenziale
    config.hsp      7   i sei ritardi del menu opzioni, e la scelta della lingua
    chara.hsp      14   «Gene from » in tredici schermate, e il lucchetto
    system.hsp      6   gli errori dei file dei PNG e degli oggetti
    main.hsp        6   il tempo, la lapide, il boss, i saluti al rientro
    help.hsp        4   la guida, la chat di rete, le scene
    economy.hsp     4   l'allineamento della citta' e il prezzo di un edificio
    text.hsp        6   i segnaposto {onii} e {syujin}
    ai.hsp          3   le suppliche di chi sta per morire
    chat.hsp        4   il racconto di Mikraanesis, e la frase mozzata
    altri           ~   blend, calculation, chara_func, event, module

### ⭐⭐⭐ L'INGLESE AVEVA APPIATTITO TRE SCENE SU UNA SOLA

`command.hsp:15042`, `:15053`, `:15064` sono i tre gradini di
`CDATA_IMPRESSION` con cui un PNG reagisce al regalo di cioccolato. In inglese
sono **la stessa riga copiata tre volte**, `txt cnvtalk("I love you."),
cnvtalk("Thank you.")`; nel ramo giapponese sono tre scene diverse e piu' lunghe
— chi guarda te, poi il cioccolato, poi di nuovo te; chi fa di tutto per
nascondere il sorriso; chi resta senza parole.

E' il difetto della 126a — l'inglese della provocazione che era l'inglese
dell'insulto — **nella forma opposta**: non copiato da un'altra scena, ma
appiattito su se' stesso. La resa segue il giapponese, che e' l'originale.

### ⚠️⚠️ «MASTER» DICEVA PADRONE ANCHE A UNA GIOCATRICE

`text.hsp:7051` e `:12081`, il segnaposto `{syujin}` dei file di dialogo. Il
giapponese sceglie fra 「ご主人様」 e 「お嬢様」 **guardando il sesso del
giocatore** (`:7043`-`:7046`); l'inglese dice «master» in tutt'e due i casi.

⭐⭐ **Qui il sesso del giocatore SI CONOSCE**, ed e' l'eccezione che la guida di
stile prevede: il participio si vieta *quando il genere e' ignoto*, e qui il
codice lo porta scritto in fronte. La resa e' «padrone»/«padrona», e la via
giusta non si scrive senza rimettere l'`if`: **toppa a blocco, con la forma
copiata dal ramo giapponese tre righe sopra**.

ⓘ `{onii}` e' 「お兄」/「お姉」, cioe' il **vocativo** e non il sostantivo: la resa
e' «fratellone»/«sorellona», perche' «fratello» renderebbe 兄 e perderebbe il
registro, che e' l'unica cosa per cui quel segnaposto esiste.

### ⚠️ «ENGLISH» IN QUESTA BUILD VUOL DIRE ITALIANO

`config.hsp:950`, `s = "Japanese", "English"`, la scelta della lingua. La resa e'
**«Giapponese», «Italiano»**, non «Inglese»: in questa build il ramo `en` **e'**
la traduzione italiana — e' li' che vivono le 26.326 firme, le 1.166 toppe e i
file dati `_it.txt` — quindi chi sceglie quella voce ottiene l'italiano.
ⓘ Il valore scritto in `config.txt` e' l'**indice**, non la stringa.

⚠️ **E' l'unica resa della 127a che non e' riscossa da nessuna parte.** Se un
giorno sembrera' sbagliata, si cambia con una riga: e' una toppa sola.

### ⭐ TRE TRAPPOLE DELL'INDENTAZIONE IN UN LOTTO SOLO

Il generatore del lotto di coda si e' fermato **tre volte**, sempre per la
stessa ragione: **due righe che dicono la stessa cosa a due profondita' diverse
sono due righe diverse**, perche' il `cerca` di una toppa e' la riga intera,
tabulazioni comprese. Le tre copie dell'avviso sui 30 KB sono 2+1; le due del
` *tick* ` sono 1+1.

💡 A fermarlo non e' stato `applica` ma **il conto atteso scritto a mano nello
strumento**: `if quante != attese: raise`. `applica` si sarebbe fermato lo
stesso, ma dicendo «e' ambigua» invece di «te ne aspettavi tre e ce ne sono
due». Chi scrive un lotto con `"tutte": true` scriva anche quel conto.

### Due bestie, e un participio che si poteva evitare

⭐ In `calculation.hsp:2352` l'inglese confonde due animali: ナメクジ e' la
**lumaca** senza guscio, かたつむり la **chiocciola** (e' un'altra battuta
ancora, a `:2342`), e «snail» le diceva tutt'e due. L'italiano distingue.

⭐ In `main.hsp:8422` i compagni salutano **il giocatore** al rientro, e
«Bentornato» li' e' vietato: 「おかえり」 di genere non ne ha. Tutte e sette le
rese sono invariabili, e «Ti aspettavo da tanto» e' all'imperfetto apposta, per
non tirarsi dietro il participio che «ti ho aspettato» avrebbe portato.

---

## ⚠️⚠️⚠️ IL DEBITO DI COLLAUDO E' ~9.650 E NON E' MISURATO DA NIENTE

E' un numero tenuto **a mano** in questo documento, non c'e' nessuno strumento
che lo calcoli, e vale come ordine di grandezza e non come misura.
ⓘ **Nessuna delle 78 toppe della 127a e' stata vista a schermo**, ne' le 40
della 126a, ne' le 167 rese e le 17 toppe della 125a.

💡 E fra le 78 ce ne sono alcune che un collaudo vedrebbe subito, perche' stanno
dove si passa comunque: la schermata del titolo senza salvataggi, il menu delle
opzioni, la creazione del personaggio con i geni, il pannello di chi si guarda,
il rientro a casa.

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 127a

    pytest                   796 passed, 6 skipped
                             ⓘ due prove nuove: la rete dei caratteri a doppia
                                larghezza e la prova che la esercita
    prova_identita           72/72 e 30.905, **invariato**
    applica                  30.764 sostituzioni, **invariato**
                             ⓘ le toppe non sono sostituzioni: command.hsp 170 ->
                                **202**, config.hsp 0 -> **7**, text.hsp 10 -> **13**
    perimetro.py             26.326 fatte, 0 da fare, 100,0%, **invariato**
    triage_nudi              **testo 62** (era 158), sigla 87, dbg 93, spenta 22
    _126-nudi-nel-ramo-jp    **59 vive**, 3 nel ramo jp
    _126-spente-da-una-costante  **14 morte**, e **45 VIVE DAVVERO**
                             ⭐ di cui 44 dichiarate in invariati.md
    _126-sorella-jp          ⭐⭐ **0 con sorella**, 59 senza — cioe' OGNI riga
                             nuda che aveva una fonte giapponese e' stata resa,
                             e quel referto ha finito il suo mestiere: quel che
                             resta ha l'inglese come unica fonte, o e' dichiarato
    _126-referti-toppe       **participi 0, elisioni 0** su 905 toppe con testo
                             ⚠️ lo zero non e' «nessun participio»: l'espressione
                                e' identica a quella di referti.py apposta
    nudi_en                  struttura 1044, **ancora da fare 264** (era 360)
    toppe                    **1.166**, e `_97-toppe-agganciate` **1.166 su 1.166**
    referti                  **participi 9, elisioni 0** (il dizionario, invariato)
    maiuscole                143/6/1/7/0, **invariato**

Tutto il resto e' **fermo dov'era** e vale l'elenco della 125a piu' sotto:
`_123-file-senza-dizionario` 2 firme mute, `menu_dialogo` 0 su 1.423,
`_108-accento-decomposto` 0 su 26.326, `verifica --dizionario` 112 in 19 file,
`_97-quanto-resta` 112/112/0, `_125-non-tradotte` 112/112/0, `creature`
1131/2466/0/0, `larghezze` 0, `diario` 0 su 205, `riquadri` 0 su 38 e 0 su 71,
`linguette` 0 e 0, `battute --divergenti` 13, `dati_sorgente` 7/7, `gronde` 0 su
5, `bilingui` 0, `lang-nel-ramo-jp` 21 | 0, `_96-morte-nella-build` 0, e tutti i
referti da `_107` a `_126`.

⚠️⚠️ **TUTTO E' COMMITTATO E SPINTO** su `origin/fase-0`, e l'albero e' pulito.

---

## Che cosa guardare quando il fronte delle righe nude sara' chiuso

Non e' una domanda per domani: con 45 righe di cui 44 dichiarate, e' la domanda
di **adesso**. Le tre cose che questo documento sa e che nessuno ha ancora
preso:

1. ⭐⭐⭐ **Il debito di collaudo.** ~9.650 rese mai viste a schermo, e nessuno
   strumento che le conti. E' il fronte piu' grande del progetto e l'unico che
   non si chiude scrivendo codice.
2. ⭐⭐ **Le reti sulle toppe.** Dopo la 126a e la 127a le toppe hanno tre
   referti — participi, elisioni, caratteri a doppia larghezza — e **nessuno**
   che guardi il **glossario**, le **larghezze** o le **maiuscole**. Sono 905
   toppe con testo dentro.
3. ⭐ **La coda nuda di una `lang()` gia' resa** (vedi `chat.hsp:17065` qui
   sopra): un referto che nessuno ha scritto, e che avrebbe trovato quella frase
   mozzata senza bisogno che qualcuno leggesse il blocco.
