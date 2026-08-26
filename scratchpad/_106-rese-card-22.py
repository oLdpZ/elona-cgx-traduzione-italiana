# -*- coding: utf-8 -*-
"""106a - Lotto 22 di `db_card.hsp`: le carte fra la riga 10601 e la 11100 (38).

⚠️ **UNDICI carte su trentotto hanno l'inglese che finisce con uno SPAZIO**:
`:10612`, `:10625`, `:10638`, `:10651`, `:10690`, `:10703`, `:10755`, `:10768`,
`:10794`, `:10911`, `:10937`.

⭐⭐⭐ **QUESTO LOTTO HA FATTO SALTARE FUORI UN NOME SDOPPIATO CHE ESISTEVA GIA'
NEL DIZIONARIO, E NON E' DI QUESTA SESSIONE.** `かたつむり` e' reso in **due**
modi:

    かたつむり              la CREATURA base   ->  «la chiocciola»
                            (`action.hsp:17991`, `custom_enemyevolution:1669`,
                             `db_card:10969`, e da qui la prosa `:10963`)
    『かたつむり（翼）』     le tre UNICHE      ->  «<Lumaca> alata»,
    『かたつむり（機乗）』                          «<Lumaca> in sella all'androide»
    かたつむり（寄生）                             «la lumaca parassitata»

Le uniche portano il nome della creatura base — in giapponese e' **la stessa
parola** — e in italiano sono diventate un'altra bestia. ⓘ Trovato leggendo il
nome di `:10963` col dossier davanti, cioe' come i quattro sbagli della 105a e
i due nomi della 104a: **leggendo, non con una rete**.

✅ **Qui dentro la prosa ubbidisce al referente**: dove il giapponese parla della
creatura base si scrive «chiocciola» (`:10963`, `:11028`), dove parla di una
delle uniche si scrive «lumaca», che e' il loro nome. ⚠️ **E per lo stesso motivo
`:9897` del lotto 19 e' stata corretta**: il 清掃員 fa pace con una かたつむり
base, non con l'unica in sella all'androide.
🔶 **La decisione vera — unificare i quattro nomi — resta aperta e non si prende
qui**, perche' tocca i nomi che il giocatore legge in tre file.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `八柱` → **le otto divinità**
(`chat.hsp`), `魔石` → **la pietra magica**, `灼熱の塔` → **la Torre Rovente**,
`アダマンタイト` → **adamantio**, `ナノマシン` → **nanomacchine**, `聖夜祭` →
**la festa della notte santa**, `化身の黒猫` → **il gatto nero delle
Incarnazioni** (coniato nella 104a, e `:10768` e' la carta dove torna),
`ノースティリス` → **Tyris del Nord**, `イルヴァ` → **Irva**, `プチ` → **il
putit**, `スライム` → **la melma**, `吟遊詩人` → **il menestrello**, `大鎌` →
**la falce**, e i nomi delle divinita': **Jure**, **Ehekatl**, **Lulwy**,
**Opatos**, **Kumiromi**, **Mani**. ⚠️ `ジュア` (Jure, la dea) non e' `ジューア`
(Juere, la nazione del lotto 20): un carattere di differenza, e il glossario lo
segnala apposta.

⚠️ **UNA CARTA HA L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.** `:10716`
dice 上辺ではいつも通りのように見えるが — «in superficie sembra la solita» — e
l'inglese legge 上辺 come «on the upside». ⓘ Nella stessa voce l'inglese porta
`\\"walking disaster\\"` con le virgolette **scappate**: la resa scioglie la
citazione in discorso diretto senza virgolette, come fanno tutte le carte, e cosi'
la giuntura non ha niente da rompere.

ⓘ `:10664` chiama la moglie 赤い義眼のクルイツゥア: il nome completo della carta
`:10651` e' «<Quruiza> l'ingannatrice dall'occhio finto», e `chat.hsp` la nomina
allo stesso modo. Qui basta «Quruiza dall'occhio rosso», che e' quel che dice il
giapponese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :10612 <Erystia> la studiosa di storia
    (10612, 'Historical researcher in the service of the Palmia royal family. She is the deputy head of the Lesimas research team, thanks to her background in researching the history of the Nefia labyrinth complex. '):
        "Ricercatrice di storia al servizio della casa reale di Palmia. Le hanno riconosciuto i trascorsi di studio sulla storia dei labirinti di Nefia, e per questo è vicecomandante della spedizione a Lesimas. ",

    # ---------------------------------------------------------- :10625 <Issizzle> l'aberrazione oscura
    (10625, 'In the past, he tried to ascend himself to godhood with his original theory and became a deformity that could neither be described as a god nor a demon. Since then, he has stopped researching and has become a fool who only protects the results of his research. '):
        "Un tempo cercò di elevarsi a dio con una teoria tutta sua, e divenne un'aberrazione che non si può dire né dio né mostro. Da allora ha smesso di studiare ed è scaduto a sciocco che si limita a difendere i risultati delle proprie ricerche. ",

    # ---------------------------------------------------------- :10638 <Wynan> il signore del Castello Antico
    (10638, 'Lord of an old castle in the dense, deep forests of southern North Tyris. He has enjoyed playing chess since before he gained the power of the magic stone, and lives with his pawns after his family passed away. '):
        "Il signore del castello antico che sta nel folto di una foresta cupa e profonda, a sud di Tyris del Nord. Gli scacchi erano il suo passatempo già prima che ottenesse la forza della pietra magica, e da quando la famiglia gli è morta vive insieme ai pezzi. ",

    # ---------------------------------------------------------- :10651 <Quruiza> l'ingannatrice dall'occhio finto
    (10651, 'A wizard with red artificial eyes who resides at the top of a burning, scorching tower. Her distrust of humans has led her to take a dragon as her husband, and they live a hot, passionate life together every day. '):
        "Una maga dall'occhio finto rosso, che ha preso casa in cima alla Torre Rovente, tutta un incendio. La sfiducia negli uomini l'ha portata a prendersi per marito un drago, e insieme passano giornate bollenti. ",

    # ---------------------------------------------------------- :10664 <Corgon> il drago d'acciaio
    (10664, 'Evil dragon, husband of the red-eyed Quruiza. Together with his wife, who holds the magic stone, he rules the Burning Tower. His digestive system as well as his skin is as tough as steel and he eats everything well.'):
        "Il drago malvagio, marito di Quruiza dall'occhio rosso. Insieme alla moglie, che custodisce la pietra magica, dominava la Torre Rovente. Non solo la pelle: anche l'apparato digerente ce l'ha resistente come l'acciaio, e mangia di tutto con gusto.",

    # ---------------------------------------------------------- :10677 <Jure>
    (10677, 'Goddess with healing powers. She makes a daily effort to make her breasts appear as large as possible and blatantly avoids standing next to Ehekatl. She is a bit absent-minded and is in all sorts of danger without a defender.'):
        "La dea che ha il potere di guarire. Ogni giorno si dà da fare per far sembrare il petto più grande che può, ed evita in modo sfacciato di mettersi accanto a Ehekatl. È un po' sbadata, e senza un difensore vicino si mette nei guai in mille modi.",

    # ---------------------------------------------------------- :10690 <Jure la Benedetta>
    (10690, 'The form in which Jua, originally a healer, releases her power to destroy her enemies. The light emitted by its wings is said to be gentle to those who follow it and searing to those who oppose it. '):
        "La forma che prende Jure, che di suo guarisce, quando libera la propria forza per annientare i nemici. La luce che sprigionano quelle ali, dicono, è dolce per chi la segue e brucia per chi le si oppone. ",

    # ---------------------------------------------------------- :10703 <Lulwy>
    (10703, 'She hates being bound by things like clothes and is usually fully naked. The most important parts of her body are obscured by distorting the air, but even so, she is sure to be difficult to look at. '):
        "Non sopporta di essere legata a una cosa come i vestiti, e se ne sta sempre completamente nuda. Le parti che contano le nasconde deformando l'aria, ma non si sa lo stesso dove guardare. ",

    # ---------------------------------------------------------- :10716 <Lulwy la Devastatrice>
    (10716, 'On the upside, she appears to be acting as usual, but on the inside she\'s a raging bull. In her anger, she goes around destroying the area as she pleases and as the wind blows. The term \\"walking disaster\\" is apt.'):
        "In superficie sembra la solita, ma dentro è in tempesta. Per la rabbia va in giro a distruggere tutto quello che le capita, dove la porta il vento. Le si addice l'espressione: una calamità che cammina.",

    # ---------------------------------------------------------- :10729 <Opatos il Possente>
    (10729, 'Beautiful and muscular with muscles strengthened to the max. He can shatter a lump of adamantite with his abdominal muscles. The only complaint is that he has not been able to train his wings.'):
        "I muscoli, potenziati fino al limite, sono belli e possenti. Con gli addominali riesce a ridurre in polvere un blocco di adamantio. L'unico cruccio è non essere riuscito ad allenare le ali.",

    # ---------------------------------------------------------- :10742 <Kumiromi l'Oscuro>
    (10742, 'The shock from the pain turned him on completely. He swings the scythe in a bizarre manner with a broken laugh. When it comes to this, there is no stopping until someone dies.'):
        "Il colpo del dolore gli ha fatto scattare l'interruttore fino in fondo. Ride di una risata rotta e mena la falce con gusto sanguinario. Quando arriva a questo punto non lo ferma più niente, finché uno dei due non muore.",

    # ---------------------------------------------------------- :10755 <Deus ex manina>
    (10755, "When Mani's makeshift body ceases to function, his true form is activated when the main programme is super-transferred. It suddenly manifests from the mechanisms and brings everything to an end. "):
        "Quando il corpo provvisorio di Mani smette di funzionare, il programma principale viene teletrasportato e accende la sua forma vera. Compare all'improvviso dal congegno e mette fine a tutto. ",

    # ---------------------------------------------------------- :10768 <Ehekatl>
    (10768, 'She looks like a grown-up woman, but on the inside she is like a friendly cat. She is often seen sunbathing or eating fish with her incarnation, a black cat. '):
        "A vederla sembra una donna adulta, ma dentro è tale e quale a un gatto affettuoso. Spesso la si trova a prendere il sole o a mangiare pesce insieme al gatto nero delle Incarnazioni. ",

    # ---------------------------------------------------------- :10781 <Il dio dentro Ehekatl>
    (10781, 'A mysterious dark Ehekatl pops out of the Ehekatl. Like a cat on the warpath, it snarls and threatens while keeping its distance. The look in its eyes is that of a beast hunting its prey.'):
        "La misteriosa Ehekatl nera che è schizzata fuori da dentro Ehekatl. Come un gatto pronto alla lotta, tiene la distanza, ringhia e minaccia. Lo sguardo che ha è quello di una bestia a caccia della preda.",

    # ---------------------------------------------------------- :10794 <Opatos>
    (10794, 'He has a well-trained body as hard as a mineral and a heart as solid as the earth. He wears a blindfold to train his sense of equilibrium, but sometimes loses his balance and causes tectonic shifts. '):
        "Ha insieme un corpo temprato duro come la pietra e un animo saldo come la terra. Per allenare il senso dell'equilibrio porta una benda sugli occhi, ma ogni tanto perde l'assetto e provoca movimenti della crosta. ",

    # ---------------------------------------------------------- :10807 <Kumiromi>
    (10807, 'A male deity who is sometimes mistaken for a goddess because of his appearance. His chest is swollen from the seeds he carries in his inside pocket, which makes his appearance even more misleading. When he feels cold, he covers his bare shoulders with his wings.'):
        "Un dio maschio che per come si presenta viene scambiato per una dea. Il petto gli si gonfia per le sementi che tiene nella tasca interna, e questo aumenta l'equivoco. Quando sente freddo si copre le spalle nude con le proprie ali.",

    # ---------------------------------------------------------- :10820 <Mani>
    (10820, 'An artificial god created by a mechanical civilisation. He has trouble concentrating when he is tinkering with machines because Lulwy is always trying to interfere with him. He is the only one of the Eight Pillars without wings, but he can fly without problems thanks to the power of science.'):
        "Un dio artificiale generato dalla civiltà meccanica. Quando armeggia con le macchine Lulwy arriva puntualmente a disturbarlo, non riesce a concentrarsi e la cosa lo tormenta. Fra le otto divinità è l'unico senza ali, ma con la forza della scienza vola senza problemi.",

    # ---------------------------------------------------------- :10833 lo zilla
    (10833, "An iguana that has mutated and grown huge under the influence of nuclear testing. It looks like a dinosaur, but prefers to eat fish rather than meat. It fights with agility, but is weak and timid. It shouldn't eat fish all the time, after all."):
        "Un'iguana mutata e diventata enorme per via degli esperimenti nucleari. A vederlo è un dinosauro, ma alla carne preferisce il pesce. Combatte facendo leva sulla rapidità, però incassa male ed è pauroso. Si vede che mangiare solo pesce non va bene.",

    # ---------------------------------------------------------- :10846 il putit
    (10846, 'A slime that was bred to be edible. Many people find them cute and keep them as pets, but beware: they sometimes prey on people.'):
        "Una melma selezionata per essere mangiata. In tanti la trovano graziosa e la tengono come animale da compagnia, ma attenzione: ogni tanto si mangia le persone.",

    # ---------------------------------------------------------- :10859 il putit rosso
    (10859, "A red-colored putit that's somewhat stronger than normal putits. Some people used to claim that red putits were simply female putits, but in truth, the two have nothing to do with each other. The actual reason behind their red coloring is unknown."):
        "Ha il corpo più rosso di un putit comune ed è anche un po' più forte. Un tempo c'era chi sosteneva che i putit rossi fossero le femmine dei putit, ma non c'entrano proprio niente. Perché siano rossi, ancora oggi, non si sa.",

    # ---------------------------------------------------------- :10872 la melma
    (10872, 'They are liquid lifeforms that move in a flowing manner, dissolving and feeding on whatever enters their bodies. Watch out for squishy puddles of moving water.'):
        "Una forma di vita liquida che si sposta scorrendo, e scioglie e mangia tutto quello che le finisce dentro. Se vedi una pozza che si muove molle molle, sta' attento.",

    # ---------------------------------------------------------- :10885 la melma acida
    (10885, 'A slime that has taken in chemicals illegally dumped by scientists and mages causing it to mutate. Dangerous chemical reactions are taking place in their bodies, and acidic body parts are dispersed when stimulated.'):
        "Una melma che ha inglobato le sostanze chimiche buttate via di nascosto da scienziati e maghi, ed è mutata. Dentro di lei avvengono reazioni chimiche pericolose, e se la si stuzzica schizza via pezzi acidi del proprio corpo.",

    # ---------------------------------------------------------- :10898 la bolla
    (10898, 'A creature with semi-transparent flesh. When a wound is inflicted on them, they multiply like bubbles, hence the name. Not a few towns are filled with them as they multiply.'):
        "Un mostro dal corpo semitrasparente. Quando si ferisce, dalla ferita si moltiplica come fanno le bolle, e di lì gli viene il nome. Le città sommerse da loro, che raddoppiano e raddoppiano, non sono poche.",

    # ---------------------------------------------------------- :10911 la bolla azzurra
    (10911, 'A subspecies of bubble with bluish flesh. Some advocate the theory that the oceans were created after their mass increase, but no one is taking them seriously. '):
        "Una sottospecie di bolla dal corpo tendente all'azzurro. C'è chi sostiene la teoria che il mare sia nato dopo che loro si erano moltiplicate a dismisura, ma non lo prende sul serio nessuno. ",

    # ---------------------------------------------------------- :10924 l'ammasso mostruoso
    (10924, 'A subspecies of dragon born during the evolutionary process. Only the muscles have developed abnormally and the original form are no longer. It has destroyed countless towns and is regarded as a dangerous demon.'):
        "Una sottospecie di drago nata lungo il cammino dell'evoluzione. Solo i muscoli le si sono sviluppati in modo anomalo, e della forma di partenza non è rimasto niente. Le città che ha distrutto non si contano, e la si teme come un mostro pericoloso.",

    # ---------------------------------------------------------- :10937 il cubo
    (10937, 'Mysterious machine discovered in underground ruins. Its nanomachine repair function has run amok due to a bug, and it creates an identical copy of itself from the faulty part. '):
        "Una macchina misteriosa ritrovata in certe rovine sotterranee. La sua funzione di riparazione a nanomacchine è impazzita per un difetto, e dalla parte guasta produce una copia identica a sé stessa. ",

    # ---------------------------------------------------------- :10950 il coniglio selvatico
    (10950, "Its fluffy fur and overall cuteness makes it one of the more popular small animals. Though they're a bit temperamental, there are many who keep them as pets. They're also delicious, but don't say that in front of their fans."):
        "Un animaletto amato per il pelo soffice e per l'aria adorabile. Ha un caratterino un po' scontroso, ma in tanti lo catturano e lo tengono come animale da compagnia. È anche buono da mangiare, però non ditelo davanti a chi gli vuole bene.",

    # ---------------------------------------------------------- :10963 la chiocciola
    (10963, 'When exposed to salt, the water inside their bodies is absorbed, causing them to shrivel into nothingness. Without a doubt the most dull and pathetic creature in Irva. How the species has managed to survive is a complete mystery.'):
        "Se le si versa del sale addosso perde l'acqua che ha in corpo, si raggrinzisce come se si sciogliesse e sparisce. È la creatura più lenta e più misera di tutta Irva, eppure fino a oggi non si è estinta: perché, resta un mistero.",

    # ---------------------------------------------------------- :10976 il soldato sconfitto
    (10976, 'A person who has lost to something, and continues to run in order to escape from that fact. The circumstances are unique to each individual, but sooner or later, the time will come when they must face reality.'):
        "Uno che ha perso. E continua a scappare per non guardare in faccia quel fatto. Che cosa ciascuno abbia perso è affare suo. Solo che, prima o poi, il giorno di battersi con la realtà arriverà.",

    # ---------------------------------------------------------- :10989 il mercenario
    (10989, "A fighter for hire. Many exaggerate their past deeds or lie about former military service in order to get hired, but considering the current economy, they don't have much of a choice."):
        "Gente che vende la propria forza a chiunque abbia una bandiera. Per farsi assumere in molti gonfiano una piccola impresa o si inventano trascorsi di guerra, ma di questi tempi magri non si può dar loro torto.",

    # ---------------------------------------------------------- :11002 l'accattone
    (11002, 'A person who has completely abandoned their pride and fear, willing to even visit the homes of random adventurers and prostrate themselves for gold. It rarely ever works though.'):
        "Ha buttato via del tutto l'orgoglio e la paura: per rimediare del denaro entra perfino in casa di un avventuriero che non ha mai visto, e si butta in ginocchio. Che poi la cosa dia frutto capita di rado.",

    # ---------------------------------------------------------- :11015 l'agricoltore
    (11015, 'Home-grown people skilled in cooking and sewing. No matter how much vegetables they produce, they are bought cheaply, so they basically live on the expenditure of their family.'):
        "Gente di casa, brava a cucinare e a cucire. Per quanta verdura produca gliela pagano sempre due soldi, e così in pratica se la consuma in famiglia.",

    # ---------------------------------------------------------- :11028 lo spazzino
    (11028, 'They will not tolerate anyone who spoils the beauty of the city. They are feared by snails because they carry salt with them at all times. It seems to be safe, in the eyes of the cleaners, to sprinkle salt at snails.'):
        "Chi rovina il decoro della città non la passa liscia. Porta sempre con sé del sale, e per questo le chiocciole lo temono. Spargere sale in giro, per uno spazzino, pare che non conti come sporcare.",

    # ---------------------------------------------------------- :11041 il minatore
    (11041, 'He digs tunnels day and night for the peace and development of the town. It is refreshing to see him digging by force and without any skill.He is attacked by demons that live in the tunnels on a daily basis.'):
        "Giorno e notte scava gallerie per la pace e la crescita della città. Vederlo scavare a forza di braccia, senza nessuna tecnica, mette quasi allegria. Che i mostri annidati nelle gallerie lo assalgano è cosa di tutti i giorni.",

    # ---------------------------------------------------------- :11054 il menestrello
    (11054, 'Performers who make a living from the music and singing they play while travelling from place to place. They are sometimes stoned for their inexperience, but they are not discouraged. They just work harder and harder.'):
        "Musicisti che girano di posto in posto e campano con la musica che suonano e con la voce che cantano. Quando il braccio è acerbo si prendono anche qualche sassata, ma non si perdono d'animo: si impegnano ancora di più.",

    # ---------------------------------------------------------- :11067 la monaca
    (11067, "Regardless of gender, they are uniformly referred to as 'nuns'. They lead a life of celibacy, but few of them make it past the Feast of the Holy Nights, which is overflowing with various desires."):
        "Uomini e donne senza distinzione vengono chiamati tutti allo stesso modo, monache. Conducono una vita di castità, ma pochi arrivano in fondo alla festa della notte santa, dove i desideri di ogni sorta traboccano.",

    # ---------------------------------------------------------- :11080 la bestia sacra
    (11080, 'It is a sacred beast that descends on the end of year festivals and has no insides. There is a superstition that if you are bitten on the head, you will live a year without illness. The clattering of its teeth is a little scary, though.'):
        "La bestia sacra che scende alla festa di fine anno, e dentro non c'è nessuno. C'è la superstizione che se ti morde la testa passi l'anno senza malattie. Il modo in cui batte i denti, però, mette un po' di paura.",

    # ---------------------------------------------------------- :11093 la mascotte a ore
    (11093, 'Part-time worker who dresses up in a bear costume and encourages people to convert. He earns bonuses according to his performance, so whenever he sees someone he can easily persuade, he calls out to them.'):
        "Uno che lavora a ore, infilato in un costume da orso, e invita la gente a convertirsi. Il premio glielo danno in base ai risultati, e così appena vede qualcuno che sembra facile da convincere lo ferma all'istante.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-022.jsonl'
DA, A = 10601, 11100
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
