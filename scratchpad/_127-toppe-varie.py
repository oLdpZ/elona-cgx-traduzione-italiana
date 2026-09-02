# -*- coding: utf-8 -*-
"""Il quinto lotto della 127a: sette righe in tre file.

    ai.hsp           3   le suppliche di chi sta per morire
    calculation.hsp  2   la follia
    blend.hsp        2   il titolo della finestra della ricetta, e il piede

⚠️⚠️ **Le tre di `ai.hsp` sono una FAMIGLIA TOPPATA A META', la terza della
127a.** Il loro giapponese e' **identico parola per parola** a quello di tre
righe di `proc.hsp` che la 126a ha gia' toppato (`:20596`, `:20677`, `:20756`
contro `ai.hsp:805`, `:813`, `:821`): e' la stessa scena — un personaggio che
implora di non essere ucciso — scritta due volte nel sorgente. Le rese si
**copiano**, non si riscrivono.
"""
import io
import json

from strumenti.accenti import degrada

NUOVE = {}
MOTIVI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

# --- ai.hsp: le suppliche ---------------------------------------------------

_SUPPLICA = (
    "ai.hsp:*ai_turn, dentro `gdata(GDATA_CUSTOM_TALK) == 100`: quel che dice "
    "un personaggio che sta per essere ucciso e non ha una battuta propria. "
    "⚠️⚠️ E' UNA FAMIGLIA TOPPATA A META': il ramo `if ( jp )` di questa riga e' "
    "IDENTICO PAROLA PER PAROLA a quello di una riga di `proc.hsp` che la 126a "
    "ha gia' resa, quindi la resa si COPIA. Copiare non e' pigrizia: due rese "
    "diverse per lo stesso giapponese sono un difetto che nessuna rete vede, "
    "ed e' la regola della 113a applicata dentro le nostre toppe. "
)

NUOVE[('ai.hsp', 808)] = (
    'txt cnvtalk("Ti do i soldi, ma lasciami vivere!"), '
    'cnvtalk("E-e\' il denaro che vuoi, vero?!")'
)
MOTIVI[('ai.hsp', 808)] = (
    NUDO + _SUPPLICA +
    "Giapponese `ai.hsp:805` = `proc.hsp:20596`, 「カネなら渡すから、許して…！」 e "
    "「か、カネが欲しいん…！？」. Resa copiata dalla toppa di `proc.hsp:20599`. "
    "ⓘ L'inglese delle due righe non e' identico («my every penny» qui, «all I "
    "have» li'): a essere identico e' l'ORIGINALE, ed e' quello che arbitra."
)

NUOVE[('ai.hsp', 816)] = (
    'txt cnvtalk("F-faro\' qualunque cosa, ma non uccidermi!"), '
    'cnvtalk("Del mio corpo fanne quel che vuoi, ma lasciami andare...")'
)
MOTIVI[('ai.hsp', 816)] = (
    NUDO + _SUPPLICA +
    "Giapponese `ai.hsp:813` = `proc.hsp:20677`, 「な、なんでもするから殺さないで」 e "
    "「…の身体は好きにしていいから、見逃して…」. Resa copiata dalla toppa di "
    "`proc.hsp:20680`. ⭐ Il giapponese dice **il corpo**, dove l'inglese si "
    "limita a «whatever you want»: la resa tiene il giapponese, come li'."
)

NUOVE[('ai.hsp', 824)] = (
    'txt cnvtalk("Clemenza... Clementia!"), '
    'cnvtalk("Chiedo scusa! Ti prego, guarda: mi inginocchio!")'
)
MOTIVI[('ai.hsp', 824)] = (
    NUDO + _SUPPLICA +
    "⭐⭐ La PRIMA battuta e' identica: `ai.hsp:821` e `proc.hsp:20756` dicono "
    "tutt'e due 「許してクレメンティア」, cioe' «perdonami» incollato al nome della "
    "mossa <Clementia>, e la 126a l'aveva gia' resa «Clemenza... Clementia!» — "
    "in italiano il gioco di parole si tiene, dove l'inglese l'ha buttato "
    "(«Forgive me...!»). Si copia. ⚠️ La SECONDA no: `proc.hsp` ha "
    "「謝る…！…！」 col secondo pezzo affidato a `_gomen(3)`, qui e' "
    "「謝る…！どうか、このとおり！」 — «chiedo scusa! ti prego, guarda: come "
    "vedi!», dove このとおり indica chi parla prostrato. Due giapponesi diversi "
    "vogliono due rese diverse, e copiare anche questa sarebbe stato "
    "l'errore opposto."
)

# --- calculation.hsp: la follia --------------------------------------------

_FOLLIA = (
    "calculation.hsp:*calcCondition, quel che fa e dice un personaggio con "
    "CDATA_CONDITION_INSANE oltre 100. ⚠️ E' la riga che la 34a cita come "
    "l'origine di `else_jp.py`: «la follia di calculation.hsp:2352 e' uscita in "
    "inglese a schermo». ⚠️ Il ramo giapponese ha CINQUE gruppi (`r2 = rnd(5)`, "
    ":2328) contro i DUE dell'inglese (`r2 = rnd(2)`, :2346): l'inglese ha "
    "buttato tre quinti della scena. La resa NON cambia il `rnd`, che sarebbe "
    "una toppa a blocco: prende dai cinque gruppi giapponesi il contenuto per i "
    "due che ci sono. "
)

