# -*- coding: utf-8 -*-
"""Lotto `command-012`: le 31 voci del «苦手なもの» e le due intestazioni di
`*com_knowSelf`.

E' la seconda sezione della finestra della telepatia — quel che il compagno
**non regge**: dodici elementi di attacco, sei stati, cinque cose fisiche e
**cinque scherzi**. Piu' il titolo della finestra e le due intestazioni della
schermata gemella, quella che legge gli effetti attivi.

⭐ **I cinque scherzi sono paure di creature precise**, e il sorgente le lega a
un `CREATURE_ID`: 「ふかふかパン」 al `CREATURE_ID_ALCHEMIST_NAPLUS`, poi il
sale, lo yeek, il gatto, lo squalo. La resa li prende **dal progetto, non
dall'inglese**: «pane soffice» sta gia' in `db_item.hsp:141763` e in
`ai.hsp:1163`, «lo yeek» in tre file, «il gatto» in quattro, «sale» in
`db_item.hsp:141789`. La rete 3 li avrebbe chiesti comunque.
💡 Coi nomi di creatura viene dentro anche **l'articolo**, che e' il contratto
dei nomi (`contratto-nomi.md` §4): in colonna si legge «lo yeek», «il gatto»,
«lo squalo», e va bene — sono le cose di cui ha paura, non etichette.

⚠️ **Undici elementi su dodici erano gia' decisi**, e non da una voce sola:
`action.hsp:6918`-`:7044` ha le ventiquattro righe di «Add X Resistance» e «Add
X Damage», e da li' vengono «fuoco», «gelo», «fulmine», «oscurita'», «mentale»,
«veleno», «oltretomba», «suono», «nervi», «caos», «magia». Cercare prima di
scrivere, di nuovo.

⚠️ **`:1985` ha `name(tc)` nel GIAPPONESE e non nell'inglese.** Il sorgente e'
`lang("<title1>◆ " + name(tc) + "の受けている影響<def>\\n", "*<title1> Your
bonuses and penalties.<def>\\n")`, e `estrai` la classifica **statica** perche'
il ramo inglese e' una stringa pura. ✅ Quindi la resa **non puo' nominare il
soggetto** anche volendo — e' la regola della 40a («se l'inglese non ha
`name()`, la resa italiana non puo' nominare il soggetto») in una forma nuova,
dove a nominare e' il giapponese.
⚠️ E il soggetto non e' sempre il giocatore: `:1981` fa `if ( tc ==
CHARA_PLAYER )` per un pezzo solo, quindi «i tuoi bonus» sarebbe sbagliato per
un alleato. ✅ «Effetti in corso», che non nomina nessuno.

💡 **E l'asterisco di `:1985` sta fuori dal tag.** L'inglese scrive
`"*<title1> Your bonuses…"` mentre `:1999` scrive `"<title1>*Effects…"` e il
giapponese mette il ◆ **dentro** in tutt'e due: a schermo, il primo asterisco
resta fuori dallo stile del titolo. La resa lo rimette dentro, come fa l'altra
riga.

⚠️ **La rete 3 su 「塩」 e' un falso positivo, e la colpa e' di come `db_item.hsp`
spezza i nomi.** `ITEM_ID_BOTTLE_SALT` in inglese ha **due** pezzi di nome —
`ioriginalnameref` = «salt» e `ioriginalnameref2` = «bottle» (`:141789`-`:141790`)
— e in giapponese uno solo, 「塩」 (`:141786`). L'estrazione appaia quindi lo
stesso giapponese sia a «salt» che a «bottle», e il dizionario ha 「塩」 reso
«sale» **e** «bottiglia». Qui la resa giusta e' «sale», che e' quella della
coppia vera. 💡 Ogni oggetto il cui nome inglese si spezza in due produrra' la
stessa segnalazione: e' un artefatto del sorgente, non un'incoerenza.

Tetto 46 caratteri (`:1999`, coi tag contati). Cinque copie di giapponese e due
di inglese trovate da `dossier.py`, tutte usate.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1796-:1840 i dodici elementi. ⭐ i nomi vengono da action.hsp:6918-:7044,
    #     le ventiquattro righe di «Add X Resistance» / «Add X Damage».
    (1796, 'Physical damage'):
        'Attacchi fisici',
    (1800, 'Fire damage'):
        'Attacchi di fuoco',
    (1804, 'Cold damage'):
        'Attacchi di gelo',
    (1808, 'Lightning damage'):
        'Attacchi di fulmine',
    (1812, 'Darkness damage'):
        'Attacchi di oscurità',
    (1816, 'Mind damage'):
        'Attacchi mentali',
    (1820, 'Poison damage'):
        'Attacchi di veleno',
    (1824, 'Nether damage'):
        "Attacchi dell'oltretomba",
    (1828, 'Sound damage'):
        'Attacchi di suono',
    (1832, 'Nerve damage'):
        'Attacchi ai nervi',
    (1836, 'Chaos damage'):
        'Attacchi caotici',
    (1840, 'Magic damage'):
        'Attacchi di magia',

    # --- :1844-:1864 i sei stati che subisce.
    (1844, 'Confuse status'):
        'Confusione',
    (1848, 'Blind status'):
        'Cecità',
    # ⭐ «Terrore» e «Sonno» sono le etichette di text.hsp:100 e :95
    (1852, 'Fear status'):
        'Terrore',
    (1856, 'Sleep status'):
        'Sonno',
    (1860, 'Paralyze status'):
        'Paralisi',
    (1864, 'Poison status'):
        'Avvelenamento',

    # --- :1884-:1900 le cinque cose fisiche.
    # ⭐ copiata: 「酸」 e' gia' «l'acido» a proc.hsp:22094
    (1884, 'Acid'):
        "l'acido",
    (1888, 'Bleeding'):
        'Sanguinamento',
    (1892, 'Trap'):
        'Trappole',
    (1896, 'Invisible enemy'):
        'Nemici invisibili',
    (1900, 'Parasite'):
        'Parassiti',

    # --- :1904-:1920 i cinque scherzi: paure legate a un CREATURE_ID preciso.
    #     ⭐ tutti e cinque i nomi vengono dal progetto, articolo compreso.
    (1904, 'Puff puff bread'):
        'pane soffice',
    (1908, 'Salt'):
        'sale',
    (1912, 'Yeek'):
        'lo yeek',
    (1916, 'Cat'):
        'il gatto',
    (1920, 'Shark'):
        'lo squalo',

    # --- :1928 il titolo della finestra.
    (1928, 'In the heart'):
        'Dentro il cuore',

    # --- :1985, :1999 le due intestazioni di *com_knowSelf.
    # ⚠️ il giapponese ha name(tc) e l'inglese no: la resa non puo' nominare
    #    nessuno, e il soggetto puo' essere un alleato invece del giocatore.
    # 💡 l'asterisco torna DENTRO <title1>, dove :1999 e il giapponese lo mettono
    (1985, '*<title1> Your bonuses and penalties.<def>\\n'):
        '<title1>*Effetti in corso<def>\\n',
    (1999, '<title1>*Effects of Blessings and Hexes<def>\\n'):
        '<title1>*Benedizioni e maledizioni<def>\\n',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-012.jsonl'
DA, A = 1796, 1999
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
