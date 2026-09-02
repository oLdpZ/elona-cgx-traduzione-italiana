# Glossario EN → IT

Vincolante: un termine tradotto qui si riusa ovunque. Se una resa non funziona
in un contesto, si cambia **qui** e si ritraduce — non si deroga nel lotto.

I termini sono misurati sul sorgente pinnato (i sei file di Fase 1: `text`,
`command`, `action`, `proc`, `skill`, `trait`), non inventati: fra parentesi le
occorrenze quando sono significative. Un glossario gonfio non si consulta.

Per i nomi propri vedi `invariati.md`, che è la lista delle stringhe che restano
in inglese per scelta. Non vanno in queste tabelle.

## Interfaccia e comandi

| EN | IT | note |
|---|---|---|
| Cancel | Annulla | |
| Close | Chiudi | |
| Attack | Attacca | verbo quando è un comando; «Attacco» quando è un'etichetta |
| Change | Cambia | |
| Stop | Interrompi | |
| Report | Resoconto | |
| Analysis | Analisi | |
| Appearance | Aspetto | |
| Ally / Ally List | Alleato / Elenco alleati | coerente con Elin, «Alleato / Ostile / Neutrale» |
| Target | Bersaglio | mai «obiettivo»: qui è sempre il bersaglio di un attacco |
| Item / Items | Oggetto / Oggetti | |
| Weight | Peso | |
| Level | Livello | abbreviato `Lv.` come in inglese |
| Body (slot) | Torso | lo slot d'equipaggiamento di `text.hsp:136`, in fila con Testa · Collo · Schiena · **Torso** · Mano · Anello · Braccio · Vita · Gamba · Tiro · Munizioni. Il giapponese è 胴, «torso»: «Corpo» accanto a Braccio e Gamba sarebbe il tutto in fila con le parti |
| Body (aspetto) | Corpo | l'editor del ritratto, giapponese 体. ⚠️ **campo a larghezza fissa di 8 caratteri**: `"Body    "` → `"Corpo   "`. `"Body CL "` è il colore del corpo e in 8 caratteri non ci sta: da risolvere nel lotto, non qui |
| Body (prosa) | corpo | `Your body is changing every moment.`, `Restore Body` → «Ripristina Corpo», `Body Blow` → «Colpo al corpo», `Body Parts` → «Parti del corpo» |

## Statistiche e attributi

Le rese vengono da `Elin - Traduzione Italiana` (`glossario.md`, «Abilità e
talenti»): sono di universo, non di motore, e devono coincidere fra i due
progetti.

| EN | IT | note |
|---|---|---|
| Strength | Forza | |
| Constitution | Costituzione | |
| Dexterity | Destrezza | |
| Perception | Percezione | |
| Learning | Apprendimento | |
| Will | Volontà | |
| Magic | Magia | |
| Charisma | Carisma | |
| Speed | Velocità | |
| Luck | Fortuna | |
| Mana | Mana | vedi `invariati.md`: termine acquisito |
| Karma | Karma | vedi `invariati.md` |

## Combattimento, danno e resistenze

| EN | IT | note |
|---|---|---|
| Damage | Danno | |
| Resistance / Resist | Resistenza / Resiste | il verbo e il sostantivo si distinguono |
| Power | Potenza | |
| Bonus | Bonus | prestito acquisito, invariato |
| Breath | Soffio | l'attacco dei draghi, non «respiro» |
| Poison | Veleno | |
| Fire | Fuoco | |
| Darkness | Oscurità | |
| Mind | Mente | `Mind damage`, `Mind Resistance` → «Danno mentale», «Resistenza mentale»: aggettivo, non complemento |
| Blood | Sangue | |
| Summon | Evoca / Evocazione | |
| Charge | Carica | |
| Sleep | Sonno / Dormi | sostantivo per lo stato, verbo per il comando |
| Gauge | Barra | la barra delle mosse speciali di Elona+. `[50% Gauge]` → «`[Barra 50%]`»: 5 caratteri come l'inglese, e le etichette dell'elenco sono a larghezza compressa. In prosa `power gauge` → «barra di potenza», che si aggancia a `Power` → «Potenza» |
| Chaos | Caos | l'elemento. `Chaos damage` → «Danno caotico», aggettivo come `Mind`. Coincide con Elin (`Nether / Ether / Chaos` → «Oltretomba / Etere / Caos») |
| Skill | Abilità | coincide con Elin. **Non** collide con *ability*, che nel sorgente è quasi sempre prosa generica e in italiano vuole «capacità»: `enhances your ability to hide` → «migliora la capacità di nascondersi» |
| hex | malocchio | ⚠️ **non** «maledizione», che è già `curse`. Il gioco ha due 呪い e li distingue: `cursed` sta sull'**oggetto** e si oppone a `blessed`; `hex` sta sulla **persona** e si oppone a un buff (`command.hsp:10814`, «blessed or hexed»). L'italiano separa le due sullo stesso asse. Il sorgente conferma che il giapponese da solo non bastava: `skill.hsp:440` scrive `呪い(hex)`, con la glossa inglese accanto |

## I nomi degli incantesimi

Tetto **24 caratteri** (`command.hsp:5382-5385`, misurato il 2026-08-09).

| EN | IT | note |
|---|---|---|
| `Dart` | Dardo | il colpo singolo debole, giapponese 魔法の**矢** |
| `Bolt` | Saetta | la linea, giapponese …**ボルト** |
| `Mist of X` | Nebbia di / d'X | |
| `Jail` | Gabbia | `Eclipse Jail` → «Gabbia d'eclissi» |
| `Roar` | Ruggito | |
| `Restore Body` / `Restore Spirit` | Ripristina Corpo / Spirito | già fissato sopra |

⚠️ **`Dart` e `Bolt` non si fondono.** In Elona sono due cose diverse — colpo
singolo contro linea — e l'italiano ha due parole: usarne una sola perderebbe
una distinzione che il gioco fa.

L'elemento è **aggettivo** dove esiste («Saetta mentale», «Saetta caotica»,
«Saetta velenosa», come `Mind damage` → «Danno mentale») e **complemento** dove
no («Saetta di gelo», «Saetta d'oltretomba»).

⚠️⚠️ **E per otto mesi `db_item.hsp` non ha seguito questa riga.** Fino al
2026-08-14 i **15** nomi di libro e di bacchetta della famiglia dicevano
«**dardo**» — «dardo d'oltretomba», «dardo di ghiaccio» — mentre `skill.hsp`
diceva «Saetta». Il giocatore comprava il libro del *dardo* e imparava la
*saetta*, ed erano la stessa magia. Peggio: **cinque nomi su dodici avevano anche
il qualificatore diverso** (`冷気` gelo/ghiaccio, `暗黒` d'oscurità/oscuro, `毒`
velenosa/di veleno, `神経` dei nervi/neurale, `魔法` magica/arcano), quindi non
era una parola sbagliata ma due famiglie parallele. Allineate a `skill.hsp` con
`scratchpad/correzione-bolt.py`. Vedi `decisioni.md`.

💡 **La lezione non è «rileggere il glossario»**: la riga qui sopra c'era già ed
era giusta. È che **nessuno strumento confronta il glossario col dizionario**, e
`battute --divergenti` guarda solo `db_creature.hsp` (misurato nella 29ª). Una
regola scritta e non sorvegliata vale finché qualcuno se la ricorda.

⚠️ E la ricerca va fatta sull'**inglese**, non sul giapponese: le tre *bacchette*
hanno un nome giapponese poetico che non contiene `ボルト` — 稲妻の軌跡 «la scia
della folgore», 炎の衝撃, 氷の視線 — e cercando il katakana si perdono. La prima
passata della correzione ne ha corrette 12 su 15 proprio per questo.

⚠️ `Hero` → **«Eroismo»**, non «Eroe»: è un'etichetta di stato, e vale la
regola dei sostantivi astratti di `guida-stile.md`. `Incognito` resta identico
e sta in `invariati.md`: è la stessa parola latina, non una svista.

## Gli atomi delle etichette di `skilldesc`

Le 348 descrizioni di incantesimi e mosse speciali non sono prosa: sono formule
che si ripetono. Questi pezzi valgono **ovunque ricompaiano**, e cambiarne uno
significa ritradurre la famiglia intera.

| EN | IT | note |
|---|---|---|
| `Target(X)` | `Bersaglio(X)` | giapponese 属性の**矢**, la freccia a bersaglio singolo |
| `Line(X)` | `Linea(X)` | 属性の**ボルト** |
| `Surround(X)` | `Area(X)` | 属性の**範囲攻撃**, «attacco ad area» alla lettera. Più corto dell'inglese, e non collide con `AOE`, che resta sigla |
| `Breath(X)` | `Soffio(X)` | 属性の**放射攻撃** |
| `Indiscriminate(X)` | `Indiscriminato(X)` | |
| `[N% Gauge]` | `[Barra N%]` | deciso il 2026-08-07 |
| `[N%GaugeDomain]` | `[Barra N%]` | ⚠️ l'inglese distingue il costo dalla portata (全域, «tutta l'area»); l'italiano tiene l'etichetta uguale alle altre e mette la portata nel testo |
| `Con-Attack/X` | `Attacco Cos/X` | 耐久属性攻撃: `Con` è **Costituzione** |
| `AOE`, `PVDV`, `SP`, `MP`, `HP`, `PURGE` | invariati | in fila con `PV fixer` → «correttore di PV» e «Assorbe SP», già in dizionario |
| `WIL-Check:` e i sei fratelli | `Vol:`, `Per:`, `Des:`, `For:`, `Mag:`, `Car:` | le sigle da 3 caratteri già fissate in `text.hsp:61` |

⚠️ **Due sigle inglesi sono la stessa cosa scritta due volte, e il giapponese lo
dice.** `END` e `CON` sono entrambe 耐久 (`Apply Bleeding/Weaken END` contro
`Gravity and CON attack`); `CHR` e `CHA` sono entrambe 魅力. In italiano
diventano una sola resa — **Cos** e **Car** — e la doppia grafia sparisce.

## Stati e qualità

| EN | IT | note |
|---|---|---|
| blessed / Blessed | benedetto | mai «consacrato»: il gioco lo contrappone a *cursed*. Nel sorgente è quasi sempre minuscolo (16 occorrenze contro 4), dentro le frasi |
| cursed / Cursed | maledetto | 40 occorrenze minuscole contro 3 maiuscole |
| `strblessed` / `strcursed` / `strdoomed` | con benedizione / con maledizione / con dannazione | ⚠️ **eccezione motivata alle due righe sopra**, e vale solo per le tre stringhe che `item_func.hsp` antepone al nome di un oggetto. Lì «benedetto» si accorderebbe con un oggetto di genere ignoto — «mantello benedetto», «pozione benedetta» — quindi diventa un complemento, e la toppa lo sposta **dopo** il nome: «mantello leggero di platino con benedizione». Nelle frasi in prosa resta «benedetto»: è un'altra firma |
| Full | Sazio → *riscrivere* | mai riferito al giocatore: il genere non si conosce. `You are too full` → «Non riesci a mangiare altro» (vedi `guida-stile.md`) |

## I nomi degli status (`buffname`, 2026-08-13)

⚠️ **44 dei 71 non si decidono qui**: il loro giapponese è già reso in
`skill.hsp`, perché un buff e l'incantesimo che lo concede sono la stessa cosa
(`decisioni.md`, «Un buff è l'incantesimo che lo concede»). Quelli si copiano.
Sotto ci sono solo le **27 rese nuove**.

| EN | IT | note |
|---|---|---|
| `Grow Strength` … `Grow Speed` | `Crescita della forza`, `… della costituzione`, `… della destrezza`, `… della percezione`, `… dell'apprendimento`, `… della volontà`, `… della magia`, `… del carisma`, `… della velocità` | i nove nomi d'attributo vengono da `skill.hsp`: inventarne altri qui li avrebbe sdoppiati |
| `Form Shift (A)/(B)/(G)/(D)` | `Cambio di forma (A)/(B)/(G)/(D)` | stesso giapponese 「フォルムシフト」, quattro inglesi: la lettera è l'unica cosa che li distingue e si conserva |
| `Final Form Shift` | `Cambio di forma finale` | |
| `Punishment` | `Punizione divina` | 天罰 è il castigo del cielo, non una punizione qualsiasi |
| `Luck` / `Unlucky` | `Fortuna` / `Sfortuna` | sostantivi: `Sfortunato` vorrebbe il genere di chi lo subisce |
| `Distracted` | `Distrazione` | idem, e vale la regola delle etichette di stato |
| `Melancholy` | `Malinconia` | |
| `Life Tasting` | `Gusto della vita` | |
| `Black Mirror` | `Specchio d'ossidiana` | 黒曜鏡 porta il materiale che l'inglese perde: si traduce la base |
| `Flame of Life` | `Lume della falsa vita` | 偽命 è la vita **falsa**, e l'inglese la perde |
| `Curse of Hunger` | `Maledizione della fame` | |
| `Chain of Mana` | `Catena del mana` | |
| `Shooting Mode` | `Modalità tiro` | |
| `Disinfection` | `Disinfezione` | |
| `Energy MAX` | `Energia al massimo` | |
| `Charge` | `Carica` | il dizionario lo dava sia `Carica` sia `carica`: un'etichetta vuole la maiuscola |

## Mondo e luoghi

| EN | IT | note |
|---|---|---|
| Guild | Gilda | `Mages Guild` → «Gilda dei Maghi», `Thieves Guild` → «Gilda dei Ladri» |
| Gold | Oro | la valuta di Elona; in Elin è «Oren» e resta invariata, qui no |
| Area | Area | parola identica in italiano, ma **non** metterla in `invariati.md`: come stringa intera compare solo in contesti dove «Area» è già italiano |
| Ground | Terreno | «per terra» quando è dove cadono gli oggetti |
| Abyss | Abisso | il luogo: `The Abyss of Magic` → «L'Abisso della Magia», `<Abyss Princess>` → «`<Principessa dell'Abisso>`» |
| abyss power | potere abissale | la risorsa che si spende. Aggettivo e non complemento, come `Mind` → «Danno mentale»; e non deroga a `Power` → «Potenza». Nell'etichetta stretta delle mosse abissali la sigla resta «Abisso»: `SAN300/Abisso300/…`, un carattere in più dell'inglese |
| Port Kapul | Porto Kapul | `Port` è parola comune, `Kapul` no: vedi la regola qui sotto |
| Cyber Dome | Cupola Cibernetica | idem, entrambe le parole sono comuni |
| magical conductor<br>Conductive Cell ⚠️ | conduttore magico | 魔導体, l'organo che conduce la magia nelle cellule: `db_item.hsp:45613` e `:46885` (114ª). ⚠️ **Non è nel dizionario in nessuna forma**, e l'inglese lo chiama in due modi diversi nelle due righe — coniato qui perché serviva, e messo per iscritto perché la prossima riga che lo nomina non lo reinventi |

## Gli oggetti della trama, fissati dal quiz prima che dal loro file

Il quiz di `text.hsp` nomina sette pietre magiche e quattro oggetti del sole.
**Tre pietre e un ankh sono oggetti veri della trama**, ma il loro nome non vive
in `db_item.hsp`: sta in `chara_func.hsp`, che **non è ancora nel dizionario**.
Le risposte del quiz sono state tradotte per prime, quindi qui il precedente lo
fissa il quiz: quando `chara_func.hsp` entrerà nella pipeline, queste rese non
si reinventano, si copiano.

| EN (`chara_func.hsp`) | IT | dove |
|---|---|---|
| `[Sage's Magic Stone]` | pietra magica del saggio | `chara_func.hsp:7359` |
| `[Fool's Magic Stone]` | pietra magica del folle | `chara_func.hsp:7347` |
| `[King's Magic Stone]` | pietra magica del conquistatore | `chara_func.hsp:7353`, giapponese 覇者 |
| `[Ankh of The Sun]` | ankh del sole | `chara_func.hsp:7448` |

⚠️ Le altre quattro pietre (`dell'eremita`, `del re`, `dei morti`, `del santo`) e
i tre oggetti del sole (`bilancia`, `torque`, `collare`) sono **esche del quiz**:
non esistono come oggetti. `王者` → «del re» e `覇者` → «del conquistatore» vanno
tenuti distinti, perché il quiz li mette fianco a fianco apposta.

⚠️ Stessa trappola per i segugi: il quiz «qual è il nome esatto» offre tre nomi
falsi accanto a quello vero. `混沌ハウンド` **non** si rende «il segugio del
caos», perché quello è `カオスハウンド`, una creatura che esiste
(`db_creature.hsp:109000`): due opzioni identiche renderebbero la domanda
irrisolvibile. I falsi sono «degli inferi», «delle tenebre» e «caotico», vicini
ai veri «dell'oltretomba», «dell'oscurità» e «del caos» senza toccarli.

## Armi e armature

Il lotto dell'equipaggiamento (`db_item.hsp`, filtri `/metal/`, `/sharp/`,
`/soft/`, 94 nomi, 2026-08-08). Questi termini sono **teste di famiglia**: si
ripresentano decine di volte con un modificatore davanti, e cambiarne uno dopo
significa ritradurre tutta la famiglia.

| EN | IT | note |
|---|---|---|
| shield | scudo | `kite shield` → «scudo a mandorla», che è il nome storico italiano; `tower shield` → «scudo a torre» |
| mail | corazza | ⚠️ **non** «cotta»: `chain mail` è «cotta di maglia» perché lì la cotta è la cosa, ma `plate mail` è «corazza a piastre» e `light mail` «corazza leggera» |
| armor | armatura | resta distinto da `mail`: l'inglese usa i due, e l'italiano ha entrambe le parole |
| helm | elmo | |
| gauntlets | guanti d'arme | ⚠️ distinti da `gloves` → «guanti». La coppia regge la distinzione che l'inglese fa fra protezione e indumento. **Eccezione nota**: `decorated gloves` è reso «guanti d'arme decorati» benché l'inglese dica *gloves* — nel sorgente sta nello stesso ramo di `thick gauntlets` (`item_func.hsp:1849-1850`), quindi è un guanto d'arme che l'inglese chiama male |
| boots | stivali | maschile **plurale**: il genere nel dizionario è `mp` e l'articolo è partitivo, «degli stivali» |
| shoes | scarpe | femminile plurale, `fp` |
| girdle | cintura | |
| cloak | mantello | |
| composite | composito | l'aggettivo della famiglia «lega/sintetico» di Elona: `composite ring/helm/mail/girdle` → «composito, -a». Coerente con `composite boots` → «stivali compositi», già in dizionario |
| armored | corazzato | `armored ring/boots/cloak` |
| plate | a piastre | complemento e non aggettivo: `plate mail` → «corazza a piastre», `plate girdle` → «cintura a piastre» |
| scythe / sickle | falce / falcetto | due oggetti diversi in Elona, e l'italiano li distingue per taglia |
| lance / spear | lancia da cavaliere / lancia | l'inglese ha due parole, l'italiano una sola: la distinzione si tiene col complemento, non con un secondo sostantivo |
| bow / crossbow | arco / balestra | |
| claymore | spadone | il giapponese dice 大剣, «grande spada»: il nome scozzese in italiano non aggiunge nulla, «spadone» è la parola vera |
| bardish | ascia lunga | 大斧, «grande ascia». «Bardiche» in italiano non si legge, e resta distinta da `battle axe` → «ascia da battaglia» |

I sette prestiti giapponesi del lotto — `katana`, `wakizashi`, `kunai`,
`shuriken`, `nunchaku`, `shakujo`, `tomahawk` — restano invariati e stanno in
`invariati.md`: sono nomi acquisiti, e il verificatore li segnalerebbe come
«traduzione identica all'inglese» se non fossero dichiarati.

## Le teste di famiglia dei nomi di creatura

Fissate col nucleo atomico (2026-08-09). Come per le armi, **si ripresentano
decine di volte con un modificatore**, e cambiarne una dopo significa
ritradurre la famiglia intera. Qui non è solo una questione di coerenza: il
taglio della rinomina cerca la testa in **testa o in coda** al nome, quindi il
modificatore italiano va **dopo** — «il lich maestro», non «il maestro lich».

| EN | IT | note |
|---|---|---|
| orc / ogre | orco / ogre | deciso il 2026-08-09: `ogre` resta invariato, vedi `decisioni.md` |
| imp | folletto | `chaos imp` → «il folletto del caos», `nether imp` → «il folletto dell'oltretomba» |
| putit | putit | prestito Elona, come `putitoro` in `invariati.md` |
| yeek | yeek | idem |
| kobold | coboldo | |
| lich | lich | ⚠️ **non** «semilich» per `demi lich`: perderebbe l'aggancio. «il lich minore» |
| mummy | mummia | `lesser`/`greater` → «minore»/«maggiore», postposti |
| golem | golem | `wooden`/`stone`/`steel` → «di legno», «di pietra», «d'acciaio»; `small` → «minore», postposto |
| slime | melma | `Slimeoid` → «il melmoide» |
| ghost / phantom | spettro / fantasma | l'inglese ha due parole e l'italiano pure: tenerle separate evita «il fantasma» due volte |
| spirit | spirito | `wisp` è a parte: «il fuoco fatuo» |
| ent | ent | prestito tolkieniano già acquisito in italiano |
| wyvern | viverna | la parola araldica italiana |
| dragon | drago | la testa alta della famiglia: `red dragon` → «il drago rosso», `nether dragon` → «il drago dell'oltretomba» |
| drake | draco | fissata col lotto `drake` (2026-08-10). ⚠️ **Non è un sinonimo di `dragon`, è un gradino sotto**: la razza è 亜竜, «sub-drago», e le carte lo dicono di tutti (`viashivan` è «mezza lucertola», `mass monster` è «una sottospecie di drago»). «draco» è italiano vero — il *Draco volans* è «il draco volante» — e la lucertola planante è esattamente l'immagine giusta. ⚠️ **Da qui viene che `action.hsp:17390` non era un refuso**: `Electric Drake` (電気竜, l'evoluzione di 電気羊) è «il draco elettrico», e renderlo «drago» lo farebbe **collidere** con エレキドラゴン, che è già «il drago elettrico» ed è un'altra creatura |
| wyrm | wyrm | fissata col lotto `drake`. L'italiano non ha una parola per il *wyrm* — «verme» direbbe un'altra cosa e «drago» è il gradino sopra — e il fantasy italiano lo lascia così, come `ent` e `lich`. `powerful great wyrm` → «il wyrm possente», `wild wyrm` → «il wyrm selvatico» |
| minotaur | minotauro | |
| centipede / scorpion / spider | millepiedi / scorpione / ragno | |
| king X | X re | postposto per l'aggancio: `king orc` → «l'orco re», `king cobra` → «il cobra reale» dove la lingua lo chiede |
| older / younger sister | sorella maggiore / minore | i nomi di creatura, non la parentela in prosa (vedi sotto) |
| dog / hound | cane / segugio | fissate col nucleo. `X hound` → «il segugio di/del X», sulla forma di `chaos imp` |
| wolf | lupo | `silver wolf` → «il lupo d'argento», materiale come complemento invariabile |
| fox | volpe | 妖狐 `fox spirit` → «la volpe ammaliatrice»: 妖 è l'ammaliare, e «volpe spirito» sarebbe un calco dall'inglese |
| werewolf | lupo mannaro | `werewolf detective` → «il lupo mannaro detective», modificatore postposto |
| Juere / Elea / Zanan / Lothria / Yerles | invariati | nomi di popolo e di nazione del canone Elona. ⚠️ **L'inglese è incoerente e il giapponese no**: scrive `yerles mortar` minuscolo, `Yerles cyborg soldier` maiuscolo, e in due casi la lascia cadere del tutto (`gravity cannon` è イェルス超重力砲, `security system` è イェルス防衛システム). In italiano c'è sempre, perché nel nome c'è sempre. ⚠️ Ma vale anche il contrario: ⚠️ **La razza sta in `dbidn`, non nel nome**: 歴戦の老兵 è «il veterano» e basta, anche se l'inglese lo chiama `zanan old soldier`. Scrivere nel nome un dato che il nome non porta è aggiungere, non tradurre. ⚠️ **ジューア (Juere) non è ジュア (Jure)**: un carattere di differenza fra la nazione e la dea, e le due si somigliano anche in italiano. `juere berserker` → «il berserker di Juere», `instigator of Elea` → «l'istigatore degli Elea» |
| rogue | canaglia **o** banda | ⚠️ l'inglese usa una parola sola per due giapponesi: ならずもの è il teppista da strada → «la canaglia»; 盗賊団 è la **banda organizzata** → «la banda», e i suoi tre ruoli l'inglese li appiattisce su `warrior/archer/wizard` mentre il giapponese dice cosa fanno (用心棒 guardaspalle, 殺し屋 sicario, 術士 stregone) |
| restoroid X | X redivivo | 復元獣 / 復元鳥, le specie estinte riportate in vita. ⚠️ **famiglia a cavallo di tre razze**: il `dire wolf` è in `dog`, il `saber tiger` in `cat`, i quattro uccelli in `bird`. Fissata col lotto `dog`, si applica agli altri quando arrivano |

⚠️ **I dieci segugi elementali li dichiara il sorgente**, non il nome:
`creaturepack = FILTER_RACE_HOUND_<ELEMENTO>` nel blocco di ognuno. È lì che si
legge l'elemento, ed è la ragione per cui `illusion hound` è **il segugio
mentale**: il suo filtro è `HOUND_MIND` e il suo giapponese, 幻惑, è lo stesso
di `Resist Mind` (幻惑攻撃) → «Resiste a mente». L'inglese lo chiama `illusion`
e stacca la creatura dal sistema delle resistenze; il giapponese non lo fa, e
nemmeno l'italiano. Gli altri nove seguono le rese d'elemento di `skill.hsp`:
fuoco, ghiaccio, fulmine, oscurità, nervi, veleno, suono, oltretomba, caos.

⚠️ **L'articolo sta dentro il nome**, per ogni nome che non cominci per `<` o
`"`: `init.hsp:1712-1719` toglie l'articolo solo a quelli. Vale anche per i
nomi capitalizzati — «l'unicorno», «la Nekomata» — perché la maiuscola non
c'entra: il codice guarda `CHARA_BIT_HAS_NAME`, che sta sul personaggio.

## La regola dei nomi propri

Decisa il 2026-08-07 insieme a `Chaos` e ai cinque toponimi aperti, e valida per
ogni nome che arriverà dopo:

- un nome **descrittivo**, fatto di parole comuni, **si traduce** — `Mages Guild`
  → «Gilda dei Maghi», `Fort of Chaos <Beast>` → «Forte del Caos `<Bestia>`»,
  `Cradle of Chaos` → «Culla del Caos», `Chaos Shrine` → «Santuario del Caos»,
  `the Mansion of Younger Sister` → «la Magione della Sorella Minore»;
- un nome **opaco**, inventato, **resta invariato** e va in `invariati.md` —
  `Vernis`, `Derphy`, `Larna`, `Arcbelc`, `Lesimas`;
- un nome **misto** si traduce per la parte comune e conserva quella opaca —
  `Port Kapul` → «Porto Kapul».

È lo stesso criterio con cui Elin ha reso `Blessing of the Abyss` →
«Benedizione dell'Abisso».

### Un nome di creatura opaco resta opaco, ma **prende l'articolo**

Aggiunto col lotto `dog` (2026-08-09). Per gli artefatti l'invarianza era tutto:
`<Mournblade>` esce così com'è. Per una **creatura** no, perché l'articolo sta
dentro il nome e `init.hsp:1712-1719` lo pretende da tutto ciò che non comincia
per `<` o `"`. Quindi la parte opaca resta e l'articolo si aggiunge davanti,
come «il Bearga» già deciso col nucleo:

| EN | IT | perché resta |
|---|---|---|
| `command wolf` | il Command Wolf | コマンドーウルフ, il modello Zoids: nome commerciale, in italiano mai tradotto. Come `<Mauser C96 Custom>` |
| `padangu` | il padangu | ラストパーダンク. **L'inglese romanizza**, cioè nemmeno lui legge il nome come descrizione — e lascia cadere ラスト, che è ambiguo fra *last* e *rust*. Scegliere quale dei due sarebbe inventare, non tradurre. Minuscolo come `putit` e `yeek`, che sono prestiti e non nomi propri |
| `badger` → tanuki | il tanuki mutaforma | 化け狸 è il *bake-danuki* del folklore. Qui l'inglese non abbrevia: **sbaglia animale**, il tasso non è un procionide. Il giapponese arbitra, e «tanuki» è la parola che l'italiano usa per la creatura del folklore |

## Persone e parentela

| EN | IT | note |
|---|---|---|
| older sister / younger sister | sorella maggiore / sorella minore | **solo quando è parentela in prosa**: `How...! You suddenly get a younger sister!` → «Ottieni all'improvviso una sorella minore!» |
| `<Big Sister>` / `<Little Sister>` | invariati | la citazione di BioShock (`Little Sister` + `Big Daddy`), che in italiano non è mai stata tradotta. Restano inglesi anche dentro le frasi che li contengono |
| H Sister | invariato | nome proprio di missione e di creatura (`[Lv. 80] H Sister`) |
| Big Sister Energy / sisterly energy / Sistergy Wave | Onda Sororale | ⭐ 姉波動, deciso nella 39ª col lotto `fase4-proc-025`. **L'inglese lo chiama in tre modi** — «Big Sister Energy» (`proc.hsp:25798`-`:25823`), «sisterly energy» (`chat.hsp:6575`), «Sistergy Wave» (`:6604`) — mentre il giapponese dice sempre 姉波動: si segue il giapponese, con **una** resa sola. «Onda» tiene il 波動 e il registro pseudoscientifico che la battuta vuole; «sororale» è un aggettivo italiano vero. ⚠️ Il grosso della materia sta in `chat.hsp:6575`-`:6676`, che **non ha ancora dizionario**: quando lo si traduce, questa riga è l'ancora. Non è `<Big Sister>` qui sopra, che è la citazione di BioShock |

