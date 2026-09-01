# -*- coding: utf-8 -*-
"""119a - Lotto 049 di `db_item.hsp`: LE POZIONI, il CORPO, prima meta'.

`FILTER_ITEM_POTION`, righe da `:43900` a `:89561`: **41 righe** su 37 oggetti —
37 dell'indice 0 e **4 dell'indice 2**. La categoria era intatta (82 da fare su
82 vive): dopo questo lotto ne restano **41**, tutte oltre la riga 90.000, ed e'
da li' che parte il 050.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese. `_previsione.py 049` non trova
gemelle — 41 righe, 41 firme distinte — e `_gia-reso.py 049` dice **0 su 41**:
nessuna di queste prose e' gia' resa altrove nel dizionario.

### ⭐⭐⭐ LA COLA: L'INGLESE SPOSTA DUE FRASI DA UN INDICE ALL'ALTRO

`:55344` e `:55346` sono lo stesso oggetto, e i due testi non si corrispondono
riga per riga:

    JP  description(0)  ...炭酸飲料...飲んだらゲップが出るのは確実。
                        ルートもわからん状態で山に登れば遭難するっていうくらい確実。
        description(2)  (VUOTO)

    EN  description(0)  ...Carbonated beverage... (le due frasi NON ci sono)
        description(2)  \\"If you drink a cola, you'll burp!! Like how you climb
                        a mountain without where the summit is...\\"

Il giapponese mette il rutto e la montagna **in fondo alla descrizione**;
l'inglese le toglie da li' e le rimette **nell'indice 2**, virgolettate, in bocca
a «some weird old guy». Non e' una perdita e non e' un'aggiunta: e' la stessa
battuta spostata di slot.

**La decisione**: si rende la disposizione che il giocatore ha davanti. Il
pannello disegna i tre indici uno sotto l'altro, quindi renderle in tutt'e due i
posti — il giapponese nell'indice 0 e l'inglese nell'indice 2 — le farebbe
leggere **due volte nella stessa schermata**. La battuta resta una sola volta,
nell'indice 2, dov'e' oggi. Il giapponese non perde niente: perde solo il
doppione.

⚠️ E' un caso che nessuna rete puo' vedere. Le due righe hanno firme diverse,
stanno in due indici diversi, e ognuna delle due presa da sola e' a posto: il
doppione nasce **dal pannello**, che le mette insieme.

### ⭐⭐ DUE VOLTE IL NOME ITALIANO ROVESCIA LA FRASE CHE LO SPIEGA

`:61652` e `:61723` aprono tutt'e due dicendo «lo chiamano anche X», e in
tutt'e due X **e' il nome che il giocatore italiano ha sotto gli occhi**:

    riga     nome JP    la frase dice          nome IT            regge?
    :61652   揮発油     «detto anche gasolina»  benzina           NO
    :61723   精油       «detto anche essential oil» olio essenziale  NO

In giapponese la frase informa: l'oggetto si chiama *olio volatile* e c'e' anche
questo altro nome, *gasolina*. In italiano il nome dell'oggetto e' gia'
«benzina», e la frase spiegherebbe il nome col nome — «la benzina, detta anche
benzina».

**La decisione**: si **gira** l'informazione invece di buttarla. «Detta anche
olio volatile», «lo chiamano anche essenza». Il fatto che il giapponese porta —
questa cosa ha due nomi — resta intero, e la frase e' vera davanti al nome che
il giocatore legge. E' la regola della 117a (i pesci che spiegano il proprio
nome): il metro non e' la fedelta' alla parola, e' la verita' a schermo.

### ⚠️⚠️ IL TE' NERO: L'INGLESE HA RICOPIATO LA FRASE DEL TE' VERDE

`:59385` (te' verde) e `:59456` (te' nero) sono due righe consecutive con la
stessa struttura, e il giapponese le oppone su una parola sola:

    :59385   茶葉を極力発酵させないようにして作られる   fermentare il MENO possibile
    :59456   茶葉を完全発酵させて作られる               fermentare DEL TUTTO

L'inglese scrive «made by minimizing the fermentation of tea leaves» **su tutt'e
due**. Sul te' nero e' falso, e non e' un'aggiunta o un appiattimento: e' la
frase dell'altra riga ricopiata dentro questa. La resa italiana segue il
giapponese, come e' regola dalla 26a.

ⓘ Il resto della riga dipende da quella parola: e' la fermentazione completa che
trasforma il mana rimasto nelle foglie, ed e' per questo che il te' nero ridA'
MP mentre il verde no.

### ⚠️ IL CARTELLO E LO STREGONE: `:56473`

L'indice 2 dell'urina porta due testi che non c'entrano niente l'uno con
l'altro. Il giapponese e' un **cartello**: 「ここにおしっこをさせないでください」,
*non fate pipi' qui*, firmato ～根元の濡れた標識～ (il cartello bagnato alla
base). L'inglese scrive «Dare you enter my magical realm?» firmato «the
Whizzard» — un gioco di parole su *wizard* e *whizz*.

**La coda italiana viene dal giapponese** (la tabella della 112a e' indicizzata
per giapponese: `~Il Cartello Bagnato alla Base~`), quindi il corpo deve venire
di li' pure: una firma che dice «cartello» sotto una battuta da stregone sarebbe
un pannello che si contraddice da solo.

### ⓘ Le altre cose che il lotto ha deciso

  - **`gli dei` senza accento.** Il preflight ha respinto `dèi` su `:71997` e
    `:72070`: `reimporta` non accetta l'accento **dentro** la parola, perche' la
    degradazione ad apostrofo esiste solo in coda. Il progetto scrive «degli
    dei» dappertutto in `chat.hsp`, quindi non c'era niente da inventare;
  - **`il te di ieri`, due volte.** 過去のあなた torna su `:83835` (la pozione
    del declino, che abbassa il livello) e su `:89149` (il sangue di Ermes, che
    alza la velocita' per sempre): due effetti opposti, la stessa immagine. Le
    due rese la dicono nello stesso modo, e la forma non chiede il genere del
    giocatore (`guida-stile.md`);
  - **`bannou mugi`** su `:55415`: il dizionario l'ha gia' traslitterato, ed e'
    la regola della 111a — un termine coniato che l'inglese traslittera resta
    traslitterato;
  - **`pericolosissima` sciolta prima di reimportare.** Il preflight l'ha data
    a 15 caratteri, dentro la finestra di rinculo dell'impaginatore. Il numero
    che decide e' quello di `_107-descrizioni-item`, ma scioglierla costava una
    parola: `:83835` dice «molto pericolosa».

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **nove**, tutte gia' in tabella con una sola resa
italiana (`_code.py 049`: righe senza resa in tabella **0**). Il cancello
«titoli resi in PIU' modi» resta a **7**.

⚠️ La forma, da `_forma.py 049`: **21** righe su 41 hanno lo spazio prima del
`\\n` e 20 no; **18** code hanno lo spazio dopo il `#` e 23 no. Le due cose non
vanno insieme — `:81811` ha lo spazio prima del `\\n` e non dopo il `#`,
`:65671` il contrario — e si copiano riga per riga.

⚠️ `:89149` e' l'unica delle 41 il cui inglese chiude con un `\\n` **dopo** la
coda. Il preflight se n'e' accorto contando i segmenti.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-049.jsonl'
RIGHE = {
    43900, 44442, 44513, 44584, 49646, 53772, 55344, 55346, 55415, 56130,
    56471, 56473, 58849, 58920, 59385, 59456, 61652, 61723, 63384, 63794,
    65671, 65742, 68521, 70065, 71997, 72070, 72141, 72212, 74432, 77634,
    77636, 79503, 79574, 81811, 83482, 83835, 83972, 83974, 84367, 89149,
    89561,
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
