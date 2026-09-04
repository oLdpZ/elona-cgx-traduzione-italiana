"""Le toppe del lotto E: gli sparsi del gioco di carte che non sono battute.

Sono righe singole, ognuna con la sua ragione, e il meccanismo giusto e' la
toppa — lo stesso dei lotti A e B. ⚠️ Le righe dell'esportazione della lista
carte (`tcg.hsp:4632-4658`) sono IDENTICHE fra i tre blocchi: portano
`"tutte": true`, che e' la deroga dichiarata dell'ambiguita', e qui e' vera
perche' le tre occorrenze vogliono la stessa resa (sono la stessa colonna
della stessa tabella).

Lo script e' idempotente: se una toppa con la stessa `cerca` c'e' gia', non la
riscrive.
"""
import json

from strumenti import percorsi

MOTIVO_LISTA = (
    "Lotto E della Fase 6: i segnaposto della lista carte che `tcg.hsp:4612` "
    "esporta in `TCG_card_list.txt` (una tabella MediaWiki). ⚠️ Non e' un "
    "formato come l'intestazione TSV di `custom_itemlist.hsp`: e' prosa in "
    "una tabella dove il nome della carta, la descrizione d'effetto e i "
    "tratti arrivano gia' in italiano dal resto della catena, e lasciare "
    "queste in inglese farebbe una tabella meta' e meta'. "
    "«Razza», «Classe» e «Alias» sono quelli che il gioco usa gia' "
    "(`chara.hsp`, `command.hsp:Aka`). ⚠️ La riga compare in tutt'e tre i "
    "blocchi (giocatore, PNG, casuale) e vuole la stessa resa: per questo "
    "`tutte`."
)
MOTIVO_POKER = (
    "Lotto E della Fase 6: le giunture del gioco del poker "
    "(`tcg_skill.hsp:6228-6246`), dichiarate in `schede.GIUNTURE` dalla 137a e "
    "rimaste li' in attesa di questa decisione. Compongono il nome della carta "
    "davanti alla scheda: «ace of » + scheda -> «asso di » + scheda. I nomi "
    "italiani delle figure sono fante, donna, re."
)

