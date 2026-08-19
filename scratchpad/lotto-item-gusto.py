# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-001.jsonl: che sapore ha quel che mangi.

`item.hsp:3304`-`:3397`, cioe' il blocco di `*item_food` che commenta **ogni
pasto**: le ventiquattro esclamazioni del giocatore secondo la qualita' del
cibo, la faccia storta di un PNG davanti alla carne cruda, e le sei reazioni al
cibo avvelenato (`ITEM_BIT_HAZARD`).

E' il primo lotto di `item.hsp`, che era il QUINDICESIMO punto cieco: 244
`lang()` e nessun file di dizionario, quindi fuori da `verifica --dizionario`.
E' la lezione della 54a — *un file senza file di dizionario non e' un file
finito, e' un file che nessun conteggio guarda* — e aprirlo anche solo per un
lotto lo fa entrare nel referto.

DUE REGISTRI IN TRENTUNO RIGHE, e li separa il codice, non il gusto:

  - `:3304`-`:3362` stanno dentro `if ( cc == CHARA_PLAYER ... )` (`:3296`):
    sono il **pensiero di chi mangia**, e vanno in prima persona o impersonali.
  - `:3368`-`:3397` portano `name(cc)`: sono **righe di log condivise** fra
    giocatore e PNG, e vanno in terza persona presente (guida-stile).

⚠️ `his(cc, 1)` — DUE argomenti — e' contenuto e va conservato (`funzioni.py`):
restituisce «il suo», maschile singolare, quindi ogni sito che la usa deve
metterle accanto un **nome maschile singolare**. Qui: «stomaco» (:3377),
«fiato» (:3389), «labbro» (:3393), «sguardo» (:3397). ⚠️ E non puo' mai stare
dopo una preposizione: «il suo» si porta l'articolo, e `da + il` fa `dal`.
Vedi `scratchpad/correzione-his-possessivo.py`, che ha appena reso quella
funzione «il suo» anche per il giocatore.

⚠️ NIENTE PARTICIPI riferiti a `name()`: il genere non si conosce. Per questo
`:3381` e' «rimpiange il giorno della nascita» e non «si pente di essere
venuto al mondo».

