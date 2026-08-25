# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %8 e %28 — il manuale del negozio e i modi di esibirsi.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-03.py lavoro/book-003.jsonl

Vale tutto quel che sta scritto in `_99-rese-book-02.py`: tetto di 43 caratteri
misurato sulla **forma degradata**, conto delle righe di ogni paragrafo uguale a
monte, niente participi riferiti a chi legge.

⚠️ **E qui in piu' la spaziatura in testa e' contenuto.** In `%8` monte centra a
mano le insegne (`      -== Setting up a Shop ==-`, cinque o sei spazi) e
incolonna la tabella fiscale: i valori partono tutti alla **colonna 23**, cioe'
dopo 22 caratteri di etichetta e spazi. Le rese tengono gli stessi spazi, perche'
`mes` stampa la riga com'e' e un rientro perso si vede.

Il lessico dal dizionario: `negoziante` (`map_user.hsp`), `registratore di
cassa`, `atto di negozio` (`text.hsp:915`), `Rango` (`chat.hsp:25597`),
`Trattativa` e `Carisma` (`skill.hsp`), `talento da negozio`
(`map_user.hsp:454`), `moneta di bronzo`, `carta YacaPoint`, `Yacatect`,
`Carretto` (`command.hsp:14176`), `Leggi` (il comando `r`); e per `%28`
`Esibizione` (`skill.hsp:357`), `Ensemble`, `Predica`, `Danza ammaliante`,
`Stradivarius`.

⚠️ Le monete si dicono «monete d'oro» per esteso, e «oro» dove la colonna non
ci sta (`chat.hsp:14613` fa gia' cosi').
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %8
# Schmidt il ricettatore: cinico, si vanta e parla al lettore come a un
# principiante. In inglese e' un manuale con le insegne centrate a mano.
BLOCCO_8 = [
    # 1-2
    "Manuale d'uso del negozio",
    "Riscritto da Schmidt il ricettatore",
    # 3-5
    "Allora, ti credi capace di tenere un",
    "negozio? Lo so: passare la giornata",
    "a strillare la merce sembra facile.",
    # 6-8
    "Allora spiegami una cosa, genio:",
    "se è così facile, perché in ogni",
    "città c'è un negozio solo per tipo?",
    # 9-11
    "La risposta è semplice:",
    "      Sopravvive solo il più forte!",
    "(Be', quello e le tasse alte...)",
    # 12-23
    "Tenere un negozio è così difficile",
    "che in città sopravvivono solo i più",
    "meschini e i più spietati. Tu però",
    "hai un vantaggio su noi di città:",
    "     tu starai fuori città!",
    "E per quanto adesso non sembri un",
    "affare, il versamento mensile alla",
    "corona ti scende a cinquemila",
    "monete d'oro al mese e basta",
    "(5.000 oro/mese)",
    "che in confronto a quel che paghiamo",
    "noi in città sono briciole, credimi.",
    # 24-26
    "     -== Come si apre un negozio ==-",
    "Passo 1) Compra un atto di negozio.",
    " (Appena 200.000 oro di base.)",
    # 27-29
    "Passo 2) Leggi l'atto ad alta voce",
    "(tasto r) nel punto del mondo dove",
    "vuoi che sorga.",
    # 30
    "Passo 3) Metti su il negozio (sotto)",
    # 31
    "Passo 4) Caveat emptor!",
    # 32-34
    "     -== Come si manda avanti ==-",
    "Il negozio c'è; adesso va mandato",
    "avanti, che è tutta un'altra cosa.",
    # 35-43
    "Prima ti serve un negoziante. E non",
    "puoi essere tu, perché tu devi girare",
    "a procurarti la roba da vendere. Ti",
    "tocca quindi mettere al banco uno dei",
    "tuoi compagni. Scegli in base a",
    "quanto è bello di faccia e a quanto",
    "sa trattare: in una vendita fatta",
    "bene, quelle due cose sono le sole",
    "che contano.",
    # 44-46
    "Trovato il tuo scagnozzo, vai al",
    "registratore di cassa del negozio",
    "e mettilo a quel lavoro.",
    # 47-50
    "L'altra parte è semplice uguale: per",
    "VENDERE roba, roba ne devi AVERE.",
    "Quindi vai, procurala, e lasciala",
    "nel negozio.",
    # 51
    "-== Pepite d'oro di sapere utile ==-",
    # 52-53
    "Chi sta al banco resta nel negozio",
    "e con te non viene.",
    # 54-55
    "Vendere roba fa soldi (ovvio) e",
    "alza anche il rango del negozio.",
    # 56-60
    "Un rango più alto porta clienti col",
    "portafogli più gonfio, pronto da",
    "svuotare. E gli oggetti cari non si",
    "vendono finché il negozio non è",
    "salito di rango.",
    # 61-64
    "Quanti clienti passano dal negozio",
    "dipende anche dal rango e dal",
    "Carisma di chi ci sta",
    "al banco.",
    # 65-67
    "Quanto un cliente è disposto a",
    "sganciare per un oggetto dipende",
    "dalla Trattativa del negoziante.",
    # 68-71
    "Il potenziale di Trattativa e di",
    "Carisma del negoziante si ricarica",
    "spendendo monete di bronzo al",
    "registratore di cassa.",
    # 72-76
    "Visita i tuoi compagni per trovare",
    "il più bello e il più bravo a",
    "trattare. Una volta costava un occhio",
    "della testa; oggi sono appena 100 oro.",
    "Voi giovani siete fortunati.",
    # 77-81
    "Nei giorni in cui il negozio vende",
    "qualcosa, il negoziante prende",
    "esperienza, e con quella arriva a",
    "prendersi fino a due talenti da",
    "negozio.",
    # 82-88
    "E non è finita! Accumuli YacaPoint",
    "in base a quanto vendi e a quanti",
    "clienti passano. Li spendi con la",
    "carta YacaPoint, che ogni negozio",
    "dovrebbe avere in dotazione grazie",
    "all'accordo con il tempio di",
    "Yacatect.",
    # 89-95
    "Per via di una lite feroce con il",
    "sindacato locale dei mobilieri, i",
    "mobili in più fuori città non si",
    "possono vendere. Noi in città sì,",
    "ancora. Lo stesso vale per il",
    "carretto: quel che ci carichi",
    "dentro, nel negozio non ci va.",
    # 96-100
    "Tutto il resto (immondizia,",
    "cianfrusaglie, perfino roba marcia)",
    "si vende, se trovi il pollo giusto.",
    "Se sta per terra, per i clienti è",
    "roba buona.",
    # 101-109
    "Quindi, se nel negozio c'è un",
    "oggetto su cui non vuoi che i",
    "clienti mettano le zampe, segnalo",
    "come pezzo in mostra con una",
    "casella corda o una casella teca",
    "di vetro. Le trovi rifacendo",
    "l'arredamento del negozio: stanno",
    "più o meno alla nona e alla decima",
    "riga dell'elenco, dall'alto.",
    # 110-115
    "La licenza ti lascia vendere SOLO",
    "10 oggetti per volta. Puoi allargare",
    "il numero con appena 2.000 oro per",
    "altri dieci posti, e poi 1.000 oro",
    "per ogni dieci posti che aggiungi",
    "dopo.",
    # 116-119   ⚠️ i valori partono alla colonna 23, come in monte
    "\t-== Dati fiscali ==-",
    "Costo base:           200.000 oro",
    "Manutenzione:         5.000 oro/mese",
    "Rendita per rango:    ??? oro/mese**",
    # 120-121
    "**Perché ??? alla rendita? Perché lì",
    "entri in gioco tu, bello!",
    # 122-123
    "Con un po' di fortuna vivrai alla",
    "grande anche tu, come me!",
    # 124
    "Ricorda: l'oro si ferma qui!",
    # 125
    "E buoni affari!",
]

