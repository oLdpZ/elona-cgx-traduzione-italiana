# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %9, %27 e %31 — i tre manuali di mestiere.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-02.py lavoro/book-002.jsonl

⚠️ **Il metro e' 43 caratteri, e si misura sulla forma degradata**: nell'albero
di build `è` diventa `e'` (`strumenti/accenti.degrada`), quindi ogni accento
costa un carattere in piu'. Qui il conto si fa **prima** di scrivere il lotto,
con lo stesso degrado, e una riga oltre il tetto ferma tutto. L'inglese di monte
non passa mai 39: le righe fra 40 e 43 si stampano a parte, come fa la rete.

⚠️ **Il conto delle righe di ogni paragrafo resta quello di monte.**
`dati_applica` sostituisce righe senza aggiungerne, e le righe vuote fra un
paragrafo e l'altro non sono nel lotto: dentro un paragrafo il testo si
ridistribuisce, da un paragrafo all'altro no. I confini si leggono con
`scratchpad/_99-para-book.py`.

⚠️ Niente aggettivi o participi riferiti a chi legge: il genere del giocatore
non si conosce. «occhio a non farti mangiare», non «sta' attento»; «se ne hai
in quantita'», non «se sei fornito».

Il lessico viene dal dizionario, non dall'inglese di monte:
`Giardinaggio`, `Scavo`, `Pesca` (`skill.hsp`), `sintesi` (il comando di
`text.hsp:137`), `vaso della fusione`, `frigo portatile`, `pulce d'acqua`,
`pastura`, `cianfrusaglie`, `attrezzi per le colture`, `canna da pesca`,
`quadrifoglio`, `ghianda dorata`, `lingotto d'oro`, `cassaforte`, `argilla`,
`Costituzione`; e i tipi di Nefia si dicono come `text.hsp:50` — **grotta,
lago, foresta, tana, forte, torre, cimitero, miniera** — al plurale «le Nefie»,
che e' la forma di `chat.hsp:14032`.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %9
# «Easy Gardnin'», la contadina Valentina Schmidt. L'inglese le da' una parlata
# rustica che il giapponese non ha (il 農民 giapponese e' compito): la parlata
# e' una scelta dell'autore inglese, non una svista, e in italiano si tiene.
BLOCCO_9 = [
    # 1-2  titolo e autore (il tab della riga 2 e' di monte)
    "Coltivare l'orto è facile",
    "\tAutore: Valentina Schmidt",
    # 3-8
    "Ti frulla in testa di farti da mangiare",
    "con le tue mani? Che tu voglia solo",
    "trastullarti con qualche erbetta, o",
    "tirar su roba seria come ho fatto io",
    "per tutta la vita, hai preso il libro",
    "giusto.",
    # 9-28
    "Per prima cosa, devi scegliere quando",
    "e dove piantare i semi. Il momento",
    "buono è quando piove, e il posto",
    "buono è una casella di campo. I semi",
    "piantati sotto la pioggia appassiscono",
    "meno spesso; e quelli piantati sul",
    "campo che trovi nelle fattorie e negli",
    "allevamenti abbandonati, dopo il",
    "raccolto lasciano più spesso un nuovo",
    "germoglio.",
    "Piantati i semi, non resta che",
    "guardarli crescere. Se ti va bene e",
    "fila tutto liscio, il seme mette",
    "radici sotto terra e nel giro di",
    "mezzo mese o un mese intero dà",
    "frutto. Se sei ai primi passi e di",
    "Giardinaggio ne mastichi poco, ti",
    "appassirà quasi tutto prima del",
    "raccolto; ma non buttarti giù per",
    "questo.",
    # 29-37
    "Per ultima viene la parte che, credo,",
    "piace a tutti quanti: il raccolto.",
    "Prima però sappi che una pianta che",
    "ha dato frutto non appassisce più",
    "finché non la raccogli. E quel che",
    "raccogli cambia con la stagione:",
    "la stessa pianta, dallo stesso seme,",
    "la stagione dopo ti dà un'altra",
    "roba.",
    # 38-42
    "È nel raccolto che la tua abilità",
    "conta di più. Se ne hai in quantità,",
    "vedrai che dopo il raccolto la pianta",
    "lascia più spesso un germoglio",
    "dietro di sé.",
    # 43-49
    "Lascia della roba organica su un",
    "compost per qualche giorno e diventa",
    "concime. Usalo sulle piante e te le",
    "ritrovi cresciute in un attimo: sì,",
    "e dico sul serio, in un attimo. Non",
    "gli resta manco il tempo di",
    "appassire.",
    # 50-56
    "Nel campo trovi anche gli attrezzi",
    "per le colture. Usali per far",
    "crescere solo certi tipi di piante:",
    "così raccogli solo certi oggetti.",
    "Provali di persona per vedere quale",
    "trattamento fa venire su che",
    "cosa.",
    # 57-65
    "Man mano che il Giardinaggio sale,",
    "sale anche la qualità della frutta e",
    "della verdura che raccogli. E questo",
    "vuol dire che ti arriveranno branchi",
    "di maledetti animali selvatici, fitti",
    "come yeek a Yowyn: occhio a non",
    "farti mangiare. Cacciali via una",
    "volta e per un po' non tornano,",
    "però.",
    # 66-69
    "In Tyris del Nord si trovano semi e",
    "raccolti d'ogni sorta, uno più strano",
    "dell'altro. Buona fortuna col tuo",
    "campo, e buona zappata!",
    # 70-75
    "P.S. Ho sentito dire che pure il",
    "raccolto andrebbe fatto quando piove.",
    "Funziona davvero? Mio padre giurava",
    "che lo zio di suo padre lo giurava a",
    "sua volta, ma che io sia dannata se",
    "lo so.",
]

