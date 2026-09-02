# -*- coding: utf-8 -*-
"""Il secondo lotto della 127a su `command.hsp`: sei blocchi piu' piccoli.

    *com_userNpcExisting_loop  4   le quattro voci dell'evocazione di un CNPC
    *com_knowOther             2   i due titoli di sezione della scheda del PNG
    *com_jukebox_loop          2   il numero di traccia e «No Music»
    *com_mirror_loop_WHILE1    2   il Si'/No delle parti da nascondere
    *com_tachi_e_WHILE1        1   la posa attuale del ritratto
    *com_applySkill_loop       2   il costo in BP nei due menu delle abilita'

Tutte e tredici sono rese **riscosse**, non decise: ognuna ha altrove nel
progetto una sorella gia' resa, e il motivo di ciascuna dice quale.
"""
import io
import json

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

NUOVE = {}
MOTIVI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

# --- *com_userNpcExisting_loop: le quattro voci del menu di evocazione -------

_EVOCA = (
    "command.hsp:*com_userNpcExisting_loop, il menu che chiede come evocare un "
    "personaggio personalizzato gia' conosciuto; la domanda sopra (:7769) passa "
    "da lang() ed e' gia' italiana, le quattro risposte no. "
    "⚠️ «Alleato» e «nemico» avrebbero concordato col PERSONAGGIO EVOCATO, il "
    "cui sesso non si conosce: la guida di stile lo vieta. «Amichevole», "
    "«neutrale» e «ostile» sono invariabili in genere e traducono le tre "
    "relazioni piu' da vicino dell'inglese. ⓘ Il prompt e' largo 280 (:7774). "
)

NUOVE[7770] = 'promptAdd "Evoca come amichevole. (" + ppcost1@NE + " pp)", "null", 1'
MOTIVI[7770] = NUDO + _EVOCA + "1 di 4: RELATION amichevole, costa `ppcost1`."
NUOVE[7771] = 'promptAdd "Evoca come neutrale. (" + ppcost2@NE + " pp)", "null", 2'
MOTIVI[7771] = NUDO + _EVOCA + "2 di 4: RELATION neutrale, costa `ppcost2`, un terzo."
NUOVE[7772] = 'promptAdd "Evoca come ostile.", "null", 3'
MOTIVI[7772] = NUDO + _EVOCA + "3 di 4: RELATION ostile, e non costa niente."
NUOVE[7773] = 'promptAdd "Annulla.", "null", 0'
MOTIVI[7773] = (
    NUDO + _EVOCA + "4 di 4. ⭐ «Annulla» e' riscossa: e' la resa di «Cancel» "
    "in sette voci di dizionario (chat.hsp:7012, :16737, :17702, :18011, "
    ":22236 e altre). ⓘ `\"null\"` non e' testo: e' la lettera di scelta di "
    "`promptAdd` (dichiarato da nudi_accanto_a_lang.py, 61a)."
)

# --- *com_knowOther: i due titoli di sezione --------------------------------

_SCHEDA = (
    "command.hsp:*com_knowOther, la scheda che si apre chiedendo a un PNG di "
    "parlare di se'. E' un blocco `if ( jp ) … if ( en ) …`, quindi la sorella "
    "giapponese c'e'. ⓘ `<title1>` e `<def>` sono marcatori di formato di "
    "`noteadd`, non testo, e restano. Il giapponese apre il titolo con ◆, "
    "l'inglese con `*`: si segue l'inglese, perche' ◆ e' a doppia larghezza e "
    "il progetto non ne ammette (guardie.py). "
)

NUOVE[1573] = 'buff += "<title1>* Pensieri<def>\\n"'
MOTIVI[1573] = (
    NUDO + _SCHEDA +
    "「思考状態」/«Mental state» apre l'elenco di quel che il PNG sta pensando, e "
    "le voci sotto sono gia' in dizionario **in prima persona**: :1575 «Non sto "
    "pensando a niente in particolare», :1578 «Voglio piu' emozioni». Sopra un "
    "elenco di pensieri, «Stato mentale» sarebbe un referto clinico: il titolo "
    "e' «Pensieri»."
)
NUOVE[1793] = 'buff += "<title1>* Punti deboli<def>\\n"'
MOTIVI[1793] = (
    NUDO + _SCHEDA +
    "「苦手なもの」/«Weak point» apre l'elenco dei tipi di danno a cui il PNG e' "
    "poco resistente, gia' in dizionario: :1796 «Attacchi fisici», :1800 "
    "«Attacchi di fuoco», :1804 «Attacchi di gelo». Sono piu' d'uno, quindi il "
    "titolo e' al plurale anche dove l'inglese e' singolare."
)

