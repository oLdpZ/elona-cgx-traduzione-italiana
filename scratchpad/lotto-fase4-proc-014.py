# -*- coding: utf-8 -*-
"""Lotto fase4-proc-014: pergamene, potenziale, dèi, decapitazioni
(proc.hsp 11500-12500).

50 rese e **una rinviata**. `proc.hsp` passa a 613 su 1.098 (56%).

⚠️⚠️ **La scoperta del lotto: la rete 6 non vedeva i commenti di blocco.**
`:11796` («Caution! While the spell bonus is 100 or more...») e' dentro un
blocco

    /********** ORIGINAL - BEGINNING ********** // Remove skill bonus limit.
    ...
     ********** ORIGINAL - ENDING **********/

cioe' il codice di monte che il mod ha **spento** per togliere il tetto ai punti
bonus. La rete 6 guarda solo le righe che cominciano per `;`, quindi l'avrebbe
lasciata passare: e' la stessa classe di `:4958` (la riga commentata del lotto
006) in una forma che nessuno aveva misurato. ✅ Rete 6 allargata ai blocchi
`/* ... */` con `scratchpad/commenti-blocco.py`.

💡 **E la misura sul dizionario intero dice che era gia' successo**: **7 voci
tradotte stanno dentro un blocco spento** — 6 in `action.hsp`, 1 in `proc.hsp`
(`:1000`, la versione originale dell'incasso delle esibizioni, sostituita dal
blocco `ANNA CUSTOM`). Non e' un difetto a schermo, e' lavoro speso su testo che
il giocatore non legge. `proc.hsp` ne ha **99** di righe spente in tutto.

⚠️ **E la misura ha trovato un secondo inganno prima di dare il numero giusto**:
fatta sulla **build** accusava anche due voci di `text.hsp` che sono giuste. La
build di `text.hsp` ha **una riga in piu'** del sorgente (12.528 contro 12.527),
perche' una toppa ne ha aggiunta una, e da li' in giu' i numeri di riga del
dizionario — che vengono dal **sorgente pinnato** — non tornano piu'. Gli
strumenti che incrociano numeri di riga e dizionario vanno puntati sul
`SORGENTE`, non sulla `build`. ⚠️ Vale anche per `dossier.py` e per la rete 6.

⚠️ **La rete 8 sbagliava, ed e' il caso che la ripresa descrive.** A `:11893` e
`:11898` la resa giusta e' «il potenziale di » + `valn`, e la rete la bocciava
perche' `valn` e' nella sua lista. Ma `valn` non e' sempre la stessa cosa: due
righe sopra il sorgente dice `valn = skillname(i)`, e i nomi di abilita' non
portano articolo («Forza», «Destrezza»), a differenza degli `itemname()` della
35a. ✅ La rete adesso **legge l'assegnamento piu' vicino** e si arrabbia solo se
`valn` viene da un `itemname()`. E' la lezione della 35a resa meccanica: il modo
di sapere che cos'e' `valn` e' guardare da dove viene.

⚠️ **`his2` della 36a ha un fratello: `godname()` restituisce inglese.**
`god.hsp:81-89` scrive `godname(2) = lang("風のルルウィ", "Lulwy of Wind")`, e
`god.hsp` **non ha dizionario** — e' uno dei 40 file mai estratti. Quindi
`:11749` a schermo dira' «lo sguardo benevolo di **Lulwy of Wind**» finche'
`god.hsp` non e' tradotto. Non e' un difetto della resa, e' la dipendenza nota
di `his(tc, 1)` a `:8849` in forma nuova. 💡 E quando si tradurra': `sdim
godname, 20, 9` da' 20 byte e «Kumiromi del Raccolto» ne occupa 21.

💡 **Nove rese su cinquanta sono copie o calchi di decisioni gia' prese**, non
scelte nuove: `:11613` e `:11703` copiano `action.hsp` (stesso inglese, stesso
giapponese), `:12060` copia «ferma il tempo», `:12011`/`:12016` le due scoperte
di `action.hsp`, `:11979`/`:11982` prendono i nomi da `skill.hsp:570`/`:575`,
`:12145` la forma «mana di ricarica (Riserva: )» da `action.hsp:15075`, `:12084`
la resa del **macro** `txt_nothinghappens`.

⚠️ **Due divergenze vecchie trovate cercando, e tutt'e due corrette a parte**
(`scratchpad/correzione-014.py`, vedi `decisioni.md`):
  1. «Nothing happens...» esisteva in **due** rese: `text.hsp:1`, che e' il
     `#define global txt_nothinghappens` usato da tutto il gioco («Non succede
     niente...»), e `action.hsp:8936` («Non succede nulla...»). Vince il macro.
  2. 「小さなメダル」 e' **«medaglietta»** in `db_item.hsp:144256`, ma
     `action.hsp:6254` diceva «Trovi una **monetina**!». Si trovava una monetina
     e ci si ritrovava una medaglietta nello zaino. E' il `Bolt` della 35a in
     miniatura, e nasce dall'inglese di monte, che scrive `small coin` nel
     messaggio e `small medal` nel nome.

⚠️ **Il genitivo davanti a `name()` non esiste**, e questa zona ne chiedeva
sette: `name()` porta gia' l'articolo («il putit») ma non sempre («Sinaha»),
quindi ne «di » ne «del » funzionano. La strada e' quella che `proc.hsp:8759` e
`:8786` avevano gia' aperto senza dichiararla — il **`-ne` enclitico**:
«colpisce X facendo**ne** saltare la testa». Dove non bastava, il nome e'
diventato complemento oggetto («attacca X puntando alla testa»).

⚠️ **`:11870` e' un errore dell'inglese di monte, il settimo della serie.**
L'inglese ripete parola per parola la riga `:11856` («blood burns and a new
strength fills his body»), mentre il giapponese dice tutt'altro: 「さらに速度の
潜在能力が最大まで回復した」, cioe' il potenziale di **Velocita'** riportato al
massimo. Reso sul giapponese, come le sei della 35a.
"""
import collections
import glob
import io
import json
import re
import unicodedata

