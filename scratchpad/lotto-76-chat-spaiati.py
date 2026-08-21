# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, altre cinque schermate a meta' (`scratchpad/menu-meta.py`).

    :867-:869     il mercante di passaggio      «Vorrei comprare/vendere» / [manca]
    :1267-:1268   Loyter e il lume della memoria      [mancano tutt'e due]
    :8934-:8944   il medium con cui si lancia         «Lascia com'e'» / [10 mancano]
    :11215-:11220 Irma la forgiatrice           2 voci su 4 / [2 mancano]
    :13713-:13714 Manytia la mercante                 «Nessuno in particolare» / [manca]

⚠️⚠️ **Il menu di Loyter e' entrato per non ROMPERSI, non perche' fosse rotto.**
`:1326`-`:1327` e' a meta' («Vorrei parlarti» c'e', «Use Light of Memory.» no),
ma la firma di quel bottone sta anche a `:1268`, dentro il menu dell'**altro**
Loyter, che oggi e' tutto inglese: tradurre solo `:1327` avrebbe chiuso una
schermata e aperta un'altra. Quindi entra anche `:1267`, e le due schermate si
chiudono insieme. E' la stessa lezione della firma condivisa, vista dal lato in
cui una rete verde puo' diventare rossa **per una riga che non hai toccato**.

⭐ **`:1269` («…。» / «...») e' un INVARIATO gia' dichiarato** (`invariati.md:400`,
«non e' testo: e' un silenzio»): la resa italiana dei puntini e' `...` in ASCII
e coincide con l'inglese per costruzione. E' la firma piu' diffusa del file —
lo stesso silenzio sta a `:1328`, `:20038`, `:23883`.

⭐⭐ **I dieci medium della magia dicono le parole dei MESSAGGI, non quelle
dell'inglese.** `text.hsp:139`-`:148` ha gia' le dieci frasi che il giocatore
legge a ogni lancio — «lancia un incantesimo», «sputa ragnatele», «spruzza
fluidi corporei», «dispiega un cerchio magico», «scaglia un pensiero maligno» —
e il menu che chiede *quale medium* deve usare quelle. E' la regola della 73a
(due schermate che mostrano la stessa scelta dicono le stesse parole) applicata
a un menu e a un messaggio invece che a due menu.
💡 `音声` in inglese e' diventato «spell», non «voice»: la resa segue l'inglese
**e** il messaggio, che dicono tutt'e due «incantesimo».

⚠️ **Due tetti stretti.** `menu_dialogo.tagliate_a_due_colonne` vieta all'italiano
di sforare 24 caratteri dove l'inglese ci sta: «Use Light of Memory.» (20) non
poteva diventare «Usare il lume della memoria» (27), ed e' «Il lume della
memoria» (21); «Let's talk.» (11) e' «Ascoltarlo» — che e' anche quel che dice
il giapponese, 「独り言を聴く」, *ascoltarlo parlare da solo*.

⚠️ **`:11223` — il giapponese e l'inglese non nominano la stessa persona**:
「猫やサリム」 (i gatti e Salim) contro «Thalia and the cats». Si segue l'inglese,
che e' la regola, e lo si dichiara qui. Irma e' donna (`<Irma> la forgiatrice
straniera`), «Lost Irva» e' «Irva Perduta» (`text.hsp:2917`) e Mayroon resta.

    python scratchpad/lotto-76-chat-spaiati.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-spaiati.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((867, 871), (1267, 1270), (8933, 8945), (11215, 11224), (13713, 13716))

RESE = {
    # --- :867 il mercante di passaggio
    (869, 'Not now.'): 'Non adesso',
    (870, "This is your lucky day. I wouldn't normally show my discounted goods to commoners but since I feel so good today..."):
        ('Oggi è il tuo giorno fortunato. Di solito la merce a prezzo scontato non la '
         'faccio nemmeno vedere alla gente comune, ma oggi sono di buon umore...'),

    # --- :1267 Loyter, le due schermate gemelle
    (1267, "Let's talk."): 'Ascoltarlo',
    (1268, 'Use Light of Memory.'): 'Il lume della memoria',
    (1269, '...'): '...',

    # --- :8934 il medium con cui si lancia (le parole di text.hsp:139-:148)
    (8933, 'Hmm... guess I can provide some guidance?'):
        'Hmm... credo di poterti dare qualche dritta.',
    (8934, 'spell'): 'Incantesimo',
    (8935, 'cobweb'): 'Ragnatele',
    (8936, 'fluid'): 'Fluidi corporei',
    (8937, 'tentacle'): 'Tentacolo',
    (8938, 'gaze'): 'Sguardo',
    (8939, 'spores'): 'Spore',
    (8940, 'vibration'): 'Vibrazioni',
    (8941, 'magical circle'): 'Cerchio magico',
    (8942, 'powder'): 'Polvere',
    (8943, 'vicious mind'): 'Pensiero maligno',
    (8945, 'Select new cast style!'): 'Scegli il nuovo modo di lanciare le magie!',

    # --- :11215 Irma la forgiatrice
    (11215, 'That so?'): 'Ah sì?',
    (11217, 'Can you evolve my potioman?'): 'Far evolvere il potioman',
    (11223, "Thalia and the cats have been sneaking into my bed at night. Is it really that cold? Maybe I'm just accustomed to it... Before I came to Lost Irva, I lived in Mayroon."):
        ('Thalia e i gatti mi si infilano nel letto di notte. Fa davvero così freddo? O '
         'sono io che ci ho fatto il callo... Prima di venire a Irva Perduta stavo a '
         'Mayroon.'),

    # --- :13713 Manytia la mercante
    (13714, 'I want the other goods (99999gp)'): "Comprare anche l'altro (99999gp)",
    (13715, 'Yeah? Do you still need something?'): 'Sì? Ti serve altro?',
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
