# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-002.jsonl: le erbe, la carne umana, i cibi speciali.

`item.hsp:3471`-`:3888`. Secondo lotto del file. Tre famiglie che il codice
tiene vicine perche' stanno tutte dentro `*item_food`, dopo il conto delle
calorie:

  :3471-:3659  le cinque ERBE (curaria, morgia, mareilon, spenseweed,
               alraunia): righe dentro `if ( cc == CHARA_PLAYER )`, quindi
               parlano solo a te -> registro «tu» (guida-stile).
  :3718-:3739  la CARNE UMANA e il tratto del cannibalismo.
  :3818-:3888  i cibi speciali: il seme sputato, la moneta di platino
               dell'oca, il tofu fritto delle volpi, il cristallo curativo,
               il mangime, il cadavere di <Little Sister>.

⭐ SETTE DELLE VENTIDUE ERANO GIA' RESE ALTROVE, e sono state copiate invece
che riscritte (regola della 58a: due rese diverse per la stessa riga sono un
difetto che nessuna rete vede, perche' la rete 3 tace proprio quando
coincidono):

    :3868       <- proc.hsp:25779      lo stesso giapponese, parola per parola
    :3877 (x5)  <- command.hsp:15103   le cinque battute del mangime
    :3881       <- command.hsp:15108   ⚠️ adattato `tc` -> `cc`: la variabile
                                       del sito e' diversa, il testo no

⚠️⚠️ `:3835` e' un caso della 58a: **l'inglese di monte porta la riga giusta
dell'evento sbagliato.** Il giapponese dice «l'uovo deposto da <nome> si e'
rotto e da dentro e' uscito del platino»; l'inglese scrive
`「Ugh-Ughu」 <nome> laid a platinum coin.`, cioe' si porta dietro il verso di
rutto di `:3818` — che li' e' giusto, perche' li' si sputa un seme — e butta
via l'uovo che si rompe. Si segue il **giapponese**.

⚠️ E `:3818` e `:3835` hanno le parentesi giapponesi 「」 DENTRO LA STRINGA
INGLESE: CP932 le codifica su due byte e la build inglese disegna un glifo per
byte. In italiano vanno le virgolette dritte, `\\"` (vedi
`accenti.doppi_byte_cp932`). Stessa ragione per cui `:3853` perde la ♪ finale,
che sta a U+266A ed e' anch'essa a due byte.

⚠️ `:3877` e' un `txt` a sei alternative su cinque firme (「パッサパサだよ」 con
e senza punto esclamativo sono due stringhe diverse; 「パッサパサ！」 compare due
volte e vale una firma sola).

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
    # ------------------------------------------------- le cinque erbe (registro «tu»)
    (3471, "This herb invigorates you."):            # このハーブは活力の源だ。
        "Quest'erba è una fonte di vigore.",
    (3518, "You feel might flowing through your body."):   # 新たな力が湧きあがってくる。
        "Senti una forza nuova che monta dentro di te.",
    (3565, "You feel magical power spring up inside you."):  # 魔力の向上を感じる。
        "Senti crescere il tuo potere magico.",
    (3612, "You feel your senses sharpen."):         # 感覚が研ぎ澄まされるようだ。
        "I tuoi sensi si fanno più acuti.",
    (3659, "Your hormones are activated."):          # ホルモンが活発化した。
        "I tuoi ormoni si sono risvegliati.",
    # ------------------------------------------------------------- la carne umana
    (3718, "It's your favorite, human flesh!"):      # これはあなたの大好きな人肉だ！
        "Questa è carne umana, la tua preferita!",
    (3721, "Eeeek! It's human flesh!"):              # これは人肉だ…うぇぇ！
        "Questa è carne umana... bleah!",
    (3739, "You would've rather eaten human flesh."):  # 人肉の方が好みだが…
        "Veramente preferirei carne umana...",
    # ----------------------------------------------------------- i cibi speciali
    (3818, "「Ugh-Ughu」  spew up ."):               # 「げふぅ」…は種を吐き出した。
        '"\\"Urp\\" " + name(cc) + " sputa fuori " + itemname(ci, 1) + "."',
    (3835, "「Ugh-Ughu」  laid a platinum coin."):    # …の産んだ卵が割れて中からプラチナが出てきた。
        'name(cc) + " depone un uovo, che si spacca: dentro c\'è del platino."',
    (3847, " muttered Abura-Age...!"):               # 「あぶらあげぇ…♪1」
        'name(cc) + " mormora " + cnvtalk("Tofu frittooo...")',
    (3850, " muttered I want to eat more!"):         # 「おかわり！！」
        'name(cc) + " mormora " + cnvtalk("Il bis!!")',
    (3853, " muttered Ah, fried tofu is the best... ♪"):  # 「油揚げ最高っ…♪」
        'name(cc) + " mormora " + cnvtalk("Il tofu fritto è il massimo...")',
    (3856, " looks worrisomely happy..."):           # …は心配になるくらい幸せそうな表情を浮かべている。
        'name(cc) + " ha un\'aria talmente felice da far quasi preoccupare..."',
    # ---- copiate da altrove: stesso giapponese, resa gia' decisa (regola della 58a)
    (3868, "Your Ether Disease is cured greatly."):  # <- proc.hsp:25779
        "Gli anticorpi dell'etere si diffondono nel tuo corpo.",
    (3877, "This is hard!"):                         # <- command.hsp:15103
        "Che roba secca!",
    (3877, "This dries your mouth!"):                # <- command.hsp:15103
        "Mi si secca la bocca!",
    (3877, "Ugh, this is so dry!"):                  # <- command.hsp:15103
        "Uff, ho la bocca tutta secca!",
    (3877, "Ugh, this is hard!"):                    # <- command.hsp:15103
        "Uff, ma quanto è secco!",
    (3877, "Ugh, this is hard."):                    # <- command.hsp:15103
        "Uff, che roba secca.",
    (3881, " grew fatter and now weighs kg."):       # <- command.hsp:15108, con tc -> cc
        'name(cc) + " mette su peso: adesso pesa " + cdata(CDATA_WEIGHT, cc) + "kg."',
    (3888, " evolve."):                              # …は進化した。
        'name(cc) + " si evolve."',
}

USCITA = "fase4-item-002.jsonl"


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
