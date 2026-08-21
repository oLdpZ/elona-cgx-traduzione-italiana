# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, il mercante di schiavi: vendere, comprare, e Lily.

`chatval` 37 (`:22355`, «Vendere uno schiavo», `:19395`), `chatval` 52
(`:23274`, «Vendere la madre di Pael», `:19870`) e la riga dell'acquisto
(`:24739`), che era l'ultima rimasta inglese nella scena del catalogo.

⚠️⚠️ **`:22375` e `:24739` sono due dei nove siti «appesi» di `maiuscole`**:
monte scrive «You sell off » + `cnven(nome)`, cioe' alza la maiuscola **in mezzo
alla frase**. Il giudizio scritto in `GIUDICATI` era «chat.hsp non e' ancora
tradotto», e oggi ci arriva il lotto: le due rese mettono il nome **in testa**,
dove la maiuscola e' giusta perche' `name()` porta l'articolo — «La gattina
passa di mano.», «La gattina entra al tuo servizio.». Il sito resta «appeso»
nel referto, perche' la rete misura il **sorgente**; cambia il motivo del
giudizio, e va riscritto.

⚠️ **Nessuna resa nomina il sesso della merce.** Il venduto e' un compagno
qualunque: «questo qui ha un bel fisico» si accorderebbe, e diventa «un bel
fisico, niente da dire»; «e' tuo» si accorderebbe, e diventa «entra al tuo
servizio». E' la regola (3) della 75a.

⭐ **Lily invece si sa che e' donna** (`:23276` la nomina, ed e' la madre di
Pael): li' l'accordo si fa, «Una donna con la faccia da mostro».

💡 **`:23278` segue l'inglese e non il giapponese.** 「やめる」 e' il solito
«Annulla», ma qui monte ci ha messo una battuta — «You cold bastard.» — e il
rifiuto e' un insulto al mercante, non un annullamento. «Carogna senza cuore!»
sta nei 24 caratteri e non si accorda con chi parla.

    python scratchpad/lotto-77-chat-schiavi.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-schiavi.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((22355, 22395), (23274, 23299), (24739, 24739))

RESE = {
    # --- 37: vendere un compagno
    (22361, "Let me see... Hmm, this one's got a nice figure. I'll give you  gold pieces."):
        ('"Vediamo... Uhm, un bel fisico, niente da dire. Ti do "'
         ' + calcslavevalue(rc) * 2 / 3 + " monete d\'oro."'),
    (22362, 'Deal.'): 'Vendere',
    (22363, 'No way.'): 'Annulla',
    (22375, 'You sell off .'):
        'cnven(cdatan(CDATAN_NAME, rc)) + " passa di mano."',

    # --- l'acquisto dal catalogo
    (24739, 'You buy .'):
        ('cnven(cdatan(CDATAN_NAME, MAX_CHARA_NC))'
         ' + " entra al tuo servizio."'),

    # --- 52: la madre di Pael
    (23276, "Look what we have! A woman who got a monster's face. It'll be a good show. Wanna sell me for 50000 gold coins?"):
        ('Toh, una donna con la faccia da mostro! Bella attrazione. '
         "Te la compro per 50.000 monete d'oro."),
    (23277, 'Sure, take her.'): 'Prendila pure',
    (23278, 'You cold bastard.'): 'Carogna senza cuore!',
    (23282, "You sell Pael's mom..."): 'Hai venduto la madre di Pael...',
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
