# Invariati

Stringhe che restano identiche all'inglese **per scelta esplicita**, non perché
la traduzione è stata dimenticata. `verifica.py` legge questo file e non le
segnala.

Senza il file `verifica.py` si comporta come prima: è un'aggiunta, non un
requisito. Un progetto senza eccezioni è un progetto senza il file.

Il confronto è sulla **stringa intera** e sensibile alle maiuscole: una riga
qui copre `Vernis` come valore completo di `en`, non la parola `Vernis` dentro
una frase più lunga. Una frase che contiene un nome proprio si traduce
normalmente.

Una riga qui è una decisione: va motivata. Se il motivo non si riesce a
scrivere, probabilmente la stringa va tradotta.

| valore | motivo |
|---|---|
| `< ` | la parentesi che apre il nome del dio in cima al pannello di scelta (`god.hsp:392`-`:416`, nove volte lo stesso `lang("《 ", "< ")`). Il giapponese usa le parentesi angolari piene 《 》, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII: le francesi «» CP932 non le codifica affatto, e le graffe piene sono a due byte, che la build inglese disegna come due glifi latini a caso. Non c'è niente da tradurre: è una cornice |
| ` >` | la parentesi che chiude, per la stessa ragione di `< ` |
| `Direct sound` | nome del driver audio (`config.hsp:805`), non una parola: e' il valore che si scrive in `config.txt` alla chiave `sound.`, e accanto a lui il pannello mostra `MCI`, che nel sorgente non passa nemmeno da una `lang()`. Tradurlo scollegherebbe l'etichetta dal file di configurazione |
| `Direct music` | nome del driver audio (`config.hsp:809`), per la stessa ragione di `Direct sound`. Il terzo e il quarto valore della stessa riga sono `MCI` e `GuruGuruSMF4`, letterali nudi che nessun dizionario raggiunge |
| `Spongebob` | nome di un modo di scrivere i nomi degli oggetti (`config.hsp:944`), accanto a `Capitalize`, `Uppercase`, `Lowercase` e `Schizophrenic`. E' la citazione del meme del testo aLtErNaTo, che in italiano circola con lo stesso nome inglese; e il giapponese qui non aiuta, perche' dice 「表示」 per tutt'e cinque i modi |
| `Info` | il nome della prima pagina della ruota dei comandi (`help.hsp:58`), giapponese 情報. ⚠️ **Non e' inglese lasciato li': e' italiano che coincide.** «Info» e' l'abbreviazione corrente in italiano, e la forma piena — «Informazioni», dodici caratteri — non ci sta: gli slot 0, 4 e 8 della ruota hanno passo 75 px a 7 px per carattere (`help.hsp:105`), cioe' **dieci**. Le altre tre pagine si traducono e infatti si sono tradotte: «Azioni», «Speciali», «Zaino» |
| `<evochat>` | nome del sistema di dialogo evoluto di Custom-GX (`chat.hsp:19431`), giapponese 【evochat】: il giapponese stesso lo tiene in caratteri **latini** dentro le parentesi piene, che e' il modo in cui quella lingua marca un nome importato. Non e' una parola comune, e' il nome di un sistema, e compare anche dentro 【タッグごとevochat】 e 【暗黒evochat】 — che infatti si traducono, perche' li' la parte italiana c'e' («in coppia», «oscuro») e il nome resta |
| `<Big Sister>` | nome di creatura (`action.hsp`, `db_creature.hsp`), giapponese 『ビッグシスター』: la citazione di BioShock, che in italiano non è mai stata tradotta. Già deciso in `glossario.md` insieme a `<Little Sister>`, ma non era mai arrivato qui: la coppia si è presentata nel primo lotto della Fase 2, dove non porta l'articolo perché sta fra `<>` |
| `<Little Sister>` | nome di creatura (`action.hsp`, `db_creature.hsp`), giapponese 『リトルシスター』: vedi la riga sopra, è l'altra metà della coppia |
| `<Pascal>` | nome di creatura (`db_creature.hsp`, razza `dog`), giapponese イヌの偉大なる『パスカル』. Il giapponese lo presenta come «il grande fra i cani, Pascal», ma l'inglese ha ridotto il nome al solo epiteto fra `<>`, e lì l'epiteto **è** il nome: non resta nessuna parola comune da rendere. Nome proprio opaco, come `Vernis`. Non porta l'articolo perché comincia per `<` |
| `@` | nome di creatura (`db_creature.hsp`, razza `norland`), giapponese ＠. È il **simbolo del giocatore** dei roguelike fatto creatura — parla «Qy@» e nient'altro. Un segno, non una parola: non c'è niente da tradurre, e non prende articolo, come i nomi fra `<>`. È la sola deroga dichiarata alla regola dell'articolo dentro il nome |
| `user` | nome di creatura (`db_creature.hsp`, razza `god`). ⚠️ **Non è un nome: è uno slot.** La riga è `lang("user", "user")`, cioè il giapponese è **identico** all'inglese — e in un file dove ogni nome vero ha la sua forma giapponese, quello è upstream che dice «questo non è testo». È il segnaposto dei PNG definiti dal giocatore (`cdata(CDATA_USERNPC_ID, rc)`), sovrascritto al caricamento. Non prende articolo perché non è una parola che qualcuno legga |
| `{` | **non è testo: è il segno che marca un nato in gioco** (`main.hsp:6325` e `:6364`, `chara.hsp:2335`, `chat.hsp:17484`), giapponese 「《」. Avvolge il nome del figlio appena partorito, e in Elona la coppia `{ }` distingue le creature **nate durante la partita** dalle uniche, che portano `< >`. ⚠️ `module.hsp:264` rende gli **stessi due caratteri giapponesi** con `<` e `>`, e non è una contraddizione: lì l'inglese di monte scrive `<`, qui scrive `{`, ed è upstream a tenere separati i due segni. Uniformarli renderebbe un figlio indistinguibile da un boss |
| `}` | **non è testo**: è l'altra metà della coppia qui sopra |
| `???` | `chat.hsp:19135`, dentro `cnvtalk`: la battuta del compagno che non capisce che cosa gli stia succedendo. Giapponese 「？？？」, cioè gli **stessi tre segni** a doppio byte. Non è inglese lasciato lì: è punteggiatura, e la punteggiatura non ha lingua. La forma italiana dei punti interrogativi è quella ASCII, e le tre domande piene giapponesi in CP932 escono a sei glifi |
| `"<<" + iroiro + ">>"` | `chat.hsp:19311`: **non è testo, è una cornice attorno a una variabile.** La riga è `lang(iroiro + " ", "<<" + iroiro + ">>")`, e `iroiro` porta già la sua resa — «(Un po' di tutto)» da `:19306`, oppure una frase che `customtalk` pesca dal database della creatura. Le doppie angolari marcano le voci **speciali** del menu degli evochat, accanto a `<<Abbracciare>>` e `<<Baciare>>`: quel che c'è da tradurre sta dentro `iroiro`, e la resa italiana di questa riga non può che essere la stessa cornice. ⚠️ Il valore dichiarato qui è l'**espressione intera**, non `<<>>`: per una dinamica il termine di paragone di `verifica.py` è `en_grezzo`, come per `" < " + s + " > "` qui sopra |
| Vernis | nome proprio di città, canone Elona |
| Palmia | nome proprio di città, canone Elona |
| Derphy | nome proprio di città, canone Elona |
| Noyel | nome proprio di città, canone Elona |
| Yowyn | nome proprio di città, canone Elona |
| Lumiest | nome proprio di città, canone Elona |
| Melugas | nome proprio di luogo, canone Elona |
| Larna | nome proprio di città, canone Elona; nome opaco, vedi «la regola dei nomi propri» in `glossario.md` |
| Arcbelc | nome proprio di luogo Elona+; nome opaco |
| Lesimas | nome proprio del dungeon sotto Vernis; nome opaco |
| Aimwell | nome proprio di villaggio di South Tyris (`text.hsp:2899`), giapponese イムウエル. Nome opaco: il katakana traslittera e basta, e come romanizzarlo è scelta dell'inglese — stesso criterio di `padangu` in `glossario.md` |
| Zaile | nome proprio di città (`text.hsp:2902`), giapponese ザイール; nome opaco |
| Ulm-Leson | nome proprio delle rovine nella foresta (`text.hsp:2920`), giapponese ウールム・レゾン; nome opaco, di due parti entrambe inventate |
| Ol-dran | nome proprio della città degli angeli (`text.hsp:2944`), giapponese オルドラン; nome opaco |
| `****` | **non è testo**: quattro asterischi, identici nelle due lingue (`text.hsp:2905`). È il nome **mascherato** di una località che il gioco non vuole svelare, e la descrizione accanto lo conferma — «qualcosa che somiglia a una città». Tradurre gli asterischi vorrebbe dire non averli capiti |
| `O` | **non è una parola: è un segno disegnato** (`proc.hsp:10036`), giapponese 「○」. È il cerchio rosso che marca il punto sulla mappa del tesoro — `mes` con `font 40` e `color 255, 20, 20`, dentro il ciclo che ridisegna la mappa. L'inglese sceglie la lettera `O` perché somiglia al 「○」 giapponese, e l'italiano non ha un segno diverso da usare: la `X` che marca i tesori nelle mappe dei pirati direbbe un'altra cosa, cioè che è stato l'inglese a scegliere il cerchio e noi lo cambieremmo. Stesso criterio di `****` |
| Karma | termine acquisito in italiano |
| `Target Acquired.` | battuta dello `<Spazzino di sotterranei>` (`db_creature.hsp:99788`). ⚠️ **Il giapponese è inglese anche lui**: la riga è `lang("「Target Acquired.」", "Target Acquired.")`, cioè l'autore fa parlare inglese la macchina *anche al giocatore giapponese*. Sono quattro battute e formano un blocco solo — inglese da robot più gergo di rete. Tradurle darebbe all'italiano una cosa che né il giapponese né l'inglese hanno: una macchina che parla la lingua di chi legge. Stesso criterio di `user`, dove il giapponese identico all'inglese è upstream che dichiara l'intenzione |
| `Resistance is futile!` | battuta dello `<Spazzino di sotterranei>` (`db_creature.hsp:99788`), giapponese 「Resistance is futile!」: vedi la riga sopra. È anche la citazione dei Borg, che il gioco fa in inglese in entrambe le lingue |
| `Pwned!` | battuta dello `<Spazzino di sotterranei>` (`db_creature.hsp:99794`), giapponese 「Pwned!」: vedi due righe sopra. Gergo di rete, intraducibile per costruzione — è un refuso di *owned* diventato parola |
| `WTF` | battuta dello `<Spazzino di sotterranei>` (`db_creature.hsp:99800`), giapponese 「wtf」: vedi tre righe sopra. Sigla di rete; il giapponese la porta in minuscolo, l'inglese in maiuscolo, e nessuna delle due la traduce |
| Dojo | termine acquisito in italiano (`text.hsp:3036`, giapponese 道場), come `Karma`. Sui vocabolari italiani con questa grafia; «palestra» direbbe un'altra cosa |
| udon | nome di piatto (`text.hsp:3702`, giapponese うどん). In italiano si chiama così, come `sushi`: tradurlo con «tagliatelle» direbbe un'altra cosa |
| ramen | nome di piatto (`text.hsp:3762`, giapponese ラーメン); vedi `udon` |
| carbonara | nome di piatto (`text.hsp:3747`, giapponese カルボナーラ). ⚠️ Qui **l'italiano è la lingua d'origine**: il giapponese traslittera un nome italiano e l'inglese lo copia. Non è una traduzione dimenticata, è la parola tornata a casa. Il gemello ペペロンチーノ **si traduce** — «aglio e olio» — perché lì il giapponese ha preso l'ingrediente per il piatto, e in italiano il piatto ha un nome suo |
| Mana | termine acquisito nei giochi di ruolo |
| Anemia | **nome di malattia** (`trait.hsp:529`, giapponese 貧血): in italiano si scrive identico all'inglese. Non e' una resa dimenticata — e' la stessa parola, dal greco *an-haima*, che le due lingue hanno preso dalla stessa radice. `verifica` la segnala come «traduzione identica all'inglese», che e' la ragione per cui questa riga esiste |
| `HP/MP` | **il giapponese è la stessa sigla**: `command.hsp:10517` è `lang("HP/MP", "HP/MP")`, i due rami identici carattere per carattere. Sono le due sigle che ogni gioco di ruolo scrive così, punti vita e punti magia, e il progetto le usa già dentro le frasi (`buff.hsp:430`, «Cura HP e stati ogni turno»). Stesso criterio di `Mana` qui sopra, con in più il fatto che qui l'identità la dichiara **upstream**: la barra fra le due è già nel ramo giapponese |
| `AP` | **la sigla dei punti che si guadagnano nelle Nefia**, etichetta della scheda del personaggio (`command.hsp:10504`), giapponese 「ＡＰ」 — la stessa sigla a **larghezza intera**, che CP932 ci vieta comunque. Chi gioca a Elona+ li chiama AP in ogni lingua, e la colonna ha 50 pixel: una resa lunga («punti abilità») non ci starebbe nemmeno volendo. Stesso criterio di `HP/MP` qui sopra |
| `Mana      : ` | **etichetta del rapporto del personaggio** (`command.hsp:17674`), il file di testo che il gioco esporta. `Mana` è già invariato qui sopra; quel che cambia è che la stringa porta dentro **gli spazi di allineamento** — le etichette del rapporto sono di dodici caratteri esatti perché i due punti cadano in colonna — e vanno perciò dichiarate fra apici inversi, verbatim. ⚠️ Se un giorno la colonna cambia larghezza, queste quattro righe cambiano con lei |
| `Karma     : ` | come sopra (`:17678`): `Karma` è invariato dal 2026-08-07, qui con gli otto spazi della colonna |
| `DV        : ` | **la sigla della difesa** nel rapporto (`:17679`), giapponese 「DV」 — i due rami identici carattere per carattere, come `HP/MP`. È la sigla che ogni gioco di ruolo scrive così, e il progetto la usa già dentro le frasi (`buff.hsp:983`, «DV, PV e Velocità -20%») |
| `PV        : ` | **la sigla della protezione** nel rapporto (`:17680`), giapponese 「PV」. Stesso criterio di `DV` qui sopra |
| `[bit]` | **l'etichetta di categoria delle righe di stato** nella scheda dei talenti (`command.hsp:2162` e le quarantacinque righe che la usano come prefisso), giapponese 「[bit]」 — i due rami identici carattere per carattere, come `HP/MP`. Sta accanto a `[Talento]`, `[Mutazione]`, `[Innato]` e `[Etere]`, che si traducono: quella colonna dice **da dove viene** una riga, e qui la provenienza è un flag del personaggio (`CHARA_BIT_INCOGNITO`, `CHARA_BIT_PREGNANT`…). ⚠️ È tecnicismo anche in originale — il giapponese aveva la scelta e ha lasciato l'inglese — e inventare «[Stato]» direbbe più di quel che dicono le due lingue di monte |
| Arena | parola latina che le due lingue hanno identica. `text.hsp:2782`, dove il giapponese dice 闘技場. Non è un nome proprio lasciato in inglese: è la resa giusta, e coincide. Il gemello `Pet Arena` si traduce — «Arena delle bestie», il termine di `db_creature.hsp:118259` — perché lì c'è anche una parola comune. ⚠️ **Vale anche per `init.hsp:355`**, dove la stessa parola è l'undicesima voce di `rankn(10, 0)`, cioè il **nome della categoria** che `module.hsp:264` stampa in «Cambio di rango (Arena 5° → 4°)»: giapponese 「アリーナ」, katakana della stessa parola. Gli altri dieci gradini della riga sono tradotti |
| Incognito | nome dell'incantesimo `skill.hsp` (giapponese インコグニート, a sua volta traslitterazione dell'inglese). **Parola italiana identica all'inglese**, dallo stesso latino: è la resa giusta, non una traduzione dimenticata. Sta qui perché `verifica.py` segnala le identità non dichiarate |
| * | simbolo, non testo: `text.hsp:12` lo stampa come marcatore. Non c'è niente da tradurre |
| . | punteggiatura: `text.hsp:108` sceglie il segno di fine frase. Identica in italiano |
| ? | punteggiatura, idem |
| ! | punteggiatura, idem |
| `$` | **simbolo, non testo**: `command.hsp:3392` stampa il valore della ricompensa di un incarico in bacheca, e il giapponese è 「★」. L'inglese ha scelto il segno del denaro al posto della stella; l'italiano non ha un terzo segno da mettere, e cambiarlo direbbe che la scelta è nostra. ⚠️ Il glifo deve stare in **13 pixel**, che è il passo con cui `:3391` incolonna i simboli. Stesso criterio di `O` e di `****` |
| `$ x ` | l'altra metà del simbolo qui sopra (`command.hsp:3397`, giapponese 「★×」): quando i simboli sono più di sei, il gioco smette di disegnarli e scrive «$ x 12». Gli apici inversi prendono lo spazio finale verbatim, perché il numero si concatena subito dopo |
| `(` | **punteggiatura**: `command.hsp:3634` è `lang(" ", "(")`, cioè il giapponese apre l'età con uno spazio e l'inglese con una parentesi. In italiano l'età fra parentesi si scrive con la parentesi. ⚠️ E non c'è margine per fare altro: la riga vive in **19 caratteri** fra `wx + 372` e la colonna dei valori a `wx + 512`, e «Lv.100 female?(999)» ne fa già 19 |
| `)` | l'altra metà (`command.hsp:3634`, `lang("歳", ")")`): il giapponese chiude con il contatore 歳 «anni», l'inglese con la parentesi. « anni)» costerebbe cinque dei diciannove caratteri della riga, e non ci sono |
| bonus | prestito acquisito, già in glossario. `strfix` (`text.hsp:190`) etichetta il `+3` di un oggetto |
| ` Lv` | la sigla di livello, che l'italiano scrive uguale. ⚠️ Non è solo un'etichetta: `action.hsp:12383` compone `evold = lang(" Lv", " Lv") + livello` e poi **cerca quella stringa in coda al nome** della creatura per togliere il suffisso (`:12384`). Tradurla qui, e non anche nel punto che il suffisso lo scrive, spezzerebbe il taglio: è la trappola del letterale confrontato contro un valore tradotto. Il resto del progetto scrive già `Lv` (`action.hsp:6545`, `text.hsp:65` e `:68`) |
| http://homepage3.nifty.com/rfish/index_e.html | indirizzo web (`text.hsp:181`), non testo |
| PER | sigla di Percezione: **identica** in italiano e in inglese. È una coincidenza, non una traduzione dimenticata |
| MAG | sigla di Magia: identica in italiano e in inglese |
| ` PER` | la stessa sigla di `text.hsp:62`, che allinea con uno spazio iniziale (`lang("感覚", " PER")`). Gli apici inversi la prendono verbatim: una cella markdown si legge con `strip()`, e senza di essi lo spazio si perderebbe |
| ` MAG` | idem, `lang("魔力", " MAG")` |
| ` ` | `strblank` (`text.hsp:198`): uno spazio di riempimento, non testo. Gli apici inversi lo prendono verbatim |
| lastwords-e.txt | nome di file (`text.hsp:465`), non testo |
| Itzpalt | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Itzpatl | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Itzpait | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Itspalt | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Zashim | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Zeome | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Zenum | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Zanam | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Larnneire | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Larnreire | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Larnneine | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Larnreine | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Valm | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Kurualm | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Azzrssil> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Issizzle> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Ulzassil> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Exossil> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Leiki> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Renki> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Lenki> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Leike> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Karam> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Slan> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Caim> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Lend> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Lexus> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Lenas> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Revlus> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Redos> | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Ludus | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Eirel | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Melkawn | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| Ruoza | nome proprio opaco del quiz (`text.hsp`). Molte voci sono **esche**: storpiature volute della risposta giusta, e tradurle o normalizzarle distruggerebbe la domanda |
| <Mournblade> | nome proprio opaco di artefatto (`db_item.hsp`). Il giapponese lo **traslittera** — 《モーンブレイド》 — invece di tradurlo: quando l'originale traslittera, nemmeno lui legge il nome come descrizione. Citazione di Moorcock, mai tradotta in italiano |
| <Zantetsuken> | nome proprio opaco di artefatto (`db_item.hsp`), giapponese 《斬鉄剣》: un nome proprio giapponese, non una descrizione |
| <Diablos> | nome proprio opaco di artefatto (`db_item.hsp`), giapponese 《ディアボロス》, traslitterato |
| mithril | materiale (`item_data.hsp`), nome opaco del canone fantasy: Tolkien in italiano lo lascia «mithril». Il giapponese lo traslittera, ミスリル |
| rubynus | materiale (`item_data.hsp`), minerale inventato da Elona; nome opaco |
| zylon | materiale (`item_data.hsp`), nome opaco. Esiste una fibra reale omonima, e in italiano si chiama così |
| mica | materiale (`item_data.hsp`): **il minerale si chiama «mica» anche in italiano**. Coincidenza, come `PER` e `MAG`. ⚠️ In una frase è anche un avverbio di negazione, ma qui la stringa intera è il nome del materiale e non compare mai da sola in prosa |
| incognito | nome dell'incantesimo (`db_item.hsp`: pergamena e grimorio). **Parola italiana identica all'inglese** — «in incognito» — e quindi la resa naturale coincide. È una coincidenza, come `PER` e `MAG`, non una traduzione dimenticata |
| <Ether Dagger> | nome proprio opaco di artefatto (`db_item.hsp`), giapponese 《エーテルダガー》, **traslitterato**: come `<Mournblade>` e `<Diablos>`, nemmeno l'originale legge il nome come descrizione |
| <Ragnarok> | nome proprio opaco di artefatto (`db_item.hsp`), giapponese 《ラグナロク》, traslitterato. Nome del mito norreno, in italiano usato tale e quale |
| `<Ether Generator>` | creatura unica (`db_creature.hsp`, razza `rock`), giapponese 『エーテルジェネレイター』. **Stessa costruzione di `<Ether Dagger>`**: katakana che traslittera l'inglese, non una descrizione che l'originale legge come tale. ⚠️ Non confonderlo con エーテル nudo, che è «etere» in tutto il resto del gioco |
| tonfa | **il nome NON IDENTIFICATO** di cinque artefatti (`db_item.hsp`, `iknownnameref`), giapponese 音速/斬撃/連撃/守護/生贄の旋棍. L'arma si chiama «tonfa» anche in italiano — e' il prestito corrente, come `guava` e `mica` — quindi la resa naturale coincide. ⚠️ Il giapponese **distingue** i cinque (sonico, tagliente, a raffica, difensivo, sacrificale), l'inglese li appiattisce tutti su «tonfa», e li' l'inglese ha ragione: e' un nome non identificato, e il suo mestiere e' **non** dire quale dei cinque hai in mano. Seguire il giapponese qui svelerebbe l'oggetto prima dell'identificazione |
| whisky | nome del distillato (`db_item.hsp`), giapponese ウィスキー. **Grafia italiana corrente**: i dizionari registrano «whisky», non una forma adattata |
| leccho | frutto inventato da Elona (`db_item.hsp`), giapponese レッチョ, traslitterato. Nome opaco, come `rubynus`. Invariato anche al plurale, come l'italiano fa con i nomi di frutti esotici |
| qucche | frutto inventato da Elona (`db_item.hsp`), giapponese クッチェ; nome opaco, invariato al plurale |
| imo | tubero inventato da Elona (`db_item.hsp`), giapponese イーモ in katakana — non il 芋 comune; nome opaco, invariato al plurale |
| quwapana | frutto inventato da Elona (`db_item.hsp`), giapponese クワパナ; nome opaco, invariato al plurale |
| guava | frutto (`db_item.hsp`): **il nome italiano è «guava»**, identico all'inglese. Coincidenza, come `mica`. Invariato al plurale |
| kiwi | frutto (`db_item.hsp`): nome italiano identico all'inglese, invariato al plurale |
| aloe | pianta (`db_item.hsp`): nome italiano identico all'inglese, invariato al plurale |
| anemone | fiore (`db_item.hsp`), giapponese アネモネの花: nome italiano identico all'inglese al singolare. Il plurale italiano è «anemoni» e sta nel campo `plurale`, che questa lista non tocca |
| gazania | fiore (`db_item.hsp`), giapponese ガザニアの花: nome italiano identico all'inglese al singolare, plurale «gazanie» |
| Mani | divinità di Elona (`db_item.hsp`: statua e gemma), giapponese マニ. Nome opaco del canone. ⚠️ **La maiuscola non è decorativa**: «mani» minuscolo è una parola italiana comunissima, e la statua si legge «statua di Mani» |
| Yacatect | divinità di Elona (`db_item.hsp`), giapponese ヤカテクト; nome opaco del canone |
| Kumiromi | divinità di Elona (`db_item.hsp`), giapponese クミロミ; nome opaco del canone |
| Ehekatl | divinità di Elona (`db_item.hsp`), giapponese エヘカトル; nome opaco del canone |
| Jure | divinità di Elona (`db_item.hsp`), giapponese ジュア; nome opaco del canone |
| Lulwy | divinità di Elona (`db_item.hsp`), giapponese ルルウィ; nome opaco del canone |
| Opatos | divinità di Elona (`db_item.hsp`), giapponese オパートス; nome opaco del canone |
| `<Jure>` | la stessa divinità **come creatura** (`db_creature.hsp`, razza `god`), giapponese 《癒しのジュア》. ⚠️ Le sette righe qui sopra sono i nomi **nudi**, che compaiono in `db_item.hsp`; questa è un'altra stringa, e il confronto di `verifica.py` è sulla stringa intera. L'inglese tiene solo il nome proprio e lascia cadere l'epiteto giapponese: la forma fra `<>` è quella che il gioco mostra, e non prende articolo |
| `<Lulwy>` | come sopra, giapponese 《風のルルウィ》 |
| `<Opatos>` | come sopra, giapponese 《地のオパートス》 |
| `<Kumiromi>` | come sopra, giapponese 《収穫のクミロミ》 |
| `<Ehekatl>` | come sopra, giapponese 《幸運のエヘカトル》 |
| `<Mani>` | come sopra, giapponese 《機械のマニ》 |
| `<Itzpalt>` | come sopra, giapponese 《元素のイツパロトル》 |
| `<Yacatect>` | come sopra, giapponese 《富のヤカテクト》 |
| `<Deus ex manina>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《デウス・エクス・マニナ》: è **latino** in tutte e tre le lingue, e il gioco di parole su `<Mani>` si perde a toccarlo |
| `<Yayauhqui Tezcatlipoca>` | divinità azteca (`db_creature.hsp`), giapponese 《黒き軍神テスカトリポカ》. L'epiteto giapponese dice «nero dio della guerra» e l'inglese lo rende col nahuatl *yayauhqui*, che vuol dire «nero»: due modi di dire la stessa cosa, e nessuno dei due è italiano da tradurre |
| `<Tezcatlipoca>` | come sopra, giapponese 《夜煙のテスカトリポカ》 |
| `<Mikraanesis>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《結束のミクラネシス》; nome opaco |
| `<Enthumesis>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《混沌のエンテュメイシス》; nome opaco |
| `<Urcaguary>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《剛石のウリカグアル》; nome opaco, dalla mitologia inca |
| `<Karavika>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《歌踊のカラヴィカ》; nome opaco |
| `<Garziem>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《鉄騎のガルジエム》; nome opaco |
| `<Rovid>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《守護のロヴィト》; nome opaco |
| `<Sinaha>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《不幸のシナア》; nome opaco |
| `<Arasiel>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《砂嵐のラシエル》; nome opaco |
| `<Amurdad>` | divinità di Elona+ (`db_creature.hsp`), giapponese 《永遠のネヘルタード》. ⚠️ Le due lingue usano **nomi diversi** — l'inglese pesca lo zoroastriano *Amurdad*, il giapponese *Nehertard* — e quando non descrivono la stessa cosa non stanno descrivendo, stanno nominando. Come `anering` |
| `<Big Daddy>` | creatura unica (`db_creature.hsp`, razza `machinegod`), giapponese 『ビッグダディ』. Citazione da *BioShock*, come `<Little Sister>` che sta gia' in questa lista: i due nomi vanno insieme, e in italiano il gioco non e' mai stato tradotto |
| Lomias | personaggio di Elona (`db_item.hsp`: l'esperienza segreta), giapponese ロミアス; nome proprio opaco |
| Aurtehom | libro orribile di Elona+ (`db_item.hsp`), giapponese アウルテホム, traslitterato; nome opaco alla maniera di Lovecraft |
| Bokonon | il libro di Bokonon, citazione da *Ghiaccio-nove* di Vonnegut (`db_item.hsp`), giapponese ボコノン: in italiano il romanzo lo lascia «Bokonon» |
| soma | la bevanda vedica (`db_item.hsp`: pozione superiore), giapponese ソーマ. **Parola italiana identica all'inglese** nel significato religioso. ⚠️ Esiste anche l'italiano «soma» femminile, «bestia da soma»: è un omografo, non una traduzione |
| aqua sanctio | nome latino (`db_item.hsp`: pozione superiore), giapponese サンクティオ. Il latino è latino in tutte e due le lingue: tradurlo con «acqua santa» direbbe un'altra cosa |
| mana | la risorsa magica (`db_item.hsp`: pergamena e bacchetta). È lo **stesso termine** di `Mana` qui sopra, ma minuscolo, e il confronto è sensibile alle maiuscole: senza questa riga la resa corretta verrebbe segnalata |
| katana | arma (`db_item.hsp`, `/sharp/`), giapponese 刀. **Prestito acquisito in italiano**, femminile — «la katana» — e invariato al plurale come i prestiti non adattati. «Spada giapponese» sarebbe la definizione, non il nome |
| wakizashi | arma (`db_item.hsp`, `/sharp/`), giapponese 忍刀; prestito acquisito, maschile, invariato al plurale. ⚠️ Il giapponese dice 忍刀 («spada ninja»), non 脇差: l'inglese ha scelto `wakizashi` e si traduce dall'inglese |
| kunai | arma (`db_item.hsp`, `/sharp/`), giapponese 苦無; prestito acquisito, maschile, invariato al plurale |
| shuriken | arma (`db_item.hsp`, `/sharp/`), giapponese 手裏剣; prestito acquisito, maschile, invariato al plurale |
| nunchaku | arma (`db_item.hsp`, `/metal/`), giapponese 節棍; prestito acquisito, maschile, invariato al plurale |
| shakujo | bastone del monaco buddhista (`db_item.hsp`, `/metal/`), giapponese 錫杖. Meno noto degli altri quattro, ma **oggetto reale con un nome proprio**: «bastone da monaco» sarebbe una perifrasi |
| tomahawk | arma (`db_item.hsp`, `/sharp/`), giapponese 投斧 («ascia da lancio»). L'inglese ha scelto il nome algonchino, che l'italiano ha acquisito identico; maschile, invariato al plurale |
| banana | frutto (`db_item.hsp`, `/fruit/`), giapponese バナナ: **il nome italiano è «banana»**, identico all'inglese. Coincidenza, come `guava` e `kiwi`. A differenza di quelli il plurale italiano esiste ed è «banane», e sta nel campo `plurale` |
| mesugaki | pesce (`db_item.hsp`, `/fish/`), giapponese メス牡蠣 — gioco di parole su 牡蠣 «ostrica». Nome opaco e scherzoso, invariato al plurale |
| sazae | mollusco (`db_item.hsp`, `/fish/`), giapponese サザエ, *Turbo cornutus*. L'italiano non ha un nome comune per questa conchiglia: «turbante» è ambiguo e direbbe un'altra cosa. Invariato al plurale |
| fane | ortaggio inventato da Elona (`db_item.hsp`, `/vege/`), giapponese フェーン; nome opaco, invariato al plurale |
| alraunia | erba di Elona (`db_item.hsp`, `/herb/`), giapponese アルローニア; nome opaco del canone, invariato al plurale. Femminile per la desinenza |
| spenseweed | erba di Elona (`db_item.hsp`, `/herb/`), giapponese スペンスウィード; nome opaco, invariato al plurale |
| mareilon | erba di Elona (`db_item.hsp`, `/herb/`), giapponese マレイロン; nome opaco, invariato al plurale |
| morgia | erba di Elona (`db_item.hsp`, `/herb/`), giapponese モージア; nome opaco, invariato al plurale. Femminile per la desinenza |
| dernefia | fiore di Elona (`db_item.hsp`, `/hana/`), giapponese デルネフィアの花. Il giapponese dice «il fiore di dernefia», l'inglese solo il nome: si traduce dall'inglese. Invariato al plurale |
| chip | componente elettronico (`db_item.hsp`, `/sf/`), giapponese チップ: **parola italiana identica all'inglese**, prestito acquisito nell'informatica. Invariato al plurale, come tutti i prestiti non adattati |
| server | macchina (`db_item.hsp`, `/sf/`), giapponese サーバー; prestito acquisito, maschile, invariato al plurale |
| computer | macchina (`db_item.hsp`, `/sf/`), giapponese コンピューター; prestito acquisito, maschile, invariato al plurale. ⚠️ «calcolatore» esiste ma in un gioco suonerebbe d'epoca |
| molotov | arma (`db_item.hsp`, `/nogive/`), giapponese 火炎瓶. In italiano «molotov» è il nome corrente della bottiglia incendiaria; femminile per il sostantivo sottinteso, invariato al plurale |
| mochi | dolce (`db_item.hsp`, `/fest/`), giapponese もち; prestito acquisito, maschile, invariato al plurale |
| yith-yaki | cibo di festa (`db_item.hsp`, `/fest/`), giapponese イス焼き — gioco di parole fra gli Yith di Lovecraft e il suffisso 焼き «alla griglia». Nome opaco e scherzoso, invariato |
| crimberry | bacca inventata da Elona (`db_item.hsp`, `/noshop/`), giapponese クラムベリー. «crim» è già del canone (`crim ale` → «birra crim»); nome opaco, femminile per il sostantivo «bacca», invariato al plurale |
| trismagistus | materia di Elona (`db_item.hsp`, `/magi/`), giapponese トリス・マギストス; nome opaco del canone, invariato al plurale |
| magistus | materia di Elona (`db_item.hsp`, `/magi/`), giapponese マギスト; nome opaco del canone, invariato al plurale |
| `<HL-KRSW>` | artefatto (`db_item.hsp`, `/sf/`), giapponese 《HL-KRSW》: una sigla, che non si traduce in nessuna lingua |
| `<Mauser C96 Custom>` | artefatto (`db_item.hsp`, `/sf/`), giapponese 《マウザーC96カスタム》: nome commerciale di un'arma reale, che in italiano si scrive uguale |
| `<Rail Gun>` | artefatto (`db_item.hsp`, `/sf/`), giapponese 《レールガン》. L'italiano usa «rail gun» così com'è: «cannone a rotaia» è la definizione da enciclopedia, non il nome |
| <AA-12 Advance> | artefatto (`db_item.hsp`), giapponese 《AA-12アドバンス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Al'ud> | artefatto (`db_item.hsp`), giapponese 《アル・ウード》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Amulet of Yekub> | artefatto (`db_item.hsp`), giapponese 《イェーキュブ・スフィア》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Arbalest> | artefatto (`db_item.hsp`), giapponese 《アルバレスト》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Argent Snow> | artefatto (`db_item.hsp`), giapponese 《アルジェントスノウ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Asteroid Belt> | artefatto (`db_item.hsp`), giapponese 《アステロイドベルト》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Astral Sickle> | artefatto (`db_item.hsp`), giapponese 《ネイベル・ネクス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Bamagicar> | artefatto (`db_item.hsp`), giapponese 《破竹魔甲冑》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Bambnir> | artefatto (`db_item.hsp`), giapponese 《バンブニール》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Beetle Cyborg> | artefatto (`db_item.hsp`), giapponese 《ビートルパワーボーグ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Blood Moon> | artefatto (`db_item.hsp`), giapponese 《ブラッドムーン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Blood Rod> | artefatto (`db_item.hsp`), giapponese 《ブラッドロッド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Bloody Tears> | artefatto (`db_item.hsp`), giapponese 《ブラッディ・ティアーズ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Claymore> | artefatto (`db_item.hsp`), giapponese 《クレイモア》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Clothworld> | artefatto (`db_item.hsp`), giapponese 《世界制服》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Crown Point> | artefatto (`db_item.hsp`), giapponese 《クラウンポイント》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Dal-i-thalion> | artefatto (`db_item.hsp`), giapponese 《ダル=イ=サリオン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <DGT-101> | artefatto (`db_item.hsp`), giapponese 《DGT-101》: **sigla o numero di modello**, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| <Dokuro-Mikaduki> | artefatto (`db_item.hsp`), giapponese 《髑髏三日月》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Drake Rod> | artefatto (`db_item.hsp`), giapponese 《ドレイクロッド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Dreadnought> | artefatto (`db_item.hsp`), giapponese 《ドレッドノート》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Elemental Staff> | artefatto (`db_item.hsp`), giapponese 《エレメンタルスタッフ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Elements Eyes> | artefatto (`db_item.hsp`), giapponese 《エレメントアイズ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Engoku> | artefatto (`db_item.hsp`), giapponese 《炎獄曼荼羅》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Epeclair> | artefatto (`db_item.hsp`), giapponese 《エペクレイル》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Flame Edge> | artefatto (`db_item.hsp`), giapponese 《フレイムザンバー》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Flash Crossbow> | artefatto (`db_item.hsp`), giapponese 《フラッシュボウガン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Fright Prawn> | artefatto (`db_item.hsp`), giapponese 《エビフライト》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <G3-EXA> | artefatto (`db_item.hsp`), giapponese 《G3-EXA》: **sigla o numero di modello**, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| <GAU-17 Custom> | artefatto (`db_item.hsp`), giapponese 《GAU-17ミニガン改》: **modello d'arma reale**, come `<Mauser C96 Custom>`. La sigla non si traduce, e `Custom` fa parte del nome commerciale |
| <Gemini> | artefatto (`db_item.hsp`), giapponese 《カストル＆ポルックス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Genocide Tail> | artefatto (`db_item.hsp`), giapponese 《ジェノサイドテール》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Go-Renge> | artefatto (`db_item.hsp`), giapponese 《伍連華草》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Gouten> | artefatto (`db_item.hsp`), giapponese 《轟天》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Grandel> | artefatto (`db_item.hsp`), giapponese 《グランデイル》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Gravitail> | artefatto (`db_item.hsp`), giapponese 《グラヴィテール》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Gravity Axe> | artefatto (`db_item.hsp`), giapponese 《グラビトンアクス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Griffon> | artefatto (`db_item.hsp`), giapponese 《イーグル＆レオン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Guliwelzen> | artefatto (`db_item.hsp`), giapponese 《グリエルゼン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Gur Bagh Nakh> | artefatto (`db_item.hsp`), giapponese 《ガルバグナウ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Hairmet> | artefatto (`db_item.hsp`), giapponese 《ヘアメット》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Harakiri> | artefatto (`db_item.hsp`), giapponese 《腹切丸》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Heltiarre> | artefatto (`db_item.hsp`), giapponese 《ヘルティアーレ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Hiden Mashi> | artefatto (`db_item.hsp`), giapponese 《秘伝魔紙》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Hiryu-To> | artefatto (`db_item.hsp`), giapponese 《飛竜刀》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Holy Lance> | artefatto (`db_item.hsp`), giapponese 《ホーリーランス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Honegum> | artefatto (`db_item.hsp`), giapponese 《骨噛矛》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Housenka> | artefatto (`db_item.hsp`), giapponese 《大太刀鳳閃火》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Ion Chakram> | artefatto (`db_item.hsp`), giapponese 《イオンチャクラム》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Ivy Spine> | artefatto (`db_item.hsp`), giapponese 《アイヴィ・スパイン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Kaneituuhou> | artefatto (`db_item.hsp`), giapponese 《寛永通宝》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Kani-Kama> | artefatto (`db_item.hsp`), giapponese 《カニカマ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Kill Kill Piano> | artefatto (`db_item.hsp`), giapponese 《キルキルピアノ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Kindness Blade> | artefatto (`db_item.hsp`), giapponese 《カインドネス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Konmou Happa> | artefatto (`db_item.hsp`), giapponese 《金毛発破》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Kumiromi Scythe> | artefatto (`db_item.hsp`), giapponese 《クミロミサイズ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Lucky Almonds> | artefatto (`db_item.hsp`), giapponese 《ラッキーアーモンド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Lucky Dagger> | artefatto (`db_item.hsp`), giapponese 《ラッキーダガー》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Mag-Abyss> | artefatto (`db_item.hsp`), giapponese 《アルアビス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Melodyus> | artefatto (`db_item.hsp`), giapponese 《メロディウス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Mighty Arms> | artefatto (`db_item.hsp`), giapponese 《GARMS-2》: **sigla o numero di modello**, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| <Moku-Jin> | artefatto (`db_item.hsp`), giapponese 木人: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Moonlight> | artefatto (`db_item.hsp`), giapponese 《ムーンライトセーバー》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Necromantis> | artefatto (`db_item.hsp`), giapponese 《邪成鎌ネクロマンティス》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Negative Edge> | artefatto (`db_item.hsp`), giapponese 《ネガティブエッヂ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Nightmare> | artefatto (`db_item.hsp`), giapponese 《ナイトメア》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Nova Grenade> | artefatto (`db_item.hsp`), giapponese 《ノヴァ・グレネード》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Numenius> | artefatto (`db_item.hsp`), giapponese 《ヌメニウス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Oti-Tubaki> | artefatto (`db_item.hsp`), giapponese 《落椿》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Otogiri> | artefatto (`db_item.hsp`), giapponese 《音切爪》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Palmia Pride> | artefatto (`db_item.hsp`), giapponese 《パルミア・プライド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Rankis> | artefatto (`db_item.hsp`), giapponese 《ランキス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Rasen> | artefatto (`db_item.hsp`), giapponese 《ダブルヘリックス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Ravenbrand> | artefatto (`db_item.hsp`), giapponese 《レイヴンブランド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Rinkhals> | artefatto (`db_item.hsp`), giapponese 《リンカルス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Saber Tonfa> | artefatto (`db_item.hsp`), giapponese 《ST-04 セイバー》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sacrifice Tonfa> | artefatto (`db_item.hsp`), giapponese 《ST-01 サクリファイス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sasumata> | artefatto (`db_item.hsp`), giapponese 《不殺の刺又》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Scorpierce> | artefatto (`db_item.hsp`), giapponese 《スコル・ピアス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sealed Shield> | artefatto (`db_item.hsp`), giapponese 《シールド・シールド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Shield Tonfa> | artefatto (`db_item.hsp`), giapponese 《ST-02 シールド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Smash Tonfa> | artefatto (`db_item.hsp`), giapponese 《ST-03 スマッシュ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Solar Cane> | artefatto (`db_item.hsp`), giapponese 《リボルケイン》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sonic Broom> | artefatto (`db_item.hsp`), giapponese 《ソニックブルーム》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sonic Tonfa> | artefatto (`db_item.hsp`), giapponese 《ST-05 ソニック》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Spadille> | artefatto (`db_item.hsp`), giapponese 《スパディール》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Stone Coin> | artefatto (`db_item.hsp`), giapponese 《ライ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Stormbringer> | artefatto (`db_item.hsp`), giapponese 《ストームブリンガー》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Stradivarius> | artefatto (`db_item.hsp`), giapponese 《ストラディバリウス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Sunbararia Helm> | artefatto (`db_item.hsp`), giapponese 《スンバラリアヘッド》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <The White Hawk> | artefatto (`db_item.hsp`), giapponese 《ウィーテハウク》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Trishula> | artefatto (`db_item.hsp`), giapponese 《トリシューラ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Turahagi> | artefatto (`db_item.hsp`), giapponese 《ツラハギ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Twin Edge> | artefatto (`db_item.hsp`), giapponese 《ツインエッジ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Unicorn Drill> | artefatto (`db_item.hsp`), giapponese 《スパイラルカオス》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Usamimi> | artefatto (`db_item.hsp`), giapponese 《ウサミミ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Valkoinen Kuolema> | artefatto (`db_item.hsp`), giapponese 《ベーラヤ・スメルチ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Vanilla Rock> | artefatto (`db_item.hsp`), giapponese 《バニラロック》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <War Suit> | artefatto (`db_item.hsp`), giapponese 《ウォースーツ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Winchester Premium> | artefatto (`db_item.hsp`), giapponese 《ウィンチェスター・プレミアム》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Wind Bow> | artefatto (`db_item.hsp`), giapponese 《ウィンドボウ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Yohualli Tezcatl> | artefatto (`db_item.hsp`), giapponese 《ヨワリ・テスカトル》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Yomi-To> | artefatto (`db_item.hsp`), giapponese 《黄泉戸欠片》: **l'inglese è già una romanizzazione o una coniazione**, non una descrizione. Come `<Zantetsuken>`: se l'inglese non dice niente, non c'è niente da rendere |
| <Zugaikurai> | artefatto (`db_item.hsp`), giapponese 《ズガイクライ》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| <Zwiebel> | artefatto (`db_item.hsp`), giapponese 《ゴルネ・ツィーベル》, **traslitterato** in katakana dentro la marca 《》: quando l'originale traslittera non legge il nome come descrizione. Come `<Mournblade>` |
| slot machine | macchina da gioco d’azzardo (`db_item.hsp`), giapponese スロットマシーン: **prestito acquisito in italiano**, femminile e invariato al plurale. «Macchina mangiasoldi» è gergo, non il nome |
| hamburger | panino (`db_item.hsp`), giapponese ハンバーガー: **prestito acquisito in italiano**, maschile e invariato al plurale. «Panino di carne» sarebbe la definizione, non il nome |
| tofu | alimento (`db_item.hsp`), giapponese とうふ: **parola italiana identica all'inglese**, maschile e invariata al plurale. Coincidenza come `mica` e `guava` |
| natto | alimento (`db_item.hsp`), giapponese 納豆: prestito acquisito, maschile e invariato al plurale. In italiano la soia fermentata si chiama «natto» |
| yogurt | alimento (`db_item.hsp`), giapponese ヨーグルト: **grafia italiana corrente identica all'inglese**, come `whisky`. Maschile, invariato al plurale |
| osiruko | dolce giapponese (`db_item.hsp`), giapponese おしるこ: l'inglese e' gia' una **romanizzazione**, non una descrizione, e l'italiano non ha un nome per questa zuppa di fagioli azuki. Maschile, invariato |
| ozouni | zuppa di capodanno (`db_item.hsp`), giapponese お雑煮: l'inglese e' una romanizzazione, come `osiruko`. Maschile, invariato |
| kagami mochi | dolce di capodanno (`db_item.hsp`), giapponese 鏡もち: romanizzazione, e `mochi` e' gia' invariato nel dizionario. Maschile, invariato |
| bannou mugi | cereale di Elona (`db_item.hsp`), giapponese 万能ムギ: l'inglese e' una romanizzazione. Nome opaco, maschile, invariato |
| b-jerky | cibo di Elona+ (`db_item.hsp`), giapponese ビジャーキー: **coniazione**, non una descrizione. Nome opaco, maschile, invariato |
| putitoro | cibo di Elona (`db_item.hsp`), giapponese プチトロ: nome opaco e scherzoso, come `mesugaki`. Maschile, invariato |
| romias | cibo di Elona+ (`db_item.hsp`), giapponese ロミアス: e' il personaggio `Lomias`, gia' invariato, con la r/l del giapponese. Nome proprio opaco, maschile, invariato |
| stomafillia | erba di Elona (`db_item.hsp`), giapponese ストマフィリア: nome opaco del canone, come `alraunia`. Femminile per la desinenza, invariata al plurale |
| curaria | erba di Elona (`db_item.hsp`), giapponese キュラリア: nome opaco del canone, come `morgia`. Femminile per la desinenza, invariata al plurale |
| ocarina | strumento musicale (`db_item.hsp`), giapponese オカリナ: **parola italiana identica all'inglese** — l'ocarina e' un'invenzione italiana e il nome e' il nostro. Coincidenza come `mica` e `guava`, non una traduzione dimenticata |
| daruma | bambola portafortuna (`db_item.hsp`), giapponese だるま: nome opaco, oggetto giapponese senza nome italiano. Maschile, invariato al plurale |
| kotatsu | tavolo riscaldato (`db_item.hsp`), giapponese こたつ: prestito acquisito nei testi italiani sul Giappone; «tavolo riscaldato» sarebbe la definizione, non il nome |
| chochin | lanterna di carta (`db_item.hsp`), giapponese 提灯: l'inglese e' gia' una **romanizzazione**, non una descrizione. `lantern` resta reso «lanterna» dove l'inglese dice lantern |
| wadaiko | tamburo giapponese (`db_item.hsp`), giapponese 和太鼓: romanizzazione, come `chochin`. Maschile, invariato al plurale |
| koma-inu | cane-leone dei santuari (`db_item.hsp`), giapponese 阿形の狛犬 e 吽形の狛犬: romanizzazione. **Una riga copre tutti e due gli oggetti**, perche' il confronto e' sulla stringa inglese e in inglese sono lo stesso nome |
| zizou | statua di Jizo (`db_item.hsp`), giapponese 地蔵: romanizzazione di un nome proprio buddhista. «Statua di Jizo» sarebbe la definizione |
| kumiromi-gurumi | peluche di Kumiromi (`db_item.hsp`), giapponese くみろみぐるみ: **coniazione** sul giapponese ぬいぐるみ, e l'inglese la riporta tale e quale. Nome opaco e scherzoso, come `yith-yaki` |
| TZ500-K | sigla di modello (`db_item.hsp`), giapponese TZ500-K型麻酔銃: numero di modello, che non si traduce in nessuna lingua. Come `<HL-KRSW>`. I quattro fucili anestetici `TZ` si distinguono solo per la sigla |
| TZC-500 | sigla di modello (`db_item.hsp`), giapponese TZC-500型麻酔銃: numero di modello, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| TZ30-C | sigla di modello (`db_item.hsp`), giapponese TZ30-C型麻酔銃: numero di modello, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| TZ-30 | sigla di modello (`db_item.hsp`), giapponese TZ-30型麻酔銃: numero di modello, che non si traduce in nessuna lingua. Come `<HL-KRSW>` |
| M202 special | lanciarazzi (`db_item.hsp`), giapponese M202スペシャル: **arma reale**, e `M202` e' la sua designazione militare. Come `<Mauser C96 Custom>` |
| panzerfaust X | lanciarazzi (`db_item.hsp`), giapponese パンツァーファウストＸ: **arma reale**, e in italiano il Panzerfaust si chiama cosi' |
| G-Finger | attrezzo di Elona+ (`db_item.hsp`), giapponese Ｇフィンガー: sigla piu' parola, coniazione opaca. Non c'e' una descrizione da rendere |
| waribasi | bacchette usa e getta (`db_item.hsp`), giapponese わりばし: l'inglese e' gia' una **romanizzazione**. «Bacchette usa e getta» sarebbe la definizione, non il nome |
| kiseru | pipa giapponese (`db_item.hsp`), giapponese キセル: romanizzazione. `tobacco pipe` resta reso «pipa» dove l'inglese dice pipe: sono due oggetti diversi e l'inglese li distingue cosi' |
| hamaki | sigaro (`db_item.hsp`), giapponese 葉巻. ⚠️ Il giapponese dice la **parola comune** per sigaro, ma l'inglese ha scelto di romanizzarla invece di tradurla, e si traduce dall'inglese. Come `wakizashi`, dove il giapponese diceva 忍刀 |
| hanabi | fuochi d'artificio (`db_item.hsp`), giapponese 連装花火ランチャー: l'inglese romanizza 花火. Nome opaco, maschile, invariato |
| kemuridama | bomba fumogena (`db_item.hsp`), giapponese 煙玉: romanizzazione, come `hanabi` |
| nyoi mimikaki | attrezzo di Elona+ (`db_item.hsp`), giapponese 如意耳掻棒: romanizzazione di un nome scherzoso. Nome opaco |
| mimirrocry | attrezzo di Elona+ (`db_item.hsp`), giapponese ミラクリー: **coniazione**, opaca in tutte e due le lingue |
| spiritium | materia di Elona (`db_item.hsp`), giapponese スピリチウム: nome opaco del canone, come `magistus` e `rubynus` |
| anering | attrezzo di Elona+ (`db_item.hsp`), giapponese アネワッシャー: coniazione opaca. ⚠️ Le due lingue coniano **cose diverse** — il giapponese dice «rondella», l'inglese «anello» — e questo conferma che non e' una descrizione |
| magatama | perla ricurva (`db_item.hsp`), giapponese 火吸の勾玉: prestito acquisito nei testi italiani sul Giappone, e il 勾玉 non ha un nome italiano. Maschile, invariato al plurale |
| magaice | perla ricurva (`db_item.hsp`), giapponese 冷吸の勾玉: **coniazione** su `magatama` piu' `ice`, e la stessa famiglia di `magaqua`. Nome opaco, come il capostipite |
| magaqua | perla ricurva (`db_item.hsp`), giapponese 被水の勾玉: coniazione su `magatama` piu' `aqua`, come `magaice` |
| hibachi | braciere giapponese (`db_item.hsp`), giapponese 火鉢: prestito acquisito in italiano. «Braciere» direbbe un'altra cosa |
| ohuda | talismano shintoista (`db_item.hsp`), giapponese 退芭符: l'inglese e' una **romanizzazione** di お札. Nome opaco |
| b-dama | biglia (`db_item.hsp`), giapponese ビーダマ: romanizzazione di ビー玉. Nome opaco |
| surstromming | conserva di aringhe (`db_item.hsp`), giapponese シュールストレミング: **nome proprio svedese** di un alimento reale, che l'italiano usa tale e quale |
| Taktstock | bacchetta da direttore d'orchestra (`db_item.hsp`), giapponese コマンドタクト. ⚠️ **L'inglese ha scelto il tedesco**, e il tedesco resta tedesco come il latino resta latino in `aqua sanctio`. Renderlo «bacchetta» perderebbe la scelta di lingua che l'originale ha fatto |
| E.G.G | attrezzo di Elona+ (`db_item.hsp`), giapponese E,G,G: **sigla**, non una parola. Come `<HL-KRSW>` |
| expoopsion | esplosivo di Elona+ (`db_item.hsp`), giapponese エクソプロージョン: **coniazione** scherzosa su `explosion`. Nome opaco |
| echinobox | attrezzo di Elona+ (`db_item.hsp`), giapponese エキノボックス: coniazione opaca |
| fukagurumi | oggetto di Elona+ (`db_item.hsp`), giapponese フカグルミ: coniazione opaca su ぬいぐるみ, come `kumiromi-gurumi` |
| cola | bevanda (`db_item.hsp`), giapponese コーラ: **parola italiana identica all'inglese**, femminile e invariata al plurale. Coincidenza come `mica` e `guava` |
| kombu | alga (`db_item.hsp`), giapponese 昆布: **prestito acquisito** nella cucina italiana, dove l'alga si chiama cosi'. Maschile, invariato al plurale |
| wakame | alga (`db_item.hsp`), giapponese ワカメ: prestito acquisito, come `kombu` |
| mozuku | alga (`db_item.hsp`), giapponese もずく: l'italiano non ha un nome per *Cladosiphon okamuranus*, e l'inglese si limita a romanizzare. Nome opaco |
| marimo | palla d'alga (`db_item.hsp`), giapponese 巨大マリモ: nome opaco, e l'italiano usa «marimo» quando ne parla. Maschile, invariato |
| buergeri | pesce (`item_data.hsp`), giapponese キンブナ: upstream usa l'**epiteto di specie latino** come nome comune. Un epiteto latino non si traduce, si cita — stessa classe di `<Turahagi>` fra gli artefatti. Maschile, invariato |
| longipinnis | pesce (`item_data.hsp`), giapponese ビワタナゴ: epiteto di specie latino, come `buergeri` |
| grandoculis | pesce (`item_data.hsp`), giapponese ニゴロブナ: epiteto di specie latino, come `buergeri` |
| rhombeus | pesce (`item_data.hsp`), giapponese カネヒラ: epiteto di specie latino, come `buergeri` |
| barbus | pesce (`item_data.hsp`), giapponese ニゴイ: **genere** latino usato come nome comune, come `buergeri` |
| remora | pesce (`item_data.hsp`), giapponese コバンザメ: **parola italiana identica all'inglese**, e viene dal latino. Femminile, plurale «remore». Coincidenza come `cola` e `mica` |
| shishamo | pesce (`item_data.hsp`), giapponese シシャモ: l'italiano non ha un nome per *Spirinchus lanceolatus*, e l'inglese si limita a romanizzare. Nome opaco, come `mozuku` |
| moopy | pesce (`item_data.hsp`), giapponese ムーピー: creatura di Elona, **nome proprio del bestiario**. Nome opaco |
| yruas | pesce (`item_data.hsp`), giapponese マンサ: coniazione opaca, e l'inglese non romanizza nemmeno il giapponese. Nome opaco |
| leggings | indumento da pescare (`item_data.hsp`), giapponese スパッツ: **prestito acquisito** in italiano, dove il capo si chiama cosi'. Maschile plurale, invariato |
| # | simbolo, non testo: `item_data.hsp:151` lo aggiunge come marcatore accanto al `*` che sta gia' qui sopra. Non c'è niente da tradurre |
| ] | simbolo, non testo: `item_data.hsp:567` chiude l'etichetta `[Mass. N]` del livello d'incantamento. La parentesi aperta si traduce perché porta la parola, questa non porta niente |
| Houzanha | mossa speciale (`skill.hsp`), giapponese 土竜乱舞: l'inglese è già una **romanizzazione**, non una descrizione. Come `<Zantetsuken>` |
| Kijin Shibari | mossa speciale (`skill.hsp`), giapponese 鬼神縛り: romanizzazione, come `Houzanha` |
| Jyusou Goushin | mossa speciale (`skill.hsp`), giapponese 呪装豪身: romanizzazione, come `Houzanha` |
| Kamikakushi | mossa speciale (`skill.hsp`), giapponese 紙隠し — **gioco di parole** su 神隠し, «rapimento divino», con 紙 «carta». L'inglese romanizza; l'italiano non ha una parola per la cosa, e il gioco di parole non si trasporta |
| `*Kamikakushi* ` | il **verso** della stessa mossa (`proc.hsp:23236`), giapponese 「*紙隠し*　」. ⚠️ Come `Ensemble!`, è una stringa diversa da `Kamikakushi` qui sopra — il confronto di `verifica.py` è sulla stringa intera, e gli asterischi e lo spazio in coda la cambiano — ma la decisione è la stessa. Gli apici inversi prendono verbatim lo spazio finale, che l'inglese mette e il giapponese scrive a doppio byte |
| Kamui | mossa speciale (`skill.hsp`), giapponese 神威: romanizzazione di un nome del pantheon ainu, opaco anche in inglese |
| Elementia | mossa speciale (`skill.hsp`), giapponese エレメンティア, traslitterato: **coniazione**, non una descrizione |
| Venotrate | mossa speciale (`skill.hsp`), giapponese ヴェノトレイト, traslitterato: coniazione opaca, come `Elementia` |
| Misteltein | mossa speciale (`skill.hsp`), giapponese ミストルティン: il vischio del mito norreno, che l'italiano cita nella grafia originale |
| Aromageddon | mossa speciale (`skill.hsp`), giapponese アロマゲドン: **parola macedonia** su *aroma* e *Armageddon*, che si legge identica in italiano |
| Ensemble | mossa speciale (`skill.hsp`), giapponese アンサンブル: **prestito acquisito in italiano** nel lessico musicale, e la mossa è un'esecuzione con gli alleati. Come `bonus` |
| `Ensemble!` | il **verso** della stessa mossa (`proc.hsp:19135`), giapponese 「アンサンブル！」. ⚠️ È una stringa diversa da `Ensemble` qui sopra — il confronto di `verifica.py` è sulla stringa intera, e il punto esclamativo la cambia — ma la decisione è la stessa: il nome della mossa è già invariato, e il verso lo grida. Trovato nel lotto `fase4-proc-019`, dove `verifica` l'ha fermato per «traduzione identica all'inglese» |
| Knockout | mossa speciale (`skill.hsp`), giapponese ノックアウト攻撃: prestito acquisito in italiano, maschile. «Colpo che mette KO» sarebbe la definizione, non il nome |
| Tuin der Lusten | mossa speciale (`skill.hsp`), giapponese 快楽の園. ⚠️ **L'inglese ha scelto l'olandese**, ed è il titolo del trittico di Bosch: come `Taktstock` col tedesco e `aqua sanctio` col latino, la lingua scelta è informazione |
| ShikiOrigami-Shuriken | mossa speciale (`skill.hsp`), giapponese 式折神・荒紙手裏剣: `shuriken` è già invariato qui sopra, e `ShikiOrigami` è una **coniazione romanizzata** (式神 + 折り紙). Le altre due della famiglia traducono la parte comune — `ShikiOrigami-Gru`, `ShikiOrigami-Aereo` — e questa non ha parte comune da tradurre |
| `<Clementia>` | mossa speciale (`skill.hsp`), giapponese 【命乞い】: **nome latino**, e il latino resta latino come in `aqua sanctio` |
| `<Purge>` | mossa speciale (`skill.hsp`), giapponese *Purge*: **il giapponese la lascia già in inglese**, ed è l'etichetta `PURGE` che il glossario tiene invariata nelle descrizioni. Tradurla qui e non là spezzerebbe la coppia |
| `\"Hjckrrh.\"` | verso del corvo (`db_creature.hsp:82915`, `:83085`), giapponese 「ヒックルー」 e 「ひっくるるう」. **Onomatopea, non parola**: l'inglese la prende dal *Corvo* di Poe e in italiano non c'è niente da cambiare. ⚠️ È diventata identica all'inglese solo il 2026-08-11, quando le virgolette tipografiche `“”` sono state sostituite dalla forma protetta `\"`: prima le due stringhe differivano **per le virgolette**, cioè per un difetto |
| `\"Hjckrrh!\"` | come sopra (`db_creature.hsp:82915`, `:82921`, `:83085`), giapponese 「百苦縷々……」, 「ヒィックルー！」 e 「ひゃっくるる」 |
| `\"Hjckrrh...\"` | come sopra (`db_creature.hsp:82921`), giapponese 「ヒジュクルル！」 |
| `-` | **non è testo: è un trattino.** È la scadenza di un incarico che non ne ha (`text.hsp:11692`, giapponese 即時, «subito»), e finisce dentro `"(" + nquestdate + ")"` in una colonna larga 48 pixel fra il livello e il nome del cliente (`command.hsp:3359`, `:3365`). «(subito)» sono otto caratteri e andrebbe addosso al nome. L'inglese ha già risolto così, e la soluzione è la stessa in italiano |
| `\"` | **non è testo: è la chiusura delle virgolette.** `proc.hsp:3376`, `:3402`, `:3537` e `:3621` — quattro siti, una firma — sono `lang("」", "\"")`, cioè il segno che chiude la battuta cominciata dal blocco `if ( en )` sopra (`:3372`, `:3533`, `:3617`, toppati). Il giapponese usa 」 e l'italiano usa `"` come l'inglese, perché è la convenzione tipografica della build inglese e il progetto vieta le tipografiche `“”` (CP932 le scrive su due byte, vedi `accenti.doppi_byte_cp932`). L'identità è la resa giusta, come per `...` qui sotto |
| `[Lv. 30] Little Sister` | titolo di missione secondaria (`text.hsp:10599`), giapponese リトルシスター. **Il titolo è il nome della creatura**, e `<Little Sister>` è già invariato qui sopra: l'etichetta `[Lv. N]` la scrive l'inglese e non è testo. Non resta niente da tradurre |
| `[Lv. 80] H Sister` | titolo di missione secondaria (`text.hsp:10851`), giapponese えっちないもうと. Come sopra: `H Sister` è già invariato qui sopra |
| `...` | **non è testo: è un silenzio.** Battuta di `<Aime> la narratrice` quando la si offende (`db_creature.hsp:45494`), giapponese 「…」. La resa italiana dei puntini di sospensione è `...` — tre punti ASCII, perché `…` su un byte non esiste e la build inglese lo sbaglia (vedi `accenti.doppi_byte_cp932`) — e coincide con l'inglese per costruzione: la traduzione giusta **è** l'identità. Non c'è nessuna parola dentro |
| `?\"` | **non è testo: è punteggiatura.** Coda di una domanda spezzata fra due `lang()` (`db_creature.hsp:49873`, giapponese さん？」). Non c'è nessuna parola da tradurre, e anche qui l'identità nasce dal passaggio a `\"` |
| `HAPPY END!!` | **il giapponese è inglese anche lui**: la riga è `lang("「HAPPY END！！」", "HAPPY END!!")` (`db_creature.hsp:53276`), la bolla drago che esulta dopo aver ucciso. Stesso criterio di `Target Acquired.` qui sopra — l'autore fa dire l'inglese anche a chi legge in giapponese, e le uniche differenze fra i due rami sono i punti esclamativi a larghezza intera, che CP932 ci vieta comunque. ⚠️ Il gemello 「Pon」 della stessa creatura **non** sta qui: quello è un'onomatopea giapponese scritta in lettere latine, non una parola inglese, e si rende in italiano — «Pop» |
| `Sushi!` | **il piatto si chiama così anche in italiano**, come `udon` e `ramen` qui sopra. È il grido dell'ombrame (`db_creature.hsp:83627`), giapponese 「スシ！」. ⚠️ Lo stesso giapponese sta anche a `104858`, dove l'inglese urla `SUSHI!!!` e la stessa resa italiana **non** coincide: l'identità nasce dall'inglese di questo sito, non dalla resa, che è quella già decisa e si copia |
| `...!` | **è lo stesso silenzio della riga sopra, con un punto esclamativo.** Battuta del ninja rosso quando lo si offende (`db_creature.hsp:87626`), giapponese 「…！」: un ninja che non parla. ⚠️ Lo stesso giapponese compare anche a `88185`, dove però l'inglese ci ha messo delle parole (`W-w-what...!`) e la resa italiana torna a essere `...!` **senza** coincidere: è la prova che l'identità qui nasce dall'inglese, non dalla resa |
| `Tekeli-li, Tekeli-li` | **è il grido di Lovecraft, e in italiano si scrive così**. Battuta oziosa dello shoggoth (`db_creature.hsp:80698`), giapponese 「テケリ・リ、テケリ・リ」: le edizioni italiane di *Alle montagne della follia* tengono `Tekeli-li`, che arriva a Lovecraft da Poe. ⚠️ Non è il criterio di `Target Acquired.` — lì il giapponese è **inglese**, qui è katakana, cioè una traslitterazione giapponese di un nome che l'italiano traslittera allo stesso modo. La resa sarebbe questa **anche senza l'inglese sotto gli occhi**, che è la prova richiesta: l'identità è una proprietà del sito, non un difetto della resa. Il gemello 「Pon」 resta il contrario — onomatopea giapponese in lettere latine, e si rende |
| `Destroy! Dynamite!` | **il giapponese e' inglese anche lui**: la riga e' `lang("「Destroy！Dynamite！」", cnvtalk("Destroy! Dynamite!"))` (`db_creature.hsp:95413`), il grido dell'androide su cui viaggia la `<Lumaca>`. Stesso criterio di `HAPPY END!!` e di `Target Acquired.` — l'autore fa gridare in inglese anche a chi legge in giapponese, e le uniche differenze fra i due rami sono i punti esclamativi a larghezza intera, che CP932 ci vieta comunque. ⚠️ Nella stessa creatura 「でーんでんむーしむし」 fa il contrario: e' la filastrocca giapponese della chiocciola, e si rende con quella italiana |
| `...!!` | **è lo stesso silenzio di `...` e `...!` qui sopra, con due punti esclamativi.** È l'alleato che ha appena mangiato cibo avariato (`proc.hsp:5880`), giapponese 「……！！」: la reazione è non riuscire a dire niente. La resa italiana dei puntini è `...` — tre punti ASCII, perché `…` a due byte la build inglese lo sbaglia (vedi `accenti.doppi_byte_cp932`) — e l'identità nasce da lì, non dalla resa. ⚠️ Le altre cinque battute dello stesso `txt` **non** coincidono, ed è la prova che qui non si è copiato l'inglese: 「まずい！」 diventa «Che schifo!» dove l'inglese aveva scritto `You fool!` |
| `...?` | **e' lo stesso silenzio di `...`, `...!`, `...!!` e `......` qui sopra, con un punto interrogativo.** E' Gavela quando il giocatore gli mette in mano tre monete di platino invece di trenta (`chat.hsp:8011`), giapponese 「…？」: il silenzio perplesso che precede la battuta 「ゼロがひとつ足りないぞ」. La resa italiana dei puntini e' `...` — tre punti ASCII, perche' `…` a due byte la build inglese lo sbaglia (vedi `accenti.doppi_byte_cp932`) — e l'identita' nasce da li', non da una resa copiata: le due battute che seguono (`:8012`, `:8013`) non coincidono affatto |
| `......` | **e' lo stesso silenzio di `...`, `...!` e `...!!` qui sopra, sei punti invece di tre.** Due siti e una firma sola: la maga che decifra i tomi dell'abisso (`chat.hsp:10475`) e lo spoglio dei voti della finta assemblea (`:22725`), giapponese 「……。」. Tutt'e due le volte e' la riga che segue un `...`: monte allunga il silenzio raddoppiandolo, e la resa italiana fa lo stesso con i punti ASCII, perche' `…` a due byte la build inglese lo sbaglia (vedi `accenti.doppi_byte_cp932`). L'identita' nasce da li', non da una resa copiata — il `…。` che precede (`:10474`, `:22724`) coincide per la stessa ragione. Non c'e' nessuna parola dentro |
| `... ...` | **e' lo stesso silenzio di `...` e `......` qui sopra, spezzato in due.** `chat.hsp:3843`, giapponese 「… …」: e' la seconda delle tre pause con cui Renton legge i libri di Rachel prima di stracciarli (`:3842` e' `...`, `:3844` e' `... ... ...`). La resa italiana dei puntini e' `...` — tre punti ASCII, perche' `…` a due byte la build inglese lo sbaglia (vedi `accenti.doppi_byte_cp932`) — e l'identita' nasce da li'. ⚠️ La riga in mezzo alla scena, `:3845`, **non** coincide affatto: e' la prova che qui non si e' copiato l'inglese |
| `... ... ...` | **la terza pausa della stessa scena** (`chat.hsp:3844`), giapponese 「… … …」. Vale parola per parola quel che dice la riga qui sopra: il silenzio si allunga aggiungendo gruppi di tre punti ASCII, e monte fa lo stesso |
| `!!` | **non e' testo: e' un sussulto.** Due siti e una firma sola: Kuroya quando il giocatore lo accusa di essere il ladro di calzini (`chat.hsp:12725`) e il lavoratore precario della spada rossa (`:14528`), giapponese 「！！」. Non e' un silenzio come `...` qui sopra — e' il suo contrario, la reazione che non arriva a farsi parola — ma vale la stessa ragione: dentro non c'e' nessuna parola, e i due punti esclamativi in italiano si scrivono come in inglese. ⚠️ Il giapponese li scrive a doppia larghezza (`！！`), che CP932 codifica su due byte e la build inglese disegna sbagliati: l'identita' nasce dalla forma ASCII, non da una resa copiata |
| `Bethel...` | **non e' testo: e' un nome e un silenzio.** `chat.hsp:1591`, giapponese 「ヴェセル…。」: Larnneire pronuncia il nome di chi sta cercando e non aggiunge niente. Il nome resta invariato (`db_card.hsp:4612`, «<Bethel> il falco bianco») e i puntini di sospensione si rendono coi tre punti ASCII come `...` qui sopra: l'identita' e' la somma di due decisioni gia' prese, non una resa copiata. ⚠️ Lo stesso inglese a `db_creature.hsp:57156` **non** coincide - li' e' Rianna che singhiozza e la resa e' «Ah, Bethel...» - ed e' la prova che qui l'identita' nasce dal sito |
| `Gene` | **parola italiana identica all'inglese**, come `tofu` e `chip` qui sopra. È il titolo della scena del concepimento (`proc.hsp:4324`, `s = lang("遺伝子", "Gene")`, sfondo `bg_re14`), e 遺伝子 è esattamente «gene»: la biologia italiana usa la stessa parola, con la stessa grafia. La resa sarebbe questa **anche senza l'inglese sotto gli occhi**, che è la prova richiesta dalla scoperta 2 della trentesima sessione. ⚠️ Un titolo più italiano («Il gene», «Un nuovo gene») direbbe più dell'originale, che è un sostantivo nudo in tutte e due le lingue |
| `Ok` | **parola italiana identica all'inglese**, come `bonus` e `chip` qui sopra. È l'unico bottone della macro `promptOk` (`init.hsp:23`), giapponese 「オッケー」 — che è a sua volta il prestito inglese scritto in katakana. In italiano il bottone di conferma si chiama così in ogni interfaccia, e la resa sarebbe questa **anche senza l'inglese sotto gli occhi**. ⚠️ Non è il caso di `stryes`/`strno`, che sono parole vere e stanno in `text.hsp` |
| `/` | **non è testo: è il separatore fra mese e giorno.** `init.hsp:2225` compone la data come `anno + lang("年", " ") + mese + lang("月", "/") + giorno + lang("日", " ")`: il giapponese ci mette i suoi tre kanji, l'inglese la barra e due spazi. L'italiano scrive la data con la barra allo stesso modo, e i due spazi sono già coperti dalla riga `` ` ` `` qui sopra. ⚠️ L'ordine — anno, mese, giorno — lo decide il codice e non si può girare: la resa non lo cambia |
| `:` | **non è testo: è il separatore dell'orologio.** `init.hsp:2235` compone il tempo di gioco come `ore + lang("時間", ":") + minuti + lang("分", ":") + secondi + lang("秒", " Sec")`. I due punti separano ore e minuti in italiano esattamente come in inglese. ⚠️ Sono **due** voci con lo stesso valore — 時間 e 分 — e infatti sono la prima chiave ambigua che ha chiesto la forma lunga `(riga, en, jp)`. La terza, ` Sec`, **non** sta qui: quella diventa « sec» |
| `h` | **non è testo: è la sigla dell'ora.** `init.hsp:2227` scrive `ora + lang("時", "h")` per la data breve. L'italiano abbrevia l'ora con la stessa lettera, che viene dal latino *hora*. Una voce sola, a differenza dei due punti qui sopra |
| ` *BAN* ` | **il giapponese è inglese anche lui**: `ai.hsp:2308` è `lang(" *BAN* ", " *BAN* ")`, i due rami identici carattere per carattere. È il ghepardo che bara (`CREATURE_ID_WALL_HACK_CHEATAH` … `_SPEED_HACK_CHEATAH`) che si becca il ban e muore sul colpo — `cdata(CDATA_HP, cc) = 0` la riga dopo. «Ban» è gergo di rete e in italiano si dice così: la resa sarebbe questa **anche senza l'inglese sotto gli occhi**. Stesso criterio di `HAPPY END!!` e `Destroy! Dynamite!`. Gli apici inversi prendono verbatim i due spazi, che sono la cornice dell'effetto sonoro |
| `Vrei sa pleci dar♪` | **è un verso in rumeno**, e il rumeno resta rumeno come l'olandese di `Tuin der Lusten` e il latino di `aqua sanctio`. È *Dragostea din tei* cantata da un compagno (`ai.hsp:1452`), e il giapponese non traduce nemmeno lui: ci mette il **soramimi** 「米さ米種だろ♪」, cioè parole giapponesi vere che suonano come il rumeno. L'inglese ha stampato il verso originale, e l'italiano fa lo stesso — la resa sarebbe questa **anche senza l'inglese sotto gli occhi**. ⚠️ Vale per **questo** sito soltanto: a `:1456` lo stesso inglese sta per un soramimi giapponese diverso, e lì la resa è un soramimi italiano («Brie♪ sale♪ pece♪ dai♪»). Come `Ensemble!` e `` `*Kamikakushi* ` ``, il confronto di `verifica.py` è sulla stringa intera |
| ` + ` | **non è testo: è il segno che unisce i due membri di una coppia.** `command.hsp:282` scrive `lang("現在のターゲットは", "You are targeting ") + cdatan(...) + lang(" ＋ ", " + ") + cdatan(...)`, cioè il bersaglio e il suo compagno di *tag team* — che il glossario chiama **coppia** (`skill.hsp:1477`). Il giapponese ci mette il ＋ a **larghezza intera**, che CP932 ci vieta comunque; l'italiano scrive il più con lo stesso segno di chiunque, e l'identità con l'inglese nasce da lì, non da una resa copiata. Stessa specie di `/` e `:` qui sopra — un separatore, non una parola. Gli apici inversi prendono verbatim i due spazi, che sono quel che stacca il segno dai due nomi |
| `Noooooooooo!` | **il giapponese lo scrive in lettere latine** — `lang("「Noooooooooo！」", cnvtalk("Noooooooooo!"))`, `db_creature.hsp:95419` — e in italiano `no` e' la stessa parola dell'inglese, con lo stesso allungamento. A differenza della riga qui sopra non c'e' nemmeno una scelta d'autore da rispettare: la resa italiana **sarebbe questa comunque**, ed e' la prova richiesta dalla scoperta 2 della trentesima sessione. L'identita' e' una proprieta' del sito |
| `Nooooo!` | **lo stesso caso con cinque «o» invece di dieci**, ed è il primo capriccio del figlio appena nato (`command.hsp:15141`, 「イヤぁぁあ！」). Qui il giapponese **non** è in lettere latine — è il katakana allungato — quindi l'identità non la dichiara upstream: nasce dal fatto che il «no» allungato si scrive uguale nelle due lingue. Le altre tre voci dello stesso array si scostano dall'inglese («Nooo!», «No e no!», «Nooo!!!!!!»), e proprio per quello questa resta: se anche la più lunga si fosse dovuta storcere, sarebbe stato per far contenta `verifica.py` e non per l'italiano |
| `Noooooooooooooo!` | **il terzo esemplare della famiglia**, con quattordici «o»: `tcg.hsp:2791`, il bottone che esce quando si perde al gioco di carte. Vale parola per parola quel che dicono le due righe qui sopra — in italiano `no` è la stessa parola dell'inglese, e le «o» in più sono l'urlo, non la lingua. ⚠️ Il giapponese qui **non** c'entra: è 「また今度ね」, cioè «sarà per la prossima volta», riusato dal mod senza toccarlo per tre inglesi diversi. Si segue l'inglese, che è la lingua di monte della resa |
| `No` | **la parola è la stessa nelle due lingue.** È il secondo bottone dei due menu di conferma del gioco di carte (`tcg.hsp:4424` e `:4433`, giapponese 「いいえ」), accanto a «Chiudi il turno» e «Arrenditi». ⚠️ Non è il caso di `Yes`, che si traduce: `text.hsp:196` rende già 「ああ」 con «Sì». La coppia italiana è **sì/no**, e solo una delle due metà cambia forma |
| `Ma` | **è una sigla di due lettere che le due lingue scrivono uguale.** `item_func.hsp:2465` disegna in cima alla finestra dell'equipaggiamento la fila degli undici elementi, una sigla ogni 20 px, e l'undicesima è `lang("魔", "Ma")` — cioè `Magic`, che in italiano è «magia». Le prime due lettere coincidono, come `PER` e `MAG` e `mica` qui sopra: coincidenza, non una resa copiata. ⚠️ Le altre dieci sigle **cambiano tutte** (`Fi`→`Fu`, `Co`→`Ge`, `Li`→`Fl`, `Da`→`Os`, `Mi`→`Me`, `Po`→`Ve`, `Nt`→`Ol`, `So`→`Su`, `Nr`→`Ne`, `Ch`→`Ca`), e il confronto è sulla stringa intera: questa riga zittisce la voce che vale esattamente `Ma`, non la parola dentro una frase |
| `"Karma(" + locvar_modkarma_a + ")"` | **è la parola già invariata qui sopra, dentro un'espressione.** ⚠️ Il valore è l'**espressione intera**, non `Karma()`: per le voci dinamiche `verifica.py:280` confronta `en_grezzo`, cioè l'HSP completo. `module.hsp:194` scrive `lang("カルマ変動(" + a + ") ", "Karma(" + a + ")")`: il messaggio nel diario quando il karma cambia, `Karma(-5)`. Il giapponese dice «variazione di karma», ma l'inglese ha scelto la sola parola col numero fra parentesi, e in italiano `Karma` è la stessa parola — vedi la riga `Karma` qui sopra, già decisa su `command.hsp:10517`. Non resta niente da rendere: le parentesi sono parentesi |
| `"" + gdata(GDATA_YEAR) + "/" + gdata(GDATA_MONTH) + "/" + gdata(GDATA_DAY)` | **non è testo: è una data, e l'ordine non è nostro.** `main.hsp:4293` è la riga della lapide (`noteadd s, 1`), e il giapponese la scrive `年 月 日` mentre l'inglese mette due barre. L'italiano scriverebbe giorno/mese/anno — ma **l'ordine anno-mese-giorno è quello di tutte le date del gioco**, e lì il dizionario non lo può cambiare: `init.hsp:2225` compone `anno + lang("年", " ") + mese + lang("月", "/") + giorno + lang("日", " ")`, cioè l'ordine sta nel **codice** e le `lang()` toccano solo i separatori (vedi la riga `/` qui sopra). Due formati di data nello stesso gioco sarebbero peggio di uno straniero. ⚠️ Il valore è l'**espressione intera**, come per `Karma(` qui sopra: `verifica.py:280` confronta `en_grezzo` per le dinamiche |
| ` -> ` | **non è testo: è la freccia fra il grado di prima e quello di adesso.** `module.hsp:263` compone `orgrank / 100 + lang("位 → ", " -> ") + gdata(p) / 100 + lang("位 ", "")`, cioè «5 -> 3» dentro il messaggio di cambio di grado. Il giapponese ci mette il contatore 位 «posto» e la freccia a larghezza intera; l'inglese la scrive coi due segni ASCII, e l'italiano non ha una freccia diversa. Stessa specie di `/` e `:` e ` + ` qui sopra. Gli apici inversi prendono verbatim i due spazi, che staccano la freccia dai numeri |

