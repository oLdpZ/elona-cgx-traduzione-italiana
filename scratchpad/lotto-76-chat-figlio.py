# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, il figlio: investire negli studi e ammetterne la crescita.

`chatval` 113 (il menu dell'istruzione, sette voci) e 114 (il passo avanti verso
l'eta' adulta). Le due voci che ci portano sono gia' rese dalla 73a:
«<Investire negli studi>» (`:19425`) e «<Ammettere la crescita>» (`:19420`).

⚠️⚠️ **Il sesso del figlio non si sa e non si puo' accordare.** `:22221` tira a
sorte `CDATA_TONE_SEX`, quindi ogni participio («cresciuto», «vicino») sarebbe
sbagliato meta' delle volte. Le vie d'uscita sono quelle della 52a (le battute
dei figli): «ha fatto un passo verso l'eta' adulta» invece di «si sente piu'
vicino», e «Ormai X e' grande!» invece di «X e' cresciuto bene!» — «grande» e'
un aggettivo in -e, invariabile al singolare.

⚠️ **`:22235` gira la frase per non mettere una preposizione davanti al nome.**
L'inglese e' «Invest N gold pieces in X education?»: in italiano il genitivo
vuole «di» e `cdatan(CDATAN_NAME, tc)` non e' garantito nudo. La resa fa del
figlio il **complemento oggetto** — «Far studiare X per N monete d'oro?» — e
usa «per», che non si fonde mai con l'articolo (regola della 70a). Le due
funzioni di contenuto restano tutt'e due, in ordine libero (regola della 40a).

⭐ **DEROGA DICHIARATA a `:22238`.** L'inglese dice «Invest in entrusting
skills(EXP up).», che non vuol dire niente: il giapponese e'
「興味のあることをやらせる(効果増)」, *fargli fare le cose che gli interessano*.
E' la deroga (1) — l'inglese ha perso l'informazione — e la resa segue il
giapponese: «Investire negli interessi (piu' esperienza)». Il resto del menu
resta parallelo all'inglese.

💡 I nomi dei cinque gruppi si leggono nel codice, non nell'inglese: `chatval 2`
sono corpo e fede (`:22287`-`:22294`), `4` sono i mestieri (contrattazione,
falegnameria, cucina, pesca...), `5` l'esplorazione, `6` lo studio e la magia.
E 修行 e' «allenamento» in tutto il progetto (`main.hsp:1524`, `text.hsp:48`).

⚠️ Le due `lang()` che restano nel blocco — 「冷やかし」+`_ka(1)` a `:22258` e
`_thanks(2)` a `:22267` — non sono in questo lotto perche' hanno gia' la loro
resa: la prima l'ha appena presa il lotto dell'oste (stessa firma di `:20093`,
spazio in coda compreso).

    python scratchpad/lotto-76-chat-figlio.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-figlio.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((22212, 22354),)

RESE = {
    # --- 114: il passo verso l'eta' adulta
    (22219, '( realized a little more grown-up!)'):
        '"(" + cdatan(CDATAN_NAME, tc) + " ha fatto un passo verso l\'età adulta!)"',
    (22224, 'You feel like the atmosphere has changed a little...'):
        "Ti sembra che l'atmosfera sia cambiata un po'...",
    (22229, '( has grown well!)'):
        '"(Ormai " + cdatan(CDATAN_NAME, tc) + " è grande!)"',

    # --- 113: il menu dell'istruzione
    (22235, '(Invest  gold pieces in  education?)'):
        '"(Far studiare " + cdatan(CDATAN_NAME, tc) + " per " + cost + " monete d\'oro?)"',
    (22236, 'Cancel'): 'Annulla',
    (22238, 'Invest in entrusting skills(EXP up).'): 'Investire negli interessi (più esperienza)',
    (22241, 'Invest in training skills.'): "Investire nell'allenamento",
    # ⚠️ «Investire nel combattimento» (27) e' bocciato da
    # menu_dialogo.tagliate_a_due_colonne: l'inglese sta in 24 e l'italiano no
    (22244, 'Invest in combat skills.'): 'Investire nelle armi',
    (22247, 'Invest in jobs skills.'): 'Investire nei mestieri',
    (22250, 'Invest in exploration skills.'): "Investire nell'esplorazione",
    (22253, 'Invest in study skills.'): 'Investire nello studio',
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
