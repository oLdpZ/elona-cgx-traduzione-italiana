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
| minotaur | minotauro | |
| centipede / scorpion / spider | millepiedi / scorpione / ragno | |
| king X | X re | postposto per l'aggancio: `king orc` → «l'orco re», `king cobra` → «il cobra reale» dove la lingua lo chiede |
| older / younger sister | sorella maggiore / minore | i nomi di creatura, non la parentela in prosa (vedi sotto) |
| dog / hound | cane / segugio | fissate col nucleo. `X hound` → «il segugio di/del X», sulla forma di `chaos imp` |
| wolf | lupo | `silver wolf` → «il lupo d'argento», materiale come complemento invariabile |
| fox | volpe | 妖狐 `fox spirit` → «la volpe ammaliatrice»: 妖 è l'ammaliare, e «volpe spirito» sarebbe un calco dall'inglese |
| werewolf | lupo mannaro | `werewolf detective` → «il lupo mannaro detective», modificatore postposto |
| Juere / Elea / Zanan | Juere / Elea / Zanan | nomi di popolo del canone Elona, invariati. ⚠️ **La razza sta in `dbidn`, non nel nome**: 歴戦の老兵 è «il veterano» e basta, anche se l'inglese lo chiama `zanan old soldier`. Scrivere nel nome un dato che il nome non porta è aggiungere, non tradurre. ⚠️ **ジューア (Juere) non è ジュア (Jure)**: un carattere di differenza fra la nazione e la dea, e le due si somigliano anche in italiano. `juere berserker` → «il berserker di Juere», `instigator of Elea` → «l'istigatore degli Elea» |
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

⚠️ Attenzione: in `action.hsp` le stringhe `Wolf Sister`, `Yandere Sister`,
`Small Older Sister`, `older sister`, `younger sister` **non sono prosa**: sono
`evname`/`evold`, cioè nomi di creatura del sistema di evoluzione. Non si
traducono qui — vedi la sezione «nomi di creatura riscritti nel salvataggio» di
`invariati.md`.

## Da decidere

*Vuota dal 2026-08-07.* I sei termini che stavano qui — `Gauge`, `Chaos`,
`Abyss`, `Skill`, `Sister`, `Body` — sono decisi e spostati nelle tabelle sopra,
insieme ai cinque toponimi che erano in `invariati.md`.
