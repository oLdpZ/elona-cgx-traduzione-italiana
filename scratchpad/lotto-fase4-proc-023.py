# -*- coding: utf-8 -*-
"""Lotto fase4-proc-023: il poker, il jolly variabile, i soldi per farsi
risparmiare, il finto dogeza e il menu della necromanzia (proc.hsp 20000-20999).

20 rese, nessuna rinviata. E' il primo dei tre lotti che chiudono `proc.hsp`.

⚠️ **Lo stesso giapponese con DUE inglesi diversi, e la rete 4 lo impone.**
「パワーゲージが足りない。」 sta a `:20054` e a `:20150`, e l'inglese di monte lo
scrive in due modi — «Insufficient power gauge.» e «Your power gauge is
insufficient.» — per **due soglie diverse** (5 e 50 punti di barra). Il
giapponese e' identico, quindi la resa e' una sola: «La barra non basta.»
💡 E' il rovescio della rete 13: li' un inglese sta per due giapponesi, qui due
inglesi stanno per **un** giapponese. La differenza non la impone il sorgente,
la impone lo stile di chi ha tradotto in inglese.

⚠️ **`:20200` ha lo stesso inglese di `action.hsp:11649` e un giapponese
diverso**, e l'ha pescato `dossier.py`. «You look around and find nothing.» sta
per 「視界内に**素材**が存在しない。」 di la' — reso «Non c'è materiale in
vista.» — e per 「視界内に**ターゲット**は存在しない。」 di qua. Due frasi
identiche a meno di una parola, e l'inglese ha buttato via proprio quella.
Copiare
sull'inglese avrebbe detto «materiale» a chi cercava un nemico. **Si copia sul
giapponese, mai sull'inglese**, per la seconda volta dopo `:19303` della 38ª.

⭐ **I quattro versi della necromanzia non stanno in `skill.hsp`: esistono solo
qui.** 「魔力増強」, 「生命の転換」, 「外道式炸裂弾」, 「コールアンデッド」 sono
le intestazioni che il gioco stampa quando scegli una voce del menu
`SKILL_SPACT_NECRO_FORCE`, e il cerca-nel-dizionario non trova niente perche'
nessun altro file le nomina. ✅ L'ancora sono le **etichette del menu**, che
`text.hsp:2089`-`:2101` ha gia' rese: «Potenzia / Cura / Fai esplodere / Raduna
i non-morti». I quattro versi le seguono passo per passo.
💡 「コールアンデッド」 e' katakana che traslittera l'inglese, ma **non e' un nome
opaco**: dice «call undead», e le altre tre della stessa serie sono kanji che si
rendono. Lasciarne una in inglese sarebbe sembrato una dimenticanza, non una
scelta. E' la regola di `invariati.md` letta per quel che dice: **invariato e' il
nome che nemmeno l'originale legge come descrizione**, non il katakana in se'.

⚠️ **`:20841` avrebbe fatto concordare un aggettivo col bersaglio.** «X e'
furibondo» sbaglia sulle femmine, e «coglierlo di sorpresa» sbaglia il clitico.
✅ «X è in preda alla furia: non c'è spiraglio per un attacco a sorpresa...» —
locuzione invariabile, come «è in preda al terrore» del lotto 022. E la strada
del genitivo era chiusa in partenza: «La furia di » + `name()` fa scattare la
rete 8.

💡 **Tre rese su venti sono copie**, e due vengono dal **menu** dell'azione:
`:20844` ricalca `text.hsp:2073` («Fingo di implorare, poi attacco!») e prende
«coglie di sorpresa» da `proc.hsp:2023`; `:20851` e' `action.hsp:263` parola per
parola.

⚠️ **カード non e' 紙**, e in italiano si direbbero tutt'e due «carta».
`:20327`/`:20330` sono le carte da gioco del Poker Force, `:23300`/`:23303` del
lotto 022 erano la carta dello ShikiOrigami. ✅ Il plurale tiene la distinzione:
«**Le carte colpiscono** X» contro «La carta colpisce X». E' la famiglia 命中
per la quarta volta — soffio, sabbia, carta, e adesso le carte da gioco.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il Poker Force e il jolly variabile.
    # stesso giapponese di :20150, due inglesi di monte diversi: una resa sola
    (20054, 'Insufficient power gauge.'):
        'La barra non basta.',
    (20150, 'Your power gauge is insufficient.'):
        'La barra non basta.',
    # ジョーカー e' «jolly» da text.hsp:2271 e db_creature.hsp:56677
    (20168, 'Only one can be the Joker.'):
        'Solo uno può fare da jolly.',
    (20184, ' transformed into the {Variable Joker}. You can change the suit and rank of the joker at will in the interaction menu. When you use this effect, no turn passes.'):
        'cdatan(CDATAN_NAME, tc) + " si trasforma in {Jolly Variabile}. Dal menu d\'interazione puoi cambiarne seme e valore a piacere. Usare questo effetto non consuma il turno."',
    # diventa il nome della creatura: le parentesi sono quelle dell'inglese,
    # che e' il ramo che sostituiamo
    (20185, '{Variable Joker}'):
        '{Jolly Variabile}',
    # ⚠️ stesso inglese di action.hsp:11649, giapponese diverso: li' 素材,
    #    qui ターゲット. Reso sul giapponese
    (20200, 'You look around and find nothing.'):
        'Non c\'è nessun bersaglio in vista.',
    # 役 e' la combinazione del poker: sotto ci sono pair, straight, flash, high
    (20225, 'Your hand ranking is not established.'):
        'Non hai formato nessuna combinazione.',
    # la famiglia 命中. ⚠️ plurale, per non confonderle con la carta dello
    # ShikiOrigami (:23300, lotto 022)
    (20327, 'Cards hits  and'):
        '"Le carte colpiscono " + name(tc) + " e"',
    (20330, 'Cards hits .'):
        '"Le carte colpiscono " + name(tc) + "."',

    # --- i soldi per farsi risparmiare.
    (20580, ' stopped attacking...'):
        'name(tc) + " smette di attaccare..."',
    (20586, "It's simply not possible with this amount of money."):
        'Con i soldi che hai in tasca non se ne parla nemmeno.',
    (20658, ' stopped attacking...'):
        'name(cnt) + " smette di attaccare..."',

    # --- il finto dogeza.
    # ⚠️ «furibondo» concorderebbe con tc e «coglierlo» sbaglierebbe il
    #    clitico: la locuzione invariabile tiene tutt'e due i generi
    (20841, ' is furious and there is no opportunity for surprise attack...'):
        'name(tc) + " è in preda alla furia: non c\'è spiraglio per un attacco a sorpresa..."',
    # copiata dal menu (text.hsp:2073) e dall'idioma di proc.hsp:2023
    (20844, ' strikes  with an uppercut from prostrate position!'):
        'name(cc) + " finge di implorare, poi coglie di sorpresa " + name(tc) + "."',
    # copiata da action.hsp:263, stesso giapponese
    (20851, '  engulfed in fury!'):
        'name(tc) + " freme di rabbia!"',

    # --- il menu della necromanzia e i suoi quattro versi.
    # voce di menu aggiunta dal mod: passa da *prompt_key, quindi la misura
    (20871, 'Undead Summon'):
        'Evoca non-morti',
    # i quattro versi seguono le etichette di text.hsp:2089-2101
    (20892, ' *MP Charge* '):
        ' *Potenziamento magico* ',
    (20896, ' *HP Convert* '):
        ' *Conversione vitale* ',
    (20900, ' *Brutal Burst* '):
        ' *Ordigno spietato* ',
    (20904, ' *Convocation* '):
        ' *Richiamo dei non-morti* ',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-023.jsonl'
DA, A = 20000, 20999
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
