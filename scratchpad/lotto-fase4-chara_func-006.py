# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-006: i versi del dolore, il corpo che cambia e chi si
sdoppia (chara_func.hsp 8000-8999).

27 rese. Il blocco del corpo: peso, statura, vomito, anoressia, i presentimenti
del cibo e la scissione.

⭐ **`:8317` e' una delle righe dello screenshot della 39ª, ed era gia' decisa.**
「は漏らした。」 sta anche a `chara_func.hsp:3377`, reso «X se la fa addosso.»
nel lotto 001 di ieri: la stessa firma in due punti dello stesso file, e il
dossier l'ha pescata. E' la riga per cui `chara_func.hsp` e' stato aperto —
compariva in inglese nel collaudo — e si chiude copiando, non decidendo.

⚠️⚠️ **`:8629` e' il trentacinquesimo errore di monte, e stampa una lettera
sola.** Il giapponese e' 「name(A)の生命核はname(B)の遺伝子を獲得した。」, due
personaggi; l'inglese scrive `name(A) + " get genes of " + _s(B) + "."`, cioe'
mette **`_s()` dove andava `name()`**. `_s()` restituisce «s» o niente
(morfologia della terza persona), quindi a schermo la build inglese stampa
«`X get genes of s.`» oppure «`X get genes of .`» ⚠️ **E la rete 11 non lascia
scrivere la resa giusta**, perche' l'inglese dichiara **un** `name()` solo: e'
esattamente `proc.hsp:18280` della 38ª. ✅ Reso nominando il soggetto e
lasciando implicito il donatore — «X acquisisce i geni nel nucleo vitale» —
come la 38ª aveva stabilito.

⚠️ **Le sei voci di `:8007` stanno tutte sulla STESSA RIGA**, sei `lang()` una
di fila all'altra dentro un `txt`, ed e' il numero piu' alto del progetto su una
riga sola. Sono i versi di chi incassa un colpo, dentro `cnvtalk()`: statiche,
quindi la resa e' **testo nudo** e non un'espressione (la lezione della 36ª,
quando la rete 11 nata sbagliata avrebbe bocciato undici rese giuste).
⚠️ **E l'inglese ne ha inventata una**: 「くっ！」 e' un mugolio di dolore, e la
riga inglese dice «`Kill me already!`», che e' un'altra cosa. Reso sul
giapponese.

⚠️ **`:8751` e `:8754` sono un inglese solo per due giapponesi, e il codice
decide quale.** «`X splits!`» sta per 分身 — lo sdoppiamento del ninja, l'ombra
che non e' viva — e per 分裂, la scissione vera, quella della melma che diventa
due. Il ramo li separa: `instr(locvar_dmghp_s, 0, "/man/")` piu' l'arpia e il
ninja rosso da una parte, tutto il resto dall'altra. ✅ «si sdoppia» e «si divide
in due». 💡 E «si sdoppia» non l'ho scelta io: e' gia' di `action.hsp:12361`,
sotto lo stesso inglese.

⚠️ **Il peso vuole un aggettivo INVARIABILE, e ce n'era gia' uno.**
`proc.hsp:10612` rende 「は太った。」 «X diventa piu' pesante», e «pesante» sta
bene con tutt'e due i generi: si copia, e la rete 3 lo pretende. ⚠️ Ma il
gemello 「は痩せた。」 non puo' fare «piu' leggero», che invece **concorda**.
✅ Girato col verbo: «X perde peso». E' la strada del participio applicata a un
aggettivo, e la coppia esce asimmetrica apposta.

