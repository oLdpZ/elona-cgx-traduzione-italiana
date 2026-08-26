# -*- coding: utf-8 -*-
"""106a - Lotto 24 di `db_card.hsp`: le carte fra la riga 11601 e la 12100 (39).

⭐⭐⭐ **L'ELEFANTE INDIANO E' UNA GAG VERA DEL GIAPPONESE, E QUESTO LOTTO LO
DIMOSTRA.** Nei lotti 19 e 20 avevo segnato tre carte in cui l'inglese scriveva
`Indian Elephant` e il giapponese diceva altro (`:9338` 人間の腕, `:9377`
下位の巨人, `:9728` 頚動脈, senza elefante). Qui `インド象` sta **nel
giapponese**, in **sette** carte di fila — tutta la famiglia dei segugi, da
`:12018` a `:12096` — ed e' il tormentone con cui monte misura la potenza di ogni
soffio.

⚠️ Quindi la conclusione dei lotti 19-20 **non cambia ma si precisa**: l'elefante
e' di monte, e proprio perche' e' un tormentone vero e' facile che il traduttore
inglese l'abbia infilato anche dove il giapponese non ce l'ha. Le tre carte di
prima restano rese dal giapponese; queste sette portano l'elefante, perche' ce
l'hanno davvero. ⓘ `インド象` → **l'elefante indiano** era gia' nel dizionario
(la carta dell'ambrosia molesta).

⚠️ **SEDICI carte hanno l'inglese che finisce con uno SPAZIO**: `:11602`,
`:11628`, `:11641`, `:11654`, `:11667`, `:11680`, `:11771`, `:11784`, `:11797`,
`:11849`, `:11914`, `:11927`, `:11940`, `:11953`, `:11966`, `:11979`.

⚠️⚠️ **TRE CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**

    :11641  手にした獲物を振るう      獲物 qui e' **l'arma** che ha in mano, non
                                      la preda: l'inglese legge `the prey in his
                                      hands` e la frase perde il senso
    :11667  己のコブシのみで戦える     コブシ sono i **pugni**; l'inglese scrive
                                      `using only his knob`
    :11875  よく裏切るやつ、という     al pipistrello da' fastidio la **fama di
            イメージのせいで迷惑        traditore**; l'inglese scrive `they are
                                      inconvenienced by the inaccurate vision`,
                                      che contraddice la frase prima

⭐ **`:11628` conferma la scelta di `:9351`.** La carta dell'uomo lucertola dice
硬い鱗の肌を持つ**竜人**の戦士: `リザードマン` **e'** un `竜人`, cioe' la razza
che il progetto chiama «Uomo lucertola». Qui non c'e' collisione, perche' la
carta parla di se stessa; a `:9351` c'era, ed e' per questo che li' 竜人 e' reso
col nome della creatura, «dragonewt».

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `インド象` → **l'elefante
indiano**, `ワイバーン` → **la viverna**, `ファイアボルト` → **saetta di fuoco**
(`db_item.hsp`), `死神` → **la Morte** (`buff.hsp:80`), `リッチ` → **il lich**
(`invariati.md`), `エレア` → **gli Elea**, `ネフィア` → **le Nefia**, `マナ` →
**il mana**, `牛人` → **l'uomo toro** (come il Moloch del lotto 20), `エント` →
**l'Ent**, `プチ`, `トロール` → **il troll**.

ⓘ **Coniati qui:** `亜人` → **una specie affine all'uomo** (`:11706`), `ジュア祭`
→ **la festa di Jure** (`:11758`), `音属性` → **l'attributo suono** (`:11810`,
sulla riga delle rese di `action.hsp` per gli altri attributi).

⚠️ **Niente lineetta lunga.** In `:11979` la incisiva chiedeva un trattino, ma
`—` in CP932 e' un carattere a **doppia larghezza** e `guardie` lo boccia come i
proibiti. Reso con le virgole.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :11602 <Xabi> il re di Palmia
    (11602, 'Wise king of Palmia. He is a benevolent ruler with a strong sense of duty to his people, but he tends to be more cautious than necessary about choices that might endanger his own people. '):
        "Il saggio re di Palmia. Ha a cuore il suo popolo e governa con giustizia, ma proprio per questo, davanti a una scelta che rischi di esporre i suoi al pericolo, tende a essere prudente più del necessario. ",

    # ---------------------------------------------------------- :11615 l'orco
    (11615, 'At one time, these were a beautiful pale-skinned tribe of people similar to the Elea. It is said that their current appearance is due to being corrupted by wicked thoughts.'):
        "Un tempo erano una stirpe dalla pelle bianca e dall'aspetto bello, simile a quello degli Elea. Si dice che una presenza malvagia li abbia corrotti e ridotti come sono adesso.",

    # ---------------------------------------------------------- :11628 l'uomo lucertola
    (11628, 'A dragonborn warrior with hard scaly skin. They have the intelligence to handle weapons and armour and have developed their own culture, but are belligerent and do not interact much with other races. '):
        "Un guerriero uomo lucertola dalla pelle coperta di scaglie dure. Ha l'intelligenza per maneggiare armi e armature e si è costruito una cultura sua, ma è bellicoso e con le altre stirpi non ha molti scambi. ",

    # ---------------------------------------------------------- :11641 il minotauro
    (11641, 'A bullfighter with tremendous muscle and strength. He has turned many adventurers into ground meat by using his physical strength to wield the prey in his hands. '):
        "Un uomo toro che vanta muscoli e vigore spaventosi. Facendo parlare quel fisico di cui va fiero, con l'arma che si ritrova in mano ha ridotto a carne trita più di un avventuriero. ",

    # ---------------------------------------------------------- :11654 il minotauro mago
    (11654, 'Despite being a cow-head, he studied hard and learnt simple magic, including firebolt. His curse word seems to be jealousy of smart adventurers. '):
        "Con una testa da bue si è messo a studiare con tutte le forze e ha imparato qualche magia semplice, a cominciare dalla saetta di fuoco. Le parolacce che gli escono pare siano invidia verso gli avventurieri intelligenti. ",

    # ---------------------------------------------------------- :11667 il minotauro pugile
    (11667, 'A fighter who has reached the point where he can fight without weapons, using only his knob. However, he is uncomfortable without his favourite axe, which he carries with him at all times. '):
        "Un lottatore arrivato al punto di sapersi battere con i soli pugni, senza armi. Solo che senza l'ascia a cui è affezionato non sta tranquillo, e alla fine se la porta sempre dietro. ",

    # ---------------------------------------------------------- :11680 il minotauro re
    (11680, 'A bullfighter who boasts tremendous muscle and physical strength. Trained as warriors, the freely wielded blunt weapons of the minotaurs crush their enemies with a roar. '):
        "Un guerriero uomo toro che vanta muscoli e vigore spaventosi. La mazza che un minotauro addestrato come guerriero rigira a piacimento fa a pezzi il nemico con un boato. ",

    # ---------------------------------------------------------- :11693 <Ungaga> il re dei minotauri
    (11693, 'King who unites the savage minotaurs. With his mighty physique and fearsome destructive axe, he utterly destroys the bodies and will to fight of his enemies. He plans to invade the royal capital, but is lost in his own lair and unable to get out.'):
        "Il re che tiene insieme i minotauri selvaggi. Con quel fisico possente e con l'ascia dalla potenza distruttiva spaventosa annienta il corpo del nemico e la sua voglia di combattere. Sta preparando l'assalto alla capitale, ma nella propria tana si è perso e non riesce a uscire.",

    # ---------------------------------------------------------- :11706 il troll
    (11706, 'A type of subhuman with a gigantic physique. They are famous for their regenerative powers and can quickly heal small wounds. The secret is said to lie in its special blood.'):
        "Una specie affine all'uomo, dal corpo gigantesco. È famoso per la capacità di rigenerarsi: le ferite piccole gli si rimarginano subito. Il segreto, dicono, sta in un sangue speciale.",

    # ---------------------------------------------------------- :11719 il guerriero di Elea
    (11719, 'An Elea who lives within ruins of Nefia. Because they were persecuted and exiled from their villages, they bear a grudge against those who enter the ruins. Their armaments are a natural consequence of having to live within the ruins.'):
        "Un Elea che vive nelle Nefia. Perseguitati e cacciati dalle città, portano rancore a chi arriva da fuori. Le armi, a quanto pare, se le porta per forza, perché nelle Nefia bisogna pur viverci.",

    # ---------------------------------------------------------- :11732 il mago di Elea
    (11732, 'Elea folks living inside Nefia. Persecuted and forced out of their town, they have no choice but to live in Nefia, where they can shelter from the wind and rain. They are very wary and will attack anyone unfamiliar to them, even if they are Elea.'):
        "Un Elea che vive nelle Nefia. Perseguitati e cacciati dalle città, non hanno altra scelta che vivere nelle Nefia, dove almeno ci si ripara dal vento e dalla pioggia. Sono molto diffidenti, e chi non conoscono lo attaccano anche se è un Elea.",

    # ---------------------------------------------------------- :11745 l'asura
    (11745, 'A belligerent demon that bears the shards of an ancient fire god. It holds a weapon in each of its many hands, and madly chops up its opponents. Sometimes concentrates too much on his hands, leaving his feet unattended.'):
        "Un mostro bellicoso in cui alberga il frammento dell'antico dio del fuoco. Tiene un'arma in ciascuna delle sue molte mani e fa a pezzi chi gli si oppone come un pazzo. A volte concentra troppo l'attenzione sulle mani e si dimentica dei piedi.",

    # ---------------------------------------------------------- :11758 il Mitra
    (11758, 'A demon that inhabits a piece of the ancient sun god. Some historians claim that the rituals of this sun god influenced the present day Jua festival. Why it is green, though, is said to be unknown to those historians.'):
        "Un mostro in cui alberga il frammento dell'antico dio del sole. C'è chi, fra gli storici, sostiene che il culto di questo dio del sole abbia influenzato la festa di Jure di oggi. Perché però sia verde, pare che nemmeno quegli storici lo sappiano.",

    # ---------------------------------------------------------- :11771 il varuna
    (11771, 'A demon that bears the fragments of an ancient god of sky and order. The ability to govern the waters has long since been lost, and this variant swivels its beautiful arms only to physically annihilate the enemy in front of it. '):
        "Un mostro in cui albergano i frammenti dell'antico dio del cielo e dell'ordine. Il potere di governare le acque l'ha perso da un pezzo, e questa creatura deforme fa roteare le sue belle braccia soltanto per annientare fisicamente il nemico che ha davanti. ",

    # ---------------------------------------------------------- :11784 il mago
    (11784, "A intellectual who communicates with spirits and lives through the circle of the gods' power. He is often at odds with scientists who emphasise the accumulation of rigorous basic facts. "):
        "Un sapiente che comunica con gli spiriti e vive dipanando il ciclo eterno della forza delle divinità. Con gli scienziati, che tengono all'accumulo di fatti solidi e di base, si trova spesso in contrasto. ",

    # ---------------------------------------------------------- :11797 il guerriero
    (11797, 'They are those who train their bodies and live with a vitality that ordinary people cannot resist. As they specialise in combat and mainly show their true value in times of war, they are often employed as soldiers, instructors or in hard work in times of peace. '):
        "Gente che tempra il proprio corpo e vive con un vigore a cui una persona comune non può opporsi. Sono specializzati nel combattimento e danno il meglio soprattutto in tempo di guerra, e così in tempo di pace fanno spesso i soldati, gli istruttori o i lavori di fatica. ",

    # ---------------------------------------------------------- :11810 la mandragora
    (11810, 'A monster, resembling a vegetable, that grows by feeding on magical energy within the soil. Their flesh contains a large amount of magical energy, and is capable of stimulating the magical powers of those who consume it. Be wary of its terrifying screams, which are magic with the attribute of sound.'):
        "Un mostro simile a un ortaggio, cresciuto nutrendosi della forza magica della terra. La sua carne, che di forza magica ne contiene parecchia, stimola un poco quella dell'avventuriero. Attenzione all'urlo, che è anche una magia dell'attributo suono.",

    # ---------------------------------------------------------- :11823 lo scarabeo
    (11823, 'Insects that are the dream of every child in the city. Wild beetles died out a long time ago due to overhunting, but bred individuals have escaped and are now in the wild. They survive over winter and have a long lifespan.'):
        "L'insetto che tutti i bambini di città sognano. Quelli selvatici si sono estinti tanto tempo fa per la caccia sfrenata, ma certi esemplari selezionati sono scappati e sono tornati allo stato brado. Passa l'inverno e vive a lungo.",

    # ---------------------------------------------------------- :11836 l'orco guerriero
    (11836, "Orcs are a tribe of particularly brave and warlike people. Orcs are very skillful with their hands and show interest in machinery, but they don't try to make anything other than weapons."):
        "Fra gli orchi, quelli particolarmente coraggiosi e bellicosi. Gli orchi hanno le mani buone e si interessano anche alle macchine, ma di costruire qualcosa che non porti distruzione, come le armi, non ne vogliono sapere.",

    # ---------------------------------------------------------- :11849 <Goda> il capitano degli orchi
    (11849, 'A brave warrior of the Orc tribe who has fought in many battles. Orcs are not stupid, but they are insensitive and self-indulgent, so it is very rare for them to become captains and try to unite their troops. '):
        "Un valoroso della stirpe degli orchi, con molte battaglie alle spalle. Gli orchi non sono affatto stupidi, ma sono duri di sentimenti e fanno di testa loro, e perciò è rarissimo che uno diventi capitano e provi a tenere insieme un reparto. ",

    # ---------------------------------------------------------- :11862 lo zombi
    (11862, "A re-animated corpse brought to life by a reaction between mana left in its body and the mana in its surroundings. It's rare to find one that retains any memories of its life."):
        "Il mana rimasto nel corpo sepolto reagisce alla forza magica che ha intorno, e per assorbirla muove il cadavere. Di rado se ne trova uno che si porti dietro la coscienza di quando era vivo.",

    # ---------------------------------------------------------- :11875 il pipistrello
    (11875, 'Wild animals often seen in the open. Dodges and dodges with quick movements. They use ultrasound to understand their surroundings, so they are not blind. They are inconvenienced by the inaccurate vision.'):
        "Un animale selvatico che si incontra spesso all'aperto. Con movimenti rapidi scarta e schiva. Grazie agli ultrasuoni sa che cosa gli sta intorno, e per questo non resta mai accecato. Gli dà fastidio la fama di essere uno che tradisce.",

    # ---------------------------------------------------------- :11888 il pipistrello vampiro
    (11888, 'A generic name for a species of bat that sucks blood. However, as their stomachs do not swell much, blood sucking is said to be only a snack. They swarm over their prey in groups and suck all the blood.'):
        "Il nome che raccoglie le specie di pipistrello che succhiano il sangue. La pancia però non gli si riempie granché, e pare che il sangue sia poco più di uno spuntino. Si ammassano in gruppo sulla preda e le succhiano tutto il sangue.",

    # ---------------------------------------------------------- :11901 il pipistrello drago
    (11901, 'A highly skilled bat with dragon-like wings. Some are said to be fascinated by its swiftness and try to ride it somehow. They have a habit of trying to compete with wyverns when they encounter them.'):
        "Un pipistrello con le ali da drago e una buona capacità di combattere. C'è chi, incantato da quella rapidità, cerca in qualche modo di montarci sopra. Quando incontra una viverna ha l'abitudine di volersi misurare con lei.",

    # ---------------------------------------------------------- :11914 l'ent di fuoco
    (11914, 'Ent with beautiful flame flowers. Although it moves rather slowly, it boasts high vitality and the strikes it delivers with its huge branches are very powerful. '):
        "Un Ent che ha aperto bellissimi fiori di fiamma. Si muove piuttosto lento, ma vanta una gran forza vitale, e il colpo che sferra con quei rami enormi è violentissimo. ",

    # ---------------------------------------------------------- :11927 l'ent di ghiaccio
    (11927, 'Ent with beautiful ice flowers. The trunks and branches, surrounded by cold air, shine like crystals and are popular among the nobility as ornamental plants. '):
        "Un Ent che ha aperto bellissimi fiori di ghiaccio. Il tronco e i rami, avvolti nel gelo, brillano come cristallo, e fra i nobili sono molto ricercati come ornamento. ",

    # ---------------------------------------------------------- :11940 il lich
    (11940, 'The result of those who were mages in life and tried to cling to this world even after death. Those who have no reason left become avengers who bring harm to others. '):
        "Quel che resta di chi in vita era un mago e, anche da morto, ha voluto restare aggrappato a questo mondo. Chi non ha più un briciolo di ragione diventa un nemico che porta danno agli uomini. ",

    # ---------------------------------------------------------- :11953 il lich maestro
    (11953, 'Lich, who has lost his physical body and has been transformed into a spirit body. The memories of the past, which sought eternity in the long passage of time, have already worn away, and he has become a monster who tries to reduce the living in his path to the same existence. '):
        "Un lich che ha perso il corpo e si è fatto via via spirito. Il ricordo di quando, nel lungo scorrere del tempo, cercava l'eternità si è ormai consumato, e si è ridotto a un mostro che vuole portare alla propria condizione i vivi che incontra. ",

    # ---------------------------------------------------------- :11966 il lich minore
    (11966, 'Lich, whose physical body collapsed and he became a half-spirit. As a result of his wandering through the ages, he became an evil spirit that tries to kill the living with only his instincts in exchange for his amazing magical powers. '):
        "Un lich il cui corpo si è sgretolato e che è diventato mezzo spirito. A furia di vagare per età intere è diventato uno spirito maligno che, in cambio di una forza magica prodigiosa, cerca di uccidere i vivi per solo istinto. ",

    # ---------------------------------------------------------- :11979 il boia
    (11979, 'A monster of the underworld that is connected to death. It has values that are incompatible with those of the living, which state that to live is a sin, and unilaterally executes sentences with a terrible curse that forcibly kills its opponents. '):
        "Un mostro dell'oltretomba che porta alla morte. Ha valori che con quelli dei vivi non stanno insieme, e cioè che vivere sia una colpa, ed esegue la sentenza da solo, con una maledizione tremenda che uccide per forza chi ha davanti. ",

    # ---------------------------------------------------------- :11992 il messo della morte
    (11992, 'A monster of the underworld that is connected to death. In order to balance the numbers of the living and the dead, they are ordered by the god of death to declare death sentences. Most of the time, the death is not the death that should have come, so it can be pretended that it never happened if the victim survives.'):
        "Un mostro dell'oltretomba che porta alla morte. Per far tornare i conti fra il numero dei vivi e quello dei morti, pronunciano la condanna per ordine della Morte. Quasi sempre non è la morte che sarebbe davvero toccata, e quindi, se lo si respinge, la cosa si può cancellare.",

    # ---------------------------------------------------------- :12005 il segugio
    (12005, 'Dogs specialize in hunting prey. Because dogs are territorial, they will not settle in areas where there are dogs on a stronger level than themselves.'):
        "Un cane specializzato nel dare la caccia alla preda. I cani hanno un forte senso del territorio, e non si stabiliscono dove c'è un cane di livello più forte del loro.",

    # ---------------------------------------------------------- :12018 il segugio di fuoco
    (12018, 'A dog that unleashes a breath of flame. The flames it releases can roast an Indian elephant whole in an instant. Only their heads and fur are resistant to heat; meat can be roasted normally.'):
        "Un cane che manda un soffio di fiamma. Le fiamme che sprigiona arrostiscono un elefante indiano intero in un istante. A resistere al calore però sono soltanto la testa e la pelliccia: la carne si cuoce come quella di tutti.",

    # ---------------------------------------------------------- :12031 il segugio di ghiaccio
    (12031, 'A dog that releases breath that freezes anything it is girdled with. He is so rabid and annoying that he invades Indian elephant territory and freezes them at random. But he is instantly popular in summer.'):
        "Un cane che manda un soffio capace di congelare quello che investe. È talmente rabbioso e molesto che entra nel territorio degli elefanti indiani e li mette sotto ghiaccio a casaccio. D'estate, però, di colpo diventa popolare.",

    # ---------------------------------------------------------- :12044 il segugio del fulmine
    (12044, 'Dogs that release lightning-breath tinged breath. Famous for electrocuting Indian elephants bathing in water. No matter how much electricity-resistant equipment you have, you will be paralysed for a short while if you are exposed to the breath.'):
        "Un cane che manda un soffio carico di fulmini. È famoso per fulminare gli elefanti indiani mentre fanno il bagno. Per quanto tu abbia un equipaggiamento che resiste all'elettricità, se ti prendi il soffio in pieno resti intorpidito per un poco.",

    # ---------------------------------------------------------- :12057 il segugio dell'oscurità
    (12057, 'A dog that releases breath that brings darkness. It is the natural enemy of many wizards, as it cannot perform many of its magic if it cannot see its target. It has a dark personality and is said to seduce poor Indian elephants and bring them down to the dark side.'):
        "Un cane che manda un soffio che porta il buio. Se non vede il bersaglio un mago non può lanciare quasi nessuna magia, e per questo è il nemico naturale di tanti maghi. Ha un carattere oscuro anche lui, e si dice che tenti perfino i poveri elefanti indiani per farli cadere nel lato oscuro.",

    # ---------------------------------------------------------- :12070 il segugio mentale
    (12070, 'Dogs that release breath containing hallucinogenic ingredients. The breath can cause even an Indian elephant to fall into a stupor if it inhales just a little. They like to watch their confused prey become flustered.'):
        "Un cane che manda un soffio pieno di sostanze che danno le allucinazioni. Basta respirarne un poco perché anche un elefante indiano stramazzi. Pare che gli piaccia guardare la preda confusa che barcolla.",

    # ---------------------------------------------------------- :12083 il segugio dei nervi
    (12083, "A dog that releases a breath that paralyses the nerves. It will bite its paralysed, immobilised prey to its heart's content. Even an Indian elephant cannot escape a stroke if it inhales the breath."):
        "Un cane che manda un soffio che paralizza i nervi. La sua tattica è addentare a sazietà la preda paralizzata e immobile. Anche un elefante indiano, se respira quel soffio, non scampa allo svenimento.",

    # ---------------------------------------------------------- :12096 il segugio del veleno
    (12096, 'The dog releases a highly poisonous breath. The poison is not fatal, but it certainly eats away at their lives over time. Records indicate that many Indian elephants have lost their lives to this poison.'):
        "Un cane che manda un soffio velenosissimo. Il veleno non è fatale, ma con il tempo consuma la vita di sicuro. Secondo le cronache, tanti elefanti indiani hanno perso la vita per questo veleno.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-024.jsonl'
DA, A = 11601, 12100
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
