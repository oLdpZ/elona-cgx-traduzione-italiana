# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-003.jsonl: il cioccolato, la mesugaki, la fortuna.

`item.hsp:3925`-`:4046`. Terzo lotto del file: quel che il cibo dice quando non
si limita a nutrire — il cioccolato guasto, la lotteria della `mesugaki`, la
gomma sputata, il kagami mochi, i due cibi che fanno girare la testa, il
biscotto della fortuna e i due pranzi che consolano.

⚠️⚠️ **LA TRAPPOLA DEL ♪ E' QUI.** `decisioni.md` (2026-08-19) l'aveva vista
arrivare e scritta a chiare lettere: «dieci righe del sorgente usano ♪ con una
cifra, **quattro in `item.hsp`**, che non e' ancora tradotto: la trappola e'
davanti a noi, non dietro». `msg_write` (`init.hsp:1372`-`:1386`) legge il
carattere **subito dopo** il ♪ come indice dell'icona da disegnare e poi toglie
dal testo la nota **e la cifra**. Una resa che si trovasse una cifra dopo la
nota la perderebbe in silenzio, e nessun controllo lo vedrebbe: il ♪ e' l'unico
carattere a due byte ammesso, quindi passa `doppi_byte_cp932` per costruzione.
La regola e' copiare l'icona che il sorgente sceglie, non inventarne una — e qui
sotto c'e' il controllo che lo verifica riga per riga contro monte.

⚠️ Le tre righe della `mesugaki` (`:3946`, `:3954`, `:3964`) sono le uniche del
lotto che portano il ♪, e tutt'e tre scelgono l'icona **1**.

⭐ 雑魚 e' «pesce piccolo» in tutt'e due i sensi, ed e' un pesce a dirlo: la
`mesugaki` e' un pesce (`invariati.md:182`, gioco di parole su メス牡蠣). L'inglese
lascia «Zako», che in italiano non dice niente; «pesce piccolo» tiene insieme
l'insulto e il fatto che a pronunciarlo sia un pesce.

⚠️ QUATTRO SITI IN CUI L'INGLESE DI MONTE HA COPIATO LA RIGA SBAGLIATA, e in
tutt'e quattro decide il giapponese (regola della 57a):

    :4013  頭がぼんやりしてきた «la testa si annebbia»  |  :4022  頭がクラクラした
           «la testa gira» — l'inglese scrive «Sheer madness!» per tutt'e due.
    :4041  心はすこし癒された «il cuore si rasserena»   |  :4046  身体を魔力が
           優しく包み込んだ «il potere magico avvolge il corpo» — l'inglese scrive
           «heart is warmed» per tutt'e due.
    :3928  味の火薬箱 «una polveriera di sapore» — l'inglese dice «tastes just
           like cocoa powder», che e' un'altra cosa.
    :3952  これは…大当たりだ！ — l'inglese scrive `<Jackpot>`, con le parentesi
           angolari che in Elona marcano un individuo (`init.hsp:1713`). Qui non
           c'e' nessun individuo: e' una vincita. Le parentesi non si copiano.

⚠️ `:4013` e `:4022` sono **statiche in inglese e dinamiche in giapponese**: il
giapponese nomina il soggetto (`name(cc)`), l'inglese no. L'elenco delle
funzioni si accorda con **l'inglese** (`verifica.py:367`), quindi la resa non
puo' nominare nessuno: resta un'esclamazione senza soggetto.

⚠️ `:3969` non puo' dire «ti senti piu' fortunato»: e' un aggettivo riferito a
chi gioca, e il genere non si conosce (guida-stile).

⭐ `:3925` copiata da `proc.hsp:10561`, stesso giapponese.

