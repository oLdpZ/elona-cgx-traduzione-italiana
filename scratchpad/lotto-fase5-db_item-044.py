# -*- coding: utf-8 -*-
"""116a - Lotto 044 di `db_item.hsp`: I CIBI, il primo lotto della categoria.

`FILTER_ITEM_FOOD`, righe da `:68650` a `:88275`: **39 righe** su 34 oggetti —
34 dell'indice 0, nessuna dell'indice 1 e 5 dell'indice 2. Restano **59 righe**
per due lotti.

⚠️ Previsione di `applica`: **+39**, fatta contando il giapponese nel sorgente
(la lezione del 042). Zero righe gemelle in questo lotto.

### ⭐⭐⭐ `_corpo.py` NON FILTRA LE RIGHE GIA' RESE, E QUI SI E' VISTO

`python _corpo.py 044 FILTER_ITEM_FOOD 0 200000` ha detto **148 righe**, ma
`_114-corpo-da-fare` dice **98 da fare su 148 vive**. Le altre 50 sono gia'
rese: `_107-chiavi-item.py` filtra per categoria, indice e intervallo, e
**basta** — «gia' tradotta» non e' fra i suoi filtri.

⚠️⚠️ Non era mai emerso perche' nelle quattro categorie chiuse finora tutto era
da fare, e i due numeri coincidevano. Su una categoria **cominciata a meta'** un
lotto costruito a occhio dall'uscita di `_corpo.py` riscriverebbe da capo 50
rese gia' in gioco, e **niente lo fermerebbe**: il preflight controlla che le
chiavi siano quelle di `righeNNN.py`, non che siano da fare.

⭐ **Come si e' evitato:** contando prima di scegliere l'intervallo. Le 50 gia'
rese sono un prefisso pulito, `:42782`-`:67985`, e le 98 da fare cominciano a
`:68650`: per questo il lotto parte da 68000. Su un'altra categoria potrebbero
essere sparse, e allora l'intervallo non basterebbe.

### ⭐⭐⭐ UNA RIGA HA IL GIAPPONESE E L'INGLESE CHE PARLANO DI DUE COSE DIVERSE

`:70398` e' l'indice 2 della castagna. Il giapponese e' una battuta:

    「う、うにを粗末にするとバチが当たるんですよ！」
    #～怯える錬金術士の『ナプラス』の言葉～

L'inglese, nella stessa posizione, e' il **testo generico** del rapporto di
identificazione: «A type of nut that restores satiety, it's used to make
candies.» con la coda `~Identification Report: <Food> Category~`.

⚠️ Non e' uno slittamento: si e' guardato il sorgente riga per riga
(`:70392` contro `:70398`), e le posizioni corrispondono. E' una **sostituzione**
fatta a monte, nel ramo inglese.

⚠️⚠️ **E il cancello non se ne accorgeva, per come e' fatto.** `_code.py` cerca
prima la coda giapponese in tabella; ～怯える錬金術士の『ナプラス』の言葉～
non c'era, quindi **ripiegava sull'inglese**, trovava il rapporto di
identificazione e assegnava quel titolo. Il referto «righe senza resa in
tabella: 0» restava verde su una riga sbagliata.

⭐ **Quanto e' grande la famiglia**: `scratchpad/_116-code-discordi.py`, nuovo,
guarda tutte le righe che hanno **tutt'e due** le code e chiede se indicano lo
stesso libro. Su **1.411** righe, le discordi sono **1**: questa. Un difetto
puntuale di monte, non un difetto della nostra estrazione.

**La decisione (dell'utente):** si rende il **giapponese**. Il titolo mancante
e' stato aggiunto alla tabella e al glossario come
`~Parole di <Naplus> l'alchimista spaventata~` — ナプラス e' donna, lo dice
`chat.hsp` («mi ha chiesto di portarle»), e `錬金術士の『ナプラス』` e' gia'
reso «<Naplus> l'alchimista».

⚠️⚠️⚠️ **IL CANCELLO «TITOLI RESI IN PIU' MODI» PASSA DA 6 A 7, ED E' QUESTA
RIGA.** Il settimo e' l'inglese `~Identification Report: <Food> Category~`, che
adesso copre due italiani: il rapporto di identificazione (nelle venti righe di
indice 2 dei cibi, dove il giapponese e' **vuoto**) e le parole di <Naplus>
(qui, dove il giapponese c'e' e dice un'altra cosa). **Il valore atteso in
apertura non e' piu' 6: e' 7.** Un **8** sarebbe un difetto nuovo.

⭐ E la battuta si regge da sola, perche' il dizionario la spiegava gia':
`chat.hsp` dice che «quelli che si dicono alchimisti, quando tirano una
castagna, insistono» che sia un riccio di mare, e 「うにーっ！」 e' reso
«Ricciooo!». Naplus e' una di quelli.

### ⭐⭐ IL LOTTO E' IL PRIMO DISOMOGENEO, E DI MOLTO

    24 righe su 39 hanno lo spazio prima del `\\n`, 15 no
    30 code su 39 sono `#~` senza spazio, 9 sono `# ~` con lo spazio
     1 riga (`:78596`) ha un `\\n` in PIU' in fondo, dopo la coda

Nel 041 le eccezioni erano tre, nel 042 e nel 043 zero. Qui non c'e' una regola
da ricordare: c'e' una tabella da leggere.

⭐ Per questo e' nato `scratchpad/lotti-113/_forma.py NNN`, che mette insieme
in una riga sola quel che prima stava in due strumenti — lo spazio prima del
`\\n` (da `_scheda034.py`) e la coda italiana esatta (da `_code.py`). Il
preflight ha poi trovato l'unica cosa che era sfuggita, il `\\n` in piu' di
`:78596`.

### ⚠️ L'INGLESE LASCIA CADERE TRE FRASI, E UNA CAMBIA IL SENSO

  - `:69598` (il mais): ちなみにヒゲのような部分には利尿作用がある — la barba
    del mais fa venire da urinare. Sparita;
  - `:69669` (la patata): イーモとほぼ同種だが、大きくてやや不格好 — che e'
    quasi la stessa specie dell'**imo**, ma piu' grande e sgraziata. E' la
    **prima** frase, e l'inglese attacca dalla seconda;
  - `:70671` (il granchio del cocco): 弱りはするが — «si indebolisce, si', ma»
    bollirlo non basta a ucciderlo. L'inglese scrive «Although they are boiled
    this way, they are still alive», che perde la concessione e dice una cosa
    piu' forte di quella scritta.

### ⭐ LO ZUCCHERO E IL SALE SONO SPECULARI, E L'INGLESE ROMPE LO SPECCHIO

`:78529` e `:78596` sono in giapponese **la stessa frase** con dolce e salato
scambiati: «aggiunge dolcezza / aggiunge sapore salato... tira fuori il sapore
pieno e il salato / il dolce». L'inglese riscrive la seconda da capo, piu'
lunga e con altre parole. L'italiano tiene lo specchio.

ⓘ Ed e' la riga con il `\\n` in piu': la stessa voce che l'inglese ha riscritto
e' anche l'unica del lotto con la struttura diversa. Le due cose vanno insieme —
qualcuno ha rimesso mano a quella riga sola.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :68650
    (68650, 'Small berries with medicinal properties. When fermented, the toxicity disappears and it makes an excellent ale. On the other hand, when dried, it becomes a highly addictive narcotic, making it a favorite of many smugglers. \\n#~Everchanging Food of Tyris~'):
        "Una bacca piccola che ha proprietà medicinali. A farla fermentare il veleno se ne va e ne viene una birra come si deve. A seccarla, invece, diventa una droga che dà una dipendenza fortissima, e per questo chi la lavora di nascosto non finisce mai. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69527
    (69527, 'A glossy, shiny purple vegetable. The fruit is spongy and easily soaks up water and oil. It has a light flavor and blends well with other ingredients.\\n#~Everchanging Food of Tyris~'):
        "Una verdura viola con una lucentezza lucida. La polpa è come una spugna e si beve facilmente l'acqua e l'olio. Ha un sapore delicato e sta bene insieme agli altri ingredienti.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69598
    (69598, 'Crop with beautifully aligned yellow grains. It is not suitable for eating raw, and the fresh taste at harvest is lost soon after harvest.\\n#~Everchanging Food of Tyris~'):
        "Una pianta bella da vedere, coi chicchi gialli allineati per bene. Cruda non va tanto, e il sapore fresco che ha appena colta lo perde subito dopo. Fra l'altro, la parte che pare una barba fa venire da urinare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69669
    (69669, 'Crop that is suitable for stewing as it does not fall apart when cooked. The skin and buds contain poison, so it is dangerous to scrape them off carefully before eating.\\n#~Everchanging Food of Tyris~'):
        "È quasi la stessa specie dell'imo, ma più grande e un po' sgraziata. Bollendola non si sfa, quindi va bene per gli stufati. Buccia e germogli contengono veleno, e se prima di mangiarla non li togli con cura è pericolosa.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69734
    (69734, 'Fruit combining a refreshing acidity with a rich sweetness. It contains substances that help break down meat and can also tenderize it. Be careful not to eat too much, as it can break down the tissues in the mouth.\\n#~Everchanging Food of Tyris~'):
        "Un frutto che tiene insieme un'acidità fresca e una dolcezza piena. Contiene sostanze che aiutano a disfare la carne, e sa anche renderla tenera. Attento a non mangiarne troppo: disfa anche i tessuti dentro la bocca.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69799
    (69799, 'Fruit with a crunchy texture. Sweet and juicy, but like apples, the core is highly acidic. Universally eaten raw, and were rarely cooked.\\n#~Everchanging Food of Tyris~'):
        "Un frutto che sotto i denti fa croc. È dolce e pieno di succo, ma come nella mela la parte vicina al torsolo è molto acida. Di base si mangia cruda, e cucinarla è raro.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69864
    (69864, 'A slender, curved yellow fruit. Popular as a snack, but also a staple food in some countries due to its high nutritional value and high yield. Note that ripe bananas can quickly become sore if left to ripen.\\n#~Everchanging Food of Tyris~'):
        "Un frutto giallo, lungo e ricurvo. Piace molto come merenda, ma dà molto nutrimento e molto raccolto, e in certi paesi è il cibo principale. Attento: una banana matura, se la lasci lì, si guasta in fretta.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69929
    (69929, 'Fruits known for its high quality. Many farmers aim to make a fortune from high-quality muskmelons. It is not known how they became so different from watermelons.\\n#~Everchanging Food of Tyris~'):
        "Un frutto famoso per essere carissimo. Molti contadini puntano a fare fortuna con meloni di gran qualità. Perché sia finito così lontano dall'anguria non si sa.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :69994
    (69994, 'A close relative of the cucumber, it is a vegetable... but because of its sweetness, it is treated exclusively as a fruit. It is a wonderful fruit that can be smashed with a long stick.\\n#~Everchanging Food of Tyris~'):
        "Una verdura parente stretta della zucca... ma per quanto è dolce la trattano da frutto e basta. E ci si può anche giocare a spaccarla con un bastone lungo: un frutto splendido.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :70396
    (70396, "Nut with a spiky shell. It is still called sea urchin by some people, perhaps because it looks like one. It's shorter spikes makes it an excellent throwing weapon.\\n#~Everchanging Food of Tyris~"):
        "Un frutto chiuso in un riccio pieno di spine. Fino a poco tempo fa lo confondevano col riccio di mare, e forse per questo c'è ancora chi lo chiama riccio. Rispetto al riccio di mare ha le spine più corte, quindi si tira meglio.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :70398
    (70398, "A type of nut that restores satiety, it's used to make candies.\\n#~Identification Report: <Food> Category~"):
        "\\\"R-rovinare un riccio porta castigo!\\\"\\n#~Parole di <Naplus> l'alchimista spaventata~",

    # ---------------------------------------------------------- :70671
    (70671, 'It is a member of the hermit crab family, although it looks a lot like a crab. They are generally distributed in a boiled state because their fibers are tough and tasteless without being cooked. Before being boiled, their body color is dark purple. Although they are boiled this way, they are still alive.\\n#~Everchanging Food of Tyris~'):
        "Somiglia molto a un granchio, ma è parente del paguro. Se non lo si cuoce le fibre restano dure e il sapore è poco, quindi in giro lo si trova quasi sempre già bollito. Prima di bollirlo il colore del corpo è viola scuro. Si indebolisce, sì, ma di regola bollirlo tanto non basta a ucciderlo.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :71163
    (71163, 'Salad made from the vegetative parts of mandrake corpses. It does not contain magic itself, but it does contain a large amount of ingredients that generate magic.\\n#~Everchanging Food of Tyris~'):
        "Un'insalata fatta con la parte vegetale del cadavere di una mandragora. Forza magica non ne contiene, ma è piena di sostanze che la magia la producono.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :71706
    (71706, 'Sweet treats. A strange custom of giving chocolate on certain days to express gratitude has taken hold in recent years. \\n#~Everchanging Food of Tyris~'):
        "Un dolce. Da qualche anno sta prendendo piede l'usanza curiosa di regalare cioccolato in certi giorni per dire grazie. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :73153
    (73153, 'Yith tentacles, chopped into small pieces, are placed in a flour dough and baked into a spherical shape. The secret of this dish is that it contains a trace amount of hallucinogenic ingredients. \\n#~Everchanging Food of Tyris~'):
        "Un piatto fatto tagliando a pezzi i tentacoli della stirpe degli yith, mettendoli in un impasto di farina e cuocendoli a palline. L'ingrediente segreto è la piccola dose di sostanze che fanno vedere le allucinazioni. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74164
    (74164, 'Ingredients unknown. Emits a suspicious odor and makes one want to refuse to eat it. Only those who are prepared to eat it should do so. \\n#~Everchanging Food of Tyris~'):
        "Composizione ignota. Manda un odore sospetto che fa venir voglia di rifiutarsi di mangiarlo. Che lo mangi solo chi si è deciso davvero. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74298
    (74298, 'Strange bentos that instantly turn you into a child when you eat them. \\n#~Everchanging Food of Tyris~'):
        "Un pranzo al sacco misterioso: a mangiarlo si torna bambini in un attimo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74361
    (74361, "Bento box lunches that contain time. Don't eat it. \\n#~Everchanging Food of Tyris~"):
        "Un pranzo al sacco in cui è chiuso il tempo. Non si deve mangiare per nessun motivo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :74631
    (74631, "An icy treat made by pouring syrup over shaved ice. When eaten in a hurry, it causes a sharp headache, which is due to the brain's misidentification of the stimulation to the pharynx. \\n#~Everchanging Food of Tyris~"):
        "Un dolce di ghiaccio, fatto versando lo sciroppo sul ghiaccio tritato. A mangiarlo di fretta viene una fitta alla testa, e il motivo è che il cervello scambia per mal di testa quel che si sente in gola. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :75847
    (75847, 'One of the last products made by a caramel maker in despair after his business failed. It evokes an apocalypse. \\n#~Everchanging Food of Tyris~'):
        "L'ultima cosa che fece un caramellaio disperato perché il lavoro non gli andava. Chiama la fine del mondo. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :75849
    (75849, '\\"Tomorrow is the day for debt collection, and I don\'t have the money ready... I wish the world would end tomorrow...\\" \\n# ~an Indebted Caramel Maker~'):
        "\\\"Domani viene chi riscuote il debito e i soldi non li ho... magari domani il mondo finisse...\\\" \\n# ~Parole di un Caramellaio sull'Orlo del Fallimento~",

    # ---------------------------------------------------------- :76719
    (76719, 'Simple dish of rice, hardened and seasoned with a firm fist. It is characterized by its ability to be eaten quickly, even with one hand. \\n#~Everchanging Food of Tyris~'):
        "Un piatto semplice: riso stretto in mano fino a compattarlo e insaporito. Quel che lo distingue è che si mangia in fretta, anche mentre fai altro. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78115
    (78115, 'The combination of a thick texture and a crunchy texture makes it a popular food. In the past, washed Putits were used directly, but due to numerous incidents of unwary customers being eaten by Putits, they now use Putits that have been put in a state of suspended animation. \\n#~Everchanging Food of Tyris~'):
        "Un cibo che piace per come mette insieme il morbido che si scioglie e i granelli che scrocchiano sotto i denti. Un tempo si usavano putit lavati e basta, ma siccome è successo più volte che un cliente distratto finisse mangiato dal putit, adesso si usano putit messi in morte apparente. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78117
    (78117, '\\"Look at this Lily, this Putit is quite lively... wait.. noooooooooooo! \\" \\n# ~Victim\'s Last Words~'):
        "\\\"Guarda un po', <Lily>, questo putit è proprio vivace... uwaaa!!\\\" \\n# ~Le Ultime Parole della Vittima~",

    # ---------------------------------------------------------- :78462
    (78462, 'By adding unique elements to the process, the bread has a fluffier texture. The softness of the bread is not only apparent when you touch it, but it is even more obvious when you taste it. \\n#~Everchanging Food of Tyris~'):
        "Un pane a cui, aggiungendo qualcosa di proprio alla lavorazione, hanno dato una consistenza più soffice. La morbidezza si sente già a toccarlo, ma in bocca si capisce molto meglio. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78464
    (78464, '\\"Oh, the fluffy bread made by my big sister is delicious!\\" \\n# ~a girl with nausea~'):
        "\\\"I-il pane soffice che ha fatto la mia sorella maggiore è buonissimo!\\\" \\n# ~Parole di una Bambina che Trattiene la Nausea~",

    # ---------------------------------------------------------- :78529
    (78529, 'One of the basic seasonings that can make or break a dish. It is an excellent seasoning that not only adds sweetness, but also brings out the umami and saltiness of the ingredients when used in small quantities. \\n#~Everchanging Food of Tyris~'):
        "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge dolcezza, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il salato che l'ingrediente ha già. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :78596
    (78596, "One of the basic seasonings that can make or break a dish. While it obviously imparts a salty flavor on any food, using it sparingly can bring out the ingredients' natural sweetness and umami, making for an excellent seasoning in moderation.\\n#~Everchanging Food of Tyris~\\n"):
        "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge sapore salato, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il dolce che l'ingrediente ha già.\\n#~Il Cibo Mutevole di Tyris~\\n",

    # ---------------------------------------------------------- :79241
    (79241, "A very tasty dish that fills you with juices that overflow when you put it in your mouth. It's probably a silly question to ask what ingredients are used. \\n#~Everchanging Food of Tyris~"):
        "Un piatto buonissimo che, appena te lo metti in bocca, ti riempie di un sugo che trabocca. Chiedere che cosa ci sia dentro sarebbe soltanto di cattivo gusto. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :79243
    (79243, '\\"Hm. The texture when you put it in your mouth, the juicy meat juices that pour out of it with great vigor, and the unique flavor that lingers in your mouth. This dish deserves the highest rank I have ever had. By the way, what kind of meat is used in this dish?\\" \\n# ~ Words of the great food critic, Gratona ~'):
        "\\\"Uhm. La consistenza appena entra in bocca, il sugo che ne esce fuori con impeto, quel sapore tutto suo che resta. Questo piatto merita il posto più alto fra quanti ne ho mangiati. ...A proposito, che carne ci mettono dentro?\\\" \\n# ~Parole di <Gratona>, grande critico gastronomico~",

# 5 voci, 0 ambigue

    # ---------------------------------------------------------- :79431
    (79431, 'Vegetable with a strong acidity that has received all the blessings of the sun. It can be prepared in a variety of ways, but one unusual way to eat it is to cut it raw into round slices and dip it in sugar.\\n#~Everchanging Food of Tyris~'):
        "Una verdura molto acida che si è presa addosso tutto il bene del sole. La si cucina in molti modi, ma fra i più strani c'è chi la taglia a fette da cruda e la mangia con lo zucchero sopra.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :80487
    (80487, 'The white devil from a foreign land. It beckons people with its savory smell and soft touch, but once it has been eaten, it will suddenly pause at the throat and deprive the eater of action and consciousness! If this happens, get help from someone nearby.\\n#~Everchanging Food of Tyris~'):
        "Il demone bianco venuto da un paese straniero. Ti chiama con l'odore invitante e con la morbidezza, ma una volta che l'hai mangiato si ferma di colpo in gola e ti toglie di botto i movimenti e i sensi! Se ti succede, fatti aiutare da chi ti sta vicino.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :80550
    (80550, 'Special rice cake decorated with festive items. A grateful rice cake blessed by God, but eaten without concern. However, God cannot do anything about the rice cake getting stuck in your throat. So be careful when eating it. \\n# ~Gifts that I am Happy to Receive~'):
        "Un mochi speciale, ornato con le cose di festa. È un mochi benedetto e degno di riconoscenza, ma lo si può mangiare senza pensarci. Contro un mochi che va di traverso, però, non può niente nemmeno un dio: quando lo mangi, guardati bene intorno. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :81669
    (81669, "Fortune for you and me! Fortune! If you take a bite gently, happiness will surely arrive. If you ate the whole thing, God's blessing will come to you. \\n# ~Note Written on the Back of the Bag~"):
        "Fortuna per te e fortuna per me! Fortuna! Se ne dai un morso piano piano, la felicità di sicuro ti arriva. Se lo mangi tutto in un colpo, ti arriva il responso di un dio. \\n# ~Postilla Scritta sul Retro del Sacco~",

    # ---------------------------------------------------------- :84100
    (84100, 'The tail of a rabbit has been considered a sign of good luck since ancient times. Some regions use it as an ornament, but the ancient North Tyris belief is that eating it brings good luck. \\n#~Iron Stomach: A Complete Diet~'):
        "La parte della coda del coniglio, che fin dai tempi antichi è segno di fortuna. Pare che in certe zone se ne faccia un ornamento, ma l'insegnamento antico di Tyris del Nord è che mangiandola la fortuna te la prendi dentro direttamente. \\n#~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",

    # ---------------------------------------------------------- :86466
    (86466, 'A lunch made by your younger sister just for you. It never spoils because of love. It is said that just eating it generates negative ions around you and has an amazing relaxation effect, but I have yet to eat it... \\n# ~report of <Moxis>, leading imouto researcher~'):
        "Un pranzo al sacco che tua sorella minore ha fatto solo per te. C'è dentro l'amore, quindi non va mai a male. Dicono che soltanto a mangiarlo intorno si formino ioni negativi e che l'effetto di rilassamento sia straordinario, ma io non l'ho ancora mai mangiato... \\n# ~Studio di <Moxis>, massimo esperto di sorelle minori~",

    # ---------------------------------------------------------- :86800
    (86800, "It is said that when eaten, a fountain of knowledge springs up in one's head. A famous wizard spent all his knowledge in researching this fruit so that he could obtain it permanently, but in the end he was unable to propagate it. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un frutto che, dicono, a mangiarlo fa sgorgare in testa una fonte di sapere. Un mago di gran fama, per averne per sempre, ci spese sopra tutto il suo sapere; ma alla fine a farlo crescere non ci riuscì. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :87253
    (87253, 'Fragrant cheese that is said to be full of life force when eaten. Since ancient times, it is said to have been a favorite food of brave and daring heroes. \\n#~Everchanging Food of Tyris~'):
        "Un formaggio profumato che, dicono, a mangiarlo riempie di forza vitale. Fin dai tempi antichi, si racconta, era il preferito degli eroi coraggiosi e arditi. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :88275
    (88275, 'A rare apple with a faint golden color. It is said to contain plenty of honey and good fortune, and in the past, people wandered the continent in search of this miraculous fruit. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una mela rara che luccica appena di un colore d'oro. Dentro, dicono, c'è miele in abbondanza e insieme la fortuna, e in passato la gente vagò per il continente in cerca di questo frutto miracoloso. \\n# ~Dizionario Fantastico di Irva~",

# 34 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-044.jsonl'
RIGHE = {
    68650, 69527, 69598, 69669, 69734, 69799, 69864, 69929, 69994, 70396,
    70398, 70671, 71163, 71706, 73153, 74164, 74298, 74361, 74631, 75847,
    75849, 76719, 78115, 78117, 78462, 78464, 78529, 78596, 79241, 79243,
    79431, 80487, 80550, 81669, 84100, 86466, 86800, 87253, 88275,
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
