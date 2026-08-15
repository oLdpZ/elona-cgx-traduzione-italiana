# -*- coding: utf-8 -*-
"""Lotto `command-009`: le 58 voci di `*com_ally`, la lista degli alleati e dei
prigionieri.

E' la finestra che si apre ogni volta che il gioco chiede **quale compagno** —
richiamarlo, venderlo, iscriverlo alla scuola, metterlo al negozio, portarlo
all'arena, rinchiuderlo. Undici usi diversi della stessa lista, distinti da
`allyctrl`, piu' gli stati che compaiono accanto a ogni nome.

⚠️⚠️ **`larghezze.py` NON misura questo file, e la ripresa della 44a diceva il
contrario.** `larghezze.py:68` dichiara `FILE = "text.hsp"`: i suoi 75 menu sono
tutti di li', e nessuna guardia ha mai guardato un menu di `command.hsp`. Quindi
il tetto se lo costruisce il lotto, come per il «Background».
✅ **Qui pero' il sorgente il budget lo dichiara davvero**, ed e' la strada
migliore della stima sull'inglese: `chara.hsp`… no, `command.hsp:1281`-`:1283`
apre una finestra da **620 px**, mette le voci a `wx + 84` e la seconda colonna
a `wx + 350`. Quindi la prima colonna ha **266 px** e la seconda **~250**, ed e'
lo stesso metro della scheda del personaggio della 43a: la differenza fra due
`pos` scritte a poche righe di distanza.
💡 Il nome del compagno mangia quasi tutta la prima colonna, quindi quel che
conta davvero e' che i **suffissi fra parentesi** non siano piu' lunghi dei
loro inglesi. Il tetto della zona e' 44 caratteri (`scratchpad/tetto-en.py`).

⚠️ **Sette suffissi inglesi non chiudono la parentesi** — `(Riding`,
`(OutRange`, `(offensive`, `(defensive`, `(intercept`, `(talking`, `(Dead` —
mentre `(Waiting)`, `(Alive)`, `(Ash)`, `(Stray)` la chiudono. Il giapponese le
chiude tutte, e per i quattro ordini di combattimento usa le **barre**,
「/突撃/」 「/防御/」 「/迎撃/」 「/交渉/」, che a schermo distinguono l'ordine
dallo stato. La resa segue il giapponese: parentesi chiuse dove il giapponese ha
le parentesi, barre dove ha le barre.

⭐ **E «Ally List» sta per DIECI titoli giapponesi diversi.** 「収容する連行者」,
「呼び戻す仲間」, 「売り飛ばす仲間」, 「出場する仲間」, 「対象候補」,
「門下生候補」, 「放牧候補」, 「店長候補」, 「ブリーダー候補」,
「滞在状態の変更」: ognuno dice **a che serve la lista**, e l'inglese li
appiattisce tutt'e dieci. E' lo stesso appiattimento del `command-005` e della
42a, e disfarlo costa zero perche' la colonna giapponese e' li' accanto.

⚠️ **Tre stati vanno detti senza participio, e sono `txt` di rifiuto**: `:1519`,
`:1524`, `:1529` sono `he(p) + " " + is(p) + " dead."` e sorelle, dove `he` e
`is` sono **morfologia inglese** e quindi spariscono — la resa italiana resta
senza funzioni e senza soggetto, e «è morto» concorderebbe col compagno.
✅ «Non è più in vita», «È in attesa», «È al lavoro»: `essere` piu' locuzione,
che non accorda niente. E' la manovra del nome astratto della 44a in forma
verbale.

💡 **Sei copie su cinquantotto**, tutte pescate da `dossier.py`: «Nome»
(`:453`, `:456`, `:14120`), «Prezzo» (`:14101`), «AP» (`:10504`), «Vita»
(`:10517` e `skill.hsp:9`), «Nessuna» (`init.hsp:371`). Piu' due termini presi
dal glossario invece che inventati: «Trattativa» (`skill.hsp:222`) e
«Ingegneria genetica» (`skill.hsp:197`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1196-:1273 gli undici usi della lista. Per ognuno: la domanda (`txt`),
    #     il titolo della finestra e le due intestazioni di colonna.
    (1196, 'Imprison who?'):
        'Chi vuoi rinchiudere?',
    (1197, 'Prisoner List'):
        'Prigionieri da rinchiudere',
    # ⭐ copiata: «Nome» sta gia' a :453, :456 e :14120
    (1197, 'Name'):
        'Nome',
    (1197, 'Status'):
        'Stato',

    (1201, 'Who to recall?'):
        'Chi vuoi richiamare?',
    (1202, 'Ally List'):
        'Alleati da richiamare',
    (1202, 'Name'):
        'Nome',

    (1206, 'Who to sell off?'):
        'Chi vuoi vendere?',
    (1207, 'Ally List'):
        'Alleati da vendere',
    # ⭐ copiata: 「値段」 e' gia' «Prezzo» a :14101
    (1207, 'Value'):
        'Prezzo',

    # ⚠️ 「試合の規定人数: 」 e' il numero regolamentare, e lo spazio in coda serve
    (1221, 'Participant: '):
        'Partecipanti: ',
    (1222, 'Ally List'):
        'Alleati in gara',

    (1227, 'Whose power will you awaken?'):
        'A chi vuoi risvegliare il potere?',
    (1228, 'Ally List'):
        'Candidati',
    # ⚠️ 「必要AP/所持AP」 dice due cose, «Cost/AP» una e mezza
    (1228, 'Cost/AP'):
        'AP necessari/AP',
    # ⭐ copiata: «AP» e' invariato dalla 43a (:10504)
    (1232, 'AP'):
        'AP',

    (1235, 'Who will you add body parts to?'):
        'A chi vuoi aggiungere una parte?',
    # ⭐ copiata: 「生命力」 e' gia' «Vita» a :10517 e a skill.hsp:9
    (1236, 'Life'):
        'Vita',

    (1239, 'Who will help?'):
        'Chi vuoi che dia una mano?',
    (1243, 'Whose story?'):
        'La storia di chi?',

    (1247, 'Who will train here?'):
        'Chi vuoi iscrivere?',
    (1248, 'Ally List'):
        'Aspiranti',

    (1251, 'Who do you want to leave here?'):
        'Chi vuoi lasciare al pascolo?',
    (1252, 'Ally List'):
        'Candidati al pascolo',

    (1255, 'Who will be the shopkeeper?'):
        'Chi vuoi come negoziante?',
    (1256, 'Ally List'):
        'Candidati al negozio',
    # ⭐ «Trattativa» viene da skill.hsp:222; CAR e' la sigla della scheda
    (1256, 'CHR/Negotiation'):
        'CAR/Trattativa',

    # ⚠️ «allevatore» concorderebbe col compagno: si nomina l'attivita'
    (1259, 'Who will be the breeder?'):
        'Chi vuoi alla riproduzione?',
    (1260, 'Ally List'):
        'Candidati alla riproduzione',
    (1260, 'Breed Power'):
        'Fertilità',

    (1263, 'Who should stay in your home?'):
        'Chi vuoi che resti qui?',
    (1264, 'Ally List'):
        'Chi resta e chi no',

    (1269, 'Who is the subject?'):
        'Chi è il soggetto?',
    (1270, 'Ally List'):
        'Alleati',
    (1273, 'Body/Skill'):
        'Parti/Abilità',

    # --- :1319 il bottone in fondo alla lista.
    (1319, 'Proceed'):
        'Conferma',

    # --- :1328-:1361 quel che si legge accanto al nome. Il giapponese chiude le
    #     parentesi e usa le BARRE per i quattro ordini: la resa fa uguale.
    (1328, '(Riding'):
        '(in sella)',
    (1332, ' *In* '):
        ' *in gara* ',
    (1345, '(OutRange'):
        '(fuori vista)',
    (1350, '(offensive'):
        '/assalto/',
    (1353, '(defensive'):
        '/difesa/',
    (1356, '(intercept'):
        '/contrasto/',
    (1359, '(talking'):
        '/dialogo/',
    (1361, ' PGauge:%'):
        '" Carica:" + cdata(CDATA_POWER_GAUGE, i) + "%"',

    # --- :1368-:1398 gli stati. ⚠️ «morto» e «disperso» concorderebbero col
    #     compagno: si dice lo stato, non la persona.
    (1368, '(revival impossible until you switch area)'):
        '(rinasce solo cambiando mappa)',
    (1371, '(Dead'):
        '(senza vita)',
    (1376, '(Waiting)'):
        '(in attesa)',
    (1379, 'Waiting'):
        'Attesa',
    (1384, '(Alive)'):
        '(in vita)',
    (1393, '(Ash)'):
        '(in cenere)',
    (1398, '(Stray)'):
        '(chissà dove)',

    # ⭐ copiata: 「なし」 e' gia' «Nessuna» a init.hsp:371, e qui il nome che
    #    sostituisce e' una parte del corpo
    (1445, 'None'):
        'Nessuna',

    # --- :1498-:1536 i quattro rifiuti.
    # ⭐ «Ingegneria genetica» viene da skill.hsp:197
    (1498, 'You need to be a better gene engineer.'):
        "L'ingegneria genetica non basta.",
    (1511, 'You need at least 1 pet to start the battle.'):
        'Serve almeno un partecipante.',
    # ⚠️ dinamiche: `he` e `is` sono morfologia e spariscono, quindi niente
    #    soggetto e niente participio — «è morto» concorderebbe
    (1519, '  dead.'):
        '"Non è più in vita."',
    (1524, '  waiting.'):
        '"È in attesa."',
    (1529, '  working.'):
        '"È al lavoro."',
    (1536, 'Too many participants.'):
        'Troppi partecipanti.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-009.jsonl'
DA, A = 1196, 1536
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
