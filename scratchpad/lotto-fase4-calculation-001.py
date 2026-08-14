# -*- coding: utf-8 -*-
"""Lotto fase4-calculation-001: il vortice di mana, la sete e la fame, i
recuperi di stato (calculation.hsp, tutto il file).

44 rese, e **`calculation.hsp` si chiude in un lotto solo**: e' il quattordicesimo
file al 100% e il **quindicesimo dei 54 con `lang()` ad avere un dizionario**.
Il file non era in nessun elenco nominato — `SPEC.md` §6 lo copre con la
designazione collettiva «i restanti 63 file `.hsp` minori» — ed e' entrato per la
stessa ragione di `chara_func.hsp`: `stands up` e `released from bind` erano nel
**collaudo della 39ª**, fra le righe inglesi rimaste nel log.
✅ Con questo, **le tre fonti inglesi dello screenshot sono tutte chiuse**:
`proc.hsp` (39ª), `chara_func.hsp` e `calculation.hsp` (40ª).

⭐ **Sette rese su quarantaquattro erano gia' scritte, e `dossier.py` le ha
pescate tutte e sette per GIAPPONESE.** «si libera dalla costrizione»
(`action.hsp:9515`), «torna in se'» (`chara_func.hsp:3884`), «se la fa addosso»
(`chara_func.hsp:3377` e `:8317`) e i **quattro versi dello stimolo** —
「そわそわ」, 「身をよじって」, 「必死におしっこを我慢」, 「微かに震えながら」 —
che stanno a `proc.hsp:6926`-`:6935` parola per parola. 💡 E' il rovescio esatto
del lotto 005 di ieri: li' otto rese gia' decise erano **invisibili** al dossier
perche' il termine stava dentro una frase piu' lunga; qui sette frasi **intere**
coincidono e lo strumento le trova tutte. Lo stesso strumento, i due estremi, in
due giorni.

⚠️⚠️ **`:1556` e' la seconda «`:26940`» del progetto: il TIPO della voce decide
la resa, non il senso.** `lang(name(cc) + "は奇妙な力に捻じ曲げられた！", "A
dimensional door opens in front of you.")` — il ramo **giapponese nomina** il
personaggio, quello inglese no, e `estrai.py` classifica sul ramo che la resa
sostituisce. Quindi la voce e' **statica**, la resa e' testo nudo, e **non puo'
portare il nome** per quanto il giapponese ce l'abbia. ✅ Resa impersonale sul
fatto, che il codice conferma: due righe sotto c'e' `efid = SKILL_SPELL_TELEPORT`,
quindi la forza strana e' un teletrasporto — «Una forza strana distorce lo
spazio!» ⚠️ **E l'inglese di monte qui non e' un errore, e' una riscrittura
completa**: parla di una porta dimensionale che si apre davanti a te, cioe' di
un'altra immagine. Reso sul giapponese, come sempre.

⚠️ **`:1821` e `:1854` sono un inglese solo per due giapponesi, e la rete 13 li
prende.** «`X is weakened.`» sta per 「瘴気の**毒で**弱くなった」 — il **veleno**
del miasma — e per 「瘴気に**蝕まれて**弱くなった」 — il miasma che **corrode**.
Il codice li separa col colore: `COLOR_LIGHT_GREEN` il primo, `COLOR_BLUE` il
secondo. ✅ «Il veleno del miasma indebolisce X» e «Il miasma consuma X e **ne**
fiacca le forze». 💡 E il secondo ha chiesto il **`-ne` enclitico** della 37ª,
perche' «lo indebolisce» e «indebolirlo» portano tutt'e due un clitico che
concorda.

⚠️ **I quattordici gradini della sete e della fame sono a coppie e a terne, e
vanno letti come una scala.** `:1689`/`:1732` (il pericolo), `:1693`/`:1736`
(il capogiro), `:1697`/`:1740` (il fastidio): tre soglie per due bisogni, con due
o **tre** varianti pescate a caso. ✅ Rese in seconda persona come tutto il resto
del giocatore, e la scala si sente: «Hai la gola arsa» → «La sete ti fa girare la
testa…» → «Di questo passo la disidratazione ti stenderà!»
💡 E l'ultima variante di ognuna delle due terne e' una **domanda al giocatore**
— 「さて何を飲もうか。」 — che l'italiano rende meglio con l'impersonale: «E
adesso, che si beve?»

⚠️ **`:1511` e `:1972` sono due genitivi, e la strada e' quella dei ventidue di
resistenza del lotto 002.** «il mana **di** X», «la difesa **di** X» non si
possono scrivere. ✅ Il dativo riflessivo per il primo — «X **si vede
risucchiare** il mana!» — e il verbo per il secondo, «X allenta la guardia».

💡 **Nota su quel che NON e' entrato**: `calculation.hsp:2352` porta
「Forgive me! Forgive me!」, 「P-P-Pika!」, 「You snail!」 dentro un
`if ( jp ) … else`, **fuori da `lang()`**. Sono la scoperta di `else_jp.py` della
34ª — uscite in inglese a schermo durante quel collaudo — e **non hanno firma**:
non entrano in questo lotto e il file resta «100%» lo stesso. Vanno per toppa,
come le 23 righe di `proc.hsp`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il vortice di mana, che interrompe la lettura.
    # ⚠️ le virgolette dentro una statica vanno protette, come fa l'inglese
    (1505, '\\"Look out!\\" An ally notices a magical vortex and interrupts your reading.'):
        '\\"Attento!\\" Un compagno si accorge del vortice di mana e ti interrompe la lettura.',
    # ⚠️ genitivo: «il mana di X». Dativo riflessivo, come i ventidue del lotto 002
    (1511, ' mana is absorbed.'):
        'name(cc) + " si vede risucchiare il mana!"',
    (1524, '  even more confused now.'):
        'name(cc) + " si confonde ancora di più."',
    (1527, "It's too difficult!"):
        'Troppo difficile!',
    # ⚠️ il giapponese dice 「何かを」, «qualcosa»: l'inglese conta le creature
    (1536, 'Several creatures are summoned from a magical vortex.'):
        'Il vortice di mana evoca qualcosa!',
    # ⚠️ STATICA benche' il giapponese nomini cc: il tipo lo decide il ramo che
    #    la resa sostituisce, quindi niente nome. Il codice dice che e' un
    #    teletrasporto (efid = SKILL_SPELL_TELEPORT due righe sotto)
    (1556, 'A dimensional door opens in front of you.'):
        'Una forza strana distorce lo spazio!',

    # --- i tre gradini della sete, con le loro varianti.
    (1689, 'You are dehydrated!'):
        'Di questo passo la disidratazione ti stenderà!',
    (1689, 'You are almost a mummy.'):
        'Ancora un poco e diventi carne secca.',
    (1693, 'Your thirst makes you dizzy.'):
        'La sete ti fa girare la testa...',
    (1693, 'You have to drink something NOW.'):
        'Devi bere qualcosa, e subito...',
    (1697, 'You are getting thirsty.'):
        'Hai la gola arsa.',
    (1697, 'You feel thirsty.'):
        'Ti è venuta sete.',
    (1697, 'Now what shall I drink?'):
        'E adesso, che si beve?',

    # --- i tre gradini della fame, uguali e paralleli.
    (1732, 'You are starving!'):
        'Di questo passo muori di fame!',
    (1732, 'You are almost dead from hunger.'):
        'Hai una fame che ti uccide.',
    (1736, 'Your hunger makes you dizzy.'):
        'La fame ti fa girare la testa...',
    (1736, 'You have to eat something NOW.'):
        'Devi mangiare qualcosa, e subito...',
    (1740, 'You are getting hungry.'):
        'Ti sta venendo fame.',
    (1740, 'You feel hungry.'):
        'Hai fame.',
    (1740, 'Now what shall I eat?'):
        'E adesso, che si mangia?',

    # --- il sonno rotto dall'esplosione, e il miasma.
    (1764, '  hurt by the blast.'):
        '"L\'onda d\'urto travolge " + name(cnt) + "."',
    # ⚠️ rete 13: lo stesso inglese per il VELENO del miasma e per il miasma che
    #    CORRODE. Il codice li separa col colore (LIGHT_GREEN contro BLUE)
    (1821, '  weakened.'):
        '"Il veleno del miasma indebolisce " + name(r1) + "."',
    # ⚠️ «lo indebolisce» e «indebolirlo» portano un clitico che concorda:
    #    il -ne enclitico della 37ª
    (1854, '  weakened.'):
        '"Il miasma consuma " + name(r1) + " e ne fiacca le forze."',

    # --- il soffocamento.
    (1873, 'Ughh...!'):
        'Uuugh...!',
    (1879, ' stopped choking.'):
        'name(r1) + " riprende fiato. \\"Cof, cof!\\""',

    # --- i recuperi di stato. Tre erano gia' decisi altrove.
    (1895, ' break away from gravity.'):
        'name(r1) + " si libera dalla gravità."',
    (1906, ' calm down.'):
        'name(r1) + " si calma un poco."',
    (1917, ' stand up.'):
        'name(r1) + " si rimette in piedi."',
    # copiata da action.hsp:9515, stesso giapponese
    (1929, ' released from bind.'):
        'name(r1) + " si libera dalla costrizione."',
    # copiata da chara_func.hsp:3884, stesso giapponese
    (1948, ' recovered from brainwash.'):
        'name(r1) + " torna in sé."',
    (1964, ' recovered from atrophy.'):
        'name(r1) + " ritrova la voglia di combattere."',
    # ⚠️ genitivo: «la difesa di X»
    (1972, "'s protection vanishes."):
        'name(r1) + " allenta la guardia."',
    (2077, 'Your body is gradually falling apart...'):
        'Il corpo ti si sfalda a poco a poco...',
    (2095, ' recovered from incapacity.'):
        'name(r1) + " torna a muoversi."',
    (2107, ' became incapacitated.'):
        'name(r1) + " non riesce più a muoversi."',
    # stessa forma di chara_func.hsp:6182, che ha un giapponese gemello
    (2257, ' returned to their original form.'):
        'name(r1) + " ha ripreso l\'aspetto di prima."',

    # --- i quattro versi dello stimolo, tutti gia' resi a proc.hsp:6926-6935
    (2390, ' is extremely restless and fidgety...'):
        'name(r1) + " si agita senza sosta..."',
    (2393, ' is squirming and writhing in discomfort...'):
        'name(r1) + " si contorce dal disagio..."',
    (2396, ' is desperately holding back urine, trying not to go...'):
        'name(r1) + " si trattiene a fatica dal fare pipì..."',
    (2399, ' is trembling slightly, barely managing to endure the urge to urinate...'):
        'name(r1) + " trema appena e resiste allo stimolo..."',
    # copiata da chara_func.hsp:3377 e :8317, stesso giapponese
    (2408, ' wet .'):
        'name(r1) + " se la fa addosso."',

    # --- il sonno e il bonus della festa.
    (2473, 'You need to sleep.'):
        'Hai bisogno di dormire.',
    # ⚠️ «e' soddisfatto» concorderebbe col personaggio
    (2654, '  satisfied.'):
        'cdatan(CDATAN_NAME, cnt) + " ha avuto quel che voleva."',
    (2659, '(Total Bonus:%)'):
        '"(Bonus totale: " + ptp + "%)"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-calculation-001.jsonl'
DA, A = 0, 9999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\calculation.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_calculation.jsonl', encoding='utf-8') if l.strip()]
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
