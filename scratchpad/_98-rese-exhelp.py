# -*- coding: utf-8 -*-
"""Le rese di `exhelp.txt`: i consigli della guida Norne.

    python scratchpad/_98-rese-exhelp.py lavoro/exhelp-001.jsonl

⚠️ **L'inglese di monte e' a capo fisso**, e `dati_applica` **sostituisce**
righe, non ne aggiunge: ogni blocco italiano deve avere lo stesso numero di
righe dell'inglese. Per questo il testo sta qui come una lista per blocco e
l'ordine e' quello delle righe piene, esattamente come le numera
`dati_estrai.voci()`.

⚠️ Il metro non e' quello degli altri file dati. `exhelp.txt` non passa da
`talk_conv`: `help.hsp:227` lo carica con `noteload` e lo disegna con `gmes`
(`module.hsp:4918`), che manda a capo **per carattere** a `gmesx + gmesw`, cioe'
330 px a 7 px per carattere ASCII: **48 caratteri**. La misura sta in
`scratchpad/_98-exhelp-gmes.py`.
"""
import io
import json
import sys

BLOCCHI = {
    "1": [
        "Ehi! Tu devi essere la faccia nuova di cui",
        "parlavano i miei.",
        "Ti do il benvenuto a Irva, nell'era di",
        "Sierra Terre. Io sono Norne, la guida.",
        "Aiutare i viaggiatori come te è il mio lavoro.",
        "Ecco il mio primo consiglio.",
        "Troppa roba nello zaino ti appesantisce",
        "e <emp1>ti rallenta le azioni<def>.",
        "Casa tua è un magazzino sicuro: quello che",
        "lasci lì dentro non sparisce.",
        "Certe guide pigre dicono ai nuovi arrivati",
        "di leggere i grimori in casa: <emp1>un libro",
        "difficile a volte ha effetti brutti<def>, e ti",
        "mette in pericolo. Ti prosciuga il mana,",
        "oppure ti confonde per un bel po'.",
        "...Non dar loro retta!",
        "A volte una lettura sbagliata fa comparire",
        "mostri devastanti.",
        "Non ti va che sfondino tutto e sputino fuoco",
        "sulla roba di valore che tieni in casa, vero?",
    ],
    "2": [
        "Sulla mappa del mondo il tempo scorre molto",
        "più in fretta. E certi oggetti e certe",
        "abilità lì non si possono usare: per quelli",
        "devi prima entrare nella mappa locale,",
        "<emp1>con la barra spaziatrice.<def>",
        "Se vuoi saperne di più sulla mappa del mondo,",
        "premi ? e apri l'aiuto del gioco: lì dentro",
        "c'è un mucchio di cose utili che ti serviranno",
        "per tutto il viaggio.",
        "Ricordati di stare sulla strada: i mostri",
        "che ci trovi sono più deboli di quelli che",
        "stanno nelle terre selvagge. E ogni tanto",
        "incroci un mercante girovago, che vende roba",
        "buona ma cara.",
    ],
    "3": [
        "Una città! Le strade sono piene di gente.",
        "Niente paura, non mordono: basta che tu",
        "non dia loro fastidio.",
        "Nelle città trovi un sacco di servizi:",
        "allenamento, commercio, gioco, incarichi...",
        "Se ti servono soldi o equipaggiamento, <emp1>vai<def>",
        "<emp1>a vedere la bacheca<def>.",
        "Non puoi non vederla: è grande.",
    ],
    "4": [
        "Qui vedi le missioni secondarie. Pensaci",
        "bene prima di accettarne una:",
        "qualcuna è parecchio pericolosa.",
        "Il segno $ e il suo colore dicono quanto è",
        "difficile il lavoro. <emp1>Verde è facile.<def>",
        "<emp1>Blu è più duro, rosso è rischioso.<def>",
    ],
    "5": [
        "Sei su un <emp1>punto di raccolta<def>.",
        "<emp1>Con la barra spaziatrice<def> raccogli",
        "in automatico i materiali che stanno qui.",
        "I materiali servono soprattutto a fabbricare",
        "oggetti. Certi, come i chip da casinò,",
        "si usano per giocare d'azzardo.",
    ],
    "6": [
        "Sei sull'icona di <emp1>un'area casuale<def>.",
        "Prima di entrarci, guarda il",
        "<emp1>livello di pericolo indicativo<def>.",
        "Meglio stare alla larga dalle aree di livello",
        "più alto del tuo.",
        "In fondo a ogni area casuale ti aspetta il",
        "signore del labirinto: è forte, ma il suo",
        "bottino vale la fatica.",
    ],
    "7": [
        "Nelle locande si mangia come si deve.",
        "Se non hai una fonte di cibo tua,",
        "passa in locanda con regolarità e tieni da",
        "parte il cibo buono per il viaggio.",
        "Le locande offrono anche <emp1>il rifugio<def>",
        "quando il tempo è brutto o soffia il vento",
        "d'etere, ed è gratis. Chiedilo al locandiere.",
    ],
    "8": [
        "Dall'istruttore impari abilità nuove e",
        "migliori quelle che hai già.",
        "Per allenarti servono",
        "<emp1>monete di platino<def>.",
        "Quelle monete sono difficili da trovare,",
        "ma senza non c'è modo di imparare",
        "un'abilità nuova!",
    ],
    "9": [
        "Ehi, hai una faccia assonnata!",
        "Si sa, <emp1>bisogna dormire con regolarità<def>.",
        "Quando ti viene sonno, cerca un letto.",
        "Anche solo riposare, a volte, ti tira",
        "dentro un sogno.",
        "Quando hai accumulato esperienza e poi",
        "dormi, il potenziale degli attributi base",
        "cresce. E nel sonno può capitarti",
        "di incontrare qualche avvenimento.",
    ],
    "10": [
        "Hai fame, eh?",
        "Se non mangi ti consumi, e alla fine",
        "<emp1>muori di fame<def>.",
        "Tieni sempre la pancia piena!",
        "Cibi diversi danno effetti diversi. Quasi",
        "sempre è roba da poco, ma anche il poco",
        "aiuta.",
        "Puoi anche mangiare i cadaveri.",
        "Qualcuno alza parecchio gli attributi,",
        "qualche altro regala una resistenza.",
    ],
    "11": [
        "Che acquazzone! Con questo tempo è meglio",
        "non uscire: si viaggia più piano e ci si",
        "può anche perdere per strada.",
        "Te l'ho detto che quando il tempo è brutto",
        "puoi ripararti nel rifugio delle locande?",
        "Approfittane!",
    ],
    "12": [
        "Nevica! A me la neve piace un mucchio!",
        "Però... per chi viaggia è una brutta bestia.",
        "Nella neve alta si cammina male, e finché",
        "c'è neve sulla mappa del mondo spostarsi",
        "da un posto all'altro porta via",
        "molto più tempo.",
        "Per fortuna a Tyris del Nord la neve non",
        "dura molto. Di solito basta fermarsi da",
        "qualche parte e prendersela comoda:",
        "prima o poi si scioglie e si riparte",
        "per la propria strada.",
        "Quando il tempo è brutto come adesso,",
        "il locandiere ti porta al rifugio",
        "della città.",
        "Faresti bene ad approfittarne.",
    ],
    "13": [
        "Il vento d'etere...",
        "Quel vento è un guaio serio.",
        "Se ci stai dentro abbastanza a lungo,",
        "cominci a mutare e, cosa ben peggiore,",
        "comincia a corroderti la malattia",
        "dell'etere.",
        "Mentre soffia, anche le terre selvagge",
        "diventano più pericolose. Però si sa",
        "quando arriva: soltanto",
        "<emp1>nei mesi multipli di 3<def>",
        "<emp1>e nei giorni dall'1 al 10.<def>",
        "Questo è meglio ricordarselo.",
        "A differenza degli altri tempi brutti, col",
        "vento d'etere sulla mappa del mondo ti",
        "muovi più in fretta del solito. Se riesci",
        "a tenere a bada mutazioni e malattia,",
        "questo vento può persino tornarti utile.",
        "Con un tempo così, il locandiere ti porta",
        "al rifugio della città. Faresti bene ad",
        "approfittarne.",
    ],
    "14": [
        "Due parole sui rifugi.",
        "Il rifugio della città ti mette al sicuro",
        "dal vento d'etere, e anche dai temporali",
        "e dalla neve.",
        "Dentro, il tempo corre decine di volte",
        "più in fretta del solito, e le provviste",
        "si consumano da sole.",
        "Quando il cielo si rimette, il tempo",
        "riprende il passo di sempre e le",
        "provviste smettono di consumarsi.",
    ],
    "15": [
        "Alla fine il male ti ha preso...",
        "Non stupirti: la corrosione avanza",
        "piano piano col tempo, qualunque cosa",
        "tu faccia.",
        "Per ora i sintomi sono ancora piccolissimi.",
        "La malattia avanza per 20 stadi. Man mano",
        "che sale, le tue condizioni si fanno più",
        "gravi, e alla fine possono anche",
        "ucciderti.",
        "Niente paura! Hai tutto il tempo per",
        "correre ai ripari. Ma il vento d'etere è",
        "un altro paio di maniche: peggiora la",
        "malattia di parecchio. Quando soffia,",
        "ritirati nel rifugio di una locanda.",
    ],
    "16": [
        "Ecco il giorno di paga!",
        "Si viene pagati il 1 e il 15 di ogni mese.",
        "A seconda del tuo rango e della tua fama",
        "ti arrivano oro e merci.",
        "La paga si ritira dal baule degli stipendi",
        "che hai in casa. Rango e paga li trovi",
        "anche nel diario.",
        "Oltre alla paga, il primo di ogni mese",
        "arriva la cartella delle tasse. Si paga",
        "all'ambasciata a nord di Palmia, e hai",
        "quattro o cinque mesi di tempo prima che",
        "ti mettano fra i criminali.",
    ],
    "17": [
        "Oh, un portale lunare!",
        "I maghi esperti li aprono per coprire",
        "distanze enormi. Se ti va, puoi seguirli:",
        "il portale resta aperto per un po'...",
    ],
    "18": [
        "Fermento!!",
        "Le Nefie sono entrate in fermento.",
        "Comincia soltanto",
        "nei mesi <emp1>che non sono multipli di 3<def>",
        "e <emp1>nei giorni dal 15 al 24<def>.",
        "Questo è meglio ricordarselo.",
        "Durante il fermento le Nefie sfornano",
        "oggetti di livello alto e un mucchio di",
        "punti di raccolta. Dura 4 o 5 giorni.",
    ],
}


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]

    # ⚠️ La prova che il testo e' allineato al lotto: stesso numero di righe per
    # blocco. Senza questa, una riga in piu' scivolerebbe su tutte le seguenti.
    per_blocco = {}
    for v in voci:
        per_blocco.setdefault(v["blocco"], []).append(v)
    for blocco, gruppo in per_blocco.items():
        attese = len(BLOCCHI[blocco])
        if attese != len(gruppo):
            raise SystemExit(f"blocco {blocco}: {attese} rese, {len(gruppo)} righe inglesi")

    for blocco, gruppo in per_blocco.items():
        for voce, resa in zip(sorted(gruppo, key=lambda v: v["riga"]), BLOCCHI[blocco]):
            voce["it"] = resa

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"{sum(1 for v in voci if v['it'])} rese su {len(voci)} righe")


if __name__ == "__main__":
    main(sys.argv[1])
