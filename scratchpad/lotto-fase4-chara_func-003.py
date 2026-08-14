# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-003: il danno, le urla e le ventitre' morti
(chara_func.hsp 6000-6999).

68 rese, ed e' **il lotto piu' grosso mai fatto** — batte le 59 del `proc-021`.
Chiude la zona piu' densa di `chara_func.hsp`. La regge un blocco solo: dal
`:6850` in giu' ci sono **tutte le cause di morte del gioco**, e vengono a
coppie.

⭐⭐ **La scoperta del lotto e' che ogni morte si scrive DUE VOLTE, e le due
meta' hanno vincoli opposti.** Per ogni causa il sorgente scrive:

  - una **riga di log**, dinamica, che nomina chi muore — «`name + は餓死した。`»;
  - un **frammento di epigrafe**, statico, assegnato a `ndeathcause` — 「飢え死
    にした。」 — che **non nomina nessuno**.

Il frammento non e' una frase: e' un pezzo che `main.hsp:4409` incolla dentro
«`cdatan(AKA) + cdatan(NAME) + <frammento> + " in " + mdatan(NAME)`», cioe' la
riga che il gioco manda in rete e scrive sulla lapide.
⚠️⚠️ **E questo decide la lingua del frammento.** Il pezzo segue il nome del
morto e ne e' il predicato: in italiano «e' morto di fame» **concorderebbe col
personaggio**, e meta' dei personaggi di Elona sono femmine. L'inglese non ha il
problema (`was starved to death`), il giapponese nemmeno (「飢え死にした」).
✅ La strada e' il **passato remoto**, che in italiano non ha genere: «mori' di
fame», «cadde dalle scale e mori'», «si tolse la vita», «si prosciugo' nel
deserto». Ventitre' frammenti, ventitre' verbi senza participio. E' la strada
del participio della 37ª applicata a un tempo verbale invece che a una
struttura, ed e' l'unica volta che il progetto ha potuto usarla: **serve una
frase intera**, e i frammenti lo sono.
💡 **Le righe di log invece non hanno il vincolo** — nominano chi muore, quindi
la sostanza puo' fare da soggetto: «Il veleno consuma X fino alla morte», «La
ghigliottina decapita X», «I residui degli elementi inghiottono X».

⚠️⚠️ **E c'e' una dipendenza da dichiarare: la cornice e' in `main.hsp`, che non
ha dizionario.** Finche' `main.hsp:4409` resta inglese, l'epigrafe si leggera'
«`<Il viandante> Sinaha mori' di fame in Vernis`» — meta' italiano e meta'
inglese, con la preposizione sbagliata. Non e' un difetto delle rese, e' la
dipendenza nota di `godname()` della 37ª in forma nuova. ⚠️ E quando si
tradurra' la cornice va ricordato che **il giapponese mette il luogo PRIMA del
frammento** e l'inglese dopo: l'italiano vuole «… mori' di fame **a** Vernis».

⚠️⚠️ **Il QUARTO punto cieco, e la battuta che era gia' morta.** `:6852` e
`:6853` fanno `cnv_str ndeathcause, "was killed by motuhegui", "was mauled to
death by a bear"`: il mod riscrive la stringa **gia' composta**, e la chiave e'
l'**inglese di monte**. Nessuno dei tre referti la vede — `blocchi_en.py` guarda
dentro `if ( en )`, `else_jp.py` dentro `if ( jp ) ... else`, `variabili_en.py`
gli assegnamenti — perche' qui non c'e' nessun letterale inglese da tradurre:
c'e' una **chiave** che deve continuare a combaciare.
✅ Misurato con **`scratchpad/cnv_str_en.py`**: 41 chiamate, **17 con la chiave
in inglese**. ⚠️⚠️ **E questa era gia' rotta**: `db_creature.hsp:37656` rende
モツヘグイ «lo sbudellatore», quindi `cdatan(CDATAN_NAME, cc)` restituisce «lo
sbudellatore» e la chiave `"was killed by motuhegui"` **non aggancia da mesi**.
La battuta dell'orso e' morta quando si e' tradotto il bestiario, e nessuna
verifica l'ha detto. 💡 Le altre 15 stanno in `module.hsp` (il parser dei
desideri, che smonta «card of …» da quel che il giocatore scrive) e in
`help.hsp`: sono **input**, non uscita, e vanno guardate quando si aprira'
`module.hsp`.

