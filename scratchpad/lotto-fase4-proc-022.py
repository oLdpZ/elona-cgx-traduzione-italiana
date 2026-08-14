# -*- coding: utf-8 -*-
"""Lotto fase4-proc-022: sorriso e polline, ShikiOrigami, tortura, i dadi del
destino e le sette invocazioni di Kamui (proc.hsp 23000-23999).

42 rese, nessuna rinviata. `proc.hsp` passa a 994 su 1.098 (91%), e con questo
la **zona densa 21000-23999 e' chiusa**: 156 voci in tre lotti.

⚠️ **`:23613` e' il ventottesimo errore di monte**: l'inglese dice
`name(cc) + " succumbed to torture."`, ma a cedere e' chi **subisce**. Il
giapponese dice `name(tc)`, e il codice conferma due volte — `chatc@DP = tc` la
riga dopo, e le sei suppliche di `:23616` le pronuncia `tc`. Reso sul
giapponese.
💡 `:23106` e' la stessa famiglia ma **innocua**: il giapponese nomina solo `tc`
e l'inglese aggiunge `cc`, che e' comunque chi agisce. Qui la rete 11 impone i
due nomi, e vanno bene tutt'e due.

⭐ **Le otto invocazioni di Kamui sono kanji con significato, non
traslitterazioni: si traducono.** L'inglese le scrive fra `<>` e una la
**romanizza e basta** — `<HOROBINOYARI>` per 「*滅火の神槍*」, che vuol dire
«lancia divina che spegne il fuoco». La regola del progetto e' quella di
`invariati.md`: **katakana che traslittera l'inglese resta**, kanji che dice una
cosa si rende. Qui sono tutte kanji, quindi si rendono tutte e otto — e il
giapponese le marca `*...*`, l'inglese `<>`; la resa tiene le parentesi
dell'inglese, che e' il ramo che sostituisce.

⚠️ **`:23236` invece resta com'e'**, e per la ragione opposta: 「*紙隠し*」 e'
gia' **`Kamikakushi`** in `invariati.md` — gioco di parole su 神隠し
(«rapimento divino») con 紙 («carta»), che l'italiano non trasporta. ⚠️ Ma la
stringa col contorno, `*Kamikakushi* `, e' **un'altra stringa** dal punto di
vista di `verifica`, come `Ensemble!` nel lotto 019: va dichiarata a parte.

💡 **Cinque rese sono copie**, e una e' la terza volta della stessa frase:
「戦慄した」 e' «e' in preda al terrore» in `action.hsp:296` e adesso in
`proc.hsp:22987` (lotto 021) e `:23025`. Piu' 「呼吸困難になった」
(`proc.hsp:7002`) e la famiglia 命中 per la carta.

⚠️ **`:23300`/`:23303` fanno gridare la rete 3 per la terza volta**, ed e'
sempre la stessa cosa: il giapponese 「に命中し」 non nomina il proiettile,
l'inglese si'. Soffio (`:9811`), sabbia (`:16831`), e adesso **carta**. La
differenza la impone il sorgente, non una scelta.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il sorriso che non arriva agli occhi.
    (23006, ' smiles, but  eyes are not laughing at all!'):
        'name(cc) + " sorride, ma gli occhi non ridono affatto!"',
    # copiata da action.hsp:296, stesso giapponese e stesso inglese
    (23025, '  overwhelmed.'):
        'name(tc) + " è in preda al terrore."',
    (23072, ' smiled.'):
        'name(cc) + " distribuisce sorrisi."',
    # il giapponese nomina solo tc, l'inglese aggiunge cc: la rete 11 impone
    # tutt'e due, e cc e' davvero chi agisce
    (23106, ' caught interest of .'):
        'name(cc) + " incuriosisce " + name(tc) + "."',

    # --- il cannone di polline e il vischio.
    (23116, ' gushed out intense pollen!'):
        'name(cc) + " sputa una nuvola di polline!"',
    (23165, ' threw the mistletoe.'):
        'name(cc) + " scaglia il vischio."',

    # --- ShikiOrigami (skill.hsp:1952 e seguenti).
    (23231, ' needs other ShikiOrigami to use the ability...'):
        'name(cc) + " ha bisogno di un altro ShikiOrigami..."',
    # ⚠️ resta com'e': `Kamikakushi` e' gia' invariato, ed e' un gioco di
    #    parole su 神隠し con 紙. Dichiarata a parte in invariati.md perche'
    #    la stringa col contorno e' un'altra stringa.
    (23236, '*Kamikakushi* '):
        '*Kamikakushi* ',
    (23243, ' call forth , making it unfold and scatter towards enemy.'):
        'name(cc) + " fa a pezzi " + name(tck) + " in un istante e li sparge tutt\'intorno."',
    # la famiglia 命中: il giapponese non nomina il proiettile, l'inglese si'
    (23300, 'The paper hits  and'):
        '"La carta colpisce " + name(tc) + " e"',
    (23303, 'The paper hits .'):
        '"La carta colpisce " + name(tc) + "."',
    (23319, ' has absorbed HP and MP of .'):
        'name(cc) + " assorbe " + name(tck) + " e si rigenera."',

    # --- le liane velenose e il veleno allergenico.
    (23338, 'Poisonous vines popped out from the ground!'):
        'Dal terreno spuntano liane avvelenate!',
    # «avvolto» concorderebbe con tc: le liane diventano soggetto
    (23383, '  bound.'):
        '"Le liane avvolgono " + name(tc) + "."',
    (23400, ' spreads allergenic poison.'):
        'name(cc) + " sparge un veleno allergenico."',
    # copiata da proc.hsp:7002, stesso giapponese su un'altra variabile
    (23459, ' suffers dyspnea.'):
        'name(tc) + " non riesce più a respirare."',
    (23478, ' shot solidified venom.'):
        'name(cc) + " scaglia veleno solidificato!"',

    # --- la tortura.
    (23572, ' tortured !'):
        'name(cc) + " tortura " + name(tc) + "!"',
    # ⚠️ reso sul giapponese: a cedere e' chi subisce, e il codice lo conferma
    #    due volte (chatc@DP = tc, e le suppliche di :23616 le dice tc)
    (23613, ' succumbed to torture.'):
        'name(tc) + " cede alla tortura."',
    (23616, "I'm sorry... really...!"):
        'Mi dispiace... davvero...',
    (23616, 'Forgive me, please.'):
        'Perdonatemi... vi prego...',
    (23616, 'I can not stand... such a thing.'):
        'Uuh... una cosa così non si può sopportare...',
    (23616, "I-I... can't!"):
        'N-non... ce la faccio...!',
    (23616, 'Kill me! Please kill me!'):
        'Fatemi fuori in un colpo solo...',
    (23616, 'A...aaaugh...'):
        'Ah, aaaah...',

    # --- i dadi del destino.
    (23629, ' threw two dice.'):
        'name(cc) + " lancia i dadi."',
    # lo spazio davanti e' dell'inglese: la riga continua quella sopra
    (23654, ' The total is...!'):
        '" Il tiro dà..." + sai1 + sai2 + "!"',
    (23709, 'The dice hits  and'):
        '"Il dado colpisce " + name(tc) + " e"',
    (23712, 'The dice hits .'):
        '"Il dado colpisce " + name(tc) + "."',

    # --- Kamui e le sette invocazioni. Kanji con significato: si rendono.
    (23746, ' unleashed the accumulated power of gods!'):
        'name(cc) + " libera il potere divino che ha assorbito!"',
    (23750, '<Respiration of Creative Gods>'):
        '<Soffio degli dèi creatori>',
    (23759, '<Roar of Fighting Gods>'):
        '<Ruggito degli dèi guerrieri>',
    (23767, '<Assault of Beast Gods>'):
        '<Artigli degli dèi bestiali>',
    (23771, '<Referee of Judicial Gods>'):
        '<Sentenza degli dèi arbitri>',
    (23775, '<Grudge of Abominable Gods>'):
        '<Rancore degli dèi maledetti>',
    (23779, '<Commandment of Hell Gods>'):
        '<Catene degli dèi infernali>',
    # 森羅万象 e' «tutto il creato», 殺 e' «uccidere»
    (23826, '<Elements Killing>'):
        '<Morte di ogni cosa creata>',
    # ⚠️ l'inglese romanizza e basta: 滅火の神槍 dice quel che fa
    (23846, '<HOROBINOYARI>'):
        '<Lancia divina che spegne il fuoco>',

    # --- la rabbia e le spore.
    (23867, ' exploded with anger!'):
        'name(cc) + " esplode di rabbia!"',
    (23900, ' calm down.'):
        'name(cc) + " si sente meglio."',
    (23907, ' spewed spores!'):
        'name(cc) + " sputa una nuvola di spore!"',
    (23992, 'A strong pheromone was scattered around.'):
        'Si è sparso in giro un feromone fortissimo.',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-022.jsonl'
DA, A = 23000, 23999
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
