# -*- coding: utf-8 -*-
"""Lotto `command-008`: le 43 voci di `*setHistory5`, la quinta e ultima riga del
«Background».

Chiude la schermata aperta dal `command-004`. A differenza della terza e della
quarta, questa riga e' una **frase intera per conto suo** — maiuscola in testa,
punto in coda — perche' `chara.hsp:3332` la disegna da sola.

⭐ **Il giapponese e' nominale gia' lui, e piu' spesso che altrove**: otto voci
su quarantatre sono la forma 「趣味は…」/「…が趣味」, cioe' letteralmente
«passatempo: …». La resa la copia — «Passatempo: il pisolino», «Passatempo: la
caccia» — invece di girarla nel «You like to…» che ci mette l'inglese.

⚠️ **Altre due voci duplicate, e sono la stessa specie del `command-007`**:
`:10059` ripete `:10047` (「慕っている師匠がいる。」) e `:10089` ripete `:10068`
(「趣味は昼寝。」). Con le due del lotto prima fanno **quattro** in due elenchi
consecutivi: il pisolino e il maestro escono col doppio della probabilita'
degli altri quarantuno. Non e' un caso isolato, e' come sono fatte le tabelle.

⚠️ **Un errore di monte nuovo**: `:10065` 「他人を否定することが快感。」 e' «che
gusto dare torto agli altri», cioe' il piacere di **negare quel che gli altri
dicono**. L'inglese legge 否定 come «deny» nel senso di privare e scrive «You
enjoy denying pleasure to others», che e' un'altra cosa — e per giunta una cosa
che il giapponese non dice.

Tetto 50 caratteri (`:10056`); la resa piu' lunga ne fa 48. Zero copie da
`dossier.py`, come per gli altri quattro gruppi: la schermata del passato non
parla la lingua di nessun'altra parte del gioco.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- le otto 「趣味は…」: il giapponese scrive «passatempo:», e la resa lo copia
    (10011, 'You like to tinker with machines.'):
        'Passatempo: armeggiare con le macchine.',
    (10017, 'You like to stalk people.'):
        'Passatempo: pedinare la gente.',
    (10023, 'You like to garden.'):
        'Passatempo: il giardinaggio.',
    (10026, 'You like to cultivate bonsai.'):
        'Passatempo: curare i bonsai.',
    (10038, 'You like to hunt.'):
        'Passatempo: la caccia.',
    (10068, 'You like to nap.'):
        'Passatempo: il pisolino.',
    (10074, 'You like to read.'):
        'Passatempo: la lettura.',
    (10104, 'You like making fun of others.'):
        'Passatempo: prendere in giro qualcuno.',

    # --- le altre trentacinque.
    # ⚠️ 「監禁」 e' la reclusione, non le catene
    (10014, 'You like being chained up.'):
        'Passatempo: farsi rinchiudere.',
    (10020, "You like to see pain on people's faces."):
        'Che piacere, una faccia stravolta dal dolore.',
    (10029, 'You like stuffed animals.'):
        'Un debole per i peluche.',
    # ⚠️ «sadico» ha un genere: si dice il vizio, non chi ce l'ha
    (10032, 'You are a self-proclaimed sadist.'):
        'Sadismo, per autodichiarazione.',
    (10035, 'You risk your life for creative activities.'):
        'La creazione vale una vita intera.',
    (10041, 'You like to wear clothes of the opposite sex.'):
        "Un interesse per i vestiti dell'altro sesso.",
    (10044, 'You love small animals.'):
        'Amore sviscerato per le bestioline.',
    (10047, 'You yearn for your master.'):
        "C'è un maestro da venerare.",
    (10050, 'You have memories of your past life.'):
        'Restano i ricordi di una vita precedente.',
    (10053, 'You like to exercise.'):
        'Il piacere di muovere il corpo.',
    (10056, 'Your body is branded by a mysterious coat of arms.'):
        'Uno stemma misterioso sulla pelle.',
    (10062, 'You have a sharp intuition.'):
        'Un intuito pronto, in ogni occasione.',
    # ⚠️ errore di monte: 「否定する」 e' dare torto, non privare di un piacere
    (10065, 'You enjoy denying pleasure to others.'):
        'Che gusto, dare torto agli altri.',
    (10071, 'You have a strong attachment to life.'):
        'Un attaccamento fortissimo alla vita.',
    (10077, 'You enjoy using violence.'):
        'Il piacere di menare le mani.',
    (10080, "You have a secret that you can't reveal."):
        "C'è un segreto che nessuno deve sapere.",
    (10083, 'You are good at singing.'):
        'Un gran talento nel canto.',
    (10086, 'You are gullible.'):
        'Una gran facilità a cascarci.',
    (10092, 'You are bad at lying.'):
        'Le bugie non riescono mai bene.',
    (10095, 'You easily fall in love.'):
        'Un cuore che si innamora in fretta.',
    (10098, 'You are a hard worker.'):
        'Un gran zelo sul lavoro.',
    (10101, 'You had a mission you failed to achieve.'):
        "C'è una missione rimasta incompiuta.",
    # ⚠️ 「弟子」 sono i discepoli, non i seguaci
    (10107, 'You have followers.'):
        "C'è qualche discepolo al seguito.",
    (10110, 'You hold a powerful grudge against someone.'):
        'Un rancore che dura più del previsto.',
    (10113, 'You fear betrayal above all else.'):
        'Il tradimento fa più paura di ogni altra cosa.',
    (10116, 'You like to collect junk.'):
        'Il gusto di raccogliere cianfrusaglie.',
    (10119, 'You actually want to live quietly.'):
        'In fondo, il sogno è una vita tranquilla.',
    (10122, 'You have a desire to be messed up.'):
        "C'è il desiderio di farsi ridurre a pezzi.",
    (10125, 'You have multiple hearts.'):
        'Più di un cuore in petto.',
    (10128, 'You sometimes have unnatural memory loss.'):
        'Ogni tanto la memoria sparisce, e non è normale.',
    (10131, 'You never forget food grudges.'):
        'I torti a tavola non si dimenticano mai.',
    (10134, "You are quick to covet other people's things."):
        'La roba altrui fa subito gola.',
    (10137, 'You think humanity should be destroyed.'):
        "L'umanità meriterebbe di sparire.",
    (10140, 'You prefer bamboo shoots to mushrooms.'):
        'Meglio i germogli di bambù dei funghi.',
    (10143, 'You are starving for motherhood.'):
        "Una fame d'affetto materno.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-008.jsonl'
DA, A = 10009, 10146
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
