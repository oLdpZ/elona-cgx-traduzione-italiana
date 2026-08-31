# -*- coding: utf-8 -*-
"""112a - La famiglia delle righe-fonte di `db_item.hsp`, decisa.

⚠️ Le righe-fonte NON sono voci del dizionario: sono l'ultimo segmento di una
descrizione che e' tutt'uno, e non passano da `reimporta`. Questa tabella e'
una decisione di **glossario**, come le ventiquattro parole dell'equipaggiamento
della 111a: si applica a mano, lotto per lotto, quando si traduce la prosa.

⚠️⚠️ **LA CHIAVE E' IL GIAPPONESE, NON L'INGLESE**, perche' l'inglese di monte
appiattisce: `~Vernis Ore Catalogue~` copre tre libri giapponesi diversi,
`~Irva Fantasy Encyclopedia~` ne copre due, e `Lead Developer <Dr. Gavela>`
copre due persone. Chi indicizza per inglese perde la distinzione e la
riscrive sbagliata in un lotto su cento.

`TITOLI_EN` serve solo per le righe **mute**: quelle dove il ramo giapponese
non ha la riga-fonte, perche' la mette in un altro indice o non ce l'ha. Li'
l'inglese e' l'unica fonte.

⚠️⚠️ **DIECI TITOLI CONTRADDICEVANO UN NOME CHE IL GIOCATORE VEDE GIA', E A
TROVARLI E' STATA UNA RETE DELLA 113a** (`scratchpad/_113-fonti-gia-rese.py`).
Il giapponese di 45 titoli su 200 e' **gia' reso** altrove nel dizionario —
`異形の森の使者『ロミアス』` sta in `db_card.hsp:10579` e `db_creature.hsp:100005`,
reso «<Lomias> il messaggero di Vindale», mentre qui c'era scritto «messo della
foresta deforme»: una terza forma che nel dizionario non esiste. Corretti anche
Balzak (netturbino -> **custode**), Gwen (bambina innocente -> **l'innocente**),
Milis (capo -> **la comandante**), Poppy (cucciolo -> **cagnolino**), Erystia,
Loyter, Sin e Abyss (**Gilda dei Ladri** maiuscola) e il sunbararian.

💡 `_112-nomi-fonti.py` cercava i **nomi** per inglese e non poteva vederli: qui
il nome sta dentro un titolo piu' lungo, e la chiave che li lega e' il
**giapponese intero**. ⓘ `《叡智のソピアー》` resta `~Parole di <Sophia>~` anche
se la carta dice «<Sophia> la Saggia»: li' l'inglese del titolo e'
`~words of <Sophia>~`, nudo come per le altre quindici divinita'.
"""

# ---------------------------------------------------------------------------
# I NOMI GIA' DECISI ALTROVE, che qui si riusano e non si ridecidono.
# Le divinita' portano in giapponese un epiteto dentro 《》 che l'inglese butta
# via; il progetto ha gia' reso `《剛石のウリカグアル》` come `<Urcaguary>`, e
# queste righe gli vanno dietro. Vedi `_112-nomi-fonti.py`.
# ---------------------------------------------------------------------------

