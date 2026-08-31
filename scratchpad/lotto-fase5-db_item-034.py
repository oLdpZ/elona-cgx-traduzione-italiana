# -*- coding: utf-8 -*-
"""115a - Lotto 034 di `db_item.hsp`: GLI ATTREZZI, seconda parte.

`FILTER_ITEM_TOOL`, righe 48.000-62.000: **44 righe** su 39 oggetti — 39
dell'indice 0, 1 dell'indice 1 e 4 dell'indice 2. Segue il 033, che aveva preso
le prime 50 righe della categoria fino a `:47288`.

La taglia e' stata scelta guardando il numero che `_corpo.py` stampa: `0 48000`
dava 38, `0 62000` ne da' 44, `0 64000` 55, `0 70000` 73. Un lotto sano sta fra
le 30 e le 55.

### ⭐⭐⭐ L'INGLESE E' SLITTATO DI UNA POSIZIONE, E LO DICONO LE CODE

Tre righe di due oggetti diversi portano un inglese che appartiene alla riga
**precedente della catena**:

    :50410  (convertitore, indice 2)  jp VUOTO      en «if the skill is too low…»
    :51288  (detriti, indice 0)       jp enciclopedia  en «treasures that provide
                                                          experience…»
    :51289  (detriti, indice 1)       jp «tesoro che da' esperienza»
                                      en «if the skill is too low…»

Il giapponese di `:51289` e' quello che l'inglese mette a `:51288`; l'inglese di
`:51289` e' quello che appartiene a `:50410`, dove il giapponese **non c'e'**.

⭐ **A dirlo con certezza sono le code, che invece sono al posto giusto**:
`:51288` ha ～イルヴァ幻想辞典～ / `~Irva Fantasy Encyclopedia~` in tutt'e due le
lingue, `:51289` ha ～遺跡荒らしのメモ～ / `~memo of a grave robber~` in tutt'e
due. La coda dice a quale fonte appartiene il testo, e il corpo inglese non le
corrisponde. Senza le code sarebbero state due prose plausibili e nessuno
avrebbe visto niente.

Si segue il giapponese (109a), e a `:50410` — che un giapponese non ce l'ha —
si segue l'inglese, che li' e' quello giusto: parla davvero del convertitore.

### ⚠️⚠️ E LE DUE RIGHE HANNO L'INGLESE IDENTICO, MA NON LA STESSA FIRMA

`:50410` e `:51289` portano lo **stesso identico inglese**, 229 caratteri. E'
l'unica coppia del lotto che condivide un testo, e sembrava il moltiplicatore
del 033 — una resa sola per due righe, con l'obbligo di scegliere quale dei due
sensi sacrificare.

Non lo e': `estrai.firma()` e' `sha1(giapponese + \\x00 + inglese)`, e il
giapponese qui e' diverso (uno e' la stringa **vuota**). Due firme, due voci,
due rese indipendenti. ⭐ Il difetto di monte si puo' riparare **su tutt'e due i
siti**, senza toppe e senza scegliere.

⚠️ La lezione: prima di dare per gemelle due righe con l'inglese uguale si
guarda il **giapponese**, perche' e' meta' della chiave. Un inglese uguale non
basta a fondere due firme.

### ⭐⭐⭐ I QUATTRO POTIO-MAN: L'INGLESE APPIATTISCE QUATTRO FRASI IN UNA

`:50474`, `:50540`, `:50606`, `:50672` sono quattro modelli dello stesso
giocattolo. Il loro giapponese ha la stessa struttura e **due** frasi che
cambiano: la seconda e l'ultima. L'inglese copia l'ultima fedelmente, ma al
posto della seconda scrive in tutt'e quattro «Its wielder is called a Potioner»,
che e' la seconda frase del **solo** `:50474`.

    :50474  これの使い手はポーショナーと呼ばれる    (il nome di chi lo usa)
    :50540  時代に合わせて色々な飲み物の栓が…      (i tappi usati nel tempo)
    :50606  地域によってはコルクマンと呼ぶ…        (come lo chiamano altrove)
    :50672  使ったポーションの数だけ弾数が増える…  (quante cariche ha)

Quattro rese diverse dove l'inglese ne aveva una. E' il verso opposto della
lezione del 033 sulle quattro carte: li' il giapponese era identico e l'inglese
distingueva, e le rese erano **una sola** ripetuta.

⚠️ `ポーショナー` e `コルクマン` non stanno in nessun dizionario: sono nomi che
nascono qui. «pozionista» e «uomo di sughero» — il secondo e' un soprannome
locale, e va reso, non traslitterato.

### ⭐⭐ I TRE GLOBI OSCURI: L'INGLESE DICE «SP» TRE VOLTE, IL GIAPPONESE NO

`:50945` (verde), `:51012` (blu), `:51079` (cremisi) hanno lo stesso testo a
meno del colore e della risorsa consumata. Il giapponese dice **ＳＰ, ＭＰ,
ＨＰ**; l'inglese scrive «SP» in tutt'e tre. E' un fatto di gioco, e la quinta
fonte (110a) e' il codice: si segue il giapponese.

⭐ **Il （未実装） qui regge, e lo conferma il codice.** Nel 033 il giapponese
diceva «non implementato» di un oggetto che funzionava, e aveva vinto il codice.
Qui e' il contrario: `action.hsp:15047-15059` ha i tre rami dei globi, e il
verde arriva a `txt lang("開発中。", "Under development.")`; gli altri due non
fanno **niente**. Il giapponese e il codice dicono la stessa cosa.

⚠️ La resa e' modellata sul **fratello bianco** `:45481`, gia' reso nel 033
(111a: la famiglia batte il lotto). «Per classificazione» resta com'e' li',
anche se e' di 15 caratteri e la finestra di rinculo e' 15: il cancello delle
parole spezzate misura la **posizione**, non la lunghezza, e nel 033 quella
stessa parola e' passata. Se si accende, si riscrive.

### ⚠️⚠️ IL DIZIONARIO FANTASTICO E' DI DUE CITTA', E L'INGLESE NE CONOSCE UNA

`:52380` (il Moku-Jin) porta la coda ～イムウエル幻想辞典～, cioe' **Aimwell**;
tutte le altre dodici del lotto portano ～イルヴァ幻想辞典～, Irva. L'inglese
scrive `~Irva Fantasy Encyclopedia~` per tutt'e due.

イムウエル e' gia' reso «Aimwell» altrove nel dizionario (due erbe di Tyris del
Nord e una mappa), e la tabella della 112a gli da' gia' `~Dizionario Fantastico
di Aimwell~`. Non c'e' niente da decidere: c'e' da non appiattire.

⚠️⚠️ **CONSEGUENZA ANNUNCIATA PRIMA DI MISURARLA**: il cancello «titoli resi in
PIU' modi» di `_112-corpo-descrizioni` chiava sull'**inglese**, quindi dopo
questo lotto passa da **2 a 3**, e il terzo e' `Irva Fantasy Encyclopedia` ->
Irva / Aimwell. E' il terzo appiattimento dell'inglese, non una nostra
divergenza. Un **4** sarebbe un difetto nuovo.

### ⚠️ LA FONTE CHE L'INGLESE SCRIVE SENZA TILDE

`:52047` e' l'unica riga del lotto la cui coda inglese e'
`# Words of the Goddess of Wealth`: il `#` c'e', le tilde no. Il giapponese le
ha (～富の女神の言葉～), e tutte le altre 233 fonti della famiglia le hanno.

Si conserva il `#` **col suo spazio**, come vuole la regola del 033 sui `#`
perduti, e si rimettono le tilde, che sono la forma della fonte e non un vezzo
dell'inglese. ⓘ `_code.py` da solo qui sbaglia: la sua `marca` e' il prefisso
dell'inglese fino alla prima tilde, e senza tilde ripiega su `#` perdendo lo
spazio. Il file `_traduzioni034.py` lo corregge a mano.

### ⭐ L'INGLESE DEL KISERU DICE «PELLE» DOVE IL GIAPPONESE DICE CARISMA

I quattro oggetti da fumo (`:60914` kiseru, `:60980` pipa, `:61046` hamaki,
`:61112` sigaretta) crescono quattro attributi diversi: 魅力 Carisma, 習得
Apprendimento, 器用 Destrezza, 感覚 Percezione. Sul kiseru l'inglese scrive
«ingredients thats beneficial to the skin»: la pelle non c'entra niente, e non
e' un fatto di gioco vago — e' l'attributo che l'oggetto alza.

I nomi dei quattro attributi si copiano da `skill.hsp`, dove sono gia' resi
(Carisma, Apprendimento, Destrezza, Percezione), e la formula e' la stessa per
tutt'e quattro: «fanno crescere l'attributo X». ⓘ «l'attributo» non e'
un'aggiunta gratuita: `l'Apprendimento` misura 15 caratteri e la finestra di
rinculo e' 15. Serviva un confine, e il gioco quella parola la usa gia'
(«Attributi base», `command.hsp:10416`).

### ⓘ Gli altri termini cercati a mano nel dizionario

Le reti non leggono il glossario (regola della 111a), quindi: 富の女神 «la dea
della ricchezza» in prosa e «Yacatect» come nome; ヤカポイント «YacaPoint»
invariato; 龍脈 «la vena del drago» (`chat.hsp`); 決戦因子 «Fattore Decisivo»;
はく製 «statuetta»; アーティファクト «artefatto»; ケサランパサラン
«kesaranpasaran»; 雑貨店 «merceria»; テスカトリポカ «Tezcatlipoca»; ゼーム
«Zeome»; 魔石 «pietra magica»; 生化学文明 «civilta' biochimica»; スタミナ
«resistenza» in prosa.

⚠️ `:52380` obbedisce al nome **non identificato** dell'oggetto («bambola di
legno»), non a quello identificato (`<Moku-Jin>`): la prosa del pannello si
legge anche prima di identificare.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :49776
    (49776, 'Water bottles manufactured at the end of the biochemical civilization. It is equipped with an advanced filtration mechanism and can somehow make contaminated water drinkable. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una borraccia costruita alla fine della civiltà biochimica. Monta un filtro di grado avanzato, e anche l'acqua sporca, se ce n'è in quantità, riesce in qualche modo a renderla bevibile. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :49847
    (49847, 'Distorted crystals spilled from Tezcatlipoca. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme caduto da Tezcatlipoca. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :49918
    (49918, 'Distorted crystals found inside the body of the deformed angel. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme trovato nel corpo di un angelo mostruoso. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :49989
    (49989, 'Distorted crystals kept by Zeome. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme che Zeome teneva in custodia. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50060
    (50060, 'The hand that holds the power of God. The story of the Golden King of Donkey Ears, who once held the same power in his hands, who defeated tragedy with the power of love, is all too well known. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una mano in cui alberga la forza di un dio. È fin troppo nota la storia del re d'oro dalle orecchie d'asino che, avendo un tempo avuto in mano la stessa forza, spezzò la tragedia con la forza dell'amore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50131
    (50131, 'Patrol program composed of photons. It flies around at the speed of light to collect information or, conversely, to spread information. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un programma di pattuglia fatto di fotoni. Vola in giro alla velocità della luce e raccoglie informazioni, oppure al contrario le diffonde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50202
    (50202, "Divine medal of honor. It symbolizes the strength to carry oneself through and the strength to protect what needs to be protected, even to the point of abandoning oneself. It has strong power, but if you don't use it thoughtfully, you will die without being able to protect or carry through anything. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una medaglia divina. Simboleggia due forze: quella di tenere fede a sé stessi fino in fondo e quella di difendere fino in fondo ciò che va difeso, anche a costo di rinunciare a sé. Racchiude un gran potere, ma se non la si usa con giudizio si finisce col morire senza aver difeso né tenuto fede a niente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50271
    (50271, 'A license prepared by God. In modern Irva, marriage is not permitted without first becoming partners. However, if the couple confronts the marriage partner with this, the marriage is possible. Of course, the other party has the right to refuse. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un permesso preparato da un dio. Nell'Irva di oggi non ci si può sposare se prima non si è compagni. Ma sbattendo in faccia questo foglio il matrimonio diventa possibile. Certo, l'altro ha sempre il diritto di dire di no. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50341
    (50341, 'An access key that calls up a floating fortress in spatial submergence. However, it has been modified in some way, with obviously non-standard electronic components attached externally. \\n# ~Irva Fantasy Encyclopedia~'):
        "La chiave d'accesso che richiama la fortezza volante immersa nello spazio. Qualcuno però l'ha modificata: ci sono attaccati fuori dei pezzi elettronici palesemente fuori standard. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50408
    (50408, "Mysterious crystals found inside a Nefia guardian's body. It is said to generate power by compounding with memories. Similar crystals were reportedly found inside the bodies of patients suffering from Nephia Syndrome. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un cristallo misterioso che si trova nel corpo dei guardiani. Dicono che generi forza combinandosi con la memoria. C'è anche un referto di quando fu aperto il corpo di un malato terminale di sindrome di Nefia: dentro gli si stava formando un cristallo uguale. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50410
    (50410, 'It seems that if the relevant skill is too low, it cannot be converted into a bonus and the skill itself will be gone. There is no such thing as an unnecessary skill, so it seems difficult to utilize. \\n# ~memo of a grave robber~'):
        "Pare che se l'abilità in questione è troppo bassa non si converta in bonus e sparisca del tutto. E siccome abilità inutili non ce ne sono, sfruttarlo sembra difficile. \\n# ~Appunti di un Predone di Rovine~",

    # ---------------------------------------------------------- :50474
    (50474, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. This Potio-man is the self-powered type, and it uses the absorbed magical power efficiently.\\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. Chi lo maneggia lo chiamano pozionista. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che ha una coscienza propria, e la forza magica assorbita la usa con criterio.\\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50540
    (50540, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Potio-man of this model can be synchronized to fire an attached grenade.\\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. Nel tempo, dicono, come proiettili sono stati usati i tappi delle bevande più varie. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che, se lo si sincronizza, spara una granata montata fuori.\\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50606
    (50606, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Potio-man of this model is equipped with a transparent shield, and raises one's defensive power for a while after firing. \\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. In certe zone lo chiamano anche uomo di sughero. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo con lo scudo mezzo trasparente, pensato per gli scontri a fuoco: dopo il colpo la difesa sale per un po'. \\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50672
    (50672, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Prototype Potioman that has no consideration of holding back power, it is easy to increase its power by grip strength. \\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. I colpi crescono col numero di pozioni usate, ma i tappi dei contenitori fuori dal comune hanno un altro diametro e non vanno. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il primo tipo, che non bada a dosare la forza: con la presa salda la potenza sale in fretta. \\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50746
    (50746, 'Board with various instruments, panels, and LCDs. A high level of information processing capability is required to handle all the functions. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un pannello con sopra strumenti di misura, quadri e schermi a cristalli liquidi. Per usarne bene tutte le funzioni ci vuole una gran capacità di elaborare informazioni. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :50945
    (50945, "Green stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra verde che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di SP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51012
    (51012, "Blue stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra blu che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di MP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51079
    (51079, "Red stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra cremisi che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di HP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51288
    (51288, 'These are treasures that provide experience, or even knowledge of the skill. In rare cases, some people are incapable of acquiring skills this way due to body rejection? \\n# ~Irva Fantasy Encyclopedia~'):
        "I detriti che lascia chi è diventato guardiano. Ci abita ancora un poco del sapere che la Nefia gli ha dato, delle tecniche di un tempo, dei ricordi del guardiano stesso. Se ne possono assorbire tecniche e sapere, ma insieme entra la memoria di un altro e c'è da uscire di senno. E se li usasse un malato terminale di sindrome di Nefia, perderebbe conoscenza e diventerebbe lui il nuovo guardiano della Nefia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51289
    (51289, 'It seems that if the relevant skill is too low, it cannot be converted into a bonus and the skill itself will be gone. There is no such thing as an unnecessary skill, so it seems difficult to utilize. \\n# ~memo of a grave robber~'):
        "Un tesoro che, se l'abilità già ce l'hai, ti dà esperienza, e se non ce l'hai te la fa imparare. Pare che di rado ci sia chi per rigetto non riesce a impararle: sarà vero? \\n# ~Appunti di un Predone di Rovine~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :51290
    (51290, '\\"Those who are resistant won\'t be taken in by Nefia and can gather memory fragments to make them stronger. There are loopholes in everything. ...No, wait. What if the original purpose of this item is to concentrate power on those who are resistant?\\" \\n# ~words of <Melochea> the Nefia Researcher~'):
        "\\\"Chi ha resistenza non viene inghiottito dalla Nefia e può farsi forte raccogliendo detriti. Una falla c'è sempre, in ogni cosa. ...No, aspetta. E se lo scopo vero fosse proprio concentrare la forza su chi resiste...?\\\" \\n# ~Parole di <Melochea>, studiosa di rovine~",

    # ---------------------------------------------------------- :51979
    (51979, 'Smoke screen generators have been used and developed by the ninja since ancient times. Older models required a fire to be lit, but modern ones no longer require ignition. When thrown, it deploys a smoke screen to block vision. The smoke screen blocks most long-range attacks, allowing the ninja to escape or surprise the enemy and destroy them individually. Some schools of ninjutsu do not use this method, but instead generate smoke by themselves. \\n# ~100 Secret of the Ninja - Illustrated~'):
        "Un apparecchio che genera cortine di fumo, usato e affinato dai ninja fin dall'antichità. I modelli vecchi andavano accesi, quelli di oggi no. Lanciandolo stende una cortina che toglie la vista. La cortina ferma quasi tutti gli attacchi da lontano, e in quel varco si può fuggire oppure piombare addosso al nemico e farlo fuori uno per volta. Dicono che fra le arti ninja ci sia anche qualche scuola che il fumo se lo fa da sé, senza questo. \\n# ~Illustrato: Cento Segreti del Ninja~",

    # ---------------------------------------------------------- :52045
    (52045, 'Cards issued by the Goddess of Wealth. They are apparently aimed at protecting and fostering merchants and promoting economic activity. Yaca points are added according to shop sales and customer traffic. The maximum amount of points is 100,000, so use them in moderation. \\n#~Merchant Life Starting from a Quitting as a Adventurer~'):
        "La carta che emette la dea della ricchezza. Pare che serva a proteggere e far crescere i mercanti e a dare una spinta all'economia. I YacaPoint si accumulano in base agli incassi del negozio e a quanta gente ci entra. Il tetto è di centomila punti, quindi conviene spenderli ogni tanto. \\n#~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :52047
    (52047, '\\"You get five times the Yaca points every December! Plan your year-end sales!\\" \\n# Words of the Goddess of Wealth'):
        "\\\"Ogni anno a dicembre i YacaPoint valgono cinque volte tanto! Le vendite di fine anno organizzatele bene!\\\" \\n# ~Parole della Dea del Tesoro~",

    # ---------------------------------------------------------- :52380
    (52380, 'A wooden person made to resemble a humanoid. You can train your weapon skills by using this wooden person as a combatant. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una bambola di legno fatta a somiglianza di una figura umana. Prendendola per avversario ci si allena nelle abilità con le armi. \\n# ~Dizionario Fantastico di Aimwell~",

    # ---------------------------------------------------------- :52382
    (52382, '\\"You\'ve been waiting in that cave for years... for your master who never returned, for years.\\" \\n# ~<Norne> the guide~'):
        "\\\"Tu in quella grotta hai aspettato tutto il tempo... padroni che non tornavano, tanti, per anni e anni.\\\" \\n# ~Parole di <Norne> la guida~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :52446
    (52446, 'Assorted farming tools. Provides growth acceleration and quality improvement to crops. Selects work methods and creates an environment in which certain varieties grow to their advantage. For this reason, other varieties in the mix will lose the growth competition and become nutrients. Note that the work consumes stamina. \\n# ~Agriculture and its New Possibilities~'):
        "Un assortimento di attrezzi da campo. Fa crescere prima le colture e ne alza la qualità. Si sceglie il modo di lavorare e si prepara il terreno perché una certa varietà cresca avvantaggiata; per questo le altre varietà mescolate perdono la gara e finiscono per farle da concime. Attenzione: il lavoro consuma resistenza. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",

    # ---------------------------------------------------------- :54885
    (54885, 'A reasonably sized branch that for some reason has fallen around. It can start a fire. \\n# ~Survival that Anyone Can Do~'):
        "Un ramo di misura giusta, che chissà come sta lì per terra. Serve ad accendere il fuoco. \\n# ~La Sopravvivenza Alla Portata di Tutti~",

    # ---------------------------------------------------------- :55142
    (55142, "A stabilizing device used to suppress hand shaking and to absorb the recoil received by the shooter and the gun mount. In addition to enabling precise shooting, it also makes it possible to fire with all one's might without worrying about the recoil. Once the automatic weapon is stuck in the ground, it is released after a certain period of time. Note that you cannot escape during this time. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un fermo che tiene ferma la mano e scarica il rinculo che prendono il tiratore e l'affusto. Rende possibile il tiro di precisione, e permette anche di sparare a più non posso senza badare al rinculo. Si pianta a terra da sé, e dopo un certo tempo si sgancia. Attenzione: nel frattempo non si può scappare. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :55481
    (55481, "Fragments that shine suspiciously to incite desire. Because it is so beautiful, it is sometimes used as a substitute for jewelry. There are rumors that it gives the user the magical power to manipulate traps, and in return, it eats away at one's life... but no one believes it. There is a legend that a long time ago, a demonic god attempting to destroy humanity was defeated and scattered into red fragments, hence the name. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un frammento che brilla in modo torbido, come per attizzare il desiderio. È abbastanza bello da servire al posto di una gemma. Gira anche la voce che dia a chi lo usa la forza magica di manovrare le trappole, e che in cambio gli roda la vita... ma non ci crede nessuno. C'è una leggenda per cui, tanto tempo fa, un dio demoniaco che voleva distruggere gli uomini fu sconfitto e si sparse in schegge rosse: di lì gli viene il nome. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :56603
    (56603, "Legendary ear picks that change size according to the user's thoughts. Whether you are a fairy or a giant, you only need one of these, but you will lose control of it if you are thinking about the wrong thing. If you master the use of this masterpiece, you can remove all the earwax at once, so you just have to train yourself. The fluffy thing attached to the end is artificial kesalanpatharan, which will die if it is not allowed to rest slowly after use. \\n# ~Irva Fantasy Encyclopedia~"):
        "Il leggendario nettaorecchie che cambia misura secondo il pensiero di chi lo usa. Che tu sia una fata o un gigante ne basta uno, ma se pensi a vanvera ti sfugge di mano. Con la pratica si arriva a cavare tutto il cerume in un colpo solo: è un pezzo pregiato, e non resta che allenarsi. Il batuffolo in punta è un kesaranpasaran artificiale, e dopo l'uso, se non lo si lascia riposare con calma, muore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :57063
    (57063, "A large Christmas cake, sold at grocery stores in December, but sometimes left unsold. It's so big that everyone can eat a whole lot of it. Of course, you can have it all to yourself, but that's wasteful; in December, you can develop the art of faith and bring good luck by eating it. \\n# ~North Tyris Travels, Winter Edition~"):
        "Un dolce enorme per il Natale. A dicembre le mercerie cominciano a venderlo, ma qualcuno resta invenduto. È grande, e ci si sazia tutti insieme. Certo, uno può anche tenerselo per sé, ma che tristezza. A dicembre fa crescere l'abilità Fede e porta anche fortuna. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :57645
    (57645, "Plushie of Yacatect holding a goose. It is said to be manufactured at the God's official factory. When gold coins are inserted, it speaks and moves its wings. The gold coins are invested by Yacatect, and generate interest at a rate of 10% per 100 days. In exchange for the high interest rate, the coins cannot be taken out until the 100th day, and after that, the interest will not increase unless additional deposits are made. And when you take it out, a gold coin comes out of its butt. The goose's butt, of course. \\n# ~Must Watch! Everything About Savings and Asset Management~"):
        "Un pupazzo di Yacatect che tiene in braccio un'oca. Pare che lo facciano in una fabbrica ufficiale degli dei. Se ci metti dentro monete d'oro, muove le ali e parla. Le monete le fa fruttare Yacatect: non al decimo giorno, ma al centesimo... un decimo di interesse ogni cento giorni circa. In cambio del tasso alto non si può né mettere né togliere fino al centesimo giorno, e dopo gli interessi non crescono se non si versa altro. E quando le tiri fuori, le monete escono dal sedere. Dell'oca, s'intende. \\n# ~Da Vedere! Tutto sul Risparmio e sugli Investimenti~",

    # ---------------------------------------------------------- :58526
    (58526, 'Bloodstained kodachi, a small dagger. It contains the thoughts of warriors who committed seppuku (ritual suicide) and died with an apology, and when held, the blade will naturally aim at your stomach. When used to apologize, it is reputed to convey one\'s true intentions to the other party. It has much more apologetic power than the \\"Kneeling on the Ground\\" method, and even enemies will let you off the hook for a while. If treated immediately, it will not kill you. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada corta insanguinata. Ci resta addosso il pensiero dei guerrieri che se ne sono andati col seppuku, chiedendo scusa, e a tenerla in mano la lama va da sola verso la pancia. Dicono che usarla per scusarsi faccia arrivare all'altro quanto sei serio. Come forza di scusa vale molto più di un inchino a terra, e perfino chi ti è nemico ti lascia in pace per un po'. Se ci si medica subito non si muore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59523
    (59523, 'Treasure that manipulates the dragon vein leading to Nefia and changes the difficulty level of Nefia. Designed to adjust to the growth of the decisive factor candidate. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma che manovra la vena del drago che porta alle Nefia e ne cambia la difficoltà. Serve a regolarla man mano che cresce chi è candidato a Fattore Decisivo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59658
    (59658, 'A piece of shattered star. They emit a mysterious deep blue light. They are just dust at the beginning, and eventually they will become the foundation of another star. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una scheggia di stella che si è spezzata non reggendo più a esistere. Manda una luce azzurra e cupa, misteriosa. C'è chi la tratta da scarto, ma prima o poi, girando di mano in mano, diventa la base di un'altra stella. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59926
    (59926, "Forbidden device in the era of biochemical civilization. It forcibly extracts the constituent materials from the subject, cultivates them at high speed, and creates a duplicate human being based on the scan data. Since there are no dedicated material transfer facilities left today, the human is reduced to a lump of flesh with no life in it, and the device itself is practically disposable. It is still used by some enthusiasts as a fabricator. Be careful not to use it without the person's permission, as it will make them angry. \\n# ~The Yowyn Book of Secrt Knowledge!~"):
        "L'apparecchio proibito dell'età della civiltà biochimica. Strappa a forza dal soggetto la materia che lo compone, la fa crescere in fretta e, sui dati di una scansione in tre dimensioni, ne cava una copia umana. Oggi gli impianti che trasferivano la materia non ci sono più, quindi ne esce solo un pezzo di carne senza vita dentro, e l'apparecchio stesso è di fatto usa e getta. Con tutto ciò, fra certi appassionati va come macchina per statuette. Attenzione: se lo usi su qualcuno senza il suo permesso, si arrabbia. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :60063
    (60063, 'A collection of disposable abrasives, repair materials, and crafting tools. Comes with instructions. Sold in small quantities by a small number of hill people. Repairing invisible minor damages and misalignments to maximize the performance of the armor. As expected, heavy rust and the like cannot be helped, and we will need some other method. \\n# ~Choosing the Best Tools for the Best Craftsmen~'):
        "Un insieme di paste abrasive usa e getta, materiali da riparo e attrezzi da lavoro fine. Con le istruzioni. Lo vende in piccola quantità un pugno di gente delle colline. Ripara le rotture e gli scarti minimi, quelli che l'occhio non vede, e tira fuori il meglio da armi e armature. Contro una ruggine forte non c'è niente da fare: meglio cercare un'altra strada. \\n# ~Scegliere Bene gli Attrezzi da Artigiano~",

    # ---------------------------------------------------------- :60649
    (60649, 'A cylinder that is sometimes found in archaeological sites along with a special gunpowder ball. Because it does not emphasize killing power, and it can only be shot straight up, experts believe that it may have been a signal bullet in those days. Because the explosion is quite beautiful, it is sometimes used as an ornamental object during festivals in recent years. \\n# ~Mystery of the Ancient Tools!~'):
        "Un tubo che ogni tanto si trova nelle rovine insieme alle sue palle di polvere. Visto che non punta a ferire e che spara solo dritto in alto, gli esperti pensano fosse un razzo di segnale dell'epoca. Lo scoppio è piuttosto bello, e negli ultimi anni lo si usa alle feste per far spettacolo. \\n# ~All'Inseguimento del Mistero degli Arnesi Antichi!~",

    # ---------------------------------------------------------- :60914
    (60914, 'A variant of the smoking pipe. In contrast to the pipe, the smoke is inhaled in a single breath without the use of flavoring. It contains ingredients thats beneficial to the skin, and activate brain cells, and make it possible to tolerate light sleepiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Una variante della pipa da fumo. Al contrario della pipa, il fumo si tira tutto in un fiato, senza aromi. Contiene sostanze che fanno crescere l'attributo Carisma, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :60980
    (60980, 'Wooden smoking utensil. Tobacco leaves are chopped and packed, and then blended with herbs and other flavoring agents. Compared to paper cigars, it is better suited for slowing down and savoring tobacco. It contains ingredients that help grow mastery, activates brain cells, and makes light drowsiness tolerable. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Un attrezzo da fumo di legno. Ci si trita e ci si pigia dentro la foglia di tabacco, e ci si mescola per gusto un aroma di erbe. Rispetto alla sigaretta è fatta per gustare il tabacco con calma. Contiene sostanze che fanno crescere l'attributo Apprendimento, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61046
    (61046, 'Tobacco leaf rolled into a cylindrical shape. Originally, the tip is cut off with a knife, but for those who are lazy, it has been processed so that it can be cut by hand. In addition to containing ingredients that help develop dexterity, it also activates brain cells and makes it possible to tolerate light sleepiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Foglia di tabacco arrotolata a tubo. In origine la punta si taglia con una lama, ma per chi ha poca voglia l'hanno lavorata in modo da poterla staccare a mano. Contiene sostanze che fanno crescere l'attributo Destrezza, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61112
    (61112, 'A tobacco leaf is chopped and rolled up in paper. It has an igniter and can be ignited without any particular ignition device. It contains ingredients that grow the senses, activate brain cells, and make it possible to tolerate light drowsiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Foglia di tabacco tritata e arrotolata nella carta. Ha già l'innesco, e si accende anche senza un accendino. Contiene sostanze che fanno crescere l'attributo Percezione, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

# 39 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-034.jsonl'
RIGHE = {
    49776, 49847, 49918, 49989, 50060, 50131, 50202, 50271, 50341, 50408,
    50410, 50474, 50540, 50606, 50672, 50746, 50945, 51012, 51079, 51288,
    51289, 51290, 51979, 52045, 52047, 52380, 52382, 52446, 54885, 55142,
    55481, 56603, 57063, 57645, 58526, 59523, 59658, 59926, 60063, 60649,
    60914, 60980, 61046, 61112,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
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
