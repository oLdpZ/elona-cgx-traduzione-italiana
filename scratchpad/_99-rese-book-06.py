# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %7, %5, %26 e %32 — le erbe, la crimberry, la lezione, il campo.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-06.py lavoro/book-006.jsonl

Valgono le regole di `_99-rese-book-02.py`.

⚠️ **I nomi delle erbe non si traducono**: `curaria`, `morgia`, `mareilon`,
`spenseweed`, `alraunia`, `crimberry` sono i nomi degli oggetti in
`db_item.hsp` e li' sono rimasti tali. Il nome latino fra parentesi quadre e'
uno scherzo di monte e resta com'e'.

⚠️ **Gli effetti delle erbe vengono dal giapponese, non dall'inglese.** Monte
inglese dice `Strength and Endurance`; il giapponese di モージア dice 筋力と耐久,
cioe' gli attributi **Forza** e **Costituzione**, che sono i nomi di
`skill.hsp:19` e `:24`. Con «resistenza» il lettore cercherebbe nella scheda
una voce che non c'e'.

⚠️ In `%7` le righe 21, 42 e 54 sono la **continuazione rientrata col tab**
della riga «Effetto:» che le precede, e il tab si ricopia. In `%5` le righe 40
e 41 sono centrate a mano con otto spazi.

Il lessico dal dizionario: `Energia da Lavoro` e `livello di lavoro`
(`map_user.hsp:480`, `:481`), `forza vitale` (`text.hsp:3110`), `campo di
prigionia` (`map_user.hsp:184`), `gabbia`, `Obbedienza`, `potere divino`
(`trait.hsp:371`), `stregone` (`chat.hsp:24095`), `Eulderna`, `yeek`.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %7
# Il dottor Schmidt in veste di scienziato: referto clinico, tono asettico che
# ogni tanto scivola nel devoto.
BLOCCO_7 = [
    # 1-2
    "Erbe benedette",
    "Raccolte dal dott. Schmidt, PhDM",
    # 3-10
    "* Curaria [KYURARIA AQUIFOLIUM]",
    "L'effetto è noto ed è medicinale.",
    "La misura di quell'effetto, però,",
    "dipende tutta dal cosiddetto stato",
    "di consacrazione, che le prove",
    "cliniche hanno dimostrato essere un",
    "effetto vero e non un placebo.",
    "Effetto: potenziamento generale",
    # 11-21
    "* Morgia [MOJIA DIPSACUS PILOSUS]",
    "Stimolante ormonale potentissimo.",
    "Aumenta massa muscolare, forza e",
    "resistenza. I soggetti alla prova",
    "cieca hanno ricevuto erbe in stati",
    "di consacrazione diversi, e hanno",
    "avuto risposte diverse. Il che",
    "dimostra che gli dei esistono, e",
    "che la nostra scienza è nulla.",
    "Effetto: potenzia Forza e",
    "\tCostituzione",
    # 22-26
    "* Mareilon [MAREIRON DIPSACUS FEROX]",
    "Stimolante neurochimico. Aumenta le",
    "capacità cognitive. La misura",
    "dell'effetto sta nella consacrazione.",
    "Effetto: potenzia la mente",
    # 27-34
    "* Spenseweed [SUPENSUUIDO LONGIFOLIA]",
    "Gli effetti sono ancora tutti",
    "ignoti, benché si sia notato che",
    "chi la ingerisce pare più desto",
    "e che la percezione può salire.",
    "Servono altre prove per stabilire",
    "tutti gli effetti collaterali.",
    "Effetto: potenzia la Percezione",
    # 35-42
    "* Alraunia [ARURONIA MARTYNIA LUTEA]",
    "Attiva gli ormoni. Afrodisiaca.",
    "Perciò gode di enorme popolarità",
    "fra la gente del posto. Curiosamente",
    "pare che migliori anche la",
    "memoria. Ricerca in attesa di fondi.",
    "Effetto: potenzia memoria e",
    "\tlibido",
    # 43-52
    "* Stomafilla [SUTOMAFIRIA HYPOGAEA]",
    "A contatto con lo stomaco l'erba",
    "si gonfia e riempie la cavità,",
    "e chi la mangia si sente molto",
    "gonfio. L'uso prolungato e il",
    "valore nutritivo della pianta sono",
    "ancora da verificare. Si riferisce",
    "anche che aumenti la velocità di",
    "chi la usa, ma quasi nessuna gara",
    "sportiva l'ha ancora vietata.",
    # 53-54
    "Effetto: sazia e potenzia la",
    "\tVelocità",
    # 55-57
    "Man mano che arrivano altri campioni",
    "e li si prova, aggiorneremo questa",
    "breve guida.",
    # 58-60
    "Fino ad allora,",
    "dott. Schmidt",
    "\tPhilosophiae Doctor Magus",
]

