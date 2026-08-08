# strumenti/genera_toppe_nomi.py
"""Genera le toppe della composizione dei nomi, prendendo `cerca` dal sorgente.

    python -m strumenti.genera_toppe_nomi

Scriverle a mano significa sbagliare un tab e scoprirlo alla build, o peggio
non scoprirlo. Qui il blocco cercato e' una **fetta del file vero**, e lo
strumento rifiuta di emettere una toppa il cui blocco non compaia
**esattamente una volta**. Ha gia' impedito un errore: la riga che spegne il
pluralizzatore inglese compare due volte, perche' upstream tiene la versione
originale in commento poco sopra.

E' ripetibile: le toppe che genera portano `"generata": "nomi"` e a ogni giro
sostituiscono quelle vecchie invece di aggiungersi. Le toppe scritte a mano non
si toccano.

Al riallineamento a una nuova versione CGX questo e' il primo comando da
rilanciare: se upstream ha riscritto uno dei blocchi lo dice qui, invece che
alla build.
"""
import io
import json
import sys

from strumenti import percorsi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
GENERATA = "nomi"

def righe(nome):
    return (percorsi.SORGENTE_HSP / nome).read_bytes().decode('cp932').split('\r\n')

INIT = righe('init.hsp')
ITEM = righe('item_func.hsp')

def fetta(r, primo, ultimo):
    """righe da `primo` a `ultimo` compresi, a base 1"""
    return r[primo - 1:ultimo]

def ind(riga):
    return riga[:len(riga) - len(riga.lstrip())]

toppe = []

# 1. i due array del plurale, dichiarati accanto a quelli che affiancano
toppe.append({
    "file": "init.hsp",
    "cerca": fetta(INIT, 2569, 2570),
    "sostituisci": fetta(INIT, 2569, 2570) + [
        "\tsdim ioriginalnamerefplur, 128, MAX_DB",
        "\tsdim ioriginalnameref2plur, 128, MAX_DB",
    ],
    "motivo": "i due array del plurale italiano dei nomi degli oggetti. Dimensionati a MAX_DB, non lasciati autoespandere come i due che affiancano: quelli li assegna db_item.hsp per OGNI oggetto, il plurale ce l'hanno solo i nomi tradotti. Un array sparso letto oltre l'ultimo indice assegnato e' un Array overflow (crash in negozio, 2026-08-08), perche' l'autoespansione vale in scrittura e non in lettura. Li popola applica_plurali dal campo `plurale` del dizionario",
})

# 2. il giunto dei nomi composti: in italiano e' sempre "di"
r189 = INIT[188]
assert ' + " of " + ' in r189, r189
toppe.append({
    "file": "init.hsp",
    "cerca": r189,
    "sostituisci": r189.replace(' + " of " + ', ' + " di " + '),
    "motivo": "cnvitemname compone `ref2 + \" of \" + ref` fuori da lang(): il giunto inglese non passa dal dizionario. In italiano e' sempre \"di\" (contratto-nomi.md §3)",
})

# 3. lo stesso giunto in itemname(), che lo sceglie cercando "with" nel nome
#    inglese: una dipendenza da dato che tradurre i nomi romperebbe in silenzio.
#    Il nome che la fa scattare e' uno solo: `ornamented with flowers`.
blocco = fetta(ITEM, 1235, 1240)
assert 'instr(' in blocco[0] and '"with"' in blocco[0], blocco[0]
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": [f'{ind(blocco[0])}locvar_itemname_s3 = "di"'],
    "motivo": "il giunto si sceglieva cercando la sottostringa \"with\" DENTRO il nome inglese (un solo nome la contiene, `ornamented with flowers`): tradurre i nomi cambierebbe il ramo in silenzio. In italiano il giunto e' sempre \"di\"",
})

# 3-bis. le sei parole-contatore cablate in item_func, che il dizionario non
#        raggiunge: non stanno in db_item.hsp e non passano da lang(). Le rese
#        vengono da contatori.jsonl, unica sorgente di verita': cambiarle li'
#        e rilanciare questo comando aggiorna sia il singolare sia il plurale.
CONTATORI = {v["en"]: v for v in (
    json.loads(r) for r in
    (percorsi.PROGETTO / "contatori.jsonl").read_text(encoding="utf-8").splitlines()
    if r.strip())}

# riga dell'assegnazione -> parola inglese. Il blocco preso e' di tre righe --
# `if`, assegnazione, `}` -- perche' `cup` compare due volte con lo stesso
# testo: da sola sarebbe ambigua, e lo strumento rifiuterebbe di emetterla.
CABLATE = ((1223, "bottle"), (1226, "cup"), (1229, "cup"),
           (1243, "cargo"), (1246, "pair"), (1253, "dish"))