⚠️ **`:6196` e `:6200` sono lo stesso inglese per due giapponesi, ed e' un
errore di monte scoperto dalla rete 13**: 「＜中破＞」 e 「＜大破＞」 sono il
danno **medio** e il danno **grave** dello scafo, e l'inglese scrive
«`<Medium damaged>`» tutt'e due le volte. Il ramo lo conferma: `:6194` guarda
`HP > MAX/4`, `:6198` guarda `HP <= MAX/4`. ✅ «Danno medio» e «Danno grave».

⚠️ **E la rete 13 in questo lotto grida QUATTRO volte, che e' il record.**
Oltre a `<Medium damaged>`: «`melt down`» sta per il cioccolato bollente
(`:6917`) **e** per l'acido (`:6959`), «`melted down`» per gli stessi due nei
frammenti (`:6919`/`:6961`), e «`is healed`» per 「再生した」 (`:6212`, il Figlio
del Caos che si rimette in piedi da solo) **e** per 「回復した」 (`:6260`, la cura
di Imposizione delle mani). Tutt'e quattro le distinzioni le fa il giapponese e
le conferma il ramo del codice; l'inglese le ha appiattite.

💡 **Cinque rese su 68 sono copie**, e le ha pescate tutte `dossier.py`: «ha
ripreso l'aspetto di prima» (`action.hsp:9265`), «si riprende»
(`proc.hsp:8199`), «freme di rabbia!» (`action.hsp:263`, `proc.hsp:20851`), «va
in pezzi» (`action.hsp:3102`) e «si contorce dal dolore» (`action.hsp:8778`).

