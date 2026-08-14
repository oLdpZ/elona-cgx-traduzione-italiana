# -*- coding: utf-8 -*-
"""Lotto fase4-proc-011: azioni speciali, borseggio, soffio, mappe del tesoro,
filtri d'amore (proc.hsp 9201-10100).

34 rese, zero rinviate. E' la prima zona dopo il 9200 dove la 35a si era
fermata, e apre la fascia 10000-12000 che l'istogramma indica come la piu'
densa di quel che resta (77 voci in 10000-10999, il doppio della media).

⚠️⚠️ **`his(x, 1)` in italiano puo' reggere SOLO nomi maschili singolari, e da
questo lotto la cosa e' una regola, non un caso.** Con due argomenti `his()` e'
**contenuto** e passa da `lang()` (`init.hsp:1963-1988`), quindi `verifica`
pretende che resti nella resa (`funzioni.PRONOMI_PER_SITO`); con un argomento e'
morfologia inglese e si toglie (`funzioni.MORFOLOGIA_INGLESE`). Ma la funzione
restituisce **un valore solo per tutto il gioco**, scelto sul genere del
POSSESSORE (`his`/`her`/`your`), mentre l'italiano accorda il possessivo con la
cosa POSSEDUTA. Il valore italiano non potra' quindi che essere «il suo» / «il
tuo», e ogni sito che usa `his(x, 1)` deve mettergli accanto un nome
**maschile singolare**. La 35a l'aveva gia' fatto senza dirlo — `:8849` mette
«sangue» — e le due rese di questo lotto (`:9605`, `:9612`) si adeguano con
«daffare», che oltretutto e' il termine giusto: `rowactend` interrompe
un'attivita' continuata qualunque (mangiare, leggere, pescare, scavare), non un
gesto singolo.

⚠️ **`:9683` e' un `lang()` col ramo GIAPPONESE vuoto**, non l'inglese: la riga
e' `valn = lang("", "breath")`, cioe' quando l'azione speciale non ha un nome
proprio il giapponese lascia il buco e l'inglese ci mette «breath». E' il
gemello rovesciato di `db_creature.hsp:86293` (30a scoperta 3), e a differenza
di quello **si traduce**, perche' il ramo che il giocatore legge e' pieno. La
resa porta l'articolo — «un soffio» — perche' finisce dentro «scatena … a piena
potenza», dove l'altro riempimento possibile e' `skillname(efid)`, che l'articolo
non ce l'ha: «scatena Soffio di fuoco» e «scatena un soffio» reggono tutt'e due.

⚠️ **Quattro nomi propri erano gia' decisi in `text.hsp` e vanno copiati, non
ridecisi**: `North Tyris` -> «Tyris del Nord» (`:2737`), `South Tyris` ->
«Tyris del Sud» (`:2887`), `Lost Irva` -> «Irva Perduta» (`:2917`), `Aimwell`
invariato (`:2899`, gia' in `invariati.md`). E `love potion` e' «filtro
d'amore» da `db_item.hsp:144292`. Cinque rese su 34 sono copie.

⚠️ **Il soffio e' «Soffio»**, con la maiuscola quando e' nome di abilita': i 14
`Breath` di `skill.hsp` sono tutti `Soffio di fuoco`, `Soffio d'oscurita'`,
`Soffio nervino`. Le due teste/code di `:9811`/`:9814` lo scrivono minuscolo
perche' li' e' un nome comune dentro una frase, non l'etichetta dell'abilita'.

⚠️ **Cinque rese sono state riscritte per la rete 8**, e tutte e cinque per lo
stesso motivo: la preposizione italiana si fonde con l'articolo che `name()` si
porta dentro. «sottrae … a » + `name(tc)` darebbe «a il putit», «accanto a » +
`cdatan(...)` idem, «Le pupille di » + `name(cc)` darebbe «di il putit». La
strada e' sempre la stessa — un verbo che regge l'accusativo invece del dativo:
«deruba X di N monete», «raggiunge X», «X spalanca le pupille».

💡 **Rete 4 rifatta.** Confrontava le rese di uno stesso giapponese **come
espressioni**, e qui avrebbe bocciato una coppia legittima: `:9605` e `:9612`
dicono la stessa identica frase su due variabili diverse (`name(tc)` e
`cdatan(CDATAN_NAME, ttc)`), perche' la seconda parla del compagno di tag team.
Adesso confronta i **letterali di testo** dell'espressione, che e' la domanda
vera: «lo stesso giapponese e' stato reso con parole diverse?»
"""
import collections
import glob
import io
import json
import re
import unicodedata

