# -*- coding: utf-8 -*-
"""97a - `command.hsp`: il pannello «Conoscenza dell'oggetto» (`:16054`-`:16987`).

25 firme. E' la finestra che si apre esaminando un oggetto — 600x408, testo a
`wx + 68`, font 12 — piu' le tre righe di contorno che vivono nella stessa zona
(il titolo, «nessun bersaglio», la conferma dell'attacco).

⭐⭐⭐ LA COSA CHE GOVERNA TUTTO IL LOTTO: **IL SOGGETTO E' L'OGGETTO, E IL SUO
GENERE NON SI SA.** L'inglese scrive «It is precious.» e se la cava: `it` non ha
genere. In italiano «È prezioso» sbaglia su ogni spada, ogni pozione, ogni
armatura. Non e' un dettaglio di stile: sono **dieci righe su venticinque**, e
il difetto uscirebbe su meta' degli oggetti del gioco.

La regola seguita, riga per riga: **si evita il participio e l'aggettivo
accordato**, con una di tre mosse —

  1. un aggettivo invariabile:  «È resistente al fuoco.»  (resistente, non
     «ignifugo/a»);
  2. un nome nostro che porta il proprio genere: «È **un oggetto** prezioso.»,
     «È **un'arma** leggera.», «È **merce** rubata.»;
  3. il verbo al posto dell'aggettivo: «**Ha** vita propria.», «**Ha** la
     benedizione di Ehekatl.», «**Finché è addosso**, fa avanzare…».

⚠️ La mossa 3 e' quella che salva `:16312`: «Se equipaggiato…» e «indossandolo…»
hanno tutt'e due il genere dentro. «Finché e' addosso» no, e vale per un'arma
come per un'armatura.

⚠️ E vale anche per `:16395`: «bisogna identificarlo» ha il genere nel clitico.
Si dice «identificare l'oggetto».

⭐⭐ LA SECONDA: `:16289` E' DENTRO UN COMMENTO DI BLOCCO, MA LA FIRMA E' VIVA.
`estrai --da-tradurre` registra la **prima** occorrenza, e la prima e' dentro il
tratto `/* ORIGINAL - BEGINNING … ENDING */` di `:16285`-`:16293`, che il mod ha
spento. La stessa firma pero' torna a `:16303`, dentro l'`ANNA CUSTOM` che l'ha
sostituito, e li' e' viva. ⚠️ **Rinviarla perche' la riga registrata e' morta
sarebbe stato un errore**, ed e' l'unico caso misto delle 69 di questo file
(`python scratchpad/_97-vive.py`: «69 da fare, 0 tutte morte»).

⭐ LA TERZA: `mtname()` NON E' ANCORA TRADOTTO, E LA RESA NON DEVE DIPENDERNE.
`item_data.hsp:1266` dichiara `sdim mtname, 18, 2, …` e i nomi dei materiali
stanno in `material_data.hsp`, che **non ha dizionario** (118 `lang()`, punto 17
della ripresa). Qualunque resa che chieda una preposizione — «è fatto **di**
mithril» / «**d'**acciaio» — mette un vincolo grammaticale su una parola che
oggi e' inglese e domani sara' italiana, e la sceglierebbe adesso alla cieca.
**«Il materiale è mithril.»** non chiede ne' preposizione ne' genere, e vale
comunque venga tradotto `mtname`. E' la stessa ragione per cui `item_func.hsp`
:2175 lo mette fra parentesi quadre invece che dentro una frase.

LESSICO EREDITATO (non deciso qui):
  - resistente agli acidi / al fuoco   `action.hsp:6628`, `:6652`, `blend.hsp:3417`
  - gelo (冷気)                        `glossario.md`, gli undici elementi
  - malattia dell'etere                `chara_func.hsp:2864` e sei altri siti
  - sala d'esposizione                 `action.hsp:11023`
  - merce rubata                       `action.hsp:1238`
  - oggetto prezioso                   `glossario.md`, 貴重品
  - Mira / Danno                       `command.hsp:12674`, la scheda
  - perfora (貫通)                     `item_func.hsp:2722`, la sigla dell'incantamento
  - DV, PV                             `glossario.md`, invariati
  - oro                                `glossario.md`, `Gold` -> `Oro`
  - «Vuoi davvero …?»                  `action.hsp:2995` e altri sei

PERIMETRO: 25 firme su 25. Nessuna esce da un ramo `if ( jp )` ne' da un
`if ( 0 )` (`python scratchpad/_97-vive.py`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io
import json
import sys

# chiave: (riga, inizio dell'inglese) — `:16365` porta DUE lang() sulla stessa riga
RESE = {
    # --- il prezzo stimato (BLOODYSHADE CUSTOM)
    (16054, 'You estimate this item would sell for'):
        '"Dovrebbe vendersi per " + item_info_value + " oro. (in tutto: " + item_value_total + ")"',

    # --- di che cosa e' fatto, e che cosa ne cresce
    (16289, 'It is made of'):
        '"Il materiale è " + mtname(0, inv(INV_ITEM_MATERIAL, ci)) + "."',
    (16300, 'It grows into'):
        '"Piantato, produce " + mtname(0, inv(INV_ITEM_MATERIAL, ci)) + "."',

    # --- le nove targhe di stato: mai un aggettivo accordato
    (16312, 'It speeds up the Ether Disease'): "Finché è addosso, fa avanzare la malattia dell'etere.",
    (16318, 'It is acidproof.'): 'È resistente agli acidi.',
    (16324, 'It is fireproof.'): 'È resistente al fuoco.',
    (16329, 'It is coldproof.'): 'È resistente al gelo.',
    (16334, 'It is precious.'): 'È un oggetto prezioso.',
    (16339, 'It is blessed by Ehekatl.'): 'Ha la benedizione di Ehekatl.',
    (16344, 'It is a stolen item.'): 'È merce rubata.',
    (16349, 'It is alive.'): 'Ha vita propria.',
    (16354, 'It can be only used in a show room.'): "Si può usare solo nella sala d'esposizione.",
    (16359, 'It is a hand-made item.'): 'È un oggetto fatto a mano con affetto.',

    # --- l'arma
    (16365, 'It can be wielded as a weapon.'): "Si può impugnare come un'arma.",
    (16365, ' Pierce '): ' perfora ',
    (16370, 'It is a light weapon.'): "È un'arma leggera.",
    (16375, 'It is a heavy weapon.'): "È un'arma pesante.",
    (16383, 'It modifies hit bonus by'):
        '"Modifica la mira di " + inv(INV_ITEM_ATTACK, ci) + " e il danno di " + inv(INV_ITEM_DAMAGE, ci) + "."',
    (16389, 'It modifies DV by'):
        '"Modifica DV di " + inv(INV_ITEM_DV, ci) + " e PV di " + inv(INV_ITEM_PV, ci) + "."',

    # --- quel che il pannello dice quando non sa, o quando sa tutto
    (16395, 'You have to identify the item to gain knowledge.'):
        "Per saperne di più bisogna identificare l'oggetto.",
    (16420, 'The enemy dies.'): 'Il nemico muore.',
    (16850, 'There is no information about this object.'):
        "Non c'è niente da sapere su questo oggetto.",
    (16867, 'Known Information'): "Conoscenza dell'oggetto",

    # --- il contorno: il bersaglio e la conferma
    (16970, 'You find no target.'): 'Non trovi nessun bersaglio.',
    (16987, 'Really attack'): '"Vuoi davvero attaccare " + name(tc) + "? "',
}

LOTTO = 'lavoro/97-command-conoscenza.jsonl'

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
