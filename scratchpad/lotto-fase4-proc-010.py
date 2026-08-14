# -*- coding: utf-8 -*-
"""Lotto fase4-proc-010: il log di combattimento — proiettili, cure, morsi
(proc.hsp 7701-9200).

36 rese, zero rinviate. E' il pezzo di `proc.hsp` che la 32ª aveva indicato come
il motivo per cui questo file viene prima degli altri: «il log di un
combattimento qualsiasi e' pieno di inglese, e viene tutto da proc.hsp».

⚠️ **Dieci rese su 36 sono TESTE di frase**, quelle che finiscono in « and». Il
ramo che le sceglie e' `tc >= MAX_CHARA_FOLLOWER` e mette `gdata(GDATA_DMG_TYPE)
= 2` / `txt3rd = 1`: la coda e' il messaggio di danno di `chara_func.hsp`
(«infligge una ferita.», «provoca appena un graffio.»), che e' un verbo alla
terza persona senza soggetto. Quindi la testa deve chiudersi con « e», e la
forma della famiglia era gia' decisa in `action.hsp:15364`/`:15367`:

    "Il raggio di particelle colpisce " + name(tc) + " e"
    "Il raggio di particelle colpisce " + name(tc) + "."

Le cinque coppie di questa zona la ricalcano parola per parola.

⚠️ A :8334 e :8337 l'inglese e' COPIATO da :8319/:8322: dice «The ball hits»
dove il giapponese dice 電撃, la scarica elettrica. Sono due incantesimi diversi
e a schermo l'inglese ne annuncia uno solo. Il giapponese arbitra.

⚠️ **`ボルト` ha gia' DUE rese nel dizionario, dodici e dodici**: «saetta» nei 12
nomi di incantesimo di `skill.hsp` (`Saetta di gelo`, `Saetta di fuoco`...) e
«dardo» nei 12 nomi di libro di `db_item.hsp` (`dardo d'oltretomba`). Non e' una
divergenza che ho introdotto io e non la chiude questo lotto: qui vale «saetta»,
perche' il messaggio nomina il proiettile che il giocatore ha appena scelto dalla
lista degli incantesimi. Ma il difetto resta ed e' visibile: si compra il libro
del «dardo», si impara la «saetta». ⚠️ `--divergenti` non lo vede, perche' guarda
solo `db_creature.hsp`.

⚠️ Le sei rese dei morsi (:8746-:8789) avevano tutte un `name(tc) + your(tc)`,
cioe' «X bites off Y's flesh»: il possessivo inglese in mezzo a due nomi. In
italiano «la carne **di** name(tc)» darebbe «di il putit». La strada e' il
**gerundio col `ne`** — «azzanna name(tc) strappandone la carne» — che tiene tutti
e due i nomi, non ha preposizione e non concorda con niente.

💡 Due copie esatte: :8303 da `action.hsp:288` («name(tc) + " esita."»), e
「[記憶の灯]」 da `text.hsp:11636` («[lume della memoria]»).
"""
import collections, glob, io, json, re, unicodedata

