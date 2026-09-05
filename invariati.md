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
| `[` | la parentesi che apre il nome della squadra in cima a un file di personaggi esportato (`system.hsp:3316`, `lang("【", "[")`). Stessa cosa di `< ` e ` >` qui sopra: il giapponese usa le graffe piene 【 】, l'inglese le ha portate in ASCII, e l'italiano tiene quelle ASCII perche' le piene sono a due byte e la build inglese le disegna come due glifi latini a caso. Non c'e' niente da tradurre: e' una cornice attorno a `gdatan(GDATAN_TEAM1)` |
| `]` | la parentesi che chiude, per la stessa ragione di `[`. ⚠️ Vale anche per `:3271`, dove l'apertura invece **si traduce** perche' porta una parola dentro (`[Made by][` -> `[Fatto da][`): li' la cornice e il testo stanno nella stessa stringa, qui no |
| `Direct sound` | nome del driver audio (`config.hsp:805`), non una parola: e' il valore che si scrive in `config.txt` alla chiave `sound.`, e accanto a lui il pannello mostra `MCI`, che nel sorgente non passa nemmeno da una `lang()`. Tradurlo scollegherebbe l'etichetta dal file di configurazione |
| `Direct music` | nome del driver audio (`config.hsp:809`), per la stessa ragione di `Direct sound`. Il terzo e il quarto valore della stessa riga sono `MCI` e `GuruGuruSMF4`, letterali nudi che nessun dizionario raggiunge |
| `Spongebob` | nome di un modo di scrivere i nomi degli oggetti (`config.hsp:944`), accanto a `Capitalize`, `Uppercase`, `Lowercase` e `Schizophrenic`. E' la citazione del meme del testo aLtErNaTo, che in italiano circola con lo stesso nome inglese; e il giapponese qui non aiuta, perche' dice 「表示」 per tutt'e cinque i modi |
| `Info` | il nome della prima pagina della ruota dei comandi (`help.hsp:58`), giapponese 情報. ⚠️ **Non e' inglese lasciato li': e' italiano che coincide.** «Info» e' l'abbreviazione corrente in italiano, e la forma piena — «Informazioni», dodici caratteri — non ci sta: gli slot 0, 4 e 8 della ruota hanno passo 75 px a 7 px per carattere (`help.hsp:105`), cioe' **dieci**. Le altre tre pagine si traducono e infatti si sono tradotte: «Azioni», «Speciali», «Zaino» |
| `t ` | l'abbreviazione dei turni nella colonna «Effetto» del menu degli incantesimi (`command.hsp:9004`), giapponese ターン. ⚠️ **Non e' inglese lasciato li': e' italiano che coincide**, come `Info` qui sopra: la parola e' «turno», l'abbreviazione italiana e' la stessa lettera, e il pezzo non e' una voce ma un frammento — la riga che si compone e' `"" + dur + lang("ターン ", "t ")` piu' `buffdesc`, dentro la colonna piu' stretta delle tre (da `wx + 460` al bordo dei 720 px). ⭐ Il progetto scrive «Turni» per esteso dove c'e' posto (`command.hsp:10526`, `:10754`, `blend.hsp:379`): qui non ce n'e' |
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
| `{} Console` | il titolo della sezione della guida in gioco che spiega la console (`data\manual_ENG.txt`). ⚠️ **Non è inglese lasciato lì: è italiano che coincide**, come `Info` e `t ` qui sopra — «console» è la parola italiana per quella finestra, e i comandi che ci si scrivono dentro (`wizard`, `freemove`, `exitroom`, `removequest`) sono chiavi che il codice confronta tal quali. Il `{}` in testa non è un segnaposto ma il marcatore di sezione che `help.hsp:338` cerca per riempire l'elenco degli argomenti |
| Vernis | nome proprio di città, canone Elona |
| Palmia | nome proprio di città, canone Elona |
| Derphy | nome proprio di città, canone Elona |
| Noyel | nome proprio di città, canone Elona |
| Yowyn | nome proprio di città, canone Elona |
| `"(" + moneyboxn(inv(INV_ITEM_PARAM2, itemowner_itemid)) + ")"` | il saldo del salvadanaio (`item_func.hsp:695`), giapponese senza parentesi. **Non e' testo, e' una cornice attorno a `moneyboxn()`**, che scrive quante monete ci sono dentro: «un salvadanaio (1200)». Le tonde sono la punteggiatura italiana per un inciso numerico esattamente come per quello inglese |
| `" <" + biten(inv(INV_ITEM_PARAM1, itemowner_itemid)) + ">"` | il nome dell'esca innestata sulla canna da pesca (`item_func.hsp:698`), giapponese senza parentesi. Cornice attorno a `biten()`: quel che c'e' da tradurre sta nei nomi delle esche, non qui. Le angolari ASCII sono gia' la convenzione del progetto per i titoli dentro un nome (vedi `< ` e ` >` qui sopra) |
| `"<" + evitemn(inv(INV_ITEM_PARAM1, itemowner_itemid))` | l'apertura del nome dell'oggetto d'evoluzione (`item_func.hsp:710`), cornice attorno a `evitemn()`. ⚠️ **La chiusura non e' invariante**: `:713` in inglese e' `s>`, cioe' l'angolare piu' la **s del plurale**, e in italiano il plurale non si fa col suffisso — quella si rende `>`, togliendo la morfologia inglese come vuole `guida-stile.md` |
| `"<" + _seikaku(inv(INV_ITEM_PARAM1, itemowner_itemid)) + "> "` | la cornice attorno al carattere dello spiritium (`item_func.hsp:916`, `_seikaku()`), giapponese 《 》の. Come `:698`: quel che si legge lo scrive la funzione, e le angolari piene giapponesi in CP932 escono a due glifi |
| `>` | l'angolare che chiude il nome di un oggetto d'evoluzione al **singolare** (`item_func.hsp:716`), giapponese vuoto. E' l'altra meta' di `:710` qui sopra, e in italiano fa anche il lavoro del plurale: `:713` si rende con lo stesso `>` invece che con `s>` |
| `primula` | il tredicesimo fiore selvatico (`item_func.hsp:1443`), giapponese プリムラ. ⚠️ **Non e' inglese lasciato li': e' italiano che coincide**, come `Info`. «Primula» e' il nome italiano corrente del genere *Primula*, ed e' anche la parola inglese: le due lingue prendono lo stesso latino. Gli altri dodici fiori della stessa lista si traducono tutti — `margaret` e' «margherita», `cosmos` e' «cosmea», `dandelion` e' «tarassaco» |
| `<` | l'angolare che apre il **titolo casuale** di un libro prodotto in gioco (`item_func.hsp:1786`), giapponese 『. Come `< ` in cima: il giapponese usa le parentesi piene, l'inglese le ha portate in ASCII, e l'italiano tiene quelle — le francesi «» CP932 non le codifica e le piene escono a due glifi. ⚠️ Qui non c'e' nemmeno un titolo da rendere: `random_title()` lo pesca a caso da una tabella |
| ` <` | la stessa angolare, con lo spazio che la stacca dal nome dell'oggetto (`item_func.hsp:1794`, il titolo di un libro di qualita' «miracolo»). Lo spazio in testa conta |
| ` {` | la graffa che apre il titolo casuale di un libro **sotto** la qualita' «miracolo» (`item_func.hsp:1797`), giapponese 《. ⚠️ **Non e' la stessa cornice di `<`**, ed e' upstream a tenerle separate: le graffe marcano il titolo comune, le angolari quello raro. Uniformarle cancellerebbe una distinzione che il gioco fa apposta — la stessa ragione della coppia `{` `}` per i nati in gioco |
| ` (lich)` | nome di creatura dentro una parentesi (`item_func.hsp:2101`, la bara della negromanzia), giapponese リッチ. **L'italiano coincide per diritto, non per pigrizia**: `db_creature.hsp:108009` rende リッチ «il lich» — parola presa di peso dal canone del genere, come in inglese — e qui l'articolo si toglie perche' e' un'apposizione attaccata al nome di un oggetto. Gli altri sette nomi della stessa lista si traducono tutti (gatto zombi, mummia, scheletro guerriero, necrobambola, drago zombi, occhi morti) |
| ` Lv. ` | la sigla di livello sulla sfera dei mostri (`item_func.hsp:2156`), giapponese ` Lv`. E' la stessa decisione di ` Lv` qui sotto — il progetto scrive `Lv` in `action.hsp:6545`, `text.hsp:65` e `:68` — con in piu' il punto e lo spazio che l'inglese mette perche' il numero segue subito. ⚠️ Lo spazio in testa conta: allinea la sigla al nome che la precede |
| `"[" + cnven(mtname(0, inv(INV_ITEM_MATERIAL, itemname_itemid))) + "]"` | **non e' testo, e' una cornice attorno a una variabile** (`item_func.hsp:2175`): il materiale dell'oggetto quando se ne conosce la qualita' ma non la benedizione. Quel che c'e' da tradurre sta dentro `mtname()`, cioe' in `material_data.hsp`, che ha una coda sua. ⚠️ Il giapponese scrive `"[" + mtname(...) + "製]"` e l'inglese butta il 製 («fatto di»): **si tiene la forma inglese apposta**, perche' la forma italiana piena sarebbe «[di acciaio]» / «[d'acciaio]», e l'elisione dipende dalla parola che `mtname()` restituisce a runtime — la stessa ragione per cui l'articolo dei nomi lo porta il nome e non una regola (`contratto-nomi.md` §4). Una parentesi quadra nuda regge qualunque materiale |
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
| `"<" + randomname() + ">, " + random_title()` | **non è testo, è una cornice attorno a due generatori** (`custom_nefiatypes.hsp:505`, il nome dei servitori di Orphe nel Vuoto). `randomname()` (`etc.hsp:357`) pesca le sillabe da `data\ndata-e.csv`, cioè da un file di dati, e `random_title()` (`etc.hsp:399`) dalle liste dello stesso file — che la **toppa della 124ª** rende italiane, perché sono letterali inglesi nudi fuori da ogni `lang()`. Fra le due chiamate non resta nessuna parola comune: le angolari ASCII e la virgola sono già la convenzione del progetto per un titolo dentro un nome (vedi `< ` e ` >` in cima). ⚠️ Il giapponese compone diversamente — `nome + "の" + randomname()` — ma il ramo italiano gira nel `lang()` **inglese**, e la sua forma è questa. Il gemello `db_creature.hsp:40819` si traduce invece, perché lì fra le variabili c'è la parola `the` |
| ` x ` | **il segno di moltiplicazione fra un nome e la sua quantità**, non una parola (`material.hsp:281` e `:458`, giapponese 「 × 」): «carbone x 3(12)» nell'elenco dei materiali che una ricetta chiede, e «carbone x 12» nel pannello dei materiali posseduti. L'italiano scrive la moltiplicazione con lo stesso segno, e la × piena del giapponese è a due byte, che la build inglese disegna a due glifi latini a caso — la stessa ragione di `< ` e di `$ x ` qui accanto. ⚠️ Gli apici inversi prendono i **due spazi** verbatim: il nome si concatena prima e il numero subito dopo. ⓘ È anche il metro con cui il budget dei 27 caratteri dei nomi di materiale fu calcolato nella 123ª (`glossario.md`): cambiarlo di lunghezza sposterebbe quel cancello |
| `(` | **punteggiatura**: `command.hsp:3634` è `lang(" ", "(")`, cioè il giapponese apre l'età con uno spazio e l'inglese con una parentesi. In italiano l'età fra parentesi si scrive con la parentesi. ⚠️ E non c'è margine per fare altro: la riga vive in **19 caratteri** fra `wx + 372` e la colonna dei valori a `wx + 512`, e «Lv.100 female?(999)» ne fa già 19 |
| `)` | l'altra metà (`command.hsp:3634`, `lang("歳", ")")`): il giapponese chiude con il contatore 歳 «anni», l'inglese con la parentesi. « anni)» costerebbe cinque dei diciannove caratteri della riga, e non ci sono |
| bonus | prestito acquisito, già in glossario. `strfix` (`text.hsp:190`) etichetta il `+3` di un oggetto |
| ` Lv` | la sigla di livello, che l'italiano scrive uguale. ⚠️ Non è solo un'etichetta: `action.hsp:12383` compone `evold = lang(" Lv", " Lv") + livello` e poi **cerca quella stringa in coda al nome** della creatura per togliere il suffisso (`:12384`). Tradurla qui, e non anche nel punto che il suffisso lo scrive, spezzerebbe il taglio: è la trappola del letterale confrontato contro un valore tradotto. Il resto del progetto scrive già `Lv` (`action.hsp:6545`, `text.hsp:65` e `:68`) |
| http://homepage3.nifty.com/rfish/index_e.html | indirizzo web (`text.hsp:181`), non testo |
| PER | sigla di Percezione: **identica** in italiano e in inglese. È una coincidenza, non una traduzione dimenticata |
| MAG | sigla di Magia: identica in italiano e in inglese |
| MP | sigla dei punti magia: **identica** in italiano e in inglese, come `PER` e `MAG`. È il titoletto della terza sezione degli appunti di stregoneria (`data\book.txt` `%26`), dove il giapponese dice MP a sua volta in caratteri latini, e la riga dopo lo scioglie per esteso — «Punti magia» — che è esattamente il modo in cui il gioco la usa altrove (`skill.hsp:941`, «Ristora gli MP»). Trovata alla 99ª, ed è la prima volta che un invariato viene da un **file dati** e non dal sorgente: fino a quel giorno `dati_reimporta` non leggeva affatto questo file |
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
| zenzai | dolce giapponese (`db_item.hsp:56934`, **dentro la descrizione** dell'osiruko), giapponese ぜんざい: il piatto somigliante da cui l'osiruko si distingue. Non e' il nome di un oggetto — e' un termine che la prosa cita — e l'italiano non ne ha uno. Maschile, invariato. Prima parola coniata dal corpo delle descrizioni (113a) |
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
| `Larnneire...` | **lo specchio esatto della riga qui sopra**, nove file piu' in la': `chat.hsp:13219`, giapponese 「ラーネイレ…。」, ed e' <Bethel> che pronuncia il nome di lei quando la storia e' finita (`gdata(GDATA_FLAG_MAIN) >= 760`) e non aggiunge altro. Se `:1591` e' Larnneire che dice «Bethel...», questa e' Bethel che dice «Larnneire...»: stesso nome invariato (`db_creature.hsp:63303`), stessi tre punti ASCII, stessa identita' che nasce dalla somma di due decisioni gia' prese. Dichiarata nella 92a, lotto `_92-bethel` |
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
| `* Curaria [KYURARIA AQUIFOLIUM]` | **nome di erba piu' binomio latino: non c'e' niente da rendere.** E' l'intestazione della prima scheda delle «Erbe benedette» (`data\book.txt` `%7`), e le due meta' sono tutt'e due invariate per ragioni diverse: `curaria` e' il nome dell'oggetto in `db_item.hsp:146975`, dove il progetto l'ha gia' lasciato tale, e il binomio fra parentesi quadre e' il **latino scherzoso** di monte, che l'italiano scrive uguale. Il giapponese dice solo ●キュラリア: e' l'inglese ad aver aggiunto la finta nomenclatura, e la si tiene per intero. Le sei schede dell'erbario stanno qui una per una, perche' il confronto e' sulla stringa intera
| `* Morgia [MOJIA DIPSACUS PILOSUS]` | la seconda scheda dell'erbario, per la stessa ragione di `* Curaria [KYURARIA AQUIFOLIUM]`
| `* Mareilon [MAREIRON DIPSACUS FEROX]` | la terza scheda dell'erbario, idem
| `* Spenseweed [SUPENSUUIDO LONGIFOLIA]` | la quarta scheda dell'erbario, idem
| `* Alraunia [ARURONIA MARTYNIA LUTEA]` | la quinta scheda dell'erbario, idem
| `* Stomafilla [SUTOMAFIRIA HYPOGAEA]` | la sesta scheda dell'erbario, idem
| `	Philosophiae Doctor Magus` | **e' latino, e il latino non si traduce in italiano: si legge.** E' la firma del dott. Schmidt in coda alle «Erbe benedette» (`data\book.txt` `%7`), lo scioglimento della sigla `PhDM` che compare nella riga 2. Il giapponese non ce l'ha affatto. Gli apici inversi prendono verbatim il tab, che rientra la firma sotto il nome
| Samisel | **nome proprio**, e in tutto il gioco compare qui soltanto: e' il destinatario della reclame per corrispondenza delle «Pergamene Mensili dello Speleologo» (`data\book.txt` `%15`), che il giapponese non ha affatto — quel blocco, in giapponese, e' un segnaposto («aspetta ancora un po'!»). Nome opaco come `Vernis`: non c'e' dentro nessuna parola comune
| `- Begin Phase - Draw Phase` | **nome di fase del gioco di carte, e a schermo e' inglese in tutt'e due le lingue.** `tcg.hsp:1592` e `:1594` lo scrivono dentro descrizioni composte con `s@tcg += "..."`, cioe' **letterali nudi** fuori da ogni `lang()`, come le parole chiave delle carte (`bmes "Windfury"`, `:953`). Il regolamento di `data\book.txt` `%14` le nomina per mandare il lettore a cercarle sulla carta: tradurle qui gli farebbe cercare una parola che sulla carta non c'e'. ⭐ Precedente nel progetto: `tcg_custom.hsp:2066`, «le carte Trample». Questa riga e la successiva sono l'elenco delle quattro fasi
| `- Main Phase - End Phase` | l'altra meta' dell'elenco delle fasi, per la stessa ragione della riga sopra
| `Begin Phase:` | il titoletto della sezione che spiega quella fase, stessa ragione
| `Draw Phase:` | idem
| `End Phase:` | idem. ⓘ `Main Phase` non ha una riga sua perche' nel libro compare dentro una frase italiana («Nella Main Phase puoi:»), e li' il confronto sulla stringa intera non scatta
| `            -== Errata ==-` | **parola latina che l'italiano scrive uguale**, come `Arena` e `Incognito` qui sopra: e' il titoletto dell'ultima sezione del manuale del museo (`data\book.txt` `%4`), dove elenca costo e rendita con l'avvertenza che sono cifre approssimative. In italiano «errata corrige» e' la stessa parola, e la cornice `-== ==-` e' cornice. Gli apici inversi prendono verbatim i **dodici spazi** che centrano l'insegna: monte li conta a mano, e senza di loro il titoletto scivola a sinistra

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
| ` ` | `net.hsp:367`: lo spazio fra l'epiteto e il nome nel messaggio che la chat manda al server — `net_send "chat" + AKA + lang("", " ") + NOME + lang("", " says, ") + inputlog`. Il giapponese non ha niente lì perché incornicia col 「」 di `:360`; l'inglese ci mette uno spazio, e l'italiano lo stesso. **Non è una parola, è la distanza fra due campi.** ⚠️ La voce accanto, `" says, "`, invece **si rende** (« dice, »): quella è testo. Gli apici inversi la prendono verbatim, perché la cella si legge con `strip()` e lo spazio è tutto ciò che c'è. Dichiarato nella 125ª, lotto `fase6-net-001` |
| `(` | `net.hsp:534`: la parentesi che apre il conto dei voti nell'urna — `s = lang(" ", "(") + cdata(CDATA_VOTES_RECEIVED, i) + "" + lang("票", ")")`. Il giapponese non usa parentesi (scrive `12票`, col contatore 票 in coda), l'inglese sì (`(12)`), e l'italiano tiene quelle dell'inglese. **Non c'è niente da tradurre: è una cornice.** Stesso criterio delle parentesi di `god.hsp` e di `chara.hsp:2331`. Dichiarata nella 125ª, lotto `fase6-net-001` |
| `)` | `net.hsp:534`: la parentesi che chiude il conto dei voti, gemella di quella qui sopra. ⚠️ **Qui il giapponese una parola ce l'ha** — 票, «voti» — e l'italiano non la ripete: la colonna si chiama già «Voti» (`:493`), e ripeterla su ogni riga costerebbe cinque caratteri in una cella larga 90 px che deve tenere fino a cinque cifre. La parola giapponese non si perde, si sposta nell'intestazione. Dichiarata nella 125ª, lotto `fase6-net-001` |

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

Aggiunta nella 72a col lotto di `help.hsp`, cresciuta nella 97a, **scesa a
quattro nella 101a**. Valori che il gioco usa per **trovare qualcosa**, non per
dire qualcosa: tradurli non fa parlare italiano nessuna schermata, fa fallire
una ricerca.

⭐ **`manual_ENG.txt` stava qui e nella 101ª è uscito**, ed è la differenza fra
un indirizzo e un indirizzo *nostro*: il giorno in cui il manuale si traduce,
quel nome deve puntare al file italiano. Diventa la resa `manual_ENG_it.txt`, e
non una toppa come diceva questa riga fino a ieri — `help.hsp:331` è l'unico
sito della famiglia in cui il nome sta **dentro** una `lang()`, quindi il
dizionario ci arriva da solo, e il ramo `exist` di ripiego che questa riga
citava è di `custom_autopick.hsp`, non del manuale (misurato: `manual_` compare
in un sito solo in tutto il sorgente). ⚠️ Gli altri quattro restano perché il
file che nominano **non è nostro**: `EN` è un marcatore dentro un file,
`iknownnameref_en.` e `author_en.` sono campi di un file che scrive il
giocatore, `scene2.hsp` è codice di monte.

| valore | motivo |
|---|---|
| `EN` | `help.hsp:228` compone `"%" + ghelp + "," + lang("JP", "EN")` e lo cerca dentro `manual_ENG.txt` con `instr`. E' **la chiave del blocco**, cioe' lo stesso marcatore `%…,EN` che regge tutti e cinque i file di `data\` (vedi la Fase 3): la sigla non si legge da nessuna parte, si confronta. Tradotta, la guida in gioco non trova piu' un argomento. ⭐ **97a: il secondo sito e' `command.hsp:8372`**, che compone `"" + inv(INV_ITEM_BOOK_ID, ci) + "," + lang("JP", "EN")` e lo cerca dentro `data\book.txt`: e' la stessa chiave, sullo stesso schema `id,EN`, per il testo dei libri. ⚠️ Resta `EN` anche il giorno in cui `book.txt` si traduce — li' `dati_applica` riscrive il **testo** dentro il blocco, non il marcatore che lo apre |
| `iknownnameref_en.` | `system.hsp:1441`, argomento di `getnpctxt()`: e' il **nome del campo** che il gioco cerca dentro il `.txt` con cui il giocatore descrive un oggetto suo, e la coppia `lang("iknownnameref.", "iknownnameref_en.")` dice che il file ne porta **due**, uno per lingua. Non si legge da nessuna parte: si confronta. Tradotta, il gioco non trova piu' il nome dell'oggetto e carica la stringa vuota. ⚠️ E il suffisso `_en` non e' un caso: e' upstream che ha chiamato «inglese» il campo non giapponese, e chi scrive un oggetto in italiano scrive **in quello** |
| `author_en.` | `system.hsp:1442`, stesso `getnpctxt()` e stessa ragione di `iknownnameref_en.`: e' il campo dell'autore dentro il file dell'oggetto. ⭐ Sulla **stessa riga** c'e' il valore di ripiego quando il campo manca — `lang("プレイヤー", "Player")` — e quello **si traduce** («Giocatore»): la chiave e il suo valore predefinito stanno appaiati, e uno solo dei due e' testo |
| `scene2.hsp` | `help.hsp:819`, stesso `noteload`, stesso motivo: e' il file delle scene sbloccabili. ⚠️ Qui l'inglese e' anche fuorviante — `lang("scene1.hsp", "scene2.hsp")` sembra una versione e sono **due file diversi**, uno per lingua |

## Termini coniati dentro una DESCRIZIONE — 111ª

Fino alla 110ª questa regola valeva solo per i **nomi** dentro le marche 《》:
*quando l'originale traslittera, non sta leggendo il nome come una descrizione,
e non c'è niente da rendere.* La 111ª l'ha applicata per la prima volta dentro
una descrizione.

| valore | motivo |
|---|---|
| `zekki` | 絶器, `db_item.hsp:75717`, la descrizione dei guanti dello Spirito Blu: 「絶器と呼ばれる篭手だ」, *guanti chiamati zekki*. Il termine **non è nel dizionario e non è nel glossario** — è una coniazione di Elona+, e l'**inglese lo traslittera** invece di scioglierlo («These are gloves that is called a 'zekki'»). Reso «Dei guanti d'arme detti zekki.» ⚠️ **Senza virgolette**: CP932 cancella « e », e la prima resa — che le aveva — è stata bocciata dalla rete dei caratteri sconosciuti. A schermo sarebbe arrivata identica a questa, e nessuno lo avrebbe saputo |

## Nomi coniati del potioman — sono un nome proprio, non una parola

Le 39 stringhe qui sotto compongono il nome di un **potioman personalizzato**
(`item_func.hsp:722`-`:871`), la macchina spara-pozioni che il fabbro migliora a
richiesta. Il nome si monta a pezzi — modo, sottonome, sigla della parte — ed
esce cosi': «Rotante-Flaenix F».

⚠️ `ioriginalnameref(ITEM_ID_CF_POTIOMAN)` e i suoi tre fratelli sono **vuoti**
(`db_item.hsp:135599` e dintorni): qui non c'e' un nome di oggetto a cui questi
pezzi si attaccano, **il nome e' questo**.

**Il modo si traduce, il sottonome no**, e la riga di taglio non e' arbitraria:

- i sei **modi** (`:738`-`:753`) hanno un senso, e lo dichiara la forma distesa
  gia' resa in `item_data.hsp:702`-`:707` — «Imprime al tappo una rotazione
  tremenda», «Ha una potenza di base elevata», «Spara due colpi insieme», «Puo'
  sparare a raffica», «Permette il tiro di precisione», «Confonde con una
  traiettoria mutevole». Sono `Rotante`, `Potente`, `Doppio`, `Rapido`,
  `Preciso`, `Ingannevole`, e stanno **fuori** da questa tabella;
- i 28 **sottonomi** (`:756`-`:837`) sono portmanteau opachi in katakana che
  l'inglese ha portato in alfabeto latino coniando una parola nuova — フレイクス
  (flame + phoenix) e' `-Flaenix`, non «fenice di fiamma». Non c'e' una parola
  italiana da trovare: c'e' un nome inventato, e i nomi inventati il progetto li
  tiene (`Vernis`, `<Pascal>`);
- le 11 **sigle di parte** (`:840`-`:870`) sono lettere sole, `Ｆ` `Ｉ` `Ｌ` …
  a un byte anche in giapponese, dove il file usa le larghe. Un segno, non una
  parola.

💡 Il confine e' lo stesso che il progetto usa da sempre sui nomi di creatura:
ネクロドール diventa «la necrobambola» perche' le due meta' vogliono dire
qualcosa in giapponese, mentre `<Pascal>` resta. Qui le due meta' sono
**inglese** gia' in giapponese: tradurle sarebbe inventare un terzo nome, che
non e' ne' quello dell'autore ne' quello di chi ha fatto la versione inglese.

⚠️ Se questa scelta si rovescia, si rovescia **tutta insieme**: 28 righe di
dizionario, e i sei modi vanno riletti con lei.

| valore | katakana | dentro |
|---|---|---|
| `-Flaenix` | フレイクス (flame + phoenix) | il sottonome del potioman, `item_func.hsp:756` |
| `-Grifeak` | グリフビーク (griffin + beak) | il sottonome del potioman, `item_func.hsp:759` |
| `-Pegather` | ペガフェザー (pegasus + feather) | il sottonome del potioman, `item_func.hsp:762` |
| `-Dragoul` | ドラゴウル (dragon + ghoul) | il sottonome del potioman, `item_func.hsp:765` |
| `-Ravrain` | レイヴレイン (raven + rain) | il sottonome del potioman, `item_func.hsp:768` |
| `-Valkspear` | バルキスピア (valkyrie + spear) | il sottonome del potioman, `item_func.hsp:771` |
| `-Orfin` | オルフィン (orca + dolphin) | il sottonome del potioman, `item_func.hsp:774` |
| `-Wolfang` | ウルファング (wolf + fang) | il sottonome del potioman, `item_func.hsp:777` |
| `-Leoheart` | レオハート (leo + heart) | il sottonome del potioman, `item_func.hsp:780` |
| `-Tigelaw` | タイガロウ (tiger + claw) | il sottonome del potioman, `item_func.hsp:783` |
| `-Foxail` | フォクテイル (fox + tail) | il sottonome del potioman, `item_func.hsp:786` |
| `-Bearm` | ベアーム (bear + arm) | il sottonome del potioman, `item_func.hsp:789` |
| `-Ifheat` | イフヒート (ifrit + heat) | il sottonome del potioman, `item_func.hsp:792` |
| `-Dinoguts` | ダイガッツ (dinosaur + guts) | il sottonome del potioman, `item_func.hsp:795` |
| `-Cerbeads` | ケルヘッズ (cerberus + heads) | il sottonome del potioman, `item_func.hsp:798` |
| `-Bihorn` | バイホーン (bicorn) | il sottonome del potioman, `item_func.hsp:801` |
| `-Wyverng` | ワイバング (wyvern + fang) | il sottonome del potioman, `item_func.hsp:804` |
| `-Leviascale` | リヴァスケイル (leviathan + scale) | il sottonome del potioman, `item_func.hsp:807` |
| `-Bushilade` | ブシレード (bushi + blade) | il sottonome del potioman, `item_func.hsp:810` |
| `-Ogreand` | オーガンド (ogre + hand) | il sottonome del potioman, `item_func.hsp:813` |
| `-Stagito` | スタアギト (stag + agito) | il sottonome del potioman, `item_func.hsp:816` |
| `-Goledy` | ゴレディ (golem + lady) | il sottonome del potioman, `item_func.hsp:819` |
| `-Knimail` | ナイメイル (knight + mail) | il sottonome del potioman, `item_func.hsp:822` |
| `-Soldigun` | ソルジガン (soldier + gun) | il sottonome del potioman, `item_func.hsp:825` |
| `-Deatranium` | デスレニアム (death + -enium) | il sottonome del potioman, `item_func.hsp:828` |
| `-Giganoot` | ギガンテット (gigant + -ett) | il sottonome del potioman, `item_func.hsp:831` |
| `-Kobolord` | コボルード (kobold + lord) | il sottonome del potioman, `item_func.hsp:834` |
| `-Hercurest` | ヘラクレスト (hercules + crest) | il sottonome del potioman, `item_func.hsp:837` |
| ` F` | Ｆ | la sigla della parte montata, `item_func.hsp:840` |
| ` I` | Ｉ | la sigla della parte montata, `item_func.hsp:843` |
| ` L` | Ｌ | la sigla della parte montata, `item_func.hsp:846` |
| ` D` | Ｄ | la sigla della parte montata, `item_func.hsp:849` |
| ` M` | Ｍ | la sigla della parte montata, `item_func.hsp:852` |
| ` P` | Ｐ | la sigla della parte montata, `item_func.hsp:855` |
| ` H` | Ｈ | la sigla della parte montata, `item_func.hsp:858` |
| ` S` | Ｓ | la sigla della parte montata, `item_func.hsp:861` |
| ` N` | Ｎ | la sigla della parte montata, `item_func.hsp:864` |
| ` C` | Ｃ | la sigla della parte montata, `item_func.hsp:867` |
| `X` | Ｘ | la sigla della parte montata, `item_func.hsp:870` |

## Una riga che il giocatore ha scelto di leggere in giapponese — 126ª

`proc.hsp:14384` è uno `switch` su `TWEAK_MISC_HOKUTO_NO_KEN_MODE`, cioè un
**ritocco che il giocatore accende**, e offre tre forme della stessa battuta di
Ken il guerriero quando un colpo uccide:

    :14386  「お前はもう死んでいる。」    il giapponese, ramo `jp`: in italiano non lo legge nessuno
    :14389  You are already dead.       SI TOPA:  «Tu sei già morto.»
    :14392  Omae wa mou shindeiru.      RESTA:    è la traslitterazione, ed è il senso dell'opzione

ⓘ **Qui non c'è una tabella apposta.** Le tabelle di questo file le legge
`verifica.py` come dichiarazioni di valore, e delle tre righe qui sopra una sola
resta invariata: una tabella ne dichiarerebbe tre. ⚠️ E la riga che resta non
sta comunque nel dizionario — è nuda — quindi `verifica.py` non la incontra mai:
la dichiarazione che conta è questa prosa e il `motivo` della toppa.

⚠️ **Il `default` non è una dimenticanza, è la terza opzione.** Chi lo sceglie
ha chiesto proprio di leggere la frase *in rōmaji*, come la si sente nella
sigla: tradurla toglierebbe l'unica cosa per cui quella voce del menu esiste.
È lo stesso criterio di `Kamikakushi` e delle altre romanizzazioni qui sopra,
solo che qui la scelta è **del giocatore e non del traduttore**.

⚠️⚠️ **E il `case 2` porta un participio maschile apposta.** «Tu sei già morto»
è la battuta del doppiaggio italiano, e `guida-stile.md` vieta il participio
riferito a chi non ha genere noto — qui il bersaglio può essere la giocatrice.
L'eccezione è dichiarata: la riga **non descrive** un personaggio, **cita** una
frase che in italiano ha una forma sola, e una versione neutra sarebbe corretta
e non sarebbe più la citazione. ⓘ Nessuna rete la vede: `referti.py` legge il
dizionario, e le toppe non ci stanno. Il posto dove è scritta è questo e il
`motivo` della toppa.

## Una battuta che nessuna rete misura ancora — 126ª

`proc.hsp:14392` resta nell'elenco di `nudi_en.py` e di `triage_nudi.py` come
riga «testo ancora da fare», e ci resterà: quei due strumenti contano i
**letterali inglesi intatti**, e una riga che deve restare intatta è
indistinguibile da una che nessuno ha guardato. È lo stesso caso di
`net.hsp:263` della 125ª — **misurata, non da fare** — e finché il triage non
avrà una classe per «dichiarata invariata» il conto delle righe nude porterà
dentro anche queste.

## Le altre righe nude che restano inglesi, e perché — 126ª

Nessuna di queste sta nel dizionario — sono nude — quindi `verifica.py` non le
incontra e questa sezione non è una tabella di valori: è la dichiarazione, e sta
qui perché non c'era nessun altro posto dove scriverla.

**`item_func.hsp:1809`, `"the " + …`** — è il **ripiego dichiarato**
dell'articolo, non una dimenticanza. La toppa che introduce
`locvar_itemname_s9` lo dice nel proprio motivo: *«se l'articolo italiano manca
resta quello inglese, come il plurale ripiega sul singolare»*. Renderlo «il »
sarebbe **peggio**: il genere della testa del nome, nella stringa composta, sta
in mezzo e qui non si conosce. La riga si spegne quando il nome ha il suo
articolo, non toccando lei.

**`item_func.hsp:2252`, `" <BGM" + … + ">"`** — `BGM` è la sigla della traccia
musicale del disco, della stessa famiglia degli `mcTown1`/`mcBoss2` che
`triage_nudi.py` classifica `sigla` e che il progetto lascia stare. Il numero
accanto lo scrive il codice.

**`screen.hsp:1125` e `:1128`, `"*debug*"` e `"loop… sub… "`** — stanno dentro
`if ( gdata(GDATA_WIZARD) == 1 )`, cioè si vedono **solo in modo mago**. Sono la
stessa cosa della classe `dbg` del triage, che riconosce le routine `dbg_*`:
qui il nome della routine è `screen_drawStatus` e la regola per forma non le
prende. ⓘ Le guardie `GDATA_WIZARD == 1` nel sorgente sono **tre** in tutto
(`chara.hsp`, `screen.hsp`, `system.hsp`): troppo poche perché valga la pena di
un referto, abbastanza perché valga la pena di scriverlo qui.

## Una riga misurata e non decisa — 126ª

**`screen.hsp:1031`, `mes "PF"`** — l'etichetta del contapunti del poker nel
casinò (`pokert@cgx`). Non si sa che cosa siano quelle due lettere: non c'è un
giapponese gemello, il codice non le scioglie, e `gcopy 3, 0, 416, 65 + en * 15, 15`
dice solo che la casella che le contiene è più larga in inglese. ⚠️ E in
italiano `PF` **si legge «Punti Ferita»**, che è un'altra cosa: tradurre a caso
qui non è impreciso, è fuorviante. Resta inglese finché qualcuno non la vede a
schermo con una mano di poker in corso.

## Le righe nude di `command.hsp` che restano inglesi — 127ª

Chiudendo `command.hsp` (51 righe nude vive, 29 toppate) restano diciotto righe
che **non si toccano**. Non sono lavoro rimandato: sono due classi, e tutt'e due
hanno un motivo misurato. ⚠️ Restano però nel conto di `nudi_en` e
`triage_nudi` come «da fare», per la ragione già scritta per `net.hsp:263`:
quei referti contano i letterali **intatti**, e una riga che deve restare
intatta è indistinguibile da una che nessuno ha guardato.

### Le sigle della colonna larga venti caratteri

**`command.hsp:1348`, `:1365`, `:1387`, `:1401`, `:1468`, `:3614`, `:3631`,
`:3638`, `:14191`, `:14205`** — `Hp:`, `Lv.`, `Rank.`, `Dv:`, `Pv:`. ⭐⭐ **Qui
la larghezza non è un'opinione: è già misurata in questo stesso file.** La riga
si stampa a `pos wx + 372` (`command.hsp:3666`) e la colonna successiva comincia
a `wx + 512` (`:3676`): **140 px**, a 7 px per carattere del corpo 12, cioè
**venti caratteri**. E l'inglese ne usa già diciannove — «Lv.100 female?(999)» —
come la voce `(` di questo file aveva già misurato per `:3634`.

⚠️ **E `Rank.` non è un'eccezione alla scelta di `item_func.hsp`, che rende
`Rank` con «Rango»**: lì la parola sta nella coda fra parentesi del nome di un
oggetto, dove il posto c'è. Qui «Rango.» costerebbe un carattere su venti già
tutti spesi, e la riga porta anche il sesso del personaggio. La stessa parola in
due mestieri diversi, come la rete 3 insegna a leggere.

ⓘ `Hp:`, `Dv:` e `Pv:` sono inoltre le sigle che **il giapponese scrive
uguali**: `command.hsp:17679`-`:17680` le mette dentro una `lang()` col
medesimo testo dalle due parti, cioè upstream stesso le tratta come simboli.

### Le quattro sigle del pannello del discernimento

**`command.hsp:188`, `:189`, `:190`, `:208`** — `" Lv:"`, `" DV:"`, `" PV:"`,
`" HP: … MP: "`, dentro `*txttargetnpcextrainfo`. Stessa ragione: sono simboli
che upstream scrive identici nelle due lingue. Le **quattro parole** dello
stesso blocco (`Target: `, `Gauge:`, `GUARD BREAK`, `Guard:`) sono invece state
tradotte, ed è la differenza che conta: una sigla non è una parola.

### Due righe che non hanno niente da tradurre — un difetto del triage

**`command.hsp:4651` e `:4652`, `promptAdd cnven(strmale), "null", 0`** —
⚠️ **sono un FALSO POSITIVO del conteggio, non lavoro.** L'unico letterale
inglese di quelle righe è `"null"`, che non è testo ma la lettera di scelta di
`promptAdd` — `nudi_accanto_a_lang.py` lo dichiara già dalla 61ª. Il testo che
il giocatore legge lì viene da `strmale`/`strfemale`, assegnate a
`text.hsp:123`-`:124`, che **hanno già la loro toppa**: nella build dicono
«maschio» e «femmina» (vedi la sezione `male`/`female` più su). La voce del
menu è italiana da sessioni.

💡 È il costo di misurare per forma: `triage_nudi` classifica `testo` una riga
che disegna e contiene un letterale, e non può sapere che quel letterale è una
chiave. Sono due righe su 141, e il rimedio — insegnare al triage l'elenco delle
chiavi di `promptAdd` — costerebbe più della dichiarazione.

### Una parola che il posto non basta a decidere

**`command.hsp:459`, `display_topic "Ver", wx + 534, wy + 36`** — l'intestazione
della colonna delle versioni nel menu che importa un personaggio. In italiano
l'abbreviazione sarebbe «Ver.» col punto, un carattere in più, e la colonna
comincia a `wx + 534` su una finestra che non è stata misurata. ⚠️ Un punto non
è una traduzione: si aggiunge quando qualcuno avrà visto la schermata.

**`command.hsp:2131`, `traitrefn2(…) + "(MAX)"`** — `MAX` è un simbolo, non una
parola, e in italiano si scrive uguale. La coda `(条件不足)`/`(requirement)` che
la riga dopo può appendere passa invece dal dizionario, ed è tradotta: la
distinzione fra le due è esattamente quella fra sigla e parola.

## Le due righe di `config.hsp` che scrivono `config.txt` — 127ª

**`config.hsp:47`, `noteadd "" + valn + " \"" + valn(1) + "\""`** e
**`config.hsp:1515`, `valn = "Pcc_show.", str(cfg_pcc_show)`** — ⚠️ **non sono
testo: sono il file di configurazione.** La prima è la riga che `*cfg_write`
scrive dentro `config.txt` quando la chiave non c'era ancora (`notesave` a
`:49`); i suoi letterali sono uno spazio e due virgolette, cioè la sintassi del
file. La seconda è il **nome di una chiave**, `Pcc_show.`, che `*config_init`
rilegge con `cfgRead`.

⚠️ Tradurne una qualunque significa scrivere in `config.txt` una chiave che il
lettore non riconosce più: le impostazioni del giocatore si perderebbero **in
silenzio**, e nessuna rete del progetto guarda dentro quel file. È la stessa
classe di `Direct sound` e `MCI` più su — il valore che lega l'etichetta al file
di configurazione — vista dal lato della chiave invece che del valore.

💡 Sono, come `command.hsp:4651`-`:4652`, un falso positivo del conteggio: il
triage vede un letterale su una riga che compone, e non può sapere che quel che
compone è un file e non una schermata.

## Le ultime righe nude sparse, e perché restano — 127ª

Chiudendo il fronte a 45, quel che resta fuori da `command.hsp` e `config.hsp`
si riduce a queste. Nessuna è lavoro rimandato.

**`screen.hsp:417` e `:423`, `"Sp"` e `"Lv"`** — le due sigle del pannello di
stato, quello sempre a schermo. Sono simboli, come `Hp:`/`DV:`/`PV:` di
`command.hsp`, e il pannello è il posto più stretto del gioco: `:417` e `:423`
scrivono con `bmes` dentro una striscia che il giocatore ha sott'occhio a ogni
turno, e «Liv» costerebbe un carattere su due.

**`chara.hsp:3204`, `listn(0, cnt) = "*Debug*"`** — la voce di debug
nell'elenco degli epiteti. Stessa classe di `screen.hsp:1125`: testo che esiste
solo per chi sviluppa.

**`chara.hsp:3450`, `"(extra)" + listn(0, cnt)`** — il prefisso delle razze
aggiunte dal mod. ⚠️ **Non è inglese lasciato lì: è italiano che coincide**,
come `Info` e `t ` più su. «Extra» in italiano è la stessa parola, e la forma
piena («aggiuntiva») allungherebbe una voce di elenco senza dire niente di più.

**`tcg.hsp:969`, `"Immune"`, e `tcg.hsp:3480`, `"Mana "`** — terza e quarta
della stessa specie: «immune» e «mana» in italiano si scrivono così, e «mana» è
già la parola del progetto in tutto il dizionario.

**`custom_tweaks.hsp:1679`, `"Nani?!"`** — la descrizione del ritocco
`TWEAK_MISC_HOKUTO_NO_KEN_MODE`. ⭐ È **la battuta stessa**, in rōmaji, ed è la
gemella di `proc.hsp:14392` («Omae wa mou shindeiru»), già dichiarata nella
126ª: là il rōmaji è una delle tre forme che il giocatore può scegliere, qui è
il modo di annunciarlo. Tradurla spegnerebbe la citazione, che è tutto quello
che quella riga è. ⓘ Le altre cinque descrizioni dello stesso blocco
(`:1673`, `:1676`, `:1682`, `:1685`) sono invece tradotte.

**`custom_itemlist.hsp:49`, `noteadd "ID⇥Type⇥JName⇥EName⇥Value"`** —
l'intestazione del file che `*Save_Item_Highlights` esporta. È un TSV, e le
cinque parole sono **nomi di colonna**, non testo di schermata; `JName` e
`EName` per giunta nominano le due lingue del database, non due parole
italiane. Chi legge quel file lo apre in un foglio di calcolo per costruirsi le
regole di autopick.

**`helloworld.hsp:4`, `mes "hello world"`** — ⚠️ **il file non fa parte della
build.** Porta il suo `#packopt name "helloworld"` alla riga 2, cioè è un
programma a sé che nessun `#include` tira dentro: è il file di prova dell'SDK
rimasto nel clone di monte. Non è testo del gioco.

**`system.hsp:4400`, la riga della console di debug** — `VARIANT_NAME + " v" +
VERSION_STRING + " Debug Console…"`, dentro `*game_debug`. Stessa classe del
`*debug*` di `screen.hsp`.

### ~~Un fronte misurato e NON chiuso: gli AP di `chara_func.hsp`~~ — CHIUSO nella 128ª, e la misura era sbagliata

⚠️⚠️⚠️ **Quel che questa sezione diceva fino al 2026-09-02 era falso nella
parte che rendeva il lavoro grande.** Diceva: «una tabella al sito di stampa che
mappa le tre basi per le **cinque code**», e che la frase si compone «per
ricorsione» con quattro frammenti inglesi, uno dei quali porta `his()` a un
argomento — «una toppa a blocco di una certa dimensione, vuole una sessione
sua». **Le cinque code non escono mai a schermo, e il lavoro erano due toppe.**

**Quel che regge.** `gain_ap_source` è davvero **operando e testo insieme**,
come `male`/`female` più su: sette confronti lo leggono per scegliere il ramo
(`:8415`, `:8436`, `:8455`, `:8509`, `:8524`, `:8530`, `:8543`) e la stessa
variabile finisce dentro la frase. Tradurre l'operando romperebbe le sette
condizioni in silenzio, quindi l'operando **non si tocca** e la resa si separa
da lui **al sito di stampa**. Quella parte era giusta.

**Quel che non reggeva.** Le otto chiamate che compongono le code (`:8533`,
`:8536`, `:8540`, `:8546`, `:8548`, `:8553`, `:8556`, `:8560`) stanno **tutte
dentro `gain_ap_old`**, e `gain_ap_old` ha **un chiamante solo in tutto il
sorgente**: `action.hsp:8992`, che gli passa `"destone"`. Le chiamate stanno
dentro `if ( gain_ap_source == "talk" )` (`:8530`) e
`if ( gain_ap_source == "kill" )` (`:8543`), e lì dentro quella variabile vale
sempre e solo `"destone"` — non viene mai riassegnata, i sei riferimenti nel
file sono tutti confronti `==`. **Quei due blocchi sono irraggiungibili.**
Nessuna coda, nessun `his()`, nessuna ricorsione.

⭐ **E l'autore del mod lo dice lui stesso**, tre righe sopra la funzione viva
(`:8342`): «*Ano made ap gain functions a lot simpler in 2.29, but he didn't
change the destone formula*». La funzione vecchia sopravvive **solo** per la
pietra, e si porta dietro la sua coda morta.

Quindi i valori vivi sono **tre e fissi**, non tre basi per cinque code:

- `:8430`, dentro `gain_ap` (`:8343`), chiamata da `chara_func.hsp:3991` e
  `:4135` — `gain_ap_source` vale `"talk"` oppure `"kill"`;
- `:8522`, dentro `gain_ap_old` (`:8443`), chiamata da `action.hsp:8992` —
  `gain_ap_source` vale sempre `"destone"`.

✅ **Chiuso con due toppe** (128ª, `scratchpad/_128-toppe-ap.py`): a `:8430` un
`if`/`else` copiato da `:8415`-`:8419` — quindici righe più su, **dentro la
stessa funzione** — che sceglie fra «**AP dalla trattativa**» e «**AP
dall'uccisione**»; a `:8522` una stringa fissa, «**AP dalla pietra del
risveglio**». Nessuna delle tre parole è stata scelta: «Trattativa» è la resa di
`Negotiation` (`skill.hsp:222`, e «switched to talking mode!» → «passa in
assetto di trattativa!»), e «pietra del risveglio» è la resa di 覚醒の閃石 /
«awakening stone» in `db_item.hsp:134581`.

⚠️⚠️ **E «destone» non era una parola inglese: era il nome interno
dell'oggetto.** `ITEM_ID_AWAKE_DESTONE` / `EFFECT_AWAKE_DESTONE`. A schermo
usciva «X obtained 3 AP from the destone.», cioè un identificatore di codice
dentro una frase — l'inglese stesso era rotto, non solo non tradotto.

ⓘ **Nota per chi volesse collaudarlo:** `spawn_item 1274` **non basta** per
vedere la terza riga. La pietra porta le statistiche della creatura da cui è
caduta in `INV_ITEM_PARAM2`/`PARAM3`/`AMUR_CAGE` (`chat.hsp:20263`-`:20265`), e
una pietra generata dalla console li ha a zero: `gain_ap_old` esce alla soglia
`>= 1000` di `:8465` e il gioco stampa invece la riga già italiana di
`action.hsp:8995`, «non sembra servirgli a niente». È un passo muto, ed è
scritto qui perché nessuno lo riprovi.
## Le ultime diciotto righe nude, e la parola che non si tocca — 130ª

Chiudendo le quattro righe vive che restavano (`init.hsp:537`, `quest.hsp:782`,
`text.hsp:11912` e `:12104`), il fronte delle righe nude di classe `testo`
scende a **56**, e quel che resta **non è lavoro rimandato**. Sono diciotto, in
cinque classi, e nessuna è una frase che il giocatore legga in inglese.

⚠️⚠️ **Il conto non scenderà mai a zero, ed è per costruzione:** `triage_nudi` e
`nudi_en` contano i letterali **intatti**, e una riga che deve restare intatta è
indistinguibile da una che nessuno ha guardato. È la stessa ragione già scritta
per `net.hsp:263` e per le diciotto della 127ª. Il numero che si legge è il
**residuo** di `scratchpad/_130-residuo-delle-righe-nude.py`, che incrocia le
righe coi siti nominati qui, in `decisioni.md` e in `rinviate.jsonl`.

### ⚠️⚠️⚠️ `init.hsp:536`, `return "user"` — un OPERANDO, non una parola

**Non si traduce, e tradurla non darebbe nessun errore.** Quella stringa è quel
che due `sreplace` **cercano**: `item_func.hsp:967` e `:1073` prendono il nome
composto dell'oggetto — carte, statuette, parti di creatura — e vi sostituiscono
la parola «user» col nome del PNG personalizzato, che arriva da
`getcnpcnamebychecksum`. Renderla «utente» spegnerebbe tutt'e due i siti **in
silenzio**: il giocatore leggerebbe per sempre il segnaposto invece del nome.

⭐ È la famiglia della 128ª — un ramo ucciso dalla traduzione perché è cambiata
la stringa **confrontata** e non quella **assegnata** — vista da un lato che
nessuna rete guarda: `_128-confronti-contro-un-nome-assegnato.py` cerca
`X == lang(J, E)`, e un `sreplace` non è un confronto.

⚠️ **Misurato il 2026-09-03, e oggi i due rami sono vivi:** nella build
`db_creature.hsp:97539` torna ancora `lang("user", "user")`, cioè il nome della
creatura `CREATURE_ID_USER` non è tradotto. Il giorno in cui un lotto di
`db_creature.hsp` lo renderà, i due `sreplace` moriranno **senza che niente lo
dica**. ⓘ Il rimedio, quando quel lotto arriverà, è la forma già usata per «Your
Home» (42ª) e per i quattro rami della 128ª: si allarga il sito che cerca, non
si tocca il nome.

ⓘ `init.hsp:537` è invece **testo**, ed è stata resa: «utente sconosciuto». Le
due righe adiacenti stanno nella stessa funzione e vogliono trattamenti opposti
— è esattamente la distinzione fra sigla e parola, portata sul confine più
sottile che il progetto abbia incontrato.

### Cinque righe di un pluralizzatore già spento

**`item_func.hsp:1894`, `:1905`, `:1915`, `:1918`, `:1921`** — `"es"`, `"ves"`,
`"ies"`, `"coffins"`: il pluralizzatore inglese dei nomi di oggetto
(`BLOODYSHADE CUSTOM`, 91 righe e 47 `case ITEM_ID`). ⚠️ **È già codice morto**:
una toppa cambia la sua guardia in `if ( 0 )`, e il plurale italiano arriva da
`ioriginalnamerefplur`, dove il nome si concatena — `contratto-nomi.md` §4-bis.
Le righe restano nel conto perché la toppa ha cambiato **la guardia**, non loro.

### Otto nomi di campo di un file, non di una schermata

**`map_rand.hsp:692`, `:693`, `:694`, `:695`, `:696`, `:697`, `:698`, `:699`**
— `area[…];`, `Rdtype[…];`, `mobdensity[…];` e
compagnia, scritti con `noteadd` dentro `mapinfo_%06d.txt` e salvati su disco
(`notesave`, `:700`). Stessa classe del TSV di `custom_itemlist.hsp:49`
dichiarato nella 127ª: sono **nomi di campo**, e chi apre quel file lo apre per
leggere i parametri di generazione di una mappa, non una frase.

### Due righe nel ramo `if ( jp )`

**`system.hsp:3521`** (`Contributor MSL / View the credits for more`) e
**`system.hsp:3537`** (le voci del menu iniziale, alternate al giapponese) —
stanno tutt'e due dentro `if ( jp )`. I gemelli vivi sono `:3524` e `:3540`, e
sono **già italiani**. Lo stesso vale per **`item_func.hsp:1020`** (`"No."`),
dentro l'`if ( jp )` di `*itemNameSub`.

### Tre righe di servizio

**`item_data.hsp:339`, `s = "error:" + val + "/" + val(1)`** — il valore di
ripiego di `*item_encdetail`, sovrascritto poche righe sotto quando
l'incantamento si riconosce. Se il giocatore lo vede, sta guardando un difetto:
tradurlo ne nasconderebbe la natura a chi lo segnala. È la stessa scelta dei
messaggi di `dbg_*`.

**`main.hsp:3258`, `txt "lv:" + gdata(GDATA_LEVEL)`** — dentro il tasto **F7**
del modo mago (`// Wizard F7 reload/regen map`), che rigenera la mappa. Testo
che esiste solo per chi sviluppa, come `screen.hsp:1125` e `system.hsp:4400`.

**`map_rand.hsp:691`** — la nona riga dello stesso dump, già nominata altrove.

## Quattro oggetti che restano senza articolo, e perché — 131ª

L'articolo italiano di un oggetto sta in `ioriginalnamearticolo(ITEM_ID)`, cioè
in un array **indicizzato per tipo d'oggetto**. Vale finché la testa del nome è
una proprietà del tipo. Per dodici oggetti non lo è: `ioriginalnameref` è la
stringa vuota in tutt'e due i rami di lingua, e il nome lo compone
`item_func.hsp` con un `if` sull'identità.

    if ( inv(INV_ITEM_ID, itemowner_itemid) == ITEM_ID_COFFEE ) {
        if ( ibit(ITEM_BIT_ACIDPROOF, itemowner_itemid) == 1 ) {
            locvar_itemowner_s += lang("カフェオーレ", "caffelatte")

Un nome che non sta nell'array non ha articolo nell'array, e il gioco ripiegava
sull'inglese: «a caffe'», «a te' nero». ⚠️ **E questi ripiegavano sempre**, anche
da identificati: non è il difetto della borraccia, che riguardava il solo stato
non identificato.

Di quei dodici, **due** erano già curati (`ITEM_ID_FISH` e `ITEM_ID_FISH_JUNK`:
la specie sta in `SUB_NAME` e ha `fishdatanarticolo`, un array suo) e **sei**
sono stati curati nella 131ª, perché la testa ha genere costante in tutte le
varianti del ramo: `COFFEE` («caffè»/«caffelatte»), `BLACK_TEA` («tè nero»/«tè
al latte») e i quattro `POTIOMAN`. La cura è una riga d'articolo in
`db_item.hsp`, generata da `genera_toppe_nomi.py` §12.

**I quattro qui sotto no, e non per pigrizia: il loro articolo non è un dato del
tipo d'oggetto.** La testa del sintagma cambia da esemplare a esemplare, quindi
non esiste una costante da mettere in un array indicizzato per `ITEM_ID`. Vanno
curati dove il nome si compone, non dove il tipo si dichiara.

| oggetto | perché la testa cambia |
|---|---|
| `ITEM_ID_JUICE` | il nome è `iknownnameref(SUB_NAME) + " " + mix/milk`: la testa è **il frutto**, cioè il nome di un altro oggetto. Il genere è quello del frutto |
| `ITEM_ID_NECRO_PARTS` | la testa è **la parte del corpo** — le nove `lang()` di `item_func.hsp:1034` — e il nome della creatura segue dopo « di ». ⓘ Quelle nove oggi stanno nel ramo `& jp`, la settima famiglia di riga morta trovata nella 129ª: il giorno che vivranno, l'articolo servirà davvero |
| `ITEM_ID_PRODUCED_BOOK` | la testa è il titolo **generato** dal gioco (`_bookselfs`), diverso a ogni libro che il giocatore scrive |
| `ITEM_ID_EVITEM` | il nome sta fra parentesi angolari, `"<" + evitemn(...)`. ⓘ Prima di dargli un articolo va deciso **se una marca `<>` lo vuole**: è la domanda dei nomi in 《》, non quella dell'articolo — e il progetto su quelli ha già una regola |

⭐ **L'elenco non è una nota: è un dato che una rete legge.**
`scratchpad/_131-quanti-articoli-inglesi.py` porta gli stessi quattro nomi in
`DICHIARATI`, e fallisce in tutt'e due i versi — se compare un quinto oggetto
senza articolo lo chiama `SCONOSCIUTO`, e se uno di questi quattro *smette* di
ripiegare lo chiama `STANTIO`, perché allora la riga qui sopra sarebbe diventata
una bugia. È il modo di `strumenti/maiuscole.py`: il referto non chiede zero,
chiede che l'elenco non si allunghi da solo.

## Le sei battute della nuvoletta che restano identiche — 138ª

Il lotto D della Fase 6 ha reso 68 battute del gioco di carte su 74. Le sei qui
sotto sono **decise**, non dimenticate, e la differenza la tiene un dato: la
loro voce in `dizionario/carte/dialoghi.jsonl` non ha `it`, ha `invariata` con
dentro la ragione, e `dialoghi.decise()` le conta insieme alle rese. Senza quel
campo il referto direbbe per sempre «6 da fare» su un lavoro che non c'è, ed è
lo stesso motivo per cui questo file esiste.

⚠️ **La sezione dei versi qui sopra copre il criterio, non l'elenco**: quattro
di queste sei non sono versi di creatura ma segni di punteggiatura, e stanno
qui per il precedente di `???` (`chat.hsp:19135`) — *la punteggiatura non ha
lingua*.

| valore | motivo |
|---|---|
| `*vroom*` | `tcg_skill.hsp:1040`, il camioncino del ladro (`CREATURE_ID_THIEF_LIGHT_TRUCK`) che si muove in campo. È il rumore di un motore, e in italiano si scrive con le stesse lettere: dentro non c'è nessuna parola da rendere |
| `AIEEE!!!` | `tcg_skill.hsp:1068`, l'urlo di una carta che finisce nel cimitero. Quattro lettere e tre punti esclamativi: un suono, non una parola inglese, e in italiano si legge uguale |
| `!!!!` | `tcg_skill.hsp:1407`, quel che dice una carta che sta per perdere lo scontro. È punteggiatura, e la punteggiatura non ha lingua |
| `!@#$` | `tcg_skill.hsp:1415`, l'imprecazione mascherata dei fumetti (*grawlix*). Non sono parole: sono i segni sopra i tasti dei numeri, uguali in ogni lingua |
| `!` | `tcg_skill.hsp:7435`, il punto esclamativo che chiude la battuta di `<Aime>` **dopo** `_onii()`: la riga è `"Hahaha! Hope you like Aime's Deck, " + _onii(...) + "!"`, e questo è il pezzo dopo la variabile. Un segno, non una parola. ⚠️ La prima metà **si traduce** ed è tradotta: qui la cornice e il testo stanno in due letterali diversi, al contrario di `[Made by][` |
| `Faaaaaaaa!! Oh Oh Oh Oh!` | `tcg_skill.hsp:6620`, una delle dieci battute a caso di `<Rianna>` quando gioca male: otto «a» e quattro «Oh». È la risata-lamento, non una frase, e in italiano si legge uguale |

## Le sigle nude che il glossario aveva già deciso — 138ª

⚠️ **Non sono decisioni nuove: sono decisioni scritte.** `glossario.md` mette
`DV`, `PV`, `HP`, `MP`, `SP`, `AP` fra gli invariati da sessioni («il giapponese
stesso le scrive in latino»), ma queste tre stanno **fuori da `lang()`**, nude
dentro un `mes`, quindi nessun dizionario le raggiunge e nessuna riga le
dichiarava. La rete di `disegnate.py` le ha ritrovate e le ha chiamate «da
fare», che era falso: quel che mancava era questa riga.

⭐ È la ragione per cui una decisione va scritta **dove la cerca chi misura**, e
non solo dove la cerca chi traduce.

| valore | motivo |
|---|---|
| `Dv:` | `command.hsp:14191` e `:14205`, la difesa nella scheda del personaggio. `glossario.md` tiene `DV` fra gli invariati, e la riga **sotto** questa traduce `EquipWt:` dentro una `lang()`: la sigla resta, l'etichetta si traduce. ⚠️ Il valore dichiarato è `Dv:` coi due punti, perché il letterale è quello — `mes "Dv:" + dvr1` |
| ` Pv:` | `command.hsp:14191` e `:14205`, la protezione, sulla stessa riga di `Dv:` e per la stessa ragione. ⚠️ Lo spazio iniziale è portante: separa le due sigle |
| `Sp` | `screen.hsp:417`, la resistenza nella barra in basso (`bmes "Sp" + cdata(CDATA_SP...)`). Stessa famiglia, e in più lo slot è quello: 38 px dal bordo |
| `Omae wa mou shindeiru.` | `proc.hsp:14392`, la citazione di Ken il guerriero in *romaji* dentro un gioco giapponese. ⚠️ **Non è inglese lasciato lì**, ed è il rovescio di `Info` e `t `: qui non è italiano che coincide, è una citazione che in italiano circola in questa forma. Tradurla — «tu sei già morto» — la spegnerebbe, perché quel che si riconosce è la frase giapponese, non il suo senso |

## Le sigle e i segni nudi che la rete dello schermo ha ripresentato — 139ª

Stessa specie della sezione qui sopra, e stesso movente: `disegnate.py` parte
da **chi manda un testo a schermo**, quindi vede anche i letterali che non
passano da nessuna `lang()` — e per quelli nessun dizionario è mai stato il
posto dove scrivere una decisione. Le tre righe qui sotto non traducono niente:
dichiarano perché non c'è niente da tradurre.

⚠️ **`Lv` non contraddice il « liv.» che il dizionario usa altrove, e il
criterio è il giapponese.** Dove il giapponese scrive la **parola** レベル,
l'italiano scrive la parola: `command.hsp:8896`-`:8900` è
`lang("制限レベル1", "Limiter LV.1")` e la resa è «Limite liv. 1». Dove il
giapponese scrive **`Lv` in lettere latine**, è una sigla e resta:
`item_func.hsp:2156` è `lang(" Lv", " Lv. ")`, `text.hsp:65` e `:68` sono
`lang("拒食Lv0", "Anorexia-Lv0")` e `lang("病気Lv0", "Sick-Lv0")`. ⭐ Le «tre
grafie per la stessa cosa» aperte dalla 138ª sono **tre cose diverse**: una
sigla, una parola e — `main.hsp:3258` — una traccia di debug che esce solo col
tasto F7 della modalità mago. Nessuna delle tre si tocca.

| valore | motivo |
|---|---|
| `Lv` | `screen.hsp:423`, la sigla del livello nella barra in basso: `bmes "Lv" + cdata(CDATA_LEVEL, CHARA_PLAYER) + "/" + (...)`. È la vicina di `Sp` (`:417`, sei righe sopra) e della stessa famiglia di `Dv:` e ` Pv:`, e il progetto la scrive già così in `action.hsp:6545`. ⚠️ La riga ` Lv. ` più in alto in questo file dichiara **lo stesso** per la sfera dei mostri: quella porta il punto e lo spazio perché il numero segue subito, questa no |
| `,Tab ` | `command.hsp:14077` e `module.hsp:5195`, lo stesso suggerimento di tasto in due file: `"" + key_prev + "," + key_next + ",Tab " + lang("[メニュー切替]", "[Change]")`. **`Tab` è la scritta stampata sul tasto**, identica su una tastiera italiana, e `key_prev` / `key_next` sono i due tasti diagonali che il giocatore si configura (`config.hsp:332`). Quel che c'è da tradurre sta dentro la `lang()` accanto, ed è tradotto: «[Cambia menu]» qui, «[Cambia]» là. ⚠️ **Non è in contraddizione con `command.hsp:11849`**, dove «Right,left [Change]» diventa «Dx,Sx [Cambia]»: lì sono due parole — destra e sinistra — qui è il nome di un tasto. ⚠️ La virgola in testa e lo spazio in coda sono la cornice dell'elenco e contano |
| `Immune` | `tcg.hsp:969`, l'etichetta del tratto `TCG_BIT_IMMUNE` nella scheda di una carta. **Italiano che coincide**: «immune» si scrive così. ⚠️ **Non è una decisione nuova: è una decisione della 127ª rimasta in prosa** — la sezione «Le ultime righe nude sparse» qui sopra la spiega da undici sessioni, ma la spiega in un paragrafo, e i paragrafi non li legge nessuno strumento. È la lezione della 138ª applicata all'indietro: una decisione va scritta dove la cerca chi misura |
| `Mana ` | `tcg.hsp:3480`, il mana del giocatore nel riepilogo di inizio partita (`mes "Mana " + cpdata@tcg(TCG_PLAYER_MAX_MANA, 0)`). `glossario.md:52` tiene «Mana» fra gli invariati da sessioni — «termine acquisito» — e le tre righe sorelle (`"Life "`, `"Card "`, `"Domain * "`) sono già toppate. ⚠️ **Lo spazio in coda è portante**: separa la parola dal numero, ed è la ragione per cui la riga del glossario non bastava — il valore dichiarato là è `Mana`, questo è `Mana ` |
| `d` | `command.hsp:10750`, la «d» dei dadi nella riga della protezione della scheda: `mes "" + (100 - 10000 / (prot + 100)) + "% + " + protdice1 + "d" + protdice2`, che a schermo fa «2d5». **Non è una parola: è la notazione dei dadi**, e in italiano si scrive con la stessa lettera — «2d5» si legge «due dadi a cinque facce» in tutt'e due le lingue. È il caso di `t ` e di `Info` visto dal lato della notazione invece che da quello dell'abbreviazione |

## Le sigle del pannello dell'equipaggiamento che la rete del salto ha ripresentato — 141ª

Stessa specie delle due sezioni qui sopra, e la terza rete che le ripresenta.
`strumenti/salti.py` parte da chi disegna e **segue la variabile anche quando
l'assegnazione sta dentro un `if` a graffe**: `item_func.hsp:2612`-`:2626`
riempie `locvar_equipinfo_s` così quindici volte, con le sigle a quattro
caratteri delle abilità potenziate su un oggetto equipaggiato.

⭐ **Quattordici delle quindici si toppano** — `Read` diventa `Lett`, `Hv-A`
diventa `Cora` — e le fa `strumenti/genera_toppe_tag_equip.py`, che ricava ogni
sigla dal nome italiano dell'abilità e rilegge il dizionario per accorgersi se
quel nome cambia. Qui sotto sta l'unica che non si tocca.

⚠️ Il tetto è di **quattro caratteri**, e non è una stima in pixel:
`item_func.hsp:2629` fa `strmid(locvar_equipinfo_s, 0, 4)`. Una sigla più
lunga non sborda dal pannello — viene tagliata.

| valore | motivo |
|---|---|
| `Trap` | `item_func.hsp:2623`, la sigla di `Disarmo trappole` nel pannello dell'equipaggiamento. **Italiano che coincide**, come `Info`, `t ` e `Immune` nelle sezioni qui sopra: la sigla abbrevia «trappole», che si scrive con le stesse quattro lettere di `trap`. ⚠️ **Non è l'inglese lasciato lì per pigrizia**: le altre quattordici sigle della stessa fila sono tutte cambiate, e questa è l'unica dove la forma italiana e quella inglese arrivano allo stesso posto. Cambiarla — `D-Tr`, `Dis.` — allontanerebbe la sigla dalla parola che il giocatore legge nella lista delle abilità, che è proprio quel che il rinvio al dizionario esiste per impedire |

## Le dodici parole chiave delle carte che stavano solo nel glossario — 141ª

⚠️⚠️ **Nessuna di queste dodici è una decisione nuova: erano tutte già prese, e
scritte in `glossario.md`.** La sezione «Le affiliazioni fra parentesi
angolari» (`glossario.md:3006`) chiude con la riga «**Invariate:** `<Yerles>`,
`<Xeren>`, `<Zanan>`, `<Lothrian>`, `<Eulderna>`, `<Elea>`, `<Juere>`,
`<Zaile>` (nomi propri di civiltà), `<Ninja>` (uguale in italiano), `<CNPC>`
(sigla tecnica)», e quella sopra dice che `Immune` e `Kamikaze` restano
invariate «per decisione, non per dimenticanza».

⚠️ **E nessuno strumento legge un paragrafo.** È la terza volta che succede —
la 138ª l'ha imparato su `Dv:`, la 139ª su `Immune` di `tcg.hsp:969` — e la
terza rete a ripresentarle è `strumenti/salti.py`, che segue `s@tcg` anche
quando l'assegnazione sta dentro un `if` a graffe (`tcg.hsp:1533`-`:1585`,
`*tcgdraw_WEND1`, la riga dei tratti sulla scheda di una carta). Le
quarantasei sorelle della stessa colonna sono tradotte da toppe; queste dodici
no, e senza una riga qui il censimento avrebbe continuato a chiederle.

⚠️ **Lo spazio in coda è portante e fa parte del valore.** I tratti si
concatenano uno dopo l'altro in `s@tcg`, e lo spazio è quel che li separa a
schermo: il valore dichiarato è `<Elea> `, non `<Elea>`. È la stessa ragione
per cui `Mana ` è una riga diversa da `Mana` più in alto in questo file.

⭐ E il confine passa in mezzo alla colonna, non attorno: `<Bandit> `,
`<Citizen> `, `<Mercenary> `, `<Teacher> `, `<Adventurer> `, `<Pirate> `,
`<Flame> `, `<Elea Mob> ` e le tre gilde **si traducono** e sono toppate, perché
sono nomi comuni. Restano solo i nomi propri, e le due parole che l'italiano
scrive uguali.

| valore | motivo |
|---|---|
| `<Yerles> ` | `tcg.hsp:1565`, l'affiliazione della carta. **Nome proprio di civiltà del canone Elona**, già invariato in `glossario.md:289` insieme agli altri: «in italiano c'è sempre, perché nel nome c'è sempre» — `Yerles machine infantry` è «la fanteria meccanica Yerles». ⚠️ Lo spazio in coda separa il tratto dal successivo |
| `<Xeren> ` | `tcg.hsp:1566`, per la stessa ragione di `<Yerles> `: nome proprio di popolo |
| `<Zanan> ` | `tcg.hsp:1571`, nome proprio di nazione. `glossario.md:2641` e `:2666` lo tengono così anche nei titoli dei libri: «Parole di un Ricercatore di Zanan» |
| `<Lothrian> ` | `tcg.hsp:1572`, nome proprio di popolo. ⚠️ Il glossario scrive la nazione «Lothria» (`:899`) e l'aggettivo di popolo resta `Lothrian` com'è nel canone: sono due parole diverse, e questa è l'etichetta della carta |
| `<Eulderna> ` | `tcg.hsp:1573`, nome proprio di popolo. `glossario.md:2794`-`:2808` lo usa invariato come aggettivo in nove rese: «un ricercatore Eulderna» |
| `<Elea> ` | `tcg.hsp:1574`, nome proprio di popolo (`TCG_BIT_ELEAREFUGEE`). ⚠️ **Non è in contraddizione con `<Elea Mob> ` → `<Folla Elea> `**, che si traduce: lì la parola comune «folla» c'è e si rende, qui il tratto è il solo nome del popolo |
| `<Juere> ` | `tcg.hsp:1576`, nome proprio di nazione. ⚠️ `glossario.md:289` avverte che ジューア (Juere) **non è** ジュア (Jure), la dea: un carattere di differenza, e le due si somigliano anche in italiano |
| `<Zaile> ` | `tcg.hsp:1578`, nome proprio. `glossario.md:1461` lo fissa su ザイール, ed è quello degli «Atlante dei Minerali di Zaile» |
| `<Ninja> ` | `tcg.hsp:1580`. **Italiano che coincide**, come `Info` e `t ` nelle sezioni qui sopra: «ninja» è la parola italiana, prestito acquisito. ⚠️ Non è un nome proprio come le otto righe qui sopra, ed è la ragione per cui ha un motivo suo: i suoi vicini di colonna — `<Teacher> ` → `<Insegnante> `, `<Adventurer> ` → `<Avventuriero> ` — sono nomi comuni e infatti si traducono |
| `<CNPC> ` | `tcg.hsp:1585`. **Sigla tecnica, non una parola**: è la cartella dei *Custom NPC* che il giocatore si mette da sé, e il tratto dice che la carta viene di lì. Stessa famiglia di `DBID`, che la riga di stato dell'editor di mazzo tiene identico |
| `Immune ` | `tcg.hsp:1549`, il tratto dell'immunità nella riga dei tratti. **Italiano che coincide**: «immune» si scrive così. ⚠️ **Non è un doppione della riga `Immune` più in alto in questo file**: quella è `tcg.hsp:969`, un `bmes` nella scheda della carta, questa è la voce della colonna dei tratti e porta lo spazio di separazione. Il confronto di `verifica.py` è sulla stringa intera, e le due stringhe sono diverse |
| `Kamikaze ` | `tcg.hsp:1558`, il tratto di `TCG_BIT_SUICIDE`. **Italiano che coincide**: «kamikaze» è prestito acquisito, e lo usa anche chi non sa che cosa voglia dire in giapponese. ⚠️ La costante dice `SUICIDE` e la parola no — ma quel che il giocatore legge è la parola, e l'inglese di monte ha già scelto il prestito invece di `Suicide` |

## Le sigle nude della scheda e della lista dei compagni — 141ª

Stessa specie delle tre sezioni qui sopra, e la stessa rete: `strumenti/salti.py`
segue `s` **dentro il blocco che lo disegna**, e in `command.hsp` ha ripresentato
diciotto letterali che nessuna delle due reti vecchie vedeva. Quattordici sono
sigle e unità di misura, e stanno qui.

⚠️ **Il criterio non è nuovo: è quello che la 138ª e la 139ª hanno già usato su
`Dv:`, ` Pv:`, `Sp` e `Lv`.** Dove il giapponese scrive la parola, l'italiano
scrive la parola; dove il sorgente scrive una sigla latina **nuda, fuori da
`lang()`**, quella sigla la legge anche chi gioca in giapponese — cioè è una
sigla che il gioco di monte ha scelto per tutt'e due le lingue, e l'italiano
non ha una terza grafia da metterci.

⚠️ **Gli spazi in testa e in coda sono portanti e fanno parte del valore.** Le
sigle si concatenano una dopo l'altra in `s`, e lo spazio è quel che le separa:
il valore dichiarato è ` DV:`, non `DV:`, e ` Lv.` è una riga diversa da `Lv.`.
È la ragione per cui `verifica.py` legge i valori fra apici inversi verbatim.

⚠️ **Restano fuori di qui quattro cose di `command.hsp`, dichiarate in
`salti.DICHIARATI`**: tre pezzi di percorso di file — che non sono testo — e
`Rank.`, che è l'unica **parola** delle diciotto e va decisa guardando la
schermata, perché il progetto rende `Rank` con «Rango» dappertutto e la colonna
in cui sta è larga 140 px.

| valore | motivo |
|---|---|
| `Lv:` | `command.hsp:188`, il livello nella riga che descrive il bersaglio (`s += " " + "Lv:" + cdata(CDATA_LEVEL, …)`). Sigla latina nuda: la stessa famiglia di `Lv` di `screen.hsp:423`, già invariato dalla 139ª, e il progetto la scrive così anche in `action.hsp:6545` |
| ` DV:` | `command.hsp:189`, la schivata, sulla stessa riga e per la stessa ragione. ⚠️ **Non è un doppione di `Dv:`**, dichiarato più in alto per `command.hsp:14191`: là è minuscolo e senza spazio, qui è maiuscolo e lo spazio separa dalla sigla precedente. Il confronto è sulla stringa intera, e sono due stringhe |
| ` PV:` | `command.hsp:190`, la protezione, e vale la stessa nota: ` Pv:` di `:14205` è un'altra stringa |
| ` HP: ` | `command.hsp:208`, i punti ferita nella riga del bersaglio. Sigla latina nuda, e i due spazi la staccano dal numero e dalla sigla accanto |
| ` MP: ` | `command.hsp:208`, i punti magia, sulla stessa riga di ` HP: ` e per la stessa ragione |
| `Hp:` | `command.hsp:1348` e `:3614`, la percentuale di vita nella lista dei compagni e in quella dei png (`"Hp:" + … + "%"`). Terza grafia della stessa sigla — `HP`, `Hp:`, ` HP: ` — e sono tre stringhe diverse perché tre punti diversi del gioco le scrivono diversamente: l'italiano non uniforma quel che il monte tiene separato |
| `Lv.` | `command.hsp:1365` e `:3631`, il livello nella lista dei compagni (`"Lv." + … + " "`). ⚠️ Il punto è l'abbreviazione, e in italiano si abbrevia con lo stesso punto: `item_func.hsp:2156` scrive già `lang(" Lv", " Lv. ")` |
| ` Lv.` | `command.hsp:1468`, la stessa sigla con lo spazio davanti, perché lì segue un altro campo |
| `(Hp: ` | `command.hsp:1387` e `:1401`, la vita fra parentesi in coda al nome del compagno. La parentesi e lo spazio sono la cornice, `Hp` è la sigla di sopra |
| `(MAX)` | `command.hsp:2131`, il tratto che ha raggiunto il livello massimo (`traitrefn2(…) + "(MAX)"`). **Italiano che coincide**: «MAX» è l'abbreviazione internazionale, e in italiano si scrive uguale — la forma piena, «(MASSIMO)», è cinque caratteri più lunga in una riga che porta già il nome del tratto |
| ` cm` | `command.hsp:10659`, l'altezza nella scheda del personaggio. **Unità di misura del sistema internazionale**: non ha lingua, e in italiano si scrive con le stesse due lettere minuscole. Lo spazio davanti stacca dal numero |
| ` kg` | `command.hsp:10659`, il peso, sulla stessa riga e per la stessa ragione |
| `p ` | `command.hsp:11020` e `:11023`, il costo in punti per allenare o imparare un'abilità (`calctraincost(…) + "p "`). **Italiano che coincide**: la parola è «punti», l'abbreviazione italiana è la stessa lettera. ⚠️ È esattamente il caso di `t ` per i turni, dichiarato più in alto in questo file, e lo spazio in coda conta allo stesso modo |
| ` x` | `command.hsp:12450`, il moltiplicatore nella riga del danno (`"" + dice1 + "d" + dice2 + … + " x" + …`), che a schermo fa «2d5+3 x1.5». **Non è una parola: è il segno di moltiplicazione**, e in italiano si scrive con la stessa lettera. È la riga sorella della `d` dei dadi, dichiarata dalla 139ª — e infatti le due stanno nella stessa espressione |
| `GuruGuruSMF4` | `config.hsp:809`, il quarto driver audio del pannello, accanto a `None`, `Direct music` e `MCI`. **Nome di un driver, non una parola**: la riga di `Direct music` più in alto in questo file lo nominava già in prosa — «il terzo e il quarto valore della stessa riga sono `MCI` e `GuruGuruSMF4`, letterali nudi che nessun dizionario raggiunge» — e adesso ha la sua riga, perché una decisione che vive in un motivo altrui non la legge nessuno strumento |
| `Nani?!` | `custom_tweaks.hsp:1679`, la descrizione della modifica «Fist of the North Star Mode» (`TWEAK_MISC_HOKUTO_NO_KEN_MODE`). ⚠️ **È l'altra metà della citazione di Ken il guerriero**, e la prima — `Omae wa mou shindeiru.` — è già dichiarata più in alto in questo file: 「何！？」 è quel che risponde chi se la sente dire, e circola in *romaji* come la frase che la precede. Tradurla — «Cosa?!» — la spegnerebbe, perché quel che si riconosce è il suono giapponese, non il senso |
