# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-006.jsonl: le carni e gli effetti, fine del mangiare.

`item.hsp:4335`-`:4648`, 36 rese. E' l'ultimo blocco di `*item_food`: quel che
ogni carne fa a chi la mangia — cavallo, troll, gatto, la carne corrotta
dall'etere — piu' i quattro cibi che allenano un attributo e le due gravidanze
(il feto e i fiori) che si mangiano il parassita.

Con questo lotto **il mangiare e' finito**: `item.hsp:3304`-`:4648` e' tutto
tradotto, cioe' la parte del file che il giocatore legge a ogni pasto.

⚠️ TUTTE le funzioni inglesi di queste righe sono MORFOLOGIA e vanno via:
`_s`, `your`, `is`, `have`, e `he(cc)`/`his(tc)` **a un argomento solo**
(`funzioni.py`: un argomento -> morfologia, due -> contenuto). Resta `name()`,
che e' contenuto e resta.

⚠️ E `name()` si porta l'articolo, quindi non puo' mai stare dopo una
preposizione: «nel cervello di » + `name(cc)` darebbe «di il viandante». In
tutt'e tre i siti dove l'inglese lo mette in coda a una preposizione
(`:4472`, `:4480`, `:4574`, `:4616`) il nome torna soggetto e il possesso si
perde, che in italiano e' la forma normale per le parti del corpo.

⚠️ **Il terzo «Sheer madness!»**: `:4404` e' la terza riga del file con quella
stessa esclamazione inglese, dopo `:4013` e `:4022`, e i tre giapponesi sono
tutti diversi — 頭がぼんやり «la testa si annebbia», 頭がクラクラ «la testa gira»,
胃は狂気で満たされた «lo stomaco si riempie di follia». Tre rese distinte.

⚠️ `:4590` e `:4633` hanno lo **stesso giapponese** (しかしすぐに花の養分に変えられた)
e due inglesi diversi: la resa e' la stessa per tutt'e due, perche' a
distinguerle e' solo la grammatica inglese che qui non c'e'.

⭐ `:4583` e' l'unico sito del lotto in cui **l'inglese sa di piu'**: il
giapponese dice solo «ma e' stato subito scomposto», l'inglese dice per che
cosa — il feto. Si segue l'inglese (regola della 57a, terzo caso).

