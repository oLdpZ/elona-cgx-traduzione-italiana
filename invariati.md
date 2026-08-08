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
| Karma | termine acquisito in italiano |
| Mana | termine acquisito nei giochi di ruolo |
| * | simbolo, non testo: `text.hsp:12` lo stampa come marcatore. Non c'è niente da tradurre |
| . | punteggiatura: `text.hsp:108` sceglie il segno di fine frase. Identica in italiano |
| ? | punteggiatura, idem |
| ! | punteggiatura, idem |
| bonus | prestito acquisito, già in glossario. `strfix` (`text.hsp:190`) etichetta il `+3` di un oggetto |
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
| male? | valore di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| female? | valore di `CDATAN_NEWSEX`; a schermo ci arriva per toppa |
| trans-male | valore di `CDATAN_NEWSEX` |
| trans-female | valore di `CDATAN_NEWSEX` |
| EN | **non è testo, è un marcatore di formato.** `text.hsp` lo usa in 52 punti dentro `instr(buff, 0, "%DEFAULT," + lang("JP", "EN"))` per trovare la sezione di lingua nei testi esterni (`talk.txt`, `board.txt`...). Tradurlo romperebbe la lettura di ogni file esterno. Presente anche in `action.hsp`, `chat.hsp`, `command.hsp`, `help.hsp`, `chara_func.hsp`, `item_func.hsp` |

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