## Valori di dato, non testo — tradurli rompe i salvataggi

Sono i valori del campo `CDATAN_NEWSEX`, **scritti** nei dati del personaggio
(`chara.hsp:2790`, `chara.hsp:4390`) e **riletti** come operandi di confronto
(`init.hsp:1813-1823` dentro `he()`/`his()`/`him()`, `text.hsp:359-375`,
`command.hsp:3639-3654`).

Tradurle sembra innocuo e non lo è: un salvataggio esistente contiene la stringa
inglese, il confronto col valore italiano fallisce, e il gioco sbaglia il genere
di ogni personaggio già creato. Il cancello della Fase 0 ha verificato proprio
che i salvataggi esistenti si carichino: questo lo vanificherebbe in silenzio.

⚠️ **Correzione del 2026-08-07.** Qui c'era scritto «queste `lang()` non
finiscono a schermo». **È falso per `male` e `female`**: `text.hsp:123-124` le
assegna a `strmale`/`strfemale`, che sono mostrate in sei punti — creazione del
personaggio (`chara.hsp:3629`, `command.hsp:4651`), scheda
(`command.hsp:10652`), `init.hsp:2074` e `text.hsp:379`. E siccome il dizionario
è indicizzato **per contenuto**, l'etichetta di riga 123 e l'operando di riga
365 sono **la stessa firma**: non si possono separare traducendo.

