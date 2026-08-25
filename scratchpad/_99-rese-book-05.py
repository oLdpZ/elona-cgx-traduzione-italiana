# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %11 — la guida all'allevamento del barone Schmidt.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-05.py lavoro/book-005.jsonl

Valgono le regole di `_99-rese-book-02.py`.

⚠️ **Questo libro da' del VOI a chi legge**, non del tu: e' un manuale
commerciale, il barone si rivolge a una platea di clienti («Salve a tutti!»,
«Alla prossima, soci!»). Il plurale evita anche il genere, che in questo libro
tornerebbe addosso al lettore una decina di volte.

⚠️ Le insegne di sezione tengono la spaziatura di monte: quattro spazi alla
riga 129, il tab alla 176.

⚠️ `3rd Edition` diventa «terza edizione» per esteso: `ª` non esiste in CP932 e
l'albero di build lo perderebbe in silenzio.

Il lessico dal dizionario: `allevamento`, `allevatore`
(`map_user.hsp:412`), `mangime per il bestiame`, `Disinfetta i locali`,
`spazzola grande`, `Accarezza` (l'azione speciale, `skill.hsp:1281`),
`carne secca` (`db_item.hsp:144965`), `Ingegneria genetica`, `essiccatoio`
(`action.hsp:2714`), `atto`, `vento d'etere`.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

BLOCCO_11 = [
    # 1-3
    "Guida all'allevamento per pivelli",
    "\tterza edizione",
    "\tdel barone del bestiame Schmidt",
    # 4-13
    "Salve a tutti! Scrivo questa guida",
    "per lo stesso motivo per cui metto",
    "in giro le mandrie: i soldi. Di",
    "diritti d'autore ce n'è in",
    "abbondanza, per chi si prende il",
    "tempo di mettere penna su carta.",
    "Certo, i miei segreti non ve li",
    "posso dare TUTTI, se no chiudo",
    "bottega; ma se non vi do almeno le",
    "basi, il prossimo libro chi lo compra?",
    # 14-17
    "Tanto per cominciare, vi servono",
    "almeno ottantamila monete per",
    "comprare l'atto di un allevamento.",
    "Meno, se avete parlantina o bellezza.",
    # 18-25
    "Poi, atto alla mano, cercate il",
    "posto migliore che riuscite a",
    "trovare. Dentro le mura della città",
    "non si può, e comunque NON vi",
    "conviene gente che ficca il naso",
    "per sapere che cosa esattamente",
    "state allevando, o altri dilemmi",
    "morali del genere.",
    # 26-28
    "Arrivati sul posto scelto, basta",
    "Leggere l'atto (tasto r) e la",
    "terra è vostra.",
    # 29
    "-== Gioie e pericoli della monta ==-",
    # 30-33
    "Far riprodurre bene le bestie è",
    "un'arte fine, ed è quel che ci",
    "distingue dai selvaggi. E in un",
    "allevamento vale più che mai.",
    # 34-43
    "Ogni bestia messa alla riproduzione",
    "resta nell'allevamento e, col tempo,",
    "dà latte, uova, sterco e altre cose.",
    "E no, non starò a spiegarvi come",
    "faccia un mammifero a fare le uova,",
    "o come si munga una lucertola",
    "sputafuoco da venti tonnellate.",
    "Certe domande io non provo a",
    "rispondere, e francamente non",
    "dovreste farle neanche voi.",
    # 44-55
    "Ora, quella roba si vende a buon",
    "prezzo, ma il guadagno vero sta",
    "nella riproduzione, ed è giusto",
    "così: questo non è un campo,",
    "dopotutto. E con l'arrivo del vento",
    "d'etere far riprodurre è diventato",
    "semplicissimo. Non come ai vecchi",
    "tempi, quando toccava tener dietro",
    "ai lignaggi e alle stagioni degli",
    "amori, e sentire i richiami e i",
    "tonfi di due carnivori da venti",
    "tonnellate. Tutta. La. Notte.",
    # 56-60
    "Ma divago. Adesso basta metterla",
    "alla riproduzione e lasciarla stare.",
    "Presto ce ne saranno altre.",
    "Mitosi? Magia? Anche queste sono",
    "domande che è meglio non fare.",
    # 61-69
    "In generale gli animali selvatici",
    "(galline, pecore, conigli e simili)",
    "figliano come conigli. Eh eh. Altra",
    "cosa da tenere a mente: più un",
    "mostro è potente, più lento si",
    "riproduce nel vostro allevamento.",
    "Ricordatevelo quando scegliete che",
    "cosa allevare, se ve ne servono",
    "un fantastilione.",
    # 70-80
    "L'ho detto: per farle riprodurre",
    "basta lasciarle fare da sé. Dargli",
    "da mangiare è facoltativo (boh,",
    "mangeranno luce del sole, che ne",
    "so), ma se gli date del mangime",
    "per il bestiame si ingrassano.",
    "Oppure usate il registratore",
    "dell'allevamento per spargere quel",
    "mangime fra tutte le bestie che ci",
    "sono. Le riempie meno, ma il",
    "lavoro lo fa.",
    # 81-87
    "Se volete carne di qualità davvero",
    "buona, dovete spazzolarle ogni",
    "tanto. Prendete una spazzola",
    "grande e datevi da fare. Certo,",
    "per farlo dovete saper usare",
    "l'azione speciale Accarezza",
    "(tasto a).",
    # 88-101
    "Ogni tanto vi capiterà di far",
    "nascere una bestia che è brava",
    "davvero in qualcosa. Non parlo di",
    "matematica: magari è brava a fare",
    "litri e litri di latte, o montagne",
    "di uova. O magari ha buona carne",
    "o buona pelle.",
    "In che cosa è brava e in che cosa",
    "no lo capite stando attenti",
    "mentre la spazzolate. Quelle doti",
    "vengono fuori finché sta",
    "nell'allevamento. E se è lei alla",
    "riproduzione, farà nascere bestie",
    "con doti simili.",
    # 102-111
    "I nati nell'allevamento partono",
    "piccoli, quindi Lanciategli (tasto",
    "T) un po' di latte perché crescano",
    "grandi e forti. Se lo fate, la",
    "carne e il latte che danno",
    "migliorano.",
    "L'allevamento va tenuto pulito.",
    "Alle bestie serve spazio per fare",
    "le uova e, ehm, mungersi. Come",
    "fanno, se è tutto pieno di sterco?",
    # 112-120
    "Lasciare in giro lo sterco le fa",
    "ammalare, e allora ne fanno ancora",
    "di più. E fa ammalare anche le",
    "altre bestie dell'allevamento.",
    "Disinfettare i locali evita che",
    "succeda E cura le bestie malate.",
    "Ma se non ve lo potete permettere,",
    "allora conviene isolarle o",
    "abbatterle.",
    # 121-128
    "Conviene tenere d'occhio quante",
    "bestie ci sono nell'allevamento.",
    "Quando è pieno si riproducono più",
    "lentamente e danno meno latte e",
    "meno uova. Per me il numero giusto",
    "è venti. Vedete se riuscite a",
    "trovare un buon equilibrio anche",
    "nei vostri allevamenti.",
    # 129
    "    -== I frutti del vostro lavoro ==-",
    # 130-132
    "Ora, questi... figli si possono",
    "usare in parecchi modi, che qui",
    "elenco:",
    # 133-134
    "Interagirci (tasto i) e portarseli",
    "dietro in viaggio.",
    # 135-136
    "Ingegneria genetica senza nessun",
    "rischio per gli originali.",
    # 137-143
    "Guadagnarci portandoli a un",
    "mercante di schiavi se, aggiungo,",
    "sapete dove andare senza che",
    "nessuno faccia domande. Rendono di",
    "più se sono mansueti, quindi",
    "conviene averli remissivi e con un",
    "discreto legame con voi.",
    # 144-147
    "Oppure ammazzarli: le probabilità",
    "di ricavarne una carcassa buona",
    "sono molto migliori che a farla",
    "fuori là fuori.",
    # 148-155
    "Sacrificarli vivi al vostro dio:",
    "un classico degli dei da tempo",
    "immemorabile. A differenza dei",
    "pezzi di cadavere sull'altare, qui",
    "il peso non conta. Pare invece che",
    "il punteggio dipenda dal legame",
    "che hanno con voi e dalla qualità",
    "della loro carne.",
    # 156-160
    "Per inciso, ogni tanto le bestie",
    "dell'allevamento si agitano un po'",
    "quando una di loro viene ammazzata.",
    "Basta uscire dall'allevamento e",
    "rientrare, e le trovate calmate.",
    # 161
    "-== L'essiccatoio. Non si butta ==-",
    # 162-169
    "Un vantaggio dell'allevamento è",
    "avere un essiccatoio a disposizione.",
    "Io il mio l'ho messo nell'angolo",
    "di sud-est, così il vento porta la",
    "puzza lontano dalla villa. Immagino",
    "valga lo stesso per voi (sperate",
    "di sì). In qualunque altro mestiere",
    "una carcassa marcia è solo perdita.",
    # 170-175
    "Non in un allevamento, dove non si",
    "butta niente. Basta buttare la",
    "carne marcia nell'essiccatoio a",
    "stagionare, e in un attimo avrete",
    "deliziosa carne secca, leggera e",
    "ricercata dagli avventurieri!",
    # 176
    "\t-== Per concludere ==-",
    # 177-180
    "A questo punto un uomo saggio",
    "smetterebbe di scrivere e vi",
    "lascerebbe sognare. Immaginate le",
    "possibilità, e poi afferratele.",
    # 181-190
    "Nel mio prossimo libro, presto in",
    "vendita, metterò in luce i trucchi",
    "più sottili del mestiere: per dire,",
    "come si fa esattamente a impedire",
    "a una forza vivente di Distruzione",
    "e Morte da venti tonnellate, che",
    "sputa fuoco, di andarsene",
    "dall'allevamento dopo aver dato",
    "tutto alle fiamme e avervi divorati",
    "sul posto per aver chiesto la monta.",
    # 191
    "Alla prossima, soci!",
]

RESE = {"11": BLOCCO_11}


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