# --- *com_jukebox_loop ------------------------------------------------------

NUOVE[3869] = 's = "n." + p + "      "'
MOTIVI[3869] = (
    NUDO +
    "command.hsp:*com_jukebox_loop, il numero della traccia nel jukebox. ⭐ La "
    "resa e' riscossa: `No.` -> «n.» e' la scelta che item_func.hsp ha gia' "
    "fatto per le code fra parentesi dei nomi degli oggetti (126a). ⚠️ "
    "L'imbottitura passa da cinque spazi a SEI: «n.» e' un carattere piu' corto "
    "di «No.», e i nomi delle tracce che seguono (` mcTown1`, ` mcSea2`) sono "
    "incollati qui dentro senza altro separatore — senza il compenso l'intera "
    "colonna dei nomi slitterebbe di un carattere a sinistra. ⓘ I nomi delle "
    "tracce sono identificatori dei file musicali, non testo, e non si toccano."
)
NUOVE[4132] = 's += "Nessuna musica"'
MOTIVI[4132] = (
    NUDO +
    "command.hsp:*com_jukebox_loop, la traccia 87 del jukebox: l'unica voce "
    "dell'elenco che non e' il nome di un file musicale ma una scelta — "
    "spegnere la musica. ⓘ Le altre 87 restano com'e' giusto che siano: "
    "`mcTown1` e sorelle sono identificatori."
)

# --- *com_mirror_loop_WHILE1 ------------------------------------------------

_SPECCHIO = (
    "command.hsp:*com_mirror_loop_WHILE1, lo specchio che nasconde i pezzi "
    "dell'equipaggiamento dal ritratto. ⭐ LA RESA E' RISCOSSA: config.hsp:960 "
    "e :977 rendono gia' `On` -> «Si'» e `Off` -> «No», ed e' la convenzione "
    "del progetto per gli interruttori. ⚠️ Qui il valore si incolla "
    "all'etichetta senza separatore (`s += ...` su `s = listn(0, p)`), e "
    "l'etichetta porta il proprio spazio in coda: :12282 ha gia' «Mantello » e "
    "«Corazza  ». E' la regola del LEGGIMI («un'etichetta di menu finisce "
    "sempre con almeno uno spazio»), e qui e' l'unico separatore che c'e'. "
    "ⓘ La colonna va da wx+60 a wx+234 (`window2` a :12307), cioe' 174 px a "
    "7 px per carattere: il margine e' largo, e la resa e' piu' corta "
    "dell'inglese. "
)
NUOVE[12333] = 's += "Sì"'
MOTIVI[12333] = NUDO + _SPECCHIO + "Il ramo `pcc(...) == 0`, cioe' il pezzo si vede."
NUOVE[12336] = 's += "No"'
MOTIVI[12336] = NUDO + _SPECCHIO + "L'altro ramo, cioe' il pezzo e' nascosto."

# --- *com_tachi_e_WHILE1 ----------------------------------------------------

NUOVE[11742] = 'bmes "Posa attuale: face" + cdata(CDATA_FACE, tc) + " ", 235, 235, 35'
MOTIVI[11742] = (
    NUDO +
    "command.hsp:*com_tachi_e_WHILE1, la scritta gialla che dice quale ritratto "
    "e' in posa mentre lo si sfoglia. E' un blocco `if ( jp ) … if ( en ) …`: "
    "la sorella giapponese e' :11738, 「現在の立ち姿：faceN　」, e dice *posa "
    "attuale*, dove l'inglese si limita a «faceN now.». ⭐⭐ E LA RESA E' "
    "RISCOSSA, non tradotta: chat.hsp:18004 rende gia' «(Currently using face)» "
    "con «(Posa attuale: face» + cdata(CDATA_FACE, tc) + «)». Stessa finestra, "
    "stesso dato, stessa parola. ⓘ Lo spazio in coda viene dal giapponese, che "
    "chiude con uno spazio a doppia larghezza: qui e' uno spazio semplice, "
    "perche' serve a staccare la scritta dal bordo e non a impaginare."
)

