# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %0 %2 %3 %6 %15 %10 %12 %13 %18 %19 %20 %4.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-07.py lavoro/book-007.jsonl

Sono i libri brevi — i biglietti, i volantini, la lettera rovinata — piu' il
manuale del museo. Valgono le regole di `_99-rese-book-02.py`.

⚠️⚠️ **`%6` si rende dal giapponese, perche' l'inglese ha letto male.** Il
giapponese dice 目がまわる ripetuto tre volte: e' l'espressione idiomatica «mi
gira la testa», ed e' il libro che fa girare la testa a chi lo legge. Monte
inglese l'ha preso alla lettera — `Round Eyes!`, «occhi rotondi» — che in
inglese non vuol dire niente e in italiano meno ancora. E' la deroga di
`decisioni.md`: si deroga quando l'inglese perde quel che il giapponese ha.

⚠️ **`%12` e' una lettera rovinata, e i pezzi mancanti li ricostruisce il
giapponese.** L'inglese di `<damaged> himself out of hand.` non e' una frase:
il giapponese sotto dice 手は尽くした, «ho fatto tutto il possibile». Il segno
`<damaged>` diventa `<rovinato>` — e' una didascalia, non un nome. ⚠️ La
chiusa latina `Requiescat in pace...` si rende: il giapponese dice
安らかに眠れ, cioe' la frase comune, e in italiano la frase comune e' «riposa
in pace» (a differenza del `Philosophiae Doctor Magus` di `%7`, che e' un
titolo accademico e resta latino).

⚠️ **Niente participi riferiti a chi legge**, e in `%13` costa caro: l'inglese
apre con `You have been cordially invited hero` e prosegue con
`you have gotten a bit of a name for yourself`. In italiano il partecipio
sceglierebbe il genere del giocatore a ogni riga, quindi la frase si gira sul
sostantivo — «Invito cordiale a te, eroe», «Il tuo nome comincia a girare».

⚠️ La spaziatura in testa e' contenuto e si ricopia: i tre spazi dei passi di
`%4` (righe 33-42), i sei dell'insegna (48), i dodici dell'errata (79) e i
**due tab** della riga 80, che monte usa li' e solo li'.

Il lessico dal dizionario: `statuetta` (`command.hsp:4849`), `bacheca della
casa` (`db_item.hsp:144424`), `registratore di cassa`, `atto di museo`
(`text.hsp:909`), `museo`, `anima gemella`, `Palmia`, `Tyris del Sud`.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %0
# Le due righe del diario di un tale: il libro piu' corto del file.
BLOCCO_0 = [
    "Da oggi comincio a tenere un diario,",
    "ogni giorno!",
]

# ---------------------------------------------------------------- %2
# Il libro che compare quando la generazione di un oggetto fallisce: e' monte
# che parla al giocatore, non un personaggio.
BLOCCO_2 = [
    # 1
    "\tAutore: <Follia!>",
    # 2-6
    "Questo libro compare quando la",
    "generazione di un oggetto fallisce.",
    "Se lo trovi e hai idea di che cosa",
    "possa aver causato il difetto che",
    "l'ha fatto comparire, segnalalo.",
    # 7-11
    "Se non hai idea di che cosa possa",
    "averlo causato, non preoccuparti.",
    "Non dovrebbe influire in alcun modo",
    "sul gioco.",
    "--La direzione",
]

# ---------------------------------------------------------------- %3
BLOCCO_3 = [
    "Te l'avevo detto.",
]

# ---------------------------------------------------------------- %6
# ⚠️ Dal giapponese: 目がまわる, «mi gira la testa». Vedi il docstring.
BLOCCO_6 = [
    "Gira tutto, gira tutto, gira tutto",
]

# ---------------------------------------------------------------- %15
# La reclame per corrispondenza, in inglese finto-arcaico.
BLOCCO_15 = [
    # 1-2
    "Cerchi i Segreti dei Sotterranei?",
    "<Schmidt XVII, duca dell'Intrigo>",
    # 3-7
    "Allora manda dieci monete d'oro a:",
    "Pergamene Mensili dello Speleologo",
    "Presso:",
    "Samisel",
    "Tyris del Sud, Elona",
]