La separazione la fanno sei **toppe** su `text.hsp` (righe 123, 124, 366, 369,
372, 375), che traducono le sole righe di display e lasciano intatti gli
operandi. Verificato che il valore scritto nel salvataggio non deriva
dall'etichetta: `zisyousex` prende i suoi valori da `lang()` proprie
(`chara.hsp:3665-3680`), non da `strmale`/`strfemale`.

`none` **non** ha una toppa, ed è l'unica che resta inglese anche a schermo: le
sue righe di display (`text.hsp:49` e `52`) sono array che contengono altre sei
stringhe traducibili ciascuno, e siccome il dizionario passa **prima** delle
toppe la riga da cercare cambierebbe a ogni traduzione. Toppare l'operando
invece dell'etichetta non è un'alternativa: `none` viene anche **scritto**
(`chara.hsp:4390`), quindi servirebbe toccare anche quello, e a quel punto nel
salvataggio finirebbe italiano.

| valore | motivo |
|---|---|
| male | operando di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| female | operando di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| none | valore di `CDATAN_NEWSEX`, scritto e riletto. Resta inglese anche a schermo |
| hermaphrodite | valore di `CDATAN_NEWSEX` |
| hermaphorodite | **refuso di upstream**, non nostro: `chara.hsp:2790` scrive `hermaphrodite`, ma `text.hsp:359` confronta con `hermaphorodite`. In inglese quel ramo è **morto** — nessuno scrive mai quella grafia — mentre in giapponese la stringa è la stessa e funziona. È un operando, e i difetti di upstream non si correggono da qui |
| bisexual | **secondo esemplare della stessa specie di `hermaphorodite`**, trovato nella 48ª: `command.hsp:3639` confronta `CDATAN_NEWSEX` con `bisexual`, ma il valore lo scrivono `chara.hsp:2790` e `command.hsp:4686`, e tutt'e due scrivono `hermaphrodite`. In inglese il ramo è **morto** e la riga di stampa che ne dipende (`:3640`) non si raggiunge mai; in giapponese la stringa è 「両性具有」 da tutt'e due le parti e funziona. È un operando, e i difetti di upstream non si correggono da qui |
| male? | valore di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| female? | valore di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| trans-male | valore di `CDATAN_NEWSEX` |
| trans-female | valore di `CDATAN_NEWSEX` |
| EN | **non è testo, è un marcatore di formato.** `text.hsp` lo usa in 52 punti dentro `instr(buff, 0, "%DEFAULT," + lang("JP", "EN"))` per trovare la sezione di lingua nei testi esterni (`talk.txt`, `board.txt`...). Tradurlo romperebbe la lettura di ogni file esterno. Presente anche in `action.hsp`, `chat.hsp`, `command.hsp`, `help.hsp`, `chara_func.hsp`, `item_func.hsp` |

