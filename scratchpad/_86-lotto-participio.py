# -*- coding: utf-8 -*-
"""Il lotto di correzione del participio che si accordava col GIOCATORE.

`chat.hsp:2973` (Miral la fabbra leggendaria, resa nella 84a) chiudeva con
«Vabbè, **sei venuto** fin quaggiù: che posso fare per te?». Il participio si
accorda col giocatore, che non ha genere noto: e' il divieto della
`guida-stile`, e nessuna guardia lo vede — l'ha trovato `scratchpad/referti.py`,
che e' un REFERTO e gira su tutto il dizionario, non sul lotto.

⚠️ Lo stesso referto segnala altri cinque siti, e sono tutti falsi positivi
legittimi: `:3152` «dove sei finita, mamma» (la mamma), `:6420` «Eurypides,
dove sei finito?» (Eurypides), `:9498` «finalmente libero» (Norne, che parla di
se': `db_creature.hsp:78005` gli mette `CDATA_SEX = 0`, cioe' `SEX_MALE`,
`defines/mod.hsp:3770`), `:16586` «la paghi cara» e `:22872` «te la sei cavata»
(due modi di dire, dove il femminile e' il pronome fisso).

Il resto della battuta non si tocca: «Un viandante?» e' un **nome comune** di
genere comune (il/la viandante), che e' la scappatoia dichiarata.
"""
import io
import json
import sys
from pathlib import Path

NUOVE = {
    ('chat.hsp', 2973):
        'Oh oh, chi si vede, roba rara! Un viandante? Ti avrei offerto un banchetto, se non '
        'fosse che oggi la cena tocca a Garok. Sappi che cucina rozzo come lavora. Vabbè, '
        'ormai sei quaggiù: che posso fare per te?',
}

VECCHIE = {('chat.hsp', 2973): 'sei venuto'}


def main() -> int:
    uscita = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_86-participio.jsonl'
    fuori = []
    for percorso in sorted(Path('dizionario').glob('*.jsonl')):
        nome = percorso.name[:-len('.jsonl')]
        for riga in io.open(percorso, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            chiave = (nome, v['riga'])
            if chiave in NUOVE and VECCHIE[chiave] in (v.get('it') or ''):
                v = dict(v)
                v['it'] = NUOVE[chiave]
                fuori.append(v)
    if len(fuori) != len(NUOVE):
        print('attesi %d siti, trovati %d' % (len(NUOVE), len(fuori)))
        return 1
    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in fuori:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d voci in %s' % (len(fuori), uscita))
    return 0


if __name__ == '__main__':
    sys.exit(main())
