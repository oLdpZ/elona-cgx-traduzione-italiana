# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-004: l'equipaggiamento che si rovina e i sei modi
buffi di morire (chara_func.hsp 4000-4999).

33 rese e **due rinviate**, su 35 voci. Due blocchi che non si somigliano:
`:4200`-`:4520` e' l'equipaggiamento aggredito dagli elementi (acido, fuoco,
gelo), `:4761`-`:4848` e' `txteledmg`, cioe' il verso che accompagna **ogni
danno elementale** del gioco.

⭐ **`txteledmg` ha tre gradini, e il secondo e' una CODA.** `txteledmg_arg1`
vale 0, 1 o 2: **ferito**, **ucciso da chi attacca**, **morto**. Il gradino 1 e'
scritto in giapponese **senza soggetto** — 「殺した。」, 「千切りにした。」,
「内部から崩壊させて殺した。」 — perche' si attacca in coda alla riga di sopra,
esattamente come le teste «… e» della 35ª ma dall'altro lato. ✅ La forma era
gia' decisa e sta nel dizionario: `chara_func.hsp:6843` rende 「殺した。」
«uccide sul colpo.», senza soggetto e senza pronome. Le altre code seguono:
«taglia a listarelle.», «fa crollare il corpo dall'interno.»
⚠️ **E una coda italiana non puo' portare il clitico**, che l'inglese invece si
concede (`him(txteledmg_arg3)`): «lo fa a listarelle» concorderebbe col
personaggio, «le» pure. Il possesso e l'oggetto restano impliciti, come fa il
giapponese.

⚠️ **Ma il gradino 1 non e' sempre una coda, e a deciderlo e' l'INGLESE.** A
`:4786` e `:4823` il giapponese e' senza soggetto («栗で抉り殺した。», 「人形に
変えて事実上殺した。」) ma l'inglese ha rimesso dentro un `name()`, e la rete 11
pretende che ci sia. Quindi la resa **nomina** — «Le castagne crivellano X a
morte», «trasforma X in una bambola» — e le due frasi convivono nello stesso
blocco con quelle che non nominano. Non e' un'incoerenza della traduzione: e'
l'inglese di monte che non e' coerente con se stesso, e la rete 11 la propaga.
💡 A `:4800` la strada e' il **`-ne` enclitico** della 37ª: l'inglese dice
`name(arg2) + " burst " + his(arg3) + " brain."` e in italiano «il cervello di
X» fonderebbe — «X **ne** fa scoppiare il cervello» tiene il nome di chi
attacca, l'invariabilita' e il possesso.

⚠️⚠️ **`:4520` e' la QUARTA riga del progetto che il dizionario non puo'
aggiustare, e la causa e' nuova: una `lang()` che `estrai.py` NON VEDE.**
`:4491` fa `locvar_item_cold_s = name(item_cold_arg1) + lang("の",
your(item_cold_arg1))`, e `:4520` usa quella variabile come **prefisso**. Il
ramo inglese di quella `lang()` e' **una sola chiamata di funzione, senza
letterale**, quindi non e' una firma: le firme di `chara_func.hsp` sono 342 e
`:4491` non e' fra loro. ⚠️ `your()` restituisce `"'s"` o `"r"`
(`init.hsp:2045`), fuori da `lang()`, e a schermo la riga italiana leggerebbe
«il putit**'s** …». ⚠️ E la resa non puo' rimediare **nemmeno nominando il
proprietario**, perche' il `name()` sta dentro la variabile e
`funzioni_di_contenuto` non lo vede: l'inglese dichiara `['itemname']` e una
resa che aggiungesse `name()` verrebbe bocciata dalla rete 11. E' la stessa
strettoia di `:3037` e di `proc.hsp:24107`, per una ragione terza.
✅ **Rinviata, e toppata in due punti**: `:4491` costruisce adesso un
**suffisso** («, che X porta addosso») invece di un prefisso possessivo, e
`:4520` lo mette in fondo. A schermo: «Il gelo manda in frantumi la spada, che
il putit porta addosso.», e «Il gelo manda in frantumi la spada.» quando
l'oggetto e' per terra e la variabile e' vuota. Il ramo giapponese di tutt'e due
le righe resta **identico**.
💡 **E' il rovescio del genitivo**: la strada di sempre — mai «di » davanti a
`name()` — qui non bastava a scriverla, perche' il pezzo da girare stava trenta
righe piu' su e in un'altra istruzione.

