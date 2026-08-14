# -*- coding: utf-8 -*-
"""Lotto fase4-proc-007: la pesca, lo scavo, la miniera e i pasti
(proc.hsp 5001-5900).

36 rese su 38 voci. Le due che restano fuori sono :5584 «Merchant ship» e
«Pirate ship», RINVIATE: non sono testo, sono **operandi di confronto**.

⚠️ E' la seconda volta che capita in questo file, dopo «Party Room» della 27ª, e
stavolta i siti sono due (:5584 e :5685). `map.hsp` ASSEGNA il nome della mappa
(`mdatan(0) = lang("商船内部", "Merchant ship")` a :4087, `:4099`, `:8291`) e
`proc.hsp` lo CONFRONTA per sapere se stai scavando dentro una nave, dove il
bottino diventa spazzatura e legname. Tradurre solo il confronto lo fa fallire
per sempre, in silenzio: `map.hsp` non e' nel dizionario e nessuna guardia
guarda due file insieme.

⭐ La scoperta della zona: **chi ride mentre scavi e' Opatos**, e il progetto ha
gia' il suo registro. Il trigger e' `ITEM_ID_DOWSING_OPATOS` (:5595), e
`text.hsp:12174` e `:12227` — le battute del dio della pietra — rendono gia'
「フハハハ！」 con «Mwahahaha!» e 「フハーン！」 con «Mwahaan!». Due delle quattro
risate sono quindi copie esatte, non invenzioni. E' la lezione di `repertorio.py`
applicata a un dio invece che a una creatura.

💡 「ここ掘れフハハ！」 (:5709) e' la filastrocca di *Hanasaka Jiisan*,
「ここ掘れワンワン」 — «scava qui, bau bau» — col cane sostituito dalla risata del
dio. In italiano la favola non e' nota: resta l'ordine di scavare piu' la risata.

⚠️ A :5880 l'inglese sbaglia l'ultima delle sei battute: 「まずい！」 in bocca a
chi sta mangiando e' «che schifo», non `You fool!`. Il giapponese arbitra.
Delle sei, `...!!` e' dichiarata in `invariati.md`: 「……！！」 e' un silenzio, e
i puntini italiani si scrivono `...` come in inglese.

💡 Quattro termini erano gia' decisi e si copiano:
- 落とし穴 -> «fossa» (`proc.hsp:252`, `:547`, `:575`);
- もち -> «mochi» (`db_item.hsp:142206`);
- マシンルアー -> `<Super Esca>` (`db_item.hsp:140140`), qui in minuscolo perche'
  il messaggio la nomina per genere, non per nome, come il segnalibro a :3753;
- ごつっ -> « *tonf* » (`action.hsp:2269`), la stessa onomatopea del piccone.

⚠️ Niente participi ne' aggettivi che concordino col giocatore, e via `_s(cc)`
a :5805, :5808 e :5900.
"""
import collections, glob, io, json, unicodedata

