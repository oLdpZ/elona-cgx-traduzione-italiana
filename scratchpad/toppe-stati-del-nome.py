# -*- coding: utf-8 -*-
"""Sposta gli stati dell'oggetto da PREFISSO a SUFFISSO fra parentesi.

Trovato in gioco nella 69a: **«un piatto di rotten pasta fresca»**. `rotten` e'
`item_func.hsp:1304`, una delle 241 righe non ancora tradotte di quel file — ma
non era una dimenticanza, era un muro.

⚠️⚠️ **UN AGGETTIVO PREFISSO NON SI PUO' TRADURRE IN ITALIANO SE SERVE PIU' DI
UN NOME.** `lang("腐った", "rotten ")` viene incollato **davanti** al nome
(`item_func.hsp:1499` appende il nome dopo l'accumulatore), e l'aggettivo
italiano prima del nome concorda: `pasta fresca` vuole «marcia», `pane` vuole
«marcio», `uova` vuole «marce». E questo prefisso serve **ogni cibo del gioco**.
E' il muro di `giftn` (69a, lotto `fase4-item-007`) senza la scappatoia che li'
c'era: `giftn` serviva un oggetto solo, «regalo», quindi il maschile era sicuro.

⭐ **La via d'uscita era gia' nel file.** Lo stesso compositore emette una
quarantina di stati **fra parentesi, in coda**, e nessuno di quelli concorda:
`(Scary)`, `(Dreadful)`, `(Temporal)`, `(Empty)`, `(Danger!)`, `(Herb)`,
`(Antiseptic)`, `(Aphrodisiac)`, `(Poisoned)`. `rotten` e `sample` sono gli
unici due stati scritti a rovescio rispetto agli altri quaranta: spostarli nella
famiglia li rende invariabili **e** uniformi.

    un piatto di rotten pasta fresca  ->  un piatto di pasta fresca (marcio)
    una rotten mela                   ->  una mela (marcio)

⭐ **`[Growable] ` invece resta dov'e'**, e non serve nessuna toppa: le
parentesi quadre ne fanno gia' un'etichetta, e «coltivabile» e' un aggettivo in
**-e**, cioe' invariabile al singolare per tutt'e due i generi. Va nel
dizionario come una voce normale. 💡 La differenza fra i tre prefissi non e' il
posto: e' se l'italiano ha o no una forma che non concorda.

⚠️ Le due righe toppate vanno **rinviate**: `applica` fa prima il dizionario e
poi le toppe, e `test_toppe.py` pretende che ogni `cerca` agganci il **sorgente
pinnato** (lezione della 53a). Una riga che il dizionario riscrive non e'
toppabile.

⚠️ Il testo di una toppa non passa da `degrada`: si scrive gia' senza accenti.
Qui non ce ne sono.

Le tre toppe:

  1. `:1299`-`:1301`  il prefisso `sample ` diventa vuoto nel ramo inglese
  2. `:1302`-`:1306`  il prefisso `rotten ` diventa vuoto nel ramo inglese
  3. `:2216`-`:2218`  dopo `(Antiseptic)` — che e' il vicino giusto, visto che
     l'antisettico e' quel che il marciume non ha — si appendono i due tag
     italiani. `itemname_itemid` e' in scope: fra `:1291` e `:2230` non c'e'
     nessun confine di funzione ne' nessun `return` di primo livello, e i due
     `goto *skipName` atterrano a `:1873`, cioe' **prima** del sito nuovo.
"""
import io
import json
import pathlib

RADICE = pathlib.Path(__file__).resolve().parent.parent
SORGENTE = pathlib.Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\item_func.hsp")

T = "\t"

TOPPE = [
    {
        "riga": 1299,
        "cerca": [
            T + 'if ( ibit(ITEM_BIT_SHOP_SAMPLE, itemname_itemid) == TRUE ) {',
            T * 2 + 'locvar_itemowner_s += lang("見本用の", "sample ")',
            T + '}',
        ],
        "sostituisci": [
            T + 'if ( ibit(ITEM_BIT_SHOP_SAMPLE, itemname_itemid) == TRUE ) {',
            T * 2 + 'locvar_itemowner_s += lang("見本用の", "")',
            T + '}',
        ],
    },
    {
        "riga": 1302,
        "cerca": [
            T + 'if ( inv(INV_ITEM_MATERIAL, itemname_itemid) == ITEM_MATERIAL_RAW ) {',
            T * 2 + 'if ( inv(INV_ITEM_ROT, itemname_itemid) < 0 ) {',
            T * 3 + 'locvar_itemowner_s += lang("腐った", "rotten ")',
            T * 2 + '}',
            T + '}',
        ],
        "sostituisci": [
            T + 'if ( inv(INV_ITEM_MATERIAL, itemname_itemid) == ITEM_MATERIAL_RAW ) {',
            T * 2 + 'if ( inv(INV_ITEM_ROT, itemname_itemid) < 0 ) {',
            T * 3 + 'locvar_itemowner_s += lang("腐った", "")',
            T * 2 + '}',
            T + '}',
        ],
    },
    {
        "riga": 2216,
        "cerca": [
            T + 'if ( ibit(ITEM_BIT_ANTISEPTIC, itemname_itemid) == 1 ) {',
            T * 2 + 'locvar_itemowner_s += lang("(防腐処理)", " (Antiseptic)")',
            T + '}',
        ],
        "sostituisci": [
            T + 'if ( ibit(ITEM_BIT_ANTISEPTIC, itemname_itemid) == 1 ) {',
            T * 2 + 'locvar_itemowner_s += lang("(防腐処理)", " (Antiseptic)")',
            T + '}',
            T + 'if ( en ) {',
            T * 2 + 'if ( inv(INV_ITEM_MATERIAL, itemname_itemid) == ITEM_MATERIAL_RAW ) {',
            T * 3 + 'if ( inv(INV_ITEM_ROT, itemname_itemid) < 0 ) {',
            T * 4 + 'locvar_itemowner_s += " (marcio)"',
            T * 3 + '}',
            T * 2 + '}',
            T * 2 + 'if ( ibit(ITEM_BIT_SHOP_SAMPLE, itemname_itemid) == TRUE ) {',
            T * 3 + 'locvar_itemowner_s += " (campione)"',
            T * 2 + '}',
            T + '}',
        ],
    },
]

