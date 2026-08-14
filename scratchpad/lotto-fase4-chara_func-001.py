# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-001: i dodici stati, i sedici recuperi e il bagnato
(chara_func.hsp 3000-3999).

39 rese e **una rinviata a toppa**. **E' il primo lotto di `chara_func.hsp`**, che apre
dopo la chiusura di `proc.hsp` e per una ragione che non viene da una misura ma
dal **collaudo**: lo screenshot della 39ª mostrava un log di combattimento
ancora mezzo inglese **adesso che `proc.hsp` e' al 100%**, e ogni riga inglese
veniva di qua o da `calculation.hsp`. E' la lezione della 26ª — *la frequenza,
non l'elenco* — trovata guardando lo schermo invece che contando le firme.

⭐ **E' il blocco piu' partecipiale del progetto: l'inglese scrive DODICI stati
su dodici col participio.** «`is blinded`», «`is faltered`», «`was knocked
down`», «`is confused`», «`is paralyzed`», «`is eroded`», «`is poisoned`»,
«`is frightened`», «`is incontinent`», «`is dimmed`». In italiano
concorderebbero tutti col personaggio, e meta' dei personaggi di Elona sono
femmine. Il giapponese non ha il problema perche' usa 「は…た」, che e' neutro.
✅ Le due strade sono quelle di sempre, e qui si dividono il lavoro a meta':
- il **verbo riflessivo o intransitivo** — «si addormenta», «si ubriaca»,
  «si ammala», «cade a terra», «comincia a tremare», «comincia a sanguinare»,
  «perde il senno», «se la fa addosso», «esita», «va in confusione»;
- la **sostanza come soggetto** — «La cecita' coglie X», «La paralisi coglie
  X», «Lo stordimento coglie X», «Il veleno invade X», «Il gelo dell'Oltretomba
  corrode X». La forma «La <cosa> coglie X» non l'ho inventata qui: e' di
  `proc.hsp:13389`, ed e' l'unica delle cinque che fosse gia' decisa.

⚠️ **I sedici recuperi hanno il problema gemello, ma di genitivo.** L'inglese
dice «`X` **`your(X)`** `bleeding stops.`», «`recover from` **`his(X)`** `illness`»,
«`suppressed` **`his(X)`** `trembling`»: il possessivo inglese diventa in
italiano «il sangue **di** X», «la malattia **di** X», e `name()` porta dentro
l'articolo. ✅ Tutti girati col nome soggetto e il possesso implicito — «X non
sanguina piu'», «X si rimette dalla malattia», «X smette di tremare».
💡 `his(X)` e `your(X)` a un argomento sono **morfologia**, quindi la rete 11
non li pretende: sparire e' quello che devono fare.

⚠️⚠️ **`:3037` e' il trentatreesimo errore di monte, ed e' la TERZA riga del
progetto che il dizionario non puo' aggiustare** — dopo `proc.hsp:11481` della
36ª e `proc.hsp:24107` di questa stessa sessione. La coppia
「濡れた」/「姿があらわになった」 compare **tre volte** nello stesso blocco, e
nel ramo inglese dell'ultima upstream ha ricopiato quella del tag-team
cambiando **due** riferimenti su tre: `is(gdata(GDATA_RIDER))` e
`his(gdata(GDATA_RIDER))` sono giusti, il `name()` e' rimasto
**`name(ttc@con)`**. Il giapponese dice `name(gdata(GDATA_RIDER))` e il codice
conferma — `cbit(CHARA_BIT_INVISIBLE, gdata(GDATA_RIDER))` due righe sopra.
💡 **E la rete 11 non lascia scampo**, perche' `funzioni_di_contenuto` conta
`gdata` come contenuto: l'inglese dichiara `['name']`, la resa giusta
dichiarerebbe `['name', 'gdata']`. ✅ Rinviata e toppata.

⚠️ **`:3380` dice due cose opposte nelle due lingue.** L'inglese e'
`cnvtalk("Don't look at me!")` — l'imbarazzo — e il giapponese e'
「…スッキリ！」, cioe' **il sollievo**: la creatura che se l'e' fatta addosso e'
contenta. Il giapponese arbitra, come sempre. 💡 E lo stesso inglese sta gia' in
`text.hsp:12229` con un giapponese diverso, reso «Non avvicinarti!»: e' la rete
13 a cavallo di due file, la terza volta nella 39ª.

