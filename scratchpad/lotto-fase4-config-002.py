# -*- coding: utf-8 -*-
"""`config.hsp` si chiude: i 74 valori del pannello delle opzioni.

`config.hsp:751`-`:1046`, cioe' la colonna di destra — quel che il pannello
scrive accanto a ogni voce — piu' le due note in fondo. Con questo lotto
`config.hsp` e' **chiuso** per il referto del dizionario: 219 `lang()`, 160
firme, 160 rese.

Il tetto della colonna dei valori e' **15 caratteri**: il valore comincia a
`wx + 250` e la freccia destra sta a `wx + 358` (`config.hsp:743`, `:747`), a
7 px per carattere. Vedi il lotto 001 per come si e' misurato.

⚠️ **L'inglese lo sfora**: «Show All in Town» ha 16 caratteri. La resa
«Tutti in citta'» ne ha 15 esatti.

## ⚠️ Una firma sola serve dieci righe

`estrai.py --da-tradurre` da' **una voce per firma**, e le coppie
「しない」/「する」 → «No»/«Yes» compaiono a `:823`, `:827`, `:831`, `:861`,
`:865`, `:869`, `:878`, `:890`, `:898` e `:902`. Una resa sola le copre tutte,
e per questo deve funzionare in tutte: e' il motivo per cui 「なし」/«Don't
show» e' «No» e non «Nessuna» — la stessa firma serve l'interruttore della
guida (`:751`), le tre statistiche (`:783`), i cinque numeri di danno
(`:981`-`:994`) e i nomi dei PNG (`:1006`).

## ⚠️ Le quattro volte che l'inglese di monte e' peggio del giapponese

1. `:799` **確認なし** e' «nessuna conferma»; l'inglese scrive «Don't Use», che
   dice un'altra cosa — non si smette di usare i punti di viaggio, si smette di
   essere interrotti. `main.hsp:8470` lo conferma: `cfg_travelexp_select == 0`
   apre la domanda, l'altro valore la salta. Reso «Non chiedere».
2. `:894` **省略** e' «si salta»; l'inglese scrive «Highest», che continua la
   scala di velocita' invece di dire che il turno automatico non si vede piu'.
   Reso «Immediato», che tiene la scala e dice il fatto.
3. `:851` il giapponese mette la ragione fra parentesi — 「なし（高速）」,
   「あり（低速）」 — e l'inglese la copia stretta, «No(Fast)». La resa tiene la
   parentesi con lo spazio: «No (veloce)», «Si' (lento)».
4. `:1046` il giapponese ha **tre** righe e l'inglese due: quella che manca dice
   che le voci con (L) e (R) servono a cambiare linguetta nei menu, che e'
   l'unica ragione per cui quelle due voci hanno un suffisso. La resa tiene le
   tre righe.

## ⚠️ Cinque valori con lo stesso giapponese e cinque inglesi diversi

`:944` e' 「表示」 cinque volte, e l'inglese ci mette `Capitalize`, `Uppercase`,
`Lowercase`, `Spongebob`, `Schizophrenic`: sono i cinque modi di scrivere i nomi
degli oggetti nel registro (`cfg_capitalizeItemName`). Qui **l'inglese sa di
piu'** e si segue lui — il giapponese dice soltanto «si mostra». La rete 4 non
le ferma perche' dalla 57a la sua chiave porta anche l'inglese.

⚠️ La voce di menu che governa questi cinque valori e' uno dei due **letterali
nudi** di `:618` (`"Capitalize item names"`), e non sta in nessun lotto: vuole
una toppa. Vedi `scratchpad/nudi_accanto_a_lang.py`.

## Il vocabolario, e da dove viene

    Agita               道具を振る / «Zap», da text.hsp:135
    Identifica          道具を調べる / «Identify», da text.hsp:135 e skill.hsp:464
    al gancio           吊るし, da command.hsp:6608 «Finche' sta al gancio» —
                        l'inglese scrive «Sandbag», che e' l'oggetto e non il
                        gancio: qui il gioco controlla CHARA_BIT_SANDBAG, cioe'
                        una creatura appesa, non il sacco da boxe di db_item
    Bestie / Alleati    ペット e 味方, da db_card.hsp:13779 («arena delle
                        bestie») e dal glossario
    Direct sound        invariato: e' il nome del driver audio, come MCI
    Direct music        invariato, per la stessa ragione
    Spongebob           invariato: e' il nome del modo, una citazione
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :751 la guida di Norne. ⚠️ Questa firma serve anche :783, :981-:994,
    #     :1006, :1010 e :1015: la resa deve reggere in tutti e sei i posti.
    (751, "Don't show"): 'No',
    (751, 'Show'): 'Sì',

    # --- :755 i PNG neutrali. 「しない」 vuol dire «non ignorare», cioe'
    #     attaccare: il giapponese nega la voce, l'inglese dice l'atto.
    (755, 'Attack'): 'Attacca',
    (755, 'Ignore'): 'Ignora',

    # --- :759 il tasto z.
    (759, 'Quick menu'): 'Menu rapido',
    (759, 'Zap'): 'Agita',
    (759, "Don't assign"): 'Nessuno',

    # --- :763 il tasto x.
    (763, 'Quick Inv'): 'Zaino rapido',
    (763, 'Identify'): 'Identifica',

    # --- :767 i passi prima di correre: 「走らない」 e' il valore 20, cioe' mai.
    (768, "Don't run"): 'Mai',
    # ⚠️ Dinamica: il numero e' `cfg_startrun + 1` e arriva a 20 — «Dopo 20
    #    passi» sta in 13 caratteri. L'inglese scrive «After 3 steps».
    (772, 'After  steps'): '"Dopo " + (cfg_startrun + 1) + " passi"',

    # --- :783 le statistiche della scheda. Il primo valore e' la firma di :751.
    (783, 'Show'): 'In parte',
    (783, 'Show Max'): 'Tutte',

    # --- :787 la voce «Attacca» nel menu di chi si punta.
    (787, 'Show'): 'Sempre',
    (787, 'Neutral'): 'Non alleati',
    (787, "Don't show"): 'Mai',

    # --- :791 lo sterco.
    (791, 'No Block'): 'No',
    (791, 'Block'): 'Sì',

    # --- :795 l'animazione delle mosse di barra. ⚠️ Il primo valore (全表示 /
    #     «Show») ha la stessa firma di :787 e sta li': «Sempre» deve reggere
    #     tutt'e due i posti, e per questo qui il secondo e' «Mai» e non «No».
    (795, "Don't show"): 'Mai',

    # --- :799 la domanda sul riordino dei punti di viaggio.
    (799, 'Confirm'): 'Chiedi',
    (799, "Don't Use"): 'Non chiedere',

    # --- :805 e :809 i driver audio. I nomi restano: sono quelli che si
    #     scrivono in config.txt, e MCI accanto a loro non e' nemmeno in lang().
    (805, 'None'): 'Nessuno',
    (805, 'Direct sound'): 'Direct sound',
    (809, 'Direct music'): 'Direct music',

    # --- :813 il modo schermo.
    (813, 'Window mode'): 'Finestra',
    (813, 'Full screen'): 'Schermo intero',

    # --- :823 la coppia generica しない/する. ⚠️ Serve dieci righe: :823, :827,
    #     :831, :861, :865, :869, :878, :890, :898, :902.
    (823, 'No'): 'No',
    (823, 'Yes'): 'Sì',

    # --- :835 il battito cardiaco.
    (835, "Don't play"): 'No',
    (835, 'Play'): 'Sì',

    # --- :839 l'animazione degli attacchi.
    (839, 'No'): 'Nessuna',
    (839, 'Only PC'): 'Solo tu',
    (839, 'Only Ally'): 'Solo alleati',
    (839, 'All'): 'Tutti',

    # --- :843 gli effetti del tempo.
    (843, 'No animation'): 'Nessuna',
    (843, 'Always'): 'Sempre',

    # --- :847 la qualita' delle luci.
    (847, 'High'): 'Alta',
    (847, 'Low'): 'Bassa',

    # --- :851 le ombre degli oggetti: il giapponese mette la ragione fra
    #     parentesi, e la resa la tiene.
    (851, 'No(Fast)'): 'No (veloce)',
    (851, 'Yes(Slow)'): 'Sì (lento)',

    # --- :855 la dimensione del PCC.
    (855, 'Full-size'): 'Originale',
    (855, 'Reduced'): 'Ridotta',

    # --- :882 l'acqua nel titolo.
    (882, 'No'): 'No',
    (882, 'Yes'): 'Sì',

    # --- :894 il turno automatico. 「省略」 e' «si salta», non «piu' veloce di
    #     tutte»: la resa dice il fatto e tiene la scala.
    (894, 'Normal'): 'Normale',
    (894, 'High'): 'Veloce',
    (894, 'Highest'): 'Immediato',

    # --- :902 il danno nel registro, terzo valore. 吊るし e' il gancio a cui si
    #     appende una creatura (CHARA_BIT_SANDBAG), non il sacco da boxe.
    (902, 'Sandbag'): 'Solo al gancio',

    # --- :911 il gamepad.
    (911, "Don't use"): 'No',
    (911, 'Use'): 'Sì',

    # --- :916 e :919 i tasti del gamepad. ⚠️ «Tasto » porta lo spazio perche'
    #     il numero si attacca subito dopo: `mes lang(...) + list(1, cnt)`.
    (916, 'Unassigned'): 'Non assegnato',
    (919, 'Button'): 'Tasto ',

    # --- :925 la coppia 非表示/表示. Serve :925, :932, :936, :940.
    (925, 'No'): 'No',
    (925, 'Yes'): 'Sì',

    # --- :944 i cinque modi di scrivere i nomi degli oggetti. Qui l'inglese sa
    #     di piu': il giapponese dice 「表示」 cinque volte.
    (944, 'Capitalize'): 'Iniziali',
    (944, 'Uppercase'): 'MAIUSCOLO',
    (944, 'Lowercase'): 'minuscolo',
    (944, 'Spongebob'): 'Spongebob',
    (944, 'Schizophrenic'): 'Schizofrenico',

    # --- :956 la raccolta automatica.
    (956, 'Disable'): 'No',
    (956, 'Enable'): 'Sì',

    # --- :960 la coppia なし/あり dei suoni. Serve :960, :964, :968.
    (960, 'Off'): 'No',
    (960, 'On'): 'Sì',

    # --- :977 i numeri di danno.
    (977, 'Off'): 'No',
    (977, 'On'): 'Sì',

    # --- :1006 i nomi dei PNG. «Tutti in citta'» ha 15 caratteri esatti dopo la
    #     degradazione, cioe' il tetto: l'inglese qui ne ha 16 e sfora.
    (1006, 'Show in Town'): 'In città',
    (1006, 'Show All in Town'): 'Tutti in città',
    (1006, 'Show All'): 'Tutti',

    # --- :1010 la barra HP. Il gioco distingue le bestie del giocatore dagli
    #     alleati in genere: `cfg_showPetHealth` vale 1 per le prime, 2 per tutti.
    (1010, 'Show pet'): 'Bestie',
    (1010, 'Show allies'): 'Alleati',

    # --- :1017 e :1021 i due suffissi numerici: il numero sta davanti.
    (1017, ' rows'): ' righe',
    (1021, ' turns'): ' turni',

    # --- :1038 e :1046 le due note in fondo al pannello, carattere piu' piccolo
    #     e 54 caratteri per riga.
    (1038, 'Items marked with * require a restart to apply changes.'):
        'Le voci con * si applicano dopo il riavvio del gioco.',
    # ⚠️ Tre righe come il giapponese, non due come l'inglese: la terza dice a
    #    che cosa servono i suffissi (L) e (R), che altrimenti non si spiegano.
    (1046, 'To assign a button, move the cursor to\\nan item and press the button.'):
        'Per assegnare un tasto, scegli la voce e premi\\n'
        'il tasto sul gamepad. Le voci con (L) e (R)\\n'
        'servono a cambiare linguetta nei menu.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-config-002.jsonl'
DA, A = 701, 1046
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\config.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_config.jsonl', encoding='utf-8') if l.strip()]
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