MOTIVO = (
    "item_func.hsp:{riga}. **Non e' una resa mancante: e' un aggettivo che in italiano non "
    "puo' stare dove l'inglese lo mette.** `lang(\"{jp}\", \"{en}\")` viene incollato **davanti** "
    "al nome dell'oggetto (`item_func.hsp:1499` appende il nome dopo l'accumulatore), e "
    "l'aggettivo italiano prima del nome concorda col genere: «pasta fresca» vuole «marcia», "
    "«pane» vuole «marcio», «uova» vuole «marce». ⚠️ E questo prefisso serve **ogni cibo del "
    "gioco**, quindi non c'e' nessun genere sicuro da scegliere: e' il muro di `giftn` "
    "(lotto `fase4-item-007`) senza la scappatoia che li' c'era, dove il prefisso serviva un "
    "oggetto solo. 💡 La via d'uscita era gia' nel file: lo stesso compositore emette una "
    "quarantina di stati **fra parentesi, in coda** — `(Scary)`, `(Empty)`, `(Herb)`, "
    "`(Antiseptic)`, `(Poisoned)` — e nessuno di quelli concorda. La toppa svuota il prefisso "
    "nel ramo inglese e rimette lo stato in coda, accanto a `(Antiseptic)`. ⭐ E il confronto "
    "che si legge da solo: `[Growable] ` (`:1295`), che e' lo stesso genere di prefisso, **non** "
    "e' rinviato — «coltivabile» e' un aggettivo in -e, invariabile al singolare, e le quadre "
    "ne fanno gia' un'etichetta. La differenza non e' il posto: e' se l'italiano ha o no una "
    "forma che non concorda. Fatta nella 69a insieme al rinvio, dopo averla vista in gioco."
)

RINVIATE = {
    "387ca9a53b85af57eecc31daf56da6f62174e7a9": (1304, "腐った", "rotten "),
    "dd2a3cc21c517e783fe2355f4aab44380ccbc6d1": (1300, "見本用の", "sample "),
}


def main():
    righe = SORGENTE.read_bytes().decode("cp932").splitlines()

    # ⚠️ Il `cerca` e' fatto di righe INTERE del sorgente pinnato e va letto con
    # .splitlines(), o il \r del CRLF resta in coda e non aggancia niente (53a).
    for t in TOPPE:
        blocco = righe[t["riga"] - 1: t["riga"] - 1 + len(t["cerca"])]
        if blocco != t["cerca"]:
            raise SystemExit("toppa :%d - il `cerca` non e' il blocco del sorgente:\n  %r\n  %r"
                             % (t["riga"], t["cerca"], blocco))
        testo = "\n".join(righe)
        quante = testo.count("\n".join(t["cerca"]))
        if quante != 1:
            raise SystemExit("toppa :%d - il `cerca` aggancia %d blocchi, non uno"
                             % (t["riga"], quante))

    nuove = [{"file": "item_func.hsp", "cerca": t["cerca"], "sostituisci": t["sostituisci"],
              "motivo": MOTIVO.format(riga=t["riga"], jp="腐った", en="rotten ")}
             for t in TOPPE]
    with io.open(RADICE / "lavoro" / "toppe-stati-del-nome.jsonl", "w",
                 encoding="utf-8", newline="\n") as f:
        for t in nuove:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    rinvii = [{"firma": firma, "file": "item_func.hsp", "en": en,
               "rinviata_a": "nessuna fase: risolta da toppa (item_func.hsp:%d, applicata nella 69a)" % riga,
               "motivo": MOTIVO.format(riga=riga, jp=jp, en=en)}
              for firma, (riga, jp, en) in RINVIATE.items()]
    with io.open(RADICE / "lavoro" / "rinviate-stati-del-nome.jsonl", "w",
                 encoding="utf-8", newline="\n") as f:
        for r in rinvii:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("%d toppe provate contro il sorgente pinnato, un blocco ciascuna" % len(TOPPE))
    for t in TOPPE:
        print("   :%-6d %d righe -> %d" % (t["riga"], len(t["cerca"]), len(t["sostituisci"])))
    print("%d rinvii scritti" % len(rinvii))


if __name__ == "__main__":
    main()
