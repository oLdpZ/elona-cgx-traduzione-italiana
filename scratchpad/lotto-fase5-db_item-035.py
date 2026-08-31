# -*- coding: utf-8 -*-
"""115a - Lotto 035 di `db_item.hsp`: GLI ATTREZZI, terza parte.

`FILTER_ITEM_TOOL`, righe 62.000-75.000: **43 righe** su 36 oggetti — 36
dell'indice 0, nessuna dell'indice 1 e 7 dell'indice 2. Segue il 034.

### ⭐⭐⭐ QUATTRO VOLTE L'INGLESE LASCIA CADERE UNA FRASE INTERA

Non e' una sfumatura di stile: sono frasi che nel giapponese ci sono e
nell'inglese **non compaiono affatto**.

  - `:63937` e i quattro fratelli — «a volte cambia solo un pezzo del
    vestiario, a volte il corpo diventa tutt'altra cosa». L'inglese si ferma a
    «largely dependent on the state of the user» e taglia l'esempio, che e' la
    sola frase che dica **che cosa** cambia;
  - `:65195`, il guanto di sfida — «che nel duello l'altro resti ferito o ci
    muoia, il karma non ne risente». E' un **fatto di gioco**, e l'inglese non
    lo dice da nessuna parte;
  - `:68587`, la pipa da oppio — il giapponese dice che nelle trattative la
    mascherano da **キセル**, una pipa comune; l'inglese scrive «a pack of
    cigarettes», che e' un altro oggetto;
  - `:73828`, lo scanner — il punto ③ giapponese dice che gli HP di chi
    comanda l'oggetto vanno a **zero**; l'inglese scrive «you lose the Duel»,
    che nel gioco non e' la stessa cosa. E la testa （効果未実装）, che
    l'indice 3 conserva, nell'inglese dell'indice 0 sparisce.

Si segue il giapponese (109a), e le quattro frasi tornano.

### ⭐⭐ I CINQUE NUCLEI SONO UNA FAMIGLIA, E L'APERTURA VIENE DAL LOTTO 033

`:63937` (alfa), `:64005` (beta), `:64073` (gamma), `:64141` (delta), `:64209`
(omega) hanno lo stesso identico giapponese a meno della frase sugli attributi.
Cinque rese identiche fino a quella frase, come vuole la regola della famiglia
(111a).

⭐ L'apertura non si inventa: 魔石が組み込まれた魔道具 e' gia' reso a `:43240`
nel lotto 033 — «Un oggetto magico con dentro una pietra magica» — e l'inglese
li' come qui scrive «special gemstone», che 魔石 non e'. La formula si copia.

Gli attributi si copiano da `skill.hsp`, dove sono gia' resi: 筋力 Forza,
感覚 Percezione, 魔力 Magia, 器用 Destrezza, 回避 Schivata.

### ⚠️⚠️ UNA RIGA SENZA GIAPPONESE, LA SECONDA IN DUE LOTTI

`:72552` (l'indice 2 della maschera) ha il giapponese **vuoto** e un inglese
vero, come `:50410` nel 034. Li' l'inglese era quello giusto per caso; qui e'
l'unico che ci sia, e per giunta e' una **battuta**: «Stop playing the race
card!», dove *race* e' insieme la razza del gioco e il modo di dire inglese.

L'italiano non ha il modo di dire, ma ha la carta: «E piantala di giocarti la
carta della razza!» tiene tutt'e due i sensi perche' **l'oggetto e' una
maschera che cambia razza**, e la carta da giocare resta un'immagine viva.

⚠️ Queste righe non sono un errore da riparare: sono due su 460 rese del corpo,
e vanno **contate**. Se diventassero tante, vorrebbe dire che l'estrazione
perde il ramo giapponese da qualche parte, e sarebbe un altro guasto.

### ⭐⭐⭐ IL GENERE DEL GIOCATORE, IN UNA RIGA DI DUE PAROLE

`:65197` e' 「うそつき」, «bugiardo», ed e' la battuta di chi ha appena preso
in faccia il guanto di sfida: la dice **al giocatore**. In italiano
«bugiardo» sceglierebbe un genere che il gioco non conosce, ed e' la regola
di `guida-stile.md` (la stessa che ha riscritto `Full` in «Non riesci a mangiare
altro»).

La resa e' **«Menti.»**: il verbo non ha genere, l'accusa resta intera e sta in
due sillabe come l'originale. ⓘ L'inglese qui scrive «Scut!», che e' una terza
cosa ancora.

### ⚠️⚠️ LE VIRGOLETTE A CAPORALE NON ESISTONO IN QUESTO DIZIONARIO

Scrivendo `:65464` — l'oggetto che «porta il nome di *洞察*» — la prima stesura
metteva il nome fra virgolette a caporale. Contate: nel dizionario intero, su
**24.940** rese, le `«` sono **zero**. Non e' una consuetudine implicita, e'
un fatto: CP932 quel carattere non ce l'ha, e `degrada()` lo perderebbe.

Il nome va in maiuscola e senza virgolette. ⚠️ La domanda giusta non era «mi
piacciono?» ma «ce ne sono altre?», e la risposta si conta, non si ricorda.

### ⓘ I termini cercati a mano nel dizionario

イェルス «Yerles»; クラムベリー «crimberry»; 時止弾 «munizioni fermatempo»;
存在級位 «grado di esistenza»; アカシックネットワーク «rete akashica» (e da li'
アカシックレコード, «registro akashico»); 解剖学 «Anatomia»; 錬金術 «Alchimia»;
料理 «Cucina»; デッキ «mazzo»; ランク in senso di carta «valore»
(『ランクチェンジ』 -> «Cambia valore»); アンデッド «non morto»; カルマ «karma»;
情報屋 «informatore»; ブラックマーケット «mercato nero»; 元素の神 «dio degli
elementi»; 富の女神 «la dea della ricchezza».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62020
    (62020, 'A weapon that fires nuclear rockets. Intended for front-line use and pinpoint target destruction, the range and blast radius are quite modest. However, the power per range is rather enhanced, so care must be taken not to get caught in the middle. It cannot be reloaded and is disposable in terms of barrel strength. Since it is too heavy to be carried individually, it is usually carried in a vehicle. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un'arma che spara razzi nucleari. È pensata per la prima linea e per distruggere un bersaglio preciso, quindi la gittata e il raggio dello scoppio sono piuttosto contenuti. La forza per area però è alzata, e bisogna stare attenti a non restarci dentro. Non si ricarica, e per come regge la canna è comunque usa e getta. Col peso che ha, portarla addosso è dura: di solito la si carica su un veicolo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62096
    (62096, 'This is a portable weapon that fires incendiary rockets from four barrels, one at a time. It has been greatly improved and has high accuracy at short distances. The special combustion agent mixed with the rockets generates a tremendous amount of heat, and direct exposure to the flying droplets can cause severe burns. Although it has the firepower to burn an entire area, it is bulky and is rarely used in the Yerles military. Because of its shape, it is sometimes mistaken as to which side the shell comes out from. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un'arma portatile che spara razzi incendiari uno alla volta da quattro canne. È molto migliorata, e sulla distanza corta è precisa. La miscela speciale che ci bruciano dentro scalda in modo tremendo, e gli schizzi addosso danno ustioni gravi. Ha fuoco da bruciare un'intera area, ma è ingombrante e fra gli Yerles non la usa quasi nessuno. Per la forma che ha, ogni tanto ci si sbaglia su da che parte esca il colpo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62098
    (62098, '\\"Aim towards the enemy!\\" \\n# ~attached manual~'):
        "\\\"Sparare in direzione del nemico.\\\" \\n# ~Il Foglietto delle Istruzioni Allegato~",

    # ---------------------------------------------------------- :62172
    (62172, 'An anti-tank rocket launcher believed to have been used by past civilizations. Its special rocket propulsion, which is resistant to crosswinds, provides high accuracy. Molded explosive warheads penetrate armor and metal armor to channel the blast and inflict damage. Its disadvantage is that it is heavy for the number of rounds it can carry. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un lanciarazzi anticarro che, dicono, si usava nelle civiltà passate. La spinta speciale del razzo tiene bene il vento di lato, e il tiro è preciso. La testata a carica cava buca la corazza e le armature di metallo, ci infila dentro lo scoppio e fa danno. Il difetto è che pesa molto per quanti colpi porta. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62234
    (62234, 'A thin but fluffy blanket. Provides a comfortable sleep, but makes it hard to get up in the morning. VERY hard. \\n# ~Palmian Winter Fashion~'):
        "Una coperta sottile e però soffice. Fa dormire bene, ma alzarsi la mattina diventa dura. Molto dura. \\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :62236
    (62236, '\\"I have to get up and make breakfast soon...and finish the gloves I made last night... No... I\'m sleepy...I\'ll sleep a little longer...... just a little more.\\" \\n# ~words of a girl wrapped in a blanket~'):
        "\\\"Ora devo alzarmi e fare colazione... e finire i guanti di ieri sera... No... ho sonno... ancora un po'... solo un altro pochino.\\\" \\n# ~Parole di una Bambina Avvolta in una Coperta~",

    # ---------------------------------------------------------- :62600
    (62600, "Toolbox containing disposable medicines and medical instruments. It can heal wounds according to the user's dexterity and knowledge of biochemistry. It also greatly reduces the symptoms of paralysis, blindness, poisoning, and bleeding. \\n#~First aid at home~"):
        "Una cassetta con dentro medicine e attrezzi da medico usa e getta. Cura le ferite secondo la destrezza di chi la usa e quanta biochimica sa. E riduce di molto i sintomi di paralisi, cecità, veleno e sanguinamento. \\n#~Primo Soccorso in Casa~",

    # ---------------------------------------------------------- :62666
    (62666, 'A box of bullet and arrows. It can replenish arrow ammunition to the maximum except for time-stopping ammunition, but it is quite heavy. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una cassa con dentro frecce e munizioni. Ricarica al massimo tutto tranne le munizioni fermatempo, ma pesa parecchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :63521
    (63521, 'When used, the lion causes a nuclear explosion after the count. Although the lion is dead, it does not matter because it can be used as an atomic bomb. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un leone che, se lo si usa, dopo un conto alla rovescia fa un'esplosione nucleare. Il leone è morto, ma siccome funziona da bomba atomica non è un problema. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63523
    (63523, '\\"A dead lion beats a live dog.\\" \\n# ~scribbling in a mysterious notebook~'):
        "\\\"Un leone morto val più di un cane vivo.\\\" \\n# ~Scarabocchi su un Quaderno Misterioso~",

    # ---------------------------------------------------------- :63937
    (63937, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's strength and perception. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Forza e la Percezione di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64005
    (64005, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's magical power and dexterity. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Magia e la Destrezza di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64073
    (64073, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's speed and agility. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco rende più veloci e alza la Schivata. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64141
    (64141, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's defense and recovery capabilities. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la difesa e la capacità di recupero. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64209
    (64209, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's all abilities in exchange for life. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza tutte le doti di chi lo usa, ma il carico è forte e rode la vita. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64553
    (64553, "A mirror that connects to the fourth dimensional space by means of filled magic power. It can be used only a limited number of times, but it is useful for organizing luggage. There is an urban legend that if the mirror likes you, a hand will reach out from the mirror's surface and drag you in. In fact, there is a report of a girl who was grabbed by the sleeve while organizing her belongings and fought back by breaking all the fingers of her hand. \\n# ~Arcane Almanac~"):
        "Uno specchio che, con la forza magica di cui è carico, si collega allo spazio a quattro dimensioni. Si usa un numero limitato di volte, ma è comodo per mettere in ordine il carico. Gira una leggenda di città: se piaci allo specchio, dalla superficie esce una mano e ti tira dentro. E infatti c'è il rapporto di una ragazza che, mentre metteva in ordine, si è vista afferrare per la manica e l'ha respinta rompendo alla mano tutte le dita. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64678
    (64678, "A fine basket filled to the brim with food. Everyone can eat to their heart's content. It is ideal for a picnic with many people, but it is difficult to prepare the food and heavy because of the quantity. \\n# ~Supporting Roles in Kitchen~"):
        "Un bel cesto pieno zeppo di cibo. Ci si sazia tutti insieme. È l'ideale per un picnic in tanti, ma preparare tutto quel cibo è una fatica e, per la quantità, pesa. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :64741
    (64741, 'The key to the Cemetery of a Different Dimension, which is located between this world and the underworld. Since this key was produced, we have heard strange stories of people wandering into an eerie world full of coffins. It may be that the interference opens entrances to other places as well. \\n# ~Arcane Almanac~'):
        "La chiave del cimitero DD, che starebbe fra questo mondo e l'oltretomba. Da quando è stata fatta si sentono storie strane di gente finita per sbaglio in un mondo sinistro pieno di bare. Forse l'interferenza apre un ingresso anche altrove. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64807
    (64807, 'A mysterious substance that cannot be understood with current technology. Think of an arm for an arm or a leg for a leg, and it is said that the part is attached to the body before you know it, as if it had been there from the beginning. The few people who have discovered it all say that it was lying around their feet when they came across it. Its origin is unknown. Only the discoverers can use its power, and its characteristic of disappearing after use makes it difficult to study. \\n# ~Bizarre Gossip~'):
        "Una materia misteriosa che la tecnica di oggi non sa spiegare. Basta pensare a un braccio, o a una gamba, e quel pezzo, dicono, ti si attacca addosso senza accorgersene, come se ci fosse sempre stato. I pochi che l'hanno trovata dicono tutti solo che se la sono vista rotolare ai piedi, e da dove venga non si sa. La usano soltanto loro e sparisce appena usata: per questo studiarla è difficile. \\n# ~Dicerie Bizzarre~",

    # ---------------------------------------------------------- :65195
    (65195, "A glove used to challenge someone to a duel. It possesses the power of a curse, and the person who throws the glove at the opponent will not be able to escape from the map until the duel is settled. The winner of the duel will take a larger amount of his or her opponent's possessions.\\n# ~Heated Duelists~"):
        "Il guanto che si usa per sfidare a duello. Che nel duello l'altro resti ferito o ci muoia, il karma non ne risente. Ha una forza come di maledizione: chi lancia il guanto non può più fuggire da quella mappa finché la cosa non è decisa. Chi vince il duello si prende una parte più grossa delle cose dell'altro.\\n# ~Duellanti Ardenti~",

    # ---------------------------------------------------------- :65197
    (65197, '\\"Scut!\\" \\n# ~words of the victim to the curse~'):
        "\\\"Menti.\\\" \\n# ~Parole di Chi è Stato Maledetto~",

    # ---------------------------------------------------------- :65464
    (65464, 'Magical tool with the name of [insight]. When you look into an object while holding it to your eyes, you can temporarily burn information about the object into the lenses. It is expensive and disposable, so it is not used by informants. \\n# ~Arcane Almanac~'):
        "Un oggetto magico che porta il nome di Intuito. Tenendolo all'occhio e guardandoci dentro un bersaglio, la lente ne imprime per un poco i dati. Costa il suo e si usa una volta sola, quindi gli informatori non lo adoperano. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :65466
    (65466, '\\"Well, isn\'t it rude to stare at people with something like that?\\" \\n# ~Worried Citizen~'):
        "\\\"M-ma non è scortese fissare la gente con un affare simile?\\\" \\n# ~Parole di un Cittadino in Affanno~",

    # ---------------------------------------------------------- :66075
    (66075, 'Amulet is blessed by the eight gods and one other mysterious deity who oversees the current Irva. At the center of the amulet is a small symbol of an eye or a pillar, which is not clear. It has no particular power to repel demons, but it is said that wearing it will keep you from being deceived by the voice of the god who urges you to convert to a new religion. \\n# ~Arcane Almanac~'):
        "Un amuleto che ha la protezione delle otto divinità che reggono l'Irva di oggi e di una nona, misteriosa. Al centro c'è disegnato piccolo un segno che non si capisce se sia un occhio o un pilastro. Non ha una vera forza contro i demoni, ma pare che a portarlo addosso non ci si lasci più confondere dalla voce che spinge a cambiare dio. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :67666
    (67666, 'Machine with many music discs built in. It has a row of song titles and buttons that allow you to select and play any song you wish. It shines beautifully with colorful lighting. \\n# ~Music of the Melodious Irva~'):
        "Una macchina con dentro tanti dischi musicali. Ha una fila di titoli e di pulsanti, e si sceglie il brano da far suonare. Brilla bella di luci colorate. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :68587
    (68587, "Illegal smoking paraphernalia handled on the black market. Those who use it are punished. When traded, it is disguised as an ordinary pack of cigarettes. It contains a narcotic made from dried crimberries, and when used, it instantly elevates the smoker's mood. The side effect is known to be depression, so unless the recipient is a submissive, the drug is likely to be rejected. \\n# ~Special Edition! Behind-the-scenes Favorites!~"):
        "Un attrezzo da fumo fuorilegge, di quelli che passano dal mercato nero. Chi lo usa viene punito. Nelle trattative, di nome, lo mascherano da kiseru comune. Dentro ha una droga fatta di crimberry essiccate, e a usarlo l'umore si alza di colpo. Si sa che come effetto secondario porta malinconia, quindi offrirlo a chi non ti obbedisce non serve: rifiuterà. \\n# ~Selezione! I Piaceri Clandestini~",

    # ---------------------------------------------------------- :68717
    (68717, 'Treasure that activates the core of Nefia and awakens its true power. Its power also affects the monsters inside Nefia, causing them to go berserk. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma che attiva il nucleo della Nefia e ne sveglia la vera forza. Quella forza agisce anche sui mostri dentro la Nefia, e li fa imbestialire. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68783
    (68783, "A red thread of destiny, spun by the souls of those bound together with a bond. No matter how the world changes, no matter how time goes, it will bring them together again at the end of time, beyond the infinite worlds. \\n# ~Aion's Prophecy~"):
        "Il filo rosso del destino, filato con le anime di chi è legato da un vincolo. Per quante volte il mondo cambi e il tempo giri, in capo al tempo, di là dai mondi infiniti, li legherà di nuovo l'uno all'altro. \\n# ~La Profezia di Aion~",

    # ---------------------------------------------------------- :69454
    (69454, "It can provide nutrients to plants, resulting in rapid growth and improved quality. Because of the unusual rate of nutrient absorption in many of Irva's crops, the effect is immediate but not sustainable. \\n# ~Agriculture and its New Possibilities~"):
        "Dà nutrimento alle piante, e porta crescita rapida e qualità migliore. Molte colture di Irva assorbono il nutrimento a una velocità fuori dal comune, quindi l'effetto è immediato ma non dura. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",

    # ---------------------------------------------------------- :70333
    (70333, "A complete set of ingredients and utensils that can be used up. Even if you have no cooking skills, you can easily complete homemade chocolates. As long as you don't mess around too much. \\n# ~Supporting Roles in Kitchen~"):
        "Un attrezzo usa e getta con dentro tutto, dagli ingredienti agli arnesi. Anche senza una briciola di Cucina il cioccolato fatto in casa viene bene. Purché non ci si metta a fare gli scemi. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :70598
    (70598, "Using the magical crystals as the nucleus, a pseudo-body is constructed with the cultured remains in a coffin. After completion, it is used mainly as a vessel for carrying around. The strength of the undead that emerges depends on the user's anatomy and alchemical skills. \\n# ~Necromancy for Noobs~"):
        "Con un cristallo di forza magica per nucleo, dentro la bara si costruisce un corpo provvisorio con i resti coltivati. Finito che è, serve soprattutto da recipiente per portarlo in giro. Quanto è forte il non morto che ne esce dipende da Anatomia e Alchimia di chi lo fa. \\n# ~Negromanzia per Principianti~",

    # ---------------------------------------------------------- :70817
    (70817, 'A quill pen imbued with astral light. It interferes exclusively with the existence records of life in this world...the Akashic Records, and rewrites them so that the subject exists as another person. The resulting person is the identical person with the same memories and personality, but free from any original role or destiny. However, the user is required to have at least half the existence level of the subject. Intervention requires material \\"magic ink\\" according to the subject\'s level of existence, and will fail if the subject does not sincerely desire it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una penna d'oca intrisa di luce astrale. Interviene, entro un limite, sul registro akashico, dove sta scritta l'esistenza di ogni vita di questo mondo, e lo riscrive perché del soggetto ne esista un secondo. Quello in più è la stessa persona, con gli stessi ricordi e lo stesso carattere, ma è sciolto dal ruolo e dal destino che aveva. Chi la usa però deve avere almeno metà del grado di esistenza del soggetto. E l'intervento chiede, secondo quel grado, l'inchiostro magico come materia: se il soggetto non lo vuole con tutto il cuore, fallisce. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71924
    (71924, 'Doll that has been passed down from generation to generation as a charm among cleaners. It is said to move by itself in the night and hunt the G-demons. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una bambola che fra gli addetti alle pulizie si tramanda da tempo come amuleto. Si dice che nel cuore della notte si metta in moto da sola e vada a caccia dei demoni neri e marroni. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72484
    (72484, 'Providing an occupation after the name, no matter how bullshit it may sound, will get you the job. However, it does not necessarily mean that you will be competent for that position. \\n# ~Extra Issue: Weird Items~'):
        "Se dopo il nome ci si scrive un mestiere, per quanto assurdo sia scritto, quel mestiere lo si ottiene. Non è detto però che vengano anche le doti che gli si addicono. \\n# ~Speciale: Oggetti Sospetti Comprati e Provati~",

    # ---------------------------------------------------------- :72486
    (72486, '\\"It is up to the customer to decide how to use this item.\\" \\n# ~Words from an Shady, Old Shopkeeper~'):
        "\\\"Come usare questo articolo sta al cliente deciderlo.\\\" \\n# ~Parole del Vecchio Bottegaio del Vicolo~",

    # ---------------------------------------------------------- :72550
    (72550, 'Mysterious stone mask. With the power of the red stone of the philosopher, it is said that when worn, the body is reconstructed and reborn into a different race. \\n# ~Extra Issue: Weird Items~'):
        "Una maschera misteriosa. Dicono che, per la forza della pietra rossa del saggio che ci è incastonata, a portarla il corpo si ricompone e si rinasce in un'altra razza. \\n# ~Alchimia: Grande Compendio dei Divieti~",

    # ---------------------------------------------------------- :72552
    (72552, '\\"Stop playing the race card!\\" \\n# ~Jonah, the Adventurer~'):
        "\\\"E piantala di giocarti la carta della razza!\\\" \\n# ~<Jonah> l'avventuriero~",

# 7 voci, 0 ambigue

    # ---------------------------------------------------------- :72620
    (72620, 'A whistle that produces a sound that can only be heard by dogs. It may look like a simple flute, but it is in fact a magical tool, and is absolutely inaudible to all but the dogs. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un fischietto che fa un suono che sentono solo i cani. Sembra un fischietto qualunque, ma è un oggetto magico a tutti gli effetti, e a parte i cani non lo sente proprio nessuno, mai, in nessun modo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73020
    (73020, 'It is a gemstone that is supposed to bring about evolution when used on certain allies who meet the requirements.\\n# ~Irva Fantasy Encyclopedia~'):
        "È una gemma che, usata su certi compagni che ne abbiano i requisiti, porterebbe un'evoluzione.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73288
    (73288, 'A flag used by commanders and others to communicate orders. It can be used to give instructions to fellow allies even when your voices cannot be heard. \\n# ~Command and Control on the Battlefield~'):
        "Una bandiera che i comandanti e simili usano per trasmettere gli ordini. Serve a dare istruzioni ai compagni anche quando la voce non arriva. \\n# ~Comando e Controllo sul Campo di Battaglia~",

    # ---------------------------------------------------------- :73698
    (73698, 'A statue in the shape of the God of Elements. created by a renowned artist. Its appearance is full of dignity. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura il dio degli elementi, opera di un artista famoso. Il portamento è pieno di dignità. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :73765
    (73765, 'A statue in the shape of the Goddess of Wealth, created by a renowned artist. The artist was required to sign a contract to give 30% of the sale price to the Yacatect. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura la dea della ricchezza, opera di un artista famoso. Per farla, l'artista fu costretto a firmare un patto: tre decimi del prezzo di vendita vanno a Yacatect. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :73828
    (73828, "① At the start of your turn: You can draw until you had 5 card in your hand. ② Once per turn: you can discard 1 card; Send cards from the top of your Deck to the GY equal to this card's rank. ③ At the end of the turn, if you have no cards left in your Deck, you lose the Duel. And if you do, shuffle all cards in your GY into your Deck. ④ You can skip your action for 30 turns. If you do, shuffle all cards in your GY into your Deck. Then, you can select any available deck for the rest of this duel.\\n# ~Heated Duelists~"):
        "(effetto non attivo) 1) All'inizio del turno peschi dal mazzo fino ad avere cinque carte in mano. 2) Una volta per turno puoi scartare una carta dalla mano e attivarne l'effetto; poi scarti dal mazzo tante carte quanto vale la carta attivata. 3) Alla fine del turno in cui il mazzo resta a zero carte, chi comanda questo oggetto va a 0 HP. Dopo, tutte le carte scartate tornano nel mazzo e si mescola. 4) Per 30 turni puoi saltare il tuo agire. Se riesce, tutte le carte scartate tornano nel mazzo e si mescola; poi scegli un mazzo qualunque fra quelli che puoi usare, e da lì in avanti giochi con quello.\\n# ~Duellanti Ardenti~",

# 36 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-035.jsonl'
RIGHE = {
    62020, 62096, 62098, 62172, 62234, 62236, 62600, 62666, 63521, 63523,
    63937, 64005, 64073, 64141, 64209, 64553, 64678, 64741, 64807, 65195,
    65197, 65464, 65466, 66075, 67666, 68587, 68717, 68783, 69454, 70333,
    70598, 70817, 71924, 72484, 72486, 72550, 72552, 72620, 73020, 73288,
    73698, 73765, 73828,
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
