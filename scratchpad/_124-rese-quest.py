# -*- coding: utf-8 -*-
"""124a - Le 22 rese di `quest.hsp`: esiti di incarico, arena, autorita'.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-rese-quest.py

Quinto dei file mai estratti che la 123a aveva trovato.

⚠️⚠️⚠️ **LA REGOLA CHE DECIDE META' DI QUESTO LOTTO E' `guida-stile.md`:51 —
mai un participio riferito al giocatore**, che un genere non ce l'ha. Le quattro
righe di esito dell'arena in inglese sono tutte participi:

    You were defeated.        ->  «Hai perso.»            non «sei stato sconfitto»
    You are victorious!       ->  «Hai vinto!»            non «sei vittorioso»
    Your team is victorious!  ->  «La tua squadra ha vinto!»
    You have failed to        ->  «Non hai saputo         non «non sei riuscito
      protect the client.           proteggere il cliente.»    a proteggere»

⭐ Cinque erano gia' rese altrove, e le ha trovate la ricerca per somiglianza
del giapponese:

    :544  == system.hsp:531    «Ehi, ho un assassino alle spalle!»
    :577  == event.hsp:4584    «Hai perso » + p + « punti fama.»
    :599  == action.hsp:1207, main.hsp:6912   «Hai guadagnato ... punti fama.»
    :672  ~= map.hsp:15265     «Sono comparse delle scale.» (qui: per uscire)
    :896  ~= il gemello di 発言力を200獲得した, «punti autorità»

⚠️⚠️ **`:709` E `:717` HANNO LO STESSO INGLESE E DUE GIAPPONESI DIVERSI** — «The
area is secured!» sta su エリアを制圧した！(caccia e scorta) e su
盗賊団を返り討ちにした！(i ladri). Le firme sono **due**, perche' la firma tiene
dentro anche il giapponese: si possono rendere diverse, e si rendono diverse,
perche' il giapponese distingue e l'inglese no. E' la 122a al contrario — li'
un inglese doppio nascondeva due oggetti, qui ne libera due.

⭐ 討伐 e' «abbattimento» (`text.hsp`, le tre spedizioni contro i demoni);
発言力 e' «autorità» (`glossario.md`); クライアント e' «cliente»
(`text.hsp`, «Scortare il cliente fino a...»); EXバトル e' «Battaglia EX».

⚠️ La freccia si scrive `->`, non →: la piena giapponese e' a due byte e la
build inglese la disegna a due glifi latini. Il progetto scrive gia' cosi' in
«Autorità: N -> M».
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_124-quest.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-quest-001.jsonl')

PREMIO = ('"Nientemeno... %s vittorie! In più, 30000 punti fama."')

RESE = {
    499: 'Hai abbandonato il cliente.',
    518: 'Hai perso.',
    522: '"Hai fallito l\'incarico affidato da " + qname(rq) + "."',
    528: 'Hai commesso un delitto grave!',
    534: 'Non hai saputo proteggere il cliente.',
    # ⓘ `:544` e `:548` sono STATICHE: `estrai` guarda dentro `cnvtalk()` e la
    #    firma e' il testo nudo, non la chiamata. La resa e' il testo, senza
    #    involucro — come il gemello `system.hsp:531`. Scriverci `cnvtalk("...")`
    #    fa scattare la guardia delle virgolette nude, ed e' giusto cosi'.
    544: 'Ehi, ho un assassino alle spalle!',
    548: 'Il veleno, il velenooo!',
    # ⭐ il giapponese dice 火をかぶった, «si e' dato fuoco»: piu' corto
    #    dell'inglese e senza il pronome di genere `him(tc)`, che in italiano
    #    non si puo' rendere su un PNG di genere ignoto.
    552: 'cnvtalk("È scaduto il tempo. A questo punto...")'
         ' + " " + name(tc) + " si dà fuoco."',
    577: '"Hai perso " + p + " punti fama."',
    596: 'La tua squadra ha vinto!',
    599: '"Hai guadagnato " + gdata(GDATA_QUEST_FAME) + " punti fama."',
    603: '"Nuovo primato di livello abbattuto nella Battaglia EX. (Lv"'
         ' + gdata(GDATA_EX_BATTLE_MAX_LVL) + " -> " + enemylv + " )"',
    614: PREMIO % ('" + adata(ADATA_PET_ARENA_WIN, gdata(GDATA_RETURN_AREA)) + "'),
    645: 'La tua squadra ha perso.',
    666: 'Hai vinto!',
    672: 'Sono comparse le scale per uscire.',
    679: PREMIO % ('" + adata(ADATA_ARENA_WIN, gdata(GDATA_RETURN_AREA)) + "'),
    709: 'Zona sotto controllo!',
    717: 'Hai respinto la banda di ladri!',
    724: 'Hai abbattuto il bersaglio!',
    888: '"Hai portato a termine l\'incarico affidato da " + qname(rq) + "."',
    896: '"Hai guadagnato " + hatugen + " punti autorità (ora "'
         ' + mdata(MDATA_CITY_AUTHORITY) + ")."',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        assert v['riga'] in RESE, v['riga']
        v['it'] = RESE[v['riga']]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
