# -*- coding: utf-8 -*-
"""Lotto fase4-proc-013: bibite, sale, equitazione, pesca, mutazioni, resurrezione
(proc.hsp 10601-11499).

45 rese e **una rinviata**. `proc.hsp` passa a 563 su 1.098 (51%): e' la prima
volta che il file supera la meta'.

⚠️⚠️ **La rinviata e' la scoperta del lotto: `his2()` non e' traducibile, e il
motivo non e' quello che sembrava.** A `:11481` l'inglese e'
`his2(tc) + your2(tc) + " equipment is surrounded by a white aura."`. La prima
lettura e' stata che fosse il gemello di `:10312` del lotto 012 — pronomi
morfologici che cancellano il nome — e la resa scritta di conseguenza, senza
soggetto. **La rete 11 l'ha bocciata**, ed e' andata a finire che aveva ragione
lei: `his2` **non e'** in `MORFOLOGIA_INGLESE`, ed e' giusto che non ci sia.

`init.hsp:1881` dice cosi':

    #defcfunc his2 int EntityID
        if ( EntityID == CHARA_PLAYER ) { return "your" }
        return name(EntityID)

Cioe' `his2()` **porta il nome** — cosa che nessun pronome morfologico fa, e per
questo `funzioni.py` la conta fra le funzioni di contenuto — ma nel ramo del
giocatore restituisce il letterale nudo `"your"`, **fuori da qualunque
`lang()`**. Quel `your` resta inglese per sempre: non lo raggiunge il dizionario
oggi e non lo raggiungera' la traduzione di `init.hsp` domani, perche' non c'e'
niente da tradurre. E' la stessa classe di `bufftxt(1)` della 28a.

⚠️ **E non esiste una resa italiana che regga tutt'e due gli esiti**, perche'
`his2()` restituisce un **possessivo** in un caso («your») e un **nome proprio
con l'articolo** nell'altro («il putit»): non c'e' slot di frase dove ci stiano
tutt'e due. Quindi la voce e' **rinviata a toppa** (`rinviate.jsonl`), e la
toppa e' fatta nella stessa sessione: riporta la riga alla forma del ramo
giapponese, che di nomi ne usa uno solo.

💡 **Il valore della rete 11 e' proprio qui.** Era nata nel lotto 012 per dire
«non aggiungere funzioni»; qui ha detto «ne manca una», e la funzione mancante
era la prova che la mia lettura del sito era sbagliata.

⚠️ **`:10641` e' un caso nuovo: l'inglese ha perso l'onomatopea.** Il giapponese
scrive 「*シュワワ* 刺激的！」 — シュワワ e' il **frizzare** di una bibita
gassata — e l'inglese ci mette `*quaff*`, che e' il rumore della **deglutizione**
e che usa in altri cinque siti di questa stessa zona per 「*ごくっ*」 e
「*ごくり*」. Non e' l'inglese che specializza: e' l'inglese che appiattisce
due suoni diversi su uno solo. L'italiano tiene la differenza — `*gluc*` per il
sorso, `*frizz*` per la bollicina.

⚠️ **Quattro rese sono copie di decisioni gia' prese, non scelte nuove:**
`tag team` -> «coppia» (`skill.hsp:1477`, `action.hsp:10861`), `undead` ->
«non morti» (`skill.hsp:1493`), 「クズ」 -> «spazzatura» (`db_item.hsp:152176`),
「ありがとう！」 -> «Grazie!» (`text.hsp:1994`). E `:10612` copia la resa di
`proc.hsp:7705` del lotto 010, che ha lo stesso inglese.

⚠️ **`:11171` interpola una parola che cambia numero e genere.** La frase e'
`"Some " + s + " fall from above!"`, dove `s` viene da `:11165`/`:11168` e vale
«materiali» (maschile plurale) o «spazzatura» (femminile singolare). Qualunque
verbo accordato ne sbaglierebbe uno: «piovono materiali» ma «piove spazzatura».
La strada e' un **sintagma nominale** — «Una pioggia di … dall'alto!» — dove
`s` sta dopo una preposizione semplice e non accorda con niente.

⚠️ **Tre rese riscritte per la rete 8**, tutte nell'equitazione: «Scendi **da** »
+ `name()` darebbe «da il cavallo». La strada e' il verbo transitivo — «Lasci il
cavallo e scendi a terra».
"""
import collections
import glob
import io
import json
import re
import unicodedata