RESE = {
    # --- la pesca
    (5055, 'You get !'):
        '"Hai tirato su " + itemname(ci, 1) + "!"',
    (5063, 'You start fishing.'):
        'Cominci a pescare.',
    # come «Usi anche il segnalibro» a :3753: l'oggetto e' <Super Esca>, ma il
    # messaggio lo nomina per genere.
    (5082, 'You also use the super lure.'):
        'Usi anche la super esca.',
    (5125, 'You stop fishing...'):
        'Smetti di pescare...',
    # 何も釣れなかった: il giapponese dice che non hai preso niente, l'inglese
    # commenta il tempo perso.
    (5332, 'A waste of time...'):
        'Non hai preso niente...',

    # --- lo scavo. ⚠️ I tre inglesi «search/dig the spot» e «dig the ground»
    #     stanno sotto tre giapponesi diversi: 採取 (raccolta), 探索 (ricerca),
    #     地面を掘る (scavare il terreno). Questo file ha gia' i primi due a
    #     :162 «Il tentativo di raccolta fallisce.» e :186 «...di ricerca...».
    (5345, 'You start to search the spot.'):
        'Cominci a raccogliere.',
    (5361, 'You start to dig the spot.'):
        'Cominci a cercare.',
    (5369, 'You start to dig the ground.'):
        'Cominci a scavare il terreno.',

    # --- i cinque rumori del piccone. Minuscoli, come le quattro di :3822 e le
    #     due della motosega del lotto 005. ⚠️ Il ♪ resta: e' l'unico carattere a
    #     due byte che la build inglese disegna, perche' init.hsp:1374 ci mette
    #     un'icona, ed e' gia' cosi' nel ramo inglese di :3822.
    (5381, ' *clink* '):        # jp ざくっ, la vanga che entra nella terra
        ' *zac* ',
    (5381, ' *smash* '):        # jp カキン, metallo contro pietra
        ' *tin* ',
    (5381, ' *thud* '):         # jp ごつっ, copiata da action.hsp:2269
        ' *tonf* ',
    (5381, ' *sing* '):         # jp じゃり, la ghiaia che frana
        ' *scric* ',
    (5381, ' *sigh* '):         # jp ♪, che canticchia mentre scava
        ' *♪* ',
    (5385, 'You finish digging.'):
        'Hai finito di scavare.',
    (5400, "*click* ...There's something here!"):
        "*clic* ...C'è qualcosa qui sotto!",
    # 落とし穴 e' «fossa» da :252, :547 e :575.
    (5438, ' set a pitfall trap.'):
        'name(cc) + " scava una fossa."',

    # --- la miniera e il muro
    (5449, 'You start to dig the mining spot.'):
        'Cominci a estrarre il minerale.',
    (5457, 'You start to dig the wall.'):
        'Cominci a scavare nel muro.',
    # jp この壁 e' singolare; l'inglese mette il plurale.
    (5463, 'These walls look pretty hard!'):
        'Questo muro sembra durissimo!',

    # --- Opatos che ride mentre trovi qualcosa. Il registro e' quello di
    #     text.hsp:12174 e :12227, le battute dello stesso dio.
    (5700, 'Muwahaha! Muwahaha!'):
        'Mwahahaha! Mwahahaha!',
    # copiata esatta da text.hsp:12227, stesso giapponese
    (5703, 'Muhan!'):
        'Mwahaan!',
    (5706, 'Mwahaha! Here it is!'):
        'È qui! Mwahahaha!',
    # 「ここ掘れフハハ！」, la filastrocca di Hanasaka Jiisan con la risata al
    # posto del cane.
    (5709, 'Dig! Dig! Mwahahaha!'):
        'Scava qui, mwahaha!',
    (5744, 'You finished digging the wall.'):
        'Hai finito di scavare nel muro.',
    # 何かを見つけた: il giapponese non dice da dove.
    (5749, 'You found something out of crushed heaps of rock.'):
        'Hai trovato qualcosa.',
    (5784, 'Your back hurts... You give up digging.'):
        'Ti fa male la schiena... rinunci a scavare.',

    # --- *eat. ⚠️ via `_s(cc)`.
    (5805, ' start to eat  in secret.'):
        'name(cc) + " comincia a mangiare " + itemname(ci, 1) + " di nascosto."',
    (5808, ' start to eat .'):
        'name(cc) + " comincia a mangiare " + itemname(ci, 1) + "."',
    # 「いただきマンモス」 e' いただきます col mammut incastrato dentro, e
    # l'inglese fa lo stesso gioco («eat» + «mammoth»). L'italiano incastra il
    # mammut in «buon appetito».
    (5811, "Let's eatammoth."):
        'Buon appetimammut!',

    # --- le sei reazioni al cibo avariato
    (5880, "Uggg! What's with the food!"):
        'Argh! Ma che roba è questa!',
    (5880, 'Yuck!!'):
        'Puah!',
    # 「……！！」 e' un silenzio: dichiarata in invariati.md
    (5880, '...!!'):
        '...!!',
    (5880, 'W-What...'):
        'Ma che...',
    (5880, 'Are you teasing me?'):
        '...Questo è un dispetto, vero?',
    # ⚠️ 「まずい！」 in bocca a chi mangia e' «che schifo», non «You fool!».
    #    Cfr. db_creature.hsp:89621, 「まずっ」 == «Bleah, che sapore.»
    (5880, 'You fool!'):
        'Che schifo!',

    # --- il mochi. もち e' «mochi» da db_item.hsp:142206. ⚠️ via `_s(cc)`.
    (5900, ' choke on mochi!'):
        'name(cc) + " si strozza con il mochi!"',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

# ⚠️ NON sono testo: sono operandi di confronto con map.hsp. Vedi rinviate.jsonl.
RINVIATE = {
    (5584, 'Merchant ship'),
    (5584, 'Pirate ship'),
}

USCITA = 'lavoro/fase4-proc-007.jsonl'
DA, A = 5001, 5900

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

# rete 7, nuova qui: una voce il cui `lang()` sta dentro un CONFRONTO non e'
# testo, e tradurla rompe il confronto in silenzio. E' il caso di «Party Room»
# (27ª) e di «Merchant ship»/«Pirate ship» qui: due volte nello stesso file.
for v in voci:
    riga = sorgente[v['riga'] - 1]
    if '==' in riga.split('lang(')[0] or '!=' in riga.split('lang(')[0]:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2, 6 e 7')

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
