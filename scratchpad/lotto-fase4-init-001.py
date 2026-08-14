# -*- coding: utf-8 -*-
"""Lotto fase4-init-001: il bottone Ok, l'errore di rete, e i primi quattro
ranghi — arena, arena delle bestie, Nefia, museo (init.hsp, righe 23-358).

46 rese, ed e' il **primo lotto di `init.hsp`**, che e' il file piu' delicato del
progetto: ci stanno le `#defcfunc` che restituiscono inglese fuori da `lang()` —
`he()`, `his()`, `him()`, `gendername()` — e i valori di `CDATAN_NEWSEX`, che
sono **scritti nel salvataggio**. Questo lotto tiene tutto quello, e prende
soltanto la parte che e' testo puro.

⭐⭐ **E' il primo lotto che usa la CHIAVE LUNGA `(riga, en, jp)`**, e il modello
l'ha imparata apposta per questo file: `:358` ha **«Great museum» due volte**,
perche' il giapponese distingue 大人気の博物館 («amatissimo») da
来客の絶えない博物館 («sempre affollato») e l'inglese ha appiattito i due gradini
in uno. Con la chiave corta la rete 0 fermava la zona; adesso le due voci si
dichiarano col giapponese accanto e il lotto passa. Vedi
`scratchpad/modello-chiave-lunga.py`.

⚠️⚠️ **Gli otto ranghi sono scale, e vanno lette come scale.** `rankn(t, c)` e'
un array `11 x 9`: per ogni categoria ci sono **dieci gradini** dal migliore al
peggiore piu' un'**undicesima voce, che non e' un gradino ma il NOME della
categoria**. `ranktitle()` (`:337`-`:351`) restituisce solo gli indici 0-9;
l'indice 10 lo legge `module.hsp:264` per scrivere «Cambio di rango (**Museo**
5° → 4°)». Tradurre l'undicesima come se fosse un titolo di rango — «Novizio»
invece di «Gilda» — e' esattamente l'errore che ha fatto l'inglese di monte.

⚠️⚠️ **La serie degli errori di monte passa da trentanove a quarantatre'**, e
sono tutti e quattro nella stessa famiglia: **l'inglese ha sbagliato gradino**.

- `:358` mette «Great museum» sul terzo gradino **e** sul quinto, e il museo
  perde una distinzione che il giapponese fa;
- `:358` chiama «Unknown **Ruin**» il decimo gradino, dove il giapponese dice
  無名の博物館, «museo senza nome». Non e' una rovina, e' un museo;
- `:357` chiama «Famous tourist» il nono gradino, dove il giapponese dice
  ちんけな遺跡荒らし, «predone di rovine da strapazzo» — cioe' l'inglese ha messo
  un complimento dove il giapponese fa uno sfottò — e chiama «Tomb robber»
  l'ottavo, dove il giapponese dice 探検者, «esploratore»;
- `:356` mette «New hope» sul settimo gradino copiandolo da `:355`, dove il
  giapponese dice ペットの母, «madre delle bestie».

✅ Tutti resi sul giapponese, che e' la regola del progetto dal lotto 019 della
38a.

⚠️ **«Madre delle bestie» non si puo' scrivere, e la ragione e' il giocatore.**
`:356` gradino 7 e' un titolo che il gioco appiccica a **te**, e meta' dei
giocatori sono femmine mentre l'altra meta' non lo e': «madre» sarebbe sbagliato
per gli uni, «padre» per gli altri. ✅ «**Balia** delle bestie»: e' un nome di
**ruolo**, grammaticalmente femminile ma applicabile a chiunque, come «una
guida» o «una spia». E' la strada del nome di genere fisso della 40a («si sente
la **pelle**…») usata su un titolo invece che su un complemento.

⚠️ **Gli accenti dentro la parola sono vietati, e qui e' la prima volta che
conta.** `accenti.py` degrada **ogni** accento in lettera + apostrofo, non solo
quelli finali: «élite» diventerebbe «e'lite» a schermo. Nei ranghi la parola era
la prima che veniva in mente — «gladiatore d'élite» — ed e' stata evitata
ovunque: «Gladiatore **scelto**», «Domatore **scelto**». 💡 Gli accenti finali
vanno benissimo — «piu'», «perche'» — perche' l'apostrofo li' e' quello che
l'italiano scrive comunque.

💡 **I termini di mondo erano tutti gia' fissati altrove**, e nessuno di loro sta
in una frase intera che `dossier.py` possa agganciare: ティリス e' **Tyris**
(`proc.hsp:9996`), イルヴァ e' **Irva** (`text.hsp:2917`), ダンジョン e' il
**sotterraneo** (`action.hsp:2180`), 博物館 il **museo** (`db_item.hsp:145651`),
ペットアリーナ l'**arena delle bestie** (`db_creature.hsp:118259`), 遺跡 le
**rovine** (`text.hsp:3021`). E' di nuovo il caso del `termini.py` che manca.

⚠️ **Una divergenza nuova e legittima: 観光客 e' «il turista» a
`db_creature.hsp:118924` e «Turista» qui.** Li' e' il **nome di una creatura**, e
il contratto dei nomi vuole che porti il proprio articolo; qui e' un **gradino di
rango** che il gioco appiccica al giocatore, e un titolo l'articolo non lo porta.
E' la stessa distinzione di 「痛っ！」 nel lotto `ai-001`: lo stesso giapponese in
due tipi di sito diversi. ⚠️ E come quella, **nessuno strumento la vede**:
`battute --divergenti` legge solo `db_creature.hsp.jsonl`.

⚠️ **Due invariati nuovi, tutt'e due dichiarati in `invariati.md`**: `Ok`
(`:23`, il bottone di `promptOk` — parola italiana identica all'inglese, come
`bonus`) e `Arena` (`:355` gradino 11, il nome della categoria — l'italiano ha
la stessa parola, e viene dallo stesso latino).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- i due sparsi.
    # ⚠️ invariato: parola italiana identica all'inglese, come «bonus»
    (23, 'Ok'):
        'Ok',
    (76, 'Error:'):
        'Errore:',

    # --- :355 l'arena. Dieci gradini piu' il nome della categoria.
    (355, 'Arena champion'):
        "Campione dell'arena",
    (355, 'Super elite gladiator'):
        'Gladiatore invitto',
    (355, 'Star gladiator'):
        "Stella dell'arena",
    # ⚠️ «d'élite» darebbe «d'e'lite» a schermo: accenti.py degrada anche gli
    #    accenti dentro la parola
    (355, 'Elite gladiator'):
        'Gladiatore scelto',
    (355, 'Veteran gladiator'):
        'Gladiatore esperto',
    (355, 'Popular gladiator'):
        'Gladiatore affermato',
    (355, 'New hope'):
        "Promessa dell'arena",
    (355, 'Darkhorse'):
        'Mina vagante',
    (355, 'Low class fighter'):
        'Gladiatore di bassa lega',
    (355, 'Unknown fighter'):
        'Gladiatore senza nome',
    # ⚠️ invariato: il nome della categoria, e l'italiano ha la stessa parola
    (355, 'Arena'):
        'Arena',

    # --- :356 l'arena delle bestie.
    (356, 'King of tamer'):
        'Sovrano di tutte le bestie',
    (356, 'Super elite tamer'):
        'Domatore impareggiabile',
    (356, 'Prince of animals'):
        'Principe delle bestie',
    (356, 'Chief of animals'):
        'Idolo delle bestie',
    (356, 'Elite tamer'):
        'Domatore scelto',
    (356, 'Notorious tamer'):
        'Domatore rinomato',
    # ⚠️ il giapponese dice ペットの母, e «madre» sarebbe sbagliato per meta' dei
    #    giocatori: «balia» e' un nome di RUOLO, buono per chiunque
    (356, 'New hope'):
        'Balia delle bestie',
    (356, 'Average tamer'):
        'Discreto domatore',
    (356, 'Petty tamer'):
        'Domatore alle prime armi',
    (356, 'Unknown tamer'):
        'Domatore senza nome',
    (356, 'Pet Arena'):
        'Arena delle bestie',

    # --- :357 Nefia e i sotterranei.
    (357, 'King of Nefia'):
        'Signore di Nefia',
    (357, 'Champion of labyrinth'):
        'Dominatore dei labirinti',
    (357, 'Dungeon master'):
        'Padrone dei sotterranei',
    (357, 'Famous adventurer'):
        'Esploratore illustre',
    (357, "Children's star"):
        'Idolo dei bambini',
    (357, 'Guide of Nefia'):
        'Guida dei sotterranei',
    (357, 'Notorious tomb robber'):
        'Famoso predone di rovine',
    (357, 'Tomb robber'):
        'Esploratore',
    # ⚠️ il giapponese dice ちんけな遺跡荒らし, uno sfottò: l'inglese ci ha messo
    #    un complimento («Famous tourist»)
    (357, 'Famous tourist'):
        'Predone di rovine da strapazzo',
    (357, 'Tourist'):
        'Turista',
    (357, 'Crawler'):
        'Esploratore di Nefia',

    # --- :358 il museo. ⚠️ «Great museum» sta su DUE gradini: chiave lunga
    (358, 'Tyris\' greatest museum'):
        'Il museo più grande di Tyris',
    (358, 'Royal museum'):
        'Museo famosissimo',
    (358, 'Great museum', '大人気の博物館'):
        'Museo amatissimo',
    (358, 'Top museum'):
        'Museo famoso',
    (358, 'Great museum', '来客の絶えない博物館'):
        'Museo sempre affollato',
    (358, 'Good museum'):
        'Museo che piace',
    (358, 'Average museum'):
        'Museo conosciuto',
    (358, 'Small museum'):
        'Museo passabile',
    (358, 'Unknown museum'):
        'Museo poco visitato',
    # ⚠️ l'inglese dice «Ruin», il giapponese 無名の博物館: e' un museo
    (358, 'Unknown Ruin'):
        'Museo senza nome',
    (358, 'Museum'):
        'Museo',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-init-001.jsonl'
DA, A = 0, 358
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\init.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_init.jsonl', encoding='utf-8') if l.strip()]
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
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
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