⚠️ Attenzione: in `action.hsp` le stringhe `Wolf Sister`, `Yandere Sister`,
`Small Older Sister`, `older sister`, `younger sister` **non sono prosa**: sono
`evname`/`evold`, cioè nomi di creatura del sistema di evoluzione. Non si
traducono qui — vedi la sezione «nomi di creatura riscritti nel salvataggio» di
`invariati.md`.

## Termini di `action.hsp`, decisi il 2026-08-10

| EN | IT | note |
|---|---|---|
| praise / authority (発言力) | autorità | ⚠️ **l'inglese usa due parole per un giapponese solo.** `action.hsp:8506` scrive `praise`, ma le altre undici occorrenze di 発言力 — `chat.hsp`, `economy.hsp` — dicono `authority`, e il giapponese arbitra: è il credito che si spende per amministrare una città (`chat.hsp:14047`), non una lode |
| mana charge (魔力の貯蓄) | mana di ricarica | la riserva di `GDATA_ABSORB_CHARGE`. Resa già fissata dall'etichetta di `skill.hsp:977`, «Bacchetta in mana di ricarica»: la prosa la segue invece di inventarne una seconda |
| abyss power | potere abissale | già in tabella sopra; qui in prosa si conta a **punti**: «Servono 5 punti di potere abissale» |
| feat | talento | il talento acquisito di Elona, non una prodezza. `action.hsp:15422` e `:18691` |
| life core (生命核) | nucleo vitale | l'organo che la gravidanza artificiale genera (`action.hsp:8800`) |
| sandbag | sacco da botte | la creatura appesa che serve da bersaglio (`action.hsp:10916`), non un sacco di sabbia |
| showroom | sala d'esposizione | `AREA_SHOW_HOUSE` |
| tag team | coppia | resa già fissata da `skill.hsp:1477` |
| AP | AP | sigla invariata, come `HP` e `MP` |
| mimikaki, potioman, YacaPoint | invariati | prestiti già fissati in `db_item.hsp` |
| `<i primi undici elementi>` | Magia · Fuoco · Gelo · Fulmine · Oscurità · Mente · Veleno · Oltretomba · Suono · Nervi · Caos | l'occhio elementale li **grida** (`action.hsp:9588`-`9628`) e in italiano prendono la maiuscola. I nomi sono quelli di `skill.hsp:70`-`120`, che li scrive minuscoli dentro le frasi: è lo stesso elenco, non un secondo |

⚠️ **Le personalità sono nomi astratti, e la frase deve accettarlo.** `_seikaku()`
(`text.hsp:52`) è già reso con «Allegria», «Prudenza», «Coraggio»…, di generi
misti. La frase che li ospita non può quindi portare articolo: `action.hsp:8851`
dice «*ha scoperto di avere* Allegria», che regge per tutti e trentasei.

⚠️ **Lo stesso vale per le parti del corpo.** `bodyn()` dà «Testa», «Mano»,
«Braccio»: `a new <parte>` non si può rendere con «un nuovo», e la resa scelta è
«**ha una parte nuova:** Mano!», dove i due punti prendono il posto
dell'articolo. Vale per le diciannove righe fra `action.hsp:12530` e `:19012`.

## I nomi di mappa, decisi il 2026-09-02 dal lotto `map_rand-001`

⚠️⚠️⚠️ **Un nome di mappa vive in DODICI caratteri.** `screen.hsp:153` lo taglia
con `strmid(mdatan(MDATAN_NAME), 0, 16 - (maplevel() != "") * 4)`: sedici se la
mappa non mostra il livello, **dodici se lo mostra** — e `maplevel()`
(`text.hsp:2595`) lo mostra per Lesimas, i sotterranei casuali, `AREA_QUEST` e
ogni mappa di tipo dungeon. Non c'è nessun avviso: il nome esce tagliato a metà
parola. Il cancello è `scratchpad/_124-nomi-mappa.py`.

| JP | EN | IT | riga |
|---|---|---|---|
| 街近郊 | Near town | **Periferia** (9) | `map_rand.hsp:784` |
| 地雷原 | Mine area | **Campo minato** (12) | `:787` — ⚠️⚠️ **non è una zona mineraria**: 地雷 è la mina esplosiva, già resa «mina» (`db_item.hsp:144067`), e il codice chiude la questione — l'etichetta è `*map_createDungeonMinefield`, il contatore `GDATA_FLAG_MINEFIELD_QUEST_LEVEL`, e le creature sono `CREATURE_ID_LANDMINE_GIRL` e le sue tre sorelle. Qui la lingua ambigua è l'inglese |
| 街周辺の畑 | Farmland | **Campi** (5) | `:938` |
| パーティー場 | Party Room | **Sala feste** (10) | `:1287` |
| 市街地 | Urban Area | **Zona urbana** (11) | `:1770` — già deciso da `text.hsp:3052` |

⚠️ **Ventuno nomi di mappa già in gioco si tagliano al tetto stretto**, e sono un
fronte aperto: «Fogne di Lumiest» (16) contro «The Sewer» (9), «Fondo di
Lesimas», «Miniera di slime», «Sala dei Seguaci», «Salone piano 15/20/25/30» e
altre. Misurati, **non decisi**: dipende dal tipo di ciascuna mappa.

## Il pannello della produzione, misurato il 2026-09-02

⚠️⚠️ **Sono DUE i pannelli di `material.hsp`, e hanno budget diversi.** La 123ª
misurò quello dei materiali **posseduti** (`*com_material`, font 12); questo è
quello della **produzione** (`*com_product`, `:216`-`:312`), che ha tre colonne
e **due font nella stessa finestra**:

    nome del prodotto     wx+86  -> wx+308   222 px, font 12 (7,7)  ->  28
    «Crea [nome]»         wx+308 -> wx+610   302 px, font 12        ->  39
    «Abilità richiesta: » wx+37  -> wx+610   573 px, font 11 (6,9)  ->  83
    materiali richiesti   passo di colonna,          font 11        ->  vedi sotto

⭐ **La colonna dei materiali richiesti è la più stretta del progetto.** A monte
sono tre da 192 px, cioè 27 caratteri, e dentro ci sta
`nome + " x " + quanti + "(" + posseduti + ")"` — più lungo del « x N» dell'altro
pannello, **sugli stessi nomi**. 27 combinazioni su 113 sforavano. ⭐ **Non si
sono accorciati i tredici nomi** (sono decisi qui sopra e tarati sull'altro
pannello): si è allargata la colonna con una toppa, **due da 288 px**, cioè 41
caratteri.

| termine | resa | dove |
|---|---|---|
| 生産品の選択 / Production | **Produzione** | `material.hsp:219`, il titolo della finestra |
| 生産品 / Product | **Prodotto** | `:221` |
| 説明 / Detail | **Descrizione** | `:222` e `:434` — già `chara.hsp:3469` |
| 詳細 / Requirement | **Requisiti** | `:223` |
| 必要素材 / Material | **Materiali necessari** | `:224` |
| 必要スキル: / Skill needed: | **Abilità richiesta: ** | `:253` — スキル è «abilità» |
| 所持マテリアル / Name | **Nome** | `:433` — «Name» è «Nome» in quattordici rese |
| アイテム[X] / Make [X] | **Crea [X]** | `:298` |
| マテリアル:Xを N個失った / N X was consumed. | **Materiale consumato: X (N)** | `:160` — la gemella di `:120`, che la toppa della 123ª rende «Materiale ricevuto: X (N)». ⚠️ Resta **senza punteggiatura finale**: la chiude `:162`, «, ne restano M. », e `locvar_matgetmain_s` non è mai stampata da sola |

⭐ **I quattro nomi di abilità non si sono decisi qui**: sono quelli di
`skill.hsp` e si copiano — 錬金術 **Alchimia**, 工作 **Falegnameria**, 宝石細工
**Oreficeria**, 裁縫 **Sartoria**. Li conferma `action.hsp:7230`-`:7272`
(«Ottiene bonus in ...»).

## «kitty» non si rende dove il giapponese non lo dice — 2026-09-02

L'inglese di Elona+ fa chiamare il giocatore **«kitty»** da Lulwy anche dove il
giapponese non dice 子猫ちゃん. Il progetto aveva già deciso in tutt'e due i
sensi, e la 124ª ha solo applicato la regola alle tre battute di `etc.hsp`:

- dove il giapponese **lo dice** (`command.hsp:7030`, `text.hsp:12156`,
  `screen.hsp:1417`), la resa è **«gattino»**;
- dove **non lo dice** (`text.hsp:12269`, `:12452`, e ora `etc.hsp:539`, `:548`,
  `:551`), l'italiano **lo toglie**, come già faceva.

⭐ E l'attribuzione delle battute degli dèi ha una forma fissa, presa dai
gemelli di `screen.hsp`: **«Nome verbo: » + `cnvtalk("battuta")`** — «Lulwy
sogghigna: », «Kumiromi si preoccupa: », «Opatos ride: », «Mani avverte: ».

⚠️⚠️ **E il gemello può essere sbagliato.** Cercando la sorella di `etc.hsp:542`
è saltato fuori che `screen.hsp:1450` scriveva **«Larneire»** con una `n` sola,
contro «Larnneire» in dodici rese su dodici. La riga sorella non serve solo a
copiare una resa: serve anche a controllarla.

## I materiali, decisi il 2026-08-15 dal lotto `command-014`

⚠️ **Questi nomi sono di `material_data.hsp`, non di `command.hsp`.** I 59
canonici stanno lì — `matname(MATERIAL_PEBBLE) = lang("石ころ", "Pebble")`,
`:249` e seguenti — e quel file **non ha ancora un dizionario**. In
`command.hsp:6289`-`:6557` gli stessi nomi compaiono **annegati dentro una
frase** (「マテリアル:石ころを…個受け取った。」), che *contiene* 石ころ senza
essergli uguale: né `dossier.py` né la rete 3 li legano. È il caso della 42ª —
un termine deciso in un file che torna a chiedere il conto in un altro — e
questa tabella è la risposta. **Chi aprirà `material_data.hsp` li trova già
decisi.**

I ventisette qui sotto sono quelli che un compagno può consegnare; gli altri
trentadue `matname()` restano da decidere quando quel file si apre.

⭐⭐⭐ **Il file si è aperto nella 123ª, e i trentadue sono decisi**: stanno nella
seconda tabella, sotto la prima. `material_data.hsp` ha ora un dizionario e
tutti e 59 i nomi (più le 59 descrizioni) sono resi.

⚠️⚠️ **E questa tabella ha fatto il suo mestiere.** Le 59 rese erano state
scritte leggendo il giapponese, *prima* di cercarla; tre erano sbagliate —
«sasso» per `Pebble`, «linfa dell'albero del mondo» per `Sap of Yaggdrasil`,
«pietra tagliavento» per `Element fragment`. L'ultima con un ragionamento
corretto e una conclusione sbagliata: il giapponese dice davvero 風切石, ma qui
la coerenza della serie delle cinque schegge batte il giapponese, ed è scritto
qui sotto. **Nessuna rete apre questo file**: leggerlo prima di scrivere è
l'unica cosa che lo fa valere.

⚠️⚠️ **C'è un vincolo di LARGHEZZA che quando questa tabella fu scritta non
c'era ancora.** Il pannello dei materiali (`material.hsp:440`-`470`) ha due
colonne strette e disegna a **font 12**, lo stesso dei menu, quindi vale il
**7,7 px/carattere** di `larghezze.py`:

    nome + « x N»   wx+96  -> wx+308  = 212 px  ->  budget **27** caratteri
    descrizione     wx+308 -> wx+560  = 252 px  ->  budget **32** caratteri

Il cancello è `scratchpad/_123-larghezze-materiali.py`, e conta **cinque** cifre
di contatore perché `mat()` non ha nessun tetto in tutto il sorgente. ⚠️⚠️ **E dalla
124ª c'è un SECONDO budget sugli stessi nomi**: il pannello della *produzione*
li scrive come `nome + " x N(M)"` in una colonna più stretta (vedi la sezione
qui sopra). Accorciare un nome per un pannello lo rompe nell'altro: prima di
toccarne uno si guardano tutt'e due i cancelli. ⓘ Una sola
eccezione **dichiarata**: «macchina generatrice» (20) sfora a cinque cifre, ma è
livello 70 e rarità 7 (`material_data.hsp:228`) e a tre cifre sta dentro.

| EN | IT | riga di `material_data.hsp` |
|---|---|---|
| Pebble | pietruzza | `:249` |
| Fine stone | pietra pregiata | `:269` |
| Ether fragment | scheggia di etere | `:49` |
| Element fragment | **scheggia elementale** | `:119` ⚠️ il giapponese dice 風切石, «pietra che taglia il vento». Qui **la coerenza batte il giapponese** (la formula della 42ª): la costante è `MATERIAL_ELEMENT_FRAGMENT` e nel gioco ci sono altre quattro schegge — etere, mithril, ferro, memoria, magia. È l'unico dei ventisette in cui le due lingue non dicono la stessa cosa |
| Chaos stone | pietra del caos | `:264` |
| Waterdrop | goccia d'acqua | `:34` |
| Hot water | acqua calda | `:134` |
| Snow | neve | `:109` |
| Witch's tear | lacrima di strega | `:64` |
| Angel's tear | lacrima d'angelo | `:59` |
| Stick | bastone | `:39` |
| Branch | ramo | `:239` |
| Holy weed | erba sacra | `:94` |
| Shining weed | erba lucente | `:154` |
| Sap of Yaggdrasil | linfa di Yaggdrasil | `:179` — nome proprio del canone Elona **con la sua storpiatura**: non «Yggdrasil» |
| Human gene | gene umano | `:164` |
| Troll gene | gene di troll | `:104` |
| Rabbit's tail | coda di coniglio | `:99` |
| Witch's eye | occhio di strega | `:169` |
| Fairy dust | polvere di fata | `:114` |
| Cloth | pezza di stoffa | `:234` |
| Paper | carta | `:224` |
| Yelling madman | pazzo urlante | `:199` — è il nome di un **materiale**, non di una persona |
| Magic ink | inchiostro magico | `:189` — ⭐ già deciso da `action.hsp:12351`-`:12355` |
| Magic mass | massa magica | `:159` |
| Generator | macchina generatrice | `:229` |
| Electricity | elettricità | `:124` |

### I trentadue restanti, decisi nella 123ª

| EN | IT | riga di `material_data.hsp` |
|---|---|---|
| Garbage | scarti | `:9` — ⚠️ **non** «cianfrusaglia», che è l'oggetto `junk` (`db_item.hsp:143816`): qui è materia prima da lavorazione |
| Casino chip | fiche da casinò | `:14` — invariabile al plurale, come in italiano |
| Charcoal | carbone | `:19` |
| Driftwood | legno di deriva | `:24` |
| Bird's feather | penna d'uccello | `:29` |
| Mithril fragment | scheggia di mithril | `:44` — `mithril` è invariato (dizionario) |
| Iron fragment | scheggia di ferro | `:54` |
| Seawater | acqua di mare | `:69` |
| Howling weed | erba che geme | `:74` |
| Red weed | erba rossa | `:79` |
| Blue weed | erba azzurra | `:84` |
| Curse weed | erba di maledizione | `:89` — ⚠️ **non** «erba della maledizione» (22): col contatore fa 29 su 27. E non «erba maledetta», che è già la sua descrizione (呪われた草) |
| Black mist | nebbia nera | `:129` |
| Fire stone | pietra di fuoco | `:139` |
| Ice stone | pietra di ghiaccio | `:144` |
| Discharging stone | pietra elettrica | `:149` |
| Leather | cuoio | `:174` |
| Magic paper | carta magica | `:184` |
| Curved stick | bastone storto | `:194` — «bastone» dalla tabella sopra, `:39` |
| Bear's tail | coda d'orso | `:204` — come «coda di coniglio», `:99` |
| 100 Yen coin | moneta da 100 yen | `:209` |
| 500 Yen coin | moneta da 500 yen | `:214` |
| Medicinal weed | erba medicinale | `:219` |
| Thick wood | ramo robusto | `:244` — «ramo» dalla tabella sopra, `:239` |
| Memory fragment | scheggia di memoria | `:254` |
| Magic fragment | scheggia magica | `:259` — ⚠️ **non** «scheggia di forza magica» (24): col contatore fa 31 su 27 |
| Vein | liana | `:274` — ⚠️ **l'inglese sbaglia parola**: ツル è la *vine*, non la *vein*. È un refuso di monte, e il giapponese arbitra |
| Adhesive | colla | `:279` |
| Good paper | carta di qualità | `:284` — «carta» dalla tabella sopra, `:224` |
| Durable cloth | stoffa resistente | `:289` |
| Log | tronco | `:294` |
| White weed | erba bianca | `:299` |

⭐ **Tre delle trentadue sono state accorciate dal cancello di larghezza**, non
scelte così: `erba di maledizione` e `scheggia magica` sforavano il budget dei
27, e la famiglia dei tre minerali si è accorciata **intera** nelle descrizioni
(«Minerale che contiene mithril / etere / ferro») perché sforava solo il
mithril — accorciare solo quello avrebbe reso in due modi tre righe che il
giapponese scrive uguali.

⭐ **E la forma della riga non fa concordare niente col numero.** L'inglese
scrive «You get 3 Pebble.», sgrammaticato anche in inglese; l'italiano non può
scrivere «Ricevi 3 pietruzza» né indovinare il plurale di una variabile. Il
giapponese ha già la soluzione — 「石ころを3個受け取った」, col contatore 個 che
lascia il nome invariato — e in italiano il contatore è la **parentesi**:

> Materiale ricevuto: pietruzza (3).

Il participio cade su «materiale», che un genere ce l'ha suo. Vale per tutte e
ventisette le righe.

## Le sette abilità del risveglio, decise il 2026-08-15 dal lotto `command-018`

⚠️ **Stesso caso dei materiali qui sopra, con un file diverso.** I nomi canonici
li dichiara `chat.hsp:17854`-`:17865` — il menu in cui si spendono gli AP,
`chatList 1, lang("魔力の集積(消費AP600)", "Crystal Spear (600AP)")` — e
`chat.hsp` **non ha ancora un dizionario**. In `command.hsp:2382`-`:2437` gli
stessi nomi compaiono dentro «You got X.», cioè la riga che la scheda dei
talenti stampa quando l'abilità è stata acquisita. Chi aprirà `chat.hsp` li
trova già decisi, col numero di riga accanto.

✅ **Le altre sette della stessa schermata non erano da decidere**: stanno in
`skill.hsp`, che è chiuso al 100%, e si copiano — 罵倒 «Insulto» (`:1052`),
空間歪曲 «Salto dimensionale» (`:968`), 挑発 «Provocazione» (`:1188`), 可変放射
«Soffio variabile» (`:1268`), 零の間撃 «Tiro zero» (`:1276`), チャージ «Carica»
(`:1212`), 悩殺攻撃 «Ammaliamento» (`:1468`).

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 魔力の集積 | `Crystal Spear` | **Accumulo di mana** | `chat.hsp:17854`. ⚠️ Le due lingue di monte dicono cose diverse: il giapponese è «concentrazione del potere magico», l'inglese nomina una lancia di cristallo che il giapponese non nomina. Qui non c'è nessuna famiglia da tenere insieme — la formula della 42ª vale al contrario — quindi decide il giapponese. `Mana` è già invariato in `invariati.md:50` |
| タクティカルヒール | `Tactical Heal` | **Cura tattica** | `chat.hsp:17860`. Il giapponese è il katakana dell'inglese: le due lingue coincidono e resta solo da tradurre |
| タクティカルアタック | `Tactical Attack` | **Attacco tattico** | `chat.hsp:17859` |
| タクティカルアーツ | `Tactical Martial Arts` | **Arti marziali tattiche** | `chat.hsp:17858`. ⚠️ Il giapponese abbrevia in «arts», l'inglese esplicita: l'italiano segue l'inglese, che dice quale arte |
| タクティカルカース | `Tactical Curse` | **Maledizione tattica** | `chat.hsp:17861`. `curse` è «maledizione», non «malocchio»: vedi `hex` più sopra |
| タクティカルスロー | `Tactical Throw` | **Lancio tattico** | `chat.hsp:17863` |
| 範囲魔法可変術式 | `Variable Storm` | **Tempesta variabile** | `chat.hsp:17865`. ⭐ Qui decide la **famiglia**, non la lettera: il giapponese è «formula variabile per magia ad area», ma la gemella 可変放射 è già «Soffio variabile» (`skill.hsp:1268`) e ogni `Storm` del progetto è una «Tempesta» (`skill.hsp:584`, `:759`, `:824`, `:849`, `:1688`). Le due parole che il nome deve portare sono quelle |

## I termini della trama finale, decisi il 2026-08-19 dai lotti `chat-002` e `chat-003`

Le due scene finali del gioco — `*chat_unique_yayauhqui` (`:18474`-`:18560`),
dove Jaldabaoth si rivela, e `*chat_unique_orphe` (`:18562`-`:18600`) — tirano
dentro otto nomi della trama. Tre erano già fissati altrove e si copiano; cinque
erano nuovi.

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 神の間 | `Eternal Seal` | **Sigillo Eterno** | già deciso: `map.hsp:4496`, `main.hsp:4186`, `action.hsp:3008`. Si copia |
| 来光の牙 | `Origin of Light` | **zanna della luce nascente** | già deciso: `main.hsp:5080`, `text.hsp:11633`. Minuscolo, come nei due siti di monte |
| イレギュラー | `Irregular` | **Irregolare** | il nome che i nemici danno al giocatore. Cinque siti, tutti in `chat.hsp` (`:9501`, `:15934`, `:18525`, `:18591`, `:24411`), nessuno tradotto prima d'ora. ⭐ La forma in `-e` non ha genere, e il giocatore non ce l'ha: è l'unico appellativo del gioco che non chiede un adattamento |
| 大戦 | `Great War` | **Grande Guerra** | `chat.hsp:18568`, la guerra che Leold vuole espiare. Nome proprio di un evento, maiuscolo |
| 混沌の超児 | `the Chaos Child` | **il Figlio del Caos** | già deciso: `db_creature.hsp:52175`, `text.hsp:9855`. ⚠️ Dentro una battuta va **nudo**, senza `<>`: vedi la regola qui sotto |
| 忘却の女神 | `Goddess of Oblivion` | **la dea dell'oblio** | `chat.hsp:18535` e altri sei siti (`:9461`, `:9488`, `:9503`, `:10353`, `:15457`, `:18095`), tutti ancora da tradurre. Minuscolo: il giapponese non la nomina, la descrive |
| アーカーシャ | `Arkasha` | **Arkasha** | `chat.hsp:18540`, i corridoi da cui affiora la luce astrale. Nome proprio senza `<>`, e regge la preposizione senza articolo. Anche `:10712` e `:10719`, da tradurre |
| 器 | `vessel` | **involucro** | `chat.hsp:18516` e `:18519`, il corpo di cui Jaldabaoth si serve. La parola torna nella domanda che Tezcatlipoca fa subito dopo, quindi deve essere la stessa nelle due righe |
| 造物主 | `creator` | **Creatore** | `chat.hsp:18536`. ⚠️ Il termine gnostico esatto per Jaldabaoth sarebbe «demiurgo», e il giapponese lo chiama 偽りの造物主, «il falso demiurgo», già nel nome della carta (`db_card.hsp:1648`). Ma nella battuta è lui che si proclama tale, e «Creatore» lo capisce chiunque: la parola dotta perderebbe la minaccia |
| クロやん / ベルっち | `Kuro` / `Bel` | **Kuro** / **Bel** | i soprannomi di Kuroya e Belphat (`chat.hsp:12654`-`:12660`). Si tengono perche' sono il PERNO della scena: a `:12656` Kuroya riconosce l'amico proprio dal modo in cui lo chiama. ⚠️ `screen.hsp:1780` scrive «Kuroya» per intero e resta com'e': li' il soprannome non e' il punto |
| シラハ | `Siraha` / `Shiraha` | **Siraha** | `chat.hsp:8237` e `:8238` scrivono «Shiraha», `db_creature.hsp:88124` e `db_card.hsp:8720` scrivono «Siraha». Vince il posto che il nome lo DEFINISCE — la creatura, non la battuta che la nomina |
| ヒトゴロシくん / カミゴロシくん | `glorious murderer` / `glorious god-killer` | **Ammazzagente** / **Ammazzadei** | come Noel la dinamitarda chiama il giocatore (`chat.hsp:3909`, `:3912`). ⚠️ Composti in *-a*: non hanno genere, e il giocatore non ce l'ha |
| ソックスソードマン | `Sock Swordsman` | **lo Spadaccino dei Calzini** | il nome da eroe che Kuroya si da' quando passa alle maniere forti (`chat.hsp:12731`). Sulla forma di «<Belphat> lo spadaccino cosmico» |
| 名声値 | `fame` | **punti di fama** | il valore numerico, `chat.hsp:5783` e `:5815`. ⚠️ Diverso dall'etichetta «Fama richiesta» delle missioni (`:1366`, `:3876`), che e' una soglia |

### Dentro una battuta il nome va nudo: le `<>` sono del motore, non della lingua

Deciso il 2026-08-19 col lotto `chat-003`, che nomina otto personaggi in
ventidue righe.

La regola è **seguire il monte riga per riga**, e il monte è già coerente:
`db_creature.hsp` scrive `<Jaldabaoth> il Figlio del Caos` perché lì le `<>`
dicono al motore che è un individuo e non una specie (`init.hsp:1713`), mentre
dentro le battute il giapponese scrive ヤルダバオート e l'inglese `Jaldabaoth`,
tutt'e due nudi. Un personaggio che parla non chiama gli altri per etichetta.

⭐ **E la forma nuda risolve da sé il guaio dell'articolo.** `<Il Figlio del
Caos>` non regge una preposizione — «il potere divino di `<Il Figlio del Caos>`»
è «di il Figlio» — ed è il motivo per cui le due rese che esistevano prima
(`text.hsp:9855`, `action.hsp:3008`) lo usano tutt'e due come **complemento
oggetto**. Nudo, diventa «del Figlio del Caos» e la frase si scrive come viene.
⚠️ Quelle due righe restano con le `<>` perché non sono battute: sono il diario
delle missioni e un avviso di sistema. Ma **una delle due non segue il monte**:
`action.hsp:3008` le `<>` ce le ha già in inglese, `text.hsp:9855` no — lì
scrive «the Chaos Child» nudo e a bracchettarlo è stata una nostra scelta, mai
motivata per iscritto. Resta com'è finché qualcuno non guarda quella riga a
schermo: è il diario delle missioni, e non si sa se le `<>` lì aiutino o disturbino.

## I termini di Gaius Vis, decisi il 2026-08-19 dai lotti `chat-004` e `chat-005`

Il filo di Loyter (`chat.hsp:9423`-`:9519`) racconta il mondo gemello distrutto,
e porta cinque nomi che il resto del progetto non aveva mai incontrato.

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 忘却の化身 | `avatar of Oblivion` | **l'incarnazione dell'oblio** | `chat.hsp:9500`, `:9503` (due volte), `:10353`. Sta accanto alla **dea** dell'oblio e le due vanno tenute distinte: la dea è una, le incarnazioni sono quelle che invadono i mondi |
| エルン | `Elun` | **Elun** | `chat.hsp:9499`, la stirpe di fate da cui viene Loyter. Invariato, perché la battuta stessa dice che «di là» il nome si storpiava in «elfi»: se si traduce il primo, la storpiatura non si vede più |
| 《深淵のプロパトル》 | `<Bythos Propater>` | **`<Propator dell'Abisso>`** | `chat.hsp:9423`, sito unico in tutto il sorgente. ⭐ Il giapponese ha già tradotto metà del nome gnostico — *Bythos* è «abisso», e in kanji diventa 深淵 — e ha tenuto *Propator*: l'italiano fa la stessa mossa, con `Abyss` → «Abisso» che era già deciso |
| 因子 | `Decisive Factor` | **Fattore Decisivo** | già deciso in `main.hsp:7083`. In `:9503` il composto 運命変革因子 diventa «fattori di mutamento del destino», che tiene la parola |
| 宇宙人 | `space man` | **extraterrestre** | `chat.hsp:9498`, `:9510`, `:9511`. ⚠️ **Non** «alieno»: エイリアン è un'altra parola e un'altra creatura (`db_creature.hsp:125009`), già resa «l'alieno» |

### ⚠️⚠️ あのお方: l'inglese di monte le dà due generi diversi, e noi nessuno

La divinità trascendente che Loyter nomina di continuo, あのお方, in giapponese è
**senza genere**: お方 è un onorifico, non dice né uomo né donna. L'inglese di
monte sceglie, e sceglie **due volte in modo opposto**:

    :9458  `I wonder if that girl is okay`      femminile
    :9461  `That fine lady ... She must be`     femminile
    :9501  `It was then that "he" appeared`     maschile

