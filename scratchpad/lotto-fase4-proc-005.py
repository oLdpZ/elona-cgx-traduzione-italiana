# -*- coding: utf-8 -*-
"""Lotto fase4-proc-005: le attivita' continuate, le due trappole e il furto
(proc.hsp 3401-4200).

E' la prima zona di `proc.hsp` in cui **chi parla e' il gioco al giocatore**, non
un personaggio: `*generalAct` (3671) ritorna subito se `cc != CHARA_PLAYER`.
Quindi vale la seconda meta' della regola della guida di stile — «se il gioco
parla a te e basta, resta il tu» — e non la terza persona dei quattro lotti
precedenti.

⚠️ La forma la decide `action.hsp`, che e' chiuso al 100% e ha 82 righe cosi':
- azione **compiuta** -> `Hai` + participio («Hai raccolto», «Hai fabbricato»,
  «Hai finito di mettere in ordine...», `action.hsp:8187`);
- azione che **comincia** o riflessiva -> presente («Ti siedi», «Usi un
  grimaldello», `action.hsp:3249` e `:3255`, che regge le due voci del `anche`).

⚠️ `itemname()` PORTA L'ARTICOLO ITALIANO (`ioriginalnamearticolo`,
`item_func.hsp:1933`): `"a "`/`"the "` alle righe 1949-1966 sono solo il ripiego
morto per quando l'array e' vuoto. Quindi davanti a `itemname()` vale il divieto
che la guida di stile scrive per `name()`: niente `di`, `a`, `da`, `in`, `su`.
E' per questo che :4150 («the hatch **of** X») e' girata su `"Hai aperto " +
itemname(...)`: l'oggetto diventa complemento oggetto invece che di specificazione.

⚠️ Due giapponesi diversi sotto lo stesso inglese `You are bored.`: :3712 e'
やる気が起きない (la voglia non viene, prima di cominciare) e :3729 e' もう飽きた
(ne ho abbastanza, a cosa gia' fatta). Arbitra il giapponese, come sempre: due
rese diverse, e la rete 4 non protesta perche' raggruppa per giapponese.

💡 Tre rese sono copie, non invenzioni:
- :3998 「ガード！ガード！」 -> `Guardie! Guardie!`, da `db_creature.hsp:50822`;
- :4063 行動を中断した -> «interrompe l'azione» di `adv.hsp:18`, voltato al tu;
- :4163 を収穫した -> «Hai raccolto ...» di `action.hsp:19482`.
E `ハッチ` e' gia' «portello» in `text.hsp:2935`, «Toil-Energy» gia' «Energia»
in `text.hsp:2170-2194`, `" gp"` gia' `" oro"` in `text.hsp:193`.

⚠️ :3986 e :3989 sono TESTE di frase: finiscono nel `txt` con `cnvtalk` di :3993
o :3998. L'inglese le chiude con la virgola, l'italiano coi due punti, che e' la
punteggiatura giusta davanti a una citazione. Nessuna delle due comincia per
minuscola o per punteggiatura, quindi non tocca ne' la maiuscola d'ufficio di
`init.hsp:1659-1661` ne' lo spazio accodato di `init.hsp:1666`.

⚠️ Niente participi ne' aggettivi che concordino col giocatore: «Ti scoprono a
rubare» e non «sei scoperto», «Ti addormenti» e non «ti sei addormentato»,
«Pesa troppo per le tue forze» e non «e' troppo pesante da maneggiarlo».
"""
import collections, glob, io, json, unicodedata