# ---------------------------------------------------------------- %10
# Il predicatore dell'acqua: invettiva, maledizioni bibliche.
BLOCCO_10 = [
    # 1-2
    "Sciacalli spreconi d'acqua! Maledetti!",
    "Di Schmidt il bandito dell'acqua",
    # 3-5
    "Da dove vengo io l'acqua è vita!",
    "Le pozze si difendono fino alla",
    "morte, fino all'ultima donna e bambino!",
    # 6-9
    "Arrivo in questo paese e che cosa",
    "vedo? Acqua, anzi, VITA, sprecata!",
    "Voi che vivete in tanta abbondanza",
    "ne buttate via da far peccato!",
    # 10-13
    "L'acqua andrebbe benedetta e offerta",
    "a tutti i vostri dei! Ma lo sapete,",
    "voi, quante cose si possono fare",
    "con l'acqua sporca?",
    # 14
    "Sospetto di no.",
    # 15-17
    "E non lo saprete mai, se continuate",
    "a buttarla via come sterco di",
    "cammello malato.",
    # 18-20
    "Che tutti gli sprecatori d'acqua",
    "appassiscano come erba nella siccità,",
    "e che i loro lombi diano sabbia!",
    # 21
    "Siate maledetti!",
]

# ---------------------------------------------------------------- %12
# La lettera rovinata del fratello di Rachel. I buchi restano buchi.
BLOCCO_12 = [
    # 1-2
    "[Non si capisce di chi sia]",
    "Del fratello di Rachel <rovinato>",
    # 3-4
    "<Nel libro marcio c'è una lettera>",
    "<La lettera è sbiadita dappertutto>",
    # 5
    "Rachel<rovinato> non dimenticherò.",
    # 6
    "Per trattenere il ricordo di<rovinato>",
    # 7-8
    "La tua malattia <rovinato>",
    "dalla medicina moderna.",
    # 9
    "<rovinato> ho fatto il possibile.",
    # 10
    "Io, senza<rovinato>",
    # 11
    "Perciò",
    # 12
    "il tuo ricordo per sempre<rovinato>",
    # 13
    "Il giardino segreto nella neve...",
    # 14-15
    "Il posto è a nord 2<rovinato>",
    "E da lì 4<rovinato>",
    # 16-17
    "Sorella mia<rovinato>",
    "Riposa in pace...",
]

# ---------------------------------------------------------------- %13
# L'invito del signore della piramide: solenne, antico, e sotto la cortesia
# c'e' una minaccia.
BLOCCO_13 = [
    # 1-2
    "Invito cordiale a te, eroe:",
    "rispondere non serve, ma preparati.",
    # 3
    "<Questo è scritto su papiro>",
    # 4-10
    "Il tuo nome comincia a girare,",
    "giovane creatura, e anche adesso ti",
    "stai facendo più forte. Presto io,",
    "nella mia età oltre ogni età, potrei",
    "non esserti pari. E, ragionevolmente,",
    "quel rischio non lo correrò. Però",
    "una sfida fresca ogni tanto mi piace.",
    # 11
    "Quindi ascolta.",
    # 12
    "Cerca la Piramide! Sfida il labirinto!",
    # 13-14
    "Certo, ti servirà un motivo più",
    "forte del mio semplice invito a sfida.",
    # 15-19
    "Che ne dici di un tesoro? Ah, lo",
    "sapevo. Nel mio Labirinto c'è molto",
    "tesoro, se riesci a trovarlo. Sta",
    "in mezzo a molto rischio, ma un",
    "premio senza rischio è freddo e vuoto.",
    # 20-23
    "E c'è anche quel che porto addosso",
    "io, benché sia giusto avvertirti",
    "che a questo gioco gioco da molto,",
    "molto tempo, e non ho ancora perso.",
    # 24-28
    "Ah, e un'altra cosa: se il tuo nome",
    "non è iscritto come si deve nel",
    "grande Libro dei Morti prima di",
    "entrare, quelli che stanno dentro",
    "provvederanno in fretta.",
    # 29
    "Affrontami, se ne hai il coraggio!",
]

