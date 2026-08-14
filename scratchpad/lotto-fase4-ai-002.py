# -*- coding: utf-8 -*-
"""Lotto fase4-ai-002: chi tira i sassi, il gioielliere che contratta, la
tag-team a tavola, i figli che crescono (ai.hsp, righe 1525-4525).

42 rese, e la **percentuale di copie piu' alta mai vista in un lotto di questo
progetto: dodici su quarantadue**, tutte pescate da `dossier.py` per **giapponese
intero**. Batte le dodici su trentaquattro del `proc-026` e le nove su
quarantadue del `proc-018`, e stavolta non e' un menu ristampato da due punti: e'
il **blocco della tag-team a tavola** (`:2087`-`:2132`), che `action.hsp`
(`:1860`-`:2023`) ha gia' parola per parola in tre varianti — chi ti cavalca, il
bersaglio, il compagno — e che `ai.hsp` ripete in due.

⭐ **Le quattro grida della trasformazione erano gia' tutte e quattro decise.**
`action.hsp:11442` ha lo stesso `txt` con gli stessi quattro giapponesi:
「変身！」 «Trasformazione!», 「フォームアップ！」 «Cambio forma!»,
「ドレスアップ！」 «Cambio d'abito!», 「トランスフォーム！」 «Metamorfosi!». ⚠️ **Non
stanno in questo lotto**: vedi la nota sulla rete 0 qui sotto.

⚠️⚠️ **La rete 0 ha fermato una zona, ed e' la prima volta.** A `:4576` due
`lang()` diverse hanno lo **stesso inglese** — 「変身！」 e 「トランスフォーム！」
sono tutt'e due `cnvtalk("Transform!")` — quindi la chiave `(riga, en)` su cui e'
costruito ogni lotto **identifica due voci, non una**, e il modello si ferma
prima di scrivere. Non e' un difetto della rete: e' il limite della chiave.
✅ La zona di questo lotto arriva a `4560`, e le quattro grida vanno in un lotto
`003` scritto a mano e indicizzato per **`firma`**, che e' l'unica chiave davvero
univoca. 💡 Il dizionario la collisione la regge gia' — `action.hsp:11442` porta
«Trasformazione!» e «Metamorfosi!» sulla stessa riga con lo stesso inglese — ed
e' solo lo **script di lotto** a non poterla esprimere.

⭐ **Le preposizioni che non si fondono hanno salvato la resa gia' decisa, e
stavolta e' «verso».** 「睨み付けた」 e' «lanciare un'occhiataccia» da
`action.hsp:1854`-`:2011`, ma li' il bersaglio e' sempre **«ti»**, un clitico; qui
sono due nomi, e «un'occhiataccia **a** name(cc)» e' chiusa in partenza dalla
rete 8. ✅ «lancia un'occhiataccia **verso** X»: «verso» non si fonde con
l'articolo, quindi la frase gia' decisa si tiene tale e quale invece di essere
girata. E' la scorciatoia della 40a — «con», «contro», «per», «sotto», «sopra» —
con una preposizione in piu' all'elenco.

⚠️ **Un genitivo di monte girato col verbo.** `:1755` dice «X seems to be aiming
at Y», e «mira **a** Y» ricadrebbe nella rete 8 come sopra. ✅ «X **punta** Y»,
che in italiano regge il complemento oggetto diretto e non vuole nessuna
preposizione.

⚠️ **Tre aggettivi appesi a un nome di genere fisso.** I cinque versi dei figli
che crescono (`:2317`-`:2341`) sono tutti participi o aggettivi in inglese —
«`is looking away with interest`», «`is thinking with a serious face`» — e in
italiano concorderebbero col figlio, che puo' essere maschio o femmina. ✅ «con
**aria** curiosa», «con **aria** seria»: l'accordo cade su «aria», che e'
femminile per sempre. E' la strada dei ventidue di resistenza della 40a («si
sente la **pelle**…») applicata a un complemento di modo.

⚠️ **` *BAN* ` resta invariato**, e va dichiarato in `invariati.md`: `:2308` e'
`lang(" *BAN* ", " *BAN* ")` — **il giapponese e' inglese anche lui**, come
`HAPPY END!!` e `Destroy! Dynamite!`. E' il ghepardo che bara (`WALL_HACK_CHEATAH`
… `SPEED_HACK_CHEATAH`) che si prende il ban e muore sul colpo: la parola e'
gergo di rete, identica nelle tre lingue.

💡 **Un giapponese solo per TRE inglesi, e la resa e' una sola: cambia solo lo
spazio.**  *クスクス*  e' `*chuckle*` ad `action.hsp:250`, ` *Snicker* ` a
`db_creature.hsp:95622` e ` *grin* ` qui: l'italiano dice «*risatina*» in tutt'e
tre, e gli spazi attorno li mette **il sito**, copiando il suo inglese. La rete 3
grida perche' confronta i letterali e lo spazio conta, ma non e' una divergenza —
e' la stessa resa in tre vestiti. E' il rovescio della rete 13: li' un inglese
per due giapponesi, qui tre inglesi per un giapponese.

💡 **I termini gia' decisi che il dossier non vede, perche' sono termini e non
frasi:** 店主 e' «il negoziante» (`db_creature.hsp:74301`), 訓練券 e' il
«biglietto d'addestramento» (`db_item.hsp:134224`), e `gold pieces` sono le
«monete d'oro» di `proc.hsp:7056` e `:9488`. ⚠️ `:1939` scrive `hiyou + "gp"`
attaccato: la resa scioglie l'abbreviazione, come ha gia' fatto
`text.hsp:10817` con «2,000,000gp».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- chi tira i sassi al gigante.
    (1525, 'Filthy monster!'):
        'Mostro schifoso!',
    (1525, 'Go to hell!'):
        'Crepa!',
    (1525, "I'll get rid of you."):
        'Adesso ti faccio fuori!',
    # ⭐ una firma copre due siti: 「くらえー！」 torna identica a :1570, e
    #    l'estrazione la conta una volta sola (lezione del lotto proc-017)
    (1525, 'Eat this!'):
        'Prendi questo!',

    # --- il pupazzo di neve.
    (1557, ' make !'):
        'name(cc) + " ha fatto " + itemname(ci) + "!"',

    # --- chi tira le cose per gioco. ⭐ la risatina e' gia' di db_creature:95622
    (1570, ' *grin* '):
        ' *risatina* ',
    (1570, 'Fire in the hole!'):
        'Toh!',
    (1570, 'Tee-hee-hee!'):
        'Alè!',
    (1570, 'Watch out!'):
        'Attenzione!',
    (1570, 'Scut!'):
        'Scansati!',

    # --- chi ha visto la lumaca.
    (1717, 'Snail!'):
        'Una lumaca!',
    (1717, 'Kill!'):
        'A morte!',

    # ⚠️ genitivo di monte: «mira a Y» si fonderebbe. «Puntare» regge diretto
    (1755, ' seems to be aiming at ...'):
        'cdatan(CDATAN_NAME, cc) + " punta " + cdatan(CDATAN_NAME, tc) + "..."',

    # --- il gioielliere che lavora e contratta. 店主 e' «il negoziante»
    (1830, ' processed the items in  possession!'):
        'name(cc) + " ha lavorato gli oggetti che portava addosso!"',
    (1834, '  negotiating prices with the shopkeeper...'):
        'name(cc) + " tratta sul prezzo con il negoziante..."',
    (1860, ' sells  items and earns  gold pieces.'):
        'name(cc) + " vende " + sell + " oggetti e guadagna " + sell(1) + " monete d\'oro."',
    # ⚠️ il giapponese dice 稼ぎ, i guadagni, non le monete di action.hsp:973
    (1866, ' shared coins with partner.'):
        'name(cc) + " ha diviso i guadagni con il compagno."',

    # --- l'allenamento. 訓練券 e' il «biglietto d'addestramento» (db_item:134224)
    (1893, ' used a training ticket at a trainer and developed  potential!'):
        'cdatan(CDATAN_NAME, cc) + " si allena con un biglietto d\'addestramento '
        'e accresce il potenziale!"',
    # ⚠️ l'inglese scrive «gp» attaccato: la resa scioglie l'abbreviazione
    (1939, ' spent gp to visit a trainer and develop  potential!'):
        'cdatan(CDATAN_NAME, cc) + " spende " + hiyou + " monete d\'oro '
        'dall\'allenatore e accresce il potenziale!"',

    # --- chi cavalca e travolge.
    (2039, ' ran over .'):
        'name(cc) + " travolge " + name(tc) + "."',
    # ⭐ copiata: quattro siti dicono gia' «esita.» (action:288, chara_func:3107,
    #    proc:8303, proc:13308)
    (2043, '  faltered.'):
        'name(tc) + " esita."',

    # --- chi spinge via chi sta mangiando, e le cinque reazioni.
    (2068, ' displace .'):
        'name(cc) + " spinge via " + name(tc) + "."',
    # ⚠️ «un'occhiataccia a X» si fonde: «verso» no. La resa di action.hsp:1986
    #    si tiene tale e quale
    (2074, ' glare at .'):
        'name(tc) + " lancia un\'occhiataccia verso " + name(cc) + "."',
    (2080, ' looked at  with dissatisfaction.'):
        'name(tc) + " guarda " + name(cc) + " con disappunto."',
    # ⭐ le tre qui sotto sono copiate da action.hsp:1992-:1998
    (2087, ' looked disappointed.'):
        'name(tc) + " china il capo per la delusione."',
    (2094, ' nodded slightly.'):
        'name(tc) + " fa un piccolo cenno del capo."',
    (2101, ' stepped back without a word.'):
        'name(tc) + " indietreggia di un passo senza dire nulla."',

    # --- le stesse cinque per il compagno di tag-team, con cdatan(ttc).
    # ⭐ le ultime tre sono copiate da action.hsp:2017-:2023, cdatan compreso
    (2113, ' glare at .'):
        'cdatan(CDATAN_NAME, ttc) + " lancia un\'occhiataccia verso " + name(cc) + "."',
    (2117, ' looked at  with dissatisfaction.'):
        'cdatan(CDATAN_NAME, ttc) + " guarda " + name(cc) + " con disappunto."',
    (2122, ' looked disappointed.'):
        'cdatan(CDATAN_NAME, ttc) + " china il capo per la delusione."',
    (2127, ' nodded slightly.'):
        'cdatan(CDATAN_NAME, ttc) + " fa un piccolo cenno del capo."',
    (2132, ' stepped back without a word.'):
        'cdatan(CDATAN_NAME, ttc) + " indietreggia di un passo senza dire nulla."',

    # --- chi sfonda quel che trova.
    (2157, ' crush the door!'):
        'name(cc) + " sfonda la porta!"',
    (2168, ' crush the wall!'):
        'name(cc) + " sfonda il muro!"',

    # --- il dolore che stende, e il ghepardo che bara.
    (2300, ' fainted after failing to endure the severe pain.'):
        'name(cc) + " non regge al dolore e perde i sensi."',
    # ⚠️ invariato: il giapponese e' inglese anche lui, e «ban» e' gergo di rete
    (2308, ' *BAN* '):
        ' *BAN* ',

    # --- i cinque versi dei figli che crescono.
    # ⚠️ l'accordo cade su «aria», che e' femminile per sempre
    (2317, '  rolling fine!'):
        'cdatan(CDATAN_NAME, cc) + " si scatena dalla gioia!"',
    (2323, '  hopping and playing!'):
        'cdatan(CDATAN_NAME, cc) + " gioca a saltelloni!"',
    (2329, '  looking away with interest!'):
        'cdatan(CDATAN_NAME, cc) + " guarda altrove con aria curiosa!"',
    (2335, '  thinking with a serious face!'):
        'cdatan(CDATAN_NAME, cc) + " riflette con aria seria!"',
    (2341, '  doubts about how  live!'):
        'cdatan(CDATAN_NAME, cc) + " si interroga su come vivere!"',

    # --- il suffisso della forma alterata. ⭐ copiato da action.hsp:11372
    (4525, '-altered'):
        '/Alter',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-ai-002.jsonl'
DA, A = 1500, 4560
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\ai.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_ai.jsonl', encoding='utf-8') if l.strip()]
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