⚠️ **`:4369` e' commentata nel sorgente** (`; txt lang(...)`, dentro il blocco
del tag-team che il mod ha spento riga per riga col `;`). Rinviata come le
quattro di `db_creature.hsp` e `proc.hsp:4958`. 💡 La resa esisteva gia'
comunque — `proc.hsp:6481` e `text.hsp:13` dicono «X protegge Y.» — quindi non
si perde niente.

💡 **E l'equipaggiamento vuole il soggetto ELEMENTO, non il partitivo.**
`:4274`-`:4520` dicono tutte 「name の itemname は…」, e `itemname()` puo' essere
**plurale** («tre frecce»): una resa come «X si vede ridurre in cenere Y»
dovrebbe accordare il verbo col numero, che non si conosce. ✅ Il fuoco, il gelo
e l'acido diventano **soggetti** — «Il fuoco riduce in cenere Y», «Il gelo manda
in frantumi Y» — cosi' il verbo resta singolare e l'oggetto puo' essere quello
che vuole. E il possesso si attacca in coda con «che X porta addosso», che e'
la forma di `proc.hsp` gia' vista a schermo nel collaudo della 39ª.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- l'acido sull'equipaggiamento. ⚠️ genitivo: 「name の itemname は…」.
    #     Il dativo riflessivo, come a :6399 e :6411.
    (4200, '  is damaged by acid.'):
        'name(item_acid_arg1) + " si vede rovinare " + itemname(locvar_item_acid_ci, , 1) + " dall\'acido."',
    (4213, '  is melted by acid.'):
        'name(item_acid_arg1) + " si vede sciogliere " + itemname(locvar_item_acid_ci, , 1) + " dall\'acido."',
    # qui il possesso si attacca in coda: la forma di proc.hsp, vista a schermo
    (4223, '  is immune to acid.'):
        'name(item_acid_arg1) + " porta addosso " + itemname(locvar_item_acid_ci, , 1) + ", che l\'acido non intacca."',

    # --- il fuoco. ⚠️ itemname() puo' essere PLURALE: l'elemento diventa
    #     soggetto cosi' il verbo resta singolare qualunque cosa arrivi.
    (4274, ' on the ground get perfectly broiled.'):
        '"Il fuoco arrostisce a puntino " + itemname(locvar_item_acid_ci, inv(INV_ITEM_NUM, locvar_item_acid_ci)) + " per terra."',
    (4280, '  get perfectly broiled.'):
        '"Il fuoco arrostisce a puntino " + itemname(locvar_item_acid_ci, inv(INV_ITEM_NUM, locvar_item_acid_ci), 1) + " che " + name(item_fire_arg1) + " porta addosso."',
    (4316, ' protects  stuff from fire.'):
        'itemname(locvar_item_fire_ti, 1) + " protegge dal fuoco quello che " + name(item_fire_arg1) + " porta addosso."',
    (4324, ' turns to dust.'):
        'itemname(locvar_item_fire_ti, 1) + " si riduce in cenere."',
    (4337, ' exploded.'):
        '"Il fuoco fa esplodere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + "."',
    # ⚠️ :4369 e' RINVIATA: riga commentata nel sorgente. La resa esisteva gia'
    #    comunque (proc.hsp:6481, text.hsp:13). Vedi il docstring.
    (4387, '  equip turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + " che " + name(item_fire_arg1) + " indossa."',
    (4397, '  turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p, 1) + " che " + name(item_fire_arg1) + " porta addosso."',
    (4404, ' on the ground turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + " per terra."',

    # --- il gelo.
    (4506, ' protects  stuff from cold.'):
        'itemname(locvar_item_fire_ti, 1) + " protegge dal gelo quello che " + name(item_cold_arg1) + " porta addosso."',
    (4511, ' is broken to pieces.'):
        '"Il gelo manda in frantumi " + itemname(locvar_item_fire_ti, 1) + "."',
    # ⚠️ :4520 e' RINVIATA a toppa: il prefisso possessivo lo costruisce :4491,
    #    dentro una lang() che estrai.py non vede. Vedi il docstring.

    # --- txteledmg: i tre gradini di ogni danno elementale.
    #     0 = ferito, 1 = ucciso da chi attacca (CODA), 2 = morto.
    (4761, ' melt.'):
        '"L\'acido scioglie " + name(txteledmg_arg3) + "."',
    (4768, ' get a cut.'):
        'name(txteledmg_arg3) + " riporta un taglio."',
    # coda senza soggetto, come «uccide sul colpo.» di :6843.
    # ⚠️ niente clitico: «lo fa a listarelle» concorderebbe col personaggio
    (4772, 'cut  into thin strips.'):
        '"taglia a listarelle."',
    (4775, '  cut into thin strips.'):
        'name(txteledmg_arg3) + " finisce a listarelle."',
    (4782, ' was beaten with chestnuts.'):
        '"Le castagne colpiscono " + name(txteledmg_arg3) + "."',
    # ⚠️ il giapponese e' una coda, ma l'inglese ci ha rimesso un name():
    #    la rete 11 pretende che ci sia
    (4786, '  gouged to death with chestnuts.'):
        '"Le castagne crivellano " + name(txteledmg_arg3) + " a morte."',
    (4789, '  gouged by chestnuts and died.'):
        'name(txteledmg_arg3) + " non regge ai colpi delle castagne e muore."',
    (4796, ' received a shock to the brain.'):
        'name(txteledmg_arg3) + " prende una scossa al cervello."',
    # ⚠️ «il cervello di X» fonderebbe: il -ne enclitico della 37ª. E il name()
    #    che l'inglese dichiara e' quello di CHI ATTACCA (arg2)
    (4800, ' burst  brain.'):
        'name(txteledmg_arg2) + " ne fa scoppiare il cervello."',
    (4803, ' die from brain rupture.'):
        'name(txteledmg_arg3) + " muore con il cervello in pezzi."',
    # ⚠️ genitivo: «la testa di X»
    (4810, ' head was hit with tofu.'):
        '"Un angolo di tofu centra " + name(txteledmg_arg3) + " in testa."',
    (4814, ' crush  head with tofu.'):
        'name(txteledmg_arg2) + " colpisce " + name(txteledmg_arg3) + " alla testa con un angolo di tofu."',
    (4817, ' die from being hit in the head with tofu.'):
        'name(txteledmg_arg3) + " muore per un angolo di tofu in testa."',
    (4823, 'change  into a doll.'):
        '"trasforma " + name(txteledmg_arg3) + " in una bambola."',
    (4826, ' change into a doll.'):
        'name(txteledmg_arg3) + " perde ogni libertà e diventa una bambola."',
    # coda: il possesso resta implicito, come fa il giapponese
    (4832, 'burst the body of .'):
        '"fa crollare il corpo dall\'interno."',
    (4835, ' burst and die.'):
        'name(txteledmg_arg3) + " non regge e il corpo crolla."',
    (4841, '  wounded.'):
        '"Il colpo ferisce " + name(txteledmg_arg3) + "."',
    # copiata da chara_func.hsp:6843, stesso giapponese 「殺した。」
    (4845, 'kill .'):
        '"uccide sul colpo."',
    (4848, '  killed.'):
        'name(txteledmg_arg3) + " muore."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(4369, ' guarded .'), (4520, ' break to pieces.')}

USCITA = 'lavoro/fase4-chara_func-004.jsonl'
DA, A = 4000, 4999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\chara_func.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_chara_func.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
voci = [v for v in zona if (v['riga'], v['en']) not in RINVIATE]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[(v['riga'], v['en'])])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
