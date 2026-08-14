# -*- coding: utf-8 -*-
"""Lotto fase4-proc-006: il sonno, il risveglio, il riposo e il viaggio
(proc.hsp 4201-5000).

32 rese su 33 voci: la 33ª e' :4958, RINVIATA perche' sta su una riga
**commentata** (il blocco `JAMES CUSTOM - MANUSCRIPT HINT`, :4950-4962, e' spento
per intero). E' la classe della scoperta 1 della 27ª — `estrai.py` non salta i
commenti HSP — e in tutto `proc.hsp` e' l'unica: misurato, non dedotto.

⚠️ A :4872 l'inglese di monte ha SCAMBIATO le due code. Il `txt` porta tre
`lang()` e le ultime due si incrociano:
    jp 雪道を進むのは大変な苦労だ (avanzare sulla neve e' una gran fatica)
       -> en «You are caught in a snowdrift.»   [il banco di neve non c'e']
    jp 深い雪に脚をとられている  (le gambe affondano nella neve alta)
       -> en «It's hard to walk on a snowy road.» [la fatica non c'e']
Arbitra il giapponese, come sempre, e la resa raddrizza l'incrocio.

⚠️ E a :4906 l'inglese dice «robs **me** of my strength»: prima persona, in un
messaggio che parla al giocatore. Il giapponese (砂漠の熱気が体力を奪う) non ha
soggetto grammaticale. Non e' una scelta, e' una svista di monte.

💡 Tre rese su 32 sono copie:
- :4228 -> «Il tuo diario è stato aggiornato.», da `action.hsp:8282` e `text.hsp:4`;
- :4310 -> «Hai imparato una nuova capacità: ...», da `action.hsp:12012`,
  `:13001` e `:14848`, che e' la stessa frase con altre tre azioni speciali;
- :4650 「カーテンコール」 -> «chiamata alla ribalta», da `db_creature.hsp:101104`.
E `刻死紋` e' gia' «Segno letale» (`text.hsp:81`), il nome accorciato nella 32ª
perche' la piastrella dell'HUD tagliava a 11 caratteri.

⚠️ `Gene` (:4324) e' dichiarato in `invariati.md`: 遺伝子 e' «gene» in italiano
con la stessa grafia dell'inglese, come `tofu` e `chip`.

💡 Le onomatopee di questa zona erano gia' fatte con una toppa (:4865 « *ciaf* »,
« *zac* », « *plop* », « *sciff* »; :4926 « *sciaf* », « *splash* », « *plaf* »,
« *sciab* »): minuscole, come le quattro dell'accetta a :3822 e le due della
motosega del lotto 005. La famiglia ha una forma sola in tutto il file.

⚠️ Niente participi ne' aggettivi che concordino col giocatore: «Le forze sono
tornate» e non «ti senti riposato», «Ti sdrai a riposare» e non «ti sei sdraiato».
"""
import collections, glob, io, json, unicodedata

