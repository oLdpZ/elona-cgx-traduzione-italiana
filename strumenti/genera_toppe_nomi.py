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
DATA = righe('item_data.hsp')

def fetta(r, primo, ultimo):
    """righe da `primo` a `ultimo` compresi, a base 1"""
    return r[primo - 1:ultimo]

def ind(riga):
    return riga[:len(riga) - len(riga.lstrip())]

toppe = []

# 1. i quattro array italiani, dichiarati accanto a quelli che affiancano
toppe.append({
    "file": "init.hsp",
    "cerca": fetta(INIT, 2569, 2570),
    "sostituisci": fetta(INIT, 2569, 2570) + [
        "\tsdim ioriginalnamerefplur, 128, MAX_DB",
        "\tsdim ioriginalnameref2plur, 128, MAX_DB",
        "\tsdim ioriginalnamearticolo, 128, MAX_DB",
        "\tsdim ioriginalnamearticolodet, 128, MAX_DB",
    ],
    "motivo": "i quattro array italiani dei nomi degli oggetti: due per il plurale (uno per array del nome) e due per l'articolo, indeterminativo e determinativo, che ne bastano due perche' l'articolo lo regge la sola TESTA del nome. Dimensionati a MAX_DB, non lasciati autoespandere come i due che affiancano: quelli li assegna db_item.hsp per OGNI oggetto, questi ce l'hanno solo i nomi tradotti. Un array sparso letto oltre l'ultimo indice assegnato e' un Array overflow (crash in negozio, 2026-08-08), perche' l'autoespansione vale in scrittura e non in lettura. Li popola applica_dati_nome dai campi `plurale` e `genere` del dizionario",
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

# 9-14. il materiale, che in inglese precede il nome e in italiano lo segue.
#
# Si mette da parte in `locvar_itemname_s6` dove l'inglese lo scriveva, e si
# riversa **dopo** `*skipName`, che e' il punto in cui tutti i rami del nome
# convergono -- identificato, non identificato, unico, nome casuale, nome da
# file dell'utente. Riversarlo sui singoli rami significherebbe dimenticarne
# uno e perdere il materiale in silenzio; li' invece o ci passano tutti o non
# ci passa nessuno. E' anche prima dell'articolo inglese (riga 1809), che si
# antepone.
#
# Il giunto sta qui e non nel dato: `mtname` va letto anche da `command.hsp`
# («It is made of » + mtname), dove un «di» cotto nella stringa direbbe «fatto
# di di cuoio». Stessa lezione del `" of "` dei nomi composti.
MATERIALE = 'mtname(0, inv(INV_ITEM_MATERIAL, itemname_itemid))'
EPITETO = 'mtname(1, inv(INV_ITEM_MATERIAL, itemname_itemid))'

# riga -> (cosa si legge, come si aggancia). L'epiteto porta gia' la sua
# preposizione dal dizionario («di mistero», «dell'antichita'»): li' basta lo
# spazio. Per gli arredi l'inglese dice «silk work chair»: «di manifattura in
# seta» non chiede accordo di genere a nessuno dei due lati, mentre «lavorato»
# lo chiederebbe al materiale e «lavorata» all'oggetto.
#
# I due siti degli arredi (1399 e 1404) sono **identici riga per riga**: si
# distinguono solo per l'`if` che li racchiude, `!= SAND` contro `!= RAW`. Da
# sole sarebbero ambigue e lo strumento rifiuterebbe di emetterle -- e' la
# quarta volta che il controllo di unicita' cambia la forma di una toppa
# invece di lasciar passare un'ambiguita'.
DA_ANTEPORRE = (
    (1386, 1386, MATERIALE, ' di '),
    (1398, 1400, MATERIALE, ' di manifattura in '),
    (1403, 1405, MATERIALE, ' di manifattura in '),
    (1476, 1476, EPITETO, ' '),
    (1481, 1481, MATERIALE, ' di '),
)

for primo, ultimo, lettura, giunto in DA_ANTEPORRE:
    blocco = fetta(ITEM, primo, ultimo)
    da_spostare = [r for r in blocco if 'locvar_itemowner_s +=' in r and lettura in r]
    assert len(da_spostare) == 1, (primo, blocco)
    nuovo = [f'{ind(r)}locvar_itemname_s6 += "{giunto}" + {lettura}'
             if r in da_spostare else r for r in blocco]
    toppe.append({
        "file": "item_func.hsp",
        "cerca": blocco if len(blocco) > 1 else blocco[0],
        "sostituisci": nuovo if len(nuovo) > 1 else nuovo[0],
        "motivo": f"il materiale si antepone in inglese e segue in italiano: qui si mette da parte in locvar_itemname_s6 col giunto «{giunto.strip()}», e si riversa dopo *skipName. Il giunto sta nella toppa e non nel dato perche' mtname lo legge anche command.hsp, dove «fatto di» + «di cuoio» direbbe due volte la stessa preposizione",
    })

# 14-bis. la qualita' dell'arredo (`_furniture`, text.hsp:56): undici gradini
#         da «shabby» a «godly» che l'inglese antepone al nome. E' la stessa
#         forma gia' chiusa per materiale ed epiteti, e per lo stesso motivo:
#         sono **prefissi a un nome di genere ignoto**, e un aggettivo italiano
#         si accorderebbe — «tavolo scadente» ma «sedia scadente**a**»? No:
#         «shabby» andrebbe reso «malandato/malandata», e l'arredamento include
#         anche plurali («dei libri sparsi»). Le rese sono percio' complementi
#         invarianti per genere **e numero** («di fattura scadente»,
#         «da capolavoro»), che e' la sesta applicazione della stessa cura.
#
#         Va nella coda del materiale e non in una sua: il sito (1324) gira
#         PRIMA dei siti del materiale (1386+), quindi un `+=` sulla stessa s6
#         produce gia' l'ordine giusto — «tavolo moderno di fattura scadente di
#         manifattura in seta» — senza aggiungere una terza coda da azzerare.
#
#         Il gemello a riga 1077 NON si tocca: sta dentro `if ( jp )`, un ramo
#         che questa build non percorre mai.
riga = ITEM[1324 - 1]
assert 'locvar_itemowner_s +=' in riga and '_furniture(' in riga, riga
assert 'itemname_itemid' in riga, riga
toppe.append({
    "file": "item_func.hsp",
    "cerca": riga,
    "sostituisci": (f'{ind(riga)}locvar_itemname_s6 += " " + '
                    '_furniture(inv(INV_ITEM_SUB_NAME, itemname_itemid))'),
    "motivo": "la qualita' dell'arredo si antepone in inglese e segue in italiano, come materiale ed epiteti: e' un prefisso a un nome di genere ignoto, e le rese sono complementi invarianti. Stessa coda s6 del materiale perche' questo sito precede i suoi e l'ordine viene gratis. Il gemello a riga 1077 sta nel ramo jp e non si tocca",
})

# 15-17. benedizione, maledizione e dannazione: stessa storia dell'epiteto.
#        `strblessed` si antepone e in italiano «benedetto» seguirebbe il nome
#        **accordandosi** — «mantello benedetto», «pozione benedetta» — e il
#        genere non si conosce. Diventano complementi («con benedizione») e
#        vanno in una coda **loro**, perche' l'ordine italiano e' materiale
#        prima e stato dopo: «mantello leggero di platino con benedizione».
#        Solo il ramo inglese: nel ramo `jp` (riga 1151) l'ordine e' gia' quello
#        giusto e le stringhe giapponesi non si toccano.
for stato in ('strblessed', 'strcursed', 'strdoomed'):
    righe_stato = [i for i in range(1200, 1213)
                   if ITEM[i - 1].strip() == f'locvar_itemowner_s = {stato} + " "']
    assert len(righe_stato) == 1, (stato, righe_stato)
    riga = ITEM[righe_stato[0] - 1]
    toppe.append({
        "file": "item_func.hsp",
        "cerca": riga,
        "sostituisci": f'{ind(riga)}locvar_itemname_s7 = " " + {stato}',
        "motivo": f"{stato} si antepone al nome; in italiano e' un complemento che segue («con benedizione»), perche' un participio si accorderebbe con un oggetto di genere ignoto. Coda separata dal materiale: prima il materiale, poi lo stato",
    })

# l'azzeramento delle due code, una volta per chiamata, prima di ogni ramo
blocco = fetta(ITEM, 1143, 1144)
assert blocco[0].strip() == 'item_checkknown itemname_itemid', blocco[0]
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": [f'{ind(blocco[0])}locvar_itemname_s6 = ""',
                    f'{ind(blocco[0])}locvar_itemname_s7 = ""'] + blocco,
    "motivo": "azzera le due code (materiale e stato) a ogni chiamata di itemname(): senza, la coda dell'oggetto precedente resterebbe attaccata al successivo",
})

