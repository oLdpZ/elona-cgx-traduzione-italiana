# Fase 5 — `tcg_mod.hsp`, le descrizioni d'effetto delle carte

Aperta **e chiusa** nella **centotrentaseiesima** sessione, 2026-09-03.

## ✅ ESITO: 833 descrizioni su 833, e 8 battute su 8

    strumenti/carte.py + 39 prove          --estrai/--reimporta/--applica/--referto
    dizionario/carte/effdesc.jsonl         833 rese
    dizionario/carte/efftalk.jsonl           8 battute
    toppe                                  1.228 -> 1.230
    copertura                              8 fronti / 1.020 -> 7 / 211
    in gioco                               eseguibile delle 23:05 del 03/09

⚠️ **Tre cose sono andate diversamente da come le prevedeva questo piano**, e
stanno scritte in `decisioni.md` (136ª) e in `RIPRESA-sessione.md`:

1. **Il cancello sulla partizione misurava il sorgente**, che è pinnato a un tag
   e non cambia mai: era un verde che non poteva diventare rosso. Spostato sulla
   build ha trovato **195 carte con la copia spenta a metà fase** — il piano
   diceva «le toppe prima delle rese», ed era giusto ma proteggeva solo l'inizio
   e la fine. Riparato facendo cercare alla toppa tutt'e due le parole.
2. **La toppa su `"ragon"` non si è fatta**: quel ramo è già spento da prima di
   questa fase, per via della traduzione di `db_card`, e ripararlo è una
   decisione di glossario fuori perimetro.
3. **Il file aveva anche 9 `efftalk@tcg`** che il piano non contava: 8 tradotte,
   1 concatenata dichiarata ed esclusa.

---

## Perché esiste questa fase

La 135ª ha costruito `strumenti/copertura.py`, la prima rete del progetto che
parte **dall'elenco dei file del sorgente** invece che dall'elenco delle cose
già coperte. Sotto un `perimetro.py` che diceva **100,0%** ha trovato 1.020
stringhe inglesi a schermo, e **1.007 erano il minigioco delle carte**.

    tcg_mod.hsp     809 distinte   le descrizioni d'effetto di OGNI carta
    tcg_skill.hsp   142            schede di carta, battute, randomchat
    tcg.hsp          52            etichette `[Command Card]`, `<Mage Guild>`, menu
    tcg_custom.hsp    4
    db_card.hsp       1

Questa fase prende **solo `tcg_mod.hsp`**. Le altre 198 sono la Fase 6, e il
perché del taglio sta più sotto.

⚠️ **La famiglia era stata lavorata a metà senza che si vedesse.** Ci sono già
118 toppe sul contorno del minigioco — le fasi del turno, il menu dei mazzi — e
`dizionario/db_card.hsp.jsonl` ha **2.285 voci tutte tradotte**: i nomi delle
carte e le loro descrizioni di sapore sono italiani da fasi. Chi apre il gioco
di carte oggi legge italiano intorno al tavolo, italiano sul nome della carta, e
**inglese sull'effetto** — cioè sull'unica riga che serve per giocare.

---

## La forma del fronte: è il caso migliore che il progetto abbia mai avuto

    835 righe    effdesc@tcg(COSTANTE) = "letterale"
    835 indici   tutti distinti, nessun duplicato
    834          letterali puri; UNO solo con `\"` dentro (r3119, TCG_EFF_MARKA)
     44.029      caratteri

Per confronto, `scene2.hsp` della Fase 4 ne aveva **167.003**. Questo fronte è un
quarto di quello, e a differenza di quello ha **una chiave naturale**: il nome
della costante. Non serve un'impronta dell'inglese, non serve `file:riga` — che
si sposta sotto una resa e ha già fatto danni.

⚠️⚠️ **E non c'è nessun giapponese da consultare.** Contati i byte:

    tcg_skill.hsp   346.475 byte,       0 non-ASCII
    tcg_mod.hsp     316.416 byte,      18 non-ASCII
    tcg.hsp         170.465 byte,     970
    db_card.hsp     888.845 byte, 167.179