# ---------------------------------------------------------------- %18
# Galateo del dono, da mercante girovago.
BLOCCO_18 = [
    # 1-2
    "Fare regali",
    "\tdi un mercante girovago",
    # 3-7
    "Che cosa fai quando vuoi fare un",
    "regalo a qualcuno? Ti capita di",
    "impigrirti e di darglielo in mano",
    "invece di posarglielo ai",
    "piedi?",
    # 8-12
    "Se è per una persona vicina, tipo",
    "un'anima gemella, o se hai una",
    "fretta tremenda, allora va bene.",
    "Ma molti anziani trovano piuttosto",
    "offensivo ricevere roba in mano.",
    # 13-16
    "In quasi tutte le zone è educato",
    "posare le cose ai piedi della",
    "gente. Certo, con i parenti non",
    "serve arrivare a tanto.",
    # 17-23
    "Una cosa da tenere a mente è che",
    "in certe parti del continente",
    "asseriano posare le cose ai piedi",
    "è maleducazione. Quando vai da",
    "quelle parti non devi prendertela",
    "se degli sconosciuti ti passano la",
    "roba in mano.",
    # 24-27
    "Come si dice: a Palmia fa' come",
    "fanno i palmiani. E ricorda: informati",
    "sempre sugli usi del posto prima",
    "di andarci!",
]

# ---------------------------------------------------------------- %19
# L'istruttore che spiega la coppia: parla a una classe, quindi voi.
BLOCCO_19 = [
    # 1-2
    "Esercizio di affiatamento",
    "\tdell'istruttore capo",
    # 3-5
    "Per la pratica di oggi vi metterete",
    "in coppia con un altro per formare",
    "una squadra.",
    # 6-7
    "Adesso prendetevi un compagno. Quello",
    "a sinistra comanda i movimenti.",
    # 8-13
    "Se combattete in coppia, guardate",
    "come si muove il vostro compagno.",
    "Se avete davanti uno forte, fate",
    "molta attenzione a come vi muovete",
    "durante lo scontro: vi garantisco",
    "che ne imparerete parecchio.",
    # 14-18
    "Quando arrivano i colpi, chi in",
    "quel momento ha più salute deve",
    "incassare per l'altro. E non",
    "scordatevi di dividere l'oro che",
    "raccogliete col compagno.",
    # 19-22
    "Camminate alla stessa velocità per",
    "non inciampare. Ehi, tu: non c'è",
    "bisogno di legarvi le gambe!",
    "Metti via quella corda.",
    # 23-24
    "Come? Non hai un compagno?",
    "E va bene, fai coppia con me.",
]

# ---------------------------------------------------------------- %20
# Edelia, cameriera dodicenne: educata, dà del voi al lettore.
BLOCCO_20 = [
    # 1-2
    "L'avventuriero trimestrale (prim. 518)",
    "\tdi Edelia, cameriera, 12 anni",
    # 3-6
    "Salve. Sono Edelia, la cameriera.",
    "Come state? Oggi vi porto consigli",
    "che spero vi tornino utili nelle",
    "vostre avventure.",
    # 7-11
    "Ci sono molti tipi di mobili di cui",
    "nessuna casa può fare a meno. In",
    "nessuna casa dovrebbero mancare",
    "letti, utensili da cucina e",
    "contenitori.",
    # 12-17
    "Certi mobili, come le librerie, si",
    "usano come attrezzo (tasto t). Altri",
    "invece, per esempio i frigoriferi,",
    "sono contenitori che si aprono",
    "(tasto o). Tornano utili per tenere",
    "la casa in ordine.",
    # 18-21
    "Prima di comprare un atto nuovo e",
    "traslocare per cambiare aria, che ne",
    "dite di dare un'occhiata a casa",
    "vostra e provare a sistemarla?",
]