💡 **Sette rese su quaranta sono copie**, e tutte da `proc.hsp` o `action.hsp`:
«esita», «cade a terra», «va in confusione», «La paralisi coglie X», «ha il
terrore addosso», «torna in se'» e «Il tuo diario e' stato aggiornato», che da
sola sta gia' in **tre** file. `dossier.py` le ha pescate tutte.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il bagnato e l'invisibile che riappare. Tre siti per due frasi:
    #     chi subisce, il compagno di tag-team, chi cavalca.
    (3012, ' get wet.'):
        'name(wet_arg1) + " si bagna."',
    (3015, '  revealed  shape.'):
        'name(wet_arg1) + " diventa visibile."',
    (3023, ' get wet.'):
        'name(ttc@con) + " si bagna."',
    (3026, '  revealed  shape.'):
        'name(ttc@con) + " diventa visibile."',
    (3034, ' get wet.'):
        'name(gdata(GDATA_RIDER)) + " si bagna."',
    # ⚠️ :3037 e' RINVIATA a toppa: l'inglese dice name(ttc@con) dove il
    #    giapponese dice name(gdata(GDATA_RIDER)), e la rete 11 non lascia
    #    scrivere la resa giusta. Vedi il docstring.

    # --- i dodici stati. L'inglese li scrive tutti col participio
    #     («is blinded», «was knocked down»), che in italiano concorderebbe.
    (3078, '  blinded.'):
        '"La cecità coglie " + name(dmgcon_charid) + "."',
    # copiata da action.hsp:288 e proc.hsp:8303
    (3107, '  faltered.'):
        'name(dmgcon_charid) + " esita."',
    (3136, ' began trembling.'):
        'name(dmgcon_charid) + " comincia a tremare."',
    # copiata da proc.hsp:9600, :17261 e :25246
    (3152, '  knocked down.'):
        'name(dmgcon_charid) + " cade a terra."',
    # copiata da proc.hsp:22902
    (3193, '  confused.'):
        'name(dmgcon_charid) + " va in confusione."',
    # copiata da proc.hsp:13389
    (3228, '  paralyzed.'):
        '"La paralisi coglie " + name(dmgcon_charid) + "."',
    # 冥界 e' l'Oltretomba, come in chara_func:4712 e :4719
    (3262, '  eroded by the netherworld energy.'):
        '"Il gelo dell\'Oltretomba corrode " + name(dmgcon_charid) + "."',
    (3297, '  poisoned.'):
        '"Il veleno invade " + name(dmgcon_charid) + "."',
    (3332, ' fall asleep.'):
        'name(dmgcon_charid) + " si addormenta."',
    # stesso inglese di proc.hsp:2870, e il giapponese dice la stessa cosa
    (3370, '  frightened.'):
        'name(dmgcon_charid) + " ha il terrore addosso."',
    (3377, '  incontinent.'):
        'name(dmgcon_charid) + " se la fa addosso."',
    # ⚠️ il giapponese dice 「…スッキリ！」, cioe' il sollievo, non l'imbarazzo
    #    dell'inglese. Reso sul giapponese
    (3380, "Don't look at me!"):
        '...Che sollievo!',
    (3426, '  dimmed.'):
        '"Lo stordimento coglie " + name(dmgcon_charid) + "."',
    (3465, ' begin to bleed.'):
        'name(dmgcon_charid) + " comincia a sanguinare."',
    (3484, ' get drunk.'):
        'name(dmgcon_charid) + " si ubriaca."',
    (3514, ' become insane.'):
        'name(dmgcon_charid) + " perde il senno."',
    (3533, ' get sick.'):
        'name(dmgcon_charid) + " si ammala."',
    # 健康のお守り e' <Amuleto di Jure> in db_item.hsp:138248
    (3543, 'But the Amulet of Jure shines brightly for a moment, instantly curing the sickness.'):
        'Ma l\'<Amuleto di Jure> brilla per un istante e guarisce la malattia sul colpo.',

    # --- i sedici recuperi. Anche qui niente participi e niente genitivi:
    #     «l'olio di X», «il sangue di X», «l'ubriacatura di X» fondono tutti.
    (3653, ' recover from faltering.'):
        'name(healcon_charid) + " si riprende dall\'esitazione."',
    (3671, ' suppressed  trembling.'):
        'name(healcon_charid) + " smette di tremare."',
    (3689, ' shake off  fear.'):
        'name(healcon_charid) + " si scrolla di dosso la paura."',
    (3707, ' can see again.'):
        'name(healcon_charid) + " ci vede di nuovo."',
    (3725, ' recover from confusion.'):
        'name(healcon_charid) + " si riprende dalla confusione."',
    (3743, ' recover from paralysis.'):
        'name(healcon_charid) + " si riprende dalla paralisi."',
    (3761, ' recover from oil.'):
        'name(healcon_charid) + " ha smaltito l\'olio."',
    (3779, ' recover from MP leak.'):
        'name(healcon_charid) + " non perde più mana."',
    (3797, ' recover from poison.'):
        'name(healcon_charid) + " si riprende dal veleno."',
    (3815, ' awake from  sleep.'):
        'name(healcon_charid) + " si sveglia da un sonno ristoratore."',
    (3833, ' conciousness becomes clear.'):
        'name(healcon_charid) + " ha di nuovo la mente lucida."',
    (3850, ' bleeding stops.'):
        'name(healcon_charid) + " non sanguina più."',
    (3867, ' get sober.'):
        'name(healcon_charid) + " ha smaltito la sbornia."',
    # copiata da proc.hsp:1359, stesso inglese e stesso senso
    (3884, ' come to  again.'):
        'name(healcon_charid) + " torna in sé."',
    (3902, ' recover from  illness.'):
        'name(healcon_charid) + " si rimette dalla malattia."',

    # --- copiata da action.hsp:8282, proc.hsp:4228 e text.hsp:4
    (3964, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(3037, '  revealed  shape.')}

USCITA = 'lavoro/fase4-chara_func-001.jsonl'
DA, A = 3000, 3999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\chara_func.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_chara_func.jsonl', encoding='utf-8') if l.strip()]
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
