# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-005: le ultime morti, i sette premi di trama e il
cadavere da cui si scende (chara_func.hsp 7000-7999).

35 rese. La zona e' la coda di `dmghp`: finiscono le cause di morte cominciate
nel lotto 003 e comincia **quello che succede quando muore qualcuno di
importante** — le pietre magiche, l'ankh, le ali del caos, il campanello.

⚠️⚠️ **Otto rese su trentacinque erano gia' decise, e `dossier.py` non ne ha
vista NESSUNA.** I sette premi di trama (`:7347`, `:7353`, `:7359`, `:7448`,
`:7454`, `:7460`, `:7473`, `:7605`) dicono 「[愚者の魔石]を手に入れた！」, e
`text.hsp:11576`-`:11630` ha gia' reso **`[愚者の魔石]`** — la stessa parentesi
quadra, lo stesso nome — come `[pietra magica del folle]`. Il dossier non le
aggancia perche' confronta la **stringa intera**, e qui il termine e' annegato
dentro una frase piu' lunga.
💡 **E' il limite dello strumento della 36ª detto con un numero**: `dossier.py`
pesca le rese gemelle, non i **termini** dentro le rese. La regola «cercare
prima di scrivere» qui va fatta ancora a mano, cercando il termine e non la
frase. Otto su trentacinque e' troppo per lasciarla al caso: e' il candidato
naturale al prossimo strumento.
✅ Copiati tutti: `[pietra magica del folle]`, `[pietra magica del
conquistatore]`, `[pietra magica del saggio]`, `[ankh del sole]`, `[chip di
dati]`, `[ali del caos]`, `[registro di dati]`, `[campanello arrugginito]`. Piu'
`<Amurdad>` (`db_creature.hsp:75293`), `<Big Daddy>`, `<Little Sister>`,
«Sentenza di morte» (`buff.hsp:71`) e «flagello degli dei»
(`item_data.hsp:1361`).

⚠️ **`:7037` e' il `valn` della 35ª in una variabile nuova.** `rtvaln` vale
`itemname(...)` — oppure il letterale 「荷物」 che `:7032` gli assegna — quindi
**porta l'articolo italiano dentro**, e l'inglese lo mette dopo «`squashed
by`»: «schiacciato **da lo** zaino». ⚠️ E la rete 8 **non lo vede**, perche' il
suo elenco e' `name|itemname|valn|cdatan` e questa variabile si chiama
`rtvaln`. ✅ Girato col carico **soggetto** — «Il carico schiaccia X sotto il
peso» — che e' la stessa strada di `valn` da soggetto della 36ª.
💡 E il frammento d'epigrafe `:7039` non poteva fare lo stesso, perche' deve
restare predicato del morto: «si accascio' **sotto** il carico», e «sotto» e'
una delle preposizioni che **non si fondono** con l'articolo. Le altre sono
«contro», «per», «tra»: e' la scorciatoia che il progetto non aveva mai
dichiarato, e in questo lotto serve due volte.

⚠️ **`:7787` ha chiesto la stessa scorciatoia e non l'ha avuta.** 「name の死体
から降りた。」 e' «scende **dal** cadavere **di** X», due fusioni in una riga, e
l'inglese ne dichiara **due** `name()` che la rete 11 pretende. ✅ Risolto con
l'**apposizione**: «X scende di sella e lascia a terra Y, ormai cadavere». Il
genitivo sparisce e i due nomi restano tutt'e due.

💡 **Le cinque morti che restavano seguono la regola del lotto 003**: riga di
log al presente, frammento d'epigrafe al **passato remoto**. «si impicco'»,
«mori' per soffocamento», «si accascio' sotto il carico», «perse il Gioco delle
Ombre contro X». ⚠️ E per l'ultima la scorciatoia di «contro» serve di nuovo,
perche' l'avversario e' un `cdatan()` che porta l'articolo.

