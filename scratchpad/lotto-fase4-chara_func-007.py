# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-007: i rapporti, la tag-team, la sella e la coda
sparsa (chara_func.hsp 0-5999, quello che restava).

22 rese, e **con questo `chara_func.hsp` e' CHIUSO**: 331 firme su 331, meno le
quattro rinviate apposta. E' il tredicesimo file al 100% del progetto, e il
quarto in due giorni dopo `proc.hsp`, `chips.hsp` e `custom_enemyevolution.hsp`.
Le voci di questo lotto non stanno in una zona: sono quello che avanzava sopra
il 2000 e sotto il 6000, cioe' i rapporti con i PNG, la squadra, la cavalcatura
e tre righe di trama.

⚠️ **`:748` non e' testo, ed e' la terza «Party Room» del progetto.**
`lang("JP", "EN")` sta dentro `instr(locvar_customtalk_buff, 0,
locvar_customtalk_s + "," + lang("JP", "EN"))`: e' la **chiave di ricerca** nel
file dei dialoghi personalizzati, non una frase. Tradurla romperebbe la ricerca.
✅ E la risposta era gia' nel dizionario due volte — `action.hsp:4816` e
`text.hsp:9361` la lasciano `EN` — quindi si copia invece di ridecidere. 💡 Non
serve rinviarla: la resa **e'** «EN», ed e' una resa vera, non un rinvio.

