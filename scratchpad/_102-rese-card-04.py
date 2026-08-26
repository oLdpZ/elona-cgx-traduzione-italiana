# -*- coding: utf-8 -*-
"""102a - Lotto 4 di `db_card.hsp`: le carte fra la riga 1601 e la 2100 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello.

⭐ **Gia' deciso altrove, e si ricopia:** `ソピアー` → **Sophia**,
`ガイアス・ヴィス` → **Gaius Vis**, `ルルウィ` → **Lulwy**, `ラスキリス` →
**Raskilis**, `生化学文明` → **la civilta' biochimica**, `廃忘獣` → **le bestie
dell'oblio**, `忘却の女神` → **la dea dell'oblio**, `たけのこ` → **i germogli di
bambu'**, `深淵` → **l'abisso**.

⭐ **Coniate qui, e vanno in `glossario.md`:** `アイオン` → **gli Aion**,
`超永遠世界` → **il mondo oltre l'eterno**, `妖術士` → **gli stregoni**,
`自律金属細胞` → **cellule metalliche autonome**.

⚠️⚠️ **`:2097` ha `He''ll` con DUE apostrofi**: e' un refuso di monte dentro la
chiave, e va ricopiato tale e quale o la rete 1 dice «voce senza resa».

⭐⭐ **`:1798` e' una battuta intraducibile alla lettera, e non e' un
dettaglio.** 「この先生きのこれるか」 — «riusciremo a sopravvivere d'ora in
poi?» — si legge anche 「この先生 きのこ」, «questo professore fungo», ed e' da
li' che viene il nome della carta. La frase italiana nasconde allo stesso modo
il fungo dentro una frase seria: «ha poco da **fungere**». L'inglese di monte
rinuncia e scrive una frase piana.

⚠️ `:1616` cita 「ヒトツメ小僧」 col nome giapponese: e' uno spiritello del
folclore e la carta dice **che non c'entra**, quindi tradurne il nome
cancellerebbe proprio la cosa che la frase nega.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :1603 l'occhio della provvidenza
    (1603, "It was created in the Biochemical Civilization to imitate God's surveillance system. Apparently it was a taboo technique even back then. It's a flop with high but incomplete spatial awareness. It has a fierce hatred for the selfish humanity that gave birth to him."):
        "Fu costruito nell'era della civiltà biochimica, imitando il sistema di sorveglianza delle divinità. Pare che già allora fosse una tecnica proibita. Ha una buona percezione dello spazio, ma è un fallimento lasciato a metà. Verso il genere umano che l'ha messo al mondo per capriccio prova un odio feroce.",

    # ---------------------------------------------------------- :1616 la ragazzina monocola
    (1616, "An eye monster that mimics a person by binding nerves and muscles together. It is often thought to have originated from a yokai called Hitotsume Kozo but contrary to the name there is no species connection. It's not a friendly monster but if you compliment its cute big eye it'll blush quite a bit."):
        "Un mostro-occhio che si finge persona legando insieme nervi e muscoli. Si crede spesso che discenda dallo spiritello chiamato Hitotsume Kozo, ma malgrado il nome non c'è nessun legame di specie. Amichevole non lo è affatto; però, se le si dice che ha un occhione carino, si ammorbidisce parecchio.",

    # ---------------------------------------------------------- :1629 <Yayauhqui Tezcatlipoca>
    (1629, 'Tezcatlipoca has been forgiven for his sins during the Great War and regained his original power. He leads an army of smoke appearing and disappearing under the cover of night and plays with the enemy.'):
        "Tezcatlipoca, perdonato per le colpe della grande guerra, ha riavuto la sua forza originaria. Guida un esercito di fumo, appare e scompare confondendosi con la notte, e si prende gioco del nemico.",

    # ---------------------------------------------------------- :1642 <Jaldabaoth> il Figlio del Caos
    (1642, 'A god who calls himself the son of chaos. The arrogant one who wants to destroy all the other gods and reign as the only god in name and reality. His ultimate goal is to reshape the world into a world full of perfect evil.'):
        "Un dio che si proclama figlio del caos. Un arrogante che vuole annientare tutte le altre divinità e regnare come dio unico di nome e di fatto. Il suo scopo ultimo è rifare il mondo perché sia colmo di male perfetto.",

    # ---------------------------------------------------------- :1655 <Orphe> il principe del regno perduto
    (1655, 'Orphe is freed from the will of chaos. A hero who once defied chaos and the only one left alive. He has lost everything he had to protect and everything he loved but he has not lost his pride. His body has been transformed and he has become ageless.'):
        "Orphe liberato dalla volontà del caos. È l'eroe che un tempo sfidò il caos e che, solo fra tutti, fu lasciato in vita. Ha perduto ciò che doveva proteggere e ciò che amava, ma non l'orgoglio. Il suo corpo si è trasformato e non invecchia più.",

    # ---------------------------------------------------------- :1668 <Orphe> l'apostolo del caos
    (1668, "Up until now it was based on Orphe's distorted will but as he approached his original body his will and power of chaos was strengthened to the extreme. With a twisted black sword in his hand he strives to achieve his goal."):
        "Finora la base era stata la volontà di Orphe, per quanto piegata; ma via via che si avvicinava al corpo di un tempo, la volontà e la forza del caos si sono rafforzate all'estremo. Con in pugno la spada nera che ha domato, trama nell'ombra per arrivare al suo scopo.",

    # ---------------------------------------------------------- :1681 <Mikraanesis>
    (1681, 'A collection of Sophia\'s brothers and sisters. Aion a race of gods who have flowed out of the abyss. They migrated to Irva and Gaius Vis from the Trans-Eternal World. They can interfere with the existence of time using the logic of the Trans-Eternal World and can act even when it is stopped. Therefore they are also treated as time gods.'):
        "L'insieme dei fratelli e delle sorelle maggiori di Sophia. Sono gli Aion, la stirpe divina defluita dall'abisso. Dal mondo oltre l'eterno sono emigrati a Irva e a Gaius Vis. Con le leggi di quel mondo interferiscono sul modo d'essere del tempo, e possono agire anche dentro il tempo fermo: per questo li si considera anche divinità del tempo.",

    # ---------------------------------------------------------- :1694 l'Indra di Taishaku
    (1694, 'He is a self-proclaimed emperor among the mighty gods. Although he occasionally lost wars he was still believed to be a powerful and matchless heroic god symbolizing lightning. During the Great War he fought a fierce blitzkrieg against Zeus and Thor.'):
        "Si proclama imperatore fra le divinità potenti. Qualche guerra l'ha anche persa, ma lo si venerava lo stesso come dio eroico e senza pari, simbolo del fulmine. Nella grande guerra, si dice, ingaggiò furiose battaglie di scariche elettriche contro Zeus e Thor.",

    # ---------------------------------------------------------- :1707 il Surya del sole
    (1707, 'Indra\'s brother god. In the past he was as powerful as Indra. It is said that he was abandoned by his mother at birth due to an intense heat emanating from his entire body. Apparently he boasts of his beautiful blonde hair.'):
        "Il dio fratello di Indra. Un tempo aveva una forza pari alla sua. Siccome emana calore intenso da tutto il corpo, si racconta che perfino sua madre, appena nato, lo scagliò via. Pare che vada fiero dei suoi bei capelli biondi.",

    # ---------------------------------------------------------- :1720 il Vayu del vento
    (1720, 'A wind god who boasts of his quickness. He was once a god on par with Indra but when Lulwy stripped him of his power and tore him to pieces the pieces became demons.'):
        "Il dio del vento, fiero della propria rapidità. Un tempo stava alla pari con Indra, ma Lulwy gli tolse la forza e per giunta lo fece a pezzi, e quei pezzi sono diventati mostri.",

    # ---------------------------------------------------------- :1733 il Ravana re dei rakshasa
    (1733, 'He cut off his own head and burned it which gave him a trait that rivals that of the gods. Before the Great War of the Gods he made full use of his characteristics to wage war against Vishnu and Indra and he fought reasonably well. During the Great War he was defeated by a demon that was neither a god nor a spirit and turned into a demon.'):
        "A furia di ripetere l'ascesi feroce di tagliarsi la testa e bruciarla, ottenne una qualità che non cede né a divinità né a spiriti. Prima della grande guerra delle divinità la sfruttò a fondo per muovere guerra a Vishnu e a Indra, e se la cavò piuttosto bene. Nella grande guerra fu sconfitto da un demone che non era né divinità né spirito, e si trasformò in mostro.",

    # ---------------------------------------------------------- :1746 l'Andhaka dio oscuro
    (1746, "Son of the god of destruction Siva. He was sent to foster care but when they were reunited he unknowingly courted Siva's wife which led to war. They reconciled and fought together during the Great War of the Gods but he was caught off guard and defeated when his father turned into a dog in the midst of it."):
        "Il figlio di Shiva, il dio della distruzione. Era stato dato a balia, e quando si ritrovarono chiese in sposa, senza saperlo, la moglie di Shiva: ne venne una guerra. Nella grande guerra delle divinità si riconciliarono e combatterono insieme, ma a metà scontro suo padre si trasformò in cane; sconvolto da quell'imprevisto, si scoprì e fu battuto.",

    # ---------------------------------------------------------- :1759 la cthulhick
    (1759, 'It is said to be born of a god who sleeps in the deep sea. They are produced in countless numbers but because they are small and weak they tend to be used as bait for fish and as a snack for fishermen. It is said that an individual that miraculously survives and grows up will become a being with high intelligence and magical powers.'):
        "Una schiera che, si dice, genera il dio addormentato negli abissi marini. Ne nascono a migliaia, ma sono piccole e deboli, e finiscono spesso come esca per i pesci o stuzzichino per i pescatori. L'esemplare che per miracolo sopravvive e cresce diventa, dicono, un essere di grande intelligenza e grande potere magico.",

    # ---------------------------------------------------------- :1772 la Matangodea
    (1772, 'A mushroom that has mutated by taking in a piece of a god and radioactive material. They are revered by the mushrooms. Its body feels and tastes like a sweet treat but it is dangerous because it is addictive and hallucinogenic.'):
        "Un fungo mutato per aver assorbito una scheggia di divinità e del materiale radioattivo. I funghi la venerano. Il suo corpo pare un dolce ed è buono da mangiare, ma dà assuefazione e allucinazioni: è pericoloso.",

    # ---------------------------------------------------------- :1785 il fungo velenoso bugiardo
    (1785, 'A haunted mushroom that has become a gigantic entity by storing water. In addition to emitting strange beams of light and toxins they also trick people into becoming infested with mycelium. High temperature is a weakness. You can rest assured that the corpse has no poisons or parasitic abilities.'):
        "Un fungo mostruoso ingigantito a forza di accumulare acqua. Oltre a scatenarsi sparando raggi strani e tossine, inganna la gente e le fa attecchire addosso il micelio. Il punto debole è il calore forte. Sul cadavere non restano né veleno né capacità di parassitare, quindi si può stare tranquilli.",

    # ---------------------------------------------------------- :1798 il professore champignon
    # ⭐ La battuta: vedi il docstring. «Fungere» nasconde il fungo dentro una
    #    frase seria, che e' esattamente quel che fa il giapponese.
    (1798, "A leader-type mushroom that leads a group of armed mushrooms. They are armed with energy weapons but quite feeble. If we can't beat it we won't live long."):
        "Un fungo del tipo comandante, che guida un drappello di funghi armati. È armato di armi a energia, ma è piuttosto gracile. Chi non riesce a batterlo, da qui in avanti, ha poco da fungere.",

    # ---------------------------------------------------------- :1811 il fungo spruzzante
    (1811, "This mushroom is particularly fond of places with high moisture content. They protect themselves from external enemies by spraying water or disorient them with fog. It is especially dangerous if it is growing in clusters. As it is it's watery and not very tasty."):
        "Un fungo che predilige i posti pieni d'acqua. Si difende dai nemici spruzzando getti d'acqua o confondendoli con la nebbia. Quando cresce in colonie è particolarmente pericoloso: attenzione. Così com'è sa d'acqua e non è granché buono.",

    # ---------------------------------------------------------- :1824 la bestia fungo
    (1824, 'A collection of various mushrooms. It is the corpse of another creature controlled by mushroom mycelium. A beast that seeks nourishment and devours all living things with its sharp fangs.'):
        "Un insieme di funghi di ogni sorta. In verità è il cadavere di un'altra creatura, manovrato dal micelio dei funghi. Una belva che cerca nutrimento e azzanna con le zanne aguzze tutto ciò che vive.",

    # ---------------------------------------------------------- :1837 il fungo travolgente
    (1837, 'It has the ability to fire a series of small spores like a machine gun. Unlike primitive mushrooms they have well-developed legs and are good at moving around. It is believed that these traits were acquired to fight against the bamboo.'):
        "Ha la capacità di sparare a raffica spore minute, come una mitragliatrice. A differenza dei funghi primitivi ha le zampe ben sviluppate ed è bravo anche a spostarsi. Si ritiene che queste qualità le abbia acquisite per combattere i germogli di bambù.",

    # ---------------------------------------------------------- :1850 <Bonyac> il merciaio
    (1850, 'A merchant who owns a general store in the depths of the valley. It is said to be rather popular among travelers and adventurers who are looking for respite. He struggled to get his own store so he has a strong attachment to it and values it more than his own life.'):
        "Un mercante che tiene una merceria in fondo alla valle. Pare che fra i viandanti e gli avventurieri in cerca di riposo abbia un discreto successo. Ha faticato parecchio prima di avere un negozio suo, e per questo ci è affezionatissimo: lo tiene più caro della propria vita.",

    # ---------------------------------------------------------- :1863 la maestà del teschio d'argento
    # ⚠️ Il nome della carta e' femminile: la resa non cambia genere a meta' strada.
    (1863, "A killing weapon made up of silvery fluid metal. Although he thinks he's a stylish little badass he's called Majesty due to his ugly appearance and actions. He has a habit of grumbling and grinning."):
        "Un'arma da assassinio fatta di metallo fluido color argento. Lei si crede appena un po' elegante e un po' cattiva, ma per l'aspetto raccapricciante e per quello che combina la chiamano maestà e ne hanno paura. Ha il vizio di battere i denti e sghignazzare.",

    # ---------------------------------------------------------- :1876 la vecchia campana
    (1876, 'An old bell that has survived many years. It\'s gotten quite large as a result of taking in a lot of metal. Its body is so heavy that it doesn\'t try to move much. The old thing hates the new and tries to corrode them by spraying them with a dissolving fluid.'):
        "Una vecchia campana che ha attraversato lunghissimi anni. A forza di inglobare metallo è diventata piuttosto grande. Ha il corpo pesante e non prova nemmeno a muoversi. Detesta i giovani e cerca di corroderli spruzzandoli di liquido solvente: una rovina di vecchia.",

    # ---------------------------------------------------------- :1889 l'oricalca
    (1889, 'A small doll made of legendary materials. It has an ego embodies the imagination and is capable of flight. It is their mission to fight in arms and bring victory to their creator lord. After the death of the master the individual becomes a stray and contracts to find a new master who will supply them with energy.'):
        "Un pupazzo di piccola taglia fatto di materiali leggendari. Ha un io suo, dà corpo all'immaginazione e sa anche volare. Combatte rivestita di armi, e la sua missione è portare la vittoria al signore che l'ha creata. L'esemplare che perde il proprio signore diventa randagio e cerca un signore nuovo con cui stringere un patto e da cui ricevere energia.",

    # ---------------------------------------------------------- :1902 il desktop alato
    (1902, 'A human-shaped mobile terminal. It began to renew multiply and evolve in a symbiotic manner with autonomous metal cells. The manufacturing company instinctively fought to increase its market share but the company has long since perished with its civilization. In the course of its evolution it adapted to aerial combat and armed itself with a large wing-like flying unit.'):
        "Un terminale portatile dalla forma umana. In simbiosi con cellule metalliche autonome, ha imparato a rigenerarsi, a moltiplicarsi e a evolversi. Continua a combattere d'istinto per allargare la quota di mercato della ditta che l'ha prodotto, ma quella ditta è finita da un pezzo insieme alla sua civiltà. Evolvendosi si è adattato al combattimento aereo e si è dotato di una grande unità di volo a forma d'ala.",

    # ---------------------------------------------------------- :1915 il desktop marino
    (1915, 'A human-shaped mobile terminal. It began to renew multiply and evolve in a symbiotic manner with autonomous metal cells. The manufacturing company instinctively fought to increase its market share but the company has long ago perished with its civilization. In the course of its evolution it adapted to underwater warfare and was equipped with a fish-like underwater mobility unit.'):
        "Un terminale portatile dalla forma umana. In simbiosi con cellule metalliche autonome, ha imparato a rigenerarsi, a moltiplicarsi e a evolversi. Continua a combattere d'istinto per allargare la quota di mercato della ditta che l'ha prodotto, ma quella ditta è finita da un pezzo insieme alla sua civiltà. Evolvendosi si è adattato al combattimento subacqueo e si è dotato di un'unità di manovra subacquea a forma di pesce.",

    # ---------------------------------------------------------- :1928 <Vecchio misterioso>
    (1928, "For as long as anyone knows he has lived in a cave with a white cat. When talking to him he only speaks gibberish so the details are unknown. Many people think he's a creepy old man with dementia but the theory that he's a sage persists."):
        "Da un tempo così lontano che nessuno lo ricorda vive in una grotta insieme a un gatto bianco. A chi gli rivolge la parola risponde solo con frasi enigmatiche, e di lui non si sa altro. I più lo credono un vecchio rimbambito e inquietante, ma l'idea che sia un eremita sapiente è dura a morire.",

    # ---------------------------------------------------------- :1941 la belva dell'oblio
    (1941, 'An incarnation of the Goddess of Oblivion as a mature self. An individual that has eaten a huge amount of memories becomes this form by possessing a healthy human being. It is dangerous because of its ability to summon the Ruined Oblivion.'):
        "La forma adulta dell'incarnazione della dea dell'oblio. Un esemplare che ha divorato una quantità enorme di ricordi assume questa forma impossessandosi di un essere umano sano. È pericolosa perché sa evocare le bestie dell'oblio.",

    # ---------------------------------------------------------- :1954 <Jenna> la fanatica del mistero
    (1954, 'A woman who loves mystical things. Apparently she witnessed a fairy when she was a child. In the past she often vacationed and visited Raskilis.'):
        "Una donna che ama tutto ciò che è misterioso. Pare che sia cominciato da quando, bambina, vide una fata. Un tempo prendeva spesso le ferie per andare a Raskilis.",

    # ---------------------------------------------------------- :1967 <Mary> la raccoglitrice di fiori
    (1967, 'A girl who loves flowers. It was her daily routine to eat freshly baked bread from a general store in Raskilis and then go flower picking. She seems to be quite familiar with flowers and even knows their medicinal and poisonous properties.'):
        "Una ragazza che ama i fiori. Mangiare il pane appena sfornato della merceria di Raskilis e poi darsi alla raccolta dei fiori era la sua giornata di sempre. Di fiori se ne intende parecchio: conosce anche le proprietà curative e quelle velenose.",

    # ---------------------------------------------------------- :1980 <Cray> l'avventuriero curioso
    (1980, 'He has had a lot of adventures so far. He is often hurt because he is driven by curiosity and rushes through. But no matter how many times he fails he never loses his appetite for adventure. For the record he takes the advice of his partner Manson very seriously.'):
        "Ne ha vissute di avventure, fino a oggi. Si lancia in avanti spinto dalla curiosità, e spesso ci rimette. Ma per quante volte fallisca non perde un briciolo di voglia di avventura. In compenso i consigli di Manson, il suo compagno, li ascolta di buon grado.",

    # ---------------------------------------------------------- :1993 <Manson> l'avventuriero prudente
    (1993, 'He is a meticulous person and is good at preparing and managing equipment and food. He worries about his partner Cray as he plunges into adventure but he also envies Cray for his straightforwardness.'):
        "Ha un carattere meticoloso ed è bravo a preparare e a tenere in ordine l'equipaggiamento e le provviste. Si preoccupa vedendo il compagno Cray buttarsi a capofitto nelle avventure, e insieme gli invidia quella schiettezza.",

    # ---------------------------------------------------------- :2006 l'uruk-altezza
    (2006, 'The uppermost species of orc. It developed on its own beyond the vision of the sorcerers. They are strong smart and gentle although they are a bit belligerent. They adamantly refuse the evil orders of sorcerers and live independently.'):
        "La specie più alta degli orchi. Si è sviluppata per conto suo, andando oltre i calcoli degli stregoni. È un po' bellicosa, ma è forte, saggia e gentile. Rifiuta con fermezza gli ordini malvagi degli stregoni e vive per conto proprio.",

    # ---------------------------------------------------------- :2019 l'uruk-hai
    (2019, 'An enhanced and improved species of orc. It was created by merging with humans through sorcery. They possess both high intelligence and a strong body. They make large settlements and live socially.'):
        "Una specie di orco potenziata e migliorata. È nata dalla fusione con gli uomini per via di stregoneria. Unisce grande intelligenza e corpo tenace. Costruisce insediamenti vasti e vive in società.",

    # ---------------------------------------------------------- :2032 il porc nero
    (2032, 'Porc with a special pedigree. From an early age it grew up eating sweet potatoes. Active toned and with good quality muscles. The meat is characterized by a crisp and tasty taste.'):
        "Un porc di stirpe particolare. Fin da piccolo è cresciuto mangiando patate dolci. È attivo, e ha muscoli asciutti e di buona qualità. La carne si distingue per un sapore netto e pulito.",

    # ---------------------------------------------------------- :2045 l'uruk
    (2045, 'An enhanced and improved species of orc created by sorcerers. He has a large strong body. His mind is not very bright so he still needs to improve.'):
        "Una specie di orco potenziata e migliorata, creata dagli stregoni. Ha un corpo grande e tenace. Di testa non è granché, e c'è ancora parecchio da migliorare.",

    # ---------------------------------------------------------- :2058 l'orco nero
    (2058, 'An orc with a completely corrupted soul. His skin is dark and his eyes are vicious. He is shunned even by ordinary orcs because of his apparent evil.'):
        "Un orco dall'anima completamente corrotta. Ha la pelle scura e lo sguardo feroce. Si vede a occhio che è malvagio, e per questo perfino gli orchi comuni lo tengono a distanza.",

    # ---------------------------------------------------------- :2071 il porc di marca
    (2071, 'Unlike the porc that grew up in the wild these elites grew up in a well-groomed environment. They look down on the average porc. The meat clearly tasted fancy.'):
        "A differenza dei porc cresciuti alla buona da qualche parte, questo è un esemplare scelto, allevato in un ambiente curato. Guarda dall'alto in basso i porc comuni. La carne ha chiaramente un sapore da prodotto di pregio.",

    # ---------------------------------------------------------- :2084 il porc
    (2084, 'They were born to an orc and a boar. They have a strong libido and are always naked. In addition when in heat they have a habit of attacking orcs. For this reason it is said to be treated as a beast by orcs. The meat is refreshing and delicious.'):
        "È nato da un orco e un cinghiale. Ha un forte appetito sessuale ed è sempre nudo. Per giunta, quando va in calore, ha l'abitudine di assalire gli orchi. Per questo, pare, gli orchi lo trattano da bestia. La carne è leggera e buona.",

    # ---------------------------------------------------------- :2097 <Toni> il pescatore provetto
    # ⚠️⚠️ `He''ll` con due apostrofi: refuso di monte dentro la chiave.
    (2097, "The man says that fishing is the only thing he enjoys about life. His past is not known in detail though his background is somehow melancholy. He''ll spend the rest of his days fishing until the day the world ends."):
        "Un uomo che dice che la pesca è l'unico piacere della sua vita. La sua schiena ha un che di malinconico, ma nessuno conosce il suo passato nei dettagli. Passerà a pescare anche l'ultimo giorno del mondo.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-004.jsonl'
DA, A = 1601, 2100
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
