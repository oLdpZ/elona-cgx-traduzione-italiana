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