# il riversamento, nell'ordine italiano: prima il materiale, poi lo stato
blocco = fetta(ITEM, 1805, 1806)
assert blocco[0].strip() == '*skipName', blocco[0]
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": [blocco[0],
                    f'{ind(blocco[1])}locvar_itemowner_s += locvar_itemname_s6',
                    f'{ind(blocco[1])}locvar_itemowner_s += locvar_itemname_s7'] + blocco[1:],
    "motivo": "riversa materiale e stato dopo il nome, in quest'ordine («mantello di platino con benedizione»). Sta su *skipName perche' e' il punto dove tutti i rami del nome convergono: sui singoli rami se ne dimenticherebbe uno e la coda sparirebbe in silenzio. Ed e' prima dell'articolo inglese, che si antepone",
})

# 15. il buffer dei materiali: 18 byte non bastano all'italiano
riga = DATA[1266 - 1]
assert riga.strip() == 'sdim mtname, 18, 2, ITEM_MATERIAL_MAX', riga
toppe.append({
    "file": "item_data.hsp",
    "cerca": riga,
    "sostituisci": riga.replace('sdim mtname, 18,', 'sdim mtname, 48,'),
    "motivo": "18 byte per stringa non bastano: l'inglese piu' lungo e' `griffon scale` (13), «scaglia di grifone» sono 18 esatti, e un accento vero ne vale due dopo la degradazione. Stesso difetto degli array del plurale, visto dal lato del buffer invece che dell'indice",
})

