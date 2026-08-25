# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %1 — «Beginner's Guide», la Guida del principiante.

    python scratchpad/_98-rese-book-01.py lavoro/book-001.jsonl

E' il libro che il gioco stesso ti dice di leggere: `chat.hsp:16594`, il
capitano della gilda degli avventurieri — «se sei della gilda ce l'hai anche tu,
rileggitela con Shift + ?». 224 righe.

⚠️ **Il metro e' 43 caratteri per riga** (306 px di colonna / 7 px per
carattere) e `command.hsp:8412` fa `mes s` **senza mandare a capo**: una riga
lunga entra nella colonna accanto. La misura sta in
`scratchpad/_98-book-mes.py`; l'inglese di monte non passa mai 39.

⚠️ **La struttura sta nelle righe, non nel testo**, e va tenuta al suo indice:
la riga 1 e' il titolo (corpo piu' grande, grassetto, `command.hsp:8403`), la 2
l'autore col suo tab (corpo piu' piccolo, `:8406`), le 69/94/145 sono le
intestazioni di sezione centrate a mano con gli spazi, le 71-93 l'elenco
geografico coi rientri, le 102-105 il riquadro dell'esempio. Dentro un
paragrafo invece le righe sono solo un a capo tipografico: li' il testo si
ridistribuisce a piacere, purche' il **conto delle righe del paragrafo** resti
quello.

