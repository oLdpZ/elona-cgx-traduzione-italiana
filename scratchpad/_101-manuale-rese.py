# -*- coding: utf-8 -*-
"""Le rese di `data\\manual_ENG.txt`, la guida in gioco (tasto `?`).

    python scratchpad/_101-manuale-rese.py lavoro/manual-001.jsonl

⚠️⚠️ **QUI NON SI TRADUCE UNA RIGA ALLA VOLTA.** Le righe del file sono
spezzate a mano da monte a meta' delle frasi, e ogni riga e' una chiamata a
`gmes` a se' stante: l'unita' di senso e' il **paragrafo**, l'unita' del file e'
la **riga**, e le due non coincidono. Quindi qui si scrive il paragrafo intero e
`_101-impagina.py` lo distribuisce in **esattamente** il numero di righe che il
paragrafo inglese occupa — ne' una di piu' (`dati_applica` non ne aggiunge) ne'
una di meno (una resa vuota lascia in campo l'inglese).

⭐ **Il vincolo che morde e' l'altezza della sezione**, non la larghezza della
riga: 436 px di pagina, 18 px per riga del file e 16 per ogni a capo che `gmes`
aggiunge da solo oltre i 73 caratteri. Il margine sta in
`_101-manual-gmes.py`, e la sezione piu' stretta ne ha il **19%** — l'italiano
ne chiede circa quindici. Non e' comodo dappertutto, ma ci sta.

⚠️ **Un manuale cita quel che e' a schermo** (regola della 99a): i nomi dei menu
e dei tasti si prendono dal dizionario, non si reinventano — «Menu rapido» e'
`config.hsp:759`, non una traduzione nuova.

⚠️ I marcatori `<emp1>` `<def>` `<command>` si conservano: `gmes` li mangia
senza disegnarli e senza pagarli in larghezza.
"""
import importlib.util
import io
import json
import os
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))


def _modulo(nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_QUI, nome + ".py"))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


_struttura = _modulo("_101-manuale-struttura")
_impagina = _modulo("_101-impagina")