| `<` | parentesi del nome proprio, non testo: `action.hsp:4612` compone `lang("『", "<") + s(1) + lang("』", ">")` attorno al nome di un'arma unica. Il giapponese usa le sue virgolette 『』, l'inglese le parentesi angolari, e l'italiano segue l'inglese perche' e' la forma che il progetto usa gia' per i nomi propri (`<Gwen>`, `<Vansesda>`). Non c'e' nessuna parola da rendere |
| `>` | l'altra meta' della parentesi qui sopra |
| `EN` | ⚠️ **non e' testo: e' una chiave di formato.** `action.hsp:4816` fa `instr(buff, 0, t + "," + lang("JP", "EN"))` per cercare la riga `%txtName,EN` dentro i file `user\item\plan*.txt` degli oggetti personalizzati. Tradotta, la ricerca non trova piu' niente e il nome dell'oggetto sparisce. Il giapponese e' `JP`: sono i due codici di lingua, non due parole |
| `????` | ⚠️ **non e' una parola: e' un nome nascosto.** `map.hsp:6552` fa `cdatan(CDATAN_NAME, rc) = lang("？？？？", "????")` — il gioco copre l'identita' di un personaggio con quattro punti interrogativi, e quattro punti interrogativi si scrivono uguali in ogni lingua. 💡 Il giapponese li usa a **larghezza intera** (`？`), l'inglese in ASCII: la resa segue l'inglese, perche' e' il ramo che sostituisce. Dichiarato nella 42a, lotto `fase4-map-003` |
## Versi senza contenuto linguistico — non c'è niente da rendere