💡 **闇のゲーム non e' «a card game»: e' il Gioco delle Ombre.** L'inglese di
`:7002` dice «`was sent to Amur-cage by X`» e inventa la gabbia; il giapponese
dice 「闇のゲームで負けた」, che e' la citazione di Yu-Gi-Oh — 闇のゲーム, il
Gioco delle Ombre, che in italiano ha un nome fatto e finito. Reso sul
giapponese, come sempre.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- le ultime cinque morti. Log al presente, epigrafe al passato remoto.
    # 闇のゲーム e' il Gioco delle Ombre di Yu-Gi-Oh, non «a card game».
    # ⚠️ «contro» non si fonde con l'articolo che cdatan porta dentro
    (7002, ' was sent to Amur-cage by .'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " perde il Gioco delle Ombre contro " + cdatan(CDATAN_NAME, (DAMAGE_FROM_CARD_GAME - dmghp_source)) + "."',
    (7004, 'lost a card game against  and was sent to Amur-cage'):
        '"perse il Gioco delle Ombre contro " + cdatan(CDATAN_NAME, (DAMAGE_FROM_CARD_GAME - dmghp_source))',
    (7009, ' hang self.'):
        'name(dmghp_charid) + " si impicca."',
    (7011, 'committed suicide by hanging'):
        'si impiccò',
    (7015, ' choke to death.'):
        'name(dmghp_charid) + " muore per soffocamento."',
    (7017, 'choked to death'):
        'morì per soffocamento',
    # rtvaln vale itemname() oppure questo letterale: porta l'articolo dentro
    (7032, 'backpack'):
        'il carico',
    # ⚠️ «schiacciato da lo zaino»: il carico diventa soggetto, come valn nella 36ª
    (7037, '  squashed by .'):
        'rtvaln + " schiaccia " + name(dmghp_charid) + " sotto il peso."',
    # ⚠️ qui il carico NON puo' fare da soggetto (e' il predicato del morto):
    #    «sotto» e' una delle preposizioni che non si fondono
    (7039, 'was squashed by '):
        '"si accasciò sotto " + rtvaln',

    # --- gli eventi che seguono la morte di qualcuno di importante.
    # ネヘルタード e' <Amurdad> in db_creature.hsp:75293
    (7139, 'Amurdad: Alas... It was in vain...'):
        '"<Amurdad>: " + cnvtalk("Non c\'è più niente da fare... che peccato...")',
    # copiate da proc.hsp:241, stesso giapponese
    (7247, 'Removal Point '):
        'Punti ',
    (7247, 'Quota '):
        'Obiettivo ',
    (7279, 'This will likely reduce bear visits a little.'):
        'Così gli orsi si vedranno un poco meno in giro.',
    (7283, 'This will likely reduce bear visits in the future.'):
        'Così in futuro gli orsi si vedranno molto meno in giro.',
    # 神殺し e' «flagello degli dei» in item_data.hsp:1361
    (7319, 'You are the godslayer!'):
        'Ormai sei il flagello degli dèi.',
    # copiata da action.hsp:18728, stesso giapponese
    (7330, '*Duel-Over!*'):
        '*Duello finito!*',

    # --- i sette premi di trama. I nomi fra parentesi quadre stanno gia'
    #     in text.hsp:11576-11630: si copiano, non si ridecidono.
    (7347, "You obtain the [Fool's Magic Stone]!"):
        'Ottieni la [pietra magica del folle]!',
    (7353, "You obtain the [King's Magic Stone]!"):
        'Ottieni la [pietra magica del conquistatore]!',
    (7359, "You obtain the [Sage's Magic Stone]!"):
        'Ottieni la [pietra magica del saggio]!',
    (7448, 'You obtain the [Ankh of The Sun]!'):
        'Ottieni l\'[ankh del sole]!',
    (7454, 'You obtain the [Data Chip]!'):
        'Ottieni il [chip di dati]!',
    (7460, 'You obtain the [Chaos Wings]!'):
        'Ottieni le [ali del caos]!',
    (7473, 'You obtain the [Data Register]!'):
        'Ottieni il [registro di dati]!',
    (7605, 'You obtain the [Rusted Bell]!'):
        'Ottieni il [campanello arrugginito]!',

    # --- la Little Sister, la capsula, le pulizie, l'allarme.
    (7423, 'The Big Daddy had already evacuated the Little Sister somewhere.'):
        '<Big Daddy> aveva già messo al sicuro la <Little Sister> da qualche parte.',
    (7430, 'You have saved Little Sisters  times and killed them  times.'):
        '"<Little Sister> salvate: " + gdata(GDATA_SISTER_SAVED) + ", uccise: " + gdata(GDATA_SISTER_KILLED) + "."',
    (7496, 'You place the lump of purified ether into the recovery capsule.'):
        'Metti il blocco di etere purissimo nella capsula di recupero.',
    # copiata da db_creature.hsp:95327, stesso inglese e stesso senso
    (7512, 'Cleaning completed!'):
        'Pulizie completate!',
    (7644, '*beeeeeep!* An alarm sounds loudly!'):
        '*biiiiip!* Un allarme squilla assordante!',
    (7765, 'You feel sad for a moment.'):
        'Ti prende la tristezza per un istante.',

    # --- il cadavere da cui si scende.
    # ⚠️ «dal cadavere di X» sono due fusioni in una riga, e la rete 11 vuole
    #    tutt'e due i name(). La strada e' l'apposizione.
    (7787, ' get off the corpse of .'):
        'name(CHARA_PLAYER) + " scende di sella e lascia a terra " + name(dmghp_charid) + ", ormai cadavere."',
    (7796, ' took down the corpse of .'):
        'name(CHARA_PLAYER) + " depone a terra con delicatezza " + name(dmghp_charid) + ", ormai cadavere."',
    # 死の宣告 e' «Sentenza di morte» in buff.hsp:71
    (7878, 'The death word breaks.'):
        'La sentenza di morte si annulla.',

    # --- la parodia di Dragon Quest: tutto in hiragana, con gli spazi larghi.
    (7915, ' stood up and offered to join you! Would you like to join ?'):
        '"Incredibile! " + cdatan(0, dmghp_charid) + " si rialza e ti guarda come se volesse unirsi a te! Vuoi accogliere " + cdatan(0, dmghp_charid) + " nel gruppo?"',
    (7934, ' vanish.'):
        '"" + cdatan(0, dmghp_charid) + " se ne va con aria mesta"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-chara_func-005.jsonl'
DA, A = 7000, 7999
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