TOPPE = [
    # ---- tcg_skill.hsp: le due descrizioni d'effetto fuori da tcg_mod ------
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\teffdesc@tcg(TCG_EFF_RYUTYE) = "In-Hand: Ryutye try to remember his Effect. Which is: " + effdesc@tcg(effref@tcg(TCG_SKILL_POWER, TCG_EFF_RYUTYE))',
        "sostituisci": '\t\t\teffdesc@tcg(TCG_EFF_RYUTYE) = "In mano: <Ryutye> cerca di ricordarsi il suo effetto. Che e\': " + effdesc@tcg(effref@tcg(TCG_SKILL_POWER, TCG_EFF_RYUTYE))',
        "motivo": (
            "Lotto E della Fase 6: una descrizione d'effetto che sta in "
            "`tcg_skill.hsp` e non in `tcg_mod.hsp`, dove `carte.py` e' "
            "l'unico a guardare. ⚠️ E' la GEMELLA di "
            "`effdesc@tcg(TCG_EFF_RYUTYE)` gia' resa in Fase 5 («In mano: "
            "<Ryutye> cerca di ricordarsi il suo effetto (un Grido di "
            "battaglia).. »): la riscrive a runtime quando il suo effetto "
            "cambia, e le due devono dire la stessa cosa nello stesso "
            "registro. `In-Hand:` e' «In mano:» in tutte le 833 descrizioni."
        ),
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\t\teffdesc@tcg(TCG_EFF_NONE) = "You can\'t seem to remember this Card\'s Effect."',
        "sostituisci": '\t\t\t\t\teffdesc@tcg(TCG_EFF_NONE) = "Non riesci a ricordarti l\'effetto di questa carta."',
        "motivo": (
            "Lotto E della Fase 6: l'altra descrizione d'effetto di "
            "`tcg_skill.hsp`. ⚠️ Riscrive `TCG_EFF_NONE`, che in "
            "`tcg_mod.hsp` e' «Nessun effetto.»: sono due testi diversi per "
            "la stessa costante, e questo lo mette in campo <Zaile> quando "
            "cancella il testo delle carte. Il gioco non contraddice se' "
            "stesso — la seconda sostituisce la prima a runtime — e per "
            "questo la resa NON deve essere «Nessun effetto.»"
        ),
    },
    # ---- tcg_skill.hsp: i nomi generati -----------------------------------
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\t\t\tboozenames@tcg = "Beer", "Ale", "Love Potion", "Whiskey", "Sake", "Tequila", "Aqua Parti-o", "Hangover", "Cola", "Wa\'ah"',
        "sostituisci": '\t\t\t\t\t\tboozenames@tcg = "Birra", "Birra chiara", "Filtro d\'amore", "Whisky", "Sake", "Tequila", "Acqua Fest-o", "Sbornia", "Cola", "Wa\'ah"',
        "motivo": (
            "Lotto E della Fase 6: i dieci nomi di bevanda che compongono il "
            "nome della carta «High Potion of ...» (`tcg_skill.hsp:931`). "
            "⚠️⚠️ Il censimento ne vedeva **due** — «Love Potion» e «Aqua "
            "Parti-o» — perche' `_PROSA` pretende due parole: le altre otto "
            "sono a schermo esattamente come quelle, ed e' lo stesso buco "
            "delle battute del lotto D. `beer`, `cola` e `love potion` "
            "seguono `db_item.hsp` («birra», «cola», «filtro d'amore»). "
            "«Sake», «Tequila», «Cola» e «Wa'ah» restano identici perche' "
            "l'italiano li scrive uguali; «Aqua Parti-o» e' un finto latino "
            "da festa e la resa ne tiene la forma."
        ),
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "High Potion of " + boozenames@tcg(rnd(10)) + "    No.???   very potent beer  Rare:None\\n[Command Card]\\nEffect: Gain 1 Extra Mana."',
        "sostituisci": '\t\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "Pozione forte di " + boozenames@tcg(rnd(10)) + "    No.???   very potent beer  Rare:None\\n[Command Card]\\nEffect: Gain 1 Extra Mana."',
        "motivo": (
            "Lotto E della Fase 6: la giuntura «High Potion of », dichiarata "
            "in `schede.GIUNTURE` dalla 137a. ⚠️ La toppa cambia SOLO la "
            "giuntura: il resto della riga e' una scheda di carta, che "
            "`schede --applica` riscrive dopo con la sua resa dal "
            "dizionario. Due meccanismi sulla stessa riga, ognuno sul suo "
            "pezzo, ed e' il motivo per cui `applica` gira per primo."
        ),
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tmarkerwords = "v","V","shoot me","ELEA","x","this guy","here"',
        "sostituisci": '\t\t\t\tmarkerwords = "v","V","sparami","ELEA","x","questo","qui"',
        "motivo": (
            "Lotto E della Fase 6: le scritte che il bersaglio si ritrova "
            "appiccicate addosso (`TCG_CARDN_REF_TAG`, disegnate da "
            "`tcg.hsp:864` dentro un bollino da 24 px). ⚠️ Le rese sono "
            "tutte piu' CORTE dell'inglese, perche' il bollino centra con "
            "`12 - 3 * strlen` e l'inglese lo sfora gia': «sparami» 7 contro "
            "8, «questo» 6 contro 8, «qui» 3 contro 4. «v», «V», «x» e "
            "«ELEA» non sono parole."
        ),
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "socks of " + name@tcg + "  No.???   socks  Rare:why?\\nEffect: Everyone on Field gets -1/-1, Except Kuroya gets +1/+1.\\n          If this is in your Hand when you win, get Opponent\'s socks."',
        "sostituisci": '\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "calzini di " + name@tcg + "  No.???   socks  Rare:why?\\nEffect: Everyone on Field gets -1/-1, Except Kuroya gets +1/+1.\\n          If this is in your Hand when you win, get Opponent\'s socks."',
        "motivo": (
            "Lotto E della Fase 6: la giuntura «socks of », dichiarata in "
            "`schede.GIUNTURE` dalla 137a. «socks» e' «calzini» in "
            "`db_item.hsp`. ⚠️ Come per «High Potion of », la toppa cambia "
            "solo la giuntura: la scheda che segue la riscrive "
            "`schede --applica`."
        ),
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "ace of " + carddetailneff@tcg(aeft@tcg)',
        "sostituisci": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "asso di " + carddetailneff@tcg(aeft@tcg)',
        "motivo": MOTIVO_POKER,
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "" + pokerrank@tcg + " of " + carddetailneff@tcg(aeft@tcg)',
        "sostituisci": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "" + pokerrank@tcg + " di " + carddetailneff@tcg(aeft@tcg)',
        "motivo": MOTIVO_POKER + " Qui la giuntura e' « of » nuda, fra il numero e il seme.",
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "jack of " + carddetailneff@tcg(aeft@tcg)',
        "sostituisci": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "fante di " + carddetailneff@tcg(aeft@tcg)',
        "motivo": MOTIVO_POKER,
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "queen of " + carddetailneff@tcg(aeft@tcg)',
        "sostituisci": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "donna di " + carddetailneff@tcg(aeft@tcg)',
        "motivo": MOTIVO_POKER,
    },
    {
        "file": "tcg_skill.hsp",
        "cerca": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "king of " + carddetailneff@tcg(aeft@tcg)',
        "sostituisci": '\t\t\t\tcarddetailneff@tcg(aeft@tcg) = "re di " + carddetailneff@tcg(aeft@tcg)',
        "motivo": MOTIVO_POKER,
    },
    # ---- tcg.hsp ----------------------------------------------------------
    {
        "file": "tcg.hsp",
        "tutte": True,
        "cerca": '\t\tfiledsc = "ElonaPlus CGX custom Deck"',
        "sostituisci": '\t\tfiledsc = "Mazzo personalizzato di ElonaPlus CGX"',
        "motivo": (
            "Lotto E della Fase 6: la descrizione del tipo di file nella "
            "finestra di dialogo di Windows che salva e carica un mazzo "
            "(`_fdialog`, `tcg.hsp:4559` e `:4579`: due volte, una per il "
            "salvataggio e una per il caricamento, e vogliono la stessa "
            "resa). ⚠️ E' testo a schermo come "
            "qualunque altro — lo disegna il sistema operativo invece del "
            "gioco — e la riga sopra («Enter file name.») e' gia' tradotta "
            "dentro una `lang()`."
        ),
    },
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tcardrefcost = "race dependent"',
     "sostituisci": '\t\t\t\t\tcardrefcost = "dipende dalla razza"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tcardrefattack = "race/class dependent"',
     "sostituisci": '\t\t\t\t\tcardrefattack = "dipende da razza e classe"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tcardrefhp = "race/class dependent"',
     "sostituisci": '\t\t\t\t\tcardrefhp = "dipende da razza e classe"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\ts@tcg = "class dependent"',
     "sostituisci": '\t\t\t\t\ts@tcg = "dipende dalla classe"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tbits@tcg = "class/affliation dependent"',
     "sostituisci": '\t\t\t\t\tbits@tcg = "dipende da classe e affiliazione"',
     "motivo": MOTIVO_LISTA + " ⓘ «affliation» e' un refuso di monte: non porta"
                              " nessun comportamento, quindi la resa e' la"
                              " parola giusta."},
    {"file": "tcg.hsp",
     "cerca": '\t\t\t\t\tbits@tcg = "class dependent"',
     "sostituisci": '\t\t\t\t\tbits@tcg = "dipende dalla classe"',
     "motivo": MOTIVO_LISTA + " ⓘ Questa riga e' UNICA (solo il blocco della"
                              " carta casuale): il blocco del giocatore e"
                              " quello del PNG scrivono «class/affliation"
                              " dependent». Niente `tutte`, e il cancello lo"
                              " pretende."},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tcardrefrace = "player race"',
     "sostituisci": '\t\t\t\t\tcardrefrace = "razza del giocatore"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp", "tutte": True,
     "cerca": '\t\t\t\t\tcardrefclass = "player class"',
     "sostituisci": '\t\t\t\t\tcardrefclass = "classe del giocatore"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp",
     "cerca": '\t\t\t\t\tcardrefrace = "random race"',
     "sostituisci": '\t\t\t\t\tcardrefrace = "razza a caso"',
     "motivo": MOTIVO_LISTA + " ⓘ Unica: solo il blocco della carta casuale."},
    {"file": "tcg.hsp",
     "cerca": '\t\t\t\t\tcardrefclass = "random class"',
     "sostituisci": '\t\t\t\t\tcardrefclass = "classe a caso"',
     "motivo": MOTIVO_LISTA + " ⓘ Unica: solo il blocco della carta casuale."},
    {"file": "tcg.hsp",
     "cerca": '\t\t\t\t\tcardrefn = "[AKA] [Player Name]"',
     "sostituisci": '\t\t\t\t\tcardrefn = "[Alias] [Nome giocatore]"',
     "motivo": MOTIVO_LISTA},
    {"file": "tcg.hsp",
     "cerca": '\t\t\t\t\tcardrefn = "[Random AKA] [Random Name]"',
     "sostituisci": '\t\t\t\t\tcardrefn = "[Alias a caso] [Nome a caso]"',
     "motivo": MOTIVO_LISTA},
]