# ---------------------------------------------------------------- %5
# Volantino da lega per la temperanza: allarmato, moralista, un po' ridicolo.
BLOCCO_5 = [
    # 1-2
    "La dipendenza da crimberry e te",
    "Un opuscolo educativo Schmidt",
    # 3-5
    "Ogni anno sempre più gente cade",
    "nella dipendenza dalla crimberry,",
    "che innocua sembra.",
    # 6-11
    "Chiamata in un antico dialetto",
    "nefiano Kur-amu-beri, il che basta",
    "a mostrare quanto lunga e sordida",
    "sia la sua storia con la nostra",
    "terra e la nostra gente, la crimberry",
    "è un allucinogeno forte e versatile.",
    # 12-22
    "Basta mangiare una bacca perché in",
    "15-60 minuti compaiano questi sintomi:",
    "- allucinazioni",
    "- stordimento come da ubriachezza",
    "- farneticamenti da matti",
    "- perdita del controllo motorio.",
    "La crimberry dà forte dipendenza,",
    "e se chi ne dipende non trova la",
    "dose successiva, o passa ad altri",
    "stupefacenti, o diventa un pericolo",
    "per la nostra comunità.",
    # 23-27
    "E naturalmente nessuno pensa ai",
    "poveri bambini, che finiscono",
    "dentro attività da grandi. Hanno",
    "perfino inventato un nuovo modo di",
    "godersi quelle bacche diaboliche:",
    # 28-39
    "copiano gli yeek selvatici, le fanno",
    "seccare e poi se le ficcano su per",
    "il naso. Questo sniffare crimberry",
    "porta a un'aggressività smodata,",
    "e spinge i più disperati a farsi",
    "chiamare avventurieri e a",
    "commettere gesti folli per",
    "procurarsi la dose.",
    "E se certi maghi anziani dai",
    "capelli lunghi pretendono che le",
    "crimberry restino legali, sia pure",
    "per i loro sacri riti, deve finire!",
    # 40
    "        PER I NOSTRI FIGLI!",
    # 41
    "        PER IL NOSTRO FUTURO!",
    # 42-43
    "SCRIVETE OGGI STESSO AL MAGISTRATO!",
    "\tFate una petizione al re!",
]

