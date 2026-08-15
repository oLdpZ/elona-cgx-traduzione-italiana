# -*- coding: utf-8 -*-
"""Lotto `command-015`: le 21 voci che rispondono ai comandi del menu — i
rifiuti, la frase da insegnare, e le otto reazioni del compagno.

⭐⭐ **Le otto reazioni sono quattro gradi d'affetto per due direzioni, e la
simmetria e' del sorgente.** `:6661`-`:6694` guarda `CDATA_IMPRESSION` a quattro
soglie (150, 100, 0, sotto zero) e le usa **due volte**: quando lo segni fra gli
indispensabili e quando ce lo togli. Chi ti adora gonfia il petto e poi si
dispera; chi ti detesta schiocca la lingua e poi sputa per terra. Le otto rese
vanno lette in colonna, non una per una.

⚠️ **E qui torna «con aria», la manovra della 41a.** «looks a little
embarrassed» non puo' diventare «sembra imbarazzato», che concorderebbe col
compagno: diventa «ha **un'aria** imbarazzata», dove l'accordo cade su «aria».
Vale per tre reazioni su otto — imbarazzata, sorpresa, disperata — e le altre
cinque non ne hanno bisogno perche' sono verbi («si azzittisce», «ti abbraccia»,
«sputa per terra»).

⚠️ **`:6577` ha `itemname(ci)` nel giapponese e non c'entra niente.** Il sorgente
e' `lang(itemname(ci) + "彼らはあなたよりずっと体力があるのだから…", "They had a
lot more health than you…")`: il ramo giapponese si porta davanti il **nome di
un oggetto** dentro un avvertimento sui punti vita dell'avversario. E' un
avanzo, e l'inglese non ce l'ha. ✅ La resa segue l'inglese, che qui e' la
versione sana — ed e' anche l'unica scelta possibile, perche' `estrai` la
classifica **statica** sul ramo inglese.
⚠️ E «are you sure about this?» non puo' diventare «sei sicuro?»: il giocatore
non ha genere. «Vuoi continuare? », con lo spazio in coda che l'inglese porta.

⚠️ **`:6631` e' il rovescio: `name(tc)` ce l'ha l'INGLESE e non il giapponese.**
「どんな言葉を教えようか。」 non nomina nessuno, «What sentence should name(tc)
learn? » si'. La rete 11 pretende le funzioni dell'inglese, quindi la resa il
compagno lo nomina: «Che frase vuoi insegnare a name(tc)? ».

💡 **Quattro copie su ventuno**, e due sono identiche parola per parola:
«Hai riposto il mazzo.» (`action.hsp:19128`, stesso giapponese e stesso inglese)
e «Non c'e' spazio per scendere.» (`proc.hsp:10749`, idem). Le altre due seguono
una **famiglia** invece di una voce: «Hai gia' il massimo di compagni: …» sta in
tre file con tre code diverse, e qui la coda e' «non puoi portarne fuori altri»;
«Hai lasciato X ad aspettare in citta'» viene da `proc.hsp:19030`.

⚠️ **Un rifiuto va detto senza participio.** 「吊るしたままでは連れ出せない。」 e'
«non lo puoi portare fuori mentre e' appeso», e «appeso» concorderebbe con la
bestia — che al ranch e' spesso una femmina. ✅ «Finche' sta al gancio non si
puo' portare fuori», dove non c'e' participio da accordare.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6577-:6589 il gioco di carte.
    # ⚠️ «sei sicuro?» concorderebbe col giocatore; lo spazio in coda e' dell'inglese
    (6577, 'They had a lot more health than you, you will be put into great disadvantage, are you sure about this? '):
        'Ha molto più vigore di te: sei in netto svantaggio. Vuoi continuare? ',
    # ⭐ copiata parola per parola da action.hsp:19128, stesso jp e stesso en
    (6589, 'You put away the deck.'):
        'Hai riposto il mazzo.',

    # --- :6608-:6613 i due rifiuti del ranch.
    # ⚠️ «appeso» concorderebbe con la bestia: si toglie il participio
    (6608, 'You cannot leave livestock on hanging.'):
        'Finché sta al gancio non si può portare fuori.',
    # ⭐ la famiglia sta in tre file (action.hsp:11036, adv.hsp:4, proc.hsp:19056):
    #    cambia solo la coda, e qui e' «portarne fuori»
    (6613, "Your party is already full. You can't invite someone anymore."):
        'Hai già il massimo di compagni: non puoi portarne fuori altri.',

    # --- :6631 la frase da insegnare. ⚠️ `name(tc)` ce l'ha l'inglese, non il
    #     giapponese: la rete 11 pretende quella dell'inglese.
    # ⚠️ rete 8: «a » + name() darebbe «a il putit». Il nome passa a soggetto.
    (6631, 'What sentence should  learn? '):
        'name(tc) + ": che frase deve imparare? "',

    # --- :6651-:6655 quando lo fai tacere e quando lo lasci parlare.
    (6651, ' stops talking...'):
        'name(tc) + " si azzittisce..."',
    (6655, ' hugs you.'):
        'name(tc) + " ti abbraccia."',

    # --- :6667-:6676 le quattro reazioni a «Metti fra gli indispensabili»,
    #     una per grado d'affetto. ⚠️ `his(tc)` e' morfologia e sparisce.
    (6667, ' puffs out  chest with pride.'):
        'name(tc) + " gonfia il petto con orgoglio."',
    # ⚠️ «imbarazzato» concorderebbe: l'accordo cade su «aria» (la 41a)
    (6670, ' looks a little embarrassed.'):
        'name(tc) + " ha un\'aria imbarazzata."',
    (6673, ' looks surprised.'):
        'name(tc) + " ha un\'aria sorpresa."',
    (6676, ' clicks  tongue disapprovingly.'):
        'name(tc) + " schiocca la lingua con disgusto."',

    # --- :6683-:6692 le quattro reazioni a «Togli dagli indispensabili», sulle
    #     stesse quattro soglie e in ordine rovesciato di gradimento.
    (6683, ' looks depressed...'):
        'name(tc) + " ha un\'aria disperata..."',
    (6686, ' appears to be lost in thought...'):
        'name(tc) + " si perde nei propri pensieri..."',
    (6689, ' looks scared...'):
        'name(tc) + " ha paura..."',
    (6692, ' spits on the ground...'):
        'name(tc) + " sputa per terra..."',

    # --- :6703-:6714 i tre ordini. ⚠️ rete 8: «a » + name() darebbe «a il
    #     putit», quindi nei primi due il nome passa a SOGGETTO.
    (6703, 'You instructed  to not pick up items off the ground.'):
        'name(tc) + " ha l\'ordine di non raccogliere gli oggetti per terra."',
    (6707, 'You instructed  to do as they like with items on the ground.'):
        'name(tc) + " può fare come vuole con gli oggetti per terra."',
    # ⭐ la forma viene da proc.hsp:19030, che dice la stessa cosa altrove
    (6714, 'You order  to wait in town.'):
        '"Hai lasciato " + name(tc) + " ad aspettare in città."',
    # ⭐ copiata parola per parola da proc.hsp:10749
    (6718, "There's no place to get off."):
        "Non c'è spazio per scendere.",

    # --- :6762 il sacco da botte, che il menu slega con «Slega» (:6110).
    (6762, 'You release .'):
        '"Hai slegato " + name(tc) + "."',

    # --- :6770 la trasformazione.
    (6770, 'Which rank?'):
        'Quale rango?',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-015.jsonl'
DA, A = 6577, 6770
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