Legge le voci gia' estratte da lavoro/_item.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    # -------------------------------------------------------------- il cioccolato
    (3925, "Arrrrg!"):                               # ぐわぁぁぁぁぁっ！！！  <- proc.hsp:10561
        "Aaaaaargh!!!",
    (3928, "It tastes just like cocoa powder!"):     # まさに味の火薬箱だ！
        "Questa sì che è una polveriera di sapore!",
    (3932, "There were hair and nails in the chocolate..."):  # チョコの中に髪の毛や爪が入っていた…。
        "Dentro il cioccolato c'erano capelli e unghie...",
    (3940, "There was a sense of incompatibility in the taste...  tilts  head, pondering."):
        '"Forse nel sapore c\'era qualcosa che non andava... " + name(cc) + " piega la testa."',
    # ------------------------------------------------- la mesugaki, e le sue note
    (3946, "You're a Zako even in terms of ideas♪1 "):   # 「考えることまで雑魚♪1」
        "Anche a pensare sei un pesce piccolo♪1 ",
    (3952, "<Jackpot>"):                             # これは…大当たりだ！！！
        "Questo è... un colpo grosso!!!",
    (3954, "Wow♪1 Zaaaako♪1♪1♪1 "):                  # 「うっわぁ♪1雑魚すぎ♪1♪1♪1」
        "Uuuuh♪1 che pesce piccolo♪1♪1♪1 ",
    (3962, "Jackpot!"):                              # これは…当たりだ！
        "Questo è... un bel colpo!",
    (3964, "Your stomach is weak and weak♪1 "):      # 「胃腸よわよわ♪1」
        "Che stomachino debole debole♪1 ",
    (3969, "You felt like you were in luck..."):     # 運が良くなった気がする…。
        "Senti che la fortuna gira dalla tua parte...",
    # ------------------------------------------------ la gomma, il mochi, la testa
    (3988, " spew up ."):                            # 「んべっ」
        'name(cc) + " sputa fuori " + itemname(ci, 1) + "."',
    (3992, "This is auspicious!"):                   # これは縁起がいい！
        "Questo sì che porta bene!",
    (4013, "Sheer madness!"):                        # …は頭がぼんやりしてきた。 (yith-yaki)
        "La testa si annebbia.",
    (4022, "Sheer madness!"):                        # …は頭がクラクラした。 (crimberry)
        "La testa gira.",
    # ------------------------------------------- il biscotto e i pranzi che consolano
    (4028, " read the paper fortune."):              # …はクッキーの中のおみくじを読んだ。
        'name(cc) + " legge l\'oracolo dentro il biscotto."',
    (4041, " heart is warmed."):                     # …の心はすこし癒された。
        'name(cc) + " si rasserena un poco."',
    (4046, " heart is warmed."):                     # …の身体を魔力が優しく包み込んだ。
        'name(cc) + " si sente avvolgere dolcemente dal potere magico."',
}

USCITA = "fase4-item-003.jsonl"
NOTA = re.compile(r"♪\d")


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

    # ⚠️ La regola di decisioni.md: un ♪ seguito da una cifra nell'italiano deve
    # comparire IDENTICO in una delle due forme di monte. Copiare l'icona che il
    # sorgente sceglie e' legittimo, inventarne una a partire dal testo no.
    for d in voci:
        nostre = NOTA.findall(d["it"])
        monte = set(NOTA.findall(d["jp_grezzo"])) | set(NOTA.findall(d["en_grezzo"]))
        intruse = sorted(set(nostre) - monte)
        if intruse:
            raise SystemExit(":%d - icone che monte non sceglie: %s (monte: %s)"
                             % (d["riga"], intruse, sorted(monte) or "nessuna"))
        if monte and not nostre:
            raise SystemExit(":%d - monte sceglie %s e la resa non ha nessuna nota"
                             % (d["riga"], sorted(monte)))

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    # ⚠️ Il ♪ e' l'unico carattere a due byte ammesso (init.hsp:1374 lo intercetta
    # e ci disegna un'icona), quindi lo si toglie prima di chiamare la guardia.
    guasti = {it: sorted(accenti.doppi_byte_cp932(it.replace("♪", "")))
              for it in RESE.values() if accenti.doppi_byte_cp932(it.replace("♪", ""))}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte (♪ escluso): %s" % (guasti or "nessuno"))
    print("note con icona, provate contro monte: %d righe"
          % sum(1 for d in voci if NOTA.search(d["it"])))
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