parole_cablate = []
for primo, inglese in CABLATE:
    blocco = fetta(ITEM, primo, primo + 2)
    resa = CONTATORI[inglese]
    assert f'"{inglese}"' in blocco[1], (primo, blocco[1])
    parole_cablate.append(resa)
    toppe.append({
        "file": "item_func.hsp",
        "cerca": blocco,
        "sostituisci": [blocco[0],
                        blocco[1].replace(f'"{inglese}"', f'"{resa["it"]}"'),
                        blocco[2]],
        "motivo": f"la parola-contatore «{inglese}» e' cablata in itemname() per classe di oggetto: non sta in db_item.hsp e non passa da lang(), quindi il dizionario non la raggiunge. Resa presa da contatori.jsonl: «{resa['it']}»",
    })


def plurale_delle_cablate(indentazione):
    """Il plurale delle parole-contatore che non vengono dal dizionario.

    Il loro plurale inglese lo faceva il pluralizzatore spento dalla toppa 4:
    senza questo `switch` ripiegherebbero sul singolare — «2 bottiglia di
    succo» — che e' peggio dell'inglese di partenza, non solo diverso.

    Si entra qui **solo** se il dizionario non ha gia' detto la sua: per i nomi
    di `db_item.hsp` il plurale arriva da `ioriginalnameref2plur` e questo
    blocco non si esegue.
    """
    righe = [f'{indentazione}switch locvar_itemname_s2']
    for resa in {r["it"]: r for r in parole_cablate}.values():
        righe += [f'{indentazione}\tcase "{resa["it"]}"',
                  f'{indentazione}\t\tlocvar_itemname_s5 = "{resa["plurale"]}"',
                  f'{indentazione}\t\tswbreak']
    righe += [f'{indentazione}\tdefault', f'{indentazione}\t\tswbreak',
              f'{indentazione}swend']
    return righe


# 4. il plurale della parola-contatore, che l'inglese fa col suffisso
blocco = fetta(ITEM, 1259, 1285)
assert blocco[0].strip() == 'if ( locvar_itemname_s2 != "" ) {', blocco[0]
i0 = ind(blocco[0])
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": [
        f'{i0}if ( locvar_itemname_s2 != "" ) {{',
        f'{i0}\tlocvar_itemname_s5 = ""',
        f'{i0}\tif ( locvar_itemowner_num2 > 1 ) {{',
        f'{i0}\t\tlocvar_itemname_s5 = ioriginalnameref2plur(inv(INV_ITEM_ID, itemname_itemid))',
        f'{i0}\t\tif ( locvar_itemname_s5 == "" ) {{',
    ] + plurale_delle_cablate(f'{i0}\t\t\t') + [
        f'{i0}\t\t}}',
        f'{i0}\t}}',
        f'{i0}\tif ( locvar_itemname_s5 == "" ) {{',
        f'{i0}\t\tlocvar_itemname_s5 = locvar_itemname_s2',
        f'{i0}\t}}',
        f'{i0}\tif ( locvar_itemowner_num2 > 1 ) {{',
        f'{i0}\t\tlocvar_itemowner_s = "" + locvar_itemowner_num2 + " " + locvar_itemowner_s + locvar_itemname_s5 + " " + locvar_itemname_s3 + " "',
        f'{i0}\t}}',
        f'{i0}\telse {{',
        f'{i0}\t\tlocvar_itemowner_s = locvar_itemowner_s + locvar_itemname_s2 + " " + locvar_itemname_s3 + " "',
        f'{i0}\t}}',
        f'{i0}}}',
    ],
    "motivo": "il plurale della parola-contatore si faceva col suffisso inglese (`scroll` + \"s \", `dish` + \"es \"): in italiano e' irregolare per parola e viene da ioriginalnameref2plur. Se il plurale manca si ripiega sul singolare, cosi' lo stato intermedio resta leggibile",
})

# 5-7. i tre punti vivi dove il nome si concatena. Gli altri tre che sembrano
#      uguali sono dentro blocchi /* ORIGINAL */, cioe' commentati, oppure nel
#      ramo `jp` che non si tocca.
APPENDE = 'locvar_itemowner_s += ioriginalnameref(inv(INV_ITEM_ID, itemname_itemid))'

