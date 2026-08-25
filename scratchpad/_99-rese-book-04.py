# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %30, %25 e %24 — la lettera del padre, il diario, la bara.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-04.py lavoro/book-004.jsonl

Valgono le regole di `_99-rese-book-02.py`. In piu':

⚠️⚠️ **`%30` non dice «figlio», e la deroga e' misurata sul giapponese.**
L'inglese apre con `Son,` e piu' avanti aggiunge «whatever you are»; il
giapponese dice 愛するわが子へ — 「わが子」 e' **la mia creatura**, senza genere,
e la chiusa giapponese non ha nessun «qualunque cosa tu sia». In italiano
«figlio» sceglierebbe un genere che ne' monte ne' il gioco conoscono: la
lettera si apre con «Tesoro mio,», che regge per tutt'e due. E' la deroga gia'
dichiarata in `decisioni.md` («si deroga quando l'inglese perde informazione
che il giapponese ha»), applicata al rovescio: qui l'inglese **aggiunge** un
genere che il giapponese non ha.

⚠️ `%30` rientra di **quattro spazi** l'inizio di ogni paragrafo (monte lo fa
al posto del 　 giapponese) e `%24` tiene il tab sulle righe 2 e 3: la
spaziatura in testa e' contenuto e si ricopia.

Il lessico dal dizionario: `Disarmo trappole` e `Percezione oggetti`
(`skill.hsp:317`, `:574`), `individuazione degli oggetti` (`text.hsp:987`),
`moneta di bronzo`, `Diario` (`command.hsp:3120`), `Mostra le statistiche`
(la voce del menu, `config.hsp:588`), `informatore`, `negromanzia`, `bara`,
`cristallo di mana`, `Alchimia`, `non morti`, `nanomacchine`.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %30
# La lettera di un padre in pensiero al figlio che se ne va di casa. E' il
# libro che spiega i tipi di incarico, quindi i nomi delle categorie devono
# dire quel che il giocatore vede in bacheca.
BLOCCO_30 = [
    # 1-2
    "Consigli sugli incarichi",
    "\tAutore: un padre in pensiero",
    # 3-10
    "Tesoro mio,",
    "    So che ti stai preparando ad",
    "andartene. Sono riuscito a mettere",
    "insieme qualche soldo: lo trovi in",
    "fondo alle tue cose. Dovrebbe",
    "bastarti finché non ti fai un",
    "guadagno tuo prendendo incarichi",
    "nelle città.",
    # 11-12
    "    Sappi però che gli incarichi",
    "sono di parecchi tipi.",
    # 13-21
    "- Procurare un oggetto",
    "    Il trucco è avere l'oggetto",
    "prima di prendere l'incarico.",
    "Di solito è roba che si trova per",
    "terra fuori città o si compra",
    "nei negozi.",
    "E se vai fuori città, non stare a",
    "combattere ogni animale selvatico",
    "che incontri.",
    # 22-30
    "- Farsi dare un oggetto da qualcuno",
    "    Chiedi a una guardia dove trovi",
    "la persona che ha l'oggetto. Poi",
    "vai da lei e prova a scambiarlo",
    "con qualcosa che hai tu.",
    "Oppure procuratelo dove ti pare:",
    "fuori città o in un negozio, chi",
    "ha dato l'incarico non nota la",
    "differenza.",
    # 31-39
    "- Preparare un piatto cucinato",
    "    Finché fai fatica a mangiare tu,",
    "procurarti gli ingredienti e cuocere",
    "il piatto che chiedono è dura.",
    "Prendi questi incarichi quando non",
    "sei alle strette. E con un po' di",
    "fortuna l'ingrediente che ti serve",
    "lo trovi in un negozio in",
    "città.",
    # 40-63   (monte tiene raccolto e mostri in un paragrafo solo)
    "- Raccogliere i frutti della terra",
    "    Sono pieni di animali selvatici,",
    "quindi devi almeno essere in grado",
    "di tenerli a bada.",
    "Vanno bene per allenarsi, perché",
    "di roba da strappare dal terreno",
    "ce n'è parecchia.",
    "Supera di parecchie volte la quota",
    "e ti pagano di più. A volte ti danno",
    "anche una moneta di bronzo.",
    "Ma andare oltre, quando si è agli",
    "inizi, è dura.",
    "Se ti scordi dov'è la cassa delle",
    "consegne, niente panico: cercala",
    "in giro col tasto *.",
    "- Abbattere mostri",
    "    Prima di prenderli, mettiti",
    "addosso un'armatura decente da capo",
    "a piedi. Se hai un compagno,",
    "equipaggia anche lui passandogli",
    "roba mentre ci interagisci",
    "(tasto i). Se non lo fai, questi",
    "incarichi TI AMMAZZANO. Sì, anche",
    "i più facili.",
    # 64-81
    "- Recapitare un oggetto",
    "    Per questi devi andare in",
    "un'altra città. Parti con cibo a",
    "sufficienza e in grado di",
    "combattere, e sapendo dove sei e",
    "dove stai andando.",
    "Nella città d'arrivo, chiedi alle",
    "guardie dove sta chi deve ricevere",
    "la consegna. Se non consegni in",
    "tempo, ti accusano di esserti",
    "intascato l'oggetto.",
    "- Fare da scorta",
    "    Anche qui si va in un'altra",
    "città. Se chi scorti muore,",
    "l'incarico è fallito. Rendono bene",
    "se la strada è corta e il cliente",
    "non corre nessun pericolo",
    "particolare.",
    # 82-86
    "- Togliere buche e mine",
    "    Senza Disarmo trappole non duri",
    "a lungo. Se no, servono magie o",
    "oggetti che permettano di percepire",
    "o individuare gli oggetti.",
    # 87-94
    "- Esibirsi",
    "    Sono difficili se non sai suonare,",
    "predicare o ballare. Se uno di",
    "livello alto ti vede fare una",
    "figuraccia, può ammazzarti. Quindi,",
    "anche se sai esibirti, all'inizio",
    "fallo solo davanti ai mendicanti e",
    "ai vecchi, finché non ci prendi mano.",
    # 95-101
    "    Quel che so io finisce qui.",
    "A sud di Vernis c'è un seminario",
    "dove tengono corsi di ogni genere:",
    "quando con gli incarichi hai messo",
    "da parte qualche soldo, faresti",
    "bene ad andarci presto, invece",
    "che tardi.",
    # 102-105
    "    Però non c'era bisogno di",
    "litigare così tanto con tua madre",
    "solo perché non ti lasciava tenere",
    "un putit.",
    # 106-115
    "    Se le cose non ti vanno come",
    "vorresti, non fare la testa dura:",
    "torna a casa. Ti conosco: sei capace",
    "di buttarti giù e finire a chiedere",
    "l'elemosina per strada, e io sto in",
    "pensiero. Fa' attenzione là fuori,",
    "e guardati le spalle: di gente che",
    "campa alle spalle dei più deboli",
    "in giro ce n'è",
    "parecchia.",
    # 116-119
    "    E sappi anche questo: io, e",
    "naturalmente anche tua madre,",
    "non desideriamo altro che la tua",
    "felicità.",
    # 120-121
    "Con affetto,",
    "tuo padre",
]