# --- *com_applySkill_loop e *com_applyWideSkill_loop ------------------------

_BP = (
    "il costo in punti bonus della voce, stampato a destra nel menu che "
    "assegna i punti. ⭐⭐ «Sp» NON RESTA: il progetto ha gia' deciso questa "
    "sigla, e ha deciso di seguire il giapponese. command.hsp:17666 e' una "
    "lang() in dizionario dove l'inglese dice `S. Points : ` e il giapponese "
    "「残りBP     : 」, e la resa italiana e' «BP        : ». Scrivere «Sp» qui "
    "sarebbe due sigle per la stessa cosa a due schermate di distanza. "
    "ⓘ Nessun rischio di larghezza: la riga e' allineata a destra da "
    "`pos wx + 288 - strlen(s) * 7`, e «BP» ha gli stessi due caratteri di "
    "«Sp». "
)
# ⚠️ Le due righe sono IDENTICHE e i due menu sono codice ricopiato per
#    trenta righe in su e sei in giu': nessun blocco unico entro le 24 righe
#    che il generatore prova. E allargare fin dove divergono sarebbe peggio —
#    una toppa lunga trenta righe si rompe al primo ritocco di monte su una
#    qualunque di quelle. Qui la forma giusta e' `"tutte": true`, che applica
#    la toppa a OGNI occorrenza: si dichiara una volta e vale dove chi la
#    scrive ha guardato tutte e due, ed e' il caso (:5384 e :5594, contate).
TUTTE = {
    'file': 'command.hsp',
    'cerca': '\t\ts = "" + sdataref(SKILL_DATAREF_COST, list(0, p)) + " Sp"',
    'sostituisci': '\t\ts = "" + sdataref(SKILL_DATAREF_COST, list(0, p)) + " BP"',
    'tutte': True,
    'motivo': (
        NUDO + "command.hsp:*com_applySkill_loop (:5384) e "
        "*com_applyWideSkill_loop (:5594), " + _BP +
        "⚠️ LE DUE RIGHE SONO IDENTICHE, e i due menu sono lo stesso codice "
        "ricopiato: nessun blocco che le distingua sta entro venticinque "
        "righe. Percio' la toppa e' dichiarata `tutte`, e le occorrenze nel "
        "sorgente pinnato sono ESATTAMENTE DUE, contate, tutt'e due guardate."
    ),
}

# ---------------------------------------------------------------------------


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(n: int) -> list:
    for altezza in range(1, 25):
        blocco = righe[n - altezza:n]
        quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                     if righe[i:i + len(blocco)] == blocco)
        if quanti == 1:
            return blocco
    raise SystemExit('riga {}: nessun blocco unico entro 24 righe'.format(n))


toppe = []
for n in sorted(NUOVE):
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(NUOVE[n])
    residuo = [c for c in nuova if not _codificabile(c)]
    if residuo:
        raise SystemExit('riga {}: caratteri che CP932 non sa scrivere: {}'.format(n, residuo))
    if nuova == originale:
        raise SystemExit('riga {}: la toppa non cambierebbe niente'.format(n))
    cerca = blocco_unico(n)
    sostituisci = cerca[:-1] + [nuova]
    toppe.append({
        'file': 'command.hsp',
        'cerca': cerca if len(cerca) > 1 else cerca[0],
        'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
        'motivo': MOTIVI[n],
    })
    print('{:6d}  blocco di {} riga/e   {}'.format(n, len(cerca), nuova.strip()[:70]))

# la toppa `tutte`, che non passa da `blocco_unico`: si controlla il conto
_quante = sum(1 for r in righe if r == TUTTE['cerca'])
if _quante != 2:
    raise SystemExit('la toppa `tutte` attende 2 occorrenze, ne trova {}'.format(_quante))
toppe.append(TUTTE)
print('  5384  tutte ({} occorrenze)   {}'.format(_quante, TUTTE['sostituisci'].strip()[:60]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-command-2.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-command-2.jsonl'.format(len(toppe)))
