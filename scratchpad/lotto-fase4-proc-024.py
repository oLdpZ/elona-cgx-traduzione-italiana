# -*- coding: utf-8 -*-
"""Lotto fase4-proc-024: l'automaledizione, lo Scambio da squalo, la posa, la
marcatura del territorio e le scosse elettriche (proc.hsp 24000-24999).

13 rese e **una rinviata a toppa**. `proc.hsp` passa a 1.027 su 1.098 (94%).

⚠️⚠️ **`:24107` e' la riga che il dizionario non puo' aggiustare, ed e' la
seconda della famiglia dopo `:11481` della 36ª.** L'azione e'
`SKILL_SPACT_JYUSOU_GOUSHIN`, e `skill.hsp:1411` la dichiara
**`TARGET_TYPE_SELF_ONLY`**: `proc.hsp:7565` fa `tc = cc`, quindi chi lancia e
chi subisce **sono lo stesso personaggio**. Il giapponese lo dice — 「自分自身に
強烈な呪いをかけた！」, «si e' scagliato addosso una maledizione tremenda» — e
`skill.hsp:1413` lo conferma nella descrizione dell'abilita', «Si maledice e si
rafforza». ⚠️ **L'inglese di monte invece nomina due personaggi**:
`name(cc) + " point" + _s(cc) + " " + name(tc) + " and mutter" + _s(cc) + " a
curse."`, che e' `proc.hsp:14703` **ricopiata parola per parola** — la riga
dell'incantesimo Maledizione, dove i due personaggi sono davvero due. A schermo
l'inglese stampa lo stesso nome due volte.
💡 **E qui la rete 11 non ha una via d'uscita**, per la prima volta nel senso
opposto a `:18280`: li' l'inglese aveva **un** `name()` e il giapponese due, e
bastava nominare il soggetto; qui l'inglese ne ha **due** e il giapponese uno,
e `verifica.py:367` pretende che le funzioni di contenuto coincidano con quelle
dell'inglese. Nessuna frase italiana nomina due volte lo stesso personaggio
senza sembrare rotta. ✅ **Rinviata e toppata**, come `:11481`: la toppa riporta
il ramo inglese alla forma del giapponese, un nome solo.

💡 **`:24139` invece e' la stessa azione e NON e' un errore**: l'inglese dice
`name(tc) + your(tc)` dove il giapponese dice `name(cc)の`, ma `tc == cc`,
quindi i due dicono la stessa cosa. ⚠️ Ha pero' un gemello di giapponese —
`proc.hsp:14766`, «valn, che X porta addosso, brilla di luce nera.» — con
l'inglese scritto su **`valn`** invece che su `itemname(ci)`: la rete 3 grida, e
ha ragione a gridare, ma le due rese **non possono** dire le stesse parole
nello stesso ordine, perche' la rete 11 impone l'ordine dell'inglese e li'
l'oggetto viene prima del nome, qui dopo. E' il litigio fra la 3 e la 11 della
37ª (`:12837`/`:13298`) su una coppia nuova.

⚠️ **«engulfed in fury» sta per due giapponesi diversi, ed e' la rete 13 a
cavallo di due lotti.** `:24801` ha lo stesso inglese di `action.hsp:263` e di
`proc.hsp:20851` — reso «freme di rabbia!» — ma il giapponese dice
「あまりの**屈辱**に体を奮わせた！」, cioe' **umiliazione**, non rabbia: e' la
riga che parte dopo che qualcuno ti ha marcato il territorio addosso, e il
codice conferma (`CDATA_CONDITION_WET` sale insieme a `ANGRY`). Resa «freme di
**umiliazione**!», sul giapponese.

💡 **`:24424` e' l'invariante di `invariati.md` in un posto assurdo.** Il ramo
inglese e' `"*" + skillname(efid) + "* "`, l'intestazione dell'azione speciale
gia' dichiarata per `:12101`; il ramo **giapponese** e' testo di **debug** che
upstream si e' scordato dentro — `"deru" + GDATA_FLAG_RARE_DROP + "、" + ...
+ "だ。運勢は" + LUC + "。"`. Non c'e' niente da rendere: la resa e' l'inglese
verbatim, spazio finale compreso.

⚠️ **Tre rese girate per non far concordare un aggettivo**: `:24107` («si
scaglia addosso», non «su se stesso»), `:24257` («con aria trionfante», non
«sicuro di se'») e `:24816`/`:24827`, dove «a » + `name()` e «di » + `name()`
avrebbero fatto scattare la rete 8 e si e' passati a «colpisce X al petto».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il profumo magico.
    (24029, 'A magical aroma envelops your surroundings.'):
        'Un profumo intriso di magia si spande tutt\'intorno.',

    # --- Jyusou Goushin, l'automaledizione (TARGET_TYPE_SELF_ONLY).
    # ⚠️ :24107 e' RINVIATA a toppa: vedi il docstring.
    # tc == cc, quindi il name(tc) dell'inglese e il name(cc)の del giapponese
    # dicono la stessa cosa. Il ciclo gira solo sull'equipaggiato
    (24139, '  glows black.'):
        'name(cc) + " porta addosso " + itemname(ci) + ", che brilla di luce nera."',

    # --- la posa e lo Scambio da squalo.
    # «sicuro di sé» concorderebbe con cc: la locuzione resta invariabile
    (24257, ' struck a pose with full of confidence!'):
        'name(cc) + " si mette in posa con aria trionfante!"',
    # シャークトレード e' «Scambio da squalo» in skill.hsp:1520
    (24281, ' set up the Shark Trade to !'):
        'name(cc) + " gioca lo Scambio da squalo contro " + name(tc) + "!"',
    (24283, '...but  could not have any more.'):
        '"...ma " + name(tc) + " non può portare altro."',

    # --- l'intestazione dell'azione speciale, gia' invariante a :12101.
    # ⚠️ il ramo giapponese qui e' testo di debug di monte: non si rende
    (24424, '** '):
        '"*" + skillname(efid) + "* "',

    # --- l'energia concentrata.
    (24453, ' release the converged energy towards !'):
        'name(cc) + " scaglia l\'energia che ha concentrato contro " + name(tc) + "!"',

    # --- la marcatura del territorio.
    (24783, ' began marking. *slop around* '):
        'name(cc) + " comincia a marcare il territorio. *scrosciooo* "',
    # ⚠️ stesso inglese di action.hsp:263 e proc.hsp:20851, ma il giapponese
    #    dice 屈辱, non 怒り: e' umiliazione, e il codice alza anche WET
    (24801, '  engulfed in fury!'):
        'name(tc) + " freme di umiliazione!"',

    # --- le scosse elettriche dell'ingegneria genetica.
    # «a » + name() e «di » + name() fondono: i due nomi restano complementi
    # diretti, e il petto diventa un locativo
    (24816, ' gave  strong electric shocks.'):
        'name(cc) + " colpisce " + name(tc) + " con una scossa elettrica tremenda! \\"Ahi!?\\""',
    (24827, ' gave  electric shocks.'):
        'name(cc) + " colpisce " + name(tc) + " al petto con una scossa elettrica. \\"Gh-agh!?\\""',

    # --- le capacita' limitate.
    (24877, ' status are temporarily limited.'):
        'name(tc) + " ha le capacità temporaneamente limitate."',
    (24902, ' status are not limited.'):
        'name(tc) + " non ha le capacità limitate."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(24107, ' point  and mutter a curse.')}

USCITA = 'lavoro/fase4-proc-024.jsonl'
DA, A = 24000, 24999
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
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