⭐ Dove giapponese e inglese divergono si segue il **giapponese** (regola della
57a): `:3343` e `:3346` hanno lo stesso inglese «Awful taste!!» per due
giapponesi diversi — ゴムっぽい («sa di gomma», e' la gomma da masticare gia'
masticata) e ひどい («un sapore atroce», e' il cibo di qualita' infima. Rese
uguali fonderebbero due righe che il gioco distingue. Idem «Delicious!» a
`:3304` (ウマイ, katakana, il cannibale davanti alla carne umana) e a `:3359`
(美味しい, il pasto buono e basta).

Legge le voci gia' estratte da lavoro/_item.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    # ---------------- il pensiero di chi mangia (dentro `if ( cc == CHARA_PLAYER )`)
    (3304, "Delicious!"):                           # ウマイ！ - il cannibale
        "Che bontà!",
    (3312, "Ugh! Rotten food!"):                    # うげっ！腐ったものを食べてしまった…うわ…
        "Bleah! Ho mangiato roba marcia... uh...",
    (3318, "Ugh... Raw meat..."):                   # 生肉だ…
        "Carne cruda...",
    (3322, "It tastes like... powder..."):          # 粉の味がする…
        "Sa di polvere...",
    (3326, "Er... this needs to be cooked."):       # 生で食べるものじゃないな…
        "Non è roba da mangiare cruda...",
    (3329, "It doesn't taste awful but..."):        # まずいわけではないが…
        "Non che sia cattivo, però...",
    (3329, "Very boring food."):                    # 平凡な味だ。
        "Un sapore banale.",
    (3334, "Wow! Cool!"):                           # つめたい！ - il ghiaccio tritato
        "Che freddo!",
    (3334, "Yummy!"):                               # 頭がキーンとする！
        "Una fitta al cervello!",
    (3339, "Er... my tongue feels weird."):         # 舌がおかしくなりそうだ… - sale, zucchero, pepe, salsa
        "Mi sto rovinando la lingua...",
    (3343, "Ugh! Yuk!"):                            # まずい！
        "Che schifo!",
    (3343, "Awful taste!!"):                        # ゴムっぽい味だ！ - la gomma masticata
        "Sa di gomma!",
    (3346, "Boy, it gives your stomach trouble!"):  # うぅ…腹を壊しそうだ。
        "Uh... adesso lo stomaco la paga.",
    (3346, "Awful taste!!"):                        # ひどい味だ！
        "Un sapore atroce!",
    (3351, "Uh-uh, the taste is so-so."):           # まあまあの味だ。
        "Un sapore così così.",
    (3351, "The taste is not bad."):                # 悪くない味だ。
        "Un sapore niente male.",
    (3355, "It tasted good."):                      # かなりいける。
        "Si mangia proprio volentieri.",
    (3355, "Decent meal."):                         # それなりに美味しかった。
        "Buono, a modo suo.",
    (3359, "Delicious!"):                           # 美味しい！
        "Delizioso!",
    (3359, "Gee what a good taste!"):               # これはいける！
        "Questo sì che si mangia!",
    (3359, "It tasted pretty good!"):               # いい味だ！
        "Che bel sapore!",
    (3362, "Wow! Terrific food!"):                  # 最高に美味しい！
        "Buonissimo!",
    (3362, "Yummy! Absolutely yummy!"):             # まさに絶品だ！
        "Una vera squisitezza!",
    (3362, "It tasted like seventh heaven!"):       # 天にも昇る味だ！
        "Un sapore da toccare il cielo!",
    # ---------------------------------------- le righe di log, terza persona
    (3368, " looks glum."):                         # name(cc)は渋い顔をした。
        'name(cc) + " storce il naso."',
    (3377, " tried hard to swallow, but  stomach rejected it."):
        'name(cc) + " manda giù a forza, ma " + his(cc, 1) + " stomaco lo rifiuta."',
    (3381, " regretted being born."):               # は生まれてきたことを後悔した。
        'name(cc) + " rimpiange il giorno della nascita."',
    (3385, " cried in agony to the point of fainting!"):
        'name(cc) + " si contorce in lacrime fino a svenire!"',
    (3389, " lets out a strangely colorful smoke from  mouth."):
        'name(cc) + " manda fuori " + his(cc, 1) + " fiato in un fumo stranamente colorato."',
    (3393, " foams from  mouth while consulsing."):
        'name(cc) + " si contorce, e la schiuma ricopre " + his(cc, 1) + " labbro."',
    (3397, " rolls back  eyes and collapses."):
        'name(cc) + " straluna " + his(cc, 1) + " sguardo e stramazza a terra."',
}

USCITA = "fase4-item-001.jsonl"


def main():
    radice = pathlib.Path(__file__).resolve().parent.parent
    voci = []
    with io.open(radice / "lavoro" / "_item.jsonl", encoding="utf-8") as f:
        for riga in f:
            d = json.loads(riga)
            chiave = (d["riga"], d["en"])
            if chiave in RESE:
                d["it"] = RESE[chiave]
                voci.append(d)

    mancanti = set(RESE) - {(d["riga"], d["en"]) for d in voci}
    if mancanti:
        raise SystemExit("chiavi non trovate nel lotto: %s" % sorted(mancanti))
    if len(voci) != len(RESE):
        raise SystemExit("attese %d voci, riempite %d" % (len(RESE), len(voci)))

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    # ⚠️ Il controllo della 67a, corretto nella 68a: si chiama la funzione VERA
    # di accenti.py, non una soglia somigliante. CP932 codifica —, “ ”, …, ° su
    # due byte e la build ne disegna uno per byte.
    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