RESE = {
    # --- la scena del sesso, la coda del lotto 003 (qui cc NON e' il giocatore)
    (3421, ' earned gp.'):
        'name(cc) + " guadagna " + sexvalue + " oro."',
    # ⚠️ «svenuto» concorderebbe con name(): resta il presente.
    (3464, ' fainted from the intensity!'):
        'name(cc) + " sviene per la troppa foga!"',
    # 疲労し過ぎて失敗した: senza soggetto in giapponese, e questo file ha gia'
    # la sua forma impersonale per il fallimento (:138 «Il tentativo di scavo
    # fallisce.», e altre quattro fra :150 e :186).
    (3467, 'You are too exhausted!'):
        'Troppa stanchezza: il tentativo fallisce!',

    # --- *generalAct: le attivita' che cominciano
    (3681, 'You target .'):
        '"Prendi di mira " + itemname(ci, 1) + "."',
    # 寝る仕度を始めた: il giapponese dice «ha cominciato a prepararsi per
    # dormire», l'inglese appiattisce su «you lie down». Casa o citta'.
    (3686, 'You lie down.'):
        'Ti prepari a dormire.',
    (3690, 'You start to camp.'):
        'Cominci a montare il campo.',
    (3695, 'You start to construct .'):
        '"Cominci a costruire " + itemname(ci, 1) + "."',
    # ⚠️ statica: l'inglese perde l'oggetto che il giapponese nomina, e la voce
    # non ha modo di rimetterlo.
    (3699, 'You start to pull the hatch.'):
        'Cominci a girare il portello.',
    (3703, 'You start to pick .'):
        '"Cominci a raccogliere " + itemname(ci, 1) + "."',
    (3707, 'You start to cut tree.'):
        "Cominci ad abbattere l'albero.",
    # やる気が起きない: la voglia non viene. E' il rifiuto PRIMA di cominciare.
    (3712, 'You are bored.'):
        'Non ne hai voglia.',
    (3716, 'You start working.'):
        'Ti metti al lavoro.',
    # もう飽きた: ne ho gia' abbastanza. Stesso inglese di :3712, altro giapponese.
    (3729, 'You are bored.'):
        'Ne hai già abbastanza.',
    (3743, 'You begin to study .'):
        '"Cominci a studiare " + skillname(inv(INV_ITEM_BOOK_ID, ci)) + "."',
    (3746, 'You start training.'):
        'Cominci ad allenarti.',
    # i due «anche» ricalcano `action.hsp:3255`, «Usi anche il passe-partout».
    (3753, 'You also use the bookmark.'):
        'Usi anche il segnalibro.',
    (3763, 'You also use the dumbbell.'):
        'Usi anche il manubrio.',
    (3771, "The weather's bad outside, you have plenty of time to waste."):
        'Fuori il tempo è pessimo: tanto vale prendersela con calma.',

    # --- la motosega (axeitem == 30). Minuscole come le quattro sorelle
    #     dell'accetta, gia' toppate a :3822: « *clang* », « *tonf* », « *crac...* ».
    (3812, ' *vroom* '):
        ' *vrum* ',
    (3812, ' *whir* '):
        ' *sgrrr* ',

    # --- le due trappole del furto. ⚠️ Qui l'inglese NON traduce il giapponese:
    #     「突然ふたが閉まった！」 e' il coperchio che si chiude, non la vergine
    #     di ferro che cade in avanti. Arbitra il giapponese.
    (3915, 'Suddenly, the iron maiden falls forward.'):
        'Di colpo il coperchio si chiude!',
    (3923, 'Suddenly, the guillotine is activated.'):
        'Di colpo la ghigliottina cala!',

    # --- il furto scoperto. :3986 e :3989 sono teste: la coda e' :3993 o :3998.
    (3986, ' notice you,'):
        'name(cnt) + " ti sorprende a rubare:"',
    (3989, ' hear a loud noise,'):
        'name(cnt) + " sente un rumore sospetto:"',
    # 「貴様、何をしている！」 e' «che stai facendo!», non «fermo!».
    (3993, 'You there, stop!'):
        'Ehi tu, che stai facendo!',
    # copiata da db_creature.hsp:50822, stesso giapponese
    (3998, 'Guards! Guards!'):
        'Guardie! Guardie!',
    (4007, 'You are found stealing.'):
        'Ti scoprono a rubare!',

    # --- i rifiuti del furto
    (4024, 'The target is dead.'):
        'Il bersaglio è morto.',
    (4030, "It can't be stolen."):
        'Non si può rubare.',
    (4036, 'You lose the target.'):
        'Non trovi più il bersaglio.',
    # 重すぎて手に負えない: troppo pesante da maneggiare. «Le tue forze» perche'
    # la soglia e' sdata(SKILL_ATTR_STR) * 500, ed evita di concordare con
    # l'oggetto, che ha genere ignoto.
    (4052, "It's too heavy."):
        'Pesa troppo per le tue forze.',
    # «quell'oggetto» porta il proprio genere, cosi' il «lo» concorda con lui e
    # non col nome dell'oggetto, che non si conosce.
    (4058, 'Someone else is using the item.'):
        "Quell'oggetto lo sta usando qualcun altro.",
    # copiata da adv.hsp:18, «name(rc) + " interrompe l'azione."», al tu
    (4063, 'You abort stealing.'):
        "Interrompi l'azione.",

    # --- il furto riuscito
    (4112, 'You successfully steal .'):
        '"Hai rubato " + itemname(ti) + "."',
    (4128, 'You feel the stings of conscience.'):
        'Senti un rimorso di coscienza.',

    # --- le attivita' che finiscono
    # la struttura con le quadre e' quella di proc.hsp:233, e «Energia» e' la
    # resa di «Toil-Energy» nel menu del campo (text.hsp:2170-2194).
    (4135, 'You have finished your toil. [Current Toil-Energy: ]'):
        '"Hai finito il turno di lavoro. [Energia attuale: " '
        '+ adata(ADATA_LABOR_CAMP_TOIL_ENERGY, gdata(GDATA_AREA)) + "]"',
    (4139, 'You fall asleep.'):
        'Ti addormenti.',
    (4144, 'You finish constructing .'):
        '"Hai finito di costruire " + itemname(ci, 1) + "."',
    # ⚠️ «the hatch OF X» non si puo' rendere: itemname() porta l'articolo e
    #    «di » + «un rifugio» darebbe «di un rifugio» solo per caso, «della il
    #    rifugio» negli altri. L'oggetto diventa complemento oggetto.
    (4150, 'You finish pulling the hatch of .'):
        '"Hai aperto " + itemname(ci, 1) + " girando il portello."',
    # copiata da action.hsp:19482, «"Hai raccolto " + itemname(ci, 1) + "."»
    (4163, 'You harvest . ()'):
        '"Hai raccolto " + itemname(ci, 1) + ". (" '
        '+ cnvweight(inv(INV_ITEM_WEIGHT, ci)) + ")"',
    # 樹木を切り倒し、材木を作り出した: l'inglese perde il legname, che pero' il
    # codice crea davvero due righe sotto (ITEM_ID_WOOD_MATERIAL, :4179).
    (4171, 'You cut off tree.'):
        "Hai abbattuto l'albero e ne hai ricavato del legname.",
    (4183, 'You finish studying .'):
        '"Hai finito di studiare " + skillname(inv(INV_ITEM_BOOK_ID, ci)) + "."',
    (4186, 'You finish training.'):
        'Hai finito di allenarti.',
}

# rete 5, nuova in questa sessione: l'accento deve essere PRECOMPOSTO.
# Scrivendo questo lotto e' uscito decomposto -- 'a' + U+0300 COMBINING GRAVE --
# in cinque rese su 43. A occhio e' identico, `degrada()` non lo riconosce
# (cerca 'a' precomposta) e CP932 non ha il combinante: sarebbe finito nel
# sorgente come «gia» senza niente. L'ha visto solo `verifica`, e la
# normalizzazione qui costa una riga.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-005.jsonl'
DA, A = 3401, 4200

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
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2')

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
