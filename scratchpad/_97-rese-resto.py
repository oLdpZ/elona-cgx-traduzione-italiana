# -*- coding: utf-8 -*-
"""97a - `command.hsp`: le tre zone che restano (`:8263`-`:11702`).

19 firme, e sono tre cose distinte tenute insieme dal fatto che sono quel che
avanza: l'evocazione dei PNG personalizzati (`:8263`-`:8372`), le quattro targhe
della scheda del personaggio (`:10268`-`:11215`) e i sei suggerimenti della
regolazione del segno dell'oggetto (`:11427`-`:11702`).

⭐⭐⭐ LA COSA PIU' UTILE DEL LOTTO: **`:11453` E `:11640` HANNO LO STESSO
INGLESE E DUE GIAPPONESI DIVERSI — ED E' LA FAMIGLIA CHE NESSUNA RETE VEDE.**

    :11453  lang("移動を終えた。", "You finished the adjustment.")
    :11640  lang("調整を終えた。", "You finished the adjustment.")

移動 e' **spostare**, 調整 e' **regolare**, e sono due comandi diversi:
`*com_item_mark` muove il segno, `*com_item_mark_adjust` ne cambia la forma.
L'inglese le ha fuse in una frase sola; l'italiano puo' tenerle distinte, e
allora le tiene. ⚠️ `battute --divergenti` **non** le avrebbe viste — cerca un
giapponese reso in piu' modi, e questi due giapponesi sono diversi. E' la rete
che manca del punto 5 della ripresa, la stessa forma del `(Empty)` della 96a, e
questa volta la coppia e' **due frasi diverse**, non due sinonimi.

⚠️ LA SECONDA: `*com_item_mark_adjust` PORTA UN COMMENTO CHE DICE «UNUSED», E IL
COMMENTO HA TORTO. `:11612` scrive «Unused in cgx, all functionality is added to
the above code», e sembra il permesso di rinviare `:11620`, `:11640` e `:11652`.
Ma `command.hsp:6833` fa `gosub *com_item_mark_adjust` sul ramo `p == 26`, che e'
una voce di menu come le altre. **Un commento non e' una misura** (la lezione
della 34a): si e' cercato il nome nel sorgente, il chiamante c'e', le tre righe
si traducono.

⭐ LA TERZA: `:8343` NON PUO' AVERE UN PARTICIPIO. La riga e'
`listn(0, listmax) + lang("は、…召喚された！", " has been summoned to your world!")`,
cioe' il nome del PNG **piu'** la coda: «è stato evocato» sbaglia su ogni PNG
femminile, e il nome lo sceglie chi ha scritto il file `.npc`. Si gira sul verbo
attivo — « risponde alla chiamata ed entra nel tuo mondo!» — che non ha genere.
E' la stessa regola del lotto della conoscenza dell'oggetto.

💡 `:8263` prende la resa che `:7608` ha gia' dato allo stesso gesto («Chi
desideri evocare?»): due giapponesi diversi, una resa sola, e va bene — la rete
che si arrabbierebbe e' quella del giapponese reso in **piu'** modi, non questa.

⚠️ Due voci di queste zone **non sono rese, e stanno altrove**:
  - `:8372` e' `lang("JP", "EN")`, la **chiave** del blocco dentro
    `data\book.txt`: sta in `invariati.md`, accanto al gemello di `help.hsp:228`;
  - `:11066` e' morta **per assegnazione** (`:11069` riscrive `s`): sta in
    `rinviate.jsonl`, e con lei la scoperta del letterale nudo `"Have"`.

LESSICO EREDITATO (non deciso qui):
  - PNG                  `chara.hsp:4314`, `command.hsp:3543` «Elenco dei PNG»
  - Cursore              `command.hsp:10344`, `Cursor [...]` -> «Cursore [...]»
  - Invio                `command.hsp:10347`, `:10351`, `:10358`, `:10366`
  - Allena / Impara abilità   `command.hsp:10358`, `:10366`
  - abilità              `glossario.md`, `Skill`
  - incantesimo          `glossario.md`

PERIMETRO: 19 firme su 19 (21 meno le due qui sopra), nessuna in un ramo
`if ( jp )` (`python scratchpad/_97-vive.py`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
⚠️ `:11430` e `:11433` cominciano con **undici spazi** che allineano le tre
righe del suggerimento sotto la prima: si conservano.
"""
import io
import json
import sys

RESE = {
    # --- l'evocazione dei PNG personalizzati
    (8263, 'Which one do you wish to summon?'): 'Chi desideri evocare?',
    (8270, 'Enter [Summon] '): 'Invio [Evoca] ',
    (8343, ' has been summoned to your world!'): ' risponde alla chiamata ed entra nel tuo mondo!',
    (8372, 'EN'): 'EN',

    # --- le quattro targhe della scheda, e il rifiuto del bonus
    (10268, 'Character Sheet'): 'Scheda del personaggio',
    (10270, 'Skill Training'): 'Allenamento delle abilità',
    (10273, 'Skill Learning'): 'Apprendimento delle abilità',
    (10276, 'Skill Select'): 'Scelta delle abilità',
    (10311, 'Train which skill?'): 'Quale abilità vuoi allenare?',
    (11215, "Bonuses can't be used for that spell."):
        'I bonus non si possono spendere su quell\'incantesimo.',

    # --- il segno dell'oggetto: spostarlo (`*com_item_mark`)
    (11427, 'Item Mark:'):
        'Segno oggetto: W/S altezza, A/D larghezza, Z/X angolo, Q/E dimensione.',
    (11430, '           ARROW keys to move'):
        '           Cursore per spostare, G davanti/dietro, F specchia, R azzera.',
    (11433, '           ENTER key to save'):
        '           Invio salva, Shift annulla ed esce, K cancella ed esce.',
    (11453, 'You finished the adjustment.'): 'Hai finito di spostare.',
    (11483, 'You stopped the adjustment.'): 'Hai smesso di spostare.',

    # --- il segno dell'oggetto: regolarlo (`*com_item_mark_adjust`)
    (11620, 'Up and down keys to adjust item mark length'):
        'Su/Giù altezza, Sinistra/Destra larghezza, z/x angolo, Invio conferma, Annulla esce.',
    (11640, 'You finished the adjustment.'): 'Hai finito di regolare.',
    (11652, 'You quit adjustment.'): 'Hai smesso di regolare.',

    # --- la scelta dell'immagine (`*com_tachi_e`)
    (11702, 'Left and right keys to change graphic'):
        'Sinistra/Destra per cambiare immagine, Invio conferma, Annulla esce.',
}

LOTTO = 'lavoro/97-command-resto.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]


def chiave(v):
    trovate = [k for k in RESE if k[0] == v['riga'] and v['en'].startswith(k[1])]
    if len(trovate) != 1:
        return None
    return trovate[0]


mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
usate = {chiave(v) for v in voci if chiave(v)}
in_piu = [k for k in RESE if k not in usate]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