Non è un caso limite da decidere a gusto: è monte che si contraddice a novanta
righe di distanza, e chi copia l'inglese eredita la contraddizione.

⭐ La resa è **«quella persona»**, in tutt'e tre i siti. Non è un ripiego: il
sintagma è grammaticalmente femminile, quindi «andiamo a cercar**la**» e «quella
persona è un dio trascendente» stanno in piedi da soli **senza dire niente sul
genere della divinità** — l'accordo cade sul sostantivo italiano, non sul
personaggio. È la stessa mossa delle etichette di stato: si sposta il peso su un
nome e il genere smette di essere una domanda.

### I termini raccolti chiudendo il perimetro (lotti `chat-007` e `chat-008`)

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 廃忘凶獸 | `oblivion rude beast` | **la belva dell'oblio** | già deciso (`db_creature.hsp:47738`). ⚠️ **Non è** 廃忘獸 «bestia dell'oblio»: sono due creature diverse e in italiano restano due parole diverse. `<Nagarew>` è una belva, i branchi che invadono i mondi sono bestie |
| 滅火 | `<HOROBI>` | **`<ESTINZIONE>`** | `chat.hsp:15937`, il colpo che chiude lo scontro, scritto in rosso. L'inglese traslittera; l'italiano traduce, come ha già fatto il progetto col fratello 滅火の神槍 → «`<Lancia divina che spegne il fuoco>`» (`proc.hsp:23846`). ⭐ «Estinzione» porta **tutt'e due** i sensi di 滅火: il fuoco che si spegne e la fine di ciò che esisteva |
| 亡国の王子 | `The Apostle of Chaos` | **il principe del regno perduto** | `chat.hsp:15457`, dentro la profezia. ⚠️ Qui l'inglese **non traduce**: 亡国の王子 è «il principe di un regno caduto» e non nomina nessun caos. Decide il giapponese |
| さいはてのうみ | `The Farthest Sea` | **il mare in capo al mondo** | `chat.hsp:15457`. Tutto in hiragana anche in giapponese: è un titolo evocato, non un toponimo, e l'italiano tiene il giro di parole invece del nome |

## I termini della tecnica di Yerles, coniati il 2026-08-22 dal lotto di Gavela

`chat.hsp:7869`-`:7896` è la spiegazione che il Dr. Gavela fa al giocatore della
tecnologia con cui il Melugast si sposta: otto battute fitte, il pezzo più
tecnico di tutto `chat.hsp`. Il termine si conia **una volta** e poi torna
identico in tutte le altre battute, perché la spiegazione si regge su di lui.

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 次元歪曲航法 | `dimensional navigation` (`Dimensional Navigation` a `:7883`) | **navigazione dimensionale** | il nome che Gavela dà al sistema, e a `:7883` racconta di averlo battezzato lui: là va scritto come un nome, non come una descrizione. Torna a `:7869`, `:7871`, `:7876`, `:7879`, `:7882`, `:7913`, `:7915` |
| 空間歪曲方式 | `spatial distortion system` | **metodo a distorsione spaziale** | uno dei due metodi che la navigazione dimensionale tiene insieme. «Metodo» e non «sistema» perché `:7883` li chiama insieme *航法*, e il sistema è quello |
| 次元扉形成方式 | `dimensional door system` | **metodo a porta dimensionale** | l'altro dei due. La coppia va tenuta parallela: se il primo è «metodo a X», il secondo è «metodo a Y» |
| 転移拠点 | `specific point` / `portable system` | **punto di trasferimento** | l'inglese lo dice in due modi diversi nella stessa battuta (`:7882`); l'italiano ne usa uno solo, perché il giocatore deve capire che è la stessa cosa |
| エーテル波 | `ether waves` | **onde d'etere** | distinto dal **vento d'etere** (`Etherwind`, già deciso a `chat.hsp:7682`): il vento è il fenomeno del mondo, le onde sono quel che rompe l'equilibrio spaziale |
| 量産型 | `mass-produced` | **modello di serie** | già in `action.hsp:17242`, «il Melugast di serie»: si copia |
| 試作型 | `test model` / `prototype` | **prototipo** | l'inglese oscilla, l'italiano no |
| 空間固定 | `spatial binding` | **fissaggio spaziale** | l'attacco che immobilizza i Melugast (`:7869`, `:7913`) |
| 空間干渉 | `spatial intervention` | **interferenza spaziale** | già in `map.hsp:14918`, «L'interferenza spaziale del demonio è cominciata»: si copia |

⚠️ **E i luoghi di Gavela non si coniano: si copiano da `text.hsp`**, che porta
i nomi come escono sulla mappa — `Machinery Fort` → **Fortezza Meccanica**
(`:3009`), `Chaos Shrine` → **Tempio Caos** (`:3012`), `Valley of Hades` →
**Valle degli Inferi** (`:3006`). ⚠️ Il glossario aveva deciso «Santuario del
Caos» per `Chaos Shrine` il 2026-08-07, ma il nome che il giocatore legge sulla
mappa è «Tempio Caos», e in una voce di menu che dice «Parlami di...» deve
esserci quello: **mandare il giocatore a cercare a schermo un nome che non
esiste è il difetto del tutorial**, alla seconda ripetizione.

## I quattro corsi del seminario, decisi il 2026-08-23 dai lotti dei conferenzieri

`chat.hsp:13950`-`:14524` sono quattro docenti che spiegano al giocatore le
meccaniche del gioco, e **si nominano fra loro**: Ajetalio manda al corso di
crescita e a quello sugli oggetti (`:14084`, `:14086`), Mito consiglia di
sentire prima gli altri (`:14386`). I quattro nomi si decidono insieme o non
si decidono affatto.

| giapponese | inglese | italiano | chi lo tiene |
|---|---|---|---|
| 生活講座 | `daily life course` | **corso di vita quotidiana** | `<Ajetalio> il docente`, «Ajira» |
| 道具講座 | `item course` / `item instructor` | **corso sugli oggetti** | `<Cresce> la docente` |
| 育成講座 | `training lecture` | **corso di crescita** | `<Iduru> il docente`, «maestro» |
| 戦闘講座 | `combat course` | **corso di combattimento** | `<Mito> la docente`, «Mitorin» |

⚠️ **I soprannomi non li porta l'inglese, li porta il giapponese**, e servono
perche' gli studenti li usano nelle voci di menu. Per Iduru sono la battuta:
gli volevano dire «いづるん», lui ha preteso 師範 — **«Idurino»** contro
**«maestro»** — e a `:14293` uno studente lo chiama Idurino lo stesso.

⭐ **La parola nuova del lotto e' una sola**, perche' tutto il resto stava gia'
in dizionario:

| giapponese | inglese | italiano | perche' |
|---|---|---|---|
| 交易品 | `cargo` | **merci da commercio** | non erano in nessun file: il `(荷車)` che le marca non entra nel nome dell'oggetto (`db_item.hsp:148280`, «cibo da viaggio»). «Merce» e non «carico» perche' il carretto e' il contenitore e ha gia' il suo nome (`command.hsp:14176`, «Carretto») |

⚠️⚠️ **E due parole che l'italiano deve tenere separate dove l'inglese lo fa e
il dizionario no.** スキル e 技能 sono tutt'e due «Skill» in inglese e tutt'e
due «Abilita'» in italiano (`module.hsp:5153`, `help.hsp:29`), ma il tutorial
le spiega **una contro l'altra**: le prime si imparano dagli istruttori, le
seconde salendo di livello. Quindi **abilita'** per スキル — che e' il nome
della linguetta — e **capacita'** per 技能, con «capacita' ad area» per
広域技能, la forma che sta gia' in `command.hsp:5673`.

⭐⭐ **Il resto del lessico non si e' deciso: si e' copiato dallo schermo**, ed
e' la regola del tutorial. Le sei classi dell'equipaggiamento vengono da
`_quality` (`text.hsp:106`) e **non** dall'inglese della battuta, che dice
«bad, normal, great, miracle, godly, unique» dove il pannello dice *scadente,
comune, eccellente, eccezionale, celestiale, speciale*. I quattro pesi dello
zaino vengono da `_burden` (`text.hsp:66`): *Fardello, Fardello!, Sovraccarico,
Sovraccarico!*. La resistenza «Superb» dell'inglese di `:14458` e' **Ottima**
(`text.hsp:107`). Le posizioni dei compagni sono **Assalto** e
**Intercettazione** (`text.hsp:2457`, `:2463`).

⚠️⚠️⚠️ **E le sette etichette del potenziale restano INGLESI, perche' a schermo
sono inglesi.** `command.hsp:10676`-`:10700` le stampa come letterali nudi
— `mes "Supreme"`, `"Amazing"`, `"Superb"`, `"Great"`, `"Good"`, `"Bad"`,
`"Hopeless"` — senza `lang()`, quindi nessun dizionario le raggiunge. Il
tutorial di Iduru le nomina, e le nomina come le legge il giocatore. 💡 *La
regola non e' «traduci tutto»: e' «di' quel che c'e' scritto sullo schermo».*
Il giorno in cui quelle righe si toppano, `chat.hsp:14246` va rifatta.

## La bottega di Irma e il servizio di Maile, decisi il 2026-08-23 dai lotti della 88a

| EN | IT | perché |
|---|---|---|
| dagger | pugnale | `db_item.hsp:152794`, e il diario della missione lo usa già (`text.hsp:11436`) |
| core of nefia | nucleo di Nefia | `db_item.hsp:138961` |
| scroll of gain attribute | pergamena di acquisizione di attributi | `db_item.hsp:149507`-`:149508` |
| evolution item / EVitem | oggetto evolutivo | `blend.hsp:1124` |
| static artifact | artefatto unico | 固定アーティファクト, `text.hsp:2151` |
| miracle-level / godly-level artifact | artefatto eccezionale / celestiale | la scala di `_quality`, `text.hsp:106` |
| the Void | il Vuoto | `text.hsp:2773` (すくつ) |
| shopkeeper feats | talenti da negoziante | `feat` era già *talento* (`command.hsp:2143`) |

⭐⭐ **Nessuno di questi è stato deciso: sono stati tutti cercati**, e due
sono arrivati da un posto che non è il dizionario dei nomi — il **diario del
giocatore**. `text.hsp:11436` diceva già «mostrare un suo **pugnale** a
<Dain>, l'anziano della collina» e `:11618` chiama l'oggetto «[pugnale di
Irma]»: le battute del lotto dovevano usare quelle parole, non sceglierne di
proprie. 💡 *Il diario è un vincolo, non una fonte* (79ª), e qui il vincolo ha
fissato tre nomi su tre.

⚠️⚠️ **La riga d'errore di sistema è un modello, non una frase.** MAILE
cancella i ricordi con **trentaquattro finte righe di diagnostica**, e la loro
forma sta già in build a `proc.hsp:26301`:

    [Sistema]Errore di origine ignota in <NOME>: valore reinizializzato.

I **nomi delle variabili non si traducono** — `GDATA_DEEPEST_LEVEL`,
`CHARA_BIT_MARRIED`, `INV_ITEM_GROWTH` e gli altri restano in inglese. Non sono
lessico: sono l'oggetto della finta diagnostica, ed è quello che li rende
spaventosi.

⚠️ **E il modello è identico a se stesso trentaquattro volte per scelta.** Il
giapponese di monte usa tre verbi diversi (初期化 / 再計算 / 削除) dove
l'inglese ne usa uno solo: si segue l'inglese, perché una macchina che si
ripete è credibile e una che varia formula non lo è. È l'unico posto del
progetto dove **la ripetizione è un valore da difendere**.

⚠️⚠️⚠️ **E un promemoria che è costato tre correzioni**: i nomi degli stati
stavano già in questo glossario — *Fardello*, *Sovraccarico* dal `_burden` di
`text.hsp:66`, scritti dalla 87ª — e la 87ª stessa ha poi reso «while
burdened» con «sei **sotto peso**», che in italiano dice il contrario. Un
termine messo in glossario non si applica da solo: `chat.hsp:14113`, `:14435`
(*Cecità*, *Confusione*, `text.hsp:96` e `:99`) e `:16586` sono stati rifatti
dal referto della 88ª.

## La collina di Dain e i Cavalieri Dorati, decisi il 2026-08-23 dai lotti della 89a

| EN | IT | perché |
|---|---|---|
| arms craftsman / arms store | armaiolo, armaiola / bottega d'armi | 武具職人. «fabbro» era già speso per 職人, i fabbri leggendari Garok e Miral (`db_creature.hsp:118328`), e il diario chiama il mestiere «forgiare le armi» (`text.hsp:11439`): «armaiolo» nomina esattamente chi fa armi e armature |
| successor | erede | 後継者. A `chat.hsp:11070` a dirlo è **il giocatore** e a `:11079` Dain lo ripete di lui: «successore» in italiano non ha femminile, «erede» non ha genere |
| my precious / treasured friend | anima gemella | 心の友, tre volte in bocca a Thalia (`:11130`, `:11170`, `:11171`) ed è un **vocativo al giocatore**: l'accordo cade sul nome femminile, non su chi ascolta |
| the Golden Knights | i Cavalieri Dorati | 黄金騎士団. Non è una scelta: 黄金の騎士 è già «il cavaliere dorato» in `db_creature.hsp`, `db_card.hsp` e `action.hsp:16890` — l'ordine prende il nome della creatura di cui è fatto |
| Procurement Officer | responsabile dei rifornimenti | 備品調達係. Vocativo al giocatore a `:12338` e `:12431`, titolo che gli viene dato a `:12473`: «addetto» si accorderebbe tutt'e tre le volte, «responsabile» è invariabile |
| the old man (in bocca a Thalia) | il vecchiaccio | ジジイ. Non deciso: **letto** in `db_creature.hsp:74088`, dove la sua battuta era già resa «Quel vecchiaccio...». Il nome neutro di Dain resta «l'anziano della collina» |
| smelting furnace | forno fusorio | `db_item.hsp:151275`, il nome dell'oggetto |
| workshop | officina | `text.hsp:2962`, il **nome sulla mappa**: «Officina Nascosta di Irma e Thalia» |
| socks | calzini | `db_item.hsp:134939` e il diario `text.hsp:11209` |
| craft repair kit / material kit | kit di riparazione / kit di materiali | il diario `text.hsp:11239`, `db_item.hsp:144134` |
| Fuhaha (Urcaguary) | Fuahaha | `db_creature.hsp:71913`, già scritto nel suo repertorio |

⭐⭐ **Quattro voci su sei della prima metà esistono per il divieto di genere,
non per il senso.** «erede», «anima gemella», «responsabile» e il giro di
`:12473` sono tutte scelte fatte perché la parola naturale — successore, amico,
addetto — si accorderebbe con **il giocatore**, che di genere non ne ha. Sono
le tre scappatoie della 85ª e della 86ª (nome comune femminile, imperativo,
relativo `chi`) più una quarta che qui torna utile: **l'aggettivo in `-e`**,
che al singolare non si accorda.

⭐⭐ **E le altre non sono state decise: sono state cercate.** «vecchiaccio»
stava nel repertorio della creatura, «officina» nel nome della mappa, «forno
fusorio» e «calzini» nei nomi degli oggetti, «kit di riparazione» e «punire» e
«Ol-dran» nel diario del giocatore, «il ladro di calzini» e «campi di neve»
nell'altra metà della stessa missione già resa (`chat.hsp:12713`-`:12728`),
«Fuahaha» perfino la risata. 💡 *Di undici termini, sette erano già scritti da
qualche parte e nessuno di quei posti era il glossario.*

⚠️⚠️ **E i Cavalieri Dorati sono la regola del DATO (79ª) applicata a un nome
proprio**: la domanda giusta non era «come si dice Golden Knights» ma «di che
cosa è fatto quest'ordine» — di 黄金の騎士, che una `grep` sul nome della
creatura dà già tradotto in tre file.

## I cinque parlanti di Ol-dran e del nord, decisi il 2026-08-23 dai lotti della 90ª

Cinque lotti, **174 rese**, e in tutto **otto** termini nuovi. Non è poco
lavoro con poche decisioni: è che il lessico stava già scritto altrove, e la
sessione l'ha cercato invece di coniarlo — vedi il riquadro in fondo.

| JP | EN | IT | perché |
|---|---|---|---|
| 限定コンサート | limited-time concert | **il concerto esclusivo** | Il diario lo chiama solo «un concerto a fine mese» (`text.hsp:11368`), quindi la parola per 限定 mancava. «A tempo limitato» è burocratico; «esclusivo» è come un'idol vende una data sola |
| ヤカ姐 | big sis Yacatect | **sorellona Yacatect** | 姐 è la sorella maggiore di strada, non di sangue. Nome per esteso perché a `chat.hsp:12282` non c'è contesto che lo disambigui, e l'inglese fa la stessa scelta |
| 残機 | remaining lives | **vite in più** | Non c'era in nessun dizionario. «Vite extra» è il calco da sala giochi; il progetto scrive già «Punti bonus in più» per la stessa idea (`chara.hsp:4305`) |
| 貴重品 | valuable items | **oggetti preziosi** | Non è una categoria con un nome fisso: i cinque siti del sorgente lo dicono ogni volta a modo loro, e `chara.hsp:4271` l'aveva già reso «quel che hanno di prezioso» |
| 努力賞 | Effort Award | **premio di consolazione** | Il giapponese è un premio d'incoraggiamento, e il 「一応、ね」 che segue lo svuota: la parola italiana che porta già quella presa in giro è «consolazione» |
| 犬ぞり | dogsled | **slitta trainata dai cani** | |
| クレバス | crevasse | **crepaccio** | |
| カマクラ | snow hut | **capanne di neve** | Le tre parole di neve mancavano perché Mayroon non era ancora stata scritta |
| 館長 | chief librarian | **il direttore della biblioteca** | Né 館長 né «librarian» comparivano da nessuna parte |
| ゴッドロイヤルゼリー | godly royal jelly | **pappa reale divina** | |
| 森の王様 | king of the forest | **il re della foresta** | |

⭐⭐⭐ **Il resto — e il resto è la maggioranza — è stato cercato, non deciso.**
Di BYSYMLHA **dieci termini su undici** erano già scritti, e **nove venivano
dalla stessa pagina**: `chara.hsp:4225`-`:4314`, la descrizione delle modalità
di gioco, che è il testo che spiega proprio quel menu — «3x», «30x»,
«Overdose», «Purge», «esperienza», «potenziale», «attributi». La riga `:4231`
dice «Di base è 3x, e in un certo posto si arriva fino a 30x», e quel «certo
posto» **è lei**.

Stessa forma per MELGET, le cui dodici curiosità del mese nominano una per una
cose che hanno già un nome: «il gufo spaziale», «penna d'oca lucente»,
«<Gigante Castagna>», «riccio» (la battuta degli alchimisti, già gridata in
`action.hsp:125`), «calzini», «<Fron> l'organizzatrice di viaggi», «una certa
cacciatrice di draghi» (Spipha), «Zanan», «Sigillo Eterno», «Lothria»,
«(10000 oro)», «Arrivederci». **Sedici termini già decisi, nessuno nel
glossario.**

💡 *Prima di decidere una parola si cerca il testo che descrive la stessa cosa
da un'altra angolazione — il nome della creatura, il nome dell'oggetto, il
diario, la pagina d'aiuto. Il glossario è l'ultimo posto dove guardare, non il
primo.*

⚠️⚠️ **E due parole non si scrivono, per il carattere e non per il senso:**
«dèi» (la degradazione CP932 mette l'apostrofo *dentro* la parola, «de'i») e
l'ordinale femminile «ª». In tutt'e due i casi la riparazione è **cambiare
parola**, non togliere l'accento: `chat.hsp:13152` chiude con «Che paura fa, un
dio», e `chat.hsp:12275` conta in avanti («Con questa fanno N strette di mano»)
invece di usare l'ordinale.

## Gli otto parlanti della 91ª, decisi il 2026-08-24

Otto lotti, 153 rese, e **tredici** parole nuove: il resto del lessico era già
scritto altrove. Come nella 90ª, la fonte non è stata il glossario ma **il
testo che descrive la stessa cosa da un'altra angolazione** — e stavolta, per
tre lotti su otto, quel testo è **il diario della missione**.

| JP | EN | IT | dove |
|---|---|---|---|
| ベルム家 | Bellum family / House Bellum | **casa Bellum** | il nome NON viene dalla riga che lo dice (`chat.hsp:10477`) ma da `scene2.hsp:3204` e `db_item.hsp:51432`, dove l'inglese lo scrive per esteso |
| 魔力電池 | mana battery | **batteria di mana** | regge il confronto con «monolito di mana», che è la stessa cosa dall'altra parte |
| 魔術研 | (fuso col palazzo) | **l'istituto di magia** | abbreviazione di 魔術研究所; l'inglese perde il secondo ente |
| 王宮魔導士長 | Archmage | **capo degli incantatori di corte** | costruito su «l'incantatore di corte», `db_creature.hsp:67065` |
| 転写魔法 | copying magic | **magia di trascrizione** | |
| 生態系 | ecosystem | **ecosistema** | la sola riga in cui Allen parla da ricercatore |
| ネクロマンサー | Necromancer | **il negromante** | nel progetto non c'era: unica occorrenza `db_card.hsp:5035`, da tradurre |
| 超生命 | (l'inglese lo perde) | **creature superiori** | `chat.hsp:14969` |
| 電子ウイルス | electronic virus | **virus elettronico** | sul modello di «serratura elettronica», `map.hsp:815` |
| 電子頭脳 | electronic brain | **cervello elettronico** | stesso modello |
| 熱暴走 | overheating | **surriscaldarsi fuori controllo** | è la stessa 暴走 dell'«impazzimento» delle macchine, ma qui il soggetto è il calore |
| 機械生命体 | mechanical lifeform | **forma di vita meccanica** | |
| 独房 | cell | **cella** | le due celle numerate (14 e 16) sono il cuore del blocco di Regulus |
| 素体 | \"ingredient\" | **materiale di partenza** | è il termine da laboratorio con cui l'istituto chiama gli uomini che usa, e la riga vive di quel gelo |
| 廃棄処理区画 | disposal area | **settore di smaltimento** | costruito su «settore», che viene dal diario di Garziem |
| 資源回収部隊 | Resource Recovery Division | **squadra di recupero risorse** | |
| アクセス端末 | access terminal | **terminale di accesso** | |
| 菌 (il Meshera visto da dentro) | bacteria | **il fungo** | l'inglese dice «bacteria», ma il Meshera nel gioco non è un batterio |

⭐ **Quello che NON è stato deciso qui, perché era già scritto — e quasi tutto
nel diario delle missioni:**

- **Nein**: «il monolito di mana» (`db_creature.hsp:65463`), «la Nave Magica»
  e ⭐ «forma di vita artificiale con circuiti magici incisi addosso»
  (`text.hsp:11157`), «Lettura» (`skill.hsp:192`), «cerchio magico»,
  «artefatto», «grimorio»;
- **Allen**: ⭐ «il gruppo (di ricerca)» e «Raskilis» (`text.hsp:11554`), «le
  bestie nere» (`chat.hsp:15440`, la donna all'imbocco della valle, **nella
  stessa missione**), «il vento d'etere», «il bar»;
- **Ssil**: ⭐ «un mazzo», «tipi di carte», «la Dimora della Strega»
  (`text.hsp:11097`), «Ihihi...» (`screen.hsp:1774`), «<Quruiza>
  l'ingannatrice dall'occhio finto», «la civiltà biochimica», «Sierre Terre»,
  «Rehm-Ido»;
- **Garziem**: ⭐ «la Nave Divina», «le macchine da lavoro», «il settore»,
  «l'impazzimento», «infiltrarsi» (tutti in `text.hsp:11305`-`:11336`), e
  «controllo approfondito» da `chat.hsp:22776`, che è **la stessa storia vista
  dalla parte delle macchine**;
- **Jin**: ⭐ «la Nave Messe» (`text.hsp:2953`), «le creature spaziali», «la
  Torre del Miraggio», e **«il mare di stelle lontano»**, che è il titolo della
  missione (`text.hsp:11165`);
- **Regulus**: «Regulus» (mai エユル), «<Renai> la calamità repressa», ⭐ «il
  Meshera» **maschile e invariabile**, «gas nervino», «diario del ricercatore»,
  «il valico»;
- **L'anima smarrita**: «l'anima smarrita» (`db_creature.hsp:44807`), «Gabbia
  di Amur», «<Amurdad>».

💡 *Tre lotti su otto avevano il lessico principale nel **diario della
missione**, che è il testo che il giocatore ha aperto mentre parla col
personaggio. Non è una fonte come un'altra: è l'unica che il giocatore legge
appaiata alla battuta, quindi una parola diversa lì si vede subito.*

⚠️ **E una parola già decisa è stata scartata apposta:** 「クソガキ」 era
«moccioso» (`chat.hsp:804`), ma il bambino dell'anima smarrita ha `CDATA_SEX`
**tirato a sorte** (`db_creature.hsp:44851` cambia il ritratto di conseguenza),
quindi «moccioso» sarebbe sbagliato una volta su due. Si dice **«peste»**, che
vale per tutti e due i sessi e tiene la stessa villania. Il glossario non è
stato cambiato: la parola resta «moccioso» dove il bersaglio ha un sesso noto.

## I sei parlanti della 92ª, decisi il 2026-08-24

Sei lotti, 132 rese, e la sorpresa è che **quasi tutte le parole nuove sono
nomi che esistevano già fuori dal gioco**: due elenchi — i ventotto eoni di
Mikraanesis e il diario di viaggio di Belphat — non chiedevano di essere
tradotti ma **riconosciuti**, e l'inglese li aveva traslitterati a orecchio.

| JP | EN | IT | dove |
|---|---|---|---|
| 交合のミクシス | Mixsis of Mixing | **Mixis dell'Unione** | `chat.hsp:9409`. Gli eoni **valentiniani**: il gioco ne usa già quattro nella trama (Sophia, il Propator dell'Abisso, Enthumesis), quindi l'elenco è il suo pleroma e i nomi si scrivono nella forma greca |
| 相互混合のシュンクラーシス | Shunkraasis | **Syncrasis della Mescolanza** | `:9409` |
| 統合のシュネシス | Shunesis | **Synesis dell'Integrazione** | `:9409` |
| 思念のエンノイア · 理法のヌース · 真理のアレーテイア | Ennoia · **Nuus** · **Areteia** | **Ennoia del Pensiero · Nous della Ragione · Aletheia della Verità** | `:9410` |
| 言葉のロゴス · 生命のゾーエー · 人間のアントローポス · 教会のエクレーシア | Logos · **Zoea** · Anthropos · Ecclesia | **Logos della Parola · Zoe della Vita · Anthropos dell'Uomo · Ecclesia della Chiesa** | `:9410` |
| 深みのビュテイオス · 不壊のアゲーラトス · 配慮のヘンノーシス | **Buteios** · Ageratos · Henosis | **Bythios della Profondità · Ageratos dell'Indistruttibile · Henosis della Premura** | `:9411` |
| 成長のアウトピュエース · 快楽のヘードネー · 不動のアキネートス | **Outpuece** · **Hedonay** · **Aquinatos** | **Autophyes della Crescita · Hedone del Piacere · Akinetos dell'Immobilità** | `:9411` |
| 独り子のモノゲーネス · 浄福のマカリア | Monogenes **of Solitude** · **Macalia** | **Monogenes dell'Unigenito · Macaria della Beatitudine** | `:9411`. ⚠️ 独り子 è *figlio unico*: l'inglese cambia il significato, non solo la grafia |
| 仲介のパラクレートス · 信仰のピスティス · 父性のパトリコス · 希望のエルピス | Paracleteos · Pistis · Patrikos · Elpis | **Parakletos della Mediazione · Pistis della Fede · Patrikos della Paternità · Elpis della Speranza** | `:9412` |
| 母性のメートリコス · 愛のアガペー · 永遠のアエイヌース | **Maitrikos** · Agape · **Aeneus** | **Metrikos della Maternità · Agape dell'Amore · Aeinous dell'Eternità** | `:9412` |
| 伝道のエクレーシアスティコス · 幸福のマカリオーテス · 意欲のテレートス | Ecclesiasticus · Macarios · Terethos | **Ecclesiasticus della Predicazione · Makariotes della Felicità · Theletos della Volontà** | `:9412` |
| ユゴス | **Yugos** | **Yuggoth** | `chat.hsp:12576`. Il pianeta di Lovecraft. Il progetto usa già le forme italiane del Ciclo: «lo shoggoth», «la Grande Razza di Yith» |
| バイアクヘー | **Bayakhae** | **Byakhee** | `:12579` |
| サイクラノーシュ | **Cyclanorch** | **Cykranosh** | `:12582`. Il Saturno di Clark Ashton Smith |
| ミ=ゴ | Mi-Go | **Mi-Go** | `:12576`. L'unico che l'inglese azzecca |
| イス焼き | **fried ice cream** | **frittelle di Yith** | `:12591`. ⚠️ L'inglese ha letto イス come *ice*: è **Yith**, e lo dicono `db_card.hsp:14390` e `action.hsp:2604`. Sta in coppia con たこやき → «frittelle di polpo»: la battuta è la sostituzione dell'ingrediente, quindi le due voci hanno la stessa forma |
| 宇宙剣術 | space sword techniques | **la scherma cosmica** | `:12565`, sotto «lo spadaccino cosmico» già deciso |
| 始まりの丘・ルストール | the hill of beginnings, Lustor | **la collina delle origini, Lustor** | `chat.hsp:13645`, la leggenda degli abitanti della collina |
| ツアーコンダクター | tour guide | **la guida turistica** | `chat.hsp:13588`. Compare **una volta sola** in tutto il sorgente e non è il titolo né di «<Arma> la guida turistica» né di «<Fron> l'organizzatrice di viaggi»: il giapponese non dice chi, e l'italiano nemmeno — mestiere, non nome, e in italiano vale per chiunque lo faccia |
| 努力賞 | reward for your efforts | **premio per l'impegno** | `chat.hsp:14530`. ⚠️ **Non** il «premio di consolazione» di `:13082`: lì è il contentino di chi non ha vinto, qui è il premio di chi ha finito tutti e sedici i pezzi del seminario |
| 四次元ポケット | 4-Dimensional Pocket | **tasca quadridimensionale** | `chat.hsp:13779` |
| 廃人 | crippled | **rovinato per sempre** | `chat.hsp:13250`, e il definitivo del giapponese si tiene |

