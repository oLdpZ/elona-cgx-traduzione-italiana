# -*- coding: utf-8 -*-
"""124a - Le rese dei quattro file piccoli senza dizionario.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-rese-piccoli.py

`scene.hsp` (1), `custom_nefiatypes.hsp` (2), `map_rand.hsp` (6) e `etc.hsp`
(11): venti firme che chiudono quattro degli undici file che la 123a aveva
trovato **mai estratti**.

⭐⭐⭐ **NOVE DELLE VENTI ERANO GIA' RESE ALTROVE**, e le ha trovate una ricerca
per somiglianza del giapponese su tutto il dizionario (la regola della 113a,
applicata a un lotto intero invece che a una riga):

    etc.hsp:536              == screen.hsp:1422   identica
    etc.hsp:560              == screen.hsp:1395   identica
    etc.hsp:542              ~= screen.hsp:1450   cambia solo il ！ finale
    etc.hsp:545              ~= screen.hsp:1455   cambia solo （ニヤリ）
    etc.hsp:557              ~= screen.hsp:1412   cambia solo ！！！
    custom_nefiatypes.hsp:516 == main.hsp:6543    identica
    map_rand.hsp:653         ~= map.hsp:1486      cambiano gli spazi in testa
    map_rand.hsp:1770        == text.hsp:3052     identica
    scene.hsp:31             == help.hsp:819      identica, ed e' un INVARIATO

⚠️⚠️⚠️ **E IL CONFRONTO HA TROVATO UN DIFETTO NEL LAVORO GIA' FATTO**:
`screen.hsp:1450` scrive «Larneire» con una `n` sola, dove il progetto scrive
«Larnneire» in dodici rese su dodici. E' una resa in gioco dalla sessione che la
scrisse, e nessuna rete la vedeva: `verifica` guarda la forma, non i nomi
propri. La corregge `_124-correzione-larneire.py`.

⚠️⚠️⚠️ **I NOMI DI MAPPA HANNO UN TETTO DI 12 CARATTERI, NON 16.**
`screen.hsp:153` taglia con `strmid(mdatan(MDATAN_NAME), 0, 16 - (maplevel() !=
"") * 4)`: sedici se la mappa non mostra il livello, **dodici se lo mostra** — e
`maplevel()` (`text.hsp:2595`) lo mostra per `AREA_QUEST`, cioe' per tutte e
cinque le mappe di questo lotto. ⭐ Il modello lo conferma monte: i suoi cinque
nomi sono 9, 9, 8, 10, 10, tutti sotto i dodici. Il cancello e'
`_124-nomi-mappa.py`.

⚠️⚠️ **«Mine area» NON E' UNA ZONA MINERARIA.** Il giapponese dice 地雷原 —
地雷 e' la **mina esplosiva** (gia' resa «mina», `db_item.hsp:144067`) e 原 e' la
distesa. Il codice conferma senza margini: l'etichetta e'
`*map_createDungeonMinefield`, il contatore `GDATA_FLAG_MINEFIELD_QUEST_LEVEL` e
le creature che ci nascono sono `CREATURE_ID_LANDMINE_GIRL` e le sue tre
sorelle. E' **campo minato**, e l'inglese e' la lingua ambigua.

⚠️ **«kitty» non si rende**, in nessuna delle tre battute di Lulwy: il
giapponese non dice 子猫ちゃん in nessuna delle tre, e il progetto lo toglie gia'
dove l'inglese lo aggiunge (`text.hsp:12269`, `:12452`). Dove il giapponese lo
dice davvero, la resa e' «gattino» (`command.hsp:7030`, `text.hsp:12156`).
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_124-piccoli.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-piccoli-001.jsonl')

RESE = {
    # --- scene.hsp: il nome del FILE delle scene, non testo. help.hsp:819 ha
    #     gia' la stessa riga, ed e' dichiarata in invariati.md.
    ('scene.hsp', 31): 'scene2.hsp',

    # --- custom_nefiatypes.hsp
    # :505 cornice attorno a due generatori: randomname() pesca da una tabella
    #      di dati e random_title() dalle liste di etc.hsp, che la toppa della
    #      124a rende italiane. Qui non c'e' nessuna parola da tradurre.
    ('custom_nefiatypes.hsp', 505):
        '"<" + randomname() + ">, " + random_title()',
    # :516 identica a main.hsp:6543, che la rende cosi'. Cambia solo la
    #      variabile del boss: li' `tc`, qui `bossrc@NT`.
    ('custom_nefiatypes.hsp', 516):
        '"Attento! Il signore di " + mapname(gdata(GDATA_AREA))'
        ' + " sorveglia questo piano: " + cdatan(CDATAN_NAME, bossrc@NT) + "."',

    # --- map_rand.hsp: cinque NOMI DI MAPPA (tetto 12) e un messaggio
    ('map_rand.hsp', 653): 'Su questo piano si sente il destino...!',
    ('map_rand.hsp', 784): 'Periferia',          # 街近郊, 9 caratteri
    ('map_rand.hsp', 787): 'Campo minato',       # 地雷原, 12 esatti
    ('map_rand.hsp', 938): 'Campi',              # 街周辺の畑, 5
    ('map_rand.hsp', 1287): 'Sala feste',        # パーティー場, 10
    ('map_rand.hsp', 1770): 'Zona urbana',       # 市街地, 11 — text.hsp:3052

    # --- etc.hsp: gli dei che ti dicono di smettere di giocare, un'ora per
    #     riga (`*time_warn_talk`, `hour_played`). La forma e' quella dei
    #     gemelli di screen.hsp: «Nome verbo: » + cnvtalk("battuta").
    ('etc.hsp', 530):
        '"Larnneire incoraggia: " + cnvtalk("Dai, forza!")',
    ('etc.hsp', 533):
        '"Lomias ghigna: " + cnvtalk("Ti seguo da lontano, e faccio il tifo.")',
    ('etc.hsp', 536):
        '"Kumiromi si preoccupa: " + cnvtalk("...Tutto bene... vero?")',
    ('etc.hsp', 539):
        '"Lulwy sogghigna: "'
        ' + cnvtalk("Oh, ti dai più da fare di quanto pensassi.")',
    ('etc.hsp', 542):
        '"Larnneire grida: "'
        ' + cnvtalk("Non va bene. Di questo passo... sarà troppo tardi...")',
    ('etc.hsp', 545):
        '"Lomias ghigna: "'
        ' + cnvtalk("Ma va\', il bello deve ancora venire, no?")',
    ('etc.hsp', 548):
        '"Lulwy avverte: "'
        ' + cnvtalk("Riposati. Se ti rompi, non mi servi più a niente.")',
    ('etc.hsp', 551):
        '"Lulwy ride: "'
        ' + cnvtalk("A quanto pare non serve dirti niente. Fa\' come ti pare.")',
    # ⭐ 元も子もない e' «rimetterci capitale e interessi»: Yacatect e' la dea
    #    della ricchezza e parla in dialetto del Kansai, e la metafora
    #    contabile e' sua. L'inglese la perde («lose everything»).
    ('etc.hsp', 554):
        '"Yacatect si domanda: "'
        ' + cnvtalk("Se ti rovini il corpo, ci rimetti capitale e interessi, no?")',
    ('etc.hsp', 557):
        '"Opatos ride: " + cnvtalk("Muahahahah! Muahaaa!")',
    ('etc.hsp', 560):
        '"Ehekatl ti abbraccia: "'
        ' + cnvtalk("Non morire! Promettimi che non muori! Promettilo!")',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        chiave = (v['file'], v['riga'])
        assert chiave in RESE, chiave
        v['it'] = RESE[chiave]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
