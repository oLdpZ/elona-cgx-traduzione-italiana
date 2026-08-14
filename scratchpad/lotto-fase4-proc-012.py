# -*- coding: utf-8 -*-
"""Lotto fase4-proc-012: pozioni, latte, ubriacature, oli, acido
(proc.hsp 10101-10600).

42 rese, zero rinviate. Chiude la fascia 10000-10600 aperta dal lotto 011 e
porta `proc.hsp` a 518 su 1.098 (47%).

⚠️⚠️ **La rete che mancava e che questo lotto ha dovuto imparare: `verifica`
pretende che l'elenco delle funzioni di CONTENUTO sia identico fra inglese e
resa — stesse funzioni, stesso ordine** (`verifica.py:367`, `attese !=
trovate`). Non basta non aggiungerne di sbagliate: non se ne puo' aggiungere
**nessuna**. A `:10312` l'inglese e' `"In addition, " + his(tc) + " body is
enchanted."` — `his()` con UN argomento e' morfologia, quindi le funzioni di
contenuto sono **zero** — mentre il giapponese dice 「突然name(tc)は元気になった！」
e nomina il soggetto. La resa italiana **non puo' nominarlo**: mettere
`name(tc)` sarebbe aggiungere una funzione che l'inglese non ha, e la catena si
ferma. Quindi «Il vigore torna all'improvviso!», senza soggetto, come fa
l'inglese. Aggiunta la rete 11, che lo controlla prima di `verifica` e dice
quale funzione sarebbe di troppo.

⚠️ **Tre inglesi sbagliati, tutti raddrizzati sul giapponese:**
  - `:10426` dice «became the oil covered», ma il blocco e' `GOLDEN_MEAD` e
    l'effetto e' `CONDITION_DRUNK` piu' esperienza: e' una riga **copiata** dalla
    pozione d'olio di `:10464`. Il giapponese dice 「奇妙な感覚に襲われた」, una
    sensazione strana, ed e' l'unico che torni col codice.
  - `:10207` dice «Argh, the milk is cursed!», ma il giapponese e'
    「ぺっぺっ、まずー」: sputa e dice che fa schifo. Che sia latte lo sa il
    giocatore dal contesto, e la battuta non lo nomina.
  - `:10280` dice «I'm going to heaven.» dove il giapponese e' 「ひっく」, che e'
    **un singhiozzo**. Non e' l'inglese che specializza un giapponese generico
    (la famiglia della 31a): e' l'inglese che inventa una battuta dove il
    giapponese ha un rumore. Reso come singhiozzo, distinto da 「うぃっ！」 della
    stessa lista.

⚠️ **Due nomi di sostanza erano gia' decisi in `db_item.hsp` e vanno copiati**:
揮発油 -> «benzina» (`:137991`, femminile) e 精油 -> «olio essenziale»
(`:138004`, maschile). L'inglese di `:10478` dice «volatile oil», che e' il nome
generico, ma l'oggetto e' `ITEM_ID_GASOLINE` e in italiano si chiama gia'
benzina: usare due nomi per lo stesso oggetto e' il difetto `Bolt` della 35a.

⚠️ **Otto rese sono state riscritte per la rete 8.** Le tre sventure
(`:10340`, `:10356`, `:10378`) volevano tutte «si abbatte **su** » + `name()`,
che darebbe «su il putit»; sono diventate verbi transitivi — «travolge»,
«coglie», «colpisce» — che tengono anche la scala del giapponese: 苦しみ
(tormento) < 禍い (sventura) < 災厄 (flagello). Stessa cura per «il cuore **di**
», «in bocca **a** », «le ferite **di** ».

💡 **Le due liste di ubriacatura sono una riga sola ciascuna**: `:10274` porta
quattro `lang()` e `:10280` ne porta sette, tutte sulla stessa riga di sorgente.
La chiave `(riga, en)` regge perche' gli inglesi sono diversi fra loro — tranne
`*Hic*`, che compare in tutt'e due le liste ma su righe diverse.
"""
import collections
import glob
import io
import json
import re
import unicodedata

