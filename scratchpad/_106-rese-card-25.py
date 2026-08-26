# -*- coding: utf-8 -*-
"""106a - Lotto 25 di `db_card.hsp`: le carte fra la riga 12101 e la 12600 (38).

ⓘ **I segugi finiscono qui**: `:12109`, `:12122` e `:12135` chiudono la famiglia
cominciata nel lotto 24, e portano l'`インド象` **nel giapponese** come le altre
sette. In tutto il tormentone dell'elefante indiano copre **dieci** carte di
fila, da `:12018` a `:12135`.

⚠️ **UNDICI carte hanno l'inglese che finisce con uno SPAZIO**: `:12135`,
`:12148`, `:12174`, `:12187`, `:12200`, `:12213`, `:12226`, `:12252`, `:12265`,
`:12278`, `:12291`.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `ケルベロス` → **il Cerbero**,
`瘴気` → **il miasma**, `ニンフ` → **la ninfa**, `インプ` → **il folletto**
(`db_card`: e il 上位インプ e' «il folletto maggiore», quindi `冥界の使い` e
`カオスインプ` restano folletti anche loro), `インド象` → **l'elefante indiano**,
`妖精` → **la fata**, `エーテル` → **l'etere**, `眷属` → **il figlio**,
`ワイバーン` → **la viverna**.

ⓘ **La formula dei draghi minori si ripete e si scrive uguale.**
進化の過程で生まれた竜の亜種 apre `:12304`, `:12538` e `:12551`, ed e' la stessa
frase gia' resa a `:10924` nel lotto 22: «Una sottospecie di drago nata lungo il
cammino dell'evoluzione». ⚠️ Nessuna rete lo pretende — la rete 3 confronta i
**giapponesi interi**, e qui gli interi sono diversi — quindi la coerenza qui e'
a carico di chi scrive, non delle reti.

🔶 **Un gioco di parole che non passa, e non e' un difetto di monte.** `:12174`,
il rancore, chiude con 生きた人間の怨念も**おんねん**: 怨念 («rancore») e
おんねん (il «ce n'e'» del dialetto del Kansai) suonano uguale, e la battuta e'
tutta li'. L'inglese l'ha lasciata cadere per primo. La resa italiana dice il
senso — «anche i vivi, di rancore, ne hanno da vendere» — e la rima si perde.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :12109 il segugio del suono
    (12109, 'A dog releases a roaring breath. Even Indian elephants easily faint when it is shouted in their ears. They also have high physical capabilities, and their blows exceed the speed of sound.'):
        "Un cane che manda un soffio accompagnato da un boato. Se glielo urla nelle orecchie, anche un elefante indiano sviene senza fatica. Ha pure grandi doti fisiche, e il suo colpo supera la velocità del suono.",

    # ---------------------------------------------------------- :12122 il segugio dell'oltretomba
    (12122, 'A dog that releases a breath tinged with the miasma of the underworld. It is said that even an Indian elephant would surely ascend to heaven if exposed to it. For a long time it was considered identical to Cerberus, but it has recently been discovered that they are completely different species.'):
        "Un cane che manda un soffio carico del miasma dell'oltretomba. Chi se lo prende in pieno sale in cielo di sicuro, elefante indiano compreso. Per molto tempo lo si è confuso con il Cerbero, ma si è scoperto da poco che come specie sono tutt'altro.",

    # ---------------------------------------------------------- :12135 il segugio del caos
    (12135, 'A dog that emits the breath of chaos. Chaos is an appearance of lack of harmony, and if exposed to its breath, even an Indian elephant will suffer multiple anomalies and die after suffering from them. '):
        "Un cane che manda il soffio del caos. Il caos è la mancanza di armonia, e chi si prende quel soffio, elefante indiano compreso, si becca insieme più disturbi e muore dopo aver penato. ",

    # ---------------------------------------------------------- :12148 lo scoiattolo gigante
    (12148, 'It was omnivorous and ate everything before it became huge, but its size finally led it to attack even humans. They need large amounts of food to sustain their bodies. '):
        "Era onnivoro e mangiava di tutto già prima di diventare enorme, ma con la taglia che si ritrova ha finito per assalire perfino gli uomini. Per mantenere quel corpo gli serve una quantità di cibo. ",

    # ---------------------------------------------------------- :12161 lo scoiattolo assassino
    (12161, 'Giant squirrels that have completely developed a taste for human flesh and actively attack people. Children who approach unprotected often become victims. It can be recognised on closer inspection because it is extremely massive and has a glare in its eyes.'):
        "Uno scoiattolo gigante che ha preso del tutto il gusto della carne umana e che assale gli uomini di sua iniziativa. Le vittime sono spesso bambini avvicinatisi senza difendersi. È tutto muscoli e ha lo sguardo che gli brilla, e a guardarlo bene lo si riconosce.",

    # ---------------------------------------------------------- :12174 il rancore
    (12174, 'It is the materialisation of vindictive thoughts that curse themselves, curse luck, curse God and curse the world. The feelings are not only those of the dead, but also those of living people. '):
        "Il pensiero di astio che maledice sé stesso, maledice la sorte, maledice il dio e maledice il mondo, preso corpo. E quel sentimento non è soltanto dei morti: anche i vivi, di rancore, ne hanno da vendere. ",

    # ---------------------------------------------------------- :12187 il demone affamato
    (12187, 'A form of unrequited souls of those who have died out through starvation. They reach out for help, but even those who touch their hands out of pity are dragged into starvation. '):
        "La forma che prendono le anime senza pace di chi è morto di fame. Tendono la mano per chiedere aiuto, ma trascinano nella fame perfino chi, per pietà, quella mano la tocca. ",

    # ---------------------------------------------------------- :12200 il leone marino ingordo
    (12200, 'A giant sea lion with a voracious appetite. It can take food possessed by its opponents through inter-dimensional space, and instantly digests the food it eats into its own energy. '):
        "Un leone marino enorme e dall'appetito formidabile. Attraverso uno spazio di un'altra dimensione riesce a portare via il cibo che l'avversario ha con sé, e quello che mangia lo digerisce in un istante trasformandolo in energia. ",

    # ---------------------------------------------------------- :12213 il leone marino ingordissimo
    (12213, 'A very large sea lion with a huge appetite. It is said that just a big sea lion evolved to give way to its bloated appetite, and as a result it has developed an advanced organ for perceiving and interfering in other dimensions. '):
        "Un leone marino gigantesco e dall'appetito formidabile. Pare che un semplice leone marino grosso, lasciandosi andare a quell'appetito smisurato, si sia evoluto fino a dotarsi di un organo raffinato che percepisce le altre dimensioni e ci interviene. ",

    # ---------------------------------------------------------- :12226 la nube elettrica
    (12226, 'A mysterious energy aggregate that discharges violently. The unstable energy that has been stored is converted into electricity and is continuously discharged into the surrounding area, making it extremely dangerous to even get close to it. '):
        "Un misterioso ammasso di energia che produce scariche violente. L'energia instabile che ha accumulato si converte in elettricità e continua a scaricarsi tutto intorno: perfino avvicinarsi è pericolosissimo. ",

    # ---------------------------------------------------------- :12239 la nube del caos
    (12239, 'The chaos condensed and became one entity. It scatters chaos around it, swallows the area and tries to grow into an even bigger chaos. Its mere appearance is a sign of disaster.'):
        "Il caos si è condensato ed è diventato un essere solo. Sparge caos tutto intorno, inghiotte quello che ha vicino e cerca di crescere in un caos ancora più grande. A vederlo è una specie di calamità.",

    # ---------------------------------------------------------- :12252 l'occhio fluttuante
    (12252, 'It is completely unclear where the mouth is, where the abdomen is and how it is alive. According to one theory, it is said to be the eye of a demon looking at us from another world. '):
        "Dove abbia la bocca, dove abbia il ventre, come faccia a essere vivo: non si capisce niente. Secondo una certa teoria è l'occhio di un demone che ci spia da un altro mondo. ",

    # ---------------------------------------------------------- :12265 l'occhio del caos
    (12265, 'It floats in the air with a mysterious power, but not very fast. The opponent whose gaze meets his or hers is physically altered, causing multiple abnormalities and physical changes. '):
        "Sta sospeso in aria per una forza misteriosa, ma non è poi così veloce. A chi ne incrocia lo sguardo il corpo va in disordine, e gli si scatenano insieme più disturbi e mutamenti della carne. ",

    # ---------------------------------------------------------- :12278 lo sguardo folle
    (12278, 'If you look directly into the eyes, you will become insane and suffer from illusions, such as maggots springing up. Its flesh is one of the most valuable means of making one resistant to illusions. '):
        "A fissarne le pupille si viene invasi dalla follia e si finisce tormentati da visioni, per esempio vermi che sgorgano da ogni parte. La sua carne è uno dei pochi mezzi preziosi per farsi resistenti all'allucinazione. ",

    # ---------------------------------------------------------- :12291 lo sguardo di morte
    (12291, 'Monsters that emit the gaze of death. Alone, it is not much of a threat, but when it stares at you, your body is paralysed and deprived of magical power, which is a big problem if you are mixed in with a group of enemies. '):
        "Un mostro che manda lo sguardo della morte. Da solo non è una gran minaccia, ma se ti fissa il corpo si paralizza e la forza magica se ne va, e quindi in mezzo a un branco di nemici diventa un guaio serio. ",

    # ---------------------------------------------------------- :12304 la viverna
    (12304, "A subspecies of dragon created during the process of evolution. Commonly referred to as pterodactyls, they have integrated arms and wings, unlike full dragons. In the wyvern's view, its own wings are better looking than those of dragons."):
        "Una sottospecie di drago nata lungo il cammino dell'evoluzione. La chiamano di solito drago alato, e a differenza di un drago completo ha le braccia e le ali tutt'uno. Secondo la viverna, le proprie ali sono più belle di quelle dei draghi.",

    # ---------------------------------------------------------- :12317 la marionetta
    (12317, 'A doll the same size as a person. Its strange movements confuse people on the street. The threads connected to its body stretch towards an unknown place.'):
        "Una bambola grande come una persona. Con i suoi movimenti strani mette in imbarazzo i passanti. I fili legati a quel corpo si allungano verso un posto che nessuno sa.",

    # ---------------------------------------------------------- :12330 la vespa
    (12330, 'Giant flying insects with venomous stingers on their hips. Each one is small and weak, but they have a habit of swarming and are dangerous once surrounded. Their wings buzz noisily.'):
        "Un insetto volante enorme, con un pungiglione velenoso in fondo al corpo. Presa una per una è piccola e debole, ma ha l'abitudine di fare sciame, e una volta che ti circondano diventa pericolosa. Il ronzio delle ali è un fastidio.",

    # ---------------------------------------------------------- :12343 la vespa rossa
    (12343, 'Wasps with fierce and vindictive habit. It uses a paralysing venom injected from its stinger to stop its prey and bring it back fresh to its nest as food. They are insects after all, and will persistently sting even when paralysis is ineffective.'):
        "Ha abitudini feroci e ostinate. Con il veleno paralizzante che inietta dal pungiglione ferma la preda e se la porta al nido fresca, come cibo. Alla fine è pur sempre un insetto, e continua a pungere con accanimento anche chi la paralisi non la sente.",

    # ---------------------------------------------------------- :12356 il ciclope
    (12356, 'A race of giants that boasts a physique approximately ten times that of the average humanoid race.The term refers to the monocular inferior species among them.They move slowly, but it is difficult to physically stop their sturdy steps.'):
        "Una stirpe di giganti che vanta un corpo dieci volte più grande di quello delle stirpi umane comuni. Il nome indica, fra loro, la specie inferiore con un occhio solo. Si muove lento, ma fermare fisicamente il passo di quei corpi robusti è difficile.",

    # ---------------------------------------------------------- :12369 il titano
    (12369, 'Descendants of a tribe of giants who lost their faith and were forced to leave the throne of God.When the apocalypse occurs, their brethren sealed in the depths of the earth will appear with an earth-shaking sound.If you eat their flesh, you will gain strength.'):
        "I discendenti della stirpe dei giganti che, persa la fede, furono cacciati dal trono divino. Si dice che, quando arriverà la fine del mondo, i fratelli sigillati nelle viscere della terra compariranno insieme a un rombo. A mangiarne la carne si guadagna vigore.",

    # ---------------------------------------------------------- :12382 il folletto
    (12382, 'Lowest species of demon. They use a kind of magic that is only marginally effective. However, its flesh promotes the awakening of magical powers, so it is sometimes attacked by adventurers when it goes on errands.'):
        "La specie più bassa fra i demoni. Usa qualche magia imparata alla svelta, ma l'effetto è debolissimo. La sua carne però risveglia la forza magica, e così capita che gli avventurieri lo assalgano mentre è in giro per commissioni.",

    # ---------------------------------------------------------- :12395 il folletto dell'oltretomba
    (12395, "Messenger demons sent from hell. Attacks creatures in the area to bring their souls back to Hell. They seem to have a hard time meeting their master's quotas and often hide and complain."):
        "Un famiglio mandato dall'inferno. Per riportare le anime all'inferno assale le creature che gli capitano intorno. Pare che le quote fissate dal padrone siano dure da raggiungere, e spesso si nasconde a lamentarsi.",

    # ---------------------------------------------------------- :12408 il folletto del caos
    (12408, "A higher demon's servant who plots the collapse of the order. Those who are hit by the arrows of chaos have their biological functions disrupted and suffer complications. They are not treated well and have recently been thinking about changing jobs."):
        "Un figlio di un demone superiore, che trama il crollo dell'ordine. A chi si prende una freccia del caos le funzioni vitali vanno in disordine e cominciano le complicazioni. Il trattamento non è granché, e ultimamente pensa di cambiare mestiere.",

    # ---------------------------------------------------------- :12421 la mano dei morti
    (12421, 'A monster that invites you into the world of death. It craves warm life and has a habit of attracting living things to its hand at random. In its spare time, it starts to draw graffti on the ground.'):
        "Un mostro che invita nel mondo della morte. Ha fame di vita calda, e ha l'abitudine di tirarsi vicino, a caso, tutto quello che è vivo. Quando si annoia si mette a scarabocchiare per terra.",

    # ---------------------------------------------------------- :12434 la mano del caos
    (12434, 'A monster whose arms take the form of chaos that has increased in density for some reason. It does not move from its place and continues to wait to swallow anyone who approaches it into its own chaos.'):
        "Un mostro nato dal caos che, per qualche ragione, si è fatto più denso e ha preso la forma di un braccio. Non si muove di lì e resta in agguato, per inghiottire nel proprio caos chi si avvicina.",

    # ---------------------------------------------------------- :12447 la mano dell'assassino
    (12447, 'A monster in the shape of an arm formed from the madness of an executed murderer. It is said to be born in a pool of blood at the place of execution, and even now that he is dead, it is still trying to produce new victims.'):
        "Un mostro fatto dalla follia di un assassino giustiziato, raccoltasi in forma di braccio. Si dice che nasca dalla pozza di sangue del patibolo e che, anche adesso che lui è morto, cerchi ancora nuove vittime.",

    # ---------------------------------------------------------- :12460 lo spettro
    (12460, 'The aggregation of the terrible negative thoughts that remain after death has become such a threat that it affects the living. The sentiments combine with the ether in the atmosphere to form a temporary body.'):
        "L'ammasso di pensieri neri e tremendi che restano dopo la morte è diventato una minaccia capace di toccare anche chi è in carne e ossa. Quel sentimento si lega all'etere dell'aria e forma un corpo provvisorio.",

    # ---------------------------------------------------------- :12473 la ninfa
    (12473, 'She used to be a fairy, but when she tried to deceive travellers with her magic, she was unexpectedly struck back and died. However, she is not aware that she is dead and wanders around as a floating spirit.'):
        "Un tempo era una fata, ma quando provò a stregare un viandante con la forza magica si prese una reazione che non si aspettava e ci lasciò la vita. Solo che di essere morta non se n'è accorta, e va in giro come spirito errante.",

    # ---------------------------------------------------------- :12486 il fiore mangiauomini
    (12486, 'A flower that grew abnormally by feeding on the mana from the land. After discovering that minced human beings can be used as nourishment, it began to actively attack people. Its dissolved fluid has properties similar to human stomach acid.'):
        "Un fiore cresciuto a dismisura nutrendosi della forza magica della terra. Da quando ha scoperto che l'uomo ridotto a carne trita è un buon nutrimento, ha cominciato ad assalire la gente di sua iniziativa. Il liquido con cui scioglie ha proprietà simili a quelle dei succhi gastrici.",

    # ---------------------------------------------------------- :12499 il fiore del caos
    (12499, 'A man-eating flower that has gained the power of chaos. They disperse a wide variety of pollen and have nourished numerous adventurers by waving hard vines. Its roots are short and strong, and it can move on foot.'):
        "Un fiore mangiauomini che ha ottenuto la forza del caos. Sparge pollini di ogni sorta e, agitando i tralci duri, si è nutrito di parecchi avventurieri. Le radici sono corte e tenaci, e gli permettono di spostarsi camminando.",

    # ---------------------------------------------------------- :12512 il cobra
    (12512, 'A type of poisonous snake. It has a strong, fast-acting venom that often results in death if the bite is not dealt with properly. It has an unpleasant odour, but is rather tasty if cooked.'):
        "Una specie di serpente velenoso. Il suo veleno è potente e agisce subito, e se dopo il morso non si interviene come si deve spesso si muore. Ha un odore forte, ma cucinato non è niente male.",

    # ---------------------------------------------------------- :12525 il cobra reale
    (12525, 'Its venom is so strong that it can kill large animals and even snakes of the same species. Its majestic appearance gives it the air of a king, but its character is surprisingly timid. Some adventurers try to develop a resistance to its venom by eating it whole.'):
        "Ha un veleno tanto forte da uccidere animali di grossa taglia e perfino serpenti della sua stessa specie. L'aspetto maestoso gli dà un'aria da re, ma il carattere è sorprendentemente pauroso. C'è qualche avventuriero che se lo mangia col veleno e tutto, per farsi resistente.",

    # ---------------------------------------------------------- :12538 il draco di fuoco
    (12538, 'A subspecies of dragon born during its evolutionary process. It is incomparably weaker than dragons, but its strength should not be underestimated. When stressed, they breathe out a sigh mixed with fire.'):
        "Una sottospecie di drago nata lungo il cammino dell'evoluzione. Con un drago non regge il confronto, ma non bisogna sottovalutare la sua forza. Quando è sotto tensione manda fuori un sospiro misto a fuoco.",

    # ---------------------------------------------------------- :12551 il draco di ghiaccio
    (12551, 'A subspecies of dragon born during its evolutionary process. They resent the fact that a pack of icehounds is considered more fearsome than a single ice drake.'):
        "Una sottospecie di drago nata lungo il cammino dell'evoluzione. Gli rode che un branco di segugi di ghiaccio venga considerato più temibile di un draco di ghiaccio da solo.",

    # ---------------------------------------------------------- :12564 la mummia minore
    (12564, 'Lowest class of mummy species. Mainly refers to the corpses of criminals and citizens who have been left to rot and accidentally mummified in poor conditions. They have no particular position and attack the living without regard.'):
        "La specie più bassa fra le mummie. Indica soprattutto i cadaveri di criminali e di cittadini lasciati lì, che si sono mummificati per caso in un ambiente pessimo. Non hanno nessun compito e assalgono i vivi senza distinzione.",

    # ---------------------------------------------------------- :12577 la mummia
    (12577, 'A former soldier in a once prosperous kingdom. He uses the weapons and skills he acquired during his life to block the way of intruders. They often work in packs.'):
        "Uno che fu soldato in un regno un tempo fiorente. Usa le armi e le tecniche che aveva da vivo e sbarra la strada agli intrusi. Spesso si muovono in gruppo.",

    # ---------------------------------------------------------- :12590 la mummia maggiore
    (12590, 'A higher species of mummy type. Refers mainly to soldiers artificially mummified to act as guards for the king. They hunt down thiefs with lower-ranked mummies in tow.'):
        "La specie superiore fra le mummie. Indica soprattutto i soldati mummificati apposta per fare da guardia al re. Si porta dietro le mummie di rango più basso e mette alle strette chi saccheggia le rovine.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-025.jsonl'
DA, A = 12101, 12600
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
