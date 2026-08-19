# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-008.jsonl: il resto di item.hsp, e il file e' chiuso.

Le ultime 32 righe sparse: il manufatto che si sbriciola, il gatto che lecca, la
frutta che secca e marcisce, il **parassita cerebrale** con le sue quattro
battute, la stima automatica dello zaino, la cronaca dei manufatti, la cucina.
Con questo lotto `item.hsp` passa da **244 `lang()` e nessun dizionario** a zero
da fare.

⚠️⚠️ **`:1995` NON E' TESTO CHE SI LEGGE: E' UNA CHIAVE DI RICERCA, e per di
piu' una che deve combaciare con `:2002`.** `instr(cdatan(CDATAN_NAME, cc), 0,
lang("の子供", "child"))` cerca quella stringa **dentro il nome** di una
creatura, e il nome che la contiene lo scrive `:2002` due righe sotto:
`"child of " + cdatan(...)`. Se le due rese non combaciano, il gioco smette di
riconoscere i figli che ha appena battezzato e ne fa nascere all'infinito.
Percio' `:1995` e' **il suffisso esatto** che `:2002` appende, `": figlio"`, e
non una parola scelta a orecchio. E' la regola delle convenzioni — *quel che
serve a un confronto non e' testo, e si guarda il sito* — nella sua forma piu'
stretta: qui la stringa e' **insieme** chiave e testo a schermo.

⭐ E la forma di `:2002` non e' nuova: `main.hsp:6324` aveva gia' risolto lo
stesso problema con i due punti — `cdatan(CDATAN_NAME, ccbk) + ": figlio"` —
perche' «figlio di » + un nome che si porta l'articolo darebbe «figlio di la
tigre bianca» (`contratto-nomi.md` §4). Copiata invece di ridecisa.

⚠️ **`:2337` e `:2344` sono la cronaca di un manufatto, e in italiano cambiano
FORMA.** L'inglese incolla tre nomi dopo tre preposizioni — «held by X at Y in
D/M, Y» — e tutt'e tre quei nomi si portano l'articolo: «da la tigre», «a la
Terra della Tregua». La resa passa a una forma da registro, con i due punti al
posto delle preposizioni, che tiene tutte le funzioni di contenuto e non ne
incolla nessuna a una preposizione.

⭐ Tre rese copiate da altrove, stesso giapponese: `:2070` da
`calculation.hsp:1536`, `:3050` da `action.hsp:8282`, e la forma di `:2002` da
`main.hsp:6324`.

⚠️ `:1824` non puo' dire «si e' essiccata»: il participio concorda con
`itemname()`, che e' qualunque oggetto. Presente indicativo, come sempre.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti
from strumenti.funzioni import funzioni_di_contenuto

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    (49, " turns its shape into stardust."):         # …はスターダストに形を変えた。
        'locvar_convertartifact_n + " si sfa in polvere di stelle."',
    (337, " licks "):                                # …は…をぺろぺろとなめている。
        'name(catitem) + " sta leccando " + itemname(ci)',
    (1824, " dried up in the sun."):                 # …は上手い具合に干された。
        'itemname(cnt) + " prende il sole e si essicca per bene."',
    (1889, " rot."):                                 # …は腐った。
        'itemname(cnt) + " marcisce."',
    (1932, "A malicious hand filches some gold pieces from  wallet."):
        'name(cc) + " ha la borsa alleggerita da una mano malevola."',
    # -------------------------------------------------- il parassita cerebrale
    (1943, " pat  head uneasily."):                  # …は不安げに頭を押さえた。
        'name(cc) + " si tocca la testa con aria inquieta."',
    (1945, "There must've been a parasite in my head!"):   # 「そうか、頭の中に寄生虫が！」
        "Ecco, avevo un parassita in testa!",
    (1948, " desperately tried to maintain the sense of self."):  # …は必死に自我を保とうとしている。
        'name(cc) + " lotta disperatamente per non perdere la ragione."',
    (1950, "Stop...get it out..."):                  # 「やめろ…出ていけぇ…」
        "Basta... vattene fuori...",
    (1958, "The brain parasite has messed up  thinking!"):
        'name(cc) + " ha il cervello invaso dal parassita: il pensiero non gira più!"',
    (1960, "This is a blessing that should be spread throughout the world!"):
        "Ecco, questa è una benedizione da spargere per il mondo intero!",
    (1972, " pat  stomach uneasily."):               # …は不安げに腹を押さえた。
        'name(cc) + " si tocca la pancia con aria inquieta."',
    (1974, "I'm going to have a baby!"):             # 「なにかが産まれそうだよ！」
        "Sta per nascere qualcosa!",
    (1974, "Something is wrong with my stomach..."):  # 「腹になにかが…」
        "Ho qualcosa nella pancia...",
    (1980, "Something splits  body and breaks out!"):  # 何かが…の腹を破り飛び出した！
        'name(cc) + " si sente squarciare il ventre da qualcosa che salta fuori!"',
    # -- ⚠️ :1995 e :2002 devono COMBACIARE: la prima cerca dentro il nome che scrive la seconda
    (1995, "child"):
        ": figlio",
    (1997, "parasite kid"):                          # 寄生生物の子供
        "figlio del parassita",
    (2002, "child of "):                             # …の子供   <- la forma di main.hsp:6324
        'cdatan(CDATAN_NAME, cc) + ": figlio"',
    (2035, "Something sucks  blood."):               # 何かが…の血を吸った。
        'name(cc) + " si sente succhiare il sangue da qualcosa."',
    (2045, "Something sucks  MP."):                  # 何かが…のMPを吸った。
        'name(cc) + " si sente succhiare gli MP da qualcosa."',
    (2055, " become inexperienced."):                # …は未熟になった。
        'name(cc) + " regredisce a principiante."',
    (2070, "Several creatures are summoned from a magical vortex."):  # <- calculation.hsp:1536
        "Il vortice di mana evoca qualcosa!",
    # ------------------------------------------------------ la stima automatica
    (2109, "You appraise  as ."):                    # バックパックの中の…は…だと判明した。
        '"Nello zaino, " + s + " si rivela " + itemname(ci) + "."',
    (2122, "You sense the quality of  is ."):        # バックパックの中の…は…だという感じがする。
        'itemname(ci) + ", nello zaino: ne intuisci la qualità, " + _quality(inv(INV_ITEM_QUALITY, ci)) + "."',
    (2132, "You appraise some items in your backpack."):
        "Di qualche oggetto nello zaino adesso sai i dettagli.",
    # ----------------------------------------------------- la cronaca dei manufatti
    (2337, " was held by  at  in /, .\\n"):
        ('cnven(iknownnameref(inv(INV_ITEM_ID, ci))) + " passa di mano il " + gdata(GDATA_DAY) '
         '+ "/" + gdata(GDATA_MONTH) + ", anno " + gdata(GDATA_YEAR) + ". Nuovo padrone: " '
         '+ cdatan(CDATAN_NAME, ii_p) + ". Luogo: " + mapname(cdata(CDATA_AREA, ii_p)) + ".\\n"'),
    (2344, " was created at  in /, .\\n"):
        ('cnven(iknownnameref(inv(INV_ITEM_ID, ci))) + " nasce il " + gdata(GDATA_DAY) + "/" '
         '+ gdata(GDATA_MONTH) + ", anno " + gdata(GDATA_YEAR) + ". Luogo: " '
         '+ mdatan(MDATAN_NAME) + ".\\n"'),
    # ------------------------------------------------------------------ il resto
    (2779, "Uh...!"):                                # 「あ…！」
        "Ah...!",
    (2830, "But  stomach isn't affected."):          # しかし、…は何ともなかった。
        '"Ma " + name(cc) + " non ne risente."',
    (2879, 'Used the flame from the sculpture. \\"Purify it.\\"'):  # 胸像の炎も使った。「浄化せよ」
        'Hai usato anche la fiamma del busto. \\"Che sia purificato.\\"',
    (2948, "You cook  with  and make ."):            # …で…を料理して、…を作った。
        '"Cucini " + s + " con " + itemname(cooktool, 1) + " e ottieni " + itemname(ci, 1) + "."',
    (3050, "Your journal has been updated."):        # <- action.hsp:8282
        "Il tuo diario è stato aggiornato.",
}

USCITA = "fase4-item-008.jsonl"


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

    # ⚠️ La prova che :1995 e :2002 combaciano: la chiave di ricerca dev'essere
    # una sottostringa del nome che l'altra riga costruisce. Nessuna rete lo
    # guarda — e' un controllo che vale per questa coppia sola.
    chiave = RESE[(1995, "child")]
    costruito = RESE[(2002, "child of ")]
    if ('"%s"' % chiave) not in costruito:
        raise SystemExit("la chiave %r non compare nel nome costruito da :2002: %r"
                         % (chiave, costruito))

    # ⚠️ Il `\n` letterale (due caratteri) della cronaca va tenuto, e negli stessi punti.
    for d in voci:
        if d["en_grezzo"].count("\\n") != d["it"].count("\\n"):
            raise SystemExit(":%d - \\n nell'inglese %d, nella resa %d"
                             % (d["riga"], d["en_grezzo"].count("\\n"), d["it"].count("\\n")))
        atteso = funzioni_di_contenuto(d["en_grezzo"])
        nostro = funzioni_di_contenuto(d["it"]) if d["tipo"] == "dinamica" else atteso
        if d["tipo"] == "dinamica" and nostro != atteso:
            raise SystemExit(":%d - funzioni %s, attese %s" % (d["riga"], nostro, atteso))

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    print("la chiave di :1995 combacia col nome di :2002: %r" % chiave)
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"][:120]))


if __name__ == "__main__":
    main()