# ---------------------------------------------------------------- %4
# Il curatore Schmidt: pomposo, sprezzante verso gli avventurieri, e alla fine
# vende il suo museo. Dà del voi, come il barone dell'allevamento.
BLOCCO_4 = [
    # 1-2
    "Manuale di gestione del museo Mk.III",
    "Scritto dal curatore Schmidt",
    # 3
    "Così volete gestire un museo, eh?",
    # 4-8
    "Signorino o signorina, per comprare",
    "un atto simile ci vuole un bel po'",
    "di capitale; ma se avete tempo,",
    "pazienza e denaro, questo vecchio",
    "curatore vi aiuta con questo manuale.",
    # 9-13
    "Nella vostra sfrenata e assai",
    "edonistica distruzione della flora",
    "e della fauna locali (d'ora in poi",
    "in questa guida: avventura) vi sarà",
    "forse capitato di trovare:",
    # 14-15
    "Oggetto a) Statuetta di <fauna>",
    "Oggetto b) Carta di <fauna>",
    # 16-24
    "Se è così, forse ci avete dato",
    "appena un'occhiata prima di",
    "ficcarle nel sacco del malloppo e",
    "tornare all'avventura.",
    "Le avrete vendute di sicuro per",
    "altri boccali di birra e cosciotti",
    "di montone; ma i più svegli fra voi",
    "forse le hanno messe da parte",
    "chiedendosi: perché ce le hanno?",
    # 25
    "La risposta: vanità! E magia!",
    # 26-28
    "Ed è da queste due cose che noi",
    "ricaveremo un guadagno. Ed è così",
    "facile che ci riesce un avventuriero!",
    # 29-31
    "Comunque, per sicurezza, ho messo",
    "per iscritto i passi esatti, così da",
    "ridurre gli incidenti spiacevoli.",
    # 32-34
    "Passo 1) Comprate un atto di museo.",
    "   È questo il passo che separa i",
    "   pesci piccoli da chi fa sul serio.",
    # 35-38
    "Passo 2) Recitate l'atto (tasto r)",
    "   nel punto del mondo dove volete",
    "   che sorga il museo. Lasciate",
    "   costruire agli gnomi: fanno presto.",
    # 39-42
    "Passo 3) Disponete con gusto tutte",
    "   le carte e le statuette che avete",
    "   trovato dentro il museo. L'ordine",
    "   è una virtù, ma non è d'obbligo.",
    # 43
    "Passo 4) Guadagno!",
    # 44-48
    "Per l'impianto di base dovrebbe",
    "bastare. Se volete altre notizie su",
    "questioni particolari, non dovete",
    "che continuare a leggere!",
    "      -== Note e avvertenze ==-",
    # 49-51
    "Avere più di un museo si può,",
    "certo, ma solo il primo vi farà",
    "guadagnare qualcosa.",
    # 52-53
    "Le statuette valgono comunque più",
    "delle carte, quasi sempre.",
    # 54-56
    "Non ammucchiate più oggetti sulla",
    "stessa casella. È del tutto",
    "poco professionale e inutile.",
    # 57-67
    "Più il mostro è potente, più valgono",
    "la sua carta e la sua statuetta.",
    "Rare sono le statuette con un Nome",
    "o un Titolo sopra. Queste cosiddette",
    "statuette Uniche sono le migliori.",
    "E per incoraggiare più musei a",
    "esporle, ho creato un fondo che",
    "premia i musei in base al numero",
    "di statuette Uniche in mostra,",
    "con versamento il primo di",
    "ogni mese.",
    # 68-72
    "Tornando al punto: avere la carta",
    "di un drago è bello, averne dieci",
    "è pacchiano. La varietà è la chiave.",
    "Più doppioni avete,",
    "meno valgono.",
    # 73-78
    "Ah, un'altra cosa... gli gnomi che",
    "vi costruiscono il museo hanno",
    "gusti, ehm, un po' stretti. Forse vi",
    "toccherà portare una <bacheca della",
    "casa> o un <registratore di cassa>",
    "per scolpirlo nella vostra visione.",
    # 79
    "            -== Errata ==-",
    # 80-82   ⚠️ i due tab della riga 80 sono di monte, e restano
    "Costo base: \t\t140.000 oro",
    "Manutenzione:         1.500 oro/mese",
    "Rendita per rango:      100 oro/mese",
    # 83
    "**Le cifre qui sopra sono indicative",
    # 84
    "Buona curatela!",
]

RESE = {
    "0": BLOCCO_0, "2": BLOCCO_2, "3": BLOCCO_3, "6": BLOCCO_6,
    "15": BLOCCO_15, "10": BLOCCO_10, "12": BLOCCO_12, "13": BLOCCO_13,
    "18": BLOCCO_18, "19": BLOCCO_19, "20": BLOCCO_20, "4": BLOCCO_4,
}


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