# ---------------------------------------------------------------- %25
# Il giornalista che spiega il Diario. Registro spavaldo, da reclame.
BLOCCO_25 = [
    # 1-2
    "I segreti del diario",
    "\tAutore: un giornalista VERO",
    # 3-7
    "Vedo che hai messo le mani",
    "sull'ultima moda che non può",
    "mancare in nessuna casa: il Diario",
    "che scrive da sé. Ma lo stai",
    "usando come si deve?",
    # 8-11
    "Il diario non elenca soltanto gli",
    "incarichi che hai preso: di",
    "ciascuno riporta anche quanto è",
    "difficile.",
    # 12-20
    "Il livello (Lv) che vedi scritto è",
    "quello del mostro da abbattere,",
    "maaa non è detto che tu debba",
    "essere di quel livello per farlo",
    "fuori. Con le armi giuste addosso,",
    "ce la puoi fare, ehm, sul 60% del",
    "livello del mostro? E poi non tutti",
    "gli incarichi vogliono un",
    "combattimento.",
    # 21-25
    "Il diario, poi, tiene il conto da",
    "solo di quante volte chi lo porta",
    "ha fatto una certa cosa.",
    "Accendi Mostra le statistiche nelle",
    "impostazioni e sei a posto.",
    # 26-31
    "Ha anche un collegamento con gli",
    "informatori delle città, così puoi",
    "controllare che cosa combinano i",
    "colleghi mentre giri. Ah, e ci",
    "trovi pure le quote della gilda e",
    "i gradi.",
    # 32-35
    "Insomma: dagli un'occhiata quando",
    "non ti ricordi più dove dovevi",
    "andare, o quando ti va di vedere",
    "come stai andando.",
]