RESE = {
    # --- le azioni speciali: freccia-turbine, bestia lanciata, passo d'ombra
    (9291, 'Hah! Begone with the winds!'):
        'Ahah! Che il turbine ti inghiotta!',
    (9318, 'You can not throw yourself.'):
        'Non puoi lanciare te stesso.',
    # copiata esatta da action.hsp:8844, stesso giapponese
    (9322, ' resist.'):
        'name(tc) + " resiste."',
    # jp e en sono senza soggetto: «il corpo» lo mette l'italiano, che un
    # soggetto lo pretende, ed e' maschile qualunque sia la creatura.
    (9362, 'It does not move to be fixed!'):
        'Il corpo è bloccato e non si muove!',
    # «contro» non si fonde con l'articolo, a differenza di «a»/«di»
    (9408, ' threw  to .'):
        'name(cc) + " scaglia " + name(tc) + " contro " + cdatan(CDATAN_NAME, cdata(CDATA_TARGET, tc)) + "."',

    # --- il borseggio (la mano sospetta). ⚠️ `is(cc)` e `his(cc)`/`his(tc)` con
    #     UN argomento sono morfologia inglese e si tolgono.
    (9474, "  struggling. It seems that the rope is so tight that you can't pull out  wallet."):
        'name(cc) + " fatica parecchio: la corda è troppo stretta e il portafogli non viene via."',
    # jp non nomina nessun ladro: «from a thief» se lo inventa l'inglese
    (9482, ' guard  wallet from a thief.'):
        'name(tc) + " protegge il portafogli."',
    # rete 8: «sottrae N monete a » + name() darebbe «a il putit». Il verbo
    # «derubare» regge l'accusativo e toglie la preposizione.
    (9488, ' steal  gold pieces from .'):
        'name(cc) + " deruba " + name(tc) + " di " + p + " monete d\'oro."',
    # rete 8: «si sposta accanto a » + cdatan() darebbe «a il putit»
    (9557, ' teleport toward .'):
        'name(cc) + " raggiunge " + cdatan(CDATAN_NAME, tcprev) + "."',

    # --- il richiamo d'ombra: trascinato, atterrato, interrotto
    # «trascinato»/«attirato» concorderebbero col bersaglio: il soggetto
    # diventa la forza, e «piu' vicino» e' avverbio, invariabile.
    (9594, '  drawn.'):
        '"Una forza trascina " + name(tc) + " più vicino."',
    (9600, '  knocked down.'):
        'name(tc) + " cade a terra."',
    # ⚠️ his(x, 1): vedi la nota in cima. «daffare» e' maschile singolare, ed e'
    #    quel che rowactend interrompe davvero: un'attivita' continuata.
    (9605, ' got surprised and interrupted  action.'):
        'name(tc) + " si sorprende e interrompe " + his(tc, 1) + " daffare."',
    # stessa frase sul compagno di tag team: cambia la variabile, non le parole
    (9612, ' got surprised and interrupted  action.'):
        'cdatan(CDATAN_NAME, ttc) + " si sorprende e interrompe " + his(ttc, 1) + " daffare."',
    (9622, 'A thief escapes laughing.'):
        'Il ladro se la ride e scappa.',
    # stesso giapponese di proc.hsp:457, dove pero' la variabile e' name(cc)
    (9625, 'Suddenly,  disappear.'):
        '"All\'improvviso " + name(tc) + " sparisce."',

    # --- il soffio. ⚠️ :9683 ha il ramo giapponese vuoto: vedi la nota in cima.
    (9683, 'breath'):
        'un soffio',
    # stessa famiglia di proc.hsp:7784 della 35a, «scatena … a piena potenza»
    (9690, ' blast  with full power.'):
        'name(cc) + " scatena " + valn + " a piena potenza."',
    (9695, ' blast .'):
        'name(cc) + " scatena " + valn + "."',
    # testa/coda sulla forma di action.hsp:15364, come le cinque coppie del 010
    (9811, 'The breath hits  and'):
        '"Il soffio colpisce " + name(tc) + " e"',
    (9814, 'The breath hits .'):
        '"Il soffio colpisce " + name(tc) + "."',
    # rete 8: «Le pupille di » + name() darebbe «di il putit»
    (9867, "'s pupils dilate."):
        'name(cc) + " spalanca le pupille."',

    # --- le mappe del tesoro. Quattro nomi propri copiati da text.hsp.
    (9934, 'You need to read it while you are in the world map.'):
        'Va letta sulla mappa del mondo.',
    (9938, "It's not a sea map."):
        'Non è una mappa del mare.',
    (9942, "It's not a map of Aimwell."):
        'Non è una mappa di Aimwell.',
    (9947, 'The cursed map crumbles as you touch it.'):
        'La mappa maledetta si sbriciola al tocco.',
    # jp dice due cose («questa e' la mappa di X. Leggila a X.»), l'inglese una
    (9996, 'You should move to North Tyris to read this map.'):
        'È la mappa di Tyris del Nord: va letta lì.',
    (10000, 'You should move to South Tyris to read this map.'):
        'È la mappa di Tyris del Sud: va letta lì.',
    (10004, 'You should move to Lost Irva to read this map.'):
        'È la mappa di Irva Perduta: va letta lì.',
    # ⚠️ i puntini sono TRE PUNTI, non «…»: CP932 scrive l'ellissi tipografica
    #    su due byte e la build inglese ne disegna uno per byte.
    (10007, "There's a mark on the map..."):
        'Sembra una mappa che segna un luogo...',
    # ⚠️ non e' una parola: e' il segno rosso disegnato sulla mappa del tesoro
    #    (`mes`, font 40, colore 255/20/20). Dichiarato in invariati.md.
    (10036, 'O'):
        'O',

    # --- i filtri d'amore. «love potion» e' «filtro d'amore» (db_item:144292).
    (10056, 'This love potion is cursed.  look at  with a contemptuous glance.'):
        '"Il filtro d\'amore era maledetto. " + name(tc) + " guarda " + name(CHARA_PLAYER) + " con disprezzo."',
    (10065, ' sense a sigh of love.'):
        'name(tc) + " ha un presentimento d\'amore."',
    # ⚠️ il ramo e' `if ( tc == CHARA_PLAYER )`, quindi parla al giocatore:
    #    «eccitato» concorderebbe col suo sesso. Il nome toglie l'accordo.
    (10084, 'You are excited!'):
        'Ti sale l\'eccitazione!',
    # rete 8: «lancia a » + name() darebbe «a il putit»
    (10087, ' give  the eye.'):
        'name(tc) + " fissa " + name(CHARA_PLAYER) + " con uno sguardo bollente."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-011.jsonl'
DA, A = 9201, 10100

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

# rete 10, nuova qui: `his(x, 1)` e `him(x, 1)`/`he(x, 1)` sono CONTENUTO e
# devono restare, ma in italiano il possessivo accorda con la cosa posseduta
# mentre la funzione sceglie sul possessore. Il valore italiano sara' «il suo»
# per tutti i siti, quindi il nome che segue dev'essere maschile singolare.
# La rete non sa il genere: controlla che `his(x, 1)` non sia stato tolto (lo
# fa gia' `verifica`) e stampa i nomi che gli stanno accanto, da leggere.
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

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

# rete 4, rifatta: lo stesso giapponese non puo' avere due rese diverse DENTRO
# il lotto. ⚠️ Il confronto e' sui LETTERALI di testo, non sull'espressione: due
# siti che dicono le stesse parole su variabili diverse sono la stessa resa.
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