La creatura `@` (`CREATURE_ID_AT_SIGN`, `db_creature.hsp:80862`) emette
`「Ｑｙ＠」` in tutte e quattro le sue classi di battuta. Il giapponese lo scrive
coi caratteri a **larghezza intera**, l'inglese li ha portati in ASCII, e in
italiano non c'è nessuna parola: è il verso di una creatura che si chiama `@`.

Non è come `Baa` della pecora, che ha un'onomatopea italiana propria (`Bee`):
qui non esiste una forma italiana perché non esiste una forma linguistica.
Qualunque «traduzione» sarebbe inventata, e lasciarla identica all'inglese è la
scelta giusta — ma senza questa dichiarazione `verifica.py` la rifiuterebbe
insieme al lotto intero, e l'unico modo di far passare il lotto sarebbe
inventare qualcosa.

⚠️ **I caratteri a larghezza intera non si copiano**: `Ｑ`, `ｙ` e `＠` sono a
due byte in CP932, e la build inglese ne disegna uno per byte. Si usa la forma
ASCII, che è quella che l'inglese ha già scelto.

⚠️ **E lo stesso motivo copre un caso che verso non è.** `proc.hsp:12101` scrive
`"*" + skillname(efid) + "* "`: è l'intestazione che il gioco stampa quando parte
un'azione speciale, e **tutto il testo che il giocatore legge viene da
`skillname()`**, che il dizionario traduce altrove. Attorno restano due asterischi
e uno spazio. Il giapponese mette lo spazio a larghezza intera (`　`) e l'inglese
quello normale: l'italiano segue l'inglese, e la resa coincide con l'inglese
**per costruzione**, non per dimenticanza. Sta qui perché il criterio della
sezione è il suo titolo — non c'è niente da rendere — e non la forma della voce.

