# -*- coding: utf-8 -*-
"""Le 11 descrizioni di razza — la colonna «Descrizione» della creazione.

Il tetto è quello di [[descrizioni_cm.py]], la rete 19: `talk_conv` manda a
capo a **62 caratteri** e la finestra regge **7 righe** prima che il testo tocchi
«Bonus attributi». Nessuna delle undici sfonda in inglese — vanno da 5 a 7 righe
— quindi qui non c'è nessuna scusa di monte: **7 righe è un tetto vero**.

⚠️ Il conto delle righe lo fa il simulatore, non `len(testo) / 62`: `talk_conv`
va a capo sulle parole.

Convenzioni prese dal glossario e dal gia' reso:

    Etherwind      -> «vento d'etere»    (gia' nel dizionario)
    Sierre Terre, Eyth Terre             nomi propri, invariati
    Elves          -> «elfi»             il nome che gli altri popoli danno agli Elea

⚠️ **Niente virgolette caporali** («»), che `guardie.py` proibisce, e niente
virgolette dritte, che dentro una stringa HSP andrebbero protette: dove
l'inglese vira sul discorso riportato la resa gira la frase.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import descrizioni_cm as D

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strumenti.accenti import degrada

ESTRAZIONE = "lavoro/_db_race.jsonl"
USCITA = "lavoro/fase4-db_race-002.jsonl"

RESE = {
    1052: (  # Yerles
        "Il giovane regno che venera l'antica civiltà scientifica di Eyth "
        "Terre ha preso potere a occidente. Realisti e materialisti, gli Yerles "
        "sanno però adattarsi a ciò che non comprendono, se giova al regno. "
        "La loro spiccata prontezza nell'imparare li rende adatti a ogni "
        "classe, e a ogni livello guadagnano punti abilità in più."
    ),
    1198: (  # Eulderna
        "Gli Eulderna sono una delle stirpi più antiche di Sierre Terre. "
        "Egoismo ed elitarismo guidano ogni pensiero di questi perfezionisti. "
        "Esperti di magia e di congegni magici, si prestano alle classi da "
        "incantatore o ibride. Hanno resistenza alla magia."
    ),
    1271: (  # Fata
        "Le fate sono graziose, misteriose e fragili. Rispetto agli umani hanno "
        "un talento superiore per la magia e per la schivata, ma la mancanza di "
        "forza fisica impedisce loro di portare anche il peso più piccolo: non "
        "possono indossare equipaggiamento oltre 1s. Le fate hanno resistenze "
        "eccellenti a tutti gli elementi."
    ),
    1555: (  # Nano
        "Il nano è figlio della terra. Duro e inflessibile come le montagne "
        "che ama, passa quasi tutta la vita sottoterra a scavare, fondere e "
        "forgiare. Qualcuno lascia le profondità per farsi avventuriero, "
        "sperando di mettere insieme le monete per fondare un clan. Bravo con "
        "la tecnica, resistente al buio e ai veleni."
    ),
    1624: (  # Juere
        "I Juere sono un popolo libero e selvaggio. Sprezzanti delle leggi "
        "altrui, che giudicano deboli, ne imparano in fretta trucchi e tecniche "
        "prima di rimettersi in cammino. L'orgoglio ne fa ottimi artisti, e "
        "sanno restare a lungo senza cibo. Agili di mano e arditi d'animo, non "
        "ce ne sono due uguali."
    ),
    1769: (  # Elea
        "Gli Elea, che gli altri popoli chiamano elfi, vivono quieti nelle loro "
        "foreste, lontano dagli uomini. Agili ed eleganti, i loro archi sono "
        "leggendari e i loro maghi hanno dimenticato più magia di quanta molti "
        "ne sapranno mai. Ogni tanto i giovani partono all'avventura, se non "
        "altro per riempire di ricordi una vita lunghissima."
    ),
    2114: (  # Chiocciola
        "C'è chi teme che un giorno il mondo passerà ai ratti, ma grazie al "
        "vento d'etere sembra che le chiocciole siano partite avanti. Lente e "
        "ottuse, anche le più possenti temono sale, aglio e burro. Eppure, per "
        "chi cerca una vera sfida, difficile trovare di peggio. Ti immagini le "
        "facce degli altri mentre avanzi verso di loro un millimetro alla volta?"
    ),
    2522: (  # Lich
        "Quando un mago potente si avvicina alla morte, il desiderio di durare "
        "lo spinge a tentare la via del lich. Di quanti ci provano ogni secolo, "
        "appena una manciata riesce. I più falliscono e muoiono, qualcuno "
        "riesce a metà: il passaggio gli ruba gran parte dei ricordi e delle "
        "capacità. La sua età giovane è una vita che ricomincia, ma il lich "
        "sa aspettare: ormai ha tutto il tempo del mondo."
    ),
    3349: (  # Goblin
        "Se i nani sono il popolo della terra, i goblin ne sono i parassiti. "
        "Goffi e brutti, ce n'è sempre di più ogni anno che passa. I loro "
        "corpi mingherlini guariscono in fretta, e vanno matti per il pesce. "
        "Gli occhietti tondi non si perdono nulla al buio, e non conviene "
        "azzuffarsi con loro: chissà che malattie si prendono."
    ),
    4105: (  # Golem
        "Creatura tutt'altro che naturale, il golem ha ricevuto dai flussi del "
        "vento d'etere una scintilla di coscienza. Forte come una coppia di "
        "buoi e duro come la roccia da cui è stato scolpito: a questo si "
        "ferma il suo repertorio. I maghi che lo fecero volevano braccia, non "
        "poeti. Può comunque migliorare, piano, e per fortuna non ha "
        "l'ingegno per annoiarsene."
    ),
    5350: (  # Mutante
        "Avvertimento vivente sui pericoli dell'ingegneria genetica, del caos e "
        "del perché una donna incinta non debba farsi cogliere dal vento "
        "d'etere: quasi tutti i mutanti hanno vite brevi e piene di dolore. Uno "
        "su mille però non solo sopravvive, ma prospera grazie ai mutamenti "
        "subiti. Guarisce in fretta per via del sangue accelerato, e parte "
        "quasi come un umano: la prova che una terza mano fa sempre comodo."
    ),
}


def main():
    voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding="utf-8") if l.strip()]
    per_riga = {v["riga"]: v for v in voci}
    lunghe = {v["riga"] for v in voci if len(v["en"]) > 80}

    guai = []
    for riga, resa in RESE.items():
        if riga not in per_riga:
            guai.append(f"la riga {riga} non sta nell'estrazione")
            continue
        righe = len(D.talk_conv(degrada(resa)))
        righe_en = len(D.talk_conv(per_riga[riga]["en"]))
        if righe > D.TETTO:
            guai.append(f"riga {riga}: {righe} righe, il tetto è {D.TETTO} (l'inglese ne fa {righe_en})")
    for riga in sorted(lunghe - set(RESE)):
        guai.append(f"la descrizione di riga {riga} non ha una resa")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("il tavolo non è a posto: non scrivo niente")

    fuori = []
    for riga, resa in sorted(RESE.items()):
        d = dict(per_riga[riga])
        d["it"] = resa
        fuori.append(d)
    testo = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in fuori)
    io.open(USCITA, "w", encoding="utf-8", newline="").write(testo)

    print(f"{len(fuori)} descrizioni in {USCITA}")
    for riga, resa in sorted(RESE.items()):
        print(
            f"   riga {riga}: it {len(D.talk_conv(degrada(resa)))} righe"
            f"  (en {len(D.talk_conv(per_riga[riga]['en']))})"
        )


if __name__ == "__main__":
    main()