⚠️⚠️ **La sella e' la testa di frase piu' lunga del progetto, e continua in
un'altra istruzione.** `:1654` finisce con «`->`» e la frase si chiude a
`:1665`, che stampa `"" + cdata(CDATA_SPEED, ...) + ") "`: la parentesi si apre
in una `lang()` e si chiude **undici righe dopo**, fuori da qualunque
traduzione. ✅ La resa deve quindi finire com'e' cominciata, con la freccia e lo
spazio, e la parentesi resta aperta apposta.
⚠️ **E dentro ci stavano due fusioni**: «Sali **in sella a** X» e «la velocita'
**di** X». ✅ Girate col nome dentro parentesi come **etichetta** — «Cavalchi X.
(X, velocita': 100 -> 120)» — che e' la forma dei referti di stato e non chiede
nessuna preposizione. I due `name()` che la rete 11 pretende restano tutt'e due.

⚠️ **`:1080`, `:1086`, `:1183`, `:1189`, `:1627`: cinque righe su ventidue
vogliono «con», e non e' un caso.** Il giapponese le scrive tutte con 「と」 —
「Xとの関係」, 「Xとタッグを組んだ」 — cioe' il complemento di compagnia, e
l'italiano lo rende con **«con»**, che e' una delle preposizioni che **non si
fondono** con l'articolo che `cdatan()` porta dentro. 💡 Dopo «sotto» del lotto
005, e' la seconda volta in due lotti che la soluzione e' scegliere la
preposizione giusta invece di girare la frase: vale la pena scriverlo una volta
per tutte — **«con», «contro», «per», «tra», «sotto», «sopra» non si fondono**,
e davanti a `name()` sono le uniche utilizzabili.
✅ **E la rete 8 l'ha imposto sul campo**: la prima stesura di `:1169` diceva
«fai colare la cera **su** X», la rete l'ha fermata («su il putit») e la
correzione e' stata cambiare **una parola** — «sopra» — invece di riscrivere la
frase. E' il caso piu' economico che la rete 8 abbia mai prodotto in nove lotti.

⚠️ **`:1668` dice due cose diverse nelle due lingue, e vince il giapponese.**
「この生物は乗馬用にちょうどいい！」 e' «questa creatura e' perfetta da
cavalcare», cioe' un giudizio **sulla cavalcatura**; l'inglese scrive «`You feel
comfortable.`», che parla di **te**. Il ramo lo conferma:
`cbit(CHARA_BIT_SUPERIOR_RIDING, gdata(GDATA_RIDER))` guarda una proprieta'
della bestia. E' la classe di `:3380` del lotto 001, la terza volta in
`chara_func.hsp`.

💡 **E le ultime due copie del file**: 「不明」 e' «Ignoto» in `text.hsp:2969`
sotto lo stesso inglese, e 媚赤蝋燭 e' `<Candela di Lulwy>` in
`db_item.hsp:138261` — che l'inglese chiama «Candle of Lulwy», per una volta
d'accordo col giapponese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # copiata da text.hsp:2969, stesso giapponese e stesso inglese
    (172, 'Unknown'):
        'Ignoto',
    # ⚠️ NON e' testo: e' la chiave di ricerca dentro instr(), sul file dei
    #    dialoghi. action.hsp:4816 e text.hsp:9361 la lasciano gia' cosi'
    (748, 'EN'):
        'EN',

    # --- i rapporti con i PNG. Il giapponese usa 「と」, il complemento di
    #     compagnia: «con» non si fonde con l'articolo che cdatan porta dentro.
    (1080, 'Your relation with  becomes <>...'):
        '"Il rapporto con " + cdatan(CDATAN_NAME, modimp_charid) + " diventa <" + locvar_modimp_pp + ">..."',
    (1086, 'Your relation with  becomes <>!'):
        '"Il rapporto con " + cdatan(CDATAN_NAME, modimp_charid) + " diventa <" + locvar_modimp_pp + ">!"',
    # 媚赤蝋燭 e' <Candela di Lulwy> in db_item.hsp:138261
    (1169, 'You drip wax on  from the Candle of Lulwy. \\"Hot hot hot~\\"'):
        '"Fai colare la cera della <Candela di Lulwy> sopra " + cdatan(CDATAN_NAME, modimp2_charid) + ". \\"Ahi ahi ahi~\\""',
    # :1183 e' il rapporto che peggiora, :1189 quello che migliora: lo dice il ramo
    (1183, 'Your master/servant relation with  becomes <>.'):
        '"Il rapporto di servizio con " + cdatan(CDATAN_NAME, modimp2_charid) + " diventa <" + locvar_modimp2_pp + ">."',
    (1189, 'Your master/servant relationship with  becomes <>.'):
        '"Il rapporto di servizio con " + cdatan(CDATAN_NAME, modimp2_charid) + " diventa <" + locvar_modimp2_pp + ">!"',

    # --- tre righe di trama.
    # ⚠️ March e' un nome proprio: girato per non doverne indovinare il genere
    (1294, 'March was destroyed.'):
        'March non esiste più.',
    # ⚠️ il giapponese parla del giocatore in TERZA persona (「あいつ」), quindi
    #    niente participio da accordare. E le virgolette vanno protette
    (1323, '??? says: \\"You.. you really made it this far, huh. We\'re going to have to get serious.\\"'):
        '???: \\"Quello lì... fa sul serio, allora. Tocca usare le maniere forti.\\"',
    (1380, 'Time starts to run again.'):
        'Il tempo riprende a scorrere.',
    (1392, ' more to go.'):
        '"[Sterminio] ne restano " + locvar_check_quest_p + ". "',

    # --- la squadra. 「と」 di nuovo, e «con» di nuovo.
    (1627, ' and  form a tag-team.'):
        'cdatan(CDATAN_NAME, tag_begin_arg1) + " fa squadra con " + cdatan(CDATAN_NAME, tag_begin_arg2) + "."',
    (1641, 'You were disbanded  with .'):
        'cdatan(CDATAN_NAME, tag_end_arg1) + " e " + cdatan(CDATAN_NAME, locvar_tag_end_ttc) + " sciolgono la squadra."',

    # --- la sella. ⚠️ TESTA di frase: la parentesi si chiude a :1665, fuori da
    #     qualunque lang(). La resa finisce con la freccia e lo spazio, come
    #     l'inglese. E il nome sta fra parentesi come ETICHETTA, per non dover
    #     scrivere «la velocita' di X».
    (1654, "You ride . ('s speed: ->"):
        '"Cavalchi " + name(ride_begin_arg1) + ". (" + name(ride_begin_arg1) + ", velocità: " + cdata(CDATA_SPEED, ride_begin_arg1) + " -> "',
    (1657, " rides you. ('s speed: ->"):
        'name(ride_begin_arg1) + " ti sale in groppa. (" + name(ride_begin_arg1) + ", velocità: " + cdata(CDATA_SPEED, ride_begin_arg1) + " -> "',
    # ⚠️ il giapponese giudica la CAVALCATURA, l'inglese parla di te. Il ramo
    #    guarda CHARA_BIT_SUPERIOR_RIDING, cioe' una proprieta' della bestia
    (1668, 'You feel comfortable.'):
        'Questa creatura è perfetta da cavalcare!',
    (1673, 'This creature is too weak to carry you.'):
        'Questa creatura è troppo debole per portarti.',

    # --- il rumore che sveglia, e chi perde la pazienza.
    (1736, ' notice the sound and wake up.'):
        'name(cnt) + " sente il rumore e si sveglia."',
    (1744, ' can no longer put up with it.'):
        'name(cnt) + " perde le staffe."',
    (1746, "That's it."):
        'Adesso basta.',

    # --- le due sparse in fondo. ⚠️ genitivo: «il patto di X»
    (5479, ' lost the effect of contingency.'):
        'name(dmghp_charid) + " vede scadere il patto."',
    # 絶対防衛 e' «Difesa assoluta» in buff.hsp:159
    (5864, '*Absolute protect*'):
        '*Difesa assoluta*',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-chara_func-007.jsonl'
DA, A = 0, 5999
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
