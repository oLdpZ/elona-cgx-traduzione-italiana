# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, il numero nuovo, l'offerta al dio e l'indulgenza.

Tre `chatval` gia' resi nel menu dalla 73a: 96 («Nuovo trucco (1 oggetto)»,
`:22145`), 97 («Offrire il bestiame», `:22171`) e 46 («Comprare
un'indulgenza», `:22507`).

⚠️⚠️ **`:22173` perde il pronome, e non lo puo' sostituire con niente che si
accordi.** L'inglese e' «Really offer `him(tc)` to your god?»: `him` a **un
argomento** e' morfologia inglese (`funzioni.py`, la regola del sito) e si
toglie. «Offrirlo» si accorderebbe col compagno, «questo compagno» pure: la
resa nomina il compagno con `name(tc)`, come la 75a ha gia' fatto per «Really
abandon `him(tc)`?» -> «Vuoi davvero abbandonare `name(tc)`?», e come fa il
giapponese di questa stessa riga. Il nome sta a **complemento oggetto**, l'unica
posizione in cui `name()` regge con l'articolo dentro.

⚠️ **`:22159` non puo' dire «con la moneta di bronzo»**: `ioriginalnameref()`
restituisce il nome **nudo** (nel dizionario degli oggetti sono senza articolo)
e l'inglese ci mette «the». La giuntura italiana e' il **due punti** — «impara
un numero nuovo: moneta di bronzo» — che e' la stessa via d'uscita di
`map.hsp:891` per `mapname()` (70a).

⚠️ **`:22509` parla al giocatore ma non lo accorda**: «Il tuo karma non e' cosi'
basso» mette l'accordo su «karma».

💡 **I tre saluti di chi viene offerto stanno su una scala di affetto**
(`CDATA_IMPRESSION` < 100, < 150, oltre): «Ci si vede!», «Vado!», «Ci
rivedremo!». Sono la stessa scala dei sei livelli di sapore della colazione
(74a): tre gradini diversi vogliono tre frasi diverse.

⚠️ 「やめておく」 qui e' «No» (fa coppia con «Si'», `:22174`), mentre a `:3032`
era «Lascio stare»: sono due firme diverse perche' monte scrive due inglesi
diversi, «No.» e «I think not.», e ognuna sta nella sua coppia.

    python scratchpad/lotto-77-chat-dio.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-dio.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((22145, 22170), (22171, 22211), (22507, 22530))

RESE = {
    # --- 96: il numero nuovo
    (22158, 'I see...'): 'Ah, ecco...',
    (22159, '( learned a new trick with the )'):
        ('"(" + name(tc) + " impara un numero nuovo: "'
         ' + ioriginalnameref(inv(INV_ITEM_ID, ci)) + ")"'),

    # --- 97: l'offerta al dio
    (22173, '( Really offer  to your god? )'):
        '"(Vuoi davvero offrire " + name(tc) + " al tuo dio?)"',
    (22174, 'Yes.'): 'Sì',
    (22175, 'No.'): 'No',
    (22179, 'You offer  to .'):
        ('"Offri " + name(tc) + " a " + godname(cdata(CDATA_GOD, CHARA_PLAYER))'
         ' + " pronunciandone il nome."'),
    (22181, 'See you!'): 'Ci si vede!',
    (22184, "I'm going!"): 'Vado!',
    (22187, 'See you again!'): 'Ci rivedremo!',
    (22194, ' glowed brightly and disappeared.'):
        'name(tc) + " brilla di una luce accecante e sparisce."',

    # --- 46: l'indulgenza
    (22509, "You karma isn't that low. Come back after you have committed more crimes!"):
        ('Il tuo karma non è così basso. Torna quando avrai qualche colpa '
         'in più da farti perdonare!'),
    (22513, 'In the authority of all the saints, I will grant you an indulgence, for money of course. The price is  gold pieces.'):
        ('"Per l\'autorità di tutti i santi ti concedo un\'indulgenza; a '
         'pagamento, s\'intende. Fanno " + calcguiltvalue() + " monete d\'oro."'),
    (22515, 'Deal.'): 'Comprare',
    (22517, 'The price is too high.'): 'Troppo caro',
}


def main() -> int:
    voci = []
    for l in io.open(RESTANTE, encoding='utf-8'):
        v = json.loads(l)
        if any(a <= v['riga'] <= b for a, b in ZONE):
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        k = (v['riga'], v['en'])
        if k not in RESE:
            errori.append('%d: voce senza resa | %r' % (v['riga'], v['en'][:80]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:80]))
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci' % (USCITA, len(voci)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
