# -*- coding: utf-8 -*-
"""103a - Lotto 9 di `db_card.hsp`: le carte fra la riga 4101 e la 4600 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_103-rese-card-07.py` per le decisioni della giornata.

⭐ **Gia' deciso altrove:** `ルルウィ` → **Lulwy**, `ノーランド` → **Norland**
(`db_race.hsp:1120`), `メシェーラ` → **Meshera**, `カラヴィカ` → **Karavika**
(`db_card.hsp:6107`), `キューピッド` → **il cupido** (`:9708`),
`メルカサラマンダー` → **l'ambystoma** (`:7277`), `飛び蛙` → **la rana
volante** (`:11281`), `妖精` → **la fata**, `ゴボウ` → **la bardana**
(`db_creature.hsp:60467`), `竜人` → **l'uomo lucertola** (`db_race.hsp:911`).

⚠️⚠️⚠️ **`:4125` NON HA UN INGLESE SUO: monte gli ha messo quello di `:4112`.**
E' il difetto piu' netto trovato finora in questo file, e si dimostra in due
righe. Il giapponese di `:4125` parla della **mandragora zappatrice**, che
picchia le cosce altrui con una bardana sbucciata; l'inglese di `:4125` parla
del **cavallo di cetriolo**, che d'estate arriva dall'oltretomba con un'anima
in groppa. Peggio: l'inglese di `:4125` e' la resa **completa** del giapponese
di `:4112`, chiusa dalla frase sul sudore che l'inglese di `:4112` **non ha**.
Cioe' monte ha tradotto due volte la stessa carta, la seconda meglio della
prima, e l'ha scritta nel blocco sbagliato.

⭐ Conseguenza pratica: `:4125` si traduce **solo** dal giapponese, e chi
guardasse l'inglese scriverebbe due volte la stessa carta. Chi traducesse
`:4112` dall'inglese perderebbe invece l'ultima frase. Il conto giusto e' che
in questo lotto ci sono **due** carte diverse, non una ripetuta.

⚠️ **`:4242` l'inglese sbaglia il carattere:** 呑気 vuol dire *tranquillo, che
se la prende comoda*; l'inglese legge il primo carattere (bere) e scrive «his
personality is a bit of a drinker».

⚠️ **`:4138`, `:4151` e `:4554` scivolano in prima persona nell'inglese**
(«The only thing I can say», «I feel that», «I move from staircase to
staircase»): il giapponese e' impersonale in tutt'e tre.

⚠️ **`:4580`: シズルコード e' il codice di Ssil.** Il giapponese chiama la
strega シズル, l'inglese di monte `<Ssil>` e il progetto ha reso il nome della
carta «<Ssil> la strega del divieto infranto»: il libro porta quel nome li',
non una traslitterazione nuova.

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`. In CP932 il resto diventa doppia larghezza.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :4112 il cavallo di cetriolo
    # ⚠️ L'inglese di monte lascia cadere l'ultima frase (il sudore): sta
    #    nell'inglese di :4125, dove non c'entra niente. Vedi la testa.
    (4112, 'A monster with an ego in a cucumber. It comes from the underworld with a ghost on its back in the summer. It runs with its short legs moving hard.'):
        "Un mostro nato quando in un cetriolo è germogliata una coscienza. Si dice che d'estate arrivi dall'oltretomba portando in groppa un'anima. Corre agitando con accanimento le zampe corte, che non hanno articolazioni. E se corre a lungo, il sudore gli porta via l'acqua un po' alla volta.",

    # ---------------------------------------------------------- :4125 la mandragora zappatrice
    # ⚠️⚠️⚠️ L'inglese qui e' quello del cavallo di cetriolo: si traduce dal
    #     giapponese e basta. Vedi la testa del file.
    (4125, "A monster with its soul in a cucumber. It is said that they come from the underworld in the summer with ghosts. They run hard on their short arthritic legs. If they keep running they''ll lose more and more water through sweat."):
        "Un mostro dal senso oscuro, che ha l'abitudine di picchiare le creature all'altezza della coscia con una bardana sbucciata. C'è chi dice che sia un rito per vendicare le bardane e chi dice che sia una provocazione, come a dire: le tue gambe sembrano due bardane. Come stiano davvero le cose, non si sa.",

    # ---------------------------------------------------------- :4138 il guscio vuoto della memoria
    (4138, 'The end of a person who has lost all of his or her personal memories and those of others. Who they were no one in this world knows anymore. The only thing I can say is that his thinking ability is the same as that of a newborn baby.'):
        "È il punto d'arrivo di chi ha perso tutto: la memoria propria e la memoria che gli altri avevano di lui. Chi fosse, ormai in questo mondo non lo sa più nessuno. L'unica consolazione è che la sua testa non ragiona più di quella di un neonato.",

    # ---------------------------------------------------------- :4151 il fedele dell'oblio
    (4151, 'People who have become obsessed with the allure of being able to erase unpleasant memories of themselves and others. He said that if he feels even the slightest bit of pain or annoyance he will turn it off. I feel that there is nothing but ruin awaiting them in such a way of life.'):
        "Gente rimasta invischiata nel fascino di poter cancellare i ricordi sgradevoli, i propri e quelli altrui. Pare che basti un filo di sofferenza o di fastidio perché lo cancellino. A vivere così, viene da pensare che non ci sia in serbo altro che la rovina.",

    # ---------------------------------------------------------- :4164 il leone senza volto
    (4164, 'Unable to contain the overflowing madness he constantly scratches his face shakes his hair and moans like a beast. He had no human intelligence left and was even described by some affluent people as being like a lion.'):
        "Non riesce a trattenere la follia che gli trabocca fuori: si gratta la faccia fino a scorticarsela, si scompiglia i capelli e geme come una bestia. Di intelligenza umana non gliene resta, e un certo riccone arrivò a dire che sembrava un leone.",

    # ---------------------------------------------------------- :4177 <Maile> la sacerdotessa fantoccio
    (4177, 'A dying monster possessed a woman who was nearby. They are erasing memories and hijacking personalities. She is on a mission to erase all memories of this world and to do so she is plotting to regain her lost power.'):
        "È una belva magica in fin di vita che si è impossessata, senza chiedere permesso, di una signora che passava di lì. Le ha cancellato la memoria e le ha preso il posto. La sua missione è cancellare tutti i ricordi di questo mondo, e per riuscirci trama nell'ombra per riprendersi la forza che ha perduto.",

    # ---------------------------------------------------------- :4190 il dio ibis
    (4190, 'A bird-man wearing blue armor. It seems that the armor contains the power of the bird deity. Approaching at high speed it unleashes a destructive beam of light slashing through the enemy with its sword as it soars. Because of its ferocity it has been called a god in some parts of the world.'):
        "Un uomo uccello che porta un'armatura azzurra. Nell'armatura, a quanto pare, abita la forza del dio degli uccelli. Si avvicina a gran velocità, scaglia una luce che distrugge e squarcia il nemico con la spada come se danzasse. Per quanto è fiero, in certe zone lo trattano alla pari di un dio.",

    # ---------------------------------------------------------- :4203 l'alkonost
    (4203, "A half-human half-bird demon that dwells in the sky. They''re emotionally unstable crying and singing horrible songs when they don't want to and inflicting eternal punishment on souls damned to hell to vent. They think they can sing better than Karavika."):
        "Un mostro metà uomo e metà uccello che abita nei cieli. Ha l'umore instabile: se qualcosa non le va, piange e intanto canta canzoni spaventose, e per sfogarsi infligge alle anime cadute all'inferno un castigo eterno. È convinta di cantare meglio di Karavika.",

    # ---------------------------------------------------------- :4216 l'ala nera
    (4216, "A bird-man brawler wearing black armor that covers even his wings. He seems to have a lot of confidence in his fists and he doesn't mind striking out at opponents stronger than him. He wants more solid armor that won't be destroyed in battle."):
        "Un pugile uomo uccello, con addosso un'armatura nera che gli copre perfino le ali. Nei propri pugni ha una fiducia smisurata, e mena le mani senza battere ciglio anche contro chi è più forte di lui. Vorrebbe un'armatura più solida, di quelle che in battaglia non si sfasciano.",

    # ---------------------------------------------------------- :4229 la mayu sibayu
    (4229, 'The reincarnation of the soul of a girl who died at an early age without knowing love. They lure their prey and attack them when they are caught off guard. They like to crush the head and suck the brain tissue and they are quite aggressive.'):
        "È l'anima di una ragazza morta da piccola senza aver conosciuto l'amore, tornata al mondo in un altro corpo. Seduce la preda e la colpisce appena abbassa la guardia. Le piace fracassare la testa e succhiarne il midollo: piuttosto aggressiva, insomma.",

    # ---------------------------------------------------------- :4242 <Belphat> lo spadaccino cosmico
    # ⚠️ 呑気 = tranquillo, non «a bit of a drinker».
    (4242, 'A swordsman who travels the various stars while eating and peddling swords. In addition to his normal arms he fights with two tentacles that extend from his shoulders. He is a warrior at heart but his personality is a bit of a drinker. Stomach acid is special and burps with a hallucinogenic component.'):
        "Uno spadaccino che gira di stella in stella mangiando dove capita e vendendo la lama a chi paga. Oltre alle braccia normali combatte con due tentacoli che gli escono dalle spalle. È di stirpe guerriera fino al midollo, ma di carattere se la prende con calma. Ha i succhi gastrici particolari, e i rutti gli vengono con dentro una sostanza che dà allucinazioni.",

    # ---------------------------------------------------------- :4255 il guerriero draconico dell'onda
    (4255, "A dragon warrior who has acquired the power to manipulate wave motion. He boasts tremendous fighting power but even he doesn't know how he got this power or what the waves are in the first place."):
        "Un guerriero uomo lucertola che ha imparato a manovrare le onde. Vanta una potenza di combattimento spaventosa, ma come gli sia venuta quella forza, e soprattutto onde di che cosa siano, non l'ha capito bene nemmeno lui.",

    # ---------------------------------------------------------- :4268 la lucertola della bufera
    (4268, "When their body temperature doesn't rise their tension doesn't rise so they absorb the heat around them turn it into cold air and release it. If you collect more than one of them it's enough to cause a blizzard in a hot area."):
        "Se non le sale la temperatura del corpo non le sale nemmeno l'umore, e allora assorbe il calore che ha intorno, lo trasforma in aria gelida e la butta fuori. Se se ne mettono insieme parecchie, arrivano a scatenare una tormenta perfino in una regione calda.",

    # ---------------------------------------------------------- :4281 il dragonewt spadone
    (4281, 'A powerful dragon man wielding a greatsword. He likes the sturdy weight of the greatsword. He is confident in his skills and has no reservations when it comes to fighting dragons and dragon hunters.'):
        "Un uomo lucertola pieno di forza, che maneggia uno spadone. Gli piace il peso pieno che ha lo spadone. Del proprio braccio è sicuro, e non fa distinzioni: se la prende con i draghi come con i cacciatori di draghi.",

    # ---------------------------------------------------------- :4294 la lucertola assassina
    (4294, "Assassin of the Dragon Man. They have formed an assassin's guild for dragon people only and they go around assassinating those who pose a threat to the clan. Their tails are in the way and they can't blend in with the crowd so they prefer clothes with stealthy abilities."):
        "L'assassino degli uomini lucertola. Hanno messo su una gilda di assassini riservata alla loro gente, e vanno in giro a togliere di mezzo chi minaccia la stirpe. La coda è ingombrante e non permette di confondersi nella folla, e per questo portano volentieri abiti che aiutano a non farsi vedere.",

    # ---------------------------------------------------------- :4307 il drago velenoso dalle scaglie nere
    (4307, "He longed to breathe fire and cultivated so much that the scales on his entire body burned with heat in an attempt to acquire the power of the flame. In the end his personality was warped in despair that it didn't work and the only thing that resulted in him being able to throw up was poison."):
        "Sognava di sputare fuoco, e per impadronirsi della forza della fiamma si sottopose a un tirocinio tale che il calore gli bruciacchiò le scaglie su tutto il corpo. Alla fine non ci riuscì, la disperazione gli storse il carattere, e l'unica cosa che ha finito per saper sputare è il veleno.",

    # ---------------------------------------------------------- :4320 il mago lucertola
    (4320, 'The dragon man has worked hard to acquire magic. However since his body is strong to begin with his physical attacks are more powerful than his magical attacks. After struggling with that for a long time he settled on using auxiliary magic.'):
        "Un uomo lucertola che a furia di impegnarsi si è impadronito della magia. Solo che il corpo ce l'ha robusto in partenza, e quindi gli attacchi fisici gli riescono meglio di quelli magici. Dopo essersi tormentato a lungo sulla faccenda, si è accomodato sulle magie di sostegno.",

    # ---------------------------------------------------------- :4333 la fata splendente
    (4333, 'Legend has it that when a fairy tribe was threatened she was born from a spring clothed in a robe of light. However due to the rise of other races they have been born sporadically over the past few hundred years. They are suffering from diminishing numbers.'):
        "La fata leggendaria che, quando sul popolo delle fate incombe il pericolo, nasce dalla sorgente avvolta in una veste di luce. Solo che, con le altre stirpi che avanzano, negli ultimi secoli continua a nascerne una ogni tanto senza mai smettere. Pare che a loro dispiaccia parecchio essere diventate meno rare.",

    # ---------------------------------------------------------- :4346 la fata Gorath
    (4346, 'It burns red and although it looks no different from a normal fairy it has more than 6000 times the mass of a normal fairy. It attacks with great force so try your best to avoid it.'):
        "A parte il fatto che brucia di rosso, all'aspetto non è tanto diversa da una fata comune; solo che ha una massa oltre seimila volte quella di una fata normale. Ti si butta addosso con una violenza tremenda, quindi mettici tutto l'impegno che hai per schivarla.",

    # ---------------------------------------------------------- :4359 la peri
    (4359, 'A fairy born of the fire element. To prove it it will use fire magic. Men are said to be dignified and women are said to be beautiful. They are almost the same size as humans and it is not uncommon for them to marry humans.'):
        "Una fata nata dall'elemento del fuoco. La prova è che sa usare la magia del fuoco. I maschi passano per solenni, le femmine per bellissime. Sono grandi pressappoco come una persona, e non è raro che sposino un umano.",

    # ---------------------------------------------------------- :4372 la fata gigante
    (4372, "A fairy with a congenital disease that prevented its growth inhibitors from functioning properly. They have grown to the size of a human and have had to leave the fairy home. They can''t use magic very well so they fight with human bows."):
        "Una fata a cui, per una malattia di nascita, il fattore che frena la crescita non ha funzionato come doveva. È cresciuta fino alla taglia di una persona, e si è vista costretta ad andarsene dal villaggio delle fate. La magia le riesce male, e perciò combatte con archi e simili, di quelli fatti per gli uomini.",

    # ---------------------------------------------------------- :4385 la pixie
    (4385, 'It is said to be the reincarnation of the soul of an unbaptized and dead child. They love to play pranks on humans but they are loyal and hardworking. They dance in groups while basking in the moonlight.'):
        "Si dice che sia l'anima di un bambino morto senza battesimo, tornata al mondo in un altro corpo. Adora fare scherzi agli uomini, ma è di parola e sul lavoro ci si mette d'impegno. Danza in gruppo sotto la luce della luna.",

    # ---------------------------------------------------------- :4398 <Renai> la calamità repressa
    (4398, "She has miraculously regained her personality but she is already physically out of her element. She is merely recreating what she looked like when she was human through bodily control. External neural adjustments by her brother somewhat suppressed Meshera's influence."):
        "Per miracolo si è ripresa la propria persona, ma il corpo ormai non è più di questo mondo: la figura che aveva da umana la ricostruisce soltanto controllando la carne. L'influenza di Meshera riesce a tenerla a bada alla meglio, grazie alla regolazione nervosa che il fratello le fa dall'esterno.",

    # ---------------------------------------------------------- :4411 l'angelo caduto
    (4411, "He has the ability to be above his rank but is unable to get promoted due to power harassment from his boss. They are currently on strike for better working conditions. Recently he's been thinking about accepting scouts from the Demon Squad."):
        "Ha una forza superiore al suo grado, ma il capo lo vessa e la promozione non arriva mai. Al momento è in sciopero per ottenere condizioni di lavoro migliori. Negli ultimi tempi va pensando che tanto vale accettare l'offerta che gli è arrivata dalla parte dei demoni.",

    # ---------------------------------------------------------- :4424 l'ispettore dell'amore
    (4424, 'The role is to supervise Cupid and the others to make sure that they are doing their best to achieve love. In the past they used to be able to do it with ease but in recent years they have become more strict because of the troubles that have come to the surface.'):
        "Il suo compito è sorvegliare e ispezionare i cupidi, per controllare che facciano nascere gli amori come si deve. Un tempo la cosa si faceva alla buona, ma negli ultimi anni sono venuti a galla dei guai e la mano si è fatta più dura.",

    # ---------------------------------------------------------- :4437 l'angelo apprendista
    (4437, "He aims to be a full-fledged angel. Only the elite who are thrown into a competitive society and win out can become true angels but they don't know that there will be pain hardship extreme hardship and even deathly hardship ahead."):
        "Punta a diventare un angelo fatto e finito. Lo hanno buttato in una società di concorrenza, e angelo vero diventa solo chi la spunta e arriva in cima; ma quello che lo aspetta dopo non lo sa ancora: dolori, pene, dolori grossi e pene da morire.",

    # ---------------------------------------------------------- :4450 il Seiashin
    (4450, 'God of frogs. Although he is not a great fighter he has been called a genius at predicting natural disasters and has been revered until recently. He is so anxious that when he is in danger he goes crazy and goes on a rampage.'):
        "Il dio delle rane. Come forza di combattimento non vale granché, ma lo chiamavano il genio che prevede le calamità naturali e fino a poco tempo fa lo veneravano. È così apprensivo che, appena si sente il pericolo addosso, dà di matto e comincia a devastare tutto.",

    # ---------------------------------------------------------- :4463 la salamandra d'oriente
    (4463, 'It specializes in using heat to attack but when it is not in combat its body becomes feverish. Normally they radiate heat without incident and when they sleep they return to their underwater nests for cooling. It is often misunderstood that they live in lava because of their appearance.'):
        "È bravissima ad attaccare sfruttando il calore, ma quando non combatte il calore le resta chiuso dentro il corpo. Di solito lo sfoga addosso a chiunque le capiti a tiro, e per dormire torna nella tana sott'acqua a raffreddarsi. Per via dell'aspetto, spesso si crede per sbaglio che viva dentro la lava.",

    # ---------------------------------------------------------- :4476 il re del pantano
    (4476, "A giant creature called the King of the Swamp. Its true identity is the shape of the Melka Salamander that caused the ancestral return. It doesn't suit the languid atmosphere but it has a lot of power. It is said that it is quite good when deep-fried without sauce and sometimes it is sold as a delicacy."):
        "Una creatura enorme che chiamano il re del pantano. In verità è un ambystoma che è tornato indietro ai suoi antenati. Con quell'aria da smidollato non si direbbe, ma di forza ne ha da vendere. Fritto senza pastella pare che non sia affatto male, e capita che lo vendano come leccornia.",

    # ---------------------------------------------------------- :4489 il girino musicale
    (4489, "The tadpole is said to manipulate sound by magic. It vibrates the air violently converting its force into an attack. It floats by magic but doesn't become a flying frog when it grows up."):
        "Un girino che, a quanto si dice, manovra il suono con il potere magico. Fa vibrare l'aria con violenza e trasforma l'urto in un attacco. Se ne sta a mezz'aria grazie alla magia, ma crescendo non diventa una rana volante.",

    # ---------------------------------------------------------- :4502 la rana dai dardi velenosi
    (4502, "A rare frog that hunts using a poisonous liquid secreted by its own body. They don't like the flashy color of their bodies but apparently it can't be helped because the process of making the poison turns out to be this color."):
        "Una rana rara, che caccia usando il liquido velenoso che il suo corpo secerne. Quel colore vistoso non le piace per niente, ma pare non ci sia niente da fare: viene così a forza di fabbricare il veleno.",

    # ---------------------------------------------------------- :4515 <Aribel> la monella
    (4515, "She has a mother of Elea and a father of Norland. She may have inherited the talents of her parents but she is also proud of her skill at a young age. Aribel has her own rules and mindset called the Seven Articles which she refers to as her father's teachings."):
        "Ha la madre Elea e il padre di Norland. Sarà che ha preso il talento da tutti e due, ma già in giovane età vanta un braccio da far paura. Ha regole e propositi tutti suoi, i Sette Articoli di Aribel, e pare li abbia ricavati dagli insegnamenti del padre.",

    # ---------------------------------------------------------- :4528 l'arcispettro
    (4528, 'The end of the life spirit that separated from the body. It seems he was a noble wizard in the past and has strong magical powers. Particularly powerful individuals are distinguished as monarchs and are prefixed with arch.'):
        "È quel che resta di uno spirito vivente separatosi dal corpo. A quanto pare in origine era un mago di nobile stirpe, e infatti ha un forte potere magico. Gli esemplari particolarmente forti si distinguono come di grado sovrano, e ricevono il prefisso arci.",

    # ---------------------------------------------------------- :4541 il mago della legione
    (4541, 'An evil spirit called The Legion. They have a habit of attacking the living in packs and taking them in as new companions. When there is more than a certain number another group is born. The ego is fading and the distinction between oneself and other individuals is blurred.'):
        "Uno spirito maligno che chiamano la legione. Ha l'abitudine di assalire i vivi in massa e di inglobarli come nuovi compagni. Superato un certo numero, ne nasce un altro gruppo. Ha l'io sbiadito, e il confine fra sé e gli altri gli è diventato incerto.",

    # ---------------------------------------------------------- :4554 lo spirito maligno del tredicesimo gradino
    (4554, 'The thought-gathering of those who died on the stairs. I move from staircase to staircase and dive in. Their hobby is to push tired passersby down the stairs but when they have nothing to do they will usually pounce on them.'):
        "L'ammasso dei pensieri di chi è morto su una scala. Si sposta di scala in scala e ci si infila dentro. Il divertimento è spingere giù dai gradini il passante stanco, ma quando si annoia capita che aggredisca e basta.",

    # ---------------------------------------------------------- :4567 la silfide
    (4567, 'A pitiful wind spirit who was captured and trained by Lulwy of the Wind. They are not fed much and are kept lifeless but not dead. It has almost lost all sense of rationality and if there is anything it can be eaten it is eaten in a desperate attempt to survive.'):
        "Un povero spirito del vento, catturato e ammaestrato da Lulwy del vento. La tengono senza darle da mangiare a sufficienza, né viva né morta. Ha perso quasi del tutto la ragione, e se le capita davanti qualcosa di commestibile ci si avventa con la disperazione di chi vuole sopravvivere.",

    # ---------------------------------------------------------- :4580 <Ssil> la strega del divieto infranto
    (4580, 'She became an undead through mystic arts and lived for an eternity. Her book a compilation of research on abstinence is called The Ssil Code because it is as esoteric as a code. It is dangerous for a gifted wizard to read it because they will be strongly enchanted by its contents.'):
        "Con le arti segrete è diventata non morta, e da allora attraversa un tempo senza fine. Il libro in cui ha raccolto le sue ricerche sul proibito è così astruso da sembrare cifrato, e per questo lo chiamano il Codice di Ssil. È pericoloso: se lo legge un mago di talento, il contenuto lo strega senza scampo.",

    # ---------------------------------------------------------- :4593 il Melugast di serie
    (4593, 'The appearance is the same as the prototype but various parts are interchangeable. It is also possible to carry heavy weapons and electronic warfare equipment to remove the dimensional distortion unit and is also excellent as a general-purpose fighter.'):
        "All'aspetto non è diverso dal prototipo, ma i vari pezzi sono diventati intercambiabili. Si può togliere l'unità di distorsione dimensionale e caricarci al suo posto equipaggiamento per la guerra elettronica o armi pesanti, e anche come caccia per ogni impiego è ottimo.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-009.jsonl'
DA, A = 4101, 4600
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