| valore | motivo |
|---|---|
| Qy@ | verso della creatura `@`, senza contenuto linguistico in nessuna lingua |
| Qy@! | il verso quando uccide |
| Qy@!! | il verso quando è furiosa |
| Q...Qy@... | il verso in punto di morte |
| `"*" + skillname(efid) + "* "` | `proc.hsp:12101`: l'intestazione dell'azione speciale. Il testo è tutto dentro `skillname()`, che è tradotto in `skill.hsp`; fuori restano due asterischi e uno spazio. Gli apici inversi la prendono verbatim, perché lo spazio finale conta |
| `Base` | `map_user.hsp:762`, la prima delle quattro voci con cui la finestra del valore della casa scompone il totale — 基本 / 家具 / 家宝 / 総合, cioè «Base», «Arredi», «Cimeli», «Totale». ⚠️ **La parola italiana giusta è identica all'inglese per combinazione**, non per dimenticanza: 基本 è il valore di partenza dell'edificio, contro quello dei mobili e dei cimeli, e in italiano si chiama base. Le altre tre della stessa riga si traducono e infatti sono tradotte. 💡 C'è anche un tetto stretto — 43 px fra l'etichetta e la prima stella, con un carattere da 10 px — che scoraggia i sinonimi lunghi, ma non è la ragione: «Base» resterebbe la resa giusta anche in una finestra larga il doppio. Dichiarato nella 60ª, lotto `fase4-map_user-003` |
| `cnvtalk(inputlog + "!!")` | `command.hsp:4465`: il gioco rimanda a schermo, gridata, **la frase che il giocatore ha appena digitato** nella finestra del desiderio. Fuori da `inputlog` non c'è nessuna parola — due punti esclamativi, e le virgolette le mette `cnvtalk`. ⚠️ Il testo è quello che ha scritto il giocatore, quindi è già nella sua lingua per definizione: non c'è niente da rendere, e una «traduzione» qui vorrebbe dire aggiungere parole che nessuna delle due lingue di monte dice. Stesso criterio della riga qui sopra, con in più il fatto che la voce è una **dinamica** e il confronto di `verifica.py` cade sull'espressione intera |
| `ninja` | `chara.hsp:2814`: la classe finta delle sei creature ninja (忍者). ⚠️ **Identica all'inglese per combinazione, non per dimenticanza**: la parola giapponese e' entrata in italiano tale e quale, e il progetto la usa gia' cosi' — `db_card.hsp:8772` rende ニンジャ con «il ninja». Qui l'articolo non c'e' perche' e' un'etichetta di classe, che il gioco mostra fra parentesi angolari (`command.hsp:4627`, `action.hsp:13706`). 💡 E' l'**unica** delle ventuno classi finte del lotto `fase4-chara-002` che resta identica: una sola eccezione e' il segno che la convenzione regge, al contrario delle cinquantadue della 54a |
| `Essential` | `chara.hsp:4175`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Essential", "Essential")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `Loss` | `chara.hsp:4176`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Loss", "Loss")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `Overdose` | `chara.hsp:4177`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Overdose", "Overdose")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `Natural` | `chara.hsp:4178`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Natural", "Natural")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `Abnormal` | `chara.hsp:4179`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Abnormal", "Abnormal")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `Claymore` | `db_class.hsp:633`, il nome della classe. Giapponese クレイモア, cioè lo **stesso prestito** che l'inglese: non c'è una parola giapponese da cui tradurre. ⚠️ La classe prende il nome dall'arma che impugna — e la descrizione lo dice esplicitamente, «l'arma prediletta è la claymore, da cui il nome» — quindi tradurre l'etichetta e lasciare l'arma, o viceversa, scollegherebbe le due. Il nome vale anche come citazione dell'opera omonima, che in italiano circola così. 💡 È l'**unica** delle tredici classi del lotto `fase4-db_class-001` che resta identica: le altre dodici si traducono, `Warmage` compreso, che il giapponese scrive 魔法戦士 cioè «mago guerriero». Dichiarata nella 64ª |
| `Purge` | `chara.hsp:4180`, uno dei sei nomi di modalita' della creazione del personaggio. ⚠️ **Il giapponese di monte li lascia in inglese tale e quale** — la riga e' `lang("Purge", "Purge")`, identica nelle due lingue — quindi non c'e' una parola giapponese da cui tradurre: e' il nome proprio della modalita', quello con cui la comunita' di Elona+ la chiama. 💡 E le schede che le descrivono lo **citano per nome** (`chara.hsp:4191`-`:4314`, trentasette righe): tradurre l'etichetta e lasciare la citazione, o viceversa, scollegherebbe le due. Dichiarati nella 63a, lotto `fase4-chara-004` |
| `<` | `chara.hsp:2331`: la parentesi che apre il nome di una creatura speciale — `lang("『", "<") + cdatan(CDATAN_NAME, rc) + …`. Stessa ragione gia' scritta qui per la coppia `< ` / ` >` di `god.hsp`: il giapponese usa le parentesi piene 『』《》, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII, perche' in CP932 le piene sono a due byte e la build inglese ne disegna uno per byte. **Non c'e' niente da tradurre: e' una cornice.** Dichiarate nella 63a, lotto `fase4-chara-005` |
| `>` | `chara.hsp:2331`: la parentesi che chiude il nome di una creatura speciale — `lang("』", ">") + cdatan(CDATAN_NAME, rc) + …`. Stessa ragione gia' scritta qui per la coppia `< ` / ` >` di `god.hsp`: il giapponese usa le parentesi piene 『』《》, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII, perche' in CP932 le piene sono a due byte e la build inglese ne disegna uno per byte. **Non c'e' niente da tradurre: e' una cornice.** Dichiarate nella 63a, lotto `fase4-chara-005` |
| `{` | `chara.hsp:2335`: la parentesi che apre il nome di una creatura speciale — `lang("《", "{") + cdatan(CDATAN_NAME, rc) + …`. Stessa ragione gia' scritta qui per la coppia `< ` / ` >` di `god.hsp`: il giapponese usa le parentesi piene 『』《》, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII, perche' in CP932 le piene sono a due byte e la build inglese ne disegna uno per byte. **Non c'e' niente da tradurre: e' una cornice.** Dichiarate nella 63a, lotto `fase4-chara-005` |
| `}` | `chara.hsp:2335`: la parentesi che chiude il nome di una creatura speciale — `lang("》", "}") + cdatan(CDATAN_NAME, rc) + …`. Stessa ragione gia' scritta qui per la coppia `< ` / ` >` di `god.hsp`: il giapponese usa le parentesi piene 『』《》, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII, perche' in CP932 le piene sono a due byte e la build inglese ne disegna uno per byte. **Non c'e' niente da tradurre: e' una cornice.** Dichiarate nella 63a, lotto `fase4-chara-005` |
| `"X" + gdata(GDATA_FLAG_REMAINING_LIVES) + " "` | `command.hsp:10434`: il contatore delle vite che restano nel modo Purge, in alto a destra nella scheda del personaggio. Fuori da `gdata()` non c'è nessuna parola: c'è il **segno del moltiplicatore**, che il giapponese scrive 「×」 e l'inglese ha reso «X». ⚠️ **Identica all'inglese per combinazione, non per dimenticanza**: l'italiano quel segno lo scrive allo stesso modo, e non ne ha un terzo. Stesso criterio del «$» di `command.hsp:3392` e delle parentesi qui sopra. 💡 La forma incollata al numero è quella di monte — `chara.hsp:4766` fa lo stesso con «Manox2» — e resta da decidere a parte, per tutt'e due i siti insieme. Dichiarato nella 66ª, lotto `fase4-command-044` |
| Necronomicon | titolo del grimorio di `item.hsp:127`, giapponese ネクロノミコン. **Nome proprio opaco**: il libro di Abdul Alhazred si chiama cosi' in italiano da sempre, e non ne esiste nessuna forma tradotta in circolazione. Identico all'inglese per combinazione, non per dimenticanza: gli altri quindici titoli della stessa tabella si traducono tutti (`Manoscritto Voynich`, `Il Ramo d'Oro`, `Frammenti di Celaeno`...). Dichiarato nella 69a, lotto `fase4-item-007` |
| `"(" + iroiro + ")"` | `event.hsp:2371`: due parentesi tonde intorno a una variabile, e basta. **Non c'è nessuna parola dentro la `lang()`**: quel che il giocatore legge lo mette `iroiro`, che è già tradotto altrove. L'italiano le parentesi le scrive uguali, e non ne ha di sue. Identica all'inglese per combinazione, non per dimenticanza — stesso criterio delle parentesi di `god.hsp` e del `X` del moltiplicatore. Lasciata fuori apposta dalla 73ª, dichiarata nella 74ª |
| `" < " + s + " > "` | `event.hsp:4171`: la **cornice del titolo** di ogni evento a schermo intero, `q = lang("《 " + s + " 》", " < " + s + " > ")`. Il titolo `s` è tradotto ognuno per conto suo; qui intorno ci sono solo due segni e i loro spazi. Il giapponese usa le parentesi piene 《 》, l'inglese le ha portate in ASCII e l'italiano tiene quelle ASCII, **per la ragione già scritta qui sopra per `< ` / ` >`**: in CP932 le piene sono a due byte e la build inglese ne disegna uno per byte. ⚠️ Gli spazi non si tolgono: sono la distanza fra il segno e il titolo. Dichiarata nella 74ª |
| Liber Damnatus | titolo del grimorio di `item.hsp:127`, giapponese 断罪の書 «il libro della condanna». ⚠️ **Il titolo e' latino, non inglese**: l'inglese di monte non l'ha tradotto e l'italiano nemmeno, per la stessa convenzione che tiene `Necronomicon`. Il giapponese qui descrive invece di nominare, ed e' il verso in cui **non** decide lui: un titolo latino in una lista di grimori del Ciclo di Cthulhu e' un nome proprio, e la lista intorno lo conferma (`Grand Grimoire`, `Necronomicon`). Dichiarato nella 69a, lotto `fase4-item-007` |
| `...???` | `chat.hsp:9829`: quel che <Alice> la formica gigante "dice" quando il giocatore, invece di curarla, le tiene la medicina alta fuori portata (`:9822`). **Non ci sono parole in nessuna delle due lingue**: tre punti e tre punti interrogativi, cioe' l'espressione di una bestia che non ha capito. Il giapponese li scrive a larghezza intera (`…？？？`) e l'inglese li ha portati in ASCII; l'italiano tiene quelli ASCII per la ragione gia' scritta qui sopra — in CP932 i pieni sono a due byte e la build inglese ne disegna uno per byte. Identica all'inglese **per costruzione**, non per dimenticanza. Dichiarata nella 92a, lotto `_92-alice` |

