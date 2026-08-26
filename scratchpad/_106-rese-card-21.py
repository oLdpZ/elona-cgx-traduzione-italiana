# -*- coding: utf-8 -*-
"""106a - Lotto 21 di `db_card.hsp`: le carte fra la riga 10101 e la 10600 (39).

⚠️ **DICIOTTO carte su trentanove hanno l'inglese che finisce con uno SPAZIO**:
`:10118`, `:10144`, `:10209`, `:10235`, `:10274`, `:10287`, `:10313`, `:10326`,
`:10417`, `:10456`, `:10482`, `:10508`, `:10521`, `:10534`, `:10547`, `:10560`,
`:10573`, `:10599`.

⭐⭐ **E' IL LOTTO DEL CANONE: quasi tutte queste carte nominano persone e luoghi
che `chat.hsp` racconta gia'.** Ogni nome e' stato cercato nel dizionario prima
di scriverlo, ed e' li' che stavano i quattro sbagli della 105a:

    異形の森        la **Foresta Eretica**   ⚠️ e `ヴィンデイル`/`Vindale` e' il suo
                                             nome proprio: «figli di Vindale,
                                             quella che chiamano la Foresta
                                             Eretica» (`chat.hsp`). Il nome della
                                             carta `:10573` dice «di Vindale», la
                                             prosa dice «Foresta Eretica»: e' la
                                             stessa cosa detta nei due modi che il
                                             progetto usa gia'
    エレアの民      **gli Elea** / «un Elea», «un'Elea»
    レシマス        **Lesimas**;  《常闇の眼》 **l'<occhio delle tenebre eterne>**
    白き鷹          **il falco bianco** (`db_card`, la carta del dopo)
    竜窟            **la Tana del Drago**
    ルードゥス      **Ludus**;    ヴェルニース **Vernis**;   カルーン **Karune**
    ガベラ          **Gavela** (`<Gavela> l'ingegnere capo`)
    シルヴィア      **Silvia** ⚠️ l'inglese di `:10521` scrive `Sylvia`, il nome
                                 della carta `:10534` e la prosa di `chat.hsp`
                                 dicono Silvia: si traduce dal giapponese
    吟遊詩人        **il menestrello**;   ルルウィ **Lulwy**;   プラチナ **platino**

ⓘ **Coniato qui:** `猫族` → **il popolo dei gatti** (`:10521`): non compare in
nessun'altra voce del dizionario.

⚠️⚠️ **DUE CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**
`:10495` dice 集めるだけでは飽き足らず — «collezionarli non le bastava» — e
l'inglese lo rovescia in `so bored with collecting them`; `:10105` dice
乗り物にすごく弱い — «i mezzi di trasporto gli fanno malissimo» — che l'inglese
appiattisce in `motion sickness`, perdendo il perche' la carta lo dica.
ⓘ E' la stessa specie del `適当な教育` del lotto 20: l'inglese di monte capovolge
la frase, non la accorcia.

ⓘ **`:10131` e' la carta della decisione aperta dell'82a**, la 🔶 sorella H: il
giapponese apre con ヒットマンな妹 e la battuta di `chat.hsp:6717` («la H sta per
hentai, ma io preferisco hitman!») arriva quando il nome italiano — «la sorella
minore sicaria» — ha gia' svelato il mestiere. **Qui non si decide niente**: la
prosa dice quel che dice il giapponese, e la decisione resta dov'era, in attesa
delle due schede a schermo.

ⓘ `:10183`, `:10222` e `:10365` hanno il **nome** ancora non reso (`IT None` nel
dossier): sono i doppioni di 姉, 店主 e ガード, che nel dizionario stanno gia'
sotto l'altra occorrenza. Le prose invece sono tutte e tre diverse, e si rendono.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :10105 <Zernard> il mercenario provetto
    (10105, 'He is an unusually skilled mercenary and has considerable experience among mercenaries, whose quality has continued to decline in recent years. However, he has motion sickness. For this reason, he mainly works in jobs that do not involve long-distance travel.'):
        "Fra i mercenari, la cui qualità continua a calare di anno in anno, è uno dei rari che sappiano davvero il mestiere, e di esperienza ne ha accumulata parecchia. Solo che i mezzi di trasporto gli fanno malissimo, e per questo prende soprattutto lavori senza lunghi spostamenti.",

    # ---------------------------------------------------------- :10118 <Heinrich> il generale corazzato
    (10118, 'He likes the smell of gunpowder, the sound of mechanical drives and machine oil, and despite being a general, his hobby is designing mechanisms. From time to time, he devises absurd equipment and gets excited with Gavela. '):
        "Gli piacciono l'odore della polvere da sparo, il rumore dei motori e il profumo dell'olio da macchine, e benché sia un generale il suo passatempo è progettare congegni. Ogni tanto inventa equipaggiamenti assurdi e si esalta insieme a Gavela. ",

    # ---------------------------------------------------------- :10131 la sorella minore sicaria
    (10131, 'Hitman younger sister. She enjoys hiding in the vicinity of her kill targets and killing them after terrorising them extensively with the daily sound of her chainsaw. She has a strong personality and keeps a very cringy diary.'):
        "Una sorella minore che fa la sicaria. Si apposta vicino al bersaglio, ogni giorno gli fa sentire il rumore della motosega e, dopo averlo fatto morire di paura, se lo prende: è quello il suo piacere. Ha un carattere fortissimo e tiene un diario da far accapponare la pelle.",

    # ---------------------------------------------------------- :10144 la sorella maggiore
    (10144, 'Your older sister, who lives in Ludus and is not blood-related to you. She is always waiting for you to come home, although she is dissatisfied with your occasional visits. '):
        "La tua sorella maggiore, che vive a Ludus e non ha il tuo sangue. Le dispiace che tu ti faccia vedere solo ogni tanto, eppure il tuo ritorno lo aspetta sempre. ",

    # ---------------------------------------------------------- :10157 la sorella cane maggiore
    (10157, "Non-blood-related older sister-in-law of a human-friendly canine family. She is not very strong, although she is as intimidating as possible towards those who would avenge her brother (or sister). Maid's clothes are a hobby."):
        "Una sorella acquisita, di stirpe canina e affettuosa, che non ha il tuo sangue. Con chi vuole fare del male al fratello (o alla sorella) minore ringhia con tutta sé stessa, ma non fa una gran paura. Il vestito da cameriera è un suo gusto.",

    # ---------------------------------------------------------- :10170 il Rudras
    (10170, 'Sons of Rudra, the storm god, who inherited his power. During a struggle for supremacy with Lulwy of the Wind, their bodies were destroyed and turned into tornadoes themselves. Since then, they have been sworn to her allegiance.'):
        "I figli che hanno ereditato la forza di Rudra, il dio della tempesta. Nella lotta per il primato con Lulwy del vento il loro corpo fu distrutto e furono trasformati in trombe d'aria. Da allora sono costretti a giurarle fedeltà.",

    # ---------------------------------------------------------- :10183 la sorella maggiore
    (10183, 'Your older sister who is not related to you by blood. She still loves you and always wants you to spoil her. To her, you will always be her little brother (sister).'):
        "La tua sorella maggiore, che non ha il tuo sangue. Eppure ti vuole un bene dell'anima e non aspetta altro che tu le faccia qualche coccola. Per lei tu resterai per sempre il fratello (o la sorella) minore.",

    # ---------------------------------------------------------- :10196 il bug
    (10196, "A being that shouldn't exist. Its origin varies."):
        "Una forma di vita che non dovrebbe esistere. Le cause per cui compare sono le più varie.",

    # ---------------------------------------------------------- :10209 user
    (10209, 'Abbreviation for unique-subconscious-extra-reactant. The unique human subconscious has reacted with things outside this world and established its presence on this side of the world. '):
        "Sigla di Unique-subconscious-extra-reactant, il corpo che reagisce fuori campo per via di un subconscio particolare. Il subconscio particolare di un essere umano ha reagito con qualcosa che sta fuori da questo mondo, e ne ha fissato la presenza al di qua. ",

    # ---------------------------------------------------------- :10222 il negoziante
    (10222, 'A person who sells various goods and serves as the public face of the town. Adept at using firearms to prevent robbery. Since they have next to no ability to negotiate, a rigorous training period is required when they inherit a store.'):
        "Il volto della città, che vende ogni sorta di merce. Contro le rapine è bravissimo a maneggiare le armi da fuoco. Di talento per la trattativa non ne ha quasi per niente, e pare che quando eredita la bottega gli tocchi un addestramento durissimo.",

    # ---------------------------------------------------------- :10235 il capo della carovana
    (10235, 'They are entrusted with leading caravans organised by traders for collective security. They are well trusted by the state and can pass through customs with only a simple check. '):
        "Gli è affidato il comando delle carovane che i mercanti organizzano per difendersi tutti insieme. Gode di grande fiducia presso lo stato, e ai posti di blocco passa con un controllo sbrigativo. ",

    # ---------------------------------------------------------- :10248 il barista
    (10248, 'One has mastered resurrection in order to collect money from drunken and dead customers as well. In recent years, they has been baffled by the growing popularity of side jobs such as resurrection services and pet care. They are secretly very happy when people order drinks from them.'):
        "Per riscuotere il conto anche dai clienti che muoiono ubriachi ha imparato l'arte di risuscitare. In questi anni i mestieri secondari, come il servizio di resurrezione e la custodia degli animali, sono diventati più richiesti del suo, e la cosa lo lascia un po' perplesso. Quando gli ordinano da bere, dentro di sé è contentissimo.",

    # ---------------------------------------------------------- :10261 l'informatore
    (10261, 'They live to reveal the information they have. When requested to do so, this professional can even find out the weight of a target in an instant. In their profession, they are sometimes blinded by national secrets and eliminated.'):
        "Vive per sfoggiare le informazioni che possiede. Se glielo si chiede, questo professionista scopre in un istante perfino quanto pesa il bersaglio. È un mestiere in cui a volte, accecati da un segreto di stato, si finisce tolti di mezzo.",

    # ---------------------------------------------------------- :10274 il padrone dell'arena
    (10274, 'Their hobby of watching bloody fights has gone too far and they have built an arena. Because of the money they spend on living expenses for the arena, they are repeatedly told by their families to stop. '):
        "Il gusto di guardare i combattimenti sanguinosi gli ha preso talmente la mano che si è costruito un anfiteatro. Siccome nell'arena butta i soldi che servono per vivere, la famiglia gli ripete da anni di smetterla. ",

    # ---------------------------------------------------------- :10287 la guaritrice
    (10287, 'They have mastered the art of dispelling mental and physical ailments and curses that have been placed on them. Because of their popularity, some people go to great lengths to be healed by them. '):
        "Ha imparato l'arte di scacciare lo sfinimento del corpo e dello spirito, e le maledizioni che ci si trova addosso. C'è perfino chi si mette apposta nei guai peggiori pur di farsi curare da loro. ",

    # ---------------------------------------------------------- :10300 la sorella
    (10300, "A nun in the service of God. She listens to all kinds of people's confessions without distinction, but when she is angry, her true nature comes out. She also shows no mercy to those who do not show sincerity."):
        "Una monaca consacrata alla divinità. Ascolta senza distinzioni le confessioni di chiunque, ma quando si arrabbia le esce fuori com'è fatta davvero. E con chi non le mostra sincerità non usa nessuna pietà.",

    # ---------------------------------------------------------- :10313 il capo villaggio
    (10313, 'When it was decided to choose a leader, no one stood for the job, so it was decided by lot. The work as head is neglected, but everyone is too lazy to even complain about it. '):
        "Quando si dovette scegliere il capo non si candidò nessuno, e allora lo tirarono a sorte. Il lavoro di capo lo trascura volentieri, ma sono tutti troppo pigri anche solo per lamentarsi. ",

    # ---------------------------------------------------------- :10326 l'istruttore
    (10326, "Has an amazing talent for teaching others things they can't do themselves. He does not belong to a guild because he hates being pinned on his earnings. "):
        "Ha il talento straordinario di insegnare agli altri perfino quello che lui non sa fare. Non gli va che gli sfilino una fetta del guadagno, e per questo alla gilda non appartiene. ",

    # ---------------------------------------------------------- :10339 l'istruttore della gilda
    (10339, 'Trainer affiliated with the guild. They are very shy and seldom go outside the guild. Half of the platinum he earns goes to the guild.'):
        "Un istruttore che appartiene alla gilda. È di una timidezza fortissima e fuori dalla gilda non mette quasi mai piede. Metà del platino che guadagna finisce alla gilda.",

    # ---------------------------------------------------------- :10352 la guardia
    (10352, 'According to one theory, they ought to protect the peaceful lives of the civilians. They have a habit of defending themselves at all costs when harm comes to them. If they die, they must undergo rigorous re-training.'):
        "Stando a una certa teoria proteggerebbe la vita tranquilla dei cittadini. Ha l'abitudine, appena il pericolo tocca lei, di difendere sé stessa con tutte le forze. Se muore, l'aspetta un riaddestramento durissimo.",

    # ---------------------------------------------------------- :10365 la guardia
    (10365, 'According to one theory, they ought to protect the peaceful lives of the civilians. They have a habit of defending themselves at all costs when harm comes to them. He is also a observer and has full knowledge of the whereabouts of the citizens.'):
        "Stando a una certa teoria proteggerebbe la vita tranquilla dei cittadini. Ha l'abitudine, appena il pericolo tocca lei, di difendere sé stessa con tutte le forze. È anche una sorvegliante, e sa in ogni momento dove si trovi ciascun cittadino.",

    # ---------------------------------------------------------- :10378 il soldato scelto di Palmia
    (10378, 'Special forces are sent out to buy time for the authorities to evacuate. Their dispersal is the spice of the battlefield. It is also sad that they are so serious about their job.'):
        "Un reparto speciale che mandano allo sbaraglio per far guadagnare tempo ai pezzi grossi in fuga. Il modo in cui cadono è la spezia che dà colore al campo di battaglia. E la cosa più triste è che loro ci credono sul serio.",

    # ---------------------------------------------------------- :10391 <Zeome> il falso profeta
    (10391, 'A mage who forsake both status and freedom to pursue his thirst for knowledge. Even had he not been sealed within the depths of Lesimas, he would have remained there to continue viewing the Origin of Vice.'):
        "Un mago che, spinto dalla fame di sapere, ha buttato via posizione e libertà. Anche se non fosse stato sigillato insieme ai piani bassi di Lesimas, sarebbe rimasto laggiù di sua volontà a contemplare l'<occhio delle tenebre eterne>.",

    # ---------------------------------------------------------- :10404 @
    (10404, 'Certain people realised the limits of their power, while others uttered the words in the hope that they would be active in the next life. Somehow it gained power and crawled around in the crevices of the world. Until the day it is called by its name.'):
        "C'è chi ha capito il limite della propria forza e chi ha pronunciato quella parola sperando in una vita futura piena di imprese. E quella parola, un giorno, ha ottenuto una forza sua e si è messa a strisciare per gli interstizi del mondo. Fino al momento in cui qualcuno la chiamerà per nome.",

    # ---------------------------------------------------------- :10417 <Orphe> il prediletto del caos
    (10417, 'Chosen by the God of Chaos as his agent. He is given a portion of the knowledge and power, as well as the Sword of Chaos, and works in the dark to envelop the world in chaos. '):
        "Colui che il dio del caos ha scelto come proprio vicario. Gli ha ceduto una parte del sapere e della forza, e insieme la spada del caos, e lui trama nell'ombra per avvolgere il mondo nel caos. ",

    # ---------------------------------------------------------- :10430 <Scienziato pazzo>
    (10430, 'One who seeks the truth of the world and wishes to control it. He has madness in his eyes and is considered dangerous to be left unchecked. His scientific powers are indistinguishable from magic.'):
        "Uno che cerca la legge che regge il mondo e vuole dominarla. Negli occhi gli abita la follia, e lasciarlo libero sembra pericoloso. La sua scienza non si distingue dalla magia.",

    # ---------------------------------------------------------- :10443 <Isca> l'angelo caduto
    (10443, 'She was stripped of her powers and dismissed from her job because she was living a self-defeating life without any work as an angel. However, she is happy that she can now take naps without any worries. She still has wings that have lost their function and have become decorations, but it appears that removing them is also a hassle.'):
        "Da angelo non lavorava per niente e conduceva una vita sregolata, così le hanno tolto i poteri e l'hanno licenziata. Lei però è contenta: adesso può schiacciare un pisolino senza pensieri. Le restano le ali, che hanno perso la loro funzione e sono diventate un ornamento, ma a quanto pare toglierle è una noia.",

    # ---------------------------------------------------------- :10456 <Chi striscia nel vuoto>
    (10456, 'The White Hawk, a commoner who rose to a high position in Zanan Military with his abilities, but has fallen to the ground after losing someone he cared about. Now addicted to drugs, with his consciousness wandering aimlessly in the sky. '):
        "Il falco bianco che, pur venendo dal popolo minuto, con le sue capacità era salito fino agli alti gradi di Zanan, e poi è caduto a terra per aver perso la persona a cui teneva. Adesso annega nella droga, e la sua coscienza vaga vuota per il cielo. ",

    # ---------------------------------------------------------- :10469 <Loyter> l'eroe cremisi di Zanan
    (10469, 'A talented soldier with long red hair who is hailed as a hero of Zanan. He wanted to win against the White Hawk on his own merit, but they dropped out on their own accord, so he feels ashamed inside. He is also famous for his strong shoulders.'):
        "Un militare capace, dai lunghi capelli rossi, che a Zanan celebrano come un eroe. Voleva battere il falco bianco sul campo, con le proprie forze, ma quello si è tirato fuori da solo, e dentro di sé se ne rode. È famoso anche per la potenza del suo braccio.",

    # ---------------------------------------------------------- :10482 <Vesda> il drago di fuoco
    (10482, 'A descendant of the legendary flame dragon, born from the flames of a primordial god. When dragon hunters once attacked the Dragon Cave, all the other dragons were wiped out, but for some reason the flame dragon was not targeted and survived. '):
        "Discendente del leggendario drago di fuoco, nato dalla fiamma del dio primordiale. Quando i cacciatori di draghi assalirono la Tana del Drago tutti gli altri draghi furono sterminati, ma il drago di fuoco, chissà perché, non fu nemmeno preso di mira e sopravvisse. ",

    # ---------------------------------------------------------- :10495 <Miches> l'apprendista
    (10495, 'A girl who loves stuffed toys. She is so bored with collecting them that she has taken up an apprenticeship to become a stuffed animal craftsman. However, she is surprisingly clumsy and is still an apprentice.'):
        "Una ragazza che va matta per i pupazzi di pezza. Collezionarli non le bastava, e allora si è messa a bottega per diventare artigiana di pupazzi. Solo che, contro ogni previsione, ha le mani di pastafrolla, e apprendista è rimasta.",

    # ---------------------------------------------------------- :10508 <Shena> l'attrazione del locale
    (10508, 'A girl who works in a tavern in Vernis. Her irresistible buttocks are a magnet for men and women alike, and she is unaware of the bloodshed amongst the nobility over her panties. '):
        "Una ragazza che lavora nella taverna di Vernis. Il suo fondoschiena incanta uomini e donne senza distinzione, e lei non sa che i nobili si stanno scannando per accaparrarsi la sua biancheria. ",

    # ---------------------------------------------------------- :10521 il guerriero dalla testa di leopardo
    (10521, 'A warrior of the cat tribe who wandered in from another world. He cares for Sylvia, but has been away on expeditions for too long. '):
        "Un guerriero del popolo dei gatti che si è smarrito qui da un altro mondo. A Silvia tiene molto, ma è stato via per le spedizioni per un tempo davvero troppo lungo. ",

    # ---------------------------------------------------------- :10534 <Silvia> la principessa
    (10534, 'She is an imperial princess who was cast out of another world. She was subjected to a full course of abduction, confinement and humiliation during a period of instability, and has turned into a sex-crazed woman who repeatedly has affairs with the people she once loved. '):
        "Una principessa imperiale sbalzata qui da un altro mondo. In un periodo fragile ha subito il trattamento completo, rapimento, prigionia e violenza, e da allora è diventata una donna smaniosa che in chi ha davanti rivede la persona amata di un tempo e ripete un amore dopo l'altro. ",

    # ---------------------------------------------------------- :10547 <Spazzino di sotterranei>
    (10547, "Artificial life forms created to clean up the town and Nefia. One is also placed in Vernis's tavern at the request of customers who are concerned about the remains of the bards. "):
        "Forme di vita artificiali costruite per ripulire le città e le Nefia. Su richiesta dei clienti, infastiditi dai resti dei menestrelli, ne hanno messo uno anche nella taverna di Vernis. ",

    # ---------------------------------------------------------- :10560 <Larnneire> l'ascoltatrice del vento
    (10560, "Elea folk who came from the Vindale Forest. She is known as 'the Listener of the Wind', due to her ability to sense distant conditions from the wind. "):
        "Un'Elea venuta dalla Foresta Eretica. La chiamano l'ascoltatrice del vento, e il nome le viene dalla capacità di sentire dal vento che cosa accade lontano. ",

    # ---------------------------------------------------------- :10573 <Lomias> il messaggero di Vindale
    (10573, 'Elea folk who came from the Vindale Forest. Initially, there were other messengers, but they all became stuck due to mysterious illnesses, and as a result, only he and Larnneire were able to leave. '):
        "Un Elea venuto dalla Foresta Eretica. All'inizio i messaggeri erano anche altri, ma si ammalarono tutti in modo misterioso e non poterono più muoversi: alla fine partirono soltanto lui e Larnneire. ",

    # ---------------------------------------------------------- :10586 <Slan> l'ombra di Palmia
    (10586, 'A secret agent in the service of the Palmia royal family. He is on the edge of his seat, determined not to die until he has passed on the information he has obtained to the king. He planned to get married when his mission was over.'):
        "Una spia al servizio della casa reale di Palmia. Finché non avrà consegnato al re le informazioni che ha raccolto non può permettersi di morire, e resiste appeso a un filo. Quando la missione fosse finita, aveva in programma di sposarsi.",

    # ---------------------------------------------------------- :10599 <Karam> il lupo solitario di Karune
    (10599, 'He is an adventurer employed to investigate Lesimas and hails from Karune. He is a solitary, competent and capable person, hence his nickname of the Lone Wolf... although he believes he is not as competent as he thinks he is. '):
        "Un avventuriero originario di Karune, assunto per l'esplorazione di Lesimas. Solitario, capace, uno che vale davvero: per questo si porta il soprannome di lupo solitario... o almeno così si era convinto lui, perché tanto in gamba non è. ",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-021.jsonl'
DA, A = 10101, 10600
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_card.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
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