# ---------------------------------------------------------------- %28
# Un artista girovago che si prende in giro da solo. I nomi in maiuscolo sono
# i modi di esibirsi, e sono i nomi che il gioco usa nei menu.
BLOCCO_28 = [
    # 1-2
    "Che cos'è un'esibizione?",
    "\tAutore: un artista girovago senza nome",
    # 3-10
    "Mi segno qui un paio di modi per",
    "portare a termine gli incarichi di",
    "spettacolo, così non me li dimentico.",
    "Ho sentito dire che basta esibirsi",
    "davanti a uno finché non è contento",
    "o non si annoia, ma io non sono",
    "abbastanza svelto per quella strada.",
    "Quindi.",
    # 11-24
    "ESIBIZIONE: suoni con lo strumento",
    "che preferisci. Al campo delle feste",
    "qualcosa lo trovi, ma magari non è",
    "nel posto giusto, quindi conviene",
    "portarsi il proprio. Lo strumento",
    "che usi può decidere se il pubblico",
    "resta contento dell'esibizione",
    "oppure no. Se lo è, ti riempiono",
    "di oro e di oggetti.",
    "Girano anche storie su un",
    "leggendario Stradivarius che",
    "migliorerebbe la qualità della roba",
    "che ti tirano",
    "addosso...",
    # 25-38
    "ENSEMBLE: canti insieme ai tuoi",
    "compagni. Per loro è buona",
    "esperienza, e strumenti non ne",
    "servono. È roba di gruppo, quindi",
    "riesce più facilmente di una normale",
    "esibizione in solitaria; e se hai",
    "abilità, anche la roba che ti tirano",
    "viene di qualità migliore. Però",
    "porta via parecchio tempo e",
    "parecchia resistenza, quindi non",
    "sprecare un ensemble in un posto",
    "deserto. E vuol dire anche che, se",
    "non fai in fretta, col committente",
    "raccogli meno punti.",
    # 39-49
    "PREDICA: diffondi la parola del tuo",
    "dio e incanti la gente con la lingua",
    "d'oro. Pare che i compagni ci",
    "guadagnino esperienza. Se la gente",
    "resta contenta della predica, ti dà",
    "un bel po' di elemosina. Cioè oro.",
    "Oggetti no. E se sei così convincente",
    "che qualcuno si converte alla tua",
    "fede, quel qualcuno resta contento",
    "ancora di",
    "più.",
    # 50-59
    "DANZA AMMALIANTE: questa è più",
    "svelta dell'esibizione e contenta",
    "la gente più facilmente, quindi è",
    "ottima per fare punti col",
    "committente. E se hai Carisma,",
    "tanto meglio. Un problemino però",
    "c'è: la gente resta talmente",
    "incantata a guardarti ancheggiare",
    "che poi i soldi non te li",
    "dà.",
    # 60-62
    "SPUTAFUOCO: ho fatto del mio meglio",
    "mentre bruciavo, ma non ha battuto",
    "ciglio nessuno...",
    # 63-69
    "Il mio sogno è diventare un grande",
    "artista e portare il sorriso sulla",
    "faccia della gente ovunque vada, ma",
    "finora ho portato a casa soltanto",
    "sassi. Tirati nella mia direzione.",
    "E mia madre mi dice di tornare",
    "a casa...",
    # 70
    "(Il documento finisce qui.)",
]

RESE = {"8": BLOCCO_8, "28": BLOCCO_28}


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
