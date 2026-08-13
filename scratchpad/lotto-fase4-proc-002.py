# -*- coding: utf-8 -*-
"""Lotto fase4-proc-002: le mosse delle tattiche e le reazioni (proc.hsp 1801-2600).

⚠️ Tempo verbale: **presente indicativo**, come le 31 dinamiche gia' rese in
questo file (`:226` «disinnesca», `:1094` «si mette a scrivere», `:1359` «torna
in se'»). Non e' solo stile: il passato prossimo farebbe concordare il
participio con `name()`, che e' una creatura di genere ignoto.
⚠️ 「〜を始めた」 e' gia' «si mette a...» in quattro siti (`:1094`, `:1118`,
`:1397`, `:1587`) e qui si segue.
⚠️ Via `is()`, `was()`, `_s()`: morfologia inglese, vietata dalle regole.
"""
import collections, glob, io, json

RESE = {
    # ⚠️ Stesso inglese in tre siti per tre giapponesi diversi: おひねり (`:1000`,
    #    la mancia dell'esibizione), めぐんでもらった (`:1571`, l'elemosina) e
    #    お布施 qui, che e' l'offerta religiosa. I primi due sono gia' distinti
    #    in dizionario; questo li segue. お布施 e' gia' «obolo» in db_creature:87382.
    (1834, 'The audience gives  total of  gold pieces.'):
        'name(cc) + " raccoglie in tutto " + cdata(CDATA_PERFORM_GOLD, cc) + " monete d\'oro in oboli."',

    # --- la carica
    (1870, ' began to accumulate power.'):
        'name(cc) + " si mette a caricare l\'energia."',
    # le quattro battute degli alleati che ti coprono mentre carichi.
    # ⚠️ Chi parla e chi ascolta hanno entrambi genere ignoto: tutte invarianti.
    (1897, 'Leave this to me!'):
        'Qui ci penso io!',
    (1897, "I'll buy you some time!"):
        'Ti faccio guadagnare tempo!',
    (1897, "I won't let them interfere!"):
        'Non lascio che disturbino la carica!',
    (1897, 'Hurry up, will you?'):
        'Fai in fretta, mi raccomando.',
    (1914, '  charging power.'):
        'name(cc) + " sta caricando l\'energia."',
    # フルチャージ e' un prestito inglese normale in giapponese, non una storpiatura:
    # si traduce (diverso da エクスプロージョン, che il giapponese deforma apposta).
    (1921, '*Full Charge!!*'):
        '*Carica completa!!*',

    # --- il balzo dall'alto
    (1944, ' jumped high into the sky.'):
        'name(cc) + " spicca un balzo altissimo."',
    # ⚠️ «sospeso in aria» concorderebbe con name(): si e' scelto un verbo.
    (1951, '  flying high in the sky.'):
        'name(cc) + " vola alto nel cielo."',
    (1966, ' attacked  with the gravitational potential of drop!'):
        'name(cc) + " piomba giù su " + cdatan(CDATAN_NAME, tc) + " con tutto il peso della caduta."',
    (1972, 'However, the distance was just a little short and it missed.'):
        'Ma per un soffio la distanza non basta e il colpo va a vuoto.',

    # --- l'agguato da sottoterra
    (2001, ' went underground.'):
        'name(cc) + " si infila sottoterra."',
    (2008, '  underground.'):
        'name(cc) + " sta sottoterra."',
    (2023, ' drilled out of the ground and attacked .'):
        'name(cc) + " sbuca da sottoterra e coglie di sorpresa " + cdatan(CDATAN_NAME, tc) + "."',

    # --- il tifo
    (2110, ' start cheering.'):
        'name(cc) + " si mette a fare il tifo."',
    (2114, ' also joined the cheering.'):
        'name(daihyou) + " si unisce al tifo!"',
    # ⚠️ たち e' il plurale, e l'inglese lo perde: le due righe sono identiche in
    #    inglese e diverse in giapponese. Arbitra il giapponese.
    (2117, ' also joined the cheering.'):
        'name(daihyou) + " e gli altri si uniscono al tifo!"',

    # --- la persuasione
    (2254, ' started to persuade.'):
        'name(cc) + " si mette a persuadere."',
    (2258, ' also joined the persuasion.'):
        'name(daihyou) + " si unisce alla persuasione!"',
    (2261, ' also joined the persuasion.'):
        'name(daihyou) + " e gli altri si uniscono alla persuasione!"',
    (2312, '  upset.'):
        'name(tc) + " vacilla."',
    (2346, ' laughed fearlessly and abruptly committed suicide.'):
        'name(tc) + " ride senza paura e di colpo si toglie la vita."',
    (2354, ' got tired of fighting and quietly walked away.'):
        'name(tc) + " si stanca di combattere e se ne va in silenzio."',

    # --- la pausa: stesso giapponese in due siti, e l'inglese di :2183 e'
    #     sgrammaticato («was a little break»). Stessa resa per tutti e due.
    (2183, ' was a little break.'):
        'name(cc) + " tira il fiato."',
    (2367, ' took a little break.'):
        'name(cc) + " tira il fiato."',

    # --- la battuta comica
    (2438, ' started telling a peculiar joke.'):
        'name(cc) + " si mette a far ridere a tutti i costi."',
    (2442, ' also joined the joke.'):
        'name(daihyou) + " si unisce alla battuta!"',
    (2445, ' also joined the joke.'):
        'name(daihyou) + " e gli altri si uniscono alla battuta!"',
    (2496, " couldn't help laughing out loud."):
        'name(tc) + " si sbellica dalle risate."',
    (2529, ' walks away in a good mood.'):
        'name(tc) + " se ne va di ottimo umore."',
}

USCITA = 'lavoro/fase4-proc-002.jsonl'
DA, A = 1801, 2600

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
voci = [v for v in tutte if DA <= v['riga'] <= A]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in voci).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
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
print(f'{len(voci)} voci scritte in {USCITA}')
