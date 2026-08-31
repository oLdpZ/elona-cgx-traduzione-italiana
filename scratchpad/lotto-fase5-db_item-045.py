# -*- coding: utf-8 -*-
"""117a - Lotto 045 di `db_item.hsp`: I CIBI, il secondo lotto della categoria.

`FILTER_ITEM_FOOD`, righe da `:92585` a `:108257`: **28 righe** su 28 oggetti,
tutte dell'indice 0. Restano **31 righe** per il lotto 046, e con quello la
categoria si chiude.

⚠️ Previsione di `applica`: **+28**, e stavolta non e' contata a mano — la
stampa `scratchpad/lotti-113/_previsione.py 045`, nuovo. Zero righe gemelle.

### ⭐⭐⭐ LA PREVISIONE DI `applica` DIVENTA UNO STRUMENTO

La 116a ha imparato che una riga puo' avere una **gemella** con giapponese e
inglese identici byte per byte — stessa firma, una resa che copre due righe — e
che la gemella **non sta in nessuna tabella**, perche' l'estrazione tiene una
voce per firma. La lezione finiva li': «il conto e' una riga di script», e la
riga di script si riscriveva a mano ogni lotto.

Adesso e' `_previsione.py NNN`: raggruppa per firma **tutte** le voci del file e
dice quante righe del sorgente porta ciascuna firma del lotto.

⭐ **Provata al contrario, e non su un lotto qualunque**: puntata sul **042**,
dove la gemella c'e' di sicuro, si accende e stampa la coppia giusta —

    :76863  ->  anche :126849   ⚠️ FUORI DAL LOTTO
    previsione di `applica`: +36 sostituzioni per 35 rese

che e' **esattamente** quello che `applica` disse nella 116a, scoperto allora
dopo il fatto. Sul 043 e sul 044 dice +34 su 34 e +39 su 39, cioe' le due
previsioni che allora furono esatte. La rete riproduce tre casi noti, due
spenti e uno acceso, prima di essere creduta su un caso nuovo.

### ⭐⭐ DUE PESCI SPIEGANO IL PROPRIO NOME, E IN ITALIANO IL NOME E' UN ALTRO

Il giapponese di quattro pesci contiene l'etimologia del nome. Due reggono la
traduzione e due no, e la differenza non e' di stile: e' se la frase resti
**vera davanti al nome che il giocatore legge**.

  - `:107673`, **pesce sciabola**: 舶刀「カトラス」 e' la sciabola, e il nostro
    nome la porta gia'. Regge, e si scrive senza nominare la parola inglese;
  - `:108111`, **pesce piatto**: 名の通り平坦で四角い, «come dice il nome».
    Regge;
  - `:107819`, **pesce palla**: グローブ e' il **guanto**, e il giapponese lo
    dice esplicito (手に装着するグローブ). Con «pesce palla» a schermo, «il
    nome viene da un guanto» e' una frase falsa;
  - `:108257`, **pesce re**: il nome viene dal 三日月, la falce di luna presa a
    forza. Con «pesce re» a schermo, la luna non spiega niente.

**La decisione** e' quella che il progetto ha gia' preso altrove: *si rende il
gioco, non le sillabe* — le fusioni delle razze, e la battuta della formica di
`chat.hsp:9942`, dove il precedente e' dell'inglese stesso. Il gioco di parole
si **rifa' sul nome che il progetto ha scelto**:

    pesce palla   il guanto resta, ma e' il guanto IMBOTTITO, che e' tondo:
                  «tonda come un guanto imbottito da infilare in mano»
    pesce re      resta il PRENDERE A FORZA, che e' il cuore dell'immagine:
                  «pare di star prendendo a forza un re che non vuole
                  saperne di arrendersi»

⚠️ Il nome **non si tocca**: `ムーンフィッシュ -> pesce re` e
`グローブフィッシュ -> pesce palla` sono gia' a schermo, e «pesce luna» e' preso
da マンボー (`:108038`), che e' il pesce luna vero. Cambiare un nome per far
tornare una descrizione sposterebbe il difetto su tre righe invece di una.
ⓘ Cercati in `_cerca.py`: nessuna delle due etimologie e' resa altrove.

### ⭐⭐ I SETTE SEMI: L'INGLESE NE APPIATTISCE TRE

Tutti e sette condividono la seconda frase parola per parola, e la terza si
sdoppia:

    杖 / 鉱石 / 果物 / 野菜   食べることができるが、そうするくらいなら少し
                              成長を待ってあげてほしい。今日よりも明日なんだ。
    アーティファクト / 謎 / ハーブ
                              食べることができるが、種の持つ可能性につりあう
                              満腹度は得られないだろう。

L'inglese scrive per **tutti e sette** la prima — «You can eat them, but you
should wait for them to grow a little longer.» — e per giunta lascia cadere
今日よりも明日なんだ, che e' la chiusa della prima variante. Quattro frasi
perse e tre righe appiattite, in un gruppo di sette.

⭐ E il **codice ha confermato il giapponese**: 杖 qui e' la **bacchetta**, non
il bastone. `action.hsp:19811` fa cadere `ITEM_ID_ROD_HEALING_HANDS`,
`..._UNCURSE`, `..._MANA` e gli altri dall'albero magico. Il dizionario ha le
due rese di 杖 gia' distinte — «bastone» per l'arma, «bacchetta» per l'oggetto
che si agita — e a scegliere non e' stato il senso comune: e' stata la fonte.

### ⚠️⚠️ UN ROVESCIAMENTO DELL'INGLESE, SU MORGIA

`:102836`: 食欲減退に効果があるとされ — l'erba fa effetto **contro** il calo
dell'appetito, che e' il sintomo. L'inglese scrive «effective in reducing
appetite», cioe' che l'appetito lo toglie: il contrario.

⭐ A dirlo non e' la grammatica ma la **frase dopo**, che il giapponese e
l'inglese hanno tutt'e due: 軽病の際には薬膳料理として食される, la si mangia
come piatto medicinale quando il male e' leggero. Un'erba che si mangia da
malati non e' un'erba che leva la fame.

### ⚠️ L'INGLESE LASCIA CADERE, RIPETE E SBAGLIA UN NOME

  - `:97601` (lo snack cibernetico): l'inglese **ripete la stessa frase due
    volte** — «But it is delicious! But it is really tasty!» — dove il
    giapponese dice でもおいしい！ una volta sola;
  - `:107746` (il tonno): perde 一尾で二度おいしい, «un pesce solo e buono due
    volte», che e' la battuta su cui la riga si chiude;
  - `:102584` (alraunia): appiattisce 舞踏会, il **ballo**, in «social
    occasions», e perde l'orto delle erbe delle gran dame;
  - `:102710` (spenseweed): perde 奮発して, cioe' che il cittadino ci si
    **sforza**, a comprarla;
  - `:102773` (mareilon): appiattisce 他の香辛料にも劣らぬ («non ha niente da
    invidiare alle altre spezie») in «for it's kick»;
  - `:108111` (il pesce piatto): scrive **«Palmyre»** dove il giapponese dice
    パルミア. E' Palmia, e nel dizionario e' Palmia da sempre.

### ⚠️⚠️ UNA `é` PERSA A MONTE, DENTRO IL CORPO — E LA FAMIGLIA E' DI UNA

`:92585` (l'uovo) scrive in inglese `our home d?cor`: la `é` di «décor» e' un
punto interrogativo **vero**, 0x3F, letto byte per byte nel sorgente pinnato.

E' lo stesso guasto delle sette code storpiate di `_115-fonti-storpiate`, ma
nel **corpo** invece che nella coda, dove nessuna rete lo cercava. Misurata la
famiglia col criterio «un `?` in mezzo a due lettere»:

    db_item.hsp     1 occorrenza     d?c        <- questa
    tutto il resto  0                (i tre di `net.hsp` sono query di URL)

Un'occorrenza in tutto il sorgente. Non serve una rete nuova per una riga sola,
e l'italiano non ci passa: «un pezzo d'arredo di casa tua» non ha accenti.
ⓘ E 我が家 lo scrive l'inglese «our home», ma il soggetto della frase e' あなた:
e' la casa di chi legge.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le due code del lotto sono `~Il Cibo Mutevole di Tyris~` (15 righe) e
`~Atlante Illustrato del Giardinaggio di Tyris~` (13), tutt'e due gia' in
tabella con **una sola** resa italiana ciascuna. Il cancello «titoli resi in
PIU' modi» resta a **7**: un 8 sarebbe un difetto nuovo.

⚠️ La forma e' di nuovo disomogenea, e le due disomogeneita' **non
coincidono**: 11 righe hanno lo spazio prima del `\\n` e 17 no; 7 code sono
`# ~` e 21 sono `#~`. I sette `# ~` sono i sette semi, che hanno anche lo
spazio; ma la carne secca e i tre snack hanno lo spazio e la coda **senza**.
Si legge `scratchpad/lotti-113/_forma.py 045` riga per riga.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :92585
    (92585, 'An oval object filled with the source of life. Naturally, it is a mass of nutrients. The North Tyris egg does not decay, so you can crack it now to feed your growth, or keep it on hand and display it as part of our home d?cor.\\n#~Everchanging Food of Tyris~'):
        "Un oggetto ovale, pieno zeppo della sorgente della vita. Va da sé che è un blocco di sostanze nutrienti. Le uova di Tyris del Nord non marciscono, quindi puoi anche romperlo subito e farne nutrimento per crescere, oppure tenerlo lì e metterlo in mostra come un pezzo d'arredo di casa tua.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :92717
    (92717, 'To prevent damaging the meat, it is cured in salt water and then dried under the sun to increase portability and shelf life. Although it is an unremarkable dish, it seems to go surprisingly well with Crim ale, and strong men often take bites of it at the bar. \\n#~Everchanging Food of Tyris~'):
        "Carne cruda messa sotto sale perché non si guasti e poi seccata al sole, così pesa poco da portare e dura a lungo. Come piatto è poca cosa, ma pare che con la birra crim ci stia benissimo, e i tipi robusti se la rosicchiano spesso alla taverna. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :93890
    (93890, 'Seeds that can be sown in the ground to harvest magical rods. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di bacchette. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :93957
    (93957, 'Seeds that can be sown in the ground to harvest ores and gems. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di minerali. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :97601
    (97601, "No ingredients or production methods are known! But it is delicious! But it is really tasty! Most of the people who eat it are children, but even adults who have a rare chance to try it are said to be captivated by the snack's unique, unhealthy taste. \\n#~Everchanging Food of Tyris~"):
        "Ingredienti e ricetta: ignoti del tutto! Però è buono! Un articolo misterioso. A mangiarlo sono quasi solo i bambini, ma dicono che perfino l'adulto che per caso ci prova resti prigioniero di quel sapore tutto suo, che sa di roba che fa male. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :97664
    (97664, 'A snack popular among young people that is made by frying certain vegetables in oil. Currently, this process is monopolized by a few vendors, so it is not available on the market. For some reason, the vendors do not aim to expand their business, so the economy is in a strange equilibrium. \\n#~Everchanging Food of Tyris~'):
        "Uno snack che va fortissimo fra i giovani: una certa verdura fritta nell'olio. Oggi la ricetta ce l'hanno in mano pochi commercianti che se la tengono stretta, quindi in giro non se ne trova; e siccome quei commercianti, chissà perché, non puntano a crescere, l'economia sta in un equilibrio bizzarro. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :97727
    (97727, 'A snack that is extremely popular among young people, made from a certain vegetable that has been transformed using a unique manufacturing process. Currently, this process is monopolized by a few vendors, so it is not available in the market. However, many customers buy it as a souvenir, and the vendors are apparently satisfied with that. \\n#~Everchanging Food of Tyris~'):
        "Uno snack che va fortissimo fra i giovani: una certa verdura rifatta da capo con una lavorazione tutta loro. Oggi la ricetta ce l'hanno in mano pochi commercianti, quindi in giro non se ne trova; ma sono in tanti a comprarne per ricordo, e ai commercianti pare che basti così. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :102521
    (102521, 'Herb famous for its plump, thick, fresh leaves. In ancient times, it was documented that when dried and watered, the herb would swell to more than its mass. Nowadays, people seem to take advantage of this and carry it as an emergency ration.\\n#~Tyris Gardening Encyclopedia~'):
        "Un'erba famosa per le foglie spesse e piene di succo. Resta scritto che nei tempi antichi, a seccarla e poi darle acqua, si gonfiava più di quanto pesasse. Oggi c'è chi si serve proprio di questo e se la porta dietro come scorta d'emergenza.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102584
    (102584, 'This herb is famed for its sweet, gentle fragrance. Its fragrance is popular among the nobility, and most ladies cultivate the herb in their gardens, perfume themselves with it before social occasions.\\n#~Tyris Gardening Encyclopedia~'):
        "Un'erba famosa per il profumo dolce e gentile che manda in giro. Quel profumo piace anche ai nobili, e quasi tutte le gran dame se la coltivano nell'orto delle erbe, se ne fanno impregnare il corpo e poi vanno al ballo.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102647
    (102647, 'This herb is widely known for its small, white blossoms. Because of its higher fertility compared to other herbs, it often thrives in the wild and can be said to be a folk herb in that respect.\\n#~Tyris Gardening Encyclopedia~'):
        "Un'erba famosa per i fiorellini bianchi che mette. Si riproduce meglio delle altre, quindi cresce spesso da sola, e sotto questo aspetto si può ben dire un'erba alla portata di tutti.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102710
    (102710, 'Herb that is well known for its refreshing fragrance. Its scent has a calming effect on the spirit of those who smell it, many citizens use it before important tasks or exams.\\n#~Tyris Gardening Encyclopedia~'):
        "Un'erba famosa per il profumo fresco che manda in giro. Quel profumo calma l'animo di chi lo annusa, e dicono che molti cittadini facciano lo sforzo di comprarla prima di un lavoro importante o di un esame.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102773
    (102773, "This herb is famous for its zesty aroma. It is not widely used due to its rarity, it is sometimes used in haute cuisine for it's kick.\\n#~Tyris Gardening Encyclopedia~"):
        "Un'erba famosa per il profumo pungente che manda in giro. È rara, quindi non la si usa molto, ma quel profumo non ha niente da invidiare alle altre spezie, tanto che a volte lo mettono come tocco finale nella cucina di lusso.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102836
    (102836, 'This herb is famous for its wild aroma. It is believed to be effective in reducing appetite and is sometimes eaten as a medicinal herb in minor illnesses.\\n#~Tyris Gardening Encyclopedia~'):
        "Un'erba famosa per il profumo selvatico che manda in giro. La dicono efficace contro il calo della fame, e a quanto pare, quando il male è leggero, la si mangia come piatto medicinale.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102903
    (102903, 'Seeds that can be sown in the ground to harvest powerful artifacts. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di artefatti. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :102970
    (102970, 'Seeds that can be sown in the ground to harvest all kinds of plants. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto delle cose più diverse. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :103037
    (103037, 'Seeds that can be sown in the ground to harvest magical herbs. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di erbe. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :103104
    (103104, 'Seeds that can be sown in the ground to harvest various fruits. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di frutta. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :103171
    (103171, 'Seeds that can be sown in the ground to harvest vegetables. It is a mixture of various genotypes and the harvest will vary depending on the environment. You can eat them, but you should wait for them to grow a little longer. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un seme che, seminato per terra, dà un raccolto di verdura. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :107600
    (107600, 'Small enough to fit in both hands. It is not suitable for large-scale cooking, but suitable for frying, tempura, etc. Rumor has it that in Palmia, it is a trend to carry and eat this fried with imo chips.\\n#~Everchanging Food of Tyris~'):
        "Un pesce piccolo, che sta in due mani. Per i piatti in grande non va bene, ma per friggerlo o farlo in tempura sì. Corre voce che a Palmia vada di moda portarselo dietro fritto, insieme all'imo fritto, e mangiarli così.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :107673
    (107673, 'Fish looked like a cutlass, because of the way it reflects the sunlight and glistens. As its name suggests, it is very long and slender and has no scales on its body. Its light taste makes it suitable for delicate dishes.\\n#~Everchanging Food of Tyris~'):
        "Un pesce che luccica al sole di un bagliore duro, e per questo l'hanno paragonato alla sciabola d'arrembaggio. Come dice il nome è lunghissimo e sottile, e non ha una squama addosso. Il sapore è delicato, quindi si presta ai piatti fini.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :107746
    (107746, 'Fish found all around Tyris, but the most famous are those found in the waters around Port Kapul. Its bright red flesh is delicious as sashimi, but it can also be cooked to give it a meaty texture.\\n#~Everchanging Food of Tyris~'):
        "Sta un po' dappertutto, ma i più famosi sono quelli che vivono nel mare vicino a Porto Kapul. La carne è di un rosso acceso ed è ottima in sashimi, ma passata sul fuoco dà anche una consistenza che pare carne: un pesce solo, e buono due volte.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :107819
    (107819, 'Brownish-brown coloured fish said to inhabit the shallow seabed, where it lurks and waits for its prey. Its name is said to derive from its overall shape, which resembles a glove worn on the hand.\\n#~Everchanging Food of Tyris~'):
        "Un pesce di color marrone. Vive sui fondali bassi e, dicono, aspetta la preda trattenendo il fiato. Il nome, si racconta, gli venne dalla forma d'insieme, tonda come un guanto imbottito da infilare in mano.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :107892
    (107892, "Saltwater fish about the width of an adult's shoulders. The taste varies considerably depending on the time of year. The fish landed at the right time of year have a bright peach-coloured flesh, a colour so distinctive that in the past it was added to the dye list at the behest of a dyer.\\n#~Everchanging Food of Tyris~"):
        "Un pesce di mare largo quanto le spalle di un adulto. A seconda della stagione il sapore cambia moltissimo, in bene o in male. Quelli tirati su nel momento giusto hanno la carne di un rosa acceso, e per quel colore così suo, un tempo, bastò la parola di un tintore a farlo entrare fra i colori da tintura.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :107965
    (107965, "The fish's bright scales are a sight to behold. The taste is also very good, with a strange and mysterious flavour that has been considered precious since ancient times. It is said that in foreign countries it is customary to grill the whole fish and serve it on special occasions.\\n#~Everchanging Food of Tyris~"):
        "Un pesce dalle squame così vivaci che diverte anche solo a guardarlo. Anche il sapore è di quelli sicuri, e quel gusto sottile è tenuto prezioso da tempi antichi. Dicono che nei paesi stranieri, per le occasioni liete, l'usanza sia di cuocerlo intero sul fuoco e portarlo in tavola così.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :108038
    (108038, "Fish with overwhelming presence. It has not been eaten for a long time, but a chef who believes in 'eating it and die rather than not eating it at all' took the plunge and found in recent years that it is not poisonous and has a rather delicate taste.\\n#~Everchanging Food of Tyris~"):
        "Un pesce che ha una presenza da schiacciarti. Per molto tempo nessuno se lo mangiò, ma un cuoco che aveva per motto \\\"meglio mangiarne e restarci che non mangiarne affatto\\\" si fece coraggio e lo assaggiò: solo di recente si è saputo che veleno non ne ha, e che il sapore è anzi piuttosto fine.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :108111
    (108111, 'As the name suggests, the fish is flat and square in shape. There is a story that it was used as a substitute for paper in the past when paper was scarce in Palmyre, but this is completely untrue. It goes without saying that its long tail was never used as a pen.\\n#~Everchanging Food of Tyris~'):
        "Come dice il nome, un pesce dalla forma piatta e quadrata. Si racconta che in passato, a Palmia, in un'epoca in cui la carta scarseggiava, lo usassero al posto suo: è una bugia bella e buona. E della storia che con la coda lunga ci scrivessero come con una penna non c'è nemmeno da parlare.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :108184
    (108184, "In ancient times, the fish was sometimes described as the 'Jewel of Port Kapul'. This is not only because of its taste, but also because it was extremely difficult to keep fresh and cooks treated it like a gem.\\n#~Everchanging Food of Tyris~"):
        "Un pesce che da tempi antichi qualcuno chiamava \\\"la gemma viva di Porto Kapul\\\". E non solo per il sapore, dicono: tenerlo fresco è difficile assai, e i cuochi lo maneggiavano come si maneggia una gemma.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :108257
    (108257, "A vigorous fish with a sharp, cone-like mouth. The name 'moonfish' comes from its desperate resistance when caught, which resembles a crescent moon being captured by force.\\n#~Everchanging Food of Tyris~"):
        "Un pesce pieno di vita, che si riconosce dalla bocca a punta, come un punteruolo. Il nome gli venne da come si dibatte quando lo tiri su: resiste con una tale ostinazione che pare di star prendendo a forza un re che non vuole saperne di arrendersi.\\n#~Il Cibo Mutevole di Tyris~",

# 28 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-045.jsonl'
RIGHE = {
    92585, 92717, 93890, 93957, 97601, 97664, 97727, 102521, 102584, 102647,
    102710, 102773, 102836, 102903, 102970, 103037, 103104, 103171, 107600, 107673,
    107746, 107819, 107892, 107965, 108038, 108111, 108184, 108257,
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
