# -*- coding: utf-8 -*-
"""Le toppe della **schermata del titolo** e dell'indicatore dei turni automatici.

Otto righe nude vive: le sette dei crediti che il gioco stampa sul titolo
(`system.hsp:*game_title`) e l'etichetta «AUTO TURN» della barra di stato
(`screen.hsp:*screen_drawAutoTurn`).

⭐ **I crediti sono la prima cosa che il giocatore legge**, e sono rimasti
inglesi per centoventicinque sessioni perche' non passano da nessuna `lang()`.
Il menu sotto di loro e' gia' italiano da una toppa vecchia (`:3540`), quindi il
titolo mostrava un menu tradotto sotto sette righe inglesi.

## ⚠️ La larghezza: il metro e' l'inglese, non una costante presa in prestito

Le sette righe stanno a `pos 20` con `font …, 13 - en * 2`, cioe' **font 11**, su
un titolo da 800 px scalato a `windoww`. Il passo di quel font **non e' mai
stato misurato su questa schermata**, e la 118a insegna che prendere una
costante da un'altra rete dicendo «tanto e' lo stesso carattere» e' esattamente
il difetto.

⭐ **Quindi il tetto qui e' l'inglese stesso**: la riga inglese e' quella che il
gioco spedisce e che quindi ci sta. Una resa non piu' lunga della riga che
sostituisce e' dentro il tetto **senza bisogno di sapere quanto vale il tetto**.
Lo script lo pretende e si ferma se una resa sfora — la piu' lunga, `:3511`, ha
103 caratteri in inglese.

## ⓘ «AUTO TURN» e' l'unica che sfora, e la sua geometria si legge

`screen.hsp:2194` disegna la finestrella `window2 sx, sy, 148, 25` e scrive a
`pos sx + 43`: restano **105 px** per l'etichetta. «TURNO AUTO» ha dieci
caratteri contro i nove dell'inglese, cioe' vuole un passo non superiore a
**10,5 px** — e i due passi che il progetto ha misurato per questo carattere
sono **6,5** (pannello di `screen.hsp:100`, 125a) e **7,7** (menu, `larghezze.py`).
Il margine e' largo, e l'argomento non e' «tanto e' lo stesso carattere»: e' che
qualunque passo plausibile ci sta.

## Che cosa dicono le rese

    Developed by            ->  Sviluppo di
    originally created by   ->  ideato da
    maintained by …         ->  curato da …
    mod created by          ->  mod creata da
    Contributor …           ->  Contributi di …
    View the credits for more  ->  Vedi i crediti

⚠️ **I nomi non si toccano**: `Noa`, `Ano`, `AnnaBannana`, `BloodyShade`,
`Hebiko`, `Glyphy`, `Jehmil`, `Ruin0x11`, `f1r3fly`, `Sunstrike`, `Schmidt`,
`Elvenspirit` sono le persone che hanno scritto il gioco e i mod, e i titoli
`Elona`, `ElonaPlus`, `Elona+ Custom-G`, `Elona+ Custom-GX` sono i nomi dei
prodotti. `&` diventa «e», che e' la congiunzione italiana, e `et al` diventa
«e altri».

⚠️ Gli spazi doppi di `:3502` e `:3504` sono di monte e restano dove sono:
separano il nome del gioco dalla riga di credito, ed e' un allineamento.

⚠️ Si compone tutto in memoria e si scrive alla fine: regola della 39a.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
USCITA = 'scratchpad/_126-toppe-titolo.jsonl'

_CIECO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

_TITOLO = (
    "system.hsp:*game_title, i crediti che il gioco stampa sulla schermata del "
    "titolo — la prima cosa che il giocatore legge, rimasta inglese sotto un "
    "menu gia' italiano (:3540). ⚠️ Il tetto di larghezza di questa schermata "
    "non e' mai stato misurato: il metro qui e' la riga inglese, che il gioco "
    "spedisce e che quindi ci sta, e la resa non e' piu' lunga di lei. "
    "⚠️ I nomi delle persone e dei prodotti non si toccano. "
)

# (file, riga, [(letterale, resa)], motivo)
CASI = [
    ('system.hsp', 3502,
     [('"Elona  Developed by Noa"', '"Elona  Sviluppo di Noa"')],
     _CIECO + _TITOLO),
    ('system.hsp', 3504,
     [('"ElonaPlus  Developed by Ano"', '"ElonaPlus  Sviluppo di Ano"')],
     _CIECO + _TITOLO +
     "ⓘ Lo spazio doppio dopo il nome del gioco e' di monte e resta: allinea "
     "questa riga con quella sopra."),
    ('system.hsp', 3509,
     [('"ElonaPlus Custom originally created by AnnaBannana"',
       '"ElonaPlus Custom ideato da AnnaBannana"')],
     _CIECO + _TITOLO +
     "ⓘ «ideato» tiene dentro «originally created»: e' chi l'ha pensato per "
     "primo, e la riga sotto dice chi lo porta avanti adesso."),
    ('system.hsp', 3511,
     [('"ElonaPlus Custom maintained by AnnaBannana & BloodyShade, contributions by Hebiko, Glyphy, Jehmil, et al"',
       '"ElonaPlus Custom curato da AnnaBannana e BloodyShade, contributi di Hebiko, Glyphy, Jehmil e altri"')],
     _CIECO + _TITOLO +
     "E' la riga piu' lunga della schermata: 103 caratteri in inglese, e la "
     "resa ne ha meno. «&» diventa «e» e «et al» diventa «e altri»."),
    ('system.hsp', 3513,
     [('"Elona+ Custom-G mod created by Glyphy"',
       '"Elona+ Custom-G mod creata da Glyphy"')],
     _CIECO + _TITOLO +
     "ⓘ «mod» resta ed e' femminile in italiano («la mod»), come «una "
     "modifica»: e' la parola che la comunita' italiana dei giochi usa."),
    ('system.hsp', 3515,
     [('"Elona+ Custom-GX mod created by Ruin0x11"',
       '"Elona+ Custom-GX mod creata da Ruin0x11"')],
     _CIECO + _TITOLO +
     "Come :3513, ed e' la mod su cui questa traduzione lavora."),
    ('system.hsp', 3524,
     [('"Contributor f1r3fly, Sunstrike, Schmidt, Elvenspirit / View the credits for more"',
       '"Contributi di f1r3fly, Sunstrike, Schmidt, Elvenspirit / Vedi i crediti"')],
     _CIECO + _TITOLO +
     "ⓘ E' il ramo `else` di un `if ( jp )`, cioe' quello che la build italiana "
     "esegue; la gemella giapponese (:3521, «Contributor MSL / …») porta "
     "un'altra lista di nomi ed e' una delle tre righe che "
     "`_126-nudi-nel-ramo-jp.py` dichiara morte."),

    ('screen.hsp', 2198,
     [('"AUTO TURN"', '"TURNO AUTO"')],
     _CIECO +
     "screen.hsp:*screen_drawAutoTurn, l'etichetta della finestrella che dice "
     "che i turni stanno scorrendo da soli. "
     "ⓘ LA GEOMETRIA SI LEGGE, non si eredita: :2194 disegna "
     "`window2 sx, sy, 148, 25` e :2196 scrive a `pos sx + 43`, quindi "
     "l'etichetta ha 105 px. Dieci caratteri contro i nove dell'inglese vogliono "
     "un passo non superiore a 10,5 px, e i due passi misurati dal progetto per "
     "questo carattere sono 6,5 (pannello di screen.hsp:100, 125a) e 7,7 (menu, "
     "larghezze.py). Il margine e' largo."),
]

ACCENTATE = 'àèéìòùÀÈÉÌÒÙ'

nuove = []
for nome, numero, coppie, motivo in CASI:
    righe = io.open(f'{SORGENTE}\\{nome}', encoding='cp932').read().split('\n')
    riga = righe[numero - 1]
    if righe.count(riga) != 1:
        raise SystemExit(f'{nome}:{numero} compare {righe.count(riga)} volte')
    nuova = riga
    for prima, dopo in coppie:
        if riga.count(prima) != 1:
            raise SystemExit(f'{nome}:{numero} contiene {prima!r} '
                             f'{riga.count(prima)} volte')
        # ⚠️ Il tetto e' l'inglese: `screen.hsp:2198` e' l'unica deroga, e la
        #    sua geometria e' letta nel motivo della toppa.
        if len(dopo) > len(prima) and not (nome == 'screen.hsp' and numero == 2198):
            raise SystemExit(f'{nome}:{numero}: la resa {dopo} ha '
                             f'{len(dopo) - 2} caratteri contro i '
                             f'{len(prima) - 2} dell\'inglese, e il tetto di '
                             'questa schermata non e\' misurato')
        nuova = nuova.replace(prima, dopo)
    if nuova == riga:
        raise SystemExit(f'{nome}:{numero} non cambia')
    fuori = [c for c in ACCENTATE if c in nuova]
    if fuori:
        raise SystemExit(f'{nome}:{numero} porta {fuori}: le toppe si scrivono '
                         "gia' degradate")
    nuova.encode('cp932')
    nuove.append({'file': nome, 'cerca': riga, 'sostituisci': nuova,
                  'motivo': motivo})

testo = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in nuove)
io.open(USCITA, 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{len(nuove)} toppe in {USCITA}')