# 18. l'articolo. L'inglese lo sceglie guardando la PRIMA LETTERA della stringa
#     composta (`a`/`an`, riga 1816) piu' un caso speciale scritto a mano per
#     `unicorn horn`. E' fonetica, e in inglese basta perche' l'articolo non ha
#     genere. In italiano l'articolo dipende dal genere del sostantivo TESTA,
#     che nella stringa composta sta in mezzo — «una pozione di cura delle
#     ferite lievi» — e nessuna lettera lo rivela.
#
#     Il genere e' quindi un dato del dizionario; la stringa dell'articolo la
#     deriva `strumenti/articolo.py` e viaggia in due array, come il plurale.
#     Qui si legge, con lo stesso ripiego: se l'articolo italiano manca resta
#     quello inglese, cosi' lo stato intermedio e' leggibile.
#
#     ⚠️ Le parole-contatore cablate vengono PRIMA dell'array, al contrario del
#     plurale. Non e' una svista: quando `itemname()` mette «paio» davanti al
#     nome, la testa del sintagma diventa «paio», e l'articolo lo regge lui —
#     «un paio di stivali pesanti», non «uno stivali pesanti». Il plurale non ha
#     lo stesso problema perche' li' l'array e la parola cablata non sono mai
#     pieni tutti e due.
from strumenti.articolo import articoli


