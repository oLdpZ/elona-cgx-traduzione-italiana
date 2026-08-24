# Decisioni

Scelte non ovvie e il perché. Le decisioni numerate stanno in `SPEC.md` §10;
qui c'è il ragionamento che non ci stava in una riga di tabella, e le domande
ancora aperte.

---

## Il registro non si decide, si trova — 2026-08-24, novantatreesima

Otto lotti su `chat.hsp`, **87 rese**, dalle 221 alle **134**. NORNE la guida
(`:9431`-`:9600`, 11), LEIKI la tartaruga nera (`:8695`-`:8774`, 15), MELUGAST
AO-I (`:13182`-`:13215`, 12), SPIPHA la cacciatrice di draghi (`:9724`-`:9793`,
12), ARIBEL la monella (`:9983`-`:10013`, 10), ALSAPIA la maschera bianca
(`:15101`-`:15122`, 9), SINAHA (`:10877`-`:10909`, 9), ARASIEL della tempesta di
sabbia (`:10729`-`:10876`, 9).

### ⭐⭐⭐ In cinque lotti su otto il tono era già stato deciso da un altro file

La domanda che sembrava aprire ogni lotto — *che registro gli do?* — quasi mai
era una domanda. Quattro posti diversi, uno per lotto:

- **un'altra riga sua, in un altro file.** Leiki parla in keigo fittissimo e la
  mossa ovvia era il «lei» da maggiordomo, che il progetto usa già per il
  maggiordomo perché non concorda mai. Ma la sua unica riga resa fuori dal
  blocco, `map.hsp:15070`, gli fa già dare del **tu**: è deferente verso la
  **principessa**, non verso chi ascolta. Il «lei» avrebbe fatto parlare in due
  modi lo stesso personaggio a due schermate di distanza;
- **le battute di combattimento della creatura.** Aribel ha in
  `db_creature.hsp:62712`-`:62724` le sue «sette regole» («Mai abbassare la
  guardia», «Se si cade... si cade in avanti»): quattro righe rese sessioni fa
  che dicono di che pasta è fatta meglio di qualunque descrizione;
- **un lotto precedente dello stesso parlante.** Il blocco
  `CREATURE_ID_MELUGAST_AO_I` **non è di una creatura**: è una radio. A
  parlare è Gavela, reso nell'85ª, e lo dice la riga stessa (`:13187`, «Qui
  Gavela»). Il registro era in `scratchpad/_85-rese-gavela.py`, per intero;
- **una particella già risolta su un'altra creatura.** Il ニャ di Sinaha
  chiude undici frasi su nove righe, e `db_creature.hsp:44182`, `:54053` e
  `:56489` avevano già fissato la forma: **«miao» in coda, con la virgola**,
  allungato in «miaao» dove il giapponese allunga.

Il costo dello sbaglio qui non è una resa brutta: è un personaggio che parla
in due modi secondo dove lo incontri, e **nessuna rete lo vede** — sono due
frasi diverse in due file diversi, tutt'e due italiano corretto. Nel vault:
[[il-registro-non-si-decide-si-trova]].

### ⭐⭐⭐ «A0-I» contro «AO-I»: un refuso di monte si conta

`chat.hsp:13191` è una voce di menu che chiede *che cos'è l'A0-I?*, con lo
**zero**, in giapponese e in inglese. Ricopiarla sembrava l'unica cosa onesta.
Ma la sigla compare in altri **sei** siti — `chat.hsp:7821`, `:7830`, `:7833`,
`:7861`, `db_card.hsp:2701`, `db_creature.hsp:52005` — e in tutti, in tutt'e due
le lingue, è **AO-I con la lettera O**; così la scrive anche l'identificativo
`CREATURE_ID_MELUGAST_AO_I`. Un sito contro sei è un refuso, e ricopiarlo
avrebbe dato **due nomi alla stessa macchina** a un menu di distanza — cioè il
difetto che la 92ª ha trovato tre volte rileggendo il vicinato.

⚠️ La regola che ne esce non è «si corregge l'inglese», ma: **quando una sigla
sembra strana, la si conta**. Se il sorgente la scrive in due modi, la forma
giusta è quella che vince nel conteggio e che porta l'identificativo — non
quella del sito che si sta traducendo.

### ⚠️⚠️ Il numero di un referto va letto, non confrontato

`referti.py` è salito da **8 a 9** durante il lotto di Spipha. La 92ª aveva
già scritto che va rilanciato dentro il lotto, e così è stato fatto; il
riflesso, però, era guardare *se* il numero è salito. La riga nuova era
**innocua**: «per come te la sei cavata coi draghi» — participio che concorda
col clitico, gemello di `:22872` già dichiarato.

Nello stesso lotto, intanto, c'era un participio **vero**: «Sei stato tu ad
abbatterlo, vero?» (`:9744`), che dà un genere al giocatore. Il referto non lo
vede, ed è saltato fuori solo rileggendo le nove rese una per una prima di
chiudere. Corretto in «L'hai abbattuto tu, vero?», che di participi non ne ha.

**Un contatore che sale per la ragione giusta può nascondere quella sbagliata.**
Il referto dice *dove guardare*, non *se guardare*.

### ⭐⭐ «Di chi è la riga in più?»: due risposte opposte nello stesso lotto

La domanda della 90ª ha funzionato meglio che mai perché ha dato risposte
diverse a due righe vicine:

- `chat.hsp:8702` — la riga in più era **mia**. Il vocativo 冒険者様 non può
  diventare «avventuriero» (porta un genere) e la formula del progetto — «tu che
  vai all'avventura» — costa venti caratteri contro i dieci di «Adventurer».
  Riassorbita girando la frase: «Ti prego, aiutaci tu che vai all'avventura!»;
- `chat.hsp:8706` — la riga in più era **dell'inglese**, che butta la citazione
  con cui i forti di Valm se ne sono andati («andiamo a convincere un paese che
  è in guerra»). Si tiene.

E `chat.hsp:13201`, lo sproloquio tecnico di Gavela, ha **sfondato il tetto**:
15 righe contro le 13 di `chatMore`, mentre l'inglese ci sta **esatto**, 13 su
13. Due giri di potatura per rientrare, senza togliere nessuna delle nove voci
dell'elenco — che sono la battuta, visto che lui si interrompe da solo. 💡 La
misura da ricordare: su un elenco di **termini composti** l'italiano paga circa
il **15%** in più dell'inglese, e su una battuta già al tetto diventano due
righe.

### ⚠️ Il mestiere del giocatore ha portato un genere cinque volte in quattro lotti

冒険者様 (Leiki, `:8702`), 立派な冒険者になった (Norne, `:9587`), 戸惑っている
(Norne, `:9590`), ドラゴンハンターとして頑張った君 (Spipha, `:9754`),
冒険者発見 (Alsapia, `:15107`): cinque siti in quattro lotti dove il giocatore
viene chiamato col nome del suo mestiere o descritto con un participio.
Nessuna è stata risolta inventando: valgono la formula già in uso — «tu che
vai all'avventura», «ecco chi va all'avventura» — o il giro sul verbo («di
strada ne hai fatta», «per come te la sei cavata», «un po' di smarrimento,
eh?»). ⭐ Il fatto che la stessa trappola sia comparsa **cinque volte in un
giorno** dice che non è un caso ma una **classe**: ogni volta che il giapponese
nomina il giocatore per quello che fa, in italiano c'è un genere da schivare.

### ⭐ Quattro cose che l'inglese aveva perso, e due che aveva capovolto

- `:15107` — 第一陣と第二陣: il giocatore è arrivato da Alsapia **sfondando la
  prima e la seconda ondata** di sicari. L'inglese: «I am surprised that you are
  already here». Era l'unica riga che legava l'agguato ai bollettini di
  `:24347`;
- `:9740` — 今回は違ったけれど: **stavolta non era quello**, cioè il drago
  abbattuto non è il drago nero che Spipha cerca da tutta la vita. Senza, la
  riga smette di chiudere la missione appena finita;
- `:8706` — la citazione dei forti partiti (sopra);
- `:9990` — 何億種 sono **specie** di insetti, non «kinds of books»: la battuta
  è che gli insetti sono infiniti e la madre legge sempre lo stesso atlante;
- `:13192` — 畳みかける non è «Interrogate him!» ma **incalzare senza dare
  respiro**: è un ordine d'attacco in mezzo a un combattimento, e interrogare
  il mostro non è nemmeno possibile;
- `:9986` — 「逆境上等！覚悟は上々！」 sono **due vanti** («le avversità? ben
  vengano!», «la mia determinazione è ottima») e l'inglese li legge tutt'e due
  come paura: «This is bad! Prepare yourself!». La spavalderia di una ragazzina
  diventa l'avvertimento di chi ha paura.

### ⭐⭐ Due frasi che dovevano essere identiche a due frasi che esistevano già

- `:10802` (Arasiel) e `map_user.hsp:878` sono **due verbi giapponesi diversi**
  — 解除 e 解散 — per lo stesso identico rifiuto del gioco, nello stesso identico
  momento. Sono due firme distinte, quindi nessuna rete le lega: si è scritta
  la **stessa frase**, «Prima devi sciogliere la coppia.», se no il giocatore
  legge due messaggi diversi per la stessa cosa;
- `:15116` e `:15119` (Alsapia) sono **gemelle**: cambia solo l'incipit, perché
  la seconda risponde alla battuta del menu. La parte comune si dice con le
  stesse parole, se no il gioco del menu non si sente. ⚠️ L'inglese le fa già
  diverse («your graveyard» / «your grave»): non lo si è seguito.

### 🔶 Da decidere: l'epiteto di Sinaha

Il nome italiano di 《不幸のシナア》 è **«<Sinaha>» e basta**. L'epiteto
«della sfortuna» è caduto seguendo l'inglese, che scrive solo «<Sinaha>» — ma
il progetto altrove **ricostruisce** l'epiteto proprio quando l'inglese lo
butta: «<Leiki> la tartaruga nera» (da 玄武の, inglese «<Leiki>»), «<Alice> la
formica gigante», «<Aribel> la monella», «<Alsapia> la maschera bianca». E qui
l'epiteto è la ragione per cui il personaggio esiste: **legge la sfortuna** al
giocatore, ed è tutto quello che fa.

Non è stato cambiato perché un nome di creatura si tocca insieme alla sua
misura di larghezza e a tutte le rese che lo citano: è un lotto suo, non una
riga di un lotto d'altri.

---

## Un nome non si traduce, si riconosce — 2026-08-24, novantaduesima

Nove lotti su `chat.hsp`, **143 rese**, dalle 364 alle **221**. AMURDAD
(`:10627`-`:10728`, 12), l'aiutante del maestro Spada Rossa
(`:14525`-`:14659`, 18), MIKRAANESIS (`:9367`-`:9430`, 18), SHURAIDA
(`:13537`-`:13633`, 17), ALICE la formica gigante (`:9794`-`:9853`, 17),
LANKATA (`:13834`-`:13896`, 16), MANYTIA (`:13634`-`:13833`, 15), BETHEL
(`:13216`-`:13265`, 15), BELPHAT (`:12560`-`:12632`, 15).

### ⭐⭐⭐ Due elenchi di katakana non erano da tradurre: erano da riconoscere

`chat.hsp:9409`-`:9412` è Mikraanesis che elenca le **ventotto** divinità di cui
è fatto: 交合のミクシス, 思念のエンノイア, 真理のアレーテイア, 独り子のモノゲーネス…
Non sono nomi inventati dall'autore: sono gli **eoni valentiniani**, il pleroma
gnostico. E la prova non sta nell'elenco — sta nella **trama intorno**, che il
progetto ha già tradotto: Sophia, il padre inconoscibile 《深淵のプロパトル》
(`:9423`), ed **Enthumesis**, che nel mito è letteralmente la passione di Sophia
staccata da lei, ed è esattamente così che `:10213` la racconta.

Nove righe più in là, in un altro lotto, la stessa forma: il diario di viaggio
di Belphat (`:12576`-`:12594`) elenca ユゴス, サイクラノーシュ, バイアクヘー,
ミ=ゴ, cioè il **Ciclo di Cthulhu**. Lì la prova sta nel dizionario: «lo
shoggoth» (`db_creature.hsp:80712`), «la Grande Razza di Yith»
(`db_card.hsp:14390`), «classe Yith» (`action.hsp:2604`), e `Necronomicon` e
`Liber Damnatus` in `invariati.md`.

⚠️ **L'inglese, in tutti e due i casi, traslittera a orecchio.** *Nuus* per
Nous, *Areteia* per Aletheia, *Outpuece* per Autophyes, *Aquinatos* per
Akinetos, *Maitrikos* per Metrikos, *Aeneus* per Aeinous, *Macalia* per Macaria;
*Yugos* per Yuggoth, *Bayakhae* per Byakhee, *Cyclanorch* per Cykranosh. Chi
traduce dall'inglese ricopia lo storpiamento in buona fede, perché **niente nel
testo che ha davanti segnala l'errore**: le forme sbagliate sono pronunciabili,
regolari, coerenti fra loro. Sembrano nomi inventati, che è quel che non sono.

💡 **E su due voci l'errore non è di grafia: cambia la parola.**
独り子のモノゲーネス è *Monogenes l'**Unigenito*** (独り子 = figlio unico) e
l'inglese scrive «Monogenes of **Solitude**»; イス焼き è *Yith alla piastra*, in
coppia con たこやき nella stessa frase, e l'inglese — leggendo イス come *ice* —
scrive «**fried ice cream**». Nessuna rete può vederlo: la forma sbagliata è
una parola italiana perfettamente regolare.

⚠️ **Ma non si inventa una fonte che non c'è.** Nello stesso elenco di Belphat,
ボッヘリト, デベロンダッタ, ジェラミス, ニャリン, スンバラリア e トゥンツァ non
appartengono a nessun canone: restano nella forma dell'inglese. *Riconoscere
vuol dire anche riconoscere quando non c'è niente da riconoscere.*

Nel vault: [[un-nome-non-si-traduce-si-riconosce]].

### ⭐⭐⭐ Un pronome possessivo inglese è un fatto di parentela, e si verifica nel codice

`:13837` in inglese dice «I was able to rescue **your** father». Il giapponese
dice 「父上は救助できましたが」, cioè *sono riuscita a salvare **il** padre* — e
di chi sia lo dice il codice: il padre di Lankata ha un identificativo,
`CREATURE_ID_ALFRED_THE_CANGNAN_WIND`, e la scena in cui lo trova sta venti
righe più in là ed è già resa (`:18131` lo crea, `:18138` è lei che dice
«Padre!», `:18143` è lei che gli estrae il reattore, `:18155` è **lui** che
chiede «Io... sono salvo?»). Il giocatore, in Elona, un padre non ce l'ha da
nessuna parte.

💡 *Un possessivo dell'inglese si tratta come un identificativo: dice chi è
parente di chi, e va cercato nel sorgente prima di ricopiarlo.*

### ⭐⭐ Le battute doppie e le parodie hanno un vincolo di forma

Tre casi in tre lotti diversi, e in tutti e tre il senso da solo non basta:

- **「アリーヴェデルチ！」** (`:9797`) è insieme (a) una parola *straniera* e
  (b) una parola che comincia per **アリ**, *formica*, come il nome della
  creatura, アリッス. «Arrivederci!» in italiano non è né l'una né l'altra.
  Rifatta sul canale che l'italiano ha — lo stesso gesto del «formicalità»
  della 90ª, sullo stesso personaggio: **ARRIFORMICARCI!**
- **「サンキューベリマッチ！！」** (`:9804`) è *thank you very much* in katakana:
  il punto è che lo dice in una **lingua straniera**. Upstream l'ha capito e ha
  fatto la mossa simmetrica — la versione inglese scrive «Arigatou
  gozaimashita!» — quindi per chi legge in italiano la lingua straniera del caso
  è l'inglese, e la riga resta **«THANK YOU VERY MUCH!!»**.
- **`:13852`** («posate **la statuetta** e lasciate **questo mondo**») è la
  parodia di **`:13856`** («posate **le armi** e lasciate **questo piano**»), e
  quella di Lankata è il `buff` che sta **sopra il menu**: si leggono nello
  stesso istante, quindi in italiano devono usare gli stessi verbi o la parodia
  sparisce.
- **`:13231`**, stessa famiglia: 猫の手も借りたい storpiato in 「鷹の翼も借りたい」
  perché chi parla **è** il falco bianco. In italiano il modo di dire esiste ed
  è sulle braccia: «qui non bastano due braccia, ci vogliono anche due ali».

### ⭐⭐ Tre righe già rese riparate, e nessuna era raggiungibile dalle reti

- **`:269`** diceva «Norne, hai fatto bene a guidare **la tua amica** fin qui».
  Il giapponese non ha oggetto: l'italiano ne aveva aggiunto uno **femminile**,
  cioè dava un genere al giocatore in una delle prime battute della storia.
- **`:10211`** chiamava 《深淵のプロパトル》 **«<Prophatorl dell'abisso>»**
  (ricopiando il refuso inglese) mentre `:9423`, resa dopo, dice **«<Propator
  dell'Abisso>»**. Una entità, due nomi a schermo.
- **`:13714`** diceva **«(99999gp)»** mentre le due voci gemelle dello stesso
  menu (`:13773`, `:13774`) dicono **«(99999 oro)»**, che è la convenzione
  (`chat.hsp:8825`).

⚠️ **Il punto non sono i tre difetti: è che nessuna rete poteva vederli.** Sono
frasi diverse fra loro, quindi `battute --divergenti` non le confronta;
`verifica --dizionario` guarda solo le firme; `controlla_voce` gira solo sui
lotti. Le ha trovate la **lettura del vicinato del blocco**, che è un lavoro
manuale e non ha uno strumento. 💡 È la stessa rete mancante che la ripresa
elenca da otto sessioni («rileggere tutto il dizionario con le regole nuove»),
e oggi ha dato tre difetti veri in tre lotti su nove: il rapporto è alto
abbastanza da giustificare una passata dedicata.

### ⭐ Due dichiarazioni in `invariati.md`, tutt'e due «identica per costruzione»

`...???` (`:9829`, quel che Alice «dice» quando le si tiene la medicina fuori
portata) e `Larnneire...` (`:13219`). La seconda è lo **specchio esatto** di
`Bethel...` (`:1591`), già dichiarata dalla 57ª: là è Larnneire che pronuncia il
nome di lui, qui è Bethel che pronuncia il nome di lei. In tutti e due i casi
l'identità con l'inglese nasce dalla somma di due decisioni già prese — il nome
resta invariato, i puntini si scrivono coi tre punti ASCII — e senza la
dichiarazione `verifica.py` boccia il lotto intero.

### 💡 Quel che l'inglese ha buttato via, e che è stato rimesso

Sei casi, tutti dello stesso tipo — l'inglese riassume e perde un **fatto**,
non una sfumatura:

- `:13575` (Shuraida): il terreno, il numero e la resistenza del nemico, e la
  capacità del giocatore di tenere il campo — cioè le tre ragioni del consiglio
  tattico, in una missione dove il giocatore decide come muoversi;
- `:13707` (Manytia): i **calzini** aggiunti alla chiave, che agganciano la
  riga a una catena di battute già resa per intero (`:12431`, `:12513`,
  `:12713`-`:12738`, `:13170`);
- `:14529` (l'aiutante): il **maestro Spada Rossa**, che è nel nome di chi parla
  (`db_creature.hsp:54727`);
- `:10685` (Amurdad): 行っても, *anche se ci vai non potresti riportarla
  indietro* — l'inglese ricicla la formula generica del gruppo pieno, identica
  in nove file;
- `:13698` (Manytia): il complimento interessato e la risatina, che sono il suo
  modo di parlare;
- `:12591` (Belphat): il polpo **vivo** che si dimena, che è il motivo per cui
  se l'è mangiato per strada.

⚠️ E tre volte l'inglese non taglia ma **capovolge**: `:13888` (Lankata) fa
diventare un fallimento un'attesa; `:13646` (Manytia) nega la leggenda due
parole prima di confermarla; `:14548` (l'aiutante) si congratula per una scelta
che il giocatore non ha ancora fatto.

---

## Una firma condivisa non e' di un lotto solo — 2026-08-24, novantunesima

Otto lotti su `chat.hsp`, **153 rese**, dalle 517 alle **364**. NEIN la strega
volante (`:10442`-`:10520`, 24), ALLEN il ricercatore (`:15145`-`:15199`, 23),
GARZIEM (`:11912`-`:12063`, 22), SSIL la strega del divieto infranto
(`:14928`-`:15070`, 20), L'ANIMA SMARRITA (`:10551`-`:10626`, 20), JIN la
macchina fuggiasca (`:10910`-`:10981`, 19), REGULUS l'uomo modificato
(`:12779`-`:12871`, 19) e **RAIZEL** (`:10391`-`:10434`, 6), che non era in
programma. Le deroghe stanno per esteso negli otto moduli di `scratchpad/`.

### ⭐⭐⭐ La rete che ha chiesto un lotto

Chiuso REGULUS, `strumenti.bilingui` e' passato da **0 a 1**:

    chat.hsp:12832-12833   2 voci, 1 rese, 1 no
            :12832  'Hold on a minute.'

La firma di 「ちょっと待って」 ha **due occorrenze** — `:10398`, nel blocco di
Raizel sulla Nave Magica, e `:12832`, nel menu di Regulus — e
`estrai --da-tradurre` la assegna alla **prima**. Quindi il lotto di Regulus
conteneva 「出発」 ma non la sua compagna di menu, e a schermo il menu sarebbe
uscito meta' in italiano e meta' in inglese.

⚠️ **La riparazione ovvia era sbagliata.** Rendere solo `:12832` avrebbe
spostato il difetto di quaranta righe: il menu di Raizel (`:10398`-`:10399`)
sarebbe diventato bilingue a sua volta, perche' 「出撃！」 non era resa. La
riparazione vera e' stata chiudere il blocchetto di Raizel per intero, sei
firme, e allora `bilingui` e' tornato **0**.

💡 *Una firma condivisa non appartiene al lotto che la incontra per primo:
appartiene a **tutti i menu in cui compare**, e si chiude con loro. Quando
`_85-blocco.py` dice «con occorrenze FUORI: 1» su una voce di `chatList`, il
lotto non e' finito quando finisce il blocco.*

⭐ E la misura c'era gia': `_85-blocco.py 12779` aveva scritto «con occorrenze
FUORI: 1» **in apertura di lotto**, e il modulo di Regulus lo aveva pure
annotato. Quello che mancava non era il dato, era la conseguenza — che si e'
vista solo dopo la reimportazione, quando ha parlato una rete diversa. Vedi la
76ª, dove `bilingui` era nata proprio per i menu che si bucano da soli.

### ⭐⭐⭐ Quando l'inglese aggiunge un fatto, il gioco puo' smentirlo

`chat.hsp:10445`, Nein: 「行方不明のミネア姉さま」, *mia sorella Minea, che e'
scomparsa*. L'inglese aggiunge **dove**: «that went missing within the ruins of
Nefia».

Minea esiste. E' `<Minea> The Puppeteer` di `scene2.hsp:2581` e seguenti, e li'
racconta lei la propria storia: ha inventato una magia per manovrare gli
uomini, l'esaminatore l'ha bocciata come volgare magia di dominio, «soon people
began to call me the shame of House Bellum», i genitori hanno tagliato i ponti
e lei se n'e' andata a fare l'avventuriera. **Non e' sparita in una Nefia: e'
stata cacciata di casa** — la casa che Nein, sua sorella minore, vuole far
tornare grande diventando capo degli incantatori di corte.

Si segue il giapponese e si tace il dove. E' la regola della 57ª, ma con un
argomento in piu': qui l'aggiunta dell'inglese non e' solo non attestata, e'
**contraddetta da un altro file dello stesso gioco**.

⚠️ `scene2.hsp` non e' nel dizionario. Chi lo tradurra' deve sapere che
`<Minea> The Puppeteer` e' la sorella di Nein: sta scritto nel modulo
`_91-rese-nein.py`, che e' l'unico posto dove i due fili si toccano.

### ⭐⭐⭐ L'inglese puo' buttare una variabile, e allora il conto sparisce

`chat.hsp:15056`, Ssil:

    jp  "…今デッキに入っているカードは" + syurui + "種類のようですのう。ひひ…"
    en  "Ah, let me see your deck... Not bad, not bad. Please, show me again..."

`syurui` **non c'e' piu' nell'espressione inglese**. E' l'unico posto del gioco
dove si legge **quanti tipi di carte si hanno gia'**, cioe' la ragione per cui
si torna a parlarle: chi traduce sull'inglese perde il conto per sempre, e
nessuna rete se ne accorge, perche' l'espressione inglese e' coerente con se
stessa e `verifica` controlla che le interpolazioni **presenti** siano
conservate, non che non ne manchi una.

L'italiano rimette `syurui` dentro. Non e' inventare un pezzo: e' ricucire un
pezzo che il giapponese ha.

💡 *Per le dinamiche, il confronto che conta non e' fra le due stringhe ma fra
le due **liste di variabili**. Una rete che le confronti non c'e'; se un giorno
si scrive, questo e' il caso di prova.*

### ⭐⭐ Il genere puo' essere ignoto per costruzione

Il bambino dell'anima smarrita non ha un sesso: `db_creature.hsp:44851` fa

    if ( cdata(CDATA_SEX, rc) == 1 ) { cdata(CDATA_PIC, rc) = xy2pic(27, 10) }

cioe' **cambia il ritratto** secondo un sesso che per quella creatura non e'
fissato da nessuna parte. Quindi la regola del genere — che il progetto
applicava al giocatore — vale anche per l'**interlocutore**, e nello stesso
modo: niente participi, niente aggettivi, e i sostantivi si scelgono neutri.

Conseguenza concreta: 「クソガキ」 era gia' reso «moccioso» (`chat.hsp:804`), ma
li' il bersaglio ha un sesso noto. Qui si dice **«peste»**, che vale per un
maschio e per una femmina. Il glossario **non** cambia: cambia il posto.

### ⭐⭐ Una via d'uscita nuova: il participio col clitico

In italiano l'accordo del participio con un complemento oggetto anteposto e'
**obbligatorio** con `lo/la/li/le` e **facoltativo** con `mi/ti/ci/vi`. Quindi

    「廃棄処理区画に送られてしまった」  ->  «mi hanno **spedito** allo smaltimento»

e' corretto e **non da' un genere a nessuno**. Vale per il parlante (Jin, che
di genere non ne ha) e vale per il **giocatore**: «ti hanno mandato», «mi hai
salvato», dove finora si giravano le frasi. Da oggi e' la prima mossa da
provare, prima del giro di frase.

### ⭐⭐ Un nome si controlla nell'ortografia del gioco

`chat.hsp:14954`: l'inglese scrive «a man named **Blade Runner**». Il
giapponese e' ブラッドランナー, e il gioco ha una sua ortografia:

    ブラッド -> blood   (living blood, blood golem, dead-eyes blood dragon: otto in db_creature.hsp)
    ブレード -> blade   (ブレードボウ = blade bow, db_item.hsp:136506)

Il nome resta **Blood Runner**. Stessa famiglia al rovescio: **casa Bellum** non
si e' dedotta dalla riga che la nomina, ma da `scene2.hsp:3204` («I'm from House
Bellum in Eulderna») e `db_item.hsp:51432` — cioe' **si e' cercato il nome
altrove prima di romanizzarlo**, come si fa con gli identificativi.

### ⭐ Tre mucchi, non due, per le righe piu' lunghe dell'inglese

La 90ª aveva diviso in due: prolissita' mia (si accorcia) e pezzo buttato
dall'inglese (si tiene). Su diciannove righe segnalate oggi ne e' servito un
terzo:

    dodici   prolissita' mia               -> accorciate
    cinque   l'inglese ha buttato un pezzo -> tenute, con la prova nel modulo
    due      italiano piu' lungo e basta   -> tenute, **dichiarate come tali**

Le due sono `chat.hsp:10968` (Jin) e `:12809`/`:12816` (Regulus, contate come
un caso solo). Il tetto non mordeva in nessuno dei diciannove casi.

💡 *Dire «qui non ho una scusa» costa una riga di modulo e vale piu' di una
scusa inventata: la sessione dopo, chi rilegge sa che quella riga e' stata
guardata e non e' sfuggita.*

### ⚠️ Le tre reti che hanno morso, e nessuna era quella che ci si aspettava

1. **`referti.py`, da 8 a 9 participi.** `chat.hsp:10488` diceva «con che mezzi
   ci sei **riuscito**»: un participio riferito al giocatore. Non poteva vederlo
   ne' `verifica` (guarda le firme) ne' `chat-lotto-misura` (guarda le righe).
   ⭐ Va rilanciato **dentro** il lotto, non solo in chiusura: la differenza fra
   8 e 9 e' leggibile solo se il numero di prima lo si conosce.
2. **`verifica`, due trattini lunghi.** `chat.hsp:10967` ne aveva due: CP932 li
   codifica su due byte e la build inglese disegna un glifo per byte.
3. **`verifica`, una virgoletta nuda** dentro una statica (`:12818`,
   「レナイ」 fra virgolette).

### ⭐ Il perimetro di `chat.hsp` si e' appiattito

Dopo oggi **non c'e' piu' nessun blocco sopra le 18 firme**. La mappa comincia
con PART_TIME_WORKER_THE_RED_SWORD (18), MIKRAANESIS (18), SHURAIDA (17) e
ALICE_THE_BIG_ANT (17) — la formica gigante di MARY, resa ieri. Le sessioni che
vengono non avranno piu' un lotto grosso da cui partire: molti blocchi piccoli,
e il costo per resa che sale. ⚠️ Con blocchi piccoli le firme condivise fra
menu diventano **piu'** probabili, non meno: la lezione di oggi serve subito.

## «Di chi e' la riga in piu'?», e un bisticcio rifatto — 2026-08-23, novantesima

Cinque lotti su `chat.hsp`, **174 rese**, dalle 691 alle **517**: il file e'
sceso di un quarto in un giorno. KARAVIKA la cantante (`:12064`-`:12331`, 41),
BYSYMLHA occhi d'ambra (`:15200`-`:15330`, 38), MELGET l'informatrice
(`:12907`-`:13181`, 32), MARKA l'orsa d'argento (`:11771`-`:11892`, 32), MARY
l'entomologa (`:9854`-`:9982`, 31). Zero contraccolpo su tutti e cinque, zero
reti nuove, zero toppe.

### ⭐⭐⭐ Davanti a una riga lunga la domanda non e' «accorcio?» ma «di chi e' la riga in piu'?»

`chat-lotto-misura` applica la regola prudente della 73a: *l'italiano non
faccia piu' righe dell'inglese*. Oggi ha segnalato **ventitre'** rese in cinque
lotti, e trattarle tutte allo stesso modo sarebbe stato sbagliato in tutt'e due
i versi.

Perche' quel metro misura contro **l'inglese**, e l'inglese qualche volta ha
buttato via del testo. Quando succede, accorciare l'italiano vuol dire
ributtarlo via una seconda volta:

- `:15214` (4 righe contro 2) e `:15328` (4 contro 3) di BYSYMLHA sono
  **esattamente** le due deroghe dove l'inglese taglia il giapponese. `:15328`
  in particolare perde 「頭ではわかっていても…私の身体がわかってくれないのです」,
  che e' la riga che dice chi e' quel personaggio.
- `:13075` di MELGET e' la deroga dove l'inglese butta via il primato
  precedente del quiz, che e' un dato che il giocatore usa.

Le altre venti erano **prolissita' mia** su un inglese di pari contenuto, e
accorciate leggono meglio. Tutte accorciate, zero rimaste.

⚠️ **E il tetto va misurato prima di decidere, in tutt'e due i versi.** Un
`chatMore` da un bottone tiene **13** righe — `(324 - 19 - 43) // 19` — e
l'italiano piu' lungo della giornata ne faceva 7. Nessuna di quelle righe
tagliava niente. E' la regola della 89a (*prima di accorciare si guarda se il
tetto puo' mordere*) girata al rovescio: **dove il tetto non morde, la riga
lunga non e' un difetto da riparare** — va guardata la sua provenienza, non la
sua lunghezza.

💡 *Una rete prudente e' prudente rispetto a un metro. Quando il metro e' un
testo di monte che ha perso qualcosa, obbedirle e' propagare la perdita.*

### ⭐⭐⭐ Un gioco di parole si rifa', e il precedente e' dell'inglese

`chat.hsp:9942` in giapponese e' 「ありがとうねぇ、アリだけに。」: 「ありがとう」
contiene 「アリ」, la formica, e Mary lo fa notare — una battuta brutta apposta,
detta dalla donna che ha appena trasformato in mostro una formica. L'inglese la
cancella e scrive «Thank you so much!».

Cancellarla anche in italiano sarebbe stato «seguire l'inglese», ma il progetto
aveva gia' deciso il contrario altrove, e senza accorgersi che era una regola
generale: le **fusioni delle razze** (piu' su in questo file) dicono che «si
rende il gioco, non le sillabe», e li' il precedente e' dell'**inglese stesso**,
che ダゴンズイ lo ricostruisce in `daganotosus` invece di tradurlo. Cioe':
l'inglese i giochi di parole li rifa' quando puo' e li butta quando non puo'.
Noi possiamo.

E la parola l'italiano ce l'aveva gia' in mano, perche' <Alice> **e'** «la
formica gigante» (`db_creature.hsp:62712`):

    «Grazie mille, eh. E non e' una formicalita'.»

💡 *La regola dei nomi vale anche per le battute: si guarda cosa il progetto ha
gia' scelto per i parenti.*

### Il genere del parlante sta nel nome, e tre volte su cinque non si e' deciso

MELGET, MARKA e MARY hanno tutt'e tre il genere **scritto nel nome della
creatura**: «l'informatrice» (`db_creature.hsp:69199`), «l'orsa d'argento»
(`:73827`), «l'entomologa» (`:76576`). Quindi «mi ha bloccata», «sono
scappata», «mi hai salvata», «l'avventuriera e' corsa su per le scale» non sono
scelte del lotto: sono conseguenze.

⚠️ **Il rovescio vale per il giocatore**, che di genere non ne ha (75a), e oggi
ha chiesto **nove** giri di frase — «stai tremando tutto», «tranquillo»,
«impalato», «non ti sei fatto male», «per uno come te», «ci siamo gia' visti»,
«uno stalker?», «maniaco», «goloso». Il caso piu' istruttivo e' `chat.hsp:12314`:
「変質者め」 ha gia' la sua parola nel progetto («maniaco»,
`db_creature.hsp:68205`), ma quella parola accorderebbe il giocatore. ✅ Si tiene
la parola e si **sposta il bersaglio**: il cavaliere la grida ai suoi («Al
maniaco!») e al giocatore da' l'ordine, che di genere non ne porta.

### Il lessico che serve non sta nel glossario: sta nella pagina che spiega la cosa

Di BYSYMLHA — il pannello delle difficolta' travestito da tentatrice — dieci
termini su undici erano gia' scritti, e **nove venivano dalla stessa pagina**:
`chara.hsp:4225`-`:4314`, la descrizione delle modalita' di gioco, che e' il
testo che spiega proprio quel menu. «Di base e' 3x, e in un certo posto si
arriva fino a 30x» (`:4231`) — e quel «certo posto» e' lei.

Stessa forma per MELGET: le dodici curiosita' del mese nominano una per una
cose che hanno gia' un nome altrove (il gufo spaziale, la penna d'oca lucente,
il <Gigante Castagna>, i calzini, l'organizzatrice di viaggi, una certa
cacciatrice di draghi), e **sedici** termini erano gia' decisi, nessuno nel
glossario.

💡 *Prima di decidere una parola, si cerca il testo che descrive la stessa cosa
da un'altra angolazione. Il glossario e' l'ultimo posto dove guardare, non il
primo.*

### ⭐⭐ L'eco puo' attraversare due personaggi, non solo due scene

La 89a aveva imparato che un'eco attraversa due sessioni (Dain che giudica i
pugnali che Irma presenta). Oggi ne e' venuta fuori una piu' larga: la
curiosita' di **novembre** di Melget (`chat.hsp:13173`) accusa
「丘の民の集落長」 di spargere notizie false per stroncare chi non gli va a
genio. Quello e' **Dain**, «l'anziano della collina», reso ieri — e il giocatore
che ha appena fatto la sua missione lo ha visto fare esattamente quello con la
nipote.

Le due righe stanno a tremila righe di distanza nello stesso file, in bocca a
due persone che non si incontrano mai. A tenerle insieme non c'e' nessuna rete:
c'e' solo l'aver cercato 「丘の民」 nel dizionario prima di scrivere.

### La firma e' la coppia (jp, en), non il posto — e il lotto se ne accorge da solo

Il menu di MARKA a `:11829` ha tre voci, e tutt'e tre erano gia' rese. Ma la
terza — 「わかった」 / «Alright.» — non veniva da un'altra riga di Marka: veniva
da `chat.hsp:1712`, dall'altra parte del file. `_88-lotto.py` l'aveva tolta dal
perimetro e `_85-applica-rese.py` si e' **rifiutato di scrivere** finche' non
gliel'ho detto («perimetro diverso: mancanti [11832], in piu [11830]»).

⭐ E' il caso in cui una rete noiosa paga: senza quel rifiuto avrei riscritto
una resa gia' esistente su una riga sbagliata, e nessun'altra verifica se ne
sarebbe accorta.

### Due parole che non si scrivono, e una che non si scrive per un altro motivo

- **「dèi」 non si scrive.** `verifica` l'ha bocciata a `chat.hsp:13152`: la
  degradazione CP932 mette l'apostrofo **dentro** la parola («de'i») e a schermo
  non si legge. La riparazione e' cambiare parola, non togliere l'accento: la
  riga chiude con «Che paura fa, un dio».
- **L'ordinale femminile «ª» non si scrive**, per la stessa ragione di
  carattere. A `chat.hsp:12275` l'italiano evita l'ordinale contando in avanti
  («Con questa fanno N strette di mano»), che dice la stessa cosa. Li' `cnvrank`
  era gia' morfologia inglese (85a).
- **ベイベー due volte, due rese.** A `chat.hsp:12153` Karavika lo grida dal
  palco al pubblico, e la resa e' l'eco di `screen.hsp:1486` («Ti amo, bella!»);
  a `:12275` lo dice **al giocatore**, e «bella» gli darebbe un genere: li' vale
  «beibi», che e' la traslitterazione con cui il progetto rende gia' ベイベー
  (`db_creature.hsp:89694`). Due siti, due rese, e la differenza la detta **chi
  ascolta**.

---

## La collina di Dain, e il tetto che si applicava dove non tagliava — 2026-08-23, ottantanovesima

Tre lotti su `chat.hsp`, **98 rese**, dalle 789 alle **691**, piu' una
correzione di rete. DAIN l'anziano della collina (`:10982`-`:11085`, 38),
THALIA la guardastelle (`:11086`-`:11205`, 28), URCAGUARY la gemma tenace
(`:12332`-`:12559`, 32).

### Il contraccolpo si misura PRIMA di scegliere il lotto, e stavolta ha scelto lui

La ripresa dava due strade: KARAVIKA (41 firme, zona chiusa) oppure la coda
della missione di Irma, cioe' DAIN e THALIA. Ma DAIN aveva «1 fuori», e prima
di decidere si e' guardato **che cosa** fosse: `chat.hsp:11069`, 「残念だ」 /
«That's too bad.», che vive anche a `:12526` — dentro il blocco di URCAGUARY —
ed e' una **voce di menu**. Quindi il contraccolpo era certo (85a: conta il
TIPO di sito, non il numero).

⭐ **E misurarlo ha reso la scelta piu' facile, non piu' difficile.** Dando
`_85-blocco.py` a tutt'e due i blocchi nella stessa invocazione si e' visto che
la catena e' **reciproca e si chiude li'**: DAIN e URCAGUARY si dividono quella
firma e solo quella, THALIA e' chiusa per conto suo. Costo vero 38 + 28 + 33 =
99 firme, che tolta la firma condivisa contata due volte fa **98**, e zero
fuori. La domanda non era «sporcare o rompere»: era «quanto costa non
rompere», e la risposta era tre lotti in un giorno (85a).

### L'ECO che tiene insieme due lotti a un giorno di distanza

Le quattro battute con cui Dain giudica i pugnali (`:11019`, `:11022`,
`:11025`, `:11028`) sono l'**eco** (84a) delle quattro con cui Irma li presenta
(`:11733`, `:11737`, `:11741`, `:11745`), rese nella 88a. Il giocatore legge le
due scene a pochi minuti di distanza: la seconda deve riconoscere la prima
**parola per parola** — «il disegno e' rozzo», «l'impugnatura», «la lama»,
«stravagante». 💡 *Un'eco puo' attraversare due sessioni, e allora non e' piu'
«due righe che si scrivono insieme»: e' una riga che si scrive rileggendo il
dizionario.* Nessuna rete la vede.

### L'inglese scambia CHI va risparmiato, e a giudicare e' il blocco

A `:10990` Dain manda il giocatore a distruggere il rifugio di Irma. L'inglese
dice di catturare **Irma** illesa, «She might still be useful for pressuring
Thalia»; il giapponese dice 「サリムにはまだ利用価値があるから傷つけずに連れて
こい」, cioe' che e' **Thalia** a servire ancora e che va riportata indietro
senza farle male.

Il pronome inglese («her») e' ambiguo, il giapponese no. E qui non c'e' un ramo
di codice a fare da giudice — nessun `if` distingue i due — quindi giudica il
**blocco**: a `:10986` Dain ha appena festeggiato che Irma se ne sia andata, a
`:11043` giura che non riconoscera' mai niente di suo, a `:11074` si strugge
perche' la nipote non vuole raccogliere la tecnica. Si segue il giapponese
(57a, «l'inglese scambia»). 💡 *Quando il codice non puo' giudicare, giudica il
personaggio — e il personaggio sta scritto nelle altre trentasette righe del
lotto.*

### Un giapponese, DUE inglesi, due firme

`:12394` e `:12473` di Urcaguary hanno lo stesso identico giapponese; l'inglese
di `:12473` conserva 「アンタは立派な騎士団備品調達係さ！」 e quello di `:12394`
lo lascia cadere. E' la 84a al contrario — li' erano *due* giapponesi in *un*
inglese — e la differenza la detta il sito: `:12473` e' la prima volta che il
titolo viene dato, `:12394` e' il giro successivo, dove il giocatore ce l'ha
gia'. Due rese diverse, e le firme restano due perche' firma = giapponese
*piu'* inglese.

### ⭐⭐⭐ Un tetto che si applicava anche dove il taglio non succede

`menu_dialogo` ha segnalato due rese al tetto delle due colonne, e il primo
istinto era accorciarle: sono voci di menu, ventotto e venticinque caratteri
contro un tetto di ventiquattro. Prima di farlo si e' guardato **da dove viene
il metro** (70a), e il metro non c'era:

    init.hsp:47      #define chatList(%1,%2) ... listn(0,listmax)=%2 : listmax++
    chat.hsp:25217   listmax = 0        <- l'ultima riga di *chat_select
    chat.hsp:25166   if ( keyrange > 10 & ... ) { listn(0,cnt) = strmid(..., 0, 24) }

`chatList` appende e incrementa; `*chat_select` azzera `listmax` in coda.
Quindi ogni menu comincia da zero, le sue voci sono esattamente le `chatList`
fra un `gosub *chat_select` e il successivo, e il numero **si legge**. I due
menu segnalati ne hanno **tre** e **due**: sotto le undici, `strmid` non gira
mai.

⚠️⚠️ **Il commento della rete diceva da quattro sessioni «non e' decidibile dal
sorgente», ed era vero per un menu solo.** Per il menu di un compagno, dove le
voci le aggiunge la trama, resta vero; per un menu scritto a mano in `chat.hsp`
e' falso, ed e' stato falso per 907 voci su 1.073. 💡 *Una limitazione
dichiarata onestamente resta una limitazione: dichiararla non la misura* — e'
la 64a («una nota onesta su un limite non lo ripara») applicata a un commento
invece che a un referto.

⚠️ **E il danno di un tetto finto e' quello della 66a, cioe' il verso
pericoloso**: non «lascia passare un errore» ma «spinge ad accorciare
l'italiano per un motivo che non esiste», e cedere costa sempre meno che
indagare. Le sessioni precedenti avevano ceduto — l'84a lo scrive: «Le rese si
accorciano lo stesso, ma la correzione vera e' ancora da fare».

✅ La correzione era gia' scritta: `chat-lotto-misura.opzioni()`, che la 87a
aveva fatto per il tetto dei `buff`. E' stata **spostata** in
`strumenti/menu_dialogo.py` come `opzioni_del_menu()`, con quattro prove nuove
e col menu di MAILE (88a, undici voci, l'unico posto dove il taglio si e' visto
mordere) come controllo positivo. `chat-lotto-misura.py` adesso la importa
invece di tenerne una copia: 54 righe in meno. 💡 *Se una rete conta, sta in
`strumenti/` e ha un test* (68a) — e se due reti contano la stessa cosa, la
contano con la stessa funzione.

### Il registro non si decide nemmeno per una parola sola

Il repertorio di Thalia in `db_creature.hsp:74088` era gia' reso, e la sua
prima battuta dice «Quel **vecchiaccio**...». ジジイ aveva quindi gia' la sua
resa italiana, in bocca alla stessa persona, per lo stesso nonno: dove
l'inglese scrive cinque volte il generico «the old man», l'italiano dice
«vecchiaccio», mentre il nome neutro di Dain resta «l'anziano della collina»,
che e' quello del diario. **Due parole per la stessa persona, tutt'e due gia'
scritte prima di oggi.**

Lo stesso vale per la risata di Urcaguary: フハハ e' «**Fuahaha**»
(`db_creature.hsp:71913`), non la trascrizione che verrebbe da se'.

### E il divieto di genere ha deciso quattro parole su undici

«successore» non ha femminile e a dirlo e' il giocatore -> **erede**. «amico»
si accorderebbe tre volte come vocativo -> **anima gemella**, dove l'accordo
cade su una parola nostra. «addetto ai rifornimenti» si accorderebbe tre volte
fra vocativo e titolo -> **responsabile**, che e' invariabile. E dove nemmeno
quello bastava, perche' serviva l'articolo, la frase e' girata: «i rifornimenti
dei Cavalieri Dorati **li curi tu**».

⚠️ Il rovescio: `CDATA_SEX` dice maschio per Dain (`db_creature.hsp:74262`) e
femmina per Thalia (`:74168`) e Urcaguary (`:71993`), quindi il loro parlato in
prima persona si accorda senza dubbi — «me n'ero **accorta**», «il paese dove
sono **nata**», «**Sola** non ci resto», «Sono **sicura** che». Il divieto e'
sul non sapere, non sull'accordo (80a).

---

## Il referto si legge sulla parola, non sulla riga — 2026-08-23, ottantottesima

Due lotti su `chat.hsp`, **99 rese** piu' **cinque rifatte**, dalle 888 alle
**789**. IRMA la forgiatrice straniera (`:11206`-`:11770`, 51) e MAILE la
sacerdotessa fantoccio (`:13266`-`:13516`, 48), tutt'e due zone chiuse.

### Un referto si legge sulla PAROLA che segnala, non sulla riga

`chat.hsp:16586` era **gia'** nella lista di `referti.py` alla 86a, e li' fu
archiviata fra i falsi positivi: la riga contiene «se le fallisci **la paghi
cara**», che e' un modo di dire dove il femminile e' il pronome fisso. Ma il
referto non segnalava quello. Segnalava «**sei ricercato**», dodici parole
dopo, scritto nella 82a e accordato col giocatore.

💡 **Il difetto stava nella riga gia' guardata, e la guardata precedente
l'aveva mancato perche' aveva cercato una spiegazione invece della parola.**
Un referto non dice «questa riga e' sospetta»: dice «questa PAROLA e'
sospetta». Chi lo legge deve trovare quella, non una qualunque.

### La resa che non accorda e' spesso anche la resa che nomina bene

A `:14435` — «le pergamene non si leggono se sei **cieco** [...] riescono male
se sei **confuso**» — la correzione ha due ragioni e non una. La prima e' il
divieto di genere. La seconda e' che il giapponese scrive 「盲目の時」 e
「混乱の時」, cioe' i **nomi degli stati**: `_conblind` e `_conconfuse`
(`text.hsp:96` e `:99`), che in italiano sono **Cecita'** e **Confusione**. La
resa che non accorda col giocatore e' anche quella che copia il nome
dell'interfaccia.

⭐ Lo stesso a `:16586`: la resa giusta non e' un giro di parole per scansare
il participio, e' la frase che il gioco **grida** quando una guardia ti
riconosce — «C'e' una taglia sulla tua testa!» (`db_creature.hsp:98449`,
`:115178`). E a `:14113` la segnalazione non era nemmeno un participio (il
referto l'ha pescata su «sotto»), ma «sei **sotto peso**» in italiano dice il
contrario di «while burdened», e lo stato in interfaccia si chiama **Fardello**
(`_burden`, `text.hsp:66`).

💡 Tre correzioni su cinque, e in tutte e tre la strada per uscire dal difetto
di grammatica passava per il **nome che il giocatore legge sullo schermo**.

### L'inglese di monte puo' costare il materiale, e il giudice e' il codice

A `chat.hsp:11348` Irma avverte che con quindici incantamenti pieni «ci monta
soltanto roba dello stesso tipo». L'inglese dice un'altra cosa: «one of them
will have to be replaced». **Non e' vero.** `encadd`
(`item_data.hsp:959`-`:973`) cerca uno slot con lo STESSO incantamento oppure
uno VUOTO, e se non lo trova fa `return 0`: non sostituisce mai niente. Ma il
materiale viene consumato lo stesso (`chat.hsp:11653`) e con lui la pergamena
di acquisizione di attributi (`:11667`).

⭐ Due righe sopra, lo stesso menu ha l'errore a monte: `:11347` in inglese
dice «Sorry.» dove il giapponese dice «cancella un incantamento», che e'
esattamente quel che il codice fa a `:11362`. **Una voce di menu deve dire che
cosa fa.**

💡 La deroga qui non e' una preferenza di resa: e' che seguire l'inglese
farebbe **perdere roba** al giocatore. Quando le due lingue divergono su una
meccanica, si apre il file che la implementa.

### Cercare prima di scrivere puo' fissare trentaquattro righe in un colpo

La zona di MAILE e' un servizio solo — cancella i ricordi del giocatore — e
non lo dice mai: mette in scena, in rosso, **trentaquattro finte righe di
errore di sistema**, una per variabile azzerata. Trentaquattro delle 48 firme
sono la stessa riga con dentro un nome diverso.

Quella riga **aveva gia' una resa**: `proc.hsp:26301`, la versione troncata
che compare quando il [記憶の灯] attutisce la cancellazione, dice «[Sistema]
Errore di origine ignota in globalda...». Il modello nuovo e' scritto perche'
la riga vecchia ne sia una **troncatura esatta**: stessa apertura, stesso «in»
davanti al nome.

⚠️ E i nomi delle variabili **restano in inglese**. Non sono lessico: sono
l'oggetto della finta diagnostica, ed e' quello che li rende spaventosi.

💡 Sulle stesse trentaquattro righe si e' deciso di **appiattire sull'inglese**
i tre verbi diversi del giapponese (初期化 / 再計算 / 削除). Una finta
diagnostica funziona **perche' e' identica a se stessa**: trentaquattro righe
con tre formule diverse smetterebbero di sembrare una macchina. E' l'unico
caso finora in cui la ripetizione e' un valore da difendere.

### Il tetto delle due colonne morde davvero sopra le dieci voci

Il menu di Maile ha **undici** voci, e sopra le dieci la pergamena passa a due
colonne e taglia con `strmid` a **24 caratteri** (`chat.hsp:25164`-`:25166`).
Non e' il tetto prudenziale da 58: li' il taglio succede. `menu_dialogo` fino
a oggi lo segnalava come «peggiorata rispetto all'inglese», che e' il modo
giusto di dirlo quando il numero di voci non e' deducibile — ma quando le voci
sono undici e si contano a mano, e' un tetto.

⭐ Per starci, le undici voci hanno perso il «Memory of» che l'inglese ripete.
Costava poco: il giapponese ce l'ha solo in due voci su undici (「〜の記憶」
contro 「〜のこと」), e la battuta che apre il menu dice gia' che si sta
scegliendo un ricordo.

### Il genere: due donne, due usi opposti dello stesso dato

Irma ha `CDATA_SEX = 1` (`db_creature.hsp:74075`), Maile pure (`:60888`).

Con **Irma** il genere si usa: «Ti hanno stroncata» (`:11700`) e' una voce di
menu rivolta a lei, e accordarla e' giusto. Col **giocatore** no: il 〜殿 che
Irma gli da' si butta — come fa l'inglese — perche' un vocativo di rispetto in
italiano vorrebbe un genere che il giocatore non ha.

Con **Maile** la soluzione e' arrivata dal registro. In giapponese da' del
貴方 al giocatore in 敬語, e la resa naturale e' il **voi di cortesia**: che
oltre a suonare come lei, e' **l'unica seconda persona italiana che non chiede
un genere**. 💡 Il tono giusto e la regola di genere possono essere la stessa
scelta.

### E una coda di metodo: due sessioni sullo stesso albero

La 87a era **ancora viva** mentre la 88a apriva. Si e' visto da `ListAgents`
(`elona-04 · busy`) e dai quattro file di chiusura che comparivano e sparivano
da `git status` mentre venivano scritti. Non si e' perso niente — le due
sessioni hanno committato in fila — ma e' successo per caso, non per
costruzione. **All'apertura si guarda `ListAgents` prima di scrivere nel
repo.**

---

## Il seminario si chiude, e tre reti imparano a leggere il codice — 2026-08-23, ottantasettesima

Quattro lotti su `chat.hsp`, **281 rese** piu' due rifatte, dalle 1.169 alle
**888**. I quattro conferenzieri del seminario — vita quotidiana, oggetti,
crescita, combattimento — sono spariti tutti dalla mappa dei parlanti.

### ⭐⭐⭐ Un commento non e' una riga che non conta

`_86-parlanti-oltre.py` diceva che il blocco di ARASIEL cominciava a `:10729` e
finiva a `:26774`: 958 firme, sedicimila righe, tutto il resto del file. Il
blocco vero e' `:10729`-`:10876`, **148 righe e 9 firme**.

Il contatore di graffe toglieva le stringhe, i commenti `//` e `;`, e i
commenti `/* ... */` che cominciano e finiscono **sulla stessa riga**. In
`chat.hsp` ce ne sono nove multiriga con graffe dentro — i blocchi `ORIGINAL` e
`BLOODYSHADE CUSTOM`, dove monte tiene il codice che ha sostituito — e **tre
portano una graffa spaiata**: `:169`, `:10752` (un `if (...) {` commentato
dentro il blocco di ARASIEL) e `:19629`.

    profondita' a fine file, contando i commenti:  3
    profondita' a fine file, togliendoli:          0

💡 *Un contatore che salta le righe commentate deve saltarle tutte, e i
commenti multiriga sono l'unico caso in cui una riga e' spenta senza portarne
il segno in testa.* ⚠️ E il numero era sbagliato anche dove sembrava giusto: i
blocchi di primo livello stavano a profondita' **0**, non 1 — quel `+1` veniva
da `:169`, e nella mappa della 86a e' passato per una convenzione.

⚠️ Corretto anche `_85-blocco.py`, che avrebbe mentito su qualunque lotto dopo
`:10752`. `_84-parlanti.py` invece non e' compromesso: li' l'offset era
uniforme su tutta la zona.

### ⭐⭐ Il tutorial e' il posto dove un nome sbagliato si vede

Il seminario spiega le meccaniche e **manda il giocatore a leggere lo schermo**.
Due rese vecchie non hanno retto al confronto:

1. `economy.hsp:357` diceva **«Influenza»** dove il gioco chiama quella
   statistica **«autorita'»** in otto altri siti, fra cui la voce di menu che
   la spende («Amministrare (autorita' 500/2000)»). Era il punto aperto dalla
   74a — *la statistica con due nomi sullo schermo* — e il tutorial lo ha reso
   insostenibile: il giocatore impara la parola a `chat.hsp:14047` e poi deve
   ritrovarla nel pannello.
2. `text.hsp:18` mandava «dal menu **<examine>**», che nell'interfaccia
   italiana si chiama **<Esamina>** (`text.hsp:135`). Un nome inglese dentro
   una frase italiana che indica dove andare.

⚠️ La colonna del prospetto e' larga **20 caratteri contati sulla forma
DEGRADATA**: «Autorita'» piu' undici spazi. Nel dizionario, con l'accento vero,
sono diciannove.

### ⚠️ Una precauzione ritirata invece che aggirata

`test_l_etichetta_italiana_non_porta_accenti` vietava l'accento in quelle
dodici etichette, e il suo docstring nominava proprio `:357`: *un'etichetta
accentata costringe a contare l'imbottitura su una forma che il file non
mostra*. Il timore era giusto quando e' stato scritto. Ma quel conto adesso non
si fa a mano: lo fa `test_l_etichetta_italiana_e_lunga_come_l_inglese`, sulla
forma degradata, contro l'inglese di monte, a ogni giro — ed e' verde.

Le strade erano tre: tenere «Influenza» e il difetto; aggiungere un'eccezione
per `:357`; togliere la precauzione. La seconda e' quella che la 77a chiama un
**debito** — *un elenco di eccezioni si rilegge ogni volta che si tocca uno dei
siti che nomina*. Tolta. `pytest` scende da 744 a **732**.

💡 *Una precauzione si ritira quando la cosa da cui proteggeva e' diventata una
misura.*

### ⭐⭐ Le guardie di un menu, finalmente lette

`chat-lotto-misura` misura una battuta contro il numero di bottoni della sua
finestra, `(324 - N*19 - 43) // 19`. Contava **sedici** bottoni nel menu dei
docenti, dove il giocatore ne vede **quattro**: le sedici `chatList` stanno in
quattro gruppi dentro `if ( gdata(STARTING_GDATA_FLAG + 329) == N )`, N da 1 a
4, che non possono essere veri insieme. Con sedici il tetto viene **negativo** e
qualunque resa risulta fuori misura.

Adesso le `chatList` si raggruppano per la guardia che le contiene, e per ogni
**sinistra** di `==` si prende il gruppo piu' numeroso invece della somma; i
gruppi con sinistre diverse, e le voci fuori da ogni guardia, si sommano lo
stesso, perche' li' l'esclusione non si sa. Nessuna regressione sui nove lotti
della 85a e della 86a.

💡 E il conto era sbagliato anche quando non lo sembrava: nel lotto di Ajetalio
la passeggiata all'indietro si fermava su una riga **commentata**
(`// chatList 4`), contava 12 invece di 16, e il tetto tornava positivo **per
caso**. ⚠️ Resta aperta l'altra meta': `menu_dialogo` conta le stesse voci allo
stesso modo.

### ⭐⭐⭐ Il giudice non e' la lingua piu' ricca: e' il ramo che si compila

A `chat.hsp:14124` Cresce elenca i segni che marcano la qualita' di un pezzo. Il
giapponese dice ☆ e 『』 per l'eccezionale, ★ e 《》 per lo speciale; l'inglese
dice `<>` e `{}`. Sembrava il solito inglese sbrigativo, e invece:

    item_func.hsp:1793   if ( ... == FIX_QUALITY_MIRACLE ) {
    item_func.hsp:1794       ... += lang("『", " <") + random_title(1) + lang("』", ">")
    item_func.hsp:1796   else {
    item_func.hsp:1797       ... += lang("《", " {") + random_title(1) + lang("》", "}")

Quei `『』` stanno nel ramo **giapponese**. L'italiano si costruisce sul ramo
inglese, quindi il giocatore vede `<>` e `{}`: seguire il giapponese gli
avrebbe insegnato a cercare segni che sul suo schermo non esistono. ⭐ E Mito
lo conferma tre volte (`:14404`, `:14471`, `:14491`), dove l'inglese scrive
«<> or {}» di suo.

### ⭐⭐⭐ Sette etichette che nessuna rete puo' vedere

Iduru insegna a leggere il potenziale nella scheda del personaggio, e i nomi
dei gradini stanno in `command.hsp:10676`-`:10700`:

    if ( p >= 400 ) { mes "Supreme" ... }
    ...
    mes "Hopeless"

**Letterali nudi, senza `lang()`.** Nessun dizionario li raggiunge: a schermo
sono inglesi oggi e restano inglesi finche' non li tocca una toppa. E' la
famiglia del punto cieco della 74a un gradino piu' sotto — li' erano
`listn(...) = lang(...)`, qui manca proprio la `lang()`.

Per la regola del tutorial la resa li lascia **in inglese**: sono le parole che
il giocatore legge davvero. ⚠️ Il giorno in cui si toppano, `chat.hsp:14246` va
rifatta, e sta scritto nel modulo delle rese.

⭐ **E il codice smentisce l'inglese sulla scala.** L'inglese di `:14246` dice
che «Superb is the best»: falso. `command.hsp:10676` mette **Supreme** in cima
(>= 400) e Superb al terzo gradino (>= 200). Il giapponese lo dice giusto.
Senza aprire il codice, l'errore era indistinguibile da una scelta di stile.

### ⭐ Un soprannome e' una catena, e si scrive tutta insieme

Iduru ha quattro battute legate: gli volevano dire «いづるん», lui ha preteso
師範 (`:14312`), la voce di menu chiede perche' (`:14275`), uno studente lo
chiama Idurino lo stesso (`:14293`) e lui sbotta (`:14373`). L'inglese la rompe
in **tre modi diversi**: a `:14275` si arrende in faccia al lettore («Is there
some untranslatable Japanese pun with your name?»), a `:14312` e' testo
automatico che non vuol dire niente («because it is an idle gumbah»), a
`:14293` usa il nome invece del soprannome rifiutato. In italiano la catena
regge: **«maestro»** contro **«Idurino»**. E' l'ECO della 84a — righe che si
scrivono insieme o non si scrivono.

### ⚠️ Quattro righe morte, rinviate invece che tradotte

`:13991` e' `// chatList 4, ...`, `:14036`-`:14038` sono `; chatMore ...`:
monte ha cambiato la quarta voce del menu del secondo incontro di Ajetalio e ha
lasciato spenta la coppia domanda/risposta vecchia. E' la famiglia di
`chat.hsp:19327` (76a): tradurle avrebbe messo numeri veri in `menu_dialogo` e
in `chat-lotto-misura` su righe che non disegnano niente. `rinviate.jsonl` da
75 a **79**.

---

## `*chat_unique` si chiude, e il divieto di genere si allarga — 2026-08-22, ottantaseiesima

Cinque lotti su `chat.hsp`, **326 rese** piu' una rifatta, dalle 1.495 alle
**1.169**. A fine giornata `scratchpad/_84-parlanti.py` dice **0 su 86
blocchi**: la zona `*chat_unique` (`:947`-`:8629`) e' chiusa.

### ⚠️⚠️ Il divieto di genere non vale solo sul giocatore

Fino a oggi la regola si diceva cosi': *il giocatore non ha genere noto, quindi
nessuna resa puo' accordarsi con lui*. E' incompleta. Il capo dei banditi e
l'istigatore degli Elea sono due creature UNICHE, con un nome e un blocco tutto
loro, e **non hanno un sesso**:

    db_creature.hsp:115501   if ( cdata(CDATA_SEX, rc) == 1 ) {   <- ROGUE_BOSS
    db_creature.hsp:40979    if ( cdata(CDATA_SEX, rc) == 1 ) {   <- INSTIGATOR_OF_ELEA

Non **assegnano** `CDATA_SEX`: lo **leggono**, e cambiano solo la faccia. Il
sesso lo ha tirato il gioco quando la creatura e' nata. Quindi «sono stanco» in
bocca al capo dei banditi e' sbagliato una volta su due, esattamente come lo
sarebbe in bocca al giocatore.

💡 *Il dato non e' nell'epiteto e non e' nel pronome giapponese: e' nel blocco
`DBMODE_SET` della creatura, e va guardato per ogni parlante nuovo.* La
domanda da porsi e' due volte: **il codice assegna il sesso?** e, se lo
assegna, **quale?**

⭐ L'altra faccia paga: MEFAN, la pifferaia di Hamelin, ha `CDATA_SEX = 1`. Il
nome della carta diceva gia' «la pifferaia» e sembrava una scelta di stile —
era il dato, e le sue battute possono accordarsi al femminile senza dubbi.

### ⭐⭐ Le firme «fuori» possono essere RECIPROCHE

`_85-blocco.py` diceva «1 fuori» per quattro blocchi diversi: il capo dei
banditi, l'istigatore degli Elea, Siraha e Kuron. Sembravano quattro debiti e
invece erano due: il capo dei banditi e l'istigatore si dividono `:5713`
(「を渡した。」), Siraha e Kuron si dividono `:8218` (「手紙を預かった…。」). Prese
le coppie insieme, il perimetro si chiude da solo e non costa niente.

💡 *Un «1 fuori» non e' un costo finche' non si guarda DOVE sta l'altro sito:
se sta in un blocco che si stava per prendere comunque, e' zero.* Si vede solo
dando a `_85-blocco.py` due righe di partenza nella stessa invocazione.

### ⭐⭐ Il contraccolpo si misura sul TIPO di sito, e la catena si ferma da sola

Mizuki (`:8459`-`:8694`) aveva una firma condivisa: 「あげないよ」/«No way.», che
vive anche a `:12697`. E' una **voce di menu**, dentro il menu dei calzini di
Kuroya — 30 firme tutte inglesi. Preso anche Kuroya. Kuroya a sua volta
condivide 「！！」 con `:14528`, ma quella e' una **battuta**: renderla non
apre nessun menu a meta', e la catena si ferma li'.

💡 *La catena dei contraccolpi si propaga finche' incontra voci di menu, e si
ferma sulla prima battuta.* E' la ragione per cui conta il tipo di sito e non
il numero (85a).

### ⚠️ «Siraha» batte «Shiraha»: il nome buono e' quello della creatura

`chat.hsp:8237` e `:8238` scrivono «Shiraha»; `db_creature.hsp:88124` e
`db_card.hsp:8720` scrivono «<Siraha> the white cloth». E' la stessa persona, e
l'inglese di `chat.hsp` e' semplicemente incoerente con se stesso. Vale la
regola del **nome sulla mappa** della 85a, in versione generale: *quando due
punti di monte scrivono un nome in due modi, vince quello del posto che il nome
lo DEFINISCE* — la creatura, non la battuta che la nomina.

### ⭐ I soprannomi si tengono quando sono il perno della scena

`chat.hsp:12654`-`:12660` e' il riconoscimento fra Kuroya e Belphat, e la
battuta di mezzo (`:12656`) e' letteralmente *«quel modo di chiamarmi...»*: se
il soprannome sparisce, la scena non funziona. クロやん e ベルっち diventano
**«Kuro»** e **«Bel»**. ⚠️ `screen.hsp:1780` rende クロやん con «Kuroya» per
intero, e resta com'e': li' il soprannome non e' il punto, e' solo il modo in
cui Belphat lo chiama in una preghiera.

### ⭐ `_sex()` cade quando l'inglese non lo chiama

`chat.hsp:1249` (Orphe davanti al piedistallo) chiama
`_sex(cdata(CDATA_SEX, CHARA_PLAYER))` nel **solo ramo giapponese**: 「この" +
_sex(...) + "は」, cioe' «quest'uomo / questa donna». L'inglese dice «this one»
e non chiama niente. Si segue l'inglese, quindi la funzione cade, e `verifica`
lo permette perche' sottrae l'**unione** dei due rami. ⚠️ Non e' un caso di
morfologia inglese come `_s`: e' contenuto che l'inglese ha scelto di non dire.

### ⚠️ La divisione nuda dentro una concatenazione: rilanciato il banco

`chat.hsp:5846` chiede al giocatore un ventesimo del suo oro, e monte scrive
`" ... " + cdata(CDATA_GOLD, CHARA_PLAYER) / 20 + " ... "`, **senza
parentesi**. Rilanciato `scratchpad/_85-banco-cnvrank.py` sul motore vero: in
HSP la divisione nuda dentro una concatenazione da' lo stesso risultato di
quella fra parentesi. Copiare la forma di monte tiene il comportamento
identico, e non c'e' bisogno di «aggiustare» niente.

### ⭐ Il nonsenso si traduce come nonsenso

Le otto farneticazioni di CAIM il riccone folle (`:7283`-`:7306`) sono nonsenso
**voluto** in giapponese, e l'inglese di monte e' gia' una resa di quel
nonsenso. Si segue l'inglese riga per riga e non si «aggiusta» niente: le frasi
devono restare sconnesse. ⚠️ Ma il tetto vale lo stesso: due sforavano le
tredici righe della finestra, e sono state accorciate — `:7289` sfora **anche
in inglese**, quattordici righe.

### ⭐ Il participio che nessuna guardia vede, e i falsi positivi che lo circondano

`scratchpad/referti.py` gira su **tutto il dizionario**, non sul lotto, e
segnala sei participi accordati con un «sei». Cinque sono legittimi e uno era
un difetto vero, scritto nella 84a:

    :2973  Miral   «Vabbe', sei venuto fin quaggiu'»          <- DIFETTO, rifatto
    :3152          «dove sei finita, mamma»                   <- la mamma
    :6420          «Eurypides, dove sei finito?»              <- Eurypides
    :9498  Norne   «finalmente libero»                        <- Norne, CDATA_SEX = 0
    :16586         «se le fallisci la paghi cara»             <- modo di dire
    :22872         «te la sei cavata»                         <- modo di dire

💡 *Due dei cinque falsi positivi sono modi di dire, dove il femminile e' il
pronome fisso e non un accordo.* Il referto non sa distinguerli, e va bene
cosi': e' un referto da leggere, non una guardia. Ma il rapporto uno a cinque
dice anche perche' nessuno lo rilegge mai, ed e' il difetto della 85a.

### ⭐ Tre silenzi nuovi in `invariati.md`

`!!` (`:12725` e `:14528`), `... ...` (`:3843`) e `... ... ...` (`:3844`). I
due ultimi sono la seconda e la terza pausa della scena in cui Renton legge i
libri di Rachel prima di stracciarli, e allungano il silenzio aggiungendo
gruppi di tre punti ASCII, come monte. Il primo non e' un silenzio ma il suo
contrario — la reazione che non arriva a farsi parola — e vale per la stessa
ragione: dentro non c'e' nessuna parola.

---


## Tre blocchi che si tengono per mano, e una morfologia che nessuna sonda vedeva — 2026-08-22, ottantacinquesima

Tre lotti su `chat.hsp`, **336 rese**, dalle 1.831 alle 1.495. Erystia (107),
Gavela (118) e Sophia (111): non tre lotti scelti, **un lotto solo diviso in
tre**, perché due firme condivise li legavano.

### ⭐⭐⭐ Il contraccolpo di una firma condivisa si MISURA prima, non si scopre dopo

`perimetro-zona.py` sul blocco di Erystia (`:1962`-`:2369`) dice 107 firme e
**due** che vivono anche fuori:

    5030f2ed  「この戦いが終わったら結婚しよう」   :1989 Erystia · :7834 Gavela · :10102 Sophia
    2854feb5  「任務について」                     :2297 Erystia · :8130 Gavela

Tutte e due sono **voci di menu**, e tutte e due stanno in menu che Erystia
deve avere interi: saltarne una avrebbe reso bilingue il menu di Erystia, che
è esattamente ciò che `bilingui` esiste per impedire. Quindi il contraccolpo
era **certo**, non probabile: renderle accendeva una voce dentro tre menu
lontani, tutti in zone ancora inglesi.

💡 **La misura ha cambiato la decisione.** Prima di scrivere una riga si è
misurato quanto costasse chiudere i tre menu davvero — `_85-blocco.py`, che
prende il confine sulla graffa come `_84-parlanti.py` ma su un blocco qualsiasi
del file, anche fuori da `*chat_unique`:

    7795-8193  Dr. Gavela        120 da fare   3 fuori
    10022-10334 Sophia la Saggia 112 da fare   1 fuori

Con quel numero in mano la scelta non era più fra «renderla e sporcare» e
«saltarla e rompere», ma fra **tre lotti in un giorno** e una toppa
provvisoria. Si sono presi i tre lotti, e a fine sessione `bilingui` è tornato
a **zero**. ⚠️ Nel mezzo, però, è stato **tre**: fra il primo commit e il
terzo l'albero portava tre menu a metà. È il prezzo di lavorare per lotti, e
va scritto perché non sembri un difetto sfuggito.

⚠️ **La terza firma, `f9ce02f7`, non era un problema e sembrava il peggiore**:
「…」/`"..."` a `:7870` (menu di Gavela) e `:3842` (Renton). Non è una voce di
menu là dove esce fuori dal lotto — è un `chatMore` — e la resa è `...`, che
non cambia niente in nessuna delle due schermate. **La domanda giusta su una
firma condivisa non è «quante volte esce» ma «in che TIPO di sito esce».**

### ⭐⭐⭐ `cnvrank` è morfologia inglese, e la sonda del test non poteva vederla

`init.hsp:149`:

```hsp
#defcfunc cnvrank int cnvrank_rank
	if ( jp ) {
		return "" + cnvrank_rank      // 2
	}
	...
	return "" + cnvrank_rank + "th"   // 2nd, 3rd, 25th
```

È la desinenza ordinale inglese: lo stesso mestiere di `_s`, e per la stessa
ragione non passa **mai** da `lang()`. Ma non stava in `MORFOLOGIA_INGLESE`, e
il prezzo era già a schermo in **quattro rese italiane**:

    command.hsp:2911   «Arena EX: 3 vittorie  livello massimo 12th»
    main.hsp:4067      «Livello di sotterraneo piu' profondo: 25th.»
    map_user.hsp:2594  «Rango del museo: 2nd -> 3rd»
    map_user.hsp:2775  «Rango della casa: 2nd -> 3rd»

⚠️⚠️ **La sonda del test cercava la famiglia sbagliata.**
`test_nessuna_morfologia_inglese_sfugge_all_elenco` rilegge `init.hsp` e
raccoglie le funzioni i cui `return` sono **letterali nudi** (`return "s"`).
`cnvrank` non restituisce un letterale: **concatena l'argomento** col suffisso,
quindi la sonda le passava accanto senza vederla. La sonda ora riconosce anche
la seconda famiglia — *ramo `jp` presente, e letterale inglese nei `return`* —
e in tutto `init.hsp` `cnvrank` è **l'unica**: non è un buco, è *il* buco.

⚠️⚠️⚠️ **E c'è una seconda cosa, più grande.** Quelle quattro righe erano nel
dizionario da sessioni, e nessuna rete le rileggeva: `verifica --dizionario`
confronta le **firme** col sorgente (voci orfane, voci non ancora tradotte) e
non rilancia mai `controlla_voce` sulle rese già dentro. Quindi **una regola
nuova non si applica retroattivamente a nessuno**: vale solo per i lotti che
passeranno da lì in poi. Le quattro righe si sono trovate solo perché la 85ª
aveva bisogno di scrivere una resa con `cnvrank` dentro. Resta aperto.

💡 **E la resa senza `cnvrank` ha chiesto il banco.** Togliendo la funzione
l'argomento va concatenato nudo, ma due dei quattro siti passano
un'espressione (`cnvrank(rankorg / 100)`) e **HSP non ha precedenza fra gli
operatori**. `scratchpad/_85-banco-cnvrank.py` con `hsp3cl` in dieci secondi:
`"x: " + (rankorg / 100)` dà `3`. Le parentesi reggono.

### ⭐⭐ Il divieto di genere sul giocatore è la regola che nessuna rete vede

Nei tre lotti sono state riscritte **ventiquattro** rese già scritte, tutte per
lo stesso motivo: un participio o un aggettivo che si accorderebbe col
giocatore, di cui non si conosce il sesso. `verifica` non ne vedeva nessuna —
erano tutte italiano corretto.

    «sei diventato cenere»        →  «di te è rimasta cenere»
    «Ridotto in quello stato»     →  «Col corpo a pezzi»
    «Oh, sei venuto»              →  «Oh, eccoti qui»
    «Non rischi di restare bloccato» → «Non c'è pericolo che tu non possa più muoverti»
    «Bravo, aspetta un attimo»    →  «Ottimo lavoro, aspetta un attimo»
    «...Sei tornato tutto intero» →  «...Ce l'hai fatta»
    «finirai reclutato»           →  «l'esercito verrà a reclutare anche te»
    «Il prototipo su cui sei arrivato» → «Il prototipo che ti ha portato qui»
    «sei stato scelto come Fattore Decisivo» → «la scelta del Fattore Decisivo è caduta su di te»
    «sei fatto così, allora»      →  «sei quel genere di persona»
    «Maniaco.»                    →  «Vergognati.»
    «te ne sei accorto»           →  «l'hai già notato»

💡 Le due scappatoie che funzionano quasi sempre: **il nome comune femminile**
(«sei la **persona** giusta», «sei quel genere di **persona**») e
**l'imperativo** («Vergognati», «Fa' attenzione»), che di genere non ne ha.

⚠️ E **la stessa regola, per il motivo opposto, su Enthumesis**: il dio del
caos è 両性具有, e l'inglese lo nomina col «they» singolare. Là non si tratta
di *non sapere*, si tratta di *sapere che sono due*: la resa non le dà mai un
genere e riscrive le frasi che ne chiederebbero uno.

### ⚠️ L'inglese che sbaglia riga, la terza volta, e stavolta sono TRE righe uguali

`chat.hsp:2184`, `:2190` e `:2199` (Erystia) portano **tutt'e tre lo stesso
inglese**, che è la riga di `:2205`:

    "Do not forget to arrive at Mayroon, please contact me through the informer."

I tre giapponesi non c'entrano niente fra loro: uno dice di continuare
l'indagine sul continente fluttuante, uno chiede che cosa sia successo durante
la traversata, uno reagisce alla risposta. Le firme sono **tre**, perché la
firma è giapponese *più* inglese, quindi ognuna può avere la sua resa — ma il
metro dell'inglese, per quelle tre righe, non vale niente: anche il confronto
delle **righe di finestra** che fa `chat-lotto-misura.py` diventa senza senso,
perché confronta con una frase che non è la loro.

Le altre deroghe della sessione, tutte per taglio dell'inglese:

* **`:2125`** — l'inglese perde *perché* bisogna sbrigarsi (Marka non dà retta
  a nessuno e potrebbe partire da sola).
* **`:2328`** — l'inglese perde **dove sta** il Castello Antico (nel bosco a
  sud di Vernis) e che è diventato un covo di fuorilegge.
* **`:2330`** — l'inglese inventa («he'll devour you like a dog») e perde che
  Wynan è 生粋の戦士; il giapponese dice che serve resistenza all'oltretomba
  **o** un modo di tenerlo a distanza.
* **`:2340`** — l'inglese non dice che lì dorme la `<pietra magica del folle>`,
  che è la ragione per cui il giocatore ha aperto quel menu.
* **`:8146`** (Gavela) — l'inglese taglia la seconda metà: «se vuoi continuare
  ad andare all'avventura a modo tuo, sta' attento a non farti inghiottire né
  dalle rovine né dall'esercito».
* **`:8163`** — l'inglese perde che **l'esercito ha deciso di abbandonare** la
  fortezza, che è il motivo per cui il lavoro tocca a un avventuriero.
* **`:8169`** — ⚠️ il più grave: l'inglese taglia **l'istruzione della
  missione**. Il giapponese dice «vammele a strappare, tutte e sei»; l'inglese
  dice solo «I want to study <Exossil> The Chaos Wing».

### ⚠️ Il tetto dei menu a due colonne si misura sulla forma DEGRADATA

Sei voci di menu passavano `verifica` e sforavano il tetto di 24 di
`menu_dialogo` a due colonne, e la ragione è che il tetto si conta **dopo**
`applica`: nel dizionario si scrive `è`, a schermo esce `e'`, e ogni accento
costa **due** caratteri invece di uno. «Non c'è da preoccuparsi.» sono 24 nel
dizionario e **25** a schermo.

### 💡 Il registro di una zona si legge, e stavolta l'ha dettato il diario

`text.hsp:9700`-`:9840` è il diario delle missioni della catena principale, ed
era **già tutto reso**. Non era una fonte di consultazione: era un vincolo.
Ha deciso «tesoro segreto di Lesimas» (dove l'inglese di Erystia dice
`<codex>`), «orsa d'argento» (femminile, perché Marka è una donna), «lettera di
presentazione», «Nave Divina», «Torre Rovente», «Castello Antico», «grotta dei
morti», «pietra magica del saggio / del folle / del conquistatore», «il
valico», «Irva Perduta». ⭐ **Il lotto è stato scritto leggendo prima il
diario del giocatore, non il glossario.**

### ⚠️ Il decimo menu rotto in inglese, e che cosa significa che siano dieci

`chat.hsp:1988` — «I want to be remembered, not just another name in a history
book.», 65 caratteri in un riquadro da 58 — è la quinta voce che entra
nell'elenco dei difetti di monte, e la quinta volta è entrata **il giorno in
cui l'abbiamo tradotta**: `voci_di_menu()` legge il dizionario, e una voce che
non abbiamo toccato non la misura nessuno. 💡 Cinque su cinque: **la rete non
misura il gioco, misura quel che abbiamo toccato.** Finché una zona resta
inglese, i suoi difetti di monte restano invisibili — e il numero «dieci» non
dice quanti ce ne sono, dice quanti ne abbiamo incontrati.

---

## Nove lotti di dialogo, e tre modi in cui monte tratta la stessa riga — 2026-08-22, ottantaquattresima

Nove lotti su `chat.hsp`, 301 rese, dalle 2.132 alle 1.831. Nessuno strumento
toccato: la sessione è stata tutta lessico, perimetri e grammatica. Quel che
resta, però, vale più delle rese.

### ⭐⭐⭐ Il perimetro di un lotto si prende sul PARLANTE, ed è uno strumento

La 81ª l'aveva scoperto sul caso di Telhureza: un'etichetta HSP è un indirizzo
di salto, non un confine di senso. Questa sessione l'ha reso meccanico.
`scratchpad/_84-parlanti.py` legge `*chat_unique` e per ogni blocco
`if ( _switch_val == CREATURE_ID_... )` trova la **graffa che lo chiude**,
conta le firme non tradotte dentro e quante di quelle vivono anche fuori.

⚠️ E il conto delle graffe deve togliere anche i commenti `//` e `/* */`, non
solo i `;`: `chat.hsp:1466` ha un `{` dentro una riga commentata, e con quello
dentro tutti i blocchi dopo `:1460` collassano in uno solo che arriva a fine
file. Il primo referto diceva «7 blocchi»; i blocchi sono **86**.

⚠️ La prima cosa che ha trovato è che il confine di **Mizuki** che la ripresa
portava dalla 79ª era sbagliato di 171 righe: il blocco comincia a `:8459`, non
a `:8630`. Quarantacinque firme che si credevano di `*chat_unique` sono sue.

### ⭐⭐⭐ La stessa riga, tre rapporti diversi fra giapponese e inglese

Tre volte in una sessione, e ogni volta la firma decide da sola che cosa fare.

**Un giapponese, tre inglesi** (Silvia, `:6341` `:6382` `:6423`). La stessa
identica esclamazione 「えっ。」 sta in tre punti, e monte la rende «Hmph.»,
«Forget it...?», «Huh?». Sono tre firme distinte — la firma è la coppia — e
vanno rese diverse: lì l'inglese non traduce un suono, interpreta un contesto.

**Due giapponesi, un inglese** (Icolle, `:4360` e `:4741`). Due frasi diverse
sul progresso della scienza diventano tutt'e due «Sacrifice is inherent to the
advancement of science~». Due firme, due rese, e la differenza la detta il
giapponese.

**Un inglese che non c'entra niente** (`:2747` di Garok, `:7648` della pianta
Meshera). L'inglese è un copia-incolla di un'altra riga, o di un altro posto.
Si segue il giapponese — ma ⚠️ `:2747` ha insegnato che quel che si butta via
è il TESTO sbagliato, non il DATO che la riga porta: `verifica` ha respinto la
prima stesura perché aveva lasciato cadere `itemname(ci)`, e aveva ragione.

### ⭐⭐ L'ECO: due righe che si scrivono insieme o non funzionano

Tre volte, in tre lotti diversi:

    :7463 / :7484        Lune    la voce di menu che lei CITA fra virgolette
    :6378 / :6382        Silvia  la voce di menu che lei RIPETE come domanda
    :8346 :8347 / :8351  Eila    le due voci in finto parlare da samurai, e lei
                                 che ci va dietro con lo stesso でござる

Nessuna rete le vede. Se si traducono separate, la citazione non cita più
niente. ⚠️ E la terza è anche una deroga: l'inglese ha buttato via il でござる
tutt'e tre le volte, e senza quello la battuta di Eila non ha più un
riferimento.

### ⭐⭐⭐ Una firma condivisa non si accorcia: si ALLARGA il lotto

`:3499` (Rilian) e `:7217` (Naive Kyle) sono la stessa voce di menu,
「まかせて」/«Leave it to me.». Renderla per Rilian avrebbe messo un menu
**tutto italiano** dentro una schermata inglese — e `bilingui` non l'avrebbe
visto, *ed è giusto che non lo veda*: quel menu ha due voci sole e l'altra è
`strbye`, già resa, quindi il gruppo non è bilingue. È il difetto della 79ª in
una forma che nessuna rete misura. La risposta è stata prendersi anche Kyle.

Stessa logica, in piccolo, per le cinque righe rosse «Required Fame: N»
(`:1366`, `:3590`, `:3876`, `:3936`, `:8341`): cinque firme diverse perché
cambia il numero, ma **una sola etichetta di sistema**. Renderne una avrebbe
fatto leggere allo stesso giocatore la stessa riga una volta in italiano e una
in inglese.

### ⭐⭐⭐ La `lang()` che è una CHIAVE, vista dalla faccia buona

`chat.hsp:7662` e `:7693` sembrano nomi da tradurre e invece sono chiavi: il
codice fa `strmid(cdatan(CDATAN_NAME, tc), 0, strlen(evold)) == evold` e, se
combacia, riscrive il nome della creatura dopo il finale. `evold` deve essere
**esattamente** il nome che `db_creature.hsp` dà a quella creatura.

In italiano combacia — tutt'e due dicono «<Milos> del Mondo Dimenticato» —
perché una sessione vecchia le aveva rese uguali senza sapere di scrivere una
chiave. ⚠️⚠️ **In inglese non combaciano affatto**: `db_creature.hsp:91226`
dice «<Milos> Of The Forgotten World», `chat.hsp:7662` dice «<Miros> hail flom
Erusia» — altro nome e due refusi. Nella build inglese quel rinomino è codice
morto. In italiano funziona, come in giapponese.

È la 81ª girata: lì una resa aveva rotto il gioco (`fix_wish`), qui una resa lo
ripara.

### ⭐⭐ Il registro e la deroga si EREDITANO, e tre volte hanno deciso loro

- **Mia la finta ingenua.** L'inglese le ha rifatto la voce da capo (finto
  inglese pieno di «nyah», una parodia di *Nobody knows the trouble I've
  seen*), ma `db_creature.hsp:121290` ha già le sue battute rese dal
  **giapponese** e `db_card.hsp:14286` rende 猫かぶり «la finta ingenua», cioè
  l'idioma e non il gatto letterale che l'inglese ha visto nel nome. Il
  personaggio italiano esisteva già.
- **Il Cane poliziotto.** In giapponese parla con であります e ワン attaccato ai
  verbi; `db_creature.hsp:96598` gli fa già dire «Alt! Un altro passo e sparo,
  bau!». Il tic è quel «bau!».
- **Arnord, `:3684`.** L'inglese dice «I'll tell the Palmian army to begin a
  steady retreat», il giapponese «appena la ritirata sarà completa ti farò
  avvisare» — e `text.hsp:10325`, già reso, dice «A ritirata compiuta arriverà
  l'avviso». Qui la deroga non è stata scelta: è stata **imposta** da una resa
  vecchia. Una riga di dialogo non può contraddire il diario che la annota.

### ⚠️ Il genere, e quante forme diverse vuole

Nel lotto dell'esercito si è presentato **cinque volte** e ogni volta ha voluto
una parola diversa: «the bravest of the brave» → «il coraggio in persona»,
«coward» → «ti manca il fegato», «once you've prepared» → «quando sei in
ordine», «your heroic figure» → «il tuo valore», «you made it back alive» → «da
quel massacro si potesse tornare».

⭐ E in un lotto solo (Silvia) i **bersagli** erano tre e la risposta diversa
per ognuno: `:6347` parla del giocatore (niente accordo), `:6352` del compagno
portato — di cui il codice guarda solo `sdata(SKILL_ATTR_CHA, rc)`, quindi può
essere chiunque — e `:6393` di Eurypides, che è un uomo, e **lì l'accordo si
fa**.

⚠️ «adventurer» rivolto al giocatore non è «avventuriero»: il progetto ha già
la forma senza genere, «tu che vai all'avventura» (`chat.hsp:1469`, `:1595`).
E l'epiteto `cdatan(CDATAN_AKA, CHARA_PLAYER)` non regge articoli: la forma che
tiene è l'apposizione, «ma tu sei X **in persona**!».

⭐ **Due sessi controllati prima di scrivere, e tutt'e due servivano**: Milis è
donna (`cdata(CDATA_SEX) = 1`, e il diario già reso dice «devo tornare a
parlarLE»), Gavela è uomo (`= 0`, come dice il giapponese 「白衣を着た男」 e come
il nome di carta «l'ingegnere capo» non diceva). È la regola della 82ª.

### ⚠️⚠️ Due reti danno lo stesso falso positivo: contano le voci di un menu senza leggere le guardie

Successo in un giorno solo, su due strumenti diversi:

- `chat-lotto-misura` ha visto **13 bottoni** dove ce ne stanno **9** (i
  materiali di Garok: 37 `chatList` dietro a guardie sul giorno che si
  escludono a vicenda, otto per classe al massimo);
- `menu_dialogo` ha applicato il tetto delle **due colonne** (24 caratteri, che
  vale solo sopra le dieci voci) a menu che di voci ne mostrano al massimo
  quattro, perché le `chatList` in testa stanno dietro a guardie mutuamente
  esclusive.

Nessuno dei due è un guasto: sono **tetti prudenti applicati a un conteggio che
non legge le condizioni**. Le rese sono state accorciate lo stesso — costa poco
e tiene le reti a zero — ma la correzione vera è leggere le guardie, e non è
stata fatta.

### ⚠️ Una nota di igiene che è costata un giro

Le rese accorciate di un lotto erano finite in uno script tampone a parte:
rilanciare il file del lotto le avrebbe disfatte **in silenzio**. Sono state
riportate dentro il file del lotto e il tampone è stato tolto. *Il file del
lotto è l'unica fonte: se una correzione sta altrove, la prossima sessione che
lo rilancia riapre un difetto già chiuso.*

---

## Il buco dei nomi non identificati, e la lezione che non era quella che sembrava — 2026-08-22, ottantatreesima

`db_item.hsp` ha **260 blocchi a sei righe** che nessuna rete vedeva: il nome che
l'oggetto porta **prima di essere identificato**. La 82ª l'aveva trovato e
l'aveva descritto bene — «articolo e plurale sono per `ITEM_ID` e appartengono al
nome identificato, serve una toppa e non solo una regola in più» — e su quello
aveva ragione. Ma la lezione vera della chiusura è **un'altra**, e sta qui.

### ⭐⭐⭐ L'astrazione inglese non era una perdita: era un ruolo grammaticale

Delle 216 stringhe, una ventina sembravano inglese sciatto. «godly powers»,
«unknown content», «a fishy figure», «blue color», «inflicting suffering»,
«a barrel-size»: nessuna di queste è un nome di oggetto, e il giapponese accanto
ce l'ha sempre — 神々しい宝石 *gemma dall'aria divina*, 謎の箱 *scatola
misteriosa*, 苦しみを呼ぶ薬 *medicina che chiama la sofferenza*.

La prima stesura le ha rese come nomi pieni, dichiarando una deroga di famiglia:
*l'italiano ha bisogno di una testa nominale, perché il nome sta dietro un
articolo che il codice antepone, e «un infliggere sofferenza» non è una frase*.
Il ragionamento era buono. **Era anche sbagliato**, e a dirlo è stato il
sorgente.

`item_func.hsp:1217` prende la parola-contatore da `ioriginalnameref2`
**senza guardare `INV_ITEM_KNOWN`**, e `:1259` la stampa. Cioè: su un oggetto
composto il giocatore legge la parola-contatore **anche quando l'oggetto non è
identificato**. «a **statue of** deity of Irva», «a **high potion of**
inflicting suffering», «a **bottle of** clear liquid». Quelle stringhe non sono
nomi: sono **complementi dopo «of»**, e in quel ruolo l'inglese è perfetto.

⚠️ **E le 21 firme che stanno in quel ruolo sono esattamente quelle che
sembravano astratte.** Non è una coincidenza da leggere a posteriori: si misura
in tre righe di Python — sono le firme i cui oggetti hanno **tutti** un
`ioriginalnameref2` pieno. 201 firme stanno solo su oggetti semplici, 21 solo su
composti, 2 su tutt'e due (e quelle vogliono una resa che regga i due telai:
«carta sbrindellata» sta bene sia da sola sia dopo «gettone di»).

Con le rese-nome il gioco avrebbe scritto **«una statua di statua di divinità»**,
**«un libro orribile di libro orribile»**, **«una scatola di scatola
misteriosa»** — otto ripetizioni su 260. Nessuna rete le avrebbe viste: sono
italiano corretto, stanno nei tetti, non sono bilingui. Le ha viste un **banco**
(`scratchpad/_83-banco-nome.py`) che legge la build e stampa tutti e 261 i nomi
**come usciranno a schermo**, articolo e parola-contatore compresi.

💡 **La regola**: *prima di decidere che l'inglese ha perso qualcosa, si guarda
in che RUOLO la stringa finisce.* È la sorella della 57ª — *quando i due rami
non dicono la stessa cosa decide il sito* — spostata dal contenuto alla
sintassi: qui i due rami dicevano la stessa cosa, e a non dirla ero io.

⚠️ Ed è anche la 61ª (*misura la cosa, non una cosa vicina*) applicata a una
**lettura**: «questa stringa sembra un nome» è una cosa vicina; «questa stringa
finisce dietro `s2 + " di "`» è la cosa.

### La stessa distinzione, nel codice: due guardie e non una

L'articolo non basta accenderlo con una spia. `locvar_itemname_ignoto` dice che
il nome scritto è quello non identificato, ma su un oggetto composto la **testa**
del sintagma resta la parola-contatore, e l'articolo lo regge lei. La seconda
guardia è `locvar_itemname_s2 == ""` — **la stessa del plurale**, che ce l'aveva
già dalla 8ª sessione e a cui non avevo pensato di chiedere.

Percio' l'array del nome identificato è il **default** e quello del nome non
identificato lo scavalca solo dove la testa è davvero lui.

### ⭐⭐ Il plurale sbagliato qui non è grammatica: è uno SPOILER

Il caso che ha reso ovvio che gli array dovevano essere propri e non condivisi:
`ITEM_ID_WAKE_UP_OF_NEFIA` da non identificato è «una gemma nera di poteri
divini»; il suo `ioriginalnamerefplur` dice «Risvegli di Nefia». Se il ramo non
identificato avesse pescato lì, **due** di quelle gemme si sarebbero chiamate
col nome vero dell'oggetto. Il plurale avrebbe svelato quel che
l'identificazione nasconde — non un errore di accordo, un difetto di gioco.

### Il caso che il dizionario non può raggiungere

⚠️ Una riga su 261 sta **fuori** da ogni `if ( jp )`:
`iknownnameref(ITEM_ID_DRAGONS_RED) = "red color"`, letta da tutt'e due le
lingue. È un difetto di monte — quella riga dice «red color» anche al giocatore
giapponese, mentre gli altri 260 un giapponese ce l'hanno — e tradurla
cancellerebbe il gioco in giapponese. `estrai` la **scarta apposta**, con un
test che lo dice; la prende una toppa che il blocco lo costruisce, lascia intatto
il ramo giapponese col suo difetto e dà all'italiano il suo. 💡 *Una scansione
che scarta un sito deve dichiararlo, o il sito diventa invisibile due volte.*

### ⚠️ Due lezioni di contorno, tutt'e due su reti che si sono mosse da sole

1. **`GIUDICATI` di `maiuscole.py` è una coordinata nella BUILD, e la build la
   muoviamo noi.** Il permesso di `item_func.hsp:2321` è morto perché le toppe
   di oggi infilano 31 righe più su nello stesso file: il sito è **intatto** e si
   è mosso il pavimento. È una causa nuova — le tre volte precedenti era il sito
   a essere cambiato — e `test_i_giudicati_esistono_ancora` l'ha presa lo stesso.
   *Un test che scatta per la ragione giusta con la causa sbagliata è comunque
   un test che funziona.*
2. **`collaudo/schermo.ps1` scrive sulla tastiera di tutto il computer.**
   `keybd_event` imposta lo stato **globale**: battendo `wizard` nella console
   del gioco, le sei lettere sono finite nel prompt di un'altra sessione di
   Claude Code aperta sulla stessa scrivania, che ci si è ritrovata scritto
   «fallwliziard». `SetForegroundWindow` chiamato da un processo che non ha il
   fuoco Windows lo **ignora**, e il pilota non se ne accorge: l'unico segnale è
   il gioco che risponde «Unknown command». Il collaudo l'ha fatto una persona,
   ed è la scelta giusta finché il computer è di qualcuno.

---

## Due funzioni dello stesso modulo, in disaccordo sulla stessa espressione — 2026-08-21, ottantaduesima

`chat.hsp:18813` è `"(" + cnven(he(tc)) + " nodded shyly.)"`, e **nessuna resa
italiana poteva passare `verifica`**.

Il perché sta in `strumenti/funzioni.py`. `he(tc)` a **un** argomento è
morfologia inglese: va tolta, e il progetto lo sa dalla Fase 1. Ma sopra ci sta
`cnven`, che `funzioni_di_contenuto` registrava fra le **attese**. In italiano
la frase comincia con un verbo scritto per esteso — «(Annuisce, con aria
imbarazzata)» — quindi non c'è né il pronome né niente da capitalizzare: la
lista delle attese conteneva un nome che nessuna resa corretta poteva
contenere. È la stessa forma del difetto di «Manuscript production» prima della
maschera dei letterali: *una guardia che rende una voce intraducibile non sta
misurando, sta sbagliando*.

⭐ **E il modulo la risposta ce l'aveva già scritta.** `TRASPARENTI` esiste dalla
72ª, con questa definizione: «chiamate che non portano NESSUN dato: aggiungono
solo punteggiatura intorno a quello che ricevono. Vanno **attraversate** invece
che registrate». `cnven` (`init.hsp:191`) fa esattamente questo — in build
giapponese restituisce l'argomento tale e quale, altrimenti ne alza la prima
lettera — ma stava fuori dall'insieme. ⚠️ **E c'era di peggio**: `_classifica`
la classe `TRASPARENTI` **non la conosceva affatto**, quindi
`funzioni_di_contenuto` registrava `cnvtalk` mentre `chiamate_di_contenuto` la
saltava. Due misure della stessa cosa nello stesso modulo, in disaccordo, e
nessun test le confrontava.

✅ `cnven` entra in `TRASPARENTI` e `_classifica` impara la classe. Tre test
nuovi, fra cui uno che verifica che le due funzioni **siano d'accordo** su ogni
trasparente.

⚠️ **Lasciar cadere `cnven` non allenta nessuna guardia**, ed è la ragione per
cui la correzione è sicura: la maiuscola ha una rete tutta sua,
`strumenti/maiuscole.py`, che legge la **build** e giudica ogni sito per
posizione (in testa / appeso / accumulato). Le due misure non si sovrappongono
— una guarda che il **dato** sopravviva alla traduzione, l'altra che la
**maiuscola** cada nel posto giusto — e pretenderle tutt'e due dalla stessa
lista rendeva impossibile la resa giusta.

💡 Sul sorgente pinnato `cnven(he(...))` compare **16 volte**. Non era un caso
limite: era la prima volta che un lotto ci passava sopra.

⚠️ **E la correzione ha fatto scadere un permesso.** `chat.hsp:18813` stava in
`GIUDICATI` di `maiuscole.py` con la motivazione «chat.hsp non è ancora
tradotto: si giudica quando ci arriva il lotto». Il lotto è arrivato, la resa ha
fatto sparire il `cnven`, e il sito appeso **non esiste più**: l'eccezione si
toglie, non si aggiorna. L'ha detto `test_i_giudicati_esistono_ancora`, ed è la
**terza** volta (le prime due nella 77ª). *Un elenco di eccezioni è un debito.*

---

## Il registro di un personaggio si legge, non si decide — 2026-08-21, ottantaduesima

Il lotto degli otto dei che si possono invitare a casa (27 rese) non ha deciso
**nessun** registro, e la ragione vale come metodo.

`main.hsp:7201`-`:7229` è la scena in cui il dio invitato **arriva** a casa:
otto righe, una per dio, tutt'e otto già rese in una sessione vecchia. Lì c'è
scritto che Ehekatl fa «Miaaao! Granchio reale! Dov'è il granchio reale?», che
Opatos fa «Muahahaha! Uahahaha! Permesso, entro!», che Kumiromi chiede «Posso...
guardare in ogni angolo...?», che Mani dice «Ecco dunque la dimora di un
mortale. Ne prendo nota.». Il lotto di oggi è l'**invito** che accende quella
scena.

⭐⭐ **Cioè: era una schermata inglese che portava a una destinazione italiana** —
il difetto della 79ª (una schermata italiana che porta a un sottosistema
inglese) **girato**. E si trova con la domanda gemella: non «dove porta questa
voce che ho già reso» ma «**da dove arriva** questa voce che sto rendendo».

⚠️⚠️ **E quelle otto righe erano state rese seguendo il GIAPPONESE**, perché lì
l'inglese di monte è rotto: `main.hsp:7213` dice «Wheeee! I'm so happy. I like
you!» dove il giapponese dice 「たらばがに！」. Quindi la deroga non è una scelta
di oggi: è **di famiglia**, già presa, e si eredita. Nel lotto morde due volte —
`chat.hsp:6120`, dove l'inglese butta via 「**前の**エヘカトル」 (e le generazioni
degli dèi sono lore vera, `chat.hsp:16502` racconta il primo Tezcatlipoca), e
`:6123`, dove l'inglese fa di Ehekatl l'**ospite** invece dell'invitata.

💡 *Prima di decidere come parla un personaggio, si cerca dove parla già.*

---

## La stessa creatura con tre nomi, e una battuta bruciata — 2026-08-21, ottantaduesima

Monte chiama えっちな妹 e 『Ｈな妹』 **tutt'e due** `<H sister>`: due creature
diverse, un nome solo. L'italiano le distingue — «la sorella minore maliziosa»
e «la sorella minore sicaria» (`db_creature.hsp:91326` e `:97006`,
`db_card.hsp:9214` e `:10137`) — ed è un miglioramento su monte.

⚠️ Ma `chat.hsp:6505`, l'incarico che manda a stanarla, diceva «una **H
Sister**»: **tre** nomi per la stessa creatura in due file, e il giocatore che
va a cercare una «H Sister» incontra «la sorella minore sicaria». ✅ Il dialogo
adesso dice **«sorella H»** dappertutto, e `:6505` è stata corretta.

🔶 **Ma resta una decisione aperta, e non è di lessico: è di tempo comico.** La
battuta finale di quella creatura è `:6717`, «la H sta per hentai, ma io
preferisco **hitman**!». Il nome italiano dice «sicaria» **dall'inizio**: la
rivelazione arriva quando il giocatore l'ha già letta sulla scheda. Le strade
sono tre — tenere «sicaria» e perdere la battuta, rinominare la creatura
«sorella H» e perdere la distinzione da えっちな妹, o rinominarla con un epiteto
che non sveli il mestiere. ⚠️ Nessuna si sceglie senza guardare le due schede a
schermo.

💡 *Una resa può essere giusta parola per parola e sbagliata nel momento in cui
arriva.*

---

## Il nome che l'oggetto porta PRIMA di essere identificato non lo vede nessuna rete — 2026-08-21, ottantaduesima

Cercando come rendere 「光玉」 di `chat.hsp:16430` («I don't have any god
jewels») ho guardato, come vuole la regola del DATO, il nome dell'oggetto in
`db_item.hsp` invece della stringa. E il nome non c'era: `iknownnameref` non è
nel dizionario, e nella **build** dice ancora `"god jewel"`.

Non è un caso isolato. `db_item.hsp` ha **261 righe `iknownnameref` col ramo
inglese**, per **217 stringhe distinte**: «god jewel», «clear liquid»,
«godly powers», «book», «tonfa», «some kind of ticket», «crumbling paper»,
«strange jewel». Sono i nomi che l'oggetto mostra finché
`inv(INV_ITEM_KNOWN, …) == ITEM_KNOWN_NONE` (`item_func.hsp:1533`) — cioè
**ogni pozione, ogni pergamena e ogni bacchetta appena raccolta**.

⚠️⚠️ **Il buco è nel perimetro dell'estrazione, non nella traduzione.**
`estrai.py` conosce due tipi di sito: `lang(jp, en)`, e il blocco a **sette**
righe di `contratto-nomi.md` §1, che pretende `ioriginalnameref` in tutte e
quattro le assegnazioni. `iknownnameref` sta in un blocco a **cinque** righe e
non lo aggancia nessuna delle due regole. Quindi `estrai db_item.hsp` dà 1.607
voci e nessuna di quelle 217: *il numero non è sbagliato, il numero non c'è*.
È la forma della 74ª, sul secondo tipo di sito invece che sul primo.

⚠️⚠️⚠️ **E allargare la regex non basta**, ed è la parte non ovvia. Il nome
non identificato entra nella pipeline in **alternativa** a quello vero
(`item_func.hsp:1533`-`:1535`), ma articolo e plurale sono per **ITEM_ID** e
li ha scritti `applica.py` per il nome **identificato**: la `l'` di
`ioriginalnamearticolodet(ITEM_ID_MAGIC_CANCELER)` è l'articolo del nome vero,
non di «gioiello divino». Un nome non identificato tradotto è **un altro
sostantivo, con un altro genere e un altro plurale**, e gli array
`iknownnamerefplur` / `iknownnamearticolo` **nel motore non esistono**
(`grep`: zero occorrenze). Quindi la strada è: estendere `estrai`/`applica` al
blocco a cinque righe **più** una toppa che dia al ramo non identificato i
propri array. 💡 *Un nome che si legge in due stati è due nomi, e la grammatica
italiana lo sa anche quando il motore inglese non lo sa.*

🔶 **Aperto**: 217 stringhe, e la decisione se pagare il costo del motore.

---

## Il lessico di Leold si riprende dal codice, quarta prova della regola della 79ª — 2026-08-21, ottantaduesima

I due lotti della Culla del Caos (148 rese) non hanno **deciso** quasi niente:
il lessico del finale era già scritto altrove, e si trova cercando il **dato**.

| dove | che cosa dava |
|---|---|
| `action.hsp:3008`, `chat.hsp:18111` | 神の間 → **«Sigillo Eterno»** |
| `main.hsp:7083` | 決戦因子 → **«Fattore Decisivo»** |
| `chat.hsp:16006`, `main.hsp:5080` | 来光の牙 → **«zanna della luce nascente»** |
| `db_card.hsp:2727`, `db_creature.hsp:52175` | 混沌の超児 → **«Il Figlio del Caos»** |
| `db_race.hsp:5553`, `chat.hsp:9503` | 化身 → **«incarnazione»** |
| `action.hsp:18565` | 獣爪兵 → **«il soldato artiglio»** |
| `db_item.hsp:140704` | 覚醒の宝玉 → **«Risveglio di Nefia»**, e il tipo è **«gemma nera»**, femminile |
| `db_item.hsp:140056` | ネフィアの核 → **«nucleo di Nefia»** |
| `skill.hsp:1056`, `chat.hsp:24416` | 衝撃波動 → «Onda d'urto», 混沌の渦 → «vortice caotico» |
| `chat.hsp:18590` | 一柱 → «una divinità» (quindi 八柱神 → «le otto divinità») |
| `command.hsp:17275`, `action.hsp:9515` | 記録 → «registrare», 束縛 → «costrizione» |

⭐ **E il dato ha deciso anche una concordanza:** `chat.hsp:16516` dice «This
gem», e in italiano bisogna sapere di che genere è. Non lo dice la stringa: lo
dice `ioriginalnameref2(ITEM_ID_WAKE_UP_OF_NEFIA) = "gemma nera"` con
`ioriginalnamearticolo = "una "`. Quindi «Questa gemma». 💡 *Il genere di un
oggetto è un dato del gioco, non una scelta del traduttore.*

---

## Orphe è uomo, e una resa vecchia lo faceva parlare al femminile — 2026-08-21, ottantaduesima

`screen.hsp:1388` diceva «È solo perché io non sono **stata** all'altezza». Ma
`db_creature.hsp:46159` mette `cdata(CDATA_SEX, rc) = 0`, e `text.hsp:378` dice
che **0 è maschio**; e i quattro epiteti di Orphe già resi sono tutti maschili
(«il principe del regno perduto», «l'apostolo del caos», «il servo del caos»,
«il prediletto del caos»). Corretta in «non sono stato all'altezza».

💡 È la 81ª (Scard, il vocativo di Oxode) una terza volta: **il sesso si legge
in `CDATA_SEX`**, e quando il codice nomina il personaggio l'accordo si fa — ma
si fa **giusto**. ⚠️ E il difetto non l'ha trovato una rete: è saltato fuori
cercando 決戦因子 nel dizionario. *Il lessico ripreso è anche un collaudo delle
rese vecchie.*

---

## Tre deroghe dichiarate, e due sono l'inglese che sbaglia la persona — 2026-08-21, ottantaduesima

1. ⚠️ **`chat.hsp:16126`** — l'inglese dice «I was originally meant to work
   **among the gods**», il giapponese dice 神の間, che in tutto il progetto è il
   **Sigillo Eterno** (il posto, non la compagnia). Chi ha tradotto in inglese
   ha letto 神の間 come «fra gli dèi». ✅ Si segue il giapponese e il lessico già
   fissato.
2. ⚠️ **`chat.hsp:16127`** — l'inglese dice «Now that **you've** regained your
   strength», ma il soggetto giapponese di 力を取り戻した è **Leold**: è lui che
   ha riavuto i poteri (lo dice la frase prima, `:16126`), e per questo adesso
   gli AP comprano più velocità e vigore. ✅ Si segue il giapponese. È la
   famiglia delle convenzioni: *l'inglese sbaglia la persona*.
3. ⚠️ **`chat.hsp:16585`** — l'inglese dice «party halls», il giapponese dice
   演奏会場, e la mappa si chiama «Sala concerti» (`map.hsp:5850`). ✅ Si usa il
   nome che il giocatore legge sulla mappa.

⚠️ **Una quarta, minore**: 「冒険者ギルド」/«Adventurer's guild» (`:16594`) non
aveva una resa. Coniata **«Gilda degli Avventurieri»**, sulla forma delle tre
che esistono già (Gilda dei Maghi / dei Guerrieri / dei Ladri).

---

## L'epiteto del giocatore non regge l'articolo, e allora si gira l'ordine — 2026-08-21, ottantaduesima

`chat.hsp:16472` è l'unica riga del progetto che concatena
`cdatan(CDATAN_AKA, …)` **e** il nome: «Good to see you here, `<aka>` `<nome>`».
L'epiteto italiano è un sintagma intero e senza articolo — la 77ª lo aveva già
misurato sul nome della casa — quindi «fragore della dipendenza Pippo» è
sgrammaticato, e mettere «il» davanti si romperebbe sul primo epiteto
femminile.

✅ Si gira nell'apposizione italiana, che l'articolo non lo chiede:
`"Bella impresa. " + nome + ", " + aka + ": qui prima di te non era arrivato
nessuno."` → «Bella impresa. Pippo, fragore della dipendenza: qui prima di te
non era arrivato nessuno.» 💡 *È la toppa 1017 senza toppa: l'ordine si può
cambiare perché l'espressione la scriviamo intera.*

⚠️ E la coda è cambiata per un secondo motivo: 一番乗り è «sei il primo», che
porta il genere. «Prima di te non era arrivato nessuno» dice la stessa cosa e
non lo porta.

---

## Quando l'etichetta e il codice non dicono la stessa cosa, vince il codice — 2026-08-21, settantanovesima

A Halloween un PNG bussa alla porta e il menu offre tre strade: dare un dolce,
oppure una delle due voci che monte ha chiamato **«Trick.»** e **«Treat.»**.
Tradotte come suonano — «Scherzetto» e «Dolcetto» — sarebbero state tutt'e due
sbagliate, perché in quel menu significano il contrario di quel che dicono.

Il codice non lascia margini (`chat.hsp:656`-`:728`):

- `chatList 2` è «Trick.», giapponese 「イタズラされる」, *farsi* fare lo scherzetto:
  chi la sceglie riceve **ventotto molotov** in faccia (`:699`-`:723`);
- `chatList 1` è «Treat.», giapponese 「イタズラする」, *fare* lo scherzetto: il PNG
  urla «Guardie! Guardie!» e il giocatore perde **due punti di karma**
  (`:726`-`:727`).

Quindi «Treat.» è la voce che fa perdere karma, e «Trick.» quella che si prende
la molotov. Il giapponese è coerente con gli effetti; l'inglese no.

✅ **Si segue il codice.** Le due voci diventano «Fare lo scherzetto» e «Farsi
fare lo scherzetto», sotto il `buff` «Dolcetto o scherzetto?». Il giocatore
italiano legge la scelta che sta per fare davvero.

⭐ **La regola generale, che questa e le altre due volte di oggi hanno la stessa
forma:** *quando i due rami di `lang()` non dicono la stessa cosa, il giudice
non è nessuno dei due — è quel che il codice fa dopo.* Era già successo nella
77ª (la riga giusta dell'evento sbagliato, `:8850`) e succede tre volte in
questa sessione: qui, con `name(cc)` che nomina il giocatore per un'azione del
compagno (`:21732`, `:21750`, `:21867`), e con le dodici battute che l'inglese
ha perso e sostituito con un segnaposto ripetuto.

⚠️ **E non è una rete: nessuna delle quindici confronta il testo con l'effetto.**
Si trova leggendo il codice del blocco *prima* di tradurre — che è la stessa
disciplina che la 74ª chiedeva per il perimetro.

---

## Il lessico di un sistema non si decide: si cerca dove il gioco lo stampa gia' — 2026-08-21, settantanovesima

Aprendo gli **evochat** c'erano dieci parole da scegliere: le dieci «route» in
cui il giocatore puo' portare il rapporto con un compagno («You've entered the
Comrade route!»). Sembrava una decisione di gusto — «via», «percorso»,
«legame», e poi dieci nomi. Non lo era.

Ogni `chatval` che stampa quel messaggio scrive anche
`cdata(CDATA_HEART_LOCK_RELATION, tc)`, e **quel valore sceglie una delle dieci
scale di rapporto** di `text.hsp:33`-`43` — `_impressiona1`-`7` e
`_impressionb1`-`3` — che sono gia' tradotte da sessioni e che il gioco stampa
in due punti che il giocatore vede subito dopo: sotto il ritratto nella
finestra del dialogo (`chat.hsp:25620`) e nel messaggio di
`chara_func.hsp:1080`, «Il rapporto con X diventa <Y>...».

Quindi la parola non era da scegliere: era da **trovare**. «Comrade route» e'
la via del **Compagno** perche' `_impressiona1` dice «Compagno»; «Owner route»
e' la via dell'**Appartenenza** perche' `_impressionb2` dice «Appartenenza» —
e li' la scala aveva gia' applicato, sessioni fa, la regola della guida di
stile sui rapporti («si rende il **legame**, non la persona»). Stessa cosa per
i due esiti dello scasso del cuore: i tratti che ne nascono si chiamano
«Nessun **cruccio**» e «**Passatempo pericoloso**» in `command.hsp:2502` e
`:2507`, e le due righe che li annunciano dicono adesso quelle parole.

⭐ **Come si trova la parola.** Non si cerca il testo: si cerca la **variabile**
che il codice scrive insieme al testo, e poi tutti i punti che la leggono. Qui
bastava `grep HEART_LOCK_RELATION` per avere in dieci righe l'elenco dei siti
che stampano il nome del rapporto. E' la stessa mossa della 78a con le voci di
diario delle prove di gilda, generalizzata: *se una resa nomina uno stato del
gioco, quello stato ha quasi sempre un nome gia' scritto da qualche parte, e la
via per arrivarci passa dal dato, non dalla stringa.*

⚠️ **E vale la pena farlo anche quando la resa sembra libera.** Nessuna delle
quindici reti avrebbe segnalato «Sei entrato nel percorso Cameratismo!»: e'
italiano corretto, sta nel tetto, non e' bilingue. Sarebbe stata solo una
schermata che chiama una cosa con un nome e la schermata accanto con un altro —
il difetto della statistica 発言力, «Influenza» in un posto e «autorita'»
nell'altro, che aspetta una decisione dalla 70a.

---

## Il perimetro di un blocco non si legge in `--da-tradurre` — 2026-08-21, settantottesima

`python -m strumenti.estrai <file> --da-tradurre` ancora una voce per **firma**
alla **prima** occorrenza. E' il comportamento giusto per la domanda a cui
serve — *quante rese restano nel file* — ma diventa una trappola appena si
usa per una domanda diversa: *che cosa manca in questa zona*.

In `*chat_default` (`chat.hsp:19870`-fine) l'elenco mostrava **77** voci. Le
firme non tradotte che hanno almeno un'occorrenza li' dentro erano **89**: le
dodici mancanti hanno la prima occorrenza altrove nel file, quindi il loro
rappresentante sta in un'altra zona e l'elenco della zona non le nomina.

⚠️⚠️ **Due delle dodici erano voci di menu**, e per questo il difetto non e'
accademico: 「ごめんなさい」/«Sorry.» vive nel menu della consegna (`:20811`) **e**
in quello della gatta Sinaha (`:10880`), 「ちょっと待って」/«Hold on.» in quello
della nave (`:23845`) **e** in quello della barca di Regulus (`:13590`).
Tradurre le 77 dell'elenco avrebbe chiuso la zona e aperto **due schermate a
meta'** in punti che nessuno stava guardando.

✅ **Il conto giusto**: firme non tradotte con **almeno un'occorrenza** nella
zona, ricavato incrociando l'estrazione completa (senza `--da-tradurre`) col
dizionario. In codice sono cinque righe, e vanno scritte **prima** di scegliere
il lotto, non dopo.

💡 E' la stessa specie di errore della 60a — una misura presa su un insieme
diverso da quello che si vuole misurare — e la stessa forma della 74a: *un buco
nel perimetro non produce un numero sbagliato, produce un numero che non c'e'.*
Qui pero' il numero sbagliato c'era, ed era plausibile: 77 invece di 89.

⭐ Nel lotto del tutorial la stessa cosa in grande: 「わかった」 sta in **sette**
menu lontani, cinque come «Alright.» e due come «Will do.», ognuno con la
sorella ancora inglese. Otto sorelle aggiunte al lotto, e `bilingui` ha dato
zero al **primo** giro — cosa che nella 77a non era mai riuscita.

---

## Una risposta italiana sotto un menu inglese e' il difetto girato — 2026-08-21, settantottesima

La 73a ha corretto in massa il difetto «il giocatore clicca italiano e riceve
inglese»: menu tradotto, risposta no. Nella 78a e' comparso il **rovescio**, e
va trattato allo stesso modo.

`*chat_default` conteneva tredici rese della famiglia **evochat**: le dieci
「…ルートに突入した！」 («You've entered the Comrade route!» e sorelle), i due esiti
del cuore a `:21732` e `:21750`, e il potere di scasso a `:21964`. Sono `txt`,
non voci di menu, quindi nessuna rete le lega a niente. Ma il menu che le
accende — `chat.hsp:19250`-`:19278`, dentro il blocco evochat — e' **ancora
tutto inglese**.

✅ **Restano fuori dal lotto**, e si faranno insieme al blocco evochat, quando
il menu e la sua risposta si potranno tradurre nello stesso giro.

⚠️ **Nessuna rete lo dice.** `bilingui` misura i gruppi di `chatList`: un menu
tutto inglese non e' bilingue, e una `txt` italiana non entra in nessun gruppo.
Il difetto si vede solo leggendo *da dove arriva* la riga che si sta per
tradurre — cioe' guardando il `chatval` che la seleziona e chiedendosi se la
voce di menu che lo produce e' resa.

💡 La stessa domanda ha invece **aperto** tre rese vicine: `:21386`, `:21417` e
`:21447` («You and X entered a world only for the two of you») stanno dietro
`<evochat>`, `<evochat in coppia>` e `<evochat oscuro>`, che la 73a ha gia'
tradotto. Li' il menu e' italiano e la risposta puo' seguirlo.

---

## In `*chat_unique` il lotto e' un sistema, non un parlante — 2026-08-21, settantottesima

`*chat_unique` e' uno smistamento `if ( _switch_val == CREATURE_ID_x )`, e la
memoria del progetto dice da tempo che *i lotti si raggruppano per chi parla*.
Vale, ma qui c'e' un taglio migliore: **il sistema**.

Le tre gilde sono **sei blocchi quasi identici** — Revlus/Fray/Sin maestri,
Lexus/Abyss/Doria guardiani — piu' i tre investigatori di Tyris del Sud
(Lenas/Naga/Ratin) che rifanno la stessa catena dall'altra parte del mare.
Nove parlanti, un lessico solo: gilda, maestro, guardiano, punti gilda,
obiettivo, addestramento del mese, consiglio. Presi insieme, il glossario si
decide **una volta** e le sei schermate parallele dicono le stesse parole.

⭐⭐ **E il glossario non si e' deciso: si e' ripreso.** Era gia' tutto scritto
altrove e nessuno lo aveva raccolto:

| termine | dove stava gia' |
|---|---|
| Gilda dei Maghi / dei Guerrieri / dei Ladri | `command.hsp:10621`-`:10627` |
| il maestro della Gilda dei Guerrieri | `text.hsp:11019` (e' Fray, ed e' donna) |
| il guardiano della gilda | `text.hsp:1094`, una domanda del quiz |
| l'investigatrice della gilda | `text.hsp:1358`, un'altra domanda del quiz |
| punti gilda | `text.hsp:10475`, la voce di diario |
| «Nefia casuali di tipo X di livello Y o piu'» | `text.hsp:10511` |
| «vendere refurtiva per N monete d'oro» | `text.hsp:10565` |
| «baule delle consegne», «libri antichi decifrati» | `text.hsp:10475` |

💡 Le tre prove d'ingresso adesso dicono **le parole del diario che le annota**:
il giocatore legge la prova dal guardiano e la ritrova identica premendo `j`.

⚠️ **Fray si accorda, la carica no.** `chat.hsp:5595` dice «call out to **her**»:
Fray e' donna e dice «sono davvero **contenta**». Ma resta «il **maestro** della
gilda», perche' e' la carica e `text.hsp:11019` l'aveva gia' fissata cosi'
parlando proprio di lei.

---

## Il tutorial nomina i menu con le parole di `text.hsp` — 2026-08-21, settantottesima

Il blocco di `chat.hsp:1701`-`:1879` non e' dialogo: e' il **tutorial**, la
prima cosa che un giocatore nuovo legge, e dice al giocatore quali tasti
premere e quali voci di menu scegliere.

✅ **I nomi non si traducono: si copiano** da `text.hsp:135`-`:136`, che il
progetto ha gia' reso — `<Mangia>`, `<Leggi>`, `<Scava>`, `<Equipaggia>`,
`Tiro`, `Raccogli`, `Posa` — e con loro `diario`, `zaino`, `pergamena di
identificazione`, `pergamena di purificazione`, `lingotto d'oro`,
`grimaldello`, `Scasso`, `bacheca della casa`, `baule degli stipendi`.

⚠️ Un tutorial che nomina i menu con parole proprie e' **peggio** che un
tutorial inglese: manda il giocatore a cercare a schermo una voce che non
esiste. E' l'unico posto del gioco dove la coerenza col lessico
dell'interfaccia non e' eleganza, e' funzionamento.

⚠️ **I tasti restano quelli**: `[g]et` e `[d]rop` in inglese portano la lettera
dentro la parola, in italiano no — «li raccogli col tasto **g**», «li posi col
tasto **d**». La lettera si nomina, non si traduce.

⚠️ **Il divieto di genere per settanta righe di seconda persona.** Il tutorial
da' del tu senza pausa, quindi: «Non serve, grazie» invece di «so cavarmela da
solo», «Attenzione:» invece di «Attento:», «All'inizio pensavo che non ci fosse
piu' niente da fare» invece di «quando ti ho vista», «Verme che non sei altro!»
invece di «brutto verme».

---

## Quando la grammatica non si risolve in una resa: si toppa l'ORDINE — 2026-08-21, settantasettesima

`chat.hsp:22500` compone il nome della casa del giocatore: prende l'epiteto di
`random_title()` e gli **appende** uno degli undici suffissi di `:22498`, come
fa l'inglese di monte («Silver Spectre Hovel»).

In italiano non funziona, e non per come sono resi i suffissi: l'epiteto della
64ª è già un **sintagma intero** — «fragore della dipendenza», «luce della
maga» — e qualunque parola gli si metta dietro esce sgrammaticata. Le rese
possibili erano tutte cattive.

⭐ **La struttura giusta ce l'aveva il giapponese**: 「<epiteto>の家」 è
*«casa DI <epiteto>»*, cioè esattamente l'ordine italiano. Quindi la toppa
(la 1017) gira la concatenazione **nel solo ramo inglese**

    mdatan(MDATAN_NAME) = lang(mdatan(MDATAN_NAME) + s(rnd(10)),
                               s(rnd(10)) + " " + mdatan(MDATAN_NAME))

e gli undici suffissi diventano **prefissi che finiscono in «di»**: «Casa di»,
«Residenza di», «Castello di», «Tana di».

⚠️ **«di» è la sola preposizione che regge.** Qualunque articolo — «Casa DEL
fragore», «Casa DELLA luce» — si accorderebbe col primo nome dell'epiteto, che
cambia a ogni tiro. È la 64ª applicata alla preposizione invece che
all'aggettivo: *esiste una costruzione italiana che non chiede accordo?*

⚠️ **La riga è toppabile per un motivo che va controllato ogni volta**: la sua
unica `lang("", " ")` non viene estratta (giapponese vuoto), quindi il
dizionario non la riscrive e sorgente pinnato e build coincidono — che è quel
che `test_toppe` pretende (53ª). Una riga con una `lang()` viva **non** si
sarebbe potuta toppare.

✅ **Provata sul banco HSP** (`scratchpad/banco_hsp.py`), fuori dal gioco e in
pochi secondi: dodici tiri, «Castello di Quiete del figlio», «Tana di Dea
dell'uccello». È la seconda volta che il banco evita un giro di
`applica` + `compila` + gioco.

💡 **Il precedente serve al muro del materiale** (`mithril sword` → «spada **di**
mithril»): è lo stesso problema — l'ordine di monte, non la resa — e adesso si
sa che costa mezz'ora.

---

## Le firme condivise di `chat.hsp` sono la regola, e la rete va rilanciata a ogni giro — 2026-08-21, settantasettesima

La 76ª aveva scoperto che una firma vive in più punti del file e che tradurne
una lascia un menu a metà. La 77ª ha misurato **quanto** è comune: tre volte su
nove lotti, e una di quelle firme stava in **cinque** menu.

| firma | rappresentante | menu accesi |
|---|---|---|
| 「やめる」/«No way!» | `:9051` | il blocco 47 dell'informatore |
| 「断る」/«I refuse.» | `:2351` | Erystia, le monete di bronzo, la capsula, la tartaruga |
| 「いいよ」/«Sure.» | `:8197` | la lettera di Siraha, la tartaruga della principessa |

⚠️⚠️ **E nessuna di queste si poteva vedere leggendo il codice prima**: finché
un menu è tutto inglese, `bilingui` tace ed è giusto che taccia — non c'è niente
di rotto. Il difetto **nasce** con la resa. Quindi l'ordine di lavoro è:
tradurre, reimportare, **poi** misurare.

💡 **E chiudere un menu ne può aprire un altro**: la resa delle monete di bronzo
(scritta per chiudere il menu di `:2996`) ha acceso quello del potioman a
`:3029`, dove mancava 「やめておく」. Tre giri per arrivare a zero. *`bilingui` non
si lancia una volta a fine lotto: si rilancia finché non dà zero.*

⭐ **L'altra faccia paga**: `:20576` è la firma di **tutti** i «Thanks!» del file
(`_thanks(2)`), e una resa sola ne ha resi una decina. La stessa proprietà che
rompe i menu è quella che moltiplica il lavoro fatto.

---

## Un permesso scritto in una rete scade quando la resa lo risolve — 2026-08-21, settantasettesima

`strumenti/maiuscole.py` tiene in `GIUDICATI` i siti `cnven()` «appesi» che
qualcuno ha già guardato e approvato. Due di essi (`chat.hsp:22375` e `:24739`)
portavano il motivo «chat.hsp non è ancora tradotto».

Tradotti nella 77ª con il nome **in testa** — «La gattina passa di mano.» —
quei due siti sono usciti dagli appesi **da soli**, perché la rete legge la
**build** e non il sorgente pinnato. Ho scritto il contrario in un messaggio di
commit, e a correggermi è stato `test_i_giudicati_esistono_ancora`, che esiste
apposta per non lasciare un permesso attaccato al vuoto.

💡 La regola generale: **un elenco di eccezioni è un debito, e va riletto ogni
volta che si tocca uno dei siti che nomina.** Se la resa risolve il difetto,
l'eccezione non va aggiornata: va tolta.

---

## Una resa gemella è valida per costruzione, ma non è gratis — 2026-08-20, settantatreesima

Il dizionario vive in `dizionario/<file>.jsonl` e `applica` cerca la firma **nel
file che sta costruendo**: una stringa identica in due file va tradotta due
volte, e niente lo diceva. La 72ª l'aveva visto a schermo (`You displace X`
cinque righe sotto «Ti scambi di posto con X», stessa firma) e misurato: 417
rese esistenti che nessun referto nominava.

`strumenti/gemelle.py` le elenca. Rimisurate dal sorgente: **405**, che con la
regola nuova sul giapponese vuoto diventano 392 gemelle più 13 divergenti.

### Le tre classi non hanno lo stesso rischio, e la differenza è la firma

- **gemella** — la firma combacia. La firma include giapponese, inglese **e
  l'espressione** (vedi il docstring di `estrai.firma`), quindi la resa è la
  chiave che `applica` andrà a cercare, con le stesse variabili: è corretta per
  costruzione.
- **divergente** — la stessa firma è già resa in due modi: «il cane» e «Cane»,
  «un sotterraneo» e «sotterraneo». Quasi sempre legittimo — l'articolo dipende
  da come la frase incornicia la stringa — e **la rete non sceglie**: mette i
  candidati nel lotto e lascia `it` vuoto.
- **quasi gemella** — combacia solo il giapponese. `chara_func.hsp:4369` e
  `map.hsp:14821` dicono la stessa cosa in giapponese e la resa dell'altro porta
  `name(cdata(CDATA_TAGTEAM_PARTNER, tc))`, cioè **le variabili dell'altro
  sito**. È l'errore che il docstring di `firma()` descrive per esteso: una
  chiave troppo debole scrive codice sbagliato in silenzio.

⚠️ **Il giapponese vuoto non fa quasi gemella.** Una dinamica di sola morfologia
(`lang(name(cc), "The " + name(cc))`) non ha letterali giapponesi, e il vuoto
combacia con qualunque altro vuoto: 34 falsi accoppiamenti, fra cui `The ` di
`action.hsp` con `Selected ` di `blend.hsp`.

### ⭐⭐⭐ Il fatto nuovo: una gemella dentro un menu non è gratis

Aprendo il lotto di `chat.hsp` è saltato fuori il pezzo che vale più della rete.
**82 delle 194 gemelle stavano dentro un menu `chatList`, e nessuno dei menu
toccati si sarebbe chiuso intero.** Il caso limpido:

    8991  punch      da fare        8997  touch      da fare
    8992  claw       GEMELLA        8998  spore      GEMELLA
    8993  kick       da fare        8999  branch     GEMELLA
    8994  bite       da fare        9000  strike     da fare

Tre voci su quattordici. Importarle avrebbe portato il menu **da inglese e
coerente a metà italiano e incoerente** — che è la trappola della 64ª
(`db_race.hsp`, la chiave mostrata accanto all'etichetta) su un oggetto diverso.

💡 La forma generale: *ogni rete del progetto parte da una stringa, ma il
giocatore non legge una stringa — legge una schermata.* Una resa può essere
giusta e fare danno perché arriva **da sola** dove le sue vicine non arrivano.
`annota_menu()` mette in ogni riga il menu in cui sta e quante voci ne mancano;
il lotto lo porta in `_menu`, il referto lo somma in fondo.

### ⚠️ E dentro il menu anche la gemella va rigiudicata

`claw` è reso «graffia» in `text.hsp`, dove è il **verbo** del messaggio di
combattimento («X ti graffia»). Nel menu che chiede quale stile si impara ci
vuole il sostantivo, «Graffio». Sei gemelle scartate così, tre per il mestiere e
tre per la misura:

    claw / spore / branch          il verbo del colpo -> il nome dello stile
    Propagate greatness of god.    «Talvolta predica la fede.» (25) -> «Predica la fede»
    Do not train in town           «Vieta di allenarsi in città» (27) -> «Non allenarsi in città»
    I want to get along with you   «Vorrei andare d'accordo con te.» (30) -> «Vorrei essere amici»

Le ultime tre non sono un errore di chi le scrisse: `text.hsp:1523-1556` è **lo
stesso elenco** di regole del compagno, visto dal pannello che lo descrive
invece che dal menu che lo imposta, e lì la colonna è più larga. Stesse parole
chiave, misura diversa. 💡 *Due schermate che mostrano la stessa scelta devono
dire le stesse parole, ma non sono tenute a dirle con la stessa lunghezza.*

### ⚠️⚠️ E `event.hsp` non si travasa affatto: le sue gemelle sono un generatore

**125 delle 148 gemelle di `event.hsp`** non sono messaggi: sono i pezzi di un
generatore. `hito`, `mon`, `tori`, `item`, `drink`, `tree` (righe 3018-3473)
vengono infilati in una trentina di cornici montate a caso:

    buff = lang("暴れる" + mon + "に" + hito + "がかぶりついている…",
                "You saw an enraged " + mon + " with a " + hito + " ...")

Le rese gemelle arrivano da `db_card.hsp` **con l'articolo dentro** («il
marinaio», «l'anziano»), le cornici sono ancora inglesi, e in italiano una
cornice deve accordarsi in genere col pezzo che ci finisce. Si traducono
**insieme alle cornici**, come gli epiteti della 64ª: è un giro di progetto, non
un travaso.

### La grammatica scelta per il generatore, e come si è provata

Fatto nella stessa sessione: 158 pezzi e 35 cornici (3523-3629: il mare, la
strada e Lost Ylva). L'accordo di genere si scioglie in quattro mosse:

1. **ogni pezzo porta il proprio articolo indeterminativo** — «un marinaio»,
   «una medusa kraken», «un'arpia» — così la cornice non deve indovinare il
   genere di quel che ci finisce dentro;
2. **`donna` diventa una locuzione invariabile POSTPOSTA.** In giapponese è un
   aggettivo prenominale (`変な髪形の` + `hito`); in italiano diventa «dal taglio
   di capelli assurdo», «in fin di vita», «pelle e ossa», «ormai cadavere» —
   nessuna di queste si accorda. ⭐ E l'ordine possiamo cambiarlo **perché
   l'espressione la scriviamo intera**: `applica` mette quel che diciamo noi,
   quindi il pezzo può passare da prima a dopo il nome;
3. `nagara` era già avverbiale e non si accordava con niente;
4. **nessuna cornice porta participi o aggettivi che si accordino col pezzo**:
   «an enraged `mon`» → «`mon` **fuori di sé**», «a flying `tori`» → «`tori` **in
   volo**», «completely naked» → «**senza un filo addosso**».

⭐⭐ **La prova è la regola della 64ª, e ha pagato.** Composte tutte e 35 le
cornici **due volte** — un giro con i pezzi tutti femminili, uno con tutti
maschili — e lette. Tre sono state riscritte, e nessuna delle tre per un accordo:

    3562   «implorare pietà A una mandragora»       → «in ginocchio davanti a…»
    3616   «una guardia … che le GUARDIE portavano via» → «in mano alle guardie»
    3626   il participio si attaccava al soggetto sbagliato

💡 *Quel che la lettura trova non è quel che il metodo prevedeva.* La grammatica
ha retto su tutte e 70 le frasi; a cadere sono state una reggenza, una ripetizione
e un'ambiguità — cose che nessuna regola di accordo avrebbe fermato.

### E la geometria si misura, non si stima

`event.hsp:4154` manda a capo con `talk_conv buff, (dx - 80) / (7 - en) - en * 4`,
dove `dx` è la larghezza del `bg_re*.bmp` più 36: **34 caratteri** per gli eventi
di mare (`bg_re25`, 275 px) e **48** per quelli di viaggio (`bg_re13`, 360). ⭐ Ma
l'altezza della finestra **cresce con le righe** (`dy = ty + noteinfo(0) * 15 +
80 + listmax * 20`), quindi non c'è un tetto duro: il costo di una riga in più è
15 px. Misurato col simulatore del progetto (`diario.manda_a_capo`) sul caso
peggiore — il pezzo più lungo di ogni famiglia in ogni cornice — l'italiano sta
al massimo **una riga** sopra l'inglese, con cinque righe in tutto.

### ⭐⭐⭐ E il collaudo ha mostrato il rovescio: la cornice che non è arrivata

Una schermata sola, mandata dopo il generatore. La frase c'era ed era in piedi —
«Hai visto uno spazzino con una corda robusta fra le chiappe, le dita della
destra nelle narici e la sinistra a tirare pugni…», tre righe dentro la
pergamena. Ma **intorno** c'erano quattro cose inglesi, e una era nostra:

    < Adventure Days >                              il titolo di OGNI evento
    I don't want to get involved.                   l'unico bottone
    You gained a good amount of travel experience.  a ogni evento
    As a salary, 215 monete d'oro e 2 oggetti have been sent to your house.

⚠️⚠️ **L'ultima l'abbiamo fatta noi, la mattina stessa.** I due pezzi
(`" monete d'oro"` e `" e N oggetti"`) erano fra le 24 gemelle importate;
la cornice che li incornicia, `event.hsp:4467`, no. 💡 *È la lezione dei menu un
livello più su: una resa può essere giusta e fare danno perché la **cornice** che
la incornicia non è arrivata.* Nei menu il danno stava fra due voci vicine, qui
sta fra il pezzo e la frase che lo contiene — e in tutt'e due i casi la resa,
presa da sola, è corretta.

⚠️ **E le due righe del registro erano quasi gemelle per uno SPAZIO.** «` You
gained a good amount of travel experience.`» è resa in sedici siti; le due che il
giocatore ha visto (`3011`, `3014`) hanno lo stesso inglese **senza lo spazio
davanti**, quindi firma diversa e nessun referto le nominava. 💡 La classe
«quasi gemella» non è solo la trappola delle variabili: è anche l'elenco dove si
va a cercare quando una riga è inglese e sembra che dovrebbe essere tradotta.

### Quel che è rimasto fuori apposta

`custom_autopick.hsp` sta in `FILE_DELICATI` e `--lotto` si rifiuta senza
`--forza`: 78 delle sue 90 `lang()` sono confronti dentro `instr` contro
`autopick.txt`, che scrive **il giocatore**. Lì una `lang()` non è un'etichetta,
è una chiave.

---
## Il danno che non sta nella stringa ma in come il codice la monta — 2026-08-20, settantaduesima

Il collaudo ha mandato quattro schermate e ne sono uscite due reti nuove. Le due
hanno in comune una cosa che vale più delle due: **il difetto non era in nessuna
stringa.** Ogni rete del progetto — e sono otto — guarda una stringa e le chiede
qualcosa: sei se ci sta nel riquadro, `battute` se il giapponese è reso in più
modi, `accenti` se ha l'accento in mezzo a una parola. Tutte partono dalla
stringa, e nessuna vede quel che succede **fra due stringhe**.

Le due famiglie trovate:

    la GRONDA        «Classe» a wx+30 e «Guerriero» a wx+79: fra i due c'è
                     uno spazio, e se l'etichetta italiana è più larga il
                     valore le finisce sopra. A schermo «ClasseGuerriero»
    cnven()          init.hsp:191 alza la prima lettera. Giusto in testa a una
                     frase, sbagliato appeso in mezzo: «il cittadino Femmina»

⚠️⚠️ **E tutt'e due esistono SOLO nelle build tradotte.** «Class» ha 5 caratteri
e «Classe» 6; `cnven` fa `if ( jp ) return` e in giapponese non tocca niente.
Sono difetti che upstream non può vedere nemmeno volendo, perché nella sua
lingua non ci sono: è la categoria di danno che un progetto di traduzione deve
guardarsi da solo, e per quattro sessioni li ha guardati soltanto il giocatore.

### ⚠️ Una rete che misura la geometria legge la BUILD, non il sorgente

`gronde.py` è la prima rete del progetto che legge `build/` invece di
`sorgente/`. Non è una scorciatoia: le altre misurano il **testo**, che il
dizionario deve ancora scrivere; questa misura la **geometria**, e la geometria
la cambiano le toppe. Letta sul sorgente pinnato, direbbe per sempre che
«Classe» sfora, perché sul sorgente la gronda è ancora quella inglese.

⭐ E leggendo la build si guadagnano due cose che il sorgente non dà. La prima:
l'italiano è già dentro la fessura inglese della `lang()`, quindi la rete non ha
bisogno del dizionario — quel che legge è quel che il giocatore vede. La
seconda, più utile: **solo la build dice quale riga è viva.** Nella colonna del
carico i valori hanno due `pos`, `wx + 86` e `wx + 102`, e il primo è dentro un
blocco `ORIGINAL - BEGINNING` commentato da monte. Chi prendesse quello
misurerebbe una gronda di 57 px che non esiste.

### ⚠️ Il prezzo: le ancore della rete inseguono le toppe

`gronde.py` cerca le righe `pos` per **testo esatto** e pretende di trovarne una
sola. Aggiunta la terza toppa, la rete è morta di `LookupError` invece di
misurare la gronda vecchia — che è il comportamento voluto, e va detto perché
sembra un difetto: chi tocca una di quelle tre toppe deve aggiornare anche
l'àncora. Il patto è quello di sempre, **rumore invece di silenzio**, e qui
costa una riga.

---

## Il conto delle voci non è il verdetto: è l'elenco da leggere — 2026-08-20, settantaduesima

`maiuscole.py` trova 148 siti di `cnven()` e **134 sono giusti**. Una guardia che
chiedesse zero sarebbe una guardia che nessuno può soddisfare, e finirebbe
spenta o aggirata.

La forma che regge è la stessa di `fuori_misura_inglese` in `menu_dialogo` e di
`invariati.md`: si classifica per **posizione nell'espressione** — in testa a
quel che si disegna, appeso dopo altro testo, accumulato con `+=` — e i dieci
casi limite si giudicano uno per uno **con un motivo scritto**. La guardia non
chiede zero appesi: chiede che quell'elenco non si allunghi da solo. Un sito
nuovo è una riga da leggere, non per forza un difetto.

💡 Vale anche per la seconda geometria del menu del dialogo. Il gioco taglia a
24 caratteri quando le voci passano le dieci (`chat.hsp:25166`), ma **quante
voci abbia il menu dipende dal PNG** — ruolo, trama, compagni — e non è
decidibile dal sorgente. Chiedere 24 a tutte vorrebbe dire mutilare anche le
voci che upstream stesso lascia tagliare. La regola che si può scrivere è:
**se l'inglese ci sta in 24, l'italiano ci deve stare.** Alla nascita ha trovato
dieci rese, e nove erano di sessioni precedenti.

⭐ E per i quattro «Il boss di …» la cura non è stata accorciare il nome del
luogo — canonico, usato anche in `map.hsp` e `text.hsp` — ma l'apposizione che
gli sta davanti: «Boss: Torre Rovente». *Quando una resa non ci sta, si guarda
prima quale pezzo NON è vincolato altrove.*

---

## Due misure della stessa cosa nella stessa funzione, e la più stretta vince sempre — 2026-08-20, settantaduesima

`screen.hsp:6759` è « have gained a level.» in inglese e 「はレベル**N**になった！」 in
giapponese: il giapponese dice **a quale** livello si sale, l'inglese aveva perso
il numero. Rimetterlo in italiano ha fatto scattare `verifica.py`.

E lì è saltato fuori che le **due guardie della stessa riga non erano
d'accordo**. Quella sugli argomenti sottraeva già l'unione dell'inglese e del
giapponese, con dieci righe di commento che spiegano perché; quella sui nomi,
dieci righe sopra, pretendeva l'uguaglianza col **solo inglese**. Convivevano da
sessioni, e la più stretta vinceva sempre: il commento della più larga
descriveva una libertà che non c'era.

💡 **Un commento che descrive un comportamento non lo produce.** È la stessa
lezione della 71ª — una regola che il progetto conosce e non ha messo in una
guardia è un ricordo — vista dall'altro lato: qui la guardia c'era, ed era la
seconda di due, e la prima la copriva.

⭐ La regola giusta non è simmetrica: **quel che l'inglese ha è DOVUTO** —
toglierlo è perdere un dato che il giocatore vede — **quel che ha solo il
giapponese è PERMESSO.** Una resa non è tenuta a recuperare tutto quello che
l'inglese ha perso, ma se lo recupera non è un difetto.

### ⚠️ E una funzione che non porta dati non è una chiamata di contenuto

Subito dopo, `screen.hsp:1442`: il giapponese saluta il giocatore per nome
**dentro** la battuta, e rimetterlo in italiano vuol dire metterlo dentro
`cnvtalk`. La guardia degli argomenti leggeva l'intera `cnvtalk(...)` come una
chiamata «che non viene da monte».

Ma `cnvtalk` mette le virgolette al discorso diretto, e basta. Non è contenuto,
è punteggiatura — e contarla come contenuto **rende invisibile il contenuto che
ha dentro**. Adesso è *trasparente*: attraversata, non registrata, che è diverso
dalla morfologia inglese, la quale invece nasconde anche il proprio contenuto.

💡 Il difetto non era nella regola, era nella **classificazione**. È la 71ª di
nuovo — i cinque segnaposto classificati sui nomi invece che sui siti — su un
oggetto diverso: lì una tassonomia, qui una funzione.

---

## Il dizionario è per file, e una firma resa in un file non arriva all'altro — 2026-08-20, settantaduesima

Nel registro il collaudo ha mostrato `You displace Tomdecker il cittadino.`
cinque righe sotto «Ti scambi di posto con Chur il cane». Stesso evento, due
righe, una resa e una no — e la firma è **la stessa**, `70e253be`:
`action.hsp:1929` è tradotta, `chat.hsp:22587` no.

Il dizionario vive in `dizionario/<file>.jsonl` e `applica` cerca la firma nel
file che sta costruendo. Una stringa identica in due file va tradotta **due
volte**, e niente lo dice: `verifica --dizionario` conta 3.920 righe da fare in
`chat.hsp` senza accorgersi che di alcune la resa esiste già.

Misurato su tutto il progetto: **417 rese gemelle** su 6.718 da fare, il 6%.

    chat.hsp 197 · event.hsp 148 · custom_autopick.hsp 21 · help.hsp 17
    init.hsp 6 · item_func.hsp 5 · chara.hsp 4 · material.hsp 4 · txtadv.hsp 4
    net.hsp 3 · system.hsp 3 · command.hsp 2 · e altri tre file con una

⚠️⚠️ **Ma non si travasano alla cieca, e il campione lo dimostra in due modi.**
`custom_autopick.hsp` confronta 78 delle sue 90 `lang()` dentro `instr` **contro
il file che scrive il giocatore**: tradurne una cambia una chiave, non
un'etichetta. E `'armor'` prenderebbe «Armatura» da `db_race.hsp`, cioè una
maiuscola e un registro che vengono da un'altra schermata.

💡 Sono un **elenco da leggere**, come i `cnven` appesi: la resa gemella è già
approvata per quel giapponese e quell'inglese, quindi è corretta per
costruzione — quel che resta da decidere è il **registro**, e quello dipende dal
sito. Vale la pena farne una rete che le elenchi per file, così un lotto sa da
dove partire.

---

## Il registro di un menu è quello del giapponese, non quello dell'inglese — 2026-08-20, settantaduesima

Le 125 voci del menu del dialogo lo dicono in fila:

    投資したい          «Vorrei investire»         Need someone to invest in your shop?
    鑑定したい          «Identificare un oggetto»  I need you to identify an item.
    そこをどいて        «Spostati»                 Move aside.
    装填              «Carica»                   Ammo
    射撃              «Tiro»                     Fire
    使う              «Usa»                      Tool

L'inglese di Elona parla in frasi intere e in prima persona; il giapponese
scrive **il verbo e basta**. Un menu vuole la seconda cosa — e non è una
questione di gusto, è la sola forma che sta nei 24 caratteri della seconda
colonna. ⚠️ E nelle ultime tre righe l'inglese ha anche cambiato **parte del
discorso**: dove il giapponese ha un verbo, lui ha messo un sostantivo. La ruota
dei comandi di `help.hsp` è fatta di verbi, e in inglese non si vede.

---

## Una finestra può avere due tetti, e misurarne uno fa credere di averla misurata — 2026-08-17, cinquantacinquesima sessione

La **rete 14** della 54ª misura l'**altezza** della finestra del dialogo: dodici
righe, a capo a 53 caratteri. Era nuova di ieri, scritta apposta perché quel
pezzo di schermo non lo guardava nessuno, ed è stata confermata a schermo — le
`<Nove Code Dorate>` occupano dodici righe su dodici e il bottone ci sta sotto.

⚠️ **E la seconda schermata del collaudo ha mostrato una voce tagliata.** La
stessa finestra, l'altra geometria:

    [5500 biglietti] Carta del dio-di-carta-piegata-segretissimo <Kamikakushi>.

a schermo si fermava su «segretissimo». **La larghezza delle voci era scoperta**,
e sopra ci vivono **1.626 righe di menu** del sorgente.

💡 **La lezione sul metodo è la sorella di «finito per quale referto» (53ª).**
Lì la domanda era *quale rete ha guardato questo file*; qui è *quale rete ha
guardato questa geometria*. Una finestra non è un'unità di misura: lo sono i
suoi riquadri, e ce n'è più d'uno per finestra.

### Il tetto, e da dove viene

    chat.hsp:25232   ww = 600                      la finestra
    chat.hsp:25160   x = wx + 136                  dove comincia la voce
    chat.hsp:25177   cs_list listn(0,cnt), x + 30
    module.hsp:129   pos arg2 + 4 ... : mes        e altri 4

Il testo parte a `wx + 170`; il bordo interno della pergamena sta a `wx + 577`,
misurato sulla schermata a finestra intera. **407 px.** Sei voci dello stesso
menu danno da **7,60 a 7,88 px per carattere** — lo stesso 7,7 che
`larghezze.py` aveva misurato il 2026-08-10 su un menu diverso, perché è lo
stesso carattere. **407 / 7,7 = 52 caratteri**, ed è `strumenti/menu_dialogo.py`.

⚠️⚠️ **`sdim` non è un tetto: quarta volta in quattro giorni.** `chatList` scrive
in `listn(0, listmax)`, dichiarato `sdim listn, 40, 2, 500` (`init.hsp:2428`), e
a schermo se ne leggono una sessantina. Le altre tre: `skilldesc` (12/08),
`cfname@tcg` nella 53ª, `skillname` nella 54ª. **Un tetto dedotto da un `sdim` è
un'ipotesi da misurare, sempre.**

⚠️ **E `cs_list` non taglia.** Fa `mes` (`module.hsp:130`) *dopo* che la cornice
è stata disegnata (`chat.hsp:25256` prima di `:25177`): lo sforo non è un
troncamento pulito, è testo stampato **sopra** il bordo decorato.

⚠️⚠️ **Un taglio duro che nessuno sapeva** (`chat.hsp:25166`): sopra le **dieci**
voci il menu passa a due colonne e fa `strmid(listn(0, cnt), 0, 24)`. *Quello* sì
è un `strmid`, e 24 caratteri in italiano sono pochissimi. Ma `keyrange` è il
numero di voci **a tempo di esecuzione** e dal sorgente non si legge: la rete 15
non prova a indovinarlo, e resta da collaudare.

### Le quattro rese accorciate, e il criterio

Il criterio è quello del 2026-08-13: **il tetto è un vincolo, non un criterio.**
Il primo accorciamento cerca i caratteri che avanzano; quello giusto cerca la
resa più corta che conserva **le due metà del senso**.

| riga | era | ora | che cosa cade |
|---|---|---|---|
| 1938 | Carta di `<Yonorne>`, la guida novellina. (56) | Carta della nuova guida `<Yonorne>`. (51) | niente: fa la guida ed è alle prime armi |
| 1968 | Carta del dio-di-carta-piegata-segretissimo `<Kamikakushi>`. (75) | Carta dell'origami `<Kamikakushi>`. (50) | «dio» e il superlativo; resta la carta piegata, che è l'identità |
| 2088 | `[Set grigio]` Giorni di nebbia nel labirinto. (60) | `[Set grigio]` Nebbia nel labirinto. (50) | «Giorni», la metà che non dice niente |
| 2108 | `[Set rosso]` Il gran teatro delle spettacameriere. (65) | `[Set rosso]` Teatro spettacameriere. (51) | «gran»; la parola inventata è il nome e si tiene |

⚠️ **Due erano regressioni nostre** (1938 e 2088: l'inglese ci stava, la resa
no), due erano **già rotte a monte** (1968 a 77 caratteri, 2108 a 54). La rete
le distingue apposta, con `fuori_misura_inglese()`: il riquadro è il tetto anche
dove upstream lo sfonda, ma sapere quali erano già rotte dice da dove viene il
danno.

💡 **E fuori dal negozio delle carte il corpus era pulito**: le uniche altre due
voci sopra il tetto stanno in `event.hsp` e sono **identiche in inglese**.

### Una guardia vale solo dove guarda, terza volta

⚠️ **La prima versione della rete 15 riconosceva le voci dal campo `contesto`** e
ne vedeva **31 su 150**: `estrai.py` lo riempie **solo per le dinamiche**, e le
opzioni di conversazione sono quasi tutte statiche. Riscritta per leggere il
sorgente pinnato, come fa `larghezze.py` con `menu_per_riga`. È lo stesso
inciampo di `txtplusbody`, che non seguiva la convenzione di nome.

### E lo stesso meccanismo spiega il decimo punto cieco

`riquadri.py` legge la **geometria** delle piastrelle da `screen.hsp`
(`FILE_HUD`) e le **etichette** da `text.hsp` (`FILE_STATI`). Un'etichetta che
vive nel file della geometria non la vede nessuno — ed è il caso di
`screen.hsp:1004`, «Autopickup», che sta nell'HUD in mezzo a quattro etichette
italiane. **Non è un difetto della rete: è il suo perimetro.**

`screen.hsp` ha **112 `lang()`** e non aveva **nessun file di dizionario**, come
`db_card.hsp` e `chat.hsp` prima della 54ª. Ed è il caso peggiore della
famiglia, perché non è una finestra che si apre: è testo **sempre** a schermo.

---

## Una stringa dichiarata invariata per un sito fa sembrare voluta la dimenticanza in un altro — 2026-08-15, quarantaquattresima sessione

Traducendo 「なし」 di `command.hsp:1445` la **rete 3** ha detto che lo stesso
giapponese era già reso in due modi: «Nessuna» a `init.hsp:371` e **«none»** a
`text.hsp:49`. Il secondo non era una resa: era l'inglese rimasto lì.

⚠️ **E `invariati.md` lo copriva, ma per un'altra cosa.** La riga 437 dichiara
«none» invariato perché è uno dei nove valori di `CDATAN_NEWSEX`, scritti nel
salvataggio e riletti come operandi di confronto (la 41ª, punto 3). A
`text.hsp:49` la stringa è la stessa e il sito è un altro — `_dengon`, il
messaggio che un avventuriero ti ha lasciato — e lì non c'è niente da
preservare. **La dichiarazione vale per il sito, non per la stringa**, e questa
è la prima volta che la differenza produce un difetto invece di una
discussione.

⚠️ **Si legge, e ha cinque parole italiane accanto.** `command.hsp:4247` stampa
`_dengon(dengon) + "(" + _impression(…) + ")"` nella lista degli avventurieri, e
gli altri cinque valori sono resi: «Collaborazione», «Invito», «Dichiarazione»,
«Incoraggiamento», «Disprezzo». Il primo diceva `none(Cordiale)`.

✅ Corretto in «Nessuna» con `scratchpad/correzione-none.py`, che è anche il
primo modello di correzione con chiave `(riga, jp)`: le sei voci di
`text.hsp:49` stanno tutte sulla stessa riga, e `correzione-schivata.py` andava
bene solo perché in `action.hsp` ogni riga ha una voce sola.

💡 **La lezione sul metodo**: la rete 3 fin qui serviva a non ridecidere una
resa già presa. Qui ha fatto un'altra cosa — ha trovato una resa **mancante**,
in un file chiuso al 100%, che nessun conteggio di «non tradotte» poteva
includere perché la voce nel dizionario c'era. È lo stesso meccanismo di
`rete8_dizionario.py` nella 37ª: una rete nata per il lavoro nuovo che, girata
all'indietro, trova il lavoro vecchio.

---

## Lo stesso giapponese può cambiare numero se cambia il sito: «Alleato» contro «Alleati» — 2026-08-15, quarantaquattresima sessione

`text.hsp:32` rende 「仲間」 «Alleato», ed è giusto: è un elemento di
`_impression`, cioè il **grado di rapporto di un personaggio solo** — si legge
accanto al nome di quello.

`command.hsp:1270` ha lo stesso 「仲間」 in `s(10)`, che è il **titolo della
finestra** che elenca tutti i compagni. Lì «Alleato» sarebbe sbagliato: la
finestra ne mostra sedici per pagina.

✅ **La differenza la impone il sorgente, non la traduzione**, che è la formula
con cui la 37ª aveva già risolto il litigio fra la rete 4 e la rete 11. Il
numero grammaticale è imposto dal sito esattamente come lo era la spaziatura di
« Turni» nella 43ª: la rete 3 segnala, e la risposta è che ha visto una
differenza vera invece di un'incoerenza.

⚠️ **Quindi la rete 3 su `command.hsp:1270` resta accesa e va lasciata accesa.**
Chi rilancia il lotto `command-009` la rivedrà: non è un difetto da chiudere.

---

## Il registro nominale, e perché una schermata intera lo pretende invece di preferirlo — 2026-08-15, quarantaquattresima sessione

La schermata «Background» (`chara.hsp:3265`-`:3336`, `command.hsp:*setHistory1`
… `5`) è cinque righe tirate a sorte che raccontano il passato di un
personaggio. La regola «il giocatore non ha genere noto» la copriva già, ma qui
si somma un secondo vincolo che nessuna schermata precedente aveva:

1. **il soggetto non è solo il giocatore.** `chat.hsp:8588`-`:8593` rilegge gli
   stessi cinque valori da `cdata(CDATA_BACKGROUND_PART_*, c)` e li fa
   raccontare a Mizuki, dove `c` è un **alleato** scelto con `*com_ally`. Non
   c'è una `lang()` gemella che distingua i due casi: è la stessa riga;
2. **le righe 3 e 4 sono mezza frase ciascuna, e si tirano a sorte
   separatamente.** `ohanasi3` e `ohanasi4` sono due `rnd(45) + 1` indipendenti
   (`chara.hsp:3261`-`:3262`): ognuno dei 45 pregi si salda a ognuno dei 43
   difetti, **1.935 frasi possibili**. Una resa che concordasse la testa con la
   coda — in genere, numero o soggetto — sbaglierebbe nella quasi totalità delle
   combinazioni.

✅ **La forma nominale è l'unica che regge tutt'e due**, ed è quella del
giapponese, che il soggetto non ce l'ha mai: 「奴隷だった過去を持つ。」,
「自意識過剰。」, 「趣味は読書。」. L'inglese è la lingua che se ne discosta,
esattamente come per le etichette di stato di `guida-stile.md` («Starving» →
«Inedia»).

💡 **Le tre manovre, e adesso sono tre e hanno un nome**, perché in 222 rese
tornano continuamente:

| manovra | esempio | dove cade l'accordo |
|---|---|---|
| il **nome astratto** al posto dell'aggettivo | 「奴隷だった」 → «Un passato di schiavitù» | in nessun posto |
| il **participio appeso a una cosa** | «Genitori perduti troppo presto», «Il paese natale, distrutto dai mostri» | su `genitori`, su `paese` |
| il **nome di genere fisso** | «Cavia», «una creatura maledetta», «Un'arma», «Il clone», «Una guida forte» | sul nome, che un genere ce l'ha suo |

⭐ La seconda è la più utile e non era mai stata scritta: **il participio non si
evita, si sposta**. È la stessa famiglia del dativo riflessivo della 40ª e
dell'impersonale «ci si dorme» della 43ª — si sposta l'accordo su qualcosa che
la resa controlla — ma applicata al participio invece che al verbo.

⚠️ **E la congiunzione va in coda, non in testa.** Il giapponese chiude la riga
3 con 「〜が、」; l'inglese mette «Though» all'inizio, che in italiano vorrebbe
«Per quanto mite e generoso,», cioè due aggettivi accordati col soggetto. Tutte
e 45 le teste finiscono in «, ma». È la manovra della rete 9 — il connettivo
che chiude la testa — applicata a un'avversativa invece che a una copulativa.

---

## Il budget di una schermata che nessuna guardia misura: l'inglese di monte — 2026-08-15, quarantaquattresima sessione

Le cinque righe del «Background» si disegnano con `mes` a `pos wx + 75, wy + 200
+ n * 15` dentro una finestra larga 360 px. È la stessa situazione della scheda
del personaggio della 43ª — `larghezze.py` conosce solo i menu di `*prompt_key`,
`riquadri.py` l'HUD e le tattiche — ma **senza il metro che la 43ª aveva**: lì il
budget era la differenza fra la `pos` dell'etichetta e quella del valore, scritte
a poche righe di distanza. Qui il valore non c'è: la riga arriva fino al bordo.

✅ **Il metro possibile è quello di `tetti_buffdesc.py`, cioè l'italiano contro
l'inglese di monte**, e il tetto è la **voce inglese più lunga dello stesso
gruppo**: quella la finestra la contiene già, per il fatto che upstream ci gira.
Una resa che non la supera non può stare peggio.

| gruppo | voci | tetto EN | resa IT più lunga |
|---|---|---|---|
| `setHistory1` origine | 46 | 54 | 54 |
| `setHistory2` la partenza | 45 | 61 | 51 |
| `setHistory3` il pregio | 45 | 57 | 48 |
| `setHistory4` il difetto | 43 | 48 | 47 |
| `setHistory5` il vizio | 43 | 50 | 48 |

Lo misura `scratchpad/misura-background.py`. ⚠️ **Non è una guardia**: è un
referto da rilanciare a mano quando si tocca uno dei cinque gruppi, come
`tetti_buffdesc.py`. E come quello, stima in caratteri quel che lo schermo
disegna in pixel.

⭐⭐⭐ **E nella 64ª lo schermo i pixel li ha dati, e la stima non bastava.** Il
collaudo della creazione ha fotografato quella finestra: due righe su cinque
uscivano dal bordo destro della pergamena, +45 px e +31 px. Il tetto vero è
**38 caratteri** — `chara.hsp:3305` apre la finestra larga 360, il testo parte
da `wx + 75` e il passo è 7 px, misurato sulla riga da 47 caratteri che va da
x=858 a x=1176. Col metro relativo `setHistory1` risultava a posto fino a **54**
caratteri, cioè sedici oltre il bordo. 💡 **Un referto che dichiara la propria
approssimazione ha ragione a dichiararla, e resta approssimato finché qualcuno
non guarda lo schermo**: la nota qui sopra lo diceva da venti sessioni.

Il successore è `scratchpad/trascorsi.py`, che porta il tetto assoluto e separa
il perimetro nostro (le righe dove l'inglese sta dentro e noi no, più quelle
dove sforiamo più di lui: erano **28**, corrette nella 64ª) dal difetto di monte
(**97 righe inglesi su 226** fuori misura, che non si toccano).

---

## Una voce duplicata dentro la stessa tabella: quattro casi in due elenchi — 2026-08-15, quarantaquattresima sessione

`*setHistory4` e `*setHistory5` dichiarano 45 valori l'uno e ne contengono 43
distinti: `:9933` ripete `:9924` (「私生活はだらしない。」), `:9972` ripete `:9966`
(「勘違いが激しい。」), `:10059` ripete `:10047` (「慕っている師匠がいる。」),
`:10089` ripete `:10068` (「趣味は昼寝。」). Stessa firma, stesso elenco, due
slot del `rnd(45)`: quei quattro tratti escono col **doppio** della probabilità
degli altri.

💡 **Non c'è niente da fare, ed è il punto**: `estrai --da-tradurre` le fonde per
firma e `applica.py` scrive la resa in tutt'e due i siti, quindi la traduzione è
corretta comunque. Ma è una **famiglia nuova** nella serie degli errori di monte,
che fin qui contava traduzioni sbagliate: qui la traduzione non c'entra, è la
tabella del gioco a essere scritta male. ⚠️ Chi apre un elenco a `rnd(N)` conti
le voci distinte prima di fidarsi di N.

---

## Una testa di frase finisce in « and» SENZA spazio, e la rete 9 guardava male — 2026-08-15, quarantatreesima sessione

La rete 9 esiste dal lotto 010 e dice una cosa giusta: se il ramo inglese finisce
in « and», quella voce è la **testa** di una frase che si salda a una coda scritta
altrove, e la resa italiana deve chiudersi col connettivo. Le dieci teste del log
di combattimento si scrivono così — `action.hsp:4866`, «name(cc) + " calcia via "
+ name(tc) + " e"» — e senza la rete si perde la « e» finale e le due metà si
attaccano.

Il controllo però era scritto `v['en'].rstrip().endswith(' and')`, e quel
`.rstrip()` **cancella esattamente la differenza che conta**:

- una **testa** finisce in `" and"`, senza spazio in coda, perché la coda che
  segue porta il suo;
- una **congiunzione infissa** è `" and "`, con lo spazio da tutt'e due le parti,
  e il connettivo lo è già: non deve chiudersi con niente.

`command.hsp:13` è del secondo tipo — `rtvaln += lang("と", " and ")` dentro il
ciclo che elenca gli oggetti su una casella — e la rete ha bocciato « e »
pretendendo che finisse col connettivo, che è l'unica cosa che quella resa
contiene.

**Misurato prima di toccarla**, che è la parte che conta: su tutto il dizionario
ci sono **29 teste vere**, e finiscono tutte in `" and"` esatto; l'unica voce che
finisce in `" and "` con lo spazio è `text.hsp:11685`, che è infissa. La
distinzione non me la sono inventata per far passare una resa: la impone il
sorgente, e la rete non la vedeva.

⚠️ **È la terza volta che una rete sbaglia lei.** La rete 8 nella 37ª bocciava
due rese giuste perché non guardava da dove veniva `valn`; la rete 4 nella 37ª
pretendeva le stesse parole dove il sorgente ne imponeva di diverse. La regola
che ne esce è sempre la stessa: quando una rete boccia, la prima domanda è **se
la resa giusta è scrivibile**, e la seconda è **che cosa dice il sorgente su
tutti gli altri siti della stessa specie**. Un solo caso non basta a cambiare una
guardia; ventinove contro uno sì.

✅ Il modello corretto è `scratchpad/modello-rete9.py`, nella stessa forma di
`modello-chiave-lunga.py` della 41ª: un file suo, con `RINVIATE = set()`, da cui
`assembla-lotto.py` copia le reti. Il modello **non può essere un lotto che
rinvia qualcosa** — l'ancora `RINVIATE = set()` non ci sarebbe più — e questa è
la ragione per cui il file esiste separato invece di essere il lotto stesso.

---

## La scheda del personaggio si misura dal sorgente, perché nessuna guardia la vede — 2026-08-15, quarantatreesima sessione

`larghezze.py` misura i menu, e lo dice: «solo le assegnazioni a `s(cnt)`» dentro
i `#deffunc` che passano da `*prompt_key`. `riquadri.py` copre le piastrelle
dell'HUD e la colonna delle tattiche. La **scheda del personaggio** non la guarda
nessuno dei due, perché le sue etichette si disegnano con `mes` a `pos` fisse.

Il metro però c'è, ed è nel sorgente: la posizione dell'etichetta e quella del
valore sono scritte a poche righe di distanza, e la **differenza è il budget**.

| gruppo | etichetta | valore | budget | inglese più lungo |
|---|---|---|---|---|
| `:10495` | `wx+355` | `wx+410+5` | 60 px | `Next Lv` (7) |
| `:10504` col. 1 | `wx+30` | `wx+68` | 38 px | `Class` (5) |
| `:10504` col. 2 | `wx+220` | `wx+270` | 50 px | `Height` (6) |
| `:10517` | `wx+255` | `wx+310` | 55 px | `Rating` (6) |
| `:10526` | `wx+29` | `wx+86` | 57 px | `Cargo Lmt` (9) |
| `:10730` | `wx+422` | `wx+468` | 46 px | `Prot` (4) |
| `:10732` | `wx+574` | `wx+617` | 43 px | `Evade` (5) |
| `:10734` | `wx+554` | `wx+617` | 63 px | `SpellPow` (8) |
| `:10837` | `wx+30` | `wx+63` | 33 px | `Desc:` (5) |

Il carattere è `12 + sizefix - en * 2`, cioè **10 px in grassetto** nella build
inglese, 9 per `:10837`. Da `Cargo Lmt` — nove caratteri dentro 57 pixel — viene
il metro: **~6,3 px per carattere**.

💡 **La conseguenza pratica è che upstream abbrevia perché è stretto, e
l'italiano deve abbreviare uguale.** `Prot`, `Evade`, `SpellPow`, `InSAN`,
`Cargo Wt` sono già sigle. Dove il progetto ha una resa distesa che non ci sta —
「回避」 è «Schivata» da `skill.hsp:307`, e vuole 46 px dove ce ne sono 43 — si
abbrevia **la resa**, «Schiv.», e non si cambia parola: non è una traduzione
nuova, è la stessa tagliata dove il riquadro taglia. La rete 3 lo segnala, ed è
giusto che lo segnali.

⚠️ **E il budget vale per il sito, non per la riga dove la firma è estratta.**
`Level` e `Name` non compaiono nella zona della scheda perché `estrai
--da-tradurre` dà una voce per firma e le loro prime occorrenze stanno a `:3556`
e `:7623`. Chi tradurrà quelle due righe sta scrivendo le etichette in cima alla
scheda, con 60 px e 38 px di spazio, e da `:3556` non si vede.

---

## «Vedi X» e non «Si vede X»: a decidere è il NUMERO — 2026-08-15, quarantatreesima sessione

`text.hsp:3095` rende 「がある。」 «Si vede " + s + ".», e la regola del progetto
è copiare la resa già decisa per lo stesso giapponese. A `command.hsp:23`-`:30`
— le tre righe che partono a ogni passo su un oggetto — copiarla sarebbe stato un
errore, e la ragione non è di stile.

In `text.hsp` quel `s` è il nome di un **edificio**: sempre singolare. Qui
`rtvaln` è `itemname()` di una **pila**, e porta il conteggio dentro: «3 pozioni».
L'impersonale italiano concorda col soggetto — «si vedono 3 pozioni» — quindi
«Si vede » sbaglia in tutti i casi in cui gli oggetti sono più d'uno, che sul
pavimento di Elona è il caso normale. Il plurale non è raro: `:13` compone
`rtvaln` unendo fino a tre nomi con « e ».

✅ **«Vedi X» è di seconda persona e regge un oggetto diretto**: non concorda né
in genere né in numero, e copre tutt'e tre le righe. Ed è la stessa famiglia di
soluzioni del dativo riflessivo della 40ª e dell'impersonale «ci si dorme» dei
sei giudizi sul letto (`:34`-`:49`), dove l'accordo cade sul «si» invece che sul
letto: **si sposta l'accordo su qualcosa che la resa controlla**.

⚠️ Il rovescio vale per i participi: 「が設置されている」 («X è installato qui»)
concorderebbe col genere dell'oggetto. Lì la strada è il **nome di genere fisso**
della 40ª più i due punti della 42ª — «Vedi qui una costruzione: X».

---

## Un valore scritto nel salvataggio si migra dove viene CARICATO, non dove viene assegnato — 2026-08-15, quarantaduesima sessione

Il collaudo ha mostrato due righe consecutive che chiamavano casa tua in due
modi:

```
[18:20] Vuoi lasciare Your Home?
        You left Casa tua.
```

La prima legge `mdatan(MDATAN_NAME)`, la seconda `mapname()`. `mapname()` è la
tabella di `text.hsp`, calcolata a ogni chiamata e già tradotta; `mdatan` è
**serializzato nel salvataggio** (`module.hsp:4598` fa `noteadd mdatan(cnt)`,
`:4601` fa `noteget`).

### Il caso è uno solo, e non era ovvio

`map.hsp:1400`-`:1402` dice che per **ogni area tranne `AREA_HOME`** il nome
viene riletto da `mapname()` a ogni `*map_init_main`. Quindi «Grassland»,
«Forest», «Plain Field» non erano un difetto separato: si sistemano da sole
appena il file passa da `applica.py`. Casa tua è l'unica mappa che il giocatore
può **rinominare**, e per questo ha una guardia che non sovrascrive il nome
scelto:

```hsp
if ( mdatan(MDATAN_NAME) == "" | mdatan(MDATAN_NAME) == lang("ノースティリス", "North Tyris") ) {
    mdatan(MDATAN_NAME) = lang("わが家", "Your Home")
}
```

`:1396` è un **confronto contro un valore serializzato**, quindi va rinviata —
è la regola che la rete 7 impose ai nove `CDATAN_NEWSEX` nella 41ª. `:1397` è un
**assegnamento**, cioè testo che si stampa, e si rende. La rete 7 guarda il
sito, non la stringa.

### ⚠️ E allargare la guardia NON basta: quella riga non viene mai eseguita

La prima toppa allargava la condizione di `:1396` con
`| mdatan(MDATAN_NAME) == "Your Home"`, e sembrava risolvere. Non risolveva.
`map.hsp:1325`-`:1344` è il bivio fra caricare e generare:

```hsp
existwrapper exedir + "tmp\\mdata_" + mid + ".s2"
if ( strsize != (-1) ) {        ; la mappa esiste su disco
    gosub *game_ctrlFile        ; la carica, mdatan compreso
    ...
    goto *map_preBegin          ; <-- SALTA *map_init_main
}
*map_init_main                  ; <-- la guardia sta qui
```

Casa tua è **persistente**: dalla seconda visita in poi il file `mdata_*.s2`
c'è, si passa sempre dal ramo di sinistra, e `:1396` resta lettera morta. Serve
alla sola **generazione** e al giro di `mapupdate` (`:1332`, cambio di versione
della mappa) — per questo la prima toppa resta e non si toglie.

✅ La migrazione vera sta a `:1328`, **subito dopo `gosub *game_ctrlFile`**:

```hsp
if ( gdata(GDATA_AREA) == AREA_HOME ) {
    if ( mdatan(MDATAN_NAME) == "Your Home" ) {
        mdatan(MDATAN_NAME) = mapname(gdata(GDATA_AREA))
    }
}
```

⭐ **E non aggiunge nessuna `lang()`**: il valore giusto lo sa già `mapname()`,
che `:1401` usa per tutte le altre aree. Copiarlo da lì evita di scrivere
l'italiano nel sorgente, evita una firma nuova che il dizionario non avrebbe, e
tiene la migrazione allineata a `text.hsp` qualunque cosa succeda a quella resa.

### Cosa resta

⭐⭐ Sono le **prime due toppe di migrazione** del progetto: le altre 306
correggono un errore di monte, queste convertono un **dato vecchio**.

💡 **A dirmi che la prima non bastava è stato lo schermo**, non il codice: dopo
averla applicata il log diceva «Entri qui: **Casa tua**.» (`:1048`, ramo
`mapname()`) e due righe sotto ancora «Vuoi lasciare **Your Home**?»
(`action.hsp:2183`, che legge `mdatan`). Nessuna misura poteva vederlo.

⚠️ **La domanda aperta**: quanti altri valori serializzati portano testo inglese
scritto dentro un salvataggio vecchio? `mdatan` è uno; `cdatan(CDATAN_NAME)` è
un altro, e per quello il progetto ha già accettato che i personaggi **già
generati** tengano il nome vecchio (tutto il bestiario funziona così). Nessuno
ha mai fatto l'elenco.

---

## Il mestiere del negoziante non si traduce: si traduce la bottega — 2026-08-15, quarantaduesima sessione

L'inglese compone il nome dei negozianti come «Gilbert the baker», con
`sncnv()`, che prende la **prima parola** del nome (`text.hsp:417`:
`strmid(arg, 0, instr(arg, 0, " ")) + " "`).

Il primo giro del lotto `map-002` traduceva il mestiere: «il tintore», «lo
stalliere», «il ricettatore», «lo scriba di grimori».

⚠️ **Sarebbe stato un errore, perché metà dei negozianti di Elona sono
femmine**, e il gioco assegna il sesso a caso.

✅ **La soluzione era già scritta, e segue il giapponese.** `text.hsp:420`-`:460`
rende **undici** mestieri della famiglia `sn*` nominando il **negozio**, che è
quel che dice il giapponese (「パン屋の」 = «della panetteria»):

| inglese | giapponese | resa |
|---|---|---|
| `the baker` | パン屋の | della panetteria |
| `the Innkeeper` | 宿屋の | della locanda |
| `the trader` | 交易店の | dell'emporio |
| `the blacksmith` | 武具店の | dell'armeria |
| `the general vendor` | 雑貨屋の | della merceria |

Il nome del negozio ha un **genere fisso suo**, e chi ci lavora resta senza
genere. Le nove nuove della 42ª seguono: «della tintoria», «della stalla»,
«della bottega dei ladri», «della bottega dei grimori», «del banco ambulante»,
«del negozio di souvenir», «del caffè», «dell'arena», «della bancarella».

💡 È la strada del **nome di genere fisso** della 40ª — «pelle», «corpo»,
«aria», «Balia delle bestie» — trovata però **già percorsa**: bastava guardare
la famiglia `sn*` invece di inventare. Vedi [[termini-non-frasi]].

⚠️ **Il confine**: vale per il suffisso appiccicato a un nome di persona. Quando
è il **nome intero della creatura** (`cdatan(CDATAN_NAME, rc) = lang(...)`), il
progetto usa da sempre nomi di ruolo con l'articolo — «il guerriero di Elea»,
«la cavia» — e quelli un genere ce l'hanno. Sono due siti diversi.

---

## Il giapponese è l'arbitro sul contenuto, ma la coerenza lo batte — e un enigma si ri-storpia — 2026-08-15, quarantaduesima sessione

`map.hsp` ha **sette appiattimenti** dell'inglese in un file solo: «Hall» per
cinque piani diversi, «The Eternal Seal» per tre stati dello stesso posto,
«basement» per una cantina **e per un covo di demoni**, «The Mine» per una
miniera **e per un presidio militare**, «tester» per **quattordici Meshera con
nome proprio**. Il giapponese distingue, l'inglese fonde.

La regola del progetto — decidere sul giapponese quando le due lingue divergono
— vale, ed è servita in tutti e sette i casi. ⚠️ **Ma non è «tradurre dal
giapponese», e in una notte si è rotta quattro volte.**

### Le quattro volte in cui il giapponese ha perso

| riga | il giapponese diceva | ha vinto | perché |
|---|---|---|---|
| `map.hsp:5839` | 「仮」, «provvisorio» | l'inglese | è un **segnaposto di sviluppo**: il giapponese non è una fonte, è un `TODO` |
| 神の間 | «la stanza del dio» | «il Sigillo Eterno» | `text.hsp` l'aveva già scelto, seguendo l'inglese, in due righe di trama |
| ネヘルタード | «Nehertard» | «Amurdad» | il nome inglese è già in **sei righe** del progetto |
| `map.hsp:9914` | «è rotolato fino ai tuoi piedi» | «viene posato per terra» | `text.hsp:3` ha la **stessa firma** già resa, e la rete 3 l'ha fermato |

💡 Le ultime due non le ho decise io: le ha imposte la **rete 3**. Senza quella
guardia avrei scritto due rese migliori prese da sole e **peggiori per il
gioco**.

### Il controesempio che tiene onesta la regola

I tredici sussurri di `map.hsp:10511`-`:10547` sono indizi di un enigma, e sono
**volutamente mangiati in tutt'e due le lingue**: 「みぎの…どに……」 è
「右の**かど**に」 con due sillabe sparite, e l'inglese fa «...ig...t co....r...».

✅ La resa italiana li **ri-storpia** — «...ang...o de..ro...» — tenendo in piedi
solo quel che il giocatore deve poter riconoscere.

⚠️ **Tradurre la frase intera sarebbe stato l'unico modo di sbagliare**: il
gioco regalerebbe in italiano una risposta che in giapponese e in inglese si
paga.

💡 **Quindi il criterio non è «rendere il testo più ricco».** È rendere quel che
il gioco intende dire, **compreso quando intende non dirlo**. Chi legge questa
pagina cercando il permesso di abbellire non lo trova.

---

## Il perimetro dichiarato non è il gioco: 47% e 35% sono due risposte diverse — 2026-08-14, trentottesima sessione

Alla domanda «a che punto siamo» il progetto ha sempre risposto con
`verifica --dizionario` e `avanzamento.md`, cioè contando quel che passa da
`lang()`. Misurato per intero con **`scratchpad/perimetro.py`**, quel numero è
**47%**: 10.940 firme rese su ~23.089.

⚠️ **Ma due blocchi di testo che il giocatore legge non sono mai stati contati
da nessuna parte**, e non per una dimenticanza: per come sono scritti.

1. **Le descrizioni degli oggetti — 5.284, zero tradotte.** `db_item.hsp` le
   scrive `description(0..3) = "..."` dentro un `if ( jp ) { ... } else { ... }`,
   **non** dentro `lang()`. `estrai.py` cerca `lang()`, quindi non le vede: non
   sono tradotte **e non risultano fra quelle da fare**. Sono 10.568 righe in
   tutto, 5.284 per lingua, ed è il testo lungo del rapporto d'identificazione.
   💡 È la stessa struttura che `else_jp.py` conta come «6.840 righe di
   `db_item.hsp` già dichiarate fuori perimetro»: quel referto le vedeva, ma le
   dichiarava fuori senza mai dire **quante voci** fossero.
2. **I quattro file di `data/` — ~2.900 righe inglesi, 118.000 caratteri, zero
   tradotte.** `book.txt` (i 33 libri, 67.184 caratteri d'inglese), `talk.txt`
   (i dialoghi legati alle aree), `exhelp.txt`, `board.txt`. Non stanno nel
   sorgente: il gioco li carica con `noteload` a runtime (`item.hsp:112`,
   `command.hsp:8371`, `text.hsp:9360`, `help.hsp:227`). `SPEC.md` §6 li chiama
   «aggiuntivi» e non li ha mai aperti; `text.hsp` ha **2 firme che aspettano
   `talk.txt`** ed è per questo che risulta «100% meno due».

**Contando tutto, il totale è ~31.306 e la traduzione è al 35%.**

> 💡 **Le due risposte sono tutt'e due vere e vanno tenute distinte.** *«Quanto
> manca del lavoro impostato»* → 47%. *«Quanto manca perché il gioco sia in
> italiano»* → 35%. Dare la prima quando è stata chiesta la seconda fa sembrare
> il progetto a metà quando è a un terzo.

⚠️ **E in caratteri il divario è peggiore di così.** Le 5.284 descrizioni e i
118.000 caratteri esterni sono **prosa continua**, non righe di log: sommati
valgono probabilmente più di tutto quello che è stato tradotto finora. Il conto
per firme li fa sembrare un quarto del lavoro e sono molto di più.

💡 **La contropartita, ed è grossa**: sono il lavoro **meno insidioso** del
progetto. Niente `name()` da accordare, niente participi che concordano col
giocatore, niente `itemname()` che si porta l'articolo, niente reti da far
scattare. Il costo è tutto in volume, non in analisi — l'opposto esatto di
`proc.hsp`, dove ogni riga costa una lettura del sorgente. ⚠️ Ma vogliono una
**catena di strumenti diversa**: le descrizioni non hanno firma `lang()` e i
file di `data/` non passano né da `estrai.py` né da `applica.py` né dalla prova
d'identità.

⚠️ **Il numero di firme è una stima e sbaglia per difetto del 2-4%**, perché
conta gli argomenti inglesi distinti di ogni `lang()` con un analizzatore di
parentesi mentre `estrai.py` ne trova qualcuno in più. Tarato sui file chiusi:
`item_data.hsp` 318 su 318 esatto, `db_creature.hsp` 3.507 contro 3.651,
`text.hsp` 1.706 contro 1.738, `action.hsp` 1.266 contro 1.286.

---

## Una variabile può portarsi dentro l'inglese, e non la vede nessun referto — 2026-08-14, trentottesima sessione

Il lotto 017 stava per rendere `proc.hsp:16991` interpolando `studybuddy`, come
fa l'inglese. Venti righe sopra:

```hsp
16976: if ( studybuddy == "" ) { studybuddy = name(tc) }
16980: else                     { studybuddy = "your friends" }
16991: txt lang("あなたと仲間たちは読書会を始めた。",
                "You started a reading party with " + studybuddy + ".")
```

Il ramo `else` — cioè **ogni volta che i compagni sono più di uno** — mette un
letterale inglese **fuori da `lang()`**. A schermo sarebbe uscito «Cominci un
circolo di lettura con **your friends**.»

È la classe di `his2()` della 36ª e di `bufftxt(1)` della 28ª — inglese che
nessun dizionario raggiunge — ma in una forma nuova: **non una funzione che
restituisce inglese, una variabile che se lo porta dentro.**

⚠️ **E qui sta il punto che vale oltre il caso**: non la vede nessuno dei due
referti esistenti. `blocchi_en.py` cerca i letterali dentro `if ( en )`,
`else_jp.py` quelli dentro `if ( jp ) ... else`, e `:16980` **non sta in
nessuna delle due forme** — è un assegnamento incondizionato, codice che gira in
tutte e due le lingue. Era un terzo punto cieco, e nessuno l'aveva cercato.

✅ Misurato con **`scratchpad/variabili_en.py`**: **66 variabili** si portano
dentro un inglese nudo, **3 arrivano dentro una `lang()`**, tutt'e tre lette a
mano e vere:

| dove | variabile | che cosa esce a schermo |
|---|---|---|
| `proc.hsp:16991` | `studybuddy` | ✅ evitato nel lotto 017, reso sul giapponese |
| `proc.hsp:19178` | `performerpal` | il **gemello identico** sull'ensemble, stesso `"your friends"`. ⚠️ Zona `19000-19999`, **ancora da tradurre** |
| `economy.hsp:319` | `s1` | «Neutral»/«Law»/«Chaos», in **tutt'e due** i rami di `lang()`: inglese anche nella build giapponese |

⚠️ **Il referto è nato sbagliato due volte, e tutt'e due gli sbagli insegnano
qualcosa.**

1. **Accoppiava le variabili per file** e contava 8 trappole. Ma `s` è la
   variabile di comodo di tutto il sorgente: accoppiava un `s = "Have"` di
   `chara_func.hsp:11043` con una `lang()` di `:7724` che sta in un'altra
   routine e parla d'altro. ✅ Stretto **all'assegnamento più vicino dentro la
   stessa routine** — la stessa lezione che la rete 8 aveva imparato nella 37ª
   per `valn`, e che vale ogni volta che si incrocia una variabile con un sito.
2. **In HSP si scrive in una variabile anche senza `=`.** A `main.hsp:4468` il
   `s` viene da `noteget s, p + 2` due righe sopra, non dal `s = "no entry"` di
   `:4449`: il referto denunciava una trappola che non c'è. ✅ Adesso un comando
   con la variabile come **primo argomento** ferma la ricerca all'indietro.

💡 **Due limiti dichiarati nel modulo**, perché il numero non è una garanzia:
conta solo l'assegnamento più vicino (se il ramo inglese non è l'ultimo, la
trappola non si vede) e solo la forma `nome = "testo"` su una riga sola.

---

## Una riga spenta non è solo una riga che comincia per `;` — 2026-08-14, trentasettesima sessione

La rete 6 nasce nel lotto 006 su `proc.hsp:4958`, il blocco `MANUSCRIPT HINT`
commentato riga per riga, e da allora controlla una cosa sola: che la riga della
voce non cominci per `;`. Nel lotto `014` `proc.hsp:11796` l'ha passata, ed era
testo morto:

```hsp
/********** ORIGINAL - BEGINNING ********** // Remove skill bonus limit.
...
        txt lang("注意！スペルボーナスは100以上あると新たに獲得できない。", "Caution! ...")
...
 ********** ORIGINAL - ENDING **********/
```

È il modo con cui **il mod spegne il codice di monte**: non commenta le righe una
per una, le avvolge in un `/* ... */`. Le uniche righe vive di quel tratto sono
`:11773`, il messaggio che i 5 punti li dà, e `:11787`, il `+= 5` che li assegna:
il tetto di 100 il mod l'ha tolto, e con lui l'avviso.

✅ `scratchpad/commenti-blocco.py` trova le righe coperte da un blocco, e la rete
6 adesso le rifiuta. `proc.hsp` ne ha **99**, `action.hsp` 132,
`custom_tweaks.hsp` 100.

💡 **E la domanda «era già successo?» ha una risposta: sette volte.** Sei voci in
`action.hsp` e `proc.hsp:1000` — la versione originale dell'incasso delle
esibizioni, sostituita dal blocco `ANNA CUSTOM` — sono tradotte dentro un blocco
spento. Non è un difetto a schermo: è lavoro speso su testo che il giocatore non
legge.

### ⚠️ E la misura ha ingannato prima di dare il numero giusto

Fatta sulla **build** ne accusava **nove**, e le due di `text.hsp` erano giuste.
La build di `text.hsp` ha **una riga in più** del sorgente — 12.528 contro
12.527 — perché una toppa ce l'ha aggiunta, e da lì in giù i numeri di riga del
dizionario, che vengono dal **sorgente pinnato**, non tornano più.

> Chi incrocia numeri di riga e dizionario deve leggere il `SORGENTE`, non la
> build. `proc.hsp` e `action.hsp` hanno lo stesso numero di righe nelle due
> copie e il problema non si vede; `text.hsp` no, e non c'è nessuna guardia che
> lo dica.

⚠️ **Vale anche per `dossier.py`**, che oggi legge la build per mostrare il
contesto: su `text.hsp` mostrerebbe la riga sbagliata.

---

## Il genitivo davanti a `name()` non esiste, e sei rese lo scrivevano — 2026-08-14, trentasettesima sessione

`init.hsp:1717` diceva `return "the " + cdatan(CDATAN_NAME, name_arg1)`, e una
toppa della Fase 1 toglie il `"the "`: in italiano l'articolo dipende da genere
ed elisione, quindi lo porta **il nome della creatura** (`db_creature.hsp`: «il
cultista del fuoco», «la medusa purificata»). Da quel momento `name(x)` e
`cdatan(CDATAN_NAME, x)` restituiscono la **stessa identica stringa**, articolo
compreso — ed è per questo che la rete 8 le tratta uguali.

La conseguenza è che **nessuna preposizione semplice può stare davanti a un
nome**: «di » + `name(tc)` stampa «di il putit», e «del » stamperebbe «del
Sinaha». Il genitivo, in questa lingua, non è disponibile.

La rete 8 lo impedisce dal lotto 009. ⚠️ **Ma nessuno l'aveva mai passata su
quello che c'era prima**, e `scratchpad/rete8_dizionario.py` trova **sei
preposizioni in cinque rese**, tutte visibili a schermo:

| dove | stampava |
|---|---|
| `action.hsp:11810` | «Hai dato istruzioni **a il** putit» |
| `action.hsp:12706` | «i movimenti **di il** putit» |
| `action.hsp:18997` | «i geni **di il** … **in il** …» |
| `action.hsp:19004` | «i geni **di il** putit» |
| `proc.hsp:1966` | «piomba giù **su il** putit» |

✅ Corrette girando la frase: il nome diventa **soggetto** o **complemento
oggetto**. La strada era già stata aperta senza dichiararla da `proc.hsp:8759` e
`:8786`, che usano il **`-ne` enclitico** — «morde X succhiando**ne** il sangue».

⚠️ **Otto segnalazioni su quattordici erano falsi positivi**, e vanno sapute
perché la misura si rifarà: «**con**» non si fonde in italiano moderno («con il
putit» è corretto, «col» è facoltativo); «Hai tirato **su** » + `itemname` è un
**verbo sintagmatico**; e `valn = skillname(i)` non porta articolo, quindi «il
potenziale **di Forza**» è giusto.

### ⚠️ E la guardia che mancava sotto tutto questo

`verifica --dizionario` **non valida le rese**: confronta il dizionario col
sorgente e conta orfane e non tradotte. Una correzione scritta a mano nel
dizionario — cioè tutte quelle di `correzione-*.py` — **non incontrava nessuna
guardia**. Adesso gli script di correzione passano le rese nuove a
`controlla_lotto`, che è quello che il lotto fa da sempre.

---

## Il compilatore ha visto quello che undici reti non vedevano — 2026-08-14, trentasettesima sessione

`proc.hsp:11534` è classificata **dinamica** perché l'inglese porta `his(tc)`:

```hsp
txt lang("幾つかのアイテムが浄化された。", "The aura uncurses some " + his(tc) + " stuff.")
```

Ma `his(tc)` a un argomento è **morfologia**, e in italiano sparisce: quello che
resta è una frase sola, senza nessuna funzione. Scritta come testo nudo —
`Qualche oggetto è stato purificato.` — ha passato le undici reti, `verifica` e
le tre guardie, perché **nessuna di loro guarda la forma HSP della resa**.
`applica.py`, che per le dinamiche non avvolge niente fra virgolette, l'ha
infilata come **codice**:

```
proc.hsp(11534) : error 4 : パラメーター式の記述が無効です
#未初期化の変数があります(qualche)
```

Il compilatore ha letto «qualche» come nome di variabile.

✅ **Rete 12**: la resa di una dinamica deve contenere almeno una `"`.

> È il primo difetto della serie che **solo il compilatore poteva vedere**, e
> arriva dopo la lezione della 34ª (la catena verde non dice niente sulla lingua
> che il giocatore legge) e della 35ª (non dice niente sulla coerenza fra due
> file). Adesso: **non dice niente su come la resa entra nel sorgente**.

---

## Quando due reti si contraddicono, a decidere è il sorgente — 2026-08-14, trentasettesima sessione

`proc.hsp:12837` e `:13298` hanno lo **stesso giapponese**:

```
name(tc) + "は咄嗟に" + name(cc) + "の攻撃を防いだ！"
```

ma due inglesi diversi: `:13298` nomina tutt'e due i personaggi
(`name(tc) + " fend" + _s(tc) + " off " + name(cc) + your(cc) + " attack!"`),
`:12837` ne nomina **uno solo**, e per giunta **quello sbagliato**
(`name(cc) + " bluntly prevented the attack!"`: dice che a parare è chi attacca).

- La **rete 11** pretende che la resa porti esattamente le funzioni di contenuto
  dell'inglese: a `:12837`, un nome solo.
- La **rete 4** pretende che due siti con lo stesso giapponese dicano le stesse
  parole: con un nome in meno, impossibile.

Le due non possono avere ragione insieme, e **la differenza non la sceglie la
traduzione: la impone il sorgente**. ✅ La rete 4 adesso raggruppa per
`(giapponese, funzioni di contenuto)` e stampa un 💡 quando lo stesso giapponese
ha due firme diverse.

💡 **E a `:12837` la resa segue il giapponese**, perché può: `verifica.py:384`
accetta ogni chiamata che compaia in **una delle due** forme di monte, e
`name(tc)` sta nel giapponese. La regola vale ogni volta che l'inglese nomina il
personaggio sbagliato — è successo cinque volte in questa sessione sola.

---

## «Pieno» non lo dicono né il giapponese né il codice — 2026-08-14, trentasettesima sessione

`action.hsp:1096` rendeva 「name(CHARA_PLAYER)のマナが回復した。」 con «ha di
nuovo il mana **pieno**». L'inglese («mana is restored») non basta a smentirlo, e
per due sessioni nessuno l'ha guardato. Il lotto `016` ha trovato lo **stesso
giapponese** a `proc.hsp:14597`, e a quel punto la domanda è diventata: pieno
rispetto a che cosa?

Il codice risponde in una riga, tutte e due le volte:

- `action.hsp:1095` — `healmp 0, inv(INV_ITEM_CHARGE, ci) * 5 * inv(INV_ITEM_NUM, ci)`
- `proc.hsp:14594` — `healmp tc, cdata(CDATA_MAX_MP, tc) / 10 + rnd(sdata(SKILL_ATTR_MAG, tc)) + 5`

Nessuno dei due riempie la barra, e 回復した significa «si è ripreso», non «è
pieno». ✅ Tutt'e due dicono «recupera mana».

> È la regola della 33ª applicata a una resa già entrata: **per una riga che
> descrive un effetto l'arbitro non è una lingua, è il codice.** Lì aveva
> corretto tre `buffdesc` su 63; qui corregge una resa che nessuna guardia
> poteva mettere in dubbio, perché era coerente con l'inglese.

---

## `his2()` porta il nome ma non passa da `lang()`: una funzione che non si traduce — 2026-08-14, trentaseiesima sessione

Il lotto `013` ha scritto una resa per `proc.hsp:11481` leggendo l'inglese

```hsp
his2(tc) + your2(tc) + " equipment is surrounded by a white aura."
```

come il gemello di `:10312` del lotto precedente: pronomi morfologici che
cancellano il nome, quindi frase italiana senza soggetto. **La rete 11 l'ha
bocciata** — «mancanti `['his2']`» — e la funzione mancante era la prova che la
lettura era sbagliata. `init.hsp:1881`:

```hsp
#defcfunc his2 int EntityID
    if ( EntityID == CHARA_PLAYER ) { return "your" }
    return name(EntityID)
```

⚠️ **`his2()` non è morfologia: porta il nome.** Per questo `funzioni.py` la
tiene fuori da `MORFOLOGIA_INGLESE` e `verifica` pretende che resti nella resa —
ed è giusto, perché toglierla perderebbe il soggetto. Ma nel ramo del giocatore
restituisce il letterale nudo `"your"`, **fuori da qualunque `lang()`**.

> Quel `your` resta inglese **per sempre**: non lo raggiunge il dizionario oggi
> e non lo raggiungerà la traduzione di `init.hsp` domani, perché non c'è
> niente da tradurre.

È la stessa classe di `bufftxt(1)` della 28ª e delle 23 righe `if ( en )` della
35ª — un letterale inglese fuori da `lang()` — **in una forma nuova: dentro una
funzione.** E questa forma nessuno strumento la vede: `blocchi_en.py` misura la
struttura del **sorgente**, non quello che una `#defcfunc` restituisce.

⚠️ **E non esiste una resa italiana che regga tutt'e due gli esiti**, perché
`his2()` dà un **possessivo** in un caso («your») e un **nome proprio con
l'articolo** nell'altro («il putit»): non c'è slot di frase dove ci stiano
entrambi. In inglese funziona perché `"your equipment"` e `"the putit's
equipment"` hanno la stessa forma — il possessivo prenominale — che l'italiano
non ha.

💡 **La strada è la toppa**, che riporta la riga alla forma del ramo giapponese
(「name(tc)の装備品は…」, un nome solo) e la rende una frase normale. Fatta nella
36ª insieme al rinvio: `rinviate.jsonl` 12 → 13, `toppe.jsonl` 301 → 302.

⚠️ **La domanda che resta aperta, e che è misurabile:** `his2` e `your2` sono
due `#defcfunc` di `init.hsp` che restituiscono inglese senza `lang()`. **Quante
sono in tutto?** Nessuno le ha mai contate, e ognuna è una famiglia di siti che
sembrano tradotti e non lo sono. È il gemello di `blocchi_en.py` un livello più
in basso.

💡 **E il valore della rete 11 sta qui.** Era nata nel lotto `012` per dire «non
aggiungere funzioni di contenuto»; un lotto dopo ha detto «ne manca una», e
quella era la prova di un difetto strutturale che nessuna lettura a occhio
avrebbe trovato — perché la riga, letta, sembra solo inglese da tradurre.

---

## La maiuscola d'ufficio non gira, e non girava da sempre — 2026-08-14, trentaseiesima sessione

Il collaudo delle 235 rese della 35ª ha mostrato, a ogni riga del log:

> `[19:07] il viandante finisce di mangiare una razione.`
> `[17:19] il viandante get wet.`

Minuscolo a inizio riga. E non è una resa sbagliata: **tutte** le rese che
cominciano con `name(cc)`, `itemname()` o `valn` escono così, e tutte le maiuscole
che si vedono nel log erano già maiuscole nel dizionario.

La ripresa registrava il contrario — «ogni resa che comincia per minuscola verrà
maiuscolata d'ufficio (`init.hsp:1659-1661`)» — ed è vero solo con **l'orologio
del log spento**:

| riga | cosa fa |
|---|---|
| `init.hsp:1569` | `if ( cfg_msgaddtime ) {` |
| `init.hsp:1578` | `msgtemp = "[" + ora + ":" + minuti + "] " + msgtemp` |
| `init.hsp:1659` | `b = peek(msgtemp, 0)` … `if ( b >= 97 & b <= 122 )` |

Il prefisso si attacca **81 righe prima** del controllo, e a quel punto
`peek(msgtemp, 0)` legge `[`, cioè 91, che non cade in 97-122. Con
`cfg_msgaddtime` acceso la maiuscola automatica **non scatta mai, su nessuna
riga, in nessuna lingua**.

⚠️ **Non è un difetto nostro.** Upstream ha `name(CHARA_PLAYER) = lang("あなた",
"you")` — minuscolo — e conta esattamente su quella maiuscola: con l'orologio
acceso anche l'inglese di monte scrive «`[19:07] you finish eating.`». Il difetto
è di upstream e nessuno l'ha mai notato perché `you` minuscolo a inizio riga si
legge come una svista tipografica. In italiano no: `name()` rende **«il
viandante»**, un sintagma articolo + nome che a inizio riga si legge come un
errore di grammatica, e compare a ogni riga del log.

💡 **La toppa maiuscola prima che i prefissi si attacchino**, subito dopo
`tnew = 0` (`init.hsp:1568`), che è il punto in cui il codice ha appena deciso
che sta cominciando **una riga nuova**:

```hsp
tnew = 0
if ( en ) {
	if ( tcontinue@txtfunc == 0 ) {
		b@txtfunc = peek(msgtemp, 0)
		if ( b@txtfunc >= 97 & b@txtfunc <= 122 ) {
			poke msgtemp, 0, b@txtfunc - 32
		}
	}
}
if ( cfg_msgaddtime ) {
```

Le due guardie sono copiate dall'originale e non inventate: `if ( en )` perché il
ramo giapponese non vuole maiuscole latine, `tcontinue == 0` perché una
continuazione non è un inizio di frase — è la stessa condizione di `:1659`. Il
controllo originale resta dov'è e **diventa muto**: vede `[` e non tocca niente.
Con l'orologio spento continua a funzionare lui, e la toppa ha già fatto il
lavoro. E la posizione sceglie da sola anche il prefisso `"(N min left) "` delle
missioni a tempo (`:1573`), che si attacca dopo.

> La lezione è la stessa della 34ª e della 35ª in una terza forma. La 34ª: la
> catena verde non dice niente sulla lingua che il giocatore legge. La 35ª: non
> dice niente sulla coerenza fra due file. Qui: **non dice niente su un'opzione
> del giocatore**. Nessuna verifica accende `cfg_msgaddtime`, e il difetto vive
> o muore su una casella delle impostazioni.

⚠️ **Materiale da guardia, non chiuso:** nessuno strumento misura le rese che
cominciano con una variabile. Finché la toppa regge non serve, ma se qualcuno la
togliesse non protesterebbe niente.

---

## `valn` da soggetto vuole l'articolo determinativo, e `itemname()` non lo dà — 2026-08-14, trentaseiesima sessione

A schermo, bevendo a un pozzo:

> `Un pozzo disseta <Sinaha>.`

La 35ª aveva scoperto che `valn` è un `itemname()` (`proc.hsp:6950`, `:6965`,
`:6970`) e aveva girato le tre frasi promuovendolo da **complemento** a
**soggetto** — «Il pozzo disseta il viandante» invece di «beve dal pozzo» — per
non dover mettere `di`/`da` davanti a un nome che si porta l'articolo. La resa
era giusta; **l'articolo che arriva a runtime no**.

`itemname()` sceglie così (`item_func.hsp:1944-1958`):

| condizione | articolo |
|---|---|
| `KNOWN_FULL` **e** qualità ≥ `MIRACLE` | determinativo (`ioriginalnamearticolodet`) |
| tutto il resto, con quantità 1 | **indeterminativo** (`ioriginalnamearticolo`) |

È il calco esatto dell'inglese — `a well` contro `the Painful Master` — e nello
stesso log del collaudo si legge infatti `l'amuleto ingioiellato <Painful
Master>` col determinativo giusto. Finché il pozzo era **complemento** (`draw
water from a well`) l'indeterminativo andava bene. Da **soggetto** no: «Un pozzo
disseta X» non è italiano.

⚠️ **E non si aggiusta dal dizionario**, perché l'articolo non sta in nessuna
resa: nasce a runtime, fuori da `lang()`. È la stessa classe di `bufftxt` della
28ª — un difetto che sembra una traduzione e invece è struttura.

💡 **Il dato per farlo c'era già, scritto da noi e mai usato in questo modo:**
`ioriginalnamearticolodet` esiste accanto a `ioriginalnamearticolo` per **1.309
voci** di `db_item.hsp` (`"il "` per pozzo e pozzo sacro, `"la "` per la fontana,
e l'elisione `"l'"` dove serve). E `itemname(ci, 1, 1)` restituisce il nome
**nudo**: il terzo argomento salta tutto il blocco degli articoli, ed è l'idioma
che upstream usa già per «your X is damaged» (`chara_func.hsp`). Tre toppe di due
righe:

```hsp
valn = ioriginalnamearticolodet(inv(INV_ITEM_ID, ci)) + itemname(ci, 1, 1)
```

⚠️ **Le tre assegnazioni sono identiche riga per riga**, quindi ognuna ha avuto
la sua toppa con la riga di `if` sopra come aggancio: `applica.py` rifiuta per
costruzione un `cerca` che compare più di una volta, ed è la rete che ha imposto
la forma giusta invece di lasciar toppare a caso.

💡 **La domanda che resta aperta**, e vale per ogni resa futura che usi un
`itemname()` come soggetto: *quante altre ce ne sono?* Nessuno strumento distingue
un `itemname()` in posizione di soggetto da uno in posizione di complemento, e la
differenza non si vede leggendo la riga.

---

## Una regola scritta e non sorvegliata: `Bolt` era «Saetta» e «dardo» insieme — 2026-08-14, trentacinquesima sessione

Traducendo il log di combattimento (`fase4-proc-010`) serviva la resa di 「ボルト」
per «The bolt hits X». Cercandola in dizionario ne sono uscite **due, dodici e
dodici**:

| | `skill.hsp` (l'incantesimo) | `db_item.hsp` (il libro) |
|---|---|---|
| アイスボルト | Saetta di **gelo** | dardo di **ghiaccio** |
| ダークネスボルト | Saetta **d'oscurità** | dardo **oscuro** |
| ポイズンボルト | Saetta **velenosa** | dardo **di veleno** |
| ナーブボルト | Saetta **dei nervi** | dardo **neurale** |
| マジックボルト | Saetta **magica** | dardo **arcano** |
| (le altre sette) | Saetta di fuoco, … | dardo di fuoco, … |

Il giocatore compra il libro del **dardo** e impara la **saetta**, ed è la stessa
magia. E in cinque casi su dodici non cambiava solo la testa: cambiava anche il
qualificatore. Non erano dodici parole sbagliate, erano **due famiglie
parallele**.

⭐ **La cosa che rende questo caso interessante è che la regola c'era già.**
`glossario.md` §«I nomi degli incantesimi» dice `Bolt` → `Saetta` dal 2026-08-09,
e spiega pure quando l'elemento va aggettivo e quando complemento. `db_item.hsp`
non l'ha mai seguita. Non è stata una decisione presa due volte in due modi: è
una decisione presa **una volta e poi non applicata**, per otto mesi di sessioni,
senza che niente protestasse.

> Il difetto non è nel dizionario e non è nel glossario. È che **nessuno
> strumento li confronta.**

⚠️ E `battute --divergenti`, che sarebbe la guardia naturale, non poteva vederla:
misurato nella 29ª, `rese_gia_decise()` apre `db_creature.hsp` e basta. Il numero
13 non copre il dizionario intero, e questa è la prova su un caso vero.

**Deciso: vince `skill.hsp`**, per due motivi. È la lista che il giocatore apre a
ogni lancio, mentre il libro lo legge una volta sola; e i suoi dodici nomi sono
già coerenti fra loro. Corretti con `scratchpad/correzione-bolt.py`, che cambia
tre campi per voce — `it`, `plurale` e **`genere`**, perché «saetta» è femminile
dove «dardo» era maschile.

💡 **Il genere non muove l'articolo, e valeva la pena verificarlo invece di
sperarlo.** `applica.ARTICOLO_DI` mette l'articolo **solo sulla testa** del nome
composto, che qui è `ioriginalnameref2` — «grimorio», «bacchetta». Controllato
nell'albero di build dopo la correzione: `ioriginalnamearticolo(...
SPELLBOOK_OF_NETHER_BOLT) = "un "` e `... ROD_ICE_BOLT) = "una "`, cioè l'articolo
segue ancora la testa e non la saetta. Il `plurale` invece viaggia su tutti i
siti ed è stato rifatto al femminile («saette velenose», «saette caotiche»).

### ⚠️ E la prima passata ne ha corrette 12 su 15, perché cercava nella lingua sbagliata

Cercando 「ボルト」 nel **giapponese** si trovano i dodici libri. Non si trovano le
tre **bacchette**, perché il loro nome giapponese è poetico e il katakana non c'è
dentro affatto:

| oggetto | giapponese | inglese | diceva |
|---|---|---|---|
| `ITEM_ID_ROD_LIGHTNING_BOLT` | 稲妻の軌跡の魔杖, «la scia della folgore» | `lightning bolt` | dardo di fulmine |
| `ITEM_ID_ROD_FIRE_BOLT` | 炎の衝撃の魔杖, «l'urto della fiamma» | `fire bolt` | dardo di fuoco |
| `ITEM_ID_ROD_ICE_BOLT` | 氷の視線の魔杖, «lo sguardo del gelo» | `ice bolt` | dardo di ghiaccio |

> Quando la famiglia è definita dall'**effetto** e non dal nome, si cerca nella
> lingua che nomina l'effetto. Qui è l'inglese, ed è l'eccezione alla regola
> «arbitra il giapponese»: il giapponese qui non nomina la magia, nomina
> l'oggetto.

La rete 2 dello script adesso lo impedisce: elenca ogni voce di `db_item.hsp` il
cui **inglese** contiene `bolt` e muore se una non sta né fra le correzioni né
fra le due dichiarate estranee — `146183` (`bolt` = i dardi da balestra) e
`151150` (`magic missile`, che è 魔法の矢 / `Magic Dart`, e «Dardo magico» è
giusto: è l'altra metà della distinzione che il glossario chiede di tenere).

💡 **I nomi giapponesi delle bacchette erano già andati persi prima di questa
correzione** e non li recupera: 泡沫の波動 («l'onda di spuma») è reso «sfera di
bolle», che viene da `bubble ball`. Chi vorrà rimetterli ha qui l'elenco di dove
guardare.

---

## Un tetto misurato in un sito solo non è il tetto — 2026-08-14, trentaquattresima sessione

La 33ª aveva accettato due `buffdesc` lunghi con questo argomento: il tetto della
lista abilità è **34**, **46 inglesi su 63 lo sfondano già**, quindi la
troncatura è una cosa che upstream accetta e non introduciamo un difetto nuovo.

L'argomento è giusto. La misura no: **i siti sono quattro e i tetti tre.**

| sito | routine | taglio |
|---|---|---|
| menu `a` (usa abilità) | `*com_applySkill_loop` | `command.hsp:5389` — **34** |
| menu `W` (abilità ad area) | `*com_applyWideSkill_loop` | `:5599` — **34** |
| menu di lancio | `*com_spell_loop` | `:8851` — **40** |
| scheda, pagina incantesimi | `*com_charainfo_loop_WHILE1` | `:10996` — **46** |

⚠️ **E il sito da 34 è quello che conta di meno.** Delle 21 abilità che mostrano
un `buffdesc` invece del proprio `skilldesc` — sono quelle il cui
`sdataref(SKILL_DATAREF_TYPE)` sta fra 1000 e 1999, e `*skill_desc`
(`command.hsp:9004`) le riconosce e compone `dur + "t " + buffdesc` — **solo
quattro sono azioni speciali**. Le altre diciassette sono incantesimi, e gli
incantesimi in quel menu non ci passano: passano dal menu di lancio, tetto 40, e
dalla scheda, tetto 46.

Rimisurato per tetto, con `scratchpad/tetti_buffdesc.py`:

| tetto | italiano sfonda | inglese sfonda |
|---|---|---|
| 34 | 43 su 62 | **46** su 62 |
| 40 | 32 su 62 | **38** su 62 |
| 46 | 23 su 62 | **31** su 62 |

✅ **La conclusione della 33ª regge, e adesso regge su tutti e tre**: l'italiano
sfonda **meno** dell'inglese ovunque. Non c'è niente da accorciare, e accorciare
peggiorerebbe i siti dove la riga ci sta comoda.

💡 **A schermo la troncatura si legge come un refuso, e non lo è.** Nel menu di
lancio escono `Res+ gra`, `Res+ sonno,confu`, `oltretomb`, `Res+ paralisi,ce`:
sono `gravita'`, `confusione`, `oltretomba`, `cecita'` tagliate dentro la parola.
Le stesse righe in inglese si tagliano allo stesso modo, perché il contenuto è un
elenco di dieci resistenze in tutte e due le lingue.

⚠️ Cautela sullo strumento: stima a due cifre le variabili interpolate, quindi i
valori assoluti hanno un margine di ±1 carattere per voce. Il metodo è identico
sulle due lingue, quindi il **confronto** è solido; il conteggio secco no.

> Un tetto non è una proprietà del testo, è una proprietà del **sito che lo
> disegna**. Cercarne uno e smettere di cercare dà un numero vero e una
> conclusione che vale per un sito solo. La domanda giusta non è «qual è il
> tetto», è «**quanti** posti disegnano questa stringa».

È la stessa forma di [[una-guardia-vale-solo-dove-guarda]], applicata a una
misura invece che a una guardia: [[un-tetto-per-sito-non-per-campo]].

---

## Il ramo inglese accoda uno spazio a ogni `txt`, il giapponese no — 2026-08-14, trentaquattresima sessione

La scena ricucita di `proc.hsp` è uscita a schermo così:

```
"Che bello ! Questo e' tutto quello che ho nel portafogli."
```

Le virgolette chiudevano, i tre pezzi si agganciavano, e la frase era comunque
sbagliata: **uno spazio prima del punto esclamativo**.

La causa sta in `init.hsp:1666`, dentro il ramo `else` di `if ( jp )` di
`txt_conv`, cioè **nel solo ramo inglese**:

```hsp
msgtemp += " "
```

Ogni `txt` inglese si porta dietro uno spazio finale. Il ramo giapponese
(`:1595-1647`) non lo fa. Due `txt` consecutivi, in inglese, sono sempre
separati da uno spazio.

⚠️ **E la conseguenza è che la struttura giapponese non si può ricopiare.** Il
giapponese spezza la frase mettendo la punteggiatura sulla **coda**
(「よかった + よ」 poi 「！さあ、小遣いを…」), e funziona perché lì lo spazio non
c'è. Upstream in inglese fa l'opposto — punteggia la **testa** e fa ripartire la
coda con la maiuscola — e non è uno stile: è l'unico modo di non pagare quello
spazio.

| | testa | coda | a schermo |
|---|---|---|---|
| giapponese | 「よかった + よ | ！さあ、小遣いを受け取ってくれ」 | 「よかったよ！さあ…」 |
| upstream EN | `"You are awesome!` | `Here, take this."` | `"You are awesome! Here, take this."` |
| noi, prima | `"Che bello` | `! Ecco, prendi questi spiccioli."` | ❌ `"Che bello ! Ecco…` |
| noi, adesso | `"Che bello!` | `Ecco, prendi questi spiccioli."` | ✅ `"Che bello! Ecco…` |

💡 **La prova che upstream lo sa** sta due righe sopra, a `init.hsp:1659-1661`:
in inglese la prima lettera minuscola di ogni `txt` viene **maiuscolata
d'ufficio** (`poke msgtemp, 0, b - 32`), a meno che non si sia chiamato
`txtcontinue`. Il ramo inglese è progettato perché ogni `txt` sia una frase
nuova. Le nostre code cominciavano per `!`, quindi la maiuscolatura non le
toccava e il difetto non aveva nessuna guardia che lo vedesse.

**Corretto in tre toppe** (le teste di `:3372`, `:3533`, `:3617`, cinque
aperture ciascuna) **e due voci di dizionario** (le code di `:3383`/`:3629` e
`:3389`/`:3635`). Riguardato a schermo lo stesso giorno: esce
`"I-incredibile! Questo e' tutto quello che ho nel portafogli."`

⚠️ **Lo spazio prima della virgoletta di chiusura resta, ed è di monte.** Dove
la coda è il solo segno di chiusura (`txt lang("」", "\"")`, a `:3376`, `:3537`,
`:3621`) a schermo esce `"Che bello! "`. Ce l'ha anche l'inglese di upstream, per
la stessa `msgtemp += " "`, e toglierlo vorrebbe dire un'altra toppa
strutturale. Segnalato, non toccato.

⚠️ **E il `motivo` delle tre toppe diceva la regola sbagliata.** Portava scritto
«la testa va senza punteggiatura finale, come il ramo giapponese: il punto lo
porta la coda», cioè documentava esattamente ciò che ha prodotto il difetto: chi
avesse riletto la toppa avrebbe rimesso lo spazio credendo di correggere. Il
`motivo` è stato riscritto insieme alla toppa.

> Una regola di resa dedotta dal ramo giapponese vale solo se il pezzo di codice
> che la stampa è quello giapponese. Noi compiliamo il ramo inglese: le sue
> abitudini tipografiche sono vincoli, non stile di upstream.

💡 **Vale oltre questa scena.** Qualunque resa italiana che *continui* un `txt`
precedente e cominci per punteggiatura mostrerà lo spazio orfano; qualunque resa
che cominci per lettera minuscola verrà maiuscolata. È materiale da guardia — la
misura su tutto il dizionario non è ancora stata fatta.

Concetto per il vault: [[lo-spazio-lo-mette-il-ramo-che-stampa]].

---

## Il referto guardava una forma sola, e la follia parlava inglese — 2026-08-14, trentaquattresima sessione

Nel log del collaudo, in mezzo alle rese nuove, c'erano `"Forgive me! Forgive
me!"`, `"P-P-Pika!"`, `"You snail!"`, `"Shhhhhh!"`. Vengono da
**`calculation.hsp:2352`**, le battute di chi impazzisce, e non stanno in nessun
conteggio: né fra le «non tradotte» (sono letterali nudi, `estrai.py` non li
vede) né fra le 99 righe di struttura misurate nella 33ª.

Il motivo è che `scratchpad/blocchi_en.py` cerca **`if ( en )`**, e lì la forma è
un'altra:

```hsp
if ( jp ) {
    txt name(r1) + "「ごめんなさいごめんなさい！」", …
}
else {
    txt cnvtalk("Forgive me! Forgive me!"), cnvtalk("P-P-Pika!"), …
}
```

⚠️ **Stessa sostanza, sintassi diversa, e la guardia non la vede.** Misurato con
`scratchpad/else_jp.py`: **144 righe in 12 file**, più 6.840 di `db_item.hsp`
che sono le descrizioni già dichiarate fuori perimetro. Le vive:

| file | righe | che cosa sono |
|---|---|---|
| `command.hsp` | 70 | intestazioni e voci di menu — file a 0%, viaggia col resto |
| `item_func.hsp` | 30 | ✅ **0 intatte**: già toppate da sessioni passate, senza che nessuno sapesse che erano una famiglia |
| `proc.hsp` | 13 | le suppliche di chi viene derubato, gli insulti |
| `text.hsp` | 11 | ✅ 0 intatte |
| `ai.hsp` | 3 | «I'll do anything! Please don't kill me....!» |
| `calculation.hsp` | 2 | la follia vista a schermo, **con `_s()` e `his()`** da togliere |
| `chat.hsp` | 2 | due righe lunghe di lore |
| resto | 8 | URL, chiavi di `#define`, generatori di nomi: rumore |

💡 **La riga di `item_func.hsp` è la lezione**: quella famiglia era già stata
toppata trenta volte, a mano, un caso per volta, senza che il fatto di essere
*una famiglia* fosse mai stato scritto. Un referto che guarda una sintassi sola
non dice «non ce n'è», dice «non ne ho viste **di quella forma**».

⚠️ **Correzione, stessa sessione, un'ora dopo.** Avevo scritto qui che
`calculation.hsp` «non era in nessun elenco di fase» e «non ha firme da
tradurre»: è falso su tutti e due i punti. `SPEC.md` §6 definisce la Fase 4 come
«i restanti **63 file** `.hsp` minori» — una designazione **collettiva**, che
copre per costruzione ogni file non nominato prima; e `calculation.hsp` ha
**44 `lang()`**. Non è `adv.hsp` della 26ª: è Fase 4 non ancora cominciata.

💡 **La misura che chiude la questione sta in `scratchpad/fuori_elenco.py`**: dei
54 file con `lang()`, **40 non hanno un file di dizionario**, per **12.620**
stringhe mai estratte. Non sono file nascosti — sono la coda, e il numero è
grande perché la coda è grande. La domanda «esiste un file che nessun elenco
nomina?» ha risposta **no**, e adesso è una misura invece che una lettura di
`SPEC.md`.

⚠️ **Quello che resta vero è la parte sui letterali nudi**: quelli non sono in
nessun conteggio nemmeno quando il file verrà tradotto, perché `estrai.py` non li
vede. È su quelli che il referto serve, non sull'appartenenza a una fase.

Concetto per il vault: [[una-guardia-vale-solo-dove-guarda]] (già esiste: questa
ne è la seconda istanza, e stavolta il punto cieco era **sintattico**).

---

## La catena verde non dimostra che la build sia tradotta — 2026-08-13, trentatreesima sessione

`reimporta` scrive **solo nel dizionario**. `applica` e' il passo che porta
dizionario e toppe dentro l'albero di build, e `compila` **senza
`--eseguibile`** produce solo `start.ax`. Nessuno dei due sta nel metodo scritto
in `RIPRESA-sessione.md`.

⚠️ **Nella 33ª ho annunciato due volte un `cgx-test.exe` rifatto, e non lo era.**
`compila` rispondeva `#No error detected.`, la catena era verde in ogni valore,
e l'eseguibile in `elonaplus2.31/` era quello di una sessione precedente: ho
letto un timestamp che combaciava e ne ho dedotto una cosa che non avevo
verificato. Scoperto solo aprendo il `.hsp` di build alla riga appena tradotta e
trovandoci ancora l'inglese.

💡 **La catena delle verifiche non poteva accorgersene, ed e' giusto cosi'**:
`prova_identita` legge il **sorgente pinnato**, `verifica` legge il
**dizionario**, `larghezze`/`diario`/`riquadri` leggono la build ma misurano
riquadri, non lingua. Nessuna guarda «la build contiene quello che il dizionario
dice». Sono tutte verdi su una build vecchia.

⚠️ **E `applica` ricrea l'albero da zero**, quindi **cancella l'exe**: dopo un
`applica` senza ricompilazione, in `build/` non c'e' nessun eseguibile. Il
sintomo e' un `Get-ChildItem *.exe` che non stampa niente.

> Un comando che risponde «ok» dice che *quel* comando e' riuscito, non che il
> risultato che ti aspetti esista. L'eseguibile si guarda col timestamp **dopo**,
> non si deduce.

**La sequenza intera**, adesso scritta anche nel metodo: `verifica` → `reimporta`
→ batteria → **`applica`** → **`compila --eseguibile`** → copia in
`elonaplus2.31\cgx-test.exe`.

---

## Ventitre' righe di `proc.hsp` parlano inglese fuori da `lang()` — 2026-08-13, trentatreesima sessione

Tre voci della zona 2601-3400 (`:3376`, `:3383`, `:3389`) sono la **coda** di una
frase la cui **testa** non e' nel dizionario: `:3372` e'

```hsp
if ( en ) {
    txt "\"You are awesome!", "\"Oh my god...", "\"Okay, okay, you win!", "\"Holy...!"
}
```

cioe' letterali **nudi** dentro un blocco `if ( en )`. `estrai.py` non li vede.
Rendere la sola coda darebbe a schermo «`"You are awesome!Ecco, prendi questi.`»

**Misurato su tutto il file: 23 righe**, ognuna con piu' stringhe — i versi della
scena del sesso (`:3319`, `:3487`, `:3574`), i suoni (`:3822`, `:4865`, `:4926`),
le battute di chi ti porta in groppa (`:10768`, `:10781`), le risate
(`:22489`-`:22506`), gli ordini agli alleati (`:26818`, `:26886`). Lo strumento
sta in `scratchpad/blocchi_en.py`.

💡 **E' la scoperta 1 della 28ª — `bufftxt` — in un altro file**, e la
conseguenza e' la stessa: **il conteggio delle non tradotte sottostima il
costo**. `proc.hsp` dice 894, ma quelle 23 righe sono testo che il giocatore
legge e che nessun lotto tocchera' mai.

⚠️ **E la strada e' una toppa, non una resa.** La 28ª lo aveva gia' scritto — «il
lavoro strutturale va fatto **prima** delle rese, non dentro un lotto» — quindi
le tre code sono andate in `rinviate.jsonl` col motivo, e non sono state rese a
meta'.

### ✅ Fatta: 23 toppe, e le tre rinviate sono tornate rendibili

`toppe.jsonl` passa da 273 a **296**, ed erano **zero** su `proc.hsp`. Poi le tre
code sono uscite da `rinviate.jsonl` e sono state rese: la frase e' italiana da
capo a fondo. Generatore in `scratchpad/genera-toppe-en.py`.

**Tre cose che il meccanismo delle toppe ha imposto, e sono tutte guardie buone:**

1. ⚠️ **`applica` si ferma se un `cerca` aggancia due volte**, non solo se non
   aggancia. Cinque di queste righe sono identiche a un'altra dello stesso file,
   quindi il `cerca` non poteva essere la riga sola: il generatore allarga il
   blocco **verso l'alto** finche' non diventa unico. Per `:3319` e `:3487` ci
   sono volute **otto righe** — i due vicinati sono identici fin sopra il ramo
   giapponese. 💡 Ed e' la ragione per cui `4865` e `4898`, che sembravano
   gemelle, sono bastate a una riga: una e' indentata con **tabulazioni** e
   l'altra con **spazi**.
2. ⚠️ **`applica` degrada gli accenti SOLO per le voci di dizionario**: le toppe
   le scrive grezze, e il file esce con `nuovo.encode("cp932")` **strict**. Un
   `più` in una toppa non si perde in silenzio — fa fallire la catena con un
   `UnicodeEncodeError`, che e' il comportamento giusto. Le toppe si scrivono
   gia' degradate (`piu'`, `faro'`, `cosi'`).
3. ⚠️ **La chiusura delle virgolette e' identica in italiano e in inglese**, e la
   guardia sull'identita' l'ha fermata: `lang("」", "\"")` sta a `:3376`, `:3402`,
   `:3537` e `:3621` — quattro siti, **una firma**. Dichiarata in `invariati.md`,
   come `...` di `<Aime>`.

### ⚠️ E la testa della frase non va punteggiata: la prima stesura sbagliava

Le tre teste erano state rese copiando la forma inglese, che il punto ce l'ha
dentro («`You are awesome!`»). **Il giapponese no**: 「よかった」+`_yo(3)` non porta
mai la punteggiatura finale, ed e' la **coda** a metterla — `！さあ…」` a `:3383` e
`:3629`, oppure il solo 」. Con la testa punteggiata sarebbe uscito
«`"Che bello...! Ecco, prendi questi spiccioli.`»

💡 **Si e' visto solo leggendo cosa segue ogni testa**, e le tre non sono uguali:
`:3372` e `:3617` proseguono in un'offerta di denaro, `:3533` no. Il conto dei
siti e' 3 teste, 4 chiusure, 2+2 code — **undici righe per tre firme**.

> Un frammento non si rende guardando il frammento. Si rende guardando la frase
> che compone, e la frase puo' stare in tre punti diversi del file.

💡 **Il filtro `if ( en )` e' molto meno rumoroso** di quello che la 28ª aveva
provato — contare i letterali fuori da `lang()` per file, che dava «quasi tutto
rumore»: percorsi, nomi di file, chiavi di `#define`.

⚠️ **Ma «per costruzione li' dentro e' tutto testo» e' falso, e l'ho scritto
prima di verificarlo.** Guardando le 18 righe dei file piccoli, **circa otto non
sono testo**: `help.hsp:568` e `main.hsp:3117` sono sostituzioni di entita' HTML
(`cnv_str s, "&quot;", "\""`), `init.hsp:1714` e `system.hsp:1682` sono operandi
di confronto, `system.hsp:1758` e `:1762` sono chiavi di dati
(`getnpctxt("raceAlias_en.", ...)`). Il filtro dimezza il rumore, non lo toglie:
ogni riga va guardata.

### ⚠️ E il conteggio di 136 era sbagliato: struttura e lingua sono due misure

La prima stesura di `blocchi_en.py` leggeva la **build** e dava **136 righe**. Ma
la build contiene anche quelle **gia' sistemate**: gli articoli italiani di
`item_func.hsp` (`locvar_itemname_s8 = "una "`) sono letterali nudi dentro
`if ( en )` esattamente come quelli inglesi, e finivano nel conto come se fossero
da fare. Di piu': **37 di quelle righe non esistono nel sorgente**, le aggiunge
`applica_dati_nome`.

I numeri veri, misurando il **sorgente pinnato** per la struttura e il confronto
sorgente/build per il lavoro che resta:

| | righe |
|---|---|
| struttura, nel sorgente | **99** |
| ancora intatte prima della 33ª | **92** |
| ancora intatte dopo | **68** |

I file: `event.hsp` 27, `screen.hsp` 14, `command.hsp` 10, `system.hsp` 4,
`material.hsp` 3, `item_func.hsp` 3, `main.hsp` 3, piu' i singoli.

💡 **E il grosso viaggia con file non ancora tradotti** (`event.hsp` e' a 5 su
654, `screen.hsp` e `command.hsp` a zero): li' la toppa non ha fretta, si fara'
insieme al file. **L'eccezione era `action.hsp`**, dato al **100%** e con una
riga inglese: `:15221`, la **gemella esatta** di `proc.hsp:26886` — jp e en
identici riga per riga. Toppata copiando la resa gia' decisa.

> Un file «al 100%» lo e' rispetto a quello che il conteggio sa vedere. Se il
> conteggio salta una classe di righe, la percentuale non e' sbagliata: e'
> risposta a una domanda piu' stretta di quella che sembra.

### 💡 Un helper con due soli siti di chiamata si puo' cambiare

`_sex2` (`text.hsp:110`) rendeva 「男」/「女」 con «ragazzo»/«ragazza», nomi nudi, e
`proc.hsp:3290` ci mette davanti un dimostrativo: «quel ragazzo» sta, «quel
ragazza» no. Un determinante non si puo' mettere nella frase, perche' varrebbe
per un genere solo.

Misurato prima di toccare: `_sex2` ha **due soli siti di chiamata** (`:3290` e
`:3450`), che sono **la stessa frase**, e le sue due voci sono uniche in
dizionario (firme diverse da `Male`/`Female` di `text.hsp:109`). Quindi il
determinante e' entrato **nel valore**: «quel ragazzo» / «quella ragazza».

⚠️ **E' la regola della preposizione applicata al determinante** — «la
preposizione sta nel valore, non nella frase» — ma vale solo perche' i siti di
chiamata sono stati **contati**. Con trenta siti sarebbe stata la scelta
sbagliata.

---

## Il presente indicativo non e' stile: e' l'unico tempo che non concorda — 2026-08-13, trentatreesima sessione

Aprendo `proc.hsp` per i due lotti della predica e delle tattiche, la domanda
era che tempo verbale usare per righe come `name(cc) + "は空高く跳躍した。"`.
Il giapponese e' al **passato**, l'inglese pure (`jumped high into the sky`).

⚠️ **E in italiano il passato prossimo e' vietato qui**, non per gusto: «e'
saltato» concorda con `name(cc)`, che e' **qualunque creatura** — «la strega e'
saltato». E' la stessa trappola dei sei participi trovati nella 30ª, ma stavolta
non e' una svista in una resa: sarebbe stata la forma **normale** di trecento
righe di log.

💡 **La risposta era gia' nel file e nessuno l'aveva scritta.** Le 31 dinamiche
di `proc.hsp` gia' rese sono **tutte al presente**: `:226` «disinnesca la
trappola», `:1094` «si mette a scrivere», `:1359` «torna in se'», `:850`
«applaude». Le sessioni precedenti l'avevano applicato senza dichiararlo.

**Regola, adesso scritta**: nelle righe di log con `name()` si usa il **presente
indicativo**. Non e' una scelta di registro — e' la forma che non ha participio
da accordare. Dove serve il passato si cerca un verbo che regga al presente, non
si accetta l'accordo.

💡 **E 「〜を始めた」 e' gia' «si mette a...» in quattro siti** (`:1094`, `:1118`,
`:1397`, `:1587`). Copiato invece di ridecidere.

### ⚠️ Lo stesso inglese per tre giapponesi diversi, a ottocento righe di distanza

`The audience gives  total of  gold pieces.` sta a `:1000`, `:1571` e `:1834`,
e i tre giapponesi sono **おひねり** (la mancia dell'esibizione), **めぐんでもらった**
(l'elemosina) e **お布施** (l'offerta religiosa). Sono tre scene diverse del gioco.

Le prime due erano gia' distinte in dizionario — «monete d'oro» e «monete d'oro
di elemosina» — e la terza le segue con «monete d'oro in oboli», dove `obolo`
viene da `db_creature.hsp:87382` («l'o-bo-lo» di `<Yacatect>`).

💡 **E' il riciclo inglese della 27ª** (l'erudito e il profugo), qui applicato a
righe di sistema invece che a battute. La rete 3 non lo prende, perche' i tre
giapponesi sono diversi: lo prende solo chi guarda il giapponese.

### 💡 La rete 3 ha lavorato di nuovo, e stavolta la resa vecchia aveva ragione

「は歓声を上げた。」 di `:1791` (la predica) e' lo stesso giapponese di `:850`
(l'esibizione), gia' reso **«applaude»**. Segnalato dalla rete, guardato, e
**copiato**: e' la stessa figura — il pubblico che reagisce bene — e divergere
avrebbe creato una divergenza che **nessuna guardia vede**, perche'
`--divergenti` legge solo `db_creature.hsp`.

⚠️ **E' la differenza con il caso 「ガウッ」 della 31ª**, dove la rete segnalo' e
la resa vecchia era **sbagliata**. La rete non dice chi ha ragione: dice di
guardare. Le due volte l'esito e' stato opposto.

### 💡 Otto registri che non si sono decisi: si sono ritrovati

Le sedici battute della predica sono gli **otto dei** che reagiscono a chi
predica la loro fede, e il registro di ognuno era gia' fissato in
`db_creature.hsp`. Non e' stato deciso niente di nuovo:

- **Opatos** ride, e le sue risate erano gia' rese: フハッハハアッ → «Fuahhahaah!»
  (`:100929`). 「フハハハハハーン！！！」 segue quell'ortografia.
- **Ehekatl** **ripete la coda della frase**: 「なっちゃった！なっちゃった！」 era gia'
  «Di muoversi! Di muoversi!» (`:101187`), quindi 「くれてるの？くれてるの？」 diventa
  «Un complimento? Un complimento?».
- **Jure** balbetta, e la balbuzie era gia' resa col raddoppio della lettera:
  「さ、寂しく」 → «N-non è che mi mancassi» (`:100593`).
- **Yacatect** parla kansai-ben, e il progetto lo rende **italiano parlato, non
  un dialetto italiano** (`:87471`, «Ma piantala, va'!»).
- **Mani** resta in **minuscolo**: la 31ª ha deciso che il maiuscolo lo porta il
  katakana, e Mani parla giapponese normale (`:101522`, «Un risultato prevedibile.»).

⚠️ **Due trappole nelle sedici.** 「いい子ね」 di Lulwy e' «brava/bravo», che
concorda col giocatore: reso **«Così mi piaci»**, invariante. E 「恥ずかしいじゃない」
di Jure ha じゃない **confermativo** — «è imbarazzante, no?» — mentre l'inglese
scrive `I'm not embarrassed`, cioe' **lo nega**. Arbitra il giapponese, e il
registro tsundere di Jure conferma che l'imbarazzo c'e'.

---

## Tre `buffdesc` dove l'inglese e' incompleto, e chi arbitra e' il codice — 2026-08-13, trentatreesima sessione

I 63 `buffdesc` chiudono `buff.hsp`. In tre di essi giapponese e inglese **non
dicono la stessa cosa**, e a differenza delle battute qui non serve interpretare:
il blocco di codice che segue la riga **dice chi ha ragione**.

| riga | il giapponese | l'inglese | il codice |
|---|---|---|---|
| `656` | sette attributi `+p`, azzera il terrore, **alza la Res magia** | «attribute by **10%**», `RES+ fear,**confusion**` | `:660-668`: sette `sdata(...) += p`, `CDATA_CONDITION_FEAR = 0`, `SKILL_RES_MAGIC += 80 + power/20`. **Niente 10%, niente confusione** |
| `1195` | DV, **軽装備20%上昇**,耐重力, 浮遊 | DV, Float, RES+ Gravity — **il Farsetto sparisce** | `:1205`: `SKILL_NORMAL_LIGHT_ARMOR * 12 / 10` |
| `1315` | «**certe** abilita'» + **barra con certi oggetti** | nomina le quattro abilita', **perde la barra** | `:1319-1322`: Dispositivi magici, Lancio, Alchimia, Lettura |

💡 **E' una famiglia nuova rispetto alle due gia' note.** Nella 31ª si erano
visti *due inglesi che si contraddicono* (「ガウッ」 = `*gulp*` e `*Growl*`), dove
arbitra il giapponese; nella 26ª *l'inglese che specializza un giapponese
generico*, dove convivono. Qui il testo e' **documentazione di un effetto
meccanico**, e c'e' un terzo testimone che non e' una lingua.

⚠️ **Su `1315` il terzo testimone smentisce anche il giapponese**, o meglio lo
completa: 特定スキル («certe abilita'») e' vago, l'inglese e' preciso, il codice
gli da' ragione. **Le due meta' non si scelgono, si sommano**: la resa nomina le
quattro abilita' *e* tiene la barra. Prendere il giapponese per regola avrebbe
buttato via l'unica cosa che l'inglese sapeva.

> Quando la riga descrive un effetto e non una battuta, aprire il blocco di
> codice sotto costa dieci righe e chiude la domanda invece di arbitrarla.

### 💡 Il tetto misurato nella 32ª e' stato riverificato, e regge

`command.hsp:9004` compone `s = dur + "t " + buffdesc` e `:5389` lo taglia con
`mes strmid(s, 0, 34)`: al `buffdesc` restano **29 byte**. Rimisurato:
**46 inglesi su 63 lo sfondano gia'**, mediana **38**, il piu' lungo **76**
(`Heavy equipment reduces physical damage taken/...`). Quindi la troncatura e'
una cosa che upstream accetta, e le due rese lunghe di questo lotto — l'elenco
dei dieci elementi a `393` e quello delle quattro abilita' a `1315` — **non
introducono un difetto nuovo**: gli altri due siti (`:2005`, `:10800`) non
tagliano, e `:10802` manda a capo apposta.

⚠️ **La scelta fra elencare e riassumere e' stata reale.** 「火冷雷闇幻毒獄音神混」
dice dieci elementi in dieci caratteri; l'italiano no. «Res+ ai dieci elementi»
sarebbe stato leggibile **anche troncato**, ed e' stato scartato lo stesso:
l'inglese elenca, upstream accetta il taglio, e riassumere avrebbe tolto al
giocatore un'informazione che nelle altre due schermate ci sta tutta.

### 💡 Le `buffdesc` non erano gemelle dei `buffname`

La domanda della 29ª — *questo file nomina cose che un altro file ha gia'
nominato?* — sui 71 `buffname` aveva risposto **44 su 71**. Sui 63 `buffdesc`
risponde **1 su 63** per identita' esatta (`707`, copiata da `skill.hsp:1241`) e
**14 su 63** per somiglianza, di cui tre copiate perche' dicono la stessa cosa
con altre parole (`1301`, `1333`, e la forma di `1230`).

⚠️ **Il confronto per stringa esatta da solo avrebbe trovato una voce e chiuso
la domanda con un no.** Il gemello concettuale si trova solo con una misura di
somiglianza — `difflib` a 0,55 sul giapponese, tre candidati per voce — e le
tredici in piu' sono esattamente quelle che avrebbero prodotto due modi di dire
la stessa cosa. Vale per ogni file nuovo, non solo per questo.

### ⚠️ E lo script che serviva era citato nella ripresa ma non esisteva

Andando a cercare `scratchpad/scheletro.py`, nominato dalla ripresa come una
cosa disponibile, si e' scoperto che **la cartella `scratchpad/` non era mai
stata creata nel repo**. Idem `scratchpad/fuori_lang.py`. E **nessuno script di
lotto e' mai stato committato**: `git ls-files "*.py"` fuori da `strumenti/`
dava zero, dalla prima sessione alla trentaduesima. Ogni sessione riscriveva le
cinque reti da capo.

💡 **E' la trappola della 28ª — lavoro fuori da git — in forma minore**, e ha la
stessa forma di quella della 29ª: non un guasto, ma una cosa scritta come vera
che nessuno aveva verificato. La ripresa e' un documento che si legge fidandosi,
e un riferimento a un file inesistente costa la ricerca a chi lo segue.

**Corretto**: `scratchpad/` esiste, contiene i quattro script riusabili piu' il
lotto della 33ª come modello, e ha un `LEGGIMI.md` che dice quando si lanciano.
I due riferimenti falsi della ripresa sono stati marcati come tali invece di
essere cancellati, perche' i numeri di `fuori_lang.py` erano ancora citati.

> Quello che serve due volte si committa. Un riferimento a uno script si
> controlla con `git ls-files`, non si presume.

---

## Due tetti che nessuno aveva misurato, e li sfondavamo tutti e due — 2026-08-13, trentaduesima sessione

La sessione era di solo collaudo, e in due schermate ha trovato due riquadri
che tagliano, che `larghezze.py` non guarda perche' non sono menu.

### 1. Le piastrelle degli stati nell'HUD

A schermo si leggeva **«Marchio letal»**. `screen.hsp:853-859` disegna
l'etichetta su una piastrella `gcopy ..., 65 + en * 30, 15`, cioe' **95 px**
nella build inglese, col testo che parte a `+6`.

Il carattere della build inglese e' **`Courier New`** (`config.txt`, `font2.`),
che e' **monospaziato**: qui contare i caratteri e' la misura giusta, non una
stima. La dimensione attiva in quel punto e' `13 - en * 2` = **11 px**, cioe'
**6,6 px per carattere**.

    piastrella 80 px -> (80 - 6) / 6,6 = 11 caratteri
    piastrella 95 px -> (95 - 6) / 6,6 = 13 caratteri

⚠️ **La misura si e' verificata da sola sullo screenshot**: «Marchio letal» sono
esattamente 13 caratteri, cioe' il taglio cade dove il conto dice.

**Fuori misura: 19 etichette su 61.** ⚠️ E qui l'ancora inglese **non**
assolveva, al contrario dei `buffdesc`: upstream ne sfora **2 su 61**, di uno o
due caratteri. Il tetto e' vero e lo rispetta.

### 2. La colonna del menu tattiche del mod

`custom_ai.hsp:3171-3175` dispone le voci in colonne ogni **145 px**, e con la
condizione `Buff` elenca **tutti** i `buffname` (`:3138`). Il carattere li' e'
`14 - en * 2` = 12 px, cioe' **7,2 px**: **20 caratteri**.

⚠️ **`cs_list` non taglia: sconfina.** A schermo si leggeva «Crescita della
destre**Cambio di forma (A)**», «Crescita della costitu**Concentrazione**»,
«Cambio di forma final**Energia al massimo**». La domanda aperta dalla 29ª —
«o le colonne si sovrappongono gia', o `cs_list` taglia come `*prompt_key`» —
si chiude sulla **prima** ipotesi.

**Fuori misura: 10 buffname su 71, e 0 inglesi su 71.** La colonna era
dimensionata sul set inglese, che ci sta comodo.

### Le rese cambiate, 33 in tutto

La famiglia `GROW` e' di nove nomi e sei sfondavano: accorciare solo quelli
avrebbe lasciato «Crescita della forza» accanto a «Cresce costituzione», quindi
si e' cambiata tutta. 💡 Il modello col sostantivo **non bastava**: «Crescita
costituzione» e' 21, cioe' ancora fuori.

| era | e' | perche' |
|---|---|---|
| Crescita della X (9 voci) | **Cresce X** | l'unico modello uniforme che ci sta tutto |
| Cambio di forma finale | **Cambio forma finale** | i fratelli `(A) (B) (G) (D)` erano gia' dentro |
| Lancio oltre il limite | **Tiro oltre il limite** | 20 esatti |
| Maledizione della fame | **Fame maledetta** | `fame` porta il proprio genere |
| Lume della falsa vita | **Lume di falsa vita** | |
| Invulnerabilita' | **Invincibile** | |
| Marchio letale | **Segno letale** | ⚠️ prima era «Marchio», vedi sotto |
| Sanguinamento / -! / Emorragia | **Sangue** / **Sangue!** / Emorragia | scala di tre |
| Veleno letale! | **Gran veleno** | ⚠️ prima era «Veleno!», vedi sotto |
| Sonno profondo | **Letargo** | |
| Instabilita' | **Instabile** | in `-e`, non concorda |
| Soffocamento | **Asfissia** | |
| Malattia-LvN (11 voci) | **Morbo-LvN** | ⚠️ `Malato-LvN` concorderebbe col giocatore |

### ⚠️ Accorciare per stare nel tetto puo' togliere il significato, non solo i byte

Due rese di questa stessa sessione sono state rifatte poche ore dopo, e la
domanda che le ha prese e' stata **«ma non era *letale* prima?»**.

| era | primo tentativo | perche' non andava | adesso |
|---|---|---|---|
| Marchio letale (14) | Marchio (7) | 刻死紋 ha 死, *morte*: «marchio» e basta puo' essere un marchio di fabbrica | **Segno letale** (12) |
| Veleno letale! (14) | Veleno! (7) | 猛毒 e' un veleno **piu' forte**, e il solo punto esclamativo non lo dice | **Gran veleno** (11) |

💡 **La lezione e' che il tetto e' un vincolo, non un criterio.** Il primo
accorciamento cerca i caratteri che avanzano; quello giusto cerca la resa piu'
corta che **conserva le due meta' del senso** — qui la cosa marchiata e il
fatto che uccida. Tutt'e due esistevano dentro il tetto e non erano state
cercate: c'era un carattere di margine per «Segno letale» e zero, ma
sufficienti, per «Gran veleno».

⚠️ **Da rifare a ogni accorciamento**: rileggere la resa nuova **senza avere
sotto gli occhi quella vecchia** e chiedersi se dice ancora quello che diceva
il giapponese. «Marchio» letto da solo non lo diceva.

⚠️ **Il tetto si misura sulla forma degradata, non su quella del dizionario.**
`volontà` e' 14 caratteri, `volonta'` e' **15**, e a schermo ci va la seconda:
la rete dello script controlla la stringa dopo `degrada`.

⚠️ **`occorrenza` non distingue gli elementi di un array**: le undici
`Malattia-LvN` stanno tutte su `text.hsp:68` con `occorrenza` **0**. La chiave
buona e' `(riga, resa attuale)`.

✅ **La guardia c'e', ed e' `strumenti/riquadri.py`**, scritta lo stesso giorno
con 18 test, e sta nelle verifiche d'apertura. `larghezze.py` non poteva
coprirli: misura i menu che passano da `*prompt_key`, e questi due non ci
passano.

💡 **Due difetti della guardia li ha trovati un test, non l'occhio**, e vale la
pena saperli perche' sono due modi di essere «giusti per sbaglio»:

1. la prima versione cercava la `gcopy` della piastrella **entro sei righe
   sopra** la `mes`. Un'etichetta priva della propria si sarebbe presa in
   silenzio quella dell'etichetta precedente, cioe' un tetto che non e' il suo.
   La regola giusta non si misura in righe: risalendo, la `gcopy` e' sua solo
   se arriva **prima** di un'altra `mes`;
2. leggeva il passo della colonna dalla **prima** `cs_list` di
   `custom_ai.hsp`. Ma gli elenchi a colonne di quel file sono **quattro**, e
   quello dei potenziamenti e' il quarto: gli altri tre hanno passo **150**. Il
   verdetto non cambiava — 150 / 7,2 fa comunque 20 — il che e' peggio, non
   meglio: una guardia che da' la risposta giusta misurando il posto sbagliato
   non avverte nessuno quando smette di essere giusta.

⚠️ **E quei tre elenchi sono un tetto non guardato**, con l'ancora che dice il
contrario: elencano nomi di incantesimo, e a sfondare i 20 caratteri sono **15
italiani su 445 ma anche 5 inglesi** (fino a `Critical Particle Cannon`, 24).
E' la famiglia dei `buffdesc` — un tetto che upstream accetta gia' rotto —
quindi non si tocca niente prima di averlo visto a schermo. Vedi
`RIPRESA-sessione.md`, «Domande aperte».

---

## «lo Yerleswood», non «l'Yerleswood» — 2026-08-13, trentaduesima sessione

Visto in combattimento: «**l'Yerleswood** di serie stands up.» La `Y` iniziale
in italiano suona **semivocale** e vuole `lo`, come «lo yogurt», «lo yacht».

💡 **La convenzione esisteva gia' e la voce le era sfuggita**: il dizionario
rende «**lo yeek**» in 18 voci, piu' «gli yeek» e «degli yeek». Non e' una
decisione nuova, e' una svista singola — cercata in tutto il dizionario, era
**l'unica**: `db_creature.hsp:78249`.

Il referto costa una riga e si rilancia quando si scrive un nome nuovo che
comincia per consonante o semivocale:

```powershell
python -c "import glob,io,json,re; p=re.compile(r\"\b([Ll]|[Uu]n[ao]?|[Dd]ell|[Aa]ll|[Nn]ell|[Ss]ull|[Qq]uell)'([A-Za-z])\"); v=set('aeiouAEIOUhH'); [print(f, json.loads(l)['riga'], m.group(0)) for f in glob.glob('dizionario/*.jsonl') for l in io.open(f,encoding='utf-8') if l.strip() for m in p.finditer(json.loads(l).get('it') or '') if m.group(2) not in v]"
```

Atteso **0**. Come per i participi, e' un referto da leggere: un nome
straniero che comincia per vocale muta darebbe un falso positivo.

---

## Undici creature su ventisette non parlano se aspetti — 2026-08-13, trentaduesima sessione

Il metodo di collaudo scritto da cinque sessioni dice: `add_ally <id>`, poi
**tenere premuto `5`** e aspettare. Per undici delle ventisette creature delle
liste arretrate quel metodo **non produce niente**, e non perche' sia andato
storto qualcosa: nel loro blocco di `db_creature.hsp` **manca
`DBMODE_FLAVOR_PASSIVE`**.

⚠️ **E' la spiegazione di perche' le liste non tornano mai.** Chi ci ha provato
si e' messo davanti a una creatura muta, ha aspettato quaranta turni e ha
lasciato perdere. La lista della 30ª diceva testualmente di aspettare per
`add_ally 502` e `add_ally 492`: tutt'e due sono mute in attesa.

| classe | quando esce | come si provoca |
|---|---|---|
| `PASSIVE` | oziosa | alleata a meno di dieci caselle, `5` premuto |
| `ANGERED` | mentre combatte | `spawn_chara` (relazione di database) e farsi attaccare |
| `DEATH` | quando muore | ucciderla |
| `KILL` | quando ammazza | darle qualcosa di debole da uccidere |
| `WELCOME` | bentornato | entrare in `AREA_HOME` con lei nell'area |

Mute in attesa: **686** `<Regulus>`, **640** `<Sinaha>`, **331** `<Ehekatl>`,
**601** e **664** i due Yerleswood, **379** `<Siva>`, **911** `<Tezcatlipoca>`,
**756** `<Shuraida>`, **534** `<Aile>`, **465** il soldato yerles infetto,
**627** il Gigante Castagna, **502** il terminale Xeren, **492** `<Pascal>`.

💡 **E una serie di battute puo' essere sparsa su quattro classi.** Le sette
regole di `<Aribel>` (796) escono cosi': la **uno** e' oziosa, **due** e **tre**
sono offese, la **quattro** e' la morte, **cinque** e **sei** sono le uccisioni.
Chi aspetta e basta ne vede una sola, e per giunta in concorrenza con altre tre
oziose. Non e' un difetto della resa: e' come e' fatto il blocco.

**Come applicarlo:** la lista di collaudo va scritta **per classe**, non per
creatura — `add_ally` per le oziose, `spawn_chara` e farsi attaccare per le
offese, uccidere per le morti. Riscritta cosi' in `RIPRESA-sessione.md`,
«Il collaudo, punto per punto».

---

## Due inglesi che si contraddicono: chi arbitra e' il giapponese — 2026-08-13, trentunesima sessione

Il verso 「ガウッ」 compare due volte in `db_creature.hsp`, e i due rami inglesi
dicono cose diverse:

| dove | creatura | inglese |
|---|---|---|
| `44170` | il ghepardo di un altro mondo | `*gulp*` |
| `52145` | `<Il Figlio del Caos>` | `*Growl*` |

La resa vecchia di `44170` era **`*gnam*`**, cioe' seguiva `*gulp*`: un
boccone. Ma ガウ in giapponese e' un **ringhio**, non una deglutizione, e la
riga accanto — 「ガルル！」, `*grrr!*` — conferma che il repertorio e' quello di
una bestia che ringhia.

💡 **La regola vale gia' e qui si vede a occhio nudo**: quando i due inglesi
dello stesso giapponese si contraddicono, non c'e' modo di «seguire l'inglese»
— bisogna aprire il giapponese. Il caso e' piu' netto della famiglia gia' nota
(l'inglese che *specializza* un giapponese generico, 「がおー」 = `*creaking*`
su un golem di legno e `*growl*` su una divinita' serpente): li' le due letture
convivono, qui una delle due e' semplicemente sbagliata.

**Corrette tutte e due a `*ringhio*`**, che e' diverso da `*grrr!*` come ガウッ
e' diverso da ガルル. La correzione e' stata fatta **nel dizionario**, non nel
lotto: `44170` era gia' in dizionario da sessioni.

⚠️ **Il conto di `--divergenti` non si e' mosso** (resta 13), ed e' il punto:
se avessi reso solo `52145` sarebbe salito a 14, e la divergenza sarebbe stata
mia. Correggere il sito vecchio costa una riga e toglie il problema invece di
registrarlo.

💡 **Come si e' trovato**: il referto del lotto stampa «⚠️ GIA' RESO ALTROVE»,
e la terza rete dello script del lotto **si ferma** su una resa che diverge da
una gia' decisa. E' la rete che ha fatto la segnalazione — non l'occhio.

---

## Sei rese facevano concordare un participio col giocatore — 2026-08-13, trentesima sessione

La regola «il giocatore non ha genere noto» è nel progetto da venti sessioni, e
`guida-stile.md` la ripete. Non era mai stata **cercata**: si applicava mentre
si scriveva, e chi scrive non rilegge trecento rese vecchie.

L'occasione è stata la sorella maggiore del lotto 028. La sua battuta di
bentornato è 「もう！お姉ちゃんを置いてどこに行ってたの？」, e la gemella quasi
identica era già in dizionario da una sessione precedente, resa

> Uffa! Dove **sei andata** a finire, lasciando qui la sorellona?

che sbaglia in metà delle partite. Cercate allora tutte le forme della stessa
famiglia in **tutto** il dizionario — seconda persona più participio, e il
vocativo con aggettivo — ed erano **sei in 9.254 voci**:

| dove | prima | dopo |
|---|---|---|
| `action.hsp:18721` | «Ti sei **aperto** il ventre» | «Ti **apri** il ventre» |
| `db_creature.hsp:42140` | «ti sei **offeso** così tanto?» | «ti **offendi** così tanto?» |
| `db_creature.hsp:42140` | «rosica di più, **sfigato**» | «rosica di più, **mezza cartuccia**» |
| `db_creature.hsp:50938` | «ti sei **schiarito** le idee» | «hai le idee più chiare» |
| `db_creature.hsp:86494` | «Dove sei **andata** a finire» | «Ma dove te ne stavi» |
| `db_creature.hsp:87554` | «Il **prossimo** sei tu» | «Adesso tocca a te» |

⚠️ **L'ultima era mia, di questa stessa sessione**, scritta due ore dopo aver
scritto la ricerca che l'ha presa. «Il prossimo sei tu» sembra invariante e non
lo è: `prossimo` è un aggettivo sostantivato che concorda con chi ascolta.
È la prova che la regola non si applica «stando attenti».

💡 **La ricerca costa una riga e va rilanciata a ogni lotto** (nel lotto 030 ha
preso un falso positivo, `Qual è il prossimo bersaglio?`, dove `prossimo`
concorda con `bersaglio` e non col giocatore — quindi è un referto da leggere,
non una guardia da automatizzare):

```powershell
python -c "import json,io,glob,re; p=re.compile(r'\b(?:ti sei|te ne sei|sei|sarai|ti eri|eri|il prossimo|la prossima)\s+(\w+(?:ato|ata|uto|uta|ito|ita|tto|tta|so|sa))\b'); [print(f, json.loads(l)['riga'], m.group(0)) for f in glob.glob('dizionario/*.jsonl') for l in io.open(f,encoding='utf-8') if l.strip() for m in p.finditer(json.loads(l).get('it') or '')]"
```

⚠️ **Non è automatizzabile in una guardia** per la stessa ragione già scritta
nella ripresa: su un lotto provato a mano dà tre falsi positivi su quattro. Il
referto lo legge una persona.

## Una resa copiata può diventare identica all'inglese — 2026-08-13, trentesima sessione

Due volte in otto lotti è successa la stessa cosa, e la seconda ha chiarito la
prima. Il giapponese 「スシ！」 compare in due punti di `db_creature.hsp`. A
`104858` l'inglese urla `SUSHI!!!` e la resa italiana è `Sushi!`: diversa
dall'inglese, nessun problema. A `83627` **lo stesso giapponese** ha come
inglese `Sushi!`, e copiare la resa già decisa — che è quello che il progetto
chiede di fare — la rende **identica all'inglese**, cioè fa scattare la guardia.

💡 **Le due regole non sono in conflitto: dicono cose su piani diversi.**
«Copia la resa già decisa» parla del giapponese; «non lasciare l'inglese» parla
del sito. Quando il secondo sito ha un inglese che coincide con la resa giusta,
l'identità **non è un difetto della resa**: è una proprietà di quel sito. Il
posto per dirlo è `invariati.md`, ed è per questo che la riga aggiunta cita
sempre **l'altro sito** come prova.

Aggiunte due righe, tutte e due con quella struttura:

- `Sushi!` — l'ombrame (`83627`), con la controprova di `104858`;
- `...!` — il ninja rosso (`87626`), giapponese 「…！」, con la controprova di
  `88185`, dove lo stesso giapponese ha un inglese pieno di parole
  (`W-w-what...!`) e la stessa resa italiana **non** coincide.

⚠️ **Il caso opposto esiste e va distinto**: nel lotto 033 la guardia ha preso
「はああああ…っ！」 reso `Haaaaah...!`, che è la **grafia inglese** di un grido
copiata pari pari. Lì l'identità era davvero un difetto, e la resa è diventata
`Aaaaaah...!`. La differenza si vede guardando se la resa italiana sarebbe
stata quella **anche senza** l'inglese sotto gli occhi.

## Il ramo inglese di una battuta può essere vuoto — 2026-08-13, trentesima sessione

`db_creature.hsp:86293` è la classe `ANGERED` della cittadina, e sono tre
`lang()` in fila. Il secondo è

```hsp
lang("「この格好じゃ動きにくい…！」", cnvtalk(""))
```

cioè **il giapponese ha una battuta e l'inglese ha la stringa vuota**. Peggio:
l'inglese che le spetterebbe (`It's hard to move in this outfit...!`, che
traduce esattamente quel giapponese) sta sul **terzo** `lang()`, dove il
giapponese dice un'altra cosa (「どうして僕を狙うのさ！」). È uno slittamento di
monte, non un caso di inglese che riscrive.

⚠️ **Per noi la conseguenza è che quella battuta è fuori perimetro**:
`estrai.py` non la estrae — non c'è nessuna stringa inglese da sostituire — e
quindi non è né tradotta né contata fra quelle da fare. Nella build italiana
esce come esce oggi in inglese: due virgolette vuote.

**Misurato su tutto il sorgente**: i `lang()` con giapponese pieno e inglese
vuoto sono **31**, e **30 sono legittimi** — sono particelle e suffissi che
l'inglese non ha (`位`, `歳`, `耐性`, `のレシピ`). Questo è **l'unico** che è una
frase.

💡 **Non si può toppare**: una toppa si aggancia solo a una riga senza `lang()`,
e questa ne ha tre. Le strade sono due, e nessuna delle due è per un lotto di
rese: far estrarre a `estrai.py` anche le voci con inglese vuoto (e allora
`applica` deve saper scrivere dentro un `cnvtalk("")`), oppure lasciarla
com'è e annotarla. **Per ora annotata**, come `iknownnameref`.

## L'avviso «NOME NON TRADOTTO» di `battute.py` può essere falso — 2026-08-13, trentesima sessione

Il lotto 027 ha stampato `⚠️ NOME NON TRADOTTO` per `CREATURE_ID_YOUNGER_SISTER2`.
Il nome **è** reso: 「妹」 è «la sorella minore», deciso da sessioni.

La causa è il modo in cui il dizionario è indicizzato. `nomi_italiani()` cerca
le voci la cui **riga** ha `dbmode == DBMODE_REF_SPEC`; ma il dizionario è
indicizzato **per contenuto**, e di due righe con lo stesso testo tiene la
prima. Il nome 「妹」 compare per la prima volta a `117743`, dentro il blocco
`DBMODE_SET` di **un'altra** creatura, e la voce resta agganciata lì. Alla riga
`117836`, che è quella con `DBMODE_REF_SPEC`, non corrisponde nessuna voce.

💡 **Quindi l'avviso va letto come «non l'ho trovato», non come «non c'è»**, e
scatta esattamente quando una creatura **condivide il nome** con una che il file
elenca prima. Prima di prenderlo per buono si cerca il giapponese del nome nel
dizionario. Non è stato corretto nello strumento perché la correzione giusta —
agganciare i nomi per `dbid` invece che per riga — tocca la stessa funzione che
compone i lotti, e non si tocca dentro un lotto.

## Un buff è l'incantesimo che lo concede — 2026-08-13, ventinovesima sessione

Aprendo i 71 `buffname` di `buff.hsp` la domanda sembrava «come si rendono 71
nomi di status». Era sbagliata: **44 di quei 71 giapponesi erano già resi**,
quasi tutti in `skill.hsp`, chiuso da dieci giorni.

Non è una coincidenza né un doppione da ripulire. 「聖なる盾」 è il nome
dell'incantesimo *e* il nome dello status che l'incantesimo lascia addosso: per
chi gioca sono **la stessa cosa vista due volte**, e devono leggersi uguale.
Renderli di nuovo, anche bene, avrebbe prodotto due nomi per un oggetto solo.

**Quindi il lotto ha copiato, non deciso**: `Scudo sacro`, `Nebbia di silenzio`,
`Possessione di Lulwy`, `Velo sacro` vengono dal dizionario. Le rese nuove sono
**27**, quelle il cui giapponese non compare da nessun'altra parte.

### ⚠️ E nessuno strumento lo controllava

`battute --divergenti` è la guardia contro «stesso giapponese, due rese
diverse». Ma `rese_gia_decise()` legge **un solo file**:

```python
FILE = "db_creature.hsp"
percorso = percorsi.DIZIONARIO / f"{FILE}.jsonl"
```

Fuori da lì è cieca. La controprova è in questo lotto: le quattro
`Cambio di forma (A)/(B)/(G)/(D)` hanno **lo stesso giapponese** 「フォルムシフト」
e quattro rese diverse, e dopo la reimportazione `--divergenti` stampa **11**
come prima. Se le 44 le avessi ridecise a caso, la catena sarebbe rimasta verde.

**Misurato sull'intero dizionario**: 436 giapponesi hanno più di una resa, 369
dentro `db_creature.hsp` (quelli che lo strumento vede) e **67 a cavallo di più
file**. ⚠️ **La maggior parte dei 67 è legittima e non va toccata**: lo stesso
giapponese breve fa il nome dell'abilità in `skill.hsp`, il nome dell'oggetto in
`db_item.hsp` e un frammento di frase in `action.hsp` — `Bastone` / `bastone` /
`il bastone` sono tre ruoli grammaticali, non tre errori. È proprio perché la
divergenza fra file è quasi sempre voluta che lo strumento è ristretto a un
corpus solo: allargarlo darebbe 67 falsi allarmi.

💡 **La regola che ne esce non è «scrivere una guardia», è una domanda da farsi
all'apertura di ogni file nuovo**: *questo file nomina cose che un altro file ha
già nominato?* Per `buff.hsp` la risposta era sì per 44 voci su 71. Vale
sicuramente anche per `chara.hsp` («You have learned a new ability, X») e per i
`bufftxt` rimanenti. Si risponde in una riga, non con un lotto:

```powershell
python -c "import json,io,glob; d=set(); [d.add(json.loads(l)['jp']) for p in glob.glob('dizionario/*.jsonl') for l in io.open(p,encoding='utf-8') if json.loads(l).get('it')]; v=[json.loads(l) for l in io.open('lavoro/_X.jsonl',encoding='utf-8')]; print(sum(1 for x in v if x['jp'] in d), 'su', len(v), 'gia rese altrove')"
```

## Dove finisce un nome di status: tre siti, tre regole — 2026-08-13, ventinovesima sessione

Prima di fissare dieci `Crescita della…` da 24-27 caratteri serviva sapere il
tetto, perché il progetto vieta di stimarlo. `buffname` esce in **tre** posti, e
non hanno la stessa regola:

| sito | come disegna | tetto |
|---|---|---|
| `command.hsp:10800` (status del personaggio) | `s = buffname + ": " + turni + buffdesc` | **manda a capo a 70**, non taglia |
| `command.hsp:256` | `bmes` a `pos` libere | nessuno |
| `custom_ai.hsp:3174` (menu tattiche del mod) | `cs_list …, wx + 18 + (145 * (cnt/22))` | colonne da **145 px**, ~13 caratteri |

Il primo è il sito che conta e **si spezza da solo**: il blocco `ANNA CUSTOM`
mette il ritorno a capo dentro `if ( en )`, cioè proprio nel ramo che
compiliamo. Il terzo sarebbe strettissimo.

⚠️ **Ma il tetto del terzo è già sfondato da rese decise settimane fa**:
`Schivata d'emergenza`, `Possessione di Lulwy` e `Dominio dello spazio` sono 20
caratteri e stanno nel dizionario da prima di questo lotto. Delle due l'una: o
in quel menu le colonne si sovrappongono già oggi, o `cs_list` non taglia come
`*prompt_key`. **Non è deducibile e va visto a schermo.** Nel frattempo i 27
nomi nuovi sono scritti con la stessa misura dei 44 esistenti: essere gli unici
corti non avrebbe sistemato niente e avrebbe reso il menu incoerente.

## Il round-trip non è una prova: vanno contati i byte — 2026-08-11, ventitreesima sessione

Uno screenshot del diario, riga delle missioni giornaliere:

```
[Fatto]EVisitare le Terre selvagge.
```

La `E` non l'aveva scritta nessuno. Era il puntino d'elenco giapponese 「・」,
che CP932 codifica `0x81 0x45`: `init.hsp:1391` sceglie il carattere con
`font lang(cfg_font1, cfg_font2)`, e per l'inglese `cfg_font2` è **Courier New**
(`config.txt:75`), un font latino. `mes` disegna **un glifo per byte**: `0x81`
non ne ha uno, `0x45` è `E`.

I quattro punti del sorgente che sanno riconoscere un byte guida — `init.hsp:1295`,
`module.hsp:57` e `:4932`, `system.hsp:4050` — fanno il controllo **solo dentro
`if ( jp )`**.

### Perché la guardia esistente non lo vedeva

`non_ascii_residuo` chiede a CP932 se sa **rappresentare** il carattere, con un
round-trip codifica/decodifica. 「…」 e 「“”」 lo passano benissimo. Il problema
non era la rappresentabilità: era la **larghezza in byte**, che nessuno contava.

> Una guardia che chiede «CP932 sa scrivere questo carattere?» risponde sì anche
> quando il carattere è inservibile. La domanda giusta era «in quanti byte?».

### Il conto del danno

**186 voci**, per due terzi da sessioni precedenti:

| carattere | voci | ora |
|---|---|---|
| `…` | 130 | `...` |
| `“ ”` | 54 | `\"` |
| `・` | 17 | via |
| `《 》` | 1 | `< >` |

### La decisione, che ne rovescia una vecchia

`verifica.py` **imponeva** le virgolette tipografiche `“”` e rifiutava la `"`.
Era il contrario del vero. La forma giusta è la **virgoletta protetta** `\"`,
che è quella che usa l'inglese upstream (`text.hsp:9879` scrive `\"Project LF\"`)
e che `applica.riscrivi_statica` scrive tale e quale, perché HSP conosce
l'escape.

La controprova che ha deciso: in ~9.000 stringhe l'inglese upstream usa **un
solo** carattere a due byte, `♪`, e per quello c'è codice apposta
(`init.hsp:1374` lo intercetta e disegna un'icona). Quindi `♪` resta ammesso in
`_DOPPI_AMMESSI`, tutto il resto no.

⚠️ **Quattro stringhe sono diventate identiche all'inglese** una volta tolte le
virgolette — i versi del corvo `\"Hjckrrh!\"` e una coda di punteggiatura `?\"`.
Sono in `invariati.md`: prima differivano dall'inglese **per il difetto**.

La guardia nuova è `accenti.doppi_byte_cp932()`, chiamata da `verifica` su resa
e plurale. Il test che affermava il contrario del vero
(`test_le_virgolette_tipografiche_alte_passano_nelle_statiche`) ora dice
l'opposto, con la data e il perché.

Vedi [[il-round-trip-non-basta-conta-i-byte]].

---

## `talk_conv` manda a capo, ma lascia scappare l'ultima parola — 2026-08-11, ventitreesima sessione

Stesso screenshot, prima riga della trama:

```
Forse a Lesimas, uno dei labirinti
di Nefia a sud di Vernis, si trova qualco
```

Non è il riquadro che taglia: è **un difetto di monte**. Il ramo inglese di
`talk_conv` (`init.hsp:1326-1369`) accumula parola per parola cercando lo spazio
successivo; quando lo spazio non c'è più — cioè sull'**ultima parola** — esce dai
due cicli e fa `talk_conv_arg1 += msgtemp`, appendendo la coda **senza guardare
la larghezza**.

L'inglese lo sfiora appena, perché le sue ultime parole sono corte. L'italiano,
più lungo del 20%, ci cade dentro di continuo: **24 righe su 214 siti**.

### La guardia: `strumenti/diario.py`

Gemello di `larghezze.py`, per l'altra famiglia di stringhe. Trova i siti che
passano da `talk_conv`, legge il tetto dal sorgente (`40 - en * 4` = **36** con
`en` = 1, `config.hsp:439`), simula l'algoritmo **difetto compreso** e segnala.
Un simulatore che correggesse il difetto non troverebbe niente.

⚠️ **Due modi di finire dentro `talk_conv`, e servono entrambi.** Il primo è
l'assegnazione locale. Il secondo è l'argomento di chiamata: `addnews2`
(`text.hsp:12100`) manda a capo il **proprio parametro**, e i chiamanti gli
passano il `lang()` dentro la chiamata. Cercando solo le assegnazioni locali
spariva tutta la pagina delle **notizie**, cioè metà del diario.

⚠️ E il parametro ci arriva **per copia**: `addnews2` scrive
`locvar_addnews2_n = addnews2_arg1` e manda a capo la copia. Cercare il nome del
parametro e basta trovava zero `#deffunc`.

### Il verso giusto è accorciare, non imbottire

⚠️ La prima stesura delle 24 correzioni infilava zeppe — «…e le 23:59 **di
sera**», «…è stato abbattuto **ormai**» — per spostare il punto di a capo. Cioè
peggiorava la prosa per far quadrare il riquadro, che è esattamente il difetto
al contrario.

Accorciando si guadagna due volte: «Devo combattere fino in fondo senza
arrendermi» sforava di 11; «fino in fondo, **senza mai** arrendermi» entra, e per
giunta è italiano migliore. «Andare a dormire fra le 21:00 e le 23:59» →
«Dormire fra le…», che è anche la forma dell'elenco.

Vedi [[accorciare-non-imbottire]] e [[il-difetto-di-monte-lo-paghiamo-noi]].

---

## Sette intestazioni del diario scritte fuori da `lang()` — 2026-08-11, ventitreesima sessione

`command.hsp` scrive `noteadd " - Quest - "` senza `lang()`: righe **2854, 2865,
2883, 2895, 2916, 2952, 3114**. Il dizionario non le vede, e restano inglesi
**anche nella build giapponese** — è una svista di upstream, non una scelta.

Toppate a mano. ⚠️ **A mano, non generate**: `genera_toppe_nomi` riscriverebbe
sopra una toppa che riconosce come sua, ed è già successo una volta con la
benedizione (ventiduesima sessione). Le righe non contengono `lang()`, quindi la
toppa vale identica sul sorgente pinnato e sulla build.

> Se una stringa che il giocatore legge non è nel dizionario, prima di
> concludere che è codice, guardare se è semplicemente **fuori da `lang()`**.

---

## Il diario delle missioni: quattro cose che il testo non dice — 2026-08-11, ventitreesima sessione

Tradotte 285 firme di `text.hsp` (dal 70% all'**89%**): trama principale,
giornaliere, 30 sottotrame, oggetti di missione, bacheca degli incarichi.

- **Il giocatore non ha genere noto**, e il diario è scritto in prima persona.
  Niente participio che concordi col soggetto: non «sono sopravvissuto» ma
  «l'esperimento è finito e sono ancora in piedi»; non «quando sono pronto» ma
  «quando sarà tutto pronto».
- **`cnvarticle` non mette un articolo.** `init.hsp:173`: nella build inglese
  avvolge il nome fra **parentesi quadre**. Il nome della funzione dice il
  contrario di quello che fa.
- **Una preposizione può agire a ventidue righe di distanza.** `s(12)` si compone
  a `text.hsp:11837` e finisce dopo «da » a `:11859`. Reso «il bersaglio» avrebbe
  prodotto «da il bersaglio»; con «chi abita a Vernis» non si fonde.
- ⚠️ **Il diario diceva «slime», il codice dice «putit».** `text.hsp:10019` scrive
  スライム, ma il dialogo di Miches (`chat.hsp:1505`, `:1517`) nomina プチ, e プチ
  è quello che il giocatore trova in casa. Arbitra il codice sullo stato del
  gioco, non la parola sciolta del diario.

### La riga che si compone a runtime, e il calcolo a mano sbagliato

`"Compenso: " + soldi + giunzione + categoria` (`text.hsp:11884`, tetto **30**):
il misuratore vede solo l'etichetta, il resto arriva a runtime. Misurata a mano
su tutte le cifre e tutte le dodici categorie di `fltname`:

| giunzione | caso peggiore |
|---|---|
| inglese, `and` | 39 |
| `e` | **43**, tagliata |
| `, più` | **29** |

⚠️ **Il primo calcolo, fatto a mente, era rovesciato**: credevo che accorciare
«monete d'oro» in «oro» aiutasse, e fa il contrario — la frase **più lunga**
provoca l'a capo prima, e così salva la categoria finale, che è la parola che
scappa al controllo. Con `oro` il peggiore sale a 36.

> Quando il difetto è nell'algoritmo di a capo, l'intuizione «più corto è
> meglio» non vale. Si misura.

---

## «In coda» non è un posto: dipende da chi scrive dopo di te — 2026-08-11, ventiduesima sessione

Uno screenshot della vetrina del panettiere di Palmia:

```
un piatto di  con benedizionewalnut bread (Rank: 3)
un piatto di walnut bread (Rank: 3)
una pasta fresca con benedizione
```

La terza riga è giusta, la prima no, e sono lo **stesso codice**.

`strblessed` in inglese si antepone (`blessed sword`); in italiano è un
complemento che segue, perché un participio si accorderebbe con un oggetto di
genere ignoto. Le toppe 41-45 lo differiscono in `locvar_itemname_s7` e lo
appendono a `*skipName`. Per ogni oggetto normale quello **è** il fondo del
nome, e infatti «pasta fresca con benedizione» esce bene.

Ma per il **cibo cotto** il nome del piatto non c'è ancora: lo appende
`gosub *itemNameSub` del ramo inglese, che sta **dopo** `*skipName`
(`item_func.hsp`, `*skipName` → … → `gosub *itemNameSub` → ritorno). Quindi la
benedizione finisce in mezzo, e senza spazio, perché `foodname()` si concatena
nuda.

**Corretto**: la toppa di `*skipName` non appende più `s7`; una toppa nuova lo
appende **prima del controllo di lunghezza a 66 caratteri**, che è l'ultimo
punto prima del ritorno — così la coda c'è sempre ed è anche misurata.

### E il primo tentativo è stato riscritto in silenzio

⚠️ **Quelle toppe non stanno a mano: le genera `strumenti/genera_toppe_nomi.py`**
(righe 452-463). Il primo tentativo modificava `toppe.jsonl` direttamente: la
build usciva giusta, e il difetto sembrava chiuso. Poi il lotto successivo ha
lanciato `genera_toppe_nomi`, che ha **riscritto la sua toppa sopra la mia
modifica** — e in vetrina la benedizione è comparsa **due volte**, la vecchia in
mezzo e la nuova in coda.

**Regola operativa: prima di correggere una riga di `toppe.jsonl`, guardare se
qualcuno la genera.** Il file è per due terzi prodotto — `toppe a mano: 230,
generate: 33` — e una modifica a una toppa generata sopravvive esattamente fino
al prossimo `genera_toppe_*`, cioè fino al prossimo lotto. Se la genera uno
strumento, la correzione va **nello strumento**.

⚠️ Nota di metodo: il difetto raddoppiato **si vedeva solo a schermo**, di
nuovo. La catena era verde tutte e due le volte — 357 test, identità 72/72,
compilatore muto — perché entrambe le toppe si agganciavano e si applicavano
senza conflitto. Una guardia che conta le toppe non può accorgersi che due
dicono la stessa cosa in due posti.

⚠️ **La lezione, che vale oltre questo caso.** Una coda «in fondo al nome» non è
un posto assoluto: è un posto **relativo a chi scrive dopo**. Prima di appendere
qualcosa a una stringa che altri continuano a comporre, bisogna sapere **chi è
l'ultimo a scrivere**, e in `itemname()` l'ultimo cambia con il tipo di oggetto.
Le due metà erano corrette prese da sole: nessuna guardia poteva vederlo, e
nessuna lettura del sorgente l'aveva visto in due sessioni. **L'ha trovato uno
screenshot**, come le voci tagliate dei menu.

Vedi [[ultima-scrittura-vince]] e [[una-guardia-vale-solo-dove-guarda]].

---

## Due interpolazioni nella stessa funzione, e solo una porta l'articolo — 2026-08-10, ventiduesima sessione

`foodname` (`text.hsp:3211`) compone il nome di ogni cibo cucinato del gioco:
cinque famiglie — carne, verdura, frutta, pasta, dolci — e una decina di piatti
per famiglia. Ma **interpola due cose diverse**, e la differenza decide la resa:

| ramo | cosa interpola | forma |
|---|---|---|
| carne | `refchara(id, DBSPEC_CHARA_NAME_ORG, 1)` | **con l'articolo**: «il minotauro» |
| verdura, frutta, dolci | `ioriginalnameref(id)` | **nuda**: «carota» |

Non è un capriccio del sorgente, è il contratto dei nomi: per le **creature**
l'articolo sta dentro il nome (`contratto-nomi.md` §4), per gli **oggetti** lo
compone `itemname()`. `foodname` pesca dagli uni e dagli altri.

Conseguenza: «carne di il minotauro» non si può scrivere, e nessuna preposizione
italiana lo salva — `di`, `da`, `al` si fondono tutte con l'articolo.

**Deciso:**

- **carne → la creatura fra parentesi**: «bistecca (il minotauro)», «crocchetta
  (la gallina)». Non è un'invenzione: è l'idioma che il sorgente stesso usa per
  attaccare un nome di creatura a un nome di oggetto (`item_func.hsp:2159`).
  Regge l'articolo, regge il genere, e regge anche il valore predefinito
  «animale», che l'articolo non ce l'ha;
- **verdura, frutta, dolci → «di»**, che davanti a un nome nudo non si fonde:
  «insalata di carota», «budino di mela», «crostata di banana».

⚠️ **Il modificatore va dopo, e si può perché sono dinamiche.** L'inglese scrive
`"kitchen refuse " + S`, con l'aggettivo davanti a un nome di genere ignoto — lo
stesso vincolo dei prefissi delle Nefia. Ma in una voce dinamica la resa è
**l'espressione intera**, quindi l'ordine è nostro: `S + " da pattumiera"`. Dove
l'aggettivo deve restare aggettivo si sceglie invariabile in -e:
«S maleodorante». Dove no, diventa un complemento: «S in pappa», «S senza più
forma», «S dall'aria immangiabile».

⚠️ **`ペペロンチーノ` si traduce, `carbonara` no.** Il secondo è una parola
italiana che il giapponese ha traslitterato e l'inglese ha copiato: lasciarla è
farla tornare a casa. Il primo invece prende **l'ingrediente per il piatto**, e
in italiano il piatto ha un nome suo: «aglio e olio».

⚠️ **Da guardare a schermo**: la parentesi è la scelta più visibile di questa
sessione, e i nomi dei cibi sono fra le stringhe che un giocatore legge di più.
Se in inventario legge male, si cambia qui e in un posto solo.

Vedi [[la-testa-porta-il-genere]] e [[una-decisione-nel-posto-sbagliato]].

---

## Quando il giapponese è un copia-incolla, arbitra la mappa — 2026-08-10, ventiduesima sessione

Due quiz portano **lo stesso identico giapponese**:

```
text.hsp:998   「Ｑ．混沌の城《奇形》に住む死霊の神は？」   EN: Fort of Chaos <Collapsed>
text.hsp:1214  「Ｑ．混沌の城《奇形》に住む死霊の神は？」   EN: Fort of Chaos <Hell>
```

Ma le **risposte giuste sono diverse**: `seitou` è `<Azzrssil>` nel quiz 19 e
`<Ulzassil>` nel quiz 28. Stessa domanda, due risposte: uno dei due giapponesi è
un copia-incolla.

Chi arbitra non è nessuna delle due lingue, è il codice che costruisce la mappa:

| forte | chi ci abita | dove sta scritto |
|---|---|---|
| `<Collapsed>` / 奇形 | Azzrssil | `map.hsp:2271` |
| `<Hell>` / 地獄 | Ulzassil | `map.hsp:9009` |

Le due risposte giuste combaciano con **l'inglese**, in entrambi i quiz. Quindi
qui è il giapponese ad avere il difetto, e le rese già in dizionario —
«`<Deforme>`» a 998, «`<Inferno>`» a 1214 — **sono giuste**. Non toccate.

⚠️ Il gemello di «un'etichetta può parlare dello stato del gioco»
(`text.hsp:2271`, 未実装 contro `Summon Joker`): là il codice stava con
l'inglese contro l'annotazione giapponese, qui contro il testo giapponese. La
regola non è «il giapponese arbitra» senza condizioni, è: **il giapponese
arbitra sul significato; sullo stato del gioco arbitra il codice.** Chi
riapre queste due righe trovi qui la ragione, invece di rifare la ricerca.

---

## L'inglese chiama lo stesso giapponese in tre modi, e uno è il nome di un altro posto — 2026-08-10, ventiduesima sessione

ルストール compare tre volte nel sorgente, e l'inglese lo rende **tre volte
diverso**:

| dove | inglese | cos'è |
|---|---|---|
| `chat.hsp:13645` | `Lustor` | «the hill of beginnings, Lustor» — la prosa, che il nome lo spiega |
| `text.hsp:2938` | `Rust Plaza` | il nome della località sulla mappa (ルストール仙窟) |
| `text.hsp:1131` | `Ruoza` | un'esca del quiz 24 |

⚠️ E `Ruoza` **è già il nome di un'altra località**: ルオザ, `text.hsp:2985`,
il campo profughi. Due giapponesi diversi, un inglese solo.

Il lotto precedente aveva tradotto l'esca sull'inglese — «Ruoza» — e il lotto di
oggi stava per introdurre l'altra «Ruoza» a 2985: la collisione sarebbe nata
**dentro un quiz**, dove due risposte identiche non sono un difetto estetico ma
una domanda senza risposta giusta.

**Deciso: ルストール è «Lustor»**, cioè il nome che l'inglese stesso usa dove
spiega la cosa invece di etichettarla. `text.hsp:1131` corretto, `2938` →
«Grotta Eremitica di Lustor» (仙窟 è la grotta dell'eremita; `Plaza` è una
lettura che il giapponese non autorizza).

⚠️ **Regola operativa**: prima di accettare un nome proprio dall'inglese,
cercare il suo giapponese **in tutto il sorgente**. Se l'inglese lo rende in più
modi, quello della **prosa** batte quello dell'etichetta: la prosa lo spiega,
l'etichetta lo abbrevia. Vedi [[una-chiave-che-collide-non-e-una-chiave]] e
[[il-nome-interno-non-e-quello-a-schermo]].

Nello stesso lotto l'inglese ha sbagliato altre tre volte, e il giapponese ha
arbitrato: `Dragon's Volcano` è セルタ火山, il **vulcano di Selta** (nessun
drago); `Shrine of Guardian` è 中央神殿, il **Santuario Centrale**; e la
descrizione di ルストール仙窟 dice «In the desert» copiata dalla Torre del
Miraggio, mentre il giapponese dice **ai piedi della collina** — coerente con la
prosa di `chat.hsp`, dove ルストール è «la collina dell'inizio».

---

## L'ordine di una concatenazione non è un vincolo: si topa — 2026-08-10, ventiduesima sessione

Il 2026-08-10 avevo scritto, poche righe più sotto, che i prefissi delle Nefia
«in italiano andrebbero **dopo** il nome; ma l'ordine lo fissa il codice, che
concatena e basta». **Non era vero**, e a scoprirlo è stato uno screenshot: a
schermo si leggeva «Audace Miniera», «Fatale Miniera», e la domanda è stata
«ma è sbagliato?».

Le rese non lo erano — sono ancorate al giapponese, e `不帰の` («senza ritorno»)
→ «Fatale» è più fedele dell'inglese `King's`, che è un'invenzione. Era
sbagliato **l'ordine**: `死の`, `闇の`, `不帰の` sono genitivi, e in italiano un
genitivo va dopo la testa del sintagma.

### Perché due toppe e non otto

Il primo tentativo agganciava una toppa a ciascuno degli otto `s += lang(...)`
del tipo, facendo premettere invece di accodare. Rosso:
`test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato` prova ogni toppa
**contro il sorgente pinnato**, dove quella riga dice ancora `"Cave"`, mentre in
build dice già `"Grotta"`.

⚠️ **Una toppa può agganciarsi solo a una riga che il dizionario lascia
identica**, cioè a una riga **senza `lang()`** — è la sola forma che coincide fra
sorgente pinnato e albero di build. Le toppe che sostituiscono l'inglese dentro
`lang()` sono un caso a parte: lì l'aggancio è la riga *non tradotta*, e infatti
quella firma nel dizionario non c'è.

Le due righe senza `lang()` erano lì: l'assegnazione del prefisso e l'`if` del
risveglio.

```hsp
s = mapnamerd(...)        →   s = ""                    ; text.hsp:3056
                              s += mapnamerd(...)       ; inserita prima di :3081
```

Gli otto `s += tipo` in mezzo restano intatti e ora scrivono per primi; il
prefisso si riaccoda in fondo, prima del suffisso `《Risveglio》`, che resta dove
stava. Lo spazio si sposta **in testa** ai dieci prefissi del dizionario
(`" Fatale"` invece di `"Fatale "`).

Ripetere l'espressione di `mapnamerd` invece di salvarla è deliberato: è una
lettura di array senza effetti, e dentro un `defcfunc` una variabile nuova
costerebbe più di quanto valga.

Risultato su tutte e **ottanta** le combinazioni: «Miniera Fatale», «Grotta
Iniziale», «Cimitero Impenetrabile», «Lago Informe».

⚠️ **La toppa rompe l'ordine giapponese**, dove il genitivo *precede*. Non fa
danni perché compiliamo la build inglese (`lang()` rende il secondo argomento),
ma se un giorno si costruisse la build giapponese le due toppe vanno escluse.

Concetto: [[l-ordine-di-una-concatenazione-si-toppa]] e
[[una-guardia-vale-solo-dove-guarda]] — qui la guardia guardava il posto giusto,
ed è lei che ha impedito la toppa sbagliata.

---

## Il riquadro di un menu taglia, e il tetto lo dichiara il chiamante — 2026-08-10, ventunesima sessione

La sessione ha tradotto 258 firme di `text.hsp` (dal 45% al 60%), ma la parte
che vale di più è una misura e la guardia che ne è nata.

### Il difetto

Uno screenshot del menu della frusta da domatore, chiesto a metà sessione e non
alla fine, ha mostrato otto frasi diverse che finivano **allo stesso identico
pixel**. Otto stringhe che si fermano nello stesso punto sono un taglio, non una
coincidenza: **il riquadro taglia**, non manda a capo e non restringe il
carattere.

### La misura

Il metro non è a schermo, è nel sorgente: lo passa il chiamante a `*prompt_key`.

```hsp
val = promptx, prompty, 300, 1
```

Due letture dello stesso giorno — 300px → 33 caratteri visibili, 500px → 55 con
margine — danno

    caratteri = (pixel − 46) / 7,7

I 46 pixel se ne vanno nella colonna della lettera di scelta. Le due costanti
sono una **lettura con una data**, non una proprietà del motore: stanno in un
punto solo (`strumenti/larghezze.py`) e due test le fissano, così se un giorno
una voce dentro il tetto uscisse tagliata fallisce prima la misura del resto.

### L'inglese non è il budget, e qui `guida-stile.md` si corregge

Su 20 menu con voci fuori misura, **in 10 sforava anche l'inglese**:
`txtsettamer` ha una voce inglese da 46 caratteri in un riquadro da 32, tagliata
a monte da sempre. La regola scritta il 2026-08-07 — «il tetto di un campo è la
stringa inglese più lunga che ci compare» — vale dove il numero non c'è; dove
c'è, vince il numero.

⚠️ **Sette delle 41 voci fuori misura non erano di questa sessione.** Avevo
preso a modello «Quando agisce da solo, vaga lontano.» della quinta e copiato il
difetto invece di misurarlo.

### La stretta ha corretto anche un accordo

«Quando agisce da solo» non entrava in 32 caratteri. La resa che ci sta —
«Senza ordini» — **è anche invariante di genere**, che l'altra non era: «solo»
concordava col compagno. Un vincolo di spazio che costringe a tornare sulla
fonte migliora la traduzione, come già per le teste diverse di `skill.hsp`.

### Tre trappole nel leggere la larghezza, e una nella guardia

- `450 - 50 * en`: la larghezza **dipende dalla lingua**, e la nostra è la build
  inglese (`map_user.hsp:1228`);
- il `val =` può stare cento righe sotto la chiamata: i 35 menu del quiz ne
  condividono uno solo (`chat.hsp:13055`);
- dentro un `#deffunc` di menu solo le assegnazioni a `s(cnt)` sono voci; un
  `txt lang(...)` come `text.hsp:1310` è la domanda del quiz e non ha tetto;
- ⚠️ e la guardia cercava i chiamanti per **convenzione di nome**
  (`txt(set|select)\w+`): `txtplusbody` non la segue e restava l'unico non
  misurato, con l'aria di essere codice morto. Ora i nomi si leggono dal
  sorgente. Terzo esemplare di [[una-guardia-vale-solo-dove-guarda]].

---

## Un prefisso che precede otto generi può solo essere un aggettivo in -e — 2026-08-10

I nomi delle Nefia a caso si compongono di due pezzi che stanno a cinquecento
righe di distanza:

```hsp
s  = mapnamerd(...)          ; text.hsp:3056, il prefisso
s += lang("洞窟", "Cave")     ; text.hsp:3058, il tipo
```

Il tipo era **già tradotto** a `text.hsp:50` e ha **genere misto**: Grotta,
Torre, Foresta, Tana, Miniera femminili; Forte, Cimitero, Lago maschili. Il
prefisso li precede tutti e otto e non può accordarsi.

Il giapponese non ha il problema perché i suoi prefissi sono genitivi — 死の,
闇の, 不帰の — che in italiano andrebbero **dopo** il nome; ma l'ordine lo fissa
il codice, che concatena e basta.

> ⚠️ **Questo capoverso è stato smentito il 2026-08-10, ventiduesima sessione.**
> L'ordine *si topa*, e costa due toppe: il vincolo che qui davo per
> insuperabile non c'era. La resa a schermo oggi è «Miniera Fatale». Vedi
> «L'ordine di una concatenazione non è un vincolo: si topa», in cima.
> Resta valida la parte sugli aggettivi in -e: quella è imposta dal genere.

**La resa: solo aggettivi in -e**, invarianti di genere al singolare. Iniziale,
Mite, Audace, Palpitante, Ingannevole, Illustre, Mortale, Impenetrabile,
Fatale, Informe. Qualche fedeltà si perde — 混沌の è «Informe» e non «Caotico» —
ed è il prezzo del vincolo, non una svista.

Conseguenza operativa: **un lotto non deve per forza essere una zona di riga**.
Questo si è preso a cavallo di due zone lontane perché i due pezzi non si
possono scrivere separati.

---

## Domanda aperta: `Cyber Dome` fu deciso sull'inglese, non sul giapponese — 2026-08-10

Il 2026-08-07 `Cyber Dome` → «Cupola Cibernetica», con la regola dei nomi
descrittivi. Ma il giapponese (`text.hsp:2791`) è **アクリ・テオラ**, cioè un nome
**opaco**, che per la stessa regola resterebbe invariato — come `Vernis` o
`Lesimas`. La decisione è già scritta anche in `db_creature.hsp` («l'abitante
della cupola cibernetica»), quindi riaprirla tocca più file.

**Non toccata**, solo segnalata. Se si riapre, si riapre insieme a tutti i siti.

---

## Quattro difetti negli strumenti, trovati traducendo — 2026-08-11, diciannovesima sessione

La sessione ha tradotto 439 firme di `action.hsp` e 45 di `chara_func.hsp`, ma
la parte che vale di più è un'altra: **quattro guardie erano rotte**, e tre lo
erano in modo da rendere certe voci intraducibili.

### 1. La guardia sulla rinomina leggeva un file solo

`evoluzioni_con_jp()` ha `action.hsp` come percorso di default, e tutti i test
che la usano guardavano lì. Gli stessi `evold` stanno in
`custom_enemyevolution.hsp`, `ai.hsp` ed `event.hsp` — i tre file entrati nel
perimetro **proprio perché** lì le rinomine erano morte.

Il controllo esteso — ogni `evold` deve combaciare in testa o in coda con
almeno un nome che può incontrare, cioè i 1.427 nomi di creatura più i 176
`evname`, perché le evoluzioni si incatenano — ha dato **249 su 250**.

L'unica rotta: `<Gwen> l'innocente` contro `evold` «la fanciulla innocente».
Resa «l'innocente», che combacia in coda e produce «<Gwen> la guerriera
innocente», la forma che il database usa già per «<Gwen> la guerriera
spietata». ⚠️ **In inglese quella rinomina è rotta anche upstream**: `the
innocent girl` non è né prefisso né suffisso di `<Gwen> the innocent`. In
giapponese funziona. Vedi [[una-guardia-vale-solo-dove-guarda]].

### 2. `is2` non era dichiarata morfologia inglese

`init.hsp:1768`: la copula accordata al **numero** (`are`/`is`), gemella di
`is` che si accorda alla persona. Fuori dall'elenco, `verifica.py` pretendeva
che la resa italiana la conservasse — cioè chiedeva di scrivere «is» dentro una
frase italiana.

Riletto il sorgente invece di aggiungerla a mano: le `#defcfunc` di `init.hsp`
che restituiscono **solo** stringhe inglesi nude sono quattordici, e `is2` era
l'unica assente. Il test ora rilegge quell'elenco dal sorgente.

### 3. Il parser leggeva il testo come codice

`"Manuscript production (" + gdata(...) + " inspiration) "`: la ricerca delle
chiamate vedeva una funzione `production`, e nella resa italiana una
`manoscritti`. Nessuna resa con una parentesi dopo una parola poteva passare.
Aggiunta `_maschera_letterali`. Vedi
[[il-testo-dentro-la-stringa-non-e-codice]].

### 4. Una resa vuota non ha modo di essere dichiarata

`action.hsp:4584` compone `lang("", "The ")` davanti al nome di un'arma unica:
il giapponese è vuoto, e vuoto è giusto anche in italiano perché il nome porta
già il suo articolo. Ma `verifica.py` rifiuta le rese vuote, **e fa bene**:
quasi sempre sono righe dimenticate. Risolto con due toppe che svuotano lo slot
inglese, più una riga in `rinviate.jsonl` con
`rinviata_a: nessuna fase: risolta da toppa`, altrimenti la firma tornava in
testa a ogni estrazione per sempre.

## Le decisioni di resa che vale la pena non rifare

- **La preposizione sta nel valore, non nella frase.** Le quattro frasi dei
  campi coltivati concatenano tutte « di » davanti alla variabile del tipo di
  seme: « di » + « erba » dava «un seme di erba». Ora il valore è «d'erbe»,
  «d'artefatti», e le frasi non portano la preposizione. È lo stesso criterio
  dell'articolo dentro il nome di creatura.
- **I nomi d'arma di `action.hsp` portano l'articolo; quelli di `db_item.hsp`
  no.** I primi finiscono in `" con " + s(i)` e non hanno nessuno che gliela
  metta; i secondi hanno l'array parallelo degli articoli. Stessa parola, due
  forme, e la forma la decide chi stampa.
- **`Sense Quality` non è un nome:** è l'identificativo interno dell'abilità
  che a schermo si chiama «Analisi» (`skill.hsp:252`). Vedi
  [[il-nome-interno-non-e-quello-a-schermo]].
- **Le continuazioni del danno sono invarianti di genere** — «ne fa cenere»,
  «infligge una ferita profonda» — perché il bersaglio è già nominato nella
  prima metà della frase e il complemento si può omettere. Vedi
  [[la-frase-che-si-compone-in-due-file]].
- **La battuta dell'orso di James** (`chara_func.hsp:6852`) era già morta prima
  di questa sessione: `cnv_str` cercava «was killed by motuhegui» in una
  stringa che ora contiene «lo sbudellatore». ⚠️ Le due toppe che la riparano
  vanno in **ordine invertito** rispetto al sorgente, perché «lo sbudellatore»
  è prefisso di «lo sbudellatore marmocchio» mentre «motuhegui» non lo era di
  «gaki-motuhegui». Stesso criterio che upstream applica in `fix_wish`
  (`module.hsp:4805`): forme lunghe prima.

## Un metodo cambiato: i lotti si prendono per zona di riga

Separare statiche e dinamiche aveva messo le otto metà di frase in « and » in
un lotto e le loro gemelle in un altro. Dalla quarta sessione di lotti si
prende una **zona contigua** del file: il sorgente attorno si legge una volta
sola, e le frasi spezzate restano insieme.

## `ドレイク` è «draco», e il refuso di `action.hsp:17390` non era un refuso

Decisa il 2026-08-10, diciassettesima sessione, col lotto `drake`.

La sedicesima sessione aveva lasciato in sospeso una voce già tradotta:
`action.hsp:17390`, `電気竜` → «il **draco** elettrico», unica occorrenza
contro decine di «drago». La lettura era «è una lettera, non una distinzione»,
e il commento diceva che andava corretta in un commit suo.

Il lotto `drake` ha costretto a guardarla di nuovo, e ha ribaltato la
conclusione. La razza è **亜竜**, che il sorgente dichiara e le carte ripetono
per ognuno dei suoi membri: `viashivan` è «mezza lucertola», `mass monster` è
«una sottospecie di drago», `powerful great wyrm` regna «sui sub-draghi».
Serviva quindi un **gradino sotto «drago»**, e in italiano esiste: **«draco»**
è il nome del *Draco volans*, la lucertola planante — l'immagine giusta per un
drago minore.

⚠️ **E soprattutto: correggere avrebbe creato una collisione.** `電気竜` è
l'evoluzione di `電気羊` (`evold`/`evname` a `action.hsp:17390-17391`), mentre
`エレキドラゴン` è un'altra creatura e ha **già** il nome «il drago elettrico».
Due mostri diversi non possono uscire a schermo con lo stesso nome. La voce
resta com'è ed esce dalle cose in sospeso.

**Cosa serve per cambiare idea.** L'obiezione vera è che «draco» e «drago»
differiscono di una lettera, ed è esattamente per questo che la sessione prima
l'aveva letta come un errore di battitura: se al collaudo in gioco i due nomi
si confondono, l'alternativa è **«dragonetto»**, e il costo è tre nomi del
lotto `drake` più quella voce. La decisione è registrata qui proprio perché è
la più revisionabile della sessione.

✅ **Confermata a schermo il 2026-08-10, diciottesima sessione.** I tre draco
(`97`, `98`, `580`) sono stati evocati accanto a `<Vansesda> il drago della
fiamma primordiale` e guardati insieme. Non si confondono: l'utente ha scelto
di tenere «draco». Esce dalle decisioni revisionabili — la prova che serviva
era proprio quella, e non poteva darla il sorgente.

Vedi `glossario.md`, «Le teste di famiglia dei nomi di creatura».

## Un nome già preso non è disponibile, e va cercato prima

Stessa sessione, tre volte. `メイド` non poteva essere «la cameriera» perché
`メイドさん` lo era già; `沙羅曼蛇` non poteva essere «la salamandra» perché
`メガサラマンダー` lo era già; `ローパー` non poteva essere «la melma
tentacolare» perché `スライムローパー` lo era già.

Nessuno dei tre casi è stato trovato dagli strumenti: `verifica.py` controlla
che l'italiano non sia identico all'inglese, non che sia unico fra le
creature. **Li ha trovati la ricerca a mano nel dizionario**, fatta prima di
scegliere.

⚠️ **Vale la pena farne una guardia?** Forse no, e la ragione è che
l'omonimia non è sempre un errore: `伝説の職人『ガロク』` e
`伝説の職人『ミラル』` sono entrambi «il fabbro leggendario», come in
giapponese, perché il nome proprio fra `<>` li distingue. Una guardia che
vietasse i duplicati boccerebbe anche quelli. Per ora resta una **cosa da
fare a mano**, scritta in `RIPRESA-sessione.md`.

## Quando le due lingue si nominano invece di descriversi

Estensione della regola di `<Amurdad>` già in `invariati.md`. Su
`星見の『サリム』` il giapponese dice サリム e l'inglese `<Thalia>`: non sono
due traduzioni della stessa cosa, sono **due nomi diversi**. Si tiene la forma
inglese, che è quella che il gioco mostra. Stesso caso per `白虎の『サンゲツ』`
(`<Lityou>`) e `モー・ショボー` (`mayu sibayu`).

⚠️ **Da non confondere col caso in cui l'inglese sbaglia**, che in questa
sessione è capitato decine di volte. Il discrimine è se le due forme *provano*
a dire la stessa cosa: `機甲将軍` e `iron colonel` sì — e allora una delle due
ha torto, ed è l'inglese; `サリム` e `Thalia` no.

---

## Come è andata la Fase 0

La catena `estrai → verifica → reimporta → applica` esiste, è coperta da **83
test** ed è stata provata end-to-end sul sorgente vero. Ma il **cancello vero
della Fase 0 non è ancora passato**: ricompilare l'eseguibile da sorgente non
modificato richiede la GUI dell'SDK HSP 3.4. Finché non passa, quella che
abbiamo è una *catena verificata*, non un *gioco verificato*.

### La prova che conta più di tutti i test

Un **dizionario identità** — ogni stringa tradotta in sé stessa — deve
riprodurre i file byte per byte. È la verifica più forte disponibile su questa
catena, perché non dipende da quali casi qualcuno si è ricordato di scrivere:
copre ogni sito del corpus reale.

Esito: **73 file su 73 identici**, con 22.602 sostituzioni eseguite.

È stata questa prova, e non i test, a trovare i due difetti più gravi del
progetto.

### I quattro difetti che i test non hanno visto

Tutti e quattro producevano **corruzione silenziosa**: virgolette pari,
parentesi bilanciate, nessun errore, sorgente rotto.

1. **Il parser era cieco all'escape `\"`.** 195 righe del sorgente lo usano.
   Costo misurato: 11 `lang()` perse, 295 voci con l'inglese mutilato, e 5 span
   sbagliati su cui `applica.py` sostituiva facendo **sparire dal sorgente** una
   chiamata `_onii(cdata(...))` e un'intera coppia `lang()`. Perdita di logica di
   gioco, non di testo.
2. **`e_dinamica` cercava il `+` anche dentro il testo.** 163 stringhe statiche
   contengono un `+` (`"Enchantment Bonus + 4"`, `"RES+ magic"`) e venivano
   classificate dinamiche, il che faceva finire l'italiano **nudo** nel sorgente.
   86 in file di Fase 1.
3. **Statiche avvolte in una chiamata.** `lang("…", cnvtalk("Urchinn!"))` non ha
   un `+` di primo livello, quindi è statica — ma sostituire l'intero span fa
   sparire `cnvtalk`. Sono **3.499**, in due sole forme: `cnvtalk(` (3.423) e
   `cnven(` (76).
4. **Firme che collidono su espressioni diverse.** La firma si calcola sui soli
   letterali, quindi `name(gdata(GDATA_RIDER)) + " glare"` e
   `cdatan(CDATAN_NAME, ttc) + " glare"` condividono la chiave: la traduzione
   dell'una finirebbe sull'altra portandosi dietro **le variabili sbagliate**.
   Sono **77 firme**, 334 occorrenze.

I primi due sono corretti. Il terzo e il quarto sono **rifiutati con un errore
esplicito** che nomina file, riga, firma e causa: la catena si ferma invece di
corrompere. Non è la soluzione definitiva, è il rifiuto onesto.

### Perché rifiutare invece di risolvere

Il cancello della Fase 0 è «la catena non corrompe il sorgente», e rifiutare lo
soddisfa in modo dimostrabile. Il caso 4 in particolare è una modifica allo
schema della chiave, cioè a `SPEC.md` §3.2: va decisa a mente fredda, non
improvvisata dentro una correzione.

---

## Il cancello è passato — 2026-08-06, seconda sessione

Il sorgente non modificato **ricompila**, l'eseguibile che ne esce si avvia dalla
cartella del gioco e **carica un salvataggio esistente**, provato in gioco. Da
*catena verificata* a *gioco verificato*: il salto che il progetto aspettava.

Il caricamento del salvataggio chiude anche la questione aperta dal pin: l'exe
ricompilato dal tag `2.31.2.0` e i dati della 2.31.2.0 installata sono
compatibili, nonostante la costante di versione discordante. Il disallineamento
è nominale, non sostanziale.

### La GUI non era un vincolo, era un'assunzione

`hspcmp.dll` espone l'intera API del compilatore: `hsc_ini`, `hsc_comp`,
`hsc3_make`. L'unico ostacolo reale è che la DLL è a **32 bit** e un Python a 64
non la carica. Windows ha però già un host a 32 bit installato di serie,
`SysWOW64\WindowsPowerShell`, e da lì si pilota tutto.

Tre trappole, nell'ordine in cui sono costate:

1. **I nomi puliti di `hspcmp.as` non esistono nella tabella di export.** Sono
   tutti decorati: `_hsc_ini@16`.
2. **L'ABI dei plugin HSP passa sempre quattro slot, e non nello stesso ordine
   per tutti.** Dal disassemblato: chi prende una stringa la legge da `[esp+8]`,
   cioè lo **slot 2**, con lo slot 1 inutilizzato; chi prende un buffer lo legge
   da `[esp+4]`, lo **slot 1**. Passare la stringa nel primo slot non dà errore:
   fa saltare il processo con una access violation. Questo è il motivo per cui
   `test_compila.py` verifica le firme dichiarate — è l'unica difesa contro una
   "semplificazione" che riporterebbe il crash.
3. **`Set-Location` non sposta la cwd del processo**, solo quella di PowerShell.
   La DLL legge la cwd vera e rispondeva `Source file not found` su un file che
   esisteva. Gli `#include` del sorgente sono relativi, quindi la cwd conta.

Il cancello è ora un comando: `python -m strumenti.compila --cancello`. Gli
strumenti si rifiutano di scrivere dentro `sorgente/`, e la costruzione dell'exe
è ammessa solo fuori, perché `#pack` scrive `packfile` nella cartella corrente.

### Il sorgente era sul ref sbagliato

Il clone era sulla testa di `work`, che dichiara **2.32.1.2** — una versione non
rilasciata — mentre `SPEC.md` decisione 7 sceglie la base 2.31. Il tag `2.31.2.0`
esiste, compila, ed è immutabile: il sorgente è stato pinnato lì (`a9135a6`).

Un branch che si muove è la peggiore base possibile per questo progetto: al primo
`git pull` manifesto e conteggi diventerebbero falsi **senza alcun segnale**. Il
pin costa una rimisura del corpus, e il momento più economico per pagarla è
adesso, con `dizionario/` vuoto.

Un fatto emerso strada facendo, che non è un difetto nostro: **il binario
installato non è riproducibile da nessun ref pubblico**. Il tag `2.31.2.0`
dichiara `VARIANT_TITLE "… 2.31.1.0"` e produce un eseguibile intitolato così;
nessun commit della storia dichiara `2.31.2.0`. La costante non è stata aggiornata
al rilascio. Tocca solo il numero nel titolo, non il testo da tradurre.

### I numeri, rimisurati sul tag

| | prima (testa di `work`) | ora (tag `2.31.2.0`) |
|---|---|---|
| occorrenze `lang()` | 26.817 | 26.588 |
| traducibili | 26.434 | 26.206 |
| da tradurre (uniche per file) | 21.965 | 21.795 |

**Il 21.965 non era sbagliato**, contrariamente a quanto sembrava a prima vista:
è l'unicità **per file**, che è l'ambito dichiarato in `SPEC.md` §3.2 e realizzato
dal partizionamento del dizionario in un `.jsonl` per file sorgente. Le firme
distinte sull'intero corpus sono invece 19.399: la differenza, 2.396 traduzioni
pari all'11% del lavoro, è il prezzo misurato dell'ambito per-file. Da conoscere
prima di discuterlo, non una proposta di cambiarlo.

---

## Domande aperte, da decidere prima della Fase 1

### 1. La firma delle dinamiche include l'espressione — DECISA il 2026-08-06

**Sì, ma solo per le dinamiche**, e con gli spazi normalizzati.

Il nodo: `firma = sha1(giapponese + NUL + inglese)` usava i soli letterali, e per
le dinamiche faceva collidere espressioni diverse che condividono il testo — 77
firme, 327 occorrenze. Includere `en_grezzo` risolve la collisione ma rende la
chiave fragile: rinominare una variabile a monte la rompe a testo invariato.

**Quello che scioglie il nodo è che i due errori non costano uguale.** Una chiave
troppo debole scrive codice sbagliato **in silenzio** — la traduzione di
`name(gdata(GDATA_RIDER)) + " glare"` iniettata su `cdatan(CDATAN_NAME, ttc) + " glare"`
si porta dietro le variabili sbagliate. Una chiave troppo fragile manda la stringa
in **coda di ritraduzione**, dove una persona la guarda. È la stessa asimmetria su
cui il progetto aveva già deciso con le decisioni 13 e 14: preferire il guasto
rumoroso a quello silenzioso.

Due correttivi tolgono quasi tutta la fragilità:

1. **la firma normalizza gli spazi**, quindi reindentare a monte non rompe nulla;
2. **la voce conserva `jp` ed `en`**, quindi una firma orfana la cui coppia
   corrisponde a una sola firma nuova si riaggancia meccanicamente. La fragilità
   diventa recuperabile invece che distruttiva.

Le statiche restano com'erano: includere l'involucro sarebbe churn senza guadagno.

**Il prezzo, misurato e non stimato:**

| | prima | dopo |
|---|---|---|
| da tradurre (uniche per file) | 21.795 | **22.030** (+235) |
| occorrenze irraggiungibili | 327 | **3** |
| sostituzioni nella prova d'identità | 22.414 | **22.738** (+324) |

Le 3 residue non sono una collisione di espressioni: sono la stessa statica
presente sia nuda sia avvolta in `cnvtalk(`, in `db_creature.hsp`. Per le statiche
l'involucro non entra nella chiave, quindi condividono la firma pur volendo
sostituzioni diverse. Spariranno quando la sostituzione dentro l'involucro sarà
implementata — che è comunque il punto 1 del piano di Fase 1.

Il controllo in `applica.py` che rifiutava le collisioni **resta**, ma cambia
significato: il sorgente non le produce più, quindi ora è la difesa contro una
voce di dizionario ritoccata a mano. Confronta le espressioni normalizzate, non
le grezze: differire di soli spazi non è un motivo per abortire un build.

### 2. Il rifiuto arriva troppo tardi nel ciclo

`estrai.py` emette comunque le 3.833 occorrenze dei casi 3 e 4 nei lotti, e
`verifica.py` non le segnala. Un traduttore le traduce, `reimporta` le accetta, e
solo `applica` esplode — abortendo l'intero build su un caso alla volta.

Il rilevamento va spostato a monte, in `estrai`/`verifica`, o le voci vanno
marcate nel lotto. Altrimenti si scopre il problema dopo aver tradotto.

---

## Rilievi parcheggiati

Reali ma non bloccanti, valutati e lasciati:

- `applica.py` importa ancora il privato `estrai._argomenti` per `_profilo`.
- `applica.main()` scrive i file uno alla volta: un errore lascia l'albero di
  build a metà. Innocuo perché `build/` è usa e getta, ma incoerente col rigore
  tutto-o-niente applicato a `reimporta`.
- Il controllo del caso 4 è saltato in silenzio se una voce di dizionario
  ritoccata a mano è priva di `en_grezzo`: `verifica.py` lo pretende, ma
  `applica.main()` legge i `.jsonl` senza passare da `verifica`.
- `_letterali` conserva gli escape come `\"` invece che `"`: fedele e
  reversibile, ma chi traduce lo vede nel campo `en`. Da fissare nella guida di
  stile.

---

## Da portare nel piano della Fase 1

Chiuso tutto il 2026-08-07.

1. ~~Sostituzione dentro `cnvtalk(` / `cnven(`~~ — **fatta** (Task 2).
2. ~~La decisione sulla firma delle dinamiche, §3.2~~ — **fatta**, vedi sopra.
3. ~~Spostare a monte il rilevamento delle statiche avvolte~~ — **decaduta**: dal
   momento in cui si sostituiscono, non c'è più niente da segnalare a monte.
4. ~~La whitelist `invariati.md`~~ — **fatta** (Task 3).
5. ~~`verifica --dizionario`~~ — **fatta** (Task 4).

---

## La quarta sessione — 2026-08-07

### Il registro: terza persona, e `init.hsp` risale alla Fase 1

Il piano della Fase 1 affermava che qui il «tu» fosse sicuro, «perché le righe
del giocatore e quelle dei PNG sono chiamate `lang()` diverse». **È falso**, e la
guida di stile stava per essere scritta su quella premessa.

`init.hsp:1699` — `name()` risolve da sé chi è il soggetto:

```hsp
if ( name_arg1 == CHARA_PLAYER ) { return lang("あなた", "you") }
...
return "the " + cdatan(CDATAN_NAME, name_arg1)
```

Una sola `lang()` serve entrambi, come il `#1` di Elin. Il caso canonico è
`text.hsp:3137`: `name(X) + " lose" + _s(X) + " patience."` diventa «you lose
patience.» oppure «the putit loses patience.» L'inglese se la cava con `_s()`,
che è morfologia; l'italiano no, e il Task 1 aveva già stabilito che `_s()` va
tolta. Resta una forma verbale sola, e la seconda persona non regge: «il putit
perdi la pazienza».

Misurato sui sei file di Fase 1: 1.522 dinamiche, **901 con `name()`**, **472
(31%) con un marcatore di morfologia**, cioè dimostrabilmente condivise.

**Decisione: terza persona singolare presente indicativo**, l'unica forma senza
accordo di genere. `you` → «il viandante», `he`/`she` → «lui»/«lei».

**Conseguenza sul piano: `init.hsp` non è lavoro di Fase 4, è una premessa della
Fase 1.** Sei voci tradotte subito, 16 sostituzioni.

Elin era arrivata alla stessa conclusione dopo averlo visto a schermo; qui è
arrivata prima, leggendo il codice.

### Le stringhe che sono dati — la trappola peggiore trovata finora

Le otto stringhe di `CDATAN_NEWSEX` (`male`, `female`, `none`, `hermaphrodite`,
`male?`, `female?`, `trans-male`, `trans-female`) stanno **nella stessa funzione**
dei pronomi appena tradotti, dentro `lang()` identiche a quelle dei messaggi.
Sembrano testo. Non lo sono: `chara.hsp:2790` e `4390` le **scrivono** nei dati
del personaggio, `init.hsp:1813-1823` le rilegge come **operandi di confronto**, e
i dati del personaggio finiscono nel salvataggio.

Tradurle non rompe niente il giorno stesso: rompe il genere di ogni personaggio
creato **prima** della traduzione, cioè vanifica in silenzio proprio ciò che il
cancello della Fase 0 aveva verificato con cura — che i salvataggi esistenti si
carichino.

Sono in `invariati.md`, sezione «valori di dato, non testo». La ricerca da fare
prima di tradurre un file nuovo:

```
grep -nE '(=|==|!=|instr\().*lang\(' <file>.hsp
```

**La prova d'identità non le prende**, ed è importante saperlo: la stringa cambia
legittimamente, la forma resta valida, ed è il significato a rompersi. Contro
questa classe serve la lettura, non il round-trip.

### `toppe.jsonl` — le sostituzioni fuori da `lang()`

`init.hsp:1718` concatena `"the "` davanti al nome dei PNG **fuori** da una
`lang()`: il dizionario non lo raggiunge, e senza quel pezzo la decisione sul
registro non sta in piedi. Sul sorgente intero i casi così sono **dieci**, in
quattro file.

Non è una deroga alla §3.1: come il dizionario, le toppe sono dati esterni
applicati all'albero di build. Verificato col manifesto dopo la build, 72/72 hash
concordi. Hanno un giro proprio in `applica.main()` e **la prova d'identità non ci
passa**, quindi la garanzia byte per byte resta quella di prima.

**La toppa toglie invece di scegliere.** L'articolo italiano dipende da genere ed
elisione — *il* putit, *lo* gnomo, *l'* orco — che si sanno per nome e non per
regola. Il prefisso si rimuove e l'articolo lo porterà il nome della creatura in
`db_creature.hsp`, **dove a decidere è un umano**. È una decisione di Fase 2 e
vale per ogni uso di `cdatan()`, non solo per `name()`.

`custom_dmgpop.hsp:224-231` *legge* la stringa `"the "` per toglierla dagli
alias: era il rischio di accoppiamento silenzioso. È protetto da `instr(...) !=
-1`, quindi senza `"the "` diventa un no-op — verificato leggendolo.

### La re-revisione di `dfe530b`: un fratello del difetto

I due punti che il rilievo chiedeva reggevano. Ma il controllo lasciava passare
`cnvtalk("x"), cnvtalk("y")`: il gruppo greedy ne cattura `"x"), cnvtalk("y"`, un
frammento con le parentesi **sbilanciate**, dove `virgola_nuda` arriva con la
profondità già a -1 e non vede la virgola di primo livello. La ricostruzione
avrebbe prodotto `cnvtalk("Ciao")`, facendo sparire la seconda chiamata.

La causa era contare sulla struttura di un frammento che per costruzione può
essere sbilanciato. `_e_letterale_singolo` non la interpreta: pretende che fra le
parentesi ci sia un letterale e nient'altro. Zero occorrenze nel sorgente
pinnato: era latente.

### Il primo lotto, visto a schermo

50 stringhe di `text.hsp`, **composte** e non prese in ordine: la prima dinamica
con morfologia sta alla voce 642, e seguire il piano alla lettera avrebbe voluto
`--max 646`. Il lotto è 44 statiche di testa più le 6 dinamiche delle righe
276-290, che sono la prova della decisione sul registro.

Sulle sei, la resa evita i **sostantivi di genere**: «un cittadino rispettoso
della legge» non regge con `he(tc,1)` che può valere «lei». Si traduce con un
verbo — «rispetta la legge di questa pacifica città». Regola generale per le
condivise.

**Il collaudo a schermo è passato il 2026-08-07**: `Non e' roba tua.` letta in
gioco, con l'apostrofo. La degradazione CP932 non è più verificata sui byte, è
osservata. Era il punto in cui il piano diceva di fermare tutto.

Un artefatto atteso dello stato intermedio: «il viandante pick up a book», con il
verbo inglese senza `s` perché `_s(cc)` restituisce `""` per il giocatore.
Sparisce quando `action.hsp` sarà tradotto. E la minuscola iniziale non è una
regressione: nella catena `txt` → `txt_select` → `txt_conv` non c'è nessuna
capitalizzazione, e in inglese quella riga esce «you pick up…» uguale.

## La quinta sessione — 2026-08-07

### I sei termini: cinque erano misura, uno era già deciso altrove

I sei di «Da decidere» sembravano sei scelte di gusto. Misurandoli, quattro
avevano una risposta nei dati e due erano già vincolati da Elin.

**`Gauge` non è prosa.** 60 occorrenze su 75 sono etichette dell'elenco delle
mosse speciali, a larghezza compressa: `[50% Gauge] Party Shooting`. La scelta
non era fra sinonimi ma fra lunghezze — «Barra» costa 5 caratteri come
l'inglese, «Indicatore» ne costava 6 in più su ogni riga. In prosa «barra di
potenza», che si aggancia a `Power` → «Potenza» invece di derogarci.

**La collisione di `Skill` non esisteva.** Il timore era che «Abilità» si
scontrasse con *ability*. Nel sorgente non si incontrano mai: `Skill` è sempre
il concetto di motore, *ability* è quasi sempre prosa generica («enhances your
ability to hide»), che in italiano vuole «capacità». Un dubbio che si scioglie
guardando, non discutendo.

**`Chaos` e `Abyss` erano già decisi**, in `Elin - Traduzione Italiana`: «Caos»
e «Abisso». Sono termini di universo, non di motore, e il glossario dichiara
che quelli devono coincidere fra i due progetti. Non erano da decidere: erano
da andare a leggere.

**`Body` non era un termine, erano tre.** Lo slot d'equipaggiamento
(`text.hsp:136`, giapponese 胴), l'aspetto nell'editor del ritratto (giapponese
体) e la prosa. «Torso» per il primo, perché in fila con Testa · Collo ·
Schiena · Mano · Braccio · Gamba un «Corpo» metterebbe il tutto insieme alle
parti. Registrato anche un vincolo che non si vede dal glossario: l'editor è a
**larghezza fissa di 8 caratteri**, e «Colore corpo» per `Body CL ` non ci sta.

### La regola dei nomi propri, che vale più delle cinque decisioni che l'hanno prodotta

I cinque toponimi aperti si potevano chiudere uno per uno. Ma altri ne
arriveranno a ogni file, e cinque decisioni singole non dicono niente al
prossimo. La regola:

- nome **descrittivo**, fatto di parole comuni → si traduce (`Fort of Chaos
  <Beast>` → «Forte del Caos `<Bestia>`», come `Mages Guild` → «Gilda dei
  Maghi» che era già in glossario);
- nome **opaco**, inventato → resta (`Vernis`, `Larna`, `Arcbelc`, `Lesimas`);
- nome **misto** → si divide (`Port Kapul` → «Porto Kapul»).

È lo stesso criterio con cui Elin ha reso `Blessing of the Abyss`. Chiude anche
il sotto-caso di `Chaos`, che era la ragione per cui quel termine era in
«Da decidere»: l'elemento e i luoghi si decidono insieme perché li decide la
stessa regola.

### 424 nomi di creatura travestiti da testo, in un file di Fase 1

Trovato cercando le occorrenze di `Sister`. `Wolf Sister`, `older sister`,
`younger sister` in `action.hsp` non sono prosa: sono `evname`/`evold`, il
sistema di evoluzione dei nemici. **424 assegnazioni, 232 valori `evold`
distinti, 203 dei quali sono nomi di creatura letterali di `db_creature.hsp`** —
che è Fase 2.

```
if ( strmid(cdatan(CDATAN_NAME, cc), 0, strlen(evold)) == evold ) {
    cdatan(CDATAN_NAME, cc) = evname + strmid(cdatan(CDATAN_NAME, cc), ...)
```

`evold` è l'**operando** confrontato col nome memorizzato del personaggio;
`evname` è il pezzo che lo **sostituisce**, e che poi si legge a schermo come
nome della creatura evoluta. In inglese `evname` non è mai stampato
direttamente: l'unico `txt` che lo contiene (`action.hsp:18632`) lo ha solo nel
ramo giapponese.

È la stessa classe di `CDATAN_NEWSEX`, ma con un vincolo in più: non basta
lasciarli stare. **Vanno tradotti in blocco con `db_creature.hsp`, mai prima** —
se uno dei due è italiano e l'altro no il confronto fallisce e l'evoluzione
smette di rinominare **in silenzio**; e sui salvataggi esistenti si rompono
comunque, perché lì il nome è già inglese. La prova d'identità non li prende.

Non sono fra gli invariati: dichiararli tali deciderebbe di lasciare i nomi
delle creature in inglese per sempre, che è una decisione di Fase 2 e non è
stata presa. Hanno una sezione propria in `invariati.md`.

### Il difetto che rendeva obbligatorio cadere nella trappola

Le otto stringhe di `CDATAN_NEWSEX` **non erano protette**. Verificato:
`carica_invariati()` restituiva dieci valori, e `male` non era fra loro.

La difesa scritta nella seconda sessione era «`carica_invariati` si ferma al
primo `##`», per non leggere i candidati di «Da decidere». Ragionamento giusto,
difesa fragile: quando la sezione «Valori di dato» fu inserita **in mezzo**,
ereditò l'esclusione senza che nessuno lo decidesse.

La conseguenza non era quella che sembrava. Il conteggio «non ancora tradotte»
non ha mai consultato gli invariati. `invariati` entra in un punto solo,
`controlla_voce`, sulla regola «traduzione identica all'inglese». Un lotto che
lasciava `male` → `male`, cioè che faceva **esattamente ciò che `invariati.md`
prescrive**, inciampava in quella regola e `controlla_lotto` rifiutava il lotto
**intero**. L'unico modo di farlo passare era tradurle.

Il controllo non sollecitava la trappola: la **imponeva**.

La correzione non sposta il confine — sarebbe il sintomo, e il prossimo che
aggiunge una sezione rifarebbe il buco. `carica_invariati` legge sezione per
sezione e le **classifica**, e **non c'è un default**: una sezione che porta
valori senza essere classificata alza `ValueError` con scritto cosa fare. Una
sezione di sola prosa non è una decisione, e si ignora.

La lezione, che vale oltre questo file: una difesa fatta di «fermati al primo
X» presume che nessuno inserisca niente prima di X. Una fatta di «ogni caso va
classificato, e il silenzio è un errore» no.

## L'ottava sessione — 2026-08-08

Il secondo lotto dei nomi di `db_item.hsp`: **166 firme**, da riga 150006 a
151839, cioè tutto quel che restava del **corredo vanilla** in coda al file —
cibo ed erbe, l'arredamento della casa, le bacchette, i grimori e le pozioni.
Il lotto non è stato scelto con `--max`: quello prende le prime per **riga**,
che sono gli oggetti aggiunti da CGX e si vedono solo andandoseli a cercare.

### Quattro decisioni di resa che valgono oltre il lotto

**Il giunto è sempre «di», quindi la testa del nome composto può portarsi
dietro il participio.** `grave` + `ornamented with flowers` non poteva diventare
«tomba di fiori ornamentali» senza perdere l'ornamento. La soluzione non è nel
modificatore ma nella **testa**: `ioriginalnameref2` → «tomba ornata»,
`ioriginalnameref` → «fiori», e il giunto cablato fa il resto — «tomba ornata
di fiori», «tombe ornate di fiori». Il pezzo che si flette al plurale è la
testa, quindi l'accordo del participio viene gratis.

**I nomi di divinità restano complemento, e l'epiteto diventa sostantivo.**
`potion of sacred healer <Jure>` non poteva essere «pozione di sacra guaritrice
<Jure>»: il giunto fisso «di» non diventa «della», e senza articolo il
sintagma non regge. Le quattro pozioni curative diventano una scala di
sostantivi — «guarigione», «guarigione <Odina>», «guarigione bianca <Eris>»,
«guarigione sacra <Jure>» — che dopo «pozione di» si leggono tutte. È la
**quinta** volta che il genere ignoto si risolve col sostantivo invece che con
l'aggettivo, ed è la prima in cui il vincolo non è il genere ma la preposizione.

**Quando la parola italiana coincide con l'inglese si dichiara, non si evita.**
Dodici voci su 166: due artefatti che il giapponese traslittera
(《エーテルダガー》, 《ラグナロク》), quattro frutti inventati da Elona
(`leccho`, `qucche`, `imo`, `quwapana`), cinque nomi botanici che l'italiano
scrive uguale (`guava`, `kiwi`, `aloe`, `anemone`, `gazania`) e `whisky`. Sono
tutte righe di `invariati.md` con un motivo scritto, perché senza `verifica.py`
rifiuta il lotto intero — ed è il comportamento voluto: una coincidenza
dichiarata e una traduzione dimenticata si somigliano troppo per distinguerle
a occhio.

⚠️ **Un nome opaco può collidere con una parola comune italiana.**
`api nut` (アピの実) reso «noce di api» si legge «noce di insetti». La maiuscola
lo rimette dov'era: «noce di **A**pi». Da rifare a ogni nome opaco che, tradotto
alla lettera, produce una parola italiana esistente.

### Due rese scelte per non collidere con un'etichetta

`cheap chair` e `cheap bed` sono «sedia **dozzinale**» e «letto dozzinale», non
«scadente»: `scadente` è già la prima delle sei qualità dell'oggetto
(`text.hsp:106`), e le due escono **attaccate** — «una sedia scadente
(Scadente)». Stessa logica di «l'etichetta si legge dove esce» in
`guida-stile.md`, applicata al verso opposto: lì si sceglieva l'etichetta
guardando il nome, qui si sceglie il nome guardando l'etichetta.

### L'articolo: il genere e' il dato, l'articolo e' una derivata

L'inglese sceglie `a`/`an` guardando la **prima lettera** della stringa gia'
composta (`item_func.hsp:1816`), piu' un caso speciale scritto a mano per
`unicorn horn`. Funziona perche' in inglese l'articolo non ha genere: e'
fonetica pura. In italiano l'articolo dipende dal **genere della testa**, che
nella stringa composta sta in mezzo — «una pozione di cura delle ferite lievi»
— e nessuna lettera lo rivela.

Il genere entra quindi nel dizionario come quinta colonna dei nomi, accanto al
plurale, e per la stessa ragione: non si deduce. Ma **l'articolo no**. Una
volta noto il genere, la scelta fra «un» e «uno», fra «la» e «l'», e' una
regola meccanica sulla forma della parola che segue — s impura, z, gn, ps, pn,
x, y, semiconsonante, h muta. Chiederla a chi traduce vorrebbe dire chiedergli
di applicare a mano una regola che una macchina applica meglio, e raddoppiare
le occasioni di sbagliarla. La deriva `strumenti/articolo.py`; nel gioco arriva
la stringa gia' fatta, come per il plurale.

**Il numero fa parte del genere**, e i valori sono quattro: `m`, `f`, `mp`,
`fp`. Non e' pignoleria: in `db_item.hsp` i nomi che esistono solo al plurale
non sono pochi — «cianfrusaglie», «attrezzi», «armi», «vestiti» — e su quelli
l'articolo indeterminativo **non esiste**. Ci vuole il partitivo, «delle
cianfrusaglie», che e' esattamente cio' che l'inglese sbaglia gia' oggi
scrivendo «a goods».

⚠️ **Le parole-contatore cablate vincono sull'array, al contrario del
plurale.** Quando `itemname()` mette «paio» davanti al nome, la testa del
sintagma diventa «paio» e l'articolo lo regge lui: «un paio di stivali
pesanti», non «uno stivali pesanti». Il plurale non ha lo stesso problema
perche' li' l'array e la parola cablata non sono mai pieni tutti e due.

L'articolo si scrive **solo sulla testa**: 207 oggetti su 252 voci tradotte,
perche' i composti hanno due voci e una testa sola.

### I 252 composti, e la terminologia degli incantesimi

Le teste non si sono decise nel lotto: erano gia' in `contatori.jsonl`. Il
lavoro erano i **218 modificatori distinti**, e il giapponese e' servito piu'
di una volta a non sbagliare — `butuzou` e' 仏像, la statua di Budda; `soul` e'
リンカネイト, la reincarnazione; `acid ground` e' 酸の海, che alla lettera e' un
mare d'acido ma in gioco e' un suolo.

Da qui in avanti questa terminologia vincola `skill.hsp`, che gli stessi
incantesimi li nomina di nuovo:

- **la famiglia dei dardi** segue quella gia' a schermo (dardo di fuoco, di
  ghiaccio, di fulmine). Per l'elemento si usa **l'aggettivo dove l'italiano ce
  l'ha** — mentale, caotico, oscuro, sonoro, neurale, che e' anche cio' che il
  glossario aveva gia' deciso per `Mind` e `Chaos` — e il **complemento dove
  no**: di veleno, d'oltretomba, d'acqua;
- `magic bolt` e `magic missile` **convivono nel sorgente**, quindi devono
  convivere anche in italiano: «dardo arcano» e «dardo magico». Una resa sola
  per due nomi diversi fonderebbe due oggetti distinti in uno;
- `magical map` (pergamena) e `magic mapping` (grimorio e bacchetta) hanno lo
  **stesso giapponese** 魔法の地図 e nomi inglesi diversi: «mappa magica» e
  «cartografia magica». Quando l'inglese distingue e il giapponese no, la
  distinzione si tiene: e' l'inglese la lingua da cui si traduce.

⚠️ **`Mani` entra negli invariati con una nota che vale oltre lui.** La
divinita' si chiama Mani, e «mani» minuscolo e' una parola italiana
comunissima: la maiuscola non e' decorativa, e' cio' che tiene «statua di Mani»
distinto da «statua di mani». Stessa classe di `noce di Api` del lotto
precedente, ed e' la seconda volta in un giorno.

### Due rese di `contatori.jsonl` riviste

Il secondo lotto aveva reso `lot` e `variety` senza guardare il termbase, e ci
sono finite dentro due deviazioni. Non si e' derogato nel lotto: si e'
cambiato il termbase, che e' la regola scritta in testa a `glossario.md`.

- `lot` → **mucchio**, non «lotto»: 本の山 e' una pila di libri, e «un lotto di
  libri» e' gergo commerciale;
- `variety` → **assortimento**, non «varietà»: regge meglio dopo «di» e non
  porta un accento in un punto molto visibile.

## La nona sessione — 2026-08-08

Sei blocchi, dodici commit, il primo push. `db_item.hsp` dal 47% al 63%.

### «Stessa forma» era un'ipotesi, e quattro array su quattro l'hanno smentita

Il documento di ripresa dava `_furniture`, `_bookself`, `_weight` e
`_bookselfs` per «la stessa identica forma»: sono tutti aggettivi prefissi in
`text.hsp`, e nel **dizionario** si somigliano davvero. Nel **codice** no.

| array | dove esce | cura |
|---|---|---|
| `_furniture` | prefisso (`item_func.hsp:1324`) | toppa: in coda su `locvar_itemname_s6` |
| `_bookself` | già fra parentesi (`:988`) | **nessuna toppa**, solo dato |
| `_weight` | già suffisso, giunto « grown » (`:974`) | toppa **sul giunto** |
| `_bookselfs` | slot parola-contatore (`:1233`) | trattamento `contatori.jsonl` |

**La regola che ne resta: prima di scrivere la toppa si guarda il sito di
concatenazione.** La somiglianza nel dizionario non dice niente su dove il
codice mette la stringa, e la cura la decide il codice.

Il caso più istruttivo è `_weight`. Era già un suffisso, quindi «spostarlo» non
voleva dire nulla; ma un aggettivo italiano in coda si sarebbe accordato lo
stesso col nome, di genere ignoto. **La leva non era la posizione ma il
giunto**: « grown » → « di taglia » introduce una testa femminile e fissa, e da
lì in poi l'accordo è con «taglia». È un modo nuovo di risolvere il genere
ignoto, il terzo dopo il complemento e il sostantivo al posto dell'aggettivo.

E `_bookself` è il primo caso della famiglia in cui **il sorgente andava bene
com'era**: esce fra parentesi, dove la parola sta da sola e non si accorda con
niente. Valeva la pena guardare prima di toccare.

### Un legame per stringa, che nessun controllo esistente vedeva

`_bookselfs` finisce in `locvar_itemname_s2`, e i due `switch` generati
confrontano la resa di `contatori.jsonl` con quella che l'array porta a
runtime, che viene dal dizionario. **Se divergono, il `case` non aggancia mai —
e restano verdi sia il compilatore sia la prova d'identità.**

Non è un difetto della prova d'identità: lei giudica la pipeline delle
sostituzioni, e le toppe girano dopo, in un giro loro. È una classe di errore
che nessuno dei due guardiani copre. Ora lo pretendono `genera_toppe_nomi.py`
alla generazione e un test a ogni giro.

### Il criterio della classe, e dove finisce

I lotti dal terzo al sesto sono stati scelti per `filter_item(ITEM_ID_X)`, che
sta in un blocco lontano dai nomi. Ha funzionato ogni volta, per un motivo che
conviene scrivere: **una classe raccoglie oggetti che pongono la stessa
domanda**, e una domanda posta una volta si risponde una volta.

Ha smesso di funzionare quando le classi sono finite. Le 599 voci rimaste sono
esattamente quelle **senza** filtro: non una classe, un residuo. Dentro ci sono
169 artefatti fra `<>`, per i quali la domanda non è di resa ma di
**invarianza** — e il criterio nuovo sarà la forma del nome.

### Quattro decisioni di resa dell'equipaggiamento

- `gauntlets` → «guanti d'arme» contro `gloves` → «guanti». L'inglese distingue
  protezione e indumento, e l'italiano può seguirlo. **Eccezione dichiarata**:
  `decorated gloves` è «guanti d'arme decorati» benché l'inglese dica *gloves*,
  perché il sorgente lo tratta come guanto d'arme (`item_func.hsp:1849-1850`);
- `mail` → «corazza», non «cotta» — tranne `chain mail` → «cotta di maglia»,
  dove la cotta è davvero la cosa;
- `lance`/`spear`: l'inglese ha due parole, l'italiano una. La distinzione si
  tiene col **complemento** («lancia da cavaliere» contro «lancia»), non
  inventando un secondo sostantivo. È la stessa cura del giunto dei composti;
- `claymore` → «spadone», `bardish` → «ascia lunga»: il giapponese dice 大剣 e
  大斧, e i nomi scozzese e slavo in italiano non aggiungono nulla.

### La storia naturale: nome vero se esiste, invariante se inventato

`hotate` → «capasanta», `cutlassfish` → «pesce sciabola», `spotted garden eel`
→ «anguilla giardiniera». E quando due pesci rischiano lo stesso nome si
separano apposta: `manboo` → «pesce luna» (mola mola), `moonfish` → «pesce re»
(Lampris), che è il nome italiano vero del secondo.

Restano invariati e dichiarati i nomi inventati da Elona — `mesugaki`, `sazae`,
`fane`, `dernefia` e le quattro erbe del canone.

### Una deroga dichiarata: i diari delle sorelle

`dog sister's diary` e `cat sister's diary` traducono 姉の秘密の日記 e
妹の秘密の日記, cioè «il diario **segreto** della sorella maggiore/minore».
Tradurre dall'inglese avrebbe dato «diario della sorella cane», che non vuol
dire nulla in nessuna lingua.

**Qui si è derogato alla regola «si traduce dall'inglese», perché l'inglese è
una svista e non una scelta.** Le rese sono «diario segreto della sorella
maggiore/minore», e restano distinte dalle due non segrete, che nel gioco sono
oggetti diversi. La deroga è dichiarata perché la prossima volta il criterio
sia già scritto: si deroga quando l'inglese perde informazione che il giapponese
ha, e la resa letterale produrrebbe una frase priva di senso.

### Il verificatore che rifiuta il lotto intero è un pregio

Ha bloccato l'equipaggiamento finché i sette prestiti giapponesi — `katana`,
`wakizashi`, `kunai`, `shuriken`, `nunchaku`, `shakujo`, `tomahawk` — non erano
in `invariati.md`. È la regola «si dichiara, non si evita» che morde invece di
lasciar passare, ed è costato cinque minuti contro un elenco di invarianti che
sarebbe rimasto incompleto per sempre.

### Un caso in cui i due campi del dizionario dicono cose diverse

`unicorn horn` ha genere `m` e plurale «corna di unicorno». In italiano «corno»
fa «corna» quando sono di un animale: il genere del singolare e la forma del
plurale non si deducono l'uno dall'altra, ed è esattamente il motivo per cui
sono due campi.

## La decima sessione — 2026-08-09

### Il residuo non esisteva: la categoria che il sorgente dichiara

I lotti dal terzo al sesto erano stati scelti per `filter_item`, e quando quel
criterio si è esaurito ciò che restava di `db_item.hsp` si chiamava «il gruppo
senza filtro»: un residuo da affrontare a occhio.

Non era un residuo. La categoria c'è, solo che non sta in `filter_item` ma
**dentro il blocco di ogni oggetto**:

```
if ( dbid == ITEM_ID_HAMBURGER ) {
    ...
    reftype = FILTER_ITEM_FOOD
```

Sono **1.320 oggetti classificati dal sorgente**. Letto con quella chiave, il
residuo torna a essere fatto di classi — `FILTER_ITEM_TOOL`, `FILTER_FURNITURE`,
`FILTER_JUNK`, `FILTER_ITEM_FOOD`, `FILTER_CONTAINER` — e i cinque lotti che
hanno chiuso il file sono usciti tutti da lì.

**La regola: prima di dichiarare che una cosa non ha struttura, si cerca dove il
codice la struttura.** Il criterio è diventato `strumenti/categorie.py`, con
cinque test, perché uno script usa e getta avrebbe costretto la prossima
sessione a riscoprirlo. Il quinto test è la rete: **ogni nome ancora da tradurre
ha una categoria**, così se domani ne arrivasse uno senza, il criterio non
tornerebbe a essere un occhio senza che nessuno lo dica.

### La marca 《》: l'invarianza degli artefatti si legge nei dati

I 169 artefatti fra `<>` ponevano una domanda di invarianza, non di resa. La
regola che ne è uscita ha tre gradini in ordine di precedenza:

1. l'inglese è già una **romanizzazione, una coniazione o una sigla** →
   invariato. Si traduce dall'inglese, e se l'inglese non dice niente non c'è
   niente da rendere;
2. il giapponese sta fra 《》 **ed è traslitterato in katakana** → invariato:
   quando l'originale traslittera, non legge il nome come descrizione;
3. il giapponese è **descrittivo in kanji**, o non porta la marca 《》 →
   tradotto, tenendo le `<>`.

Il pezzo nuovo è la **marca 《》**, e viene dai dati: 157 nomi su 169 ce l'hanno,
dodici no — e quei dodici sono esattamente quelli che si leggono come oggetti
ordinari a cui l'inglese ha messo le `<>` per decorazione (`<Dog Whistle>` 犬笛,
`<Amulet of Jure>` 健康のお守り).

**La prova che la regola non è stata cucita addosso al lotto: riproduce tutti e
otto i precedenti già presi**, compresi i due che tirano in direzioni opposte —
`<Zantetsuken>` 《斬鉄剣》 invariato benché kanji, perché l'inglese è
romanizzazione, e `<Scythe of the Void>` 《虚無の大鎌》 tradotto benché porti la
marca, perché il kanji descrive.

Esito: 105 invariati e 63 tradotti.

### Quando l'inglese sceglie una lingua, la scelta è informazione

Tre casi diversi della stessa idea, trovati in tre lotti diversi:

- **`hamaki`** (葉巻). Il giapponese usa la **parola comune** per «sigaro», ma
  l'inglese ha scelto di romanizzarla. È il caso di `wakizashi` rifatto: si
  traduce dall'inglese, quindi resta. E poiché `cigarette` (紙巻タバコ) nello
  stesso lotto diventa «sigaretta», la distinzione che l'inglese fa fra i due
  resta visibile anche in italiano.
- **`Taktstock`** (コマンドタクト). L'inglese ha scelto il **tedesco**, e il
  tedesco resta tedesco come il latino resta latino in `aqua sanctio`. Renderlo
  «bacchetta» perderebbe la scelta di lingua che l'originale ha fatto.
- **`anering`** (アネワッシャー). Invariato per una ragione che si vede solo
  guardando le due lingue **insieme**: coniano cose diverse — il giapponese dice
  «rondella», l'inglese «anello». Quando le due lingue non descrivono la stessa
  cosa, non stanno descrivendo: stanno nominando.

### Il registro e il segmento: due livelli, non due verità

Chiudendo `db_item.hsp` una voce non tornava: `contatori.jsonl` registra
`grave` → «tomba», il dizionario rende lo stesso `grave` con «tomba ornata».

Sembrava una divergenza da sanare, e a dire di no è stato il **sito di
concatenazione**, come sempre. Il nome si monta `s2 + " " + s3 + " " + s1`, e la
toppa 3 fissa il giunto a «di». Per `ITEM_ID_GRAVE_ORNAMENTED_WITH_FLOWERS` le
due parti sono «tomba ornata» e «fiori»: a schermo esce **«tomba ornata di
fiori»**, e al plurale «3 tombe ornate di fiori».

L'aggettivo sta in `s2` perché **è lì che può accordarsi con la testa**. Con
«tomba» in `s2` uscirebbe «tomba di ornata di fiori»; con «tomba» più «fiori» si
perderebbe l'«ornamented». Il giunto è fisso: l'unico posto dove l'accordo può
vivere è la testa.

**Quindi il registro dice il termine e il dizionario dice il segmento.** Sono
due livelli, non due verità in conflitto — e allineare i due file avrebbe rotto
una resa giusta per far tornare un confronto sbagliato.

Il test nuovo vive al livello che li tiene insieme: la resa del dizionario
**comincia con** il termine del registro. Prende i 38 casi identici, accetta la
variante contestuale senza costringere a dichiarare un'eccezione falsa, e se un
domani una variante non fosse un prefisso lo dice — perché allora sarebbe una
testa diversa, e le teste diverse si dichiarano.

### Il primo rinvio deciso da `db_item.hsp`, e una procura che si è rotta

`<Pants of Ogre>` è rinviato alla Fase 2: il nome contiene `ogre`, e in
`db_creature.hsp` `orc` e `ogre` convivono come creature distinte (`orc
warrior`, `black orc` contro `slash ogre`, `shine ogre`). «Orco» non può
coprirle entrambe, e quale delle due se lo prenda è una decisione dei nomi di
creatura.

Il test `test_i_nomi_di_db_item_non_sono_rinviati_da_text` è caduto, e non
perché la proprietà che difende fosse violata. Diceva `== set()`: una
**procura**, vera solo finché `db_item.hsp` non aveva rinvii suoi. La proprietà
— nessuna rinviata di `text.hsp` toglie lavoro alla coda di `db_item.hsp` — è
rimasta vera per tutto il tempo. Adesso è scritta com'è: ogni firma che esce per
`db_item.hsp` viene da una riga **di** `db_item.hsp`.

**La lezione: un test che passa per procura passa finché il mondo somiglia a
quando l'hai scritto.** Quando cade, la prima domanda è se sia caduta la
proprietà o la procura.

## L'undicesima sessione — 2026-08-09

### `item_data.hsp` è chiuso, e la classe era di nuovo nel sorgente

Le 235 voci rimaste non erano un residuo. La chiave qui non è `reftype` come
in `db_item.hsp` ma **l'array che dichiara la voce**, e con quella si sciolgono
in cinque discipline: `fishdatan` 113, `encDisp` 62, le dinamiche di
`*item_encdetail` 21, i due ego 29, `ammoname` 6. Tre lotti, nessun rinvio,
318 su 318.

### Il posto decide se i dati arrivano in tempo

`ioriginalnameref(ITEM_ID_FISH)` è la **stringa vuota**: il nome della specie
non è un pezzo del nome dell'oggetto, è tutto il nome, e arriva da
`itemNameSub` (`item_func.hsp:997`), che gira a riga 1936 — cioè **dopo** che
l'articolo è stato messo davanti e dopo che il plurale è stato scelto.

Tradurre i 113 nomi e basta avrebbe dato «a salmone». E **nessun test lo
avrebbe visto**: `verifica` non chiede plurale e genere a una voce che non
dichiara un array, e i pesci non lo dichiaravano.

> Prima di tradurre un nome si guarda **dove** il gioco lo mette. Il posto
> decide se i dati che porta arrivano in tempo.

I pesci usano ora la stessa macchina di `db_item` invece di una nuova:
`ARRAY_IN_LANG` in `estrai.py` riconosce la forma su una riga sola dentro
`lang()`, `ARTICOLO_DI` in `applica.py` fa dell'array dell'articolo una
proprietà della **famiglia** e non della riga, e `siti()` non riemette il nome
che il ciclo di `lang()` ha già visto — erano 113 sostituzioni doppie.

### Prima di scegliere la forma di una frase si contano i posti da cui esce

La descrizione d'incantamento (`s` di `*item_encdetail`) esce da **quattro
siti** e solo uno le mette un soggetto davanti — `command.hsp:16405` scrive
`lang("それは", "It ") + s`; gli altri tre la usano nuda. Un soggetto italiano
cablato lì andrebbe bene in un sito e male negli altri tre.

Le rese sono quindi **verbi alla terza persona senza soggetto**, e il prefisso
si spegne con una toppa a mano — `command.hsp` non è fra i file estratti.

### La stessa cura, tre cose ignote diverse

«Non accordarsi con ciò che non si conosce» ha scelto la forma tre volte in
questa sessione, e ogni volta l'ignoto era un altro:

| dove | cosa non si conosce |
|---|---|
| ego, `egominorn` | il genere dell'**oggetto** |
| `"deals X damage."` | il genere dell'**abilità**, che è pure ancora inglese |
| `skillencdesc` | il genere del **giocatore** — «ti rende letterato/letterata» |

### La `h` muta non rende pura la `s` impura

`articolo.py` teneva la `h` fra le vocali, perché a inizio di parola è muta e
chiede l'elisione («l'hotel»). Ma `_s_impura` interrogava lo stesso insieme
per una domanda **diversa** — «la lettera dopo la `s` è una consonante?» — e
per `sh` le due danno risposte opposte: usciva «un shuriken».

> Due domande che si somigliano non sono la stessa domanda. Il posto dove si
> separano è un caso solo, e lo trova il collaudo, non i test.

### Il giunto del materiale non è uno solo: sette elidono

« di » era cablato nella toppa, e lì deve restare — `command.hsp` legge
`mtname` nudo, e «fatto di» + «di cuoio» direbbe due volte la preposizione. Ma
una preposizione sola non copre 38 materiali: sette cominciano per vocale.
Terza via, quella già usata per plurale e articolo: `mtcomplemento`, un array
italiano accanto a quello inglese col complemento già montato.

### `skill.hsp`: solo le prime tre lettere arrivano a schermo

`chara.hsp:4679` fa `strmid(skillname(r), 0, 4 - (jp == 0))`: nella schermata
di razza e classe gli attributi sono **tagliati a 3 caratteri**.

Le scelte del glossario sopravvivono tutte — Vit, Man, For, Cos, Des, Per,
App, Vol, Mag, Car, Vel, undici distinte, e coincidono con le sigle già
fissate in `text.hsp:61`. La collisione che ci sarebbe (`Forza` e `Fortuna`
tagliano entrambe a «For») **non arriva a schermo**: il campo mostra
STR…SPD più Vita e Mana, e `Luck` non ci passa. Lo dice il sorgente stesso:
`MAX_SKILL_ATTR_BASIC 8 // this basically excludes luck and speed`.

⚠️ Vale per gli attributi, non per le 445 voci di `skillname`: il resto del
file va in altri campi, che vanno guardati prima di tradurlo.

### La misura dei campi di `skillname` — 2026-08-09

Fatta **prima** di tradurre, come per i pesci. Quattro campi, misurati sul
sorgente e non a occhio:

| campo | dove | larghezza | chi ci passa |
|---|---|---|---|
| tracciatore abilità (HUD) | `screen.hsp:2002` e `:2029` | **6 caratteri** | i 77 nomi tracciabili |
| razza e classe | `chara.hsp:4679`, `:4682`, `:4686` | **3 caratteri** | gli 11 attributi |
| lista abilità, nome | `command.hsp:5383` | ~**29 caratteri** | tutti i 445 |
| lista abilità, descrizione | `command.hsp:5389` | **34 caratteri** | i 415 `skilldesc` |

**Il 6 non è un numero a caso, è una misura.** Il nome sta a `pos 16` e il
valore a `pos 66`: cinquanta pixel, e il sorgente stesso assume 7 px per
carattere (`command.hsp:5385` fa `288 - strlen(s) * 7`). 50/7 = 7,14 — sei
caratteri con un carattere di margine.

Stessa aritmetica per la lista: nome a `wx+84`, costo allineato a destra a
`wx+288`, cioè 204 px ≈ 29 caratteri. L'inglese più lungo ne ha 24
(`Critical Particle Cannon`), quindi il margine c'è ma è sottile.

**I 34 caratteri della descrizione non sono un tetto da rispettare**: 41 delle
415 descrizioni inglesi lo superano già, e il gioco le tronca. È invece la
**finestra**: i primi 34 caratteri devono portare il senso.

#### Il vincolo che morde è il 6, e in inglese quasi non si vede

Fra i 77 nomi tracciabili le collisioni inglesi nei primi sei caratteri sono
**due**: `Magic`/`magic` (attributo e resistenza, distinte solo dal caso) e
`Magic Capacity`/`Magic Device`, che è una collisione vera già oggi.

In italiano il rischio è più alto, e per una ragione strutturale: **l'inglese
mette il qualificatore davanti, l'italiano dietro**, quindi la parte che
distingue esce dalla finestra. Le famiglie a rischio, trovate sul set vero:

| inglese | italiano naturale | primi 6 |
|---|---|---|
| Heavy / Medium / Light Armor | Armatura pesante / media / leggera | `Armatu` ×3 |
| Long / Short Sword | Spada lunga / corta | `Spada ` ×2 |
| Evasion / Greater Evasion | Evasione / Evasione superiore | `Evasio` ×2 |
| Throwing / Casting | Lancio / Lancio incantesimi | `Lancio` ×2 |

Da notare che l'italiano **risolve** l'unica collisione vera dell'inglese:
`Magic Capacity` e `Magic Device` diventano «Capacità magica» e «Dispositivi
magici», cioè `Capaci` e `Dispos`.

⚠️ **Decisione ancora aperta**, e va presa prima del lotto di `skillname`: se
scegliere teste diverse per le famiglie che collidono, abbreviare la testa, o
accettare la collisione nel solo tracciatore (dove il nome intero resta
visibile nella lista).

### I nove gradi di `_resist`: un campo che non tronca, invade — 2026-08-09

Trovato **in gioco**, non dai test: nella lista abilità (`a`, pagina delle
resistenze) «Resistenza debole» finiva sopra `Resist Fulmine`.

Il campo non è come quelli misurati finora. Gli altri **tagliano**, e il taglio
si vede nel campo stesso. Questo è **ancorato a destra**:

```
command.hsp:11002   pos wx + 280 - strlen(s) * 7, ...   ← la colonna dei gradi
command.hsp:10893   x = 54                              ← da dove parte il nome
```

> Un campo allineato a destra non ha un tetto: cresce verso sinistra finché
> non copre il vicino. **Il difetto non compare nel campo lungo, compare in
> quello accanto** — e nessun test che guardi una stringa alla volta lo vede.

Lo spazio fra i due estremi è **226 px**, e va diviso fra il nome e il grado.
Il caso peggiore è la coppia più lunga possibile, non la media: `Resist
Oltretomba` (17 caratteri, il nome più lungo dei nostri) col grado più lungo.
L'inglese nel suo peggiore ne impegna 30, `Resist Lightning` + `Criticaly Weak`.

Sette gradi su nove sforavano, e per la stessa ragione strutturale del campo da
6: **ripetevano una testa che la colonna non deve dire.** «Resistenza debole»
accanto a una riga che si chiama già `Resist Fulmine` dice «resistenza» due
volte. La cura è la stessa già usata per i nomi tracciabili — **togliere la
testa, tenere ciò che distingue**:

| jp | en | prima | ora |
|---|---|---|---|
| 致命的な弱点 | Criticaly Weak | Debolezza critica | **Fatale** |
| 弱点 | Weak | Debolezza | Debolezza |
| 耐性なし | No Resist | Nessuna resistenza | **Nessuna** |
| 弱い耐性 | Little | Resistenza debole | **Scarsa** |
| 普通の耐性 | Normal | Resistenza normale | **Normale** |
| 強い耐性 | Strong | Resistenza forte | **Forte** |
| 素晴らしい耐性 | Superb | Resistenza ottima | **Ottima** |
| 凄まじい耐性 | Amazing | Resistenza enorme | **Enorme** |
| 究極の耐性 | Supreme | Resistenza suprema | **Suprema** |

Il peggiore passa da 17 caratteri a **9**, e i nostri 17 + 9 = 26 stanno sotto
i 30 dell'inglese. Il 9 non è dedotto: la schermata di prima della correzione
mostrava già `Resist Oltretomba` con «Debolezza» **senza toccarsi**.

`Fatale` viene dal giapponese, 致命的 — più fedele di «critica», e in più
inequivocabile: un aggettivo da solo in una colonna di gradi si può leggere al
contrario, e «critica» poteva passare per un pregio.

⚠️ **I due gradi che si somigliano vanno tenuti distinti a vista.**
`Debolezza` (slot 1, si subisce il 133%) e `Scarsa` (slot 3, il 37%) sono
opposti. L'inglese li separa cambiando il sostantivo sottinteso a metà scala —
*Weak* è una debolezza, *Little* è una resistenza — e l'italiano deve fare lo
stesso: nome per la metà cattiva, aggettivo per quella buona.

Il secondo sito che legge `_resist` è `command.hsp:8136`, la scheda di un PNG
conosciuto (`_resist(...) + " " + skilldesc(...)`): testo che scorre, senza
vincolo di larghezza, e il grado corto ci sta come ci stava quello inglese.

⚠️ **Il `#####` accanto ai gradi non è nostro.** È `putenclv`
(`item_data.hsp:145`), disegnato a `wx+282` fisso: un `#` per livello di bonus,
`+` oltre il quinto. Esce identico nel gioco inglese.

### `skilldesc`, tutte e 415 — 2026-08-09

Un solo campo, la finestra da 34 caratteri di `command.hsp:5389`, ma **due
corpora diversi**, e trattarli allo stesso modo sarebbe stato l'errore:

| | quante | forma |
|---|---|---|
| prosa | **67** | `Indicates your skill with axes.` — frasi, termini già in glossario |
| etichette | **348** | `Line(Cold)`, `[100% Gauge] Rapid Slash`, `WIL-Check:Fatigue low-SP enemies` |

Le 348 non si traducono una per una: si traducono **gli atomi**, che stanno ora
in `glossario.md`. Tradurne una alla volta avrebbe prodotto quattordici rese
diverse di `Surround`.

#### Il riempitivo inglese non è contenuto

`Indicates your skill with…` compare **dodici volte** e non dice nulla: la
colonna si chiama già `Detail` e la riga porta già il nome dell'abilità.
Toglierlo fa entrare tutte e dodici nella finestra — `Indicates your skill with
blunt weapons.` (40) → «Abilità con le armi contundenti.» (32).

Il bilancio sulla finestra, che è la misura vera del lotto: **41 delle 415
inglesi la sforano**, delle nostre **cinque**, e quattro di quelle cinque sono
più corte del loro inglese.

#### Il giapponese scioglie le sigle che l'inglese lascia opache

`Con-Attack`, `END`, `PVDV`, `CHR` non sono spiegate da nessuna parte
nell'inglese. Il giapponese le dice tutte — 耐久属性攻撃, 耐久, 魅力 — e ha
mostrato **due sigle che sono la stessa cosa scritta due volte**:

| | inglese | giapponese | italiano |
|---|---|---|---|
| Costituzione | `CON` **e** `END` | 耐久 in entrambi | **Cos** |
| Carisma | `CHA` **e** `CHR` | 魅力 in entrambi | **Car** |

> Una sigla che l'inglese non scioglie va cercata nell'originale, non indovinata
> dal contesto. Due volte su quattro l'originale ha detto che le sigle erano una.

E ha corretto una scelta già fatta: `Surround(X)` è 範囲**攻撃**, «attacco ad
area». Avevo proposto `Attorno(X)` per tenere `Area` libera; con `AOE` che resta
sigla, `Area(X)` è insieme più fedele e più corto.

#### Chiavare sull'inglese avrebbe fuso sette voci distinte

Sette stringhe inglesi si ripetono con un **giapponese diverso**:

```
Create mist   →  濃い霧の発生    nebbia fitta
Create mist   →  眩い霧の発生    nebbia abbagliante
Teleport self →  瞬間移動        teletrasporto
Teleport self →  近くへの瞬間移動 teletrasporto vicino
```

Il lotto è quindi chiavato sull'**indice**, con l'inglese atteso accanto e
verificato a ogni voce. Una mappa `inglese → italiano` avrebbe silenziosamente
tradotto due cose diverse allo stesso modo — e nessuna guardia lo vedeva,
perché ogni firma sarebbe stata comunque tradotta.

#### Tre voci inglesi sono `?`

`skilldesc` 218, 263 e 355 dicono letteralmente `?`: buchi che l'autore inglese
non ha mai riempito. Il giapponese c'è ed è pieno (治癒力超上昇, 能力の変動・
暴れ回る, 煙幕＆能力転写). Sono rese **dal giapponese**: un `?` non è una
stringa da tradurre, è una che manca, e noi la fonte ce l'abbiamo.

#### L'accento a metà parola degrada male

Avevo scritto «dèi», che è la grafia giusta. `applica.py` degrada gli accenti in
apostrofo e ne esce **`de'i`**, con l'apostrofo dentro la parola. Tutti gli
accenti incontrati finora stavano a fine parola — «Abilità» → `Abilita'`, «più»
→ `piu'` — e lì la degradazione è invisibile.

> Prima di scrivere un accento, guardare **dove** cade nella parola. In fondo è
> gratis, in mezzo no.

### `custom_tweaks.hsp` riscrive `skill.hsp`, e vince — 2026-08-09

Trovato guardando una schermata del collaudo: il menù delle mosse speciali
mostrava `Enable/Disable **the** use of power gauge`, mentre la voce appena
tradotta dice `Enable/Disable use of power gauge`. **Due stringhe diverse.**

```
skill.hsp:1529          skilldesc(SKILL_SPACT_GAUGE_RELEASE) = lang(…, "Enable/Disable use of power gauge")
custom_tweaks.hsp:1261  skilldesc(SKILL_SPACT_GAUGE_RELEASE) = lang(…, "Enable/Disable the use of power gauge")
```

`custom_tweaks.hsp` applica le opzioni di configurazione **riassegnando** le
stesse chiavi dopo `skill.hsp`. A schermo arriva l'ultima scrittura.

> Una traduzione può essere giusta, verificata, byte per byte, dentro la build —
> e non vedersi mai, perché un altro file scrive dopo. La firma garantisce
> **dove** hai scritto, non **cosa** legge il gioco.

Le chiavi riscritte sono **sei**: `SKILL_SPACT_GAUGE_RELEASE` e quattro
resistenze (`LIGHTNING`, `MIND`, `NERVE`, `CHAOS`). Le quattro resistenze erano
proprio fra quelle appena tradotte, e si vedevano nella schermata del collaudo:
la colonna sarebbe uscita **mezza italiana**.

I siti sono **dodici**, non sei, perché ogni tweak ha due rami — `if (Tweak…)`
ed `else` — e quale gira lo decide il giocatore nelle opzioni. **Vanno tradotti
entrambi.**

**Non abbiamo usato le toppe.** Il file ha 28 `lang()` in tutto, e 16 sono
`font lang(cfg_font1, cfg_font2)`, cioè scelta del carattere e non testo:
restano **12 stringhe vere**. Dodici toppe le metterebbero fuori dalla
garanzia byte per byte (`contratto-nomi.md` §2); `custom_tweaks.hsp` come
settimo file di dizionario ce le tiene dentro, e **non è costato una riga di
codice** — `estrai` prende qualunque `.hsp`, e il resto della catena scorre i
dizionari, non una lista fissa.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`. Oggi è solo `custom_tweaks.hsp`, ma è un file
di *tweak*: cresce a ogni rilascio.

Nessun buco nella prova d'identità, e per una ragione di disegno:
`prova_identita.py:84` fa `radice.glob("*.hsp")` e attraversa **tutti e 72 i
file**, non quelli che traduciamo. Le 12 stringhe erano già dentro i 27.813.

### La misura dei campi di `skillname`, seconda parte — 2026-08-09

Fatta prima di tradurre i 368 nomi che restano. ⚠️ **Corregge il «~29
caratteri» scritto ieri**, che era una lettura sbagliata dello stesso codice:

```
command.hsp:5382   cs_list skillname(…) + s, wx + 84      ← il nome parte da 84
command.hsp:5385   pos wx + 288 - strlen(s) * 7           ← il costo, ancorato a destra
command.hsp:5389   mes strmid(s, 0, 34)                   ← la descrizione, tagliata
```

A 288 ci arriva **il costo**, non il nome. `"12 Sp"` sono 5 caratteri, 35 px, e
al nome restano 169 px ≈ **24 caratteri**. Il nome porta inoltre appiccicato il
segnaposto della scorciatoia (`{0}`…`{10}`), fino a 4 caratteri.

L'inglese conferma il 24 dal lato suo, come vuole la regola della guida:

| famiglia | nomi | max inglese | mediana |
|---|---|---|---|
| incantesimi | 90 | 20 (`4-Dimensional Pocket`) | 11 |
| mosse speciali | 276 | **24** (`Critical Particle Cannon`) | 12 |

**Il tetto è 24.** Cinque nomi inglesi superano i 20, e con una scorciatoia
assegnata sforano già oggi: la sovrapposizione col costo è un difetto che il
gioco inglese ha per conto suo, non un margine da spendere.

### I nomi delle mosse speciali, e perché la traslitterazione qui non basta — 2026-08-09

Per gli artefatti di `db_item.hsp` vale la regola della marca 《》: se il
giapponese **traslittera** invece di descrivere, nemmeno lui legge il nome come
descrizione, e il nome resta inglese. Applicata alle 276 mosse quella regola ne
lascerebbe inglesi una quarantina — `シャドウステップ`, `ブースト`, `グレネード`.

Non si applica, e la ragione è che **le due cose non sono lo stesso genere di
nome**. Il nome di un artefatto è un nome proprio: si legge una volta, dà colore,
e nessuna decisione dipende dal capirlo. Il nome di una mossa è un'**etichetta
funzionale**: sta in un elenco da cui il giocatore sceglie mentre combatte, ed è
la stessa classe delle voci di menù, che nessuno si sognerebbe di lasciare in
inglese perché il giapponese le scrive in katakana.

Quindi per le mosse vale il criterio dei nomi propri e basta: **fatto di parole
comuni → si traduce**, qualunque alfabeto abbia usato il giapponese; **opaco →
resta**. Restano quindici nomi, dichiarati in `invariati.md`.

Due rese sono cambiate proprio per questo criterio, dopo la prima stesura:

- `Dupli-Cane` → «Duplibacchetta». Lasciato com'era, un lettore italiano ci
  legge **«doppio cane»**: una coniazione opaca in inglese può essere
  trasparente e sbagliata in italiano;
- `Shine Snail` → «Lumaca lucente», che è katakana ma di parole comunissime.

⚠️ **`Ensemble` e `Knockout` restano, e non è una deroga**: sono prestiti che
l'italiano ha davvero, come `bonus`. `Tuin der Lusten` resta perché l'inglese ha
scelto l'**olandese** — è il trittico di Bosch — come `Taktstock` aveva scelto il
tedesco: la lingua scelta è informazione.

### Un rinvio motivato da una dipendenza che non esiste — 2026-08-09

Le sei parti meccaniche di `text.hsp` (`Change Spinning Foot` e compagne) erano
rinviate alla Fase 2 con questa motivazione:

> Nome di parte meccanica. **Verificato** che compare anche in `db_item.hsp`,
> quindi è un nome d'oggetto: stessa dipendenza di Fase 2.

In `db_item.hsp` non ce n'è nessuna, né in inglese né in katakana. Le sei
vivono in `text.hsp`, `action.hsp` e `proc.hsp` — e le ultime due sono file non
ancora tradotti, il che impone **coerenza**, non una dipendenza di fase.

> La parola «verificato» dentro una motivazione non è una verifica: è il
> ricordo di una verifica, e invecchia come tutto il resto.

Le quattro risposte del quiz sui grimori erano rinviate a `skill.hsp`, che oggi
è chiuso: il rinvio era giusto ed è scaduto da sé. ⚠️ Le rese **non** sono i
nomi d'incantesimo di `skill.hsp` («Terreno acido») ma i nomi di **grimorio** di
`db_item.hsp` («suolo acido»): la domanda è «quale grimorio non esiste?», e la
risposta deve combaciare con ciò che il giocatore legge sullo scaffale.

Le sei parti si traducono nella cornice e non nel nome — «Passa a Spinning
Foot» — perché sono modelli di ricambio di un automa, gridati come nome proprio
al momento del cambio (`action.hsp:12969`, `proc.hsp:17424`), e perché `server`
e `computer` sono già invariati per conto loro.

**Cosa resta rinviato: 110 voci**, e i tre motivi sono vivi — 59 risposte di
quiz che aspettano i nomi di creatura, 30 del sistema dei nomi casuali, 20
`elename()` che aspettano `proc.hsp`, più `<Pants of Ogre>`.

### I nomi casuali degli oggetti non identificati — 2026-08-09

Il gruppo più grosso delle rinviate (30 voci). `db_item.hsp` compone il nome che
il giocatore legge **prima** di identificare un oggetto:

```hsp
iknownnameref(ITEM_ID_POTION_GEM) = _namepotion(p) + strblank + strpotion
```

aggettivo, spazio, nome — «a clear potion». In italiano l'aggettivo segue il
nome, e l'ordine sta **nel codice, non nelle stringhe**: il dizionario non lo
raggiunge. I siti sono **213**, tutti della stessa forma e ognuno con il proprio
`ITEM_ID`, quindi ognuno è un aggancio unico: si generano, con
`strumenti/genera_toppe_casuali.py`.

**Il genere è una proprietà dell'array, non della riga** — `_namepotion` serve
solo pozioni, `_namespellbook` solo grimori — quindi le rese si accordano una
volta per famiglia. È la stessa scoperta di `ARTICOLO_DI` per i pesci, e vale
anche dove l'array ne serve due: `_namering` copre `strring` e `stramulet`, che
in italiano sono entrambi maschili.

⚠️ **L'articolo non era un terzo problema, e non è un caso.** La testa del nome
vero è la **stessa parola di famiglia** — `ioriginalnameref2` vale `potion`,
`spellbook`, `scroll` — quindi `ioriginalnamearticolo` porta già l'articolo
giusto anche per il nome casuale. Il rinvio nominava ordine e genere, e su
questo aveva ragione a non spaventarsi.

**Trenta slot, ventiquattro firme.** Sei coppie condividono giapponese e
inglese fra due famiglie, e siccome il dizionario è indicizzato per contenuto
non può dare due rese. Quattro non fanno danno — 鉄の, サファイアの, 金の, 木の
sono **materiali**, e in italiano diventano complementi invariabili («di ferro»,
«d'oro»). Due erano un vero scontro di genere: 苔むした e 古びた stanno in
`_namespellbook` (grimorio, m) e in `_namescroll` (pergamena, f).

> Una firma condivisa fra due generi **impone la forma invariabile**: non è una
> resa peggiore per pigrizia, è l'unica che non mente in uno dei due posti.

Da qui «col muschio» e «d'altri tempi», che stanno bene a tutti e due.

⚠️ **Il primo tentativo era una toppa, e un test l'ha respinta — con ragione.**
La toppa accordava al femminile la riga di `_namescroll`, e per farlo cercava il
testo **già tradotto**. `test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato`
pretende che ogni toppa si agganci al sorgente pinnato, ed è quella pretesa a
renderla una guardia: se upstream riscrive la riga, la build diventa rossa
prima di produrre qualcosa di sbagliato.

> Una toppa agganciata alla nostra uscita invece che al sorgente **combacia per
> sempre**, qualunque cosa faccia upstream. Continua a funzionare e smette di
> proteggere.

Concetto: `wiki/concepts/una-guardia-agganciata-a-se-stessa.md`.

### L'articolo dei nomi di creatura sta dentro il nome — 2026-08-09

E con lui cade la concordanza di genere fra `evold` e `evname`, che avevo
appena messo come guardia. Vale la pena scrivere il giro per intero, perché la
proprietà sbagliata sembrava più prudente di quella giusta.

`name()` (`init.hsp:1718`) anteponeva `"the "` **al momento di mostrare**, e una
toppa di due sessioni fa l'ha tolto, con la nota: «in italiano l'articolo
dipende da genere ed elisione, quindi lo porta il nome della creatura». Restava
da capire *come*.

Per gli oggetti la risposta era stata un **array parallelo**
(`ioriginalnamearticolo`), indicizzato per id. Per le creature non funziona, e
la ragione è tutta nell'evoluzione:

> L'id della creatura **non cambia** quando evolve. Il nome sì. Un articolo
> indicizzato per id darebbe per sempre l'articolo di prima della
> trasformazione.

Quindi l'articolo sta **dentro** il nome. Il prezzo si misura: `cdatan(CDATAN_NAME)`
finisce grezzo dentro **1.815 siti di prosa**, e sono quasi tutti in posizione di
soggetto — «`X` ti ha guardato in faccia» — dove «la giraffa ti ha guardato in
faccia» è giusto. I pochi con preposizione («il cambiamento **di** `X`») sono
stringhe **dinamiche**, cioè le traduciamo noi: si riformulano, e il problema
sparisce dal lato del testo invece che dal lato del codice.

⚠️ **La conseguenza è che anche `evold` e `evname` devono portare l'articolo**,
e il taglio lo sostituisce insieme alla specie. Da qui il ribaltamento della
guardia:

| guardia | esito |
|---|---|
| ~~le due metà di ogni coppia concordano nel genere~~ | **cade**: con l'articolo dentro, `giraffe` → `Kirin` va da «la giraffa» a «il kirin» senza lasciare «la kirin» |
| ogni nome e ogni stringa d'evoluzione **porta il proprio articolo** | **la sostituisce**, e vede il difetto vero: se una sola delle due metà lo dimentica, esce un nome senza articolo o con due |

> La concordanza di genere era una guardia che difendeva un difetto che il
> disegno giusto **non può avere**, e ne lasciava passare uno che può avere.

I nomi propri fra `<>` e fra virgolette restano fuori: `name()` li riconosce
dalla prima lettera e non ci ha mai messo l'articolo davanti.

### `orc` è «orco», `ogre` resta «ogre» — 2026-08-09

Forzata dal primo lotto della Fase 2, che contiene `orc`, `king orc` e
`orc warrior`. È la coppia che teneva in ostaggio `<Pants of Ogre>` dal
2026-08-09 mattina.

L'italiano del fantasy ha un solo termine popolare, «orco», e due creature da
coprire. La convenzione consolidata — quella dei manuali di D&D in italiano e
delle traduzioni tolkieniane — assegna **«orco» a `orc`** e lascia **`ogre`
invariato**, che è anche il trattamento che il progetto riserva ai prestiti
acquisiti. Sono due creature distinte in `db_creature.hsp` (`orc warrior`,
`black orc` contro `slash ogre`, `shine ogre`) e così restano distinte anche in
italiano.

Sblocca `<Pants of Ogre>`, l'unica firma rinviata di `db_item.hsp`.

## La quattordicesima sessione — 2026-08-09

### Il giapponese arbitra, perché in due punti l'inglese non identifica un nome

Il primo lotto della Fase 2 ha messo in luce che la colonna inglese di upstream
non è una chiave. Sbaglia in due direzioni opposte, e tutte e due rompono la
rinomina dell'evoluzione, che confronta **stringhe**:

- **un giapponese scritto in due modi in inglese.** `フレアチック` è
  `Flare Chick` in `action.hsp:18191` e `Flare chick` in `18202`; lo stesso per
  `イノブタ`, `ヤドナシ`, `デュラハン`. Il confronto distingue le maiuscole,
  quindi quelle **quattro evoluzioni di secondo stadio in inglese non scattano
  mai**, mentre in giapponese funzionano;
- **due giapponesi ridotti a un inglese solo.** `サラブレッド` — *purosangue* —
  è `wild horse` in `action.hsp:16684`, ma `db_creature.hsp` lo chiama
  `thoroughbred`: quell'`evold` non aggancia nessuno. Idem `野うさぎ`, che è
  `rabbit` in `action.hsp` e `wild rabbit` in `db_creature.hsp`. E i due
  segnaposto `aaaaaaa` ed `EV`, che in giapponese sono `トゥーンコボルト` e
  `コボルト`.

**La decisione: dove le due colonne divergono, si traduce il giapponese.** Non
è correggere upstream per gusto — è l'unico modo di non scrivere un nome falso
in dizionario. Rendere `サラブレッド` con «cavallo selvatico» sarebbe sbagliato
in italiano a prescindere dal codice, e scrivere lo stesso nome con due
maiuscole diverse per riprodurre un refuso sarebbe inventare un difetto in una
lingua che non ce l'ha. Che quattro catene tornino a funzionare è la
conseguenza, non lo scopo.

> Un difetto di upstream non si corregge; ma una colonna che sbaglia il nome
> non è un difetto da conservare, è una fonte da non usare.

**Conseguenza sulle guardie: la chiave è la firma, non l'inglese.**
`test_evold_resta_agganciato` costruiva `{v["en"]: v["it"]}` e su `wild horse`
di due rese ne teneva una sola, in silenzio — la guardia sarebbe passata
guardando il nome sbagliato. Ora tutto il campo della rinomina si legge in
coppie (giapponese, inglese): `evoluzioni_con_jp`, `nomi_per_creatura_con_jp`,
`nomi_visibili_con_jp`.

### L'articolo lo prende tutto ciò che non comincia per `<` o `"`

Verificato in `init.hsp:1712-1719`, e non era ovvio: si poteva credere che
`name()` riconoscesse i nomi propri **dalla maiuscola**, e allora metà del
nucleo — `Unicorn`, `Silver Fang`, `Nekomata` — sarebbe rimasta senza articolo.
Non è così. Il codice guarda solo il primo carattere (`"` o `<`) e il bit
`CHARA_BIT_HAS_NAME`, che sta sul personaggio e non sulla stringa: un nome di
specie, anche capitalizzato, riceveva «the ». Quindi lo riceve anche in
italiano: «l'unicorno», «la zanna d'argento», «la Nekomata».

### Un aggancio dichiarato non conservabile, e perché è l'unico

`bisque doll` è prefisso di `bisque dolls` **solo per la -s del plurale
inglese**, che in italiano non esiste: «la bambola di porcellana» diventa «le
bambole di porcellana», e cambiano articolo e sostantivo insieme.

L'evoluzione vera passa lo stesso, perché lì il confronto è **esatto**.
L'aggancio parziale descriveva solo il **rientro** — una `bisque dolls` che
ripassa dallo stesso ramo — e in inglese quel rientro produce `bisque dollss`,
che è una stortura, non una rinomina. In italiano non fa niente, ed è meglio.

Sta in `AGGANCI_SOLO_INGLESI`, con il motivo accanto. Tutto ciò che non è in
quella lista deve agganciare: la deroga si dichiara una per una, come le
rinviate e le toppe.

### Due strumenti che non erano mai stati eseguiti

`python -m strumenti.creature --classe nome` — il comando che la RIPRESA
documentava per il lotto dei ~750 nomi — passava una `str` dove
`estrai_da_file` vuole un `Path`, e moriva in `AttributeError`. Riparato, e il
nucleo è diventato un comando suo: `--nucleo`.

`<Big Sister>` e `<Little Sister>` erano dichiarati invariati in
`glossario.md` da due sessioni, ma non erano mai stati scritti in
`invariati.md`, che è il file che `verifica.py` legge davvero. Il lotto veniva
rifiutato per «traduzione identica all'inglese». **Una decisione scritta nel
posto sbagliato non è una decisione presa.**

### In italiano il ramo del suffisso è irraggiungibile, e va saputo prima del collaudo

La RIPRESA della tredicesima sessione chiedeva di collaudare in gioco la
riparazione di `action.hsp:18644` — il ramo del **suffisso** della rinomina,
l'unica cosa della Fase 2 già nell'eseguibile. **Con i nomi del nucleo quel
ramo non scatta mai.**

Contati sui 43 agganci parziali più tutti gli esatti: **zero** passano dal
suffisso. Il motivo è strutturale e non un caso. `action.hsp:18640` prova
**prima** il prefisso e cade nell'`else` solo se fallisce; in italiano `evold`
è «articolo + testa di famiglia» e il modificatore va **dopo** — «l'orco» sta
in testa a «l'orco re», «il lich» in testa a «il lich maestro». Dove l'inglese
agganciava in coda (`lesser mummy` finisce per `mummy`), l'italiano aggancia in
testa («la mummia minore» comincia per «la mummia»), e dove il nome coincide
col tutto è di nuovo il prefisso a scattare, perché il confronto è lo stesso.

**Conseguenze pratiche:**

- il collaudo in gioco dell'evoluzione prova il ramo del **prefisso**, non
  quello riparato. Non c'è un'evoluzione da scegliere meglio: non ne esiste
  nessuna che ci passi;
- la riparazione **resta**, ed è giusta lo stesso. Serve al ramo che un
  giocatore può ancora raggiungere rinominando un alleato in modo che la specie
  finisca in coda, e servirebbe subito a un nome futuro che mettesse il
  modificatore davanti;
- il giorno che un nome invertisse l'ordine — «il grande orco» invece di
  «l'orco grande» — il ramo si riaccenderebbe **in silenzio**, con dentro una
  riga che senza la toppa porta la lunghezza del nome di un'altra creatura.

> Una riparazione che nessun collaudo può raggiungere non è una riparazione
> inutile: è una riparazione che non saprai mai se hai rotto.

### «Sorcas the il cane»: il collaudo trova il secondo sito che compone l'articolo

Il primo giro in gioco, con i nomi di creatura appena entrati, ha mostrato
**«Sorcas the il cane»**. Non è la toppa di `init.hsp:1718` che ha ceduto: è un
**secondo** sito, e non è nemmeno una toppa da scrivere.

`db_creature.hsp` compone l'epiteto dei personaggi con nome proprio così, in
**152 punti**:

```hsp
cdatan(CDATAN_NAME, rc) = lang(cdatan(CDATAN_NAME, rc) + "の" + randomname(),
                               randomname() + " the " + cdatan(CDATAN_NAME, rc))
```

È dentro `lang()`, quindi è una **dinamica traducibile** — una firma sola per
tutte e 152 le occorrenze — e stava semplicemente fra le 3.452 di
`db_creature.hsp` non ancora tradotte. Con l'articolo dentro il nome la resa è
`randomname() + " " + cdatan(CDATAN_NAME, rc)`: il `the` sparisce e resta
«Sorcas il cane», che è la forma italiana dell'epiteto («Alessandro il Grande»).

**La lezione è sull'ordine, non sul difetto.** `guida-stile.md` avvertiva di
guardare *dove altro* quei nomi compaiono prima di tradurli, e l'avvertimento
era giusto; ma il posto dove compaiono non si trova leggendo, si trova
**guardando lo schermo**. Cinque minuti di gioco hanno mostrato in una riga ciò
che due sessioni di lettura del sorgente non avevano tirato fuori.

⚠️ **Da rifare quando arrivano gli altri ~930 nomi**: gli stessi 152 siti sono
`cbitmod CHARA_BIT_HAS_NAME`, cioè i personaggi che `name()` mostra **senza**
articolo. L'articolo lì lo porta il nome di specie dentro l'epiteto, ed è
giusto; ma un nome di specie che finisse in quell'epiteto senza articolo
darebbe «Sorcas cane». La guardia dell'articolo lo copre.

### La guardia dell'articolo guardava anche le dinamiche

La stessa voce ha fatto cadere `test_ogni_nome_e_ogni_stringa_di_evoluzione_
porta_il_proprio_articolo`: caricava **tutte** le voci tradotte di
`db_creature.hsp` e pretendeva l'articolo da ciascuna, epiteto compreso.

Chiedere l'articolo a quell'espressione voleva dire chiederle di cominciare per
«il », cioè di scrivere un articolo **fuori** dal nome — l'opposto esatto della
regola che la guardia difende. Il filtro giusto c'era già ed è `classi()`, la
stessa autorità che decide i lotti: la riga è di forma `cdatan(...) = lang(...)`
ma non contiene nessuna coppia di letterali, quindi non è un nome.

### ⚠️ Correzione, mezz'ora dopo: il ramo del suffisso è la strada normale

Poco sopra ho scritto che in italiano il ramo del suffisso di
`action.hsp:18644` **non scatta mai**, e che la riparazione era di fatto
irraggiungibile. **È falso**, e l'ha mostrato il secondo screenshot del
collaudo: «Lazrof il cavallo zoppo».

Il conto di prima guardava il **nome nudo della specie** — «il cavallo zoppo» —
e lì `evold` è davvero in testa. Ma il nome che sta nel salvataggio di un
alleato con nome proprio è l'**epiteto**: `randomname() + " " + <specie>`. Con
un nome proprio davanti, `evold` non può essere in testa: è in coda, sempre.

Simulando il taglio su tutte le coppie con un epiteto davanti: **245 su 245
passano dal suffisso, zero dal prefisso.**

```
'Lazrof il cavallo zoppo' -['il cavallo zoppo']-> "Lazrof l'unicorno"
```

E i personaggi con epiteto sono esattamente i 152 con `CHARA_BIT_HAS_NAME`,
cioè quelli che si tengono in squadra — cioè **quelli che evolvono**. Non è un
caso limite: è il caso normale, e la riparazione di `action.hsp:18644` non è
una precauzione ma la condizione perché l'evoluzione di un alleato con nome
funzioni. Vale anche in inglese, dove `Lazrof the lame horse` finisce per
`lame horse`: il difetto di upstream stava lì da sempre.

**Perché l'errore è stato possibile:** ho contato la proprietà su una forma del
nome — quella di `db_creature.hsp` — invece che sulla forma che il gioco
**memorizza**. È lo stesso scarto delle due guardie nate sbagliate nella
tredicesima sessione, e la correzione è arrivata dallo stesso posto: dal
guardare, non dal contare.

> Il dato non è quello che il sorgente scrive: è quello che il salvataggio
> conserva.

La guardia nuova, `test_il_taglio_rinomina_bene_anche_un_alleato_con_epiteto`,
non controlla l'aggancio: monta il nome come lo monta il gioco, esegue le sette
righe di `18640-18646` con il suffisso riparato e confronta il **risultato**.
245 tagli, e pretende di trovarne più di 200 per non passare a vuoto il giorno
che la simulazione smettesse di agganciare niente.

## La quindicesima sessione — 2026-08-10

Dodici lotti per razza, 351 nomi, tredici commit. Da 928 nomi da tradurre a
**577 in 64 razze**. Non c'è stata una scoperta grossa come il ramo del
suffisso: c'è stato un criterio che ha retto dodici volte di fila, e tre
correzioni al criterio stesso, che sono la parte interessante.

### Il taglio per razza è uno strumento, non uno script

Il nucleo atomico si era preso da sé, per definizione. Tutto il resto si taglia
per **razza**, che il sorgente dichiara in `dbidn` subito prima di
`gosub *db_race`, e non si deduce dal nome.

Il motivo per cui non si deduce merita una riga, perché è più forte del solito:
**il nome è il dato che stiamo per tradurre, quindi non può fare da chiave a sé
stesso.** Con `reftype` (`db_item.hsp`) e con l'array dichiarante
(`item_data.hsp`) l'argomento era di comodità e di verificabilità; qui è di
principio.

`--razze` e `--razza` stanno in `strumenti/creature.py` con sei guardie nuove.
La rete è `firme_senza_razza()`, oggi vuota su 1.131 nomi. Serve perché un
criterio che copre novecento nomi meno uno **non lo dice**: il residuo si
scopre alla fine, quando non c'è più niente da tagliare e i conti non tornano.

Nuovo concept, che raccoglie i tre casi: `wiki/concepts/il-campo-che-il-sorgente-dichiara.md`.

### L'articolo di un nome di persona, e la correzione che l'ha ridimensionato

Il nucleo erano mostri; `norland` sono le persone delle città, e lì l'articolo
dentro il nome smette di essere gratis: in italiano l'articolo di «negoziante»
dipende da chi lo porta, e il sorgente dichiara `cdata(CDATA_SEX, rc)` **solo
per 52 nomi su 90**.

⚠️ `/man/` **non è il sesso**. È la stringa di `DBSPEC_CHARA_FILTER`, accanto a
`/god/`, `/sf/`, `/nefia0/`: la categoria di generazione. Ce l'hanno anche
修道女 e 娼婦, che femmine lo sono per definizione.

Il criterio scritto in `guida-stile.md`: sesso dichiarato → si concorda; sesso
casuale → sostantivo il cui articolo **non dipenda dalla persona**, e ce ne sono
in tre forme (genere fisso «la guardia», articolo elidibile «l'artista»,
prestito invariabile «il ninja»); maschile non marcato solo dove l'italiano non
offre altro — 14 su 90.

**Poi il lotto `imp` ha ridimensionato il problema.** Cinque demoni con sesso
dichiarato, tre femmine e due maschi, ricevono tutti «il demone di X»: concorda
**«demone»**, che è la testa del sintagma, e il sesso del personaggio non entra
mai. `CDATA_SEX` conta solo quando la testa *è* la persona — «`<Neres>` la
smemorata».

Vale la pena averlo scoperto prima di costruire: si stava valutando un campo
femminile nel dizionario con array paralleli fino al gioco, sulla stima
sbagliata di quanti casi lo volessero. Nuovo concept:
`wiki/concepts/la-testa-porta-il-genere.md`.

### Il sorgente arbitra quattro volte su cinque, e la quinta è quella che insegna

Quattro dubbi di traduzione sciolti dal blocco della creatura:
`FILTER_RACE_HOUND_MIND` dice che `illusion hound` è il segugio **mentale**;
`ACTION_RANGE` dice che ガン in ガンデグー è *gun*; tre attacchi in mischia più
succhiasangue dicono che カオス・ブレーダー è uno **spadaccino** e non il
paladino dell'inglese; il ringhiare nel proprio blocco dice che 面忘の獅子 è un
uomo che non è più un uomo.

⚠️ **La quinta volta la stessa prova non ha dato la stessa conclusione.**
幻惑折鶴 lancia davvero `SKILL_SPELL_MIND_THORN`, quindi l'elemento è Mente —
eppure non si rende «mentale». Perché nel caso dei segugi il nome era **uno di
dieci**, uno per elemento, e funzionava da **etichetta**; una gru sola no, e lì
幻惑 descrive cosa fa. *La stessa prova non porta alla stessa conclusione quando
cambia cosa il nome sta facendo.*

### Prima di scegliere, guardare cosa il nucleo ha scelto per i parenti

ハムスター finisce per **スター**, e Elona+ ci costruisce sopra una famiglia:
モーニングスター, デススター, シューティングスター. L'inglese salva il criceto
(`death hamster`, `shooting hamster`) e perde il gioco di parole.

La scelta sembrava aperta — criceti o stelle — e non lo era: il nucleo aveva
già reso `Morningstar` → «la stella mattutina». Decidere per i criceti avrebbe
spezzato la famiglia a metà, in silenzio, e nessun test l'avrebbe visto.

### L'inglese sbaglia più di quanto il progetto stimasse

Su 351 nomi, una dozzina di errori veri di lettura, non abbreviazioni: 腕白
(*monella*) letto coi kanji separati e diventato `the white arms`; 猫かぶり
(l'idioma «fingersi ingenui») preso alla lettera in `the cat freak`; 首切雀 (il
passero mozzatesta) scambiato per la passera mattugia; 化け狸 reso `badger`, che
è un altro animale; 魔剣士 reso `knight`; 淫婦 reso `camouflaged imp`; 虚空
(*vuoto*) reso `vanity`; ヤミクミロミ (*oscuro*) reso `Insane`.

E tre volte ha **spostato la razza**: la aggiunge dove il giapponese non ce l'ha
(歴戦の老兵 → `zanan old soldier`) e la toglie dove ce l'ha (エレアの難民 →
`refugee`; イェルス超重力砲 → `gravity cannon`). In tutti e tre i casi si segue
il giapponese, che è quello che il nome dice.

### Le fusioni si rifanno, non si leggono

Razze intere sono costruite su giochi di parole, e **l'inglese non li traduce:
li ricostruisce in inglese**. ダゴンズイ (ダゴン + ゴンズイ) diventa
`daganotosus` col nome scientifico *Plotosus*; エンタメイド・ザンコック
(残酷 + コック) diventa `cocruel`; インコニート (インコ dentro «incognito»)
diventa `inconeet` con `keet` di *parakeet*.

Quindi il precedente c'è già, ed è dell'inglese: si rende il **gioco**, non le
sillabe. «Il pesce gatto Dagon», «la spettacameriera cuocrudele»,
«l'incocorito».

### Un aggancio riparato all'indietro, e la regola che ne resta

`text.hsp` chiedeva «Come si chiama l'**investigatore** della Gilda dei
Maghi?», ma la risposta è `<Lenas>` e `db_creature.hsp` le dà `SEX=1`.
Ritradotta al femminile.

**Le domande del quiz sono già a schermo, i nomi no**: di norma sono i nomi a
doversi adeguare alle risposte già tradotte — `<Lexus>` è «il guardiano della
Gilda dei Maghi» perché così dice la domanda. Tranne quando la domanda contiene
un'ipotesi presa quando i nomi non c'erano ancora, ed è il caso di `<Lenas>`.

### Due deroghe alla regola dell'articolo, e non una di più

`SENZA_ARTICOLO` in `test_creature.py` ha due voci e un test pretende che
restino esattamente quelle: `＠`, il simbolo del giocatore fatto creatura (parla
«Qy@» e nient'altro), e `user`, che non è un nome ma lo slot dei PNG definiti
dal giocatore.

Il secondo lo firma il sorgente: `lang("user", "user")`. Il giapponese è
**identico** all'inglese, e in un file dove ogni nome vero ha la sua forma
giapponese quello è upstream che dice «questo non è testo».

## La sedicesima sessione — 2026-08-10

Aperta con le quattro verifiche verdi (336 test, identità 72/72 e 27.813, 0 da
ritradurre, creature 1131/320 senza doppie). Poi una domanda — «per il collaudo
serve un salvataggio nuovo?» — che ha chiuso un collaudo in sospeso da due
sessioni e ne ha tirato fuori tre cose da non riscoprire.

### L'evoluzione vera è stata provata, e la rinomina regge

`Norfor il cavallo zoppo` → **`Norfor l'unicorno`**. È il collaudo rimasto
aperto dalla quattordicesima sessione, e adesso è chiuso.

Le condizioni, tutte dal sorgente: impressione ≥ 150 (`action.hsp:16630`),
`CDATA_EVOLUTION_STAGE == 0`, nessuna Form Shift, bersaglio in uno slot alleato
(`tc < MAX_CHARA_FOLLOWER`, cioè 16 — `action.hsp:16626`), e l'oggetto usato su
una delle **otto caselle adiacenti**, perché `*prompt_direction`
(`system.hsp:4105`) non ne offre altre.

### È scattato il ramo suffisso, e il bug che contiene è latente

Il nome memorizzato era `Norfor il cavallo zoppo`: il prefisso non combacia, e
la rinomina è passata da `action.hsp:18643-18644`. Quella riga calcola la
lunghezza su `cdatan(CDATAN_NAME, rc)` invece che su `tc` — indice sbagliato,
e `*charaRefresh` poco sopra lavora su `r1`, non tocca `rc`.

**Ha dato il risultato giusto**, quindi lì `rc` valeva `tc`. Il difetto è
latente, non attivo su questo percorso. Va scritto proprio perché non si è
manifestato: se un domani un'altra evoluzione ci arriva con `rc` diverso, il
nome viene troncato e non ci sarebbe modo di risalire al perché.

Conferma sul campo di [[la-forma-memorizzata-non-e-quella-scritta]]: il ramo
che il conteggio sul sorgente dava per irraggiungibile è quello che il gioco
percorre davvero, perché il nome proprio va in testa e la specie in coda.

### Il non tradotto esce in inglese, non in giapponese

Sembra ovvio detto così, e non lo era: `applica` sostituisce l'italiano nello
slot **inglese** di `lang(jp, en)` (`applica.py:305`, `inizio_en`), e il gioco
gira in modalità inglese. Quindi ogni cornice non ancora tradotta si legge in
inglese, con dentro i nomi italiani già fatti — `Norfor il cavallo zoppo's
speed increases`, genitivo sassone su nome italiano.

Non è un difetto: sono fra le **915 dinamiche di `action.hsp`**. Ma è il modo
in cui il gioco si presenterà a ogni collaudo da qui alla fine del punto 3, e
conviene saperlo prima di segnalarlo come rotto.

### La console Lua non c'era, e la spiegazione che combaciava era un'altra

Per scrivere impressione e `PARAM1` serviva la console Lua. Non rispondeva. La
causa non era `--develop` — `dirinfo(4)` restituisce esattamente `[--develop]`,
verificato compilando un exe di quattro righe con l'SDK — ma
`main.hsp:9`, `;#define CUSTOM_GX_LUA`, **commentata a monte**: il ramo che
sceglie fra le due console (`system.hsp:4417-4425`) è dentro `#ifdef`, quindi
senza define si va sempre sulla console vecchia.

Nel frattempo era emersa una spiegazione alternativa che combaciava con tutte
le prove — il comando `lua` confronta con `"lua\n"` mentre il buffer finisce
con `\r\n` (`system.hsp:4820` contro `5021`) — e che **resta non verificata**,
perché in quel binario quel codice non era compilato. Sta in
[[strumento-di-diagnosi-assente-non-guasto]].

### Come si rifà il collaudo con la console

Esiste ora `cgx-lua.exe` in `elonaplus2.31\`: stessa build della traduzione ma
con `CUSTOM_GX_LUA` attiva. La modifica è stata fatta **solo in BUILD** e
subito ripristinata — SORGENTE non è stato toccato e `compila --eseguibile`
produce di nuovo l'exe normale. Serve anche `hsplua.dll`, che nella cartella
del gioco non c'era ed è stata copiata dal sorgente.

Si avvia con `--develop` (senza, `dbg_luaConsole` resta 0 e il comando `lua`
per riaccenderlo è quello di cui sopra). Poi **F12**, e la sintassi che
funziona è `dim[attributo][indice]`:

```lua
return cdata[17][2]                 -- CDATA_IMPRESSION dell'alleato 2
cdata[17][2] = 150
return cdata[214][2]                -- CDATA_EVOLUTION_STAGE, dev'essere 0
return itemcreate(869, 0, 0, 0, 0)  -- ITEM_ID_EVITEM in inventario, torna ci
inv[25][17] = 14                    -- INV_ITEM_PARAM1 = EVITEM_HEART_ANOTHER
```

`cgx-lua.exe` è uno strumento di collaudo, non l'eseguibile che si spedisce:
quello resta `cgx-test.exe`.

### Otto lotti, e `db_card.hsp` come arbitro

122 nomi: `karune` 18, `ghost` 17, `roran` 17, `worm` 15, `dragon` 15, `cat` 14,
`metal` 14, `largeanimal` 13. Il criterio del taglio per razza non è cambiato.
È cambiato **a chi si chiede quando il nome è opaco**.

Il blocco della creatura dice cosa la creatura è nel sistema — razza, sesso,
classe, azioni. Non dice cosa **rappresenta**, e per un nome è quello che serve.
`db_card.hsp` sì: ogni creatura ha una carta con due o tre frasi di prosa in
`cardrefskill`, e lì c'è l'intenzione.

Su `ghost` e `roran` ha deciso quasi tutti i nomi che dal solo blocco sarebbero
rimasti opachi, e ha ribaltato l'inglese cinque volte. I casi in tabella stanno
in `avanzamento.md`; qui vale la pena tenere i due che insegnano il metodo:

- **`アークレイス`** — la carta non spiega il caso, spiega la **regola**: «gli
  individui particolarmente forti si distinguono come rango sovrano e prendono
  il prefisso `アーク`». Una riga che decide tutta la famiglia futura, non un
  nome. «L'arcispettro».
- **`『Ｈな妹』` contro `えっちな妹`** — stesso scherzo apparente, stessa resa
  inglese (`H sister` due volte), e sono due cose diverse: la carta della
  seconda comincia con «**ヒットマン**な妹». «La sorella minore maliziosa» e «la
  sorella minore sicaria». Senza le carte sarebbero diventate lo stesso nome, e
  nessun test l'avrebbe visto.

⚠️ **La carta non sostituisce il blocco.** Su `病兄` servono tutti e due:
`CDATA_SEX = 0` dal blocco, e dalla carta il fatto che i maschi di Roran siano
davvero malati e muoiano da bambini — che è la ragione per cui **non** segue il
precedente di `病妹` → «la sorella yandere». Terza volta che la stessa forma non
porta alla stessa conclusione.

### I kanji omofoni: si traduce la base, non la patina

Due nomi scritti con kanji che suonano come un'altra parola, e l'inglese aveva
tradotto l'omofono — stavolta **giustamente**, che è la parte che poteva
ingannare, perché su questo file l'abitudine è che l'inglese sbagli.

Il criterio, ora in `guida-stile.md`: il lettore giapponese sente per prima la
parola base, i kanji sono la patina; l'italiano non ha gli ateji e non può
sovrapporre i due strati, quindi traduce la base e prova a far entrare la patina
**dentro un'espressione idiomatica** invece che in una parola in più.

- `非情ベル` (spietato / `非常ベル`, il campanello antincendio) →
  **«la campana a martello»**: suonare a martello *è* l'allarme, e «a martello»
  porta da sé la durezza. I due strati in tre parole, come l'originale.
- `烈闘龍『サンライズ』` (lotta feroce / `列島`, arcipelago) →
  **«<Sunrise> il drago dell'arcipelago»**: qui una parola che faccia tutte e
  due non c'è, e allora si prende la base — la carta parla di mare, alba e
  dimensioni, di lotta non dice niente.

Il modo di distinguerlo dal caso «l'inglese ha letto male» è di nuovo la carta:
se descrive l'omofono e non i kanji scritti, i kanji sono la patina.

### La guardia dell'articolo ha fermato un nome

`シルバースカル陛下` era diventato «sua maestà il teschio d'argento» e il test
l'ha bocciato: non comincia con un articolo. La rinomina all'evoluzione
sostituisce la stringa intera e `name()` non antepone più nulla, quindi sarebbe
uscito nudo a schermo. «La maestà del teschio d'argento».

Vale la pena notarlo insieme al collaudo di questa stessa sessione: la proprietà
che il test difende è **esattamente** quella che l'evoluzione di Norfor ha
mostrato funzionare. Il test non era una precauzione teorica.

### Lasciato aperto di proposito

`action.hsp:17390`, `電気竜` → «il **draco** elettrico». Unica occorrenza contro
decine di «drago»: è un refuso, non una distinzione. Non corretto perché sta
fuori dai lotti, e una voce già chiusa che si ritocca va vista in un commit suo.

## La diciottesima sessione — 2026-08-10

Aperta per collaudare i 1.131 nomi mai visti a schermo. Il collaudo ha fatto il
suo mestiere — ha confermato «draco» e ha mostrato un difetto tipografico — ma
la scoperta più grossa è arrivata leggendo il sorgente per prepararlo.

### 440 rinomine all'evoluzione erano morte, e nessuna guardia poteva vederlo

Il difetto più grave trovato finora, e sta **fra due file**, non dentro uno.

La rinomina all'evoluzione confronta il nome memorizzato con un letterale del
sorgente (`strmid(nome, 0, strlen(evold)) == evold`). In `action.hsp` quel
letterale è tradotto insieme al resto, ed è per questo che il collaudo di Norfor
aveva visto la rinomina funzionare. Ma la stessa logica esiste in tre file **che
non erano nel dizionario**:

| file | letterali `evold`/`evname` ancora inglesi |
|---|---|
| `custom_enemyevolution.hsp` | 418 |
| `ai.hsp` | 16 |
| `event.hsp` | 6 |

Là `evold` era rimasto inglese mentre il nome a schermo era diventato italiano:
`strmid(nome, 0, strlen("hand of the murderer")) == "hand of the murderer"`
contro «la mano dell'assassino». Non combacia mai, né col ramo prefisso né col
suffisso. Il nemico evolve — statistiche e sprite cambiano — e **tiene il nome
di prima**. Il codice è vivo: `init.hsp:117` lo include, `chara.hsp:2321` lo
chiama quando l'opzione *Spawn evolved enemies* è attiva.

Tutte le guardie erano verdi, e nessuna poteva vederlo: ognuna misura la salute
di un file tracciato, e il difetto stava nella relazione con un file fuori
perimetro. Nuovo concetto: [[coerenza-fra-due-file-uno-solo-tracciato]].

**La riparazione.** I tre file sono entrati nel dizionario: 379 firme uniche
(le 440 letterali contengono ripetizioni), **tutte risolte automaticamente
cercando il giapponese** nel dizionario esistente — zero ambigue, zero mancanti.
La chiave giusta era il giapponese, non l'inglese, perché entrambi i file
copiano il nome della creatura e il giapponese è identico per costruzione.
`custom_enemyevolution.hsp` risulta chiuso al 100%: le sue uniche stringhe
`lang()` sono quelle.

⚠️ **Riparare ha reso raggiungibile un ramo che non girava.**
`custom_enemyevolution.hsp:2400` porta lo stesso scambio di indice (`rc` invece
di `tc@PE`) del difetto latente noto di `action.hsp:18643`. Verificato che resta
latente: non esiste nessun `#module PE`, quindi quel `rc` è il globale, nel
modulo non viene mai riassegnato, e `chara.hsp:2320` fa `tc@PE = rc` subito
prima della chiamata. È inerte **per coincidenza, non per costruzione** — ed è
ora il secondo esemplare dello stesso difetto.

### Il title case inglese sugli epiteti — una toppa di tipo nuovo

Trovato al primo screenshot del collaudo: `<Ratin> L'investigatrice Della Gilda
Dei Guerrieri`. Il dizionario aveva scritto tutto in minuscolo.

`custom_dmgpop.hsp:237` — l'etichetta sopra la testa delle creature — faceva
`capitalize(names@DP(0), 1)`, dove il modo `1` è il title case inglese. È
**cablato a mano**: non passa dall'opzione `capitalizeItemName`, che l'utente
può spegnere e che di default vale già 0. Le altre tre chiamate a `capitalize`
riguardano i nomi d'oggetto e obbediscono all'opzione: quella era l'unica
forzata.

Si vedeva solo sulle creature **con epiteto**: senza alias il nome passa dal
ramo `s@DP(0) == ""` (riga 239) che salta la capitalizzazione, ed è per questo
che «il draco di fuoco» e «il ratto sanguinario» nello stesso screenshot erano
corretti. Un collaudo su tre mostri comuni non l'avrebbe incontrato.

Toppa 255ª. È un tipo che il progetto non aveva ancora incontrato: non una
stringa che il dizionario non raggiunge, ma una **trasformazione che deforma una
stringa tradotta bene**. Registrato in [[toppe-fuori-dal-dizionario]].

### «sigillo dei nove dèi» usciva «de'i»

Il caso che questo stesso documento descrive dalla decima sessione — l'accento a
metà parola degrada male — era rimasto **nel dizionario**, mai corretto. Vivo nel
build in due forme, singolare e plurale. Reso «sigillo delle nove divinità»:
l'accento torna a fine parola, dove la degradazione è invisibile.

⚠️ Il primo giro di correzione ha mancato il plurale, perché il plurale è un
**campo separato** del dizionario (`plurale`), non derivato dal singolare in
fase di build. Il controllo dell'accento a metà parola è stato riesteso a tutti
i campi di testo — 6.772 invece di 5.053 — e ora sono zero.

### Le 320 stringhe di voce, e l'inglese che inventa

Chiuse tutte. Su questo lotto l'inglese non abbrevia: **inventa**. `「ガルルル…」`
è un ringhio, e l'inglese ci ha messo «You hear the near silent footfalls of a
cat. A Big cat.» — una frase intera che nel giapponese non esiste. Stessa cosa
per il grifone, per il fabbro `<Garok>` e per la fatina. Due volte ha proprio
capovolto il senso: `あの男` (*quell'uomo*) diventa «that girl» nella battuta di
Loyter, e `トドメを刺した` (*ha dato il colpo di grazia*) diventa «tormented».
Reso il giapponese, come da regola.

**Le virgolette hanno sciolto un problema di identità.** Il grido del grifone è
`Hjckrrh`, che in italiano resta `Hjckrrh`, e la guardia dell'identità l'avrebbe
bocciato otto volte. Ma la resa corretta non è identica: il sorgente inglese
scrive le virgolette dritte, e la convenzione del progetto impone le tipografiche
`“”` perché una `"` chiuderebbe la stringa HSP. La differenza è reale, non un
aggiramento della guardia.

**Nuovo controllo: gli spazi esterni.** Molte di queste stringhe sono ` *così* `,
con spazi che fanno parte della resa e che nessuna guardia esistente guardava.
Il controllo ha segnalato 14 disallineamenti fra italiano e inglese: tutti e 14
seguono il **giapponese**, coerentemente con la regola dell'arbitro. Uno solo è
diverso per scelta — il frammento `, vuoi assaggiare anche tu?”`, dove la virgola
deve seguire il nome interpolato senza spazio.

### Le 59 rinviate del quiz, e un falso che rendeva una domanda irrisolvibile

Chiuse. `rinviate.jsonl` scende da 79 a 20: restano solo quelle che aspettano
`proc.hsp`.

⚠️ **Il caso da non ripetere.** La domanda «quale di questi segugi ha il nome
esatto?» offre un vero e tre falsi. Il falso `混沌ハウンド` sarebbe diventato «il
segugio del caos» — ma `カオスハウンド` **esiste** (`db_creature.hsp:109000`) e
in dizionario è già «il segugio del caos». Due opzioni identiche a schermo, e la
domanda non ha più risposta. Trovato facendo controllare a uno script che
nessuna resa collidesse con un nome già in dizionario, non a occhio. I tre falsi
sono ora «degli inferi», «delle tenebre» e «caotico», vicini ai veri
«dell'oltretomba», «dell'oscurità» e «del caos» senza toccarli — che è il
rapporto che hanno anche in giapponese. Vedi
[[una-chiave-che-collide-non-e-una-chiave]].

⚠️ **Quattro risposte sono oggetti veri il cui nome vive in un file non
tradotto.** Le tre pietre di Lesimas e l'ankh del sole si ottengono da
`chara_func.hsp:7347-7448`. Tradurre il quiz e non quel file significa che il
giocatore riceve `[Sage's Magic Stone]` in inglese e la ritrova in italiano
nella domanda. Non risolvibile qui — è un file intero — ma il precedente è
**fissato in `glossario.md`** con la tabella EN→IT e i riferimenti di riga:
quando `chara_func.hsp` entrerà nella pipeline quelle rese si copiano, non si
reinventano.

Quattro voci non erano un quiz: `zombie + dragon zombie` e le altre tre sono il
menù di negromanzia (`txtsetnecrom`), coppie di non morti da evocare.

### La guardia delle interpolazioni rendeva certe dinamiche intraducibili

Aperto `action.hsp` (26 dinamiche su 318) e la strada era bloccata.

`verifica.py` pretende che la traduzione conservi le chiamate di contenuto
dell'inglese — giusto, perdere `name(tc)` significa perdere il nome dal
messaggio. Ma `funzioni_di_contenuto` contava anche ciò che sta **dentro** una
chiamata di morfologia. In `action.hsp:1016`:

```hsp
name(gdata(GDATA_RIDER)) + " " + is(gdata(GDATA_RIDER)) + " using it."
```

il secondo `gdata` serve solo a scegliere fra «is» e «are». `is()` va tolta per
forza — non passa mai da `lang()`, resterebbe inglese per sempre — e togliendola
sparisce il suo argomento: **nessuna resa italiana corretta poteva passare**.
L'unico modo di soddisfare la guardia era stampare il dato due volte.

Corretto `_classifica` perché salti gli argomenti della morfologia. Il criterio
non è «la guardia è scomoda», è che **una funzione di grammatica non stampa mai
ciò che riceve**: verificate una per una, `is`, `was`, `_s`, `your`, `have`,
`does`, `yourself` restituiscono tutte una parola inglese fissa, scelta
guardando l'argomento e basta.

⚠️ **La correzione ha fatto cadere due test esistenti**, ed è lì che si decide se
si sta riparando o aggirando. Riletti per il loro obiettivo dichiarato: entrambi
volevano dimostrare che `his` a un argomento e `_s2` sono morfologia, e quello è
intatto. Le asserzioni cadute erano **incidentali** e sbagliate per la stessa
ragione del difetto — `his(cdatan(CDATAN_NAME, tc))` pretendeva `cdatan` nella
traduzione, ma la resa giusta è «il suo portafoglio», e pretenderlo significava
chiedere una chiamata che a schermo stampa il **nome del personaggio**, cioè
un'altra frase. Aggiunti due test per la regola nuova. Vedi
[[guardia-troppo-severa]], di cui è il terzo esemplare.

**«Mordes» è localizzato.** `action.hsp:4887`: `_melee(0, ...)` è già tradotto in
`text.hsp:164` come «morde», e `_s(cc)` gli attacca la «s». Sparisce quando si
traduce quella riga. Il gemello è in `proc.hsp:8797` — lo stesso file su cui
puntano le 20 rinviate rimaste: i due difetti si chiudono insieme.

### Cosa il collaudo ha insegnato sul collaudo

Il primo screenshot ha trovato il title case, che due letture del sorgente non
avevano visto. Ma è servita anche la direzione opposta: l'utente ha riferito che
`spawn_chara 659` gli aveva prodotto un ratto. Verificato da qui che le ID erano
corrette (`659` è davvero `<Vansesda>`, nessun `#define` doppio, e la
sostituzione casuale in `chara_init` scatta **solo** con `dbid == -1`), e che il
ratto è `412`, un numero mai dato. Era un mostro già presente sulla mappa.

> Un difetto riferito va verificato come uno trovato. La lista di passi fa
> entrare nel lavoro prove che il codice non sa dare, ma non tutto ciò che
> arriva da lì è un difetto.

⚠️ **Nota operativa:** la console di debug parte in **modalità HSP**, non Lua;
`characreate` è il nome Lua e risponde «comando sconosciuto» finché non si
digita `lua`. Il comando nativo è `spawn_chara <id>`, sta fuori dall'`#ifdef
CUSTOM_GX_LUA` (`system.hsp:4831`) e quindi funziona anche in `cgx-test.exe`,
che è l'eseguibile che si spedisce — meglio collaudare quello.


## 2026-08-10 — `action.hsp` chiuso: le due righe che non si traducono, e una guardia troppo severa

`action.hsp` è finito: 1.286 firme su 1.288. Le due che restano non sono
arretrato, sono decisioni.

### `action.hsp:9631` — un possessivo che in italiano si omette

La riga compone `name(tc) + " changed " + his(tc, 1) + " elemental affinity."`.
`his(x, 1)` — **due** argomenti — passa da `lang()`, quindi va localizzato, e la
guardia sulle interpolazioni pretende giustamente che sopravviva: a un argomento
solo resterebbe inglese dentro una frase italiana.

Ma in italiano il possessivo concorda con **la cosa posseduta**, non con chi
possiede, e `his()` è una funzione sola per **36 siti di chiamata** sparsi su
otto file, con nomi di generi diversi. Non esiste una forma che vada bene
ovunque: «suo» sbaglia davanti a un femminile, «sua» davanti a un maschile. La
resa giusta è quindi **vuota** — «ha cambiato elemento» —, e una resa vuota non
si può dichiarare nel dizionario.

Si risolve come `action.hsp:4584`: una riga in `rinviate.jsonl` e una toppa a
mano che riscrive la riga intera. ⚠️ Le toppe girano **dopo** il dizionario e non
passano da `degrada`, quindi il testo di una toppa va scritto **senza accenti**:
è il motivo per cui la resa è «ha cambiato elemento» e non «ha cambiato
affinità elementale».

⚠️ Da qui in avanti le righe da scartare a mano quando si compone un lotto sono
**due**: la 4584 e la 9631. `estrai --da-tradurre` le toglie già lui, ma il
conto delle non tradotte le porta per sempre.

### `action.hsp:12383` — ` Lv` invariato, e la guardia che ne è uscita rossa

`evold = lang(" Lv", " Lv")` è l'unico `evold` del sorgente che **non**
rinomina: cerca il suffisso di livello in coda al nome e lo taglia via
(`strmid`, riga successiva). L'italiano scrive `Lv` uguale — lo fanno già
`action.hsp:6545` e `text.hsp:65` — quindi la voce è andata in `invariati.md`.

Dichiararla ha però fatto diventare rossa
`test_ogni_evold_puo_combaciare_con_un_nome_che_esiste`: la guardia chiedeva a
ogni `evold` **tradotto** di combaciare con un nome di creatura, e ` Lv` non
combacia con niente. Non era un difetto della traduzione: era la guardia che
guardava una riga che non è una rinomina.

La discriminazione giusta il progetto ce l'aveva già: `accoppia_dal_sorgente`
tiene fuori gli `evold` **senza `evname` davanti**, perché l'`evname` è il nome
nuovo e senza di lui non c'è nessuna sostituzione. Portata su tutti e quattro i
file dell'evoluzione, quella regola esclude **una riga sola** su 514, e
`test_la_deroga_all_evname_vale_per_una_riga_sola` la inchioda a quella: se
upstream ne scrivesse un'altra si vuole scoprirlo, non ereditarla in silenzio.

> Verificato che la guardia resta viva: rimesso a mano un `evold` guasto
> (`younger cat sister` → un nome che non esiste), il test è tornato **rosso**;
> ripristinato il dizionario, verde. Una guardia allargata che non si è vista
> fallire dopo l'allargamento non è più una guardia.

Test: **344** (erano 343).

### Tre trappole di resa che questa zona ha ripetuto

1. **Il possessivo non è l'unico che concorda.** `_seikaku()` dà nomi astratti di
   generi misti e `bodyn()` dà parti del corpo di generi misti: in entrambi i
   casi la frase italiana ha dovuto **rinunciare all'articolo**, con «ha scoperto
   di avere Allegria» e «ha una parte nuova: Mano!». È la stessa regola
   dell'articolo dentro il nome di creatura, vista dal lato della frase.
2. **L'invarianza di genere costa una parola, non una perifrasi.** «prende
   fuoco» invece di «è avvolto dalle fiamme»; «Quella creatura è già appesa»
   invece di «È già appeso», dove il genere lo fissa il nome comune che si
   aggiunge. E per gli insulti rivolti al giocatore esiste una parola invariante
   che li risolve quasi tutti: «idiota».
3. **Una `statica` si scrive nuda.** Il `it` di una voce statica è testo, non
   espressione: incapsularlo fra virgolette come si fa con le dinamiche fa
   fallire `verifica` su sedici voci in un colpo solo. E dentro una statica le
   virgolette devono essere le tipografiche `“”`.


## 2026-08-10 — 391 stringhe che il giocatore legge e che nessun conteggio vedeva

Trovate da uno screenshot dell'utente, non da una lettura del sorgente. Provando
l'occhio elementale, a schermo compariva **`colorful eyes`**.

Non era un difetto della traduzione di `action.hsp`: un oggetto di Elona ha
**due** nomi, e noi ne traducevamo uno solo.

- `ioriginalnameref(ITEM_ID_ELEMENTS_EYES)` = `<Elements Eyes>` — il nome vero,
  quello dopo l'identificazione. In dizionario da sempre.
- `iknownnameref(ITEM_ID_ELEMENTS_EYES)` = `colorful eyes` — il nome che il
  gioco mostra **finché l'oggetto non è identificato**. Mai estratto.

La causa è esplicita e non è una svista di scansione: `_ASSEGNA_NOME`
(`estrai.py:65`) accetta `ioriginalnameref` e `ioriginalnameref2`, e basta. La
scelta era motivata — il commento sopra dice che agganciare per analogia gli
altri `if ( jp )` di `db_item.hsp`, che sono 2.902 contro 1.321 di nomi, è il
modo di corrompere il sorgente in silenzio — ma ha lasciato fuori una classe
intera di testo visibile.

### Il censimento

Contate tutte le assegnazioni `array(...) = "letterale"` con caratteri latini,
fuori da `lang()`, che il dizionario del loro file non copre:

| file | array | quante | cosa sono |
|---|---|---|---|
| `db_item.hsp` | `iknownnameref` | **261** | nomi non identificati |
| `custom_tweaks.hsp` | `TweakData` | **77** | il menu opzioni di Custom-GX |
| `custom_ai.hsp` | `listn` | **20** | il menu dell'IA dei compagni |
| `custom_pet.hsp` | `listn` | **10** | il menu impostazioni dei compagni |
| `custom_dmgparse.hsp` | `DmgParsesClass` | 12 | da classificare |
| vari | `listn`, `cellobjname`, `description` | ~11 | spiccioli |

**391 stringhe.** Escluso a mano ciò che è dato e non testo: `filter_item`,
`rffilter_item` e `filter_creature` (1.489 stringhe come `/fish/`, `/noshop/`,
`/nogive/`) e gli identificativi di razza di `db_race.hsp`
(`listn(1, listmax) = "kobolt"`).

⚠️ **Verificato che l'estrattore non ha altri buchi sui nomi.** I 39
`ioriginalnameref` che risultavano scoperti sono il ramo **giapponese**, presi
dal filtro perché contengono lettere latine (`Resアッパー`, `TZ500-K型麻酔銃`):
il 1.321 su 1.321 dichiarato in `estrai.py` regge.

### Due 100% falsi

`db_item.hsp` e `custom_tweaks.hsp` risultano chiusi mentre hanno
rispettivamente 261 e 77 stringhe visibili in inglese. Non è un errore di
calcolo: il denominatore conta solo ciò che l'estrattore sa vedere.

> Una percentuale non dice quanto manca: dice quanto manca **di ciò che lo
> strumento guarda**. Le due cose divergono in silenzio, e a farle divergere è
> sempre una classe di siti che nessuno ha dichiarato.

### Decisione

**Si annota e si prosegue col piano.** Il perimetro nuovo si affronta dopo la
Fase 1. Quando ci si torna, l'ordine giusto è:

1. **prima lo strumento che misura**, non la traduzione: un conteggio dei
   letterali scoperti con l'elenco esplicito di ciò che è dato, così il buco
   resta visibile invece di dipendere da chi si ricorda di questa pagina;
2. poi i 261 `iknownnameref`, che sono la classe che si vede di più giocando —
   ogni oggetto non identificato la mostra;
3. ⚠️ e attenzione: `iknownnameref` alimenta `itemname()` come il nome vero,
   quindi vuole lo **stesso trattamento** di articolo e plurale descritto in
   `contratto-nomi.md`. Non è una tabella di etichette, è un nome.

⚠️ **Restano fuori dal conteggio anche i nomi calcolati**, non solo i letterali:
`iknownnameref(ITEM_ID_SCROLL_...) = _namescroll(p) + strblank + strscroll`. Le
loro parti hanno già toppe generate (`genera_toppe_casuali`), ma nessuno ha
verificato che la copertura sia completa.

### La regola che questa scoperta conferma

È la terza volta che una prova a schermo dell'utente trova ciò che due letture
del sorgente non trovano. Le prime due erano difetti; questa è **un pezzo di
perimetro**. Chiedere la prova presto non serve a validare: serve a scoprire
cosa non stiamo nemmeno guardando.

## 2026-08-11 — `text.hsp` chiuso, e le 20 rinviate di `elename()` sciolte spostando l'articolo

`proc.hsp:8797` compone la frase del tocco elementale come **aggettivo + parte
del corpo**:

```hsp
name(cc) + " touch" + _s(cc) + " " + name(tc) + " with " + his(cc)
+ " " + elename(ele) + " " + _melee(2, cdata(CDATA_MELEE_STYLE, cc)) + " and"
```

In italiano l'aggettivo **segue** il nome e ne prende il genere, e le parti del
corpo sono di generi misti — mano, artiglio, gamba, zanna, occhio, aculeo,
spora, ramo, braccio, corpo, chela. Nessuna resa di `elename()` poteva
accordarsi con tutte, e per questo dalla nona sessione le sue 20 firme stavano
in `rinviate.jsonl`.

**La soluzione ha tre pezzi, e nessuno funziona da solo.**

1. **`elename()` smette di essere un aggettivo.** Diventa un complemento
   invariabile: «di fuoco», «di veleno», «di tenebra», «della fame». Senza
   genere non c'è accordo da sbagliare.
2. **La parte del corpo si porta dietro il proprio articolo** — «la mano»,
   «l'artiglio» — che è la cosa che a runtime nessuno potrebbe scegliere.
   ⚠️ Si può fare **solo** perché la terza colonna di `_melee` esce da due righe
   in tutto: `grep _melee(2,` dà `proc.hsp:8797` e `:8800` e basta. Cambiare il
   valore di una funzione condivisa senza contare i chiamanti è il modo di
   rompere venti frasi per aggiustarne una.
3. **La resa riordina la concatenazione.** È permesso: `funzioni_di_contenuto`
   (`strumenti/funzioni.py:183`) confronta le interpolazioni **ordinate**, cioè
   l'ordine non entra nel confronto. `his(cc)` a un argomento si toglie, e
   l'articolo della parte del corpo copre il possessivo che l'italiano omette.

Esito: «tocca il cane con la zanna di veleno e...».

> **Un rinvio può dipendere da dove sta l'articolo, non dalla resa.** Prima di
> dichiarare intraducibile una concatenazione, contare i chiamanti di ogni
> pezzo: se sono pochi, il pezzo si può ridefinire, e il problema si sposta
> dove è risolvibile.

Con questo `text.hsp` è **chiuso**: 1.718 firme su 1.720, e le 2 che restano
aspettano `data/talk.txt`, fuori perimetro. ⚠️ Il denominatore è **sceso** da
1.740 a 1.720, perché venti firme sono passate dal fuori-conto al numeratore.

## 2026-08-11 — Una stringa può essere invisibile perché manca un interruttore

Le 169 battute degli dèi (`txtgod`, `text.hsp:12143-12522`) sono state tradotte
tutte in questa sessione, e **non escono mai** se il giocatore non indossa un
oggetto con `ENCHANT_GOD_SIGNALS`: `gdata(GDATA_GOD_TALK)` parte a 0
(`screen.hsp:8216`) e solo quell'incantesimo lo accende (`screen.hsp:8474`). In
tutto il gioco lo porta **un oggetto solo**, `<Conchiglia Ignota>`
(`db_item.hsp:81492`). E serve anche seguire un dio: con `GOD_EYTH` la funzione
esce alla prima riga (`text.hsp:12144`).

Una lista di collaudo data senza saperlo avrebbe prodotto uno screenshot muto e
la conclusione «non tradotto» su lavoro giusto — e sarebbe stata colpa mia, non
sua.

> **Prima di chiedere una prova a schermo, cercare chi accende la stringa, non
> solo chi la scrive.** Il percorso va verificato fino all'interruttore.

Corollario trovato nello stesso giro: `spawn_item 171` genera un altare **senza
dio** (`db_item.hsp:119828` non tocca `INV_ITEM_GOD`), e pregarci rende
«unbeliever» invece di convertire. La conversione vera vuole un altare di mappa,
e il dio è quello dell'altare (`god.hsp:551`). La scorciatoia ovvia era
sbagliata, come `spawn_item 733` per il cibo.

## 2026-08-11 — La venticinquesima sessione: tre guardie che passavano guardando la cosa sbagliata

Sessione lunga, sei commit. Il lavoro visibile è `proc.hsp` da 78 a 127 firme e
`db_creature.hsp` da 2.203 a 1.975 da fare, ma la parte che conta sono **tre
difetti**, tutti della stessa forma: un controllo verde perché misurava qualcosa
di adiacente a ciò che doveva misurare.

### 1. `name(cc)` e `name(tc)` erano la stessa cosa per ogni guardia

`proc.hsp:763` faceva **tirare il sasso all'artista** invece che allo spettatore
che si era stufato: il sorgente dice `name(tc)`, la resa diceva `name(cc)`.

Il compilatore non ha niente da dire — `cc` e `tc` sono due variabili valide — e
la prova d'identità nemmeno, perché giudica la pipeline delle sostituzioni.
`funzioni_di_contenuto` (`funzioni.py:180`) confronta i **nomi** delle chiamate,
e i due nomi sono entrambi `name`.

La guardia nuova è `chiamate_di_contenuto`, che confronta la chiamata **intera,
argomenti compresi**, e `verifica.py` pretende che ogni chiamata dell'italiano
compaia identica in una delle **due** forme di monte.

⚠️ **L'unione delle due, non il solo inglese.** I due rami di `lang()` a volte
scelgono soggetti diversi per lo stesso evento: `action.hsp:1698` è
`name(cc) + " disturb" + ... + his(tc) + " sleep."` in inglese e
`name(tc) + "は睡眠を妨害された。"` in giapponese, e la resa italiana segue il
giapponese («si sveglia di soprassalto») perché l'inglese chiederebbe il
possessivo che l'italiano omette. Pretendere l'inglese avrebbe **rifiutato una
resa giusta**.

Il testo dentro le stringhe non conta come argomento: `cnvtalk("Ciao")` e
`cnvtalk("Hi")` sono la stessa chiamata. Senza la maschera dei letterali la
regola avrebbe segnalato 27 battute tradotte bene.

Sul dizionario intero: **una sola violazione**, il difetto.

> Una guardia che confronta i nomi delle chiamate non sta confrontando le
> chiamate. Il personaggio sta negli argomenti.

### 2. `creature.py` classificava 320 battute su 2.466

`_LANG` pretendeva un letterale nudo subito dopo il giapponese, mentre **il ramo
inglese di una battuta sta dentro `cnvtalk()`**. Restavano fuori 1.213 righe su
1.304, cioè **2.939 firme su 5.717 senza classe** — e
`nessuna_firma_in_due_classi`, la rete che impedisce a un nome di essere anche
una battuta, girava a vuoto su **metà del file**.

⚠️ **Il test pinnato non ha protetto niente, e non poteva.** Diceva
`conto == {"nome": 1131, "voce": 320}`: era stato scritto sul numero che il
codice produceva, quindi **confermava il difetto invece di trovarlo**, e ha
resistito venti sessioni.

Il test nuovo misura il **sorgente** e non le uscite dello strumento: 1.565 righe
`txt lang(`, di cui 1.304 con `cnvtalk` dentro, e ognuna deve ricevere una
classe. Le 241 che restano senza sono le dinamiche, ed è giusto.

> Un test pinnato su un numero che lo strumento produce non è una misura: è una
> fotografia. La misura indipendente parte dal dato, non dall'uscita.

### 3. La cifra dopo il ♪ non arriva a schermo

`msg_write` (`init.hsp:1372-1386`) cerca il ♪, legge il carattere **subito dopo**
come indice dell'icona (`mark = int(strmid(msg, mp + 2, 1))`), disegna
`gcopy 3, 600 + mark * 24, 360, 16, 16` e poi **toglie dal testo il ♪ e la
cifra** (`mp + 2 + (mark != 0)`, riga 1382).

Non è un difetto di monte: è una notazione, e upstream la usa di proposito —
`item.hsp:3954` scrive `"Wow♪1 Zaaaako♪1♪1♪1 "`. Ma una resa che si trovasse una
cifra dopo la nota la perderebbe **in silenzio**, e nessun controllo lo vede: il
♪ è l'unico carattere a due byte ammesso, quindi passa `doppi_byte_cp932` per
costruzione. Dieci righe del sorgente usano `♪` con una cifra, **quattro in
`item.hsp`**, che non è ancora tradotto: la trappola è davanti a noi, non dietro.

Regola: un `♪` seguito da una cifra nell'italiano deve comparire identico in una
delle due forme di monte. Copiare l'icona che il sorgente sceglie è legittimo,
inventarne una a partire dal testo no.

Correzione dalla stessa lettura: `db_creature.hsp:46713` è
`lang("「♪1～！」", cnvtalk("~ ~"))` — il giapponese sceglie l'icona **1**,
l'inglese ha perso la nota del tutto, e la resa aveva due note nude (icona 0 due
volte). Ora porta l'icona che il sorgente ha scelto.

## 2026-08-11 — Le battute delle creature non possono stare ultime nel piano

Deciso guardando uno screenshot, non il codice.

Il log del gioco era dominato da **quattro stringhe inglesi** ripetute una
ventina di volte in due ore — «Crawling in my Robes!», «Oh I once heard of a
place called Nantucket...» — in mezzo a un log per il resto italiano. Sono le
battute del menestrello, `db_creature.hsp:102878`.

La misura che ne è seguita:

| classe | firme da fare |
|---|---|
| `DBMODE_FLAVOR_ANGERED` | 685 |
| `DBMODE_FLAVOR_DEATH` | 521 |
| `DBMODE_FLAVOR_PASSIVE` | 454 |
| `DBMODE_FLAVOR_KILL` | 438 |
| `DBMODE_FLAVOR_WELCOME` | 104 |
| un nome | 1 |

**2.202 delle 2.203 firme che restavano in `db_creature.hsp` sono battute**, e
delle 1.452 già fatte **1.131 sono nomi**: la Fase 2 ha chiuso i nomi e lasciato
intatto il corpus a frequenza più alta di tutto il gioco. Un nome si legge **una
volta**, quando incontri la creatura; una battuta oziosa **a ogni turno** in cui
la creatura ti sta accanto, e quelle di offesa e di morte a ogni combattimento.

`RIPRESA-sessione.md` le metteva al punto 7, ultime. Ora vengono prima di
`command.hsp` e `trait.hsp`.

> La frequenza di una stringa non si deduce dal file in cui vive. Il numero di
> firme dice quanto lavoro è, non quanto si vede.

### Il metodo: creature intere, non una classe alla volta

Il lotto prende **creature intere**, tutte e cinque le classi insieme. Il
registro di un mostro è uno, e scriverne una situazione per volta spezza la voce.
Lo strumento che compone il lotto raggruppa per `dbid` e ordina per riga.

### Le regole di resa che i quattro lotti hanno stabilito

**Un verso si rende in ortografia italiana, non si copia dall'inglese**, che
romanizza il katakana a modo suo. `Woof..` sta per l'ululato 「ワオーン…」, e
`Beep` sta a `Bip` come `Woof` sta a `Bau`. Dove il giapponese identifica
l'animale la resa lo segue: 「キーキー！」 su una **cavia** è uno squittio, cioè
«Squit».

⚠️ **Il giocatore è l'interlocutore, e non ha genere noto.** La regola del diario
valeva per la prima persona; qui vale per la **seconda**, ed è più insidiosa
perché «Welcome home!» chiede un participio in italiano. Le rese sono «Eccoti a
casa!», «Rieccola a casa.», «Eccoti di ritorno.». Vale anche per i vocativi:
`sir` sparisce, `You thief!` diventa «Al ladro!», `Die thief` diventa «Muori,
canaglia» — che è invariabile.

**Il registro può risolvere il genere.** Il maggiordomo e il vecchio maggiordomo
danno del **lei**, che è il loro tono e per di più non concorda mai.

**Il ♪ che l'inglese ha perso si rimette.** Le due battute della cthulhick sono
「～♪」 e 「♪1～！」 in giapponese e `~` e `~ ~` in inglese: la nota è sparita a
monte. ✅ **Verificato a schermo**: esce come icona, non come lettera latina.

**`...` è un invariato dichiarato**, non una riga dimenticata: è il silenzio di
`<Aime>`, giapponese 「…」, e la resa italiana dei puntini — tre punti ASCII,
perché `…` la build inglese lo sbaglia — coincide con l'inglese per costruzione.
La traduzione giusta **è** l'identità, e va scritta in `invariati.md` invece di
essere aggirata con una variante peggiore.

### `_onii` cambia genere col giocatore, e lo fa fuori da `lang()`

`text.hsp:111` è `_onii = lang("お兄", "Big bro"), lang("お姉", "Big sis")`, un
array indicizzato sul **sesso del giocatore**: in italiano «Fratellone» /
«Sorellona». Ha **36 siti di chiamata**, 24 solo in `db_creature.hsp`.

`db_creature.hsp:49879` lo interpola **fuori** da `lang()`: i due `lang()` sono
**due statiche separate** attorno al nome, e l'inglese mette «my» nella prima —
`"\"All thanks to my "` più `_onii(...)` più `"!\""`. In italiano «al mio»/«alla
mia» dovrebbe accordarsi con una parola che a runtime non si conosce. Stessa
forma delle 20 rinviate di `elename()`, e stessa soluzione: **si toglie
l'articolo e resta la preposizione nuda**. «Fratellone» non porta articolo — a
differenza di `name()` — quindi «a Fratellone» e «a Sorellona» reggono entrambe.

⚠️ E la seconda statica non poteva restare `!\"`, che sarebbe stata identica
all'inglese: le si fa portare la **domanda finale che il giapponese ha e
l'inglese ha perso** (「…ね？」). Così entrambi i frammenti sono tradotti davvero,
invece di uno tradotto e uno dichiarato invariante.

> Quando una concatenazione si spezza in due `lang()`, i due frammenti sono un
> lotto solo: il primo decide cosa il secondo può dire.

## 2026-08-11 — `Party Room` non è testo: è l'operando di un confronto

`proc.hsp:1123` confronta il nome della mappa con un letterale —
`if ( mdatan(MDATAN_NAME) == lang("パーティー場", "Party Room") )` — e il nome lo
**assegna** `map_rand.hsp:1287`, che è fuori perimetro. Tradurre solo il
confronto lo fa fallire per sempre, in silenzio: il ballo nella sala delle feste
torna a durare 4 turni invece di 41. Nessuna guardia lo vede, perché ognuna
misura un file tracciato e il legame sta fra due file.

**Rinviata**, come `evold`/`evname` con `db_creature.hsp`: si traduce **insieme**
a `map_rand.hsp`, non prima. Sta in `rinviate.jsonl` con il motivo.

## 2026-08-11 — Il collaudo delle esibizioni, e due percorsi che non esistono

Provato in gioco con `spawn_chara 326` (il menestrello) e `spawn_chara 9` (il
mendicante) in una piazza: dieci rese viste, tutte giuste, articoli compresi
davanti a un nome con epiteto fra parentesi angolari.

⚠️ **Due percorsi che sembravano provabili e non lo sono.** `ai.hsp:1654` e
`:1668` accendono la predica e il ballo dei PNG con `CDATA_AI_CALM` a **7** e
**8**, e in **tutto il sorgente nessuno assegna quei due valori**: sono codice
morto. Le battute del ballo e le reazioni alla predica si vedono solo usando tu
le abilità, e «Danza ammaliante» vuole un talento.

L'interruttore delle battute, invece, è acceso per costruzione: `ai.hsp:766`
chiede `cdata(CDATA_TXT, cc) != 0`, e `db_creature.hsp` lo incrementa **una
volta per ogni classe di battuta che la creatura possiede**. Poi serve stare
entro dieci caselle, e la battuta esce ogni 5 turni con probabilità 1 su 4
(`ai.hsp:768-771`).

> Prima di dare una lista di collaudo, cercare chi accende la stringa — e
> accertarsi che **qualcuno** assegni quel valore.

## 2026-08-11, ventiseiesima sessione — L'ordine dei lotti passa dal file al giocatore

Le battute si prendevano «per creatura intera, in ordine di riga». L'ordine di
riga è quello in cui le creature sono state aggiunte al gioco negli anni, e non
ha niente a che vedere con quante volte il giocatore le incontra: metteva
l'accattone di livello 2, che sta in ogni città, accanto a `<Jure la Benedetta>`
di livello 1200, che come creatura non si incontra mai.

Misurato prima di decidere: delle 1.975 voci che restavano, **605 stavano su
creature di livello 1-10** — quasi tutte con filtro `/man/`, cioè gli abitanti
delle città — e **528 su creature oltre il livello 100**.

**Deciso: ordine per livello crescente**, e a parità di livello prima chi ha più
battute. `--per-riga` rimette l'ordine vecchio.

⚠️ **Il livello è una procura, non una misura, e va detto.** Nel sorgente non
esiste un campo «quanto spesso esce»: `DBSPEC_CHARA_RARE` non lo è — lo leggono
solo il valore del cadavere (`item_func.hsp:2295`) e la mappa utente. Il livello
decide in quale fascia di Nefia la creatura può comparire, e le creature di
città lo hanno bassissimo: sbaglia sui casi singoli, ma sposta il lavoro dalla
coda verso la testa, che è quello che serve.

## 2026-08-11 — La stessa battuta giapponese può avere due firme

Il punk (`db_creature.hsp:104157`) e il teppista dicono **tredici battute
giapponesi identiche**, e da monte hanno ricevuto tredici inglesi tutti diversi
(「チキショー」 è `Son of a..` per uno e `Shit.` per l'altro). Il dizionario è
indicizzato per contenuto e nel contenuto c'è l'inglese: sono **due voci da
tradurre**, a lotti di distanza.

Se le due rese divergono, la stessa frase esce in due modi da due creature —
e **nessuna guardia lo vede**: sono entrambe italiano valido, entrambe diverse
dal loro inglese, entrambe senza morfologia residua. Le guardie erano scritte
tutte per voce singola.

Misurato: **88 giapponesi comparivano più di una volta**, dieci con rese già
divergenti, trentasette con una resa decisa e una voce ancora da fare.

⚠️ **Deciso: un promemoria, non un divieto.** Delle dieci divergenze **otto sono
legittime**, perché l'inglese *specializza* ciò che il giapponese lascia
generico: 「がおー」 è `*creaking*` su un golem di legno e `*growl*` su una
divinità serpente, e le rese «scricchiolio» e «grooo» seguono l'inglese come
devono — un golem di legno non ringhia. Una regola che pretendesse una resa sola
per giapponese avrebbe rifiutato lavoro giusto.

Quindi: `battute.rese_gia_decise()` stampa **nel referto del lotto**, accanto a
ogni voce, la resa che quel giapponese ha già ricevuto altrove; e
`battute --divergenti` elenca le divergenze da giudicare a mano. Allineate le
due introdotte l'11/08 (「わふっ」, 「お、カモだ…」) e quella della cthulhick, che
lasciava `~♪` non tradotto. Ne restano nove, tutte legittime.

## 2026-08-11 — `adv.hsp` non era in nessun elenco, ed è in perimetro

Uno screenshot ha mostrato «Hedorre il fratello volpe **joins your party!**»:
nome tradotto, frase inglese. Viene da `adv.hsp:202`, un file **dentro il
perimetro degli strumenti** ma assente da ogni elenco di lavoro — 12 voci, tutte
messaggi ad alta frequenza (reclutamento, gruppo pieno, contratto scaduto,
potere divino perduto). **Tradotto e chiuso al 100%.**

Due cose imparate lì:

- ⚠️ **`cdatan(CDATAN_NAME, rc)` porta l'articolo dentro**, come `name()`: il
  nome italiano è «il fratello volpe». Quindi «Some of X's power» non si poteva
  rendere con «di» — darebbe «di il fratello volpe» — mentre `con` regge
  («Il contratto con il fratello volpe è scaduto»);
- le righe 7 e 12 hanno **inglese identico e giapponese diverso** (chi se ne va
  triste e chi decide di vivere solo): il giapponese le distingue, e vanno rese
  diverse.

💡 **Da rifare**: cercare altri file in perimetro che nessun elenco nomina.

## 2026-08-11 — «Welcome traveler!» è fuori da `lang()`

`main.hsp:227` è `msgtemp = " Welcome traveler! "`, il primo messaggio del log
all'ingresso nel mondo: **inglese anche nella build giapponese**, come le sette
intestazioni del diario. Toppata a mano.

Resa «Buon cammino!» perché sia «Benvenuto» sia «viaggiatore» concorderebbero
col giocatore, che non ha genere noto. Gli spazi ai due lati sono
nell'originale e restano.

## 2026-08-11 — Due simboli che non si possono usare, e uno che si può

- ⚠️ **`☆` non si usa**: CP932 lo scrive su due byte e la build inglese ne
  disegna uno per byte. Reso con **`♪`**, che ha la stessa funzione decorativa
  ed è l'unico due-byte che il gioco disegna davvero, come icona
  (`init.hsp:1385`). Stessa sorte per `～`, reso coi puntini;
- ✅ **il `♪` senza cifra dopo è sicuro nella build inglese.** `msg_write` legge
  il carattere successivo come indice icona; se non c'è, `mark` vale 0 e viene
  disegnata l'icona 0. Il ramo che interromperebbe (`init.hsp:1377`) è **solo
  quello giapponese**.

## 2026-08-11 — La creatura `@` non è traducibile, ed è una decisione

`CREATURE_ID_AT_SIGN` dice 「Ｑｙ＠」 in tutte e quattro le classi. Non esiste una
forma italiana perché non esiste una forma linguistica: qualunque resa sarebbe
inventata. Ma lasciarla identica all'inglese faceva **rifiutare il lotto
intero**, e l'unico modo di farlo passare sarebbe stato inventare qualcosa.

**Deciso: sezione nuova in `invariati.md`**, «Versi senza contenuto
linguistico», registrata in `_SEZIONI_INVARIANTI`. Il file non ammette default:
ogni sezione con valori va classificata, o `carica_invariati` alza `ValueError`.

⚠️ Non vale per la pecora: `Baa` ha un'onomatopea italiana propria (`Bee`). La
sezione è per ciò che non è lingua in nessuna delle due.

## 2026-08-11 — `_syujin` è la gemella di `_onii`, e la guardia era scritta sul nome sbagliato

`text.hsp:112` definisce `_syujin`: «Padrone» / «Padroncina», che cambia col
sesso del **giocatore** esattamente come `_onii`. La guardia sull'articolo,
scritta poche ore prima, cercava il solo `_onii` e avrebbe lasciato passare la
domestica.

Riscritta sulla famiglia — «gli appellativi che cambiano col sesso del
giocatore» — invece che sul caso che l'aveva generata.

## 2026-08-11 — La build si è rotta, e la prima spiegazione era falsa

`applica` si è fermata con «Accesso negato» rifacendo l'albero, lasciandolo
**incompleto**; `compila` poi accusava `#Error: in line 112 [main.hsp]`, che è
la riga dell'`#include "init.hsp"` e non dice niente della causa.

Causa verificata: le cartelle del clone portano l'attributo di sola lettura,
`copytree` lo copia su BUILD, e su Windows `os.rmdir` rifiuta una cartella con
quell'attributo **anche quando è vuota** (provato su una cartella temporanea).
Corretto con un handler in `applica.prepara_albero`, che tocca **solo BUILD**.

⚠️ **La prima spiegazione scritta nel commento era falsa e va ricordata come
tale**: diceva che quell'attributo *era* il modo in cui è tenuta la regola «il
sorgente non si scrive mai». Verificato: i **3.374 file del clone sono tutti
scrivibili**, solo le 34 cartelle hanno il flag, che su Windows è acceso quasi
ovunque. La regola la tengono la disciplina e il **manifesto SHA-256** —
ricontrollato dopo la correzione: **72 file su 72**.

Il primo fallimento, per onestà, l'ha causato una shell lasciata con la
directory corrente dentro l'albero di build.

## 2026-08-11 — L'inglese riscrive, e in cinque modi diversi

Tradotte ~410 battute, e la lingua ponte ha sbagliato in cinque forme distinte,
ognuna con una risposta diversa. Vedi [[l-inglese-non-traduce-riscrive]].

- **inventa**: `<Gwen>` ha un ♪ in *ogni* battuta e contenuti nuovi («that's a
  pretty flower» → «Eat flowers evil-doer!»); `<Mia>` ha filastrocche giapponesi
  sostituite da battute sui gatti; 「がぼぼぼ」 (il gorgoglio di chi affoga) →
  «I'm sorry I failed you»;
- **amplia**: 「ククク…」 del ladro, tre sillabe, diventa una frase di venti
  parole; 「お、カモだ…」 («oh, un pollo») diventa un paragrafo;
- **restringe**: la canzoncina di `<Mia>` diventa «Meow♪!»;
- **scambia**: `<Tam>` ha le prime due battute invertite;
- ⚠️ **cambia il personaggio**: la macchina delle pulizie è **infantile** in
  giapponese («spostatiii», «ho fame!») e **robotica** in inglese («Trash
  detected», «Battery low»). Ogni singola frase è plausibile: si vede solo
  guardando la creatura intera — un altro motivo per cui il lotto prende
  creature intere.

**Regola**: l'originale arbitra sul *significato*; l'inglese conserva il diritto
di *specializzare* quando sa qualcosa che il giapponese non dice (vedi 「がおー」
sopra). Se ha semplicemente messo altro, si scarta.

## 2026-08-11 — Un gioco di parole visivo si rifà su un altro canale

La recluta dice 「矢耐性かと思ったら失耐性だった」: il gioco sta in 矢 e 失, due kanji
che **si somigliano a vederli** — ha letto male, non sentito male. L'inglese l'ha
spostato sul suono (*nether* / *nerve*), che in italiano sono «oltretomba» e
«nervi» e non si somigliano affatto: tradurre la soluzione inglese avrebbe dato
una frase senza motivo.

**Reso con suono / sonno**: una lettera di differenza, e «Suono» è una
resistenza che **esiste davvero** (`text.hsp`, `Sound` → `Suono`), mentre
«sonno» è l'inciampo naturale. Il personaggio resta quello che l'originale
voleva — uno che confonde i nomi — e infatti nella battuta accanto sbaglia anche
il nome di una città. Vedi [[il-gioco-di-parole-cambia-canale]].

---

## 2026-08-12 — L'ultimo «nome da fare» stava su una riga commentata

`strumenti/estrai.py` non riconosce i commenti HSP: raccoglie anche le righe che
cominciano per `;`, che il compilatore non vede. Misurato incrociando le 27.813
voci estratte con la riga da cui vengono: **28 stanno su righe commentate**, di
cui **17 in `db_creature.hsp`**, e 4 cadevano nel lavoro che restava.

Una di quelle quattro era **l'unico `nome` di creatura ancora aperto**, e le
riprese lo portavano avanti da sessioni come «1 nome»:

```
105060  ; return lang("ハードゲイ", "hard gay")
105061    return lang("エクスプロージョマン", "explosioman")
```

La riga viva è la 105061, e `explosioman` era **già reso** «l'uomo esplosivo».
L'altra occorrenza di `ハードゲイ` (`:105098`) è anch'essa commentata: **zero
occorrenze vive**. Renderla avrebbe dato alla stessa creatura un secondo nome
italiano, e un nome già preso non si riusa. Le altre tre erano i versi
「フーーー」 dello stesso mostro, commentati in tutte e cinque le occorrenze.

**Deciso:** le quattro voci in `rinviate.jsonl` col motivo, non tradotte.
`estrai --da-tradurre` le toglie dai lotti, `verifica --dizionario` continua a
contarle fra le non tradotte — che è giusto: sono lavoro *escluso*, non lavoro
*chiuso*. **I nomi di `db_creature.hsp` risultano da qui chiusi.**

**Rinviata, e va rinviata apertamente:** far saltare i commenti a `estrai.py` è
la correzione giusta in astratto, ma sposterebbe la prova d'identità da
**27.813 a 27.785**, e quel numero è citato come firma dello stato buono in
`SPEC.md`, in `RIPRESA-sessione.md` e nelle attese di apertura. Cambiarlo di
soppiatto renderebbe illeggibile ogni confronto con le sessioni precedenti. La
decisione è **quando** pagarla, non **se**.

⚠️ Il controllo va fatto sulla **riga**, non sul contenuto: una stringa può
comparire in un commento e anche viva altrove. La domanda è se *tutte* le sue
occorrenze sono morte.

---

## 2026-08-12 — Quattro battute restano in inglese, perché il giapponese è inglese

Lo `<Spazzino di sotterranei>` (`db_creature.hsp:99788-99800`):

```
lang("「Target Acquired.」",      "Target Acquired.")
lang("「Resistance is futile!」", "Resistance is futile!")
lang("「Pwned!」",                "Pwned!")
lang("「wtf」",                   "WTF")
```

In un file dove **ogni** altra voce ha due forme diverse, l'identità dei due
slot è upstream che dichiara un'intenzione: la macchina parla inglese **anche al
giocatore giapponese**. È inglese da robot più gergo di rete — «Resistance is
futile!» è la citazione dei Borg, «Pwned!» è un refuso di *owned* diventato
parola, «wtf» è una sigla.

Il giocatore giapponese sente una macchina che parla **straniero**. Renderlo in
italiano gli farebbe parlare la lingua di chi legge, cioè l'opposto
dell'effetto voluto.

**Deciso:** le quattro in `invariati.md`, col motivo scritto per esteso. Stesso
criterio già usato per `user`, dove il giapponese identico all'inglese segnala
uno slot e non un nome.

⚠️ **Non vale per automatismo.** Nello stesso progetto un verso animale identico
nelle due lingue *va* reso, perché l'italiano ha la sua onomatopea: lì
l'identità è un caso, non una scelta. La prova è chiedersi se l'originale, letto
da chi lo parla, suoni estraneo **di proposito**.

⚠️ **Da rimettere in discussione con uno screenshot.** È la decisione della 27ª
che regge su un ragionamento e non su una prova: se a schermo, in mezzo a un log
italiano, quelle quattro righe stonano invece di caratterizzare, la riga di
`invariati.md` va tolta. `spawn_chara 32`.

---

## 2026-08-12 — L'inglese non riscrive soltanto: ricicla il repertorio di un'altra creatura

Sesto modo, che non era nei cinque della ventiseiesima. Le battute
dell'**erudito** (`76452`/`76458`/`76464`) — «P-please, no sir...», «You are
cruel.», «Ha ha ha!» — escono **identiche** in bocca a:

| creatura | righe | che cosa dice il giapponese |
|---|---|---|
| profugo degli Elea | `88274`-`88286` | ha fame, vuole rivedere la sua terra |
| viaggiatore | `88185`-`88197` | viene rapinato, chiede di smetterla |
| saggio della collina | `73911` | muore riconoscendo di non aver saputo abbastanza |
| pescatore | `90657` | impreca in parlata da porto |
| addetto del casinò | `88363`-`88375` | minaccia la tortura, chiama i buttafuori |

Cinque registri opposti, un solo testo inglese. ⚠️ Il rimedio contro «cambia il
personaggio» — prendere la **creatura intera** nel lotto — qui non serve, perché
anche l'insieme resta coerente con sé: chi traduce dall'inglese scrive cinque
volte lo stesso vigliacco senza mai insospettirsi.

**Misurato invece che scoperto un lotto per volta: 84 stringhe inglesi coprono
231 giapponesi diversi** in `db_creature.hsp`. `Huh?` da solo ne copre sei;
`Why are you doing this?`, `P-please, no sir...`, `You are cruel.`, `Ahhhh!`,
`Go to hell!`, `Stop it!` ne coprono cinque ciascuna.

**Deciso:** il raggruppamento per inglese entra nel metodo, prima di comporre il
lotto — non come guardia automatica (non c'è niente da bocciare: ogni resa è
legittima) ma come **elenco di righe su cui l'inglese non è una fonte**.
Resta aperta `102518`/`102524`/`102530`.

💡 **E funziona al rovescio.** La **guardia cittadina** (`98449`) e il
**guerriero mercenario** (`115178`) hanno le stesse quattro frasi giapponesi con
due inglesi diversi. Lì la regola si capovolge: non si reinventa, si **copia** la
resa già decisa, e la differenza dell'inglese è rumore. Stesso caso per
`<Carla> del Mondo Dimenticato` e `<Larnneire>`, che condividono tre battute.

⚠️ Ma `<Carla>` invoca `ザビ王`, non `ジャビ王`: viene da un altro mondo, e
l'inglese scrive «King Zabi» qui e «Xabi» per Palmia. **Sono due nomi**, e il
riuso del resto non autorizza a fonderli.

## Il blocco ad alta frequenza di Fase 4 non si anticipa in blocco (2026-08-12)

La 27ª aveva aperto la domanda: `buff.hsp`, `chara.hsp`, `item_func.hsp` e
`screen.hsp` sono ~830 firme che il giocatore legge a ogni partita e stanno in
coda a tutto, come `adv.hsp`. Anticiparle?

I numeri sono giusti, rimisurati tutti. Ma un conteggio dell'estrattore **non è
una stima di costo**, e per il file che portava l'argomento era metà della
verità: ogni messaggio di `buff.hsp` è spezzato in due elementi d'array e solo il
primo sta dentro `lang()`. Il secondo è un letterale nudo — 70 in quel file — e
il sito che ricompone la frase è un blocco custom del mod
(`chara_func.hsp:2316-2375`) che compone **solo nel ramo inglese**, con `_s()` e
sette casi speciali anch'essi scritti nudi. La riga originale con `lang()` è
commentata.

**Deciso, in tre parti:**

1. si anticipano **solo i ~90 `buffname`**: sono dentro `lang()`, non dipendono
   da nulla, e si vedono nel popup sopra la testa, in «The effect of X ends.» e
   nella lista dei potenziamenti della scheda;
2. i **`bufftxt`** diventano un lavoro **strutturale**, non un lotto di rese:
   prima una toppa che riporti il ramo inglese alla forma giapponese — frammento
   unico `name + bufftxt(0)`, via `_s()`, via i sette casi — poi le rese. Una
   toppa scioglie ~90 messaggi; novanta toppe sarebbero il modo sbagliato;
3. `chara.hsp`, `item_func.hsp`, `screen.hsp` e `main.hsp` **restano in Fase 4**
   finché non esiste un conteggio dei letterali fuori da `lang()` che sappia
   scartare percorsi, nomi di file e chiavi di `#define`. Senza quel filtro il
   loro costo è ignoto, e decidere l'ordine su un numero che non misura il costo
   è l'errore che questa decisione corregge.

⚠️ **E la motivazione della 27ª era inventata.** «I nomi degli status stanno
nell'HUD in permanenza» è falso: l'HUD disegna le **icone**. La frequenza è alta
per altre vie e la conclusione tiene, ma la prova no — corretta nella ripresa
dove era scritta.

💡 Due cose utili trovate misurando: `chara.hsp` costa molto meno del suo numero
(258 firme, 143 testi distinti, 87 dei quali la stessa frase), e `sdim` **non è
un tetto** — `skilldesc` è dimensionato a 40 e porta già una resa da 59
caratteri, vista a schermo.

## 2026-08-17 — L'articolo dentro il nome vale anche sulla carta, e a dirlo è stata una rete

Aprendo `db_card.hsp` (il nono punto cieco: 1.162 nomi di carta fuori dal
perimetro) serviva decidere se il nome della carta porta l'articolo come vuole
`contratto-nomi.md` §4.

**Il primo disegno lo toglieva**, e l'argomento sembrava buono: sulla carta il
nome non entra in una frase, è un'**etichetta** in testa a una riga di dati
(`tcg.hsp:1492`-`:1509`), e «la zanzara gigante  No.1142  Rare:Common» ha un
articolo che non regge niente. È la regola della `guida-stile.md`, «l'etichetta
si legge dove esce».

**Poi `reimporta` ha rifiutato il lotto: 52 voci, traduzione identica
all'inglese.** Senza articolo «lo yeek» diventa «yeek», «il troll» «troll», «la
medusa» «medusa». Cioè: **l'articolo era quel che rendeva italiana la resa.**
Passare il lotto avrebbe voluto dire scrivere 52 righe motivate in
`invariati.md` per nomi che non sono invariati per niente — e `invariati.md`
dice che una riga lì è una decisione da motivare. Cinquantadue motivazioni che
non esistono sono la prova che la decisione era sbagliata.

Con l'articolo, le identità che restano sono **26 e sono tutte già dichiarate**:
zero righe nuove.

⚠️ **E l'argomento che aveva convinto a toglierlo non reggeva al controllo.** Il
numerale del negozio delle carte — « 1 zanzara gigante» — sta dentro un elenco
`[Contains]` che è **prosa scritta a mano** in `tcg_custom.hsp` e non interpola
`cardrefn`: là il nome si scrive nudo perché lo scriviamo noi, e non c'entra con
quello che la carta porta. L'unico sito che il nome lo interpola davvero è la
voce di menu di `tcg_custom.hsp:1917`, e là l'articolo sta **meglio**: «Carta:
la zanzara gigante».

**Deciso:** il nome della carta porta l'articolo, come ogni altro nome di
creatura. **Deroga dichiarata** per le otto **terre** (`cardreftype = 30`) e le
due **magie** (`cardreftype = 20`): non sono creature, non entrano in nessuna
frase, e compaiono solo con « <Terreno>» o « <Magia>» appiccicato dietro.

💡 La lezione generale è sul metodo, non sull'articolo: **una convenzione che
obbliga a scrivere cinquantadue eccezioni è la convenzione sbagliata.** Il conto
delle eccezioni è un modo di scegliere fra due regole, e costa una prova.

## 2026-08-17 — `sdim` non è un tetto, e questa è la terza volta che serve dirlo

Misurando se il nome italiano della carta ci sta nella riga d'aiuto del tavolo
(`tcg.hsp:3506`, 680 px) serviva il nome di mossa più lungo, perché
`cardrefrace` porta dentro `skillname(cardrefattack)`. `skill.hsp:3` dichiara
`sdim skillname, 16, MAX_SKILL`, e sembra dire **quindici caratteri**.

Non li dice. HSP riespande la stringa in assegnazione, e questo documento lo
aveva **già misurato** in fondo alla decisione del 2026-08-12: «`skilldesc` è
dimensionato a 40 e porta già una resa da 59 caratteri, vista a schermo».

Contato adesso sulle assegnazioni vere: **47 nomi di mossa inglesi e 172
italiani superano i 15 caratteri**, e il massimo è 24 in tutt'e due le lingue.

⚠️ **E la deduzione sbagliata è stata fatta tre volte in due giorni**: dal lotto
`tcg_mod-001` della 53ª sul `sdim` di `cfname@tcg` («il tetto sta nel `sdim`, in
due punti, e vince il più stretto: **quindici**»), e due volte dalla 54ª. Regge
per caso quando la resa è corta.

**Deciso:** un tetto dedotto da un `sdim` è un'**ipotesi**, non un dato, e va
misurato contando le assegnazioni o guardando la geometria del disegno (i pixel
della finestra, il passo delle righe). ⚠️ Da riguardare con questo metro il
tetto delle schede dell'editor del mazzo, che la 53ª ha dedotto così.

## 2026-08-18 — Il nome della mappa: un tetto di 16 caratteri, e un salvataggio che lo congela

Il collaudo del pannello degli dei ha mostrato, in fondo alla schermata, la
barra che diceva «**La Terra della T**». Il nome della mappa non è una resa
sbagliata: è `screen.hsp:153`, che taglia.

    if ( strlen(mdatan(MDATAN_NAME)) > 16 - (maplevel() != "") * 4 ) {
        mes cnven(strmid(mdatan(MDATAN_NAME), 0, 16 - (maplevel() != "") * 4))
    }

**16 caratteri**, **12** se la mappa mostra il numero di piano — cioè Lesimas, i
nefia generati, le missioni e ogni mappa il cui `mdata(MDATA_TYPE)` sta fra
`MAP_TYPE_DUNGEON_MIN` e `MAP_TYPE_DUNGEON_MAX`. Il taglio è netto, senza
puntini, e si legge in **ogni schermata del gioco**.

⚠️ **Il tetto non si alza con una toppa.** Misurato sulla schermata: il passo è
7 px (Courier New a corpo 12, `12 + sizefix - en * 2`), il nome comincia a
`inf_raderw + 24` = x 161 e la prima piastrella di stato sta a
`inf_raderw + 148` = x 284. Sono 124 px, cioè **17 caratteri**: `strmid` a 16 è
già il massimo fisico, e alzarlo guadagnerebbe una lettera.

**Deciso:** un nome di mappa nuovo si scrive **entro 16 caratteri**, entro 12 se
quella mappa ha il piano. Il referto è `scratchpad/nomi_mappa.py`.

⚠️ **Ma il metro non è «sforare»: è «sforare dove l'inglese ci stava».** Su 197
nomi, l'inglese di monte ne taglia **46**. Sulle nefia generate — le mappe più
visitate del gioco — ne taglia **51 su 80**: «Beginner's Cave» diventa
«Beginner's C». Il taglio è una condizione di questo gioco, non un difetto della
traduzione. Il lavoro nostro erano i **60** dove upstream ci stava e noi no, e
sono stati accorciati tutti; l'italiano adesso ne taglia 44, due meno
dell'inglese.

### Il nome vive nel salvataggio, non nell'eseguibile

`map.hsp:1406` chiama `mapname()` solo quando la mappa viene **generata**. Da lì
in poi `mdatan(MDATAN_NAME)` viaggia con i dati della mappa: `system.hsp:2727`
lo scrive e lo rilegge come `mdatan_<area>_<100+livello>.s2`. Una mappa già
visitata **conserva per sempre il nome che aveva il giorno della prima visita**.

Misurato sul salvataggio di collaudo (21 mappe): `mdatan_4_101.s2` contiene
ancora `North Tyris` e `mdatan_11_101.s2` `Port Kapul` — visitate prima della
traduzione — mentre `mdatan_20_101.s2` contiene `la Terra della Tregua`, cioè
una resa italiana di una build precedente. **Il salvataggio è un museo di tutte
le build che ha attraversato.**

**Deciso: non si toppa.** La toppa ovvia — ricalcolare `mdatan` dal `mapname()`
dell'area quando la mappa si ricarica — **cancella i nomi buoni**: i sei piani
del «Palazzo Infero» stanno dentro `AREA_AMUR_CAGE` e il laboratorio biologico
dentro `AREA_VERNIS`, quindi diventerebbero «Gabbia di Amur» e «Vernis». E la
variante prudente («rinfresca solo mondo, città e villaggi») userebbe il tipo
dell'**area** mentre i nomi propri stanno su sotto-mappe che riscrivono il
proprio `mdata(MDATA_TYPE)`: è la trappola di misurare una cosa vicina.

Il conto dice che non vale il rischio: nel salvataggio di collaudo i nomi fermi
all'inglese sono **due**, perché le città sono nomi propri che non cambiano
(Vernis, Palmia, Yowyn, Derphy, Noyel, Lumiest, Eirel). Il congelamento morde
sui posti **descrittivi**, che sono esattamente quelli che la toppa non può
toccare.

💡 **La regola di collaudo che ne esce: un nome di mappa si può collaudare solo
dove il salvataggio non è ancora passato.** Chi verifica una resa nuova deve
andare in un posto mai visitato, o aprire una partita nuova. Guardare una mappa
già vista non prova niente — né in un senso né nell'altro.

### E un nome di mappa non è solo un nome di mappa

«Ranch in rovina», scritto oggi per 廃モンスター牧場, contraddiceva il **rogito
che compra quel posto**: `db_item.hsp:139803` dice «allevamento abbandonato», e
l'allevamento normale è «allevamento». Corretto in «Ex allevamento», che sta
sotto il tetto e resta nella stessa famiglia di parole.

⚠️ **Resta aperta la stessa frattura sul 収容所**: il rogito
(`db_item.hsp:134276`) dice «accampamento» mentre la mappa e i messaggi dicono
«campo di prigionia» — e `adv.hsp:197` parla di prigionieri da condurre lì, cioè
«accampamento» è la parola sbagliata, non solo una parola diversa.


## 63ª — Il sesso dichiarato vive nel salvataggio, e per ora non si tocca

`chara.hsp` è stato aperto e chiuso quasi tutto (258 firme, 254 rese). Le
**quattro** che restano sono una famiglia sola, e non sono state lasciate per
stanchezza: sono una decisione da prendere con gli occhi aperti.

    chara.hsp:2790   lang("両性具有", "hermaphrodite")   -> CDATAN_NEWSEX
    chara.hsp:3631   lang("自称男性", "male?")           -> menu, poi zisyousex
    chara.hsp:3632   lang("自称女性", "female?")         -> menu, poi zisyousex
    chara.hsp:4390   lang("なし", "none")                -> CDATAN_NEWSEX

### Perché non basta tradurle

`cdatan(CDATAN_NEWSEX, …)` **finisce nel salvataggio**, ed è la stessa forma
del congelamento di `mdatan` scoperto nella 62ª: quel che è scritto lì dentro
resta com'era al momento della creazione, per sempre. E non è solo un dato da
mostrare — lo **confrontano** due posti in altri file:

- `init.hsp:2089` (`gendername`): se il valore è `lang("なし", "none")` mostra
  «sconosciuto», altrimenti **restituisce la stringa così com'è**;
- `command.hsp:3639`-`:3656`: sei rami che confrontano il valore con sei
  letterali e, quando ne trovano uno, appendono lo **stesso** letterale alla
  riga dell'elenco alleati in modo `Rank.`.

Da qui i tre casi, che sono diversi fra loro:

1. **`none` non si traduce mai.** È una chiave pura: nessuno la mostra —
   `gendername` la intercetta e stampa «sconosciuto» al suo posto. Tradurla
   spegnerebbe l'intercettazione e a schermo comparirebbe la chiave.
2. **`hermaphrodite` si potrebbe tradurre subito.** `gendername` lo mostra
   verbatim, e l'unico confronto (`command.hsp:3639`) cerca `"bisexual"`, che
   **non è la stessa parola**: in inglese quel ramo non scatta già oggi. ⚠️ In
   giapponese sì — sono tutt'e due 両性具有 — quindi è un guasto della sola
   build inglese, di monte, non nostro.
3. **`male?` e `female?` sono il caso vero.** Vanno in `zisyousex` e da lì in
   `CDATAN_NEWSEX`. `gendername` li mostra verbatim, quindi tradurli fa bene
   alla schermata principale; ma `command.hsp:3651`/`:3654` cercano `"male?"` e
   `"female?"`, e se non li trovano quella riga resta **senza il sesso**.
   Tradurre da tutt'e due le parti rimette a posto le partite nuove e lascia
   indietro quelle vecchie, che nel salvataggio hanno la parola inglese.

### Che cosa serve per chiudere

Una schermata: l'elenco degli alleati in modo `Rank.` (`allyctrl == 6`), con un
personaggio che abbia un sesso dichiarato. Serve a misurare **quanto pesa**
quella riga prima di scegliere se accettare la rottura sulle partite vecchie —
la lezione della 55ª: un referto dice che una riga esiste, solo lo schermo dice
quanto pesa.

💡 E c'è un dato che il conto già dà: 性別不明 è **già** reso «sconosciuto» in
`command.hsp:3643` e in `init.hsp:2090`, e la voce di `chara.hsp:3634` è stata
resa così nella 63ª proprio per non aprire una terza variante. La famiglia è
quindi già mezza decisa: quel che manca è solo il pezzo che attraversa il
salvataggio.


## 64ª — Gli epiteti si traducono, e vivono fuori dai sorgenti

Il collaudo della creazione del personaggio ha aperto la finestra «Scelta
dell'epiteto» e l'elenco era **tutto inglese**: `Retard Tank`, `Corrupted Wolf`,
`Dusk of Copper`, `Axe wielding Serpent`. L'unica riga italiana era
«Risorteggia», che è una `lang()` come le altre.

### Perché nessun referto l'aveva visto

`etc.hsp:335` non ha letterali: **carica il vocabolario da un file dati**.

    noteload exedir + lang("data\\ndata.csv", "data\\ndata-e.csv")

Il file è `C:\Games\Elona\elonaplus2.31\data\ndata-e.csv`, 365 righe e **950
parole distinte**, e non sta nei sorgenti HSP. È il **quindicesimo punto cieco**
e il primo di una famiglia nuova: fino a oggi ogni punto cieco era una forma di
riga che gli strumenti non guardavano — un `if ( en )`, un ramo `jp`, una
tabella, un commento di blocco. Questo non è una riga: è **un altro file**, e
tutti gli strumenti del progetto leggono `.hsp`.

⚠️ **E non è solo l'epiteto del giocatore.** `random_title()` genera anche il
nome di **ogni avventuriero PNG** (`adv.hsp:225`), il nome della squadra
(`command.hsp:17527`), il nome di certe mappe (`chat.hsp:22497`), i PNG delle
nefia speciali (`custom_nefiatypes.hsp:505`) e altri due siti in `action.hsp`.
È inglese che si legge di continuo, non una schermata sola.

### La decisione: si traduce

Un epiteto generato non è un nome proprio: è un **nome comune composto**, della
stessa identica classe di «a cursed bronze helmet» — che il progetto traduce già,
con l'accordo di genere e le qualifiche in coda. Lasciarlo in inglese sarebbe
incoerente con la scelta più vecchia del progetto. Yerles e Larnneire restano
inglesi perché sono nomi propri; «Lupo corrotto» non lo è.

### La grammatica, provata e non dedotta

`etc.hsp:399-505`, ramo non giapponese:

    1. parola1 = una colonna a caso (rnd(14)) di una riga a caso
    2. se parola1 sta nelle colonne 0-1, cioè è un sostantivo:
         1 su 6         ->  parola1 + " of"          «Dusk of Copper»
         se no, 1 su 6  ->  "the " + parola1, FINE   «The infinity»
    3. parola2 = colonna 0 o 1 (sempre sostantivo) di un'altra riga, di
       categoria diversa (colonna 14; l'eccezione è 万能, il jolly)
    4. risultato = parola1 + " " + parola2           «Corrupted Wolf»
    5. da 28 caratteri in su si ributta tutto e si rifà

⭐ **La prova non è un ragionamento: sono i sedici epiteti veri** della schermata
di collaudo, che `scratchpad/epiteti.py` scompone nella griglia **16 su 16**. È
la regola della 61ª — gli strumenti si provano dove si sa già che cosa deve
venire fuori — applicata a una grammatica invece che a una misura.

### Perché non basta tradurre le parole

L'inglese mette il **modificatore prima della testa**; l'italiano lo mette dopo,
e lo accorda:

    Corrupted Wolf        ->  Lupo corrotto        aggettivo accordato
    Elegance Fairy        ->  Fata dell'eleganza   nome + preposizione articolata
    Dagger Ring           ->  Anello del pugnale
    Dusk of Copper        ->  Crepuscolo di rame   qui l'ordine è già giusto
    Coolness of Curse     ->  Freddezza della maledizione
    The infinity          ->  L'infinito           articolo, non «the»

⚠️ Nella forma «A B» la testa è **B**; nella forma «A of B» la testa è **A**.
Sono due ordini diversi, e una toppa che ne applicasse uno solo produrrebbe
mostri a ogni schermata.

Quindi il vocabolario italiano deve portare **più di una forma per parola**:

    sostantivo    forma nuda | genere | forma preposizionale
                  lupo|m|del lupo      eleganza|f|dell'eleganza      rame|m|di rame
    modificatore  maschile | femminile
                  corrotto|corrotta    abominevole|abominevole

e `etc.hsp` va **toppato** perché componga all'italiana: scegliere la testa
secondo la forma, accordare il modificatore al genere della testa, e mettere
l'articolo nella forma «the».

### Il piano, in tre pezzi

1. **Il vocabolario**: 950 parole in `dati/ndata-i.csv` dentro il repo, nella
   griglia 365×15 di monte, con i campi separati da `|`. È un lotto lungo ma
   ordinario — 581 sostantivi col genere, 401 modificatori con due desinenze.
2. **La toppa a `etc.hsp`**: legge `data\\ndata-i.csv` invece di `ndata-e.csv`
   (così il file originale del gioco resta intatto, come `cgx-test.exe` non
   sovrascrive `elonapluscgx.exe`), spezza sui `|` e compone nell'ordine
   italiano. ⚠️ E alza il limite dei 28 caratteri, che in italiano taglierebbe
   troppo: la finestra degli epiteti è larga 400 col testo a `wx + 64`, cioè
   **45 caratteri**, e 34 sta comodo.
3. **La catena**: il file dati va copiato nell'installazione insieme
   all'eseguibile. Oggi quel passo non esiste — `installa.py` non è mai stato
   scritto e l'eseguibile si copia a mano — quindi è il momento di scriverlo.

⚠️ **Il pezzo 2 è quello che va provato per primo e sull'inglese**, come vuole la
61ª: una toppa che compone si prova rigenerando gli epiteti inglesi e
verificando che escano identici a quelli di oggi. Se la toppa non sa riprodurre
l'inglese, non è pronta per l'italiano.

## 67ª — Una scena dove l'inglese ha riscritto la battuta, e un contatore letto male

Il lotto `chat-002` chiude il perimetro `18560`-`18720` di `chat.hsp`: le otto
battute dello scontro finale con Orphe e la scena dell'anniversario. Trentatré
rese, e in tre punti le due lingue di monte non dicono la stessa cosa.

### ⭐⭐⭐ La scena dell'anniversario: l'inglese ha buttato via il gioco di parole

`chat.hsp:18720`-`:18785` è la scena che parte se `kinenflag == 1`: il compagno o
la compagna chiede «…今日は何の日？», e le risposte del giocatore sono cinque voci
di `chatList`. La terza — 「えーとアレだよアレアレ」, «ecco, è quella cosa, quella cosa lì,
quella lì» — apre un **secondo** menu, che in giapponese è tutto lì:

    chatList 0   「アレ！」    quello!
    chatList 1   「コレ！」    questo!
    chatList 2   「ソレ！」    codesto!
    buff         「…どれ？」   …quale?

È una gag di dimostrativi: il giocatore non si ricorda niente e continua a
indicare. **L'inglese l'ha sostituita con tre battute diverse** — «I do not
remember...», «Please give me a hint.», «By the way, the weather is nice today.»
— e con «So what?» al posto di «…どれ？», che scollega la domanda dalle risposte.

L'italiano ha i tre dimostrativi e la gag ci sta intera: «Quella lì!», «Questa
qui!», «Quella là!», con «…E quale?» a chiudere. Si è seguito il **giapponese**,
e non è una preferenza di gusto: la risposta del PNG a tutte e tre è la stessa
(「もういい。」 + `(呆れている)`), e regge solo se le tre voci sono la stessa non
risposta detta tre volte. Con le tre battute inglesi, che sono tre cose diverse,
la reazione unica non ha più un perché.

💡 È lo stesso verso della 66ª — «nursing a lowly adventurer» dove il giapponese
non ha nessun «lowly» — ma un passo più in là: lì l'inglese aveva **aggiunto**,
qui ha **sostituito**. Il segnale è sempre lo stesso: quando la reazione del
gioco a più scelte è una sola, le scelte sono variazioni di una cosa sola, e una
lingua che le rende tutte diverse ha perso la struttura.

### ⚠️ 一柱 non è «one pillar»

`chat.hsp:18590`, Orphe che vede arrivare Tezcatlipoca:

    jp  全ての神々の力を一柱に集中してきたか
    en  So you've concentrated the power of all the gods into one pillar

一柱 è il **contatore** delle divinità — «una divinità», come 一人 è «una
persona». L'inglese ha tradotto il carattere invece del contatore, e ne è uscito
un pilastro che nella scena non c'è: quel che è appena successo è che gli dèi
hanno concentrato la loro forza in **un dio solo**, che sta in mezzo allo
schermo. L'italiano dice «in una divinità sola».

⚠️ Il contatore compare anche due righe sopra, a `:18567`: 「一柱ずつ、目の前でくび
り殺してやろう」, e lì l'inglese lo rende giusto («One by one, I'll snuff them
out»). Stessa parola, due righe di distanza, due letture diverse: **la lettura
buona e quella cattiva convivono nello stesso blocco**, quindi non basta fidarsi
del fatto che l'inglese altrove ci abbia preso.

### La regola del genere, di nuovo, e stavolta su una risposta del giocatore

Quattro righe su trentatré hanno dovuto cambiare costruzione per non scegliere un
genere:

    :18591  «trascinato in una partita»  →  «che tocchi anche a te una partita»
    :18591  «non saresti mai dovuto arrivare» → «non era previsto che arrivassi»
    :18771  「ごめん寝ぼけてた」  →  «Scusa, ho ancora il sonno addosso»
    :18765  「悲しくなった」      →  «ci rimane male»

⭐ Le prime due stanno nella **stessa battuta**: `Irregular, what a pity...` ne
porta due participi di fila, ed è la battuta che il nemico rivolge al giocatore
nell'ultima scena del gioco. ⚠️ E `:18771` è la prima volta che il vincolo morde
su una voce di `chatList`, cioè su una frase che il giocatore **dice**, non che
riceve: «ero mezzo addormentato» è la resa ovvia di 寝ぼけてた e non si può
scrivere. La forma che regge è quella che sposta il predicato su un sostantivo —
«ho ancora il sonno addosso» — ed è la stessa mossa delle etichette di stato.

---

## 71ª — L'accento in mezzo alla parola, e tre segnaposto classificati male

Due reti nuove, nate tutt'e due da una riga che stavo per scrivere e non da un
sospetto generico. Le racconto insieme perché hanno la stessa forma: **una
regola vera che il progetto conosceva e non aveva mai messo in una guardia**.

### 1. La degradazione regge solo sull'ultima lettera

`accenti.degrada()` sostituisce ogni vocale accentata con vocale + apostrofo,
perché CP932 non codifica `à è é ì ò ù`. Funziona perché in italiano l'accento
cade quasi sempre sull'**ultima** lettera, e lì l'apostrofo è quel che la lingua
scrive comunque: `piu'`, `citta'`, `perche'`.

⚠️ **Ma «dèi» diventa «de'i» e «élite» diventa «e'lite».** È la lezione della
41ª (2026-08-14), che si chiudeva con *«si evita la parola, non si toglie
l'accento»* — e per trenta sessioni è rimasta una cosa da ricordarsi.

Stavo per scrivere «gli dèi» in una resa di `talk.txt` e mi sono fermato a
chiedermi che cosa ne facesse `degrada`. Poi ho misurato il dizionario intero:
**quindici occorrenze**, tutte scritte *dopo* la 41ª, fra cui **sei nomi di
mossa** in `proc.hsp` che il giocatore legge a ogni uso — `<Soffio degli dèi
creatori>`, `<Ruggito degli dèi guerrieri>`.

💡 **Nessuno dei tre controlli esistenti poteva vederle**, e il motivo è
istruttivo: la forma degradata «de'i» CP932 la scrive benissimo, quindi
`doppi_byte_cp932` e `non_ascii_residuo` tacciono; e
`ha_apostrofo_scritto_a_mano` guarda il **lotto**, dove l'accento è scritto
giusto. Il difetto non è un carattere: è **dove cade**. Una guardia che chiede
«questo carattere si può scrivere?» non risponde alla domanda «questa parola si
legge?».

La correzione è `dei`: l'accento grave serve solo a distinguerlo dalla
preposizione, quindi si toglie senza cambiare parola. Adesso c'è
`accenti.accenti_interni()`, agganciata a `verifica.py` e a `dati_verifica.py`,
e un test che gira su tutto il dizionario.

### 2. `{you}` e `{me}` escono in giapponese anche nella build inglese

`AAREA,30|4` è l'unica riga inglese di `talk.txt` che porta `{you}`. Prima di
tradurla sono andato a vedere che cosa ci mette l'espansore: `_kimi(3)`,
`text.hsp:5329`. E quella funzione — come `_ore(3)` per `{me}`, `:5851` — **non
ha nessun `lang()`**: ottantasei righe di `if ( cdata(CDATA_TONE, tc) == n )`
che scelgono fra 貴方, お前, 君, 私, 俺, 僕 secondo il tono del parlante, in
qualunque lingua.

⚠️ **Non è un difetto nostro: è di monte, e si vede nella sua build inglese.**
Un mese l'anno, nel rifugio, un cittadino dice «We're almost out of food. お前,
share some of yours with us.»

Erano classificati come **contenuto** in tutt'e due gli espansori. Non lo sono,
ma non sono nemmeno conversioni giapponesi da rifiutare: sono una terza
famiglia, `Espansore.da_togliere`, e il confronto sui segnaposto li **sottrae
all'inglese** invece di pretenderli nella resa.

### 3. E allora ho guardato gli altri tre nomi latini

`_GIAPPONESI` conteneva `onii`, `syujin`, `sex`. Nessuno dei tre era al posto
giusto, e in due modi diversi:

| nome | sito | che cosa fa davvero |
|---|---|---|
| `{sex}` | `text.hsp:7057` | `lang("男", "boy")` — è **contenuto**, ed è già tradotto |
| `{onii}` | `text.hsp:7030` | ramo `else`: `"brother"` / `"sister"`, letterali **fuori** da `lang()` |
| `{syujin}` | `text.hsp:7050` | ramo `else`: `"master"`, idem |

`onii` e `syujin` non escono in giapponese: escono in **inglese**, anche in
build italiana, perché il dizionario non arriva a un letterale nudo. Sono
`_INGLESI_NUDI`, con un messaggio che dice questo — e sarebbero toppabili, se
mai un inglese di monte li usasse (oggi nessuno lo fa, né in `talk.txt` né in
`board.txt`).

Le diciotto conversioni kana sono state ricontrollate una per una: zero `lang()`
e zero rami `if ( jp )` nel corpo. Quelle stavano bene dov'erano.

💡 **La lezione di metodo:** la classificazione era stata scritta guardando i
**nomi** — `onii` e `syujin` *suonano* giapponesi, `you` e `me` *suonano*
inglesi — invece dei **siti**. È la regola della 61ª (*misura la cosa, non una
cosa vicina*) applicata a una tassonomia: cinque nomi su cinque erano nella
casella sbagliata, e tre di loro erano esattamente al contrario.

### 4. `{sex}` porta il dimostrativo, e la colpa è di un altro file

`{sex}` rende `lang("男", "boy")`, che ha la **stessa firma** di `_sex2`
(`text.hsp:110`). E `_sex2` lo usa `proc.hsp:3290` dentro «C-con quel ragazzo
era solo una cosa di letto», dove il dimostrativo dev'essere dentro la parola
perché *quel* e *quella* non si possono scrivere fuori.

Quindi in italiano `{sex}` vale **«quel ragazzo» / «quella ragazza»**, e una
resa che lo usasse come vocativo direbbe «che bel quel ragazzo che sei».

È la 63ª — *una stringa in due siti, e una decisione presa guardandone uno rompe
l'altro* — ma senza la via d'uscita di allora: lì bastava un due punti nella
giuntura, qui la giuntura è dentro una funzione che sceglie fra due generi. La
resa gira intorno all'ostacolo mettendo `{sex}` in **terza persona** («quel
ragazzo mi piace proprio»), che in italiano è anche un modo di corteggiare.
È la 64ª: *esiste una costruzione che non chiede quello che non posso dare?*

### 5. Il rinvio che si è chiuso da solo

Le due voci di `" guest"` in `text.hsp` erano rinviate dalla 69ª con un motivo
che diceva **quando** riaprirle: «va tradotta INSIEME a `talk.txt`». Il lotto
002 ha reso `MAID|1` — proprio la frase che le incornicia — e la condizione era
soddisfatta.

La resa non traduce «guest»: lo **toglie**. `{ref}` diventa il numero nudo, cioè
lo stesso che già rende il ramo giapponese, e il sostantivo passa nella frase:

    Eccoti a casa, {player}! Ospiti in attesa: {ref}. Li ricevi subito?

💡 Così il plurale **sparisce** invece di essere risolto: «Ospiti in attesa: 1»
regge come «: 3», mentre ogni resa che porti il sostantivo dentro `{ref}` sbaglia
su uno dei due casi. `text.hsp` non ha più nessuna `lang()` scoperta.

## 75ª — `*chat_default`: cinque famiglie, tre generi vietati, e una toppa ritirata

### 1. Perché la correzione di `economy.hsp:357` è stata ritirata

Aprendo il lotto della gestione della città ho notato che la statistica 発言力
(`MDATA_CITY_AUTHORITY`) aveva **tre nomi** nel dizionario: «punti autorità»
(`action.hsp:8506`), «autorità» (`chat.hsp:19563`) e «Influenza» nel pannello
della città (`economy.hsp:357`). `glossario.md:356` fissa «autorità» e **nomina
`economy.hsp` per nome**, quindi sembrava una violazione: l'ho corretta.

Non lo era. `strumenti/tests/test_colonne_economy.py` esisteva da prima, e il
suo docstring dice testualmente:

> è la stessa ragione per cui la resa di `:357` è «Influenza» e non
> «Autorita'»: un'etichetta accentata costringe a contare l'imbottitura su una
> cosa che il file non mostra.

Il prospetto allinea le colonne con gli **spazi**, e `applica` degrada «à» in
«a'», che è **due caratteri**: l'imbottitura giusta si conta su una forma che il
dizionario non mostra. La scelta era deliberata, scritta e sotto test.

💡 **La regola che ne esce: prima di correggere un sito si cerca chi lo
sorveglia.** Il glossario dice *quale parola*, un test può dire *perché lì non
si può*. Cercare il primo senza cercare il secondo produce una correzione che
sembra ovvia ed è sbagliata.

⚠️ **E il difetto di partenza resta aperto**: due nomi sullo schermo per la
stessa statistica, e il giocatore apre le due schermate nella stessa sessione.
Nessuna rete lo vede — `gemelle` confronta le firme e 発言力 sta dentro tre frasi
diverse. Chiuderlo vuol dire trovare un **sinonimo senza accento** per la
colonna, non rimettere l'accento.

### 2. Il genere non si conosce, e non è sempre lo stesso soggetto

`guida-stile.md` vieta l'aggettivo e il participio riferiti al giocatore. Oggi la
regola è scattata su **tre soggetti diversi**, con tre vie d'uscita diverse:

1. **Il giocatore** — la via d'uscita è il **nome predicativo**, che non
   accorda: «sei una mezza calzetta», «un pezzo di merda come te», «Che
   schiappa!», «la fortuna qui è TUA» invece di «il fortunato sei tu».
2. **Il parlante.** `chat.hsp:22654` (`chatval == 107`) non ha nessun ramo su
   `CDATA_SEX`, quindi il capo del Dock può essere uomo o donna: «quando sono
   arrivato io» sarebbe sbagliato metà delle volte, e si dice «ai miei tempi».
   Nel blocco accanto (`:22618`) il ramo c'è, e lì il parlante si accorda.
3. **L'oggetto.** `itemname(ci)` può essere «la pozione» o «il mantello»: «becomes
   lighter» non è «diventa più leggero» ma «**perde peso**», e «becomes heavier»
   è «**prende peso**» — verbo e nome, che non accordano.

💡 E le espressioni del volto girano sul **nome**: «ha l'aria abbattuta», «fa una
faccia sorpresa». L'accordo cade su «aria» e «faccia», che sono parole nostre.

### 3. La finestra del dialogo ha un tetto, e non è una troncatura

`chat.hsp:25226` manda a capo `buff` a **53** caratteri; `:25728` disegna la
prima riga a `wy+43` col passo di 19 px; `:25161` fa risalire i bottoni dal
basso, da `wy + wh - 56`. Con `wh = 380` le righe che ci stanno sono

    (324 - bottoni * 19 - 43) // 19

cioè 13 con un bottone solo, 12 con due, 11 con tre, 8 con sei. ⚠️ **Chi sfora
non viene tagliato: si sovrappone al menu**, e una rete di soli tetti non lo
troverebbe comunque.

Il simulatore esatto di `talk_conv` esiste dalla 54ª in
`scratchpad/chat_righe.py` — e non è un `textwrap`: taglia sugli spazi, quindi
una parola più lunga della riga **sfonda** invece di spezzarsi. Ma il suo
perimetro sono le 29 descrizioni di `cardsetdesc@tcg`. Farne una rete vera, con
il perimetro su tutti i `buff = lang(...)`, è lavoro ancora da fare.

### 4. I `chatval` sono numeri locali, non identificatori

`32` è «chain» nel menu dei materiali del fabbro e il **portafoglio smarrito**
dentro `*chat_default`. Uno strumento che mappa `chatval` → voce di menu
cercando la prima `chatList` del file con quel numero risponde con la voce
sbagliata, e per un quarto d'ora ho creduto di avere davanti un lotto «i
materiali» che non esisteva. `scratchpad/chatval-mappa.py` adesso cerca solo
dentro il menu che porta davvero a quei blocchi (`chat.hsp:19320`-`:19880`).

💡 È la famiglia della 74ª — *un buco nel perimetro non produce un numero
sbagliato, produce un numero che non c'è* — con una variante: qui il perimetro
era giusto e a essere sbagliata era la **chiave**.


## 76ª — Un menu si buca da solo: la rete `bilingui`, e due difetti nella rete che misura i menu

### 1. La firma è condivisa, quindi la schermata non è l'unità che si controlla

La 73ª aveva stabilito che **un menu si traduce intero o non si traduce**: le
voci di `chatList` che stanno una sotto l'altra sono una schermata sola, e
tradurne tre su quattordici la porta da inglese e coerente a metà italiana e
incoerente. La guardia però viveva dentro `gemelle.annota_menu()`, che misura
quanto di un menu copre **un lotto**, mentre il lotto si prepara.

Non basta, e la ragione è che il dizionario è indicizzato per **firma**
(giapponese + inglese + espressione), non per sito: la stessa firma vive in più
punti del file. Tradurre una voce in un menu ne traduce **un'altra altrove**.
Nella 76ª è successo tre volte in un giorno:

1. il «No.» di `chat.hsp:24653` — l'offerta di accompagnarti a cercare qualcuno
   — ha la firma del «No.» di `:6277`, che sta nel menu di conferma del
   **venditore di Jure a Noyel**, tutto inglese: tradurre l'uno traduceva
   l'altro, e la scena di Jure è dovuta entrare nel lotto **intera**;
2. «Use Light of Memory.» a `:1327` (menu a metà) non si poteva chiudere senza
   **aprirne un altro**: la stessa firma sta a `:1268`, nel menu dell'altro
   Loyter, che era tutto inglese. Qui il verso è opposto — una rete verde
   sarebbe diventata rossa per una riga che non avevo toccato;
3. 「習得する」 e 「訓練する」 di `:24954` stanno anche a `:390` e `:396`, dentro
   la schermata dell'allenatore «a prezzo d'amico».

Quindi la domanda giusta non è «questo lotto copre il suo menu?» ma **«dopo
questo lotto esiste un menu a metà?»**, e si può fare solo al file intero.
`strumenti/bilingui.py` la fa: elenca i gruppi di `chatList` con almeno una voce
resa e almeno una no. Alla nascita, **quindici** in `chat.hsp`; chiusi tutti
nella stessa sessione. È la quindicesima verifica d'apertura, attesa **0**.

⚠️ **Il limite è dichiarato nella docstring**: i menu si raggruppano per
**distanza** (`gemelle.blocchi_menu`, sei righe). `chat.hsp:24945` — il bottone
«Allenare» dell'addestratore — sta sedici righe sopra i suoi fratelli e finisce
in un gruppo suo. La rete sbaglia **per difetto**: può tacere su una schermata
rotta, non può inventarne una.

### 2. Tradurre codice morto non è gratis

`chat.hsp:19327` e `:19334` sono righe **commentate** a monte
(`// chatList 84, ...`): la variante lunga di due voci vive, con la coda
`[Total EXP 200%, Satiety increase halved]`. Le avevo tradotte con l'argomento
«tanto non costa niente», ed è costato: **una voce tradotta entra in
`menu_dialogo.voci_di_menu()`**, perché quella rete legge il dizionario. Così la
coda inglese da 74 caratteri è finita nel registro delle voci **rotte a monte** e
la resa italiana da 61 fra le voci **fuori misura** — due numeri veri su una riga
che non disegna niente.

Sono andate in `rinviate.jsonl` (73 → 75) con la condizione scritta («il giorno
in cui monte togliesse il commento»), come le tre voci del blocco `ORIGINAL`
spento di `command.hsp`. E `bilingui` conta le **rinviate come fatte**:
altrimenti l'unico modo di chiudere quel menu sarebbe tradurre codice morto, che
è esattamente quel che il rinvio esiste per non fare.

### 3. Due difetti in `menu_dialogo.reso()`, e uno era travestito da difetto di monte

`reso()` riduce un'espressione HSP alla forma che arriva a schermo: tiene i pezzi
letterali e conta ogni valore interpolato come quattro cifre.

- **`_INTERPOLAZIONE` non ammetteva un `+` dentro il valore.**
  `chat.hsp:24715` interpola `limit(cdata(CDATA_LEVEL, CHARA_PLAYER) / 2 + 5, 6,
  130)`: il pezzo non veniva riconosciuto, `reso()` restituiva l'espressione
  **intera** — virgolette, nome della funzione, argomenti — e la voce del
  catalogo degli schiavi risultava lunga **84** caratteri invece di 24.
  ⚠️ **Da fuori non si vedeva un difetto della rete**: si vedeva una voce «fuori
  misura» che si salvava per «già rotta in inglese», perché l'inglese ha la
  stessa forma e sbagliava allo stesso modo. 💡 È la 70ª — *una rete puntata sul
  file sbagliato non tace, mente* — nella forma in cui il metro sbaglia **su
  tutt'e due i lati del confronto**, e quindi il confronto lo assolve.
- **Un valore interpolato può stare in testa o in coda.** `_INTERPOLAZIONE`
  cerca un valore **fra due letterali**, quindi non vedeva né
  `cdatan(CDATAN_NAME, tc) + " lascia..."` né `"Catalogo A: max Lv. " +
  limit(...)`. Due regex nuove chiedono un `+` prima o dopo la virgoletta, che è
  quel che distingue un'espressione da una **statica**: `\"Miao?\"` e `città`
  non hanno nessun `+` e restano intatte.

### 4. Un test che filtra un referto vuoto non prova niente

`test_le_voci_del_pannello_dei_ci_stanno_tutte` e
`test_le_due_leggi_della_citta_ci_stanno` scrivevano
`[v for v in fuori_misura() if v["file"] == "god.hsp"]`, ma `fuori_misura()`
restituisce **tuple**. Passavano da sempre perché un ciclo su zero elementi non
indicizza niente: sono morti di `TypeError` il giorno in cui la rete ha trovato
una voce fuori misura **in un altro file**.

💡 La regola: un test che filtra un referto per tenersi solo la sua parte è verde
finché il referto è vuoto, cioè finché non serve. Va provato almeno una volta con
il referto pieno — o scritto in modo che il filtro non possa essere l'unica cosa
che lo tiene in piedi.

### 5. Un menu che nomina la stessa scelta di un messaggio dice le parole del messaggio

I dieci medium con cui si lancia una magia (`chat.hsp:8934`-`:8943`) sono le
stesse dieci cose che `text.hsp:139`-`:148` racconta a ogni lancio: «lancia un
incantesimo», «sputa ragnatele», «spruzza fluidi corporei», «dispiega un cerchio
magico», «scaglia un pensiero maligno». Il menu che chiede *quale medium* usa
quelle parole. È la regola della 73ª — due schermate che mostrano la stessa
scelta dicono le stesse parole — applicata a un menu e a un **messaggio**
invece che a due menu.

💡 E l'inglese qui non era la guida: 音声 (*voce*) l'inglese lo chiama «spell»
perché il messaggio dice «casts a spell». Le due strade portano allo stesso
posto, «Incantesimo», ma solo perché il messaggio era già tradotto.

## 80ª — Leold: due volte l'inglese contro se stesso, e una decisione rimasta aperta

Il sistema di Leold (`chat.hsp:16645`-`:18001`) vende AP: slot d'equipaggiamento,
velocità, Vita, talenti, tecniche, risvegli del compagno. Novanta rese, zona
chiusa (zero firme con occorrenze fuori), `bilingui` zero al primo giro.

### 1. Il lessico non si è deciso: stava in un pannello già tradotto

Ogni voce di questi menu vende un `CHARA_BIT_AWAKE_*` o uno `SKILL_SPACT_*`. Un
`grep` sul nome della **variabile** — non sulla stringa (79ª) — porta in venti
righe al pannello dei talenti di `command.hsp:2355`-`:2452`, dove ognuno di quei
bit ha già la sua frase italiana: «Il fascino stordisce chi attacca in mischia»,
«L'orgoglio cresce col pericolo», «La forza nascosta cresce col pericolo», «La
barriera annulla i danni», «Cura tattica appresa», «Maledizione tattica
appresa», «Preferenza per la mischia / per il tiro / per le magie a freccia».
I nomi dei menu sono i sostantivi di quelle frasi. Le cinque tecniche del
giocatore vengono da `skill.hsp` (`skillname()`), e la cornice «Hai imparato una
nuova capacità: X.» era già resa in tre file per altre costanti.

💡 **Notevole quanto poco restasse da inventare**: su novanta rese, i venti nomi
propri del sistema erano tutti già scritti da qualche parte, e nessuno di essi
sarebbe stato segnalato da una rete se l'avessimo scelto diverso — sarebbe stato
italiano corretto, dentro il tetto, non bilingue.

### 2. ⚠️⚠️ L'inglese di monte sbaglia un PREZZO, e il giudice è il codice

`chat.hsp:17864` etichetta 可変放射 «Variable Breath (**300**AP)». Il giapponese
dice 消費AP**400**, e `:17925` fa `leoap = 400`. Chi gioca in inglese mette da
parte 300 AP e si sente rispondere che non bastano. La resa italiana dice 400.

⭐ **E il modo di saperlo è stato contarli tutti**: verificati uno per uno i
ventisei prezzi dei due menu contro il `leoap` che ciascun ramo assegna. È
l'unico che diverge — e senza il conto completo sarebbe stato indistinguibile da
un refuso qualunque. *Un prezzo scritto in un'etichetta è un numero che il codice
ripete altrove: si confronta, non si copia.*

### 3. ⚠️⚠️ E sbaglia DUE nomi di parte del corpo, sempre contro se stesso

`:16741` offre «Chest» e `:16743` «Finger», ma gli slot che concedono sono
`EQUIP_SLOT_BODY` e `EQUIP_SLOT_RING`, che `bodyn()` (`text.hsp:136`) chiama
«Body» e «Ring». Il menu inglese nomina una cosa che il messaggio di conferma —
`name(r1) + " grows a new " + bodyn(...)` — chiama in un altro modo. Il
giapponese è coerente in tutt'e due i punti (胴体/胴体, 指/指).

### 4. 🔶 DECISIONE APERTA: il menu degli arti non dice le parole di `bodyn()`

Le nove voci di `:16738`-`:16746` sono tradotte da una sessione vecchia e dicono
**Testa, Collo, Schiena, Torso, Mano, Dito, Braccio, Fianchi, Gamba**. `bodyn()`
in italiano dice **Testa, Collo, Dorso, Torso, Mano, Anello, Arto, Vita, Gamba**.
Quattro su nove non combaciano: chi sceglie «Dito» si sente rispondere «ha una
parte nuova: Anello».

Per la regola della 76ª il menu dovrebbe dire le parole del messaggio. Ma la
correzione ovvia inciampa: `bodyn(EQUIP_SLOT_WAIST)` è «**Vita**», e nella stessa
riga «Vita» è già il nome della statistica che si paga — «Vita (Vita -12)» non si
può scrivere. È lo stesso inciampo del 発言力 con due nomi sullo schermo: la
parola giusta è occupata.

Le tre strade, nessuna scelta:

1. cambiare l'etichetta del costo — «Fianchi (-12 vitalità)» — e allora il menu
   può dire tutte e nove le parole di `bodyn()`;
2. cambiare `bodyn(EQUIP_SLOT_WAIST)` da «Vita» a «Fianchi», che però è
   un'etichetta di casella letta in ogni finestra dell'equipaggiamento e la
   `gronde`/`riquadri` la misurano;
3. lasciare com'è e dichiarare che il menu degli arti parla di anatomia mentre
   `bodyn()` parla di caselle d'equipaggiamento — che è vero, ed è forse il
   motivo per cui la sessione vecchia ha scelto così.

⚠️ Nessuna delle tre si può decidere senza **guardare le due schermate**: quanto
sono vicine nel tempo, e se il giocatore le legge davvero di fila.

### 5. Due schermate, le stesse parole, due lunghezze diverse

Il menu dei tredici poteri del compagno (`:17853`-`:17865`) ha più di dieci voci,
quindi due colonne e `strmid(..., 0, 24)`. Lo stile del progetto per i costi è
«(100 AP)» — è quello che `:17704`-`:17716` ha già in build — ma lì non ci sta:
«Accumulo di mana (600 AP)» fa 25. Nel solo menu a tredici il costo si stringe a
«AP600», e i **nomi** restano identici. È la regola della 73ª: *due schermate che
mostrano la stessa scelta devono dire le stesse parole, non sono tenute a dirle
con la stessa lunghezza.*

⚠️ Una sola voce non entrava lo stesso, «Maledizione tattica AP500» (25). Si è
accorciato il **qualificatore condiviso** e non il nome (72ª): «Maledizione tatt.
AP500».

### 6. La misura di un lotto va letta sapendo quale finestra misura

`chat-lotto-misura` ha segnalato due rese «una riga in più dell'inglese», e
tutt'e due erano false: `:16932` va a `*screen_drawMsg2` (targa, tetto 89, la
resa ne usa 82) e `:17110` è una riga del pannello delle modalità
(`pos wx + 165`, tetto 73, la resa ne usa 71). Lo strumento le misura col metro
della **finestra del dialogo**, 53 caratteri, perché tratta come battuta tutto
quel che non è `chatList`. 💡 È la 70ª in piccolo: prima di accorciare una resa
per un referto, si guarda **da dove viene il metro**.

### 7. ⭐ Il pannello delle modalità: la prima geometria letta del punto cieco della 74ª

Le **sette** righe `listn(...) = lang(...)` di `chat.hsp` che la 74ª aveva
trovato e mai misurato sono quelle di `*com_change_gamemode_loop`
(`:16934`-`:16940`). La geometria, letta ora:

    display_window  (windoww-680)/2, ..., 680, 400      -> wx, ww = 680
    cs_list listn(0, cnt), wx + 64, ...                 font 14 - en*2 = 12
    pos wx + 165 ; mes s                                font 13 - en*2 = 11

* **colonna di sinistra** (i nomi delle modalità): testo a `wx + 64`, ostacolo a
  `wx + 165` -> 101 px, a 7 px per carattere **14 caratteri**. Sei delle sette
  voci sono nomi propri identici in tutt'e tre le lingue (Essential, Loss,
  Overdose, Natural, Abnormal, Purge); la settima è `*Cancel*`, resa
  «*Annulla*», 9. ⚠️ Nessuna riga inglese sfiora il tetto, e per la regola della
  63ª questo di solito vuol dire che si è misurata una cosa vicina — qui no: le
  sei voci sono nomi che upstream non può allungare.
* **colonna di destra** (le descrizioni): testo a `wx + 165`, la finestra
  finisce a `wx + 680` -> 515 px, **73 caratteri**. ⭐ E la riga inglese più
  lunga (`:17004`, «it's easy mode. This mode is best for those who just want to
  take it easy») ne fa **73 esatti**: è la firma della 63ª, *upstream scrive
  dentro la finestra che ha disegnato*, e il tetto è quello vero.

⚠️⚠️ **Le trentasette descrizioni erano già tradotte da una sessione vecchia e
non le aveva mai misurate nessuno.** Misurate adesso: la più lunga è
`:17082` («- Ricarica con F2 per rigiocare la sorte. Salvataggio automatico
spento.») con **72**. Dentro per un carattere. 💡 Il punto non è che erano
giuste: è che *nessuno lo sapeva*, e restavano giuste per fortuna.

---

## 81ª — Il confine di una zona non è un parlante, un partner fuori da `lang()`, e il primo collaudo dopo dieci sessioni

### 1. ⚠️⚠️⚠️ Il perimetro di una ZONA è un'etichetta HSP, e taglia i blocchi a metà

La 79ª aveva fatto del conto del perimetro uno strumento
(`scratchpad/perimetro-zona.py`) e la 80ª ci aveva costruito sopra la nozione di
**zona chiusa**. Ma la zona `*label_6452` è delimitata da `:15509`, che è
l'etichetta `*label_6450` — e il blocco di **Telhureza** comincia a `:15491`.

    :15491   if ( _switch_val == CREATURE_ID_TELHUREZA_THE_HOUSE_GUARD ...
    :15493   chatList 0..2                  <- zona di *chat_unique_mizuki
    :15496   buff
    :15508   chatMore
    :15509  *label_6450                     <- il confine
    :15514   txt "Chi vuoi che attacchi?"   <- zona di *label_6452
    :15531   il grido

Tradurre il perimetro come lo dava lo strumento — 47 firme — avrebbe messo un
**sottodialogo italiano sotto un menu inglese**: il difetto della 79ª, quello
che `bilingui` non vede *ed è giusto che non veda*, perché un menu tutto inglese
non è bilingue.

✅ **Il lotto si prende sul PARLANTE, non sull'etichetta**: `:15491`-`:15764`,
54 firme invece di 47. `bilingui` ha dato zero al primo giro.

💡 La regola generale: *un'etichetta HSP è un indirizzo di salto, non un confine
di senso.* Prima di aprire un lotto su una zona si guarda la riga del confine e
si risale al `if ( _switch_val == ... )` che la contiene.

### 2. ⚠️⚠️ «landlord» cade, e con lui un vocativo vecchio

Tre inquilini chiamano il giocatore 大家さん / 家主さん. In italiano ogni resa
porta il genere — «padrone di casa» / «padrona di casa» — ed è il primo dei
quattro bersagli del divieto (75ª): il **vocativo**. Il titolo si lascia cadere,
come i benvenuti della 58ª.

⚠️ E lo stesso difetto stava già in `db_creature.hsp:43882`, dove Oxode diceva
**«Ah, padrone di casa, sei di ritorno.»** — resa vecchia, mai rivista.
Corretta in «Ah, eccoti a casa.». 💡 *Un elenco di eccezioni è un debito: si
rilegge ogni volta che si tocca uno dei siti che nomina* (77ª), e qui il sito
non era in nessun elenco — l'ha portato a galla il lotto.

### 3. ⭐ Il DATO decide di nuovo: `servant` è «incarnazione»

Talka spiega i 下僕 / «servants» che ogni dio concede. La parola non si è
scelta: `db_race.hsp:5553` rende 神の化身 con «Incarnazione», ed è la **razza che
il giocatore legge sulla scheda** della creatura che riceve. Chiamarli
«servitori» sarebbe stato italiano corretto e dentro il tetto, e avrebbe
lasciato il giocatore senza il collegamento. Terza prova della regola della 79ª.

Nello stesso lotto: Piety → «devozione» (`command.hsp:7626`), faith skill →
«abilità Fede» (`skill.hsp:347`), «insetti cattivi» e «geco di guardia» dal
repertorio di Telhureza in `db_creature.hsp`, «affitto» da `chat.hsp:766`.

### 4. ⭐ Il sesso si legge nel codice, non nell'epiteto

`text.hsp:378` dice che `CDATA_SEX == 0` è **maschio**. Quindi **Scard è un
uomo**, anche se l'epiteto italiano è «<Scard> **la** rondine felice» — lì il
femminile è del sostantivo «rondine», non del personaggio. La sua battuta finale
«I'm so happppppppy!!!» è resa con la forma **invariabile**: «Io sono così
feliceeeeee!!!!». 💡 *Un epiteto non è una dichiarazione di genere.*

Gli altri sei del lotto, letti nei loro blocchi `DBMODE_SET`: Oxode, Imarituka,
Talka, Telhureza e Kyu-bi donne; Boyciana senza sesso fisso, ma dà del **lei**
(lo dice la sua riga di `db_creature.hsp`).

### 5. ⚠️⚠️⚠️ La toppa 1018 e una classe di difetto nuova: la `lang()` tradotta il cui PARTNER non sta in `lang()`

Cercando la strada per il collaudo è saltato fuori che **in italiano ogni
desiderio di una creatura dava la statuetta di `@`**.

* le quattro parole d'innesco stanno in `lang()` (`command.hsp:4846`-`:4856`) e
  sono tradotte: carta, statuetta, bambola dorata, bambola di carne;
* le righe che le **tolgono** dalla stringa prima di cercare il nome stanno in
  `fix_wish` (`module.hsp:4815`-`:4826`), **non** sono in `lang()`, e il
  dizionario non le ha mai viste: sono rimaste `card`, `figure`, `golden doll`,
  `flesh doll`.

Quindi «statuetta di Telhureza» arrivava intera a `*wish_monster`, non
combaciava con nessun nome, e `wish_monster` ripiegava su `dbid = 0` =
`CREATURE_ID_AT_SIGN`.

Provato sul banco HSP (`scratchpad/_81-banco-desiderio.py`), prima sull'inglese
di monte come vuole la regola della 61ª:

    MONTE inglese      «figure of Telhureza»     -> [telhureza]                COMBACIA
    BUILD senza toppa  «statuetta di Telhureza»  -> [statuetta di telhureza]   nessuno
    BUILD con toppa    «statuetta di Telhureza»  -> [telhureza]                COMBACIA
    BUILD con toppa    «carta di Oxode»          -> [oxode]                    COMBACIA
    BUILD con toppa    «figure of Telhureza»     -> [telhureza]                COMBACIA

⭐⭐⭐ **La lezione vale più della toppa.** Il progetto sapeva già che certe
`lang()` sono **chiavi** e non testo (`custom_autopick.hsp`, che sta in
`FILE_DELICATI`). Questo è il caso girato: la `lang()` è testo vero, ma **da
qualche altra parte, fuori da `lang()`, c'è del codice che la deve
riconoscere**. Nessuna rete lo guarda, e non basta leggere il sito: bisogna
cercare **chi confronta quella stringa**. ⚠️ *Rete ancora da fare, e il
perimetro è tutto il sorgente.*

⚠️ Difetto di MONTE trovato per strada e **non** toccato: `cnv_str ..., "card",
""` morde dentro i nomi, quindi «figure of Scard» diventa «s» e combacia con la
prima creatura che contiene una «s».

### 6. ⚠️ DEROGA DICHIARATA — `chat.hsp:15783`, il livello di un racconto

La lista dei tredici racconti di Aime sale 200, 250, **300**, 400, 500... nel
giapponese. L'inglese scrive «The Muddy Hands (**Lv250**)», ripetendo il livello
del racconto precedente. È la famiglia del prezzo di Leold (80ª) — *un numero
scritto in un'etichetta si confronta, non si copia* — con la differenza che qui
il confronto non è col codice ma con la **serie**: nessun `leoap` da leggere,
perché `:15793` dice che i racconti sono tutti ancora da implementare. ✅ Si
segue il giapponese: «Le mani di fango (Lv300)».

⚠️ E quel menu ha **tredici voci**, quindi passa a due colonne e taglia a 24
caratteri (76ª): sette titoli inglesi sforano già a monte, i sei che ci stanno
sono stati tenuti dentro anche in italiano.

### 7. ⭐⭐⭐ Il collaudo non dipende più da dove è arrivato il salvataggio

Il debito era di **2.242 rese mai viste a schermo in dieci sessioni**, e la
ragione vera non era la pigrizia: per collaudare il dialogo di un PNG bisognava
che il salvataggio ci fosse arrivato. Gli inquilini della casa, per dire, sono
**ospiti casuali** (`main.hsp:8215`: `rnd(10) == 0`, poi
`(giorno + homeu) \ 5`).

La strada c'era ed era scritta nel sorgente:

1. **F12** apre la console di debug (`main.hsp:3322`, `getkey a, 123`);
2. `wizard` accende la modalità mago (`system.hsp:4718`) — ⚠️ riscrive
   l'appellativo del personaggio in `*Debug*`, quindi si fa su un salvataggio di
   collaudo;
3. `spawn_chara <ID>` fa comparire la creatura sulla casella del giocatore
   (`system.hsp:4831`, dietro `if ( gdata(GDATA_WIZARD) )` a `:4815`);
4. le si cammina addosso per parlarle.

⚠️ **Non si usa `add_ally`**: `chat.hsp:281` manda al dialogo unico solo se
`tc >= MAX_CHARA_FOLLOWER`. Arruolare il PNG fa apparire il menu del compagno e
il dialogo da collaudare non si vede più.

Gli ID stanno in `defines/mod.hsp`. Quelli di oggi: Telhureza 1042, Imarituka
1043, Oxode 1044, Scard 1045, Talka 1056, Kyu-bi 1125, Boyciana 690, Momalaria
1143, Aime 1024, Jaldabaoth 1017, Leold 526. Tutti e sette gli inquilini hanno
`RELATION_NEUTRAL`: non attaccano.

✅ **Le sette schermate del lotto sono state guardate a schermo e sono a
posto.** ⚠️ Il limite resta dove il dialogo dipende da una bandiera di trama: il
menu degli arti di Leold vuole `gdata(GDATA_FLAG_MAIN) >= 220`
(`chat.hsp:8181`), e la console **non ha un comando per muovere quel flag** — la
console Lua che potrebbe farlo è compilata via (`main.hsp:9`).

### 8. ⚠️ Una trappola del collaudo: il registro dei messaggi all'apertura è VECCHIO

Aperto il gioco, la riga in fondo diceva «Informer of God Hildegard **goes wild
with joy**, "shop!!" A deed of shop appears.» — inglese pieno. Non è un difetto:
Elona **ripristina il registro dal salvataggio**, e quelle righe erano state
scritte da una build precedente. Nel build di adesso `command.hsp:4436` dice
«esulta di gioia». 💡 *Del riquadro dei messaggi vale solo quel che si stampa
dopo aver caricato.*
