# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %17 e %21 — la psicosi nefiana e il diario di Zanan.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-10.py lavoro/book-010.jsonl

Valgono le regole di `_99-rese-book-02.py`. Sono gli ultimi due blocchi di
`book.txt`: con questo lotto il file si chiude.

⚠️ **`%21` e' un diario, e le sue righe finali sono rotte di proposito.** Le
ultime cinque righe di monte perdono lettere man mano che chi scrive muore
(`Hand  go ng numb`, `    t write`): in italiano si rompono allo stesso modo,
con gli stessi buchi. Non e' un refuso da correggere — e' la scena.

⚠️ I separatori `-------------------` fra un'annotazione e l'altra restano
identici all'inglese: sono ventisette caratteri di soli segni, e la rete
`identica` di `dati_verifica` li lascia passare da sola (nessuna lettera
dentro, quindi non c'e' niente che qualcuno possa aver dimenticato).

⚠️ In `%17` le insegne di sezione (`-=Segni e sintomi=-`) tengono la
spaziatura in testa di monte, che le centra a mano.

Il lessico dal dizionario: `Meshera` (nome proprio, femminile in
`db_creature.hsp:91387`), `l'eroe cremisi di Zanan` (`db_card.hsp:10475`, il
titolo di `<Loyter>`), `Zanan`, `labirinto` per `dungeon` (`chat.hsp:13977`).
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

SEPARATORE = "          -------------------"

# ---------------------------------------------------------------- %17
# Articolo di psicologia: terza persona, distacco clinico, note a pie' di
# pagina. Il pezzo funziona perche' descrive con freddezza il giocatore stesso.
BLOCCO_17 = [
    # 1-2
    "Studio sulla psicosi nefiana",
    "\tdi uno psicologo di Zanan",
    # 3-6
    "La psicosi nefiana è un disturbo",
    "mentale che si sviluppa in alcune",
    "persone quando si trovano dentro una",
    "Nefia (comunemente detta labirinto).",
    # 7-11
    "       -=Segni e sintomi=-",
    "Il disturbo si presenta in tre",
    "stadi, descritti qui sotto, dei",
    "quali gli ultimi sono i più",
    "gravi.",
    # 12-19
    "       -=Psicosi di stadio 1=-",
    "Caratterizzata da capacità",
    "cognitiva ridotta. Il calo varia",
    "da paziente a paziente, ma di",
    "norma manca la capacità di",
    "riconoscere gli oggetti: si ignorano",
    "oggetti utili per terra o ci si",
    "getta alla cieca sui nemici.",
    # 20-23
    "Ciò nonostante, molti avventurieri",
    "riescono a mantenere in città una",
    "buona qualità di vita anche con",
    "questo stadio del disturbo.",
    # 24-31
    "       -=Psicosi di stadio 2=-",
    "Capacità di riconoscere gli oggetti",
    "bassissima, con incapacità completa",
    "per alcune classi di oggetti.",
    "Molti colpiti da questo stadio non",
    "riconoscono le scale e trovano",
    "grandissima difficoltà a ritrovare",
    "la via di casa.",
    # 32-39
    "       -=Psicosi di stadio 3=-",
    "Segnata da aggressività crescente.",
    "A questo stadio i pazienti prendono",
    "di mira e aggrediscono altre",
    "persone, conoscenti ed ex compagni",
    "compresi. Per ragioni ancora ignote,",
    "i pazienti di stadio 3 non si",
    "attaccano fra loro.",
    # 40-48
    "Alcuni dei colpiti si mettono",
    "insieme in gruppi di lavoro, quindi",
    "pare che in qualche modo si",
    "riconoscano. Si è anche osservato",
    "che chi non mostrava condotte",
    "aggressive prima dell'esordio del",
    "disturbo non ne mostra nessuna",
    "nemmeno a questo",
    "stadio.",
    # 49-54
    "Molti malati di psicosi di stadio 2",
    "restano intrappolati nei labirinti,",
    "ma si riferisce spesso di individui",
    "simili che ricompaiono di colpo in",
    "superficie quando il labirinto",
    "sprofonda nella crosta.",
    # 55-69
    "          -=Ipotesi=-",
    "Per spiegare il fenomeno sono state",
    "avanzate due ipotesi: che derivi",
    "dall'esposizione al mana dei",
    "labirinti, oppure a un particolare",
    "tipo di campo magnetico. Nessuna",
    "delle due spiegazioni, però, si è",
    "dimostrata del tutto soddisfacente.",
    "Per quanto ci sia una correlazione",
    "forte e positiva fra il tempo",
    "passato nei labirinti e la gravità",
    "della psicosi, questo non spiega",
    "la grande variabilità nella rapidità",
    "e nella gravità dell'esordio da",
    "individuo a individuo.",
    # 70-76
    "Molti avventurieri colpiti non vanno",
    "mai oltre lo stadio 1, e molti altri",
    "non sviluppano affatto la psicosi.",
    "È possibile che chi diventa",
    "avventuriero sia per natura meno",
    "predisposto al",
    "disturbo.",
    # 77-91
    " -=Prevenzione della psicosi nefiana=-",
    "Al momento in cui si scrive non",
    "esiste una cura per la psicosi",
    "nefiana. La ricerca ha però mostrato",
    "che arruolare compagni non",
    "predisposti alla psicosi offre una",
    "certa protezione contro il disturbo.",
    "C'è stato anche un caso in cui un",
    "intero gruppo ha sviluppato il",
    "disturbo dopo aver perso il",
    "comandante: si ritiene perciò che",
    "l'umore e lo stato mentale delle",
    "persone abbiano parte importante",
    "sia nel progredire sia nel prevenire",
    "il disturbo.",
    # 92-95
    "Alcuni riferiscono anche un",
    "miglioramento delle condizioni dopo",
    "aver evitato i labirinti per un",
    "periodo.",
    # 96-108
    "       -=Come la vede la gente=-",
    "L'idea che i labirinti siano",
    "pericolosi è radicata nella società",
    "fin dall'antichità, ma pochi",
    "collegano la psicosi nefiana a quel",
    "pericolo. È diffusa l'idea sbagliata",
    "che i labirinti siano innocui senza",
    "i mostri che ci abitano. Di casi",
    "documentati di espertissimi",
    "esploratori di labirinti che si",
    "sono ammalati ce ne sono molti",
    "fin dall'antichità",
    "(vedi la nota 1).",
    # 109-114
    "Per questo alcuni paesi vietano",
    "l'accesso ai labirinti e altri lo",
    "riservano ai militari, ma queste",
    "misure non bastano ancora a",
    "prevenire i casi di psicosi",
    "nefiana.",
    # 115-122
    "Nota 1:",
    "La testimonianza più antica di un",
    "caso simile è un'iscrizione trovata",
    "a Kjaraht, che risale a 3.000 anni",
    "fa. Un noto conquistatore di",
    "labirinti impazzì e si sospettò",
    "che fosse posseduto da un labirinto,",
    "il che portò alla sua esecuzione.",
]