def articolo_delle_cablate(indentazione):
    righe = [f'{indentazione}switch locvar_itemname_s2']
    for resa in {r["it"]: r for r in parole_cablate}.values():
        indeterminativo, determinativo = articoli(resa["genere"], resa["it"])
        righe += [f'{indentazione}\tcase "{resa["it"]}"',
                  f'{indentazione}\t\tlocvar_itemname_s8 = "{indeterminativo}"',
                  f'{indentazione}\t\tlocvar_itemname_s9 = "{determinativo}"',
                  f'{indentazione}\t\tswbreak']
    righe += [f'{indentazione}\tdefault', f'{indentazione}\t\tswbreak',
              f'{indentazione}swend']
    return righe


blocco = fetta(ITEM, 1807, 1826)
assert blocco[0].strip() == 'if ( itemname_arg3 == 0 ) {', blocco[0]
assert '"the " + locvar_itemowner_s' in blocco[2], blocco[2]
assert blocco[4].strip() == 'else {', blocco[4]
assert blocco[5].strip() == 'if ( locvar_itemowner_num2 == 1 ) {', blocco[5]
i0, i1 = ind(blocco[0]), ind(blocco[1])
# la condizione del «the» e il ripiego inglese si prendono VERBATIM dal
# sorgente: sono le due cose che non vogliamo riscrivere a mano
condizione_the = blocco[1]
ripiego_inglese = ['\t\t' + r for r in blocco[6:17]]
toppe.append({
    "file": "item_func.hsp",
    "cerca": blocco,
    "sostituisci": [
        blocco[0],
        f'{i1}locvar_itemname_s8 = ""',
        f'{i1}locvar_itemname_s9 = ""',
    ] + articolo_delle_cablate(i1) + [
        f'{i1}if ( locvar_itemname_s8 == "" ) {{',
        f'{i1}\tlocvar_itemname_s8 = ioriginalnamearticolo(inv(INV_ITEM_ID, itemname_itemid))',
        f'{i1}\tlocvar_itemname_s9 = ioriginalnamearticolodet(inv(INV_ITEM_ID, itemname_itemid))',
        f'{i1}}}',
        condizione_the,
        f'{i1}\tif ( locvar_itemname_s9 != "" ) {{',
        f'{i1}\t\tlocvar_itemowner_s = locvar_itemname_s9 + locvar_itemowner_s',
        f'{i1}\t}}',
        f'{i1}\telse {{',
        blocco[2],
        f'{i1}\t}}',
        blocco[3],
        blocco[4],
        blocco[5],
        f'{i1}\t\tif ( locvar_itemname_s8 != "" ) {{',
        f'{i1}\t\t\tlocvar_itemowner_s = locvar_itemname_s8 + locvar_itemowner_s',
        f'{i1}\t\t}}',
        f'{i1}\t\telse {{',
    ] + ripiego_inglese + [
        f'{i1}\t\t}}',
        blocco[17],
        blocco[18],
        blocco[19],
    ],
    "motivo": "l'articolo inglese si sceglie sulla prima lettera della stringa (a/an); in italiano dipende dal GENERE della testa del nome, che nella stringa composta sta in mezzo. Il genere e' un dato del dizionario, la stringa dell'articolo la deriva strumenti/articolo.py e arriva in ioriginalnamearticolo/ioriginalnamearticolodet. Le parole-contatore cablate vincono sull'array perche' quando ci sono la testa del sintagma e' la parola-contatore («un paio di stivali pesanti»). Se l'articolo italiano manca resta quello inglese, come il plurale ripiega sul singolare",
})

# --- il controllo che conta: ogni blocco compare esattamente una volta -------
sorgenti = {"init.hsp": INIT, "item_func.hsp": ITEM, "item_data.hsp": DATA}
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
