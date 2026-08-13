# -*- coding: utf-8 -*-
"""Lotto fase4-proc-003: bugia, minaccia, canto, pasto, spogliarello
(proc.hsp 2601-3400).

⚠️ Presente indicativo, come deciso nella 33ª: e' l'unico tempo che non fa
concordare il participio con `name()`.
⚠️ Via `is()`, `was()`, `_s()`, `his()`.
⚠️ Tre voci della zona sono RINVIATE (3376, 3383, 3389): sono la coda di una
frase la cui testa sta a `:3372`, dentro un blocco `if ( en )` con letterali
NUDI fuori da lang(). Vedi rinviate.jsonl.
"""
import collections, glob, io, json

RESE = {
    # --- la bugia. ⚠️ L'inglese appiattisce tre verbi giapponesi diversi su
    #     «also joined»: 補強 (rinforza) qui, 加担 (prende parte) alle minacce,
    #     重ねた (sovrappone la voce) al canto. Arbitra il giapponese.
    (2613, ' starts talking with mixed lies.'):
        'name(cc) + " si mette a raccontare balle."',
    (2617, ' also joined the lie.'):
        'name(daihyou) + " dà man forte alla bugia!"',
    # ⚠️ たち e' il plurale, che l'inglese perde.
    (2620, ' also joined the lie.'):
        'name(daihyou) + " e gli altri danno man forte alla bugia!"',
    (2671, ' believed the lie and became uneasy.'):
        'name(tc) + " crede alla bugia e si inquieta."',
    (2728, '  completely fooled and left in a hurry.'):
        'name(tc) + " ci casca in pieno e se ne va."',

    # --- la minaccia
    (2812, ' started to intimidate.'):
        'name(cc) + " si mette a minacciare."',
    (2816, ' also joined the intimidation.'):
        'name(daihyou) + " si unisce alle minacce!"',
    (2819, ' also joined the intimidation.'):
        'name(daihyou) + " e gli altri si uniscono alle minacce!"',
    # ⚠️ «terrorizzato» concorderebbe con name(): il terrore diventa un nome.
    (2870, '  frightened.'):
        'name(tc) + " ha il terrore addosso."',
    (2927, ' got scared and ran away quickly.'):
        'name(tc) + " scappa via in preda al panico."',

    # --- il canto
    (3011, ' sing a magically charged song.'):
        'name(cc) + " si mette a cantare una melodia intrisa di magia."',
    (3014, ' also joined the song.'):
        'name(daihyou) + " unisce la sua voce!"',
    (3017, ' also joined the song.'):
        'name(daihyou) + " e gli altri uniscono le loro voci!"',
    (3069, '  deeply impressed.'):
        'name(tc) + " si commuove."',

    # --- il pasto. Stesso giapponese 「は食事を終えた。」 a :3145 e :3258, con
    #     due inglesi diversi: una resa sola.
    (3130, ' started having a meal.'):
        'name(cc) + " si mette a mangiare."',
    (3140, '*Munch munch*'):
        '*gnam gnam*',
    (3145, ' finished a meal.'):
        'name(cc) + " finisce di mangiare."',
    (3258, ' finished  meal.'):
        'name(cc) + " finisce di mangiare."',
    (3168, 'You have failed.'):
        'Tentativo fallito.',
    (3174, '...Something is missing!'):
        '...No, così non va: manca qualcosa!',
    # copiata da :2183 e :2367, stesso giapponese (la rete 3 l'ha segnalata)
    (3233, ' took a small break.'):
        'name(cc) + " tira il fiato."',

    # --- la scena del sesso
    (3278, ' begin to take  clothes off.'):
        'name(cc) + " comincia a togliersi i vestiti."',
    # ⚠️ `_sex2` e' «ragazzo»/«ragazza», un nome nudo: il dimostrativo italiano
    #    concorderebbe. Corretto in `text.hsp:110` perche' porti dentro il
    #    proprio («quel ragazzo» / «quella ragazza»), come la preposizione sta
    #    nel valore e non nella frase. Ha due soli siti di chiamata, :3290 e
    #    :3450, che sono questa stessa frase.
    (3290, '\\"I-I don\'t really know that . Please spare my life!\\"'):
        '"\\"C-con " + _sex2(cdata(CDATA_SEX, tc)) + " era solo una cosa di letto! Io non so niente, la vita almeno...!\\""',
    # ⚠️ L'inglese travisa tutt'e due: 「なめてんの？」 e' «mi prendi in giro?», non
    #    «pensi di poter scappare?»; 「文句あんの？」 e' «hai qualcosa da ridire?».
    (3393, ' gets furious, And you think you can just run away?'):
        'name(cc) + " si infuria. " + cnvtalk("Mi stai prendendo in giro?")',
    (3396, ' retorted, Are you complaining?'):
        'name(tc) + " perde le staffe. " + cnvtalk("Che c\'è, hai qualcosa da ridire?")',
}

# le tre voci della zona che NON si rendono qui: la loro testa e' fuori da lang()
RINVIATE = {
    (3376, '\\"'),
    (3383, 'Here, take this.\\"'),
    (3389, 'Take this money, it\'s all I have!\\"'),
}

USCITA = 'lavoro/fase4-proc-003.jsonl'
DA, A = 2601, 3400

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
# le rinviate devono esistere davvero, se no il rinvio e' scritto sul nulla
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2')

gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.split('\\')[-1]
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

per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[v['jp']].add(RESE[(v['riga'], v['en'])])
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi: {rese}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
