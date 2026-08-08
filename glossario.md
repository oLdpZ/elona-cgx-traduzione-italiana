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