💡 **E i due blocchi del cibo sono ricopiati, come `resistmod`/`resistmodh` del
lotto 002**: `eatstatus` (`:8655`, `:8661`) e `eatstatusfood` (`:8677`, `:8683`)
dicono le stesse due frasi con una variabile diversa. Quattro voci, due rese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- i sei versi di chi incassa un colpo. Stanno tutti sulla STESSA riga,
    #     dentro cnvtalk(): statiche, quindi la resa e' testo nudo.
    # ⚠️ l'inglese di 「くっ！」 dice «Kill me already!», che e' un'altra cosa:
    #    il giapponese e' un mugolio. Reso sul giapponese
    (8007, 'Kill me already!'):
        'Ngh!',
    (8007, 'No... not yet...!'):
        'Non ancora!',
    (8007, "I can't take it anymore..."):
        'Non ce la faccio più...',
    (8007, 'Argh!'):
        'Uuugh',
    (8007, 'Uhhh'):
        'Ah',
    (8007, 'Ugggg'):
        'Aaah',

    # ⚠️ genitivo: «la mente di X»
    (8039, 'Magic reaction hurts !'):
        '"Il contraccolpo del mana colpisce " + name(dmgmp_charid) + " nella mente!"',

    # --- il peso e la statura.
    # copiata da proc.hsp:10612, stesso giapponese. «pesante» non concorda
    (8178, ' gain weight.'):
        'name(modweight_charid) + " diventa più pesante."',
    # ⚠️ ma «più leggero» concorderebbe: girato col verbo
    (8181, ' lose weight.'):
        'name(modweight_charid) + " perde peso."',
    # ⚠️ genitivo: «la statura di X»
    (8197, ' grow taller.'):
        'name(modheight_charid) + " cresce un poco in altezza."',
    (8200, ' grow smaller.'):
        'name(modheight_charid) + " cala un poco in altezza."',

    # --- il vomito e l'anoressia. ⚠️ genitivo: «l'anoressia di X»
    (8211, ' manage to recover from anorexia.'):
        'name(cure_anorexia_charid) + " guarisce dall\'anoressia."',
    (8220, ' vomit.'):
        'name(chara_vomit_charid) + " vomita."',
    # ⚠️ il giapponese dice 異物, «corpo estraneo», non «children»
    (8225, ' spit children from  body!'):
        'name(chara_vomit_charid) + " sputa fuori quello che aveva in corpo!"',
    (8270, ' develop anorexia.'):
        'name(chara_vomit_charid) + " sviluppa l\'anoressia."',
    # stessa forma di chara_func:3543, 健康のお守り e' <Amuleto di Jure>
    (8280, 'But the Amulet of Jure shines brightly for a moment, instantly curing the anorexia.'):
        'Ma l\'<Amuleto di Jure> brilla per un istante e guarisce l\'anoressia sul colpo.',
    # copiata da chara_func:3377, stesso giapponese. E' una riga dello screenshot
    (8317, ' is incontinent.'):
        'name(chara_morasi_arg1) + " se la fa addosso."',

    # --- il nucleo vitale. ⚠️ l'inglese mette _s() dove andava name(): la rete
    #     11 concede un name() solo, quindi il donatore resta implicito
    (8629, ' get genes of .'):
        'name(gain_iden_charaid2) + " acquisisce i geni nel nucleo vitale."',
    (8634, '[Phase 1 progress  %]'):
        '"[Fase 1, avanzamento: " + locvar_gain_iden_sintyoku + "%]"',
    # in giapponese l'intestazione e' gia' in lettere latine: resta com'e'
    (8640, '[SURVIVABILITY EXTENSION !] Phase 1 completed. From now on, it need to grow with the nutrition of foods.'):
        '[SURVIVABILITY EXTENSION!] Fase 1 completata. D\'ora in poi deve crescere con il nutrimento del cibo.',

    # --- i presentimenti del cibo. Due blocchi ricopiati: quattro voci, due rese
    (8655, ' feel bad.'):
        'name(eatstatus_arg2) + " ha un brutto presentimento."',
    (8661, ' feel good.'):
        'name(eatstatus_arg2) + " ha un buon presentimento."',
    (8677, ' feel bad.'):
        'name(eatstatusfood_charaidx) + " ha un brutto presentimento."',
    (8683, ' feel good.'):
        'name(eatstatusfood_charaidx) + " ha un buon presentimento."',
    (8703, ' feel grumpy.'):
        'name(sickifcursed_arg2) + " si sente male."',

    # --- la scissione. ⚠️ un inglese per due giapponesi, e il codice decide:
    #     分身 e' l'ombra del ninja, 分裂 e' la melma che diventa due
    # «si sdoppia» e' gia' di action.hsp:12361, sotto lo stesso inglese
    (8751, ' split!'):
        'name(charaCanSplit_charidx) + " si sdoppia!"',
    (8754, ' split!'):
        'name(charaCanSplit_charidx) + " si divide in due!"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-chara_func-006.jsonl'
DA, A = 8000, 8999
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