# ---------------------------------------------------------------- %21
# Il diario di un ricercatore di Zanan, dall'ordine di trasferimento alla
# morte nel reparto sigillato. Prima persona, rabbia crescente, e la
# maledizione ricorrente («Damn it», «Damn these people») che scandisce le
# annotazioni: in italiano resta ricorrente, perche' e' il ritmo del pezzo.
BLOCCO_21 = [
    # 1-2
    "Ultime parole amare",
    "\tdi un ricercatore di Zanan",
    # 3-15
    "Oggi il capo mi ha convocato. Pare",
    "che mi trasferiscano in un altro",
    "centro di ricerca. Perché?",
    "Siamo a un passo dal mettere a",
    "punto gli insetti da guerra! Sarò",
    "basso nella gerarchia, ma resto",
    "quello che guida la sua squadra.",
    "Se mi trasferiscono, qui non",
    "resterà abbastanza gente.",
    "E il peggio è che nel centro dove",
    "vado fanno ricerca sul potenziamento",
    "umano per via batterica.",
    "Solo a dirlo mi vengono i brividi.",
    # 16-21
    "È un ordine, quindi non posso dire",
    "di no; ma mi fa una rabbia tremenda",
    "che abbiano deciso senza",
    "consultarmi. E adesso me lo",
    "dicono di sfuggita, come se",
    "non fosse niente.",
    # 22
    "Maledizione.",
    # 23
    SEPARATORE,
    # 24-31
    "Quelli di questo centro nuovo sono",
    "matti. E, considerato dove lavoravo",
    "prima, è tutto dire. Mi chiedevo",
    "da dove prendessero i soggetti.",
    "Risulta che truffavano i soldi alla",
    "gente e poi, quando non poteva",
    "pagare, la costringevano a vendere",
    "i familiari.",
    # 32-33
    "Non riesco a credere che facciano",
    "esperimenti anche sui bambini.",
    # 34
    "Maledetta gente.",
    # 35-42
    "Come faccio a saperlo? Perché il",
    "capo era così contento dopo aver",
    "contato l'oro spillato alle",
    "famiglie che ha dovuto raccontarmelo.",
    "Ci credete? Sto seriamente pensando",
    "di passare a un altro paese, perché",
    "qui non c'è verso che io voglia",
    "lavorare.",
    # 43-50
    "Scappare però non posso. Le guardie",
    "armate sorvegliano sempre. Lo",
    "chiamano protocollo di contenimento",
    "biologico, ed è così stretto che di",
    "qui non esce nemmeno una formica.",
    "Dovrei in qualche modo avere la",
    "meglio sulle guardie o aprire un",
    "buco nel muro per uscire...",
    # 51
    SEPARATORE,
    # 52-57
    "I soggetti si chiamano con un",
    "numero, stanno in celle singole",
    "(che loro chiamano suite) e sono",
    "sorvegliati senza sosta. Sono",
    "prigionieri, colpevoli di niente",
    "se non di essere caduti in una truffa.",
    # 58-61
    "L'ho detto a un collega e mi ha",
    "risposto che è colpa loro se ci",
    "sono cascati. L'ha detto sul",
    "serio.",
    # 62-65
    "E per finire mi hanno appioppato",
    "il giro d'ispezione. Dicendo che,",
    "se mi stanno tanto simpatici, posso",
    "andare a chiacchierarci.",
    # 66-67
    "Maledetta gente.",
    SEPARATORE,
    # 68-82
    "Così ho ingoiato il rospo e ho",
    "fatto il giro d'ispezione. I",
    "soggetti mi hanno insultato appena",
    "mi hanno visto. Io non gli ho fatto",
    "niente, ma dal loro punto di vista",
    "immagino di essere il nemico.",
    "Altro che chiacchierare. Tornando",
    "indietro ho sentito qualcuno",
    "singhiozzare nella cella in fondo",
    "al corridoio, e qualcun altro che",
    "sembrava consolare chi piangeva.",
    "Qualcosa l'avevo sentita, di due",
    "fratelli, un maschio e una femmina",
    "per la precisione, che hanno le",
    "celle una accanto all'altra.",
    # 83-85
    "Spezza il cuore, ma non posso certo",
    "dirlo a nessuno né farci qualcosa.",
    "Sono proprio un vigliacco.",
    # 86
    "Maledetto me.",
    # 87
    SEPARATORE,
    # 88-94
    "Ma stiamo scherzando. Qui stanno",
    "cercando di controllare degli",
    "omuncoli uomo-Meshera! Voglio dire,",
    "tecnicamente batteri LO sono, ma",
    "è tutta un'altra cosa da quel che",
    "dicono i rapporti che mandiamo",
    "ai militari!",
    # 95-100
    "Sulla Meshera avevano già provato a",
    "fare ricerca, ma il progetto fu",
    "chiuso. Se adesso lo fanno di",
    "nascosto, vuol dire che cercano",
    "risultati abbastanza grossi da far",
    "tacere i militari.",
    # 101-102
    "Sotto c'è dell'altro, di sicuro.",
    "Continuo a cercare.",
    # 103
    SEPARATORE,
    # 104-109
    "Pare che vogliano controllare la",
    "Meshera con fibre nervose alterate.",
    "Espongono il corpo alla Meshera e",
    "lo lasciano trasformare, poi lo",
    "usano come un burattino quando",
    "è finito.",
    # 110-116
    "Quando invade i nervi, il batterio",
    "prende il controllo dei movimenti e",
    "prova a muovere il corpo: lo",
    "impediscono con farmaci e con la",
    "chirurgia. Su ogni soggetto qui",
    "l'operazione l'hanno già",
    "fatta.",
    # 117-123
    "In teoria funziona; ma se dopo",
    "l'intervento i soggetti sfuggono",
    "al controllo? Risulta che dopo",
    "la procedura i soggetti li",
    "abbattono col gas. Lo useranno",
    "sui soldati solo quando avranno",
    "messo a punto la tecnica.",
    # 124
    "Maledizione. È imperdonabile.",
    # 125
    SEPARATORE,
    # 126-139
    "Oggi corrono tutti come pazzi. Ho",
    "sentito che i pezzi grossi del",
    "comando militare vengono a",
    "ispezionare il posto nel",
    "pomeriggio. Devono essere davvero",
    "disperati per nascondere tutto,",
    "perché hanno tirato dentro anche",
    "un nuovo come me a coprire. E",
    "grazie a questo adesso so fin dove",
    "si sono spinti con la ricerca.",
    "Che questo posto vada all'inferno.",
    "Quel che fanno qui è così schifoso",
    "che mi viene da vomitare. Questa",
    "ricerca ha passato ogni limite.",
    # 140-141
    "I documenti che ho visto oggi",
    "me li sono imparati a memoria.",
    # 142
    SEPARATORE,
    # 143-151
    "Quello venuto a ispezionare è",
    "risultato essere un sottoposto",
    "dell'eroe cremisi. Il Cremisi di",
    "Zanan è famoso come militare, ma",
    "negli ambienti della ricerca è",
    "famoso per la sua diffidenza verso",
    "le armi biologiche. È proprio lui",
    "che ha tagliato a zero i fondi",
    "della mia ricerca sugli insetti.",
    # 152-157
    "Comunque. È la mia occasione per",
    "far sparire questo inferno! Ho",
    "scarabocchiato su un foglio tutto",
    "quel che sapevo di questo posto e",
    "sono riuscito a passarglielo",
    "mentre se ne andava.",
    # 158-165
    "Immagino sia questo che chiamano",
    "fare la spia. È tutto quel che",
    "posso fare. Da quando sono arrivato",
    "non sono più uscito di qui. Ora",
    "resta da pregare che non scoprano",
    "che la soffiata è mia, e che",
    "arrivino prima che i soggetti",
    "vengano sacrificati...",
    # 166
    SEPARATORE,
    # 167-173
    "Brutta storia. Il capo deve aver",
    "fiutato qualcosa nell'ispezione",
    "in arrivo, perché ha anticipato",
    "l'esperimento. Maledizione, mi",
    "stanno già chiamando: dicono di",
    "prepararmi a cominciare.",
    "Devo fare qualcosa!",
    # 174
    SEPARATORE,
    # 175-179
    "Non ho potuto fare niente. Non ho",
    "avuto il tempo di fare niente.",
    "Ho solo eseguito gli ordini. Dopo",
    "che la Meshera dei soggetti si è",
    "attivata, abbiamo dato i farmaci.",
    # 180-185
    "I farmaci purtroppo non erano",
    "abbastanza forti da ridurre la",
    "gente a un vegetale, e tutti hanno",
    "cominciato a contorcersi dal dolore.",
    "O forse era la Meshera. Non lo",
    "so.",
    # 186-191
    "Tutti gli altri ricercatori",
    "guardavano i soggetti che si",
    "contorcevano pieni di aspettativa.",
    "Non tocca a me dirlo, forse, visto",
    "che studio armi; ma la loro",
    "indifferenza mi fa rabbia.",
    # 192
    "Maledetta gente. Maledetti tutti.",
    # 193
    SEPARATORE,
    # 194-208
    "Due ore dopo l'inizio",
    "dell'esperimento hanno cominciato",
    "a vedersi i cambiamenti. A certi",
    "soggetti il corpo cambiava colore,",
    "ad altri crescevano tentacoli.",
    "Il capo li ha chiamati scarti a",
    "bassa compatibilità. Sapete che vi",
    "dico? Gli scarti siete voi.",
    "Mentre tutti gli altri soggetti",
    "avevano le convulsioni, il numero 14",
    "è semplicemente stramazzato e si è",
    "fermato. Il corpo era rimasto",
    "uguale, quindi l'hanno creduto",
    "compatibile, ma a me qualcosa non",
    "tornava. Portato via per esami. Vado.",
    # 209
    SEPARATORE,
    # 210-214
    "Appena l'abbiamo portato nell'altra",
    "stanza, il numero 14 è balzato in",
    "piedi. Pare facesse il morto.",
    "Il trucco più vecchio del mondo,",
    "ma ha funzionato eccome.",
    # 215-218
    "Con la sua forza sovrumana ha",
    "scagliato via le guardie come",
    "bambole di pezza, e la ferita gli",
    "si è chiusa all'istante.",
    # 219-223
    "Sarà abbastanza forte da farsi",
    "strada fuori da questo complesso?",
    "Ho gridato alle guardie di",
    "presidiare la porta, indicando",
    "l'uscita.",
    # 224-227
    "Pare che il 14 abbia capito,",
    "perché è filato dritto verso",
    "l'uscita falciando le guardie",
    "lungo la strada. Bene.",
    # 228
    SEPARATORE,
    # 229-231
    "Maledizione, che idiota! Se era",
    "così forte poteva ripulire da solo",
    "tutto il complesso!",
    # 232-235
    "Il 14 è sfuggito agli inseguitori,",
    "ma è scattato l'allarme. Adesso",
    "salvare la 16, sua sorella, sarà",
    "molto più difficile.",
    # 236-237
    "Perché non ci ho pensato?",
    "Maledizione, che idiota!",
    # 238
    SEPARATORE,
    # 239-240
    "La gente mi disgusta. Sono stufo",
    "marcio di tutto.",
    # 241-245
    "Sono passate 12 ore",
    "dall'esperimento. Alcuni, me",
    "compreso, sono stati mandati a",
    "vedere se ci fossero altri",
    "soggetti compatibili.",
    # 246-252
    "Avevo la testa piena di pensieri",
    "su come scappare dal reparto di",
    "quarantena, se là ci fosse stato",
    "un altro soggetto compatibile.",
    "Senza accorgermene ero già",
    "arrivato alle suite, e non ero",
    "pronto a quel che ho visto.",
    # 253-257
    "I corpi dei soggetti si erano",
    "trasformati in bozzoli. Gli altri",
    "ricercatori gridavano qualcosa.",
    "Che era troppo presto, che non",
    "potevano cambiare in 12 ore.",
    # 258-266
    "Hanno provato disperatamente a",
    "chiamare quelli fuori dalla radio,",
    "ma poi c'è stato un rumore forte.",
    "Erano le barriere di contenimento",
    "che si chiudevano attorno al",
    "reparto di quarantena. Il",
    "ricercatore che stava proprio in",
    "fondo al gruppo è corso a uscire,",
    "ma i muri erano già calati.",
    # 267
    "La radio taceva.",
    # 268
    SEPARATORE,
    # 269-275
    "Mentre eravamo disperati, i bozzoli",
    "hanno cominciato ad assalirci con",
    "i tentacoli. Siamo riusciti a",
    "ritirarci fino al muro di",
    "contenimento, ma quasi tutti si",
    "erano feriti gravemente. Siamo",
    "in trappola. Non c'è via d'uscita.",
    # 276-282
    "Abbiamo sentito un rumore forte",
    "in fondo al centro. Era un altro",
    "soggetto scatenato che colpiva i",
    "muri? Ero curioso, ma coi tentacoli",
    "che ci tenevano bloccati qui non",
    "c'era verso che riuscissi ad",
    "arrivare fin là.",
    # 283-287
    "Alcuni ricercatori hanno perso la",
    "testa e ridono, gli altri si sono",
    "barricati in un angolo. Io?",
    "Io sto scrivendo",
    "questo.",
    # 288
    SEPARATORE,
    # 289-293   ⚠️ rotte di proposito: vedi il docstring
    "Maledizione, ci gassano tutti",
    "Le man  si intorp discono",
    "    o scriv re",
    "devo mo ire  qui",
    "male     all inf",
]

