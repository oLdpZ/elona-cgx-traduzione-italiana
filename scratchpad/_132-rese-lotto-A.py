# -*- coding: utf-8 -*-
"""Le rese del lotto A di `scene2.hsp`: scene 0-5, il prologo e Vernis.

Tre scelte che vanno dette, perche' non discendono dall'inglese:

⚠️⚠️ **La geografia della scena 0 segue il giapponese, perche' l'inglese si
contraddice.** `scene1.hsp` distingue due foreste che l'inglese chiama con lo
stesso nome: `辺境の地カルーンの森` (la foresta di Karune, quella che cambia) e
`ヴィンデールの森` (la foresta di Vindale, dove l'anomalia comincia, sul
continente orientale). L'inglese scrive «the Vindale Forest» in tutt'e due i
punti, e cosi' facendo fa cambiare e insieme invadere la stessa foresta,
perdendo il continente orientale. E' la deroga gia' presa dalla 79a-81a: dove
l'inglese di monte e' rotto, si segue il giapponese.

⚠️ **`異形の森` resta «Foresta Eretica», `ヴィンデールの森` resta «foresta di
Vindale».** Diciassette voci del dizionario rendono la prima cosi', e il nome
inglese non basta a distinguerle: in `4.13` e `4.27` il giapponese dice Vindale,
in `1.6`, `1.7`, `4.12` e `0.3` dice Eretica -- e l'inglese scrive «Heretical»
e «Vindale» senza seguire la stessa linea.

⚠️ **`ヴェセル` resta «Bethel».** Il giapponese lo chiama Veseru, l'inglese
Bethel, e il progetto ha gia' deciso «<Bethel> il falco bianco»
(`db_creature.hsp`, `db_card.hsp`). Un nome deciso non si cambia in un file
nuovo: la coerenza col resto del gioco vale piu' della fedelta' al giapponese
su una traslitterazione.

ⓘ `2.29` segue il giapponese anche nel senso: l'inglese dice che Bethel non e'
piu' pericoloso, il giapponese dice l'opposto -- che non c'e' elemento piu'
pericoloso di lui. Le due frasi non sono sfumature diverse, sono contrarie.

Termini ripresi dal dizionario, non inventati qui: birra crim, crimberry,
Meshera, il falco bianco, vento d'etere, Tyris del Nord, la <Regina Sedona>,
<Loyter> l'eroe cremisi di Zanan, <Larnneire> l'ascoltatrice del vento,
<Lomias> il messaggero di Vindale, <Xabi> il re di Palmia, <Bethel> il falco
bianco, Elishe, Ylva, Sierra Terre, Rehm-Ido, Elea, Zanan, Palmia, Vernis.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi, scene

LOTTO = percorsi.LAVORO_LOTTI / "scene2-0-5.jsonl"

RESE = {
    # ---------------- scena 0: il prologo e il naufragio ----------------
    ("0", 2): [
        "In tempi ormai dimenticati la terra di Ylva vide dieci grandi civiltà,",
        "e le loro rovine punteggiano ancora il suolo. Le ferite lasciate dall'ultima",
        "di esse, Rehm-Ido, non si sono ancora rimarginate. Questa è la storia",
        "di Sierra Terre, l'undicesima era, che si dice abbia distrutto e generato",
        "più di ogni altra.",
    ],
    ("0", 3): [
        "Dopo un mese di pioggia ininterrotta, la foresta di Karune, terra di confine,",
        "cambiò aspetto. Avvolta da una strana nebbia luminosa, allargò in fretta",
        "le radici e generò un ambiente in cui nessun uomo poteva vivere.",
        "L'anomalia era cominciata nella foresta di Vindale, sul continente orientale;",
        "in poco tempo tolse al popolo di Karune la terra su cui viveva,",
        "e una folla di profughi si riversò in Tyris del Nord.",
        "Il principe di un regno d'occidente predicò che quel fenomeno era la sciagura",
        "che aveva già colpito Rehm-Ido, e invocò lo sterminio della Foresta Eretica",
        "e del popolo che la abita.",
        "Gli Elea di Vindale si ritirarono dalle terre degli uomini per sfuggire all'odio,",
        "ma il solco non si colmò, e la guerra di sterminio stava per cominciare.",
    ],
    ("0", 5): [
        "Mancava poco all'alba. Ti eri intrufolato fra le merci della nave mercantile",
        "<Regina Sedona>, diretta a Tyris del Nord, e dormivi; ti svegliò d'un tratto",
        "un boato simile a un urlo.",
        "Il legno che si spacca, le onde che scuotono lo scafo, il vento che azzanna",
        "le vele. In mezzo a una raffica che pareva mandata da un demone",
        "un vecchio marinaio bestemmiò il suo dio e mormorò:",
        '"E\' il vento d\'etere"',
        "...E la nave gridò una seconda volta.",
        "Un muro d'onde schiacciò ogni cosa e, senza lasciare il tempo di una preghiera,",
        "la <Regina Sedona> fu inghiottita dal mare notturno.",
    ],

    # ---------------- scena 1: il discorso del principe ----------------
    ("1", 0): "<Saimore> il principe di Zanan",
    ("1", 3): [
        "Mentre stavi per entrare a Vernis, un soldato con lo stemma di Zanan",
        "ti fermò. Dopo un interrogatorio minuzioso, accortosi del tuo sguardo",
        "perplesso, ti rispose che il principe di Zanan era in città per un comizio.",
        "Nella piazza si era radunata una folla, e tutti ascoltavano le parole",
        "del principe albino, appoggiato con languore al braccio del suo servitore.",
    ],
    ("1", 5): "...E così un profondo dolore mi assale. Zanan ha perduto la guerra contro i nuovi regni, e il continente, rimasto senza guida, sarà teatro dello scontro fra le due grandi nazioni per anni e anni ancora. Anche raccogliendo l'eredità del compianto principe Clyne e cercando la pace, il solco fra i due stati non si colmerebbe, e la corda resterebbe tesa come oggi.",
    ("1", 6): "La guerra... Possibile che nazioni intrise di sangue e di fuoco non si accorgano della crisi senza precedenti che incombe su Sierra Terre? Il vento della sciagura divora le nostre foreste, e proprio ora tanti nostri fratelli perdono la vita e la terra. Eppure la Foresta Eretica e gli Elea, il popolo eretico, stanno per risvegliare i <Meshera>, gli incubi che distrussero Rehm-Ido.",
    ("1", 7): "La grande prova mandata a Ylva è, nello stesso momento, un'occasione di unità. Se smetteremo di combatterci, se impareremo a comprenderci e ci daremo la mano, potremo cancellare da questa terra la foresta marcia e i suoi eretici, e vincere la catastrofe.",
    ("1", 8): "Zanan non ha più l'influenza di un tempo sulle grandi potenze. Ciò che posso fare, dunque, è farvelo sapere: la speranza di Sierra Terre è Palmia, che non si è piegata alle due grandi nazioni e si è costruita una posizione salda, e la fermezza del suo popolo fedele.",
    ("1", 9): [
        "Un applauso più fragoroso degli altri risuonò nella piazza.",
        "Il discorso era ormai sommerso dal frastuono e non arrivava più fino a te,",
        "che stavi in fondo alla folla.",
        "Con una strana inquietudine e una strana curiosità per il principe albino,",
        "ti allontanasti lentamente dalla piazza.",
    ],

    # ---------------- scena 2: l'osteria di Vernis ----------------
    ("2", 0): "<Loyter> l'eroe cremisi di Zanan",
    ("2", 1): "Soldato",
    ("2", 2): "????",
    ("2", 5): ["Alla stessa ora - l'osteria di Vernis -"],
    ("2", 6): [
        "Fra i boccali che i soldati semplici di Zanan facevano tintinnare",
        "l'osteria di Vernis aveva ritrovato un'animazione che non conosceva da tempo.",
        "Un soldato giovane, ubriaco e con troppa forza da spendere,",
        "aveva attaccato briga con un uomo malmesso,",
        "e ogni tanto alzava la voce e menava le mani.",
        "L'ufficiale dai capelli rossi, accortosi della rissa del sottoposto,",
        "vuotò il boccale colmo di birra crim e si alzò senza fretta.",
    ],
    ("2", 7): "Che succede qui?",
    ("2", 8): "Ah, capitano. Niente di grave. Interrogavo solo questo tipo sospetto avvolto negli stracci. Col principe in comizio e la guardia affidata a noi non possiamo ignorare un losco, nemmeno mentre beviamo! ...Ehi, dico a te. Mi senti?",
    ("2", 9): "...",
    ("2", 10): "Quest'uomo è...",
    ("2", 11): "Come vede, è un bel faccia tosta. Gli do ancora una lezione e poi lo caccio via. Non farà male a nessuno, ma solo a vederlo il vino ci diventa acido in bocca.",
    ("2", 12): "Lascia stare.",
    ("2", 13): "Però, capitano, con una gamba rotta un accattone fa più scena, no?",
    ("2", 14): "E secondo te per chi l'ho detto? Quello che hai davanti è il falco bianco di Zanan. ...Lasciateci soli un momento.",
    ("2", 18): "Così sei venuto a seppellirti qui. E quella figura che significa, ti sei messo a fare l'eremita?",
    ("2", 19): "...",
    ("2", 21): "Le persone cambiano. Il falco bianco, di cui tutto il paese invidiava il talento e lodava le imprese, a cui erano stati concessi persino i privilegi della nobiltà, se ne sta nascosto nell'angolo di un'osteria lurida a fissare il cielo con gli occhi di un morto. Da quando hai lasciato Zanan mi manca qualcuno con cui misurarmi, e la cosa mi secca.",
    ("2", 22): "...",
    ("2", 24): "Ah, potresti almeno rispondermi male. Ti ricordi quando mi dicevi che eri stanco di essere un altro?",
    ("2", 25): "Se vuoi darmi a bere che quel figuro sudicio da mendicante è il tuo vero volto, ricchezza e fama gettate via, allora è una barzelletta. O forse rinunciare a ogni desiderio e vivere come un colpevole sarebbe il tuo modo di onorare quella ragazza?",
    ("2", 26): "Non voglio parlarne.",
    ("2", 27): "Quella ragazzina Elea... Elishe, giusto? Se posso prendere in prestito le tue parole, non era anche lei una parte della tua maschera?",
    ("2", 28): "Non ho intenzione di stare al gioco delle domande. Preferivo le botte e la cella: almeno là si stava in silenzio.",
    ("2", 29): "E allora ti accontento: ti metto agli arresti, Bethel Rumford. Fuori da Zanan non esiste elemento più pericoloso di te.",

    # ---------------- scena 3: l'accampamento di Saimore ----------------
    ("3", 0): "<Saimore> il principe di Zanan",
    ("3", 1): "<Barius> dai capelli azzurri",
    ("3", 2): "Soldato",
    ("3", 5): ["Alla stessa ora - l'accampamento del principe di Zanan -"],
    ("3", 6): "Signor Saimore, ci riferiscono che all'osteria è stato catturato un uomo sospetto. Il signor Loyter sostiene che sia il <falco bianco> scomparso tre anni fa.",
    ("3", 7): "Ne sei certo?",
    ("3", 8): "Ah, ecco... Qualcosa del vecchio aspetto c'è, ma è molto cambiato e agli interrogatori non dice una parola. A me pare un altro uomo, ma se lo dice il signor Loyter non ci saranno dubbi.",
    ("3", 9): "È cambiato, dunque. Fufu... certo che sì, non poteva restare quello di un tempo. Lasciatelo stare. Non torcetegli un capello.",
    ("3", 10): "Agli ordini.",
    ("3", 12): "Che ironia. Ti ho fatto cercare da quando hai lasciato Zanan, e ti si trova proprio adesso.",
    ("3", 13): "Il falco bianco di Zanan... E che cosa vi aspettate ancora da quell'uomo?",
    ("3", 14): "Non mi aspetto nulla. Mi basta che viva e faccia da testimone alla commedia che sta per cominciare. Senza di lui la mia storia non può arrivare alla fine.",

    # ---------------- scena 4: la sala del trono di Palmia ----------------
    ("4", 0): "<Xabi> il re di Palmia",
    ("4", 1): "<Larnneire> l'ascoltatrice del vento",
    ("4", 2): "<Barius> dai capelli azzurri",
    ("4", 3): "<Saimore> il principe di Zanan",
    ("4", 6): ["Alla stessa ora - Palmia, la sala del trono -"],
    ("4", 7): "Ben venuta, Larnneire. Quella bambina scavezzacollo è cresciuta proprio bene. Di questi tempi, e nella tua posizione, il viaggio non dev'essere stato facile.",
    ("4", 8): "È passato molto tempo, maestà. Se persino noi, popolo straniero, siamo giunti alla capitale senza un graffio, lo dobbiamo soltanto al vostro prestigio. E come messaggera della Foresta Eretica sono qui proprio per questo: per chiedervi ancora una volta di prestarci la vostra forza, per il popolo Elea e per Sierra Terre.",
    ("4", 9): "...Larnneire, mi dispiace, ma a questa attesa non posso rispondere. Anche a me duole la sciagura che si abbatte sugli Elea. Ma tu lo sai bene: fra gli Yerles e gli Eulderna le forze sono vicinissime, e a Palmia tocca soltanto tenere in equilibrio quella bilancia.",
    ("4", 10): "Adesso che molti regni e molti uomini danno ragione al principe di Zanan, e per la prima volta voltano le lame che si puntavano a vicenda contro un nemico comune, la Foresta Eretica, se Palmia alzasse la voce non sarebbe più soltanto Zanan a trattarci da ribelli, ma anche le due grandi nazioni. E il declino di Palmia significherebbe una guerra fra di loro senza più freni. Non posso esporre di nuovo Sierra Terre al fuoco e all'odio.",
    ("4", 11): "...Allora ci dite che gli Elea devono farsi vittime sacrificali per le due grandi nazioni. Per una pace fragile e passeggera, costruita con il sangue di un popolo straniero e innocente. Non esiste più, in questo continente, un cuore abbastanza grande da tendere la mano ai deboli?",
    ("4", 12): "...Innocente, dite? Mi offendete. Non vorrete darmi a intendere di ignorare i danni che la vostra Foresta Eretica, e il vento d'etere, hanno portato su di noi.",
    ("4", 13): "Siete arrivato anche voi, conte Barius. È vero, la foresta è sconvolta dal vento d'etere. Ma la foresta di Vindale ha convissuto con Sierra Terre da quando c'è memoria: perché proprio adesso avrebbe chiamato quel vento? Accusare senza nemmeno cercarne la causa non è forse un pregiudizio contro ciò che ci sembra diverso?",
    ("4", 14): "Il turbamento della foresta e il vento d'etere sono un fenomeno diverso da quella sciagura. Maestà, ascoltatemi bene. Se le pretese del principe di Zanan fossero sbagliate...",
    ("4", 15): "Non dire altro, Larnneire.",
    ("4", 16): "Maestà, ma la verità...",
    ("4", 17): "Basta così. Il resto lo ascolterò domani. Per stanotte l'alloggio ve lo faccio preparare io. Ora... non è il momento di parlarne. Cerca di capirmi.",
    ("4", 19): "Maestà... Ho capito. Ma domani tornerò. La vostra decisione è l'ultima speranza.",
    ("4", 23): "L'ultima speranza, addirittura. ...Non vorrete credere alle sciocchezze di quella ragazza, re Xabi.",
    ("4", 24): "Fin da bambino ho studiato la sciagura. I <Meshera> si chiamano anche i giganti che divorano le stelle. La Foresta Eretica, che corrode la terra e allunga le sue radici immonde, non è esattamente quello? E anche se fosse vero, come dice la ragazza, che si tratta di un fenomeno diverso, resta il fatto che quella foresta ci ruba la terra e genera mostri ripugnanti. Re Xabi, sarebbe saggio affidare la ragazza a me.",
    ("4", 25): "Uhm. Sarebbe perché è Larnneire a tenere in mano la verità?",
    ("4", 26): "La verità è la mia lettura dei fatti. Quello che mi interessa di quella ragazza è un'altra cosa. E poi, maestà, non dimenticherete che Palmia esiste perché esiste Zanan?",
    ("4", 27): "Larnneire è un'ospite di riguardo. Non posso consegnarla, nemmeno se a chiederlo è il principe di Zanan. Palmia non interverrà nella questione della foresta di Vindale: non vi basta? Ora vogliate scusarmi. Ho altro da fare.",
    ("4", 29): "...Fufu, è scappata. Però che sorpresa. Quella ragazza le somiglia in tutto, non trovi?",
    ("4", 30): "Prima il falco bianco, adesso questa Larnneire. Finalmente gli ingranaggi del destino hanno cominciato a girare.",
    ("4", 31): "Nel destino non ho più voglia di credere, ma che il palcoscenico si sia animato più del previsto è cosa da accogliere volentieri. A quei due prepara una parte all'altezza. Ho fiducia nella tua abilità, Barius dai capelli azzurri.",
    ("4", 32): "...",

    # ---------------- scena 5: l'osteria di Palmia ----------------
    ("5", 0): "<Larnneire> l'ascoltatrice del vento",
    ("5", 1): "<Lomias> il messaggero di Vindale",
    ("5", 2): "????",
    ("5", 3): "<Bethel> il falco bianco",
    ("5", 6): ["- L'osteria di Palmia -"],
    ("5", 7): "Cerchiamo una donna di nome Liana. Ne sai qualcosa?",
    ("5", 8): "...E che cosa volete da lei?",
    ("5", 9): "Ci hanno detto soltanto che è in gamba e che, se il prezzo è giusto, accetta qualunque incarico. Non credo ci serva una scorta, ma abbiamo ricevuto istruzioni da un inviato del re.",
    ("5", 10): "Qualunque incarico, se il prezzo è giusto... Fufu. In gamba lo è davvero, e non gli importa quanto sia rischiosa l'impresa. Solo che quell'uomo, vedi, non va a prezzo: va a umore. Sì, Liana sono io. Venite con me, tutti e due.",
    ("5", 14): "<Liana> la ragazza dei sogni a occhi aperti",
    ("5", 15): "Bethel, è arrivato un lavoro dopo tanto tempo... Ah... cof, cof.",
    ("5", 17): "Tu non mangi quasi niente e ti sei rimesso a fumare crimberry. Povero il mio Bethel... Su, alzati e saluta i clienti.",
    ("5", 18): "Magnifico. Il maestro di spada su cui dovremmo contare è un malato intontito dalla droga. Larnneire, mi sa che abbiamo fatto un viaggio a vuoto. Non so di che abilità andasse fiero un tempo, ma non abbiamo il tempo di stargli dietro mentre si cura.",
    ("5", 19): "Su, su... non mettetegli fretta. Bethel, tu non dar loro retta. Questa gente non sa quanto sei stato umiliato, quanto ti hanno ridotto male. A me è bastato guardarti una volta negli occhi tristi per capirlo subito: quest'uomo porta un dolore incalcolabile e si trascina dietro un passato che non riesce a recidere, poveretto. E che, se gli resto accanto, riuscirà a superare tutto e a diventare un uomo intero. Però, sai... se non ti metti a lavorare, non c'è nemmeno da mangiare!",
    ("5", 20): "Morire di fame con te non sarebbe un brutto modo di andarsene.",
    ("5", 21): "Uffa, Bethel!!",
    ("5", 22): "Fufu, Liana. Non ho intenzione di portarmi dietro anche te all'altro mondo. Dunque, l'incarico...",
    ("5", 23): "...Voi siete... Elishe...?",
    ("5", 24): "Elishe?",
    ("5", 25): "No, non farci caso. Ascoltiamo l'incarico.",
    ("5", 26): "Non ce n'è bisogno. L'ordine di affidarci a una guardia del corpo imbottita di droga lo prenderò per una pessima burla alla palmiana. Del resto non mi risulta che qualcuno ce l'abbia con noi.",
    ("5", 27): "...Scorta, dite, con molta leggerezza. Se i miei sensi non sono ottusi dalla droga, il numero di presenze che circonda questa casa va ben oltre ciò che un uomo solo può proteggere.",
    ("5", 28): "Circondati? C'è qualcuno che ci vuole colpire?",
    ("5", 29): "Sarei io a volerlo chiedere, ma pare che non ci sia tempo per parlarne. Non perdete di vista la mia schiena. Usciamo dalla città per i vicoli.",
}


def main() -> None:
    voci = [json.loads(r) for r in LOTTO.read_text(encoding="utf-8").splitlines() if r.strip()]
    senza = []
    for voce in voci:
        chiave = (voce["scena"], voce["blocco"])
        if chiave in RESE:
            resa = RESE[chiave]
            # ⭐ nel file le righe di un `{txt}` stanno in lista, perche' cosi'
            # si leggono e si contano; nel dizionario diventano **una stringa
            # sola** con gli a capo dentro, come in ogni altro file del
            # progetto. Il primo giro le scriveva come liste e ha acceso due
            # reti (`accenti`, `bilingui`) in strumenti che non c'entravano
            # niente: leggono `it` e chiamano `.strip()`.
            voce["it"] = "\n".join(resa) if isinstance(resa, list) else resa
        else:
            senza.append(chiave)
    LOTTO.write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci),
        encoding="utf-8")
    print("rese scritte : %d su %d" % (len(voci) - len(senza), len(voci)))
    if senza:
        print("SENZA RESA   :", senza)
    avanzate = set(RESE) - {(v["scena"], v["blocco"]) for v in voci}
    if avanzate:
        print("⚠️ rese che non agganciano nessuna voce:", sorted(avanzate))

    guasti = 0
    for voce in voci:
        for guaio in scene.problemi(voce):
            print("  FUORI  %s.%s %-8s %s" % (voce["scena"], voce["blocco"],
                                              voce["tipo"], guaio))
            guasti += 1
    print("fuori misura : %d   (atteso: 0)" % guasti)
    # ⚠️ separati apposta: una riga in piu' dell'inglese si guarda, non si
    # rifiuta -- l'italiano e' quasi sempre piu' lungo (regola della 70a)
    allungate = [(v, a) for v in voci for a in scene.avvisi(v)]
    print("una riga in piu' dell'inglese : %d   (si guardano)" % len(allungate))
    for voce, avviso in allungate:
        print("  guarda %s.%s %-8s %s" % (voce["scena"], voce["blocco"],
                                          voce["tipo"], avviso))
    if guasti or senza:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
