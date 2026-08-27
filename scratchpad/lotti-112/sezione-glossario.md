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
| ～街中の名脇役達～ | `~Supporting Roles on the Streets~` | `~I Grandi Comprimari della Citta'~` | 15 |
| ～あなたの見知らぬ世界～ | `~ Worlds you've Never Seen~`<br>`~Worlds you've Never Seen~` ⚠️ | `~I Mondi che Non Hai Mai Visto~` | 12 |
| ～遊技大典・全年齢対応版～ | `~Game Tricks, All Ages Version~` | `~Grande Compendio dei Giochi: Per Tutte le Eta'~` | 11 |
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
| ～病みつきになる煙の味は～ | `~Sickly Taste of Smoke~` | `~Il Sapore del Fumo che Da' Dipendenza~` | 5 |
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
| ～農業、その新たな可能性～ | `~Agriculture and its New Possibilities~` | `~L'Agricoltura e le sue Nuove Possibilita'~` | 2 |
| ～家庭でできる応急処置～ | `~First aid at home~` | `~Primo Soccorso in Casa~` | 2 |
| ～イムウエル交易譚～ | `~the Aimwell tale of trade~` | `~Racconti di Commercio di Aimwell~` | 2 |
| ～いいもの選ぼう職人道具～ | `~Choosing the Best Tools for the Best Craftsmen~` | `~Scegliere Bene gli Attrezzi da Artigiano~` | 2 |
| ～税金との付き合い方～ | `~Irva Revenue Services~` | `~Come Andare d'Accordo con le Tasse~` | 2 |
| ～牧畜と暮らす生活～ | `~Living with Livestock~` | `~Vivere Insieme al Bestiame~` | 2 |
| ～ザナンの紅の英雄『ロイター』の言葉～ | `~words of <Loyter> the crimson of Zanan~` | `~Parole di <Loyter>, l'eroe cremisi di Zanan~` | 2 |
| ～異形の森の使者『ロミアス』の言葉～ | `~<Lomias> The Messenger From Vindale~`<br>`~<Lomias> the messenger from Vindale~` ⚠️ | `~Parole di <Lomias>, messo della foresta deforme~` | 2 |
| ～釣り自慢のフィッシャーの言葉～ | `~words of a fisherman proud of his catch~` | `~Parole di un Pescatore Fiero della Sua Preda~` | 2 |
| ～本の為の本・歴史書編～ | `~Big Books of Historical Books~` | `~Il Libro dei Libri: i Libri di Storia~` | 2 |
| ～情報屋ウィーゼムの調べた情報～ | `~Intel of the Informant Wiesem~` | `~Le Notizie Raccolte da <Wiesem> l'informatore~` | 2 |
| ～鉄の胃袋を求めて・完食列伝～ | `~Iron Stomach: A Complete Diet~` | `~In Cerca di uno Stomaco di Ferro: Piatti Finiti~` | 2 |
| ～ティリス武具大全、広告のページ～ | `~Tyris Armor Compendium, page of advertisements~` | `~Grande Compendio delle Armi di Tyris: le Reclame~` | 2 |
| ～敗北者のうめき声～ | `~words of the defeated~` | `~Il Gemito dello Sconfitto~` | 1 |
| ～涙目の煽りイカの言葉～ | `~words of a Provocasquid~` | `~Parole del Calamaro Provocatore con gli Occhi Lucidi~` | 1 |
| ～続・明日から使えるあなたの為の武具集～ | `~Collection of Armaments you can Use Tomorrow Cont.~` | `~Ancora Armi e Armature da Usare Domani~` | 1 |
| ～もう化かされない！魔物の罠の見抜き方～ | `~Fool me twice, Shame on me!~` | `~Non ci Casco Piu'! Come Scoprire i Trucchi dei Mostri~` | 1 |
| ～金毛九尾の言葉～ | `~words of Kyu-Bi~` | `~Parole della Volpe a Nove Code dal Manto d'Oro~` | 1 |
| ～ペットトレイナーの言葉～ | `~words of a Pet Trainer~` | `~Parole dell'Addestratore di Bestie~` | 1 |
| ～訓練所の張り紙～ | `~words at the Training Center ~` | `~Avviso Affisso alla Palestra~` | 1 |
| ～鎖自慢された奴隷の言葉～ | `a Slave showing off his chains.` | `~Parole di uno Schiavo Fiero delle Sue Catene~` | 1 |
| ～拘束器具の歴史～ | `~ History of Bondage ~` | `~Storia degli Strumenti di Costrizione~` | 1 |
| ～機甲将軍『アインリッヒ』の言葉～ | `~<Heinrich> the Armored General~` | `~Parole di <Heinrich> il generale corazzato~` | 1 |
| ～特殊部隊長『ミーリス』の言葉～ | `~<Milis> Captain of the Special Forces~` | `~Parole di <Milis>, capo delle forze speciali~` | 1 |
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
| ～ソックスソードマンの評価～ | `~words of a sockswordman~` | `~Il Giudizio del Sockswordman~` | 1 |
| ～君にもできるサバイバル～ | `~Survival that Anyone Can Do~` | `~La Sopravvivenza Alla Portata di Tutti~` | 1 |
| ～危険物取扱マニュアル～ | `~Hazardous Materials Handling Manual~` | `~Manuale per il Maneggio di Materiali Pericolosi~` | 1 |
| ～夢の廃物利用～ | `~Magical Ways of Waste Utilization~` | `~Il Sogno di Riusare gli Scarti~` | 1 |
| ～根元の濡れた標識～ | `~the Whizzard~` | `~Il Cartello Bagnato alla Base~` | 1 |
| ～はく製マニアからの手紙～ | `~words of an Fossil Enthusiast~` | `~Lettera di un Fissato di Tassidermia~` | 1 |
| ～本の為の本・成年誌編～ | `~Big Book of Adult Books~` | `~Il Libro dei Libri: le Riviste per Adulti~` | 1 |
| ～必見！貯蓄型資産運用のすべて～ | `~Must Watch! Everything About Savings and Asset Management~` | `~Da Vedere! Tutto sul Risparmio e sugli Investimenti~` | 1 |
| ～発見！世界の珍品～ | `~Discovery! Curiosities of the World~` | `~Scoperta! Le Rarita' del Mondo~` | 1 |
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
| ～呪われた者の言葉～ | `~words of the victim to the curse~` | `~Parole di Chi e' Stato Maledetto~` | 1 |
| ～慌てる市民の言葉～ | `~Worried Citizen~` | `~Parole di un Cittadino in Affanno~` | 1 |
| ～古代祭事のルーツに迫る～ | `~a Close Look at the Ancient Rituals~` | `~Alle Radici degli Antichi Riti~` | 1 |
| ～スンバラリア星人の言葉～ | `~words of a Sunbararian~` | `~Parole di un Abitante del Pianeta Sunbararia~` | 1 |
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
| ～目覚めてしまった冒険者の言葉～ | `~words of an adventurer who has entered a new world~` | `~Parole di un Avventuriero che si e' Risvegliato~` | 1 |
| ～命を救う応急処置～ | `~Life-saving First-aid~` | `~Il Primo Soccorso che Salva la Vita~` | 1 |
| ～毒物薬物辞典～ | `~Encyclopedia of Poison~` | `~Dizionario dei Veleni e dei Farmaci~` | 1 |
| ～インテリアパラダイス増刊号～ | `~Interior Paradise: Extra Issue~` | `~Interior Paradise: Numero Straordinario~` | 1 |
| ～おしゃれアイテム大特集～ | `~Stylish Item Special~` | `~Grande Speciale sugli Oggetti alla Moda~` | 1 |
| ～裁縫大百科～ | `~The Encyclopedia of Sewing~` | `~Grande Enciclopedia del Cucito~` | 1 |
| ～謎のレポート～ | `~Mysterious Report~` | `~Rapporto Misterioso~` | 1 |
| ～特集・機械文明の遺産～ | `~the Legacy of Mechanical Civilization~` | `~Speciale: l'Eredita' della Civilta' Meccanica~` | 1 |
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
| ～掃除屋『バルザック』の言葉～ | `~the Cleaner Balzak~` | `~Parole di <Balzak> il netturbino~` | 1 |
| ～本の為の本・解読書編～ | `~Big Book of Magical Books: Pre-Censorship~` | `~Il Libro dei Libri: i Libri da Decifrare~` | 1 |
| ～説明書の最後のページに書かれた文字～ | `~the last page of the instruction manual~` | `~Le Parole sull'Ultima Pagina del Manuale~` | 1 |
| ～妹研究の第一人者モクシスの研究論文～ | `~report of <Moxis>, leading imouto researcher~` | `~Studio di <Moxis>, massimo esperto di sorelle minori~` | 1 |
| ～盗賊ギルドマスター『シン』の言葉～ | `~words of <Sin> the thief guildmaster~` | `~Parole di <Sin>, maestro della gilda dei ladri~` | 1 |
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
| ～盗賊ギルドの番人『アビス』の言葉～ | `~words of <Abyss> the thief watchman~` | `~Parole di <Abyss>, guardiano della gilda dei ladri~` | 1 |
| ～街の子供のセスの言葉～ | `~words of <Seth> the kid~` | `~Parole di <Seth>, ragazzino di citta'~` | 1 |
| ～爆弾魔『ノエル』の言葉～ | `~words of <Noel> the bomber~` | `~Parole di <Noel> la dinamitarda~` | 1 |
| ～無邪気な少女『グウェン』の言葉～ | `~words of <Gwen> the innocent~` | `~Parole di <Gwen> la bambina innocente~` | 1 |
| ～歴史を学ぶ『エリステア』の言葉～ | `~words of <Erystia> the scholar of history~` | `~Parole di <Erystia>, studiosa di storia~` | 1 |
| ～子犬の『ポピー』の言葉～ | `~Poppy the Puppy~` | `~Parole di <Poppy> il cucciolo~` | 1 |

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

