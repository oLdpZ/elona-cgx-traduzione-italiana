# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-007.jsonl: le cinque tabelle in testa a item.hsp.

`item.hsp:107`-`:127`, 42 rese. Sono cinque array che `item_func.hsp` incolla
al nome di un oggetto — quindi non si leggono da soli, si leggono **dentro un
nome**, e questo decide la forma di ognuno:

    giftn      :107   il regalo         `item_func.hsp:1448`  PREFISSO
    moneyboxn  :108   il salvadanaio    `item_func.hsp:695`   suffisso «(...)»
    biten      :109   l'esca            `item_func.hsp:698`   suffisso «<...>»
    evitemn    :110   l'oggetto d'evoluzione `item_func.hsp:704`  suffisso «<...>»
    magebookn  :127   il libro antico   `item_func.hsp:880`   suffisso «titled <...>»

⭐ **Prima di tradurle e' stato guardato dove finiscono** (regola della 64a), e
la risposta ha cambiato la forma di due tabelle su cinque:

1. `giftn` e' un **prefisso**, non un suffisso: `item_func.hsp:1499` appende il
   nome dell'oggetto **dopo** quel che l'accumulatore ha gia' dentro, e
   l'inglese ci mette un `lang("", " ")` di coda che il giapponese non ha. Quindi
   le sei voci vanno rese con **aggettivi che in italiano stanno prima del
   nome** e concordati al maschile singolare: l'unico oggetto che li usa e'
   `ITEM_ID_GIFT`, che `db_item.hsp:142615` chiama «regalo». Non c'e' nessun
   altro genere da servire.
2. `evitemn` segue il **giapponese** e non l'inglese, che ha inventato una
   famiglia («king heart», «machine heart», «god heart», «another heart»...)
   dove il giapponese ha sette nomi tutti diversi. A decidere non e' il gusto:
   `blend.hsp:764` ha **gia' reso** 進化の側枝 con «ramo evolutivo», e quella e'
   la ricetta che fabbrica proprio questo oggetto. Tradurre dall'inglese
   avrebbe dato due nomi diversi alla stessa cosa in due finestre.

⚠️ `biten` segue il giapponese in due voci su sei, e sono due errori
dell'inglese: セミ e' la **cicala** (l'inglese scrive «locust», la locusta) e
ヘラクレス e' lo **scarabeo ercole** (l'inglese scrive «beetle» e basta).

⚠️ **Due titoli restano identici all'inglese e sono dichiarati in
`invariati.md`**: `Necronomicon` e `Liber Damnatus`. Sono nomi propri opachi —
uno greco-arabo, l'altro latino — che l'italiano non traduce; gli altri
quattordici titoli della stessa tabella si traducono tutti, ed e' la prova che
non si tratta di dimenticanza. ⭐ `The Golden Bough` prende il titolo italiano
vero dell'opera di Frazer, «Il Ramo d'Oro».

⚠️ `moneyboxn` scrive «monete» per esteso e tiene la scala di monte
(`500 / 2k / 10k / 50k / 500k / 5M / 100M`): il numero e' quel che il giocatore
confronta, e abbreviare la parola avrebbe risparmiato quattro caratteri in
cambio di una sigla che nessun'altra finestra del gioco usa.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# I due titoli dichiarati in invariati.md: la resa E' l'inglese, per scelta.
INVARIATI = {"Necronomicon", "Liber Damnatus"}

