# -*- coding: utf-8 -*-
"""105a - Lotto 18 di `db_card.hsp`: le carte fra la riga 8601 e la 9100 (38).

⚠️⚠️ **QUATTORDICI carte di questo lotto hanno l'inglese che finisce con uno
SPAZIO**, e la resa deve finire con lo spazio anche lei: `verifica` lo pretende
(la giuntura col pezzo che segue). Sono `:8740`, `:8805`, `:8870`, `:8883`,
`:8909`, `:8922`, `:8935`, `:8961`, `:8974`, `:8987`, `:9000`, `:9013`, `:9078`
e `:9091`. ⓘ E' una proprieta' del blocco, non una svista di una riga: da qui in
avanti conviene guardarla prima di scrivere, non dopo che la rete boccia.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `手裏剣` → **shuriken**
(`invariati.md`: prestito acquisito, maschile, invariato al plurale — ⚠️ nel
lotto 17 l'avevo reso «stelline da lancio» a `:8441` e l'ho corretto),
`リトルシスター` → **Little Sister** (`action.hsp:17383`, invariato: quindi
`ビッグシスター` e' **la Big Sister** e la prosa di `:9078` la chiama cosi'),
`死神` → **la Morte** (`buff.hsp:80`), `メシェーラ` → **i Meshera**,
`ヴァルム` → **Valm** (`chat.hsp:24292`), `ロスリア` → **Lothria**,
`イェルス` → **Yerles**, `ニンジャ` → **il ninja** (`invariati.md`, ed e' l'unica
delle ventuno classi finte che resta identica all'inglese), `1gp` → **una moneta
d'oro** (`glossario.md`).

ⓘ **Due carte di questa sessione si tengono per mano**: `:9091`, il vecchio
`<Stoke>`, e' il nonno che manda le caramelle, e `:8103` (lotto 17) e' il ragazzo
`<Wel>`, che al nonno che gli manda caramelle e lettere e' affezionatissimo. Le
due prose usano la stessa parola per la stessa cosa.

ⓘ `鎖鎌` non era mai comparso: reso **la falce a catena** (`:8766`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :8610 <Yacatect>
    (8610, 'She loves business and will trade with anyone, whether they are gods, men or demons. She is very picky about money and will not allow even 1gp to be wasted. Loves the stone money she has recently acquired.'):
        "Le piace commerciare, e tratta senza fare differenze con gli dei, con gli uomini e con i mostri. Sui soldi è pignola e non ammette che si sprechi neanche una moneta d'oro. Ultimamente va matta per certe monete di pietra che si è procurata.",

    # ---------------------------------------------------------- :8623 <Iper Yacatect>
    (8623, 'Yacatect in a rage. She completely loses control of herself and goes on a rampage, throwing her precious collection at people. After she calms down, she suffers from self-loathing over the incident.'):
        "Yacatect fuori di sé dalla rabbia. Non è più in sé per niente e arriva a scagliare addosso alla gente la sua preziosa collezione. Quando poi si calma, si detesta per quello che ha fatto.",

    # ---------------------------------------------------------- :8636 il signor becco a scarpa
    (8636, 'A huge bird with the elegance of a stone statue. It is almost motionless, but this is so as not to alarm its prey. Nevertheless, its eyes are so sharp that one has no choice but to be wary.'):
        "Un uccello enorme, che emana la nobiltà di una statua di pietra. Non si muove quasi mai, e lo fa per non mettere in allarme la preda. Solo che ha uno sguardo talmente tagliente che in allarme ci si mette lo stesso.",

    # ---------------------------------------------------------- :8649 il ninja rosso
    (8649, 'A ninja that, after relentless training, has abandoned the idea of being a human. The way it uses its massive afterimages to toy with the enemy and crush them with its sheer mass is truly breathtaking. They say that if you want to hide a tree, hide in the forest, the essence of covert manoeuvre is mastered by this ninja.'):
        "Uno che, dopo un allenamento senza tregua, ha smesso di essere un uomo. Confonde il nemico con immagini residue che hanno una massa vera e poi lo schiaccia con la quantità: uno spettacolo. Se vuoi nascondere un albero, nascondilo nel bosco: l'essenza del movimento furtivo sta tutta qui.",

    # ---------------------------------------------------------- :8662 <Eila> la kunoichi fuggiasca
    (8662, 'From an early age, she often ran away from home because she could not endure the rigorous training of the ninja. She does not have a very favourable view of ninjas. She has not been able to show her ability because she does not want to, but her brother and father saw that Eila had the potential to be a prodigious ninja.'):
        "Da piccola non reggeva l'addestramento durissimo dei ninja e scappava spesso di casa. I ninja non le vanno tanto a genio. Siccome fa tutto controvoglia non rende quanto potrebbe, ma il fratello e il padre lo avevano capito, che Eila ha la stoffa del ninja geniale.",

    # ---------------------------------------------------------- :8675 <Getuei> il maestro ninja
    (8675, 'He has endured the rigours of ninja training since childhood. He became chieftain of the ninja army at a young age. Extremely strict.His speciality is the art of shapeshifting, which can fool even the most seasoned adventurers.'):
        "Fin da piccolo ha retto l'addestramento durissimo dei ninja, e ancora giovane è diventato capo della schiera. È di una severità estrema. La sua specialità è l'arte della sostituzione, con cui inganna perfino l'avventuriero più smaliziato.",

    # ---------------------------------------------------------- :8688 <Naplus> l'alchimista
    (8688, 'She has a straightforward and hard-working personality, but also shows a mad side when it comes to alchemy. She has a soft-bread phobia after a lot of things with her alchemy teacher.'):
        "Di carattere è schietta e gran lavoratrice, ma quando si parla di alchimia mostra anche un lato da folle. Col suo maestro di alchimia ne sono successe di tutti i colori, e da allora ha il terrore del pane soffice.",

    # ---------------------------------------------------------- :8701 <Kuron> la veste nera
    (8701, "She is very close to Siraha, who is experiencing the same difficulties since young. So much so that when she decided to move out, she cried a lot and didn't leave until he promised to exchange letters with her on a regular basis."):
        "Con Siraha, che ha avuto la sua stessa sorte, va d'accordissimo. Tanto che, quando si decise il trasloco, pianse a dirotto e non si staccò da lui finché non le promise che si sarebbero scritti con regolarità.",

    # ---------------------------------------------------------- :8714 <Siraha> la pelle candida
    (8714, 'Goats, a paper-eating creature, are said to have been among their ancestors. Perhaps because of this, when he sees a piece of paper, he unconsciously brings it to his mouth. Until now, he has accidentally eaten a letter he was in the middle of writing about 34 times.'):
        "Pare che fra i suoi antenati ci fosse la capra, una bestia che mangia la carta. Sarà per questo che, quando vede un foglio, se lo porta alla bocca senza nemmeno accorgersene. Fino a oggi gli è capitato trentaquattro volte di mangiarsi per sbaglio la lettera che stava scrivendo.",

    # ---------------------------------------------------------- :8727 il viaggiatore
    (8727, "Rootless people go from town to town in search of a safe haven. Each person's path is his or her own, whether to become a tourist for funds or an adventurer or mercenary for power."):
        "Gente senza radici, che va di città in città in cerca di un posto dove fermarsi in pace. Chi mette insieme i quattrini si fa turista, chi mette insieme la forza va all'avventura o si fa mercenario: ognuno prende la sua strada.",

    # ---------------------------------------------------------- :8740 il profugo degli Elea
    (8740, 'The refugees, who were burned out of their forests and settled in Lothria, were scattered all over the world with the fall of Lothria. They lost their homes and hope, but only persecution remained after the truth was revealed. '):
        "Gli hanno bruciato la foresta e sono andati a stare a Lothria; poi Lothria è caduta in disgrazia e loro si sono sparsi per il mondo. Avevano perduto la patria e la speranza, e quando la verità è venuta a galla l'unica cosa che è rimasta è stata la persecuzione. ",

    # ---------------------------------------------------------- :8753 l'addetto del casinò
    (8753, 'The casino never rejects anyone and welcomes those who dream of getting rich. The casino staff are heartily supportive of their gambling endeavours. As long as the customer loses money.'):
        "Il casinò non respinge nessuno e accoglie a braccia aperte chi sogna di far fortuna in un colpo solo. E gli addetti fanno il tifo di cuore per chi si mette a giocare. Finché quel cliente lascia soldi sul tavolo.",

    # ---------------------------------------------------------- :8766 il ninja
    (8766, 'A man who keeps to himself and hides in plain sight, performing all sorts of black work. This nasty fellow uses shuriken and chain scythes from medium range to slowly drain the blood and strength of the opponent. When not working, they live by farming.'):
        "Uno che mette da parte sé stesso, si nasconde e sbriga ogni sorta di lavoro sporco. Un tipo scorretto: da mezza distanza, con gli shuriken e la falce a catena, ti porta via il sangue e le forze un po' per volta. Quando non ha lavoro campa coltivando la terra.",

    # ---------------------------------------------------------- :8779 la lama re
    (8779, 'A blade that absorbs the souls of enemies it has slain and takes their mighty power for itself. It has the ability to control gravity and is capable of simple flight. Its full power is unleashed when facing powerful enemies.'):
        "Una lama che ha assorbito le anime dei nemici abbattuti e ne ha fatto propria la forza smisurata. Sa comandare la gravità e riesce perfino a volare, alla buona. Quando si trova davanti un avversario forte, quella forza si scatena tutta.",

    # ---------------------------------------------------------- :8792 l'estivante
    (8792, "They like the sea very much and come to visit Valm, where there is a beautiful coastline. They are too excited to go to the sea, so they come here in their swimming costumes and later get into trouble because they don't have any clothes to change into."):
        "Ama moltissimo il mare, e viene a divertirsi a Valm, dove la costa è bellissima. Ma non stava più nella pelle all'idea di andarci, ed è partito già col costume addosso: da cambiarsi non ha niente, e dopo saranno guai.",

    # ---------------------------------------------------------- :8805 il soldato Yerles di nuovo modello
    (8805, "Members of the ultra-elite Yerles unit, where prototypes of the latest armaments are deployed as a priority. Often at the mercy of the chief development officer's playful attitude, some of them are seen returning home in tears. "):
        "Fa parte del reparto scelto fra gli scelti di Yerles, quello a cui i prototipi degli armamenti nuovi arrivano per primi. Lo spirito burlone del capo dello sviluppo se li rigira come vuole, e capita spesso di vederne tornare qualcuno in lacrime. ",

    # ---------------------------------------------------------- :8818 il giocatore d'azzardo
    (8818, 'A general term for people who do not have regular jobs and try to make a living through gambling. Those who lose their money disappear without being noticed, and no one knows their whereabouts.'):
        "È il nome che si dà a tutti quelli che non hanno un lavoro fisso e cercano di campare con l'azzardo. Quelli che restano senza soldi spariscono senza che nessuno se ne accorga, e dove siano finiti non lo sa nessuno.",

    # ---------------------------------------------------------- :8831 il soldato yerles infetto
    (8831, 'The elites of the Yerles army. Although they were able to avoid being absorbed, they have been trapped by the mycelium growing from the ground and have undergone assimilation. It is only a matter of time before they are unable to retain their human form.'):
        "Truppa scelta dell'esercito di Yerles. Di farsi inghiottire è riuscito a evitarlo, ma il micelio che spunta dal terreno lo ha afferrato e l'assimilazione va avanti. Che non riesca più a tenere la forma di uomo è solo questione di tempo.",

    # ---------------------------------------------------------- :8844 la candela della vita
    (8844, 'A candle controlled by the Death that has been set in motion. It enjoys dropping hot wax on a dying, writhing human being. The fire in their heads is strangely not hot to the touch.'):
        "Una candela che la Morte teneva in custodia e che si è messa in movimento. Il suo passatempo è gocciolare cera bollente addosso a chi è in fin di vita e non riesce più a muoversi. Il fuoco che ha in testa, stranamente, a toccarlo non scotta.",

    # ---------------------------------------------------------- :8857 lo spirito del budino
    (8857, 'One has double-downed on their love for pudding gathered and became a pudding spirit. Popular for being very sweet, combined with a simple facial expression. However, their corpses are not pudding-flavoured.'):
        "Tanto amore per il budino si è raccolto in un punto solo, ed è nato uno spirito. Con quella faccia da ingenuo piace parecchio, e tutti lo trovano dolcissimo. Il cadavere, però, di budino non sa.",

    # ---------------------------------------------------------- :8870 lo spirito magico
    (8870, 'The magical residues of wizards who have already left this world, have fused with the mana that abounds in the wilderness and become independent as spirits. They react to specific magic and come close to it. '):
        "Quel che restava del potere magico dei maghi già andati via da questo mondo si è fuso con la mana di cui la natura abbonda, e se n'è staccato uno spirito. Se sente certe magie, arriva. ",

    # ---------------------------------------------------------- :8883 lo spirito guerriero
    (8883, "One fought demons with one's bare hands to protect his family, stabbed to death, and a part of their souls became spirits. Their shining fists are wielded for the sake of those they are supposed to protect. "):
        "C'è chi ha affrontato i mostri a mani nude per difendere la famiglia ed è morto uccidendo: un pezzo di quelle anime è diventato spirito. Quei pugni che risplendono si alzano per chi va protetto. ",

    # ---------------------------------------------------------- :8896 la campana del giudizio
    (8896, 'A bell monster that wanders around with abnormal speed. It was born when a bell signalling the end of the world came to life. It is a dangerous being, but it has a surprising fondness for caramels.'):
        "Un mostro a forma di campana, che vaga con una rapidità che non è normale. È nato quando la campana che annuncia la fine del mondo ha preso vita. È un essere inquietante, ma ha un debole che non ti aspetti: le caramelle mou.",

    # ---------------------------------------------------------- :8909 <Gavela> l'ingegnere capo
    (8909, 'He is familiar with technology in a wide range of fields and often develops things that are beyond the level of civilisation. He is regarded by those around him as being beyond a genius and is now considered to be a freak. '):
        "Conosce a fondo le tecniche dei campi più diversi, e non di rado tira fuori roba che col livello di civiltà di adesso non sta in piedi. Attorno a lui hanno smesso di chiamarlo genio: ormai lo trattano da svitato. ",

    # ---------------------------------------------------------- :8922 l'angelo deforme
    (8922, 'The latest disaster created by an assemblage of cornered Meshera, reconstituting the materials they have absorbed. Compared to the original, it lacks various functions, but has superior combat power. '):
        "L'ultima sciagura, generata dall'ammasso dei Meshera messi alle strette rimettendo insieme la materia che avevano assorbito. Rispetto all'originale gli mancano parecchie funzioni, ma in combattimento vale di più. ",

    # ---------------------------------------------------------- :8935 il chupacabra
    (8935, 'Formerly an unidentified animal, it has been sighted more frequently in recent years due to environmental changes. Its staple diet is wild animal and human blood, and it has a strong body. '):
        "Un tempo era un animale mai confermato, ma da qualche anno, con l'ambiente che cambia, lo si avvista spesso. Si nutre soprattutto del sangue degli animali selvatici e degli uomini, e ha un fisico tenace. ",

    # ---------------------------------------------------------- :8948 la Carmilla
    (8948, 'Female vampire hails from the depths of hell in search of fresh blood. Her hobby is to brainwash her opponents completely before slowly sucking their blood. She prefers to prey on women.'):
        "Una vampira salita dal fondo dell'inferno in cerca di sangue fresco. Il suo passatempo è lavare per bene il cervello alla vittima e poi succhiarle il sangue con tutta calma. Se può scegliere, preferisce le donne.",

    # ---------------------------------------------------------- :8961 il vampiro
    (8961, 'Their main source of nutrition is raw blood, but they will eat basically anything. Vampires are naturally vulnerable to sunlight, but they are able to work in broad daylight because they block sunlight by cloaking their entire body in magical powers. '):
        "Si nutre di sangue vivo, ma in sostanza mangia qualunque cosa. Un vampiro per natura teme la luce del sole; questo però si avvolge tutto quanto di potere magico e la respinge, così può muoversi anche in pieno giorno. ",

    # ---------------------------------------------------------- :8974 il Meshera Vim
    (8974, 'They are desperately trying to stay conscious, but their whole body has been so infested with bacteria that they no longer even know who they were. They are waiting for an entity that could kill them. '):
        "Si aggrappa con le unghie alla coscienza, ma i batteri gli hanno corroso il corpo da capo a piedi e ormai non sa più nemmeno chi fosse. Aspetta con ansia qualcuno che gli dia la morte. ",

    # ---------------------------------------------------------- :8987 il Meshera Argin
    (8987, 'The result of a human who may have once been a wizard, infected by Meshera. They are faintly conscious, but the bacteria have now invaded 80% of their brains and they are completely helpless. '):
        "È quel che resta di un uomo invaso dai Meshera, e che prima doveva essere un mago. Un filo di coscienza gli è rimasto, ma i batteri gli hanno preso ormai l'ottanta per cento del cervello: di libertà non ne ha più. ",

    # ---------------------------------------------------------- :9000 il Meshera Hergmut
    (9000, 'Their bodies are controlled by electrical signals produced by the bacteria. Due to imperfect nerve take-over, the person who is the prime body is in constant severe pain. '):
        "Il corpo glielo comandano i segnali elettrici che emettono i batteri. I nervi non sono stati presi per intero, e per questo l'uomo che gli fa da base soffre dolori atroci senza un attimo di tregua. ",

    # ---------------------------------------------------------- :9013 il cordiceps
    (9013, "It was given this name as a result of constantly fending off those who tried to eat it, and as a result, it is considered to be 'always in the fight'. It is shunned by other mushrooms because it is extremely aggressive. "):
        "Ha respinto per anni chiunque provasse a mangiarselo, e allora si è detto che sta sempre in mezzo alla battaglia e gli hanno dato questo nome. Ha una foga soffocante, e gli altri funghi lo tengono a distanza. ",

    # ---------------------------------------------------------- :9026 il cucciolo di drago di fuoco
    (9026, 'They are curious and follow things that interest them. Escaped from the nest quickly, causing problems for its parents. They make a chirping sound similar to that of bird chicks. Barking and fire breathing skills are learned from their parents, so they need to be taught properly if they are to be kept in captivity.'):
        "È curioso e va dietro a tutto quello che gli mette curiosità. Scappa dal nido in un attimo, e per i genitori sono guai. Il verso che fa somiglia a quello dei pulcini. A ruggire e a sputare fuoco impara dai genitori: chi se lo alleva glielo deve insegnare per bene.",

    # ---------------------------------------------------------- :9039 <Arma> la guida turistica
    (9039, 'Member of the West Irva Tourist Association. She is popular for her spectacular killing shows in which she literally tears off and throws wild thieves and monsters. Sometimes she tears apart her customers by mistake.'):
        "Fa parte dell'associazione turistica di Irva occidentale. È famosa per i suoi spettacoli di massacro a grande effetto, dove briganti e mostri li fa a pezzi e li scaglia via per davvero. Ogni tanto, per sbaglio, fa a pezzi un cliente.",

    # ---------------------------------------------------------- :9052 la maledizione del faraone
    (9052, 'Mana-mediated traps designed to counter grave robbers. It operates by trapping the victim, who is now the source of the mana, inside the coffin. Sprays curses and its horrifying appearance leaves the viewer in a daze.'):
        "Una trappola che si muove servendosi della mana, pensata contro chi va a saccheggiare le rovine. Funziona fissando dentro il sarcofago qualcuno che faccia da fonte di mana. Sparge maledizioni, e chi vede quella forma orrenda resta intontito.",

    # ---------------------------------------------------------- :9065 il gatto zombi
    (9065, 'The soul of a cat, once dead and separated from its body, returns to its own body and is reborn. This often occurs when they have a strong attachment to their original body. Although the loving nature of the soul remains the same as when it was alive, their body is rapidly deteriorating.'):
        "È nato quando l'anima di un gatto morto, che dal corpo si era già staccata, è tornata dentro la propria carcassa. Succede spesso quando al corpo di prima si è molto attaccati. La tenerezza è la stessa di quando era vivo, ma il corpo gli va in pezzi giorno dopo giorno.",

    # ---------------------------------------------------------- :9078 la Big Sister
    (9078, 'Grown-up Little Sister. She boasts such fighting ability that there is no need for a symbiotic relationship, but she was considered a failure because she uses all the energy she was supposed to accumulate for fighting. '):
        "Una Little Sister cresciuta. In combattimento vale al punto che di una simbiosi non ha più bisogno; ma siccome l'energia che dovrebbe mettere da parte la spende tutta a combattere, l'hanno giudicata un esperimento riuscito male. ",

    # ---------------------------------------------------------- :9091 il vecchio <Stoke>
    (9091, 'He became addicted to the candy his grandfather gave him as a child and has been giving the same candy to his own grandchildren. He enjoys throwing performance parties and bringing people together. '):
        "Da bambino si era preso il vizio dei dolciumi che gli dava il nonno, e adesso dà gli stessi dolciumi ai suoi nipoti. Il suo passatempo è organizzare feste con la musica e radunare gente. ",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-018.jsonl'
DA, A = 8601, 9100
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
