# -*- coding: utf-8 -*-
"""`config.hsp` si apre: le 86 etichette del pannello delle opzioni.

`config.hsp:580`-`:681`, cioe' il nome del pannello, i nove nomi di sezione e
tutte le voci delle nove sottosezioni. I valori accanto a ogni voce (`Show`,
`Don't show`, `Yes`, `No`...) stanno nel lotto 002.

⚠️ **Il file non aveva dizionario**: 219 `lang()` che nessun conteggio guardava.
E' la regola della 54a — «un file senza file di dizionario non e' un file
finito: e' un file che nessun conteggio guarda» — e con questo lotto
`config.hsp` entra nel referto.

## I due tetti, misurati nel disegnatore e non stimati

`cs_list` (`module.hsp:70`-`:130`) disegna l'etichetta e dichiara da se' quanto
misura un carattere:

    locvar_cs_list_tx = limit(strlen(cs_list_arg1) * 7 + 32 + cs_list_arg5, 10, 480)

**7 px per carattere**, e non e' una stima: il carattere inglese e' `Courier
New` (`config.txt`, `font2.`), monospaziato, e `config.hsp:716` lo chiede a
`14 - en * 2` = **12**. A 12 px di corpo il passo del Courier e' 0,6 em = 7,2 px,
cioe' i 7 che il sorgente scrive. ⚠️ E' lo stesso 7 della 59a, di nuovo
confermato: il 7,7 di `larghezze.py` viene da un altro carattere.

I due confini stanno nel disegnatore del pannello (`config.hsp:738`-`:747`):

    cs_list s, wx + 56 + x, ...      l'etichetta comincia a wx + 60 (+4 di cs_list)
    pos wx + 220 : gcopy ...         la freccia sinistra
    pos wx + 250 : mes s(...)        il valore
    pos wx + 358 : gcopy ...         la freccia destra

    etichetta   (220 - 60) / 7 = 22 caratteri
    valore      (358 - 250) / 7 = 15 caratteri     <- lotto 002

⚠️ **`mes` non taglia e non manda a capo**: quel che sfora finisce *sopra* la
freccia e poi sopra il valore. E' la stessa forma di `command.hsp:8186` nella
59a, dove l'eccedenza si stampava sopra la mappa.

⚠️ **L'inglese non e' il tetto, e qui sfora due volte**: «Block defecate
generation» ha 25 caratteri in un riquadro da 22, e «Show All in Town» ne ha 16
in uno da 15 (lotto 002). La resa italiana sta dentro tutt'e due.

💡 **L'elenco delle sezioni ha un riquadro suo**: `dx = 370` invece di 440
(`:583`), e li' non ci sono ne' frecce ne' valore — la voce arriva fino al bordo.
Per questo «Impostazioni extra 2 (schermo)» puo' avere 30 caratteri: la
linguetta del titolo cresce da sola (`module.hsp:4328`,
`limit(strlen(s) * 8 - 120, 0, 200)`).

## ⚠️ Due voci di questo menu NON sono in questo lotto, e non e' un rinvio

`:618` ha sei voci, e due sono letterali inglesi **nudi**, senza `lang()`:
`"  Display log instead*"` e `"Capitalize item names"`. Il dizionario non le
raggiunge e vogliono una toppa. Le ha trovate `scratchpad/nudi_accanto_a_lang.py`,
scritto oggi: e' il **dodicesimo punto cieco**, e nasce dal fatto che
`nudi_en.py` salta la riga intera appena ci legge un `lang(`.

## Il vocabolario fissato qui, e da dove viene

    PNG                 gia' 5 volte in command.hsp, mai «NPC»
    Norne               la guida, da db_creature.hsp:77957 — il giapponese
                        nomina il personaggio, l'inglese scrive «Extra Help»
    sterco              shit, da db_item.hsp:144913 — 汚物 non era mai stato reso
    barra               ゲージ技, «mossa di barra» da proc.hsp:12899
    malocchio           hex, dal glossario (⚠ non «maledizione», che e' curse)
    Alleato             ally, dal glossario
    Bersaglio / Tiro    da text.hsp:135 e :136, le due etichette gia' rese
    Schivata            da command.hsp:10732 («Schiv.», abbreviata li' per posto)
    Zaino               inventory, da command.hsp:12929 «Il tuo zaino e' pieno»
    Scheda              la linguetta di module.hsp:5148, per «Chara-sheet»
    Registro            la linguetta di module.hsp:5158, per «Log»
    Voce                項目, come «Category» e «Part» in command.hsp

## ⚠️ Le tre volte che il giapponese dice piu' dell'inglese

1. `:588` **ノルンの冒険ガイド** nomina Norne; l'inglese scrive «Extra Help» e
   perde chi parla. La guida in gioco e' scritta in prima persona da lei
   (`data/exhelp.txt`): la resa tiene il nome.
2. `:588` **汚物生成の阻止** dice che cosa si blocca (lo sterco); «Block defecate
   generation» dice l'atto. In italiano si nomina la cosa, come il giapponese.
3. `:606` **オートターンの挙動** dice «comportamento», l'inglese «Auto Turn
   Speed». I valori sono 普通 / 速め / 省略, che sono tre velocita': qui
   l'inglese ha ragione sul contenuto e il giapponese sulla forma, e la resa
   sta col giapponese perche' l'etichetta e' un sostantivo.

## ⚠️ E la volta che lo stesso giapponese vale due voci diverse

**ダメージ表示** compare a `:606` (inglese «Damage show») e a `:636` (inglese
«Damage Popups»), e sono **due impostazioni diverse**: la prima e' `cfg_dhyouji`,
che scrive il danno fra parentesi **nel registro** (`chara_func.hsp:6006`,
`:8020`); la seconda e' `cfg_dmgpopups`, i numeri che volano sopra il bersaglio.
Le rese devono differire, e la rete 4 non le ferma perche' l'inglese e' diverso.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :580 il nome del pannello.
    (580, 'Option'): 'Opzioni',

    # --- :581 le nove sezioni. Riquadro da 370 e nessuna freccia: qui il tetto
    #     e' il bordo, non i 22 caratteri delle voci.
    (581, 'Game Setting'): 'Impostazioni di gioco',
    (581, 'Screen & Sound'): 'Schermo e audio',
    (581, 'Network Setting'): 'Impostazioni di rete',
    (581, 'Detailed Setting'): 'Impostazioni avanzate',
    (581, 'Game Pad'): 'Gamepad',
    (581, 'Message & Log'): 'Messaggi e registro',
    # ⚠️ Il giapponese scrive 言語(Language) apposta: chi ha sbagliato lingua non
    #    sa leggere l'etichetta, e la parola inglese e' il modo di ritrovarla.
    #    La resa tiene lo stesso servizio.
    (581, 'Language'): 'Lingua (Language)',
    (581, 'EX Setting 1'): 'Impostazioni extra 1',
    (581, 'EX Setting 2 (Display)'): 'Impostazioni extra 2 (schermo)',

    # --- :588 «Impostazioni di gioco», dodici voci. Tetto 22.
    (588, 'Extra Help'): 'Guida di Norne',
    (588, 'Neutral Npcs'): 'Ignora PNG neutrali',
    (588, 'Assign z key'): 'Assegna tasto z',
    (588, 'Assign x key'): 'Assegna tasto x',
    (588, 'Start Running After'): 'Passi prima di correre',
    (588, 'Walk Speed'): 'Velocità camminata',
    (588, 'Attack Interval'): 'Intervallo attacchi',
    # `cfg_record` accende la sezione « - Records of Adventure - » della scheda
    # (command.hsp:2951): livello piu' profondo, uccisioni, miglia, incarichi.
    (588, 'Record'): 'Mostra le statistiche',
    # La voce «Attacca» dentro il menu che si apre puntando qualcuno
    # (command.hsp:5954): si mostra sempre, solo sui non alleati, o mai.
    (588, 'Attack Select'): 'Opzione Attacca',
    (588, 'Block defecate generation'): 'Blocca lo sterco',
    (588, 'Gauge-Action Animation'): 'Animazione barra',
    # La domanda «vuoi mettere in ordine i punti di viaggio?» (main.hsp:8470).
    (588, 'TravelExp Confirmation'): 'Conferma riordino',

    # --- :594 «Schermo e audio», quattordici voci. Tetto 22.
    (594, 'Sound*'): 'Effetti sonori*',
    (594, 'Music*'): 'Musica*',
    (594, 'Screen Mode*'): 'Modo schermo*',
    (594, 'Screen Resolution*'): 'Risoluzione*',
    (594, 'High DPI Scaling*'): 'Scala DPI elevati*',
    (594, 'High DPI Smoothing*'): 'Smussatura DPI*',
    (594, 'Smooth Scroll'): 'Scorrimento fluido',
    (594, 'Always Center'): 'Centra sul giocatore',
    (594, 'Heartbeat Sound'): 'Battito cardiaco',
    (594, 'Attack Animation'): 'Animazione attacchi',
    (594, 'Weather Effect'): 'Effetti del tempo',
    # 光源の描写 e' il disegno delle sorgenti di luce, e i valori sono 高画質 /
    # 低画質: e' una scelta di qualita', non un interruttore.
    (594, 'Lighting'): 'Qualità delle luci',
    (594, 'Object Shadow'): 'Ombre degli oggetti',
    # I valori sono 原寸表示 / 縮小表示, cioe' due misure: PCC resta sigla.
    (594, 'PCC show'): 'Dimensione PCC',

    # --- :600 «Impostazioni di rete», tre voci. Tetto 22.
    (600, 'Use Network'): 'Usa la rete',
    (600, 'Constantly Connect'): 'Connessione periodica',
    (600, 'Filter Chat'): 'Filtra la chat',

    # --- :606 «Impostazioni avanzate», nove voci. Tetto 22.
    (606, 'Run Speed'): 'Velocità di corsa',
    (606, 'Auto Numlock'): 'Numlock automatico',
    (606, 'Title Water Effect'): 'Acqua nel titolo',
    (606, 'Screen Refresh'): 'Frequenza schermo',
    (606, 'Scroll When Run'): 'Scorrimento in corsa',
    (606, 'Auto Turn Speed'): 'Turno automatico',
    (606, 'Skip Random Events'): 'Eventi abbreviati',
    # ⚠️ `cfg_dhyouji` scrive «(37)» NEL REGISTRO (chara_func.hsp:6006). L'altra
    #    ダメージ表示, a :636, sono i numeri che volano sopra il bersaglio.
    (606, 'Damage show'): 'Danni nel registro',
    (606, 'Effect Speed'): 'Velocità effetti',

    # --- :612 «Gamepad», tredici voci. Tetto 22.
    #     La prima (ゲームパッド) ha la stessa firma di :581 e sta li'.
    (612, 'Enter/Ok'): 'Conferma',
    (612, 'Cancel'): 'Annulla',
    (612, 'Inventory'): 'Zaino',
    (612, 'Action'): 'Azione',
    (612, 'diagonal Move/(L)'): 'Diagonale (L)',
    (612, 'Pick/(R)'): 'Raccogli (R)',
    (612, 'Shoot/(R)'): 'Tiro (R)',
    (612, 'Target/(L)'): 'Bersaglio (L)',
    (612, 'Pause/Menu'): 'Menu di pausa',
    (612, 'Help'): 'Aiuto',
    (612, 'Chara-sheet'): 'Scheda',
    (612, 'Reload'): 'Ricarica',

    # --- :617/:618 «Messaggi e registro». ⚠️ Due delle sei voci sono nude e
    #     vogliono una toppa: vedi il docstring.
    (617, 'Message&Log'): 'Messaggi e registro',
    (618, 'Add time info'): 'Ora nel registro',
    # Il valore e' una percentuale (`cfg_msgtrans * 10 + " %"`, :929).
    (618, 'Transparency'): 'Trasparenza',
    (618, 'Disclaimer at startup'): "Avviso all'avvio",
    (618, 'Control Help*'): 'Guida ai comandi*',

    # --- :624 «Lingua». L'asterisco vuole il riavvio.
    (624, 'Language*'): 'Lingua*',

    # --- :630 «Impostazioni extra 1», cinque voci. Tetto 22.
    (630, 'Auto pickup & destroy'): 'Raccolta e distruzione',
    (630, 'Autopick sound'): 'Suono raccolta',
    (630, 'Autodestroy sound'): 'Suono distruzione',
    # MMAH e TCG sono sigle del mod e restano: nominano da dove viene la voce.
    (630, '(MMAH) Mouse Control'): '(MMAH) Mouse esteso',
    (630, '(TCG) Effect Speed'): '(TCG) Velocità',

    # --- :636 «Impostazioni extra 2 (schermo)», quattordici voci. Tetto 22.
    # ⚠️ Le tredici rientrate cominciano con DUE SPAZI normali, come l'inglese:
    #    il giapponese usa uno spazio a doppia larghezza (U+3000), che in CP932
    #    starebbe su due byte e la build inglese disegnerebbe due glifi.
    (636, 'Damage Popups'): 'Numeri di danno',
    (636, '  Hexes/Buffs'): '  Buff e malocchi',
    (636, '  Ailments'): '  Alterazioni',
    (636, '  Evade'): '  Schivate',
    (636, '  Chat'): '  Dialoghi',
    (636, '  Font Size'): '  Dim. carattere',
    (636, '  Font Shift'): '  Scarto carattere',
    # 表示速度 dice «velocita'», l'inglese «Duration»: e' il tempo che il numero
    # resta a schermo, e li' l'inglese e' quello giusto.
    (636, '  Display Duration'): '  Durata',
    (636, '  Show NPC Name'): '  Nomi dei PNG',
    (636, '  Show Pet HP gauge'): '  Barra HP bestie',
    (636, '  Show Damage Meter'): '  Misura danni',
    (636, '  Meter Duration Turns'): '  Turni misurati',
    (636, '  Extra UI Auto Hide'): '  Nascondi UI',
    (636, '  Multi-lined Name/Chat'): '  Nome/chat multiriga',

    # --- :681 l'intestazione della colonna, sopra l'elenco.
    (681, 'Menu'): 'Voce',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-config-001.jsonl'
DA, A = 580, 700
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