# (riga, inglese) -> italiano
RESE = {
    # -- giftn :107 - PREFISSO di «regalo», maschile singolare, prima del nome
    (107, "cheap"): "misero",                        # つまらない
    (107, "so-so"): "normale",                       # 普通の
    (107, "exciting"): "stuzzicante",                # ちょっとドキドキする
    (107, "expensive"): "costoso",                   # 高価な
    (107, "hot and gorgeous"): "favoloso",           # 気絶しそうなほど素晴らしい
    (107, "crazy epic"): "principesco",              # 王様が羨むほどの
    # -- moneyboxn :108 - «(...)» dopo «salvadanaio a gattino»
    (108, "500 GP"): "500 monete",                   # 5百金貨
    (108, "2k GP"): "2k monete",                     # 2千金貨
    (108, "10K GP"): "10k monete",                   # 1万金貨
    (108, "50K GP"): "50k monete",                   # 5万金貨
    (108, "500K GP"): "500k monete",                 # 50万金貨
    (108, "5M GP"): "5M monete",                     # 500万金貨
    (108, "100M GP"): "100M monete",                 # 1億金貨
    # -- biten :109 - «<...>» dopo «esca»
    (109, "water flea"): "pulce d'acqua",            # ミジンコ
    (109, "grasshopper"): "cavalletta",              # バッタ
    (109, "ladybug"): "coccinella",                  # テントウ
    (109, "dragonfly"): "libellula",                 # トンボ
    (109, "locust"): "cicala",                       # セミ - l'inglese sbaglia insetto
    (109, "beetle"): "scarabeo ercole",              # ヘラクレス
    # -- evitemn :110 - «<...>»; si segue il giapponese, come blend.hsp:764
    (110, "remnant"): "scarto",                      # 残りカス
    (110, "king heart"): "vaso del re",              # 王の器
    (110, "machine heart"): "anima meccanica",       # マシンソウル
    (110, "god heart"): "Yoloteotl",                 # ヨロテオトル
    (110, "another heart"): "ramo evolutivo",        # 進化の側枝  <- blend.hsp:764
    (110, "evolution heart"): "pietra evolutiva",    # 進化の導石
    (110, "magic heart"): "corno dei demoni",        # 魔族の角飾り
    # -- magebookn :127 - «titled <...>» dopo «libro antico»
    (127, "Voynich Manuscript"): "Manoscritto Voynich",     # ヴォイニッチ写本
    (127, "Dhol Chants"): "Canti di Dhol",                  # ドール賛歌
    (127, "Ponape Scripture"): "Scrittura di Ponape",       # ポナペ教教典
    (127, "Revelations of Glaaki"): "Rivelazioni di Glaaki",  # グラーキ黙示録
    (127, "G'harne Fragments"): "Frammenti di G'harne",     # グ＝ハーン断章
    (127, "Liber Damnatus"): "Liber Damnatus",              # 断罪の書 - invariato
    (127, "Book of Dzyan"): "Libro di Dzyan",               # ドジアンの書
    (127, "Book of Eibon"): "Libro di Eibon",               # エイボンの書
    (127, "Grand Grimoire"): "Gran Grimorio",               # 大いなる教書
    (127, "Celaeno Fragments"): "Frammenti di Celaeno",     # セラエノ断章
    (127, "Necronomicon"): "Necronomicon",                  # ネクロノミコン - invariato
    (127, "The R'lyeh Text"): "Il Testo di R'lyeh",         # ルルイエ異本
    (127, "Eltdown Shards"): "Frammenti di Eltdown",        # エルトダウン・シャールズ
    (127, "The Golden Bough"): "Il Ramo d'Oro",             # 金枝篇 - il titolo di Frazer
    (127, "Apocalypse"): "Apocalisse",                      # 終焉の書
    (127, "True Apocalypse"): "Vera Apocalisse",            # 真なる終焉の書
}

USCITA = "fase4-item-007.jsonl"


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

    identiche = {d["en"] for d in voci if d["it"] == d["en"]}
    if identiche != INVARIATI:
        raise SystemExit("identiche all'inglese: %s, attese %s"
                         % (sorted(identiche), sorted(INVARIATI)))

    # ⚠️ Queste rese finiscono DENTRO un nome di oggetto, che le finestre
    # tagliano: si dichiara quanto costano rispetto a monte, cosi' il numero
    # sta scritto invece che supposto. Si misura la forma DEGRADATA (64a).
    peggiori = sorted(((len(accenti.degrada(d["it"])) - len(d["en"]), d["riga"], d["en"], d["it"])
                       for d in voci), reverse=True)[:3]

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    print("invariate dichiarate: %s" % sorted(identiche))
    print("le tre che allungano di piu' rispetto all'inglese:")
    for delta, riga, en, it in peggiori:
        print("   :%-4d +%-2d  %r -> %r" % (riga, delta, en, it))
    for d in voci:
        print("   :%-5d %-24s %s" % (d["riga"], d["en"], d["it"]))


if __name__ == "__main__":
    main()