💡 **E i tre gradini del dolore vanno rimessi in ordine sul giapponese.** `:6351`,
`:6358` e `:6365` sono i tre livelli di danno crescente, e il giapponese sale —
痛手を負った, 苦痛にもだえた, 悲痛な叫び声をあげた — mentre l'inglese mette
«`scream`» al **primo** gradino e «`is severely hurt`» al terzo. Reso sul
giapponese: «incassa un colpo doloroso», «si contorce dal dolore», «lancia un
urlo straziante».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il corpo che si rimette in piedi, e lo scafo che si spacca.
    # ⚠️ genitivo: 「name の身体が…」 sarebbe «il corpo di X»
    (6168, '  quickly restored!'):
        'name(dmghp_charid) + " si ricompone in un lampo!"',
    # copiata da action.hsp:9265, stesso giapponese e stesso inglese
    (6182, ' returned to the original form.'):
        'name(dmghp_charid) + " ha ripreso l\'aspetto di prima."',
    # ⚠️ rete 13: lo stesso inglese per 中破 e 大破. Il ramo lo conferma:
    #    :6194 guarda HP > MAX/4, :6198 guarda HP <= MAX/4.
    (6196, '<Medium damaged>'):
        '<Danno medio>',
    (6200, '<Medium damaged>'):
        '<Danno grave>',
    # わらわ e' il «io» arcaico di una nobildonna: la nave parla di se'
    (6202, "My ship's hull has been torn apart again...!"):
        'Il mio scafo è di nuovo a pezzi...!',

    # --- chi si rigenera e chi viene guarito.
    (6212, '  healed.'):
        'name(dmghp_charid) + " si rigenera."',
    (6218, '  regenerated.'):
        'name(dmghp_charid) + " si rigenera."',
    # レイハンド e' l'imposizione delle mani: katakana che l'originale legge
    # come descrizione, quindi si rende (regola di invariati.md, lotto 023)
    (6258, ' shout, Lay on Hands!'):
        'name(cnt) + " grida, " + cnvtalk("Imposizione delle mani!")',
    # copiata da proc.hsp:8199, stesso giapponese
    (6260, '  healed.'):
        'name(dmghp_charid) + " si riprende."',
    (6271, '<Continue> '):
        '<Continua> ',

    # --- i tre gradini del dolore. ⚠️ l'inglese li mette in disordine:
    #     «scream» al primo e «severely hurt» al terzo. Sale il giapponese.
    (6351, ' scream.'):
        'name(dmghp_charid) + " incassa un colpo doloroso."',
    # stessa resa di action.hsp:8778
    (6358, ' writhe in pain.'):
        'name(dmghp_charid) + " si contorce dal dolore."',
    (6365, '  severely hurt!'):
        'name(dmghp_charid) + " lancia un urlo straziante!"',

    # --- l'equipaggiamento che si rovina. ⚠️ genitivo: 「name の itemname は…」.
    #     Il dativo riflessivo lascia il possesso implicito.
    (6399, '  is damaged.'):
        'name(dmghp_charid) + " si vede rovinare " + itemname(locvar_dmghp_ci, , 1) + " dal colpo."',
    (6411, '  is melted by acid.'):
        'name(dmghp_charid) + " si vede sbriciolare " + itemname(locvar_dmghp_ci, , 1) + "."',

    # --- il terrore, il sonno rotto, il parassita, il clic e la furia.
    (6441, ' is frozen in fear.'):
        '"Il terrore inchioda " + name(dmghp_charid) + " sul posto."',
    # ⚠️ genitivo: «il sonno di X»
    (6544, ' sleep  disturbed.'):
        'name(dmghp_charid) + " si sveglia di soprassalto."',
    # ⚠️ genitivo: «il parassita cerebrale di X»
    (6634, "'s brain parasite died from the damage."):
        'name(dmghp_charid) + " prende un colpo al cervello, e il parassita che ci vive muore."',
    (6665, '*click*'):
        '*clic*',
    # copiata da action.hsp:263 e proc.hsp:20851, stesso giapponese
    (6682, '  engulfed in fury!'):
        'name(dmghp_charid) + " freme di rabbia!"',
    # katakana preso a prestito anche in giapponese: l'italiano ha il suo
    (6750, '*Knockout*'):
        '*K.O.*',

    # --- LE VENTITRE MORTI. Per ognuna: la riga di log (dinamica, nomina chi
    #     muore) e il frammento di epigrafe (statico, che main.hsp:4409 incolla
    #     dopo il nome del morto).
    #     ⚠️⚠️ I frammenti vanno al PASSATO REMOTO: seguono il nome e ne sono il
    #     predicato, quindi un participio concorderebbe col personaggio. Il
    #     passato remoto italiano non ha genere.
    # ⚠️ «contro» non si fonde con l'articolo che cdatan porta dentro; «di» sì
    (6850, 'was killed by '):
        '"perse la vita contro " + cdatan(CDATAN_NAME, cc)',
    (6857, ' revealed the true appearance!!'):
        'name(dmghp_charid) + " si mostra nella sua vera forma!"',
    (6859, 'got assassinated by the unseen hand'):
        'sparì per una mano invisibile',
    (6863, '  assassinated by the unseen hand.'):
        '"Una mano invisibile porta via " + name(dmghp_charid) + "."',
    (6869, '  caught in a trap and die.'):
        'name(dmghp_charid) + " finisce in una trappola e muore."',
    (6871, 'got caught in a trap and died'):
        'morì in una trappola',
    (6875, ' shielded you and turned to ashes.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " ti fa scudo e si riduce in cenere."',
    (6877, 'crumbled to ashes'):
        'cadde in cenere',
    (6881, ' turned to ashes and collapsed.'):
        'name(dmghp_charid) + " si accascia e si riduce in cenere."',
    (6887, ' die from over-casting.'):
        '"Il contraccolpo del mana uccide " + name(dmghp_charid) + "."',
    (6889, 'was completely wiped by magic reaction'):
        'svanì nel contraccolpo del mana',
    (6893, '  starved to death.'):
        'name(dmghp_charid) + " muore di fame."',
    (6895, 'was starved to death'):
        'morì di fame',
    (6899, '  killed with poison.'):
        '"Il veleno consuma " + name(dmghp_charid) + " fino alla morte."',
    (6901, 'miserably died from poison'):
        'morì fra i tormenti del veleno',
    (6905, ' die from loss of blood.'):
        'name(dmghp_charid) + " perde tutto il sangue e muore."',
    (6907, 'died from loss of blood'):
        'perse tutto il sangue',
    (6911, ' dried up in the desert and die.'):
        'name(dmghp_charid) + " si prosciuga e muore."',
    (6913, 'dried up in the desert'):
        'si prosciugò nel deserto',
    # ⚠️ rete 13: «melt down» sta qui per il cioccolato bollente e a :6959 per
    #    l'acido. Il giapponese distingue, e il ramo pure (CHOCO / ACID).
    (6917, ' melt down.'):
        '"Il cioccolato bollente ustiona " + name(dmghp_charid) + " a morte."',
    (6919, 'melted down'):
        'morì nel cioccolato bollente',
    (6923, ' die from a curse.'):
        '"Una maledizione uccide " + name(dmghp_charid) + "."',
    (6925, 'died from a curse'):
        'morì per una maledizione',
    (6929, ' tumble down the stairs and die.'):
        'name(dmghp_charid) + " rotola giù per le scale e muore."',
    (6931, 'tumbled down the stairs and died'):
        'cadde dalle scale e morì',
    (6935, '  killed by an audience.'):
        '"Il pubblico uccide " + name(dmghp_charid) + "."',
    (6937, 'was killed by an audience'):
        'morì per mano del pubblico inferocito',
    (6941, '  burnt and turned into ash.'):
        'name(dmghp_charid) + " brucia fino a morire."',
    (6943, 'was burnt and turned into ash'):
        'bruciò fino a sparire',
    (6947, '  killed by food poisoning.'):
        '"Un\'intossicazione uccide " + name(dmghp_charid) + "."',
    (6949, 'got killed by food poisoning'):
        'morì per un\'intossicazione',
    # l'etere corrode: stessa immagine di proc.hsp:25789 e chara_func:2903
    (6953, ' die of Ether Disease.'):
        '"L\'etere corrode " + name(dmghp_charid) + " fino alla morte."',
    (6955, 'died of Ether Disease'):
        'morì della malattia dell\'etere',
    (6959, ' melt down.'):
        'name(dmghp_charid) + " si scioglie in una pozza di liquido."',
    (6961, 'melted down'):
        'si sciolse in una pozza di liquido',
    (6965, ' was consumed by the remnants of the elements and died..'):
        '"I residui degli elementi inghiottono " + name(dmghp_charid) + "."',
    (6967, 'consumed by the remnants of the elements'):
        'sparì fra i residui degli elementi',
    # copiata da action.hsp:3102, stesso inglese e stesso senso
    (6971, ' shatter.'):
        'name(dmghp_charid) + " va in pezzi."',
    (6973, 'committed suicide'):
        'si tolse la vita',
    (6977, '  turned into atoms.'):
        '"L\'esplosione atomica riduce " + name(dmghp_charid) + " in polvere."',
    (6979, 'was killed by an atomic bomb'):
        'morì in un\'esplosione atomica',
    (6983, ' step in an iron maiden and die.'):
        '"La vergine di ferro trafigge " + name(dmghp_charid) + "."',
    (6985, 'stepped in an iron maiden and died'):
        'morì nella vergine di ferro',
    # ⚠️ «stacca la testa a X» fonderebbe: «a il putit». Verbo transitivo
    (6989, '  guillotined and die.'):
        '"La ghigliottina decapita " + name(dmghp_charid) + "."',
    (6991, 'was guillotined'):
        'morì sotto la ghigliottina',
    (6995, ' was executed by result of fair vote.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " finisce al patibolo per voto regolare."',
    (6998, ' weakened and died.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " deperisce fino a spegnersi."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-chara_func-003.jsonl'
DA, A = 6000, 6999
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