def main() -> None:
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    gia = {(t["file"], t["cerca"] if isinstance(t["cerca"], str) else
            tuple(t["cerca"])) for t in esistenti}

    testi = {}
    nuove = []
    for toppa in TOPPE:
        nome = toppa["file"]
        if nome not in testi:
            testi[nome] = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
            righe = testi[nome].split("\r\n")
            if len(righe) < 500:
                raise SystemExit("%s: la divisione in righe e' fallita" % nome)
            testi[nome] = righe

        quante = testi[nome].count(toppa["cerca"])
        if quante == 0:
            raise SystemExit("%s: la riga cercata non esiste nel sorgente: %r"
                             % (nome, toppa["cerca"][:70]))
        if quante > 1 and not toppa.get("tutte"):
            raise SystemExit("%s: la riga compare %d volte e la toppa non"
                             " dichiara `tutte`: %r"
                             % (nome, quante, toppa["cerca"][:70]))
        if quante == 1 and toppa.get("tutte"):
            raise SystemExit("%s: la toppa dichiara `tutte` ma la riga e'"
                             " unica: la deroga non serve e mente: %r"
                             % (nome, toppa["cerca"][:70]))
        if toppa["cerca"] == toppa["sostituisci"]:
            raise SystemExit("toppa muta: %r" % toppa["cerca"][:70])
        toppa["sostituisci"].encode("cp932")

        if (nome, toppa["cerca"]) in gia:
            print("gia' presente, saltata: %r" % toppa["cerca"][:60])
            continue
        nuove.append(toppa)
        print("%-16s x%d  %r" % (nome, quante, toppa["sostituisci"].strip()[:76]))

    if nuove:
        with percorso.open("a", encoding="utf-8") as scrittura:
            for toppa in nuove:
                scrittura.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("\ntoppe nuove: %d   (totale: %d)" % (len(nuove),
                                                len(esistenti) + len(nuove)))


if __name__ == "__main__":
    main()