# ---------------------------------------------------------------- %27
# «You dig mining?», Borzoi J. Hammer: spaccone, si vanta e parla a raffica.
BLOCCO_27 = [
    # 1-2
    "Lo scavo è una bellezza",
    "\tAutore: Borzoi J. Hammer",
    # 3-4
    "Qui Borzoi. E quando si parla di",
    "scavo, il migliore sono IO.",
    # 5-9
    "Ti piace scavare? A me da matti.",
    "Allena la Costituzione. Trovi roba.",
    "E soprattutto: se non c'è la strada,",
    "puoi sempre",
    "APRIRTELA.",
    # 10-12
    "E lo sapevi che scavando in posti",
    "diversi salta fuori roba diversa?",
    "Scommetto di no.",
    # 13-21
    "Le Nefie grotta e lago sono piene",
    "di minerali, quindi è lì che devi",
    "andare se vuoi qualcosa da offrire",
    "agli dei della Terra o della",
    "Guarigione. E se non è il tuo",
    "genere, dagli una lucidata buttando",
    "i grezzi nel vaso della fusione:",
    "dopo si vendono per una bella",
    "cifra.",
    # 22-30
    "Le Nefie foresta sono piene di cibo",
    "che non trovi da nessun'altra parte.",
    "Le ghiande non marciscono mai, così",
    "te ne puoi tenere in tasca sempre.",
    "E poi ci sono le ghiande dorate, che",
    "valgono. Oro! Le avrà nascoste lì",
    "qualche scoiattolo, o roba simile.",
    "Con un po' di fortuna ti capita pure",
    "un quadrifoglio.",
    # 31-39
    "Le Nefie forte e torre sono fatte",
    "di pietra, e quindi indovina che",
    "cosa ricavi scavando lì? Pietra!",
    "Dicono che ci si possano fare delle",
    "sculture con la, ehm, fusione degli",
    "oggetti; ma io di roba artistica",
    "non ci capisco niente. E poi trovi",
    "le casseforti che la gente ci ha",
    "nascosto secoli fa.",
    # 40-44
    "Le Nefie tana hanno dentro i resti e",
    "le uova di quel che ci viveva. E una",
    "montagna di merda, che ti tocca",
    "spalare tutta prima di trovare",
    "qualcosa di buono.",
    # 45-52
    "Nei cimiteri la gente i morti se li",
    "mette dentro i muri. Sarà rimasta",
    "l'abitudine di chi la roba se la",
    "nascondeva nei muri. Scava un po'",
    "e trovi offerte e bare. Se uno si",
    "becca una maledizione a farlo,",
    "chiedi? Ma va'. Chi non spreca,",
    "non manca.",
    # 53-57
    "Le miniere danno minerali, ma non",
    "quelli normali: quelli li avranno",
    "esauriti, se no non sarebbero",
    "diventate Nefie, no? Però qui c'è un",
    "sacco di argilla per la ceramica.",
    # 58-66
    "Vediamo... ah, giusto. Le città.",
    "Scava lì e ti capitano le monete e i",
    "lingotti d'oro che la gente si è",
    "messa da parte. Perché i soldi non",
    "li puoi tenere nella credenza: quella",
    "te la rubano tutta intera, contenuto",
    "compreso. E allora è nei muri che",
    "quella gente si tiene i risparmi di",
    "una vita.",
    # 67-68
    "E allora che aspetti?",
    "Comincia a scavare!",
]

