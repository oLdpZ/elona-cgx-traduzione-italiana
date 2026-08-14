# -*- coding: utf-8 -*-
"""Lotto fase4-proc-017: navi, ricarica, muri e porte, le azioni speciali di
barra, meteore, cannone di sabbia, circolo di lettura (proc.hsp 15500-16999).

49 rese, nessuna rinviata. `proc.hsp` passa a 758 su 1.098 (69%).

⚠️⚠️ **`studybuddy` e' un letterale inglese nudo, e la resa non lo puo' usare.**
A `:16991` l'inglese e' `"You started a reading party with " + studybuddy + "."`,
e `studybuddy` viene assegnato venti righe sopra:

    16976: if ( studybuddy == "" ) { studybuddy = name(tc) }
    16980: else                     { studybuddy = "your friends" }

Il ramo `else` — cioe' **ogni volta che i compagni sono piu' di uno** — mette un
letterale inglese **fuori da `lang()`**, e nessun dizionario lo raggiunge: a
schermo si leggerebbe «Cominci un circolo di lettura con **your friends**.» E' la
stessa classe di `his2()` della 36a e di `bufftxt(1)` della 28a, in una forma
nuova: non una funzione che restituisce inglese, ma **una variabile che se lo
porta dentro**. Il giapponese non usa `studybuddy` («あなたと仲間たちは») e la
resa lo segue.
💡 ⚠️ **E questa famiglia non la vede nessuno dei due referti**: `blocchi_en.py`
cerca i letterali dentro `if ( en )`, `else_jp.py` quelli dentro
`if ( jp ) ... else`, e `:16980` non sta ne' nell'uno ne' nell'altro — e' un
assegnamento incondizionato. Quante altre variabili si portino dentro l'inglese
non lo ha mai contato nessuno.

⚠️ **Due errori nuovi dell'inglese di monte, e sono lo stesso copia-e-incolla.**
«These walls seem to resist your magic» e' giusto a `:15976` (parla davvero di
muri) ed e' ricopiato tale e quale su altri due siti dove il giapponese dice
tutt'altro:
  - `:16001` 「むぅ 最大の奥義がかき消されるとは！」 — il 崩山破 annullato
    dentro l'arena, la piramide, la prigione o la mappa del mondo;
  - `:16679` 「隕石は大気圏で燃え尽きてしまったようだ…。」 — le meteore che si
    consumano nell'atmosfera, stesso controllo d'area, stessa struttura.
Sono il dodicesimo e il tredicesimo della serie. **Resi sul giapponese**, e la
rete 13 li pesca da sola perche' un inglese sta per tre giapponesi diversi.

💡 **`:16087` copre due siti, non uno.** `proc.hsp` porta **due blocchi
identici** per Tiro a segno — `_switch_val == 738` a `:16079` e
`_switch_val == SKILL_SPACT_STRUCK_OUT` a `:16251` — con lo stesso corpo e lo
stesso `txt`. Il secondo non entra nell'estrazione perche' il dizionario e'
indicizzato per **firma**, non per riga, e `applica.py` porta la resa su tutt'e
due. Non e' una voce persa.

⚠️ **`:16520` e' una statica il cui GIAPPONESE nomina il bersaglio.**
「過剰なまでの癒しの力が」+ name(tc) + 「の体組織を崩壊させる…！」, mentre
l'inglese dice «tissue of target» e non interpola niente. La voce e' `statica`, e
**nessuna statica del dizionario porta un'espressione** (misurato: 0 su tutte).
La resa segue l'inglese e dice «del bersaglio»: il nome si perde, ed e' una
perdita di monte, non una scelta.

💡 **Otto rese vengono da una famiglia gia' decisa**, e non sono state ridecise:
`itemname(ci) + " resiste."` (`action.hsp:12920`), «Miamiamiao!»
(`skill.hsp:1096`), «Un'aura dorata avvolge X» (`proc.hsp:11151`), «X colpisce
name(tc) e» / «X colpisce name(tc).» (la famiglia 命中, quattordici siti),
«mana di ricarica» con «(Rimasto:» e «(Riserva:» (`action.hsp:10327`,
`proc.hsp:12145`), «Non hai abbastanza denaro» (`text.hsp:133`), «Va letto...»
(`proc.hsp:15489`), e i quattro nomi di azione speciale presi da `skill.hsp`:
**Tiro a segno** (`:1464`), **Sciame** (`:984`), **Lumaca lucente** (`:1128`),
**Elementia** (`:1140`).

⚠️ **Sette rese girano la frase per non far concordare un participio.** L'inglese
scrive `is2()`/`was()`/`_s()` — «is surrounded», «is recharged», «was struck by
debris», «becomes as light as a feather» — e in italiano concorderebbero con un
oggetto o un personaggio di genere ignoto. La strada e' quella del lotto 016: la
sostanza diventa **soggetto** («Le schegge colpiscono X», «Un'aura dorata avvolge
X», «Il luccichio abbaglia X») oppure il verbo diventa **riflessivo** («si
ricarica», «si trasforma», «cambia forma»). Dove serviva un aggettivo, l'accordo
si sposta su un **nome**: «acquista la leggerezza di una piuma», «acquista il
peso di un macigno».

⚠️ **La rete 3 gridera' su `:16831`/`:16834`, ed e' legittimo.** Il giapponese
「に命中し」 e' identico a quello di `proc.hsp:9811`/`:9814`, reso «Il soffio
colpisce X e» / «Il soffio colpisce X.»: e' il **soffio** di `SKILL_SPACT_MP_
BREATH`, mentre qui siamo in `SKILL_SPACT_SAND_CANNON` (砂塵砲, «Cannone di
sabbia»). Il giapponese non nomina il proiettile, l'inglese si' («The sand hits»
contro «The breath hits»), e **la differenza la impone il sorgente**. E' la
stessa forma del 「この場所では効果がない。」 del lotto 016.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il mezzo di trasporto sulla mappa del mondo e la nave.
    #     乗り物 -> «mezzo»: non e' nel dizionario, e il solo parente e'
    #     db_item.hsp:135815 (大型馬車 «carrozza»), che e' UNO dei mezzi.
    (15511, 'You decide to travel on foot instead of using a vehicle.'):
        'Hai deciso di viaggiare a piedi invece di usare un mezzo.',
    (15524, 'You called the world-vehicle out to the suburbs.'):
        'Hai chiamato subito il mezzo fuori città.',
    # famiglia di proc.hsp:15489 «Va letto fuori dalla mappa del mondo.»
    (15544, 'You need to read it while you are in the town by the sea.'):
        'Va letto in una città che si affaccia sul mare.',
    # gp -> «oro» (text.hsp:193, proc.hsp:3421). La forma «Costa X. Fare Y?» e'
    # quella di action.hsp:12355.
    (15571, 'Do you pay gp for insurance and set sail?'):
        '"L\'assicurazione costa " + cost + " d\'oro. Salpare?"',
    # copiata da text.hsp:133, stesso senso e stesso registro
    (15584, "You don't have enough money."):
        'Non hai abbastanza denaro...',

    # --- l'incantamento dell'equipaggiamento. «avvolto» concorderebbe con
    #     l'oggetto: l'aura diventa soggetto, come a proc.hsp:11151.
    (15645, '  surrounded by a golden aura.'):
        '"Un\'aura dorata avvolge " + itemname(ci) + "."',
    # copiata da action.hsp:12920, stesso giapponese e stesso inglese
    (15649, ' resist.'):
        'itemname(ci) + " resiste."',

    # --- la ricarica. 充填 -> «ricarica» (db_item:145740, skill.hsp:980),
    #     魔力の貯蓄 -> «mana di ricarica» (action.hsp:10196, :10327).
    (15672, 'You need at least 10 mana charge to recharge items.'):
        'Per caricare un oggetto servono almeno 10 mana di ricarica.',
    # «(Rimasto:» e' la forma di action.hsp:10327, stesso giapponese (残り)
    (15676, 'You spend 10 mana charge. (Remaining:)'):
        '"Hai consumato 10 mana di ricarica. (Rimasto: " + gdata(GDATA_ABSORB_CHARGE) + ")"',
    (15687, "You can't recharge this item."):
        'Quell\'oggetto non si può ricaricare.',
    (15695, ' cannot be recharged anymore.'):
        'itemname(ci) + " non si può ricaricare oltre."',
    # «ricaricato» concorderebbe con l'oggetto: il verbo diventa riflessivo
    (15723, '  recharged by +.'):
        'itemname(ci) + " si ricarica (+" + p + ")"',
    (15733, ' explode.'):
        'itemname(ci) + " esplode."',
    (15738, 'You fail to recharge .'):
        '"Non riesci a ricaricare " + itemname(ci) + "."',
    # «(Riserva:» e' la forma di proc.hsp:12145, stesso giapponese (計)
    (15795, 'You destroy  and extract  mana charge. (Total:)'):
        '"Distruggi " + itemname(ci) + " e ne estrai " + p + " mana di ricarica. '
        '(Riserva: " + gdata(GDATA_ABSORB_CHARGE) + ")"',

    # --- la trasmutazione. 変化 -> «cambiare forma» (buff.hsp:192),
    #     変容 -> «trasformarsi» (proc.hsp:11328).
    (15819, ' change.'):
        'name(tc) + " cambia forma."',
    (15832, ' cannot be changed.'):
        'name(tc) + " non può cambiare forma."',
    # «leggero»/«pesante»: il primo concorderebbe con l'oggetto. L'accordo si
    # sposta su un nome, e le due rese restano simmetriche.
    (15855, ' becomes as light as a feather.'):
        'itemname(ci, 1) + " acquista la leggerezza di una piuma."',
    (15859, ' becomes heavy.'):
        'itemname(ci, 1) + " acquista il peso di un macigno."',
    # «diventato» concorderebbe con l'oggetto vecchio, che qui non e' nominato
    (15920, 'It metamorphosed into .'):
        '"Si trasforma e diventa " + itemname(ci, 1) + "."',

    # --- i muri e le porte. Il giapponese descrive il pavimento che si solleva,
    #     l'inglese il muro che appare: la resa tiene tutt'e due.
    (15961, 'A wall appears.'):
        'Dal pavimento si alza un muro.',
    (15976, 'These walls seem to resist your magic.'):
        'Questi muri sembrano resistere alla magia.',
    (15979, 'A door appears.'):
        'Appare una porta.',

    # --- 崩山破. L'inglese e' un grido, il giapponese una descrizione, e il
    #     verso vero e' quello di :16001, che sta fra le virgolette giapponesi.
    (15998, 'Haaaaaaaaaa!'):
        'Dal terreno erompono fiotti di energia senza fine!',
    # ⚠️ reso sul giapponese: l'inglese ricopia la riga dei muri di :15976
    (16001, 'These walls seem to resist your magic.'):
        'Mmh! Che l\'arte suprema venga cancellata così...!',

    # --- Corsa all'oro (skill.hsp:1148). Yacatect parla in kansai e il
    #     dizionario la rende in tono sbrigativo (action.hsp:14116).
    #     «imbecille» e' invariabile: il bersaglio puo' essere chiunque.
    (16061, '*Ooban-Burumai*'):
        'Ma insomma! Che imbecille!!!',
    # «accecato» concorderebbe con tc: il luccichio diventa soggetto
    (16072, ' dazzle.'):
        '"Il luccichio abbaglia " + name(tc) + "!"',
    # ⚠️ copre anche :16259, che e' lo stesso txt in un blocco gemello.
    #    Il nome dell'azione e' skill.hsp:1464.
    (16087, 'Struck Out!'):
        'Tiro a segno!',
    (16140, ' smash the ground!'):
        'name(cc) + " spacca il terreno!"',
    # «colpito» concorderebbe con tc: le schegge diventano soggetto, e la
    # forma e' quella della famiglia 命中 (proc.hsp:7903 e altri tredici siti)
    (16170, '  struck by debris.'):
        '"Le schegge colpiscono " + name(tc) + "."',
    # skill.hsp:984
    (16189, 'Swarm!'):
        'Sciame!',
    (16318, ' drop something on the ground.'):
        'name(cc) + " lascia cadere qualcosa a terra."',
    # il giapponese porta i turni, l'inglese li perde: si tengono
    (16345, ' feel gravity.'):
        'name(tc) + " sente la gravità per " + gra + " turni."',
    # copiata da skill.hsp:1096, stesso giapponese e stesso inglese
    (16368, 'Mewmewmew!'):
        'Miamiamiao!',

    # --- i versi delle azioni speciali. Sono `cnvtalk()` nell'inglese e 「」
    #     nel giapponese: la resa e' testo nudo, l'involucro lo mette il codice.
    (16425, 'Delete.'):
        'Le funzioni superflue vanno cancellate.',
    (16469, 'Muwahahahaha!'):
        'Beccati questo! Muahahahah!',
    # ⚠️ statica: il name(tc) del giapponese non si puo' tenere. Vedi la nota.
    (16520, 'Excessive heal power break tissue of target!'):
        'Un potere curativo eccessivo distrugge i tessuti del bersaglio!',
    # skill.hsp:1128 «Lumaca lucente». Le vocali si allungano come nel giapponese
    (16568, 'OK? Shine-Snail!!'):
        'Uoooooh! Luuumaca luceeenteee!!',
    # skill.hsp:1140 tiene «Elementia» come nome
    (16599, 'Complete Elementia!'):
        'Io guido: armonia degli elementi, compiti! Magia elementale suprema, Elementia!',
    # Corsa all'oro, di nuovo Yacatect
    (16645, 'This is my rush!'):
        'Guarda un po\' che assalto dorato ti scateno addosso!',

    # --- Meteora (skill.hsp:784).
    # ⚠️ reso sul giapponese: l'inglese ricopia la riga dei muri di :15976
    (16679, 'These walls seem to resist your magic.'):
        'Le meteore sembrano essersi consumate nell\'atmosfera...',
    (16684, ' meteorites fall all over the area!'):
        '"Piovono " + efp + " meteore sulla zona!"',

    # --- Esplosione di mana (skill.hsp:1136). «il mana», maschile, come a
    #     proc.hsp:14607 «assorbe il mana dall'aria».
    (16726, ' released own mana.'):
        'name(cc) + " libera il proprio mana."',
    # famiglia di proc.hsp:9695, dove lo stesso giapponese e' «scatena»
    (16776, ' blast .'):
        'name(cc) + " scatena " + skillname(efid) + "."',

    # --- Cannone di sabbia (skill.hsp:1848). ⚠️ Il giapponese non nomina il
    #     proiettile e coincide con quello del soffio: vedi la nota in cima.
    (16831, 'The sand hits  and'):
        '"La sabbia colpisce " + name(tc) + " e"',
    (16834, 'The sand hits .'):
        '"La sabbia colpisce " + name(tc) + "."',

    # --- Circolo di lettura (skill.hsp:1548).
    (16943, 'Which book?'):
        'Che cosa vuoi leggere?',
    # «solo» concorderebbe col giocatore, che puo' essere donna
    (16988, "You're all alone."):
        'Non c\'è nessuno con te...',
    # ⚠️ reso sul giapponese: `studybuddy` porta «your friends» in inglese nudo.
    #    Vedi la nota in cima.
    (16991, 'You started a reading party with .'):
        '"Cominci un circolo di lettura con i tuoi compagni."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-017.jsonl'
DA, A = 15500, 16999
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

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
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
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
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
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
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
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
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
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