# ---------------------------------------------------------------- %24
# Il negromante annoiato: cortese, compiaciuto, e parla di cadaveri come un
# cuoco parla di ricette. Le righe 2 e 3 tengono il tab di monte.
BLOCCO_24 = [
    # 1-3
    "Manuale di negromanzia",
    "\tscritto da",
    "\tun negromante annoiato",
    # 4
    "Gli scacchi hanno stancato.",
    # 5-9
    "Anche la negromanzia sta in fretta",
    "diventando un'arte dimenticata, e",
    "questo non va: quindi, caro lettore,",
    "forse posso insegnartene",
    "un paio.",
    # 10-14
    "Per cominciare, metti in una bara",
    "un pezzo di mostro. Poi, con un",
    "cristallo di mana, dai al corpo la",
    "forma che vuoi usando l'Alchimia.",
    "Infine, guarnisci con cattiveria.",
    # 15-26
    "Non c'è altro, davvero, se quel che",
    "vuoi è un esercito di non morti",
    "prodotti in serie. Ma per una vera",
    "opera d'arte servono gusto raffinato,",
    "conoscenza completa della",
    "negromanzia e anni di esperienza.",
    "Scegliere il pezzo di mostro",
    "perfetto non è certo lavoro da",
    "principianti.",
    "E le nanomacchine speciali e i",
    "batteri che servono, di questi",
    "tempi sono difficili da trovare.",
    # 27-32
    "Tieni solo a mente che da un pezzo",
    "di mostro di bassa qualità non",
    "esce niente di grosso. Lo stiri,",
    "sì, ma fino a un certo punto: poi",
    "comincia a crollare su se",
    "stesso.",
    # 33-41
    "I non morti che hai fatto si",
    "possono ritoccare aggiungendo un",
    "altro pezzo di mostro. Come vengono",
    "ritoccati dipende dal pezzo che",
    "aggiungi, quindi conviene provare",
    "e riprovare. Niente paura: se il",
    "risultato non ti piace, puoi sempre",
    "ritoccare di nuovo con un pezzo",
    "diverso.",
    # 42-50
    "Questi non morti non hanno la",
    "capacità di pensare, e restano lì",
    "impalati finché non ricevono un",
    "ordine chiaro da te. Ricordati di",
    "dirgli quali umani devono",
    "attaccare. E se abbattono qualcosa,",
    "ti prendi buona esperienza e ti",
    "diverti senza muovere",
    "un dito.",
    # 51-56
    "Nel numero c'è la forza. Fanne",
    "abbastanza e potrai rimpiazzare",
    "subito quelli che cadono in",
    "combattimento. Ne viene fuori",
    "un'orda implacabile che schiaccerà",
    "i nemici senza pietà.",
    # 57-68
    "Puoi curarli a prezzo della tua",
    "stessa vita, ma non è una buona",
    "idea quando ti trovi davanti",
    "qualcosa che da solo tiene testa",
    "a tutto il tuo esercito di non",
    "morti. In quei casi, meglio farli",
    "saltare in aria. Guarda i nemici",
    "sballottati come bambole di pezza,",
    "esplosione dopo esplosione. Costa,",
    "sì, ma al divertimento non si può",
    "attaccare un",
    "cartellino del prezzo.",
    # 69-70
    "Per ora è tutto. Adesso vai e",
    "provaci di persona. Sciò.",
]

RESE = {"30": BLOCCO_30, "25": BLOCCO_25, "24": BLOCCO_24}


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
