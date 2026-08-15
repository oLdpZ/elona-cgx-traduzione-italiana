# -*- coding: utf-8 -*-
"""Lotto `command-007`: i 43 difetti di `*setHistory4`, la CODA della terza frase
del «Background».

E' l'altra meta' del `command-006`: ogni difetto si salda a ognuno dei 45 pregi,
che finiscono tutti in «, ma». Quindi ogni resa qui e' un **sintagma nominale
minuscolo** che regge dopo un «ma» e chiude col punto — mai un verbo di persona,
che vorrebbe un soggetto e quindi un genere.

⚠️ **Quarantatre voci e non quarantacinque, perche' DUE SONO SCRITTE DUE
VOLTE.** `:9933` ripete `:9924` (「私生活はだらしない。」) e `:9972` ripete `:9966`
(「勘違いが激しい。」), stessa firma dentro lo stesso elenco: quei due difetti
escono col **doppio** della probabilita' degli altri. `estrai --da-tradurre`
li fonde per firma e `applica.py` scrive la resa in tutt'e due i siti, quindi
non c'e' niente da fare — ma e' una famiglia nuova nella serie degli errori di
monte: non una traduzione sbagliata, una **voce duplicata nella tabella**.

⚠️ **E quattro su quarantatre cominciano con la maiuscola** — `:9996`, `:9999`,
`:10002`, `:10005`, «You can't read…» invece di «you can't read…» — dentro un
elenco di code di frase, dove le altre trentanove sono minuscole. In italiano
sono minuscole tutte e quarantatre: la maiuscola spezzerebbe la frase che la
riga di sopra ha aperto.

⚠️⚠️ **Due volte l'inglese dice un'altra cosa, e sono errori di monte veri:**
  - `:9873` 「熱中すると周りが見えなくなる。」 e' «quando ci si appassiona non si
    vede piu' niente intorno»; l'inglese scrive «you drain the enthusiasm from
    those around you», cioe' che l'entusiasmo lo **togli agli altri**. Non e'
    una sfumatura: e' il contrario del soggetto;
  - `:9978` 「周囲からよく誤解される。」 e' «gli altri ti fraintendono spesso» —
    passivo — e l'inglese lo gira in attivo, «you often misunderstand
    situations». ⚠️ E cosi' facendo lo rende **quasi identico** a `:9966`
    「勘違いが激しい。」, che invece e' proprio «capisci fischi per fiaschi»: due
    voci diverse dell'elenco diventano la stessa in inglese.
  - 💡 minore, `:9930` 「肝心なところで失敗する。」 e' «sbagli nel momento
    decisivo», non «you fail at basic things».

Tetto 48 caratteri (`:10002`), il piu' stretto dei cinque gruppi; la resa piu'
lunga ne fa 45. Zero copie da `dossier.py`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9873-:10005 i quarantatre difetti. Tutti minuscoli, tutti nominali:
    #     ognuno deve reggere dopo il «, ma» di uno qualsiasi dei 45 pregi.
    # ⚠️ errore di monte: il giapponese dice che chi si appassiona non vede piu'
    #    niente intorno, l'inglese che l'entusiasmo lo togli agli altri
    (9873, 'you drain the enthusiasm from those around you.'):
        'la passione fa perdere di vista tutto il resto.',
    (9876, "you are insensitive the other's goodwill."):
        "nessuna sensibilità per l'affetto altrui.",
    (9879, 'you often get caught up in your own delusions.'):
        'una gran brutta tendenza a fantasticare.',
    (9882, 'you look down on others.'):
        'uno sguardo dall\'alto in basso sugli altri.',
    (9885, 'you are in enormous debt.'):
        'un debito enorme sul groppone.',
    (9888, 'you have a strange sense of fashion.'):
        'un gusto strambo nel vestire.',
    (9891, 'your body odor is worrisome.'):
        'un cruccio fisso: il proprio odore.',
    (9894, 'your personality changes when you hold a knife.'):
        'il carattere cambia con una lama in mano.',
    (9897, 'you have experienced major trauma.'):
        'un trauma grosso da qualche parte.',
    (9900, 'you do not trust others.'):
        'nessuna fiducia negli altri.',
    (9903, 'you are surprisingly servile.'):
        'una remissività da far paura.',
    (9906, 'you suffer from a rare disease.'):
        'un male raro addosso.',
    (9909, 'you are cold to those who do not interest you.'):
        'gelo per chi non interessa.',
    (9912, 'you make poor financial decisions.'):
        'nessun senso del denaro.',
    (9915, 'you are not good at socializing.'):
        'poca dimestichezza con la gente.',
    (9918, 'you easily get carried away.'):
        'la testa si monta al primo successo.',
    (9921, 'your sense of taste is odd.'):
        'un palato tutto suo.',
    (9924, 'you are undisciplined in your private life.'):
        'una vita privata sciatta.',
    (9927, 'you make lots of mistakes.'):
        'una certa dose di sbadataggine.',
    # ⚠️ 「肝心なところで」: lo sbaglio arriva quando conta, non sulle cose facili
    (9930, 'you fail at basic things.'):
        'lo sbaglio arriva nel momento decisivo.',
    (9936, 'you act terribly when drunk.'):
        "pessime maniere quando c'è di mezzo il vino.",
    (9939, 'you hate yourself.'):
        'nessuna simpatia per se stessi.',
    (9942, 'you have no confidence in yourself.'):
        'nessuna fiducia in se stessi.',
    (9945, 'you are actually a gigantic pervert.'):
        'in verità, una perversione smisurata.',
    (9948, 'you have no sense of direction.'):
        "nessun senso dell'orientamento.",
    (9951, 'you are in love with money.'):
        'una debolezza per il denaro.',
    (9954, 'you are self-conscious.'):
        'troppa coscienza di sé.',
    (9957, 'your jokes are terrible.'):
        'battute che non fanno ridere nessuno.',
    (9960, 'you are greedy.'):
        'una certa ingordigia.',
    (9963, "you can't draw whatsoever."):
        'disegni da far pietà.',
    (9966, 'you tend to misunderstand people.'):
        'malintesi a ripetizione.',
    (9969, "you don't really have any friends."):
        'nemmeno un amico come si deve.',
    (9975, 'your emotions are easy to read.'):
        'i pensieri si leggono in faccia.',
    # ⚠️ errore di monte: 「周囲からよく誤解される」 e' passivo — sono gli altri a
    #    fraintendere. L'inglese lo gira in attivo e lo confonde con :9966.
    (9978, 'you often misunderstand situations.'):
        'gli altri fraintendono spesso.',
    (9981, "you can't handle insects."):
        'gli insetti fanno ribrezzo.',
    (9984, "you don't have much of a presence."):
        'una presenza che non si nota.',
    (9987, 'you are very prideful.'):
        'un orgoglio smisurato.',
    (9990, 'you love shady things.'):
        'una passione per le cose equivoche.',
    (9993, 'you have a hidden personality.'):
        "un'altra personalità tenuta nascosta.",
    # --- le quattro che in inglese cominciano con la maiuscola: qui no.
    (9996, "You can't read texts longer than five lines."):
        'niente testi più lunghi di cinque righe.',
    (9999, 'You are big foodie.'):
        'una gola notevole.',
    # ⚠️ il giapponese dice facce E nomi, l'inglese solo i nomi
    (10002, "You are bad at remembering other people's names."):
        'facce e nomi degli altri non restano in mente.',
    (10005, "You tend to put off things you don't like."):
        'le cose sgradite finiscono sempre rimandate.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-007.jsonl'
DA, A = 9871, 10008
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