RESE = {
    # --- il rovid che si difende, i parassiti
    (10119, ' says: \\"Absolute protect!\\"'):
        'cdatan(CDATAN_NAME, cnt) + " grida: \\"Difesa assoluta!\\""',
    # rete 8: «la pelle di » + name() darebbe «di il putit». «vi» e' invariabile.
    (10125, ' stab  in the skin and injected something!'):
        'name(cc) + " trafigge " + name(tc) + " e vi inietta qualcosa!"',
    # rete 8: «in bocca a » + name() darebbe «a il putit»
    (10149, ' put something into  mouth!'):
        'name(cc) + " costringe " + name(tc) + " a inghiottire qualcosa!"',

    # --- lo specchio: leggere il cuore, esaminare
    # rete 8: «il cuore di » + name(). «scrutare» regge l'accusativo.
    (10175, "You look into 's heart."):
        '"Scruti " + name(tc) + " fin dentro il cuore."',
    (10191, 'You examine .'):
        '"Esamini " + name(tc) + "."',

    # --- il latte. ⚠️ :10207 l'inglese nomina il latte, il giapponese no.
    # «roba» toglie l'accordo: la bevanda puo' essere maschile o femminile.
    (10202, "Geee it's cursed! The taste is very dangerous."):
        'Uh, è roba maledetta! Il sapore è inquietante...',
    (10207, 'Argh, the milk is cursed!'):
        'Puah, puah! Che schifo!',
    (10212, 'The taste is very thick, almost addictive.'):
        'Un sapore denso, di quelli che danno dipendenza.',
    (10217, 'Yummy!'):
        'Che bontà!',
    (10221, ' grew quickly.'):
        'name(tc) + " cresce a vista d\'occhio."',
    # 「げふぅ」 e' un rutto; l'inglese aggiunge «muttered» e il nome
    (10241, ' muttered Ugh-Ughu'):
        'name(tc) + " borbotta " + cnvtalk("Buurp")',

    # --- la brutta ubriacatura (una riga sola, quattro lang())
    (10274, '*Hic*'):
        '*Hic...*',
    (10274, 'Ah, bad booze.'):
        'Che roba schifosa.',
    (10274, 'Ugh...'):
        'Bleah...',
    (10274, 'Bah, smells like rotten milk.'):
        'Sa di latte andato a male.',

    # --- la buona ubriacatura (una riga sola, sette lang())
    (10280, '*Hic*'):
        '*Hic!*',
    (10280, 'Ah, good booze.'):
        'Ah, roba buona.',
    (10280, 'La-la-la-la.'):
        'La-la-la-là.',
    # ⚠️ il giapponese e' 「ひっく」, un singhiozzo: l'inglese inventa la battuta
    (10280, "I'm going to heaven."):
        '*Hicc...*',
    (10280, 'Whew!'):
        'Fiuu.',
    (10280, "I'm revived!"):
        'Irresistibile.',
    (10280, 'Awesome.'):
        'Mmmh!',

    # --- i dolci impastati
    (10290, 'The taste is very thick!!'):
        'Uh, è troppo buono!',
    (10295, 'Very yummy!'):
        'Buonissimo!!',
    (10303, '  dimmed.'):
        'name(tc) + " sviene."',

    # ⚠️ l'inglese NON ha name(): ha solo his(tc), che e' morfologia. Le funzioni
    #    di contenuto sono zero, quindi la resa non puo' nominare nessuno —
    #    vedi la nota in cima. Il giapponese invece nomina il soggetto.
    (10312, 'In addition,  body is enchanted.'):
        '"Il vigore torna all\'improvviso!"',

    # --- le tre sventure, in scala: 苦しみ < 禍い < 災厄.
    #     rete 8: «si abbatte su » + name() darebbe «su il putit».
    (10340, 'Agony has befallen .'):
        '"Il tormento travolge " + name(tc) + "!"',
    (10356, 'Calamity has befallen .'):
        '"La sventura coglie " + name(tc) + "!"',
    (10378, 'Disaster has befallen !'):
        '"Il flagello colpisce " + name(tc) + "!"',

    # --- le pozioni che curano e quelle che sporcano
    # rete 8: «le ferite di » + name(). Il ferito diventa soggetto.
    (10415, 'The potion greatly heals .'):
        'name(tc) + " chiude le ferite a una velocità impressionante..."',
    # ⚠️ inglese copiato dalla pozione d'olio: qui e' GOLDEN_MEAD. Il giapponese
    #    arbitra. «preda» e' invariabile.
    (10426, ' became the oil covered.'):
        'name(tc) + " è preda di una sensazione strana..."',
    (10439, 'Movement keys to move current position, hit the cancel key to exit.'):
        'Sposta il corpo astrale con i tasti di movimento, esci con il tasto Annulla.',
    # 精油 -> «olio essenziale», copiato da db_item.hsp:138004
    (10464, ' got covered in essential oil.'):
        'name(tc) + " si copre di olio essenziale."',
    (10466, 'So smelly!'):
        'Che puzza!',
    # ⚠️ 揮発油 -> «benzina», copiato da db_item.hsp:137991: l'oggetto e'
    #    ITEM_ID_GASOLINE e ha gia' un nome italiano
    (10478, ' got covered in volatile oil.'):
        'name(tc) + " si copre di benzina."',

    # --- l'acido. Due urla di lunghezza diversa nel giapponese, una sola in
    #     inglese: la lunghezza la porta l'italiano, come il giapponese.
    (10540, 'Arrrrg!'):
        'Aaargh!',
    (10542, 'The sulfuric acid melts .'):
        '"L\'acido corrode " + name(tc) + "."',
    # ⚠️ l'inglese dice «child», il giapponese 異物, «corpo estraneo»: piu'
    #    sobrio, e your()/his() sono morfologia e si tolgono.
    #    «dentro» non si fonde con l'articolo, a differenza di «di»/«a».
    (10547, ' child melts in  stomach.'):
        '"Il corpo estraneo dentro " + name(tc) + " si scioglie."',
    (10561, 'Arrrrg!'):
        'Aaaaaargh!!!',

    # --- l'acqua e il disinfettante
    (10578, '*quaff* The water is refreshing.'):
        '*gluc* Acqua limpida.',
    (10582, ' *quaff* '):
        ' *gluc* ',
    # ⚠️ `name(tc)` sta FUORI da lang() (`txt name(tc) + lang(...)`), quindi la
    #    resa e' la coda della frase e comincia con uno spazio. «disinfettato»
    #    concorderebbe: il nome toglie l'accordo.
    (10590, '  disinfected.'):
        '" riceve la disinfezione."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-012.jsonl'
DA, A = 10101, 10600

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
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

# rete 6: nessuna voce del lotto deve stare su una riga commentata (lotto 006).
sorgente = io.open(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\proc.hsp',
                   encoding='cp932').read().split('\n')
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    if FONDONO.search(resa):
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a un nome -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo, se no si salda alla coda del danno senza respiro (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` e' contenuto e resta, ma in italiano varra' «il suo»/«il
# tuo» per tutti i siti, quindi il nome che segue dev'essere maschile singolare
# (lotto 011). La rete non sa il genere: stampa il nome, da leggere.
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 11, nuova qui: le funzioni di CONTENUTO della resa devono essere le
# stesse dell'inglese, nello stesso ordine — e' la regola di verifica.py:367,
# ma qui il messaggio dice quale funzione e' di troppo o quale manca, invece di
# stampare due elenchi da confrontare a occhio. ⚠️ Non basta non toglierne:
# non se ne puo' AGGIUNGERE nessuna, nemmeno per dire quello che dice il
# giapponese (vedi :10312).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        # ⚠️ solo le DINAMICHE: verifica.py:359 mette il confronto dentro
        #    `if tipo == "dinamica"`. Una statica dentro `cnvtalk(...)` ha
        #    l'involucro nell'en_grezzo ma la resa e' testo nudo, e pretendere
        #    che porti `cnvtalk` boccerebbe undici rese giuste di questo lotto.
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
    raise SystemExit('lotto fermato dalle reti 0-2, 6, 7, 8, 9 e 11')

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
        if it != resa:
            print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
                  f"      qui      {resa!r}\n"
                  f"      {nome}:{riga}  {it!r}")

# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# ⚠️ Il confronto e' sui LETTERALI di testo, non sull'espressione: due siti che
# dicono le stesse parole su variabili diverse sono la stessa resa (lotto 011).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[v['jp']].add(parole(RESE[(v['riga'], v['en'])]))
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi: {rese}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