TITOLI_JP = {
    # --- i libri di casa, i piu' frequenti ---------------------------------
    "～イルヴァ幻想辞典～": "~Dizionario Fantastico di Irva~",
    "～イムウエル幻想辞典～": "~Dizionario Fantastico di Aimwell~",
    "～明日から使えるあなたの為の武具集～": "~Raccolta di Armi e Armature da Usare Domani~",
    "～続・明日から使えるあなたの為の武具集～": "~Ancora Armi e Armature da Usare Domani~",
    "～移り変わりゆくティリスの食～": "~Il Cibo Mutevole di Tyris~",
    "～ノースティリス大家具事典～": "~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    "～飲めるのみもの、飲めないのみもの～": "~Bevande da Bere e Bevande da Non Bere~",
    "～魔具全典～": "~Compendio Completo degli Oggetti Magici~",
    "～ルミエスト美術目録～": "~Catalogo d'Arte di Lumiest~",
    "～ティリス園芸図鑑～": "~Atlante Illustrato del Giardinaggio di Tyris~",
    "～今日から君も冒険者・旅用マニュアル～": "~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    "～旅用マニュアル注釈～": "~Note al Manuale di Viaggio~",
    "～ヴェルニース鉱物図鑑～": "~Atlante dei Minerali di Vernis~",
    "～ザイール鉱物図鑑～": "~Atlante dei Minerali di Zaile~",
    "～別冊ヨウィン・未知の知識を追え！～": "~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    "～家庭を彩る日用雑貨～": "~Casalinghi che Danno Colore alla Casa~",
    "～私の愛する幾千ものガラクタ～": "~Le Mille Cianfrusaglie che Amo~",
    "?私の愛する幾千ものガラクタ?": "~Le Mille Cianfrusaglie che Amo~",
    "～ゴミの山に光るもの～": "~Quel che Brilla nel Mucchio dei Rifiuti~",
    "～料理を支える脇役達～": "~I Comprimari della Cucina~",
    "～街中の名脇役達～": "~I Grandi Comprimari della Città~",
    "～エウダーナに学ぶ必勝交易法～": "~Il Commercio Vincente Secondo gli Eulderna~",
    "～玲瓏たるイルヴァの調べ～": "~Le Melodie della Limpida Irva~",
    "～遊技大典・全年齢対応版～": "~Grande Compendio dei Giochi: Per Tutte le Età~",
    "～貰って嬉しい贈り物あれこれ～": "~Regali che Fa Piacere Ricevere~",

    # --- la famiglia «本の為の本», che va tenuta insieme --------------------
    "～本の為の本～": "~Il Libro dei Libri~",
    "～本の為の本・魔法書編～": "~Il Libro dei Libri: i Grimori~",
    "～本の為の本・児童書編～": "~Il Libro dei Libri: i Libri per Bambini~",
    "～本の為の本・歴史書編～": "~Il Libro dei Libri: i Libri di Storia~",
    "～本の為の本・成年誌編～": "~Il Libro dei Libri: le Riviste per Adulti~",
    "～本の為の本・解読書編～": "~Il Libro dei Libri: i Libri da Decifrare~",
    "～本の為の本・指導書編～": "~Il Libro dei Libri: i Manuali d'Insegnamento~",

    # --- viaggi, citta', mestieri ------------------------------------------
    "～脱冒険者から始める商いライフ～": "~Vita da Mercante Dopo l'Avventura~",
    "～死にゆく者へ贈る書～": "~Libro in Dono a Chi Sta Morendo~",
    "～ノースティリス紀行・冬版～": "~Viaggio in Tyris del Nord: Inverno~",
    "～ノースティリス紀行・夏版～": "~Viaggio in Tyris del Nord: Estate~",
    "～子供を騙す１００のテクニック・お土産編～": "~Cento Modi per Fregare i Bambini: i Souvenir~",
    "～打切上等！箱マニア・創刊号～": "~Chiudeteci Pure! Box Mania, Numero Uno~",
    "～ダルフィ不動産・商品カタログ～": "~Immobiliare Derphy: Catalogo~",
    "～ダルフィ不動産・廃棄物件リスト～": "~Immobiliare Derphy: Immobili Dismessi~",
    "～あなたの見知らぬ世界～": "~I Mondi che Non Hai Mai Visto~",
    "～パルミア秋冬物コレクション～": "~Palmia: Collezione Autunno-Inverno~",
    "～パルミア春夏物コレクション～": "~Palmia: Collezione Primavera-Estate~",
    "～パルミア広報～": "~Bollettino di Palmia~",
    "～病みつきになる煙の味は～": "~Il Sapore del Fumo che Dà Dipendenza~",
    "～これからの魔物被害対策～": "~Difendersi dai Mostri, da Qui in Avanti~",
    "～君にも使える！発掘兵器～": "~Puoi Usarle Anche Tu! Le Armi Riesumate~",
    "～バトルホビー列伝～": "~Cronache del Battle Hobby~",
    "～世界のコイン・ティリス編～": "~Le Monete del Mondo: Tyris~",
    "～海藻と海草の違い～": "~Alghe e Piante Marine: la Differenza~",
    "～毒も薬も用法・用量～": "~Veleno o Medicina: Modo e Dose~",
    "～奥深い酒の世界～": "~Il Mondo Profondo dei Liquori~",
    "～不思議な古代装飾品～": "~Misteriosi Ornamenti Antichi~",
    "～熱き決闘者たち～": "~Duellanti Ardenti~",
    "～巻かれる為の長いもの～": "~Cose Lunghe Fatte per Essere Avvolte~",
    "～嘘と勘違いされる全くの作り話・第２巻～": "~Storie Inventate Scambiate per Bugie, Volume 2~",
    "～より良い業物を目指して～": "~Verso una Lama Migliore~",
    "～選ぼう、大切な人への贈り物～": "~Scegliamo un Dono per Chi ci sta a Cuore~",
    "～今日から始める奴隷運用～": "~Gestire uno Schiavo, da Oggi~",
    "～拘束器具の歴史～": "~Storia degli Strumenti di Costrizione~",
    "～ロストテクノロジー、その片鱗～": "~Tecnologia Perduta: un Barlume~",
    "～遺跡荒らしのメモ～": "~Appunti di un Predone di Rovine~",
    "～叡智の書～": "~Il Libro della Sapienza~",
    "～農業、その新たな可能性～": "~L'Agricoltura e le sue Nuove Possibilità~",
    "～家庭でできる応急処置～": "~Primo Soccorso in Casa~",
    "～命を救う応急処置～": "~Il Primo Soccorso che Salva la Vita~",
    "～イムウエル交易譚～": "~Racconti di Commercio di Aimwell~",
    "～いいもの選ぼう職人道具～": "~Scegliere Bene gli Attrezzi da Artigiano~",
    "～税金との付き合い方～": "~Come Andare d'Accordo con le Tasse~",
    "～牧畜と暮らす生活～": "~Vivere Insieme al Bestiame~",
    "～別冊・怪しいアイテム買って試した～": "~Speciale: Oggetti Sospetti Comprati e Provati~",
    "～錬金術・禁忌大全～": "~Alchimia: Grande Compendio dei Divieti~",
    "～情報屋ウィーゼムの調べた情報～": "~Le Notizie Raccolte da <Wiesem> l'informatore~",
    "～鉄の胃袋を求めて・完食列伝～": "~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",
    "～ティリス武具大全、広告のページ～": "~Grande Compendio delle Armi di Tyris: le Reclame~",
    "～もう化かされない！魔物の罠の見抜き方～": "~Non ci Casco Più! Come Scoprire i Trucchi dei Mostri~",
    "～訓練所の張り紙～": "~Avviso Affisso alla Palestra~",
    "～サメ信者大全～": "~Grande Compendio dei Fedeli dello Squalo~",
    "～職人が教える武器の歴史～": "~La Storia delle Armi Raccontata da un Artigiano~",
    "～姉波動聖典～": "~Il Testo Sacro dell'Onda Sororale~",
    "～進め！オカルト探検隊～": "~Avanti! Squadra Esploratrice dell'Occulto~",
    "～イルヴァ昆虫大百科～": "~Grande Enciclopedia degli Insetti di Irva~",
    "～イルヴァ昆虫大百科注釈～": "~Grande Enciclopedia degli Insetti di Irva: Note~",
    "～無名吟遊詩人の短歌～": "~Le Liriche di un Bardo Senza Nome~",
    "～図解・忍者のひみつ１００選～": "~Illustrato: Cento Segreti del Ninja~",
    "～君にもできるサバイバル～": "~La Sopravvivenza Alla Portata di Tutti~",
    "～危険物取扱マニュアル～": "~Manuale per il Maneggio di Materiali Pericolosi~",
    "～夢の廃物利用～": "~Il Sogno di Riusare gli Scarti~",
    "～根元の濡れた標識～": "~Il Cartello Bagnato alla Base~",
    "～必見！貯蓄型資産運用のすべて～": "~Da Vedere! Tutto sul Risparmio e sugli Investimenti~",
    "～発見！世界の珍品～": "~Scoperta! Le Rarità del Mondo~",
    "～古代道具の謎に迫る！～": "~All'Inseguimento del Mistero degli Arnesi Antichi!~",
    "～道端の危険物～": "~I Pericoli sul Ciglio della Strada~",
    "～少女の寝言～": "~Le Parole nel Sonno di una Bambina~",
    "～添えられた説明書～": "~Il Foglietto delle Istruzioni Allegato~",
    "～不思議なノートの走り書き～": "~Scarabocchi su un Quaderno Misterioso~",
    "～奇妙な噂話～": "~Dicerie Bizzarre~",
    "～古代祭事のルーツに迫る～": "~Alle Radici degli Antichi Riti~",
    "～食べられる草、食べられない草～": "~Erbe che si Mangiano ed Erbe che Non si Mangiano~",
    "～森林と経済活動・製材編～": "~Foreste ed Economia: la Segheria~",
    "～特集・幻の植物を追う～": "~Speciale: sulle Tracce delle Piante Leggendarie~",
    "～特選！裏の嗜好品～": "~Selezione! I Piaceri Clandestini~",
    "～アイオンの予言～": "~La Profezia di Aion~",
    "～イルヴァ航空販売カタログ～": "~Catalogo di Vendita di Irva Airlines~",
    "～ネクロマンサー入門～": "~Negromanzia per Principianti~",
    "～謎のメモ～": "~Appunto Misterioso~",
    "～謎のレポート～": "~Rapporto Misterioso~",
    "～戦場における指揮統制～": "~Comando e Controllo sul Campo di Battaglia~",
    "～毒物薬物辞典～": "~Dizionario dei Veleni e dei Farmaci~",
    "～インテリアパラダイス増刊号～": "~Interior Paradise: Numero Straordinario~",
    "～おしゃれアイテム大特集～": "~Grande Speciale sugli Oggetti alla Moda~",
    "～裁縫大百科～": "~Grande Enciclopedia del Cucito~",
    "～特集・機械文明の遺産～": "~Speciale: l'Eredità della Civiltà Meccanica~",
    "～錬金術入門書～": "~Manuale d'Introduzione all'Alchimia~",
    "～袋の裏に書かれた端書～": "~Postilla Scritta sul Retro del Sacco~",
    "～箱裏に書かれた注意書き～": "~Avvertenza Scritta sul Retro della Scatola~",
    "～説明書の最後のページに書かれた文字～": "~Le Parole sull'Ultima Pagina del Manuale~",
    "～妹研究の第一人者モクシスの研究論文～": "~Studio di <Moxis>, massimo esperto di sorelle minori~",
    "～囚人達が選ぶ、人気商品ベスト５０～": "~I 50 Prodotti Preferiti dai Detenuti~",
    "～ヴェルニースの雑貨店に張られた広告～": "~Reclame Affissa al Bazar di Vernis~",
    "～トレーニングマシーンの隅にかけられた謎の説明文～": "~Istruzioni Misteriose in un Angolo dell'Attrezzo~",
    "～挟まれていた紙片の殴り書き～": "~Scarabocchio sul Foglietto Infilato Dentro~",
    "～特別な孫の言葉～": "~Parole di un Nipote Speciale~",
    "～犠牲者の言葉～": "~Le Ultime Parole della Vittima~",
    "～呪われた者の言葉～": "~Parole di Chi è Stato Maledetto~",
    "～慌てる市民の言葉～": "~Parole di un Cittadino in Affanno~",

    # --- le divinita': l'epiteto sta nel giapponese, il nome e' gia' deciso -
    "～《剛石のウリカグアル》の言葉～": "~Parole di <Urcaguary>~",
    "～《地のオパートス》の言葉～": "~Parole di <Opatos>~",
    "～《守護のロヴィト》の言葉～": "~Parole di <Rovid>~",
    "～《癒しのジュア》の言葉～": "~Parole di <Jure>~",
    "～《砂嵐のラシエル》の言葉～": "~Parole di <Arasiel>~",
    "～《風のルルウィ》の言葉～": "~Parole di <Lulwy>~",
    "～《機械のマニ》の言葉～": "~Parole di <Mani>~",
    "～《鉄騎のガルジエム》の言葉～": "~Parole di <Garziem>~",
    "～《富のヤカテクト》の言葉～": "~Parole di <Yacatect>~",
    "～《歌踊のカラヴィカ》の言葉～": "~Parole di <Karavika>~",
    "～《叡智のソピアー》の言葉～": "~Parole di <Sophia>~",
    "～《元素のイツパロトル》の言葉～": "~Parole di <Itzpalt>~",
    "～《不幸のシナア》の言葉～": "~Parole di <Sinaha>~",
    "～《幸運のエヘカトル》の言葉～": "~Parole di <Ehekatl>~",
    "～《収穫のクミロミ》の言葉～": "~Parole di <Kumiromi>~",
    "～《永遠のネヘルタード》の言葉～": "~Parole di <Amurdad>~",
    "～富の女神の言葉～": "~Parole della Dea del Tesoro~",
    "～破壊の神の言葉～": "~Parole del Dio della Distruzione~",
    "?ジュアの狂信者の独り言?": "~Monologo di un Fanatico di Jure~",

    # --- le persone: l'epiteto lo tiene il giapponese ------------------------
    "～ザナンの紅の英雄『ロイター』の言葉～": "~Parole di <Loyter> l'eroe cremisi di Zanan~",
    "～機甲将軍『アインリッヒ』の言葉～": "~Parole di <Heinrich> il generale corazzato~",
    "～特殊部隊長『ミーリス』の言葉～": "~Parole di <Milis> la comandante delle forze speciali~",
    "～開発主任『ガベラ』の言葉～": "~Parole di <Gavela> l'ingegnere capo~",
    "～生化学者『イコール』の言葉～": "~Parole di <Icolle> il biochimico~",
    "～ガイドの『ノルン』の言葉～": "~Parole di <Norne> la guida~",
    "～遺跡研究者『メローキア』の言葉～": "~Parole di <Melochea>, studiosa di rovine~",
    "～伝説の職人『ガロク』の言葉～": "~Parole di <Garok> il fabbro leggendario~",
    "～異形の森の使者『ロミアス』の言葉～": "~Parole di <Lomias> il messaggero di Vindale~",
    "～盗賊ギルドマスター『シン』の言葉～": "~Parole di <Sin> il maestro della Gilda dei Ladri~",
    "～盗賊ギルドの番人『アビス』の言葉～": "~Parole di <Abyss> il guardiano della Gilda dei Ladri~",
    "～稀代の怪盗『マークス』の言葉～": "~Parole di <Marks>, ladro senza pari~",
    "～こそどろのグリドの言葉～": "~Parole di <Gleed> il topo d'appartamento~",
    "～ならずもののオネストの言葉～": "~Parole di <Onest> il farabutto~",
    "～街の子供のセスの言葉～": "~Parole di <Seth>, ragazzino di città~",
    "～掃除屋『バルザック』の言葉～": "~Parole di <Balzak> il custode~",
    "～猫嫌いの『タム』の言葉～": "~Parole di <Tam> il nemico dei gatti~",
    "～青い髪の『ヴァリウス』の言葉～": "~Parole di <Barius> dai capelli blu~",
    "～見世物屋の『モイアー』がガラクタを売り付ける際の口上～": "~La Cantilena di <Moyer> l'imbonitore~",
    "～悩める魔術士『レントン』の言葉～": "~Parole di <Renton> il mago tormentato~",
    "～見習い騎士『アインク』の言葉～": "~Parole di <Ainc> il cavaliere novizio~",
    "～女たらしの『ラファエロ』の言葉～": "~Parole di <Raphael> il donnaiolo~",
    "～爆弾魔『ノエル』の言葉～": "~Parole di <Noel> la dinamitarda~",
    "～無邪気な少女『グウェン』の言葉～": "~Parole di <Gwen> l'innocente~",
    "～歴史を学ぶ『エリステア』の言葉～": "~Parole di <Erystia> la studiosa di storia~",
    "～妄想少女『リアナ』の言葉～": "~Parole di <Rianna> la sognatrice~",
    "～子犬の『ポピー』の言葉～": "~Parole di <Poppy> il cagnolino~",
    "～貴族のラスター、最後の言葉～": "~Le Ultime Parole di <Luster> il nobile~",
    "～偉大なる料理評論家グラトナの言葉～": "~Parole di <Gratona>, grande critico gastronomico~",
    "～金毛九尾の言葉～": "~Parole della Volpe a Nove Code dal Manto d'Oro~",
    "～麻酔の射手の言葉～": "~Parole del Tiratore Anestetista~",
    "～熟練狩人の言葉～": "~Parole del Cacciatore Esperto~",
    "～敗北者のうめき声～": "~Il Gemito dello Sconfitto~",
    "～涙目の煽りイカの言葉～": "~Parole del Calamaro Provocatore con gli Occhi Lucidi~",
    "～ペットトレイナーの言葉～": "~Parole dell'Addestratore di Bestie~",
    "～鎖自慢された奴隷の言葉～": "~Parole di uno Schiavo Fiero delle Sue Catene~",
    "～退屈ネクロマンサーの言葉～": "~Parole di un Negromante Annoiato~",
    "～困惑する素人の言葉～": "~Parole di un Profano Disorientato~",
    "～解説中のマニアの言葉～": "~Parole di un Fissato in Piena Spiegazione~",
    "～ザナン研究員の言葉～": "~Parole di un Ricercatore di Zanan~",
    "～邪悪な魔法使いの言葉～": "~Parole di un Mago Malvagio~",
    "～釣り自慢のフィッシャーの言葉～": "~Parole di un Pescatore Fiero della Sua Preda~",
    "～現場を見た専門家の言葉～": "~Parole di un Esperto che ha Visto la Scena~",
    "～自称天才魔道具技師の言葉～": "~Parole di un Sedicente Genio degli Arnesi Magici~",
    "～隅に記された魔女の言葉～": "~Parole di una Strega Scritte in un Angolo~",
    "～混乱する店員の言葉～": "~Parole di un Commesso Confuso~",
    "～ソックスソードマンの評価～": "~Il Giudizio del Sockswordman~",
    "～はく製マニアからの手紙～": "~Lettera di un Fissato di Tassidermia~",
    "～ブランケットにくるまった少女の言葉～": "~Parole di una Bambina Avvolta in una Coperta~",
    "～スンバラリア星人の言葉～": "~Parole di un alieno di Sunbararia~",
    "～廃業寸前のキャラメル職人の言葉～": "~Parole di un Caramellaio sull'Orlo del Fallimento~",
    "～迫り来る妹の言葉～": "~Parole della Sorella Minore che si Fa Sotto~",
    "～吐き気をこらえる少女の言葉～": "~Parole di una Bambina che Trattiene la Nausea~",
    "～裏路地の老店主の言葉～": "~Parole del Vecchio Bottegaio del Vicolo~",
    "～目覚めてしまった冒険者の言葉～": "~Parole di un Avventuriero che si è Risvegliato~",
}

