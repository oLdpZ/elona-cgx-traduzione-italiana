# -*- coding: utf-8 -*-
"""Lotto `command-028`: **la dea dei desideri e gli otto dèi che rispondono**.
Ventun rese, il cuore della zona 4000-4999.

⭐⭐ **Otto battute su ventuno sono di divinità che hanno già una voce, e
`action.hsp:14051`-`:14228` me l'ha data tutta.** Chi ha chiuso quel file ha
deciso come parla ciascuno, e qui si riscuote invece di ridecidere: Opatos ride
«Muahahah», Jure balbetta «N-non è mica…», Kumiromi parla a puntini, Mani
comanda, Itzpalt invoca gli elementi al vocativo, Yacatect fa la commerciante
in tono familiare, Lulwy apre con un sostantivo di disprezzo («Che ingenuità»,
qui «Che sfacciataggine»), Ehekatl raddoppia le frasi come una gatta.
💡 È la stessa cosa del punto 5 della 46ª un piano più su: là a tornare erano
sei battute **identiche**, qui torna il **registro** di otto personaggi. La
domanda di `repertorio.py` — «questo file fa parlare qualcuno che un altro ha già
fatto parlare?» — vale anche quando le parole sono nuove.

⭐⭐ **E l'inglese sbaglia due volte in questo lotto, tutte e due per una NEGAZIONE
persa.** A `:4454` il giapponese dice 「神力に余裕がない」, cioè che alla dea **non**
avanzano forze; l'inglese scrive «can afford to use her powers now», che dice
l'opposto e in mezzo a un `if` che blocca il desiderio. A `:4482` il giapponese
chiude con 「聞かなかったことにしてね」 — «fa' finta di non aver sentito» — e l'inglese
ci mette «Hey, listen to me!», che è il rovescio esatto della battuta: la dea si
lascia sfuggire che dentro Ehekatl c'è un dio e poi si rimangia tutto.
✅ In tutt'e due i casi la resa segue il **giapponese**, e nessuna rete deve
intervenire perché sono statiche: non c'è un contratto di funzioni da rispettare.
💡 È il terzo tipo di errore di monte in tre sessioni di lavoro su questo file —
dopo lo slot copiato (`:15188`) e l'inglese che appiattisce (`:15636`): qui
l'inglese **capovolge**.

⚠️ **Una voce non ha niente da tradurre e va dichiarata.** `:4465` è
`cnvtalk(inputlog + "!!")`: il gioco rimanda a schermo, gridata, la frase che il
giocatore ha appena **digitato**. Fuori da `inputlog` non c'è nessuna parola —
due punti esclamativi e le virgolette che ci mette `cnvtalk`. La resa coincide
con l'inglese **per costruzione**, ed è lo stesso criterio di
`"*" + skillname(efid) + "* "` (`proc.hsp:12101`): sta nella sezione «non c'è
niente da rendere» di `invariati.md`.

⚠️ **`:4436` non è un messaggio: è quello che parte in rete.** Tre righe sotto
c'è `net_send "wish" + s`, cioè il desiderio che finisce sulla bacheca condivisa.
Si traduce lo stesso — è anche il testo che il giocatore vede — ma vale la pena
saperlo: quella riga esce dal gioco.

⭐ Riscosso senza decidere: «Nemmeno il potere della dea dei desideri arriva fin
qui...» (`proc.hsp:14492`, stesso inglese), «il dio dentro» (`db_creature.hsp:101284`,
`<Il dio dentro Ehekatl>`) e «Alias» per 異名 (`command.hsp:10504`, la scheda del
personaggio). ⚠️ E «Quu» per 「きゅー」 della creatura quantistica, che
`db_creature.hsp` aveva già scelto: è una delle tredici divergenze volute di
`battute --divergenti`, e va tenuta.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4436 il desiderio che parte in rete (net_send, :4439).
    (4436, '  goes wild with joy, \\"!!\\" '):
        'cdatan(CDATAN_AKA, CHARA_PLAYER) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) '
        '+ " esulta di gioia, \\"" + inputlog + "!!\\" " + cnven(txtcopy)',

    # --- :4449-:4460 la dea dei desideri.
    # ⭐ stesso inglese di proc.hsp:14492
    (4449, 'The power of the Wish Goddess does not seem to reach here...'):
        'Nemmeno il potere della dea dei desideri arriva fin qui...',
    # ⚠️⚠️ l'inglese ha perso una negazione: 「神力に余裕がない」 dice che alla dea
    #    NON avanzano forze, e infatti la riga blocca il desiderio. Si segue il
    #    giapponese. Vedi il docstring.
    (4454, 'It seems that even the Wish Goddess can afford to use her powers now...'):
        'Nemmeno la dea dei desideri ha forze da spendere, adesso...',
    # lo spazio in coda è la giuntura con la finestra di input
    (4460, 'What do you wish for? '): 'Che cosa desideri? ',

    # --- :4465 NON si traduce: è la frase che il giocatore ha appena digitato,
    #     rimandata a schermo. Fuori da inputlog non c'è nessuna parola.
    #     Dichiarata in invariati.md, sezione «non c'è niente da rendere».
    (4465, '!!'): 'cnvtalk(inputlog + "!!")',

    # --- :4478-:4486 le tre risposte scherzose.
    (4478, "I don't quite understand what you're saying underwater..."):
        'Sott\'acqua fai solo glu glu, non ci capisco niente...',
    # ⚠️⚠️ l'inglese capovolge la chiusa: 「聞かなかったことにしてね」 è «fa' finta di
    #    non aver sentito», non «listen to me». La dea si lascia sfuggire il
    #    segreto e se lo rimangia. ⭐ «il dio dentro» è db_creature.hsp:101284.
    (4482, "It must be rough for the god insi... Ah... There's no god inside!... Hey, listen to me!"):
        'Dev\'essere dura per il dio dentro... ah... ma quale dio dentro, non esiste '
        'nessun dio dentro!... Ehi, fa\' finta di non aver sentito.',
    (4486, 'It must be rough for the person inside.'):
        'Dev\'essere dura per la persona dentro.',

    # --- :4490-:4547 gli otto dèi che rispondono al proprio nome.
    #     ⭐ il registro di ciascuno è quello di action.hsp:14051-:14228.
    # Ehekatl, la gatta: raddoppia (action.hsp:14108, «Mi hai chiamata? Mi hai chiamata?»)
    (4490, 'Meeewmew!'): 'Miaomiaomiaaa!',
    # Lulwy, altezzosa: apre col sostantivo di disprezzo (action.hsp:14207, «Che ingenuità.»)
    (4497, 'How bold you are to summon me like this.'):
        'Che sfacciataggine, convocarmi così.',
    # Opatos, fragoroso: «Muahahah» è di action.hsp:14051
    (4504, 'Muwahaha! Here I am!'): 'Muahahahah! Eccomi qua!',
    # Kumiromi, timido: parla a puntini (action.hsp:14068)
    (4511, "I'm happy... that you summoned me..."):
        'Mi hai chiamato... che gioia...',
    # Mani, che comanda (action.hsp:14099)
    (4518, "You did well to summon me. I'll allow you the honor of worshiping me."):
        'Hai fatto bene a chiamarmi. Ti concedo il diritto di adorarmi.',
    # Itzpalt, solenne, al vocativo (action.hsp:14161)
    (4526, 'The engraving upon your soul... This too is part of the fate spun by the Element.'):
        'Imprimilo nella tua anima: anche questo è destino tessuto dall\'Elemento.',
    # Yacatect, commerciante in tono familiare (action.hsp:14116)
    (4533, "You call on me and I appear! What's up? Got a business transaction for me?"):
        'Se mi chiami, arrivo subito! Allora? C\'è un affare da fare?',
    # Jure, che balbetta e nega (action.hsp:14058, «N-non è mica per te...»)
    (4540, "I-it's not like I wanted to come or anything! It's not!"):
        'N-non è mica che volessi venire, sai! Per niente!',
    # ⭐ la creatura quantistica: db_creature.hsp rende 「きゅう…」 «Quu...», ed è una
    #    delle tredici divergenze volute di `battute --divergenti`.
    (4547, 'q!'): 'Quu!',

    # --- :4554-:4570 il desiderio banale e il cambio di alias.
    (4554, 'A typical wish.'): 'Mmh... ti accontenti di poco.',
    # 「だめよ。」: in modalità mago il desiderio è rifiutato, e il giapponese lo
    # dice; l'inglese ci mette una risata.
    (4563, '*laugh*'): 'Neanche per idea.',
    # ⭐ «Alias» è il termine della scheda del personaggio, command.hsp:10504
    (4566, "What's your new alias?"): 'Qual è il tuo nuovo alias?',
    (4570, 'You will be known as <>.'):
        '"D\'ora in poi ti chiameranno <" + cmaka + ">."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-028.jsonl'
DA, A = 4401, 4574
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
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

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