NUOVE[('calculation.hsp', 2348)] = (
    'txt name(r1) + " si mette a ballare all\'improvviso.", '
    'name(r1) + " comincia a togliersi i vestiti.", '
    'name(r1) + " si mette a girare in tondo.", '
    'name(r1) + " lancia un grido stranissimo."'
)
MOTIVI[('calculation.hsp', 2348)] = (
    NUDO + _FOLLIA +
    "Il gruppo delle AZIONI, e il suo gemello giapponese e' :2336, che ne ha "
    "quattro dove l'inglese ne ha tre: ci si e' persa 「ぐるぐる回りだした」, "
    "cioe' il girare in tondo. ⚠️⚠️ L'inglese scrive `name(r1) + \" start\" + "
    "_s(r1) + \" to take \" + his(r1) + \" clothes off.\"`: `_s` e `his` a un "
    "argomento sono MORFOLOGIA INGLESE (strumenti/funzioni.py) e vanno tolte, e "
    "con `his` se ne va il possessivo — in italiano «si toglie i vestiti» il "
    "possessivo non lo vuole. ⚠️ Nessun participio: «si mette a ballare», non "
    "«si e' messo a ballare», perche' `name(r1)` puo' essere chiunque."
)

NUOVE[('calculation.hsp', 2352)] = (
    'txt cnvtalk("Fuahahahaa!"), cnvtalk("Perdonami! Perdonami!"), '
    'cnvtalk("Pi... pi... pika..."), cnvtalk("Sciaaaa!"), '
    'cnvtalk("E allora devo uccidere. Si\'♪"), cnvtalk("Brutta lumaca!")'
)
MOTIVI[('calculation.hsp', 2352)] = (
    NUDO + _FOLLIA +
    "Il gruppo delle BATTUTE, e le sei dell'inglese si ritrovano una per una "
    "sparse nei quattro gruppi giapponesi: 「フゥハハハー！」 (:2333), "
    "「許しなさい許しなさい！！」 (:2330), 「ぴ…ぴ…ぴか…」 (:2333, la citazione di "
    "Pikachu), 「シャアァァ」 (:2330), 「じゃあ殺さなきゃ。うん♪」 (:2339), "
    "「このナメクジがっ」 (:2339). ⭐ E l'ultima e' un caso in cui l'inglese "
    "sbaglia bestia: ナメクジ e' la LUMACA senza guscio, e la chiocciola "
    "(かたつむり) e' un'altra battuta ancora, a :2342 — «snail» le ha confuse. "
    "L'italiano distingue, e qui dice «lumaca». ⓘ ♪ e' l'unico carattere a "
    "doppia larghezza che il progetto ammette."
)

# --- blend.hsp --------------------------------------------------------------

NUOVE[('blend.hsp', 1384)] = 's = "Aggiungi " + rpmatname(step)'
MOTIVI[('blend.hsp', 1384)] = (
    NUDO +
    "blend.hsp:*com_blend_material_loop_WHILE1, il TITOLO della finestra che "
    "chiede l'ingrediente successivo di una ricetta. E' il ramo `else` di un "
    "`if ( jp )` (:1381, `rpmatname(step) + \"を追加\"`). ⭐⭐ RESA RISCOSSA A OTTO "
    "RIGHE DI DISTANZA: `blend.hsp:1376` e' una `lang()` gia' in dizionario che "
    "dice la stessa identica cosa — «Aggiungi \"X\".» — ed e' il messaggio che "
    "apre questa stessa finestra. Due parole diverse per lo stesso gesto, a "
    "otto righe l'una dall'altra, sarebbero state visibili a chiunque giochi."
)

NUOVE[('blend.hsp', 1390)] = 's = "" + listmax + " oggetti"'
MOTIVI[('blend.hsp', 1390)] = (
    NUDO +
    "blend.hsp:*com_blend_material_loop_WHILE1, il piede della finestra: quanti "
    "oggetti l'elenco contiene. ⭐ RESA RISCOSSA: `\" items\"` -> «\" oggetti\"» "
    "e' gia' la toppa di `command.hsp:14175`, cioe' il piede dell'inventario — "
    "ed e' proprio la riga da cui `nudi_en.py` e' nato nella 49a. Stessa "
    "finestra di sistema, stessa parola."
)

# ---------------------------------------------------------------------------

SORGENTI = {}


def righe_di(nome):
    if nome not in SORGENTI:
        percorso = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\{}'.format(nome)
        SORGENTI[nome] = io.open(percorso, encoding='cp932').read().split('\n')
    return SORGENTI[nome]


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(nome, n):
    righe = righe_di(nome)
    for altezza in range(1, 25):
        blocco = righe[n - altezza:n]
        quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                     if righe[i:i + len(blocco)] == blocco)
        if quanti == 1:
            return blocco
    raise SystemExit('{}:{}: nessun blocco unico entro 24 righe'.format(nome, n))


PROIBITI = '…“”～«»'

toppe = []
for (nome, n) in sorted(NUOVE):
    righe = righe_di(nome)
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(NUOVE[(nome, n)])
    residuo = [c for c in nuova if c != '♪' and not _codificabile(c)]
    if residuo:
        raise SystemExit('{}:{}: CP932 non sa scrivere {}'.format(nome, n, residuo))
    cattivi = [c for c in nuova if c in PROIBITI]
    if cattivi:
        raise SystemExit('{}:{}: caratteri proibiti {}'.format(nome, n, cattivi))
    if nuova == originale:
        raise SystemExit('{}:{}: la toppa non cambierebbe niente'.format(nome, n))
    cerca = blocco_unico(nome, n)
    sostituisci = cerca[:-1] + [nuova]
    toppe.append({
        'file': nome,
        'cerca': cerca if len(cerca) > 1 else cerca[0],
        'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
        'motivo': MOTIVI[(nome, n)],
    })
    print('{:18s}{:6d}  blocco di {}   {}'.format(nome, n, len(cerca), nuova.strip()[:60]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-varie.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-varie.jsonl'.format(len(toppe)))
