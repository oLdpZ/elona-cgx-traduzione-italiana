# -*- coding: utf-8 -*-
"""Lotto fase4-command-003: la scheda del personaggio
(command.hsp, righe 10495-10948).

⭐⭐ **È la schermata che si guarda più di ogni altra dopo il log**, e i valori
dentro sono **già italiani** da tre sessioni — «Maschio», «Nessuna», «FOR COS DES
PER APP VOL MAG CAR», i nomi di razza e di classe. Mancava solo la cornice: 41
rese e 1 rinviata.

⚠️⚠️ **Nessuna guardia misura questa schermata, e i budget sono di trentotto
pixel.** `larghezze.py` conosce solo i menu che passano da `*prompt_key`
(il suo docstring lo dice: «solo le assegnazioni a `s(cnt)`» dentro quei
`#deffunc`); qui le etichette si disegnano con `mes` a `pos` fisse, e il metro
è la **distanza fra la posizione dell'etichetta e quella del valore**, che il
sorgente scrive due volte a poche righe di distanza:

| gruppo | etichetta | valore | budget | inglese più lungo |
|---|---|---|---|---|
| `:10495` | `wx+355` | `wx+410+5` | **60 px** | `Next Lv` (7) |
| `:10504` col. 1 | `wx+30` | `wx+68` | **38 px** | `Class` (5) |
| `:10504` col. 2 | `wx+220` | `wx+270` | **50 px** | `Height` (6) |
| `:10517` | `wx+255` | `wx+310` | **55 px** | `Rating` (6) |
| `:10526` | `wx+29` | `wx+86` | **57 px** | `Cargo Lmt` (9) |
| `:10730` | `wx+422` | `wx+468` | **46 px** | `Prot` (4) |
| `:10732` | `wx+574` | `wx+617` | **43 px** | `Evade` (5) |
| `:10734` | `wx+554` | `wx+617` | **63 px** | `SpellPow` (8) |
| `:10837` | `wx+30` | `wx+63` | **33 px** | `Desc:` (5) |

💡 Il carattere è `12 + sizefix - en * 2`, cioè **10 px in grassetto** nella
build inglese (9 px per `:10837`). Da `Cargo Lmt` — nove caratteri dentro 57
pixel — viene il metro usato qui: **~6,3 px per carattere**, e la regola pratica
è che l'italiano non superi l'inglese di più di un paio di caratteri.
⚠️ **Perciò upstream abbrevia, e l'italiano deve abbreviare uguale**: `Prot`,
`Evade`, `SpellPow`, `InSAN`, `Cargo Wt` sono già tutte sigle. Dove il progetto
ha una resa distesa e non ci sta, si abbrevia **quella**, non si allarga il
riquadro.

⚠️⚠️ **La scheda NON si chiude con questo lotto, e non è una dimenticanza.**
`Level` e `Name` non compaiono in questa zona perché `estrai --da-tradurre` dà
**una voce per firma**, e le loro prime occorrenze stanno a `:3556` e `:7623`.
Finché non si traducono quelle due righe, la scheda avrà due etichette inglesi
in cima. ⚠️ E i loro budget sono questi — 60 px per `Level`, 38 per `Name` —
non quelli dei siti dove le firme sono estratte: chi scriverà quel lotto guardi
qui prima di scegliere.

⚠️ **`Schiv.` contro la rete 3, ed è la larghezza a decidere.** `skill.hsp:307`
rende 「回避」 «Schivata», ed è la resa giusta per il **nome dell'abilità**; qui
l'etichetta ha **43 pixel** e «Schivata» ne vuole ~46. ✅ Abbreviata: non è una
resa nuova, è la stessa parola tagliata dove il riquadro taglia. Stesso motivo
per «Prot.» e «Pot. magia».
💡 Idem per `Sesso` contro `text.hsp:191`, che scrive «sesso» minuscolo: lì la
parola sta **dentro una frase**, qui è l'intestazione di una colonna. La
maiuscola la mette il sito, non una scelta diversa.

⚠️⚠️ **Un giapponese solo per due siti, e la rete 4 impone lo spazio.**
「ターン」 sta a `:10526` come **etichetta** di colonna (`Turns`) e a `:10754`
come **suffisso di un numero** (` Turns`, con lo spazio davanti): l'inglese
mette lo spazio dove serve e la rete 4 pretende una resa sola. ✅ « Turni» con
lo spazio in tutt'e due: il valore ne ha bisogno («12345 Turni») e l'etichetta
se lo assorbe come un rientro di tre pixel. È la lezione del brusio del
`map-005` — lo stesso giapponese, una resa sola, spazi compresi.

⭐ **Sei etichette non le ho decise io.** 「信仰」 è «Fede» (`skill.hsp:347`),
「生命力」 «Vita» (`:9`), 「マナ」 «Mana» (`:14`), 「速度」 «Velocità» (`:59`),
`Shoot` «Tiro» (`text.hsp:136`), e le tre gilde sono parola per parola quelle di
`init.hsp:373`-`:379`. ⚠️ Le gilde sono lunghe — «Gilda dei Guerrieri» sono
diciannove caratteri — ma quella è la **colonna dei valori**, che ha 186 pixel
fino al ritratto: il tetto stretto è delle etichette, non dei valori.

💡 **`INI` è `INIT`, e vuol dire i tiri iniziali**: `:10657` compone
`inipower = CDATA_INIT_LIFEMANA + CDATA_INIT_ATTR` e il valore accanto è
`inipower + "/" + CDATA_INIT_SPEED`. «Iniz.» in cinque caratteri.
💡 **`AP` e `HP/MP` sono due invariati nuovi**, dichiarati in `invariati.md`:
il giapponese scrive `HP/MP` identico e 「ＡＰ」 a larghezza intera, che CP932
vieta comunque. `Karma` e `Mana` erano **già** dichiarati dalle sessioni
passate — si guarda prima di aggiungere.

⚠️ **`:10825` è rinviata: sta dentro l'`ORIGINAL` che il mod ha spento**
(`:10817`-`:10827`). È la gemella di `:10837`, che è viva e resa: stesso
giapponese 「説明:」, due inglesi diversi (`Hint:` e `Desc:`). Senza il rinvio la
rete 4 avrebbe preteso una resa sola per tutt'e due, e sarebbe stato un vincolo
imposto da **testo morto**.

💡 **`:10948` è un prefisso che il giapponese mette in coda.**
`s = lang("", "Resist ") + cnven(s) + lang("耐性", "")`: l'inglese antepone
«Resist », il giapponese posticipa 「耐性」, e il ramo inglese della seconda
`lang()` è **vuoto**, quindi non c'è nessuna firma da tradurre lì. L'italiano
può solo anteporre: «Res. fuoco», nella colonna della lista abilità.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :10495 la colonna di destra in cima. Budget 60 px.
    (10495, 'Next Lv'):
        'Prossimo',
    # ⭐ copiata: skill.hsp:347 rende 「信仰」 «Fede»
    (10495, 'God'):
        'Fede',
    (10495, 'Guild'):
        'Gilda',
    (10495, 'Growth'):
        'Crescita',

    # --- :10504 la prima colonna. Budget 38 px: al massimo sei caratteri.
    (10504, 'Aka'):
        'Alias',
    (10504, 'Race'):
        'Razza',
    # ⚠️ rete 3: text.hsp:191 scrive «sesso» minuscolo, ma li' e' dentro una
    #    frase. Qui e' l'intestazione di una colonna.
    (10504, 'Sex'):
        'Sesso',
    (10504, 'Class'):
        'Classe',

    # --- :10504 la seconda colonna. Budget 50 px.
    (10504, 'Age'):
        'Età',
    (10504, 'Height'):
        'Altezza',
    (10504, 'Weight'):
        'Peso',
    # 💡 INIT sono i tiri iniziali: :10657 somma CDATA_INIT_LIFEMANA e _ATTR
    (10504, 'INI'):
        'Iniz.',
    # 💡 invariato dichiarato in invariati.md: il giapponese e' 「ＡＰ」
    (10504, 'AP'):
        'AP',

    # --- :10517 la colonna centrale. Budget 55 px.
    # 💡 invariato dichiarato in invariati.md: il giapponese scrive HP/MP uguale
    (10517, 'HP/MP'):
        'HP/MP',
    # ⭐ copiate: skill.hsp:9, :14, :59
    (10517, 'Life'):
        'Vita',
    (10517, 'Mana'):
        'Mana',
    (10517, 'InSAN'):
        'Follia',
    (10517, 'Speed'):
        'Velocità',
    (10517, 'Fame'):
        'Fama',
    (10517, 'Karma'):
        'Karma',
    (10517, 'Rating'):
        'Potenza',
    (10517, 'Melee'):
        'Mischia',
    # ⭐ copiata: text.hsp:136 rende `Shoot` «Tiro»
    (10517, 'Shoot'):
        'Tiro',

    # --- :10526 la colonna in basso a sinistra. Budget 57 px.
    (10526, 'Cargo Wt'):
        'Carico',
    (10526, 'Cargo Lmt'):
        'Limite',
    # ⭐ stessa sigla di :14193 nel lotto 002
    (10526, 'Equip Wt'):
        'Peso eq.',
    # ⚠️ rete 4: stesso giapponese 「ターン」 di :10754, e la resa dev'essere una
    #    sola. Lo spazio serve li' e qui e' un rientro di tre pixel.
    (10526, 'Turns'):
        ' Turni',
    (10526, 'Time'):
        'Tempo',

    # --- :10609 il segno di percentuale della crescita.
    # 💡 attaccato al numero come nel giapponese: cosi' non coincide con
    #    l'inglese, che ci mette uno spazio davanti
    (10609, ' %'):
        '%',

    # --- :10621-:10627 le tre gilde. ⭐ parola per parola init.hsp:373-:379.
    (10621, 'Mages Guild'):
        'Gilda dei Maghi',
    (10624, 'Fighters Guild'):
        'Gilda dei Guerrieri',
    (10627, 'Thieves Guild'):
        'Gilda dei Ladri',

    # --- :10730-:10734 le tre sigle del riquadro di destra.
    # ⚠️ abbreviate perche' il riquadro e' stretto, non perche' la resa cambi:
    #    «Schivata» e' skill.hsp:307 e vuole 46 px dove ce ne sono 43
    (10730, 'Prot'):
        'Prot.',
    (10732, 'Evade'):
        'Schiv.',
    (10734, 'SpellPow'):
        'Pot. magia',

    # --- :10754 il contatore dei turni. ⚠️ vedi :10526.
    (10754, ' Turns'):
        ' Turni',

    # --- :10814-:10847 il piede della scheda e le intestazioni della lista.
    (10814, "This character isn't currently blessed or hexed."):
        'Adesso non ha nessun effetto attivo.',
    # ⚠️ 33 px soli: «Spiegazione:» ne vorrebbe settanta
    (10837, 'Desc:'):
        'Info:',
    (10845, 'Lv(Potential)'):
        'Lv(potenziale)',
    (10847, 'Detail'):
        'Effetto',

    # --- :10948 il prefisso delle resistenze nella lista abilita'.
    (10948, 'Resist '):
        'Res. ',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    (10825, 'Hint:'),
}

USCITA = 'lavoro/fase4-command-003.jsonl'
DA, A = 10440, 11000
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

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
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
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
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
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
    resa = RESE[chiave(v)]
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
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
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
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