# ---------------------------------------------------------------------------
# Le righe MUTE: il ramo giapponese non le ha (le mette in un altro indice, o
# non ce l'ha). Li' l'inglese e' l'unica fonte.
# ⚠️ I quattro «rapporti di identificazione» il giapponese ce l'ha, ma
# nell'INDICE 3 — dove `trimdesc(desc, 1)` lo tronca al primo `#` e non arriva
# mai a schermo. La forma e' `～鑑定報告書：＜食物＞カテゴリ～`, e le categorie
# sono quelle del gioco.
# ---------------------------------------------------------------------------

TITOLI_EN = {
    "~Identification Report: <Food> Category~":
        "~Rapporto di Identificazione: categoria <Cibo>~",
    "~ Identification Report <Item> Category~":
        "~Rapporto di Identificazione: categoria <Oggetti>~",
    "~Identification Report: <Seaweed> Category~":
        "~Rapporto di Identificazione: categoria <Alghe>~",
    "~Identification Report: <Plants> Category~":
        "~Rapporto di Identificazione: categoria <Piante>~",
    "a Eulderna Researcher": "un ricercatore Eulderna",
    "a Eulderna Researcher handling this tome":
        "un ricercatore Eulderna che maneggia questo tomo",
    "a Eulderna Researcher holding this tome":
        "un ricercatore Eulderna che tiene in mano questo tomo",
    "outcast Eulderna Researcher": "un ricercatore Eulderna ripudiato",
    "~some Eulderna Pyromaniac~": "~un piromane Eulderna~",
    "Bureau of Eulderna Punditry (BEP)":
        "Ufficio Eulderna degli Studi Dotti (UESD)",
    "~Jonah, the Adventurer~": "~<Jonah> l'avventuriero~",
    "~Lane, the Fairy Invoker~": "~<Lane>, evocatrice di fate~",
    "~some weird old guy~": "~un vecchio bizzarro~",
    "~some Bearded Guy~": "~un tizio con la barba~",
    "~a Mysterious Note~": "~un appunto misterioso~",
    "~words on the cover~": "~parole sulla copertina~",
    "~words of a ex-excutioner~": "~parole di un ex boia~",
    "arrested arsonist": "un incendiario in arresto",
    # ⚠️ questo titolo esiste due volte: una col giapponese (～遺跡荒らしのメモ～)
    # e una senza. La resa e' la stessa, o la famiglia si spacca su una riga.
    "~memo of a grave robber~": "~Appunti di un Predone di Rovine~",
}