def scelta_plurale(indentazione):
    """Il nome al plurale, ma solo dove l'inglese lo faceva.

    La guardia `locvar_itemname_s2 == ""` e' quella del pluralizzatore inglese
    che la toppa 8 spegne (`item_func.hsp:1842`): si flette **la parola-contatore
    oppure il nome, mai tutti e due**. In inglese «3 scrolls of identify»; in
    italiano «3 pergamene di identificazione», perche' la testa del sintagma e'
    il contatore e il complemento dopo «di» resta singolare.

    Senza la guardia uscirebbe «3 pergamene di identificazioni», e non per un
    dato sbagliato: `verifica.py` pretende il `plurale` su ogni nome tradotto,
    quindi la coda di un composto un plurale ce l'ha per forza. La regola su
    quando usarlo sta qui, nel codice, non nella disciplina di chi traduce.

    Le if sono annidate e non unite con `&`: HSP valuta le espressioni da
    sinistra a destra senza precedenza fra operatori, e una condizione composta
    andrebbe letta con attenzione ogni volta che qualcuno ci ripassa.
    """
    return [
        f'{indentazione}locvar_itemname_s5 = ""',
        f'{indentazione}if ( locvar_itemname_s2 == "" ) {{',
        f'{indentazione}\tif ( locvar_itemowner_num2 > 1 ) {{',
        f'{indentazione}\t\tlocvar_itemname_s5 = ioriginalnamerefplur(inv(INV_ITEM_ID, itemname_itemid))',
        f'{indentazione}\t}}',
        f'{indentazione}}}',
        f'{indentazione}if ( locvar_itemname_s5 != "" ) {{',
        f'{indentazione}\tlocvar_itemowner_s += locvar_itemname_s5',
        f'{indentazione}}}',
        f'{indentazione}else {{',
        f'{indentazione}\t{APPENDE}',
        f'{indentazione}}}',
    ]

MOTIVO_SITO = ("il nome si flette dove si concatena, non dopo: a valle "
               "locvar_itemowner_s e' gia' la stringa composta (benedizione, "
               "materiale, ego, titoli) e il sostantivo da flettere sta in mezzo, "
               "non in fondo come in inglese")

for primo, ultimo, quale in ((1728, 1734, "non identificato"),
                             (1746, 1748, "unico o prezioso"),
                             (1767, 1773, "identificato")):
    blocco = fetta(ITEM, primo, ultimo)
    riga_append = [r for r in blocco if r.strip() == APPENDE]
    assert len(riga_append) == 1, (primo, blocco)
    nuovo = []
    for r in blocco:
        nuovo.extend(scelta_plurale(ind(r)) if r.strip() == APPENDE else [r])
    toppe.append({
        "file": "item_func.hsp",
        "cerca": blocco,
        "sostituisci": nuovo,
        "motivo": f"{MOTIVO_SITO} — ramo «{quale}»",
    })

# 8. il pluralizzatore inglese del nome, reso irraggiungibile invece che
#    riscritto: sono 91 righe di suffissi e di eccezioni per oggetti gia'
#    plurali in inglese, e in italiano non ne serve nessuna.
#    La riga da spegnere compare DUE volte: upstream tiene la versione
#    originale in commento poco sopra, con lo stesso testo. Il blocco parte
#    percio' dal marcatore, che e' unico.
blocco = fetta(ITEM, 1840, 1842)
assert blocco[0].strip().startswith('/********** BLOODYSHADE'), blocco[0]
assert blocco[2].strip() == 'if ( locvar_itemname_s2 == "" ) {', blocco[2]
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": blocco[:2] + [
        f'{ind(blocco[2])}if ( 0 ) {{ // il plurale italiano viene da ioriginalnamerefplur, dove il nome si concatena',
    ],
    "motivo": "spegne il pluralizzatore inglese del nome (91 righe di suffissi e di eccezioni per oggetti gia' plurali). Si rende irraggiungibile invece di cancellarlo, cosi' resta leggibile accanto alla versione originale che upstream tiene in commento",
})

# --- il controllo che conta: ogni blocco compare esattamente una volta -------
sorgenti = {"init.hsp": INIT, "item_func.hsp": ITEM}
for t in toppe:
    cerca = t["cerca"] if isinstance(t["cerca"], list) else [t["cerca"]]
    r = sorgenti[t["file"]]
    quante = sum(1 for i in range(len(r) - len(cerca) + 1) if r[i:i + len(cerca)] == cerca)
    stato = "ok" if quante == 1 else f"!! {quante} VOLTE !!"
    print(f'{stato:10} {t["file"]:14} {len(cerca):3} righe -> {len(t["sostituisci"]) if isinstance(t["sostituisci"], list) else 1:3}   {t["motivo"][:60]}')
    assert quante == 1, t["motivo"]

for t in toppe:
    t["generata"] = GENERATA

percorso = percorsi.PROGETTO / "toppe.jsonl"
esistenti = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
# le generate del giro precedente si sostituiscono, non si accumulano; quelle
# scritte a mano restano dove sono
a_mano = [t for t in esistenti if t.get("generata") != GENERATA]
print(f'\ntoppe a mano: {len(a_mano)}, generate: {len(toppe)} '
      f'(ne sostituiscono {len(esistenti) - len(a_mano)})')
with percorso.open("w", encoding="utf-8", newline="\n") as f:
    for t in a_mano + toppe:
        f.write(json.dumps(t, ensure_ascii=False) + "\n")
print("scritto", percorso)