RESE = {
    # --- *sleep: non si dorme, e il diario
    # しかし、大事な用を思い出して飛び起きた: il giapponese dice PERCHE' non si
    # dorme (ti sei ricordato una cosa), l'inglese si limita al divieto.
    (4218, "But you can't sleep right now."):
        'Ma ti torna in mente una faccenda importante e salti in piedi.',
    # copiata da action.hsp:8282 e text.hsp:4, stesso giapponese
    (4228, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',
    # copiata da action.hsp:12012 / :13001 / :14848, stesso giapponese
    (4310, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " '
        '+ skillname(SKILL_SPACT_SERIOUS_BEGGING) + "."',

    # --- la scena del gene. `Gene` sta in invariati.md.
    (4324, 'Gene'):
        'Gene',
    # ⚠️ «con» non si fonde con l'articolo che name() porta: e' una delle tre
    #    preposizioni che la guida di stile lascia passare, con «per» e «tra».
    (4326, 'You spent a night with . A new gene is created.'):
        '"Hai passato una notte di fuoco con " + name(tc) '
        '+ ". Ne è nato un nuovo gene."',
    # ふぅ e' un sospiro di appagamento, non una parola. E' l'unica voce del
    # `chatList`, cioe' il bottone con cui si chiude la scena.
    (4328, 'Sweet.'):
        'Ahhh...',

    # --- la sveglia di Mani, che e' una macchina e parla da macchina
    (4351, "It's time. Restarting."):
        'È ora. Riavviati.',
    (4354, 'It is almost time to cancel sleep mode.'):
        'È quasi ora di uscire dalla modalità di sospensione.',
    (4357, 'I will send an awakening signal to your brain.'):
        'Trasmetto un segnale di risveglio al cervello.',
    (4360, 'I will start a forced wake-up program.'):
        'Avvio il programma di risveglio forzato.',

    # --- il risveglio
    # ⚠️ «riposato» concorderebbe col giocatore: il merito passa alle forze.
    (4365, 'You have slept for  hours. You are refreshed.'):
        '"Hai dormito " + timeslept + " ore. Le forze sono tornate."',
    # sintagma nominale, che e' la forma che questo file usa per i giudizi
    # (:954 «Un disastro completo...», :978 «Un\'esibizione convincente.»).
    (4388, 'You wake up feeling so-so.'):
        'Un risveglio così così.',
    # 主能力計 / スキル計 / 魔法計: il giapponese dice QUALI totali sono, l'inglese
    # chiama «Total» il primo e basta.
    (4585, 'You wake up feeling good. Your potential increases. (Total:%)(SkillTotal:%)(SpellTotal:%)'):
        '"Un bel risveglio. Il potenziale è cresciuto. (Attributi: " + grown '
        '+ "%)(Abilità: " + growns + "%)(Magia: " + grownsp + "%)"',
    # 刻死紋 e' «Segno letale» dalla 32ª (text.hsp:81): il nome corto che sta
    # nella piastrella dell'HUD.
    (4590, 'Death-Crest that had been carved into you had disappeared before you knew it.'):
        'Il Segno letale che ti era stato inciso addosso è svanito senza che te ne accorgessi.',

    # --- il Ragnarok. ⚠️ «Let's Ragnarok!» e' una battuta dell'inglese; il
    #     giapponese (終末の日が訪れた) e' solenne, e arbitra lui.
    (4641, "Let's Ragnarok!"):
        'È giunto il giorno della fine.',
    # copiata da db_creature.hsp:101104, 「カーテンコールも終わりだ」
    (4650, ' *Curtain Call* '):
        ' *Chiamata alla ribalta* ',

    # --- *rest
    (4722, 'You lie down to rest.'):
        'Ti sdrai a riposare.',
    (4758, 'After a short while, you drop off to sleep.'):
        'Poco dopo scivoli nel sonno.',
    (4765, 'You finished taking a rest.'):
        'Hai finito di riposare.',

    # --- il pasto degli alleati. ⚠️ `have(cc)` e' morfologia inglese e va tolta;
    #     la forma e' quella che questo file usa gia' a :3145 e :3258,
    #     «name(cc) + " finisce di mangiare."».
    (4832, '  finished eating .'):
        'name(cc) + " finisce di mangiare " + itemname(ci, 1) + "."',
    # ⚠️ il giapponese non ha soggetto (さらに、…も飲んだ), l'inglese lo mette:
    #    qui serve, perche' il messaggio puo' riguardare un alleato qualunque.
    (4838, ' also drank the beverage that came with the food.'):
        'name(cc) + " beve anche la bevanda che accompagnava il pasto."',

    # --- *travel: il mare
    (4850, 'High waves delays your travel.'):
        'Le onde alte rallentano il viaggio.',
    (4850, "It's hard to go against the flow."):
        'Andare controcorrente costa una fatica enorme.',

    # --- *travel: la neve. ⚠️ Le due code sono scambiate nell'inglese: la resa
    #     segue il giapponese di CIASCUNA riga, non l'inglese che le sta sopra.
    (4872, 'Snow delays your travel.'):
        'La neve rallenta il viaggio.',
    # jp 雪道を進むのは大変な苦労だ — la fatica, non il banco di neve
    (4872, 'You are caught in a snowdrift.'):
        'Avanzare nella neve è una fatica enorme.',
    # jp 深い雪に脚をとられている — le gambe che affondano, non la fatica
    (4872, "It's hard to walk on a snowy road."):
        'Le gambe affondano nella neve alta.',
    (4879, 'You are too hungry. You chow down snow.'):
        'La fame è troppa: ti ingozzi della neve accumulata.',

    # --- *travel: il deserto. ⚠️ L'inglese dice «robs ME of MY strength».
    (4906, 'The desert heat robs me of my strength.'):
        'Il calore del deserto ti prosciuga le forze.',
    (4906, 'The sun shines mercilessly...'):
        'Il sole picchia senza pietà...',

    # --- *travel: il diluvio
    (4934, "It's raining heavily. You lose your way."):
        'Piove così forte che non capisci più dove stai andando!',
    (4934, "You can't see a thing!"):
        'La visibilità è ridotta a zero.',
    (4934, "You can't see an inch of front of you."):
        'Il diluvio non ti lascia vedere un palmo davanti.',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005, dove cinque rese
# su 43 sono uscite decomposte ('a' + U+0300) e solo `verifica` se n'e' accorta.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

# ⚠️ riga COMMENTATA: il blocco MANUSCRIPT HINT (:4950-4962) e' spento per
# intero. Vedi rinviate.jsonl.
RINVIATE = {
    (4958, 'While travelling, you accumulated some ideas for writing a book. '),
}

USCITA = 'lavoro/fase4-proc-006.jsonl'
DA, A = 4201, 5000

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

# rete 6, nuova qui: nessuna voce del lotto deve stare su una riga commentata.
# Il caso e' reale in questa zona (:4958) e nella 27ª ne aveva prodotti quattro
# in db_creature.hsp, uno dei quali era l'ultimo «nome da fare» del file.
sorgente = io.open(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\proc.hsp',
                   encoding='cp932').read().split('\n')
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2 e 6')

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
