# -*- coding: utf-8 -*-
"""Lotto `command-018`: la scheda dei talenti, seconda meta' — il risveglio, le
tredici abilita' acquisite, i tratti da negoziante e i due caratteri.

Stesso registro nominale del `command-017`, e per lo stesso motivo: `:2561`-`:2564`
converte la schermata su un alleato con `cnv_str "You" -> him2(tc)`, e la resa
italiana quella conversione la spegne. Qui pero' il registro non e' una scelta
del traduttore in **due** righe: e' imposto dal sorgente.

⭐⭐ **`_seikaku` era gia' stato girato al nome astratto da chi ha chiuso
`text.hsp`, e questo decide `:2492` e `:2497`.** Il vettore dei caratteri
(`text.hsp:52`) e' reso «Allegria», «Prudenza», «Devozione», «Malignità»,
«Codardia» — **nomi, non aggettivi** — perche' un aggettivo avrebbe accordato
con la persona. Quindi «You are » + `_seikaku(...)` non puo' diventare «Sei
Allegria»: l'unica forma che regge e' l'etichetta, «Carattere: Allegria». ⚠️ E
non e' una scelta di questo lotto: e' la conseguenza di una scelta gia' fatta in
un altro file, che qui si riscuote. La lezione della 42ª — un termine deciso
altrove torna a chiedere il conto — vale anche per la **forma grammaticale**,
non solo per le parole.

⭐ **Sette nomi decisi in `glossario.md`, sette copiati.** Le abilita' del
risveglio hanno il loro nome in `chat.hsp:17854`-`:17865`, il menu in cui si
spendono gli AP, e `chat.hsp` non ha ancora un dizionario: le sette che nascono
li' — «Accumulo di mana», le cinque «tattiche», «Tempesta variabile» — vanno in
glossario col numero di riga, come i ventisette materiali della 44ª. ✅ Le altre
sette invece stanno in `skill.hsp`, che e' chiuso al 100%, e si copiano parola
per parola: «Insulto», «Salto dimensionale», «Provocazione», «Soffio
variabile», «Tiro zero», «Carica», «Ammaliamento».
💡 **Quattro rese su cinque, in questo lotto, non si sono decise: si sono
ritrovate.** Vale anche per «malattia dell'etere» (`chara_func.hsp:2864`), «la
barra» (`proc.hsp:20054`), «Follia» (`command.hsp:10517`) e «Cos»
(`buff.hsp:752`).

⚠️ **Il giapponese vince cinque volte, e sempre perche' l'inglese butta via la
parentesi.** Le righe del risveglio hanno tutte la forma 「frase[effetto]」, e
l'inglese tiene solo la frase: `:2357` 「あなたの魅力は敵さえも朦朧とさせる[直接
攻撃してきた敵が朦朧]」 diventa «You dim enemies that directly attack you», che
perde il **fascino** — cioe' il motivo per cui i nemici restano storditi;
`:2362` e `:2367` perdono «[meno HP, piu' schivata e critici]» e «[piu' danni]»;
`:2372` perde «[consuma MP pari al danno]». ✅ La resa tiene la parentesi, che e'
anche il modo in cui la riga diventa **utile**: dice che cosa fa, non come suona.

⚠️ **E `:2347` e' un errore di monte minore ma vero**: 「生もの製のアイテムを食べ
る」 sono gli oggetti **fatti di roba fresca** — il cuoio crudo, la carne — e
l'inglese scrive «You eat raw items», che in un gioco dove si mangia di tutto non
distingue niente.

Tetto 56 caratteri (`:2467`, la riga inglese piu' lunga della schermata). Le
quattro righe da negoziante ci arrivano vicine e sono le uniche: 45, 38, 47, 42.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2336-:2352 i tratti del corpo. ⭐ «malattia dell'etere» e' la resa di
    #     chara_func.hsp:2864 e text.hsp:10113; «Cos» e' la sigla di buff.hsp:752.
    (2336, 'Your Ether Disease grows fast.'): "La malattia dell'etere avanza in fretta",
    (2341, 'Your Ether Disease grows slow.'): "La malattia dell'etere avanza lentamente",
    # ⚠️ 「生もの製のアイテム」 sono gli oggetti FATTI di roba fresca, non il cibo
    #    crudo: l'inglese «raw items» non distingue niente.
    (2347, 'You eat raw items.'): 'Dieta di materie prime fresche',
    (2352, 'You have given birth. [CON RES+]'): 'Esperienza di parto [Cos: danni dimezzati]',

    # --- :2357 il risveglio. ⚠️ il giapponese porta la parentesi con l'effetto e
    #     l'inglese la butta via: la resa la tiene, che e' quel che serve leggere.
    (2357, '[AWAKE]'): '[Risveglio]',
    (2357, 'You dim enemies that directly attack you.'):
        'Il fascino stordisce chi attacca in mischia',
    (2362, 'You become more evasive as you near death.'):
        "L'orgoglio cresce col pericolo [più schivata e critici]",
    (2367, 'Your damage increases as you near death.'):
        'La forza nascosta cresce col pericolo [più danni]',
    (2372, 'You use your MP as a barrier against damage.'):
        'La barriera annulla i danni [consuma MP pari al danno]',

    # --- :2377-:2437 le tredici abilita' acquisite.
    #     ⭐ sette copiate da skill.hsp, chiuso al 100%; sette decise in
    #     glossario.md perche' nascono in chat.hsp, che non ha dizionario.
    (2377, 'You got Insult.'): 'Insulto appreso',
    (2382, 'You got Crystal Spear.'): 'Accumulo di mana appreso',
    (2387, 'You got Dimensional Move.'): 'Salto dimensionale appreso',
    (2392, 'You got Tactical Heal.'): 'Cura tattica appresa',
    (2397, 'You got Tactical Attack.'): 'Attacco tattico appreso',
    (2402, 'You got Tactical Martial Arts.'): 'Arti marziali tattiche apprese',
    (2407, 'You got Tactical Curse.'): 'Maledizione tattica appresa',
    (2412, 'You got Charge Attack.'): 'Carica appresa',
    (2417, 'You got Provoke.'): 'Provocazione appresa',
    (2422, 'You got Zero shoot.'): 'Tiro zero appreso',
    (2427, 'You got Tactical Throw.'): 'Lancio tattico appreso',
    (2432, 'You got Variable Breath.'): 'Soffio variabile appreso',
    (2437, 'You got Variable Storm.'): 'Tempesta variabile appresa',

    # --- :2442-:2462 le preferenze di combattimento e i due sigilli.
    (2442, 'You prefer the proximity attack.'): 'Preferenza per la mischia',
    (2447, 'You prefer the shot.'): 'Preferenza per il tiro',
    (2452, 'You prefer the magic arrows.'): 'Preferenza per le magie a freccia',
    (2457, 'Your magic is sealed.'): 'Magia sigillata',
    # 「技能」 sono le tecniche, non le abilita' generiche.
    (2462, 'Your ability is sealed.'): 'Tecniche sigillate',

    # --- :2467-:2487 i cinque tratti da negoziante. ⚠️ tutti con la parentesi
    #     dell'effetto: qui ce l'hanno tutt'e due le lingue di monte.
    (2467, '[SHOP]'): '[Negozio]',
    (2467, 'You got elegance. [Increase Quality Of Customers In Shop]'):
        'Eleganza [clientela migliore]',
    (2472, 'You got aesthetic sense. [Increase Exchange Rate]'):
        "Occhio da intenditore [cambio più favorevole]",
    (2477, 'You got your own sales route. [Earn Gold Independently Each Day]'):
        'Rifornimenti propri [guadagno giornaliero]',
    (2482, 'You got strong alliances. [Increases Sell Value When In Party]'):
        'Forti alleanze [vendite migliori al seguito]',
    # ⭐ Bewitch e' «Ammaliamento», skill.hsp:1468.
    (2487, 'You got a business smile. [Learns Bewitch]'):
        'Sorriso professionale perfetto [impara Ammaliamento]',

    # --- :2492-:2507 i due caratteri e i due limiti della barra.
    #     ⚠️⚠️ dinamiche: `_seikaku` restituisce un NOME astratto («Allegria»,
    #     «Prudenza»), perche' text.hsp:52 lo ha gia' girato cosi'. «Sei
    #     Allegria» non si puo' scrivere: l'unica forma che regge e' l'etichetta.
    #     ⭐ «la barra» e' la resa di proc.hsp:20054 e skill.hsp:1529.
    (2492, '[CHARA]'): '[Carattere]',
    (2492, 'You are . [Power gauge +3 at the start of the map]'):
        '"Carattere: " + _seikaku(cdata(CDATA_ROLE_SHOP_LEVEL, tc)) + " [barra +3 a inizio mappa]"',
    (2497, 'You have a  aspect. [Power gauge +1 when damaged]'):
        '"Anche un lato di " + _seikaku(cdata(CDATA_ROLE_RESTOCK, tc)) + " [barra +1 se colpito]"',
    (2502, 'You are not trapped by your trouble. [Power gauge lower limit +1]'):
        'Nessun cruccio [barra: minimo +1]',
    # ⭐ «SAN» e' «Follia» nella scheda del personaggio, command.hsp:10517.
    (2507, 'You have developed a dangerous hobby. [SAN lower limit +10/Power gauge lower limit +5]'):
        'Passatempo pericoloso [Follia minima +10, barra minima +5]',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-018.jsonl'
DA, A = 2336, 2507
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

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
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
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
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
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
    resa = RESE[chiave(v)]
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
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
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
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
