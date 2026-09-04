"""Quanto e' larga la riga dei tratti, in inglese e in italiano, carta per carta.

`tcg.hsp:1520-1605` costruisce la seconda riga della scheda concatenando le
etichette dei bit **accesi su quella carta**. Quella riga **non passa da
`talk_conv`**: `reconstruct_card_text` la prende intera (`lines@tcg(1)`) e `mes`
la disegna verbatim. Quindi la sua larghezza non la limita niente, e l'italiano
la allunga.

Il soffitto e' lo stesso della Fase 5 e per lo stesso motivo: **il massimo che
l'inglese di monte gia' disegna**. Sotto quello si sa che il riquadro regge;
sopra non si sa niente.

⚠️ Le combinazioni non si ipotizzano: si leggono dai 1.152 `cardrefbits = "..."`
del sorgente. Una prova che inventa il caso peggiore non prova niente
(lezione della 107a).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

COSTANTE = re.compile(r"#define global\s+(TCG_BIT_[A-Z_0-9]+)\s+(\d+)")
ETICHETTA = re.compile(r"if \( p@tcg == (TCG_BIT_[A-Z_0-9]+) \) \{ s@tcg \+= \"([^\"]*)\"\}")
BITS = re.compile(r'cardrefbits = "([^"]*)"')

TESTA_EN = "Bits:  "
TESTA_IT = "Tratti:  "

# Il lotto B, deciso qui e non altrove finche' non e' misurato.
# `None` = resta invariata, e la ragione sta accanto.
RESE = {
    # --- le gilde e le affiliazioni ------------------------------------
    "<Fighter Guild> ": "<Gilda dei Guerrieri> ",   # come chat.hsp e db_card
    "<Thief Guild> ":   "<Gilda dei Ladri> ",
    "<Mage Guild> ":    "<Gilda dei Maghi> ",
    "<Bandit> ":        "<Bandito> ",
    "<Mercenary> ":     "<Mercenario> ",           # «il mercenario», db_creature
    "<Citizen> ":       "<Cittadino> ",            # «il cittadino», db_creature
    "<Adventurer> ":    "<Avventuriero> ",
    "<Teacher> ":       "<Insegnante> ",           # «l'insegnante», db_creature
    "<Pirate> ":        "<Pirata> ",               # «il pirata», db_creature
    "<Flame> ":         "<Fiamma> ",               # TCG_BIT_FLAMETOWER
    "<Elea Mob> ":      "<Folla Elea> ",           # ELEAMOB, contro ELEAREFUGEE
    # --- le etichette fra parentesi quadre -----------------------------
    "[Command Card] ":  "[Carta comando] ",
    "[Illegal Card] ":  "[Carta illegale] ",
    "[Cannot Sacrifice] ": "[Non sacrificabile] ",
    "[No Deckbuild Limit] ": "[Nessun limite nel mazzo] ",
    "[Starts in your Hand] ": "[Parte nella tua mano] ",
    "[Starts in Opponent Deck] ": "[Parte nel mazzo avversario] ",
    "[Summoned on Opponent Field] ": "[Evocata nel campo avversario] ",
    "[Drawn when Mana=Cost] ": "[Pescata quando Mana=Costo] ",
    "[Cannot be drawn when Mana<=2] ": "[Non si pesca con Mana<=2] ",
    "[Cost at least 1 Mana] ": "[Costa almeno 1 Mana] ",
    "[Effect Cost 2 Life] ": "[L'effetto costa 2 di vita] ",
    "[Discard if not Played] ": "[Scartata se non giocata] ",
    "[Return on Begin Phase] ": "[Torna alla Fase iniziale] ",
    "[After Drawn: Discard this and Draw 1] ":
        "[Dopo la pesca: scartala e pesca 1] ",
    "[Does Nothing until Unfossiled/Graved] ":
        "[Inerte fino a dissotterramento/cimitero] ",
    "[Summon itself when Sent to Graveyard from Deck] ":
        "[Si evoca se va dal mazzo al cimitero] ",
    # ⚠️ Accorciata, non imbottita: con «Evocata nel mazzo avversario» la riga
    # dei tratti passava da 67 colonne in inglese a 81 in italiano, ed era
    # l'UNICA delle 249 combinazioni vere a uscire per colpa della traduzione.
    # «Nel mazzo avversario» dice dove finisce, che e' quel che serve sapere.
    "[Summoned into Opponent Deck / Gain [OnDraw:Discard&Draw1]] ":
        "[Nel mazzo avversario / ottiene [Alla pesca: scarta e pesca 1]] ",
}

INVARIATE = {
    "<Yerles> ": "nome proprio di civilta'",
    "<Xeren> ": "nome proprio di civilta'",
    "<Zanan> ": "nome proprio di civilta'",
    "<Lothrian> ": "nome proprio di civilta'",
    "<Eulderna> ": "nome proprio di civilta'",
    "<Elea> ": "nome proprio di razza (TCG_BIT_ELEAREFUGEE)",
    "<Juere> ": "nome proprio di civilta'",
    "<Zaile> ": "nome proprio di civilta'",
    "<Ninja> ": "in italiano si scrive uguale",
    "<CNPC> ": "sigla tecnica: Custom NPC, la cartella dell'utente",
    "[???] ": "segnaposto, non una parola",
    "Immune ": "in italiano si scrive uguale (lotto A)",
    "Kamikaze ": "in italiano si scrive uguale (lotto A)",
}


def _sorgente(nome: str) -> list[str]:
    righe = (percorsi.SORGENTE_HSP / nome).read_text(encoding="cp932").splitlines()
    if len(righe) < 500:
        raise SystemExit("%s: divisione fallita (%d righe)" % (nome, len(righe)))
    return righe


def main() -> int:
    tcg = "\n".join(_sorgente("tcg.hsp"))
    mod = "\n".join(_sorgente("tcg_mod.hsp"))

    numero_di = {n: int(v) for n, v in COSTANTE.findall(mod)}
    inglese_di = {}
    for costante, testo in ETICHETTA.findall(tcg):
        if costante in numero_di:
            inglese_di[numero_di[costante]] = testo
    if len(inglese_di) < 40:
        raise SystemExit("solo %d etichette agganciate: il riconoscitore non"
                         " sta leggendo il blocco giusto" % len(inglese_di))

    # ⚠️ Ogni etichetta a schermo dev'essere DECISA: o resa, o dichiarata
    # invariata con la sua ragione. Una tabella incompleta non sbaglia: tace
    # (la lezione della 136a su `PAROLE_CHIAVE`, 7 voci su 26).
    from strumenti.carte import PAROLE_CHIAVE
    # ⚠️ `PAROLE_CHIAVE` scrive «First Strike» con lo spazio, il sorgente
    # «First-Strike» col trattino: la sola tabella del glossario lascerebbe
    # fuori quattro etichette che il lotto A ha gia' reso.
    gia_fatte = ({"%s " % k for k in PAROLE_CHIAVE}
                 | {"Windfury(1) ", "First-Strike ", "Dual-Strike ",
                    "Splits ", "Kamikaze "})
    non_decise = [e for e in inglese_di.values()
                  if e not in RESE and e not in INVARIATE and e not in gia_fatte]
    if non_decise:
        raise SystemExit("etichette a schermo che nessuno ha deciso: %s"
                         % non_decise)

    # ⚠️⚠️ Le rese del lotto A vanno LETTE, non escluse. Il primo giro le aveva
    # messe fra le `gia_fatte` — cioe' fra quelle di cui non ci si occupa — e
    # la misura ricadeva sull'inglese: usciva «Regeneration Armored Flying»
    # dentro la riga italiana, e uno scarto di +4 colonne dove il vero e' molto
    # piu' largo. Una tabella incompleta non sbaglia: tace, e il controllo di
    # completezza qui sopra non l'aveva vista perche' controlla che siano
    # DECISE, non che questa misura ne conosca la resa.
    import json
    for riga_toppa in (percorsi.PROGETTO / "toppe.jsonl").read_text(
            encoding="utf-8").splitlines():
        if not riga_toppa.strip():
            continue
        toppa = json.loads(riga_toppa)
        if toppa["file"] != "tcg.hsp":
            continue
        cerca, sostituisci = toppa["cerca"], toppa["sostituisci"]
        if isinstance(cerca, list) or "s@tcg +=" not in cerca:
            continue
        prima = re.search(r's@tcg \+= "([^"]*)"', cerca)
        dopo = re.search(r's@tcg \+= "([^"]*)"', sostituisci)
        if prima and dopo and prima.group(1) in inglese_di.values():
            RESE.setdefault(prima.group(1), dopo.group(1))

    mancanti = [e for e in inglese_di.values()
                if e not in RESE and e not in INVARIATE]
    if mancanti:
        raise SystemExit("etichette senza resa NOTA A QUESTA MISURA: %s"
                         % mancanti)

    combinazioni = set(BITS.findall("\n".join(_sorgente("db_card.hsp"))
                                    + "\n"
                                    + "\n".join(_sorgente("tcg_custom.hsp"))))
    combinazioni.discard("")
    print("combinazioni di bit lette dal sorgente: %d" % len(combinazioni))

    peggio_en, peggio_it = (0, ""), (0, "")
    for combinazione in combinazioni:
        en, it = TESTA_EN, TESTA_IT
        for pezzo in combinazione.split(","):
            if not pezzo.strip().isdigit():
                continue
            etichetta = inglese_di.get(int(pezzo))
            if etichetta is None:
                continue
            en += etichetta
            it += RESE.get(etichetta, etichetta)
        peggio_en = max(peggio_en, (len(en), en))
        peggio_it = max(peggio_it, (len(it), it))

    print()
    print("riga dei tratti piu' larga, INGLESE : %d colonne" % peggio_en[0])
    print("   %s" % peggio_en[1])
    print("riga dei tratti piu' larga, ITALIANO: %d colonne" % peggio_it[0])
    print("   %s" % peggio_it[1])
    print()
    scarto = peggio_it[0] - peggio_en[0]
    print("scarto sul massimo: %+d colonne" % scarto)
    print()

    # ⭐ Il massimo da solo non dice niente di utile, perche' l'INGLESE e' gia'
    # a 154 colonne: quella riga esce dal riquadro da prima di noi. La domanda
    # che si puo' agire e' un'altra — **quante carte l'italiano fa uscire che
    # in inglese ci stavano**. Il confine e' 77, la larghezza piu' grande che
    # l'inglese di monte disegna nella riga d'effetto (`carte.LARGHEZZA_MASSIMA`,
    # 137a): non e' il bordo vero del riquadro, che nessuno ha visto, ma e'
    # l'unica larghezza di cui si sappia che regge.
    from strumenti.carte import LARGHEZZA_MASSIMA as CONFINE

    dentro_en_fuori_it, fuori_en, dentro_tutt_e_due = 0, 0, 0
    nuove_fuori = []
    for combinazione in combinazioni:
        en, it = TESTA_EN, TESTA_IT
        for pezzo in combinazione.split(","):
            if not pezzo.strip().isdigit():
                continue
            etichetta = inglese_di.get(int(pezzo))
            if etichetta is None:
                continue
            en += etichetta
            it += RESE.get(etichetta, etichetta)
        if len(en) > CONFINE:
            fuori_en += 1
        elif len(it) > CONFINE:
            dentro_en_fuori_it += 1
            nuove_fuori.append((combinazione, len(en), en, len(it), it))
        else:
            dentro_tutt_e_due += 1

    print("sulle %d combinazioni di bit che le carte usano davvero,"
          " col confine a %d colonne:" % (len(combinazioni), CONFINE))
    print("   dentro in tutt'e due le lingue      : %d" % dentro_tutt_e_due)
    print("   ⚠️ dentro in inglese, FUORI in italiano: %d" % dentro_en_fuori_it)
    print("   gia' fuori in inglese               : %d" % fuori_en)
    for combinazione, largo_en, en, largo_it, it in nuove_fuori:
        print()
        print("   ⚠️ bit %s" % combinazione)
        print("      EN %3d  %s" % (largo_en, en))
        print("      IT %3d  %s" % (largo_it, it))

    if "--scrivi" in sys.argv:
        if nuove_fuori:
            raise SystemExit("non scrivo: ci sono ancora %d combinazioni che"
                             " l'italiano fa uscire" % len(nuove_fuori))
        print()
        print(scrivi_toppe(_sorgente("tcg.hsp")))
    return 0


MOTIVO = (
    "Lotto B della Fase 6: le etichette che `tcg.hsp:1520-1605` appende alla "
    "riga dei tratti della scheda di una carta. ⚠️ Ventisei di queste il "
    "censimento non le contava: `copertura._PROSA` pretende due parole "
    "alfabetiche separate da uno spazio, e ne bastano meno per sparire — "
    "`\"<Yerles> \"` ha una parola sola, e `\"Filter: Attack   \"` ne ha due ma "
    "coi due punti attaccati alla prima. Nello stesso menu, `\"Sort by: Attack "
    "  \"` invece si vedeva. ⚠️ Le gilde portano la forma che il progetto usa "
    "gia' in `chat.hsp` e `db_card.hsp` (Gilda dei Guerrieri/Ladri/Maghi), i "
    "mestieri quella di `db_creature.hsp`."
)


def scrivi_toppe(righe: list[str]) -> str:
    """Le toppe del lotto B, generate dalla stessa tabella che si e' misurata.

    ⚠️ La tabella sta in un posto solo apposta: al primo giro la misura non
    conosceva le rese del lotto A e ricadeva sull'inglese, dicendo +4 colonne
    dove il vero era +22. Due copie della stessa tabella sono due tabelle.
    """
    import json

    nuove = []
    for inglese, italiano in RESE.items():
        if inglese == italiano:
            continue
        ago = 's@tcg += "%s"' % inglese
        trovate = [r for r in righe if ago in r]
        if len(trovate) != 1:
            raise SystemExit("«%s»: %d righe, ne serviva 1"
                             % (inglese, len(trovate)))
        riga = trovate[0]
        nuove.append({"file": "tcg.hsp", "cerca": riga,
                      "sostituisci": riga.replace('"%s"' % inglese,
                                                  '"%s"' % italiano),
                      "motivo": MOTIVO})

    bersaglio = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = set()
    for testo in bersaglio.read_text(encoding="utf-8").splitlines():
        if testo.strip():
            cerca = json.loads(testo)["cerca"]
            esistenti.add(cerca if isinstance(cerca, str) else tuple(cerca))
    da_scrivere = [t for t in nuove if t["cerca"] not in esistenti]
    if not da_scrivere:
        return "niente da aggiungere: le %d toppe ci sono gia'" % len(nuove)
    with bersaglio.open("a", encoding="utf-8") as scrittura:
        for toppa in da_scrivere:
            scrittura.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    return ("toppe del lotto B aggiunte: %d   (gia' presenti %d)"
            % (len(da_scrivere), len(nuove) - len(da_scrivere)))


if __name__ == "__main__":
    raise SystemExit(main())
