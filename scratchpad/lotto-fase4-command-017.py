# -*- coding: utf-8 -*-
"""Lotto `command-017`: la scheda dei talenti, prima meta' — le intestazioni e
le quarantasei righe di stato che il gioco elenca sotto `[bit]`.

⚠️⚠️ **Questa schermata si apre ANCHE su un alleato, e l'inglese ci arriva con un
trucco che l'italiano non puo' ereditare.** `*com_trait` si raggiunge con
`z,x [Ally]` (`:2589`), e quando `tc != CHARA_PLAYER` il gioco **non ricompone**
le frasi: fa `cnv_str` sulla stringa **gia' costruita** (`:2561`-`:2564`),
sostituendo `"You"` con `him2(tc)` e `"Your"` con `his(tc, 1)`. Ecco perche' le
righe di monte sono tutte in seconda persona: servono a quella sostituzione.
✅ Una resa italiana non contiene piu' `You`, quindi **la conversione muore**. La
strada non e' subirla ma disinnescarla: **registro nominale**, senza soggetto e
senza participio riferito alla persona, cosi' la riga vale identica per te e per
il compagno. Il precedente e' della 44ª, nella schermata gemella: `:1985`
«*Your bonuses and penalties.» -> «Effetti in corso», col possessivo tolto.
💡 E la scoperta ha corretto uno strumento: `cnv_str_en.py` non vedeva quelle
quattro chiamate perche' la sua regex pretendeva un identificatore semplice come
primo argomento, mentre qui c'e' `listn(0, cnt)`. Allargata: 41 chiamate -> **49**,
chiavi inglesi 17 -> **24**.

⭐ **La testa della famiglia era gia' ferma**: `feat` -> «talento»
(`glossario.md:359`, deciso il 2026-08-10 su `action.hsp:15422`). Da li'
`[Available feats]` -> «[Talenti disponibili]» e `[Feat]` -> «[Talento]».

⭐ **Tre nomi non si sono decisi qui, si sono ritrovati.** 「レイハンド」 e' gia'
«Imposizione delle mani» (`chara_func.hsp:6258`, la battuta di Jure);
「死を司る」 nomina la **Sentenza di morte** di `skill.hsp:1044` e `buff.hsp:71`;
`Analysis` e' «Analisi» in `skill.hsp:252`. Nessuno dei tre lo avrebbe pescato la
rete 3, che confronta il giapponese **intero**.

⚠️ **Due errori di monte, e vengono dalla stessa coppia di righe.**
- `:2275` 「乗馬に適さない」 e' «non adatto alla cavalcatura», e l'inglese scrive
  **«You are too weak to carry you.»**, che oltre a essere sgrammaticato dice
  un'altra cosa — che sei tu a essere troppo debole per portare te stesso. La
  coppia giusta e' `:2260`/`:2275`, «Cavalcabile»/«Non cavalcabile»;
- `:2265` 「あなたは分裂できる」 e' «puoi dividerti», secco, e `:2285`
  「元気な場合分裂する」 e' «ti dividi **se sei in forze**». L'inglese mette
  «when attacked easily» sulla prima e «when attacked» sulla seconda: sposta la
  condizione sulla riga sbagliata e la cambia. Le due rese seguono il giapponese.

💡 **«Cavalcabile» e «Non cavalcabile» sono la manovra del lotto**: un aggettivo
in `-bile` non ha genere al singolare, quindi regge sia sul giocatore sia su una
compagna. Dove non c'e', si passa al nome astratto — «Autodistruzione»,
«Corazza speciale», «Neutralizzazione degli attacchi elementali» — o si sposta
l'accordo su una cosa: «Furia al primo attacco **subito**» concorda con
«attacco», non con chi la prova, ed e' il participio spostato della 44ª.

Tetto 56 caratteri: e' l'inglese di monte piu' lungo della schermata
(«You got elegance. [Increase Quality Of Customers In Shop]», `:2467`), e la
finestra lo contiene gia' perche' upstream ci gira. ⚠️ `larghezze.py` qui non
misura niente — copre solo `text.hsp` (scoperta 4 della 44ª). Il metro del
sorgente: finestra 730 px, righe di stato a `wx + 70` su una barra da 640 px, e
**senza** la colonna del grado, che sta a `wx + 270` ed e' solo dei talenti veri.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2005 la durata di un effetto nell'analisi di stato. ⚠️ dinamica:
    #     l'inglese da' solo «(3) », il giapponese dice «per 3 turni». La resa
    #     segue il giapponese, che qui e' l'unico dei due a spiegare il numero.
    (2005, '() '):
        '"(" + dur + " turni) "',

    # --- :2012-:2014 le due intestazioni dell'analisi. ⭐ «Analisi» copiata da
    #     skill.hsp:252.
    (2012, 'Analysis'): 'Analisi',
    (2014, 'Results'): 'Risultati',

    # --- :2113-:2152 le intestazioni della scheda dei talenti.
    #     ⭐ feat -> talento, glossario.md:359.
    (2113, '[Available feats]'): '[Talenti disponibili]',
    (2116, '[Feats and traits]'): '[Talenti e tratti]',
    # ⚠️ 「(条件不足)」 e' «condizione insufficiente»: l'inglese dice solo
    #    «(requirement)». Si accoda al nome del talento in 186 px, quindi resta
    #    corta come l'inglese invece di spiegare.
    (2134, '(requirement)'): '(requisiti)',
    (2143, '[Feat]'): '[Talento]',
    (2146, '[Mutation]'): '[Mutazione]',
    # ⚠️ 「[先天]」 e' «congenito», non «razza»: e' la categoria del tratto che
    #    nasce col personaggio. Il giapponese e' piu' preciso e piu' corto, e
    #    «Razza» qui si confonderebbe col campo Razza della scheda.
    (2149, '[Race]'): '[Innato]',
    (2152, '[Ether]'): '[Etere]',
    # ⚠️ invariato: il giapponese scrive «[bit]» tale e quale.
    (2162, '[bit]'): '[bit]',

    # --- :2165-:2330 le righe di stato. Registro nominale: nessun soggetto,
    #     nessun participio riferito alla persona (vedi il docstring).
    (2165, 'You are disguising yourself.'): 'Sotto mentite spoglie',
    (2170, 'You are infected with abdominal parasites.'): "Parassiti nell'addome",
    (2175, 'You are infected with brain parasites.'): 'Parassiti nel cervello',
    (2180, 'You have anorexia.'): 'Anoressia',
    (2185, 'You can float.'): 'Levitazione',
    # ⚠️ le due dell'invisibilita' sono diverse: 「透明になれる」 e' diventarlo,
    #    「透明な存在が見える」 e' vederla.
    (2190, 'You can be invisible.'): 'Invisibilità a volontà',
    (2195, 'You see invisible creatures.'): "Vista dell'invisibile",

    # --- :2200-:2225 le sei immunita'. ⭐ i nomi degli stati sono quelli della
    #     44ª (`:1844`-`:1864`): confusione, cecita', terrore, sonno, paralisi.
    (2200, 'You negates the effect of confusion.'): 'Immunità alla confusione',
    (2205, 'You negates the effect of blindness.'): 'Immunità alla cecità',
    (2210, 'You negates the effect of fear.'): 'Immunità al terrore',
    (2215, 'You negates the effect of sleep.'): 'Immunità al sonno',
    (2220, 'You negates the effect of paralysis.'): 'Immunità alla paralisi',
    (2225, 'You negates the effect of poison.'): 'Immunità al veleno',

    (2230, 'You can digest rotten foods.'): 'Digestione del cibo marcio',
    (2235, 'You will not have item stolen.'): 'Immunità ai furti',
    (2240, 'You self-destruct.'): 'Autodistruzione',
    # ⭐ «death word» e' la Sentenza di morte di skill.hsp:1044 e buff.hsp:71.
    (2245, 'You govern death word.'): 'Dominio sulla sentenza di morte',
    (2250, 'You can cast triple arrow spells.'): 'Magie a tripla freccia',
    # ⭐ 「レイハンド」 e' gia' «Imposizione delle mani», chara_func.hsp:6258.
    (2255, 'You can use Layhand.'): 'Imposizione delle mani',

    # --- la coppia della cavalcatura. ⚠️ l'inglese di :2275 e' sgrammaticato e
    #     dice un'altra cosa; il giapponese e' il semplice contrario di :2260.
    #     💡 «-bile» non ha genere al singolare: regge anche su una compagna.
    (2260, 'You are suitable for riding.'): 'Cavalcabile',
    (2275, 'You are too weak to carry you.'): 'Non cavalcabile',

    # --- la coppia della scissione. ⚠️ l'inglese sposta la condizione sulla
    #     riga sbagliata: il giapponese ce l'ha su :2285, non su :2265.
    (2265, 'You can split when attacked easily.'): 'Scissione',
    (2285, 'You can split when attacked.'): 'Scissione se in forze',

    (2270, 'You are strong against curses.'): 'Resistenza alle maledizioni',
    (2280, "You neutralize each other's attribute attacks."):
        'Neutralizzazione degli attacchi elementali',
    (2290, 'You are made of special metal'): 'Corpo di metallo speciale',
    (2295, "You don't bleed easily."): 'Resistenza al sanguinamento',
    # 💡 il soggetto passa alle mine, che un genere ce l'hanno per conto loro.
    (2300, 'You are not sensed by land mines.'): 'Le mine non scattano',
    # 💡 il participio c'e' e concorda con «attacco»: e' la manovra della 44ª.
    (2305, 'You get angry when attacked.'): 'Furia al primo attacco subito',
    (2310, 'You are covered in special armor.'): 'Corazza speciale',
    (2315, 'You are good at shooting fast.'): 'Maestria nel tiro rapido',
    (2320, 'You are ready for Jiujitsu.'): 'Postura di jujitsu',
    # 「詠唱中」 e' durante la recitazione dell'incantesimo; l'impersonale «si»
    # tiene fuori il genere.
    (2325, 'You feel uplifted while casting.'): 'Esaltazione nel lanciare magie',

    # --- :2330 la testata delle varie e il corpo complesso.
    #     ⚠️ dinamica: «Speed» e' «Velocità» in tutto il progetto
    #     (command.hsp:10517, skill.hsp:59), e la sigla SPD non esiste in resa.
    (2330, '[ETC]'): '[Varie]',
    (2330, 'Your body is complicated. [SPD-%]'):
        '"Corpo complesso [Velocità -" + cdata(CDATA_BODY_SPEED_FIX, tc) + "%]"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-017.jsonl'
DA, A = 2005, 2330
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