RESE = {
    # --- gli effetti sul corpo. ⚠️ via `your(tc)`.
    (7705, ' gain weight.'):
        'name(tc) + " diventa più pesante."',
    # specchio di :7692 del lotto 009
    (7716, ' aging process speeds up.'):
        'name(tc) + " invecchia più in fretta."',
    (7784, ' blast magic by full power.'):
        'name(cc) + " scatena un incantesimo a piena potenza."',

    # --- i proiettili: cinque coppie testa/coda sulla forma di action.hsp:15364
    # ボルト -> «saetta», come i 12 incantesimi di skill.hsp
    (7903, 'The bolt hits  and'):
        '"La saetta colpisce " + name(tc) + " e"',
    (7906, 'The bolt hits .'):
        '"La saetta colpisce " + name(tc) + "."',
    (8283, 'The explosion hits  and'):
        '"L\'esplosione colpisce " + name(tc) + " e"',
    (8286, 'The explosion hits .'):
        '"L\'esplosione colpisce " + name(tc) + "."',
    # ボール -> «sfera», come le bacchette di db_item.hsp (sfera di veleno...)
    (8319, 'The ball hits  and'):
        '"La sfera colpisce " + name(tc) + " e"',
    (8322, 'The ball hits .'):
        '"La sfera colpisce " + name(tc) + "."',
    # ⚠️ qui l'inglese e' copiato da :8319: il giapponese dice 電撃, la scarica.
    (8334, 'The ball hits  and'):
        '"La scarica colpisce " + name(tc) + " e"',
    (8337, 'The ball hits .'):
        '"La scarica colpisce " + name(tc) + "."',
    (8554, 'The arrow hits  and'):
        '"La freccia colpisce " + name(tc) + " e"',
    (8557, 'The arrow hits .'):
        '"La freccia colpisce " + name(tc) + "."',

    # --- le esplosioni. Due giapponesi diversi sotto lo stesso inglese:
    #     爆発した (esplode) e 誘爆した (esplode per contagio).
    (8087, ' explode.'):
        'name(cc) + " esplode."',
    (8499, ' explode.'):
        'name(cc) + " esplode a catena."',

    # --- le cure. ⚠️ via `is(tc)`: «healed» in italiano sarebbe un participio
    #     che concorda col curato.
    (8199, '  healed.'):
        'name(tc) + " si riprende."',
    (8227, '  completely sane again.'):
        'name(tc) + " si libera della follia."',
    (8662, '  slightly healed.'):
        'name(tc) + " rimargina le ferite."',
    (8672, '  greatly healed.'):
        'name(tc) + " si riempie di forza vitale."',
    (8677, '  rapidly healed.'):
        'name(tc) + " recupera a vista d\'occhio."',
    # copiata esatta da action.hsp:288, stesso giapponese
    (8303, '  faltered.'):
        'name(tc) + " esita."',
    (8887, '  weakened.'):
        'name(tc) + " si indebolisce."',
    (8937, " won't weaken."):
        'name(tc) + " non si indebolisce."',

    # --- i morsi. ⚠️ «name(tc) + your(tc) + " flesh"» non si puo' rendere con
    #     «la carne di » + name(): il gerundio col `ne` tiene i due nomi senza
    #     preposizione e senza accordo.
    (8746, ' bite off  flesh and'):
        'name(cc) + " azzanna " + name(tc) + " strappandone la carne e"',
    (8749, ' bite off  flesh.'):
        'name(cc) + " azzanna " + name(tc) + " e ne strappa la carne."',
    (8759, ' bite off  memory and'):
        'name(cc) + " assale " + name(tc) + " divorandone i ricordi e"',
    (8762, ' bite off  memory.'):
        'name(cc) + " assale " + name(tc) + " e ne divora i ricordi."',
    (8786, ' suck  blood and'):
        'name(cc) + " morde " + name(tc) + " succhiandone il sangue e"',
    (8789, ' suck  blood.'):
        'name(cc) + " morde " + name(tc) + " e ne succhia il sangue."',

    # --- il prelievo consenziente.
    # ⚠️ `his(tc, 1)` con DUE argomenti e' contenuto, non morfologia: passa da
    #    `lang()` (`init.hsp:1959-1981`) e `verifica` pretende che resti — l'ha
    #    fermato il lotto quando l'avevo tolto («attese ['his', 'name', 'name'],
    #    trovate ['name', 'name']»). La forma che lo regge e' il congiuntivo
    #    «lascia che X succhi il suo sangue», che non ha bisogno ne' di una
    #    preposizione davanti a name() ne' di un accordo di genere.
    # ⚠️ Fino a che `init.hsp` non e' tradotto, `his()` stampa ancora `his`/`her`/
    #    `your`: e' la dipendenza gia' nota della guida di stile, non un difetto
    #    di questa resa. E quando lo sara', il valore italiano dovra' concordare
    #    con la cosa POSSEDUTA e non col possessore -- qui «sangue», maschile.
    (8849, ' obediently allows  to suck  blood.'):
        'name(tc) + " lascia docilmente che " + name(cc) + " succhi " + his(tc, 1) + " sangue."',
    (8849, 'Here you go...'):
        'Prego...',
    (8849, 'Is it good?'):
        'È buono?',

    # --- il resto
    # 「[記憶の灯]」 e' «[lume della memoria]» da text.hsp:11636
    (8911, 'The light emitted from Light of memory relieved memory delete!'):
        'La luce del [lume della memoria] ha attutito la cancellazione dei ricordi!',
    (8967, 'Touched portion is turned into dust.'):
        'La parte toccata si riduce in polvere.',
    # 魔法でモンスターが召喚された: il giapponese dice che e' una magia, l'inglese
    # si inventa un portale.
    (9115, 'Several monsters come out from a portal.'):
        'Una magia ha evocato dei mostri.',
    (9147, ' *Necro Awake* '):
        ' *Risveglio dei morti* ',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-010.jsonl'
DA, A = 7701, 9200

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

# rete 9, nuova qui: una TESTA di frase (l'inglese finisce in « and») deve
# chiudersi col connettivo, se no si salda alla coda del danno senza respiro.
# ⚠️ Si guarda il TESTO prodotto, non la forma dell'espressione: il connettivo
# puo' stare da solo (`+ " e"`) o in coda a un letterale piu' lungo
# (`" strappandone la carne e"`). La prima versione di questa rete cercava solo
# il primo caso e ha bocciato tre rese giuste.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2, 6, 7, 8 e 9')

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
