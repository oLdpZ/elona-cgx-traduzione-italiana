# -*- coding: utf-8 -*-
"""Lotto fase4-proc-025: le onde, il filo e l'ago, l'esplosivo, la gravita',
l'etere e l'Onda Sororale (proc.hsp 25000-25999).

30 rese, nessuna rinviata. `proc.hsp` passa a 1.057 su 1.098 (96%).

⭐ **Nasce qui un termine che servira' a un altro file: 姉波動 e' l'«Onda
Sororale».** Le quattro righe `:25798`, `:25802`, `:25818`, `:25823` sono le
**prime** del progetto a nominarlo, ma il grosso della materia sta in
`chat.hsp:6575`-`:6676` — una catechesi intera sul culto delle sorelle
maggiori — e `chat.hsp` e' uno dei 40 file senza dizionario. ⚠️ **E l'inglese
di monte non aiuta, perche' lo chiama in tre modi**: «Big Sister Energy» qui,
«sisterly energy» a `chat.hsp:6575`, «Sistergy Wave» a `:6604`. Il giapponese
invece dice sempre 姉波動. 💡 «Onda Sororale» tiene il 波動 («onda», e il
registro pseudoscientifico che la battuta vuole) e usa un aggettivo italiano
vero; va messo in `glossario.md` **adesso**, perche' e' esattamente la
situazione del `Bolt` della 35ª: una scelta presa una volta e poi da applicare
in un altro file mesi dopo.

⚠️⚠️ **`:25178` e' il ventinovesimo errore di monte, e di una forma nuova:
l'inglese nomina DUE VOLTE lo stesso personaggio.**
`name(tc) + " slashed " + name(tc) + " with holy power."` — il primo dei due
e' `cc`, lo dice il giapponese (「name(cc)は name(tc)を…斬りつけた」) e lo
conferma il codice, che fa partire l'animazione **su** `tc` due righe sotto.
💡 E' il gemello di `:24107` del lotto 024, dove l'inglese aveva **aggiunto**
un personaggio che non c'era: li' i due `name()` erano lo stesso e non si
poteva rendere, qui sono due davvero e basta raddrizzare il primo.

⚠️ **Due errori di monte nella stessa azione, uno dietro l'altro**: `:25071` e
`:25119` dicono tutt'e due `name(tc)` dove ad agire e' `cc` — e' il purificatore
che emette l'onda, non chi la riceve. Il giapponese dice `name(cc)` in
tutt'e due. Con `:25178` la serie degli errori di monte passa da ventotto a
**trentadue**.

⚠️ **Un inglese solo per due giapponesi, e stavolta i due sono i due rami dello
stesso `if`.** `:25206` e `:25216` hanno tutt'e due
«`name(cc) + " sewed " + name(tc) + " up quickly!"`», ma il giapponese
distingue: 「縫い**つけた**」 sul nemico — e il codice mette
`CONDITION_BIND` — e 「**縫合**した」 sull'alleato, dove il codice **dimezza**
`CONDITION_BLEED`. Sono due cose opposte: inchiodare e ricucire. La rete 13 le
ha viste, il codice ha deciso.

💡 **La strada del participio regge per il quarto lotto di fila**, e stavolta le
sostanze che diventano soggetto sono due: «**I fili** lacerano X» (`:25335`,
dove l'inglese ha `was(tc) + " slashed"`) e «**La sfera di gravità** schiaccia
X» (`:25577`, `was(tc) + " pressed"`). ⚠️ `:25335` e' anche un caso `:18280`:
il giapponese nomina `cc` e `tc`, l'inglese solo `tc`, e la rete 11 concede un
nome solo.

⚠️ **Sei rese girate per non far fondere una preposizione con `name()`**:
«il corpo **di** X» (`:25368`), «il livello **di** X» (`:25818`), «la sorella
maggiore **di** X» (`:25802`), «lo sguardo **di** X» (`:25798`), «lava il
cervello **a** X» (`:25918`, risolto con «soggioga», che e' anche il verbo di
`skill.hsp:1200`) e «si lascia cadere **su** X» (`:25231`). La rete 8 non ha
gridato nemmeno una volta perche' le sei erano gia' girate in partenza: dopo
quattro lotti il genitivo davanti a `name()` non si scrive piu'.

💡 **Tre copie**: `:25246` da `proc.hsp:9600`/`:17261` («cade a terra»),
`:25837` da `:9867` («spalanca le pupille»), e «malattia dell'etere» /
«etere» dal glossario di `text.hsp`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- le onde: quella calmante e quella di purificazione.
    # ⚠️ l'inglese dice name(tc) dove agisce cc. Reso sul giapponese
    (25071, ' emitted calming spiritual wave...'):
        'name(cc) + " emana un\'onda psichica quieta..."',
    (25113, 'Nothing happens....It seems like your karma is too low.'):
        'Non succede nulla... Il tuo karma è troppo basso.',
    # ⚠️ stesso errore della riga sopra, nella stessa azione
    (25119, ' emitted a wave of purification.'):
        'name(cc) + " sprigiona tutt\'intorno un\'onda di purificazione."',
    # ⚠️ l'inglese scrive name(tc) DUE volte: il primo e' cc, lo dice il
    #    giapponese e lo dice il codice (l'animazione parte su tc)
    (25178, ' slashed  with holy power.'):
        'name(cc) + " colpisce " + name(tc) + " con un fendente carico di potere sacro."',

    # --- il filo e l'ago: due giapponesi sotto un inglese solo.
    # 縫いつけた, il nemico inchiodato (CONDITION_BIND)
    (25206, ' sewed  up quickly!'):
        'name(cc) + " cuce " + name(tc) + " sul posto in un lampo!"',
    # 縫合した, l'alleato ricucito (CONDITION_BLEED dimezzato)
    (25216, ' sewed  up quickly!'):
        'name(cc) + " ricuce " + name(tc) + " in un lampo!"',

    # --- il sedere.
    # «disteso»/«finito» concorderebbero con tc: «ormai a terra» no
    (25231, ' crushes  with hip!'):
        'name(cc) + " schiaccia col sedere " + name(tc) + ", ormai a terra!"',
    (25241, ' topples  with the tackle.'):
        'name(cc) + " travolge " + name(tc) + " con una botta di sedere."',
    # copiata da proc.hsp:9600 e :17261
    (25246, ' fell.'):
        'name(tc) + " cade a terra."',

    # --- l'esplosivo.
    (25288, 'You tried to plant explosives on ally, but decided not to...'):
        'Volevi piazzare l\'esplosivo su un compagno, ma ci hai ripensato...',
    # il giapponese non nomina nessuno, l'inglese si': la rete 11 vuole il nome
    (25292, ' planted an explosive. [Target Self to detonate.]'):
        'name(cc) + " piazza un esplosivo. [Mira su di te per farlo detonare.]"',
    (25298, ' pressed explosives against  and detonates it.'):
        'name(cc) + " preme l\'esplosivo contro " + name(tc) + " e lo fa detonare."',
    (25323, ' set something on the ground.'):
        'name(cc) + " prepara qualcosa sul terreno."',

    # --- i fili.
    # ⚠️ il giapponese nomina cc e tc, l'inglese solo tc (was() e' morfologia):
    #    i fili diventano soggetto, come il veleno del lotto 016
    (25335, '  slashed with threads.'):
        '"I fili lacerano " + name(tc) + "."',
    # «nel corpo di » + name() fonde: i due nomi restano complementi diretti
    (25368, ' put thread in .'):
        'name(cc) + " trafigge " + name(tc) + " con i suoi fili."',
    (25432, ' entangles  by wire.'):
        'name(cc) + " avviluppa " + name(tc) + " nei fili."',

    # --- la cattura e la gravita'.
    (25564, 'You have been overpowered.'):
        'Ti hanno immobilizzato...',
    # «schiacciato» concorderebbe con tc: la sfera diventa soggetto
    (25577, '  pressed by super Gravity.'):
        '"La sfera di gravità schiaccia " + name(tc) + "."',
    (25750, '  watching out for the damage.'):
        'name(cc) + " si prepara a incassare il colpo."',
    (25763, "You can't afford to lead others."):
        'Non sei in condizione di istruire nessuno.',

    # --- l'etere.
    (25779, 'Your Ether Disease is cured greatly.'):
        'Gli anticorpi dell\'etere si diffondono nel tuo corpo.',
    (25789, 'The Ether erodes your body.'):
        'L\'etere ti corrode il corpo.',

    # --- l'Onda Sororale (姉波動), che nasce qui e servira' a chat.hsp.
    # «X attacca, ma Y para»: la forma del lotto 015, che evita il genitivo
    (25798, ' defended against  gaze with Big Sister Energy!'):
        'name(cc) + " tenta lo sguardo soggiogante, ma " + name(tc) + " lo para con l\'Onda Sororale!"',
    # il giapponese ripete 勝手に due volte: la resa tiene la ripetizione
    (25802, ' became the older sister of  without permission, and  healed for some reason.'):
        'name(cc) + " fa la sorella maggiore con " + name(tc) + " di sua iniziativa, e di sua iniziativa ne trae conforto!"',
    # «il livello di » + name() fonde: il nome resta soggetto
    (25818, "'s level cannot contain any more of the Big Sister Energy..."):
        'name(cc) + " non ha il livello per contenere altra Onda Sororale..."',
    (25823, ' feel more in touch with the Big Sister Energy!'):
        'name(cc) + " sente l\'Onda Sororale più vicina!"',

    # --- l'abisso nell'occhio.
    # copiata da proc.hsp:9867
    (25837, ' pupils dilated.'):
        'name(cc) + " spalanca le pupille."',
    (25874, ' gazes at you. The Ether erodes your body.'):
        'name(cc) + " ti fissa, e l\'etere ti corrode il corpo."',

    # --- il lavaggio del cervello.
    # 洗脳の眼差し e' «Sguardo soggiogante» in skill.hsp:1200
    (25918, ' brainwash .'):
        'name(cc) + " soggioga " + name(tc) + "."',
    (25921, ' resisted the brainwashing.'):
        'name(tc) + " sembra non subire alcun effetto..."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-025.jsonl'
DA, A = 25000, 25999
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