`tcg_mod.hsp` è inglese cablato: diciotto byte in tutto il file. La Fase 4 aveva
`scene1.hsp` accanto e poteva **appaiare** ogni blocco al suo giapponese quando
l'inglese era ambiguo — qui quella rete non c'è. Dove l'inglese è oscuro (e le
descrizioni d'effetto lo sono: sono gergo di regole scritto stretto) non c'è una
seconda lingua di monte a dirimere: c'è solo **il codice che implementa
l'effetto**, in `tcg_skill.hsp`. È il primo fronte del progetto in cui la fonte
di verità di una resa dubbia è il comportamento, non un secondo testo.

⭐ **E il lavoro vero non sono le 835 rese: è un glossario di quaranta voci.**

    teste di frase distinte: 38
      443  Battlecry          38  Deathrattle        11  After Combat
       63  Begin Phase        14  End Phase          11  In-Hand
       57  Ongoing             9  Battlecry/OnKill    6  Start of the game
       39  Sacrifice           5  When Opponent Draw this

Le 30 teste più frequenti coprono **727 frasi su 735**. Sotto la testa il
vocabolario è altrettanto chiuso: `Card` 313, `Deck` 162, `Hand` 124, `Draw`
113, `Opponent` 104, `Damage` 94, `Field` 94. Decisi questi, le descrizioni sono
formulaiche.

⚠️⚠️ **E l'inglese non è coerente con sé stesso**: `Begin Phase` / `BeginPhase`,
`In-Hand` / `In Hand`, `Start of the game` / `Start of the Game`. L'italiano non
deve ereditare l'incoerenza, e il modo per non ereditarla non è la buona volontà:
è una tabella di grafie con **un cancello che la legge** (vedi «Le reti»).

---

## I sei vincoli di comportamento, e perché si toppa l'operando

Cinque righe del codice **cercano un letterale dentro il testo della carta**. Se
la resa italiana non contiene più quella parola, il ramo non scatta e il gioco
non lo dice.

    tcg_skill.hsp:618    instr(effdesc@tcg(dbid), 0, "Battlecry")
    tcg_skill.hsp:4960   instr(carddetailneff@tcg(...), 0, "ragon")
    tcg_skill.hsp:4972   idem
    tcg_skill.hsp:5003   idem
    tcg.hsp:1470         instr(carddetailneffbk@tcg, 0, "Bits:  ")

⚠️ **`tcg_skill.hsp:618` non era nell'elenco della ripresa della 135ª**, che ne
contava tre. Decide se una carta può essere **copiata**: cerca a caso fino a
dieci carte con `TCG_SKILL_TYPE_BATTLECRY` e accetta solo quelle la cui
descrizione contiene la parola. Se nessuna la contiene, `dbid@tcg` resta -1 e
l'effetto non copia niente.

⭐ **La conclusione è opposta a quella che la ripresa suggeriva.** La ripresa
diceva: la resa di «dragon» deve contenere «ragon», quindi «dragone» va e
«drago» no. Ma:

    "Battlecry"   compare in  475 descrizioni su 835
    "Deathrattle" compare in   49
    "ragon"       compare in    4
    "Bits:  "     compare in    0   <- sta in carddetailneff, non in effdesc

Vincolare 475 rese a contenere una parola inglese per non toccare **un `if`** è
il verso sbagliato di tre ordini di grandezza. Il progetto ha già la regola
giusta, scritta nella 135ª per le uova di Pasqua di `command.hsp`: *tradurre
senza tradurre l'altro capo del confronto spegne l'evento in silenzio*. Qui
l'altro capo sono cinque righe, e si toppano.

⚠️⚠️ **E le toppe vanno scritte PRIMA delle rese, non dopo.** Finché l'operando
cerca l'inglese, ogni resa nuova spegne un effetto — e lo spegne in silenzio,
perché nessun contatore del progetto guarda dentro un `instr`. È l'unico ordine
possibile dei lavori.

⚠️ `"Bits:  "` (con **due** spazi) va guardato a parte: non compare in nessuna
`effdesc`, quindi la Fase 5 non lo tocca. Lo produce `tcg.hsp` componendo la
scheda, ed è roba della Fase 6. Va comunque verificato che resti intatto: il
`--referto` lo controlla.

---

## L'a capo automatico che nessuno aveva visto

`tcg.hsp:1465-1476` ricompone la scheda della carta:

    carddetailneffbk@tcg = "Effect: " + effdesc@tcg(card@tcg(TCG_CARD_EFFECT, aeft))
    talk_conv carddetailneffbk@tcg, 65
    carddetailneff@tcg(aeft) += "\n" + carddetailneffbk@tcg