RESE = {
    # --- l'aura di purificazione. `uncurse` -> «purificare», da skill.hsp:469
    # ⚠️ Sono DINAMICHE (l'inglese porta `his(tc)`, che in italiano sparisce) ma
    #    la resa non ha piu' nessuna funzione: va comunque scritta come
    #    espressione HSP, cioe' fra virgolette. Vedi la rete 12.
    (11534, 'The aura uncurses some  stuff.'):
        '"Qualche oggetto è stato purificato."',
    (11541, 'The aura uncurses some of  equipment.'):
        '"Una parte dell\'equipaggiamento indossato è stata purificata."',
    (11547, 'Several items resist the aura and remain cursed.'):
        'Qualche oggetto resiste e resta maledetto.',

    # --- gli artefatti
    (11569, 'You hear a sepulchral whisper but the voice is too small to distinguish a word.'):
        'Qualcosa ti sussurra all\'orecchio, ma non riesci a capire una parola.',
    # `artifact` -> «artefatto», da skill.hsp:475
    (11573, 'No artifacts have been generated yet.'):
        'Non è ancora stato generato nessun artefatto.',

    # --- la pergamena della stregoneria: teste di frase montate su `s`
    (11606, 'Suddenly, '):
        'All\'improvviso, ',
    # ⚠️ «Futhermore» e' il refuso di monte per «Furthermore»
    (11609, 'Futhermore, '):
        'Inoltre, ',
    # copiata da action.hsp:1092, stesso inglese
    (11613, 'you gain knowledge of a spell, .'):
        's + "hai imparato l\'incantesimo " + skillname(p) + "."',
    (11625, 'Suddenly, you lose knowledge of a spell, .'):
        '"All\'improvviso, hai dimenticato l\'incantesimo " '
        '+ skillname(p + STARTING_SKILL_SPELL) + "."',

    # --- livelli e abilità
    (11655, ' lose a level...'):
        'name(tc) + " scende di livello..."',
    (11668, ' cannot gain a level...'):
        'name(tc) + " non può salire di livello..."',
    # copiata da action.hsp:9429, stesso giapponese
    (11703, ' gain a skill of !'):
        'name(tc) + " ha imparato " + skillname(p) + "!"',

    # --- gli dèi. ⚠️ godname() resta inglese finché god.hsp non è tradotto
    (11737, 'Your god doubts your faith.'):
        'Il tuo dio dubita della tua fede.',
    (11749, 'You feel as if  is watching you.'):
        '"Senti su di te lo sguardo benevolo di " '
        '+ godname(cdata(CDATA_GOD, CHARA_PLAYER)) + "."',
    # 三つ葉 e' il trifoglio: il quadrifoglio sarebbe 四つ葉, e la battuta e'
    # che il dio della fortuna manda quello che porta fortuna a nessuno
    (11751, 'A three-leaved clover falls from the sky.'):
        'Dal cielo cade un trifoglio.',
    # il «5» sta nell'inglese e non nel giapponese, e il codice gli da' ragione:
    # `gdata(...) += 5` alla riga 11787, l'unica riga viva del blocco
    (11773, 'You gain 5 spell bonus points.'):
        'Ottieni 5 punti bonus per gli incantesimi.',

    # :11796 e' RINVIATA: sta dentro un blocco spento. Vedi la nota in cima.

    # --- il potenziale. La coppia «vede crescere/calare» tiene il parallelo e
    #     non fa concordare nessun participio col soggetto.
    (11820, 'The potentials of  skills increase.'):
        'name(tc) + " vede crescere il potenziale delle abilità."',
    (11827, "The potentials of 's skills decreases."):
        'name(tc) + " vede calare il potenziale delle abilità."',
    (11856, ' blood burns and a new strength fills  body!'):
        'name(tc) + " sente il sangue ribollire e una forza nuova nel corpo!"',
    # ⚠️ reso sul giapponese: l'inglese qui ricopia :11856. Vedi la nota in cima.
    (11870, ' blood burns and a new strength fills  body!'):
        '"Inoltre, " + name(tc) + " riporta al massimo il potenziale di Velocità."',
    # 主能力 -> «attributi», da proc.hsp:4585
    (11883, ' potential of every attribute expands.'):
        'name(tc) + " vede crescere il potenziale di ogni attributo."',
    # ⚠️ qui `valn = skillname(i)` (riga 11891): niente articolo, «di » ci sta
    (11893, ' potential of  expands.'):
        'name(tc) + " vede crescere il potenziale di " + valn + "."',
    (11898, ' potential of  decreases.'):
        'name(tc) + " vede calare il potenziale di " + valn + "."',
    (11927, ' vanish.'):
        'name(tc) + " svanisce."',

    # --- percezione e mappa. I nomi vengono da skill.hsp:570 e :575.
    (11975, 'Hmm? You suffer minor memory defect.'):
        'Eh...? Hai un piccolo vuoto di memoria.',
    (11979, ' sense nearby locations.'):
        'name(tc) + " percepisce il terreno intorno."',
    (11982, ' sense nearby objects.'):
        'name(tc) + " percepisce gli oggetti vicini."',
    # copiate da action.hsp:6238 e :6246
    (12011, 'You discover a trap.'):
        'Scopri una trappola.',
    (12016, 'You discover a hidden path.'):
        'Scopri un passaggio nascosto.',
    # ⚠️ 小さなメダル e' la «medaglietta» di db_item.hsp:144256, non una
    #    monetina: vedi correzione-014.py
    (12022, 'You find a small coin!'):
        'Trovi una medaglietta!',

    # --- il tempo fermo
    (12048, 'Time is already stopped.'):
        'Il tempo è già fermo.',
    # copiata da action.hsp:6012, stesso giapponese
    (12060, ' stop time.'):
        'name(cc) + " ferma il tempo."',
    # la resa del macro `txt_nothinghappens` (text.hsp:1), che e' quella che il
    # giocatore legge dappertutto
    (12084, 'Nothing happens...'):
        'Non succede niente...',

    # --- le azioni speciali di carica
    (12101, '** '):
        '"*" + skillname(efid) + "* "',
    # 魔杖 -> «bacchetta», da db_item.hsp (60 voci)
    (12106, ' released rod power into the sky!'):
        'name(cc) + " libera in cielo il potere della bacchetta!"',
    # forma copiata da action.hsp:15075, «mana di ricarica (Riserva: )»
    (12145, 'You get 10 mana charge. (Total:)'):
        '"Hai ottenuto 10 mana di ricarica. (Riserva: " '
        '+ gdata(GDATA_ABSORB_CHARGE) + ")"',
    (12188, ' attune  with the mana in the air and let out a blast!'):
        'name(cc) + " sintonizza il proprio potere con il mana intorno e lo scatena!"',

    # --- la decapitazione. ⚠️ Sette siti chiedevano il genitivo di name(): la
    #     strada e' il `-ne` enclitico di proc.hsp:8759, o il nome come oggetto.
    (12240, ' aim at  head and attack.'):
        'name(cc) + " attacca " + name(tc) + " puntando alla testa."',
    (12265, ' *Bang* '):
        ' *zac* ',
    (12269, ' blew  head off and'):
        'name(cc) + " colpisce " + name(tc) + " facendone saltare la testa e"',
    (12272, ' blew  head off.'):
        'name(cc) + " colpisce " + name(tc) + " facendone saltare la testa."',
    (12280, ' *Gash* '):
        ' *spruzz* ',
    (12284, ' cut  neck and'):
        'name(cc) + " decapita " + name(tc) + " e"',
    (12287, ' cut  neck.'):
        'name(cc) + " decapita " + name(tc) + "."',
    # ⚠️ stesso giapponese di :12269 e :12272, altro ramo dell'if: stessa resa
    (12313, " blew 's head off and"):
        'name(cc) + " colpisce " + name(tc) + " facendone saltare la testa e"',
    (12316, " blew 's head off."):
        'name(cc) + " colpisce " + name(tc) + " facendone saltare la testa."',
    # マテリアル -> «materiali», la stessa parola di :11165 (lotto 013)
    (12351, ' convert  body to material and'):
        'name(cc) + " riduce " + name(tc) + " in materiali e"',
    (12354, ' convert  body to material.'):
        'name(cc) + " riduce " + name(tc) + " in materiali."',

    # --- il legaccio di pergamene
    (12396, 'Which scrolls?'):
        'Quali pergamene consumare?',
    # il soggetto e' la pergamena, come in giapponese: cosi' il verbo non
    # concorda con tc e non serve sapere se e' maschio o femmina
    (12435, '  entangled in a scroll!'):
        '"Una pergamena avvolge " + name(tc) + "!"',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # ⚠️ Dentro il blocco /* ORIGINAL - BEGINNING ... ORIGINAL - ENDING */ che
    #    il mod ha spento per togliere il tetto di 100 ai punti bonus: il
    #    giocatore non leggera' mai questa riga. Vedi rinviate.jsonl.
    (11796, 'Caution! While the spell bonus is 100 or more, you cannot get new.'),
}