## Nomi di creatura riscritti nel salvataggio — non decidibili qui

⚠️ Trovate il 2026-08-07 misurando `Sister`. In `action.hsp` (Fase 1) ci sono
**424 assegnazioni** di `evname`/`evold`, il sistema di evoluzione dei nemici:
**232 valori `evold` distinti, 203 dei quali sono nomi di creatura letterali di
`db_creature.hsp`**, che è Fase 2.

Non sono testo e non sono nemmeno solo dati. Il codice fa chirurgia di stringa
sul nome memorizzato del personaggio:

```
if ( strmid(cdatan(CDATAN_NAME, cc), 0, strlen(evold)) == evold ) {
    cdatan(CDATAN_NAME, cc) = evname + strmid(cdatan(CDATAN_NAME, cc), ...)
```

`evold` è l'**operando** confrontato col nome che sta nel salvataggio; `evname`
è il pezzo che lo **sostituisce**, e quindi finisce a schermo come nuovo nome
della creatura evoluta. In inglese `evname` non è mai stampato direttamente:
l'unico `txt` che lo contiene (`action.hsp:18632`) lo ha solo nel ramo
giapponese.

Le conseguenze, nessuna delle quali si vede provandolo su una partita nuova:

- **vanno tradotti in blocco con `db_creature.hsp`**, mai prima: se `evold`
  diventa italiano e il nome della creatura no (o viceversa), il confronto
  fallisce e l'evoluzione smette di rinominare **in silenzio**;
