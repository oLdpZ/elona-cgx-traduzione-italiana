# -*- coding: utf-8 -*-
"""52a, lotto `event-figli`: le 54 battute dei figli in `event.hsp`.

Nove scene casuali che capitano coi figli — il sogno per il futuro, il tesoro
raccolto per terra, da dove nascono i bambini, la battaglia immaginaria, il
disegno per terra, il senso dello studio, il soprannome da eroe, i vestiti
sbagliati, l'essere trattati da bambini. Ogni scena ha tre scelte per il
giocatore e due battute di risposta per ognuna: `txt A, B` ne sceglie una a caso.

⚠️⚠️ **Il figlio puo' essere maschio o femmina, e l'inglese non se ne accorge.**
`child` e' un personaggio con un sesso, e in inglese nessuna di queste battute lo
mostra. In italiano quasi tutte lo mostrerebbero: «sono stanco», «faro'
l'avventuriero», «troppo diverso dagli altri», «mi consideri adulto». Ogni resa
di questo lotto e' scritta per NON accordarsi col parlante — e dove la via corta
avrebbe accordato, la frase gira intorno all'ostacolo:

    I'm going to be an adventurer   ->  «Tanto andro' all'avventura»
    too different from everyone     ->  «non mi va di stonare in mezzo agli altri»
    recognize me as an adult        ->  «mi consideri una persona adulta»

💡 E' la stessa disciplina degli helper `_s(rc)`/`his(rc)` che il progetto toglie
da anni, ma al contrario: li' si toglie una funzione che l'inglese ha, qui si
evita un accordo che l'italiano aggiungerebbe da solo.

⚠️ Il giapponese ha gli helper del parlato infantile (`_ore`, `_yo`, `_nda`,
`_kana`, `_noka`, `_daro`, `_kure`) che segnano la personalita' del bambino;
l'inglese li ha persi tutti e l'italiano non li puo' rimettere — la resa va
sull'inglese, e aggiungere funzioni che l'inglese non ha e' vietato dalla rete
11. Il registro infantile si tiene col lessico, non con la morfologia.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\event.hsp")
FILE = "event.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

# riga: [(inglese, italiano), …] nell'ordine in cui stanno sulla riga
LOTTO = {
    # --- Sogno per il futuro
    1490: [("Hehehe...", "Eheheh..."),
           ("I don't mind if you imitate me!", "Se vuoi puoi copiare il mio sogno!")],
    1502: [("I'm serious!", "Ma dico sul serio!"),
           ("Is it no good?", "Non va bene?")],
    1513: [("I'll stop then", "E allora lascio perdere"),
           ("Huh?", "Uffa...")],
    # --- Tesoro ritrovato
    1595: [("I won't give it to you!?", "Non te lo do mica!"),
           ("Just show! I just want to show you!", "Te lo faccio solo vedere! Solo vedere!")],
    1606: [("You don't throw it away, do you?", "Non lo butti via, vero?"),
           ("It was hard to find...", "Ho fatto una fatica a trovarlo...")],
    1617: [("I am sorry...", "Scusa..."),
           ("It's not junk...", "Ma non e' spazzatura...")],
    # --- Le proprie radici
    1646: [("Gene...???", "I geni...???"),
           ("I do not know the meaning!", "Non ci ho capito niente!")],
    1656: [("Where does the white stork bring the baby from?",
            "E la cicogna da dove li prende, i bambini?"),
           ("It's a lie!", "Non e' vero niente!")],
    1667: [("I am shocked!", "Che colpo!"),
           ("Was I also a cabbage!?", "Allora venivo da un cavolo anch'io!?")],
    # --- Battaglia nella testa
    1696: [("Huh!", "Tie'!"),
           ("This guy is a formidable enemy!", "Questo qui e' un avversario tosto!")],
    1706: [("Do not disturb...", "Ed era sul piu' bello..."),
           ("But...", "M-ma...")],
    1717: [("I hate it because it's boring!", "No, e' una noia!"),
           ("Just studying tactical skills is enough!",
            "Per quello basta studiare le tattiche!")],
    # --- Il mondo e' una tela
    1746: [("I'm embarrassed...", "Che vergogna..."),
           ("Don't look at this...", "Non guardare senza chiedere!")],
    1757: [("I know that!", "Lo so gia'!"),
           ("I'll delete it now!", "E va bene, lo cancello subito!")],
    1768: [("I will refrain from studying...", "Studiare? Lascio perdere"),
           ("I don't want to draw a good picture...",
            "Non e' che voglio disegnare bene...")],
    # --- Il senso dello studio
    1797: [("I don't know what you mean...", "Non ho capito bene..."),
           ("I'm going to be an adventurer anyway, so it doesn't matter!",
            "Tanto andro' all'avventura, che me ne importa!")],
    1807: [("I thought I wouldn't have to study when I grew up...",
            "Pensavo che da grande non si studiasse piu'..."),
           ("Does that mean that there are things I can learn only now?",
            "Vuoi dire che certe cose si imparano solo adesso?")],
    1818: [("You think of children as decorations?",
            "Per te i figli sono un soprammobile?"),
           ("Isn't it embarrassing that you can only answer like that?",
            "Non ti vergogni a rispondere cosi'?")],
    # --- Il soprannome
    1847: [("I don't know what you mean...", "Non ha senso quello che dici"),
           ("I'll practice poses, so go over there!",
            "Devo provare la posa, vai di la'!")],
    1857: [("Your taste is so old-fashioned that I don't need it...",
            "Hai dei gusti antichi, lascia stare..."),
           ("Annoying!", "Che pizza, vai via!")],
    1868: [("Study, study, study! It's noisy!!", "Studia, studia! Che barba!"),
           ("Do you have enough vocabulary to preach?",
            "Ce l'hai il vocabolario per farmi la predica?")],
    # --- I vestiti sbagliati
    1897: [("You don't know...", "Lascia stare..."),
           ("I took the wrong person for advice!",
            "Ho chiesto un consiglio alla persona sbagliata!")],
    1908: [("There is a risk in the individual appearance!",
            "Se sono originale mi prendono in giro!"),
           ("I don't like being too different from everyone...",
            "Non mi va di stonare in mezzo agli altri...")],
    1919: [("Can I do it?", "Ce la faccio?"),
           ("It might be a good idea to try it for a while...",
            "Se lo dici tu, magari ci provo un po'...")],
    # --- Uomo marginale
    1948: [("Don't mislead me with difficult words...",
            "Non imbrogliarmi con le parole difficili..."),
           ("...Are adults struggling too?", "...Anche i grandi fanno fatica?")],
    1958: [("Damn it!", "Non prendermi in giro!"),
           ("Does that mean that a true adult can keep a cool face even if he's treated like a child?",
            "Vuoi dire che un vero adulto resta calmo anche se lo trattano da bambino?")],
    1969: [("A marginal man is someone who exists on the border of multiple groups. Especially in psychology, it refers to the gap between children and adults, that is, adolescents.",
            "L'uomo marginale e' chi sta sul confine fra piu' gruppi. In psicologia indica chi sta fra l'infanzia e l'eta' adulta, cioe' l'adolescente."),
           ("How far do I have to study before you will recognize me as an adult?",
            "Quanto devo studiare prima che mi consideri una persona adulta?")],
}

MOTIVO = (
    "Una delle nove scene casuali coi figli (`random_eventProc`): il giocatore "
    "sceglie fra tre risposte e il figlio replica, con due battute fra cui `txt` "
    "pesca a caso. ⚠️⚠️ La resa e' scritta per NON accordarsi col parlante, "
    "perche' `child` puo' essere maschio o femmina e in inglese nessuna di "
    "queste battute lo mostra: dove la via corta avrebbe accordato — «faro' "
    "l'avventuriero», «troppo diverso dagli altri», «mi consideri adulto» — la "
    "frase gira intorno all'ostacolo. ⚠️ Gli helper del parlato infantile "
    "(`_ore`, `_yo`, `_nda`, `_kana`) ci sono solo nel ramo giapponese: "
    "l'inglese li ha persi e l'italiano non li puo' rimettere, perche' "
    "aggiungere funzioni che l'inglese non ha e' vietato. Il registro si tiene "
    "col lessico."
)


def main() -> None:
    toppe, problemi = [], []
    for n, coppie in LOTTO.items():
        cerca = TESTO[n - 1]
        resa = cerca
        for inglese, italiano in coppie:
            atteso = f'cnvtalk("{inglese}")'
            if atteso not in resa:
                problemi.append(f":{n} non contiene {atteso[:60]!r}")
                continue
            resa = resa.replace(atteso, f'cnvtalk("{italiano}")', 1)
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII: {c!r}")
        # la riga deve restare dentro il ramo `if ( en )`, e le funzioni di
        # contenuto (`cdatan`, `cnvtalk`) devono essere le stesse di prima
        for funzione in ("cdatan", "cnvtalk"):
            if cerca.count(funzione) != resa.count(funzione):
                problemi.append(f":{n} il numero di `{funzione}` e' cambiato")
        quante = TESTO.count(cerca)
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": MOTIVO}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    battute = sum(len(c) for c in LOTTO.values())
    print(f"{len(toppe)} toppe, {battute} battute")

    uscita = REPO / "lavoro" / "_toppe-event-figli.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