# ---------------------------------------------------------------- %31
# «Fishing Introduction». Il titolo e' anche il nome dell'oggetto in
# `db_item.hsp:135737`, gia' reso «introduzione alla pesca»: qui va uguale.
BLOCCO_31 = [
    # 1-2
    "Introduzione alla pesca",
    "\tAutore: un pescatore orgoglioso",
    # 3-6
    "Ammazzi il tempo e prendi pesci!",
    "Due piccioni con una fava!",
    "Ti ho già preso all'amo?",
    "Allora continua a leggere!",
    # 7-9
    "Per prima cosa ti serve l'abilità",
    "Pesca. Non ce l'hai? Fattela",
    "insegnare dall'istruttore di Vernis!",
    # 10-15
    "Poi ti tocca comprare una canna da",
    "pesca e l'esca. Per cominciare, la",
    "pulce d'acqua è quella giusta. Con",
    "la sintesi (shift+b) attaccala alla",
    "canna. Una pulce d'acqua basta per",
    "15-24 lanci.",
    # 16-24
    "Le esche care e buone non funzionano",
    "se la Pesca non è all'altezza. Come",
    "regola, puoi passare all'esca",
    "superiore ogni 10 livelli di",
    "abilità. Se tiri su solo",
    "cianfrusaglie, vuol dire che quella",
    "esca ti chiede più abilità di quanta",
    "ne hai. E le cianfrusaglie sono",
    "cianfrusaglie: non servono a nulla.",
    # 25-29
    "Quanto al pesce: quel che ti frutta",
    "quando lo vendi dipende da quanto è",
    "grosso e da quanto pesa. La misura di",
    "quello che abbocca, però, non la",
    "scegli tu: decide Ehekatl!",
    # 30-37
    "Il pesce va a male in circa 8 ore,",
    "quindi conviene cucinarlo, e",
    "cucinarlo spesso. Oppure portarlo in",
    "giro nel frigo portatile. E se hai",
    "più pesce di quanto ne puoi portare",
    "(caspita!), mettilo in una pozza",
    "d'acqua per terra: lì non marcisce",
    "mai.",
    # 38-46
    "A proposito dei pesci nella pozza:",
    "con loro si possono fare dei giochi.",
    "A me piace dargli la pastura, fatta",
    "nel vaso della fusione. Così il",
    "pesce migliora di qualità, e ogni",
    "tanto ti sputa fuori pure un oggetto",
    "utile! Se sei di quelli che ai propri",
    "pesci non dà mai da mangiare, ti",
    "stai perdendo il bello!",
]

RESE = {"9": BLOCCO_9, "27": BLOCCO_27, "31": BLOCCO_31}


def misura(riga):
    """La lunghezza che la riga avra' nell'albero di build."""
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