⭐⭐ È **lo stesso `talk_conv` della Fase 4** (`init.hsp:1329-1368`), che spezza
sugli spazi e mai dentro una parola, qui a **65 colonne**. Quindi le 835
descrizioni **non si impaginano a mano**: hanno solo un soffitto di righe.

Simulando `talk_conv` a 65 col prefisso `"Effect: "`:

    570 descrizioni da 1 riga
    255 da 2
     10 da 3        <- la più lunga in inglese: 137 caratteri (TCG_EFF_SOCKS)

⚠️ **L'inglese non è una taratura.** Sta comodo entro 3 righe e non sfiora mai
un limite, quindi non dice dove sia il limite. L'italiano cresce del 15-20% e
una parte delle 255 da 2 righe passerà a 3, e le 10 da 3 passeranno a 4.

### Il resto del riquadro invece NON va a capo

`tcg.hsp:3493-3507`, che disegna `helpmsg@tcg`:

    if ( gdata(GDATA_QUICK_USE) == 1 ) {
        font ..., 12, 0
        pos basex + 125, basey + 542
        mes helpmsg@tcg
    } else {
        font ..., 10, 0
        if ( displayinfo@tcg == 1 ) {
            font cfg_font2, 13, 0
            split helpmsg@tcg, "\n", splitbuff
            if ( stat >= 4 ) { font cfg_font2, 11, 0 }     <- il corpo SCENDE
        }
        pos basex + 120, basey + 537
        mes helpmsg@tcg
    }

`mes` in HSP disegna le righe separate da `\n` **verbatim**: nessun a capo
automatico. E sopra le **4 righe** il corpo scende da 13 a 11.

⚠️⚠️ **QUESTO SOFFITTO NON LO SO, E NON LO DEDUCO.** Il numero di righe che il
riquadro regge prima di mangiarsi il testo non sta scritto da nessuna parte: sta
in quanto è alto il riquadro disegnato, che è grafica. La 132ª ha già sbagliato
**tre** numeri dedotti in questo modo, e li ha smentiti una schermata; la 135ª
ha registrato la lezione generale (*un numero che nessuno ha visto a schermo non
è un vincolo, è un'ipotesi*).

⭐ **Come si chiude questa incognita:** una schermata del dettaglio di una carta
lunga — `TCG_EFF_ZEOME` (r3250, 125 caratteri), `TCG_EFF_SOCKS` (r3208, 137) o
`TCG_EFF_CHAOSUNICORN` (r2708, 116) — con `displayinfo@tcg` acceso. Si conta il
passo fra le righe e quante ne entrano, come la 132ª ha fatto per `{txt}`.

⚠️ **Fino ad allora il cancello NON rifiuta**: usa il massimo dell'inglese (3
righe, 4 col prefisso) come **soglia d'avviso**, e stampa il punto in cui si
accende — «TCG_EFF_X: 5 righe, l'inglese ne faceva 3». Un cancello che chiede
l'impossibile viene disattivato, non rispettato: è la lezione della 134ª sul
soffitto dei `{txt}`.

---

## Lo strumento: `strumenti/carte.py`

Ricalcato su `strumenti/scene.py`, che è il modello del progetto per «un fronte
che il dizionario non raggiunge». Stessa forma, stessi quattro comandi:

    python -m strumenti.carte --estrai NOME    -> lavoro/lotti/tcg-<NOME>.jsonl
    python -m strumenti.carte --reimporta FILE -> dizionario/carte/effdesc.jsonl
    python -m strumenti.carte --applica        -> riscrive build/tcg_mod.hsp
    python -m strumenti.carte --referto        -> il cancello

**Il riconoscitore** accetta **solo** la forma esatta

    ^\s*effdesc@tcg\(([A-Za-z_][A-Za-z0-9_]*)\)\s*=\s*"(.*)"\s*$

e **conta quante righe ha riconosciuto**. Se non sono 835, si ferma. ⚠️ È la
lezione delle «35 toppe che nessuno confrontava con niente» (96ª): il numero
atteso batte l'avviso, perché non chiede a nessuno di ricordarsi.

**La chiave è il nome della costante.** Non l'impronta dell'inglese (due carte
possono avere la stessa descrizione), non `file:riga` (si sposta).

### ⚠️ Il dizionario va in `dizionario/carte/effdesc.jsonl`, in sottocartella

Non è estetica. `applica.py:772` fa

    for percorso_dizionario in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):

