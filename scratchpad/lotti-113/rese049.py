import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43900
    (43900, "A beverage containing toil-energy. It has the effect of borrowing energy in advance and prevents stamina consumption or a one-time reduction in lifespan due to labor or milking. There are rumors that drinking too much of it can damage one's health, but at least no creature is that poor in the modern Ylva.\\n#~Drinks to Drink, Drinks Not to Drink~"):
        "Bevanda a base di Energia da Lavoro. Anticipa le forze, e impedisce una volta sola che gli SP calino o che la vita scenda per il lavoro o la mungitura. Si dice che a berne troppa si rovini la salute, ma nell'Irva di oggi non esiste creatura tanto gracile.\\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :44442
    (44442, "An advanced potion packed with a number of sufferings. If your enemy isn't ver strong, you will be able to neutralise them with one of these.\\n#~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione superiore in cui sono stipate sofferenze d'ogni sorta. Se il nemico non è davvero forte, una bottiglia sola basta a renderlo inoffensivo.\\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :44513
    (44513, 'An advanced potion packed with many curses. It could be ued to rapidly weaken a tough opponent.\\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione superiore in cui sono stipate molte maledizioni. È tanto sinistra che l'avversario più tenace si indebolisce di colpo.\\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :44584
    (44584, 'An advanced potion that temporarily sharpens physical abilities. It is a new medicine whose formulation has been established fairly recently.\\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione superiore che affina per un po' le doti fisiche. È un preparato nuovo, la cui formula è stata messa a punto solo di recente.\\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :49646
    (49646, 'An elegant golden liquor made from honey. When drunk, it temporarily separates the mind from the body, allowing the drinker to walk freely around the area. \\n#~The Wide World of Alcohol~'):
        "Un liquore d'un elegante color oro, fatto con il miele. A berlo, lo spirito si stacca per un po' dal corpo e si può passeggiare in giro a piacere. \\n#~Il Mondo Profondo dei Liquori~",

    # ---------------------------------------------------------- :53772
    (53772, 'Popular chemical for germaphobes. Through its purifying power and chemical mechanism, it weakens pathogenic microorganisms and viruses and renders them non-pathogenic. It cannot sterilize, but it is effective against poisons and diseases. Its main ingredient is the same as alcohol, but because it is purified, it cannot be consumed to get drunk. \\n#~First aid at home~'):
        "Un preparato che va a genio ai maniaci della pulizia. Con la forza della purificazione e con la chimica indebolisce microbi e virus e li rende innocui. Sterilizzare non sterilizza, ma contro veleni e malattie funziona. Ha lo stesso ingrediente principale dei liquori, ma essendo purificato non ubriaca. \\n#~Primo Soccorso in Casa~",

    # ---------------------------------------------------------- :55344
    (55344, 'Carbonated beverage with a distinctive cinnamon and vanilla flavor. The name comes from the fact that it was initially made from the fruit of a tree called cola. It contains large amounts of sugar and makes you fat if you drink too much. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una bevanda gassata dal caratteristico sapore di cannella e vaniglia. Il nome viene dal frutto di un albero, la cola, che all'inizio se ne usava. Contiene molto zucchero: a berne troppa si ingrassa. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :55346
    (55346, '\\"If you drink a cola, you\'ll burp!! Like how you climb a mountain without where the summit is, you\'ll run into trouble! You absolutely will! It\'s inevitable!\\" \\n#~some weird old guy~'):
        "\\\"Se bevi una cola, il rutto arriva!! Sicuro come chi va in montagna senza sapere la strada e ci resta! Sicurissimo! Non c'è scampo!\\\" \\n#~un vecchio bizzarro~",

    # ---------------------------------------------------------- :55415
    (55415, 'Tea made by infusing the seeds of the all-purpose wheatgrass. Since it is not made from tea leaves, it does not contain caffeine. It is characterized by its savory and refreshing taste. It also improves blood flow. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Un tè fatto con i semi del bannou mugi, tostati e messi in infusione. Non venendo da foglie di tè non contiene caffeina. Ha un gusto tostato e pulito, e migliora anche la circolazione del sangue. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :56130
    (56130, 'This is a concentrated agent with ingredients that instinctively put creatures on alert. If sprayed regularly around the area while walking, wildlife attacks can be avoided. Even a small amount is effective and can be used for 400 miles. It is possible to drink it, but it is best not to, as your body will reject it beyond alarm. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Un preparato che concentra le sostanze con cui gli animali si mettono d'istinto in allarme. Spruzzato di tanto in tanto intorno a sé mentre si cammina, evita gli assalti delle bestie selvatiche. Ne basta pochissimo, e una boccetta dura per 400 miglia buone. Berlo si può, ma il corpo va oltre l'allarme e lo rigetta: meglio di no. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :56471
    (56471, 'Liquid excrement made from waste and excess water. It is by no means hygienic, but when fermented, it can be used for washing clothes. It is not a medicine, but it is drinkable..... Do beware its high salt content. \\n#~Magical Ways of Waste Utilization~'):
        "Escrementi liquidi, fatti di scorie e d'acqua in eccesso. Igienico non lo è affatto, eppure fatto fermentare serve per il bucato: c'è più di quel che sembra. Non è una pozione, ma bere si può... Attenzione però, il sale è parecchio. \\n#~Il Sogno di Riusare gli Scarti~",

    # ---------------------------------------------------------- :56473
    (56473, '\\"Dare you enter my magical realm?\\" \\n#~the Whizzard~'):
        "\\\"Non fate pipì qui.\\\" \\n#~Il Cartello Bagnato alla Base~",

    # ---------------------------------------------------------- :58849
    (58849, "A high-level potion that temporarily hones one's mind and body. Said to have been formulated by an ancient emperor who was also a prodigious alchemist.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione superiore che affina per un po' corpo e mente. Si dice l'abbia creata un antico personaggio che era imperatore e insieme un ottimo alchimista.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :58920
    (58920, "This potion envelops the imbiber in a dance of glittering lights, reminiscent of sparkling gems. It's enough to leave a dazzling impression, though it only lasts a short time.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che, a berla, avvolge in un luccichio come di gemme che danzano tutt'intorno. Dura poco, ma per darsi un'aria sfolgorante basta e avanza.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :59385
    (59385, "Highly popular beverage of choice. It is made by minimizing the fermentation of tea leaves. In addition to calming the mind, it also has the effect of boosting the body's immune system and aiding in the burning of fat. \\n#~Drinks to Drink, Drinks Not to Drink~"):
        "Una bevanda voluttuaria molto amata. Si fa lasciando fermentare le foglie il meno possibile. Oltre a calmare l'animo, rinforza le difese del corpo e aiuta a bruciare i grassi. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :59456
    (59456, 'Highly popular beverage of choice. It is made by minimizing the fermentation of tea leaves. The mana remaining in the leaves is transformed into an easily absorbable form during the fermentation process, and is effective for MP recovery, recovery from fatigue, etc. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una bevanda voluttuaria molto amata. Si fa lasciando fermentare le foglie fino in fondo. Il mana rimasto nelle foglie, con la fermentazione, prende una forma che il corpo assorbe facilmente: ridà MP e toglie la fatica. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :61652
    (61652, 'Also known as petrol. Used as fuel by ancient civilizations. Highly volatile, it evaporates in a short time in the current atmospheric environment of Irva. Because it is flammable and dangerous, if you must be exposed to it, do so in a place where there is no fire. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Detta anche olio volatile. Pare che le civiltà antiche la usassero come carburante. È molto volatile, e nell'aria dell'Irva di oggi evapora in poco tempo. Prende fuoco ed è pericolosa: se proprio ce la si vuole versare addosso, che sia dove non c'è fiamma. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :61723
    (61723, 'Essential oils. Expensive because they must be extracted from large quantities of plants. They are highly volatile and evaporate in a short time in the current atmospheric environment of Irva. It is usually used in small quantities as a fragrance. It has a strong odor when applied in large quantities, so do not apply too much. It is also flammable. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Lo chiamano anche essenza. Costa caro, perché per ricavarlo serve una gran quantità di piante. È molto volatile, e nell'aria dell'Irva di oggi evapora in poco tempo. Di solito si usa a gocce, come profumo: a metterne troppo l'odore diventa pesante, quindi non si esageri. È anche infiammabile. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :63384
    (63384, 'Mysterious syrup that changes color and increases in efficacy the more it is kneaded. The witch spent many years kneading it in her spare time, and as a result, it became so delicious that people would faint.\\n#~Everchanging Food of Tyris~'):
        "Uno sciroppo strano: più lo si impasta, più cambia colore e più cresce l'effetto. La strega, per ammazzare il tempo, l'ha impastato e reimpastato per anni, e il risultato è così buono che si sviene.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :63794
    (63794, "A beverage made from the juice of fruits, vegetables and nuts. The nutrients of the ingredients can be absorbed efficiently. You can mix several kinds to make a mixed juice or mix it with milk, according to each person's taste. \\n#~Drinks to Drink, Drinks Not to Drink~"):
        "Una bevanda fatta col succo di frutta, di verdura e di frutti degli alberi. Le sostanze nutrienti si assorbono senza sprechi. Secondo i gusti si possono mescolare più qualità per farne un misto, oppure allungarlo con il latte. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :65671
    (65671, 'This potion imparts a sudden feeling of becoming a bird, soaring through the sky. Temporarily weakens the effects of gravity on the user, and makes the body feel more nimble for a while.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che d'un tratto fa sentire come un uccello che corre per il cielo. Indebolisce per un po' la gravità, e per un po' il corpo si fa leggero.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :65742
    (65742, "A potion that instantly sharpens one's ability to concentrate. Though it clears the user's head and wards off drowsiness, it will not make you any smarter.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che d'un tratto alza la capacità di concentrarsi. La testa si fa lucida e dà resistenza al sonno, ma intelligenti non si diventa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :68521
    (68521, 'A popular beverage of choice. Its flavor varies depending on the degree of roasting and grinding, the brewing method and equipment used, and there is no one best for everyone. Mixing with milk is also popular. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una bevanda voluttuaria molto amata. Il sapore cambia con il grado di tostatura, con la macinatura, con il modo di prepararlo e con gli arnesi che si usano, e non ne esiste uno che vada bene a tutti. Va molto anche allungato con il latte. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :70065
    (70065, "When mixed with food, this chemical permanently prevents it from rotting, though its nutritional value will be halved. It's meant to be diluted in food, and is highly toxic when consumed as-is. Naturally, this preservative will have no effect on things that are already rotten, so it will not stop undead from decaying, even if they drink it.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Un preparato che, mescolato a un cibo, gli impedisce per sempre di marcire, ma dimezza la crescita che quel cibo dà. Va diluito e mescolato al cibo: bevuto com'è, fa male. Su ciò che è già marcio, naturalmente, non ha effetto: darlo da bere a un non morto non gli impedirà di decomporsi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :71997
    (71997, 'A nutritional supplement used by the gods. It energizes the mind and body, wipes away drowsiness and fatigue, and even cures illnesses with just a single dose. However, be advised that its extreme potency is known to induce hallucinations.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Il ricostituente che usano gli dei. Rinforza corpo e mente, spazza via fatica e sonnolenza e guarisce d'un colpo perfino le malattie. Attenzione però: è così forte che si arriva a vedere le allucinazioni.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :72070
    (72070, "In ancient times, the gods were said to have drunk an alcohol that granted immortality; this is a reproduction of that drink. It goes well with all manner of foods, and its delicious flavor can even cure anorexia. However, this replica is imperfect, and even though it's heavily diluted, it will make anyone violently drunk.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "La riproduzione del liquore d'immortalità che si dice bevessero gli dei antichi. Sta bene con qualunque cibo, ed è così buono da far dimenticare perfino l'inappetenza. Ma la riproduzione è imperfetta: per quanto allungato, ubriaca di brutto.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :72141
    (72141, 'A great calamity has been sealed within this high-level potion. Said to have been created on accident by a wizard burning with revenge.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione superiore che tiene chiusa dentro una sciagura. Si dice l'abbia creata per caso un mago che ardeva di vendetta.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :72212
    (72212, 'A dangerous fluid that, when exposed to air, reacts explosively to heat or physical shocks. It was once used to punish criminals.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Un liquido pericoloso: esposto all'aria, se prende un urto o del calore fa una piccola esplosione. Un tempo lo si usava per punire i criminali.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :74432
    (74432, 'A potion formulated by a distinguished alchemist after many years of research. Its production process is too complicated for any other alchemist to comprehend.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che un alchimista famoso ha ottenuto dopo anni di ricerche. Il modo di prepararla è troppo complicato perché gli altri alchimisti ci capiscano qualcosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :77634
    (77634, 'This traditional candy has been made in Vernis since the old days. It is only available among the wealthy and other special people, and the general public does not usually have the opportunity to taste it. In fact, it is rare to even see it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una caramella tradizionale, fatta a Vernis da tempo immemorabile. Gira soltanto fra i ricchi e la gente che conta, e alla gente comune non capita di assaggiarla. Non capita nemmeno di vederla. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77636
    (77636, '\\"Grandpa always gives me candy, it\'s very creamy and delicious... but I\'d rather have an allowance.\\" \\n# ~words of a grand-son~'):
        "\\\"La caramella che il nonno mi dà sempre è cremosa e buonissima, però... a dirla tutta preferirei la paghetta.\\\" \\n# ~Parole di un Nipote Speciale~",

    # ---------------------------------------------------------- :79503
    (79503, "Small cylindrical substance made of blue material. It is rumored to be a food that activates one's body, but no one seems to be willing to try it because of its appearance. \\n# ~The Yowyn Book of Secrt Knowledge!~"):
        "Un piccolo oggetto cilindrico fatto di una materia azzurra. Si dice sia un cibo che rimette in moto il corpo, ma con quell'aspetto nessuno pare avere voglia di provarlo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :79574
    (79574, 'Often sold at festivals, even children can enjoy this tongue-tingling drink. Its refreshing semisweet taste seems to melt away fatigue somehow.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Si vende alle bancarelle delle feste, e la possono bere anche i bambini: solletica la lingua. È dolce al punto giusto, e a berla pare che la stanchezza voli via.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :81811
    (81811, 'Potion that applies a flame-resistant protective coating to the item in which it is immersed. It is only effective on the item, so when you drink it, your internal organs will not show any resistance to the burns that occur when you eat something hot. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che stende una pellicola resistente alle fiamme su ciò che vi si immerge. Funziona solo sugli oggetti: a berla, le tue viscere non opporranno la minima resistenza alle scottature di quando si mangia qualcosa di bollente. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :83482
    (83482, "A potion that reconstructs the imbiber's body in a logical fashion. Its composition is unknown. All that's known is that a group from a mysterious dome may understand a part of the secret.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che rimette insieme il corpo di chi la beve secondo ragione. Di che cosa sia fatta non si sa; si sa soltanto che il gruppo della cupola misteriosa pare tenere in mano un pezzo del segreto.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :83835
    (83835, 'The moment you drink this highly dangerous potion, it will feel as though something you have built up has crumbled away. Beware, for you are now the you-of-the-past!\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione molto pericolosa: nell'istante in cui la si beve si ha la sensazione che qualcosa di quel che si è costruito fin lì stia franando. Sta' in guardia: adesso sei il te di ieri!\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :83972
    (83972, "Produced by excessive consumption or eating spoiled food. It is a tragic substance produced by the body's self-protective actions in such cases. It is not a potion, but it is drinkable. Surely.. drinkable... \\n#~Iron Stomach: A Complete Diet~"):
        "Si esagera con il bere, oppure si mangia qualcosa di andato a male: è la materia tragica che il corpo produce difendendosi in quei frangenti. Non è una pozione, ma bere si può. Si può... bere... \\n#~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",

    # ---------------------------------------------------------- :83974
    (83974, '\\"As long as you\'re alive, you\'re going to throw up. But I will never allow you to throw up in the city. If you do it in front of me, I will immediately push it back into your mouth!\\" \\n#~the Cleaner Balzak~'):
        "\\\"Finché si è vivi capita anche di vomitare, lo so. Ma dentro la città non lo permetto, mai. Provaci davanti a me, e te lo ricaccio in bocca all'istante!\\\" \\n#~Parole di <Balzak> il custode~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :84367
    (84367, "A potion containing excessive amounts of sodium. Since the salt is completely dissolved, it can't be used for cooking. But town cleaners supposedly carry lots of this substance for use in pest control.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione con dentro sale in eccesso. Il sale è sciolto del tutto, quindi in cucina non si può usare; pare però che i netturbini della città ne portino con sé parecchie, per sterminare gli insetti nocivi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :89149
    (89149, 'A strange liquid substance, its intense heat can be felt even through the bottle. When gulped down with determination, you might see your past self!\\n# ~Irva Fantasy Encyclopedia~\\n'):
        "Un liquido strano, così caldo che lo si sente attraverso il vetro. Quando ti farai coraggio e lo manderai giù, ci vedrai dentro il te di ieri!\\n# ~Dizionario Fantastico di Irva~\\n",

    # ---------------------------------------------------------- :89561
    (89561, 'Just the name alone is enough to make one feel a certain kind of crush. Those with no sense of delicacy will get a painful slap if they try to hand it to you directly, but those who have a taste for such things are free to do so. It has no effect on relationships beyond acquaintance. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione seducente: già solo il nome fa battere il cuore. Chi è privo di delicatezza prova a consegnarla di persona e si becca uno schiaffo sonoro; ma chi ha quel gusto lì faccia pure. Su chi è già più che amico non ha effetto. \\n#~Bevande da Bere e Bevande da Non Bere~",

# 37 voci, 0 ambigue
}
