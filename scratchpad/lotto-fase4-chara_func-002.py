# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-002: lo sguardo storto, l'ira, le maledizioni respinte
e i ventidue messaggi di resistenza (chara_func.hsp 2000-2999).

58 rese e **una rinviata**, su 59 voci. La zona e' stata scelta guardando lo
schermo, non l'elenco: lo screenshot del collaudo della 39ª aveva `glares at
you` (`:2021`) e `gets furious!` (`:2047`) fra le righe inglesi rimaste, e
`:2021` parte a **ogni** azione ostile contro un cittadino amichevole. E' la
lezione della 26ª — *la frequenza, non l'elenco* — per la seconda volta di
fila.

⭐⭐ **Quarantaquattro voci su cinquantanove sono lo STESSO blocco scritto due
volte.** `resistmod` (`:2675`-`:2741`) e `resistmodh` (`:2769`-`:2835`) sono i
due punti da cui il gioco annuncia che una resistenza e' salita o scesa — undici
elementi per due segni — e upstream li ha ricopiati **parola per parola**,
cambiando solo il nome della variabile (`resistmod_charid` /
`resistmodh_charid`). Quindi **ventidue rese coprono quarantaquattro siti**, e la
rete 4 le tiene inchiodate a coppie: stesso giapponese, stessa firma `['name']`,
stessi letterali. E' la percentuale di duplicazione piu' alta mai vista in un
lotto — piu' del menu delle tattiche del lotto `proc-026` (dodici su
trentaquattro) e dell'X-Frame del `-018` (nove su quarantadue).

⚠️⚠️ **E i ventidue sono tutti genitivo o participio, cioe' le due strade
insieme.** Il giapponese dice 「name **の**身体は…」, 「name **の**神経は…」,
「name **の**魂は…」, 「name **の**皮膚は…」: in italiano sarebbe «il corpo
**di** X», «i nervi **di** X», «l'anima **di** X», e `name()` porta gia'
l'articolo dentro (rete 8). E l'inglese ci mette il participio sopra — «`is
struck by an electric shock`», «`is covered by a magical aura`» — che
concorderebbe col personaggio.
✅ La strada e' una sola e vale per tutt'e ventidue: **il possesso implicito col
dativo riflessivo**, «X **si sente** il corpo in fiamme», «X **si sente** la
pelle avvolta in un'aura magica». Il possessivo sparisce e la concordanza cade
su un nome di genere fisso — «pelle» femminile, «corpo» maschile — non sul
personaggio. Dove il dativo non serviva basta il nome soggetto: «X ha i nervi
saldi», «X non teme piu' il buio», «X regge meglio i veleni».
💡 **E' la stessa scoperta del lotto 001 in forma nuova**: li' i sedici recuperi
si giravano col nome soggetto e il possesso implicito; qui il possesso implicito
si ottiene con «si sente», che l'italiano ha e l'inglese no.

⚠️⚠️ **`:2310` e' la seconda voce del progetto dentro un blocco spento.** Sta
in un `/********** ORIGINAL - BEGINNING
**********/ ... /********** ORIGINAL - ENDING **********/` — la riga con cui
monte annunciava un buff prima che il mod la sostituisse — ed e' testo che il
giocatore non legge mai. E' la classe di `proc.hsp:11796` della 37ª, la riga per
cui la rete 6 e' stata allargata ai commenti di BLOCCO. ✅ Rinviata, e **non c'e'
toppa da fare**: non e' un difetto a schermo, e' testo morto.
💡 **L'ha trovata il `dossier.py`, non la rete**: il blocco si vede nelle due
righe di contesto sopra la voce, e la rete 6 sarebbe scattata dopo — provato
girando `commenti-blocco.py` sul sorgente, che mette `:2310` fra le sue 46 righe
spente. Le due letture si confermano a vicenda, ed e' il motivo per cui il
dossier si legge prima di scrivere le rese e non dopo.

⚠️ **`:2280` e `:2298` sono un inglese solo per due giapponesi diversi**, ed e'
la rete 13 per la quarta volta. «`The holy veil repels the hex.`» sta per
「呪いを**防いだ**」 — la maledizione **respinta**, e il codice fa `return`
subito dopo — e per 「呪いを**弱めた**」, dove invece la maledizione entra e il
codice le **accorcia la durata** (`locvar_addbuff_fixeddur = limit(...)` due
righe sopra). L'inglese ha appiattito due esiti diversi in una riga; il
giapponese **e il codice** li distinguono. ✅ «respinge» e «attenua».

⚠️ **`:2021` e' un errore di monte piccolo e frequentissimo, ed e' il
trentaquattresimo.** Il giapponese e' 「name は嫌な顔をした。」 — *ha fatto una
faccia scocciata* — e l'inglese scrive «`glares at you`», cioe' **nomina il
giocatore**. Ma il ramo e' `cdata(CDATA_RELATION, hostileaction_target) == 10` e
basta: chi compie l'azione ostile puo' essere **chiunque**, e infatti il ramo
`else` di `:2024` guarda `hostileaction_source` proprio perche' li' la
distinzione serve. ✅ Reso sul giapponese, «`X storce il naso.`», che non nomina
nessun osservatore. 💡 E la rete 11 sarebbe stata d'accordo lo stesso:
l'inglese ha **un** `name()` e «you» non e' una funzione.

💡 **Quattro rese su cinquantotto sono copie**, tutte pescate da `dossier.py`:
«interrompe l'azione» (`adv.hsp:18`, stesso giapponese **e** stesso inglese),
«resiste» (`action.hsp:8844` e `proc.hsp:9322`), «L'etere ti corrode il corpo»
(`proc.hsp:25789`, stesso giapponese identico) e il termine «malattia
dell'etere» (`text.hsp:10113`).

💡 **E un termine tolto all'inglese**: `:2122` dice «`Incognito`», che e' il nome
del buff (`buff.hsp:67`, invariato), ma il giapponese scrive 「変装」, il nome
comune, che `buff.hsp:1020` rende gia' «Travestimento». Si segue il giapponese:
la riga parla della cosa, non del buff.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- l'azione ostile: due righe che partono a ogni colpo dato in citta'.
    # ⚠️ il giapponese dice solo 「嫌な顔をした」: l'inglese ci aggiunge «at you»,
    #    ma il ramo non sa chi sia la sorgente. Reso sul giapponese.
    (2021, ' glares at you.'):
        'name(hostileaction_target) + " storce il naso."',
    (2047, ' gets furious!'):
        'name(hostileaction_target) + " va su tutte le furie!"',
    # 家畜 e' «bestiame», come in db_item.hsp:137486
    (2067, 'The livestock got excited!'):
        'Il bestiame si agita!',
    # copiata da adv.hsp:18, stesso giapponese e stesso inglese
    (2101, ' cancel  action.'):
        'name(cnt) + " interrompe l\'azione."',
    # ⚠️ l'inglese dice «Incognito» (il buff), il giapponese 「変装」 (la cosa):
    #    buff.hsp:1020 la rende gia' «Travestimento»
    (2122, 'Incognito does not work for the duel opponent.'):
        'Durante un duello il travestimento non funziona.',

    # --- l'aggiunta di un buff: cosa lo ferma, cosa lo attenua, cosa lo chiude.
    (2248, 'But it produces no effect.'):
        'Ma non produce alcun effetto.',
    # riga di debug: stampa un numero
    (2260, 'Buff Power:.'):
        '"Potenza: " + locvar_addbuff_bpower + "."',
    # ホーリーヴェイル e' <Velo sacro> in buff.hsp:47
    # ⚠️ rete 13: :2280 e :2298 hanno lo STESSO inglese e due giapponesi diversi.
    #    防いだ = respinta (il codice fa `return`); 弱めた = attenuata (il codice
    #    accorcia la durata). Vedi il docstring.
    (2280, 'The holy veil repels the hex.'):
        'Il velo sacro respinge la maledizione.',
    # copiata da action.hsp:8844 e proc.hsp:9322, stesso giapponese
    (2288, ' resist the hex.'):
        'name(addbuff_charid) + " resiste."',
    (2298, 'The holy veil repels the hex.'):
        'Il velo sacro attenua la maledizione.',
    # ⚠️ :2310 e' RINVIATA: sta dentro un blocco /* ORIGINAL */ spento dal mod,
    #    ed e' testo che il giocatore non legge mai. Vedi il docstring.
    (2404, 'The effect of  ends.'):
        '"L\'effetto di " + buffname(delbuff_buffid) + " svanisce."',

    # --- le undici resistenze che SALGONO (resistmod, txtef COLOR_GREEN).
    #     ⚠️ il giapponese dice 「name の身体は…」, 「name の魂は…」: il genitivo
    #     davanti a name() non esiste. La strada e' il dativo riflessivo, che
    #     lascia il possesso implicito e sposta l'accordo su un nome di genere
    #     fisso. Le stesse ventidue rese tornano identiche in resistmodh.
    (2675, 'Suddenly,  feel very hot.'):
        '"D\'improvviso " + name(resistmod_charid) + " si sente il corpo in fiamme."',
    (2678, 'Suddenly,  feel cool.'):
        '"D\'improvviso " + name(resistmod_charid) + " si sente il corpo di ghiaccio."',
    (2681, '  struck by an electric shock.'):
        '"Una scarica elettrica percorre " + name(resistmod_charid) + "."',
    (2684, 'Suddenly,  mind becomes very clear.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha la mente limpida."',
    (2687, ' nerve is sharpened.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha i nervi saldi."',
    (2690, ' no longer fear darkness.'):
        '"D\'improvviso " + name(resistmod_charid) + " non teme più il buio."',
    (2693, ' eardrums get thick.'):
        'name(resistmod_charid) + " non bada più al frastuono."',
    (2696, 'Suddenly,  understand chaos.'):
        '"D\'improvviso " + name(resistmod_charid) + " comprende il caos."',
    (2699, ' now  antibodies to poisons.'):
        'name(resistmod_charid) + " regge meglio i veleni."',
    (2702, '  no longer afraid of hell.'):
        'name(resistmod_charid) + " sente l\'anima avvicinarsi all\'inferno."',
    (2705, ' body is covered by a magical aura.'):
        'name(resistmod_charid) + " si sente la pelle avvolta in un\'aura magica."',

    # --- le undici resistenze che SCENDONO (resistmod, txtef COLOR_PURPLE).
    (2711, ' sweat.'):
        '"D\'improvviso " + name(resistmod_charid) + " comincia a sudare."',
    (2714, ' shiver.'):
        '"D\'improvviso " + name(resistmod_charid) + " sente un brivido di freddo."',
    (2717, '  shocked.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha la pelle sensibile all\'elettricità."',
    (2720, ' mind becomes slippery.'):
        'name(resistmod_charid) + " non ha più la mente limpida di prima."',
    (2723, ' become dull.'):
        '"D\'improvviso " + name(resistmod_charid) + " ha i nervi a pezzi."',
    (2726, 'Suddenly,  fear darkness.'):
        '"D\'improvviso " + name(resistmod_charid) + " teme il buio."',
    (2729, ' become very sensitive to noises.'):
        '"D\'improvviso " + name(resistmod_charid) + " trova assordante ogni rumore."',
    (2732, ' no longer understand chaos.'):
        'name(resistmod_charid) + " non comprende più il caos."',
    (2735, ' lose antibodies to poisons.'):
        'name(resistmod_charid) + " regge peggio i veleni."',
    (2738, '  afraid of hell.'):
        'name(resistmod_charid) + " sente l\'anima allontanarsi dall\'inferno."',
    (2741, 'The magical aura disappears from  body.'):
        'name(resistmod_charid) + " si sente svanire l\'aura magica dalla pelle."',

    # --- resistmodh: le stesse ventidue righe, ricopiate parola per parola da
    #     upstream con l'unica differenza del nome della variabile. Le rese
    #     devono coincidere nei letterali, e la rete 4 lo pretende.
    (2769, 'Suddenly,  feel very hot.'):
        '"D\'improvviso " + name(resistmodh_charid) + " si sente il corpo in fiamme."',
    (2772, 'Suddenly,  feel cool.'):
        '"D\'improvviso " + name(resistmodh_charid) + " si sente il corpo di ghiaccio."',
    (2775, '  struck by an electric shock.'):
        '"Una scarica elettrica percorre " + name(resistmodh_charid) + "."',
    (2778, 'Suddenly,  mind becomes very clear.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha la mente limpida."',
    (2781, ' nerve is sharpened.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha i nervi saldi."',
    (2784, ' no longer fear darkness.'):
        '"D\'improvviso " + name(resistmodh_charid) + " non teme più il buio."',
    (2787, ' eardrums get thick.'):
        'name(resistmodh_charid) + " non bada più al frastuono."',
    (2790, 'Suddenly,  understand chaos.'):
        '"D\'improvviso " + name(resistmodh_charid) + " comprende il caos."',
    (2793, ' now  antibodies to poisons.'):
        'name(resistmodh_charid) + " regge meglio i veleni."',
    (2796, '  no longer afraid of hell.'):
        'name(resistmodh_charid) + " sente l\'anima avvicinarsi all\'inferno."',
    (2799, ' body is covered by a magical aura.'):
        'name(resistmodh_charid) + " si sente la pelle avvolta in un\'aura magica."',
    (2805, ' sweat.'):
        '"D\'improvviso " + name(resistmodh_charid) + " comincia a sudare."',
    (2808, ' shiver.'):
        '"D\'improvviso " + name(resistmodh_charid) + " sente un brivido di freddo."',
    (2811, '  shocked.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha la pelle sensibile all\'elettricità."',
    (2814, ' mind becomes slippery.'):
        'name(resistmodh_charid) + " non ha più la mente limpida di prima."',
    (2817, ' become dull.'):
        '"D\'improvviso " + name(resistmodh_charid) + " ha i nervi a pezzi."',
    (2820, 'Suddenly,  fear darkness.'):
        '"D\'improvviso " + name(resistmodh_charid) + " teme il buio."',
    (2823, ' become very sensitive to noises.'):
        '"D\'improvviso " + name(resistmodh_charid) + " trova assordante ogni rumore."',
    (2826, ' no longer understand chaos.'):
        'name(resistmodh_charid) + " non comprende più il caos."',
    (2829, ' lose antibodies to poisons.'):
        'name(resistmodh_charid) + " regge peggio i veleni."',
    (2832, '  afraid of hell.'):
        'name(resistmodh_charid) + " sente l\'anima allontanarsi dall\'inferno."',
    (2835, 'The magical aura disappears from  body.'):
        'name(resistmodh_charid) + " si sente svanire l\'aura magica dalla pelle."',

    # --- la malattia dell'etere. 「エーテル病」 e' «malattia dell'etere»
    #     in text.hsp:10113.
    (2864, 'You show signs of Ether Disease.'):
        'Compaiono i primi sintomi della malattia dell\'etere.',
    # copiata da proc.hsp:25789: stesso giapponese, identico
    (2903, 'Your disease is getting worse.'):
        'L\'etere ti corrode il corpo.',
    (2991, 'The symptoms of the Ether Disease seem to calm down.'):
        'La corrosione dell\'etere si attenua.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(2310, ' ')}

USCITA = 'lavoro/fase4-chara_func-002.jsonl'
DA, A = 2000, 2999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\chara_func.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_chara_func.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
voci = [v for v in zona if (v['riga'], v['en']) not in RINVIATE]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

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
    resa = RESE[(v['riga'], v['en'])]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
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
        trovate = funzioni_di_contenuto(RESE[(v['riga'], v['en'])])
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
    resa = RESE[(v['riga'], v['en'])]
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
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
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
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
