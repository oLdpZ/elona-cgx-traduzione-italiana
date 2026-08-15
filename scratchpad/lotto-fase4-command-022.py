# -*- coding: utf-8 -*-
"""Lotto `command-022`: i rifiuti, l'uscita dal gioco e il menu personalizzato.
Prima meta' della zona 17000-17999.

Sono le frasi che il gioco dice quando dice **di no** — «射撃用の道具を装備して
いない。», «ここではセーブできない。» — piu' la schermata che si apre premendo
`Esc` e il menu `[Customize Menu]` con cui si registrano l'area, la squadra e i
PNG personalizzati.

⭐⭐ **Nove rese su quarantasei erano gia' scritte altrove, e `dossier.py` le ha
pescate tutte.** «Se non indebolisci <Il Figlio del Caos>, uscira' dal Sigillo
Eterno!» (`action.hsp:3008`), «Non e' il momento di mollare. Finiamola qui.»
(`:3013`), «L'aria intorno comincia a vibrare.» (`proc.hsp:14533`), «Uscendo
adesso, la missione di questo piano non si potra' piu' completare...»
(`:14537`), «Non si puo' usare in quest'area.» (due file), «Devi equipaggiare le
munizioni.» (`proc.hsp:26940`), «Annulla», «Normali», «Illimitate». ⚠️ Sono
**scene duplicate**, non frasi generiche: `command.hsp` e `proc.hsp` hanno due
copie dello stesso comando di ritorno.

⚠️⚠️ **E proprio li' c'e' un errore di monte nuovo, che il gemello rende
visibile.** `:17367` e `proc.hsp:14527` hanno l'inglese **identico** — «Returning
while taking a quest is forbidden. Are you sure you want to return?» — ma il
giapponese distingue: `:14527` e' 「脱出」 (la **fuga**, l'incantesimo Escape) e
`:17367` e' 「帰還」 (il **ritorno**, l'incantesimo Return). Sono due comandi
diversi con due tasti diversi, e l'inglese li appiattisce sullo stesso «return».
✅ La resa italiana li separa — «Fuggire…» resta a `proc.hsp`, qui si scrive
«Tornare indietro…» — ed e' una divergenza voluta, non una svista: la rete 13 la
segnalera' come referto e ha ragione a farlo.
💡 **Il dossier serve a copiare, ma qui e' servito a distinguere**: senza il
gemello non avrei mai guardato il giapponese di una frase che l'inglese dava per
identica.

⚠️⚠️ **La rete 6 ha bocciato cinque righe e su due sbagliava lei — ed e' la
QUARTA rete che si corregge.** Il menu dell'uscita esiste in due copie: l'
`ORIGINAL` che il mod ha spento (`:17281`-`:17311`) e il blocco
`ANNA/BLOODYSHADE CUSTOM` che gira davvero (`:17313`-`:17339`). Cinque voci hanno
l'ancora nel primo, ma **due di esse rivivono nel secondo**: 「ゲーム設定」 sta a
`:17285` e a `:17316`, 「無事に記録された。」 a `:17296` e a `:17330`. Rinviarle
avrebbe lasciato inglese un menu che il giocatore apre a **ogni uscita dal
gioco**.
✅ La causa e' la stessa scoperta 4 della 43ª — `estrai --da-tradurre` da' una
voce per firma e la ancora alla **prima** occorrenza — vista qui dal lato della
guardia: la rete guardava la riga d'ancoraggio invece della firma.
⭐ **Misurato prima di toccarla**, com'e' d'obbligo: su tutto il sorgente **36
firme** toccano un blocco spento, **28 sono spente del tutto** (e li' la rete
aveva ragione) e **8 sono miste**, sette delle quali con l'ancora nella riga
morta. Ventotto contro otto: la rete resta, cambia solo che ora guarda **tutte**
le occorrenze e boccia se sono spente tutte. Il modello nuovo e'
`scratchpad/modello-rete6.py`.
✅ Rinviate le tre che sono morte davvero: `:17283` 「はい」, `:17284` 「いいえ」,
`:17297`.

⚠️ **`:17297` e `:17331` hanno `name(cc)` nel GIAPPONESE e non nell'inglese**, e
il tipo estratto e' `statica`: la rete 11 pretende le funzioni dell'inglese, che
sono zero, quindi il soggetto non si puo' nominare nemmeno volendo. ✅ «Gli occhi
si chiudono» — il soggetto sono gli occhi, e l'italiano non chiede altro.

💡 **Due «Exit» con due rese, ed e' giusto**: `:17283` e' 「はい」 dentro un
si'/no («Esci»), `:17315` e' 「ゲームをやめる」 in un menu («Esci dal gioco»).
L'inglese scrive «Exit» tutt'e due le volte.

⚠️ **`:17515` dice «wizard mode» e il giapponese dice 「デバッグモード」**: la resa
segue il giapponese — «modalita' debug» — che e' anche l'unica delle due in
italiano. Nessun file del progetto aveva ancora reso quel termine.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :17014-:17026 i tre rifiuti del tiro.
    (17014, 'You need to equip a firing weapon.'):
        'Devi equipaggiare un\'arma da tiro.',
    (17020, 'You need to equip ammo or arrows.'):
        'Devi equipaggiare frecce o munizioni.',
    (17026, "You're equipped with wrong type of ammo."):
        'Le munizioni equipaggiate non sono adatte.',
    (17156, "It's not possible on the world map."):
        'Sulla mappa del mondo non si può.',

    # --- :17267 l'interruzione di un'azione in corso. ⚠️ dinamica: `actlistn`
    #     dà il nome dell'azione, senza articolo.
    (17267, 'Do you want to cancel ? '):
        '"Interrompere " + actlistn(cdata(CDATA_ROW_ACT, cc)) + "? "',

    # --- :17275-:17318 l'uscita dal gioco.
    (17275, "You can't save the game here. Exit anyway?"):
        'Qui non si può registrare. Uscire lo stesso?',
    (17278, 'Do you want to save the game and exit?'):
        "Registrare l'avventura e uscire?",
    # ⭐ :17285 e :17296 hanno l'ANCORA nel blocco spento e rivivono nel blocco
    #   nuovo (:17316, :17330): si traducono. Vedi il docstring e la rete 6.
    (17285, 'Game Setting'): 'Impostazioni',
    (17296, 'Your game has been saved successfully.'):
        "L'avventura è stata registrata.",
    (17315, 'Exit'): 'Esci dal gioco',
    (17317, 'Tweaks'): 'Regolazioni',
    (17318, 'Cancel'): 'Annulla',
    # ⚠️ statica: il giapponese ha name(cc), l'inglese no, e la rete 11 pretende
    #    le funzioni dell'inglese. Il soggetto sono gli occhi.
    #    💡 la gemella :17297 ha i puntini di sospensione veri (…) invece dei tre
    #    punti: firma diversa, e sta tutta dentro il blocco spento. Rinviata.
    (17331, 'You close your eyes and peacefully fade away. (Hit any key to exit)'):
        'Gli occhi si chiudono, e tutto svanisce in pace. (premi un tasto per uscire)',

    # --- :17367 ⚠️ errore di monte: stesso inglese di proc.hsp:14527, ma là il
    #     giapponese è 「脱出」 (la fuga) e qui è 「帰還」 (il ritorno). Due comandi
    #     diversi che l'inglese appiattisce. La resa li separa.
    (17367, 'Returning while taking a quest is forbidden. Are you sure you want to return?'):
        'Tornare indietro mentre hai un incarico in corso è vietato dalla legge. Tornare lo stesso?',
    # ⭐ copiate da action.hsp:3008 e :3013
    (17376, 'If you do not weaken the <Chaos Child>, it will come out of the Eternal Seal!'):
        'Se non indebolisci <Il Figlio del Caos>, uscirà dal Sigillo Eterno!',
    (17382, "I shouldn't give up here. Let's finish this."):
        'Non è il momento di mollare. Finiamola qui.',

    # --- :17435-:17454 la lista dei luoghi di ritorno.
    #     ⚠️ 「階」 è il piano del sotterraneo; l'inglese abbrevia in « Lv».
    #     Il numero lo mette `cnvrank` due funzioni più in là.
    (17435, ' Lv'): ' piano',
    (17441, "You don't know any location you can return to."):
        'Non conosci nessun luogo dove poter tornare.',
    (17444, 'Where do you want to go?'): 'Dove vuoi tornare?',
    # ⭐ copiate da proc.hsp:14533 e :14537
    (17450, 'The air around you becomes charged.'):
        "L'aria intorno comincia a vibrare.",
    (17454, 'The lord of the dungeon might disappear if you escape now.'):
        'Uscendo adesso, la missione di questo piano non si potrà più completare...',

    # --- :17473-:17501 il gasha-gasha e il libro.
    #     ⚠️ `matname` non porta l'articolo: la frase gli si costruisce intorno.
    (17473, 'Pay  to gasha-gasha?'):
        '"Usare " + matname(tmat) + " per il gasha-gasha?"',
    (17493, "You don't have ."):
        '"Non hai " + matname(tmat) + "."',
    (17501, 'You are not interested in this book. Do you want to read it anyway? '):
        'Questo libro non ti interessa. Leggerlo lo stesso? ',

    # --- :17515-:17538 il menu personalizzato.
    #     ⚠️ il giapponese dice 「デバッグモード」, non «wizard».
    (17515, 'This function is disabled in wizard mode.'):
        'In modalità debug non funziona.',
    # ⭐ copiata da action.hsp:10848 e proc.hsp:14856
    (17521, "You can't use it in this area."): "Non si può usare in quest'area.",
    # ⭐ «team» è «squadra» in command.hsp:436 e :448
    (17528, 'Your initial team name is . You can change it any time.'):
        '"La squadra si chiama " + gdatan(GDATAN_TEAM1) + ". Puoi cambiarle nome quando vuoi."',
    (17531, '[Customize Menu] What do you want to do?'):
        '[Personalizzazione] Che cosa vuoi fare?',
    (17532, 'Save current area'): "Registra quest'area",
    (17533, 'Save your pet team'): 'Registra la squadra',
    (17534, 'Change your team name'): 'Cambia nome alla squadra',
    (17535, 'Make custom NPC'): 'Crea un PNG personalizzato',
    (17537, 'Upload'): 'Invia in rete',
    (17538, 'Setting'): 'Impostazioni',

    # --- :17548-:17635 il salvataggio dell'area e della squadra, l'invio.
    (17548, "You can't save this area."): "Quest'area non si può registrare.",
    (17552, 'Enter file name.'): 'Con che nome salvare?',
    (17563, 'Current area is saved to .'):
        '"L\'area è stata registrata in " + userfile + "."',
    (17567, 'Which members do you want to save?'): 'Quali compagni registrare?',
    (17608, 'Your team is saved to .'):
        '"La squadra è stata registrata in " + userfile + "."',
    (17617, 'Your team name is  now.'):
        '"Adesso la squadra si chiama " + gdatan(GDATAN_TEAM1) + "."',
    (17626, "You can't do it in this area."): "Non si può fare in quest'area.",
    (17630, 'You need to be at least level 10 to upload.'):
        "Per inviare serve almeno il livello 10.",
    (17635, "You can't do this till ."):
        '"Non prima del " + cnvdate(gdata(GDATA_NEXT_UPLOAD), 1) + "."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # Le tre voci del blocco ORIGINAL spento (:17281-:17311) che NON rivivono
    # nel blocco che il mod ha messo al suo posto. Le altre due — :17285 e
    # :17296 — hanno la stessa firma a :17316 e :17330 e si traducono.
    (17283, 'Exit'),
    (17284, 'Cancel'),
    (17297, 'You close your eyes and peacefully fade away. (Hit any key to exit)'),
}

USCITA = 'lavoro/fase4-command-022.jsonl'
DA, A = 17000, 17640
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
