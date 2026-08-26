# -*- coding: utf-8 -*-
"""106a - Lotto 23 di `db_card.hsp`: le carte fra la riga 11101 e la 11600.

⚠️⚠️ **QUARANTA VOCI, TRENTOTTO RESE: LE DUE RIGHE MORTE SI RINVIANO.**
`:11405` (la prosa) e `:11412` (il nome) stanno dentro il blocco di
`CREATURE_ID_HARD_GAY` (`:11403`) e cominciano tutt'e due con `;`. Monte le ha
spente e le ha rimpiazzate **una riga sotto**, a `:11406` e `:11413`, con
`エクスプロージョマン` / `explosioman` — «l'uomo esplosivo». La carta e' la
stessa, il testo vivo e' quello nuovo. ⓘ La rete 6 le fermerebbe da sola; qui
sono in `RINVIATE` **e** in `rinviate.jsonl`, scritte da
`scratchpad/_106-rinvia-card-morte.py`.
💡 `:11412` non ha aggiunto una riga al registro: la sua **firma** c'era gia',
rinviata da `db_creature.hsp` — stessa creatura spenta nei due file. Il registro
passa da 112 a **113**, non a 114, ed e' giusto cosi'.

⚠️ **DICIASSETTE carte hanno l'inglese che finisce con uno SPAZIO**: `:11223`,
`:11236`, `:11249`, `:11314`, `:11340`, `:11353`, `:11366`, `:11379`, `:11392`,
`:11472`, `:11485`, `:11511`, `:11524`, `:11537`, `:11550`, `:11563`, `:11576`.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `ジャビ王` → **re Xabi**
(`chat.hsp`: ⚠️ l'inglese scrive `King Jabi`, e il progetto ha scelto Xabi),
`エイス・テール` → **Eyth Terre**, `ヨウィン` → **Yowyn**, `ヴェルニース` →
**Vernis**, `生化学文明` → **la civiltà biochimica** (`chat.hsp`), `機械信仰` →
**il culto della macchina** (`db_card:3397`), `ギルドマスター` → **il maestro
della gilda** (`chat.hsp`), `魔術士ギルド`/`盗賊ギルド`/`戦士ギルド` → **Gilda
dei Maghi / dei Ladri / dei Guerrieri**, `エーテルの風` → **il vento d'etere**
(glossario, distinto dalle **onde d'etere**), `イーク` → **lo yeek**, `コボルト`
→ **il coboldo**, `パンク` → **il punk** (`guida-stile.md`, prestito
invariabile).

ⓘ **`アクリ・テオラ` ha due rese gia' in casa, e qui vince la piu' lunga.**
`text.hsp:2791` e' il nome sulla **mappa** e dice «Cibercupola», stretto perche'
li' la colonna e' stretta; `text.hsp:10609`, che e' prosa come questa, dice «la
Cupola Cibernetica», e cosi' si chiama anche la carta (`:11530`, «l'abitante
della cupola cibernetica»). Nella prosa di `:11524` il nome sta due righe sotto
il nome della carta: si scrive uguale a quello.

ⓘ **Coniato qui:** `オチムシャ` → **ochimusha** (`:11379`), invariato: e'
`落武者` scritto in katakana proprio per farne un soprannome, e l'inglese lo
traslittera a sua volta (`Ochimsha`, con un refuso).

ⓘ Le citazioni fra 「」 e le virgolette **scappate** dell'inglese (`\\"swim\\"` a
`:11275`, `\\"cobalt\\"` a `:11301`, «人生» e «生き様» a `:11158`) si sciolgono in
discorso indiretto, come in tutte le carte gia' rese: cosi' la giuntura non ha
niente da rompere.
⚠️ E niente `…`: il carattere di sospensione e' fra i **proibiti** di `guardie`.
`:11106` finisce con tre punti normali.

⚠️ **`élite` non si puo' scrivere** (`:11353`): `degrada()` la porta a `e'lite`,
con l'apostrofo **dentro** la parola, e `verifica` la boccia — e' la stessa
regola che oggi ha fermato «dèi» nel lotto 19. Reso «il migliore fra i migliori».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :11106 il fanatico di Jure
    (11106, 'The figure of a person who has gone mad with delusion about the healing goddess Jure. There is not a shred of healing in their appearance. As far as the eye can see, they are happy...'):
        "L'aspetto di chi è impazzito a furia di rimuginare sulla dea che guarisce, Jure. Di guarigione, in quell'aspetto, non c'è nemmeno un briciolo. A vederli, però, sembrano felici...",

    # ---------------------------------------------------------- :11119 la canaglia
    (11119, 'They had to get their hands dirty in order to live in the town of their birth. They know no other way of life.They live today on the money they skim off the backs of the unwary.'):
        "Per vivere nella città dove sono nati non hanno potuto che sporcarsi le mani. Un altro modo di vivere non lo conoscono. Anche oggi tirano avanti con i soldi sfilati a chi non sta attento.",

    # ---------------------------------------------------------- :11132 la prostituta
    (11132, "Gives massages that feel so good that they drive you crazy. They usually speak to customers in a catcall voice, but their attitude changes abruptly when they realise that the customer doesn't have any money."):
        "Fa massaggi così piacevoli da far uscire di testa. Di solito parla ai clienti con la voce melliflua, ma appena capisce che il cliente non ha soldi cambia atteggiamento di colpo.",

    # ---------------------------------------------------------- :11145 il prigioniero
    (11145, 'Captives and prisoners. It takes hours, days or even years to clear the negative karma they have accumulated. Today, the voices of those pleading for their innocence echo in vain in their cells.'):
        "Chi è stato catturato e tenuto rinchiuso. Per saldare il karma negativo che ha accumulato ci vogliono qualche ora, qualche giorno o forse qualche anno. Anche oggi, nelle celle, la voce di chi grida la propria innocenza risuona a vuoto.",

    # ---------------------------------------------------------- :11158 l'artista
    (11158, "They paint a picture of their 'way of life' on the canvas of 'life'. Whether it will be a masterpiece or not, and when it will be completed, is up to them."):
        "Sulla tela che si chiama vita dipingono il quadro che si chiama modo di vivere. Se ne verrà fuori un capolavoro, e quando sarà finito, dipende soltanto da loro.",

    # ---------------------------------------------------------- :11171 l'aristocratico
    (11171, "He usually observes the lives of commoners in search of excitement. Basically, he doesn't carry much cash, but behind the scenes he spends money lavishly for his own proclivities."):
        "Di solito osserva la vita dei popolani in cerca di emozioni. Di contante in tasca ne porta poco, ma di nascosto spende senza risparmio per i propri gusti particolari.",

    # ---------------------------------------------------------- :11184 il membro della Gilda dei Maghi
    (11184, "A member of the Mages' Guild. His job is to decipher ancient texts, and he can use his knowledge to do magic, but he is not good at rough work as he is always researching."):
        "Un affiliato della Gilda dei Maghi. Il suo lavoro è decifrare i testi antichi, e con quel sapere sa anche usare la magia, ma siccome sta sempre a studiare non è capace di menare le mani.",

    # ---------------------------------------------------------- :11197 il membro della Gilda dei Ladri
    (11197, 'A group of people who live in the underworld. They have their own way of doing things. They have strict rules. Their skills can be of great help as long as you keep to the rules.'):
        "Un giro di gente che vive nel mondo di sotto. Hanno un loro modo di fare, e leggi severe a cui sottostare. Finché stai alle regole e le rispetti, la loro abilità è un grande aiuto.",

    # ---------------------------------------------------------- :11210 il membro della Gilda dei Guerrieri
    (11210, 'Basically, he is not good at thinking things deeply. However, that is why they have no doubts at all and are very reliable in battle. Many of them have admiration for their guildmaster.'):
        "Ragionare a fondo sulle cose, di norma, non gli riesce. Proprio per questo, però, non ha un solo dubbio, e in battaglia ci si può contare. In molti guardano al maestro della gilda con ammirazione.",

    # ---------------------------------------------------------- :11223 il bambino di città
    (11223, 'Their unquestioning faith in the bright future that will come their way is what we call a child. No matter how much time passes, they are children as long as they continue to believe in it blindly. '):
        "Credere senza un dubbio nel futuro luminoso che di sicuro arriverà: è proprio questo che merita il nome di bambino. Per quanto tempo passi, finché continuano a crederci ciecamente, bambini restano. ",

    # ---------------------------------------------------------- :11236 l'anziano
    (11236, 'This includes not only those who have aged, but also those who have aged rapidly, but only physically, at a young age. They spend their days just wandering around the city aimlessly. '):
        "Non ci sono soltanto quelli che hanno accumulato anni, ma anche quelli che, ancora giovani, hanno visto invecchiare di colpo il solo corpo. Le giornate passano tutte a girare per la città senza uno scopo. ",

    # ---------------------------------------------------------- :11249 il punk
    (11249, 'These eccentrics are devoted to the legacy and knowledge of ancient civilisations, and play around with machines in strange outfits. They are, they say, imitating the heretics of Eyth Terre. '):
        "Tipi strani, votati all'eredità e al sapere delle civiltà antiche, che armeggiano con le macchine conciati in modo bizzarro. A sentir loro, imitano gli eretici di Eyth Terre. ",

    # ---------------------------------------------------------- :11262 la pecora selvatica
    (11262, 'The perfect animal: edible and delicious meat, produces nutritional milk, and grows wool that can be used for clothing. Many escape their pens and snack on the neighboring fields.'):
        "La carne si mangia, il latte nutre da matti e il pelo serve per i vestiti: non le manca proprio niente. Tante scappano dal recinto e vanno a rubare nei campi qui intorno.",

    # ---------------------------------------------------------- :11275 la rana volante
    (11275, 'A species of flying frog found all over North Tyris. They can \\"swim\\" through the air as easily as swimming through water, though how this functions is unknown. Since even children are strong enough to take one down, they\'re a popular snack.'):
        "Una rana migratrice selvatica che saltella per tutta Tyris. Nuota nell'aria come se nuotasse sott'acqua, ma con che principio non si sa. Ad abbatterla riesce anche un bambino, e per questo è uno spuntino molto amato.",

    # ---------------------------------------------------------- :11288 il teppista
    (11288, 'Unemployed hooligans that wander about using blackmail and picking pockets in order to support themselves. They look strong and put up a brave front, but their true strength you can probably guess.'):
        "Bighellona senza lavorare e si guadagna il pane con l'estorsione e con qualcosa che somiglia al borseggio. Fa il gradasso e sembra forte, ma su quanto valga davvero c'è poco da illudersi.",

    # ---------------------------------------------------------- :11301 il coboldo
    (11301, 'A small monster with the head of a dog. Though it\'s difficult to process and so isn\'t used very often, the ore \\"cobalt\\" is said to come from this monster.'):
        "Un piccolo mostro con la testa da cane. Lavorarlo è difficile e quindi non lo si usa granché, ma dicono che il nome del minerale cobalto venga proprio da questa bestia.",

    # ---------------------------------------------------------- :11314 lo yeek
    (11314, 'Beasts with a human-like appearance. They are stupid and frail, and on their own are only as capable as human children, but they attack with numbers to compensate. '):
        "Una bestia dall'aspetto simile a quello dell'uomo. Sono sciocchi e deboli, e da soli valgono quanto un bambino umano, ma per rimediare attaccano in tanti. ",

    # ---------------------------------------------------------- :11327 lo yeek guerriero
    (11327, 'Beasts with a human-like appearance. Only those who have endured the most rigorous training among the Yeeks are awarded the title of warrior. For this reason, they are proud to be warriors.'):
        "Una bestia dall'aspetto simile a quello dell'uomo. Fra gli yeek, soltanto chi ha retto un allenamento durissimo riceve il titolo di guerriero. Ed è per questo che di esserlo va fiero.",

    # ---------------------------------------------------------- :11340 lo yeek arciere
    (11340, 'The yeek has the intelligence to attack from a distance compared to other members of his tribe. As a result of continually pulling the strings to handle the bow, his body has been trained, although not as well as the warriors of his own tribe. '):
        "Uno yeek che, rispetto agli altri della sua gente, ha l'intelligenza di attaccare da lontano. A furia di tendere la corda per maneggiare l'arco si è irrobustito, anche se non quanto i guerrieri dei suoi. ",

    # ---------------------------------------------------------- :11353 lo yeek maestro
    (11353, 'Elite of the elite, destined to become a master from birth. They excel in their ability to command and lead their own people, and they have commanded a large number of Yeeks. '):
        "Il migliore fra i migliori, destinato fin dalla nascita a diventare maestro. Eccelle nel comandare e nel guidare la propria gente, e ha ai suoi ordini un gran numero di yeek. ",

    # ---------------------------------------------------------- :11366 lo yeek kamikaze
    (11366, 'The means they chose to overcome the low physical capabilities of the Yeeks was self-destruction at the cost of their own lives. However, it was easily detonated and their allies were also collateralised. '):
        "Il mezzo che hanno scelto per rimediare alle poche doti fisiche degli yeek è stato farsi esplodere, sacrificando la propria vita. Solo che l'innesco parte con niente, e nell'esplosione ci finiscono dentro anche i compagni. ",

    # ---------------------------------------------------------- :11379 il samurai kamikaze
    (11379, 'They are the result of warriors exiled from the East. Known as Ochimsha, they are said to want to die spectacularly on the battlefield for the sake of their home and honour, but they are actually very afraid of dying. '):
        "Quel che resta dei guerrieri cacciati dal paese d'oriente. Li chiamano ochimusha, e si dice che desiderino una morte splendida sul campo, per la casata e per l'onore, ma in verità pare che di morire abbiano una paura tremenda. ",

    # ---------------------------------------------------------- :11392 la roccia esplosiva
    (11392, 'An ordinary rock has mutated into a monster. It is watched with a grin, but even the slightest provocation can cause it to explode, so it should be handled carefully from a distance. '):
        "Una roccia qualunque che è mutata ed è diventata un mostro. Ti guarda con un sorrisetto, ma basta un urto da niente perché esploda, e quindi conviene occuparsene da lontano e con prudenza. ",

    # ---------------------------------------------------------- :11406 l'uomo esplosivo
    (11406, 'Cloned human beings produced by terrorists exploiting relics of biochemical civilisations. The aim is to detonate them in crowded places. As the terrorists do not know how to use the relics well, they are all output in the same appearance. They are instinctively imprinted with the idea that risking their lives in an explosion is an art form.'):
        "Cloni umani prodotti dai terroristi con un uso storto dei resti della civiltà biochimica. Lo scopo è farli esplodere in mezzo alla folla. Siccome i terroristi non hanno capito bene come si usano quei resti, escono tutti con lo stesso aspetto. Nell'istinto gli hanno impresso che giocarsi la vita in un'esplosione sia arte.",

    # ---------------------------------------------------------- :11420 <Rodlob> il capo degli yeek
    (11420, "Absolute charisma of the yeek world. Highly intelligent, he unites the entire tribe. He plans to gather his friends and plunder Yowyn's crops."):
        "Il carisma assoluto del mondo degli yeek. Ha un'intelligenza alta e tiene unita l'intera stirpe. Sta tramando di radunare i suoi e di razziare i raccolti di Yowyn.",

    # ---------------------------------------------------------- :11433 l'amante delle terme
    (11433, "Those who have fallen under the spell of the hot springs and continue to bathe in them like a curse. Their whole body is already soaked. If you try to ask about the charms of hot springs, you will be told endless maniacal stories, so it's best not to try."):
        "Gente presa dal fascino delle terme, che continua a stare a mollo come sotto una maledizione. Il corpo ce l'hanno già tutto raggrinzito dall'acqua. Se ti viene in mente di chiedere che cosa abbiano di bello le terme ti tocca un discorso infinito da fanatici, e allora meglio lasciar perdere.",

    # ---------------------------------------------------------- :11446 il millepiedi
    (11446, "A small creature that lives in soil, and thus appears in many places. Though it doesn't use it to attack, the creature does contain poison, so eating it will make you sick."):
        "Vive volentieri dove c'è molta terra, e lo si incontra nelle zone più diverse. Per attaccare non lo usa, ma il veleno ce l'ha, e a mangiarlo viene la nausea.",

    # ---------------------------------------------------------- :11459 il fungo
    (11459, 'A mushroom that feeds on decaying corpses in order to grow. Exposure to Ether has caused it to mutate and grow to gigantic sizes. That includes its spores, which it uses as a weapon.'):
        "Un fungo che cresce nutrendosi dei cadaveri. L'etere lo ha fatto mutare all'improvviso e diventare enorme. Anche le spore sono diventate enormi, e gli servono per attaccare.",

    # ---------------------------------------------------------- :11472 il fungo sporifero
    (11472, 'Mushrooms that have become poisonous in their spores due to the soil and air in which they grow. If consumed carelessly, the mushrooms can cause abdominal pain. '):
        "Un fungo a cui, forse per il terreno in cui è spuntato o per l'aria, le spore si sono riempite di veleno. A mangiarlo alla leggera ci si ritrova a rotolare per il mal di pancia. ",

    # ---------------------------------------------------------- :11485 il fungo del caos
    (11485, 'A mycelium that has taken on the power of chaos, it uses its spores to target and slowly weaken its enemies. Its dangerous spores have the power to inflict various kinds of suffering. '):
        "Un fungo che ha assorbito la forza del caos e che, con le spore, prende di mira il nemico e lo indebolisce piano piano. Quelle spore pericolose hanno il potere di infliggere sofferenze di ogni sorta. ",

    # ---------------------------------------------------------- :11498 il cittadino
    (11498, "People who live in a city. They'll keep you busy by asking you to provide them birthday gifts, performing for parties, getting things from other people, and protecting the town from monsters."):
        "Gente che vive in città. Festeggia il compleanno dei figli, va alle feste, si mette in testa la roba degli altri, viene assalita dai mostri: sono giornate piene.",

    # ---------------------------------------------------------- :11511 il cittadino
    (11511, "They are ordinary citizens in every town, who are not different in any way. They generally like to collect light objects, but at the same time they have a side that carries around uneaten and rotten food that they can't throw away. "):
        "Cittadini comuni, che si trovano in qualunque paese e non hanno niente di diverso dagli altri. In genere amano collezionare le cose che luccicano, ma insieme hanno anche il vizio di portarsi dietro il cibo che non sono riusciti a finire e che è marcito, senza decidersi a buttarlo. ",

    # ---------------------------------------------------------- :11524 l'abitante della cupola cibernetica
    (11524, 'People live in Cyber Dome, a huge structure made of machines, which is said to be the legacy of Eyth Terre. They live in an artificially prepared and comfortable environment and have a thriving machine religion. '):
        "Gente che vive nella Cupola Cibernetica, l'enorme costruzione fatta di macchine che dicono sia un lascito di Eyth Terre. Passano le giornate in un ambiente comodo, regolato per via artificiale, e il culto della macchina è molto praticato. ",

    # ---------------------------------------------------------- :11537 l'abitante della cupola cibernetica
    (11537, 'People live in a mysterious building that exists in the forest south-west of Vernis. According to one theory, it is a legacy of the old civilisation and may or may not have been blessed by a certain god. '):
        "Gente che vive in un edificio sospetto in mezzo al bosco a sud-ovest di Vernis. Secondo una certa teoria è un lascito della vecchia civiltà, e forse ha ricevuto la benedizione di una certa divinità, o forse no. ",

    # ---------------------------------------------------------- :11550 l'agente di commercio
    (11550, 'The products they handle range from various types of property and inheritance rights to firearms. It can be said that they cover everything from the cradle to the grave. '):
        "La merce che tratta va dai beni immobili di ogni sorta e dai titoli di eredità fino, in fondo, alle armi da fuoco. Si può proprio dire che copra tutto, dalla culla alla tomba. ",

    # ---------------------------------------------------------- :11563 il marinaio
    (11563, 'A man of business who loves the sea and sailing his ship across foreign lands. The sea is full of pirates and dangerous monsters, but it is also difficult to get around them, and it is said that port towns on the ground are a place of peace for sailors. '):
        "Un uomo di mestiere che ama il mare e che, manovrando la nave, passa da un paese straniero all'altro. Il mare è pieno di pirati e di mostri pericolosi, e scansarli non è facile: per un marinaio pare che le città portuali sulla terraferma siano il posto della quiete. ",

    # ---------------------------------------------------------- :11576 il capitano
    (11576, 'A fierce warrior who lives on the sea, bathed in waves and winds, and travels across countries in a ship whose life is equal to his own. Even the most skilled of sailors often end up with their ships in the sea due to the ether winds, which are difficult to predict. '):
        "Un fiero che vive sul mare, si prende in faccia onde e vento e passa da un paese all'altro guidando una nave che vale quanto la sua vita. Per quanto sia esperto, capita spesso che il vento d'etere, difficile da prevedere, se lo porti in fondo al mare insieme alla nave. ",

    # ---------------------------------------------------------- :11589 <Stersha> la regina di Palmia
    (11589, 'Queen of the benevolent and modest King Jabi. She is deeply in love with her husband and is well known in Palmia as the ideal couple. She is soft-spoken, but can be condescending towards bandits.'):
        "La sposa di re Xabi, uomo pieno di misericordia e di riserbo. Ama il marito profondamente, e in tutta Palmia sono famosi come la coppia ideale. I modi sono gentili, ma con i briganti sa prendere un'aria di disprezzo.",
}

# ⚠️ Le due righe spente con `;` dentro il blocco di `CREATURE_ID_HARD_GAY`:
# monte le ha rimpiazzate una riga sotto con l'uomo esplosivo. Registrate anche
# in `rinviate.jsonl` da `scratchpad/_106-rinvia-card-morte.py`.
RINVIATE = {
    (11405, 'It was designated a hard gay species because it was the hardest of the gay '
            'species. They have a habit of being attracted to muscular muscles. The '
            'existence of soft gay species is debated in academic circles.'),
    (11412, 'hard gay'),
}

USCITA = 'lavoro/fase5-db_card-023.jsonl'
DA, A = 11101, 11600
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_card.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
