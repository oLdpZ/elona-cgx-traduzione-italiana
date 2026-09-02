# -*- coding: utf-8 -*-
"""Le toppe della 127a su `command.hsp`: tre blocchi di righe inglesi nude.

    *skipCustomizationOptions   6   le reazioni alla testa piena di cioccolato
    *inv_skipSc                 5   il regalo di cioccolato, e le due della sfida
    *dump_chara                 5   la scala del potenziale, gia' decisa altrove

⚠️ `applica` si ferma se una toppa non aggancia **o se aggancia due volte**, e
le tre righe del regalo (`:15042`, `:15053`, `:15064`) sono **identiche fra
loro**: il `cerca` si allarga verso l'alto finche' non e' unico, ed e' il ramo
giapponese sopra a distinguerle.

Le righe si leggono dal **sorgente pinnato**: nessuna delle sedici contiene
`lang()`, quindi sono identiche nella build prima delle toppe.
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

# ---------------------------------------------------------------------------
# 1. *skipCustomizationOptions — la scena della testa piena di cioccolato
#
# Sei gradini di CDATA_IMPRESSION, ognuno un `if ( jp ) … else …`: il ramo
# giapponese e' la sorella (la regola della 126a), e qui c'e' sempre.
# ---------------------------------------------------------------------------

SCENA = (
    "command.hsp:*skipCustomizationOptions, `p == 15`: il giocatore si mostra "
    "con la testa impiastricciata di cioccolato, e il PNG reagisce secondo "
    "CDATA_IMPRESSION. ⭐ LA SORELLA GIAPPONESE C'E' (regola della 126a): sta "
    "tre righe sopra, nel ramo `if ( jp )` di cui questa riga e' l'`else`, e "
    "arbitra il contenuto. "
)

NUOVE[7115] = (
    'txt name(tc) + " ti guarda e fa una smorfia di disgusto senza nemmeno nasconderla!", '
    'cnvtalk("Che schifo."), cnvtalk("Sta\' lontano! Che porcata!"), '
    'cnvtalk("Uh... non ci posso credere...")'
)
MOTIVI[7115] = (
    NUDO + SCENA +
    "Gradino CDATA_IMPRESSION < 0, il piu' basso. ⭐⭐ DUE RESE SU QUATTRO SONO "
    "RISCOSSE, NON DECISE: 「このヘンタイ！」 e' gia' «Che porcata!» in dizionario "
    "(la stessa esclamazione, altrove), e 「気持ち悪い」 e' gia' «Che schifo!». "
    "⚠️ «Pervertito» sarebbe stato un aggettivo riferito al GIOCATORE, che in "
    "Elona puo' essere donna: la guida di stile lo vieta, e il giapponese non "
    "lo chiede — ヘンタイ non ha genere. Il difetto si evita rendendo l'atto e "
    "non la persona. ⓘ Il giapponese di 「露骨に嫌そうな顔」 dice «senza "
    "nascondersi», che l'inglese («seems disgusted») aveva smussato."
)

NUOVE[7125] = (
    'txt name(tc) + " prova per te un ribrezzo sincero!", '
    'cnvtalk("Non avvicinarti di un altro passo."), cnvtalk("Guardie! Guardie!!")'
)
MOTIVI[7125] = (
    NUDO + SCENA +
    "Gradino 0 <= impressione < 50. ⭐ 「ガード！ガード！」 e' gia' «Guardie! "
    "Guardie!» in dizionario, quattro volte e sempre uguale: la resa e' "
    "riscossa. ⚠️ «ti trova disgustoso» concorderebbe col giocatore: si rende "
    "il sentimento del PNG («prova un ribrezzo»), che e' anche quel che dice il "
    "giapponese 「本気で気持ち悪がっている」 — il soggetto e' lui, non tu."
)

NUOVE[7135] = (
    'txt name(tc) + " indietreggia di qualche passo. Sembra parecchio a disagio.", '
    'cnvtalk("O-oddio..."), name(tc) + " fa finta di non aver visto niente."'
)
MOTIVI[7135] = (
    NUDO + SCENA +
    "Gradino 50 <= impressione < 100. ⓘ 「何も見なかったことにした」 e' il modo di "
    "dire italiano «fa finta di non aver visto niente», e va al presente come "
    "tutta la terza persona del progetto (guida di stile). ⚠️ L'inglese aveva "
    "«W-wow...», che e' meraviglia; il giapponese 「う、うわぁ…」 e' sgomento."
)

NUOVE[7145] = (
    'txt name(tc) + " ha il viso irrigidito.", cnvtalk("Eh?"), '
    'name(tc) + " guarda una seconda volta e resta di sasso..."'
)
MOTIVI[7145] = (
    NUDO + SCENA +
    "Gradino 100 <= impressione < 150. ⚠️ L'inglese qui usa `was(tc)`, che e' "
    "MORFOLOGIA INGLESE (strumenti/funzioni.py: `was` restituisce sempre una "
    "stringa inglese nuda) e in italiano va tolta con tutto il participio che "
    "regge. «Resta di sasso» e' invariabile in genere, «irrigidito» concorda "
    "con «viso» e non con name(): nessuno dei due chiede il sesso del PNG."
)

NUOVE[7154] = (
    'txt name(tc) + " fa un sorriso imbarazzato...", '
    'name(tc) + ", pur nella confusione, ti consiglia di andarti a lavare al più presto."'
)
MOTIVI[7154] = (
    NUDO + SCENA +
    "Gradino 150 <= impressione < 200. ⚠️ Anche qui l'inglese usa `was(tc)` e "
    "per giunta con una frase rotta di monte («While X was bewildered, and "
    "urged you...»): il giapponese 「困惑しながらも」 e' una subordinata sola, e la "
    "resa la segue. ⚠️ «Perplesso» concorderebbe col PNG: si rende con un "
    "sostantivo, «pur nella confusione», come la guida di stile chiede per le "
    "etichette di stato."
)

NUOVE[7163] = (
    'txt name(tc) + " si preoccupa sul serio per la tua testa...", '
    'cnvtalk("Andiamo a lavare via quel cioccolato, e in fretta.")'
)
MOTIVI[7163] = (
    NUDO + SCENA +
    "Gradino impressione >= 200, il piu' alto. ⚠️ L'inglese usa `is(tc)`, "
    "morfologia inglese, e va tolta. ⭐ «Cioccolato» e non «cioccolata» e' la "
    "parola che il progetto ha gia' scelto in tutta la festa: 「付着していたチョコが"
    "流れ落ちた」 e' «La copertura di cioccolato si e' sciolta via», ed e' la "
    "riga che chiude questa stessa scena."
)

# ---------------------------------------------------------------------------
# 2. *inv_skipSc — il regalo di cioccolato, e le due righe della sfida
#
# ⚠️⚠️ Qui l'inglese NON e' una traduzione del giapponese: e' la stessa riga
# copiata tre volte, `txt cnvtalk("I love you."), cnvtalk("Thank you.")`, su
# tre gradini di CDATA_IMPRESSION che in giapponese hanno tre scene diverse.
# E' il difetto della 126a (la provocazione che portava l'insulto) di nuovo, e
# la resa si prende dal giapponese.
# ---------------------------------------------------------------------------

REGALO = (
    "command.hsp:*inv_skipSc: il giocatore regala il cioccolato a un PNG, e la "
    "reazione dipende da CDATA_IMPRESSION. ⚠️⚠️ L'INGLESE HA BUTTATO LA SCENA: "
    "`txt cnvtalk(\"I love you.\"), cnvtalk(\"Thank you.\")` e' scritto IDENTICO "
    "su tutt'e tre i gradini (:15042, :15053, :15064), mentre il ramo "
    "giapponese ne ha tre diverse e piu' lunghe. E' il difetto della 126a — "
    "l'inglese della provocazione che era l'inglese dell'insulto — nella forma "
    "opposta: non copiato da un'altra scena, ma appiattito su se' stesso. La "
    "resa segue il giapponese, che e' l'originale. "
)

NUOVE[15042] = (
    'txt name(tc) + " guarda te, poi il cioccolato, poi di nuovo te, e non riesce a smettere di sorridere...", '
    'name(tc) + " si commuove e ti salta al collo! Ma torna subito in sé e si stacca di scatto."'
)
MOTIVI[15042] = (
    NUDO + REGALO +
    "Gradino impressione >= 200, il piu' alto (modimp +50). ⚠️ «Tutto "
    "imbarazzato» chiudeva bene la frase e concordava col PNG: tolto. ⓘ Il "
    "`cerca` e' un blocco e non una riga sola, perche' la riga inglese e' "
    "identica a quella degli altri due gradini."
)

NUOVE[15053] = (
    'txt name(tc) + " fa di tutto per nascondere il sorriso che sale!", '
    'name(tc) + " sorride: è un sorriso come non gliene hai mai visto.", '
    'name(tc) + " si sforza di restare impassibile. Ma ha la faccia tutta rossa."'
)
MOTIVI[15053] = (
    NUDO + REGALO +
    "Gradino 150 <= impressione < 200 (modimp +40). Tre battute in giapponese "
    "contro le due copiate dell'inglese. ⚠️ «Non l'hai mai visto sorridere» "
    "avrebbe fatto concordare il participio col PNG attraverso il clitico: "
    "girata in «un sorriso come non gliene hai mai visto», dove «visto» "
    "concorda con «sorriso». «Impassibile» e' invariabile."
)

NUOVE[15064] = (
    'txt name(tc) + " resta un attimo senza parole, poi lascia uscire un\'esclamazione di stupore. Non se lo aspettava proprio.", '
    'name(tc) + " sorride, e il piacere si vede.", '
    'name(tc) + " guarda il cioccolato con gli occhi che brillano: la gioia è tanta."'
)
MOTIVI[15064] = (
    NUDO + REGALO +
    "Gradino 100 <= impressione < 150 (modimp +30). Tre battute in giapponese. "
    "⚠️ 「まんざらでもなさそうだ」 vuole «non gli dispiace affatto», ma «gli» e' "
    "dativo maschile e «le» femminile: in italiano il pronome tradisce il "
    "sesso come il participio, e la resa gira sul fatto («il piacere si "
    "vede»). Stesso motivo per 「余程嬉しかったのか」 -> «la gioia e' tanta»."
)

NUOVE[15531] = (
    'txt "Pagare una fattura a zero fa fallire la sfida. Vuoi farlo davvero?"'
)
MOTIVI[15531] = (
    NUDO +
    "command.hsp:*inv_skipSc, dentro il blocco «JAMES CUSTOM - CHALLENGE - "
    "DOUBLE TAX EACH MONTH»: un'aggiunta del mod, che non ha nessun ramo "
    "`if ( jp )` perche' non e' mai passata da monte. E' l'avviso che precede "
    "un `promptYesNo`, quindi si legge sempre prima di una scelta. ⭐ «Fattura» "
    "e' riscossa da db_item.hsp:144367 (`bill` -> «fattura»), e «sfida» "
    "traduce la categoria TWEAK_CATEGORY_CHALLENGE. ⓘ «A empty bill» e' "
    "sgrammaticato di monte, e «vuota» in italiano direbbe *senza contenuto*: "
    "quel che il codice guarda e' `inv(INV_ITEM_SUB_NAME, ci) == 0`, cioe' "
    "l'importo a zero."
)

NUOVE[15556] = 'txt "HAI EVASO LE TASSE."'
MOTIVI[15556] = (
    NUDO +
    "command.hsp:*inv_skipSc, la riga che chiude la sfida «Tasse doppie ogni "
    "mese» quando la fattura pagata era a zero: `TweakData(...) = (-1)`, cioe' "
    "sfida fallita per sempre. ⓘ Le maiuscole si conservano: sono la voce del "
    "mod, stampata in COLOR_RED dopo un `txtmore`. ⭐ «Tasse doppie ogni mese» "
    "e' gia' in dizionario a :15560, sedici righe piu' giu', e non si tocca "
    "qui. ⓘ «COMMITED» e' un refuso di monte."
)

# ---------------------------------------------------------------------------
# 3. *dump_chara — la scala del potenziale, che il progetto ha gia' deciso
#
# ⚠️⚠️ E' UNA FAMIGLIA GIA' TOPPATA A META'. La stessa scala sta nella scheda
# del personaggio (command.hsp:10677-10700) ed e' gia' italiana per sette
# toppe: Supremo / Enorme / Ottimo / Notevole / Buono / Scarso / Nullo, rese
# riscosse da map_user.hsp:383 e :405. Qui ne servono cinque, minuscole.
# ---------------------------------------------------------------------------

SCALA = {17687: 'superb', 17691: 'great', 17695: 'good',
         17699: 'bad', 17702: 'hopeless'}
RESA = {'superb': 'ottimo', 'great': 'notevole', 'good': 'buono',
        'bad': 'scarso', 'hopeless': 'nullo'}

for _n, _en in SCALA.items():
    NUOVE[_n] = 's += "{}"'.format(RESA[_en])
    MOTIVI[_n] = (
        NUDO +
        "command.hsp:*dump_chara, la scala del POTENZIALE nel dump del "
        "personaggio — il file di testo che il giocatore salva e mostra agli "
        "altri. ⚠️⚠️ NON E' UNA DECISIONE NUOVA: E' UNA FAMIGLIA GIA' TOPPATA A "
        "META'. La stessa scala sta nella scheda del personaggio "
        "(command.hsp:10677-10700), dove sette toppe l'hanno gia' resa "
        "Supremo/Enorme/Ottimo/Notevole/Buono/Scarso/Nullo riscuotendola da "
        "map_user.hsp:383 e :405 («[Potenziale trattativa: Nullo]»). Qui la "
        "resa e' la stessa parola in minuscolo, perche' minuscolo e' "
        "l'inglese: «{}» -> «{}». ⓘ Il tetto e' `fixtxt(s, 15)` a :17707, "
        "quindi quindici caratteri, e la piu' lunga ne usa otto. ⚠️ Il dump "
        "conosce cinque gradini contro i sette della scheda: sopra 200 dice "
        "«superb» dove la scheda direbbe «Supremo». E' un'asimmetria di monte "
        "e non si corregge qui — sarebbe una toppa a blocco.".format(_en, RESA[_en])
    )

# ---------------------------------------------------------------------------


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(n: int) -> list:
    """Il blocco piu' corto che finisce alla riga n ed e' unico nel file."""
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
    # ⚠️ `applica` degrada gli accenti SOLO per le voci di dizionario: le toppe
    #    le scrive grezze, e `nuovo.encode("cp932")` e' strict. Si degrada qui.
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

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-command.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-command.jsonl'.format(len(toppe)))