⚠️ Niente aggettivi ne' participi riferiti al giocatore: il vecchio avventuriero
scrive a chi legge, e il genere non si conosce. «Non so da che parte arriverai»,
non «da che parte sei arrivato»; «quando hai sonno», non «quando sei stanco»;
«occhio al tempo», non «attenta al tempo».
"""
import io
import json
import sys

RIGHE = [
    # 1-2  titolo e autore: corpo diverso, e il tab della riga 2 e' di monte
    "Guida del principiante",
    "\tAutore: un vecchio avventuriero",
    # 3-4
    "<Il libro è sciupato e ingiallito",
    "dagli anni>",
    # 5-8
    "Lascio qui questo libro nel caso non",
    "torni dall'ultima avventura: che",
    "almeno qualcuno impari dalle mie",
    "prove e dai miei guai.",
    # 9-11
    "Ho vissuto molti anni e fatto molte",
    "cose. Di quel che questo mondo ha da",
    "offrire ne ho visto parecchio.",
    # 12-16
    "Questa grotta è stata il mio",
    "nascondiglio nelle ultime stagioni;",
    "ma se stai leggendo, ormai è casa",
    "tua. Non me ne dolgo: o sono morto,",
    "o sono ricco sfondato.",
    # 17-20
    "Comunque, se hai in mente di fare il",
    "mio stesso mestiere, e non sei uno",
    "dei monelli del posto che ci giocano,",
    "qualche consiglio te lo devo.",
    # 21
    "Da dove comincio?",
    # 22-24
    "Non so da che parte arriverai, quindi",
    "meglio che ti dica come sono messi",
    "i posti qui intorno;",
    # 25-34
    "Se segui il sentiero da qui verso",
    "sud-est arrivi a Vernis. È una città",
    "di minatori, ma qualche bottega, una",
    "taverna e una locanda ce le ha. Lì",
    "dovresti trovare lavoro, e anche",
    "cibo, attrezzatura e magari un amico",
    "o due. La locandiera, se ricordo",
    "bene, aveva qualche noia con i",
    "teppisti del posto, l'ultima volta",
    "che ci sono passato.",
    # 35-39
    "A est di Vernis c'è quella che qui",
    "chiamano \"la Grotta dei Cuccioli\".",
    "Ecco... cambia in continuo. Un mago",
    "del posto la disse un \"piano frattale",
    "di Hausdorff-Besicovitch\". Boh.",
    # 40-45
    "Se esci dalla grotta e rientri, o",
    "scendi e risali di piano, cambia",
    "tutto: creature, oggetti, muri e",
    "uscite. Di roba se ne trova parecchia,",
    "se non ti pesa entrare e uscire di",
    "continuo.",
    # 46-53
    "Il \"cucciolo\" della grotta sta",
    "parecchio in fondo, e in città c'è",
    "un bambino che se lo riprenderebbe",
    "volentieri; ma ogni volta che ci ho",
    "provato si faceva ammazzare. Uscivo e",
    "rientravo, e lui era di nuovo lì; poi",
    "ho lasciato perdere. Magari tu ce la",
    "fai. Solo, non ti perdere.",
    # 54-61
    "Quando sarai un po' più in gamba e",
    "avrai roba migliore addosso, la",
    "grotta grigia di Lesimas può essere",
    "un altro buon posto. È una delle",
    "rovine più antiche di Nefia, e",
    "qualcosa d'interessante là dentro",
    "per forza c'è. Senza badare alle",
    "strade, sta quasi a sud di qui.",
    # 62-68
    "In giro per la terra ci saranno",
    "grotte e boschi che brulicano di",
    "bestiacce schifose. Non entrarci alla",
    "cieca: guarda che roba c'è PRIMA di",
    "metterci piede. È la preparazione che",
    "fa la differenza fra un avventuriero",
    "vivo e uno morto.",
    # 69  intestazione centrata a mano
    "         -== Geografia ==-",
    # 70
    "Se segui le strade partendo da Vernis:",
    # 71-73
    "-Porto Kapul è a ovest. 3-5 giorni",
    "  Buoni affari: è un porto",
    "  Gilda dei Guerrieri e un'Arena",
    # 74-77
    "-Palmia è a est. 2-3 giorni",
    "  Città grande, da vedere e da fare",
    "  Ci abita il re",
    "  Ha l'Arena",
    # 78-82
    "-Yowyn è a sud-est. 2-3 giorni",
    "  Paese di campagna, poco da fare se",
    "  non ti piacciono rape e Raccolto.",
    "  Nota per me: ripulire la Grotta",
    "  degli yeek ANCORA... son come conigli",
    # 83-85
    "-Lumiest è a sud-est di Palmia",
    "  Su un'isola",
    "  Ci vivono un sacco di maghi",
    # 86-89
    "-Derphy è a sud-ovest di Vernis",
    "  Non ci arriva nessuna strada",
    "  Covo miserabile di feccia e canaglie",
    "  Gira alla larga dalla Tana del Drago!",
    # 90-93
    "-Noyel è lontana, MOLTO lontana, a est",
    "  Portati un panino: è una tirata",
    "  Con la neve si va piano",
    "  Il gigante di fuoco non si stuzzica",
    # 94  intestazione
    "      -== Lavoro e incarichi ==-",
    # 95-99
    "Avrai voglia di ammazzare draghi e",
    "salvare fanciulle, ma conviene",
    "cominciare in piccolo. Fare",
    "l'avventuriero vuol dire prendersi i",
    "lavori che nessun altro vuole.",
    # 100-101
    "Le consegne sono un buon modo per",
    "cominciare. Per esempio:",
    # 102-105  il riquadro dell'esempio, coi rientri di monte
    "     Accetta il lavoro",
    "  -->PRENDI L'OGGETTO AI TUOI PIEDI!<--",
    "     Consegnalo al destinatario",
    "     Incassa il compenso",
    # 106-111
    "Occhio: dimenticare l'oggetto da",
    "consegnare è MALE, ma non è la fine",
    "del mondo. Con un po' di fortuna,",
    "le botteghe o i campi del posto hanno",
    "quello che cerchi. Non se ne",
    "accorgeranno, fidati.",
    # 112-116
    "Guarda anche quanti giorni hai per",
    "consegnare. Correre da Lumiest a",
    "Porto Kapul NON è uno spasso, e",
    "magari non sei ancora abbastanza",
    "veloce per quelli che pagano di più.",
    # 117-121
    "La caccia va dal facile al MOLTO",
    "difficile. Quanto pagano è un buon",
    "modo per capire quanto sarà brutta.",
    "Vacci piano: basta una bestiaccia",
    "e ti fa fuori.",
    # 122-126
    "Anche i regali vanno dal facile",
    "all'assurdo. Ricorda che una volta",
    "accettato il lavoro, andare dalla",
    "città a casa e tornare porta via",
    "tempo, e magari non ne hai tanto.",
    # 127-133
    "Le richieste di cucina valgono solo",
    "se sai cucinare, hai gli ingredienti",
    "e consegni prima che il cibo marcisca.",
    "Però se dai un'occhiata al forno del",
    "posto prima di accettare, magari",
    "quello che serve lo compri e basta,",
    "e il lavoro è fatto.",
    # 134-137
    "Il Raccolto SEMBRA facile, e invece",
    "può essere durissimo. Non perdere",
    "tempo e portati dietro poco o niente:",
    "in quei lavori conta la velocità.",
    # 138-144
    "Infine, cerca di non fallire un",
    "lavoro: è una macchia sul tuo nome,",
    "e troppe ti tirano addosso le",
    "guardie. Usa la testa PRIMA di",
    "accettare. Ce la faccio? Ho il tempo?",
    "Chi è che regala robaccia al figlio",
    "il giorno del compleanno?",
    # 145  intestazione
    "      -== Consigli e dritte ==-",
    # 146
    "E adesso qualche briciola di saggezza:",
    # 147-151
    "-I carichi di cibo del carretto",
    "costano poco, e li mangi mentre",
    "viaggi. Ma dentro città e labirinti",
    "no: se hai fame esci, mangia e",
    "rientra.",
    # 152-157
    "-Fai il tirchio. Sfonda ('b') gli",
    "alberi da frutto in città e nei",
    "campi, e fuori racimola tutte le",
    "piante che riesci. Quell'armatura",
    "non ti verrà in mano se continui a",
    "mangiare torte e crostate.",
    # 158-161
    "-La carne di molti mostri si mangia.",
    "Le donne vanno matte per quella di",
    "putit, per la pelle. Certa non ti fa",
    "bene, ma se hai fame...",
    # 162-165
    "-La carne umana è succulenta e sa di",
    "maiale giovane, ma non si mangia.",
    "Solo i pazzi mangiano la gente, e",
    "tu non sei fra quelli, vero?",
    # 166-167
    "-I locandieri, per due monete, ti",
    "danno da mangiare bene. E hanno letti.",
    # 168-171
    "-Finché non compri, trovi o rubi un",
    "letto per casa, quando hai sonno",
    "dormi in locanda. Per i labirinti",
    "profondi, prendi un sacco a pelo.",
    # 172-174
    "-Se una bestia o un compagno cade in",
    "battaglia, quasi ogni città ha un",
    "barista che lo riporta su, a pagamento.",
    # 175-178
    "-Guarda il diario ('j')! Ci trovi",
    "tutto: le missioni che hai in corso,",
    "i lavori, gli avvenimenti, la tua",
    "fama e le tasse. Guardalo spesso.",
    # 179-189
    "-A proposito di tasse. Quando avrai",
    "fama abbastanza, due volte al mese",
    "ti arriva una paga in denaro e in",
    "merci, e te la trovi nel baule degli",
    "stipendi di casa tua. Ma con la paga",
    "arrivano anche le tasse. Prendi la",
    "cartella e i contanti e vai a pagare",
    "all'ambasciata, appena a nord di",
    "Palmia. Non lasciare che si accumuli:",
    "gli esattori sono peggio di qualunque",
    "drago o demone.",
    # 190-197
    "-Se le abilità smettono di salire,",
    "cerca un istruttore. Ce n'è uno in",
    "ogni città, e affila quelle che già",
    "hai. Ne conosce anche di nuove, e a",
    "pagamento te le insegna. Attenzione,",
    "però: accettano solo monete di",
    "platino, e di quelle in giro ce ne",
    "sono poche.",
    # 198-205
    "-E infine, occhio al tempo. Sì, due",
    "gocce non hanno mai ucciso nessuno,",
    "ma con la pioggia forte arrivano i",
    "fulmini che accecano e i tuoni che",
    "confondono. Cerca di non perderti",
    "mentre infuria. A volte la cosa",
    "migliore è stare fermi finché la",
    "testa non si schiarisce.",
    # 206-218
    "Di rado, ma sempre più spesso, arriva",
    "il temuto vento d'etere. Da quello",
    "guardati davvero. Un mio amico ci è",
    "rimasto fuori in mezzo, e quando è",
    "rientrato barcollando aveva poco di",
    "umano addosso. Quando arriva, TROVA",
    "UN RIFUGIO! Non lo dirò mai",
    "abbastanza. Nasconditi in una grotta,",
    "se i mostri dentro non ti fanno a",
    "pezzi. In città non sei al sicuro",
    "per niente: corri dal locandiere e",
    "chiedi il Rifugio. Aspetta che quella",
    "roba passi: solo dopo si torna.",
    # 219-223
    "Per chiudere: spero che tutto questo",
    "ti serva, e spero che la mia ultima",
    "avventura sia buona. Ora, con",
    "permesso: ho un forte da conquistare.",
    "Che sarà mai?",
    # 224
    "Buona fortuna a te e ai tuoi viaggi.",
]

BLOCCO = "1"


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]
    gruppo = sorted((v for v in voci if v["blocco"] == BLOCCO), key=lambda v: v["riga"])

    if len(gruppo) != len(RIGHE):
        raise SystemExit(f"%{BLOCCO}: {len(RIGHE)} rese, {len(gruppo)} righe inglesi")

    for voce, resa in zip(gruppo, RIGHE):
        voce["it"] = resa

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"%{BLOCCO}: {len(gruppo)} rese; nel lotto {sum(1 for v in voci if v['it'])} "
          f"su {len(voci)}")


if __name__ == "__main__":
    main(sys.argv[1])
