# -*- coding: utf-8 -*-
"""116a - Lotto 042 di `db_item.hsp`: LE ARMI, seconda parte.

`FILTER_WEAPON`, righe da `:67045` a `:81879`: **35 righe** su 33 oggetti — 33
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. L'intervallo scelto e'
`67000 82000`, che lascia **34 righe** al lotto 043: due meta' pari invece di
un 42 e un 27.

ⓘ Come nel 041, la categoria non ha moltiplicatore: `applica` deve salire di
**35 esatte**.

### ⭐⭐⭐ DUE FAMIGLIE, E UNA ATTRAVERSA I LOTTI

**La prima e' dentro il lotto, ed e' di cinque righe.** `:75445` (<Libro
Distruttore>), `:77005` (<Kindness Blade>), `:77215` (<Distruttore di Dei>),
`:77285` (<Falce della Bestia>) e `:81606` (<Coda di Frisia>) portano in
giapponese la **stessa identica frase**:

    人では振るえない程の重さだが、使いこなす者が現れた時この武器は
    使用者に<X>を授けるだろう。それと少しばかりの気まぐれを。

e cambia solo l'attributo donato. ⭐ Misurato con uno script prima di scrivere:
la frase compare **5 volte in tutto `db_item.hsp`**, e sono tutte e cinque qui.
La famiglia e' chiusa dentro il lotto, quindi non puo' rompersi dopo.

⚠️ **L'inglese la riscrive cinque volte in modo diverso** — «so heavy that it
cannot be wielded by a single person», «too heavy for a man to wield», «so
heavy that no man can wield it», «It is too heavy for a man to wield», «It is
so heavy that it cannot be wielded by a human being» — dove il giapponese ha
una formula sola. Nessun cancello lo vede: l'inglese e' cinque stringhe
diverse, quindi per la rete 4 sono cinque cose diverse.

⭐ **La forma italiana e' senza genere apposta.** I cinque oggetti sono un
libro, una spada, un'ascia, una falce e un bastone: qualunque clitico («la
possa brandire») avrebbe costretto a cambiare la frase, e la famiglia si
sarebbe rotta sulla grammatica. La forma scelta gira intorno al problema:

    E' di un peso che un uomo non regge, ma quando comparira' chi sa
    servirsene, quest'arma gli donera' <X>. E, insieme, un pizzico di capriccio.

I cinque attributi sono i **nomi del dizionario**, non inventati:
習得 → apprendimento, 意志 → volontà, パワー → forza, 耐久 → costituzione,
魔力 → magia (tutti da `chara.hsp`, «Ottiene +11 in ...»).

**La seconda famiglia attraversa i lotti**, ed e' la sola ragione per cui va
scritta qui. `:76863` (<Stormbringer>) apre con la **stessa prima frase** di
`:51779` (<Ravenbrand>), che sta nel **lotto 041**, chiuso stamattina:
邪を祓う為に更に強大な邪を用いる、という考えから生み出された黒の剣。
Confrontate byte per byte: identiche. La resa e' copiata parola per parola.
⭐ Sono **2 in tutto il file**, e la seconda cambia: `:51779` dice 分身
(«sdoppiamenti»), `:76863` dice 兄弟剣 («gemella», come gia' scrive l'indice 3
di Mournblade). Uguale dove il giapponese e' uguale, diversa dove e' diverso.

⚠️ E l'inglese aggiunge «surrounded with an aura of dread» a **tutt'e due**:
nel giapponese non c'e' ne' qui ne' la'. Un'invenzione ripetuta e' comunque
un'invenzione.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, CIOE' ANCORA INVARIATO

Le sei code del lotto, e nessuna copre due giapponesi:

    ~Irva Fantasy Encyclopedia~      27 righe  (gia' uno dei sei, per Aimwell)
    ~Collection of Armaments...~      4 righe
    ~Book of Wisdom~                  1 riga
    ~words of a God of Destruction~   1 riga
    ~words of a younger sister~       1 riga
    ~Supporting Roles in Kitchen~     1 riga

⭐ E stavolta si e' anche fatta la domanda della 116a — *questo titolo
contraddice un nome gia' a schermo?* — su tutt'e sei, invece di aspettare che
saltasse fuori: «il dio della distruzione» e «sorella minore» sono le forme che
il dizionario usa gia'. Nessuna terza forma. Il numero e' scritto qui **prima**
del montaggio.

### ⭐⭐ L'INGLESE SBAGLIA IN GROSSO TRE VOLTE, E DUE SONO PAROLE SOSTITUITE

  - `:73631` (<Scorticatore Vitale>): **lascia cadere la seconda frase
    intera**, cioe' da dove viene il bastone — le ossa e gli occhi di una
    bestia magica leggendaria, abbattuta al prezzo di migliaia di vite di
    maghi. L'inglese e' una riga sola e la storia sparisce;
  - `:78052` (<Battipalo>): il giapponese dice che a usarlo di gusto e' «un
    fedele accanito di Mani o un **romantico**» (ロマンチスト). L'inglese
    scrive «maniac», che e' un'altra parola e rovescia il senso della battuta:
    il giapponese prende in giro chi ama le macchine, non chi e' pazzo;
  - `:77706` (<Sciabola Dinamica>): 振るうと力が湧いてくる vuol dire «a
    girarla, ti monta dentro la forza» — l'effetto e' su **chi la impugna**.
    L'inglese scrive «it produces a shockwave of power», che e' un'onda d'urto
    e non esiste nel giapponese.

⚠️ La seconda e la terza **nessun cancello le puo' vedere**: l'inglese e'
grammaticale, coerente e plausibile. Solo il giapponese accanto le smaschera.

### ⚠️ E DUE VOLTE APPIATTISCE, NELLA STESSA RIGA

`:67530` (<Housenka>): il giapponese dice che il capo dello sviluppo la
**destino' alle armi pesanti** (大型兵器用にした), e l'inglese scrive «larger
and more powerful», che e' un'altra cosa; e la balsamina del paragone
**sputa i semi** (種を放つ), che e' tutto il punto dell'immagine — l'inglese
scrive «explodes like a rose balsam» e il seme non c'e' piu'.

E `:67181` (falce a catena) perde la frase del 護拳, la guardia sul manico che
serve perche' il contraccolpo della catena non ti faccia ferire la mano sulla
lama.

### ⓘ Il lotto e' uniforme, e la cosa si e' misurata

Tutte e trentacinque le righe hanno lo spazio prima del `\\n` e tutte e
trentacinque la coda `# ~` con lo spazio. Nel 041 c'erano **tre** eccezioni.
Non e' una regola: e' una proprieta' di questo intervallo, e si legge con
`_scheda034.py 042`.

ⓘ Il preflight e' passato al primo colpo: 0 guasti di struttura, nessuna parola
oltre i 14 caratteri, nessun carattere respinto.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :67045
    (67045, 'A combat whip with the tip of the cord reinforced with metal. Originally, the whip was designed to inflict pain rather than fatal injury, but the strengthening of the whip has given it the power to shatter bones. The sound of the tip reaching the speed of sound and striking the air is different from the sound produced when it strikes an object. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una frusta da combattimento, con la punta della corda rinforzata di metallo. In origine la frusta era un arnese per dare dolore più che per uccidere, ma il rinforzo le ha dato la forza di spezzare almeno le ossa. Lo schiocco è il rumore della punta che raggiunge la velocità del suono e batte l'aria: non è il rumore che fa quando colpisce qualcosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :67113
    (67113, 'A sock with a sturdy construction, designed by experts to be used as a weapon. It is a first-class product that does not lose its shape even when filled with sand or coins and swung around as much as possible. The disadvantage is that they are too fine-grained, making them susceptible to moisture and odors. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un calzino di fattura robusta che, dicono, un esperto ha disegnato perché servisse anche da arma. È roba di prima qualità: riempilo di sabbia o di monete e giralo con tutta la forza, non perde la forma. Il difetto è che la trama è troppo fitta, quindi dentro si suda e l'odore ci si attacca. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :67181
    (67181, "A self-defense weapon developed from the scythe, a farming tool. It is common to use the chain to slow down the attacker's movement before approaching and attacking with the sickle. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'arma da difesa nata dalla falce, che è un attrezzo da campo. Ha una guardia sul manico perché il contraccolpo del colpo di catena non ti faccia ferire la mano sulla lama. Di solito si rallenta il nemico con la catena, poi ci si avvicina e si colpisce con la falce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :67460
    (67460, 'Once upon a time, when the God of Destruction assaulted the Goddess of Healing, the guardian protected the Goddess from the destructive blow by using his own body as a shield. The God of Destruction was so impressed by the guardian, who was able to withstand the attack even though his body was shredded, that he gave him this weapon and left. \\n# ~Irva Fantasy Encyclopedia~'):
        "Tanto tempo fa, quando il dio della distruzione assalì la dea della guarigione, il guardiano fece scudo del proprio corpo e la difese fino in fondo dal colpo. Resse l'attacco pur essendo ridotto a brandelli, e alla dea non toccò un graffio; il dio della distruzione ne fu ammirato, gli lasciò quest'arma e se ne andò. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :67462
    (67462, '\\"Offense and defense are two sides of the same coin. If you have something to defend, you should have the strength to do so.\\" \\n# ~words of a God of Destruction~'):
        "\\\"Attacco e difesa sono le due facce della stessa cosa. Se hai qualcosa da proteggere, devi avere la forza che ci vuole.\\\" \\n# ~Parole del Dio della Distruzione~",

    # ---------------------------------------------------------- :67530
    (67530, 'A huge, katana-shaped, high-frequency blade. Originally intended as a personal weapon, it was difficult to handle, so the chief developer decided to make it even larger and more powerful. The excess heat is converted into a flaming projectile, which explodes like a rose balsam. The weight of the sword has been further increased to produce this effect. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lama enorme ad alta frequenza, a forma di katana. In origine era un'arma per un uomo solo, ma era difficile da maneggiare; allora il capo dello sviluppo, non sapendo più che pesci pigliare, la fece ancora più grande e la destinò alle armi pesanti. Quando converte il calore in eccesso in proiettili di fuoco e li fa scoppiare, pare una balsamina che sputa i semi. E per via di questo effetto pesa ancora di più. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :69326
    (69326, 'A scythe whose blade is made of converged astral light. It can be separated from the bone-like section to form a multi-sectioned whip-like shape, allowing for flexible slashing. It symbolizes the severed samsara, eternal rest. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce la cui lama è luce astrale raccolta in un fascio. Si separa in corrispondenza dei nodi, che paiono ossa, e prende la forma di una frusta a più sezioni: così il colpo diventa flessibile. È il simbolo del ciclo delle rinascite spezzato, del riposo eterno. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :70267
    (70267, 'This staff has been handed down from generation to generation to the Gods of Wisdom. It has the power to perceive and record what is happening around the world in an instant, but can only be used by a very limited number of deities. It is also closely related to the Origin of Vice that was once lost. \\n# ~Book of Wisdom~'):
        "Un bastone tramandato di generazione in generazione fra gli dei che presiedono alla sapienza. Ha il potere di percepire e registrare in un istante quel che accade in tutto il mondo, ma solo pochissimi dei sanno usarlo. Ha molto a che fare anche con l'occhio delle tenebre eterne, perduto tanto tempo fa. \\n# ~Il Libro della Sapienza~",

    # ---------------------------------------------------------- :70887
    (70887, 'A hatchet with the power to manipulate gravity. It crushes a slashed opponent by trapping him in a ball of gravity. The slash itself is also heavy with added gravity. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'accetta che racchiude il potere di comandare la gravità. Chiude chi ha colpito dentro una sfera di gravità e lo schiaccia. E anche il colpo in sé, con la gravità addosso, è pesante. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :70958
    (70958, 'A staff-shaped weapon that holds the power of the drake race. Because it is a staff, it is not particularly destructive compared to other weapons. However, it is easy to handle and can be used to make fast, technical strikes. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma a forma di bastone che racchiude la forza della stirpe dei draco. Essendo un bastone non ha una potenza distruttiva particolare, se la confronti con altre armi. Ma si maneggia benissimo, e permette attacchi rapidi e di tecnica. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71776
    (71776, 'A beautiful long sword of light made from a stone said to have been recovered from the moon and used as an oscillator. The surplus energy produced is converted into waves of light. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una bella spada lunga di luce, fatta usando come oscillatore una pietra che, si dice, viene dalla luna. L'energia in eccesso che produce la converte in onde di luce. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73090
    (73090, 'Lance made of the horn of a black unicorn. The power of chaos swirls along the spiral of its surface, gouging through anything that opposes it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lancia fatta con il corno di un unicorno nero. Lungo la spirale della superficie vortica la forza del caos, che scava e passa da parte a parte chi le si oppone. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73422
    (73422, 'Greatsword said to have been born from the fire of God. With holy fire in its blade, it burns and purifies the defiled immortals. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno spadone che, si dice, nacque dentro il fuoco di un dio. Porta nella lama una fiamma sacra, e i non morti corrotti li brucia fino in fondo e li purifica. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73492
    (73492, 'It was born from a failed cultivating attempt. In addition to being uselessly durable like a weapon, the tip is rich in nutrients, making it twice as beneficial as a weapon in one. For some reason, just holding it makes it easier to get a critical hit. \\n# ~Irva Fantasy Encyclopedia~'):
        "È nato da un incrocio andato male. Ha una durezza che non gli serve a niente, e per questo si usa da arma; e visto che la punta è piena di sostanze nutrienti, uno solo è buono due volte. Chissà perché, a tenerlo in mano vengono più colpi critici. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73631
    (73631, "A staff that greatly amplifies magical power at the expense of one's own physical abilities. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un bastone che sacrifica le doti fisiche di chi lo porta per aumentare di molto la forza magica. È fatto con le ossa e gli occhi di una bestia magica leggendaria che, si dice, fu abbattuta a fatica al prezzo di migliaia di vite di maghi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :74030
    (74030, 'What a surprise! Legendary musical instrument, transformed into a blunt weapon by the hands of a master craftsman. The extravagance of the instrument is enough to make anyone who understands the value of musical instruments swoon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Ma guarda un po' che roba. Uno strumento leggendario, per mano di un maestro artigiano, è rinato come arma contundente. Uno sfarzo tale che chi capisce il valore degli strumenti sviene sul posto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75445
    (75445, "A huge book. It is so thick that even a God couldn't read it. It is so heavy that it cannot be wielded by a human being, but when a person comes along who knows how to use it, this weapon will give the user tremendous learning ability. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un libro enorme. Così spesso che nemmeno un dio riuscirebbe a leggerlo tutto. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una capacità di apprendimento smisurata. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75784
    (75784, 'A demon sword that seeps an endless supply of poison from its blade. It is a secret of the ninja, and few people know the details. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lama maledetta dalla quale il veleno trasuda senza fine. È un segreto dei ninja, e quasi nessuno ne conosce i particolari. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75917
    (75917, 'Self-defense item of the Goddess of Healing. It is used to seize an opponent without harming him. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'oggetto con cui la dea della guarigione si difende. Serve a bloccare qualcuno senza fargli male. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76656
    (76656, 'A staff created by the son of the sun God by crystallizing light. It looks like a sword and can actually be used like a sword, but it is only a long staff. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un bastoncino che il figlio del dio del sole ha ricavato facendo cristallo della luce. Sembra una spada, e in effetti si usa anche come una spada, ma resta comunque un bastone lungo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76863
    (76863, 'A black sword, surrounded with an aura of dread, was created from the idea of using an even more powerful evil to exorcise evil. It is rumored that there are a counterpart sword, and that if each is held in both hands, they can become so powerful that they can destroy even the world. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada nera, nata dall'idea di usare un male ancora più grande per scacciare il male. Ne esiste una che si potrebbe dire sua gemella, e dicono che, a stringerle tutt'e due, una per mano, si ottenga una forza capace di distruggere perfino il mondo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77005
    (77005, 'Giant crossed swords designed for euthanasia. Some things can only be healed through death. It is so heavy that no man can wield it, but when someone comes along who knows how to use it, this weapon will give the user a firm will. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada a croce, enorme, fatta per dare una morte dolce. Ci sono cose che solo la morte può guarire. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una volontà ferma. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77215
    (77215, 'A huge battle axe that destroys everything. It is so heavy that it cannot be wielded by a single person, but when a person finds a way to master it, this weapon will give the user tremendous strength. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'ascia da battaglia enorme, che distrugge ogni cosa. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una forza smisurata. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77285
    (77285, 'Scythe made from the bones of a huge subterranean beast. It is too heavy for a man to wield, but when a master emerges, this weapon will give the user boundless constitution. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce ricavata dalle ossa di una bestia sotterranea gigantesca. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una costituzione senza fine. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77494
    (77494, 'Kitchen knife filled with love, anger, and sorrow. The sharpness with which it cuts off the heads of enemies one after another reminds the viewer of a camellia flower falling in droplets. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un coltello da cucina in cui stanno chiusi amore, rabbia e dolore. Taglia via una testa dopo l'altra, e a vederlo viene in mente il fiore della camelia che cade a terra tutto intero, uno dietro l'altro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77496
    (77496, '\\"Hey...get out of the way. If you don\'t get out of my way, I can\'t kill her, can I? I have to teach that thieving pussy cat what happens when you stole something that belongs to someone else...so please don\'t protect her...please. Otherwise, I...!\\" \\n# ~words of a younger sister~'):
        "\\\"Senti... spostati. Se non ti sposti non posso ammazzarla, no? A quella ladra bisogna pure insegnarglielo, che cosa succede a prendersi la roba degli altri... quindi smettila di difenderla... ti prego. Se no io...!\\\" \\n# ~Parole della Sorella Minore che si Fa Sotto~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :77706
    (77706, 'Saber used by a hero who was stigmatized as a pirate. Ironically, it is now in the hands of real pirates. When swung, it produces a shockwave of power. \\n# ~Irva Fantasy Encyclopedia~'):
        "La sciabola che usava un eroe a cui avevano affibbiato il marchio di pirata. Per ironia della sorte, adesso è finita in mano a dei banditi veri. A girarla, ti monta dentro la forza. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77983
    (77983, 'Chainsaw with tremendous cutting power. It can even dismember God. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una motosega che taglia in modo spaventoso. Potrebbe fare a pezzi perfino un dio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :78052
    (78052, 'An electrified stake-shaped shooting spear. It is very difficult to handle, and only a serious Mani-devotee or maniac would like to use such a weapon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma che uccide sparando in avanti una lancia a forma di palo, carica di elettricità. È scomodissima da usare, e a sceglierla di gusto ci sarà solo un fedele accanito di Mani o un romantico. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :78187
    (78187, 'A huge sword. It is so large, thick, heavy, and rough that it is more appropriate to call it a lump of iron than a sword. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno spadone enorme. È talmente grande, spesso, pesante e rozzo che chiamarlo blocco di ferro è più giusto che chiamarlo spada. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :78857
    (78857, 'Small dagger used to handle foodstuffs. Its original purpose is for household use, but since the blade is well sharpened, it may be used in battle. \\n# ~Supporting Roles in Kitchen~'):
        "Un coltellino corto che serve a preparare quel che si mangia. L'uso per cui è fatto è quello di casa, ma la lama è affilata per bene, quindi si potrà usare anche per combattere. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :80286
    (80286, 'A strange long sword with a brilliantly shining blade. The method of making it is completely unknown, but according to rumors, knights in other worlds make it by themselves to show their power when they become full-fledged knights. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada lunga fuori dall'ordinario, con la lama che splende di luce viva. Come si faccia non si sa proprio, ma a quel che si dice i cavalieri di un altro mondo, quando diventano adulti, se la costruiscono da soli per mostrare quanto valgono. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81469
    (81469, 'Special sword made to repel dragons. Its blade glows mysteriously as if it is drenched in fresh blood, and it is said that it slaughters dragons day and night with blows so sharp that they produce electric shocks. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lama speciale, fatta per respingere i draghi. Il suo acciaio luccica in modo inquietante, come fosse bagnato di sangue fresco, e dicono che notte e giorno faccia strage di draghi con colpi tanto affilati da produrre scariche elettriche. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81606
    (81606, "The staff is so large that it could be mistaken for a statue of a giant cat's tail. It is too heavy for a man to wield, but if one were to master it, this weapon would bestow unparalleled magical power upon its wielder. And a little whimsy. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un bastone talmente grande da scambiarlo per la statua della coda di un gatto gigantesco. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una magia senza pari. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81879
    (81879, 'A large scythe with a long handle. The blade is less curved than a sickle, but by grasping the handle with both hands and swinging it vigorously, it is said to reap the battle spirit and body parts of the enemy. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una falce grande, dal manico lungo. La lama è meno ricurva di quella di un falcetto, ma dicono che, afferrando il manico a due mani e girandolo con slancio, si mietono insieme la voglia di combattere del nemico e i pezzi del suo corpo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 33 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-042.jsonl'
RIGHE = {
    67045, 67113, 67181, 67460, 67462, 67530, 69326, 70267, 70887, 70958,
    71776, 73090, 73422, 73492, 73631, 74030, 75445, 75784, 75917, 76656,
    76863, 77005, 77215, 77285, 77494, 77496, 77706, 77983, 78052, 78187,
    78857, 80286, 81469, 81606, 81879,
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
