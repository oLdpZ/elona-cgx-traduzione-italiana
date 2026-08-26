# -*- coding: utf-8 -*-
"""105a - Lotto 16 di `db_card.hsp`: le carte fra la riga 7601 e la 8100 (38).

⚠️⚠️ **Due carte dove l'inglese di monte dice un'altra cosa dal giapponese**, e
si traducono **dal giapponese**:

    :7648  la Hel     性根が腐っている, «ha l'animo marcio» -> l'inglese legge
                      quel 性 come sesso e scrive «she has a corrupt sexual
                      drive», che il giapponese non dice da nessuna parte
    :7843  l'omega    精霊の力を宿しており, «porta in se' la forza di uno
                      spirito» -> l'inglese scrive «the power of a demigod»

⚠️ **E una carta dove l'inglese di monte e' PIU' CORTO**: `:7882`, il fratello
volpe, dove il giapponese ha tre frasi e l'inglese due — quella che manca e' la
battuta su 「おとおと」, un essere ancora piu' misterioso di cui si studia la
parentela. Il gioco di parole (弟 *otooto*, «fratello minore», scritto storto)
non si rende: la parola resta com'e', come `tsukumogami` e `kunoichi`.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `神の欠片` → **una scheggia di
divinita'**, `冥界` → **l'oltretomba**, `シェイド` → **l'ombra**
(`chara.hsp:2295`, e il nome シュイド e' gia' reso **l'ombrame**: la prosa di
`:8012` spiega proprio quel nome), `幻獣` → **la bestia fantastica**
(`db_creature`), `イルヴァ` → **Irva**, `魔導船` → **la nave magica**
(`chat.hsp:2133`), `エウダーナ` → **Eulderna**, `イェルス` → **Yerles**,
`精霊` → **lo spirito**, `テスカトリポカ` → **Tezcatlipoca** (lotto 15, `:7258`).

ⓘ `決戦兵器` non era mai comparso: reso **l'arma della battaglia decisiva**
(`:7687`). E `旧時代` → **il tempo antico** (`:8064`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :7609 il berrettorosso rapido
    (7609, 'They approach in the blink of an eye with frightening speed and attack with a swinging axe. After slaughtering a person they take great pleasure in using the overflowing blood to dye their hats.'):
        "Ti arriva addosso in un battito di ciglia, con una rapidità che spaventa, e ti assale roteando l'ascia. Dopo aver massacrato qualcuno, non c'è gioia più grande per lui che tingersi il berretto con il sangue che sgorga.",

    # ---------------------------------------------------------- :7622 il Camazotz
    (7622, "The Evil One of the Bats. It has large fangs and a sharp knife-shaped nose but its biggest feature is its claws which are so large and sharp that they can cut off a person's head with a single blow."):
        "Il dio malvagio dei pipistrelli. Ha zanne grandi e un naso affilato a forma di lama, ma quel che lo distingue davvero sono gli artigli: così grossi e taglienti che staccano una testa con un colpo solo.",

    # ---------------------------------------------------------- :7635 l'Osiride
    (7635, 'A demon possessing a piece of the god that once ruled the underworld. Its body is mummified and its entire body is covered with bandages. He loves his sister but hates his brother.'):
        "Un mostro che porta in sé una scheggia del dio che un tempo governava l'oltretomba. Il suo corpo è mummificato e fasciato da capo a piedi. Vuole un gran bene alla sorella e non sopporta il fratello.",

    # ---------------------------------------------------------- :7648 la Hel
    (7648, 'In the underworld she is responsible for judging those who have died of disease or old age as well as the wicked. She has a rotten lower body but more than that she has a corrupt sexual drive and on a whim she can go to earth and slaughter people.'):
        "Nell'oltretomba ha il compito di giudicare i malvagi e chi è morto di malattia o di vecchiaia. Dalla cintola in giù è tutta marcia, ma è ancora più marcia dentro: quando le gira, sale in superficie e fa strage di gente.",

    # ---------------------------------------------------------- :7661 la Nemain
    (7661, "A black-bodied divine bird. They fly around the battlefield bringing fear and frenzy to the warriors and making them strike out at each other. Surprisingly homely it washes others' blood-soaked arsenal. If a weapon is washed its owner will be killed in battle in the near future."):
        "Un uccello divino dal corpo nero. Vola sopra i campi di battaglia, porta ai guerrieri il terrore e la follia e li fa scannare fra loro. È di casa più di quanto si direbbe: lava le armi e le armature imbrattate di sangue. Ma a chi gliele fa lavare resta poco da vivere, perché cadrà presto in battaglia.",

    # ---------------------------------------------------------- :7674 l'alto incantatore
    (7674, 'He is a high-ranking wizard in Eulderna. Most of them were born with a huge amount of magical power and are looked upon with respect and awe by lower-level wizards.'):
        "Un mago di grado elevato fra quelli di Eulderna. Quasi tutti sono nati con un potere magico smisurato, e i maghi di grado inferiore li guardano con rispetto e con timore.",

    # ---------------------------------------------------------- :7687 il cannone a supergravità di Yerles
    (7687, 'It was developed as an additional armament to the decisive weapon. When connected and fired at maximum power it was found that there was a danger of the crust of Irva collapsing in the aftermath so it was reluctantly operated as a stand-alone turret.'):
        "Fu messo a punto come armamento aggiuntivo dell'arma della battaglia decisiva. Poi si scoprì che, montato e sparato alla massima potenza, il contraccolpo rischiava di sfondare la crosta di Irva: e così, obtorto collo, lo fanno funzionare da solo, come una batteria.",

    # ---------------------------------------------------------- :7700 il golem composito
    (7700, 'A rational golem made from a composite of many materials with both strength and flexibility. However there is an opinion that it is a foul play not to make it out of a single material and it has become a controversy at academic conferences.'):
        "Un golem ragionevole, fatto mettendo insieme molti materiali, che unisce la forza alla scioltezza. C'è però chi sostiene che non farlo di un materiale solo sia barare, e all'accademia ne discutono ancora.",

    # ---------------------------------------------------------- :7713 l'ulfhednar
    (7713, 'A mad warrior imp with a dog-like head. They lay down their weapons and armor and pounce on their prey fiercely like unintelligent beasts.'):
        "Un folletto berserker con la testa da cane. Butta via armi e armatura e si avventa sulla preda con la furia di una bestia senza raziocinio.",

    # ---------------------------------------------------------- :7726 il pagliaccio demoniaco
    (7726, 'A demon clown with high physical abilities. The prey is chased down and played with while the clown repeatedly says and does jokes. Many are horrified at the sight of it.'):
        "Un pagliaccio demoniaco dalle doti fisiche notevoli. Incalza la preda fino a metterla all'angolo e ci gioca, continuando a dire e a fare buffonate. A vederlo, in molti si sentono gelare.",

    # ---------------------------------------------------------- :7739 il lich antico
    (7739, 'A lich that has been taking human life and magic since ancient times. He has no memory of his life anymore because he has spent so much time in this world.'):
        "Un lich che fin dall'antichità continua a rubare agli uomini la vita e il potere magico. È passato tanto di quel tempo che di quando era vivo non gli resta più nessun ricordo.",

    # ---------------------------------------------------------- :7752 il Garuda
    (7752, 'A half-human half-bird demon with red wings. It glows like a flame and emits heat. They are often mistaken for flaming dragons or Vermilion Sparrow companions which is deeply disturbing.'):
        "Un mostro mezzo uomo e mezzo uccello, dalle ali rosse. Risplende come una fiamma ed emana calore. Lo scambiano di continuo per un parente del drago di fuoco o del passero vermiglio, e la cosa gli dà un fastidio profondo.",

    # ---------------------------------------------------------- :7765 l'arciere alato
    (7765, 'Half-man half-bird demon. It has excellent maneuverability and excels at surprise attacks from above. They have a bird-headed complex and are envious of harpies.'):
        "Un mostro mezzo uomo e mezzo uccello. Si muove benissimo ed è bravissimo a piombare addosso dall'alto quando meno te lo aspetti. Ha il complesso della testa da uccello e invidia le arpie.",

    # ---------------------------------------------------------- :7778 il golem di sangue
    (7778, 'A golem created by solidifying the blood of many demon races including the blood of the wizard himself. Even during combat the blood is transformed into a thorn and the blood is thrust into the opponent to steal their blood.'):
        "Un golem fatto solidificando il sangue di molte stirpi demoniache, a cominciare da quello del mago che lo ha creato. Anche in combattimento tramuta il sangue in spine, le conficca nell'avversario e gliene ruba dell'altro.",

    # ---------------------------------------------------------- :7791 l'occhio scrutatore
    (7791, 'A demon that continues to stare at you with an intimidating gaze. There are some ugly things to do such as taking away the eyesight of those who come at them brainwashing them and making them get down on their knees.'):
        "Un mostro che ti tiene addosso uno sguardo che mette soggezione, e non lo stacca mai. A chi gli si ribella toglie la vista, oppure gli lava il cervello e lo costringe a inginocchiarsi fino a terra: sono modi brutti.",

    # ---------------------------------------------------------- :7804 il behemot
    (7804, 'An amphibious beast. It used to symbolize gluttony but nowadays due to lack of food most of them are small and small eaters.'):
        "Una bestia che vive in acqua e sulla terra. Un tempo, a furia di mangiare e bere senza freno, era il simbolo della gola; oggi il cibo scarseggia e quasi tutti sono piccoli e di bocca parca.",

    # ---------------------------------------------------------- :7817 l'ocelome
    (7817, 'A jaguar warrior in the service of Tezcatlipoca. Even among the elite nobles with high status only the chosen ones can become a member of the Warrior Corps.'):
        "Un guerriero giaguaro al servizio di Tezcatlipoca. Perfino fra i nobili di rango alto, che stanno già in cima a tutti, solo i prescelti entrano nel corpo dei guerrieri.",

    # ---------------------------------------------------------- :7830 l'Arcturus
    (7830, 'A bear with the power of the stars in its body. The body glows orange. Its name is derived from the star which is the source of its power and it means guardian of the bear.'):
        "Un orso che porta nel corpo la forza delle stelle, e il corpo gli brilla di arancione. Il nome gli viene dalla stella da cui prende quella forza, e vuol dire il guardiano dell'orsa.",

    # ---------------------------------------------------------- :7843 lo scarabeo ercole omega
    (7843, 'It harbors the power of a demigod and is a superior being among insects. They have an aptitude for riding because of their symbiotic relationship in which they receive a small share of life energy in exchange for carrying other insects on their backs.'):
        "Porta in sé la forza di uno spirito ed è, fra gli insetti, una creatura di rango alto. Vive in simbiosi con gli altri insetti: se li carica sulla schiena e in cambio ne riceve un po' di energia vitale, e per questo è adatto a farsi cavalcare.",

    # ---------------------------------------------------------- :7856 il Vishnu
    (7856, 'A demon that possesses a piece of the god that maintains the world. The original deity before it was scattered as a fragment had the power to tread the world in three steps manipulate sunlight and so on.'):
        "Un mostro che porta in sé una scheggia del dio che tiene in piedi il mondo. Il nume di prima, quello che poi si è sparso in schegge, aveva la forza di attraversare il mondo in tre passi, di comandare la luce del sole e altro ancora.",

    # ---------------------------------------------------------- :7869 la roccia esplosiva a grappolo
    (7869, 'It is a moving rock that has the habit of sticking together as a large family. In the body of the parent the child lives in hiding and in that body the grandchild lives in hiding. When the parent rock blows up everyone blows up.'):
        "Una roccia che cammina e che ha l'abitudine di vivere ammucchiata in famiglie numerose. Dentro il corpo del genitore sta nascosto il figlio, e dentro quello del figlio il nipote. Se scoppia la roccia madre, scoppiano tutti.",

    # ---------------------------------------------------------- :7882 il fratello volpe
    (7882, "The fox's non-blooded brother-in-law. He can' t wear the hood because his fox ears are in the way."):
        "Il fratello acquisito della volpe, con cui non ha legami di sangue. Si studia ancora che parentela abbia con otooto, un essere ancora più misterioso. Le orecchie da volpe gli danno impiccio e il cappuccio non riesce a mettercelo.",

    # ---------------------------------------------------------- :7895 il grifone del miraggio
    (7895, 'A gryphon bred in Eulderna. It has the power to create and manipulate fog and mirages around it and to fire a series of spells to disorient its prey.'):
        "Un grifone allevato a Eulderna con selezioni successive. Sa creare intorno a sé nebbie e miraggi e comandarli, e in più tira una raffica di magie che stordiscono la preda.",

    # ---------------------------------------------------------- :7908 il grifone nero
    (7908, 'A rabid gryffon with a black body. It has both speed and power and the blows delivered from the high-speed rush can easily tear even machines apart.'):
        "Un grifone dal corpo nero, e feroce. Unisce la velocità alla potenza: il colpo che sferra al termine di una carica lanciata squarcia senza fatica perfino una macchina.",

    # ---------------------------------------------------------- :7921 il cucciolo di grifone
    (7921, 'A fantastic beast with the wings and upper body of an eagle or hawk and the lower body of a lion. Their fur has grown up to look more like a gryffon but they are still young and not very good at flying.'):
        "Una bestia fantastica, con le ali e il torso di aquila o di falco e le zampe posteriori di leone. Il pelo gli è ricresciuto e ormai somiglia parecchio a un grifone, ma è ancora un bambino e a volare è un disastro.",

    # ---------------------------------------------------------- :7934 <Aile> l'assistente di volo
    (7934, "A flight attendant with the blood of a demon. She is physically capable and has the top sales record for the number of hijackers eliminated. Originally a wagon attendant she was hired as a wizard ship's escort because of her fighting ability."):
        "Un'assistente di cabina con sangue demoniaco nelle vene. Ha doti fisiche notevoli e detiene il primato aziendale di dirottatori eliminati. Prima faceva la stessa cosa sui carri da trasporto, ma per come sa battersi l'hanno assunta come scorta della nave magica.",

    # ---------------------------------------------------------- :7947 il fiore mangiagiganti
    (7947, 'A giant man-eating flower that has grown abnormally. They prey by stopping the movement of their prey with tendrils that secrete a viscous fluid. As its name implies it also feeds on giants.'):
        "Un fiore mangiauomini cresciuto oltre misura. Blocca la preda con i tralci, che trasudano un liquido appiccicoso, e poi se la mangia. E come dice il nome, capita che si nutra anche di giganti.",

    # ---------------------------------------------------------- :7960 il soldato cyborg di Yerles
    (7960, 'He had been complaining for some time that the armament did not fit his body well. After hearing about it the chief of development performed an alteration surgery while he was asleep and his armament became a part of his body.'):
        "Andava dicendo da tempo che l'armamento non gli si adattava bene al corpo. Il capo dello sviluppo lo venne a sapere, lo operò mentre dormiva, e adesso l'armamento è parte del suo corpo: buon per lui.",

    # ---------------------------------------------------------- :7973 il tiranno cervo volante
    (7973, 'They contain the evil forces in their own bodies. A tyrant in the form of a guardian god of insects able to tear time and space apart and manipulate lightning. Be prepared to die if caught between those mandibles.'):
        "Tiene sigillata dentro di sé una forza malvagia. È il nume corazzato che regna sugli insetti, ed è un tiranno: squarcia lo spazio e il tempo e comanda il fulmine. Se ti stringe fra quelle mandibole, mettiti l'anima in pace.",

    # ---------------------------------------------------------- :7986 il millepiedi drago argenteo
    (7986, 'It has a mysterious body that shines white and silver and has been regarded as a good omen since ancient times. Their temper is relaxed and basically harmless but their body fluids are powerful acids.'):
        "Ha un corpo misterioso che riluce d'argento, e fin dai tempi antichi lo tengono di buon auspicio. Di carattere è tranquillo e in sostanza innocuo, ma i suoi umori sono un acido potentissimo.",

    # ---------------------------------------------------------- :7999 <Gran Maestro>
    (7999, 'The way the pieces fused together with their hearts and strength. Although its ability to control is reduced the power of its unity is neither tactical nor flawless it defeats the enemy army single-handedly.'):
        "È la forma che prendono i pezzi quando uniscono i cuori e le forze e si fondono. Il dominio del campo gli è calato, ma la forza di quell'unione non sa che farsene della tattica: falcia l'esercito nemico da sola.",

    # ---------------------------------------------------------- :8012 l'ombrame
    (8012, "A being that is a fusion of multiple shades named shadow because it is a collection of shades. The shadow of this demon can become even more shades so it's very confusing."):
        "Un essere nato dalla fusione di più ombre, e siccome è un ammasso di ombre lo hanno chiamato ombrame. La cosa si complica parecchio, perché anche l'ombra di questo mostro può farsi ombra a sua volta.",

    # ---------------------------------------------------------- :8025 l'aquila solitaria
    (8025, 'A being whose spirit has materialized in the form of an eagle. Both wings can be flapped to emit destructive light bullets. It gets tired of flying high and occasionally fly low.'):
        "Uno spirito che ha preso corpo nella forma di un'aquila. Battendo le due ali scaglia proiettili di luce che distruggono. Ogni tanto si stanca di volare alto e allora vola raso terra.",

    # ---------------------------------------------------------- :8038 l'aquila d'assalto
    (8038, 'A huge eagle that excels at attacking the ground from a steep drop. It is an endangered species because many individuals mistakenly attack small animals that are stronger than themselves only to killed.'):
        "Un'aquila enorme, che è maestra nel piombare in picchiata su quel che sta a terra. Molte però sbagliano bersaglio, si buttano su animaletti più forti di loro e ci restano: per questo è una specie a rischio di estinzione.",

    # ---------------------------------------------------------- :8051 <Leold> il braccio nero
    (8051, 'He uses a black gauntlet that covers his right arm and prefers to fight in close quarters. He is in search of something stronger and in some cases he is willing to raise a stronger person himself.'):
        "Si serve del guanto d'arme nero che gli copre il braccio destro, ed è un lottatore che ama il corpo a corpo. Va in cerca di qualcuno più forte di lui, e se serve non si tira indietro dall'allevarselo da sé.",

    # ---------------------------------------------------------- :8064 il signor Progetto
    (8064, 'A small robot for old-fashioned pest control. It is equipped with an ultra-compact jet engine developed just for this purpose. However due to the high price and low versatility sales did not increase and production was discontinued.'):
        "Un robottino del tempo antico, fatto per sterminare i parassiti. Dentro ha un motore a reazione piccolissimo, sviluppato solo per lui. Ma costava troppo e andava d'accordo con poco, le vendite non decollarono e la produzione fu chiusa.",

    # ---------------------------------------------------------- :8077 <Sarashina> il re dei parassiti
    (8077, 'A demon king of fear who controls the vermin. Toxic electromagnetic waves and pheromones can be used to summon cockroaches within a 14km radius. No insecticide will work.'):
        "Il terribile re dei demoni che comanda i parassiti. Con onde velenose e feromoni richiama a sé gli scarafaggi nel raggio di quattordici chilometri e se li mette al servizio. Non c'è insetticida che lo tocchi.",

    # ---------------------------------------------------------- :8090 lo scarafaggio assassino
    (8090, 'An abundance of insecticides radiation and ether resulted in an outrageous mutation that boosted their fighting power immunity and proliferation. Their favorite food is human flesh.'):
        "A furia di prendersi addosso insetticidi, radiazioni ed etere a piene mani è mutato in modo mostruoso: adesso combatte meglio, si ammala di meno e si moltiplica di più. Il suo piatto preferito è la carne umana.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-016.jsonl'
DA, A = 7601, 8100
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
