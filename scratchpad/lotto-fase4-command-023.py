# -*- coding: utf-8 -*-
"""Lotto `command-023`: il **rapporto del personaggio** e le munizioni.
Chiude la zona 17000-17999.

Il rapporto non e' una schermata: e' il **file di testo** che il gioco scrive
quando esporti il personaggio, e infatti si legge in un editor. Questo cambia
tutte le regole della larghezza.

⭐⭐ **Qui il tetto non e' in pixel, e' in CARATTERI — e non e' un tetto, e' una
misura esatta.** Le etichette si scrivono con gli spazi dentro la stringa
(«`Life      : `», «`Sanity    : `») per far cadere i due punti tutti sulla
stessa colonna: sono **dodici caratteri** ciascuna, e una resa di undici o
tredici storce la colonna di tutte le righe sotto. ✅ Le sedici rese del blocco
sono tutte di dodici: «Vita      : », «Follia    : », «Velocità  : »,
«Protezione: ». ⚠️ E' l'opposto del lavoro sui menu, dove il tetto e' un massimo
da non superare: qui **anche piu' corto e' sbagliato**.
💡 E per una volta l'italiano lungo non da' fastidio: «Schivata» e «Protezione»
si scrivono per intero, mentre nella scheda del personaggio (43ª) gli stessi due
termini erano dovuti diventare «Schiv.» e «Prot.» per stare in 43 e 46 px. La
stessa parola, tagliata dove taglia il sito e distesa dove il sito la lascia
stare.

⚠️ **Quattro etichette restano identiche all'inglese e vanno dichiarate**:
«`Mana      : `», «`Karma     : `», «`DV        : `», «`PV        : `». Le prime
due sono parole che il progetto tiene gia' invariate (`invariati.md`), le altre
due sono le sigle di difesa e protezione che ogni gioco di ruolo scrive cosi'.
✅ In `invariati.md` vanno **fra apici inversi**, perche' gli spazi di
allineamento fanno parte della stringa e `_valore_di_riga` legge verbatim solo
quel che sta fra i backtick — una previdenza scritta per `text.hsp:62` che qui
serve per la prima volta a quattro voci in un colpo.

⚠️ **Un errore di monte nuovo, e ha la forma piu' banale che ci sia**: `:17658`
scrive **«Elona Version 3.03»** come letterale, mentre il giapponese della stessa
riga usa `VERSION_STRING`. Il rapporto dichiara una versione fissa e sbagliata a
ogni esportazione. ⚠️ La resa **non lo puo' correggere**: aggiungere
`VERSION_STRING` vorrebbe dire aggiungere una funzione che l'inglese non ha, ed
e' la rete 11. Sta qui perche' qualcuno lo tolga con una toppa.

💡 **La data si gira, e le funzioni restano le stesse.** L'inglese scrive
`month + "/" + day + "/" + year`; l'italiano `day + "/" + month + "/" + year`.
La rete 11 confronta l'**insieme** delle funzioni di contenuto, non l'ordine (la
misura della 40ª), quindi riordinarle e' lecito — ed e' l'unico modo di scrivere
una data italiana.

⭐ Copiate senza decidere: «Devi equipaggiare le munizioni.» (`proc.hsp:26940`),
«Normali» e «Illimitate» (`action.hsp:15273`, `proc.hsp:26945`), e le nove
etichette che la scheda del personaggio aveva gia' — «Razza», «Fede», «Classe»,
«Gilda», «Livello», «Vita», «Velocità», «Fama», «Follia».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :17658 l'intestazione del rapporto.
    #     ⚠️ «Elona Version 3.03» è un letterale fisso dell'inglese, dove il
    #        giapponese usa VERSION_STRING: errore di monte che la resa non può
    #        correggere (sarebbe una funzione in più, ed è la rete 11).
    #     💡 la data si gira all'italiana: la rete 11 guarda l'insieme delle
    #        funzioni, non l'ordine.
    (17658, 'Elona Version 3.03 Character Report. Generated at : // in '):
        '"Elona Version 3.03 Scheda del personaggio. Generata alle " + gdata(GDATA_HOUR) + ":" '
        '+ gdata(GDATA_MIN) + " del " + gdata(GDATA_DAY) + "/" + gdata(GDATA_MONTH) + "/" '
        '+ gdata(GDATA_YEAR) + " a " + mdatan(MDATAN_NAME)',

    # --- :17660 la riga del personaggio.
    (17660, 'Name: Sex:    Age:  \\nHeight: cm   Weight: kg'):
        '"Nome: " + fixtxt("" + cdatan(CDATAN_AKA, CHARA_PLAYER) + cdatan(CDATAN_NAME, CHARA_PLAYER), 34) '
        '+ "Sesso: " + _sex(cdata(CDATA_SEX, CHARA_PLAYER)) + "   Età: " + calcage(CHARA_PLAYER) '
        '+ " \\nAltezza: " + cdata(CDATA_HEIGHT, CHARA_PLAYER) + "cm   Peso: " '
        '+ cdata(CDATA_WEIGHT, CHARA_PLAYER) + "kg"',

    # --- :17662-:17670 le sei righe a due colonne. ⚠️ dodici caratteri esatti
    #     per etichetta, spazi compresi: `fixtxt` pareggia la riga, ma i due
    #     punti li allinea la stringa.
    (17662, 'Race      : God       : '):
        'fixtxt("Razza     : " + racename, 30) + fixtxt("Fede      : " + godname(cdata(CDATA_GOD,0)), 32)',
    (17663, 'Class     : Guild     : '):
        'fixtxt("Classe    : " + classname, 30) + fixtxt("Gilda     : " + guildname(), 32)',
    (17664, 'Level     : Tot. Days : '):
        'fixtxt("Livello   : " + cdata(CDATA_LEVEL,0), 30) + fixtxt("Giorni    : " + gdata(GDATA_DAY_PAST), 32)',
    # 「残りBP」: il giapponese chiama BP i punti bonus, e sta in due caratteri
    (17666, 'S. Points : Turns     : '):
        'fixtxt("BP        : " + cdata(CDATA_SKILLPOINT, CHARA_PLAYER),30) + fixtxt("Turni     : " + gdata(GDATA_TURN), 32)',
    (17667, 'Gold      : Kills     : '):
        'fixtxt("Oro       : " + cdata(CDATA_GOLD, CHARA_PLAYER), 30) + fixtxt("Uccisioni : " + gdata(GDATA_KILLED), 32)',
    (17669, 'Platinum  : Max D Lvl : '):
        'fixtxt("Platino   : " + cdata(CDATA_PLATINUM, CHARA_PLAYER), 30) + fixtxt("Prof. max : " + gdata(GDATA_DEEPEST_LEVEL), 32)',
    (17670, 'Playtime  : '):
        'fixtxt("Tempo     : " + cnvplaytime(gdata(GDATA_PLAY_TIME) + timeGetTime() / 1000 - time_begin), 30)',

    # --- :17673-:17720 le dieci statistiche. Dodici caratteri ciascuna.
    (17673, 'Life      : '): 'Vita      : ',
    (17674, 'Mana      : '): 'Mana      : ',
    (17675, 'Sanity    : '): 'Follia    : ',
    (17676, 'Speed     : '): 'Velocità  : ',
    (17677, 'Fame      : '): 'Fama      : ',
    (17678, 'Karma     : '): 'Karma     : ',
    (17679, 'DV        : '): 'DV        : ',
    (17680, 'PV        : '): 'PV        : ',
    # 💡 qui «Schivata» e «Protezione» ci stanno per intero: nella scheda del
    #    personaggio gli stessi due erano «Schiv.» e «Prot.» per 43 e 46 px.
    (17719, 'Evade     : '): 'Schivata  : ',
    (17720, 'Prot      : '): 'Protezione: ',

    # --- i quattro titoli di sezione, trenta trattini e il nome.
    #     ⚠️ questo non è un titolo: `:17722` è `lang(...) + cnvweight(...)`, e i
    #        tre spazi finali dell'inglese sono la giuntura col peso che segue.
    #        L'italiano ci mette i due punti, che è quel che l'etichetta chiede.
    (17722, '------------------------------ Equip Weight   '):
        '------------------------------ Equipaggiamento, peso: ',
    # 「装備なし」: qui il soggetto è l'equipaggiamento, maschile
    (17774, 'None'): 'Nessuno',
    (17799, '------------------------------ Characteristics'):
        '------------------------------ Tratti',
    (17815, '------------------------------ Companions'):
        '------------------------------ Alleati',
    (17844, '------------------------------ Titles'):
        '------------------------------ Titoli',

    # --- :17831-:17838 le due righe dei compagni.
    (17831, ' Race:  \\nClass:    Sex:    Age:  \\nHeight: cm   Weight: kg'):
        'cdatan(CDATAN_NAME, cnt) + " Razza: " + racename + " \\nClasse: " + classname '
        '+ "   Sesso: " + _sex(cdata(CDATA_SEX, cnt)) + "   Età: " + calcage(cnt) + "" '
        '+ " \\nAltezza: " + cdata(CDATA_HEIGHT, cnt) + "cm" + "   Peso: " + cdata(CDATA_WEIGHT, cnt) + "kg"',
    (17834, ' Race:  \\nClass:   Sex:    Age:   \\nHeight: cm   Weight: kg'):
        'cdatan(CDATAN_NAME, cnt) + " Razza: " + racename + " \\nClasse:" + classname '
        '+ "   Sesso: " + cdatan(CDATAN_NEWSEX, cnt) + "   Età: " + calcage(cnt) + "" '
        '+ "  \\nAltezza: " + cdata(CDATA_HEIGHT, cnt) + "cm" + "   Peso: " + cdata(CDATA_WEIGHT, cnt) + "kg"',
    (17836, 'Level: '): 'Livello: ',
    # ⚠️ «Engaged» accorderebbe col compagno: nome astratto.
    (17838, 'Engaged   '): 'Fidanzamento ',

    # --- :17849-:17855 la paga e la scadenza dei ranghi.
    #     ⚠️ «Salary   : about » è di diciassette caratteri e la resa pure.
    (17849, 'Salary   : about '): 'Paga     : circa ',
    # ⚠️ rete 3: lo stesso 「ノルマ: 」 è reso «\nScadenza: » a :2905, dove la riga
    #    comincia con un a capo e non deve allinearsi a niente. Qui la colonna
    #    vuole dodici caratteri: due siti, due esigenze.
    (17849, 'Deadline  : '): 'Scadenza  : ',
    (17855, 'Within '): 'Entro ',
    # ⭐ 「日以内」 è già « giorni» a :2905
    (17855, ' days'): ' giorni',

    # --- :17881-:17920 le munizioni.
    # ⭐ copiata da proc.hsp:26940
    (17881, 'You need to equip ammo.'): 'Devi equipaggiare le munizioni.',
    (17906, " isn't capable of changing ammo."):
        'itemname(ci) + " non può cambiare munizioni."',
    (17917, 'Current Ammo Type:'): 'Munizioni caricate:',
    # ⭐ copiate da action.hsp:15273 e proc.hsp:26945
    (17920, 'Normal'): 'Normali',
    (17920, 'Unlimited'): 'Illimitate',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-023.jsonl'
DA, A = 17650, 17999
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
