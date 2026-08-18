# -*- coding: utf-8 -*-
"""Lotto fase4-main-013: l'ospite, il rientro a casa e la fine del mondo
(main.hsp, 8121-8834).

Ventuno rese e **un rinvio**. Il gruppo grosso e' il rientro a casa dopo un
viaggio: la riga che accoglie chi gioca e le sei battute dei compagni.

⚠️⚠️⚠️ **Sette rese su otto sono girate per non dire «bentornato».** Le righe
di `:8381` e `:8465` parlano **a** chi gioca, e in italiano ogni forma naturale
di benvenuto — «bentornato», «sano e salvo», «ben trovato» — porta il genere di
chi la riceve. Le rese dicono la stessa cosa da un lato che non lo chiede:
«Eccoti a casa!», «Ah, sei di ritorno.», «Meno male, nessun guaio.». E' la
disciplina della 52a applicata al caso piu' fitto trovato finora: non una riga,
ma un intero saluto.
⚠️ Una sola resa e' stata **copiata**: «Eccoti a casa!» sta gia' in
`db_creature.hsp:42237` per lo stesso inglese, e va bene com'e'.
💡 Il prezzo si paga su 「おかか♪」, che e' 「おかえり」 storpiato da un bambino: in
italiano ogni storpiatura di «bentornato» finisce sulla vocale che porta il
genere, quindi si tiene l'affetto («Rieccoti!♪») e si lascia andare il gioco di
parole. E' una perdita dichiarata, non una svista.

⭐⭐⭐ **`:8490` e' morta, e la rete 6 non la vede: sta dentro un `if ( 0 )`.**
E' la **quarta** famiglia di riga spenta dopo il `;`, il `/* … */` e il ramo
`if ( jp )` della 56a — e stavolta non e' nemmeno un commento: e' un ramo che il
compilatore tiene e che non e' mai vero. La riga stampa `gain1` e `gain2`, cioe'
i due numeri del calcolo: e' una stampa di **debug** che qualcuno ha spento
lasciandola dov'era. La prova che non e' testo sta anche nell'inglese, che e'
copiato pari pari da `:8493`, la riga viva tre righe sotto — chi l'ha spenta non
si e' curato di dargli un inglese suo.
⚠️ Nessun referto del progetto guarda gli `if ( 0 )`:
`misura-blocchi-spenti.py` guarda i commenti di blocco, la rete 6 il `;`.
Quanti altri ce ne siano non lo sa nessuno.

💡 **Tre righe non si traducono, si copiano**: `:8712`, `:8724` e `:8797` hanno
lo stesso giapponese **e** lo stesso inglese di `proc.hsp:4641`, `:4650` e
`chara_func.hsp:7644`. Sono le schermate della fine del mondo, e due rese
diverse per la stessa schermata sarebbero un difetto che nessuna rete vedrebbe:
la rete 3 tace proprio perche' le rese coincidono.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :8121-:8182 l'ospite che viene a casa (EVENT_VISITOR).
    (8121, 'The guest lost his way.'):
        "L'ospite si è perso per strada.",
    (8182, 'It seems the guest has already left your house.'):
        "L'ospite se n'era già andato.",
    # Le quattro battute le dice il dipinto di <Ehekatl> e del pesce spada
    # (`:8125` lo cerca nell'inventario): sono versi di gatto, e 招く e' quel che
    # fa il gatto portafortuna — attirare gente.
    (8128, 'Meow!'):                    'Miuuu!',
    (8131, 'Mew mew!'):                 'Miu miu!',
    (8134, 'I invite guests! guests!'): 'Porto ospiti! Ospiti!',
    (8137, 'Swordfish!'):               'Pesce spada!',

    # --- :8373 il lampo che acceca i presenti. `_s(cnt)` e' morfologia e
    # sparisce; `name` e `cnvtalk` restano. Il modello e' chara_func.hsp:6258.
    (8373, ' shout Eyes! My eyes!'):
        'name(cnt) + " grida, " + cnvtalk("Gli occhi! I miei occhi!!")',

    # --- :8381-:8465 il rientro a casa. ⚠️⚠️ Tutte queste righe parlano A chi
    # gioca, e «bentornato» ne marcherebbe il genere: sette rese su otto sono
    # girate per non chiederlo.
    (8381, 'Welcome back.'):
        'Eccoti di nuovo qui.',
    # «Eccoti a casa!» e' gia' la resa di db_creature.hsp:42237 per lo stesso
    # inglese: si copia.
    (8465, 'Welcome home!'):            'Eccoti a casa!',
    (8465, 'Hey, dear.'):               'Ah, sei di ritorno.',
    # 無事 e' «sano e salvo», che concorderebbe: la resa dice la stessa cosa
    # dal lato del guaio, che non ha genere.
    (8465, "You're back safely!"):      'Meno male, nessun guaio.',
    # ⚠️ 「おかか」 e' 「おかえり」 storpiato da un bambino (e sono i fiocchi di
    # bonito): ogni storpiatura italiana di «bentornato» porterebbe il genere,
    # quindi si tiene l'affetto e si lascia andare il gioco di parole.
    (8465, 'Welcome back♪'):            'Rieccoti!♪',
    (8465, 'I was waiting for you.'):   'Ti stavo aspettando.',
    (8465, 'Nice to see you again.'):   'Che bello riaverti qui!',

    # --- :8475-:8493 l'esperienza di viaggio da spartire coi compagni.
    (8475, 'Organize and share your accumulated  travelExp?'):
        '"Vuoi mettere in ordine e spartire i " + gdata(GDATA_TRAVEL_DISTANCE) '
        '+ " punti di esperienza di viaggio accumulati?"',
    (8493, " didn't seem to have anything to gain from the travel."):
        'name(tc) + " non sembra averci guadagnato granché."',

    # --- :8546-:8834 le quattro righe sparse.
    (8546, ' *RRROOM-KABOOOOM* '):
        ' *RRROMBO-KABOOOM* ',
    # ⚠️ Stesso giapponese E stesso inglese di proc.hsp:4641 e :4650: si copiano
    # tali e quali, o due schermate della fine del mondo direbbero cose diverse.
    (8712, "Let's Ragnarok!"):
        'È giunto il giorno della fine.',
    (8724, ' *Curtain Call* '):
        ' *Chiamata alla ribalta* ',
    # Stesso giapponese di chara_func.hsp:7644.
    (8797, '*beeeeeep* An alarm sounds loudly!'):
        '*biiiiip!* Un allarme squilla assordante!',
    (8834, 'The robber turns their attention to you!'):
        'Un rapinatore ti ha messo gli occhi addosso!',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

# ⚠️ :8490 sta dentro un `if ( 0 )`: vedi la lezione in cima.
RINVIATE = {(8490, " didn't seem to have anything to gain from the travel.")}

USCITA = 'lavoro/fase4-main-013.jsonl'
DA, A = 8000, 8999
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\main.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_main.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**. Vedi il
# lotto 007 per il perche' e per la chiave lunga `(riga, en, jp)`.
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

# ⚠️ Il controllo di rete 1 va PRIMA delle altre reti (lotto 007).
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` o dentro un blocco. ⚠️ Si guarda la FIRMA.
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

# rete 7: una voce dentro un CONFRONTO non e' testo.
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome.
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

# rete 9: una TESTA di frase (l'inglese finisce in « and») chiude col connettivo.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare.
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo.
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

# rete 15-bis: le voci di menu di questo file stanno in `*re_select`, e il tetto
# e' quello dello sfondo. Adesso lo sa anche `strumenti/menu_dialogo.py`.
try:
    from strumenti.menu_dialogo import FINESTRA_EVENTO, reso, tetto_di
except ImportError:
    reso = None
if reso is not None:
    def sfondo_di(riga: int) -> str:
        for i in range(riga - 1, max(0, riga - 40), -1):
            trovato = re.match(r'^\s*file\s*=\s*"([^"]+)"', sorgente[i - 1])
            if trovato:
                return trovato.group(1)
        return '?'

    for v in voci:
        if 'chatList' not in sorgente[v['riga'] - 1]:
            continue
        sfondo = sfondo_di(v['riga'])
        tetto = tetto_di(FINESTRA_EVENTO, sfondo)
        testo = reso(RESE[chiave(v)])
        if tetto is None:
            print(f"⚠️ rete 15-bis: riga {v['riga']} — sfondo {sfondo!r} non trovato, "
                  f"NON misurata")
        elif len(testo) > tetto:
            errori.append(f"rete 15-bis: riga {v['riga']} {len(testo)} > {tetto} "
                          f"({sfondo}) -> {testo}")
        else:
            print(f"💡 rete 15-bis: riga {v['riga']} {len(testo):3d}/{tetto} "
                  f"({sfondo})  {testo}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione.
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


# rete 4: chiave `(giapponese, funzioni, inglese)` — corretta nella 57a.
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

# rete 13: stesso inglese, giapponese diverso. Referto da leggere.
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
