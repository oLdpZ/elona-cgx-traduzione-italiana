# -*- coding: utf-8 -*-
"""115a - Lotto 038 di `db_item.hsp`: GLI SCARTI, prima parte.

`FILTER_JUNK`, righe 0-62.000: **44 righe** su 36 oggetti — 36 dell'indice 0,
4 dell'indice 1 e 4 dell'indice 2. E' il primo lotto della categoria, che ne ha
124 e non ha moltiplicatore: «da fare» e «vive» coincidono.

⚠️ La taglia si e' scelta con due tentativi in piu' del solito: fra `0 60000`
(39 righe) e `0 64000` (70) c'e' un **addensamento** — i sei materium e i sei
esplosivi stanno quasi attaccati. `0 62000` ne da' 44.

### ⭐⭐⭐ LA TILDE DI MONTE NON E' SEMPRE UNA TILDE, E SONO SETTE RIGHE

`_code.py` ha aperto il lotto dicendo «righe senza resa in tabella: **1**»,
dove il valore atteso e' 0. La riga e' `:46213`, la dernefia, e la sua coda
giapponese e' `#?ティリス園芸図鑑?`: **due punti interrogativi ASCII**
(U+003F) al posto della tilde larga (U+FF5E) che le altre **quaranta**
occorrenze dello stesso libro portano.

Non e' un artefatto della nostra estrazione: `db_item.hsp:46207` sta scritta
cosi' nel sorgente pinnato, e si legge byte per byte.

⭐ **Misurata, la famiglia e' piccola e compatta**:
`scratchpad/_115-fonti-storpiate.py` conta **7 code su 2.542**, tutte fra
`:46213` e `:46340` — tre oggetti soli, cioe' una sola sessione di lavoro di
monte. ⓘ Due delle sette la 112a le aveva gia' incontrate e messe in tabella
**con i punti interrogativi dentro la chiave**; questa e' la terza, e si e'
aggiunta allo stesso modo. La tabella adesso porta tre chiavi storpiate.

⚠️ Aggiungere la chiave **non cambia** il 234 di `_112-verifica-fonti`, che
conta le coppie del sorgente e non le voci della tabella. Verificato prima e
dopo.

### ⭐⭐ E UNA RIGA HA LA CODA IN GIAPPONESE E NON IN INGLESE: E' LA TERZA IN TUTTO IL CORPO

Sempre `:46213`: l'inglese la coda-fonte **non ce l'ha proprio**. Le altre due
in questa condizione sono `:47287` e `:47288`, trovate dal lotto 033, e la 114a
aveva gia' deciso che non gliela rimettiamo — il cancello conta il `#` contro
l'inglese, e aggiungerlo lo accende.

La resa quindi **non ha coda**, ed e' l'unica delle 44.

⚠️⚠️ `_112-verifica-fonti` questa cosa non la vede: la sua copertura salta le
righe senza coda inglese (`if not t_en: continue`). Il conto giusto lo da'
`_115-fonti-storpiate.py`, che dice **3 righe** — e per dirlo deve escludere i
**1.128 rapporti di identificazione**, il cui inglese una coda non ce l'ha mai.
ⓘ Senza quel taglio il numero e' 1.131 e non vuol dire niente: e' la lezione
della 114a sulla soglia mancante, ripetuta su un altro referto.

### ⚠️⚠️ IL CANCELLO DEI TITOLI PASSA DA 5 A 6, E ANCHE QUESTO E' DI MONTE

`:55921` (l'argilla) ha per fonte giapponese ～ルミエスト美術目録～, il catalogo
d'arte di Lumiest; l'inglese ci mette `~Vernis Ore Catalogue~`, che e' la fonte
di `:55983` (lo zolfo) e che in giapponese e' ～ヴェルニース鉱物図鑑～.

Il cancello chiava sull'inglese, quindi dopo questo lotto passa da **5 a 6**:
il sesto e' `~Vernis Ore Catalogue~` -> Catalogo d'Arte di Lumiest / Atlante
dei Minerali di Vernis. **Annunciato prima di misurarlo.** Un 7 e' nuovo.

ⓘ Che l'argilla stia nel catalogo d'arte e non in quello dei minerali ha senso:
serve a fare ceramiche. L'inglese ha guardato la sostanza e non il libro.

### ⭐⭐ I NOMI DELLE ABILITA' NON SI SCRIVONO A MEMORIA

Gli scarti da lancio dicono quasi tutti da quali **due** abilita' dipende la
loro potenza, e sono nove nomi in un lotto solo. Stanno gia' resi in
`skill.hsp`, e si prendono da li' con `lotti-113/_abilita038.py`:

    宝石細工 Oreficeria      生化学 Ingegneria genetica   戦術 Tattica
    魔力制御 Controllo magia  魔力の限界 Capacità magica    瞑想 Meditazione
    罠の知識 Disarmo trappole 工作 Falegnameria           投擲 Lancio
    魔道具 Dispositivi magici 料理 Cucina

⚠️⚠️ **E uno di questi nove non e' quello che sembra**: 射撃 in `skill.hsp` e'
**Mira** (`Marksman`), non «Tiro». «Tiro» e' la resa di `command.hsp` e
`help.hsp`, dove 射撃 e' l'azione. Nel corpo, dove il testo dice 〜の技術, la
parola giusta e' il nome dell'abilita' che il giocatore trova nella sua lista:
**Mira**.
⚠️ Difetto nostro gia' in gioco: l'indice 3 di `:76317` (la gemma di Mani) dice
«secondo il **Tiro**» per 射撃スキル依存. E' scritto qui perche' non si perda:
va uniformato in una passata sull'indice 3, non in un lotto del corpo.

### ⭐ L'INGLESE SBAGLIA CALDO PER FREDDO

`:52579`, il magaice: il giapponese dice 冷気 tre volte — il **gelo**. L'inglese
scrive «absorb hot air» e «when exposed to hot air», poi pero' chiude con
«freezing damage» e «the cold air», contraddicendosi da solo dentro la stessa
riga. Il nome dell'oggetto (冷吸の勾玉, «perla ricurva che assorbe il freddo») e
l'indice 3, gia' reso, dicono gelo. Si segue il giapponese.

### ⓘ Due giochi di parole, e uno si puo' tenere

`:46010`, il fukagurumi: il giapponese scrive なかなかジョーズに作られており,
dove ジョーズ e' insieme «Jaws» e 上手, «ben fatto». L'inglese dice «jawsome».
L'italiano ha **«fatto a pinna d'arte»**, che tiene tutt'e due i sensi.

`:42976`, l'expoopsion: la battuta e' nel nome, non nel testo, e il testo
giapponese e' serio (una fatta di forma «troppo artistica» che, essendo arte,
esplode). L'inglese ci aggiunge «the magnum poopus», che il giapponese non ha:
non si riporta.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42914
    (42914, "An unregistered card with special magic. It records information from the person hit by it. Using it on anyone other than close friends will definitely make them angry, as it's like stealing personal information. \\n#~Lumiest Art Catalogue~"):
        "Una carta su cui non è ancora scritta nessuna informazione. Ha addosso una magia particolare, e registra i dati di chi colpisce. È come portarsi via i dati di una persona senza permesso: usarla su chi non è di casa fa arrabbiare di sicuro. \\n#~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :42976
    (42976, 'This is not mere strawberry ice cream. But a masterpiece of shit, sculpted with such artistic perfection. And like any true art, it naturally explodes, the magnum poopus. Its explosive power depends on the techniques of gem-cutting and gene-engineering.\\n# ~Lumiest Art Catalogue~'):
        "Non è un gelato alla fragola. È uno sterco venuto in una forma fin troppo artistica. Essendo arte a tutti gli effetti, va da sé che esplode. La sua potenza, dicono, dipende dalle tecniche di Oreficeria e di Ingegneria genetica.\\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :43174
    (43174, "The result of a preserved food that has been fermenting in a can. According to analysis, it appears to be an ancient salted fish. The can is extremely bloated, and if subjected to strong impact, it will release a powerful stench, causing an explosion dependent on user's gene engineering and cooking skills. It is dangerous to open, as scans reveal the contents have mostly degraded into a gaseous state.\\n#~Everchanging Food of Tyris~"):
        "Quel che resta di una conserva che nella scatola ha continuato a fermentare. A leggerla pare fosse pesce salato dei tempi antichi. È gonfia da scoppiare, e a darle un colpo forte sprigiona il fetore e fa un'esplosione che dipende dalle tecniche di Ingegneria genetica e di Cucina. Aprirla è pericoloso, e sondandone dentro la materia si è scoperto che il contenuto si è decomposto ed è quasi tutto allo stato di gas.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :43302
    (43302, "Too-big-to-be-true snowflakes manufactured by wizards. Apparently, they tested a dubious theory that if you speak kind words to water and freeze it, it will turn into beautiful crystals. The wizard's hypothesis- that humans should not be allowed to decide what is beautiful or ugly, that he should not speak in human terms, and that humans should not freeze these without permission in the first place - which cause explosions that rely on user's meditation and gem cutting skills. \\n#~Arcane Almanac~"):
        "Un cristallo di neve fin troppo grosso, fabbricato da un mago. Pare che verificasse una teoria sospetta: che l'acqua, se le si parla con dolcezza e poi la si congela, diventi un bel cristallo. Il suo malumore (non sia mai che siano gli uomini a decidere che cosa è bello; e non mi si parli con parole d'uomo; e soprattutto non mi si congeli senza permesso) fa un'esplosione che dipende dalle tecniche di Meditazione e di Oreficeria, e ferisce i nemici. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :43364
    (43364, "Non-lethal weapons that envelops its surroundings in darkness. Its power is said to depend on user's tactics and marksmanship skills. According to documents, the world used to be full of flashbangs. However, they were defeated by the sudden appearance of darkbangs, and the flashbangs were buried in the darkness of history. \\n#~Collection of Armaments you can Use Tomorrow Cont.~"):
        "Un'arma non letale che avvolge di buio tutto intorno. La sua potenza, dicono, dipende dalle tecniche di Tattica e di Mira. Secondo i documenti, un tempo questo mondo era pieno di colpi accecanti; poi comparve di colpo il colpo oscuro, li batté, e i colpi accecanti furono sepolti nel buio della storia. \\n#~Ancora Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :43426
    (43426, "Device based on the lightning conductor. The needle itself stores the energy of lightning strikes through magical protection and can discharge it as needed. The output of the discharge is said to depend on the user's Control Magic and Magic Capacity skills. Normally, they are stored away for fear of theft or damage, but when a thunderstorm occurs, mages begin to set them up in the open air. \\n#~Arcane Almanac~"):
        "Un apparecchio nato dal parafulmine. Con una protezione magica l'ago stesso accumula l'energia dei fulmini, e la scarica quando serve. La forza della scarica, pare, dipende da Controllo magia e da Capacità magica. Di solito lo tengono al chiuso per paura dei ladri e dei danni, ma quando viene il temporale i maghi cominciano a piantarlo all'aperto. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :43488
    (43488, "Also known as box of plagues. Disguised as a gift, it is a chemical armament used by foxes as deterrants. It is made from cultivated parasites, which acts on the opponent's brain and causes disorientation. The brain waves are then transmitted by sorcery to surrounding enemies, causing secondary damage. Its power is said to depend on the skills of Disarm Traps and Gene Engineering of the user. \\n#~Fool me twice, Shame on me!~"):
        "Detta anche la scatola della pestilenza. È mascherata da regalo, ma è un'arma chimica che le volpi usano per stregare e uccidere. La fanno coi parassiti: agisce sul cervello e porta disturbi di coscienza. Poi la stregoneria propaga quelle onde ai nemici intorno e fa danni di rimbalzo. La sua potenza, dicono, dipende dalle tecniche di Disarmo trappole e di Ingegneria genetica. \\n#~Non ci Casco Più! Come Scoprire i Trucchi dei Mostri~",

    # ---------------------------------------------------------- :43767
    (43767, 'Introduced as a solution to the increasing number of untrained pets, which was becoming a social problem. Pets can be trained in exchange for this coupon. They are distributed free of charge to each household, and people who do not have pets can use them as gifts for those who do. \\n#~Palmia Public Services~'):
        "È stato introdotto come rimedio a un problema sociale: i compagni maleducati erano sempre di più. Dandolo a un compagno, in cambio del biglietto viene addestrato. Lo distribuiscono gratis a ogni famiglia, e chi un compagno non ce l'ha pare lo regali a chi ce l'ha, per farsi offrire da bere. \\n#~Bollettino di Palmia~",

    # ---------------------------------------------------------- :43768
    (43768, 'The training ticket will only take them up to the basic course. Anything beyond that is not covered.\\n# ~words of a Pet Trainer~'):
        "\\\"Col biglietto si arriva al corso base e non oltre. Più in là non conviene, se non si paga in contanti.\\\"\\n# ~Parole dell'Addestratore di Bestie~",

    # ---------------------------------------------------------- :43769
    (43769, 'Saving tickets is annoying! Pay in Cash!\\n# ~words at the Training Center ~'):
        "\\\"Il biglietto si può usare, ma la pratica è una noia: meglio pagare in contanti!\\\"\\n# ~Avviso Affisso alla Palestra~",

    # ---------------------------------------------------------- :43829
    (43829, 'A potion plug commonly used in modern times. To the average person, they are garbage. \\n#~Thousands of pieces of Junk I love~'):
        "Il tappo di pozione che si usa comunemente oggi. Per la gente normale è spazzatura. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :43962
    (43962, 'A magnificent chain to be proud of. The design is popular because it can be worn anywhere, on the neck, wrist, or ankle, but the most standard is to wear it around the neck and drape it like a necktie.\\n#~Gift for your loved ones~'):
        "Una catena tanto bella da vantarsene. Piace perché il disegno la lascia mettere dove si vuole, al collo, al polso, alla caviglia; ma il modo più comune è portarla al collo e lasciarla pendere come una cravatta.\\n#~Scegliamo un Dono per Chi ci sta a Cuore~",

    # ---------------------------------------------------------- :43963
    (43963, '\\"Don\'t hate me chains because they beautiful, maybe get yourself some cool ass golden chains you\'d be braggin \'bout them like me.\\" \\n# a Slave showing off his chains.'):
        "\\\"Gli altri schiavi, da un po', mi sventolano davanti le loro belle catene e se ne vantano di continuo. La voglio anch'io una catena bella così!\\\" \\n#~Parole di uno Schiavo Fiero delle Sue Catene~",

    # ---------------------------------------------------------- :46010
    (46010, 'Large stuffed shark. It is quite jawsome and very fluffy. However, sharks in Ylva are usually named by their creators on their plush toys. For this reason, they are shunned by humans who want to name their plush toys themselves, and are considered childish by humans who do not name their plush toys, and are not in great demand.\\n#~Shark Believer Compendium~'):
        "Un pupazzo di squalo bello grosso. È fatto proprio a pinna d'arte, e morbidissimo. Solo che a Irva, per i pupazzi di squalo, di regola è chi li fa a dare loro un nome. Per questo chi il nome vuole darlo da sé lo evita, e chi ai pupazzi il nome non lo dà lo trova infantile: di richiesta ce n'è poca.\\n#~Grande Compendio dei Fedeli dello Squalo~",

    # ---------------------------------------------------------- :46213
    (46213, 'A flower that does not grow outdoors. It grows wild in Nefia and absorb its magic using the roots, but almost all plants in this form are monstrous except Dernefia. This very oddity has been studied for many years, but alas fruitless. In addition to the fact that it is difficult to grow in safe layers, it has great medicinal value, which is why there are so few samples of it.'):
        "Un fiore che all'aperto non cresce. Nasce spontaneo nelle Nefia e ne succhia la forza magica dalle radici, ma le piante fatte così, tranne la dernefia, sono quasi tutte diventate mostri. Perché solo la dernefia non diventi un mostro lo studiano da anni, e pare che non ne vengano a capo. Ai piani sicuri attecchisce male, e in più ha virtù che curano, così che mostri e avventurieri se la mangiano volentieri: di campioni ce n'è pochi.",

    # ---------------------------------------------------------- :46214
    (46214, '\\"YES OF COURSE IT SUITS JUA! SHE WILL DEFINITELY GET ALL FLUSTERED WHEN I GIVE IT TO HER! YES I AM GOING NEFIA DIVING\\" \\n# Monologue of a Jure Fanatic'):
        "\\\"Pare che ci sia un fiore introvabile che a Jure donerebbe... Se glielo porto, di sicuro, per quanto faccia la difficile a parole, ci resta contenta... Vado un attimo giù in una Nefia.\\\" \\n# ~Monologo di un Fanatico di Jure~",

    # ---------------------------------------------------------- :46215
    (46215, "It's a plant that heals you a bit when you eat it. \\n#~Identification Report: <Plants> Category~"):
        "È una pianta che, a mangiarla, cura un poco. \\n#~Rapporto di Identificazione: categoria <Piante>~",

    # ---------------------------------------------------------- :46275
    (46275, 'Plastic lid. Light, strong and recyclable. Abundant in the world when plastic bottles were still used. However, many of them were not washed and sent for recycling, and there are idiots who discard them and cause environmental pollution, and eco-terrorist attacks have also broken out because of it. A villain even attempts to control society with a weapon that ejects bottle caps at high speed. It is said that the manufacturers could not stand the various social problems accumulated, leading to the discontinuation of production. Today, with the spread of cheap, easy-to-process pseudo-glass, they have completely become a relic of the past.\\n#~Thousands of pieces of Junk I love~'):
        "Un coperchio di plastica. Leggero, resistente e riciclabile. Ai tempi in cui andavano le bottiglie di plastica ne era pieno il mondo. Solo che in tanti li buttavano nel riciclo senza lavarli, i costi e la fatica sono cresciuti e il recupero è saltato. Per colpa degli imbecilli che li gettavano per strada l'inquinamento è andato avanti, e sono scoppiati anche attentati di ecoterroristi che avevano sbagliato bersaglio. È perfino comparso un malvivente che voleva tenere in pugno la società con un arnese che sparava tappi ad alta velocità. Si dice che i fabbricanti non abbiano retto ai problemi accumulati per più di cent'anni e abbiano smesso di produrli. Oggi che si è diffuso il vetro finto, che costa poco e si lavora facile, sono del tutto roba del passato.\\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :46337
    (46337, 'Small glass beads. In recent years, they have been given a variety of patterns and colours for ornamental purposes. The origin of the name is unknown, there are theories that B-dama is a ball that reacts to the B soul. The pattern inside is sometimes called Flame, because it looks like the Burning Flame inside of a Burning Soul.\\n#~Thousands of pieces of Junk I love~'):
        "Una pallina di vetro. Da qualche anno se ne fanno anche con fantasie e colori vari, che servono da ornamento. Da dove venga il nome non si sa: le tre spiegazioni più accreditate sono che venga da biidoro, che in lingua antica vuol dire vetro; che fossero palline di grado B; e che siano palline che rispondono all'anima B. Quelle col disegno dentro hanno un disegno che a volte chiamano fiamma, e anche qui le spiegazioni più accreditate sono due: che a una cosa senza nome si sia attaccato un termine inventato, e che si chiami fiamma perché a volte, rispondendo all'anima B, pare una fiamma che brucia.\\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :47149
    (47149, 'Warning whistle. A short, sharp blast is used to alert anyone who hears it.The volume itself is not very loud, so it is not suitable for waking sleeping people.\\n#~Tunes of Irva~'):
        "Un fischietto d'allarme. Soffiandoci un colpo corto e secco, chi lo sente si fa attento. Il volume in sé non è granché, quindi per svegliare chi dorme non va bene.\\n#~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :48735
    (48735, 'Cicada had never been popular in its life. After years of being cooped up in the dirt, it decided that it could not go on like this and entered a town. It kept on trying to court females in a way it was not accustomed to. It desperately wants to stay in the forefront until the end of its life if its going to die anyway. \\n#~Irva Insect Encyclopedia~'):
        "Una cicala che in tutta la vita non è mai piaciuta a nessuno. Dopo anni chiusa sottoterra ha deciso che così non poteva andare ed è scesa in città a cercare compagnia. Ha continuato a corteggiare come poteva, ma senza mai un premio, e alla fine le forze le sono venute meno. Se morire deve, vuole morire buttandosi in avanti fino all'ultimo, e si dimena con tutta l'anima. \\n#~Grande Enciclopedia degli Insetti di Irva~",

    # ---------------------------------------------------------- :48736
    (48736, "When hit, they are startled and generate a wave of roars, depending on thrower's gene-engineering and throwing skills. Normal human may not be able to withstand the impact and will probably die. \\n#~Irva Insect Encyclopedia (Footnote)~"):
        "A colpirla si spaventa e manda un'onda di fragore che dipende da Ingegneria genetica, da Lancio e dal livello. Certe volte non regge l'urto e ci lascia la pelle. \\n#~Grande Enciclopedia degli Insetti di Irva: Note~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :48737
    (48737, '\\"Evening heat lingers, and the sound of cicadas on the roadside fades away.\\" \\n#~Songs of a nameless poet~'):
        "\\\"Nel tramonto, sul ciglio dove il caldo ancora dura, si spegne la voce della cicala che si contorce.\\\" \\n#~Le Liriche di un Bardo Senza Nome~",

    # ---------------------------------------------------------- :50878
    (50878, 'Paper with various texts and drawings on it. They are carefully placed in envelopes, but are generally of little value in this state. \\n#~Big Book of Books~'):
        "Un foglio con sopra scritti e disegni di ogni sorta. Lo tengono con cura dentro una busta, ma così com'è, in genere, non vale niente. \\n#~Il Libro dei Libri~",

    # ---------------------------------------------------------- :52579
    (52579, 'A curved stone with magical power to absorb hot air. When it is used as a lens when exposed to hot air, it can pass the magic power through it to suppress freezing damage. However, its range of effect is very narrow and it is useless to protect oneself from the cold air that covers the surroundings. \\n#~Mysterious Ancient Ornaments~'):
        "Una pietra ricurva con la forza magica di assorbire il gelo. Quando si manda gelo, facendoci passare la magia come attraverso una lente, si trattiene la rottura da congelamento. Ma il raggio in cui agisce è strettissimo, e per ripararsi dal gelo che copre tutt'intorno non serve. \\n#~Misteriosi Ornamenti Antichi~",

    # ---------------------------------------------------------- :55273
    (55273, "A barrel with multiple blocks of gunpowder packed in it. When hit, it produces an explosive flame that burns away the surrounding area. Apart from that, when set on fire, it spews out a residue of flame. The power depends on one's carpentry and engineering techniques.\\n# ~Hazardous Materials Handling Manual~"):
        "Un barile con dentro più blocchi di polvere da sparo. A colpirlo genera una fiammata che brucia tutt'intorno. E per conto suo, se prende fuoco, sputa fuori quel che resta della fiamma. In tutt'e due i casi la potenza dipende dalle tecniche di Falegnameria e di Ingegneria genetica.\\n# ~Manuale per il Maneggio di Materiali Pericolosi~",

    # ---------------------------------------------------------- :55859
    (55859, 'Remains of past organisms encapsulated in sedimentary rocks. Body tissues have been replaced by minerals in older strata, but may remain in relatively newer strata. During the Biogeocenozoic period, the technology to reconstruct original organisms from fossils was established. \\n# ~Lumiest Art Catalogue~'):
        "I resti di esseri vissuti un tempo, chiusi dentro una roccia sedimentaria. Nei terreni antichi i tessuti sono stati sostituiti da minerali, ma in quelli più recenti a volte restano. Nell'era della civiltà biochimica, dicono, si era arrivati anche alla tecnica per ricostruire dal fossile l'essere di partenza. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55921
    (55921, 'Soil consisting of very fine particles. It can be kneaded by hand and becomes hard when heated. This property is used to make ceramics. \\n#~Vernis Ore Catalogue~'):
        "Terra fatta di grani molto fini. La si lavora impastandola a mano, e scaldandola diventa dura. È per questa sua qualità che ci si fanno le ceramiche. \\n#~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55983
    (55983, "A mineral with the nickname 'burning stone'. It is said to have been used as a raw material in various fields in former civilizations, but there is not much demand for it in modern Irva. \\n#~Vernis Ore Catalogue~"):
        "Un minerale che ha per soprannome pietra che brucia. Nelle civiltà passate, pare, era materia prima in molti campi, ma nell'Irva di oggi non se ne cerca granché. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :56533
    (56533, 'Survival equipment used in biochemical civilization. It is like an external fat. It has the function of converting excess mass into an energy source, storing it for a long period of time, and then restoring it as needed. Because it was developed for the human physique of the time, it is only as effective as maintaining height and weight for modern organisms. It cannot prevent starvation, so make sure you eat your food. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un arnese da sopravvivenza che si usava nella civiltà biochimica. È come del grasso attaccato fuori. Sa cambiare la massa in più in una riserva di energia, tenerla a lungo e restituirla quando serve. Siccome l'hanno fatto sulla costituzione degli uomini di allora, sui viventi di oggi l'effetto arriva sì e no a mantenere altezza e peso. Di fame non ti salva, quindi mangia come si deve. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :57893
    (57893, 'Tickets issued by Palmia in recent years. They can be used to learn work-related skills for free. The aim is to reduce the burden on jobseekers as much as possible and to stimulate economic activity. They are sent with the salary to citizens who are identified as needing assistance. \\n#~Palmia Public Relations~'):
        "Un biglietto che Palmia emette da qualche anno. Serve a imparare gratis le abilità che il lavoro richiede. Lo scopo è alleggerire il più possibile chi cerca lavoro e dare una spinta all'economia. Arriva insieme allo stipendio ai cittadini che vengono giudicati bisognosi d'aiuto. \\n#~Bollettino di Palmia~",

    # ---------------------------------------------------------- :58024
    (58024, 'Materials processed into a semi-material condition. It is useful in the manufacture of sharp weapons. Apparently the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature affilate. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58086
    (58086, 'Materials processed into a semi-material condition. It is useful for refurbishing sharp weapons. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature affilate. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58148
    (58148, 'Materials processed into a semi-material condition. It is useful in the manufacture of sturdy armor. It is said that the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature robuste. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58210
    (58210, 'Materials processed into a semi-material condition. It is useful for refurbishing sturdy armor. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature robuste. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58272
    (58272, 'Materials processed into a semi-material condition. It is useful in the manufacture of soft armor. It is said that the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature morbide. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58334
    (58334, 'Materials processed into a semi-material condition. It is useful for refurbishing soft armor. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature morbide. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :59728
    (59728, "A gift of trimmed flowers, all in one decorative package. However, it conveys too much seriousness and is rather heavy. If you give it to someone you don't get along with very well, they will be turned off, so think carefully about who you give it to. \\n#~Gift for your loved ones~"):
        "Un dono di fiori recisi messi insieme e decorati. Solo che dice fin troppo bene quanto uno ci tenga, e finisce per pesare. A regalarlo a qualcuno con cui non si va molto d'accordo lo si mette a disagio: pensa bene a chi lo dai. \\n#~Scegliamo un Dono per Chi ci sta a Cuore~",

    # ---------------------------------------------------------- :59790
    (59790, "At first glance, it appears to be just a piece of paper with a pattern drawn on it, but it is imbued with magical power. When thrown, it flies lightly through the air, dealing magical damage to anyone it touches and removing blessing effects. Its power depends on the user's magical equipment and throwing technique. \\n# ~Arcane Almanac~"):
        "A prima vista è solo un foglio con sopra un disegno, ma dentro ci hanno messo forza magica. Lanciandolo vola leggero senza curarsi dell'aria, fa danno magico a chi tocca e cancella anche l'effetto della benedizione. La potenza dipende anche da Dispositivi magici e da Lancio di chi lo usa. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :60125
    (60125, 'When you wake up at certain times of the year, this mysterious box is placed beside you before you know it. When presented to others, this mysterious object is said to bring pain to those who are hostile to it and healing to those who are friendly to it. Since the wrapping cannot be removed by any means, the contents cannot be confirmed, but according to one theory, it is said to contain both disaster and hope. \\n# ~Arcane Almanac~'):
        "Una scatola misteriosa che, in certi periodi, al risveglio ti ritrovi accanto senza ricordarti di averla messa lì. Regalandola, dicono, dà dolore a chi ti è nemico e sollievo a chi ti è amico: un oggetto che nessuno capisce. L'involucro non si stacca in nessun modo, così che il contenuto non si può vedere; ma secondo una voce ci sono dentro la sciagura e la speranza. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :60848
    (60848, 'Remnants of shortened and discarded cigarettes. Note that even in this state, it might still ignite. Although the fire is weak, do not throw it on the ground by mistake. \\n#~Dangers on the Road~'):
        "Quel che resta di una sigaretta fumata e buttata via. Attenzione: anche così può prendere fuoco. La fiamma che fa è debole, ma non ti venga in mente di gettarlo in giro. \\n#~I Pericoli sul Ciglio della Strada~",

    # ---------------------------------------------------------- :61178
    (61178, 'A relative of the eggplant. It is processed into various forms and used for smoking. In ancient times it was toxic to the body, but was bred during biochemical civilization. The current species is not toxic, on the contrary, it contains a large amount of medicinal properties, so it is safe...but be careful, it is addictive. You can chew the leaves as they are to enjoy the flavor and provide nicotine. If they are of good quality, they can help you quit smoking. \\n# ~Sickly Taste of Smoke~'):
        "Una pianta parente della melanzana. La lavorano in tanti modi e serve per fumare. Nell'antichità faceva male, ma nell'era della civiltà biochimica l'hanno migliorata. La specie di oggi non è velenosa, anzi ha dentro molte sostanze che curano, quindi si sta tranquilli... o quasi: dà dipendenza, e va tenuto a mente. Anche masticando la foglia così com'è si sente il sapore e si prende la nicotina. Se è di buona qualità può perfino aiutare a smettere. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61310
    (61310, 'It is not a copper coin because it is made of bronze, not pure copper. It was created for those who want to show their appreciation but do not have enough money to pay platinum coins. They have only recently come into circulation and are still less familiar than platinum coins. \\n# ~Coins of this World - Tyris Edition~'):
        "Non è una moneta di rame, perché è fatta di bronzo e non di rame puro. L'hanno pensata per quando si vuole dire grazie ma non al punto di tirare fuori una moneta di platino. Ha cominciato a girare da poco, e rispetto alla moneta di platino è ancora poco familiare. \\n# ~Le Monete del Mondo: Tyris~",

# 36 voci, 0 ambigue

    # ---------------------------------------------------------- :61312
    (61312, '\\"I was surprised when I found out we have bronze coins over here.\\" \\n# ~words of <Norne> the guide~'):
        "\\\"Quando ho scoperto che anche da queste parti c'erano le monete di bronzo mi sono stupita.\\\" \\n# ~Parole di <Norne> la guida~",

# 4 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-038.jsonl'
RIGHE = {
    42914, 42976, 43174, 43302, 43364, 43426, 43488, 43767, 43768, 43769,
    43829, 43962, 43963, 46010, 46213, 46214, 46215, 46275, 46337, 47149,
    48735, 48736, 48737, 50878, 52579, 55273, 55859, 55921, 55983, 56533,
    57893, 58024, 58086, 58148, 58210, 58272, 58334, 59728, 59790, 60125,
    60848, 61178, 61310, 61312,
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
