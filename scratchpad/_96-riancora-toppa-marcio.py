# -*- coding: utf-8 -*-
"""96a - Ri-ancora la toppa del «(marcio)» a una riga che nessuno traducera'.

⚠️⚠️⚠️ IL GUASTO, E CHI L'HA FATTO. La toppa della 69a — quella che toglie i
prefissi 「腐った」/«rotten » e 「見本用の」/«sample » e li rimette **in coda fra
parentesi**, perche' in italiano un aggettivo prima del nome dovrebbe
concordare col genere di ogni cibo del gioco — si aggancia a questo blocco:

    if ( ibit(ITEM_BIT_ANTISEPTIC, itemname_itemid) == 1 ) {
        locvar_itemowner_s += lang("(防腐処理)", " (Antiseptic)")
    }

Il primo lotto della 96a ha tradotto quella `lang()` in « (antisettico)». Il
blocco cercato **non esiste piu'**, `applica` l'ha detto e ha tirato dritto, e
la build che ne e' uscita — piu' l'eseguibile copiato nel gioco alle 03:15 —
era **senza la toppa**: «rotten » e «sample » tornati prefissi inglesi davanti
al nome di ogni cibo, cioe' il difetto del 2026-08-19 riaperto in silenzio.

⭐⭐⭐ LA LEZIONE, ED E' DELLA CATENA, NON DI QUESTA RIGA. Le toppe si applicano
**dopo** la sostituzione del dizionario, quindi il loro `cerca` corre sul testo
gia' tradotto. Una toppa ancorata a una riga che contiene una `lang()`
traducibile e' **una bomba a orologeria**: si disinnesca da sola il giorno in
cui quella riga entra in un lotto, e chi traduce non ha nessun motivo di
sospettarlo. E' la stessa forma della trappola che `invariati.md` descrive per
` Lv` — un letterale confrontato contro un valore che qualcun altro traduce.

⚠️ E `applica` **non si ferma**: stampa la riga e continua. In un output di
decine di righe, chi guarda la coda non la vede. Vista qui solo perche'
`test_i_giudicati_esistono_ancora` di `maiuscole.py` e' scattato — quella rete
tiene coordinate nella build, e la build si era accorciata di 177 righe.
💡 Cioe': a trovare il guasto e' stata una guardia che guarda **un'altra cosa**.

## Il rimedio: ancora strutturale

Non si aggiorna il `cerca` alla resa italiana — sarebbe la stessa bomba con la
miccia piu' corta. Si sposta l'ancora sulla riga **dopo**, che non contiene
nessuna `lang()` e che nessun dizionario puo' raggiungere:

    if ( ibit(ITEM_BIT_PERIOD, itemname_itemid) == 1 ) {

Verificata unica nella build (`item_func.hsp:2219`). Il blocco nuovo si infila
**prima** di quella riga, cioe' esattamente dove stava prima: subito dopo il
tassello dell'antisettico, in coda agli altri stati fra parentesi.
"""
import io
import json

FILE = 'item_func.hsp'

VECCHIO_CERCA = [
    "\tif ( ibit(ITEM_BIT_ANTISEPTIC, itemname_itemid) == 1 ) {",
    "\t\tlocvar_itemowner_s += lang(\"(防腐処理)\", \" (Antiseptic)\")",
    "\t}",
]
NUOVO_CERCA = [
    "\tif ( ibit(ITEM_BIT_PERIOD, itemname_itemid) == 1 ) {",
]
NUOVO_SOSTITUISCI = [
    "\tif ( en ) {",
    "\t\tif ( inv(INV_ITEM_MATERIAL, itemname_itemid) == ITEM_MATERIAL_RAW ) {",
    "\t\t\tif ( inv(INV_ITEM_ROT, itemname_itemid) < 0 ) {",
    "\t\t\t\tlocvar_itemowner_s += \" (marcio)\"",
    "\t\t\t}",
    "\t\t}",
    "\t\tif ( ibit(ITEM_BIT_SHOP_SAMPLE, itemname_itemid) == TRUE ) {",
    "\t\t\tlocvar_itemowner_s += \" (campione)\"",
    "\t\t}",
    "\t}",
    "\tif ( ibit(ITEM_BIT_PERIOD, itemname_itemid) == 1 ) {",
]

NOTA = (
    " ⚠️⚠️ **Ri-ancorata nella 96a, e il motivo vale piu' della toppa.** Il "
    "`cerca` conteneva `lang(\"(防腐処理)\", \" (Antiseptic)\")`, cioe' una riga "
    "**traducibile**: il primo lotto della 96a l'ha resa « (antisettico)», il "
    "blocco non e' piu' esistito, `applica` l'ha detto in una riga e ha tirato "
    "dritto, e la build piu' l'eseguibile copiato nel gioco sono rimasti "
    "**senza questa toppa** — cioe' col difetto del 2026-08-19 riaperto. Le "
    "toppe corrono sul testo **gia' tradotto**, quindi ancorarle a una `lang()` "
    "e' una bomba a orologeria che scatta il giorno in cui quella riga entra in "
    "un lotto. L'ancora e' ora `if ( ibit(ITEM_BIT_PERIOD, itemname_itemid) == "
    "1 ) {`, che non porta nessuna `lang()` e che nessun dizionario raggiunge; "
    "il blocco si infila prima di lei, cioe' esattamente dove stava. 💡 A "
    "trovare il guasto e' stata `maiuscole.py`, che tiene coordinate nella "
    "build e si e' accorta che il file si era accorciato di 177 righe: una "
    "guardia che guardava un'altra cosa."
)

righe = [l for l in io.open('toppe.jsonl', encoding='utf-8').read().splitlines()
         if l.strip()]
toppe = [json.loads(l) for l in righe]

bersagli = [i for i, t in enumerate(toppe)
            if t.get('file') == FILE and t.get('cerca') == VECCHIO_CERCA]
if len(bersagli) != 1:
    raise SystemExit(f'attesa 1 toppa con quel cerca, trovate {len(bersagli)}')
i = bersagli[0]
t = toppe[i]
if t['sostituisci'][:3] != VECCHIO_CERCA:
    raise SystemExit('il sostituisci non ricomincia col blocco cercato: fermo tutto')

# l'ancora nuova esiste, ed e' unica, nella build gia' tradotta
build = io.open('C:/Games/Elona/_traduzione/build/2.05-custom-gx/item_func.hsp',
                encoding='cp932').read().split('\n')
quante = sum(1 for l in build if l.rstrip('\r') == NUOVO_CERCA[0])
if quante != 1:
    raise SystemExit(f'l\'ancora nuova compare {quante} volte, ne serve una sola')

t['cerca'] = NUOVO_CERCA
t['sostituisci'] = NUOVO_SOSTITUISCI
t['motivo'] = t['motivo'] + NOTA
righe[i] = json.dumps(t, ensure_ascii=False)

with io.open('toppe.jsonl', 'wb') as f:
    f.write(('\n'.join(righe) + '\n').encode('utf-8'))
print('toppa %d ri-ancorata: %r' % (i, NUOVO_CERCA[0].strip()))
