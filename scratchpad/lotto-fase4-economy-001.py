# -*- coding: utf-8 -*-
"""`economy.hsp` si apre e si chiude: le 39 firme del governo della citta'.

Il prospetto cittadino, il bilancio, il giudizio dei cittadini, le leggi e la
costruzione degli edifici. `economy.hsp` non aveva dizionario, ed era anche uno
dei due file che `file_senza_dizionario.py` chiamava **mezzo tradotto**: una
toppa (`:778`, «k gp» -> «k oro») e nessun dizionario, cioe' una riga italiana
in un file che per il referto non esisteva. Adesso e' intero.

## ⚠️ Le colonne si allineano con gli SPAZI, e l'italiano ne conta di piu'

`economy.hsp:319`-`:365` scrive dodici righe fatte cosi':

    mes lang("...", "Water pollution     " + mdata(...) + " (dead " + ... )

L'etichetta e' **imbottita a 20 caratteri** e il numero comincia sempre alla
stessa colonna: e' un allineamento a mano, non una tabella. Le rese tengono i
20 caratteri, e per questo 発言力 diventa «Influenza» e non «Autorita'»:
⚠️⚠️ **un'etichetta con l'accento romperebbe l'allineamento**, perche' nel
dizionario si scrive «Autorità» (8 caratteri) e `applica` scrive «Autorita'»
(9). L'imbottitura andrebbe contata sulla forma degradata, cioe' su una cosa che
il file del dizionario non mostra. Meglio un sinonimo senza accento.

## Il tetto delle due leggi, letto dalla striscia e non dalla finestra

`economy.hsp:440`-`:441` sono due voci di `chatList`, e la rete 15 le pretende
misurate. La finestra e' larga 480 (`:458`), ma il confine vero e' la
**striscia** che il gioco disegna sotto le righe pari — `gfini 365, 18` da
wx+74 (`:494`-`:495`) — e la voce comincia a wx+104 (`:509` piu' i 4 di
`cs_list`). Sono **47 caratteri**, non 53.

⚠️ E il contenitore si chiama `*skip_rule`, che e' un'etichetta di salto: i due
`chatList` stanno sopra, il disegno sotto, e in mezzo c'e' un `goto`. E' il
quarto contenitore misurato dopo la pergamena, la finestra dell'evento e il
pannello degli dei.

## ⚠️ Due volte l'inglese di monte perde qualcosa

1. `:440` **perde il segno di percentuale.** Il giapponese scrive
   「この街の消費税は%だ。」, l'inglese «The consumption tax of this town is .»
   — e a schermo esce «...is 15.», un numero senza unita'.
2. `:327` **cambia l'ordine e perde la parola.** 「今までの死者N人」 e' «N morti
   fino a oggi»; l'inglese scrive «(dead N people)», che si legge come un
   aggettivo.

## Il vocabolario, e da dove viene

    oro                 gp / GP, gia' otto volte nelle toppe
    cgp                 resta: e' la valuta della citta' (city gold piece),
                        una sigla del gioco come GP
    Leggi               la linguetta di module.hsp:5163
    citta'              mdatan(MDATAN_NAME), come ovunque
    Prospetto           チャート: e' il quadro dello stato della citta',
                        non un grafico — quello e' la linguetta «Grafico»
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :64-:116 il prospetto della citta'.
    (64, 'City Chart'): 'Prospetto cittadino',
    (74, "There's no information in this area."):
        'Di questo posto non ci sono informazioni.',
    (83, ' City Chart'):
        '"Prospetto di " + mapname(adata(ADATA_ID, gdata(GDATA_AREA)))',
    # il posto vuoto nell'elenco delle cariche
    (116, 'Empty'): 'Vacante',

    # --- :285-:303 il giudizio dei cittadini, dal peggiore al migliore.
    #     Sono etichette di stato, quindi sostantivi: guida-stile.md.
    (285, '<Tax-Thief>'): '<Ladro di tasse>',
    (288, 'Disappointment'): 'Delusione',
    (291, 'No Voice Raised'): 'Perplessità',
    (294, 'No Opinion'): 'Indifferenza',
    (297, 'No Complaints'): 'Nessuna lamentela',
    (300, 'Role Model'): 'Modello di gestione',
    (303, '<the Hope of >'):
        '"<Speranza di " + mdatan(MDATAN_NAME) + ">"',

    # --- :309-:312 i tre titoletti del pannello.
    (309, 'Town Information'): 'Quadro generale',
    (310, 'Town Finance'): 'Finanze',
    (312, 'Administrator'): 'Amministratore',

    # --- :319-:365 le dodici righe del prospetto. ⚠️ L'etichetta e' imbottita a
    #     VENTI caratteri e il numero comincia sempre alla stessa colonna: e' un
    #     allineamento a mano. Niente accenti nelle etichette, o la degradazione
    #     ne aggiunge uno e la colonna si sposta.
    (319, 'Security           ()  '):
        '"Sicurezza          (" + mdata(MDATA_CITY_PROPERTY_VALUE) + ") " + s1 + " "',
    (323, 'Population           '):
        '"Popolazione         " + mdata(MDATA_MODERATE_CROWD) + " "',
    # ⚠️ 「今までの死者N人」 e' «N morti fino a oggi»; l'inglese scrive
    #    «(dead N people)», che si legge come un aggettivo.
    (327, 'Water pollution      (dead  people) '):
        '"Acque inquinate     " + mdata(MDATA_CITY_WATER_POLLUTION) '
        '+ " (morti finora: " + mdata(MDATA_CITY_DEAD_PEOPLE) + ") "',
    (331, 'Ether concentration  '):
        '"Etere nell\'aria     " + taiki + " "',
    (335, 'Tax                 % '):
        '"Tassa sui consumi   " + mdata(MDATA_CITY_TAXES) + "% "',
    (339, 'Tourism revenue      cgp '):
        '"Entrate dal turismo " + mdata(MDATA_CITY_TOURISM_REVENUE) + " cgp "',
    (343, 'Maintenance costs    cgp '):
        '"Costi di gestione   " + mdata(MDATA_CITY_MAINTENANCE_COST) + " cgp "',
    (347, 'Budget              gp '):
        '"Bilancio            " + mdata(MDATA_CITY_BUDGET) + "gp "',
    (353, 'Complaint            '):
        '"Lamentele           " + mdata(MDATA_CITY_COMPLAINTS) + " "',
    # ⚠️ «Influenza» e non «Autorita'»: un'etichetta con l'accento si allunga di
    #    un carattere dopo la degradazione e sposta la colonna.
    (357, 'Authority            '):
        '"Influenza           " + mdata(MDATA_CITY_AUTHORITY) + " "',
    (361, 'Approval rate       % '):
        '"Gradimento          " + imp + "% "',
    (365, 'Evaluation           '):
        '"Giudizio            " + s2 + " "',

    # --- :440-:441 le due leggi. Tetto 47 caratteri: la striscia della riga,
    #     non il bordo della finestra.
    # ⚠️ L'inglese perde il segno di percentuale che il giapponese ha: a schermo
    #    esce «...is 15.», un numero senza unita'.
    (440, 'The consumption tax of this town is .'):
        '"Qui la tassa sui consumi è del " + mdata(MDATA_CITY_TAXES) + "%."',
    (441, 'Allow murder in this town.'): 'Qui è permesso uccidere.',

    # --- :468-:475 le due colonne delle leggi. «Nazionale» sta nei cento pixel
    #     fra le due icone (wx+185 e wx+285, :471 e :474): quattordici caratteri.
    (468, 'Law'): 'Leggi',
    (472, 'Global'): 'Nazionale',
    (475, 'Law of '): '"Legge di " + mapname(gdata(GDATA_AREA))',

    # --- :636-:752 la costruzione degli edifici.
    (636, "The city can't hold any more building."):
        'Questa città non può ospitare altri edifici.',
    # ⚠️ Lo stesso giapponese e' gia' reso «Qui non si può costruire.» in
    #    map_user.hsp:60, e la resa si allinea: 「その場所」 e' «li'» piu' che
    #    «qui», ma per lo stesso giapponese due rese diverse sono un difetto
    #    piu' grosso della sfumatura che si guadagna.
    (643, "You can't build here."): 'Qui non si può costruire.',
    (652, 'This location is too far from the town.'):
        'Quel posto è troppo lontano dal centro abitato.',
    (686, 'What do you want to build?'): 'Che cosa vuoi costruire?',
    (689, 'Building List'): 'Elenco degli edifici',
    (746, "Your city can't afford it..."): 'Il bilancio non basta...',
    (752, 'You have built a !'):
        '"Hai costruito: " + bdrefn(p) + "!"',

    # --- :778 il bilancio in fondo alla finestra di costruzione.
    (778, 'Budget:'): 'Bilancio:',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-economy-001.jsonl'
DA, A = 0, 99999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\economy.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_economy.jsonl', encoding='utf-8') if l.strip()]
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
# vive. `event.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
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
# `event.hsp:13` compone la lista degli oggetti sulla casella con
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
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
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
