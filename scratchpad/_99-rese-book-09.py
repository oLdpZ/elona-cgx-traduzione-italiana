# -*- coding: utf-8 -*-
"""Le rese di `book.txt` %29 e %14 — l'articolo scientifico e il regolamento del TCG.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-rese-book-09.py lavoro/book-009.jsonl

Valgono le regole di `_99-rese-book-02.py`.

⚠️⚠️ **In `%14` le parole chiave delle carte restano in inglese, e non e' una
scelta di stile: e' quel che il giocatore ha davanti.** `tcg.hsp:887`-`:961`
le disegna con `bmes "Windfury"`, `bmes "Trample"`, `bmes "Silenced"` —
**letterali nudi**, fuori da ogni `lang()`, quindi a schermo sono inglesi in
tutt'e due le lingue e nessun dizionario le raggiunge. Un libro che le
traducesse manderebbe il lettore a cercare sulla carta una parola che li' non
c'e'. Stessa ragione per i nomi delle fasi (`Begin Phase`, `Draw Phase`,
`Main Phase`, `End Phase`) e per `Graveyard`, che compaiono nelle stesse
descrizioni (`tcg.hsp:1592`, `:1594`). ⭐ C'e' gia' un precedente nel
progetto: `tcg_custom.hsp:2066` dice «le carte Trample» in italiano.

Tutto il resto della riga si traduce: il regolamento e' prosa, e la parola
chiave e' un'etichetta dentro la prosa.
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 43
TETTO_CORPUS = 39

# ---------------------------------------------------------------- %29
# Articolo scientifico vero e proprio: passivo impersonale, prima persona
# plurale, appendici. Il registro accademico e' il pezzo.
BLOCCO_29 = [
    # 1-3
    "Caratterizzazione sperimentale",
    "\tdell'energia dimensionale",
    "\tdi Gavela et al.",
    # 4-9
    "L'energia dimensionale è una forma",
    "di energia capace di interagire",
    "attraverso le dimensioni con gli",
    "oggetti, persone comprese. La sua",
    "esistenza è teorizzata da tempo, ma",
    "mancava di prove sperimentali certe.",
    # 10-16
    "Qui ne presentiamo la",
    "caratterizzazione per mezzo di",
    "esperimenti di Verde-Hermann con",
    "una nuova unità di distorsione",
    "dimensionale. Esploriamo anche le",
    "possibili conseguenze e applicazioni",
    "di questa tecnologia.",
    # 17-27
    "Per mettere alla prova il postulato",
    "di Verde-Hermann, secondo cui la",
    "misura dell'energia dimensionale è",
    "difficile perché la barriera",
    "interdimensionale la smorza, abbiamo",
    "perturbato la barriera con un'unità",
    "di distorsione dimensionale e",
    "condotto la prima e la seconda",
    "prova di Verde-Hermann. L'unità",
    "di osservazione impiegata è",
    "descritta nell'appendice 1.",
    # 28-32
    "Dai dati (appendici da 1 a 6)",
    "abbiamo stabilito che l'energia",
    "dimensionale si indebolisce di un",
    "fattore di circa lo 0,0025% in",
    "condizioni normali.",
    # 33-46
    "Nella seconda prova abbiamo",
    "stabilito, con alta confidenza, che",
    "è verosimile che l'intensità",
    "dell'energia dimensionale sia",
    "inversamente proporzionale alla",
    "distorsione dimensionale, in accordo",
    "con le leggi dell'energia di Ariane.",
    "Troviamo però anche che, quando due",
    "oggetti analoghi A e B vengono",
    "spostati fino a stare nella stessa",
    "dimensione, l'energia dimensionale",
    "si dissipa rapidamente. Servono",
    "altri esperimenti per chiarire il",
    "meccanismo del fenomeno.",
    # 47-51
    "Poiché l'energia dimensionale",
    "scorre lungo il gradiente di",
    "potenziale, troviamo possibile",
    "imbrigliare energia illimitata",
    "se le dimensioni si collegano.",
    # 52-60
    "Raccomandiamo però prudenza nello",
    "sfruttamento a lungo termine",
    "dell'energia dimensionale, perché",
    "gli effetti sulle dimensioni",
    "coinvolte sono ancora ignoti.",
    "Inoltre, anche se l'estrazione",
    "non causasse effetti diretti,",
    "potrebbe essere giudicata un atto",
    "ostile dagli abitanti dell'altra.",
    # 61-68
    "In conclusione, serve altra",
    "ricerca per stabilire come le",
    "esistenze analoghe siano collegate",
    "nello spazio multidimensionale, e",
    "per studiare il meccanismo di quel",
    "collegamento, così da mettere a",
    "punto uno strumento pratico di",
    "comunicazione transdimensionale.",
]

# ---------------------------------------------------------------- %14
# La reclame del gioco di carte, poi il regolamento secco. ⚠️ Le parole chiave
# restano inglesi: vedi il docstring.
BLOCCO_14 = [
    # 1-2
    "Azione! Avventura! Battaglie di carte!",
    "<Di Schmidt, maestro di mazzi>",
    # 3-6
    "Cercavate un gioco per i vostri",
    "figli che non preveda freccette da",
    "prato, uno yeek morto e un pezzo",
    "di spago?",
    # 7
    "NON CERCATE OLTRE!",
    # 8-12
    "Presto nel paese di Tyris del Nord,",
    "un gioco nuovo di zecca fatto di",
    "carte da collezionare, duelli e",
    "pettinature bizzarre che, per",
    "esistere, vogliono ingegneria genetica!",
    # 13-15
    "Seguito del gioco un tempo famoso",
    "Duelli di Mostri, che a sua volta",
    "seguiva Maghi e Magia!",
    # 16
    "Diventa il Re dei Giochi!",
    # 17-18
    "Ogni giocatore parte con un mazzo",
    "di 30-60 carte creatura",
    # 19-22
    "I Domini sono 6: le carte in mano",
    "iniziali e la vita sono inversamente",
    "proporzionali al numero di Domini.",
    "(Neutrale e Leggendario non contano.)",
    # 23-24
    "Copie della stessa carta al massimo X:",
    "Normale:X=4 Neutrale:X=2 Leggend.:X=1",
    # 25-29
    "Vince il primo che porta a 0 la",
    "vita dell'avversario. Se al momento",
    "di pescare non ci sono carte nel",
    "mazzo, la vita del giocatore",
    "scende a 0.",
    # 30-32
    "Le fasi sono 4:",
    "- Begin Phase - Draw Phase",
    "- Main Phase - End Phase",
    # 33-36
    "Begin Phase:",
    "Attiva gli effetti d'inizio turno.",
    "Riattiva tutte le carte sul Campo.",
    "Il Mana torna al massimo.",
    # 37-39
    "Draw Phase:",
    "Il giocatore pesca 1 carta.",
    "Attiva gli effetti in mano.",
    # 40-43
    "Nella Main Phase puoi:",
    "spendere il Mana e giocare le carte.",
    "sacrificare una carta: +1 Mana massimo.",
    "attaccare con le tue creature.",
    # 44-53
    "End Phase:",
    "Attiva gli effetti di fine turno.",
    "Uso delle carte:",
    "Le carte si esauriscono all'evocazione.",
    "Una carta esaurita non può attaccare,",
    "ma può difendere dagli attacchi.",
    "Le creature attaccate non possono",
    "bloccare fino alla Begin Phase dopo.",
    "Le creature con 0 salute dopo lo",
    "scontro vanno al Graveyard.",
    # 54-60
    "Comandi:",
    "Invio: scegli.",
    "Annulla: salta il turno / difendi",
    "/ bersaglio a caso per l'effetto.",
    "Tasto s: arrenditi",
    "SU: gioca / attacca / difendi.",
    "GIÙ: sacrifica la carta.",
    # 61-63
    "Descrizione della carta:",
    "In alto: costo in Mana",
    "In basso: attacco / salute",
    # 64
    "Parole chiave:",
    # 65-74
    "Battlecry: si attiva all'evocazione.",
    "Deathrattle: si attiva al Graveyard.",
    "Sacrifice: si attiva col sacrificio.",
    "On-Draw: si attiva quando la peschi.",
    "In-Hand: si attiva dopo la Draw Phase.",
    "Ongoing: si attiva da sola sul Campo.",
    "Aftercombat: si attiva dopo lo scontro.",
    "On-Kill: si attiva dopo lo scontro,",
    "quando l'avversario è battuto e",
    "questa carta sopravvive.",
    # 75
    "Tratti positivi:",
    # 76-91
    "- Regeneration: gli HP tornano al",
    "massimo nella Begin Phase.",
    "- Armor: annulla un colpo, una volta.",
    "- Flying: la può bloccare solo chi ha",
    "flying o reach.",
    "- Intimidate: la bloccano solo carte",
    "dello stesso Dominio.",
    "- Reach: blocca le carte flying.",
    "- Lifelink: dà vita pari al danno.",
    "- Haste: evocata, non si esaurisce.",
    "- Trample: l'eccesso va al giocatore.",
    "- First-Strike: colpisce solo al",
    "primo round dello scontro.",
    "- Dual-Strike: colpisce al primo",
    "round e al round normale.",
    "- Deathtouch: danno alla carta +999.",
    # 92
    "Tratti positivi:",
    # 93-101
    "- Windfury: primo attacco gratis.",
    "- Vigilance: blocca sempre.",
    "- Defender: blocca sempre, non attacca.",
    "- Critical: attacco x3 con 1 su 6.",
    "- Barrier: nessun danno da effetto.",
    "- Evasion: non può essere bersagliata.",
    "- Split: se sopravvive, si sdoppia.",
    "- Rider: Armor e +2 attacco. Colpita,",
    "perde il tratto e 2 salute.",
    # 102
    "Tratti negativi:",
    # 103-114
    "- Deathword: al Graveyard dopo 3 turni.",
    "- Gravity: si può sempre bloccare.",
    "- Bleeding: subisce +1 danno.",
    "- Poisoned: 1 danno nella Begin Phase.",
    "- Kamikaze: Battlecry, si uccide.",
    "- Paralysed: non difende questo turno.",
    "- Frozen: non attacca questo turno.",
    "- Silenced: nessun effetto si attiva.",
    "- Confused: non attacca, non difende",
    "e non usa effetti. Non si esaurisce.",
    "- Insane: passa dall'altra parte la",
    "seconda volta che la prende.",
]

RESE = {"29": BLOCCO_29, "14": BLOCCO_14}


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