— **non ricorsivo** — e per `scene2.hsp` ha dovuto mettere uno **scarto cablato**
a `applica.py:782` (`if nome_file == scene.FILE: continue`). Qui lo scarto non si
può fare: `dizionario/tcg_mod.hsp.jsonl` **esiste già** con 8 voci `lang()` vere
(i colori delle carte: BLUE→BLU, GREEN→VERDE, WHITE→BIANCO...) che `applica`
deve continuare a vedere. Un secondo file `tcg_mod.hsp.*.jsonl` accanto sarebbe
raccolto dal `glob` e passato al riconoscitore delle firme `lang()`, che non le
troverebbe.

La sottocartella è la soluzione che il progetto **usa già**: `dizionario/dati/`
per i sei file di `data\`, letta da `dati_applica.py` e invisibile al `glob`.

### ⚠️ L'a capo si calcola sulla forma DEGRADATA, non sulla resa

CP932 non contiene **nessuna** vocale accentata italiana: non `à`, non `è`, non
`ù`. Il progetto lo risolve con `strumenti/accenti.degrada`, che il dizionario
non applica — lì l'accento vero si conserva, ed è giusto così — e che chiamano
`applica.py` e `scene.py:376` scrivendo nell'albero di build:

    "Rarità"  (6 caratteri nel dizionario)  ->  "Rarita'"  (7 a schermo)

Quindi ogni accento **allunga il testo di un carattere**, e `talk_conv` conta i
caratteri che vede lui. `carte.py` deve:

- chiamare `degrada` in `--applica`, come `scene.py`;
- calcolare le righe in `--referto` **sulla forma degradata**, altrimenti il
  conto è ottimista proprio sulle rese più italiane;
- controllare `accenti.non_ascii_residuo` e `accenti.doppi_byte_cp932` su quel
  che scrive, come fa `dati_verifica.py:461-464`.

⚠️ E vale la trappola su cui sono inciampate la 133ª **e** la 135ª: le caporali
`«»` CP932 non le sa scrivere. Una resa che le contiene va fermata prima
dell'albero di build, non dopo.

### L'ordine di build guadagna un passo

    python -m strumenti.applica            <- rigenera l'albero da sorgente/,
                                              CANCELLA ogni iniezione
    python -m strumenti.scene --applica
    python -m strumenti.carte --applica    <- NUOVO, qui
    python -m strumenti.compila --eseguibile
    cp .../build/2.05-custom-gx/elonapluscgx.exe .../elonaplus2.31/cgx-test.exe

⚠️ `strumenti.installa` non esiste: l'ultimo passo è una copia a mano.

⚠️ E vale il vincolo di sempre: `sorgente/` **non si scrive mai**. Il file da
riscrivere è `build/tcg_mod.hsp`.

---

## Le reti

**`carte --referto`**, sul modello di `scene --referto`:

    righe riconosciute       835 su 835        <- si ferma se non torna
    tradotte                 N su 835
    prova d'identita'        il file torna identico, 0 sostituzioni
    righe fuori misura       N   (soglia d'avviso: 4 righe a 65 col prefisso)
    operandi intatti         5 su 5            <- vedi sotto

**La guardia degli operandi.** Cerca sulla **BUILD**, non sul sorgente, che ogni
`instr` dei sei vincoli abbia dall'altra parte una descrizione che lo contiene:

    per ogni (file, riga, letterale) dei 5 vincoli:
        il letterale cercato compare in >= 1 descrizione italiana?

Si accende quando una resa svuota un ramo. ⚠️ **E va provata al contrario prima
di crederle** — puntata su una descrizione dove il termine c'è di sicuro, con la
toppa dell'operando disinnescata, deve accendersi — e la prova deve **stampare
il punto in cui si è accesa**, non un ✅ (lezione della 107ª: un esito booleano
non distingue «ho trovato il guasto» da «non l'ho cercato abbastanza»). ⚠️⚠️ E la
prova si fa su una **copia** del file (`cp`, si rompe, si prova, `mv` indietro),
mai con `git checkout` su una riparazione non committata: è il nono modo di
perdere lavoro, costato una riparazione nella 134ª.

**La tabella delle grafie.** `carte.GRAFIE`, la resa canonica di ciascuna delle
38 teste e dei ~20 sostantivi del vocabolario chiuso. ⭐ A differenza di
`scene.GRAFIE` — che dalla 133ª è pronta e **nessuno legge** — questa nasce con
il cancello che la legge dentro `--referto`: una resa che scrive «Grido di
battaglia» dove la tabella dice «Grido di guerra» si accende.

**`copertura.MECCANISMI`.** La riga per `tcg_mod.hsp` si aggiunge **solo quando
lo strumento esiste e il conto torna**, non prima: una dichiarazione scritta in
anticipo è un fronte che sparisce dal censimento senza essere stato lavorato.

**`pytest`.** Test sul riconoscitore (le 835, il letterale con `\"` di r3119,
le righe che NON devono essere riconosciute), sulla simulazione di `talk_conv` a
65, sull'identità, sulla guardia degli operandi.

