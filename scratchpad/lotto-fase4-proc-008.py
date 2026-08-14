# -*- coding: utf-8 -*-
"""Lotto fase4-proc-008: la sazieta', la lettura, l'abisso e i lanci falliti
(proc.hsp 5901-6800).

58 rese, zero rinviate. Venti sono i **cinque gradini della sazieta'**
(:5912-:5931), tre o quattro alternative per gradino, che il gioco pesca a caso
a ogni boccone: e' il testo che il giocatore legge piu' spesso di ogni altro in
questa zona.

⚠️ Il gradino piu' pieno e' quello dove l'italiano rischia di piu': «You are
pretty bloated», «satisfied», «full» sono tutti aggettivi che concorderebbero
col giocatore. Le rese passano per un nome («Una sazieta' da non credere!»,
«Lo stomaco e' pieno!») o per un verbo («Hai saziato l'appetito»), che e' la
stessa strada delle etichette di stato della guida di stile. E «sazieta'» non e'
scelto a caso: e' gia' l'etichetta di 満腹 in `text.hsp:63-72`.

⚠️ A :6200 l'inglese stampa `name(tc)` dove il giapponese stampa `name(cc)`, e a
:6189 — undici righe sopra — c'e' `cc = CHARA_PLAYER`. Il `tc` inglese e' quello
rimasto in giro da prima: a schermo esce il nome sbagliato. La resa segue il
giapponese.

⚠️ A :6429 il nome sta FUORI da `lang()`: la riga e'
`txt cnven(cdatan(CDATAN_NAME, rc)) + lang("は復活した！", " " + have(rc) + " been resurrected!")`.
La voce e' solo la coda, e `have()` va tolta. «tornato in vita» concorderebbe
col morto, che puo' essere chiunque: resta il presente.

⚠️ A :6481 «guarded» chiede un complemento oggetto, non un `a` + `name()`:
«fa scudo **a** il putit» e' la trappola che la guida di stile vieta. «protegge»
regge l'oggetto diretto e non ha bisogno di preposizione. Stessa cosa a :6590,
dove «passes through» diventa «risparmia».

💡 Tre termini erano gia' decisi e si copiano:
- 深淵魔力 -> «potere abissale», e la riga con le quadre e' identica a
  `action.hsp:8929`, `:15073` e `proc.hsp:233`;
- すくつ / «the void» -> «il vuoto» (`db_item.hsp:142413`, «esploratore del vuoto»);
- ストック -> «copie» (`action.hsp:7816`, «dimezza le copie»).

💡 A :6756 lo stesso inglese di :6753 sta sotto un giapponese diverso: 詠唱に失敗
(ha sbagliato l'incantesimo) contro しかしうまく決まらなかった (ma non e' venuto
bene). Sono i due rami di `CDATA_CAST_STYLE`, e l'italiano li tiene distinti.
"""
import collections, glob, io, json, unicodedata