⭐ **Quello che NON è stato deciso qui, perché era già scritto.** Sei lotti su
sei hanno trovato il lessico in righe già rese, e tre volte è stata quella
consultazione a scoprire un difetto: «<Amurdad>» e la Gabbia di Amur
(`text.hsp:2929`, `:11274`), «l'anima smarrita» (`db_creature.hsp:44807`), i
quattro corsi del seminario e i loro docenti (87ª), «Kikkasu» e «il demone
della pestilenza» (`chat.hsp:2111`, `:2140`-`:2141`), «<Bethel> il falco
bianco» e «Larnneire», «<Kuroya> lo scrutatore del cosmo» e il suo soprannome
«Kuro» (`chat.hsp:12657`), «Irva Perduta», «gli abitanti della collina»,
«armi non morte», «calzini», «statuetta», «mortale», «luce astrale», «Arkasha».

⚠️ **E una parola che il glossario NON cambia:** 定命 resta «mortale» — l'inglese
di `chat.hsp:10706` scrive «destined one», leggendo 定命 come *destino*, ma nel
progetto è «mortale» in cinque punti ed è il contrario di «predestinato».

## Gli otto parlanti della 93a, decisi il 2026-08-24

Otto lotti, 87 rese, e la sorpresa e' il rovescio di quella della 92a: qui
**quasi nessuna parola nuova andava decisa**, perche' cinque lotti su otto
avevano il registro e il lessico gia' scritti da un'altra parte. Le voci qui
sotto sono le poche che non c'erano.

| JP | EN | IT | dove |
|---|---|---|---|
| 次元アンカー | dimensional anchor | **ancora dimensionale** | `chat.hsp:13186`, `:13201`. Sotto «navigazione dimensionale» (`:7876`) e «distorsione spaziale» (`:7883`), gia' decise |
| 次元歪曲ユニット | dimensional distortion unit | **unita' a distorsione dimensionale** | `chat.hsp:13201` |
| 自律戦闘通信機の特殊電波システム | special radio system for autonomous combat communications | **sistema radio speciale del ricetrasmettitore autonomo** | `:13201` |
| 生体ハードポイント理論 | — | **teoria dei punti d'aggancio biologici** | `:13201`. L'inglese lo rende ma senza nome fisso |
| A0-I | A0-I | **AO-I** | `chat.hsp:13191`. ⚠️ **Refuso di monte**: lo zero compare in un sito solo, contro sei che scrivono AO-I con la lettera O (`:7821`, `:7830`, `:7833`, `:7861`, `db_card.hsp:2701`, `db_creature.hsp:52005`, piu' l'identificativo `MELUGAST_AO_I`). Si conta, non si ricopia |
| 災厄クラス | Calamity class | **classe calamita'** | `chat.hsp:9781`, sotto «calamita'» gia' in uso (`db_card.hsp:9227`) |
| 火の鳥 | phoenixes | **uccelli di fuoco** | `chat.hsp:9753`. ⚠️ Compare **una volta sola** in tutto il sorgente e **non e' un identificativo di creatura**: non si va a cercare la fenice, che l'inglese tira dentro e che nel gioco non c'e' |
| 不幸度 | misfortune | **sfortuna** | `chat.hsp:10879` (gia' reso), `:10886`. E' 100 meno la Fortuna |
| ニャ (particella finale) | meow | **«, miao» in coda alla frase** | `chat.hsp:10881`-`:10905`. ⚠️ **Non deciso qui**: `db_creature.hsp:44182`, `:54053`, `:56489` l'avevano gia' fissato. Dove il giapponese allunga (ニャア) si allunga anche l'italiano, «miaao», come `:56471` |
| ごろごろ (del gatto) | laze | **le fusa** | `chat.hsp:10881`. L'inglese lo legge come «pigrizia»: e' l'onomatopea delle fusa, cioe' quel che il giocatore sta interrompendo |
| 亀助け | a favor for this old tortoise | **aiutare il prossimo... cioe', una tartaruga** | `chat.hsp:8741`. Storpiatura di 人助け: il senso sta nella **sostituzione**, e in italiano l'espressione fissa esiste e si storpia uguale |
| 第一陣・第二陣 | — | **il primo e il secondo squadrone** | `chat.hsp:15107`, le ondate di sicari che l'inglese cancella |
| ボス猫女神 | empress cat god | **dea gatta capobanda** | `chat.hsp:10785`. 女神 e' **dea**: in Elona la dea gatta e' Ehekatl, e Arasiel promette di punirla |
| ルルウィお姉さま | Miss Lulwy | **sorella Lulwy** | `chat.hsp:10776`, `:10782`. Gia' cosi' in `db_creature.hsp:75097` |
| 逆境上等・覚悟は上々 | This is bad! Prepare yourself! | **Le avversita'? Ben vengano! La determinazione? Al massimo!** | `chat.hsp:9986`. ⚠️ Sono **due vanti**, e l'inglese li legge tutt'e due come paura |
| 拳で語り合う | Father speaks through his fists | **parlarsi a suon di pugni** | `chat.hsp:9986`, `:10001`. E' **reciproco** |
| 管理不行届き | incompetence at taking care of | **custodia negligente** | `chat.hsp:9996`. Lingua da verbale applicata a una formica gigante: la comicita' sta nell'attrito |
| 畳みかける | Interrogate him! | **non dargli tregua** | `chat.hsp:13192`. E' un ordine d'attacco, non un interrogatorio |

⭐ **Quello che NON e' stato deciso qui, perche' era gia' scritto.** «Irva
Perduta» (`text.hsp:2917`), «Tyris del Nord» (`chat.hsp:9519`), «Santuario
Centrale» (`text.hsp:2941`), «gli dei» senza accento, «<Leiki> la tartaruga
nera», «<Alice> la formica gigante», «<Aribel> la monella», «<Alsapia> la
maschera bianca», «<Spipha> la cacciatrice di draghi», «onde mentali»
(`chat.hsp:8537`), «mezzo drago» (`screen.hsp:1738`), «cannone a supergravita'
di Yerles», «il demone dei vincoli», «Lesimas», «tesoro segreto», «la coppia»,
«l'angelo nero», «atlante degli insetti», «missione secondaria».

⚠️ **E una parola che il glossario NON decide, ma segnala:** il nome di
《不幸のシナア》 in italiano e' **«<Sinaha>» e basta**, senza l'epiteto. Il
progetto altrove lo ricostruisce proprio quando l'inglese lo butta (<Leiki>,
<Alice>, <Aribel>, <Alsapia>): qui l'epiteto e' «della sfortuna», ed e' la
ragione per cui il personaggio esiste. Un nome di creatura si cambia insieme
alla sua misura di larghezza e alle rese che lo citano: **da decidere**.

## I diciotto parlanti della 95a, decisi il 2026-08-25 — `chat.hsp` si chiude

Sette lotti, 73 rese, e la stessa cosa della 94a in forma piu' forte: **quasi
niente da decidere**. Il lessico stava tutto nel vicinato, e stavolta il
vicinato l'ha indicato `map.hsp` — la Valle di Raskilis nelle rese della 91a e
della 94a, la Gabbia di Amur nelle rese della 92a, il Meshera nella catena di
Regulus, l'oblio nelle rese di Mikraanesis. Le voci qui sotto sono le poche che
mancavano, piu' due **correzioni di coerenza** su rese gia' esistenti.

