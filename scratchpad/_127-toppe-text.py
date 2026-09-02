# -*- coding: utf-8 -*-
"""Il sesto lotto della 127a: i segnaposto `{onii}` e `{syujin}` di `text.hsp`.

`*convert_word` (:7020) e `*talktxt_conv` (:12050) sono **la stessa funzione
scritta due volte**: sostituiscono i segnaposto dentro le battute dei file di
dialogo — `talk.txt` e i file dei PNG personalizzati che il giocatore si scrive
in `user\\`. Le sei righe nude sono tre coppie identiche, e ogni coppia vuole la
stessa resa: si dichiarano `"tutte": true`.

⭐⭐ **Qui il sesso del giocatore SI CONOSCE**, e per una volta l'accordo di
genere non solo si puo' fare, si deve: le righe stanno dentro
`if ( cdata(CDATA_SEX, CHARA_PLAYER) == 0 )`. E' l'eccezione alla regola della
guida di stile — che vieta il participio *quando il genere non si conosce* — e
il codice la porta scritta in fronte.

⚠️⚠️ **E su `syujin` l'inglese ha buttato la distinzione**: il giapponese
sceglie fra ご主人様 (padrone) e お嬢様 (padrona) guardando il sesso del
giocatore, l'inglese dice «master» in tutt'e due i casi. La toppa e' **a
blocco**: rimette le due vie, copiando la forma dal ramo giapponese tre righe
sopra.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\text.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

_DOVE = (
    "text.hsp:*convert_word (:7020) e *talktxt_conv (:12050), che sono la "
    "stessa funzione scritta due volte: sciolgono i segnaposto delle battute "
    "dei file di dialogo. ⓘ Nel `talk.txt` di monte `{onii}` compare solo "
    "nelle sezioni JP — le EN usano `{player}` — ma i segnaposto li scrive "
    "anche il GIOCATORE nei file dei PNG personalizzati (`user\\npc_template.txt` "
    "li documenta): la riga non e' morta, ci si arriva scrivendosi un "
    "compagno. ⚠️ Le due occorrenze sono identiche e vogliono la stessa resa, "
    "quindi la toppa e' dichiarata `tutte`, e sono ESATTAMENTE DUE, contate. "
    "⭐ E qui il sesso del giocatore SI CONOSCE — la riga sta dentro un "
    "`if ( cdata(CDATA_SEX, CHARA_PLAYER) == … )` — quindi l'accordo di genere "
    "non solo si puo' fare: si deve. "
)

TOPPE = [
    {
        'cerca': '\t\t\t\t\t\ts = "brother"',
        'sostituisci': '\t\t\t\t\t\ts = "fratellone"',
        'attese': 2,
        'motivo': (
            NUDO + _DOVE +
            "Il segnaposto `{onii}`, ramo del giocatore maschio. Il giapponese "
            "e' 「お兄」, cioe' la forma con cui ci si RIVOLGE a un fratello "
            "maggiore, non il sostantivo 兄: il template la usa come "
            "「{onii}ちゃん」, e la tenerezza sta nel suffisso. In italiano il "
            "vocativo corrispondente e' «fratellone» — «fratello» renderebbe "
            "il sostantivo e perderebbe il registro, che e' l'unica cosa per "
            "cui quel segnaposto esiste."
        ),
    },
    {
        'cerca': '\t\t\t\t\t\ts = "sister"',
        'sostituisci': '\t\t\t\t\t\ts = "sorellona"',
        'attese': 2,
        'motivo': (
            NUDO + _DOVE +
            "Il segnaposto `{onii}`, ramo della giocatrice. Giapponese 「お姉」, "
            "e vale parola per parola quel che e' scritto per «fratellone»."
        ),
    },
    {
        'cerca': [
            '\t\t\t\telse {',
            '\t\t\t\t\ts = "master"',
            '\t\t\t\t\tbreak',
            '\t\t\t\t}',
        ],
        'sostituisci': [
            '\t\t\t\telse {',
            '\t\t\t\t\tif ( cdata(CDATA_SEX, CHARA_PLAYER) == 0 ) {',
            '\t\t\t\t\t\ts = "padrone"',
            '\t\t\t\t\t}',
            '\t\t\t\t\tif ( cdata(CDATA_SEX, CHARA_PLAYER) == 1 ) {',
            '\t\t\t\t\t\ts = "padrona"',
            '\t\t\t\t\t}',
            '\t\t\t\t\tbreak',
            '\t\t\t\t}',
        ],
        'attese': 2,
        'motivo': (
            NUDO + _DOVE +
            "⚠️⚠️ TOPPA A BLOCCO, e il blocco serve: il segnaposto `{syujin}` "
            "in giapponese ha DUE vie — 「ご主人様」 se il giocatore e' maschio, "
            "「お嬢様」 se e' femmina (:7043-:7046) — e l'inglese le ha "
            "collassate in un «master» solo. In italiano «padrone» detto a una "
            "giocatrice e' un errore, non un'approssimazione, e la via giusta "
            "non si puo' scrivere senza rimettere l'`if`. ⭐ La forma del "
            "blocco non e' inventata: e' COPIATA dal ramo giapponese tre righe "
            "sopra, stesso `cdata(CDATA_SEX, CHARA_PLAYER)`, stesso ordine, "
            "stesso `break`. ⓘ 「お嬢様」 e' la signorina di casa detta da chi "
            "serve, e il suo maschile italiano e' «padrona»: la coppia "
            "padrone/padrona tiene il rapporto, che e' quel che il segnaposto "
            "porta."
        ),
    },
]

for t in TOPPE:
    cerca = t['cerca'] if isinstance(t['cerca'], list) else [t['cerca']]
    quante = sum(1 for i in range(len(righe) - len(cerca) + 1)
                 if righe[i:i + len(cerca)] == cerca)
    if quante != t['attese']:
        raise SystemExit('«{}»: attese {} occorrenze, trovate {}'
                         .format(cerca[-1].strip(), t['attese'], quante))
    for riga in (t['sostituisci'] if isinstance(t['sostituisci'], list) else [t['sostituisci']]):
        riga.encode('cp932')   # solleva se CP932 non sa scrivere
        if any(c in '…“”～«»' for c in riga):
            raise SystemExit('carattere proibito in: {}'.format(riga))
    print('{:4d} occorrenze   {}'.format(quante, cerca[-1].strip()[:60]))

fuori = [{'file': 'text.hsp', 'cerca': t['cerca'], 'sostituisci': t['sostituisci'],
          'tutte': True, 'motivo': t['motivo']} for t in TOPPE]

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in fuori).encode('utf-8')
with io.open('lavoro/toppe-127-text.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe (6 righe) -> lavoro/toppe-127-text.jsonl'.format(len(fuori)))