RESE = {
    # --- le bibite. ⚠️ *gluc* per il sorso, *frizz* per la bollicina: l'inglese
    #     usa `*quaff*` per tutt'e due (vedi la nota in cima).
    # 「げふぅ」 e' lo stesso rutto di :10241, ma li' la frase ha la cornice
    # («X borbotta …») e qui e' il suono nudo, come nell'inglese.
    (10601, '*Ughu*'):
        '*Buurp*',
    # copiata da proc.hsp:7705 (lotto 010), stesso inglese
    (10612, ' gain weight.'):
        'name(tc) + " diventa più pesante."',
    (10622, '*quaff* It seems to help my circulation.'):
        '*gluc* Sembra faccia bene alla circolazione.',
    # ⚠️ シュワワ e' il frizzare, non il sorso: l'inglese li appiattisce
    (10641, '*quaff* Refreshing!'):
        '*frizz* Che sprint!',
    (10642, ' restore some stamina.'):
        'name(tc) + " recupera un po\' di vigore."',
    # copiata da proc.hsp:10582 (lotto 012), stesso inglese
    (10656, ' *quaff* '):
        ' *gluc* ',
    (10657, ' greatly restore stamina.'):
        'name(tc) + " recupera parecchio vigore."',

    # --- il sale, e la macchina che lo teme
    (10669, 'Anti-salt system activated.'):
        'Sistema antisale attivato.',
    (10677, "It's salt!  start to melt."):
        '"È sale! " + name(tc) + " comincia a sciogliersi!"',
    (10691, 'Salty!'):
        'Salatooo!',
    (10700, '*quaff* Yucky!'):
        '*gluc* Che sapore orrendo!',

    # --- il borseggio e l'equitazione
    (10712, 'You have no time for it!'):
        'Non è il momento per queste cose!',
    (10749, "There's no place to get off."):
        'Non c\'è spazio per scendere.',
    # rete 8: «Scendi da » + name() darebbe «da il cavallo»
    (10754, 'You dismount from .'):
        '"Lasci " + name(gdata(GDATA_RIDER)) + " e scendi a terra."',
    (10757, ' dismounts from you.'):
        'name(gdata(GDATA_RIDER)) + " ti scende di dosso."',
    # `tag team` -> «coppia», da skill.hsp:1477 e action.hsp:10861
    (10793, 'You need to dissolve the tag-team.'):
        'Prima devi sciogliere la coppia.',
    (10797, 'You can only ride an ally.'):
        'Puoi cavalcare solo un alleato.',
    # 護衛対象 e' chi stai scortando: l'inglese dice «client»
    (10801, "You can't ride a client."):
        'Non puoi cavalcare chi hai sotto scorta.',
    (10806, 'You try to ride yourself.'):
        'Provi a salire su te stesso.',
    (10811, 'The ally currently stays in this area.'):
        'Quell\'alleato è di stanza qui.',
    (10816, '  currently riding .'):
        'name(cc) + " sta già cavalcando " + name(gdata(GDATA_RIDER)) + "."',
    # ⚠️ qui i due nomi sono scambiati rispetto a :10816: e' l'alleato che
    #    cavalca il giocatore. L'inglese ha ragione, il giapponese lo dice al
    #    contrario («X sta portando Y in groppa»), e il senso e' lo stesso.
    (10819, '  currently riding .'):
        'name(gdata(GDATA_RIDER)) + " sta cavalcando " + name(cc) + "."',

    # --- suonare e pescare
    (10894, " n't know how to play an instrument."):
        'name(cc) + " non sa suonare."',
    (10939, "You don't know how to fish."):
        'Non sai pescare.',
    # jp: «la canna non ha l'esca», che e' piu' preciso di «ti serve un'esca»
    (10947, 'You need a bait to fish.'):
        'La canna non ha l\'esca.',
    (10977, "This isn't a good place to fish."):
        'Qui non si vede un posto dove pescare.',
    (10982, "You can't fish while swimming."):
        'Non si pesca stando in acqua.',
    (11017, 'How many hours do you fish?'):
        'Per quante ore peschi?',

    # --- le maledizioni e le mutazioni
    (11033, ' hear devils laugh.'):
        'name(tc) + " sente ridere i demoni."',
    (11151, 'A golden aura envelops !'):
        '"Un\'aura dorata avvolge " + name(tc) + "!"',
    (11165, 'materials'):
        'materiali',
    # 「クズ」 -> «spazzatura», da db_item.hsp:152176
    (11168, 'junks'):
        'spazzatura',
    # ⚠️ `s` vale «materiali» (m. pl.) o «spazzatura» (f. sing.): nessun verbo
    #    accordato regge tutt'e due. Il sintagma nominale non accorda con niente.
    (11171, 'Some  fall from above!'):
        '"Una pioggia di " + s + " dall\'alto!"',
    (11248, 'You feel yourself changing.'):
        'Senti che stai cambiando.',
    (11268, ' cast an insane glance on .'):
        'name(cc) + " fissa " + name(tc) + " con uno sguardo folle."',
    # «attecchire» toglie l'accordo che «hai resistito» porterebbe
    (11280, 'You resist the threat of mutation.'):
        'La mutazione non ti attecchisce.',
    (11328, 'You mutate.'):
        'Ti trasformi!',
    # «maledetto» concorderebbe con l'oggetto, che qui non e' nominato
    (11358, "It's cursed!"):
        'Porta una maledizione!',
    # «avvicinato» concorderebbe col giocatore: il sintagma nominale no
    (11381, 'You are now one step closer to your normal self.'):
        'Un passo in più verso com\'eri prima.',

    # --- la resurrezione
    (11424, "Your party is full. You can't invite anyone else."):
        'Il gruppo è al completo: non puoi richiamare nessuno.',
    # `undead` -> «non morti», da skill.hsp:1493
    (11428, 'Hordes of undead arise from hell!'):
        'Dall\'oltretomba si levano i non morti!',
    (11445, 'It can not be revived until you switch area.'):
        'Non può tornare in vita finché non cambi mappa.',
    # 冥界 -> «oltretomba», la stessa parola dei Soffi di skill.hsp
    (11450, " prayer doesn't reach the underworld."):
        'name(cc) + " non ha la forza di arrivare all\'oltretomba."',
    # copiata da text.hsp:1994
    (11462, 'Thanks!'):
        'Grazie!',

    # :11481 e' RINVIATA e toppata: vedi la nota in cima e rinviate.jsonl.
    (11486, '  surrounded by a holy aura.'):
        '"Una luce sacra avvolge " + name(tc) + "."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # ⚠️ `his2()` non ha nessun lang(): restituisce il letterale nudo "your" per
    #    il giocatore e name() per gli altri. Non e' traducibile dal dizionario,
    #    e nessuna resa italiana regge tutt'e due gli esiti. Rinviata a toppa,
    #    fatta nella stessa sessione. Vedi rinviate.jsonl.
    (11481, ' equipment is surrounded by a white aura.'),
}

USCITA = 'lavoro/fase4-proc-013.jsonl'
DA, A = 10601, 11499

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

# rete 11: le funzioni di CONTENUTO della resa devono essere le stesse
# dell'inglese, nello stesso ordine (verifica.py:367). ⚠️ Solo le DINAMICHE:
# una statica dentro `cnvtalk(...)` ha l'involucro nell'en_grezzo ma la resa e'
# testo nudo. ⚠️ E non se ne puo' AGGIUNGERE nessuna, nemmeno per dire quello
# che dice il giapponese: vedi :10312 (lotto 012) e :11481 (qui).
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
# ⚠️ Il confronto e' sui LETTERALI di testo, non sull'espressione (lotto 011).
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