- **rompono i salvataggi esistenti comunque li si tratti**, perché lì il nome
  memorizzato è già in inglese;
- la **prova d'identità non li prende**: come per `CDATAN_NEWSEX`, la forma
  resta giusta ed è il significato a rompersi.

Non li metto nella tabella sopra: dichiararli invariati deciderebbe di lasciare
i nomi delle creature in inglese per sempre, che è una decisione di Fase 2 e
non è stata presa. Restano segnalati da `verifica.py` come non tradotti, che è
il comportamento voluto finché la Fase 2 non li affronta.

Vedi [[stringhe-che-sono-dati]].

## Da decidere nel glossario

*Vuota dal 2026-08-07.* I cinque toponimi che stavano qui sono stati decisi con
«la regola dei nomi propri» di `glossario.md`: `Larna`, `Arcbelc` e `Lesimas`
sono saliti nella tabella degli invariati; `Port Kapul` → «Porto Kapul» e
`Cyber Dome` → «Cupola Cibernetica» si traducono e quindi qui non ci vanno.

La sezione resta perché il meccanismo serve: un candidato messo qui è segnalato
da `verifica.py`, così la decisione non passa inosservata.

## Chiavi e nomi di file — non sono testo, sono indirizzi

Aggiunta nella 72a col lotto di `help.hsp`. Tre valori che il gioco usa per
**trovare qualcosa**, non per dire qualcosa: tradurli non fa parlare italiano
nessuna schermata, fa fallire una ricerca.

| valore | motivo |
|---|---|
| `EN` | `help.hsp:228` compone `"%" + ghelp + "," + lang("JP", "EN")` e lo cerca dentro `manual_ENG.txt` con `instr`. E' **la chiave del blocco**, cioe' lo stesso marcatore `%…,EN` che regge tutti e cinque i file di `data\` (vedi la Fase 3): la sigla non si legge da nessuna parte, si confronta. Tradotta, la guida in gioco non trova piu' un argomento |
| `manual_ENG.txt` | `help.hsp:331`, argomento di un `noteload`: e' il **nome del file** del manuale, non il suo titolo. ⚠️ E il giorno in cui il manuale si traduce, questa riga non diventa una resa ma una **toppa** con `manual_IT.txt` e il ramo `exist` di ripiego — la stessa disciplina di `board_it.txt` e `talk_it.txt`, e per la stessa ragione: `noteload` su un file assente e' un errore di esecuzione, cioe' il gioco che muore |
| `scene2.hsp` | `help.hsp:819`, stesso `noteload`, stesso motivo: e' il file delle scene sbloccabili. ⚠️ Qui l'inglese e' anche fuorviante — `lang("scene1.hsp", "scene2.hsp")` sembra una versione e sono **due file diversi**, uno per lingua |
