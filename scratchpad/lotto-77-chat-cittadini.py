# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, quel che i PNG rispondono: confessione, sfratto, portafoglio.

Cinque `chatval` di `*chat_default` che hanno in comune la **forma**: righe di
narrazione in terza persona costruite attorno a `cdatan()` o `name()`, dove il
soggetto e' un PNG estratto a caso.

- 100 (`:20316`) — le trenta frasi della confessione erano gia' rese; qui ci
  sono le **sei reazioni**, che nessuno vedeva in italiano.
- 85 (`:20400`, «Cacciare gli intrusi») — lo sfratto e i quattro saluti.
- 32 (`:20907`, «Consegnare il portafogli») — la guardia, e il sospetto quando
  di portafogli ne hai riportati dieci.
- 106 (`:22569`, «Spostati») e 34 (`:21004`, l'ordine di aspettare in citta').

⚠️⚠️ **Niente participi sul PNG.** «non sembra dispiaciuto» (`:20379`) si
accorda col soggetto, che e' estratto a caso: diventa «la prende bene». Cosi'
«che cosa volevi **dirgli**» (`:20356`) diventa «che cosa volevi dire», e
«guarda con una faccia disgustata» mette l'accordo su **faccia**, che e' una
parola nostra (75a).

⚠️ **`:21005` non puo' dire «ordinare A X»**: `name()` porta l'articolo e
stamperebbe «a il cittadino». Il nome diventa complemento oggetto — «Mandi X ad
aspettare in citta'» — che e' la prima delle due vie d'uscita di
`guida-stile.md:275`.

⚠️ **`:20915` non puo' dire «e' vuoto»**: l'oggetto restituito e' il
**portafogli** o la **valigia** (`:20909`-`:20911`, due `itemfind` diversi), e
l'aggettivo cadrebbe sul genere sbagliato una volta su due. «Qui dentro non c'e'
niente!» non si accorda con nessuno dei due.

⚠️ **`:20922` non puo' dire «cittadino modello»**: e' rivolto al giocatore.
«Sei un esempio per tutti i cittadini» mette l'accordo su «esempio» — la via
d'uscita (1) della 75a, il nome predicativo.

⚠️⚠️⚠️ **I quattro saluti dello sfratto seguono il GIAPPONESE, non l'inglese**
(57a, caso 2: *l'inglese scambia*). Le quattro battute escono a sorte da un
`rnd(4)`, quindi a schermo l'ordine non si vede; ma la colonna che si legge
accanto alla resa e' il giapponese, e monte ha accoppiato 「また会う日まで！」
(*alla prossima!*) a «Get out of here!». Le rese dicono quel che dice il
giapponese: «L'uscita e' di qua!», «A casa, a casa!», «Alla prossima!», «Torna a
trovarci!».

⚠️ **Le quattro `lang()` dello sfratto cominciano con uno SPAZIO** e finiscono
dentro `cnvtalk`, che mette le virgolette da se' (`init.hsp:171`, 74a): la resa
tiene la giuntura — `" " + cnvtalk("...")` — e dentro non ci va nessuna
virgoletta.

    python scratchpad/lotto-77-chat-cittadini.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-cittadini.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((20316, 20399), (20400, 20434), (20907, 20940), (21004, 21030),
        (22569, 22592))

NOME = 'cdatan(CDATAN_NAME, tc)'


def saluto(testo: str) -> str:
    return '" " + cnvtalk("%s")' % testo


RESE = {
    # --- 100: le sei reazioni alla confessione
    (20356, ' cares what you tried to tell.'):
        NOME + ' + " si chiede che cosa volevi dire..."',
    (20373, ' felt you creepy.'):
        NOME + ' + " ti guarda con una faccia disgustata..."',
    (20379, " felt it wasn't too bad."): NOME + ' + " la prende bene."',
    (20388, " can't believe the ear..."):
        NOME + ' + " non crede alle proprie orecchie..."',
    (20391, ' looked at you with merciful eyes.'):
        NOME + ' + " ti guarda con occhi pieni di pietà."',
    (20394, ' shrugged.'): NOME + ' + " alza le spalle e lascia perdere."',

    # --- 85: lo sfratto
    (20402, 'Who do you drive out?'): 'Chi vuoi cacciare?',
    (20409, '  moved to the location.'):
        'cdatan(CDATAN_NAME, hometc) + " se ne va."',
    (20419, ' Go back!'): saluto("L'uscita è di qua!"),
    (20423, ' Go home!'): saluto('A casa, a casa!'),
    (20427, ' Get out of here!'): saluto('Alla prossima!'),
    (20431, ' See you again!'): saluto('Torna a trovarci!'),

    # --- 32: il portafogli smarrito
    (20915, "Hmm! It's empty!"): "Uhm... qui dentro non c'è niente!",
    (20916, 'Oops...!'): 'Ops...!',
    (20922, "How nice of you to take the trouble to bring it. You're a model citizen indeed!"):
        ('Che gentilezza, portarcelo fin qui. Sei un esempio per tutti '
         'i cittadini!'),
    (20923, "It's nothing."): 'Era il minimo',
    (20929, "Oh, it's you again? How come you find the wallets so often?"):
        'Uh, ancora tu? Come mai trovi portafogli così spesso?',
    (20930, '(...suspicious)'): "(...qui c'è qualcosa che non va)",
    (20931, 'I really found it on the street!'):
        "L'ho trovato davvero per strada!",

    # --- 106 e 34: spostati, e aspetta in citta'
    (22572, ' gently refuses your request.'):
        'name(tc) + " rifiuta con garbo."',
    (21005, '(You order  to wait in town.)'):
        '"(Mandi " + name(tc) + " ad aspettare in città.)"',
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