RESE = {"17": BLOCCO_17, "21": BLOCCO_21}


def misura(riga):
    return len(degrada(riga))


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]

    fuori, strette = [], []
    for blocco, righe in RESE.items():
        gruppo = sorted((v for v in voci if v["blocco"] == blocco),
                        key=lambda v: v["riga"])
        if len(gruppo) != len(righe):
            raise SystemExit(
                f"%{blocco}: {len(righe)} rese, {len(gruppo)} righe inglesi")
        for voce, resa in zip(gruppo, righe):
            larga = misura(resa)
            if larga > TETTO:
                fuori.append((blocco, voce["riga"], larga, resa))
            elif larga > TETTO_CORPUS:
                strette.append((blocco, voce["riga"], larga, resa))
            voce["it"] = resa

    for blocco, riga, larga, resa in fuori:
        print(f"  FUORI   %{blocco} riga {riga}: {larga} caratteri — {resa!r}")
    for blocco, riga, larga, resa in strette:
        print(f"  stretta %{blocco} riga {riga}: {larga} caratteri — {resa!r}")
    if fuori:
        raise SystemExit(f"{len(fuori)} righe oltre il tetto di {TETTO}: "
                         "il lotto non si scrive")

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")

    quante = sum(len(r) for r in RESE.values())
    print(f"{quante} rese in {len(RESE)} blocchi; nel lotto "
          f"{sum(1 for v in voci if v['it'])} su {len(voci)}")


if __name__ == "__main__":
    main(sys.argv[1])