# titolo inglese della sezione -> (titolo italiano, [paragrafi])
#
# ⚠️ Il titolo ha un tetto suo: 21 caratteri, perche' l'elenco a sinistra
# comincia a `wx + 66` e il corpo a `wx + 216` (`_101-manual-gmes.py`).
SEZIONI = {
    "(testa)": (None, [
        "Questo manuale è stato tradotto da f1r3fly, aggiornato da Aquillion e "
        "portato in italiano dal progetto di traduzione.",

        "Questo manuale si consulta dentro il gioco. Per questo, se ci trovi "
        "simboli <command> come parentesi o altri segni di contorno, non "
        "farci caso: li usa il gioco.",
    ]),

    "For Beginners": ("Per cominciare", [
        "Con i tasti come sono all'inizio, il personaggio si muove col "
        "tastierino numerico. Per correre, tieni premuto Maiusc mentre ti muovi.",

        "Nei menu, la barra spaziatrice conferma e Maiusc annulla.",

        "I menu di scelta rapida sono tre: il tasto Z apre il menu rapido, il "
        "tasto X quello degli oggetti e il tasto C quello del personaggio.",

        "Nel menu rapido si sceglie un'azione premendo la direzione "
        "corrispondente sul tastierino numerico. Nel menu degli oggetti e in "
        "quello del personaggio si cambia linguetta con 7 o 9 del tastierino.",

        "Per raccogliere un oggetto premi 0 sul tastierino numerico. Per "
        "prendere di mira una creatura, con un'arma da tiro o con una magia, "
        "premi * sul tastierino.",
    ]),

    "For Advanced Players": ("Per giocatori esperti", [
        "Ogni azione ha il suo tasto: l'elenco completo sta in <emp1>Elenco "
        "dei tasti<def>. Per esempio, per mangiare si preme il tasto E.",

        "Puoi assegnare tasti di scelta rapida a magie, abilità e oggetti da "
        "usare: metti in evidenza quello che ti serve e premi un tasto da 0 a "
        "9. Con CTRL e poi 0-9 ne aggiungi altri. Per usarli mentre giochi "
        "premi 0-9, o MAIUSC e 0-9 per quelli che hai fatto con CTRL.",

        "Per muoverti solo in diagonale, tieni premuto ALT.",
    ]),

    "Character Creation": ("Creare il personaggio", [
        "Le scelte che fai creando il personaggio contano su più cose. "
        "Razza, classe, attributi e valore iniziale delle abilità decidono "
        "l'equipaggiamento di partenza. Anche la velocità con cui "
        "un'abilità cresce dipende dal suo valore iniziale: più è alto, "
        "più in fretta quell'abilità sale.",

        "Le abilità sono tante e quasi tutte si imparano più avanti. Quelle "
        "imparate dopo la creazione crescono molto più lentamente di quelle "
        "scelte lì. Questo non vuol dire che un guerriero non possa "
        "diventare bravo con la magia: conviene partire mago se vuoi lanciare "
        "incantesimi, ma con l'esercizio anche un guerriero diventa un buon "
        "incantatore.",

        "Sesso e nome del personaggio non contano sugli attributi.",

        "La crescita degli <emp1>attributi<def> non dipende dai valori che "
        "hanno, quindi non serve spingerli al massimo alla creazione (anche "
        "se aiuta a superare l'inizio del gioco).",
    ]),

    # ⚠️ Le sigle STR/CON/DEX... non esistono a schermo in questa build: la
    # scheda del personaggio scrive i nomi per esteso (`skill.hsp:19`-`:54`).
    # Un manuale cita quel che e' a schermo, quindi qui vanno i nomi.
    "Abilities": ("Attributi", [
        "<emp1>Forza<def>: conta sugli HP massimi, sul bonus ai danni in "
        "mischia e su quanto peso riesci a portare. "
        "<emp1>Costituzione<def>: conta sugli HP massimi, sugli SP e sul peso "
        "che porti. "
        "<emp1>Destrezza<def>: conta sulla probabilità di colpire e riduce i "
        "danni che subisci. "
        "<emp1>Percezione<def>: conta sulla schivata, sul bonus ai danni da "
        "tiro e sui colpi critici. "
        "<emp1>Apprendimento<def>: conta sugli MP massimi e sul ritmo di "
        "crescita delle abilità. "
        "<emp1>Volontà<def>: conta su MP, HP e SP massimi. "
        "<emp1>Magia<def>: conta sugli MP massimi. "
        "<emp1>Carisma<def>: conta su come i PNG trattano il tuo personaggio.",

        "Gli attributi qui sopra contano anche sulle abilità, sulle magie e "
        "su certi eventi. L'attributo di una magia o di un'abilità si legge "
        "alla sinistra del nome, sotto forma di simbolo: per esempio quasi "
        "tutte le abilità con le armi hanno due spade incrociate.",

        "Ci sono anche <emp1>Vita<def>, <emp1>Mana<def>, <emp1>Velocità<def>, "
        "<emp1>Fortuna<def> e gli <emp1>SP<def>, che però non crescono come "
        "gli attributi qui sopra.",
    ]),

    "Skills": ("Abilità", [
        "Le abilità del personaggio salgono usandole, allenandole e "
        "spendendoci i punti bonus.",

        "Certe abilità consumano SP quando le usi. Quando gli SP calano "
        "arriva la stanchezza, la velocità scende e l'abilità fallisce più "
        "spesso. Riposare li recupera. Gli SP si leggono alla sinistra dei "
        "soldi.",

        "Certe abilità vogliono un oggetto per funzionare: l'Esibizione "
        "vuole uno strumento, la Cucina vuole di che cucinare e qualcosa da "
        "cuocere, la Pesca vuole una canna.",

        "Ci sono oggetti che danno un bonus a un'abilità. Lo dicono nella "
        "descrizione e portano accanto il simbolo [*]. Ogni * vale da 1 a 5 "
        "punti di quell'abilità.",
    ]),

    "Skill Gain": ("Crescita abilità", [
        "Ogni volta che usi un'abilità la sua esperienza sale, e raggiunta "
        "una certa quota l'abilità cresce di un livello. Di quanto cresce "
        "dipende dal suo ritmo di crescita. Così le abilità salgono a forza "
        "di usarle, e con loro può salire anche l'attributo collegato.",

        "In più, salendo di livello prendi HP e punti bonus, e quanti punti "
        "bonus dipende dal tuo Apprendimento. Si spendono per far salire le "
        "abilità.",

        "Nel menu del personaggio, accanto al valore di ogni abilità c'è "
        "una percentuale: è la velocità con cui quell'abilità sale "
        "usandola. Un'abilità al (200%) cresce il doppio di una al ritmo "
        "normale (100%). Il ritmo di crescita di abilità e attributi si "
        "decide creando il personaggio.",

        "Quando il valore di un'abilità sale, il suo ritmo di crescita cala. "
        "Lo si rialza con certe erbe e allenandosi nei campi di addestramento.",

        "Il valore massimo di un'abilità è 2000.",
    ]),

    "Learning Skills": ("Imparare abilità", [
        "Per imparare abilità nuove parla con l'istruttore di una città "
        "qualunque. In cambio vogliono monete di platino, sia per insegnarti "
        "un'abilità nuova sia per potenziarne una che hai già.",

        "Quante monete di platino servano cambia secondo l'abilità e secondo "
        "il valore a cui vuoi portarla.",
    ]),

    "Magic": ("Magia", [
        "Per usare la magia devi prima imparare gli incantesimi dai grimori.",

        "Che tu riesca a impararlo dipende dalla potenza dell'incantesimo e "
        "dai tuoi attributi di <emp1>Apprendimento<def> e <emp1>Magia<def>. "
        "Puoi provarci anche con valori bassi, ma può finire male.",

        "Quando finisci di leggere un grimorio, la scorta che hai di "
        "quell'incantesimo sale. Ogni volta che lo lanci la scorta cala del "
        "mana che l'incantesimo costa: per esempio, con 5 di scorta in un "
        "incantesimo che costa 5 di mana lo lanci una volta sola, perché "
        "lanciarlo esaurisce la scorta. Per averne ancora bisogna rileggere "
        "il libro.",

        "L'abilità di magia cresce lanciando incantesimi, ma per rifare "
        "scorta bisogna sempre rileggere i grimori. (???)",
    ]),

    # ⚠️ L'inglese di monte qui dice una cosa che il gioco non fa: «resistance
    # to nerve paralysis reduces your chance of being paralyzed». Nel gioco i
    # nervi tengono il **sonno** e la paralisi sta sotto fulmine
    # (`skill.hsp:81` e `:111`). Il manuale cita quel che e' a schermo, quindi
    # qui va la coppia giusta. Per esteso in `decisioni.md` §101a.
    "Resistance": ("Resistenze", [
        "La resistenza dice quanto reggi un certo tipo di attacco. Se ti "
        "colpisce un danno a cui resisti, quel danno cala di molto. Aiuta "
        "anche contro gli stati alterati: per esempio la resistenza a "
        "oscurità riduce la probabilità di essere accecato, quella ai nervi "
        "riduce quella di addormentarti, e così via. Se resisti molto alla "
        "magia, ci vuole una maledizione più potente per maledirti.",

        "Le resistenze si alzano soprattutto con l'equipaggiamento, ma ci "
        "sono anche talenti che le aumentano.",
    ]),

    "Feats & Mutations": ("Talenti e mutazioni", [
        "Andando all'avventura può capitare che il personaggio cambi, in "
        "bene o in male. I cambiamenti utili sono i talenti, quelli dannosi "
        "le mutazioni.",

        "Se non è una mutazione speciale si può curare, di solito con una "
        "medicina di cura della mutazione.",

        "Un talento, una volta preso, è per sempre. Se ne prendono creando "
        "il personaggio e salendo di livello.",
    ]),

    "Curses & Blessings": ("Maledetto o benedetto", [
        "Sia gli oggetti sia le creature possono essere maledetti o benedetti.",

        "Un oggetto benedetto dà +1 al danno se è un'arma e +2 al PV se è "
        "una protezione. Gli oggetti maledetti danno effetti cattivi di vario "
        "genere. La maledizione si toglie con una pergamena di purificazione.",

        "Sulle creature, benedizioni e maledizioni durano un tempo fissato. "
        "Una maledizione può abbassare la difesa o intralciare gli "
        "incantesimi; una benedizione fa l'opposto, dà forza o fa recuperare "
        "MP più in fretta.",

        "Mentre sei benedetto o maledetto, in basso a destra compare "
        "un'icona. Il numero sull'icona dice quante mosse dura ancora.",
    ]),

    # ⚠️ Questa sezione sfonda la pagina **gia' in inglese** — 32 righe per 624
    # px su 436 — e non c'e' resa che la aggiusti: l'altezza la fa il **numero
    # di righe**, che e' fisso. L'unica cosa che qui dipende da noi e' non
    # peggiorarla, cioe' tenere ogni riga sotto i 73 caratteri.
    "Abnormal States": ("Stati alterati", [
        "Andando all'avventura ti capiteranno molti stati alterati.",

        "Quando ne subisci uno, in basso a sinistra compare un'icona che resta "
        "finché lo stato non passa; quanto duri non si sa.",

        "Ecco i più comuni:",

        [
            "Esitazione: aumenta i danni che subisci.",
            "Tremore: riduce i danni che fai.",
            "Paralisi: hai una probabilità su due di non riuscire ad agire.",
            "Cecità: non vedi quel che ti sta intorno e non prendi la mira.",
            "Terrore: non riesci a muoverti e la barra della carica cala.",
            "Veleno: subisci danni a ogni turno.",
            "Erosione: gli MP calano a ogni turno. Recuperare MP accorcia la",
            "durata dell'effetto.",
            "Stordimento: ti muovi in modo incerto e sei più esposto ai colpi",
            "in mischia.",
            "Sonno: non puoi agire, e a svegliarti è un colpo che ti fa danno.",
            "Confusione: ti muovi in modo incerto e lanciare incantesimi",
            "diventa più difficile.",
            "Ubriachezza: ti muovi in modo incerto, ma resisti di più alla",
            "follia.",
            "Plagio: l'equipaggiamento ti viene tolto a caso e finché dura non",
            "puoi rimetterlo.",
            "Un alleato plagiato ti attacca per un massimo di trenta turni.",
            "Vincolo: non puoi muoverti né schivare, e gli SP calano.",
        ],

        "Molti stati alterati si curano con una magia o con una pozione.",
    ]),

    "Weapons & Armor (1)": ("Armi e armature (1)", [
        "Il valore numerico si legge in fondo al nome di un'arma o di "
        "un'armatura.",

        "In un guanto di ferro (1,2) [3,4], il (1,2) è il bonus al colpire e "
        "quello ai danni, mentre il [3,4] è il bonus a DV e PV che dà quando "
        "lo indossi. Per saperne di più c'è la sezione <emp1>DV, PV e "
        "altro<def>.",

        "In una spada di ferro (3d4+5) (6), il 3d4 vuol dire tre dadi da "
        "quattro facce, cioè un danno base che arriva a 12. Il +5 è un bonus "
        "ai danni, il (6) è un bonus al colpire, e valgono soltanto quando "
        "attacchi con quell'arma.",
    ]),

    "Weapons & Armor (2)": ("Armi e armature (2)", [
        "Quando un'arma o una protezione viene potenziata, in fondo al nome "
        "compare un +1, un +2 o più.",

        "Sulle armi, ogni punto in più di quel valore vale +1 ai danni.",

        "Un'arma benedetta ha +1 ai danni.",

        "Sulle armature, ogni punto in più di quel valore alza il PV di 2.",

        "Un'armatura benedetta ha +2 al PV.",

        "C'è anche equipaggiamento che alza gli attributi o le resistenze: lo "
        "verifichi esaminando l'oggetto col tasto X.",

        "Le armi con una percentuale di perforazione ignorano quella parte "
        "dell'armatura nemica: al 60% ne ignorano il 60%.",
    ]),

    "Fighting Styles": ("Modi di combattere", [
        "Con lo scudo: se porti uno scudo puoi usare una sola arma, ma prendi "
        "un bonus a PV e DV secondo quanto sei bravo con lo Scudo.",

        "A due mani: impugnando l'arma a due mani, il bonus al colpire e "
        "quello ai danni salgono un poco. Se l'arma è fatta per le due mani e "
        "sei bravo con l'abilità Due mani, salgono parecchio di più.",

        "Con due armi: impugnandone due rendi di più se metti la più pesante "
        "nella mano principale, quella in alto, e la più leggera nell'altra. "
        "Prendi una penalità al colpire che dipende dal peso delle armi e "
        "dalla tua abilità Doppia arma.",
    ]),

    # ⚠️ Il paragrafo e' UNO SOLO di 22 righe e dentro c'e' una **tabella a
    # colonne fisse**: reimpaginarlo la distruggerebbe. Per questo le righe
    # sono scritte a mano. La colonna dei nomi passa da 11 a 20 caratteri
    # perche' «fucile di precisione» non ci sta in undici, e le cifre restano
    # incolonnate perche' cominciano tutte due caratteri dopo la colonna.
    "Ranged Weapons": ("Armi da tiro", [
        [
            "La gittata utile cambia da un'arma da tiro all'altra. Di norma,",
            "più il bersaglio è lontano, più è difficile colpirlo e meno danno",
            "gli fai. Qui sotto ci sono la gittata massima e il danno secondo",
            "la distanza.",
            "Arma  distanza        1  2  3  4  5  6  7",
            "------------------------------------------",
            "      fucile a pompa  20-20-10-05-05-05-05",
            "            balestra  15-15-10-10-10-05-05",
            "          arco corto  10-15-15-10-10-05-05",
            "      mitragliatrice  10-10-15-15-10-05-05",
            "      arco di teschi  05-10-10-15-15-10-05",
            "    pistola a fotoni  10-10-10-10-10-10-10",
            "             pistola  15-15-15-10-05-05-05",
            "              lancio  10-15-15-15-05-05-05",
            "          arco lungo  05-05-15-15-15-10-05",
            "fucile di precisione  05-05-10-15-15-15-05",
            "------------------------------------------",
            "Per esempio, a distanza 1 - il nemico ti è accanto - con un arco",
            "lungo il modificatore dell'arma è 05, cioè il 50%. A sei caselle",
            "di distanza diventa 10, cioè il 100% del tuo colpire base. Con",
            "l'arco lungo, quindi, conviene stare lontano: la distanza si",
            "legge col comando di osservazione, il tasto L.",
        ],
    ]),

    # ⚠️ La scheda di QUESTA build non dice «Melee1, Melee2, Dist» come
    # l'inglese del manuale: dice **Arma**, **Lotta** e **Tiro**
    # (`command.hsp:12402`, `:12408`, `:12414`). Un manuale cita quel che e' a
    # schermo. Per esteso in `decisioni.md` §101a.
    "DV, PV & More": ("DV, PV e altro", [
        "DV (valore di difesa): più è alto, più schivi. Conta sulla Schivata, "
        "che si legge nella scheda del personaggio.",

        "PV (valore di protezione): più è alto, meno danni subisci. Conta "
        "sulla percentuale di protezione, che si legge nella scheda del "
        "personaggio.",

        "Mira: è la percentuale con cui vai a segno. Più è alta, più spesso "
        "colpisci il bersaglio. Sta nella scheda, alla destra dei tiri di "
        "Arma, Lotta e Tiro.",

        "Tiro di danno: è quanto danno fanno le armi che impugni. Si scrive "
        "xdy, dove x è il numero dei dadi e y il numero delle facce: 2d5 sono "
        "due dadi da cinque facce. Sta nella scheda, accanto ad Arma, Lotta e "
        "Tiro.",

        "Moltiplicatore di danno: è di quanto viene moltiplicato il danno che "
        "fai a una creatura, per esempio x2,0. Dipende da quanto sei bravo "
        "con quell'arma e dai tuoi attributi. Nella scheda sta subito dopo i "
        "tiri di danno.",
    ]),

    "Equipment Weight": ("Peso equipaggiato", [
        "Le armature sono di tre tipi: leggera, media e pesante.",

        "Quando le indossi, il loro peso e quello delle armi che impugni "
        "entrano nel peso totale che il personaggio si porta addosso.",

        "Il tipo di armatura conta direttamente sulla riuscita degli "
        "incantesimi: più l'armatura è pesante, più è difficile che un "
        "incantesimo riesca.",

        "Con l'armatura media o pesante la probabilità di riuscita si alza "
        "se sei bravo con l'abilità che le riguarda - Maglia e Corazza - ma "
        "resta comunque più bassa di quella di chi porta l'armatura leggera.",
    ]),

    "Meals": ("I pasti", [
        "In Elonia il cibo serve a sopravvivere: mangiare ogni tanto è "
        "l'unico modo di evitare i guai della fame.",

        "Più fame hai, più la velocità cala. Se continui a non mangiare, "
        "prima o poi il personaggio muore di inedia.",

        "Oltre a riempire la pancia, il cibo conta anche sulla crescita del "
        "personaggio: per esempio la carne aiuta gli attributi fisici e la "
        "verdura quelli mentali, mentre le erbe alzano il ritmo di crescita "
        "delle abilità. (???)",

        "Se il cibo è cucinato, l'effetto buono può crescere secondo quanto "
        "bene è riuscita la cottura e secondo quanto è fresco. (???)",

        "Puoi anche mangiare la carne delle creature che uccidi, e lì "
        "l'effetto cambia secondo il mostro da cui viene: certa carne ti fa "
        "male, certa altra dà tolleranze o altri effetti utili.",

        "Se hai un carretto con dentro del cibo, il personaggio ci mangia da "
        "sé ogni volta che gli viene fame mentre viaggia sulla mappa del mondo.",
    ]),

    # ⚠️ «Divinità» e non «Dèi»: `degrada()` porta l'accento sull'apostrofo e
    # «De'i» non e' una parola. E' la regola della 64a vista dal lato del
    # titolo, dove non c'e' spazio per rimediare.
    "Gods & Faith": ("Divinità e fede", [
        "Andando all'avventura può capitarti di trovare l'altare di una "
        "divinità. All'altare puoi pregare il dio a cui appartiene e alzare "
        "così la tua fede verso di lui. Attenzione però: se preghi un dio "
        "diverso, fai arrabbiare quello che avevi cominciato a venerare.",

        "Stare in buoni rapporti col tuo dio ti frutta anche bonus agli "
        "attributi, alle abilità e ai poteri speciali. Che cosa ti dia il "
        "culto cambia da un dio all'altro.",
    ]),

    "Offerings & Prayer": ("Offerte e preghiera", [
        "Se veneri un dio puoi pregarlo, e può concederti una guarigione "
        "completa; ma ci vuole una certa quantità di <emp1>fede<def>.",

        "La fede si guadagna facendo offerte al tuo dio, e quanta ne prendi "
        "dipende dal tipo e dal valore dell'oggetto. Il massimo di fede che "
        "puoi avere lo decide la tua abilità Fede, che sale a forza di "
        "offerte e di preghiere.",
    ]),

    "Rest & Sleep": ("Riposo e sonno", [
        "Quando hai perso HP e MP puoi recuperarli più in fretta riposando "
        "col tasto R. Attento che mentre riposi il tempo avanza da solo. "
        "Oltre a HP e MP, riposando smaltisci anche la stanchezza.",

        "Ogni tanto devi anche dormire, e che sia ora lo dice un'icona in "
        "basso a sinistra dello schermo. Più il personaggio è stanco, più la "
        "stanchezza si accumula e più la rigenerazione naturale di HP e MP "
        "viene penalizzata.",

        "Per dormire usa un sacco a pelo o un letto quando in basso a "
        "sinistra compare Sonnolenza o il bisogno di dormire. Si dorme anche "
        "riposando, quando il sonno è arrivato.",

        "Dormendo puoi prendere bonus in base al tuo livello di esperienza, e "
        "possono essere attributi, abilità, magie e altro ancora. Cerca però "
        "di dormire in un giaciglio: chi dorme senza prende solo metà del "
        "solito.",
    ]),

    "Weather": ("Il tempo che fa", [
        "Pioggia, neve e vento d'etere ostacolano chi viaggia per Elona. La "
        "pioggia porta stati alterati che ti rallentano, ma la velocità di "
        "viaggio non cambia. Con la neve, invece, ti muovi tre volte più "
        "lentamente: attento a viaggiare con questo tempo, perché le ore "
        "corrono più in fretta.",

        "Durante una tempesta di vento d'etere succedono parecchie cose. I "
        "mostri mutano per effetto dell'etere magico e diventano molto più "
        "forti di prima. Anche tu puoi mutare: l'effetto è immediato e può "
        "farti bene come male.",

        "Per non subire il vento d'etere devi lasciare l'aperto e trovare un "
        "riparo al chiuso. Puoi farti portare in un <emp1>rifugio<def> "
        "parlando con l'oste di una locanda, oppure entrare nel tuo se ne hai "
        "uno. Dentro il rifugio, mentre riposi, il tempo passa velocissimo, e "
        "di cibo ce n'è in abbondanza: delle scorte non ti devi preoccupare.",

        "Puoi ripararti anche in casa tua o in un sotterraneo, ma lì il tempo "
        "passa al ritmo normale e la tempesta può metterci un bel po'.",
    ]),

    "Ether Exposure": ("Esposizione all'etere", [
        "Stare a lungo nel vento d'etere prima o poi ti fa venire una "
        "malattia dell'etere. La malattia avanza in venti stadi, e via via ti "
        "attacca addosso caratteristiche di malattia o di mutazione, che si "
        "leggono nella linguetta dei talenti della scheda del personaggio. "
        "Certi oggetti e gli attacchi di certe creature la fanno avanzare più "
        "in fretta. Questi effetti si curano con la magia.",
    ]),

    "Companions": ("Alleati", [
        "La prima volta che entri in una città puoi scegliere il tuo primo "
        "alleato. Con lui interagisci premendo il tasto I.",

        "Dal menu di interazione puoi parlargli, rimandarlo in città, "
        "abbandonarlo e altro ancora, e puoi anche scambiarci oggetti.",

        "Se il tuo alleato viene rimandato in città o muore, parla col "
        "barista di una città qualunque e, pagando, te lo riporta.",

        "Gli alleati crescono come te: prendono attributi e abilità a forza "
        "di ripetere, e anche quello che mangiano conta. Di fame non muoiono, "
        "ma se vuoi rinforzarli conviene dargli da mangiare ogni tanto.",
    ]),

    "Investment": ("Investire", [
        "Se te lo puoi permettere, puoi investire monete nei negozi. "
        "Investendo alzi il livello del negozio, che così tiene più merce e "
        "di qualità migliore. Investire costa parecchio: scegli bene dove "
        "mettere i soldi.",
    ]),

    "Identification": ("Identificazione", [
        "Viaggiando troverai molti oggetti da identificare per scoprire che "
        "cosa nascondono. L'identificazione si può fare in più modi.",

        "Puoi farti un'idea della qualità semplicemente portando l'oggetto "
        "nello zaino per un po', finché non ti viene il sospetto di quanto "
        "valga: te lo dice il nome (scadente, buono, eccellente e così via).",

        "Puoi far identificare gli oggetti dal mago di una città: a pagamento "
        "ti <emp1>identifica<def> un oggetto solo, oppure tutti quelli non "
        "identificati che porti. Se l'oggetto è potente o il mago non lo è "
        "abbastanza, può servire un esame più a fondo: quello costa di più, "
        "si fa su un oggetto alla volta e si chiede facendo "
        "<emp1>esaminare<def> l'oggetto al mago.",

        "Gli oggetti si identificano anche con la magia.",
    ]),

    "Death": ("La morte", [
        "Muori quando gli HP scendono sotto zero. Non perdi né gli oggetti né "
        "i soldi, ma se muori col Segno letale addosso i tuoi attributi "
        "calano per sempre.",

        "Il punteggio scende a un decimo ogni volta che muori: se non stai "
        "puntando al record, non è un gran danno.",
    ]),

    "Owning Buildings": ("I tuoi edifici", [
        "In Elona si possono possedere edifici di ogni genere. Per farlo "
        "compra un atto di proprietà in un negozio: se ne trovano parecchi "
        "all'Ambasciata, a nord di Palmia. Con l'atto in mano vai sulla mappa "
        "del mondo e leggilo stando sulla casella dove vuoi che l'edificio "
        "nasca.",

        "Di edifici ce n'è di più tipi, e quale sia lo dice il nome "
        "sull'atto. Un magazzino dà spazio per tenere tanta roba, un "
        "allevamento produce cibo in quantità, e si può piazzare anche un "
        "negozio. Per vincere non servono, ma usati bene aiutano parecchio "
        "qualunque avventuriero.",

        "Per far rendere di più gli edifici che producono, puoi metterci a "
        "lavorare degli alleati: un negozio, per esempio, ha bisogno di un "
        "commesso, e puoi lasciarcelo mentre tu continui l'avventura. Attento "
        "però che gli alleati al lavoro contano lo stesso nel numero totale "
        "dei tuoi alleati.",
    ]),

    "Auto-turn": ("Turni automatici", [
        "Il gioco salta i tuoi turni da solo quando non puoi agire di "
        "persona: mentre mangi, scavi, dormi, sei paralizzato e così via. "
        "Durante questi turni automatici il tempo corre più in fretta: "
        "dormire richiederebbe moltissimi turni, e invece con i turni "
        "automatici ci vuole poco.",
    ]),

    "Spot Sampling": ("Punti di raccolta", [
        "Sia sulla mappa locale sia su quella del mondo possono comparire "
        "punti di raccolta, e nascono a caso. Quando ci sei sopra, premi S o "
        "la barra spaziatrice per prenderne le <emp1>materie<def>.",

        "Ogni tipo di punto di raccolta ha un'abilità collegata: più sei "
        "bravo con quella, più è probabile che tu riesca a cavarne materie.",
    ]),

    "Materials & Crafting": ("Materie e artigianato", [
        "In Elona le materie sono tante. Quelle che trovi cercando, negli "
        "eventi casuali e nei punti di raccolta servono a produrre e ai "
        "minigiochi, e molte abilità di produzione le usano per fare oggetti.",

        "Le materie non si comprano e non si vendono, e non pesano niente. "
        "Per vedere quelle che hai, premi il tasto M.",

        "Per produrre oggetti usa lo strumento dell'abilità di produzione che "
        "ti serve. Ti compare l'elenco degli oggetti che puoi fare e, sotto, "
        "che cosa serve per ognuno. Se le materie in fondo alla finestra sono "
        "scritte in blu, ne hai abbastanza.",
    ]),

    "The World Map": ("La mappa del mondo", [
        "Viaggiando sulla mappa del mondo il tempo passa più di dieci volte "
        "più in fretta che sulla mappa locale. Cerca di fare strade corte: "
        "tagliare gli angoli risparmia ore, e su un viaggio lungo perfino "
        "giorni. Meno tempo di viaggio, meno cibo ti serve; e se il cibo "
        "finisce si patisce la fame.",

        "Per entrare nella mappa locale premi la barra spaziatrice: entri in "
        "quello che c'è sulla casella dove ti trovi, foresta, grotta, città e "
        "così via. Sulla mappa del mondo puoi anche raccogliere materie. "
        "Attento che certi oggetti si usano solo nella mappa locale.",

        "Mentre viaggi sulla mappa del mondo succedono eventi. Se ti tendono "
        "un'imboscata, più sei lontano da una città più i nemici sono forti. "
        "Se invece viaggi su una strada maestra, la forza dei nemici e la "
        "probabilità di incontrarli calano parecchio.",
    ]),

    # ⚠️ «la grotta dei cuccioli» e' una resa NUOVA: il nome di quella mappa
    # sta in `map_user.hsp`, che e' uno dei dodici file con `lang()` e senza
    # dizionario, quindi a schermo oggi e' ancora inglese. Il giorno che quel
    # file si apre, il nome deve combaciare — le parole vengono da
    # `text.hsp:50` («grotta») e `action.hsp:18214` («il cucciolo di cane»).
    "Saved Maps": ("Mappe salvate", [
        "Secondo il tipo di mappa locale - sotterraneo, città, zona casuale e "
        "così via - la mappa resta sempre la stessa, come nelle città e negli "
        "edifici che hai piazzato, oppure cambia ogni volta che ci entri, "
        "come la grotta dei cuccioli.",

        "Negli edifici tuoi puoi lasciare gli oggetti, ma se li lasci in una "
        "città è probabile che al ritorno non ci siano più. Gli artefatti "
        "lasciati in città spariscono, ma vengono generati di nuovo altrove.",
    ]),

    "Random Areas": ("Zone casuali", [
        "Col tempo, sulla mappa del mondo compaiono a caso zone come foreste, "
        "grotte, forti, torri e altro ancora: sono i sotterranei principali, "
        "generati a caso. In fondo c'è un signore, un nemico potente, che "
        "battuto lascia bottino e medagliette migliori.",

        "Prima di entrare in una zona casuale, accanto al nome ne vedi il "
        "pericolo all'incirca. È la forza stimata dei nemici al piano "
        "d'ingresso, e scendendo diventano più forti. Se il pericolo è pari o "
        "superiore al tuo livello, conviene tornarci quando sarai più forte.",
    ]),

    "Requests": ("Incarichi", [
        "Gli incarichi sono missioni secondarie: portandole a termine la tua "
        "fama sale, e di quanto dipende dalla difficoltà. Per accettarne uno "
        "puoi parlare col PNG che lo propone, oppure andare alla bacheca "
        "della città, dove sono elencati quelli di tutti gli abitanti.",

        "Ogni incarico ha un tempo massimo: qualcuno poche ore, qualcun altro "
        "qualche settimana. Se non lo risolvi entro quel tempo, fallisci. In "
        "bacheca il tempo sta fra parentesi; il PNG che te lo affida te lo "
        "dice a voce.",

        "Anche la difficoltà sta in bacheca, sotto forma di <emp1>$ "
        "colorati<def>, da un solo <emp1>$<def> verde fino a più "
        "<emp1>$<def> rossi. Più la difficoltà è alta, più il tempo è corto, "
        "più il compito è duro e più il premio è ricco. Attento ad accettare "
        "incarichi che non sei sicuro di finire: la fama può calare di "
        "parecchio, e ci si può perfino ritrovare criminali!",
    ]),

    "Trade": ("Commercio", [
        "La merce da commercio si compra dal mercante che sta in ogni "
        "taverna. I prezzi cambiano da una città all'altra secondo la domanda "
        "e l'offerta, e si fanno bei guadagni vendendo molta merce a una "
        "città che ne ha bisogno. Quando la compri - la riconosci perché nel "
        "nome c'è la parola carico - la merce va nel carretto, che serve solo "
        "a quello. Quel che sta nel carretto non ti pesa addosso, ma dentro i "
        "sotterranei non lo puoi usare. Per vedere che cosa c'è nel carretto, "
        "guarda la scheda del personaggio.",
    ]),

    "Adventurers": ("Avventurieri", [
        "Nel Tyris del Nord vivono e lavorano molti altri avventurieri: con "
        "loro puoi chiacchierare, e puoi comprare e vendere oggetti.",
    ]),

    "Fame & Karma": ("Fama e karma", [
        "La fama dice quanto sei conosciuto come avventuriero per le terre di "
        "Elona. Più è alta, più gli incarichi dei PNG sono difficili e, di "
        "conseguenza, più rendono.",

        "Il karma misura la tua condotta. Quando fai cose buone - portare a "
        "termine incarichi, restituire portafogli e così via - sale; se ne "
        "fai di cattive, come rubare o fallire un incarico, cala. Attento: se "
        "il karma scende troppo diventi un criminale, e le guardie ti "
        "attaccano!",
    ]),

    "Rank & Salary": ("Grado e stipendio", [
        "Di gradi ce n'è di più tipi: quello nell'arena, quello nell'arena "
        "delle bestie e quello di avventuriero, e si leggono tutti nel tuo "
        "<emp1>diario<def>. A farli salire sono azioni precise, come vincere "
        "nell'arena da concorrente o da addestratore, oppure conquistare un "
        "sotterraneo.",

        "Man mano che i gradi salgono ottieni titoli diversi, e con i titoli "
        "cresce lo stipendio.",

        "Il primo e il quindici di ogni mese è giorno di paga: ti arrivano "
        "oro e roba secondo il grado e i titoli. Ti arriva però anche una "
        "fattura, per la tassa sulla proprietà e per vari altri servizi "
        "legati alle terre che possiedi. Per pagarla prendi la fattura dal "
        "baule degli stipendi e portala all'Ambasciata a nord di Palmia: lì "
        "apri la cassetta delle tasse e mettila dentro. Bada di avere "
        "abbastanza oro nello zaino, o non riuscirai a pagare.",
    ]),

    "Marriage & Genes": ("Matrimonio e geni", [
        "Quando l'amicizia con un alleato arriva a un certo punto, potete "
        "sposarvi. Da sposati, tu e chi hai sposato potete creare un gene: "
        "basta scegliere la voce di dialogo che lo propone quando ti viene "
        "sonno.",

        "Quando hai un gene puoi ricominciare nei panni di tuo figlio, "
        "ereditando l'equipaggiamento del personaggio di adesso e qualche "
        "bonus. Se ne parla nella sezione <emp1>Eredità<def>.",

        "L'amicizia con un alleato cresce combattendo insieme a lui e "
        "regalandogli anelli nuziali e collane.",
    ]),

    "Transition": ("Eredità", [
        "Se hai un gene da parte, vai al menu del titolo e scegli di "
        "ereditare: crei un personaggio nuovo che parte con i beni ereditati "
        "dal precedente e con qualche bonus. Per reclamare gli oggetti "
        "ereditati serve un diritto d'eredità, e gli oggetti si prendono "
        "dalla borsa dell'erede, nella casa di partenza.",
    ]),

    # ⚠️⚠️ **QUI LE PAROLE SONO CHIAVI CHE IL GIOCATORE SCRIVE**, come nel
    # modello della raccolta automatica (100a), e vanno citate per quel che il
    # codice confronta davvero:
    #   `command.hsp:4336` e `:4840` cercano `lang("スキル", "skill")`, che il
    #   dizionario rende **`abilita`** — senza accento, perche' una chiave
    #   accentata non si scriverebbe mai uguale;
    #   `command.hsp:4726` confronta `"友達" | "friend" | "company" | "ally"`,
    #   **letterali nudi fuori da ogni `lang()`**: in italiano restano quelli.
    # ⚠️ E l'inglese di monte qui sbaglia: dice di scrivere «companion», che in
    # quell'elenco **non c'e'**. Per esteso in `decisioni.md` §101a.
    "Wishes": ("Desideri", [
        "In casi rarissimi ti può capitare l'occasione di esprimere un "
        "desiderio: lo capisci perché compare una riga da scrivere che ti "
        "chiede che cosa desideri. Scrivi quello che vuoi ottenere, il nome "
        "di un oggetto, di un'abilità o di un alleato; e bada di scrivere il "
        "nome esatto, o non otterrai niente!",

        "Se vuoi un'abilità, scrivi abilita e poi il nome dell'abilità: per "
        "esempio abilita tattica. Quando c'è la parola abilita, il gioco "
        "cerca prima nell'elenco delle abilità e poi in quello degli oggetti.",

        "Se vuoi un alleato, scrivi ally, friend o company.",
    ]),

    "Troubleshooting": ("Problemi comuni", [
        "D: Il tastierino numerico non fa niente. R: Può succedere se tieni "
        "premuto Maiusc mentre lo usi. Capita spesso a chi ha il Bloc Num "
        "acceso: giocando, tienilo spento.",

        "D: Che cosa sono questi oggetti in quantità 0? R: La zona ha un "
        "difetto; se riesci a capirne la causa, segnalalo. Per rimettere a "
        "posto il conteggio, prova a posare l'oggetto e a riprenderlo.",

        "D: Sono bloccato nella sala d'esposizione. R: Premi F12 per aprire "
        "la console e scrivi <emp1>exitroom<def>.",
    ]),

    "Tips (1)": ("Consigli (1)", [
        "Puoi <emp1>usare<def> i gashapon e le macchine del casinò, e tanti "
        "altri oggetti. Quando ne incontri uno che non conosci, prova il "
        "comando di uso.",

        "Come insegna il tutorial, la barra spaziatrice è un tasto utilissimo.",

        "Per pescare devi stare sulla riva, e ti serve anche l'esca: "
        "<emp1>mescola<def> l'esca con la canna da pesca.",

        "Se un nemico ha addosso un artefatto, lo lascia cadere quando muore.",

        "Se usi il comando <emp1>mescola<def> su un pozzo, prima o poi riesci "
        "a riempirlo e a usarlo di nuovo.",

        "I resti delle creature - pelli, cuori e così via - si vendono bene "
        "nei negozi.",

        "La riuscita delle abilità di artigianato e di esibizione dipende "
        "dalla qualità e dalla materia degli strumenti che usi.",
    ]),

    "Tips (2)": ("Consigli (2)", [
        "I risultati dell'arena si salvano a parte in ogni città che ne ha una.",

        "I PNG importanti, come i cittadini e i negozianti, tornano in vita "
        "dopo un tempo fissato.",

        "Non esiste un tasto per suicidarsi.",

        "La riduzione del danno di Opatos è del 10%, a parte quella del PV.",

        "I bonus di resistenza dell'equipaggiamento che li dà si sommano. Ma "
        "la somma che leggi può sembrare strana, perché un solo [*] vale in "
        "realtà da 1 a 5: per esempio *(2)+**(5+2) = **(5+4).",

        "Sfonda gli alberi da frutto per farne cadere i frutti.",

        "Un oggetto benedetto è sempre meglio, di qualunque tipo sia.",

        "Avere più di un museo non serve a niente.",

        "Se fallisci un incarico di consegna, perdi un mucchio di karma.",
    ]),

    # ⚠️ Il file delle ultime parole si chiama `lastwords-e.txt`, non
    # `lastwords.txt` come dice l'inglese di monte: e' `text.hsp:465`, ed e' un
    # nome di file **che il giocatore deve scrivere sul disco**, quindi va
    # citato esatto. Quarto scarto fra il manuale e il gioco: `decisioni.md` §101a.
    "Tips (3)": ("Consigli (3)", [
        "Gli effetti delle armi che alzano il potere magico non si sommano: "
        "vale il più alto.",

        "Appiccare incendi per le strade e nei boschi è severamente vietato. "
        "Se scoppia un incendio, scappa subito e torna dopo che ha piovuto.",

        "Le coperte possono proteggere l'equipaggiamento da certi effetti "
        "rovinosi, ma quando lo fanno rischiano di andare distrutte.",

        "La forza di una pozione lanciata dipende dalla tua Forza e dal Lancio.",

        "Il borseggio riesce più spesso fra le sette di sera e le sette del "
        "mattino, e chi dorme non si accorge di quello che fai.",

        "Si possono aggiungere ultime parole a caso nel file lastwords-e.txt.",

        "Dicono che le terme di Lana guariscano perfino la follia.",

        "Dai geni umani, con la macchina genetica, non si ottengono parti del "
        "corpo.",
    ]),

    # ⓘ I comandi della console restano in inglese: sono parole che il
    # giocatore **scrive**, e il codice le confronta tal quali.
    "Console": ("Console", [
        "Per aprire la console non devi avere finestre di gioco aperte: "
        "premi F12. Serve soprattutto a scovare difetti, specie quando in "
        "gioco non riesci più a fare niente. I comandi principali sono questi:",

        "<emp1>wizard<def> accende la modalità mago. Una volta che il "
        "personaggio ci è entrato, non si torna indietro.",

        "<emp1>freemove<def> sulla mappa del mondo ti fa spostare dovunque. "
        "Se però entri in un edificio, tocca riavviare.",

        "<emp1>exitroom<def> ti tira fuori dalla sala d'esposizione.",

        "<emp1>removequest<def> chiude tutti gli incarichi che hai.",
    ]),

    "Credits": ("Ringraziamenti", [
        "Grazie di cuore a f1r3fly, che ha tradotto questo manuale.",

        "Grazie di cuore a Brad, che mi ha mandato liste di correzioni "
        "all'inglese.",

        "Grazie di cuore ad Aquillion, che ha aggiornato il manuale di f1r3fly.",

        "Grazie di cuore a Sunstrike, che ha tradotto i dialoghi degli "
        "incarichi.",

        "Grazie di cuore a Lord Nightmare, che ha tradotto il testo del gioco.",

        "Grazie di cuore a Schmidt, che ha tradotto i libri del gioco.",

        "Grazie a tutti gli altri che hanno trovato e segnalato difetti nei "
        "forum.",

        "Quasi tutta la grafica e quasi tutti i suoni di Elona sono materiale "
        "libero: un grazie caloroso agli autori di tutto quello che è stato "
        "usato.",
    ]),
}


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]
    per_numero = {v["riga"]: v for v in voci}
    struttura = _struttura.sezioni()

    fatte = righe = 0
    for inglese, (italiano, paragrafi) in SEZIONI.items():
        if inglese not in struttura:
            raise SystemExit(f"sezione ignota: {inglese!r}")
        sezione = struttura[inglese]

        if len(paragrafi) != len(sezione["paragrafi"]):
            raise SystemExit(
                f"{inglese}: {len(paragrafi)} paragrafi italiani contro "
                f"{len(sezione['paragrafi'])} inglesi")

        if italiano is not None:
            per_numero[sezione["numero"]]["it"] = "{} " + italiano
            righe += 1
        elif sezione["numero"] is not None:
            raise SystemExit(f"{inglese}: manca il titolo italiano")

        for testo, monte in zip(paragrafi, sezione["paragrafi"]):
            # ⚠️ Un paragrafo dato come **elenco** e' un paragrafo che non si
            # puo' reimpaginare: una tabella a colonne fisse (la portata delle
            # armi da tiro) o un elenco in cui la spezzatura e' contenuto.
            # Li' le righe si scrivono a mano, una per una.
            if isinstance(testo, list):
                if len(testo) != len(monte):
                    raise SystemExit(
                        f"{inglese}: {len(testo)} righe scritte a mano contro "
                        f"{len(monte)} inglesi")
                spezzato = testo
            else:
                spezzato = _impagina.impagina(testo, len(monte))
            for resa, (numero, _) in zip(spezzato, monte):
                per_numero[numero]["it"] = resa
                righe += 1
        fatte += 1

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")

    resi = sum(1 for v in voci if v["it"])
    print(f"{fatte} sezioni su {len(struttura)}, {righe} righe scritte; "
          f"{resi} rese su {len(voci)} righe del file")


if __name__ == "__main__":
    main(sys.argv[1])