⚠️ `@` di `:4375` e' un nome di creatura invariato (`invariati.md`): e' il
simbolo del giocatore dei roguelike fatto creatura. Resta com'e'.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    (4335, "It's too hard!  stomach screams."):      # まるで鉄のように硬い！…の胃は悲鳴をあげた。
        '"Duro come il ferro! " + name(cc) + " sente lo stomaco urlare."',
    (4343, "It tastes really, really strange."):     # 気が変になりそうな味だ。
        "Un sapore da farti uscire di senno.",
    (4352, " feel less sick."):                      # …の病気は軽くなった。
        'name(cc) + " sente la malattia alleggerirsi."',
    (4360, "A horsemeat! It's nourishing."):         # 馬肉だ！これは精がつきそうだ。
        "Carne di cavallo! Roba che tira su.",
    (4368, " feel as   been corrupted."):            # …は神聖なものを汚した気がした。
        'name(cc) + " ha la sensazione di aver profanato qualcosa di sacro."',
    (4375, "You dare to eat @..."):                  # ＠を食べるなんて…
        "Mangiarsi @... roba da non credere.",
    (4385, "Guards hate you."):                      # ガード達はあなたを憎悪した。
        "Le guardie ti hanno preso in odio.",
    (4394, " body burns up for a second."):          # …の体は一瞬燃え上がった。
        'name(cc) + " sente il corpo avvampare per un istante."',
    (4404, "Sheer madness!"):                        # …の胃は狂気で満たされた。
        "Lo stomaco si riempie di follia.",
    (4415, " skin becomes smooth."):                 # 肌がつるつるになりそうだ。
        'name(cc) + " sente la pelle farsi liscia."',
    (4423, " feel love!"):                           # …は恋をしている気分になった！
        'name(cc) + " si sente in amore!"',
    (4431, "Argh! It's poisonous!"):                 # これは有毒だ！
        "Argh, è roba velenosa!",
    (4439, "A troll meat. This must be good for your body."):  # 血が沸き立つようだ。
        "Ti senti ribollire il sangue.",
    (4447, "Of course, it's rotten! Urgh..."):       # 腐ってるなんて分かりきっていたのに…うげぇ
        "Lo sapevo benissimo che era roba marcia... bleah.",
    (4455, "Mighty taste!"):                         # 力が湧いてくるようだ。
        "Ti senti sgorgare la forza dentro.",
    (4463, "  magically stimulated."):               # 微かな魔力の刺激を感じた。
        'name(cc) + " avverte un lieve fremito di potere magico."',
    (4472, "Something is wrong with  stomach..."):   # 胃の調子がおかしい…
        'name(cc) + " ha lo stomaco che non va..."',
    (4480, "Eating this brings  inner peace."):      # この肉は心を落ち着かせる効果があるようだ。
        '"Questa carne calma l\'animo: " + name(cc) + " si acquieta."',
    (4497, "  shaken by a chaotic power."):          # …の胃は混沌で満たされた。
        'name(cc) + " sente lo stomaco riempirsi di caos."',
    (4505, " nerve is damaged."):                    # …の神経に電流が走った。
        'name(cc) + " sente una scarica correre nei nervi."',
    (4515, "How can you eat a cat!!"):               # 猫を食べるなんて！！
        "Mangiarsi un gatto!!",
    (4526, "Ether corrupts your body."):             # …の体内はエーテルで満たされた。
        "L'etere dilaga nel corpo.",
    # ------------------------------------------------ i quattro cibi che allenano
    (4534, "This food is good for your endurance."):  # 体力がつきそうだ。
        "Questo cibo fa bene alla costituzione.",
    (4541, "This food is good for your magic."):     # 魔力が鍛えられる。
        "Questo cibo tempra la magia.",
    (4548, "This food is good for your strength."):  # 力がつきそうだ。
        "Questo cibo dà forza.",
    (4555, "This food is good for your willpower."):  # 精神が少しずぶとくなった。
        "Lo spirito si fa un po' più tenace.",
    (4562, "Wow,  speed up!"):                       # ワアーォ、…は速くなった気がする！
        '"Uaaah, " + name(cc) + " si sente più veloce!"',
    # -------------------------------------------- il parassita: il cervello e il ventre
    (4574, "Something gets into  brain."):           # 何かが…の体内に入り込んだ。
        'name(cc) + " si sente entrare qualcosa nel cervello."',
    (4583, "But it was immediately turned into fetus nutrients."):  # しかしすぐに分解された。
        "Ma viene subito scomposto per nutrire il feto.",
    (4590, "But it was immediately turned into flower nutrients."):  # しかしすぐに花の養分に変えられた。
        "Ma viene subito trasformato in nutrimento per i fiori.",
    (4597, "But  eject it out quickly."):            # しかしすぐに弾き出した。
        '"Ma viene subito respinto fuori."',
    (4603, " get parasitized in the brain."):        # …は脳髄に寄生された。
        'name(tc) + " ha un parassita nel cervello."',
    (4616, "Something gets into  body."):            # 何かが…の体内に入り込んだ。
        'name(cc) + " si sente entrare qualcosa nel corpo."',
    (4633, "But  rapidly break it down into nutrients for  flowers."):  # しかしすぐに花の養分に変えられた。
        '"Ma viene subito trasformato in nutrimento per i fiori."',
    (4641, "But  puke it out quickly."):             # しかしすぐに吐き出した。
        '"Ma viene subito risputato fuori."',
    (4648, " get parasitized in the abdomen."):      # …は寄生された。
        'name(tc) + " ha un parassita nel ventre."',
}

USCITA = "fase4-item-006.jsonl"


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

    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