RESE = {
    # --- il mochi che va di traverso (coda di :5900)
    (5902, 'Mm-ghmm'):
        'Mmgh!',

    # --- gradino 1: strapieno. ⚠️ Nessun aggettivo riferito al giocatore.
    (5912, 'Phew! You are pretty bloated.'):
        'Per un bel pezzo non ci sarà bisogno di mangiare.',
    (5912, "You've never eaten this much before!"):
        'Non avevi mai mangiato tanto!',
    # 満腹 e' «sazieta'» gia' in text.hsp:63-72, dove e' un'etichetta di stato.
    (5912, 'Your stomach is unbelievably full!'):
        'Una sazietà da non credere!',

    # --- gradino 2: sazio
    (5916, 'You are satisfied!'):
        'Adesso ti senti a posto.',
    (5916, 'This hearty meal has filled your stomach.'):
        'Lo stomaco è pieno!',
    (5916, 'You really ate!'):
        "Hai saziato l'appetito.",
    (5916, 'You pat your stomach contentedly.'):
        'Ti accarezzi la pancia con aria beata.',

    # --- gradino 3: un po' meglio
    (5920, 'You can eat more.'):
        'Ci starebbe ancora qualcosa...',
    (5920, 'You pat your stomach.'):
        'Ti accarezzi la pancia.',
    (5920, 'You satisfied your appetite a little.'):
        "Hai calmato un po' l'appetito.",

    # --- gradino 4: ancora fame
    (5924, 'You are still a bit hungry.'):
        'Non hai ancora mangiato abbastanza.',
    (5924, 'Not enough...'):
        'Non basta...',
    (5924, 'You want to eat more.'):
        "La fame c'è ancora.",
    (5924, 'Your stomach is still somewhat empty.'):
        'Qualcosa nello stomaco ci è finito, almeno...',

    # --- gradino 5: fame vera
    (5928, 'No, it was not enough at all.'):
        'Non è bastato per niente!',
    (5928, 'You still feel very hungry.'):
        'Non ha fatto nemmeno il solletico allo stomaco.',
    (5928, "You aren't satisfied."):
        'Lo stomaco brontola di nuovo.',

    # --- gradino 6: si muore di fame
    (5931, "It didn't help you from starving!"):
        'Con questa razione non cambia niente!',
    (5931, 'It prolonged your death for seconds.'):
        'Così è servito solo a rimandare la morte di poco.',
    (5931, 'Empty! Your stomach is still empty!'):
        'Inutile... serve ben altro nutrimento.',

    # --- la lettura
    (5938, 'You have already decoded the book.'):
        'Quel libro è già stato decifrato.',
    (5944, ' can see nothing.'):
        'name(cc) + " non vede niente."',
    (5966, ' start to read .'):
        'name(cc) + " comincia a leggere " + itemname(ci, 1) + "."',
    (6009, ' falls apart.'):
        'itemname(ci, 1) + " si sbriciola in polvere."',
    # ⚠️ Qui l'inglese perde il nome del libro che il giapponese ha
    #    (npcn(cc) + itemname(ci, 1)), e NON si puo' rimettere: `verifica`
    #    pretende che le interpolazioni della resa siano ESATTAMENTE quelle
    #    dell'inglese, e con `itemname` in piu' ferma il lotto («attese
    #    ['name'], trovate ['itemname', 'name']»). Il guardiano ha ragione: le
    #    interpolazioni sono il contratto con la riga, non una scelta di stile.
    #    Resta l'asimmetria con :5966, che il nome ce l'ha.
    (6016, '  finished reading the book.'):
        'name(cc) + " finisce di leggere il libro."',
    (6023, 'You learned the recipe!'):
        'Hai imparato la ricetta!',
    (6039, 'You finished decoding !'):
        '"Hai decifrato " + itemname(ci, 1) + "!"',
    # copiata da action.hsp:8929 / :15073 e proc.hsp:233
    (6043, '[Abyss power: ] '):
        '"[Potere abissale: " + gdata(GDATA_FLAG_ABYSS_POWER) + "] "',
    # «stock» e' «copie» da action.hsp:7816
    (6052, 'You gain  spell stocks.'):
        '"Le copie dell\'incantesimo aumentano di " + gain + "."',

    # --- i libri che si leggono e basta
    # ⚠️ «autorizzato» concorderebbe col giocatore: soggetto l'esplorazione.
    #    «il vuoto» e' la resa di すくつ in db_item.hsp:142413.
    (6117, 'According to the card, you are permitted to explore the void now.'):
        "Sulla licenza c'è scritto, in piena forma burocratica, che l'esplorazione del vuoto è permessa.",
    # ⚠️ «firmata Rachel» evita di dover decidere il genere di 作家.
    (6131, "It's a lovely fairy tale written by Rachel."):
        'È una raccolta di fiabe che scaldano il cuore, firmata Rachel.',
    # la raccolta di foto di Lulwy (db_item.hsp:137111)
    (6136, 'Extreme photos are arranged...'):
        'Roba parecchio spinta...',

    # --- l'autore che rilegge il proprio libro: sette gradini di qualita'
    (6142, 'Why am I unable to express the ideas I have in my head...?'):
        'Perché non riesco a tirar fuori quello che ho in testa...?',
    (6145, 'Reading this now makes me cringe...'):
        'A rileggerlo adesso fa un male fisico...',
    # 王道: la via maestra, il canone. Non «cliche», che e' il giudizio contrario.
    (6148, "...I don't care if it's cliche. It's tried-and-true formula of storytelling."):
        '...Questo è il canone. Che dicano quel che vogliono, è il canone.',
    (6151, 'It has its flaws, but... it also carries its own unique charm.'):
        "Ha ancora molto di grezzo... ma un fascino tutto suo ce l'ha.",
    (6154, "It's not bad, but it could have been so much better...!"):
        'Non è male, ma si poteva fare molto, molto meglio...!',
    (6157, '...This is my favorite work!'):
        '...A me piace, e tanto basta!',
    (6160, "I'm surprised that I managed to write something *this* good..."):
        "Pensare che l'ho scritto io...",
    (6173, 'A strange air exudes from the open book...'):
        'Dalle pagine aperte esce un freddo innaturale...',

    # --- l'abisso
    # ⚠️ cc, non tc: :6189 fa `cc = CHARA_PLAYER`, e il tc inglese e' rimasto
    #    in giro da prima. Il giapponese ha ragione.
    (6200, ' emanated invisible blades.'):
        'name(cc) + " scaglia lame invisibili."',
    (6249, 'Deep darkness wraps around...'):
        'Un buio fondo avvolge ogni cosa...',
    (6291, 'It seems that you cannot escape from this floor.'):
        'Da questo piano sembra impossibile fuggire.',
    (6295, 'It seems that you cannot escape here.'):
        'Di qui non si fugge.',
    (6303, 'You jumped into the darkness that appeared in front of you...'):
        'Ti fai coraggio e ti addentri in quel buio orrendo...',
    # ⚠️ il nome sta fuori da lang() (cnven(cdatan(CDATAN_NAME, rc))): questa e'
    #    solo la coda. `have()` via, e niente participio: chi risorge puo' essere
    #    chiunque.
    (6429, '  been resurrected!'):
        '" torna in vita!"',
    (6432, 'It hurts...'):
        'Che dolore...',

    # --- il combattimento
    # ⚠️ «fa scudo a » + name() darebbe «a il putit»: «protegge» regge
    #    l'oggetto diretto. 💡 COPIATA da text.hsp:13, stesso giapponese: ci ero
    #    arrivato per conto mio allo stesso verbo, ma con un punto esclamativo
    #    invece del punto, e sarebbe stata una divergenza inutile. L'ha vista la
    #    rete 3.
    (6481, ' guarded .'):
        'name(tc) + " protegge " + name(cdata(CDATA_TAGTEAM_PARTNER, tc)) + "."',
    # 💡 COPIATA da action.hsp:6868, stesso giapponese. La mia era «riflette una
    #    parte della magia»: stesso senso, altre parole. Vince quella gia' decisa.
    (6492, ' reflected magic.'):
        'name(tc) + " ha riflesso parte della magia."',

    # --- la magia
    (6528, 'All the dropped items are swallowed in the abyss. Do you really use this magic?'):
        "Tutti gli oggetti a terra verranno inghiottiti dall'abisso. Vuoi davvero usare questa magia?",
    # ⚠️ «passa attraverso» + name() reggerebbe, ma 巻き込みを免れた dice che
    #    l'incantesimo NON lo coinvolge: «risparmia» lo dice con l'oggetto diretto.
    (6590, 'The spell passes through .'):
        '"L\'incantesimo risparmia " + name(calcmagiccontrol_arg2) + "."',
    # マナが足りないが: il giapponese dice perche', l'inglese dice solo che stai
    # per strafare.
    (6636, 'You are going to over-cast the spell. Are you sure?'):
        'Non hai abbastanza mana. Vuoi tentare il lancio lo stesso?',
    (6714, ' try to cast a spell in confusion.'):
        'name(cc) + " tenta un incantesimo nonostante la confusione."',
    # ⚠️ «accecato» concorderebbe con name(): la nebbia diventa il soggetto.
    (6743, ' fail to cast by glare of mist.'):
        'name(cc) + " non vede più nulla per la nebbia luminosa e sbaglia il lancio."',
    (6753, ' fail to cast a spell.'):
        'name(cc) + " sbaglia il lancio."',
    # stesso inglese di :6753, giapponese diverso: しかしうまく決まらなかった
    (6756, ' fail to cast a spell.'):
        'name(cc) + " non riesce a chiudere l\'incantesimo."',
    (6768, ' got too tired and failed!'):
        'name(cc) + " sbaglia il lancio per la troppa stanchezza!"',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-008.jsonl'
DA, A = 5901, 6800

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