# ---------------------------------------------------------------- %26
# Appunti di lezione: registro accademico, definizioni pulite. Le righe di
# `=====` sono la sottolineatura del titoletto e restano lunghe uguale.
BLOCCO_26 = [
    # 1-3
    "SOR110 Introduzione alla stregoneria",
    "\tappunti della lezione 1",
    "\tUniversità metropolitana di Eulderna",
    # 4-17
    "Mana",
    "=====",
    "Fonte di potere primordiale,",
    "presente ovunque nel mondo: nel",
    "mare, nell'atmosfera e dentro la",
    "terra. Gli organismi viventi",
    "trattengono il mana, che può anche",
    "passare da un organismo all'altro",
    "con la predazione e in altri modi.",
    "È il cosiddetto ciclo del mana.",
    "Il mana trattenuto dentro un",
    "organismo non può superare la sua",
    "capienza: quel che eccede viene",
    "espulso nell'ambiente.",
    # 18-22
    "Gli organismi morti non trattengono",
    "il mana. Con la morte, il mana che",
    "l'organismo conteneva comincia a",
    "disperdersi di nuovo",
    "nell'ambiente.",
    # 23-26
    "Poiché l'uso principale del mana è",
    "convertirlo in MP, molti stregoni",
    "usano MP e mana come se fossero",
    "la stessa parola.",
    # 27-35
    "Magia",
    "======",
    "Forma di energia in cui il mana",
    "viene convertito, e che serve per",
    "praticare la stregoneria. Senza",
    "conversione il mana non si può",
    "usare bene per gli incantesimi, e",
    "serve solo per gli scopi più",
    "rudimentali.",
    # 36-42
    "Anche l'affinità di un essere con",
    "la magia si chiama Magia (a volte",
    "detta anche attributo Magia), ma",
    "questo modo di dire è piuttosto",
    "nuovo ed è entrato nell'uso comune",
    "solo un centinaio di anni",
    "fa.",
    # 43-46
    "MP",
    "===",
    "Punti magia. Unità di misura della",
    "quantità di energia magica.",
    # 47-58
    "Potere divino",
    "=============",
    "Energia che serve agli dei per",
    "usare i loro poteri. La teoria",
    "corrente è che venga estratta",
    "dalle offerte dei fedeli e unita",
    "al mana. Per certi versi somiglia",
    "alla magia, ma per il resto è una",
    "forma di energia del tutto",
    "diversa. Gli stregoni del nostro",
    "paese devono ancora scoprire come",
    "si imbrigli questo potere.",
    # 59-62
    "Per fare un paragone: se il mana",
    "fosse acqua, gli MP sarebbero",
    "bottiglie d'acqua, e il potere",
    "divino bottiglie di gassosa.",
]

# ---------------------------------------------------------------- %32
# Il senpai del campo di prigionia: allegro, servizievole, e quel che dice fa
# gelare il sangue. Il contrasto e' tutto il pezzo e va tenuto.
BLOCCO_32 = [
    # 1-2
    "Manuale di correzione dei prigionieri",
    "Scritto dal senpai responsabile",
    # 3-8
    "Congratulazioni per il tuo debutto",
    "come sorvegliante dei prigionieri!",
    "Da adesso puoi tenere in gabbia i",
    "ragazzi più promettenti e portarli",
    "al campo di",
    "prigionia!",
    # 9-14
    "Una volta fatti obbedienti nel",
    "campo, non avranno altra scelta che",
    "ubbidirti, per quanto tu gli stia",
    "antipatico. Possono diventare tuoi",
    "compagni fedeli! O perfino",
    "amici!",
    # 15-19
    "Eh? Basta comprare uno schiavo per",
    "evitare la fatica, se quel che",
    "vuoi è un amico? Non ti serve un",
    "gulag perché hai la magia del",
    "dominio?",
    # 20-21
    "E va bene: intanto usiamo il",
    "pannello, che ne dici?",
    # 22-28
    "Dopo aver fatto uscire dalle gabbie",
    "i ragazzi catturati, imposta il",
    "livello di lavoro e falli lavorare!",
    "Tanto scappare non può nessuno:",
    "lasciali lì per tre giorni circa",
    "e poi torna a vedere come",
    "vanno le cose.",
    # 29-35
    "Più alto è il livello di lavoro",
    "che imposti, più Energia da Lavoro",
    "accumuli. Ma più alto è, più forza",
    "vitale consuma: quindi non",
    "dimenticarti di rimpiazzarli con",
    "gente nuova quando muoiono,",
    "d'accordo?",
    # 36-39
    "Le cose che stanno nel campo non",
    "cambiano granché l'Energia che",
    "ricavi, quindi la disposizione",
    "falla come ti pare.",
    # 40-43
    "E poi... più i ragazzi sono",
    "obbedienti e bravi, più è probabile",
    "che lavorino sodo e producano più",
    "Energia da Lavoro.",
    # 44-49
    "Correggerli e farli onesti e",
    "perbene è facilissimo! Basta",
    "farne un esempio giustiziandoli!",
    "Tanto è più comodo se sono di meno,",
    "compresi quelli che servono per",
    "le esecuzioni.",
    # 50-52
    "Come pensi di cavartela?",
    "Su, correggiamoli tutti, questi",
    "maledetti ragazzini!",
]

RESE = {"7": BLOCCO_7, "5": BLOCCO_5, "26": BLOCCO_26, "32": BLOCCO_32}


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
