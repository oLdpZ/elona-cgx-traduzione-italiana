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

## Da decidere

*Vuota dal 2026-08-07.* I sei termini che stavano qui — `Gauge`, `Chaos`,
`Abyss`, `Skill`, `Sister`, `Body` — sono decisi e spostati nelle tabelle sopra,
insieme ai cinque toponimi che erano in `invariati.md`.