| JP | EN | IT | dove |
|---|---|---|---|
| 裂け目 (Raskilis) | crevice / rift | **fenditura** | `action.hsp:2854` lo dice gia' cosi' ed e' **la casella su cui si cammina** in `AREA_WEST_RASKILIS`. ⚠️ `chat.hsp:15440` (91a) diceva «fessura»: **rifatta**, era un secondo nome per lo stesso oggetto sulla stessa mappa |
| 悪魔の獣 | devilish beasts | **bestie diaboliche** | `chat.hsp:15354`. ⚠️ NON «demoniache»: 悪魔 in questo progetto e' **il demone** della trama (Mayroon, Eulderna, Kikkasu). Nancy da' un nome suo alle stesse creature che tutti chiamano 黒い獣 «le bestie nere» |
| ウキ | (buttato dall'inglese) | **galleggiante** | `chat.hsp:15366`, il segnale sull'acqua dove si pesca. L'inglese perde sia il galleggiante sia il fatto che sia un segnale |
| キャンプ地 | campsite | **il campo** | `chat.hsp:15338`. ⚠️ Non «campo profughi», gia' preso da `text.hsp:2985` per la terra di Ruoza |
| 水辺 | waterfront | **specchio d'acqua** | `chat.hsp:15365`, `:15373` |
| 冥宮の悪鬼 | hellabyrinth ruler | **il demone del palazzo infero** | gia' in `db_card.hsp:1388`; ripreso qui per le tre rese di `:10530`-`:10541` |
| 嬉シイ (katakana) | I'm glad | **CHE GIOIA.** | `chat.hsp:15126`. ⚠️ Non «CONTENTO», che porta un genere che Gilphem non ha. Il **maiuscolo** rende il katakana, come `db_creature.hsp:52721` |
| ツアープランナー | tour planner | **organizzatrice di viaggi** / **chi organizza viaggi** | `chat.hsp:13176` (gia' reso) e `:12760`. Tenuto distinto da **guida turistica** (ツアーガイド, `:7774`) |
| 本部 | council *(inglese)* | **il quartier generale** | `chat.hsp:9362`, come `db_creature.hsp:79879`. ⚠️ **Non** «il consiglio» di `:5423`, che rende 審査会, la commissione d'esame della Gilda dei Maghi: due parole diverse in giapponese |
| 忘却 | oblivion | **l'oblio** | gia' in `chat.hsp:18095` e `:10353`; **confermato** qui da `:15139` di BURT, che e' la riga che lega i cinque buchi di memoria della giornata |
| 未開 | unexplored | **terra selvaggia** | `chat.hsp:15342`, come `:2334` |
| 怪電波 | electromagnetic waves | **onde strane** | `chat.hsp:8784` |
| 駆動系 / データ格納部分 | drive system / data registers | **la parte motrice** / **la parte dove stanno i dati** | `chat.hsp:8784` |

⚠️ **Tre conferme, non decisioni** — cercate oggi e trovate gia' scritte: 護衛
«scorta» (`:6735`), 屋敷 «la villa» (`:7554`), 過保護 «apprensivo»
(`db_creature.hsp:62008`, di RENAI stessa).

## Gli otto parlanti della 94a, decisi il 2026-08-25

Otto lotti, 55 rese, e di nuovo **poche parole da decidere**: il lessico stava
gia' scritto nel vicinato — la valle di Raskilis nella donna resa nella 91a, il
seminario nei conferenzieri dell'87a, la Nave Magica nella catena delle
missioni, Gavela nell'85a. Le voci qui sotto sono quelle che mancavano, e tre
sono **conferme di una resa gia' esistente** messe qui perche' oggi sono state
cercate due volte.

| JP | EN | IT | dove |
|---|---|---|---|
| 露払い | personal bodyguards / *(butta)* | **ripulire la strada** | `chat.hsp:15078` (AIKAGE), `:9703` (SAIMEF), su precedente `:18160`. ⚠️ **L'inglese la perde due volte oggi**, e nella prima la capovolge: 露払い e' chi va **avanti** a sgombrare, non chi sta a fianco a proteggere |
| 分身の術 | shadow decoy | **tecnica dello sdoppiamento** | `chat.hsp:15087`. Distinta da 身代わりの術, gia' «tecnica della sostituzione» (`db_creature.hsp:73146`). Il bollettino su Aikage — `chat.hsp:24445`, «se lo colpisci a meta' **si sdoppia**» — decide il verbo |
| ツクモガミ | tsukumogami | **tsukumogami** (con glossa) | `chat.hsp:14914`. Compare **una volta sola** in tutto il sorgente. La parola resta, come «tanuki» e «kunoichi», ma la riga e' una **definizione** e senza capirla il confronto col mimic non si sente: accanto le va la glossa minima |
| 努力賞 | a little something for your effort | **premio per l'impegno** | `chat.hsp:14808`, su precedente `:14530` — lo stesso seminario, lo stesso premio |
| バネッサコーポレーション | Vanessa Corporation | **Vanessa Corporation** | `chat.hsp:14918`, `:14924`. Nome d'azienda, non si traduce |
| 神の心臓 / ヨロテオトル | god heart | **cuore di un dio** / **Yoloteotl** | `chat.hsp:9697`. ⚠️ ヨロテオトル **non e' un vocativo**: e' il nome dell'oggetto, `item.hsp:110` |
| 大氷河 | the glacier | **il grande ghiacciaio** | `chat.hsp:9702`. Compare una volta sola |
| 次元歪曲シーケンス | dimensional distortion sequence | **sequenza di distorsione dimensionale** | `chat.hsp:9637`, sotto «unita' a distorsione dimensionale» (93a) |
| 本機 | this Melugast | **l'apparecchio** | `chat.hsp:9606`. La macchina parla di se' in terza persona: e' la sua voce, non un sinonimo |
| 休止状態 | hibernation mode | **stato di riposo** | `chat.hsp:9686` |
| 携帯旅糧 | supplies | **cibo da viaggio** | `chat.hsp:15391`, sotto 旅糧 gia' «cibo da viaggio» (`db_item.hsp:148280`) |
| 有閑 | *(butta)* | **sfaccendato** | gia' in «<Zisilion> il re sfaccendato delle miniere». Rimesso qui perche' regge tutte e sei le sue righe |
| 素晴らしい汗 | Another day, another platinum coin | **che bella sudata** | `chat.hsp:13916`. ⚠️ Gemella di 「いい汗をかいたよ」, gia' «Ho fatto una bella **sudata**» (`db_creature.hsp:55277`): stessa immagine, stesso personaggio, due file. Si scrive la stessa parola |
| 街の依頼 | a request for the city | **incarico di citta'** | `chat.hsp:13913`, su precedente `:13964`, `:13978`. E' il nome di una meccanica, non un giro di parole |

⭐ **Quello che NON e' stato deciso qui, perche' era gia' scritto.** «il Sigillo
Eterno» (`chat.hsp:7829`), «potere divino», «dio cane» (`text.hsp:3030`),
«Noyel», «Mayroon», «Raskilis» e «la Valle di Raskilis» (`chat.hsp:9381`),
«continente fluttuante» (`:2184`), «navigazione dimensionale» (`:7879`), «il
Melugast», «barriera», «la capitale», «Eulderna», «nave magica»
(`text.hsp:9822`), «il dio del caos», «monete di platino», «posto di frontiera»
(`map.hsp:682`), «armi non morte», «baule», «mimic», «tanuki», «gilda»,
«Seminario d'Avventura», «<Karata> la mascotte», «<Bonyac> il merciaio»,
«<Saimef> il bianco ghiaccio», «<Manson> l'avventuriero prudente», «<Aikage> il
ninja dalla maschera demoniaca», e la formula «chi va all'avventura».

## `item_func.hsp`, decisi il 2026-08-25 — novantaseiesima

Il compositore del nome degli oggetti. Tre famiglie, e in due l'inglese non e' il
testimone da seguire.

### Il fabbro degli incantamenti (`custom_itemenchantment.hsp`, `chat.hsp`)

Il lessico è quello già in gioco dal dialogo di monte; qui c'è solo ciò che la
125ª ha dovuto decidere per la copia di Custom-GX.

| dove | IT | nota |
|---|---|---|
| エンチャント, in prosa | **incantamento** | come `chat.hsp:11290` e sorelle |
| エンチャント, in una voce di menu | **incanto** | forma corta: il tetto della pergamena è 58 caratteri e nella parentesi ci va `cnvitemname()`. Già scelta in `chat.hsp:11347` |
| サリムの言うエンチャント強度 | **la scala di Thalia** | サリム è **Thalia** in dodici rese su dodici; l'inglese di Custom-GX la chiama «hill folk rating» e ha cambiato nome lui, non il giapponese |
| 固定アーティファクト / 奇跡品 / 神器品 | artefatti **unici** / **eccezionali** / **celestiali** | già in `chat.hsp:11290` |
| 丘の民 | **gli abitanti della collina** | nove rese su nove |
| `"[N gold] "`, etichetta di prezzo | **`"[N oro] "`** | forma corta come `<N oro>` di `text.hsp:193`: quella lista può passare le dieci voci e allora `chat.hsp:25166` la tronca a 24 caratteri |
| 改造 / 弱める / 消去 dell'incantamento | **Potenziamento** / **Indebolimento** / **Cancellazione** | i tre messaggi finali, e le tre voci di menu che li aprono: «Potenziare?», «Indebolire?», «Cancellare?» |

⚠️ **Le tre voci di menu sono il verbo solo**, senza il nome dell'oggetto:
`cnvitemname()` può valere **38 caratteri** («pergamena di acquisizione di
attributi») contro i 24 dell'inglese, e restano 18 per l'etichetta. Che cosa si
potenzia lo dice il testo della finestra due righe sopra. Misura in
`scratchpad/_125-larghezze-menu-incanti.py`.

### Le sigle degli incantamenti (`showresist == 4`)

Abbreviano la lista distesa di `item_data.hsp:613`-`:709`, **gia' tradotta**: il
lessico viene da li'. ⚠️ Tetto del sito: **47 caratteri per riga**, condivisi fra
tutte le enchant di un oggetto. Niente accenti — «a'» costa due caratteri.

| EN | IT | nota |
|---|---|---|
| `Dmg` | Dann | mezza sigla: l'elemento lo scrive `skillname()` |
| `RandTeleport` | TeleCasuale | |
| `NoTeleport` | BloccaTele | |
| `Bloodsucking` | SucchiaSangue | |
| `MP-Absorb` | SucchiaMP | e' un **malus**: succhia gli MP di chi impugna |
| `EXP-Absorb` | FrenaCrescita | ⚠️ l'inglese sbaglia: `ENCHANT_DISTURB_GROWTH`, *ostacola* |
| `SummonMonster` | AttiraMostri | |
| `HealMP` / `HealSP` | CuraMP / CuraSP | |
| `Float` | Levita | «levitazione» in `command.hsp:2185` |
| `DigestRot` | MangiaMarcio | |
| `WorldTravel` | Viaggi+ | |
| `SeeInvisible` | VedeInvisib | |
| `ResCurse` | ResMalediz | |
| `ResSteal` | ResLadri | |
| `ResEther` | ResEtere | |
| `ResWeather` | ResMaltempo | |
| `ResPregnant` | ResAlieni | |
| `ResMutation` | ResMutazioni | |
| `SpellPow+` | Magia+ | |
| `BreathPow+` | Soffio+ | |
| `ThrowPow+` | Sassi+ | |
| `ChargePow+` | Carica+ | |
| `Fire/Cold-Combine` | Fuoco/Gelo | le sigle degli elementi sono `Fu Ge Fl Os Me Ve Ol Su Ne Ca Ma` |
| `Mind/Sound-Combine` | Mente/Suono | |
| `Poison/Nerver-Comine` | Veleno/Nervi | |
| `Dark/Nether-Combine` | Oscur/Oltret | |
| `DistantAttack` | ColpoLontano | |
| `Pierce` | Perfora | |
| `Critical` | Critico | |
| `ExtraMelee` / `ExtraShot` | Mischia+ / Tiro+ | |
| `InterlockShot` | TiroConcat | |
| `ProximityAttack` | Appoggio | |
| `StopTime` | FermaTempo | |
| `CutReflect` | RendeTaglio | |
| `MagicReflect` | RiflMagia | |
| `ShotReflect` | **TiroRapido** | ⚠️ l'inglese sbaglia: `ENCHANT_QUICK_SHOOTING`, non riflette niente |
| `CritiGuard` | MenoCritici | |
| `PhysicalRes` | ResFisico | |
| `DmgImmune` | AnnullaDanni | |
| `Dragonkiller` | Anti-draghi | la famiglia dei cinque tiene il prefisso `Anti-` |
| `Undeadkiller` | Anti-nonmorti | |
| `Birdkiller` | Anti-volanti | 空敵殺し: nemici **in volo**, non uccelli |
| `Godkiller` | Anti-dei | |
| `MetalKiller` | Anti-metalli | |
| `Reveal Religion` | **MantieneFede** | ⚠️ sbagliano tutt'e due: `ENCHANT_PRESERVE_PIETY` |
| `Radiowave` | SegnaliDei | |
| `Ragnarok` | PortaLaFine | 終結, e la distesa dice «Porta la fine» |
| `ManaOvercharge` | ManaInAttacco | |
| `PerformReward+` | Ricompense+ | |
| `Clock-Up` | PortaIlTempo | 時を纏っている, «Porta con se' il tempo» |
| `BoozeMelody` | Inebria | |

### Le parentesi di stato della riga d'inventario

| EN | IT | nota |
|---|---|---|
| `(Charges: N)` | (cariche: N) | «cariche» da `action.hsp:6742` |
| `(Bullets: N)` | (colpi: N) | |
| `(Remain: N/5)` | (ancora N/5) | |
| `(Scary)` | (spavento) | il presagio, non il verdetto: **non** «con maledizione» |
| `(Dreadful)` | (malaugurio) | idem, per `ITEM_STATUS_DOOMED` |
| `(Temporal)` | (svanisce in viaggio) | 移動時消滅 |
| `(Empty)` — sfera dei mostri | (vuota) | genere noto: un sito solo, femminile |
| `(Empty)` — contenitori | (niente dentro) | ⚠️ li' il genere cambia a ogni oggetto |
| `(Aphrodisiac)` | (afrodisiaco) | |
| `(Poisoned)` | (veleno) | come `text.hsp:69` |
| `(Danger!)` | (pericolo!) | |
| `(Herb)` | (con erbe) | |
| `(Antiseptic)` | (antisettico) | |
| `(Need Sleep)` | (serve dormire) | |
| `(Next: Nh.)` | (fra N ore) | il giapponese dice solo «N ore» |
| `(Buying price: N)` | (prezzo: Ng) | la `g` che l'inglese butta |
| `Lock-Lv. N` | serratura liv. N | |
| `Serial No.` / `Property No.` | n. serie / immobile n. | |
| `(Model-N)` | (modo N) | モード e' **modo**, non «model» |

⚠️ **La bara della negromanzia non e' in questa tabella**: le sue otto parentesi
sono **nomi di creatura** gia' decisi in `db_creature.hsp` — gatto zombi, zombi,
mummia, **scheletro guerriero**, lich, necrobambola, **drago zombi**, **occhi
morti** — e si copiano da li' togliendo l'articolo.

### I pezzi del nome, e i tredici fiori

| EN | IT | nota |
|---|---|---|
| ` of X` (altare, vomito, fuso) | di X | ⚠️ l'inglese incornicia (`<X>`), il giapponese dice の |
| ` titled <T>` | dal titolo \<T\> | invariabile: regge qualunque genere di libro |
| ` titled <Art of S>` | dal titolo \<S\> | «Art of» **non c'e' in giapponese** e cade |
| ` of Rachel No.` | di Rachel n. | |
| ` which cannot be used anymore` | ormai inservibile | |
| ` of saint` / ` of wicked` | del giusto / del malvagio | 善人 / 悪人 |
| `<N gp>` | \<N oro\> | «oro» da `text.hsp:193` |
| `unknown item (incompatible version)` | oggetto sconosciuto (versione incompatibile) | |
| `milk coffee` / `coffee` | caffelatte / caffè | |
| `milk tea` / `black tea` | tè al latte / **tè nero** | 紅茶: il gioco ha anche il tè verde |
| `CF potioman` | potioman CF | «potioman» tenuto, da `chat.hsp:3118` |
| `crush` / `battle` / `super potioman` | potioman d'urto / da battaglia / super | |
| `Spinning` `Mighty` `Dual` | Rotante / Potente / Doppio | i modi hanno un senso: `item_data.hsp:702`-`:707` |
| `Rapid` `Snipe` `Deceive` | Rapido / Preciso / Ingannevole | |

**I tredici fiori selvatici**, col genere da cui `strumenti/articolo.py` ricava
l'articolo (la toppa lo sceglie su `PARAM2`):

| EN | IT | genere |
|---|---|---|
| `wild flower` | fiore selvatico | m |
| `daffodil` | narciso | m |
| `margaret` | margherita | f — ⚠️ マーガレット e' il fiore, non un nome di persona |
| `dandelion` | tarassaco | m — «soffione» e' la testa sfiorita, un'altra fase |
| `tulip` | tulipano | m |
| `rose` | rosa | f |
| `hydrangea` | ortensia | f — **elide**: «un'ortensia» |
| `lily` | giglio | m |
| `sunflower` | girasole | m |
| `marigold` | calendula | f |
| `cosmos` | cosmea | f — ⚠️ non «cosmo» |
| `chrysanthemum` | crisantemo | m |
| `primula` | primula | f — identica all'inglese **per coincidenza**, vedi `invariati.md` |



## Le 54 chiavi della raccolta automatica, decise il 2026-08-26 dalla 100ª

⚠️⚠️ **Queste non sono etichette da leggere: sono le parole che il giocatore
scrive in `data\autopick.txt`**, e `custom_autopick.hsp` le confronta per
**sottostringa** con la sua regola e col nome dell'oggetto. Cambiarne una qui
senza cambiare il modello — o viceversa — spegne la funzione: vedi
`decisioni.md` §98ª e §100ª.

Tre vincoli che valgono per tutte e che non si vedono guardando la parola:

1. **invariabili**: il giocatore le scrive a mano, e nessuno accorda il genere
   per lui. Dove l'aggettivo si accorderebbe, la chiave diventa un complemento;
2. **senza accenti**: il modello è in UTF-8 e l'eseguibile in CP932, e una
   chiave accentata esisterebbe in due forme che non si agganciano;
3. **nessuna dentro un'altra**: `instr` confronta per sottostringa, e una chiave
   contenuta in un'altra rompe tutt'e due. Lo misura
   `scratchpad/_100-selettori-ombra.py` — l'inglese di monte ne ha **due**, noi
   zero.

### I 21 modificatori (con gli spazi attorno)

| EN | IT | perché |
|---|---|---|
| ` all ` | ` ogni ` | invariabile, e regge il singolare dei tipi qui sotto |
| ` unknown ` | ` senza nome ` | `ITEM_KNOWN_NONE` |
| ` name identified ` | ` con nome noto ` | `ITEM_KNOWN_NAME`. I tre gradini sono paralleli, e l'aggettivo concorda con un nome che sta **dentro la chiave** |
| ` quality identified ` | ` con pregio noto ` | `ITEM_KNOWN_QUALITY` |
| ` fully identified ` | ` con effetti noti ` | `ITEM_KNOWN_FULL`. «Effetti» perché è quello che l'identificazione piena rivela, e lo dice già il tutorial (`chat.hsp:14107`) |
| ` worthless ` | ` senza valore ` | la coda che `db_item.hsp:149970` dà già al lingotto falso |
| ` rotten ` | ` marcio ` | vale solo sul cibo (`:191` chiede `FILTER_ITEM_FOOD`), ed è la parola di `command.hsp:2230` |
| ` empty ` | ` vuoto ` | vale solo sui contenitori (`:221`, `FILTER_CONTAINER`) |
| ` bad ` | ` scadente ` | ⭐ le sei qualità vengono da `_quality` (`text.hsp:106`), la scala che il giocatore legge nel pannello — e finiscono tutte in `-e`, cioè non si accordano |
| ` good ` | ` comune ` | ⚠️⚠️ **non «buono»**: `FIX_QUALITY_GOOD` è l'indice 2 di `_quality`, che a schermo dice `common`. Si dice quel che c'è scritto sullo schermo |
| ` great ` | ` eccellente ` | `_quality` 3 |
| ` miracle ` | ` eccezionale ` | `_quality` 4 |
| ` godly ` | ` celestiale ` | `_quality` 5 |
| ` special ` | ` speciale ` | `_quality` 6 (`FIX_QUALITY_UNIQUE`) |
| ` precious ` | ` prezioso ` | non è un gradino della scala: è `ITEM_BIT_PRECIOUS` |
| ` blessed ` | ` con benedizione ` | ⭐ la deroga già decisa più sopra per `strblessed`: complemento invariabile, e **le stesse parole che stanno dentro il nome dell'oggetto** contro cui `:358` confronta |
| ` uncursed ` | ` senza maledizione ` | `ITEM_STATUS_NORMAL` |
| ` cursed ` | ` con maledizione ` | come `strcursed` |
| ` doomed ` | ` con dannazione ` | come `strdoomed` |
| ` alive ` | ` in vita ` | `ITEM_BIT_ALIVE` |
| ` evolution ` | ` di evoluzione ` | complemento, per non accordarsi col genere di quel che segue. Il nome dell'oggetto resta «oggetto evolutivo» |

### I 33 tipi (chiavi nude, al singolare)

| EN | IT | da dove viene |
|---|---|---|
| `item` | oggetto | |
| `equipment` | equipaggiamento | `command.hsp:12618` |
| `melee weapon` | arma da mischia | «Mischia» è il nome della casella (`command.hsp:10517`) |
| `helm` | elmo | |
| `shield` | scudo | |
| `armor` | armatura | ⓘ `db_item.hsp:152729` dice «corazza» per il pezzo, «armatura» è la classe |
| `boot` | stivale | singolare: ` ogni ` regge il singolare |
| `belt` | cintura | |
| `cloak` | mantello | |
| `glove` | guanto | |
| `ranged weapon` | arma da tiro | «Tiro» è il nome della casella (`command.hsp:15309`) |
| `ammo` | dardo | |
| `ring` | anello | |
| `necklace` | collana | |
| `potion` | pozione | |
| `scroll` | pergamena | |
| `spellbook` | grimorio | ⭐ e per questo non fa ombra a «libro», dove l'inglese `spellbook` contiene `book` e rompe la coppia |
| `book` | libro | |
| `rod` | bacchetta | |
| `food` | commestibile | ⚠️ **non «cibo»**, per non fare ombra a «cibo da viaggio»: è la seconda coppia rotta in inglese, e la parola che si sposta è la generica |
| `tool` | attrezzo | `chat.hsp:14172` |
| `furniture` | mobilio | `text.hsp:9671` |
| `well` | pozzo | |
| `altar` | altare | |
| `remains` | resto | ⓘ il modello inglese qui documenta `all remain`, che **non aggancia**: la chiave è `remains` |
| `junk` | cianfrusaglia | `db_item.hsp:143816` |
| `gold piece` | moneta d'oro | |
| `platinum coin` | moneta di platino | |
| `chest` | baule | |
| `ore` | minerale | |
| `tree` | albero | |
| `traveler's food` | cibo da viaggio | il nome che l'oggetto ha (`chat.hsp:13959`) |
| `cargo` | merce da commercio | «merci da commercio», `chat.hsp:14079` |

ⓘ Due selettori del sorgente **non** sono qui: ` zombie ` (腐りきった) e
` dragon's ` (ドラゴンの) stanno dietro un commento `//` a `:200`-`:217`, cioè
sono codice che il compilatore non vede. Sono in `rinviate.jsonl`.

## `db_card.hsp`, decisi il 2026-08-26 dalla 102ª — la prosa delle carte

⚠️ Queste parole si sono decise **traducendo la prosa delle carte**, dove il
testo nomina creature e luoghi che altrove hanno già un nome. La regola resta
quella di sempre: se il nome esiste nel dizionario si ricopia, non si
reinventa. Qui stanno solo le parole che un nome **non ce l'avevano**.

| giapponese | inglese di monte | italiano | perché |
|---|---|---|---|
| ギガモール | `Gigamole` | **la talpa colossale** | `メガモール` è già «la talpa gigante» (`db_card.hsp:7212`), e `:7206` dice che questa è **dieci volte più alta e mille volte più pesante**. Compare in tre carte (`:628`, `:5516`, `:7206`) e le altre due dovranno dire lo stesso. ⓘ `《ギガモールの骨鎌》` resta `<Falce della Bestia>` (`db_item.hsp:141477`): lì il nome era stato aggirato |
| アイオン | `Aion` | **gli Aion** | la stirpe divina di Mikraanesis (`:1681`), defluita dall'abisso |
| 超永遠世界 | `Trans-Eternal World` | **il mondo oltre l'eterno** | il luogo da cui gli Aion sono emigrati a Irva e a Gaius Vis |
| 妖術士 | `sorcerer` | **gli stregoni** | quelli che hanno fabbricato gli uruk (`:2006`, `:2045`) |
| 自律金属細胞 | `autonomous metal cells` | **cellule metalliche autonome** | i due desktop (`:1902`, `:1915`) |
| 泡はきドラゴン | `foam-eating dragon` | **il drago sputabolle** | ⚠️ **coniato qui e non ancora nel dizionario**: `:2903` lo cita, e il suo blocco in `db_card.hsp` arriva più avanti. Quando quel blocco si apre, il nome dev'essere questo |
| 鮫殴りセンター | `Shark Punching Centre` | **il Centro Pugilistico Antisqualo** | ⓘ occorrenza **unica** in tutto il sorgente (`:927`), ed è da lì che viene la sigla SP di `SP Champion` |

### ⚠️⚠️ `菌` è «il fungo» o «il batterio», e a distinguerli è l'inglese

`glossario.md` fissa già `菌` → **il fungo** quando è *il Meshera visto da
dentro*. Nella 102ª `細菌` è comparso **tre volte** con la stessa parola
giapponese, e sono tre cose diverse:

- `:680` e `:693` — l'inglese di monte scrive **Meshera**: è il fungo;
- `:719` — l'inglese scrive **bacteria**, e la carta racconta di un batterio
  coltivato per davvero in laboratorio: resta **batterio**.

⭐ La distinzione **non si deduce dal giapponese**, che dice `細菌` in tutt'e
tre. Qui l'inglese non è la lingua di partenza ma un testimone: chi ha scritto
quella versione sapeva quale delle due cose fosse in gioco. È il caso simmetrico
di quelli in cui l'inglese appiattisce, e va guardato con lo stesso sospetto —
si controlla, non si crede.

⚠️ E il nome della carta può tirare dall'altra parte: `モンスターバクテリア` è
**il batterio mostruoso** perché quello è il suo *nome proprio* in katakana, non
la sostanza di cui è fatto. Nome e prosa si leggono a due righe di distanza
nello stesso pannello, quindi la tensione si vede: è voluta.

### ⚠️ Un nome che l'inglese appiattisce e il giapponese distingue

`:2487` — la banca è `ザイエルン銀行`, **Zaielun**; la città in cui sta la
filiale è `ザイール`, **Zaile**. L'inglese scrive «the Zaile branch of the Zaile
Bank», cioè lo stesso nome due volte. In italiano i due nomi restano due.

### ⭐ Tre giochi di parole tenuti, e come

- `:1798` `先生きのこ` — 「この先生きのこれるか」 («riusciremo a sopravvivere
  d'ora in poi?») si legge anche 「この先生 きのこ」, «questo professore fungo».
  L'italiano nasconde il fungo dentro una frase seria: «ha poco da **fungere**».
  L'inglese di monte rinuncia e scrive una frase piana.
- `:1486` `邪拳王` («il re del pugno malvagio») suona come `ジャンケン`, il nome
  giapponese della morra: la carta racconta l'origine del gioco, e in italiano
  il gioco è **la morra**.
- `:1512` chiude sul modo di dire `猫の手も借りたい`, «tanto indaffarati da
  farsi prestare perfino la zampa di un gatto»: la resa lo tiene per intero.
- `:2240` regge su una metafora che l'italiano ha uguale: il mediatore è una
  **colomba** ed è un **falco**. Rendere `鳩` con «piccione» avrebbe spento la
  battuta a fine carta.

## `db_card.hsp`, decisi il 2026-08-26 dalla 103ª — i lotti 7-10

⚠️ Vale la premessa della 102ª: qui stanno solo le parole che un nome **non
ce l'avevano**. Con una eccezione, la prima, che è invece la correzione di un
nome che ce l'aveva ed era sbagliato.

| giapponese | inglese di monte | italiano | perché |
|---|---|---|---|
| カブ | `cub` | **il Cub** | ⚠️⚠️ **correzione di un nome già reso.** Diceva «il cucciolo», dall'inglese `cub` preso alla lettera nella fase dei nomi. La sua carta lo smentisce: 機械の馬, «un cavallo meccanico robusto e che consuma poco» (`:13955`). È la Honda Super Cub, e `:3423` presenta «la moto grossa» come sua parente. Sei voci corrette in quattro dizionari da `scratchpad/correzione-cub.py`; `カブ=トライズ` diventa **il Cub Toraizu** |
| ハム将軍 | `General Ham` | **il criceto generale** | occorrenza **unica** in tutto il sorgente, e sta dentro la prosa di `:4788`: non c'è nessun nome da rispettare. Segue il fratello maggiore `ハム大老` → «il criceto gran anziano» |
| サイロニア | `Cyronia` | **Cyronia** | il regno antico di `:3774`, dove salire in groppa all'insetto coronato era il rito di successione. Occorrenza unica |
| 三途の川 | `Sanzu River` | **il fiume Sanzu** | `:3761` e `:3839`. Non si italianizza in «Stige»: il mondo dei morti di Elona ha già un lessico suo |
| 冥海 | `the Underworld` | **il mare dei morti** | dove finisce il fiume Sanzu (`:3839`). ⓘ Il `冥海魔オルチヌス` era già reso «il demone marino Orcinus», e la prosa non lo tocca |
| シズルコード | `the Ssil Code` | **il Codice di Ssil** | `:4580` lo battezza, `:5022` lo cita. ⚠️ Il giapponese chiama la strega `シズル`, ma il nome della carta è già `<Ssil>`: il libro porta **quel** nome, non una traslitterazione nuova |
| 竜人 | `dragon man` | **l'uomo lucertola** | nella prosa segue il nome della razza (`db_race.hsp:911`), non i nomi delle singole carte, che alternano «dragonewt» e «lucertola» |
| ショクパンヨリフランスパン | `shoku panyori French bread` | **megliobaguettechepancarré** | ⚠️ **coniato qui.** È il materiale superduro di cui è fatto lo spirito del pane (`:4931`), e in giapponese è già una parola-scherzo. ⚠️⚠️ Dopo `degrada()` sono **27 caratteri**, e la finestra in cui il taglio del pannello cerca uno stacco ne è **15**: oggi cade in un punto che regge, ma è la stringa più fragile del progetto. Se `_102-carta-conoscenza` dovesse mai segnalare una parola spezzata in `db_card`, è la prima da guardare |

### ⚠️ `ヴァリウス` è **Barius**, anche dove l'inglese scrive «Vallius»

`:3345` e `:3696` lo chiamano *Vallius*. È lo stesso personaggio di
`chat.hsp:13927` e `db_creature.hsp:55752`, dove l'inglese di monte dice *Lord
Barius* e il progetto ha reso **Barius**. Vince il nome che il giocatore legge
quando gli parla, non quello che monte ha scritto qui.

### Tre bisticci persi, e uno tenuto di peso

- ⭐ **Tenuto.** `:4697` chiude su 全ては亀のみぞ…もとい、神のみぞ知る: la
  **tartaruga** infilata al posto del **dio** nel modo di dire. In italiano
  «lo sa soltanto la tartaru... pardon, soltanto il cielo» fa lo stesso scherzo
  con le stesse parole, ed è raro che capiti.
- **Persi, e tutti e tre stanno nel nome, non nella prosa.** `イリス` è la dea
  Iris dentro リス (scoiattolo); `テロリス` è テロリスト col medesimo innesto;
  `ブルーブル` incastra ブルー (avvilito), ブルブル震える (tremare) e la
  ブルーバブル che la carta nomina in coda. I nomi erano già resi: la prosa non
  ci prova e non spiega.
- **Perso senza rimedio.** `:3878`: la stella marina sale a terra perché ha
  saputo che lassù è popolare un ハムスター — che finisce in **スター**. In
  italiano «criceto» non contiene «stella». Si tiene il criceto, che è una
  creatura del gioco e quindi verificabile, e si lascia cadere il bisticcio.
  ⓘ L'inglese di monte aveva risolto togliendo il criceto: così la carta non
  dice più niente.

## I lotti 11-14 di `db_card.hsp`, decisi il 2026-08-26 (104ª)

| JP | EN di monte | IT | perché |
|---|---|---|---|
| キッカス | `Kikkasu` / `Kikkas` | **Kikkasu** | ⚠️ **Monte lo scrive in due modi** e ogni lotto aveva seguito il file davanti: 7 volte `Kikkasu` in `chat.hsp` e `text.hsp`, 3 `Kikkas` nelle carte. Vince la maggioranza, che è anche quella della catena della missione. Tocca il **nome** `il pitone di Kikkasu`, stessa firma in due dizionari. Vedi `correzione-kikkasu.py` |
| エルン | `Eln` / `Elun` | **Eln** | ⚠️ Stesso guasto, stesso giorno, e di nuovo di monte. `chat.hsp:7676` **definisce** i Norne nominando le tre stirpi insieme (Ahlung, Eln, Dovarn); `:9499` è una menzione. Serve a `db_card.hsp:7011`. Vedi `correzione-eln.py` |
| 化身の黒猫 | the Black Cat | **il gatto nero delle Incarnazioni** | `化身` non è una parola sciolta: è una **razza**, `神の化身` → «Incarnazione» (`db_race.hsp:5553`), quella dei compagni-avatar che il lotto 13 nomina uno per uno. ⚠️ Torna a `db_card.hsp:10768` |
| レム・イド | Rehmido | **Rehm-Ido** | ⚠️ **Non** `レミード` → «Remido», che sono le **rovine**: Rehm-Ido è la **civiltà** (`chat.hsp:8144`). Due nomi simili a due lotti di distanza |
| 眷属 (混沌の—) | the Military Force | **il figlio del caos** | `chat.hsp:10321` lo aveva già reso «i figli del caos». L'inglese di `:6335`, `:6348` e `:6361` legge 眷属 come un corpo militare: non è né il senso né il numero |
| 妖怪 (nei tre 鬼) | — | **creatura soprannaturale** | `:5529`, `:5542`, `:5555` hanno la stessa prima frase, e dentro c'è **anche** 悪魔, che nel progetto è «il demone». I loro nomi sono già `il demone splendente / squartatore / frantumatore`: chiamarli tutt'e due «demone» nella stessa riga li appiattisce |
| 精霊が◯◯を象って実体化した存在 | a being whose spirit has materialized in the form of… | **uno spirito che ha preso corpo nella forma di…** | formula fissa, tre carte (`:5711`, `:5841`, `:5854`): si rende identica |
| 外法 | foreign laws / the Outer Law | **le arti proibite** | `:5867` e `:6257`. L'inglese sbaglia due volte in due modi diversi, e la seconda la maiuscola come se fosse un'istituzione |
| 当て馬 | a guessing horse | **l'esca** | `:5191`. È il cavallo che si mette in pista per far correre gli altri; l'inglese traduce alla lettera e in inglese non vuol dire niente |
| 疫病神 (`:5399`) / 厄病神 (`:5828`) | the pestilence god / a god of disaster | **il dio della pestilenza** / **portasfortuna** | ⚠️ Stessa parola, due usi. A `:5399` è letterale ma **non è una creatura del gioco** (unica occorrenza nel sorgente) e **non** si aggancia al `疫病の悪魔` della missione; a `:5828` è il modo di dire |
| 盆踊り | bon-dancing | **il ballo dell'Obon, la festa dei morti** | `:5880`. La glossa serve: la battuta è che a ballare il ballo dei morti è un morto |
| élite | an elite | **fra le elette** | ⚠️ Non è una scelta di gusto: `verifica.py` boccia `élite`, perché `degrada()` in CP932 mette l'apostrofo **dentro** la parola e a schermo si legge `e'lite` |

⭐ **Due citazioni con una forma italiana già fatta.** `:5243` ricalca Gettysburg
— ペンギンのペンギンによるペンギンのための国 → *un paese dei pinguini, dai
pinguini, per i pinguini* — e `:5802` è Muhammad Ali, 蝶のように舞い、蜂のように
刺す → *vola come una farfalla, pungi come un'ape*. `:5386` porta la **pecorella
smarrita** del Vangelo, che regge anche la carta gemella `:5373`.

⭐ **Un bisticcio che si tiene cambiando parola.** `:5373`: 外道 è *fuori dalla
via*, e il nome della carta è `la pecora smarrita`. In italiano *smarrire la
retta via* fa lo stesso doppio senso, morale e stradale, che l'inglese («truly
an outsider») aveva perso.

⚠️ **Sei errori di monte presi dal giapponese nei lotti 11-13**, tutti
verificabili riga per riga: `:5139` 食べられないことはない (*non è che non si
possa mangiare*) reso «It's never eaten»; `:5178` 後天的 (*acquisito*) reso «born
with»; `:5256` 少なくない (litote: *non pochi*) reso «there are few»; `:5646` un
«God of Creation» inventato che rovescia il paragone; `:5672` 比較にならない
(*incomparabilmente più forte*) reso «in comparison to»; `:5763` 効かない (*non
fa presa su di lui*) reso come un gigante malato, cioè il rovescio della carta.

## I lotti 15-18 di `db_card.hsp`, decisi il 2026-08-26 (105ª)

⚠️⚠️ **Quattro termini di questa sessione erano già decisi altrove e li ho
sbagliati lo stesso.** Le reti del lotto — `verifica`, `guardie` e le tredici
reti dello script — **non leggono questo file né `invariati.md`**, e tutte e
quattro le rese sarebbero finite nel gioco. Stanno qui in cima perché la lezione
è quella, non i termini nuovi.

| JP | come l'avevo reso | resa giusta | dove stava già scritto |
|---|---|---|---|
| 手裏剣 | ~~stelline da lancio~~ | **shuriken** | `invariati.md`: prestito acquisito, maschile, invariato al plurale (`:8441`) |
| レム・イド | ~~Rehmido~~ | **Rehm-Ido** | glossario della 104ª. ⚠️ `Rehmido` è l'inglese di monte, e `Remido` (レミード) sono le **rovine**: la distinzione è il motivo per cui la 104ª aveva scelto il trattino. Quattro carte, `:8168`-`:8207` |
| 精霊が◯◯を象って実体化した存在 | ~~uno spirito che ha preso corpo dando a sé stesso la forma di…~~ | **uno spirito che ha preso corpo nella forma di…** | glossario della 104ª: formula fissa, e tre carte (`:5711`, `:5841`, `:5854`) la rendono identica. Qui torna a `:8025` |
| 眷属 (混沌の—) | ~~una creatura al seguito del caos~~ | **il figlio del caos** | glossario della 104ª, da `chat.hsp:10321` (`:8337`) |

### I termini nuovi

| JP | EN di monte | IT | perché |
|---|---|---|---|
| 超獣 | `superbeast` | **la superbestia** | `:7193`. ⚠️ Compare **una volta sola in tutto il sorgente**: coniata, e se tornasse si ubbidisce a questa |
| ロストテクノロジー | `lost technology` | **la tecnologia perduta** | `:7310` e `:7323`, i due moai. Le due carte condividono la prima frase in giapponese e in inglese, e le rese la condividono uguale |
| 第一紀 | `the early First Age` | **la Prima Era** | `:7505` |
| 決戦兵器 | `the decisive weapon` | **l'arma della battaglia decisiva** | `:7687`, il cannone a supergravità che ne era l'armamento aggiuntivo |
| 旧時代 | `old-fashioned` | **il tempo antico** | `:8064`. L'inglese lo legge come «all'antica», ma è l'era precedente, quella delle macchine |
| 鎖鎌 | `chain scythe` | **la falce a catena** | `:8766` |
| ボコノン教 / カラース | `Bokononism` / `Kalas` | **il bokononismo** / **il karass** | `:8376`. Il nome della carta era già «il guardiano del karass»: la prosa gli va dietro. ⚠️ L'inglese scrive `Kalas` nel corpo e `wrang-wrang` nel nome, due traslitterazioni diverse dello stesso romanzo |
| メルカ地方 | `the Melkawn region` | **la regione di Merca** | `:7271`. ⚠️ **メルカ non è メルカーン**: `map.hsp:3619` ha «Palude di Merca» e `map.hsp:8085` «di Melkawn». L'inglese le confonde in una sola |
| 化け狸 (prosa) | `badger` | **il tanuki mutaforma** | `:7154`, e la prosa lo mette accanto al `mimic`: due che si ingannano a vicenda |

⭐ **Una formula che si ripete e va resa identica**: `異常な素早さで彷徨する鐘の
魔物` apre sia `:7167` (la campana a martello) sia `:8896` (la campana del
giudizio), a due lotti di distanza. Stessa prima frase in italiano.

⚠️ **Sei errori di monte presi dal giapponese**, verificabili riga per riga:

- `:7648` 性根が腐っている (*ha l'animo marcio*, ed è il seguito di «dalla
  cintola in giù è marcia») letto come una **pulsione sessuale corrotta**;
- `:7843` 精霊の力 (*la forza di uno spirito*) reso «the power of a demigod»;
- `:7882` l'inglese **salta una frase intera** delle tre del giapponese;
- `:8129` やる気が空回りした (*la voglia le gira a vuoto*) reso «her lack of
  motivation», che è il contrario: non le manca la voglia, la spende male;
- `:8246` 調子に乗った部下を一喝する (*zittire con un urlo il sottoposto che si
  monta la testa*) reso «cheer up a subordinate who's in a bad mood»;
- `:8311` i puntini in mezzo alla frase, che il giapponese non ha.

ⓘ **Il gioco di parole che non si rende, e la parola che resta**: `:7882` studia
la parentela con 「おとおと」, cioè 弟 (*otooto*, «fratello minore») scritto
storto. La parola resta com'è, come `tsukumogami` e `kunoichi`.

## I lotti 19-30 di `db_card.hsp`, decisi il 2026-08-26 (106ª) — il file si chiude

| giapponese | inglese di monte | italiano | perché |
|---|---|---|---|
| 冥王 | `the Dark Lord` | **il signore dell'oltretomba** | `:9325`, l'olog. Hapax come **persona**; il progetto ha già 冥王の咆哮 → «ruggito dell'oltretomba» (`skill.hsp:814`) |
| 不死鳥 / 鳳凰 | `phoenixes and phoenixes` | **l'araba fenice** / **la fenice d'oriente** | `:9260`. ⚠️ L'inglese le **appiattisce tutt'e due** sulla stessa parola, e il senso della carta è proprio che l'uccello vermiglio odia essere confuso con l'una **e** con l'altra |
| 猫族 | `the cat tribe` | **il popolo dei gatti** | `:10521`, il guerriero dalla testa di leopardo; torna a `:13539` (il leone) |
| オチムシャ | `Ochimsha` | **ochimusha** | `:11379`. È 落武者 scritto in katakana per farne un soprannome, e resta invariato: l'inglese lo traslittera a sua volta, con un refuso |
| 亜人 | `subhuman` | **una specie affine all'uomo** | `:11706`, il troll |
| ジュア祭 | `the Jua festival` | **la festa di Jure** | `:11758`. La dea è già **Jure** dappertutto |
| 音属性 | `the attribute of sound` | **l'attributo suono** | `:11810`, la mandragora. Sulla riga delle rese di `action.hsp` per gli altri attributi |
| 邪眼 | `the evil eye` | **il malocchio** | `:14007`, l'occhio impuro |

⭐ **Quattro formule che si ripetono e vanno rese identiche.** Nessuna rete le
pretende — la rete 3 confronta i **giapponesi interi**, e questi sono interi
diversi — quindi la coerenza è a carico di chi scrive:

    エーテルを好む、竜族の一種      «Una specie della stirpe dei draghi, con un
                                    debole per l'etere»  — sei carte, :12889-:12954
    進化の過程で生まれた竜の亜種    «Una sottospecie di drago nata lungo il
                                    cammino dell'evoluzione» — :10924, :12304,
                                    :12538, :12551
    〜の一部にしてその下僕          «Una parte di X e insieme il suo servo» — gli
                                    otto servitori delle otto divinità,
                                    :14449-:14540, che nel mazzo si leggono di fila
    異常な素早さで彷徨する鐘の魔物   «Un mostro campana che vaga con una rapidità
                                    anomala» — :14839 e :14852. ⚠️ E in :14839
                                    l'inglese ha **perso** questa prima frase

⚠️⚠️ **Quindici errori di monte presi dal giapponese**, verificabili riga per riga:

- `:9338` 人間の腕 e `:9377` 下位の巨人, tutt'e due resi `an Indian Elephant`;
- `:9728` 頚動脈 con lo stesso elefante aggiunto dal nulla;
- `:9845` l'inglese **ha perso la prima frase** e comincia a metà;
- `:10105` 乗り物にすごく弱い appiattito in `motion sickness`, che perde il perché;
- `:10495` 集めるだけでは飽き足らず (*collezionarli non le bastava*) **rovesciato**
  in `so bored with collecting them`;
- `:10716` 上辺では (*in superficie*) letto come `on the upside`;
- `:10027` 適当な教育 (*educata alla come viene*) **rovesciato** in
  `her mother's proper upbringing`, ed è la ragione per cui il ragazzo è ingenuo;
- `:11641` 手にした獲物 (*l'arma che ha in mano*) reso `the prey in his hands`;
- `:11667` コブシ (*i pugni*) reso `his knob`;
- `:11875` la fama di **traditore** del pipistrello resa `the inaccurate vision`,
  che contraddice la frase prima;
- `:12720` ハイイログマ (*l'orso grigio*) traslitterato `the hylog bear`;
- `:12785` 悪阻 (*la nausea*, ed è uno stato del gioco) reso `malice`;
- `:12811` la combinazione fra la creatura e i **suoi** serpenti resa
  `the combination of the snakes and the snakes`;
- `:12876` 姦しい (*chiassosa*, dai tre 女 del kanji) reso `fornicating`;
- `:13292` キングは尻に敷かれている **rovesciato** in `the King is a pain in the
  arse`: l'inglese scambia chi comanda, e la battuta è tutta lì;
- `:13435` 地のオパートス (il **dio** Opatos della terra) reso `a local opus`;
- `:13409` 衛生兵 (*il medico da campo*) reso `air supports`;
- `:13370` センセイ traslitterato `senshi`;
- `:12733` レム・イド reso `Remido`, che sono le **rovine** e non la civiltà.

ⓘ **L'elefante indiano è una gag vera, ed è per questo che i tre errori sopra
sono difficili da vedere.** `インド象` sta nel **giapponese** di dieci carte di
fila, da `:12018` a `:12135`: è il tormentone con cui monte misura la potenza di
ogni soffio dei segugi. Il traduttore inglese l'ha esteso a tre carte che non ce
l'avevano.

ⓘ **Tre giochi di parole che non passano, e la resa dice il senso**: `:9611`
モロク / モーロク (*Moloch* / «rimbambito»), `:9624` てんとう虫 scritto 天道虫
(«insetto della via del cielo») che regge tutta la frase su 天の道を行く, e
`:12174` 怨念もおんねん, che è 怨念 più il «ce n'è» del Kansai. 🔶 Il quarto,
`:9858`, non si può risolvere qui: la giraffa dice «esiste una bestia fantastica
con lo stesso nome» ed è vero in giapponese (キリンさん e 麒麟), non in italiano
(«la giraffa» e «il Kirin»). **Da guardare a schermo.**

⚠️ **Tre parole che `degrada()` vieta**, tutte trovate da `verifica` in questa
sessione: **dèi**, **élite** e **elite**. L'apostrofo finisce **dentro** la
parola (`de'i`, `e'lite`) e a schermo non si legge. Rese «divinità», «il migliore
fra i migliori», «il fior fiore». ⓘ E la **lineetta lunga** `—` è un carattere a
doppia larghezza in CP932: la boccia `guardie`, non `verifica`.

## `db_item.hsp`, deciso il 2026-08-27 dalla 108ª — la FORMULA del rapporto di identificazione

`description(3)` non è prosa: è il **rapporto di identificazione**, la riga che
chiude la scheda di `com_identify` (`command.hsp:16275`, dentro
`inv(INV_ITEM_KNOWN, ci) >= ITEM_KNOWN_FULL`). Il giapponese la scrive **uguale**
su tutta una categoria e la cambia solo quando cambia il fatto. L'italiano tiene
la forma del referto, perché un referto che dice cose diverse per il tonno e per
la sardina ha smesso di essere un referto.

⚠️ **Il tetto è secco: 69 caratteri degradati.** Nessun impaginatore, nessun
taglio: sfora e basta. La rete è `scratchpad/_107-descrizioni-item.py`, e la
resa più lunga del primo lotto ne misura **65**: il margine è di quattro.

| giapponese | italiano |
|---|---|
| 満腹度を回復することができる食物。 | **Un cibo che sazia.** |
| … 調理することができる。 | **… e che si può cucinare.** |
| … のどに詰まることがある。 | **… Certe volte va di traverso.** |
| 満腹度をわずかに回復する… | **Un cibo che sazia poco.** |
| 満腹度をほんのわずかに回復する… | **Un cibo che sazia appena appena.** |
| 使用することができる（使い捨て） | **Si può usare (usa e getta).** |
| Xの木に成長する種。 | **Un seme che diventa un albero di X.** |
| ⟨erba⟩ …の能力値を上昇させる食物だ。 | **Un'erba che alza ⟨attributi⟩.** |

E le caselle di categoria, che le riempie **l'inglese** perché il giapponese
scrive 食物 per tutte: `seafood` → **un cibo di mare** (copre pesci e molluschi,
dove «frutto di mare» no), `vegetable` → **una verdura**, `fruit` → **un
frutto**, `nuts` → **frutti a guscio**, `egg` → **un uovo**.

### ⭐⭐ Tre difetti di monte riparati, e sette aggiunte taciute

- **`:115655`, la razione: l'inglese dice il CONTRARIO del giapponese.**
  「調理することができる。」 è «si può cucinare», e l'inglese scrive «it cannot
  be cooked». Non è un'aggiunta, è una negazione, e in gioco la razione si cucina.
- **`:80490`, il mochi: l'inglese ha perso una frase intera** —
  「のどに詰まることがある。」 — che la gemella `:80553`, il kagami mochi, ce l'ha
  come «CHOKE WARNING». I due giapponesi sono identici e ora lo sono i due italiani.
- **`:113943`, il filoncino: l'inglese ha perso 「調理することができる。」.**

🔶 **E sette righe dove l'inglese, invece di riempire la casella, racconta**: il
tonno «carnivoro», il salmone «dalle abitudini di deposizione uniche», il pesce
sciabola «che somiglia a un'anguilla», la farina «da forno», la pasta «che
verrebbe meglio cotta», il cadavere «che si può cucinare in piatti di carne», e
il condimento che «qualcuno versa sul bestiame prima della macellazione». Il
giapponese di tutte e sette è la formula generica: si segue lui e si tace
l'aggiunta, per la regola di `decisioni.md` «Quando l'inglese aggiunge un fatto».

ⓘ **I termini che il lotto porta e che erano già decisi altrove:**
「エーテル病」 → «la malattia dell'etere» (`command.hsp:2336`), 「狂気度」 →
«Follia» (`command.hsp:10517`), 「運勢」 → «fortuna» (`skill.hsp:64`),
「生命力」 → «la vita» (`chat.hsp:16738`), 「マナ」 → mana (`invariati.md`).

ⓘ **`:74301`, il pranzo del ringiovanimento**: «ti riporta all'infanzia» e non
«ti fa tornare bambino» — il genere del giocatore non si conosce
(`guida-stile.md`).

### I lotti 002 e 003 — le pozioni, le pergamene e gli atti

La formula regge, e prende la parola che il **giapponese** mette in fondo alla
frase: 「…ポーションだ。」 → «Una pozione che …», 「…飲み物だ。」 → «Una bevanda
che …», 「…巻物だ。」 → «Una pergamena che …», 「…権利書だ。」 → «Un atto: letto,
…».

⚠️⚠️ **E quando il fatto riempie i 69 caratteri, la testa cade e la frase apre
col VERBO.** Sette righe delle pozioni compongono due fatti («alza X e Y, e
resiste a Z e W») e venticinque pergamene aprono in inglese con «It is a scroll
that when read, …», che in italiano costa venti caratteri per ripetere il nome
dell'oggetto. Non è un'eccezione alla formula: è la formula che cede la testa
quando il contenuto la riempie — e infatti 110 righe dell'indice 3 sforano già
in inglese proprio così.

| giapponese | italiano |
|---|---|
| 一時的に… | **… per un po'** (mai «temporaneamente», che ne mangia quindici) |
| 耐性を得る | **resiste a …** / **dà resistenza a …** |
| より強力だ | **È più forte del solito.** |
| 何度でも読むことができる | **Si può rileggere sempre.** |
| 混ぜた物を…する | **Mescolata a una cosa, la …** |

⚠️ **Le stelle non si scrivono.** 「☆のついた武器防具」 (`:81743`) e gli oggetti
col ★ (`:130246`): **`☆` e `★` sono a doppia larghezza in CP932**, li boccia
`guardie`, e nel dizionario non ce n'è nemmeno uno su 23.590 rese. Si scrive
quel che la stella significa — ☆ marca `_quality` 4 e 5, «eccezionale» e
«celestiale»; ★ marca gli **artefatti**.

⭐⭐ **Dieci atti, un solo giapponese, dieci inglesi.** `:45063`-`:45418` e
`:51362`-`:51575` sono i mezzi di trasporto, e il giapponese scrive la stessa
frase per tutti e dieci: 「海マップでの乗り物の権利書だ。」 e
「ワールドマップでの…」. L'inglese ci mette il nome del mezzo, che è **già il
nome dell'oggetto** dieci righe più su nella stessa scheda; la distinzione che
serve è quella che fa il giapponese, mare contro terra, perché dice **dove** il
mezzo si usa. Due rese per dieci firme.

ⓘ **Quattro giapponesi uguali che l'inglese distingue**, e la resa è una:
`:44445`/`:72144` (様々な状態異常, «undesired effects» / «negative status
effects») e `:126010`/`:126081` (HPと状態異常, con «all» solo sulla pozione di
Jure). Li stampa la **rete 13**, ed è il caso per cui esiste.

ⓘ **Tre righe dove il giapponese dice un'altra cosa, e vince lui:** `:90772` la
bottiglia «vuota», che in giapponese è *una bottiglia in cui si può prendere
l'acqua*; `:129442` l'acqua sporca, che **può** far ammalare e non fa ammalare;
`:63387` i dolcetti della strega, che l'inglese chiama «food» e il giapponese
飲み物.

ⓘ **Tre aggiunte dell'inglese taciute:** il «5» dei punti bonus (`:52520`), il
**dove** del Vuoto (`:81402`), il «from sources unknown» della mappa del tesoro
(`:89493`).

ⓘ **I termini nuovi fissati qui:** 友好度 → «la simpatia» (`chat.hsp:25511`),
状態異常 → «gli stati alterati», 巻物 → «pergamena», 権利書 → «atto», 呪い →
«la maledizione», マテリアル → «materiale», スペルボーナス → «punti bonus per
gli incantesimi». `DV`, `PV`, `HP`, `MP` restano **invariati**: il giapponese
scrive le stesse sigle.

## `db_item.hsp`, deciso il 2026-08-27 dalla 109ª — le CODE del rapporto, e la scala della LUCE

I lotti 004 (attrezzi, `FILTER_ITEM_TOOL`) e 005 (mobilio, `FILTER_FURNITURE`)
portano la formula della 108ª su due categorie che non l'avevano vista. La
formula regge; quel che si aggiunge sono le **code fisse**.

### ⚠️ La coda quadrupla: quante volte l'oggetto si usa

Il giapponese chiude quasi ogni rapporto degli attrezzi dicendo **quante volte**
l'oggetto si usa, e sono quattro fatti di gioco distinti — illimitato, cariche
contate, tempo di ricarica, una volta sola:

| giapponese | italiano |
|---|---|
| 何度でも使用することができる | **Si può usare sempre.** |
| 何度か使用することができる | **Si può usare più volte.** |
| 定期的に使用することができる | **Si può usare ogni tanto.** |
| 使用することができる（使い捨て） | **Si usa (usa e getta).** (già 108ª) |
| 投げつけて使う（使い捨て） | **Si lancia (usa e getta).** |
| 投げることができる | **Si può lanciare.** |
| 使用することはできない | **Non si può usare.** |
| 装備することはできない | **Non si può equipaggiare.** |
| 所持していると自動で使う | **Si usa da sé se lo porti.** |

⚠️⚠️ **La coda costa fino a 27 caratteri degradati su 69, e dove il fatto di
testa non ci sta nei quaranta che restano il MODALE cade**: «Si usa sempre», «Si
usa ogni tanto», «Si usa più volte». Non è una seconda formula, è la stessa che
si stringe — la 108ª faceva già cadere la testa «Una pergamena che …» quando il
contenuto la riempiva.

### ⭐ La scala della LUCE, cinque scalini, e in italiano si legge in ordine

Il giapponese grada l'illuminazione con avverbi che tradotti uno per uno danno
italiano illeggibile («illumina un po' debolmente»). La resa usa un **nome con
un aggettivo**, così l'ordine è visibile a colpo d'occhio:

| giapponese | italiano |
|---|---|
| 常に周囲を照らす。 | **Illumina sempre intorno.** (già 108ª, il falò) |
| 常に周囲を明るく照らす。 | **Illumina sempre di luce viva.** |
| 夜間、周囲を弱く照らす。 | **Di notte fa una luce fioca.** |
| 夜間、周囲をやや弱く照らす。 | **Di notte fa una luce un po' fioca.** |
| 夜間、周囲をやや明るく照らす。 | **Di notte fa una luce abbastanza viva.** |
| 夜間、周囲を明るく照らす。 | **Di notte fa una luce viva.** |

### Le altre formule fisse del mobilio

| giapponese | italiano |
|---|---|
| 座る為の家具。 | **Un mobile per sedersi.** (7 firme) |
| 眠る為の家具（ランクN）。 | **Un letto (rango N).** |
| 演奏用の道具。 | **Uno strumento per suonare.** (4 firme) |
| 観賞用の鉢植えだ。 | **Una pianta ornamentale in vaso.** |
| 観賞用の植物だ。 | **Una pianta ornamentale.** |
| その身を映す鏡。 | **Uno specchio per guardarsi.** |
| とても重い建造物だ。 | **Una costruzione molto pesante.** (7 firme, le tombe) |
| 本類を100種類まで入れることができる。 | **Ci stanno fino a 100 tipi di libri.** |
| 使用することでランクNまでの料理を… | **Ci si cucinano i piatti fino al rango N.** |

### ⭐ Il termine che NON aveva una voce, e adesso ce l'ha

| giapponese | inglese | italiano | dove |
|---|---|---|---|
| ペット | pet | **il compagno** | `:81133` la frusta del domatore, `:85301` la macchina genetica. ⚠️ Il dizionario lo rendeva **dieci volte «animale» e dodici «compagno»**, senza una voce che arbitrasse. Vince «compagno» perché in Elona+ un ペット **può benissimo essere umano**, e «animale» sarebbe falso su metà dei casi; 仲間 è reso «compagno» anche lui, e nessuna riga del gioco mette i due in contrasto |

### ⓘ I termini che i due lotti portano, tutti già decisi altrove

労働エナジー → «energia da lavoro» · フィート → «talento» · ゲージ → «barra» ·
はく製 → «statuetta» · ショウルーム → «sala d'esposizione» ·
クラムベリー → «crimberry» · 生きている武器 → «arma vivente» ·
アーティファクト → «artefatto» · 補正 → «modificatore» · ランク → «rango» ·
職業 → «classe» · 種族 → «razza» · 部位 → «parte del corpo» ·
鍵開け → «scasso» · 発言力 → «autorità» · 名声 → «fama» · スキル → «abilità» ·
技能 → «capacità» · 狂気度 → «Follia» · 素材 → «materiale» · 栓 → «tappo» ·
矢弾 → «munizioni» · 味方/仲間 → «compagni» · 魔導船 → «nave magica» ·
ガシャポンの玉 → «sfera del tesoro» · 狂戦士 → «berserker» ·
主能力 → «attributi base» · おひねり → «mance» · 友好度 → «la simpatia» ·
木の実 → «frutti a guscio» · `<Little Sister>` invariato ·
`AP`, `HP`, `MP`, `DV`, `PV`, `SP` invariati.

⚠️ **Una parola vietata, e non dalla lunghezza.** `:89215` chiedeva *gli dèi
stranieri*, e **«dèi» porta l'accento in mezzo alla parola**: a schermo diventa
«de'i». È la lezione della 41ª, misurata sul dizionario nella 71ª. Si evita la
parola — «le divinità straniere» — non si toglie l'accento.

## `db_item.hsp`, deciso il 2026-08-27 dalla 110ª — le code che c'erano già, e il codice come fonte

Cinque lotti — scarti, minerali, libri, bacchette, contenitori: **207 righe del
sorgente, 173 firme**. La formula della 108ª e le code della 109ª hanno retto su
tutte e cinque le categorie senza doversi allargare. Quel che si aggiunge sono
**tre code nuove** e una fonte che finora non era stata usata.

### Le code nuove, e quelle che erano già nel dizionario

| giapponese | italiano | dove stava |
|---|---|---|
| 開けることができる | **Si può aprire.** | nuova (20 contenitori) |
| 読むことができる | **Si può leggere.** | **c'era già** (108ª, la mappa del continente) |
| 何度でも読むことができる | **Si può rileggere sempre.** | **c'era già** (108ª, i dieci atti) |
| 振ることで… | **Una bacchetta che, agitata, …** | il verbo **c'era già**: 「を振った。」 → «Hai agitato …» |
| 模造品だ。 | **Una riproduzione.** | **c'era già** in `db_item.hsp` |
| 合成用のアイテムだ。 | **Un oggetto per la sintesi.** | **c'era già** (`chat.hsp`, 「合成用アイテムを持ってきた」) |

⭐⭐ **Cinque righe su sei di questa tabella non sono decisioni: sono ritrovamenti.**
La parte cara del lavoro dell'indice 3 non è scegliere la resa — è ricordarsi di
cercare se qualcuno l'ha già scelta, e cercarla dove **il giocatore la legge**
(il messaggio dell'azione, il nome dell'oggetto), non solo nel glossario.

### ⭐⭐ Il CODICE è una fonte, e due volte ha battuto tutt'e due i testi

- **`:59793`, l'ohuda: cancella UN potenziamento.** 「バフを消去する御札だ。」 non
  dice il numero, l'inglese dice «erases buffs» al plurale, e l'italiano **deve**
  scegliere. `action.hsp:752-766` scorre i potenziamenti, chiama `delbuff` sul
  primo che trova e poi `break`: **uno solo**. Senza leggere il codice si sarebbe
  seguito l'inglese, che qui è la fonte peggiore delle tre.
- **`:63586`, 「態勢を崩す」 è la ROTTURA GUARDIA.** L'inglese dice
  «disorientates opponent», che non è un termine e non aggancia niente.
  `action.hsp:745` chiama `chara_guardbreak tc, 15`: è il meccanismo, e il
  dizionario ha già la parola — «Rottura guardia» (`command.hsp`), «Abbassa la
  rottura guardia». ⭐ Lo stesso termine torna a `:47152`, il fischietto, dove il
  giapponese lo scrive per esteso (「ガードブレイクゲージ」): due righe lontane
  che ora dicono la stessa cosa con la stessa parola.

⚠️ **Nessuna rete poteva vedere né l'una né l'altra**, e non per una svista: le
reti guardano la forma della resa, l'inglese di monte e il dizionario. Qui la
fonte era il **comportamento del gioco**, che nessuno strumento del progetto
legge.

### ⚠️ Quando il modale cade per tenere insieme una FAMIGLIA, non per stare nel tetto

La 109ª aveva stabilito che il modale cade quando il fatto riempie i 69
caratteri («Si usa sempre» invece di «Si può usare sempre»). Il lotto dei libri
aggiunge il caso in cui cade **anche dove ci starebbe**:

sette libri hanno lo stesso giapponese di coda, 「読むことができる。」. Due —
la sorella cane maggiore e la sorella gatta minore, i nomi più lunghi del gioco —
arrivavano a **71 e 70** su 69 e il modale doveva cadere per forza. Farlo cadere
**solo lì** avrebbe dato due code diverse dentro una famiglia sola, cioè il
difetto che la formula esiste per impedire. Cadono tutte e sette: «Si legge.».

ⓘ Fuori dalla famiglia il modale resta («Si può leggere.», `:71103`, `:83700`,
`:84236`): lì non c'è nessuna famiglia da tenere insieme.

### ⓘ «Un compagno» anche quando la figura è femminile

Cinque dei sette libri qui sopra fanno di una **donna** un compagno — la sorella
maggiore, la sorella cane maggiore, la signorina, la sorella gatta minore, la
sorella minore — e «fa della signorina **una compagna**» sarebbe italiano più
liscio. Resta **«un compagno»** per tutte e sette: qui la parola non è un
aggettivo che concorda, è il **nome della categoria di gioco** — ペット, reso
«compagno» dalla 109ª.

### ⓘ Un participio che non poteva concordare col giocatore

`:66012`, la magaqua: 「所持していると濡れ状態になる勾玉だ。」. «ti tiene
**bagnato**» concorda col genere del giocatore, che non si conosce
(`guida-stile.md`, e la rete dei participi di `referti.py`). Reso con
l'impersonale: «portandola addosso, **ci si bagna**».

### ⓘ Le righe dove l'inglese racconta e il giapponese no — altre sei

Regola di `decisioni.md`, «Quando l'inglese aggiunge un fatto»:

| riga | il giapponese | quel che l'inglese aggiunge |
|---|---|---|
| `:48738` | 「死にかけのセミだ。」, *una cicala moribonda* | che spaventa chi colpisci — e il nome è già «cicala morente» |
| `:116668` | dentro c'è qualcosa | una citazione di Laozi, «the empty space which makes the bowl useful» |
| `:46013` | solo la coda, 「何度でも使用することができる。」 | «Worth less than you think» |
| `:82613` | il foglio **non fa niente** | a chi vengono dati i biglietti |
| `:112199`, `:112261` | 「金品が入った袋/カバン。」 | che sono stati persi **da un turista** |

### ⭐ Un giapponese, più inglesi, una resa — la quarta e la quinta volta

`:115137`/`:115261` (un giapponese, «container containing money and goods» e
«ancient jeweled chest») e le **dodici gemme dei mesi** `:48808`-`:49508` (un
giapponese, 「贈り物に適した宝石だ。」, per granato, ametista, acquamarina,
diamante, smeraldo, alessandrite, rubino, sardonice, zaffiro, opale, topazio e
lapislazzuli).

⭐ **Che si ripeta cinque volte in tre sessioni non è un caso**: il giapponese di
`db_item.hsp` descrive **la classe**, l'inglese descrive **l'esemplare**, e il
nome dell'oggetto sta dieci righe sopra a dire già qual è l'esemplare.

### ⚠️ Due righe dell'indice 3 hanno il giapponese VUOTO

`:89761`, l'esca (lotto 006) e `:129513`, il libro bacato (lotto 008). Sulla
seconda l'inglese è per giunta una **nota per chi programma** — «generated when
failed to create an item» — ma `description(3)` si vede quando l'oggetto è
identificato a fondo, e l'oggetto esiste: la riga si rende com'è.

ⓘ **Ed è per la prima che `_coerenza.py` è stato riparato**: la stringa vuota non
è un giapponese, e raggruppava trenta voci che di comune hanno solo il non avere
una fonte. Vedi `avanzamento.md`.

### ⓘ I termini fissati o ritrovati in questi cinque lotti

ガードブレイク → «rottura guardia» · 主従度 → «grado di sottomissione» ·
バフ → «potenziamento» · 支配 → «dominare» · 合成用アイテム → «oggetti per la
sintesi» · 勾玉 → «perla ricurva» (`invariati.md`) · ラムネ → «gazzosa» ·
電撃 → «fulmine» · 疫 → «pestilenza» · 学習書 → «libro di studio» ·
戦術指示 → «ordini tattici» · 士気 → «morale» · 調教 → «addestrare» ·
プラチナ → «platino» · 潜在能力 → «potenziale» · 深淵 → «Abisso» ·
執事 → «il maggiordomo» · 姉犬 → «la sorella cane maggiore» ·
妹猫 → «la sorella gatta minore» · お嬢様 → «la signorina» ·
宝石 → «gemma» · メダル → «medaglietta» · 模造品 → «riproduzione» ·
武具 → «armi e armature» · 金品 → «denaro e beni» · 請求書 → «fattura» ·
マテリアル → «materiali da lavorazione» · 振る → «agitare» ·
沈黙 → «silenzio» · 加速 → «Accelerazione» · 鈍足 → «Rallentamento» ·
蜘蛛の巣 → «ragnatela».

ⓘ **`子宝` non era nel dizionario, e l'ha deciso `description(0)`.** `:66326`,
l'E.G.G, dice 「子宝だ。」 in due caratteri; la descrizione lunga dello stesso
oggetto (`db_item.hsp:66317`) dice che è la capsula che la cicogna porta **agli
sposi**. È la benedizione dei figli, non un tesoro qualunque, e la categoria
giapponese ＜秘宝＞ non bastava a dirlo. Reso «Il dono dei figli.».

⚠️ **Una divergenza di monte che resta aperta:** 合成 è reso «sintesi» in
`chat.hsp` (「合成用アイテム」) e «fusione» in 「合成の壺」, il vaso. Qui si è
seguita la voce più vicina — la stessa frase, 合成用アイテム — ma nessuno
strumento confronta le due, e vale la lezione della famiglia `dardo`/`Saetta`:
una regola scritta e non sorvegliata vale finché qualcuno se la ricorda.

## `db_item.hsp`, deciso il 2026-08-27 dalla 110ª (seguito) — le tre categorie grosse

Tre lotti ancora — grimori, armi da mischia, armi a distanza: **243 righe, 242
firme**. Sono le tre categorie più grandi rimaste, e sono anche le due facce
opposte dell'indice 3: i grimori hanno **una griglia**, le armi non hanno
**niente**.

### ⚠️⚠️ Il RANGO non si scrive, e qui la prova è enorme

**Ognuno degli 82 inglesi dei grimori apre con «Book of Rank N Magic»**, e il
giapponese non lo dice mai — non su una sola riga. È l'aggiunta dell'inglese più
sistematica trovata in questo file: non una riga qua e là, ma una **colonna
intera**.

Si tace, e vale il controllo della 109ª che trasforma la regola in un argomento:
*questo file, altrove, dice la cosa che l'inglese aggiunge?* Sì —
`db_item.hsp` scrive 「（ランクN）」 quando vuole dirlo, su **tutti** i letti e
su **tutti** i fornelli. Il rango si sa dire; qui l'autore ha scelto di non
dirlo.

ⓘ Ed è la **terza** volta: gli strumenti musicali (109ª), gli 82 grimori, e
`:66843` del lotto delle armi — il pugnale che suona, dove l'inglese precisa
«Rank 0-6 instrument» e il giapponese dice 「一応、楽器としても使える」.

### ⭐ La griglia dei grimori: tre classi per dodici elementi

| giapponese | italiano |
|---|---|
| 〜属性の矢 | **una freccia …** (12 firme) |
| 〜属性のボルト | **una saetta …** (12 firme) |
| 〜属性の範囲魔法呪文 | **una magia ad area …** (12 firme) |

Trentasei righe su 82. In italiano le tre teste sono tutte **femminili** —
freccia, saetta, magia — quindi l'aggettivo dell'elemento è lo stesso in tutt'e
tre le righe della colonna, e la griglia si legge per righe e per colonne.

⭐ I nomi degli elementi vengono da `skill.hsp`, che ha già tutta la famiglia
delle saette (gelo, fuoco, fulmine, d'oscurità, mentale, d'oltretomba, velenosa,
sonora, caotica, dei nervi, magica, d'acqua) — la stessa che la 90ª aveva
riallineato quando `db_item.hsp` diceva «dardo». Le altre due classi si
agganciano lì.

⚠️ **Un'eccezione voluta:** `:84516` è 魔法属性 nella classe ad area, e «una
magia ad area **magica**» si morde la coda. Reso **«arcana»**, che la riga della
90ª dà come sinonimo pieno di 魔法. Sulla saetta e sulla freccia resta «magica»,
perché lì i nomi degli oggetti lo dicono.

### ⚠️ La coda dei grimori c'è o non c'è, e non è una svista da riparare

Cinquantasei righe chiudono con 「読むことができる。」 e ventisei con
「…必要な本だ。」 e basta. Un grimorio si legge sempre: la differenza non è un
fatto di gioco, è come è stato scritto il file. Si segue il giapponese riga per
riga.

⭐ **E il conto torna da solo**: tutte le righe lunghe stanno fra quelle **senza**
coda — i tre grimori degli attributi, le due resistenze abbassate, l'oracolo, la
contingenza — e ci stanno nei 69 proprio perché non portano i diciassette
caratteri di «Si può leggere.». Aggiungere la coda «per uniformità» avrebbe
sfondato il tetto su almeno sei righe.

### ⭐⭐ Le armi: il vocabolario non si è dovuto inventare

`FILTER_WEAPON` è **105 righe, 105 firme, 105 giapponesi distinti** — zero
doppioni, zero famiglie, zero formule, la categoria meno formulaica dell'indice
3. Ogni riga dice **che arma è** e **una cosa sola** su di lei.

Le trentatré parole di tipo d'arma c'erano **tutte** nei nomi degli oggetti,
resi in sessioni precedenti:

    長剣 spada lunga · 短剣 pugnale · 大剣 spadone · 細剣 fioretto · 刀 katana
    忍刀 wakizashi · 海賊刀 scimitarra · 大斧 ascia lunga · 戦斧 ascia da
    battaglia · 手斧 accetta · 投斧 tomahawk · 鎌 falcetto · 大鎌 falce ·
    骨鎌 falce d'ossa · 鎖鎌 falce a catena · 鋏鎌 cesoie · 長槍 lancia ·
    鉾槍 alabarda · 三叉槍 tridente · 騎士槍 lancia da cavaliere ·
    棍棒 randello · 大槌 martello · 戦槌 martello da guerra ·
    星球槌 mazza ferrata · 杖 bastone · 長棒 bastone lungo · 錫杖 shakujo ·
    節棍 nunchaku · 鞭 frusta · 螺旋機 trapano · 鎖鋸 motosega ·
    包丁 coltello da cucina · 苦無 kunai

E per le armi a distanza: 弩/クロスボウ «balestra», 弩砲 «balista», 連弩 «arco a
ripetizione», 短弓 «arco corto», 長弓 «arco lungo», 機械弓 «arco meccanico»,
銃器 «arma da fuoco», 拳銃 «pistola», 双銃 «pistole gemelle», 狙撃銃 «fucile di
precisione», 散弾銃 «fucile a pompa», 機関銃 «mitragliatrice», 光子銃 «pistola
laser», 手榴弾 «granata», 投擲用武器 «arma da lancio».

⚠️ **E il tipo d'arma va letto nel giapponese, non nel nome.** `:52720` è un
budino di mandorle a forma di spada laser, e il giapponese dice
「長剣として装備可能」: si impugna come **spada lunga**. `:67533` è un 大太刀 e
il giapponese avverte che 「刀だが大剣に属する」 — *è un katana, ma sta fra gli
spadoni*. Due righe dove la categoria di gioco e la forma non coincidono, e il
giapponese lo dice apposta.

### ⭐ Le sette armi degli dèi, e nessuna ha avuto bisogno di una decisione

Cinque nel lotto delle armi (「〜の神から下賜される〜だ。」) e due in quello a
distanza. I nomi delle divinità stanno **nello stesso file**, dalle statue, dai
pendoli, dai dipinti e dai peluche resi prima:

| giapponese | italiano | dove |
|---|---|---|
| 大地の神 | **il dio della terra** | 「大地の神を模したペンデュラム」 |
| 収穫の神 | **il dio del raccolto** | 「収穫の神のぬいぐるみ」 |
| 元素の神 | **il dio degli elementi** | 「元素の神を模した胸像」 |
| 幸運の女神 | **la dea della fortuna** | 「幸運の女神を描いた絵」 |
| 癒しの女神 | **la dea della guarigione** | 「癒しの女神を模った彫像」 |
| 機械の神 | **il dio delle macchine** | 「機械の神を模した目覚まし時計」 |
| 風の神 | **la dea del vento** | 「風の女神を模った彫像」 ⚠️ vedi sotto |

⚠️ **Non sono gli epiteti.** Il dizionario ha anche «Jure della Cura», «Ehekatl
della Sorte», «Kumiromi della Messe»: quelli sono **nomi**, e si usano dove il
giapponese scrive il nome. Qui il giapponese scrive la **perifrasi**, e la
perifrasi ha già la sua resa nello stesso file. Confondere le due avrebbe fatto
dire alla scheda «donata da Jure della Cura» dove il giapponese non nomina Jure.

⚠️ **E `:86070`, 風の神, è una dea.** Il giapponese scrive 神, che non ha genere;
l'italiano il genere lo deve scegliere, e lo sceglie come lo ha già scelto
questo file per 風の女神 — «la dea del vento». Lulwy è femminile e l'inglese qui
è d'accordo.

### ⭐ La scala della gittata, quattro scalini e una parola sola

Il giapponese grada quanto un'arma da fuoco perde con la distanza usando sempre
**減衰**, *il calo*, e cambiando l'avverbio:

| giapponese | italiano |
|---|---|
| 遠距離でも安定した威力 | **tiene la forza anche a distanza** |
| 距離による減衰が殆どない | **con la distanza non cala quasi** |
| 距離による減衰が少ない | **con la distanza cala poco** |
| 距離によって威力が減衰する | **con la distanza perde forza** |

Stessa mossa della scala della luce della 109ª, e per la stessa ragione: quattro
righe che il giocatore legge in schede diverse e che devono restare
confrontabili. ⓘ `:97806` (有効射程が短い) **non** è della scala — parla della
gittata utile, non del calo — e infatti dice un'altra cosa.

### ⚠️ Due mitragliatrici, due modi di dire «molto pesante»

`:77148` è 非常に重い, `:77916` è とても重い. Due giapponesi distinti, due rese:
**«pesantissima»** e **«molto pesante»**. Renderle uguali sarebbe stato più
liscio e avrebbe cancellato una differenza che il sorgente scrive. La rete 13 lo
segnala perché l'inglese è identico, ed è il caso per cui esiste.

⚠️ **E il contrario vale altrettanto**: `:68185` e `:117188` hanno lo *stesso*
giapponese e due inglesi diversi («Difficult to use. Hurt as hell when hit.»
contro «It is just a stone.»). Stessa resa. E `:72354`, `:74238`, `:83345` sono
**tre** righe con un giapponese solo.

### ⓘ Le altre righe dove l'inglese aggiunge e il giapponese no

`:105304` la luce sacra (il giapponese dice 自らの, *a sé stessi*; l'inglese dice
«from nearby people» — e la gemella `:105231` è d'accordo col giapponese) ·
`:53911` la spada leggerissima («with electric properties») · `:117463` il
pugnale del tuono («wind and lightning» per il solo 雷).

### ⓘ Una riga che non è un libro

`:78730`, la ricetta: è 「紙」, e non si legge — si **usa** e si consuma. È
l'unica delle 82 del lotto dei grimori con la coda della 108ª invece di quella
dei libri, e l'unica che non parla di una magia.

### ⓘ I termini nuovi di questi tre lotti

クリティカル → «colpi critici» (`buff.hsp`) · 潜在能力 → «potenziale» ·
シーナ → «Shena» · 投げ銭 → «mance» (come おひねり, 109ª) ·
主能力 → «attributi base» (109ª) · マナ → «mana» (`invariati.md`) ·
★ → «artefatti» (108ª: le stelle non si scrivono, si scrive quel che
significano). Le sei sigle degli attributi — Cos, Car, For, Des, Per, Vol — e le
cinque parole degli stati — paralisi, cecità, terrore, confusione, sonno —
vengono dalle **righe di potenziamento degli stessi tre incantesimi**, che il
dizionario ha già: la scheda dell'oggetto e la barra dello stato adesso dicono
le stesse parole.

## `db_item.hsp`, deciso il 2026-08-27 dalla 111ª — l'EQUIPAGGIAMENTO, e l'indice 3 si chiude

Dodici lotti, 169 firme, 176 righe: scudi, armature, merci da commercio, elmi,
amuleti, alberi, anelli, mantelli, guanti, cinture, calzature e la coda. Con
questi il rapporto di identificazione è **1.319 su 1.319**.

### ⭐ Le parole dell'equipaggiamento, e i nomi che le avevano già decise

Quasi tutto il vocabolario di questi lotti era **già a schermo**, nei nomi degli
oggetti resi in sessioni precedenti. Qui sta scritto solo per poterlo cercare.

| il giapponese | la resa | dove stava già |
|---|---|---|
| 盾 | scudo | i nomi: 小盾 «scudo piccolo», 長盾 «scudo a mandorla», 重層盾 «scudo a torre» |
| 鉤爪 | artiglio, artigli | il nome dell'oggetto comune |
| トンファー | tonfa | `invariati.md`: è il prestito corrente |
| 鎧 | corazza | i nomi: 軽鎧, 輪鎧, 重層鎧, 厚鎧 |
| アーマー | armatura | ⚠️ il **katakana**, tenuto distinto da 鎧 |
| 防具 | armatura | la voce generica |
| 服 | vestito | 衣服 era già «vestiti» (i vestiti sporchi nel cesto) |
| スーツ | tuta | il nome non identificato «tuta blu» |
| 兜 | elmo | i nomi: 合金兜, 騎士兜, 重兜 |
| 帽子 | cappello | i nomi: 羽帽子 «cappello piumato», 魔法帽 «cappello magico» |
| ヘルメット | casco | ⚠️ il **katakana**, tenuto distinto da 兜 |
| ウィッグ | parrucca | i nomi non identificati |
| 首輪 | collana | la voce generica del dizionario. ⚠️ **Ma in 《暴風の首輪》 è «collare»**: la parola segue il NOME dell'oggetto, che il giocatore legge in cima al pannello (122ª) |
| 装身具 | ornamento | 122ª, dal corpo delle collane. È l'oggetto che si porta addosso, e nel corpo sta dove l'indice 3 usa 首輪 |
| 宝飾品 | gioiello | 122ª. In `:99519` sta nella stessa frase di 装身具, e la distinzione è tutto il senso della riga |
| 指輪 | anello | la voce generica |
| 外套 | mantello | i nomi: 防護外套 «mantello corazzato», 軽外套 «mantello leggero» |
| 篭手 | guanti d'arme | i nomi: 合成篭手, 重層篭手, 厚篭手 |
| 手袋 | guanti | la voce, più 軽手袋 «guanti leggeri» |
| 腕装備 | bracciale | ⓘ è un'altra parola da 篭手, e resta un'altra parola |
| 腰当 / ベルト | cintura | la voce 腰当 → «cintura», più tutti i nomi |
| 靴 | scarpe | ⓘ una parola sola per sei oggetti, di cui tre «stivali» nel nome |
| 樹木 | albero | la voce del dizionario |
| モミの木 | abete | 「小さなモミの木だ」 → «Un piccolo abete» |
| 交易品 | merce da commercio | la voce, **e** il manuale |
| 生物 | creatura | la parola del progetto |

### ⭐ I termini nuovi, e da dove vengono

出血 → **«sanguinamento»**, che è l'etichetta di stato di `command.hsp:1888` ·
光子 → **«laser»** (110ª, la pistola) · 黒曜石 → **«ossidiana»** (dal
`Black Mirror` «Specchio d'ossidiana») · 推進装置 → **«propulsore»** ·
連続攻撃 → **«raffica di colpi»** (il messaggio d'attacco) · 軽装備 →
**«armatura leggera»** · 追加打撃 / 追加射撃 → **«attacco extra in mischia / a
distanza»** (le righe di potenziamento) · 魔力 → **«potere magico»** · 友好度 →
**«simpatia»** · 運勢 → **«fortuna»** · 貫通 → **«perforare»** · 見えない者 →
**«chi non si vede»** (110ª) · 異星人 → **«extraterrestre»** · 魔法使い →
**«mago»** · 浮遊 → **«levitare»** · エーテルの嵐 → **«vento di etere»** (dal
già reso エーテルの風) · トレイナー → **«istruttore»** · 捧げ物 → **«offerte»** ·
デッキ → **«mazzo»** · 海藻 → **«alga»** · 絶器 → **«zekki»**, invariato
(vedi `invariati.md`).

### ⭐ Le scale, che attraversano più categorie e vanno lette insieme

**Il peso**, fissato dalla 110ª sulle due mitragliatrici e adesso valido su
cinque categorie:

    非常に重い  -> pesantissimo/a     (scudo, corazza, guanti d'arme)
    とても重い  -> molto pesante      (le merci da commercio)
    重い        -> pesante            (le merci, le scarpe)
    重量がある  -> di un certo peso   (l'elmo — ⚠️ è un'altra espressione)

**La durezza**, sulle stesse categorie: 固い → «duro/a», 分厚い → «spesso/a»
(era già «spesso» nel dizionario, dal 分厚い魔法書 «libro spesso»).

**Il viaggio**, due scalini nelle calzature: 旅の歩みを早める → «che fanno
viaggiare più svelti», 旅の歩みを非常にはやめる → «... molto più svelti».

### ⭐ Le formule, che si scrivono in fila o non si leggono come formule

    〜ために作られた服だ     tre righe, le armature del corpo
    〜を束ねて作った鎧だ     due righe (束ねて era già «legando insieme»)
    〜のこめられた首輪だ     due righe (想い «un sentimento», 魔力 «il potere magico»)
    〜のついた〜だ           tre righe in tre lotti, tutte con «con»
    〜を守る為の防具だ       quattro righe in quattro lotti: testa, corpo, fianchi, piedi
    〜と共に装備する武器だ   quattro righe, le munizioni
    生物の〜だ               cinque righe, i resti di creatura
    身に着けると変形して〜になる  **otto** righe in otto categorie (vedi `decisioni.md`)

### ⚠️ Due parole che il giapponese distingue e l'italiano no

- 用 / 向け / のため — tre modi di dire «per», e in italiano sono tutti «per»
  (騎士用の兜, 妖精向けの帽子, 魔法使いのための帽子, e i due del lotto 014).
- 腰当 / ベルト — il kanji e il katakana della cintura. La distinzione
  kanji/katakana regge negli altri tre casi perché l'italiano ce l'ha **già**
  nei nomi resi; qui no, e non si inventa.

### ⓘ Dove la descrizione NON ripete il nome

枯れた樹木だ diventa «Un albero secco» e non «Un albero morto», che è il nome
dell'oggetto; 葉の無い樹木だ diventa «Un albero senza foglie» e non «spoglio».
Il nome sta una riga sopra nella stessa scheda, e una descrizione che lo ripete
non dice niente.

## `db_item.hsp`, deciso il 2026-09-01 dalla 118ª — il CORPO dei GRIMORI

Due lotti, 92 righe, e `FILTER_ITEM_SPELLBOOK` si chiude. Ottanta delle 92
portano la stessa formula, che è la più grande del corpo:

    「「X」という呪文について学ぶことができる魔法書。〜なあなたに。」
    Un grimorio su cui studiare l'incantesimo X. Per te che ...

### ⭐⭐⭐ X è il nome dell'INCANTESIMO, e lo dà il codice

Il nome della magia si prende da `skillname()` di `skill.hsp`, **non** dal nome
del libro. Il percorso è nel codice, e non si fa a occhio:
`scratchpad/lotti-113/_incantesimo.py NNN` va dal blocco `if ( dbid == ... )`
all'`efid = SKILL_SPELL_...` del ramo `DBMODE_ON_READ`, e da lì allo
`skillname`. Su 80 righe su 80 risolve un nome già reso.

**Perché**: quella riga serve al giocatore per **cercare la magia nella lista**.
Col nome del libro non la troverebbe.

⚠️⚠️ **E in italiano le due cose divergono su 37 grimori su 80.** Misurate da
`scratchpad/_118-nomi-vs-incantesimi.py`, che le separa in due specie:

| | | divergenti |
|---|---|---|
| il giapponese | nome del libro contro `skillname` | **2** su 80 |
| l'italiano | nome dell'oggetto contro `skillname` | **37** su 80 |

Le due di monte sono `:91976` (扉生成 contro ドア生成) e `:102031` (自己変容
contro 自己の変容). **Le altre 35 sono nostre**: i nomi degli oggetti e i nomi
degli incantesimi sono stati resi in sessioni diverse, e nessuno strumento del
progetto confronta le due tabelle. «cartografia magica» insegna *Mappa magica*,
«mani guaritrici» insegna *Tocco curativo*, «gemma» insegna *Pietra
protettrice*. In giapponese il giocatore legge la stessa parola in testa al
pannello e dentro la descrizione; in italiano, 37 volte su 80, ne legge due.
Il rimedio è allineare i **nomi** allo `skillname`, ed è un lavoro suo.

### ⭐⭐ La dedica in seconda persona: «Per te che ...»

「〜なあなたに。」 è una dedica da quarta di copertina, rivolta a **te** che
leggi. L'inglese la gira in terza persona **tutte e 80 le volte** — «For those
who...», «For sadists», «Designed for lazy hoarders» — e otto volte butta la
dedica e ne scrive una sua sul libro invece che sul lettore. In italiano resta
«Per te che...», che è la forma del risvolto di copertina.

### ⚠️⚠️⚠️ E il RANGO era detto: la premessa della 110ª era falsa

La sezione della 110ª qui sopra dice, degli 82 inglesi dell'indice 3: «il
giapponese non lo dice mai — non su una sola riga [...] Il rango si sa dire; qui
l'autore ha scelto di non dirlo». **Non è vero.** Cercato 「ランク…魔法」 su ogni
`description()` di `db_item.hsp`, il tassello del rango è su **80 righe**, una
per ogni grimorio, in `description(1)` del ramo `if ( jp )`.

    JP   description(1)   <ランク6魔法>            80 su 80
    EN   description(3)   Book of Rank 6 Magic.    82 su 82
    IT   da nessuna parte                          (la decisione della 110ª)

Non si erano mai viste perché su **76** di quelle 80 l'inglese lascia
`description(1) = ""`, e una riga con l'inglese vuoto non entra
nell'estrazione. Le quattro vive — `:113099`, `:113172`, `:113245`, `:113460` —
sono in questo lotto, e lì l'inglese ci mette una battuta al posto del rango.

Oggi il giocatore italiano è **l'unico dei tre** che il rango non lo legge. La
decisione va riaperta; non la riapre questo lotto, perché l'indice 3 è chiuso a
1.319 su 1.319 col tetto **secco a 69**, e la sezione della 110ª nota che quelle
righe ci stanno dentro proprio perché non portano parole in più.

### ⓘ I termini nuovi di questi due lotti

パワーストーン → **«i cristalli e il loro potere»** (l'inglese conferma:
«Healing Crystals») · 水芸 → **«i giochi d'acqua»**, il prestigio da
palcoscenico, non la navigazione dell'inglese · 毒々しい → **«dai colori
velenosi»**, non «tossico» · 流し眼 → **«sguardo di sottecchi»** · 冷え症 →
**«patire il freddo»**, e 寒がり → **«soffrire il freddo»**, che sono due cose
diverse · 死神 → **«la Morte»** (era già nella riga del patto di `buff.hsp`) ·
高位の存在 → **«esseri superiori»** · tome → **«tomo»** (era già nella tabella
dei titoli-fonte).

⭐ E 痺れさせる, che è insieme intorpidire e far restare a bocca aperta, è reso
**«folgorare»**, che in italiano è insieme tutt'e due: il gioco di parole si
rifà, non si spiega. È il precedente delle fusioni delle razze.

## `db_item.hsp`, deciso il 2026-09-01 dalla 119ª — il CORPO delle POZIONI e delle PERGAMENE

Quattro lotti (049-052), 154 rese, e due categorie chiuse: `FILTER_ITEM_POTION`
e `FILTER_ITEM_SCROLL`.

### ⭐⭐⭐ La scala della fragilità dei mezzi di mare, quattro gradini

Sei mezzi di mare portano la stessa nota del manuale di viaggio, e in inglese
sono **sei stringhe identiche**. Il giapponese cambia un avverbio, ed è un fatto
di gioco:

| giapponese | italiano | mezzi |
|---|---|---|
| とてつもなく弱い | **debolissima** | la zattera |
| かなり弱い | **parecchio debole** | il peschereccio, la nave pirata |
| 結構弱い | **abbastanza debole** | la nave da crociera |
| 弱い | **debole** | la nave da guerra, il sottomarino |

Vale la regola della scala della gittata (110ª): **quattro gradini, una parola
sola ciascuno, e nessuna perifrasi**, perché una scala si legge solo se le
parole si allineano.

⚠️ Peschereccio e nave pirata hanno lo **stesso** giapponese, e così nave da
guerra e sottomarino: due rese coprono quattro righe. La divisione in gradini è
dell'autore, non nostra.

### ⭐⭐ La scala del potenziamento e del materiale: normale contro superiore

Otto pergamene in due coppie più due, e il giapponese oppone due formule fisse:

| giapponese | italiano |
|---|---|
| 一段階強くなる | **sale di un gradino** |
| 性能の限界を超えて強くなる | **oltre il limite di ciò che X può dare** |
| より強力である為失敗することはない、はずだ | **non fallisce mai. Dovrebbe.** |

⭐ L'ultima è la battuta della riga: はずだ si rimangia la promessa che la frase
ha appena fatto, e l'inglese («never fails to break the curse») la toglie. In
italiano sta in una parola staccata.

### ⓘ Le formule fisse degli atti e dei mezzi

| giapponese | italiano |
|---|---|
| 〜の権利が得られる証書 | **un atto che dà il diritto di …** |
| 〜の所有権を得られる証書 | **un atto che dà la proprietà di …** |
| 権利書を染めることで塗装を指定可能 | **tingendo l'atto si sceglie la vernice** |
| 税金は…最も高価な乗り物で計算される | **le tasse si calcolano sul mezzo più caro che hai usato nel periodo** |
| 勉強代と思って諦めよう | **pazienza: consideralo il prezzo della lezione** |

### ⚠️ 装備品 non è sempre «equipaggiamento»

Il termine resta quello del glossario, ma **dentro la prosa impaginata** con la
preposizione articolata arriva a 19-20 caratteri e l'impaginatore lo spezza. In
cinque righe del lotto 052 è reso **«un oggetto indossato»**, che è la forma già
usata dal rapporto di identificazione di quelle stesse pergamene.

⚠️ E la soglia è un indizio, non un vincolo: nel 051 la stessa parola si è
spezzata a `:81740` e **non** a `:95990`. Conta dove cade il taglio.

### ⓘ I termini che il corpo porta, tutti già decisi altrove

スライム → **la melma** (non «slime») · ハウンド → **il segugio** ·
パラライザー → **il paralizzatore** · パンプキン → **la zucca** ·
ダイオウサソリ → **lo scorpione re** (l'inglese scrive «giant scorpion») ·
死神 → **la Morte**, femminile e maiuscola · ベルム家 → **casa Bellum** ·
ポート・カプール → **Porto Kapul** · ノイエル → **Noyel** ·
ダルフィ → **Derphy** · エウダーナ → **Eulderna** · ネフィア → **Nefia** ·
すくつ → **il Vuoto** (l'inglese scrive «the sanctuary») ·
形見のカバン → **la borsa dei ricordi** · 万能ムギ → **bannou mugi** ·
沈黙の霧 → **Nebbia di silenzio** · 悪夢 → **Incubo** ·
元素の傷 → **Cicatrice elementale** · ホーリーヴェイル → **velo sacro** ·
マテリアル → **materiale** · 労働エナジー → **Energia da Lavoro** ·
スタミナ → gli **SP** · 生命力 → **la vita**.

### ⭐ Una parola che resta traslitterata, e la ragione è nuova

**hidensho** (`:115001`). 秘伝書 scritto in **katakana**: il giapponese si
traslittera da solo, perché la frase dice «in terre lontane e straniere le
chiamavano così» e la terra straniera, vista da Irva, è il Giappone. Regola
della 111ª applicata al verso opposto.

## `db_item.hsp`, deciso il 2026-09-01 dalla 121ª — il CORPO di SCUDI, LIBRI e ARMATURE

Tre lotti (058-060), 67 rese, tre categorie chiuse: `FILTER_SHIELD`,
`FILTER_ITEM_BOOK` e `FILTER_ARMOR`.

### ⭐⭐⭐ I nomi che il giapponese porta e l'inglese scioglie in parole comuni

Cinque volte in tre lotti il giapponese ha nominato qualcosa che il giocatore
italiano **conosce già**, e cinque volte l'inglese l'ha reso come lingua comune.
Sono la ragione per cui `_cerca.py` va lanciato anche sulle parole che non
sembrano nomi.

| giapponese | la resa, e da dove viene | che cosa scrive l'inglese |
|---|---|---|
| 神の間 | **il Sigillo Eterno** — il luogo, quaranta battute rese | «for the gods» (letto come lingua) |
| カイン | **<Caim>** — `<Caim> il riccone folle`, dodici voci | «a mad man named **Cain**» |
| 第三部 | **la parte terza** — `@QM[…]` → «Parte terza - Il patto eterno» | «ACT III» |
| クイーン・セドナ号 | **la <Regina Sedona>** — nave *e* persona | «the Queen Sedona» |
| 開発主任 | **l'ingegnere capo** — è `<Gavela>`, un personaggio | «the chief developer» |

⭐ Più メイルーン → **Mayroon**, テスカトリポカ → **Tezcatlipoca**, 冒険ゼミ →
**Seminario d'Avventura**, 赤剣先生 → **il maestro Spada Rossa**,
レイチェル → **Rachel** (ed è una **donna**: «la scrittrice di favole Rachel»).

### ⭐ I termini nuovi, e da dove vengono

バリアコーティング → **«rivestimento a barriera»** (nasce qui, e nasce già in
tre righe) · 記録媒体 → **«supporto di registrazione»**, il tecnicismo secco con
cui l'enciclopedia parla del libro, ed è la battuta · 斥力シールド →
**«scudo repulsivo»** · 攻防一体 → **«che unisce attacco e difesa»** ·
したためる → **«vergare»** (⚠️ non 書く, che è «scrivere») ·
鎖帷子 → **«cotta di maglia»**, che è il nome dell'oggetto 綴り鎧 ·
甲冑 → **«piastre»** (il nome 重層鎧 è «corazza a piastre») ·
大鎧 → **«grande corazza»** · 秘術 → **«arti segrete»** · 手枷 → **«manette»** ·
猛禽 → **«rapaci»** · インド象 → **«elefante indiano»** · 現代イルヴァ →
**«l'Irva di oggi»** · 潜在値 → **«potenziale»** · 掲示板 → **«bacheca»** ·
シルフ → **«silfidi»** · 研究家 → **«studiosi»** · 童話集 → **«raccolta di
fiabe»** · 法衣 → **«veste»**, 法王衣 → **«veste papale»**.

⚠️ 光子 resta **«laser»** (110ª) anche in 光子刃 → «lama laser», perché
l'indice 3 dello stesso tonfa dice già «lame laser» e i due segmenti stanno
**nello stesso pannello**.

### ⭐⭐ Le formule che si ripetono, e che si scrivono in fila

    攻防一体の装備。              CINQUE righe, i tonfa ST-01..ST-05
    ◯がしたためたとされる日記。    QUATTRO righe, i diari
    ◯の秘密が隠された日記。        DUE righe, sorella maggiore e minore
    服の中に(多数の)素材片を…      DUE righe, e a distinguerle è 多数の
    非常に分厚く作られた◯。        DUE righe, ma in DUE LOTTI (058 e 060)
    特殊な素材を…得た◯。          DUE righe, ma in DUE LOTTI (058 e 060)

⚠️⚠️ Le ultime due attraversano il **confine del lotto**, e nessuno strumento
le accosta: vedi `decisioni.md`, «La riga sorella può stare nel lotto di un'ora
fa».

### ⚠️ Due parole che il giapponese distingue e l'italiano deve distinguere

- 防具 **«armatura»** contro 鎧 **«corazza»**: il glossario della 111ª le teneva
  già separate, e il lotto 060 le mette **nella stessa frase** (`:101639`: «è
  un'armatura che pesa un po' di più, ma sempre meno di una corazza»);
- したためる **«vergare»** contro 書く **«scrivere»**: quattro diari usano il
  primo e uno (`:97200`) il secondo. Appiattirli sarebbe stato cancellare una
  differenza che l'autore ha scritto.

### ⓘ Due divergenze di monte, viste passando e non toccate

- **«Rachael»** in `text.hsp` contro **«Rachel»** altrove — 3 contro 12. Anche
  l'inglese ne ha una sola con la a, quindi è ricopiata da monte;
- **«vento di etere»** in due voci contro **«vento d'etere»** in venticinque.
  La seconda è la forma del progetto.

## Da decidere

*Vuota dal 2026-08-07.* I sei termini che stavano qui — `Gauge`, `Chaos`,
`Abyss`, `Skill`, `Sister`, `Body` — sono decisi e spostati nelle tabelle sopra,
insieme ai cinque toponimi che erano in `invariati.md`.

## Le righe-fonte delle descrizioni di `db_item.hsp` — 112ª

1.509 descrizioni del **corpo** (indici 0-2) finiscono con una riga marcata
da `#`, che `command.hsp:16836`-`:16840` disegna a **destra**, in corsivo,
con un **trattino** davanti: è il titolo del libro da cui la notizia viene.
I titoli distinti sono **224**, e i venti più frequenti coprono il **74%**
delle righe — sono una famiglia chiusa sparsa su tutte le categorie, quindi
su tutti i lotti futuri. La tabella eseguibile sta in
`scratchpad/lotti-112/titoli_fonte.py`; il cancello è
`scratchpad/_112-verifica-fonti.py`.

⚠️⚠️ **Il tetto è 66 caratteri degradati, e non è un tetto di larghezza:**
è la soglia che decide *di che tipo* è la riga (`:16758`). A 67 la fonte
smette di essere una fonte, cade nell'impaginatore e viene disegnata a
sinistra come testo normale. Non rompe niente e non si vede in un conteggio.
La resa più lunga decisa qui ne misura 55.

⚠️⚠️ **La chiave è il giapponese, non l'inglese.** L'inglese di monte
appiattisce: `~Vernis Ore Catalogue~` copre **tre** libri giapponesi diversi,
`~Irva Fantasy Encyclopedia~` ne copre due, `Lead Developer <Dr. Gavela>`
copre due persone, e `~Battles, Dragons, Swords and Magic~` traduce
「巻かれる為の長いもの」, *cose lunghe fatte per essere avvolte*, che non
c'entra niente. Arbitra il giapponese, com'è regola dalla 26ª.

⚠️ **Due titoli il sorgente li scrive con la tilde larga** `～`
(`db_item.hsp:60514` e `:114277`), che sta fra i caratteri proibiti di
`guardie.py`: copiati verbatim fanno bocciare il lotto. La tilde giusta è
quella ASCII.

⚠️ **Le divinità portano in giapponese un epiteto dentro `《》`** che
l'inglese butta via — `《風のルルウィ》` è *Lulwy del vento*. Il progetto
aveva già reso quella forma come `<Lulwy>` (in `db_card.hsp`), e queste
righe le vanno dietro: l'epiteto resta nel giapponese.

### I titoli indicizzati per giapponese (200)

| jp | en | it | righe |
|---|---|---|---|
| ～イルヴァ幻想辞典～ | `~Irva Fantasy Encyclopedia~` | `~Dizionario Fantastico di Irva~` | 236 |
| ～明日から使えるあなたの為の武具集～ | `~Collection of Armaments you can Use Tomorrow~` | `~Raccolta di Armi e Armature da Usare Domani~` | 118 |
| ～移り変わりゆくティリスの食～ | `~Everchanging Food of Tyris~`<br>`~Everchanging Food of Tyris～` ⚠️ | `~Il Cibo Mutevole di Tyris~` | 111 |
| ～ノースティリス大家具事典～ | `~ Great Encyclopedia of North Tyris Furnitures~`<br>`~Great Encyclopedia of North Tyris Furnitures~` ⚠️ | `~Grande Enciclopedia dei Mobili di Tyris del Nord~` | 105 |
| ～魔具全典～ | `~Arcane Alamanac~`<br>`~Arcane Almanac~` ⚠️ | `~Compendio Completo degli Oggetti Magici~` | 93 |
| ～本の為の本・魔法書編～ | `~Big Book of Magical Books~` | `~Il Libro dei Libri: i Grimori~` | 81 |
| ～飲めるのみもの、飲めないのみもの～ | `~Drinks to Drink, Drinks Not to Drink~` | `~Bevande da Bere e Bevande da Non Bere~` | 64 |
| ～ルミエスト美術目録～ | `~Lumiest Art Catalogue~`<br>`~Vernis Ore Catalogue~` ⚠️ | `~Catalogo d'Arte di Lumiest~` | 44 |
| ～ティリス園芸図鑑～ | `~Illustrated Guide to Tyris Horticulture~`<br>`~Tyris Gardening Encyclopedia~` ⚠️ | `~Atlante Illustrato del Giardinaggio di Tyris~` | 39 |
| ～今日から君も冒険者・旅用マニュアル～ | `~ Great Encyclopedia of North Tyris Furnitures~`<br>`~an Adventurer is You! Guide for Travels~` ⚠️ | `~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~` | 28 |
| ～別冊ヨウィン・未知の知識を追え！～ | `~The Yowyn Book of Secrt Knowledge!~` | `~Speciale Yowyn: a Caccia del Sapere Ignoto!~` | 26 |
| ～ヴェルニース鉱物図鑑～ | `~Vernis Ore Catalogue~` | `~Atlante dei Minerali di Vernis~` | 25 |
| ～家庭を彩る日用雑貨～ | `~Daily Necessities for the Home~` | `~Casalinghi che Danno Colore alla Casa~` | 23 |
| ～料理を支える脇役達～ | `~Supporting Roles in Kitchen~` | `~I Comprimari della Cucina~` | 20 |
| ～私の愛する幾千ものガラクタ～ | `~Thousands of pieces of Junk I love~` | `~Le Mille Cianfrusaglie che Amo~` | 18 |
| ～玲瓏たるイルヴァの調べ～ | `~Music of the Melodious Irva~`<br>`~Tunes of Irva~` ⚠️ | `~Le Melodie della Limpida Irva~` | 17 |
| ～エウダーナに学ぶ必勝交易法～ | `~Eulderna's Winning Strategy for Trading~` | `~Il Commercio Vincente Secondo gli Eulderna~` | 17 |
| ～街中の名脇役達～ | `~Supporting Roles on the Streets~` | `~I Grandi Comprimari della Città~` | 15 |
| ～あなたの見知らぬ世界～ | `~ Worlds you've Never Seen~`<br>`~Worlds you've Never Seen~` ⚠️ | `~I Mondi che Non Hai Mai Visto~` | 12 |
| ～遊技大典・全年齢対応版～ | `~Game Tricks, All Ages Version~` | `~Grande Compendio dei Giochi: Per Tutte le Età~` | 11 |
| ～旅用マニュアル注釈～ | `~note for Travelers~` | `~Note al Manuale di Viaggio~` | 10 |
| ～貰って嬉しい贈り物あれこれ～ | `~Gifts that I am Happy to Receive~` | `~Regali che Fa Piacere Ricevere~` | 10 |
| ～死にゆく者へ贈る書～ | `~ Book for the Dying Ones~`<br>`~Book for the Dying Ones~` ⚠️ | `~Libro in Dono a Chi Sta Morendo~` | 10 |
| ～本の為の本～ | `~Big Book of Books~` | `~Il Libro dei Libri~` | 9 |
| ～脱冒険者から始める商いライフ～ | `~Merchant Life Starting from a Quitting as a Adventurer~` | `~Vita da Mercante Dopo l'Avventura~` | 9 |
| ～本の為の本・児童書編～ | `~Big Book of Children's Books~` | `~Il Libro dei Libri: i Libri per Bambini~` | 8 |
| ～ノースティリス紀行・冬版～ | `~North Tyris Travels, Winter Edition~` | `~Viaggio in Tyris del Nord: Inverno~` | 8 |
| ～子供を騙す１００のテクニック・お土産編～ | `~Cheap Gifts for Your Kids~` | `~Cento Modi per Fregare i Bambini: i Souvenir~` | 8 |
| ～打切上等！箱マニア・創刊号～ | `~Censored! Box Mania, First Issue~` | `~Chiudeteci Pure! Box Mania, Numero Uno~` | 7 |
| ～ダルフィ不動産・商品カタログ～ | `~Derphy Real Estate - Catalogue~` | `~Immobiliare Derphy: Catalogo~` | 6 |
| ～パルミア秋冬物コレクション～ | `~Palmian Winter Fashion~` | `~Palmia: Collezione Autunno-Inverno~` | 5 |
| ～病みつきになる煙の味は～ | `~Sickly Taste of Smoke~` | `~Il Sapore del Fumo che Dà Dipendenza~` | 5 |
| ～これからの魔物被害対策～ | `~Future Monster Damage Countermeasures~` | `~Difendersi dai Mostri, da Qui in Avanti~` | 4 |
| ～麻酔の射手の言葉～ | `~words of Expert Marksman~` | `~Parole del Tiratore Anestetista~` | 4 |
| ～熟練狩人の言葉～ | `~words of Expert Huntsman~` | `~Parole del Cacciatore Esperto~` | 4 |
| ～君にも使える！発掘兵器～ | `~You Can Use it too! Excavated Weapons~` | `~Puoi Usarle Anche Tu! Le Armi Riesumate~` | 4 |
| ～奥深い酒の世界～ | `~The Wide World of Alcohol~`<br>`~The Wide World of Alcohol～` ⚠️ | `~Il Mondo Profondo dei Liquori~` | 4 |
| ～バトルホビー列伝～ | `~Battle-Hobby Legend~` | `~Cronache del Battle Hobby~` | 4 |
| ～世界のコイン・ティリス編～ | `~Coins of this World - Tyris Edition~` | `~Le Monete del Mondo: Tyris~` | 4 |
| ～海藻と海草の違い～ | `~Seaweed is not Sea Weed~` | `~Alghe e Piante Marine: la Differenza~` | 3 |
| ～毒も薬も用法・用量～ | `~ Administration of Medicines ~` | `~Veleno o Medicina: Modo e Dose~` | 3 |
| ～不思議な古代装飾品～ | `~Mysterious Ancient Ornaments~` | `~Misteriosi Ornamenti Antichi~` | 3 |
| ～熱き決闘者たち～ | `~Heated Duelists~` | `~Duellanti Ardenti~` | 3 |
| ～巻かれる為の長いもの～ | `~Battles, Dragons, Swords and Magic~` | `~Cose Lunghe Fatte per Essere Avvolte~` | 3 |
| ～嘘と勘違いされる全くの作り話・第２巻～ | `~Totally Made-up Stories that are Mistaken for Lies, Volume 2~` | `~Storie Inventate Scambiate per Bugie, Volume 2~` | 3 |
| ～パルミア春夏物コレクション～ | `~Palmian Summer Fashion~` | `~Palmia: Collezione Primavera-Estate~` | 3 |
| ～より良い業物を目指して～ | `~Aiming for Better Workmanship~` | `~Verso una Lama Migliore~` | 3 |
| ～パルミア広報～ | `~Palmia Public Relations~`<br>`~Palmia Public Services~` ⚠️ | `~Bollettino di Palmia~` | 2 |
| ～選ぼう、大切な人への贈り物～ | `~Gift for your loved ones~` | `~Scegliamo un Dono per Chi ci sta a Cuore~` | 2 |
| ～今日から始める奴隷運用～ | `~ Let's Slavery - Today ~` | `~Gestire uno Schiavo, da Oggi~` | 2 |
| ～ロストテクノロジー、その片鱗～ | `~a Glimpse of Lost Technology~` | `~Tecnologia Perduta: un Barlume~` | 2 |
| ?私の愛する幾千ものガラクタ? | `~Thousands of pieces of Junk I love~` | `~Le Mille Cianfrusaglie che Amo~` | 2 |
| ～叡智の書～ | `~Book of Wisdom~` | `~Il Libro della Sapienza~` | 2 |
| ～ザイール鉱物図鑑～ | `~Vernis Ore Catalogue~`<br>`~Zaile's Book of Mineralogy~` ⚠️ | `~Atlante dei Minerali di Zaile~` | 2 |
| ～ガイドの『ノルン』の言葉～ | `~<Norne> the guide~`<br>`~words of <Norne> the guide~` ⚠️ | `~Parole di <Norne> la guida~` | 2 |
| ～農業、その新たな可能性～ | `~Agriculture and its New Possibilities~` | `~L'Agricoltura e le sue Nuove Possibilità~` | 2 |
| ～家庭でできる応急処置～ | `~First aid at home~` | `~Primo Soccorso in Casa~` | 2 |
| ～イムウエル交易譚～ | `~the Aimwell tale of trade~` | `~Racconti di Commercio di Aimwell~` | 2 |
| ～いいもの選ぼう職人道具～ | `~Choosing the Best Tools for the Best Craftsmen~` | `~Scegliere Bene gli Attrezzi da Artigiano~` | 2 |
| ～税金との付き合い方～ | `~Irva Revenue Services~` | `~Come Andare d'Accordo con le Tasse~` | 2 |
| ～牧畜と暮らす生活～ | `~Living with Livestock~` | `~Vivere Insieme al Bestiame~` | 2 |
| ～ザナンの紅の英雄『ロイター』の言葉～ | `~words of <Loyter> the crimson of Zanan~` | `~Parole di <Loyter> l'eroe cremisi di Zanan~` | 2 |
| ～異形の森の使者『ロミアス』の言葉～ | `~<Lomias> The Messenger From Vindale~`<br>`~<Lomias> the messenger from Vindale~` ⚠️ | `~Parole di <Lomias> il messaggero di Vindale~` | 2 |
| ～釣り自慢のフィッシャーの言葉～ | `~words of a fisherman proud of his catch~` | `~Parole di un Pescatore Fiero della Sua Preda~` | 2 |
| ～本の為の本・歴史書編～ | `~Big Books of Historical Books~` | `~Il Libro dei Libri: i Libri di Storia~` | 2 |
| ～情報屋ウィーゼムの調べた情報～ | `~Intel of the Informant Wiesem~` | `~Le Notizie Raccolte da <Wiesem> l'informatore~` | 2 |
| ～鉄の胃袋を求めて・完食列伝～ | `~Iron Stomach: A Complete Diet~` | `~In Cerca di uno Stomaco di Ferro: Piatti Finiti~` | 2 |
| ～ティリス武具大全、広告のページ～ | `~Tyris Armor Compendium, page of advertisements~` | `~Grande Compendio delle Armi di Tyris: le Reclame~` | 2 |
| ～敗北者のうめき声～ | `~words of the defeated~` | `~Il Gemito dello Sconfitto~` | 1 |
| ～涙目の煽りイカの言葉～ | `~words of a Provocasquid~` | `~Parole del Calamaro Provocatore con gli Occhi Lucidi~` | 1 |
| ～続・明日から使えるあなたの為の武具集～ | `~Collection of Armaments you can Use Tomorrow Cont.~` | `~Ancora Armi e Armature da Usare Domani~` | 1 |
| ～もう化かされない！魔物の罠の見抜き方～ | `~Fool me twice, Shame on me!~` | `~Non ci Casco Più! Come Scoprire i Trucchi dei Mostri~` | 1 |
| ～金毛九尾の言葉～ | `~words of Kyu-Bi~` | `~Parole della Volpe a Nove Code dal Manto d'Oro~` | 1 |
| ～ペットトレイナーの言葉～ | `~words of a Pet Trainer~` | `~Parole dell'Addestratore di Bestie~` | 1 |
| ～訓練所の張り紙～ | `~words at the Training Center ~` | `~Avviso Affisso alla Palestra~` | 1 |
| ～鎖自慢された奴隷の言葉～ | `a Slave showing off his chains.` | `~Parole di uno Schiavo Fiero delle Sue Catene~` | 1 |
| ～拘束器具の歴史～ | `~ History of Bondage ~` | `~Storia degli Strumenti di Costrizione~` | 1 |
| ～機甲将軍『アインリッヒ』の言葉～ | `~<Heinrich> the Armored General~` | `~Parole di <Heinrich> il generale corazzato~` | 1 |
| ～特殊部隊長『ミーリス』の言葉～ | `~<Milis> Captain of the Special Forces~` | `~Parole di <Milis> la comandante delle forze speciali~` | 1 |
| ～サメ信者大全～ | `~Shark Believer Compendium~` | `~Grande Compendio dei Fedeli dello Squalo~` | 1 |
| ～退屈ネクロマンサーの言葉～ | `a Bored Necromancer` | `~Parole di un Negromante Annoiato~` | 1 |
| ?ジュアの狂信者の独り言? | `Monologue of a Jure Fanatic` | `~Monologo di un Fanatico di Jure~` | 1 |
| ～ゴミの山に光るもの～ | `~Thousands of pieces of Junk I love~` | `~Quel che Brilla nel Mucchio dei Rifiuti~` | 1 |
| ～困惑する素人の言葉～ | `a bewildered amateur` | `~Parole di un Profano Disorientato~` | 1 |
| ～解説中のマニアの言葉～ | `angry potio-plug nerd` | `~Parole di un Fissato in Piena Spiegazione~` | 1 |
| ～進め！オカルト探検隊～ | `~Embark! Occultists~` | `~Avanti! Squadra Esploratrice dell'Occulto~` | 1 |
| ～ザナン研究員の言葉～ | `a Zanan Researcher` | `~Parole di un Ricercatore di Zanan~` | 1 |
| ～開発主任『ガベラ』の言葉～ | `Lead Developer <Dr. Gavela>` | `~Parole di <Gavela> l'ingegnere capo~` | 1 |
| ～邪悪な魔法使いの言葉～ | `a Evil Wizard` | `~Parole di un Mago Malvagio~` | 1 |
| ～生化学者『イコール』の言葉～ | `Lead Developer <Dr. Gavela>` | `~Parole di <Icolle> il biochimico~` | 1 |
| ～職人が教える武器の歴史～ | `~Blacksmithing History~` | `~La Storia delle Armi Raccontata da un Artigiano~` | 1 |
| ～姉波動聖典～ | `~Big Sister Energy Waves~` | `~Il Testo Sacro dell'Onda Sororale~` | 1 |
| ～挟まれていた紙片の殴り書き～ | `a Punched-in note` | `~Scarabocchio sul Foglietto Infilato Dentro~` | 1 |
| ～イルヴァ昆虫大百科～ | `~Irva Insect Encyclopedia~` | `~Grande Enciclopedia degli Insetti di Irva~` | 1 |
| ～イルヴァ昆虫大百科注釈～ | `~Irva Insect Encyclopedia (Footnote)~` | `~Grande Enciclopedia degli Insetti di Irva: Note~` | 1 |
| ～無名吟遊詩人の短歌～ | `~Songs of a nameless poet~` | `~Le Liriche di un Bardo Senza Nome~` | 1 |
| ～遺跡荒らしのメモ～ | `~memo of a grave robber~` | `~Appunti di un Predone di Rovine~` | 1 |
| ～遺跡研究者『メローキア』の言葉～ | `~words of <Melochea> the Nefia Researcher~` | `~Parole di <Melochea>, studiosa di rovine~` | 1 |
| ～現場を見た専門家の言葉～ | `~words of an Expert on the Scene~` | `~Parole di un Esperto che ha Visto la Scena~` | 1 |
| ～自称天才魔道具技師の言葉～ | `~words of a Self-proclaimed Genius Grimoire Technician~` | `~Parole di un Sedicente Genio degli Arnesi Magici~` | 1 |
| ～図解・忍者のひみつ１００選～ | `~100 Secret of the Ninja - Illustrated~` | `~Illustrato: Cento Segreti del Ninja~` | 1 |
| ～富の女神の言葉～ | `Words of the Goddess of Wealth` | `~Parole della Dea del Tesoro~` | 1 |
| ～イムウエル幻想辞典～ | `~Irva Fantasy Encyclopedia~` | `~Dizionario Fantastico di Aimwell~` | 1 |
| ～隅に記された魔女の言葉～ | `Witch's words, written in the corner` | `~Parole di una Strega Scritte in un Angolo~` | 1 |
| ～混乱する店員の言葉～ | `~words of a eccentric bandit~` | `~Parole di un Commesso Confuso~` | 1 |
| ～怯える錬金術士の『ナプラス』の言葉～ | `~Identification Report: <Food> Category~` ⚠️ | `~Parole di <Naplus> l'alchimista spaventata~` | 1 |
| ～ソックスソードマンの評価～ | `~words of a sockswordman~` | `~Il Giudizio dello Spadaccino dei Calzini~` | 1 |
| ～君にもできるサバイバル～ | `~Survival that Anyone Can Do~` | `~La Sopravvivenza Alla Portata di Tutti~` | 1 |
| ～危険物取扱マニュアル～ | `~Hazardous Materials Handling Manual~` | `~Manuale per il Maneggio di Materiali Pericolosi~` | 1 |
| ～夢の廃物利用～ | `~Magical Ways of Waste Utilization~` | `~Il Sogno di Riusare gli Scarti~` | 1 |
| ～根元の濡れた標識～ | `~the Whizzard~` | `~Il Cartello Bagnato alla Base~` | 1 |
| ～はく製マニアからの手紙～ | `~words of an Fossil Enthusiast~` | `~Lettera di un Fissato di Tassidermia~` | 1 |
| ～本の為の本・成年誌編～ | `~Big Book of Adult Books~` | `~Il Libro dei Libri: le Riviste per Adulti~` | 1 |
| ～必見！貯蓄型資産運用のすべて～ | `~Must Watch! Everything About Savings and Asset Management~` | `~Da Vedere! Tutto sul Risparmio e sugli Investimenti~` | 1 |
| ～発見！世界の珍品～ | `~Discovery! Curiosities of the World~` | `~Scoperta! Le Rarità del Mondo~` | 1 |
| ～古代道具の謎に迫る！～ | `~Mystery of the Ancient Tools!~` | `~All'Inseguimento del Mistero degli Arnesi Antichi!~` | 1 |
| ～道端の危険物～ | `~Dangers on the Road~` | `~I Pericoli sul Ciglio della Strada~` | 1 |
| ～少女の寝言～ | `~a Little Girl's Bedtime Story~` | `~Le Parole nel Sonno di una Bambina~` | 1 |
| ～添えられた説明書～ | `~attached manual~` | `~Il Foglietto delle Istruzioni Allegato~` | 1 |
| ～ブランケットにくるまった少女の言葉～ | `~words of a girl wrapped in a blanket~` | `~Parole di una Bambina Avvolta in una Coperta~` | 1 |
| ～《剛石のウリカグアル》の言葉～ | `~words of <Urcaguary>~` | `~Parole di <Urcaguary>~` | 1 |
| ～《地のオパートス》の言葉～ | `~words of <Opatos>~` | `~Parole di <Opatos>~` | 1 |
| ～《守護のロヴィト》の言葉～ | `~words of <Rovid>~` | `~Parole di <Rovid>~` | 1 |
| ～《癒しのジュア》の言葉～ | `~words of <Jure>~` | `~Parole di <Jure>~` | 1 |
| ～《砂嵐のラシエル》の言葉～ | `~words of <Arasiel>~` | `~Parole di <Arasiel>~` | 1 |
| ～《風のルルウィ》の言葉～ | `~words of <Lulwy>~` | `~Parole di <Lulwy>~` | 1 |
| ～《機械のマニ》の言葉～ | `~words of <Mani>~` | `~Parole di <Mani>~` | 1 |
| ～《鉄騎のガルジエム》の言葉～ | `~words of <Garziem>~` | `~Parole di <Garziem>~` | 1 |
| ～《富のヤカテクト》の言葉～ | `~words of <Yacatect>~` | `~Parole di <Yacatect>~` | 1 |
| ～《歌踊のカラヴィカ》の言葉～ | `~words of <Karavika>~` | `~Parole di <Karavika>~` | 1 |
| ～《叡智のソピアー》の言葉～ | `~words of <Sophia>~` | `~Parole di <Sophia>~` | 1 |
| ～《元素のイツパロトル》の言葉～ | `~words of <Itzpalt>~` | `~Parole di <Itzpalt>~` | 1 |
| ～《不幸のシナア》の言葉～ | `~words of <Sinaha>~` | `~Parole di <Sinaha>~` | 1 |
| ～《幸運のエヘカトル》の言葉～ | `~words of <Ehekatl>~` | `~Parole di <Ehekatl>~` | 1 |
| ～《収穫のクミロミ》の言葉～ | `~words of <Kumiromi>~` | `~Parole di <Kumiromi>~` | 1 |
| ～《永遠のネヘルタード》の言葉～ | `~words of <Amurdad>~` | `~Parole di <Amurdad>~` | 1 |
| ～不思議なノートの走り書き～ | `~scribbling in a mysterious notebook~` | `~Scarabocchi su un Quaderno Misterioso~` | 1 |
| ～奇妙な噂話～ | `~Bizarre Gossip~` | `~Dicerie Bizzarre~` | 1 |
| ～呪われた者の言葉～ | `~words of the victim to the curse~` | `~Parole di Chi è Stato Maledetto~` | 1 |
| ～慌てる市民の言葉～ | `~Worried Citizen~` | `~Parole di un Cittadino in Affanno~` | 1 |
| ～古代祭事のルーツに迫る～ | `~a Close Look at the Ancient Rituals~` | `~Alle Radici degli Antichi Riti~` | 1 |
| ～スンバラリア星人の言葉～ | `~words of a Sunbararian~` | `~Parole di un alieno di Sunbararia~` | 1 |
| ～破壊の神の言葉～ | `~words of a God of Destruction~` | `~Parole del Dio della Distruzione~` | 1 |
| ～食べられる草、食べられない草～ | `~Weeds you can Eat and Weeds you can't Eat~` | `~Erbe che si Mangiano ed Erbe che Non si Mangiano~` | 1 |
| ～森林と経済活動・製材編～ | `~Forest Economics, Sawmill Edition~` | `~Foreste ed Economia: la Segheria~` | 1 |
| ～特集・幻の植物を追う～ | `~Special Edition: Pursuing Mythical Plants~` | `~Speciale: sulle Tracce delle Piante Leggendarie~` | 1 |
| ～特選！裏の嗜好品～ | `~Special Edition! Behind-the-scenes Favorites!~` | `~Selezione! I Piaceri Clandestini~` | 1 |
| ～アイオンの予言～ | `~Aion's Prophecy~` | `~La Profezia di Aion~` | 1 |
| ～イルヴァ航空販売カタログ～ | `~Irva Airlines Sales Catalogue~` | `~Catalogo di Vendita di Irva Airlines~` | 1 |
| ～ダルフィ不動産・廃棄物件リスト～ | `~Derphy Real Estate - Unlisted~` | `~Immobiliare Derphy: Immobili Dismessi~` | 1 |
| ～ネクロマンサー入門～ | `~Necromancy for Noobs~` | `~Negromanzia per Principianti~` | 1 |
| ～謎のメモ～ | `~Weird Memo~` | `~Appunto Misterioso~` | 1 |
| ～伝説の職人『ガロク』の言葉～ | `~words of <Garok> the Legendary Smith~` | `~Parole di <Garok> il fabbro leggendario~` | 1 |
| ～別冊・怪しいアイテム買って試した～ | `~Extra Issue: Weird Items~` | `~Speciale: Oggetti Sospetti Comprati e Provati~` | 1 |
| ～裏路地の老店主の言葉～ | `~Words from an Shady, Old Shopkeeper~` | `~Parole del Vecchio Bottegaio del Vicolo~` | 1 |
| ～錬金術・禁忌大全～ | `~Extra Issue: Weird Items~` | `~Alchimia: Grande Compendio dei Divieti~` | 1 |
| ～戦場における指揮統制～ | `~Command and Control on the Battlefield~` | `~Comando e Controllo sul Campo di Battaglia~` | 1 |
| ～目覚めてしまった冒険者の言葉～ | `~words of an adventurer who has entered a new world~` | `~Parole di un Avventuriero che si è Risvegliato~` | 1 |
| ～命を救う応急処置～ | `~Life-saving First-aid~` | `~Il Primo Soccorso che Salva la Vita~` | 1 |
| ～毒物薬物辞典～ | `~Encyclopedia of Poison~` | `~Dizionario dei Veleni e dei Farmaci~` | 1 |
| ～インテリアパラダイス増刊号～ | `~Interior Paradise: Extra Issue~` | `~Interior Paradise: Numero Straordinario~` | 1 |
| ～おしゃれアイテム大特集～ | `~Stylish Item Special~` | `~Grande Speciale sugli Oggetti alla Moda~` | 1 |
| ～裁縫大百科～ | `~The Encyclopedia of Sewing~` | `~Grande Enciclopedia del Cucito~` | 1 |
| ～謎のレポート～ | `~Mysterious Report~` | `~Rapporto Misterioso~` | 1 |
| ～特集・機械文明の遺産～ | `~the Legacy of Mechanical Civilization~` | `~Speciale: l'Eredità della Civiltà Meccanica~` | 1 |
| ～廃業寸前のキャラメル職人の言葉～ | `~an Indebted Caramel Maker~` | `~Parole di un Caramellaio sull'Orlo del Fallimento~` | 1 |
| ～ノースティリス紀行・夏版～ | `~North Tyris Travels - Summer Edition~` | `~Viaggio in Tyris del Nord: Estate~` | 1 |
| ～迫り来る妹の言葉～ | `~words of a younger sister~` | `~Parole della Sorella Minore che si Fa Sotto~` | 1 |
| ～特別な孫の言葉～ | `~words of a grand-son~` | `~Parole di un Nipote Speciale~` | 1 |
| ～犠牲者の言葉～ | `~Victim's Last Words~` | `~Le Ultime Parole della Vittima~` | 1 |
| ～錬金術入門書～ | `~An Introduction to Alchemy~` | `~Manuale d'Introduzione all'Alchimia~` | 1 |
| ～吐き気をこらえる少女の言葉～ | `~a girl with nausea~` | `~Parole di una Bambina che Trattiene la Nausea~` | 1 |
| ～偉大なる料理評論家グラトナの言葉～ | `~ Words of the great food critic, Gratona ~` | `~Parole di <Gratona>, grande critico gastronomico~` | 1 |
| ～袋の裏に書かれた端書～ | `~Note Written on the Back of the Bag~` | `~Postilla Scritta sul Retro del Sacco~` | 1 |
| ～箱裏に書かれた注意書き～ | `~note written on the back of the box~` | `~Avvertenza Scritta sul Retro della Scatola~` | 1 |
| ～貴族のラスター、最後の言葉～ | `~last words, of Luster the noble~` | `~Le Ultime Parole di <Luster> il nobile~` | 1 |
| ～掃除屋『バルザック』の言葉～ | `~the Cleaner Balzak~` | `~Parole di <Balzak> il custode~` | 1 |
| ～本の為の本・解読書編～ | `~Big Book of Magical Books: Pre-Censorship~` | `~Il Libro dei Libri: i Libri da Decifrare~` | 1 |
| ～説明書の最後のページに書かれた文字～ | `~the last page of the instruction manual~` | `~Le Parole sull'Ultima Pagina del Manuale~` | 1 |
| ～妹研究の第一人者モクシスの研究論文～ | `~report of <Moxis>, leading imouto researcher~` | `~Studio di <Moxis>, massimo esperto di sorelle minori~` | 1 |
| ～盗賊ギルドマスター『シン』の言葉～ | `~words of <Sin> the thief guildmaster~` | `~Parole di <Sin> il maestro della Gilda dei Ladri~` | 1 |
| ～囚人達が選ぶ、人気商品ベスト５０～ | `~Top 50 Most Popular Products Among Prisoners~` | `~I 50 Prodotti Preferiti dai Detenuti~` | 1 |
| ～ヴェルニースの雑貨店に張られた広告～ | `~notice of good store of Vernis~` | `~Reclame Affissa al Bazar di Vernis~` | 1 |
| ～本の為の本・指導書編～ | `~Big Book of Books: Teacher's Edition~` | `~Il Libro dei Libri: i Manuali d'Insegnamento~` | 1 |
| ～猫嫌いの『タム』の言葉～ | `~<Tam> the cat hater~` | `~Parole di <Tam> il nemico dei gatti~` | 1 |
| ～青い髪の『ヴァリウス』の言葉～ | `~words of <Barius> the blue haired~` | `~Parole di <Barius> dai capelli blu~` | 1 |
| ～見世物屋の『モイアー』がガラクタを売り付ける際の口上～ | `~<Moyer> the crooked~` | `~La Cantilena di <Moyer> l'imbonitore~` | 1 |
| ～トレーニングマシーンの隅にかけられた謎の説明文～ | `~Mysterious Memo on the Training Machine~` | `~Istruzioni Misteriose in un Angolo dell'Attrezzo~` | 1 |
| ～妄想少女『リアナ』の言葉～ | `~Rianna the Daydreamer~` | `~Parole di <Rianna> la sognatrice~` | 1 |
| ～悩める魔術士『レントン』の言葉～ | `~words of <Renton> the suffering wizard~` | `~Parole di <Renton> il mago tormentato~` | 1 |
| ～見習い騎士『アインク』の言葉～ | `~words of <Ainc> the novice knight~` | `~Parole di <Ainc> il cavaliere novizio~` | 1 |
| ～女たらしの『ラファエロ』の言葉～ | `~words of <Raphael> the womanizer~` | `~Parole di <Raphael> il donnaiolo~` | 1 |
| ～ならずもののオネストの言葉～ | `~words of the honest? rogue~` | `~Parole di <Onest> il farabutto~` | 1 |
| ～こそどろのグリドの言葉～ | `~words of <Gleed> the thief~` | `~Parole di <Gleed> il topo d'appartamento~` | 1 |
| ～稀代の怪盗『マークス』の言葉～ | `~words of <Marks> the great thief~` | `~Parole di <Marks>, ladro senza pari~` | 1 |
| ～盗賊ギルドの番人『アビス』の言葉～ | `~words of <Abyss> the thief watchman~` | `~Parole di <Abyss> il guardiano della Gilda dei Ladri~` | 1 |
| ～街の子供のセスの言葉～ | `~words of <Seth> the kid~` | `~Parole di <Seth>, ragazzino di città~` | 1 |
| ～爆弾魔『ノエル』の言葉～ | `~words of <Noel> the bomber~` | `~Parole di <Noel> la dinamitarda~` | 1 |
| ～無邪気な少女『グウェン』の言葉～ | `~words of <Gwen> the innocent~` | `~Parole di <Gwen> l'innocente~` | 1 |
| ～歴史を学ぶ『エリステア』の言葉～ | `~words of <Erystia> the scholar of history~` | `~Parole di <Erystia> la studiosa di storia~` | 1 |
| ～子犬の『ポピー』の言葉～ | `~Poppy the Puppy~` | `~Parole di <Poppy> il cagnolino~` | 1 |

### Le righe **mute**, dove l'inglese è l'unica fonte (19)

Il ramo giapponese non ha questa riga: o è vuoto, o la mette in un altro
indice. ⓘ I quattro «rapporti di identificazione» il giapponese ce li ha,
ma nell'**indice 3**, dove `trimdesc(desc, 1)` tronca al primo `#` e non
arrivano mai a schermo: la forma è `～鑑定報告書：＜食物＞カテゴリ～`.

| en | it | righe |
|---|---|---|
| `~Identification Report: <Food> Category~` | `~Rapporto di Identificazione: categoria <Cibo>~` | 57 |
| `~ Identification Report <Item> Category~` | `~Rapporto di Identificazione: categoria <Oggetti>~` | 6 |
| `~Identification Report: <Seaweed> Category~` | `~Rapporto di Identificazione: categoria <Alghe>~` | 3 |
| `a Eulderna Researcher handling this tome` | `un ricercatore Eulderna che maneggia questo tomo` | 3 |
| `a Eulderna Researcher` | `un ricercatore Eulderna` | 2 |
| `~Identification Report: <Plants> Category~` | `~Rapporto di Identificazione: categoria <Piante>~` | 1 |
| `~some Eulderna Pyromaniac~` | `~un piromane Eulderna~` | 1 |
| `~memo of a grave robber~` | `~Appunti di un Predone di Rovine~` | 1 |
| `~some weird old guy~` | `~un vecchio bizzarro~` | 1 |
| `~Jonah, the Adventurer~` | `~<Jonah> l'avventuriero~` | 1 |
| `~Lane, the Fairy Invoker~` | `~<Lane>, evocatrice di fate~` | 1 |
| `Bureau of Eulderna Punditry (BEP)` | `Ufficio Eulderna degli Studi Dotti (UESD)` | 1 |
| `~words of a ex-excutioner~` | `~parole di un ex boia~` | 1 |
| `~words on the cover~` | `~parole sulla copertina~` | 1 |
| `~a Mysterious Note~` | `~un appunto misterioso~` | 1 |
| `a Eulderna Researcher holding this tome` | `un ricercatore Eulderna che tiene in mano questo tomo` | 1 |
| `arrested arsonist` | `un incendiario in arresto` | 1 |
| `outcast Eulderna Researcher` | `un ricercatore Eulderna ripudiato` | 1 |
| `~some Bearded Guy~` | `~un tizio con la barba~` | 1 |