USCITA = 'lavoro/fase4-proc-014.jsonl'
DA, A = 11500, 12500
# ⚠️ il SORGENTE pinnato, non la build: i numeri di riga del dizionario vengono
#    da li'. Vedi la nota in cima.
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'

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

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: nessuna voce del lotto deve stare su una riga spenta (lotto 006).
# ⚠️ Allargata nella 37a ai commenti di BLOCCO: `:11796` sta dentro un
#    /* ORIGINAL ... */ e la vecchia rete, che guardava solo il `;`, la
#    lasciava passare.
import importlib.util  # noqa: E402
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
# ⚠️ Allargata nella 37a: `valn` non e' sempre un `itemname()`. Si legge
#    l'assegnamento piu' vicino sopra la riga — `valn = skillname(i)` a :11891 —
#    e i nomi di abilita' non portano articolo, quindi «di Forza» e' giusto.
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    """Il nome della funzione che riempie `valn` piu' vicino sopra `riga`."""
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

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo.
# ⚠️ Nata nella 37a da un errore del compilatore, non da un'idea: `:11534` e
# `:11541` sono dinamiche perche' l'inglese porta `his(tc)`, ma in italiano la
# morfologia sparisce e la resa resta una frase sola. Scritta senza virgolette,
# `applica.py` — che per le dinamiche NON avvolge niente — l'ha infilata come
# codice, e il compilatore ha letto «qualche» come nome di variabile:
#     proc.hsp(11534) : error 4 : パラメーター式の記述が無効です
# Le nove reti, `verifica` e le guardie l'avevano lasciata passare tutte: e' il
# primo difetto della serie che solo il compilatore poteva vedere.
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO della resa devono essere le stesse
# dell'inglese, nello stesso ordine (verifica.py:367). ⚠️ Solo le DINAMICHE.
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
    raise SystemExit('lotto fermato dalle reti 0-2, 6, 7, 8, 9 e 11')

# ⚠️ Il confronto fra due rese e' sui LETTERALI di testo, non sull'espressione:
# due siti che dicono le stesse identiche parole su variabili diverse
# (`name(cc)` di qua, `name(cnt)` di la') sono la STESSA resa. Nato per la rete 4
# nel lotto 011; nella 37a la rete 3 aveva lo stesso difetto e gridava su
# `:12287`, dove le parole coincidevano gia'.
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
