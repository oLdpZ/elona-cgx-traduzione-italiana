# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %23, %16 e %22 — la Barra, il testo sconnesso, il briefing.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-08.py lavoro/book-008.jsonl

Valgono le regole di `_99-rese-book-02.py`.

⚠️ **`%23` parla della Barra, che e' un pezzo di interfaccia**, non una
metafora: `skill.hsp` la chiama cosi' in una trentina di mosse
(`[Barra 100%] Fendente rapido`) e `screen.hsp:542` dice «Carica piena». Le
maiuscole sparse (Aura, Percepire, Culmine, Volonta') sono il vezzo del
personaggio e si tengono tutte: e' un invasato che scrive.

⚠️ **`%16` e' sconnesso di proposito** — righe che non si agganciano l'una
all'altra, un soggetto che cambia a meta' frase — e in italiano resta
sconnesso. Non e' un testo da aggiustare: e' il pezzo che monte usa per il
libro «tesi» senza senso, e una versione italiana che filasse liscia sarebbe
un'altra cosa.

⚠️ **I quattro ordini di `%22` sono i nomi che il giocatore vede sulla
bandiera**: `Assalto`, `Difesa`, `Intercettazione`, `Trattativa`
(`text.hsp:2457`-`:2466`). Non si inventano sinonimi militari piu' belli: chi
legge il libro poi cerca quelle quattro parole nel menu.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %23
BLOCCO_23 = [
    # 1-2
    "Arriva al mio livello",
    "\tdel Prescelto(?)",
    # 3-6
    "Quanti di voi, o quanto pochi, la",
    "riescono a Percepire? L'Aura che",
    "brilla ai piedi della gente. Quest'Aura",
    "è quella che io chiamo...",
    # 7
    "La Barra.",
    # 8-17
    "Essere così Speciale nella mia",
    "Capacità di Percepirla mi ha a lungo",
    "tormentato. Ma in verità Percepirla",
    "non è molto difficile: basta...",
    "guardare. Quando in combattimento",
    "le Emozioni salgono, guarda.",
    "Guarda l'Aura che cresce e tocca",
    "il suo Culmine. Vale anche il",
    "contrario: tenendo a freno le",
    "Emozioni, la Barra si abbassa.",
    # 18-24
    "Al Culmine la Barra luccica di un",
    "riverbero di perla. Versando la tua",
    "stessa Anima nelle Tecniche e",
    "concentrando ogni Fibra del tuo",
    "Essere, puoi Manifestare la tua",
    "Volontà nell'Unico Colpo Che",
    "Abbatterà Il Nemico.",
    # 25-27
    "...Che poi vuol dire che, quando",
    "è bianca, puoi tirare un attacco",
    "extra forte.",
    # 28-32
    "Ma non è tutto qui, perché la",
    "Barra Bianca non è l'ultimo grado.",
    "Oltre c'è la Barra Verde Pallido,",
    "che permette a chi la Usa di avere",
    "potere sul Tempo stesso.",
    # 33-36
    "Prima o poi capirai che cosa",
    "intendo. Se mai arriverai al mio",
    "livello, s'intende. E io sarò lì",
    "ad aspettare.",
]

# ---------------------------------------------------------------- %16
# ⚠️ Sconnesso di proposito: vedi il docstring.
BLOCCO_16 = [
    # 1-2
    "La tesi dell'astuto Mujaf",
    "\tdi <Caim>",
    # 3-23
    "Ho visto la città ridotta a un",
    "cumulo di macerie fumanti. Speravo",
    "solo in un'altra occasione.",
    "Fatto sta che non l'ho avuta. Perché",
    "lei ha combattuto i leoni una volta",
    "e un'altra, rifiutando di morire.",
    "Guarda, la gabbia toracica è ancora",
    "intatta. Non l'hanno intaccata.",
    "Come nuova. Roba da matti, per me.",
    "Ora, tu ricevi quattro opzioni.",
    "La prima è molto attraente e non",
    "proverà a ucciderti. Poi, stupenda...",
    "un carattere all'altezza del suo",
    "aspetto. La terza ha il vizio di",
    "poltrire. Per ultima, una maga",
    "fedele che per te camminerebbe",
    "sulla brace. Vorrei essere ovunque",
    "tranne che qui. Anzi, POSSO",
    "scappare. SUBITO. È ora di darsela",
    "a gambe. Vivo non mi prendete.",
    "Continuo a correre. Passo e chiudo.",
    # 24-40
    "10.000 monete d'oro. Più che",
    "abbastanza per lavare via tutto.",
    "Voglio dimenticare questi ricordi",
    "ancora vivi. Sembra ieri, quando",
    "è successo. Ma per quanto voglia",
    "dimenticare, non ci riesco.",
    "Avrei potuto fermare tutto quel",
    "che è successo? Tanto lei non",
    "torna più. Sarei impazzito a",
    "vedere la gente sanguinare e",
    "grattarsi via la faccia. Schegge",
    "di pelle per aria. È stato un bel",
    "mal di testa per tutti in città,",
    "dai reali ai contadini. Ora,",
    "se solo gli alieni fossero vicini",
    "turisti violenti che accumulano",
    "energia mutaforma. Aspettano. (Fine.)",
]

# ---------------------------------------------------------------- %22
# Il sottotenente Gornock: ordini secchi, seconda persona plurale.
BLOCCO_22 = [
    # 1-3
    "Istruzioni per la missione",
    "\ta cura di:",
    "\tsottotenente Gornock, Esercito Yerles",
    # 4-6
    "Nell'esercitazione di oggi voi",
    "avventurieri sarete mobilitati",
    "col mio plotone. Ai miei ordini.",
    # 7-10
    "Vedete questa? È la bandiera di",
    "comando. La userò per dare gli",
    "ordini tattici a ciascuno",
    "di voi.",
    # 11-12
    "Gli ordini sono semplici e sono",
    "soltanto quattro.",
    # 13-21
    "Il primo è Assalto: cercare e",
    "distruggere. Quando do quest'ordine,",
    "tutti voi dovete continuare a",
    "muovervi cercando nemici. Distruggete",
    "ogni nemico che incontrate. State",
    "all'attacco e inseguite i bersagli.",
    "Usate tutto quel che avete e non",
    "lasciate in piedi",
    "nessun nemico.",
    # 22-30
    "Poi c'è Difesa: non attaccate.",
    "Per nessun motivo dovete ingaggiare",
    "il nemico quando do quest'ordine.",
    "Sorvegliate i movimenti nemici,",
    "sabotate o distraete il nemico",
    "quando potete, ma non aprite il",
    "fuoco. Se vi sparano addosso,",
    "tenete la posizione come potete",
    "e aspettate nuovi ordini.",
    # 31-38
    "Terzo, Intercettazione: ingaggiate",
    "solo i nemici vicini. Ogni scontro",
    "deve restare a portata del",
    "comandante. Se io il nemico non lo",
    "vedo, non lo vedete nemmeno voi.",
    "Chiaro? Non allargatevi. Risparmiate",
    "le risorse e aspettate ordini nuovi.",
    "Non inseguite nemici fuori portata.",
    # 39-43
    "Per ultimo abbiamo Trattativa: non",
    "attaccate nessun nemico, ma parlate",
    "o cantate per spezzargli la volontà.",
    "Lo scopo è logorarli e farli",
    "ritirare.",
    # 44-48
    "Non siete addestrati, quindi le",
    "istruzioni che riceverete sono",
    "poche e semplici. Altri ordini",
    "li riceverete sul campo. Questo è",
    "tutto.",
]

RESE = {"23": BLOCCO_23, "16": BLOCCO_16, "22": BLOCCO_22}


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