---

## L'ordine dei lavori

1. **Le cinque toppe sugli operandi**, con i termini italiani scelti al passo 2.
   ⚠️ Prima delle rese, sempre: è l'unico ordine che non spegne effetti.
2. **Il glossario del gioco di carte**: le 38 teste e il vocabolario chiuso, in
   `glossario.md`, con la decisione «il gergo si traduce» in `decisioni.md`. ⚠️
   I nomi delle carte **non si decidono qui**: sono già italiani nelle 2.285
   voci di `dizionario/db_card.hsp.jsonl`, e le descrizioni li seguono.
3. **`strumenti/carte.py`** e i suoi test, con `--estrai`/`--reimporta`/
   `--applica`/`--referto`.
4. **Le 835 rese**, a lotti, come `scene2.hsp`.
5. **La riga in `copertura.MECCANISMI`**, quando il conto torna.
6. **La compilazione e la copia in gioco**, e almeno una schermata guardata.

⚠️ **Il passo 6 non è facoltativo.** «È costruito» e «è provato a schermo» sono
due stati distinti, e il progetto porta un debito di ~11.400 rese mai viste.
Questa fase ne aggiunge 835 in un riquadro che **nessuno ha mai guardato**: se
il soffitto delle righe è più basso di quanto sembra, si scopre qui o non si
scopre.

---

## Perché la Fase 5 si ferma a `tcg_mod.hsp`

Le altre 198 stringhe sono un lavoro di **natura diversa**, non di dimensione
diversa:

- `tcg_skill.hsp` non ha una chiave stabile: 79 `carddetailneff@tcg(cextra@tcg)`
  con indice **variabile** e valore **concatenato** (`"High Potion of " +
  boozenames@tcg(rnd(10)) + "..."`), 28 `efllistaddchat "..."`, 8
  `efllistaddchatplayer`, 5 liste `randomchat@tcg = "a","b",...`;
- le etichette di `tcg.hsp:1560-1605` (`"<Mage Guild> "`, `"[Command Card] "`)
  si **appendono** con `s@tcg +=` alla stessa stringa delle schede: i due file
  vanno lavorati insieme, e nessuno dei due somiglia a `effdesc`;
- ⚠️ `tcg_skill.hsp` ha **zero byte non-ASCII** su 346.475: nessun ramo
  giapponese, l'inglese è cablato e si legge qualunque lingua si scelga. Vale
  quasi identico per `tcg_mod.hsp` (18 byte), quindi non è questo a separare le
  due fasi — è la chiave.

Un meccanismo che regga fin dal primo giorno due forme di chiave così diverse è
un meccanismo che non chiude un cancello finché non è finito tutto. Meglio due
fasi, ciascuna col suo cancello che chiude davvero.

⚠️ E le 198 vanno **lasciate dichiarate in `copertura`** finché non tocca a
loro. Un fronte che esce da un elenco non è un fronte chiuso: `scene2.hsp` uscì
dall'elenco della ripresa verso la 111ª senza essere stato lavorato, e ci
tornò venticinque sessioni dopo.

---

## Le incognite dichiarate

1. **Il soffitto di righe del riquadro.** Da misurare su una schermata. Fino
   allora il cancello avvisa e non rifiuta.
2. **`displayinfo@tcg`**: quando vale 1 non si sa senza giocare, e cambia il
   corpo del carattere da 10 a 13/11. La misura del punto 1 va presa sapendo in
   quale dei due rami si è.
3. **Il termine italiano di «Battlecry»** decide 475 descrizioni e una toppa: è
   la voce di glossario più pesante che il progetto abbia mai scritto in un
   colpo solo.
