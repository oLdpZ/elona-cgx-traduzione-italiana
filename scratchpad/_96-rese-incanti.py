# -*- coding: utf-8 -*-
"""96a - `item_func.hsp`: le sigle degli incantamenti nel pannello dell'equipaggiamento.

53 firme fra `:2667` e `:2750`, dentro `equipinfo_mmah` (`:2505`), il ramo
`showresist == 4`. Sono le etichette compatte che il giocatore vede **in fila su
una riga sola**, accanto a ogni pezzo indossato, premendo `z` fino alla pagina
«Special Enchantment».

⭐⭐⭐ LA COSA CHE DECIDE IL LOTTO: QUESTE CINQUANTATRE SIGLE SONO
L'ABBREVIAZIONE DI UNA LISTA CHE E' GIA' TRADOTTA. `item_data.hsp:613`-`:709`
porta le **stesse** enchant in forma distesa, rese fra la 60a e la 70a, e il
giocatore legge le due cose sullo stesso oggetto a due tasti di distanza. Il
lessico quindi non si sceglie qui: si **abbrevia** quello.

    :674  早撃ちを可能にする         «Permette il tiro rapido.»       -> TiroRapido
    :677  完全貫通攻撃発動の…        «un attacco che perfora sempre»  -> Perfora
    :691  攻撃された時、相手に切り傷…   «Infligge danni da taglio a…»    -> RendeTaglio
    :651  魔物を呼び寄せる          «Attira i mostri.»               -> AttiraMostri

⚠️⚠️⚠️ E COSI' SI VEDE CHE L'INGLESE QUI SBAGLIA, NON ABBREVIA — TRE VOLTE, E
UNA E' UN CONTROSENSO:

1. **`:2732` `ShotReflect` non riflette niente.** La costante e'
   `ENCHANT_QUICK_SHOOTING`, il giapponese e' 早撃 («tiro veloce») e la forma
   distesa `item_data.hsp:674` dice «Permette il tiro rapido». Tre testimoni
   contro uno: l'inglese ha scritto «riflette i colpi» dove il gioco dice «spara
   prima». -> **TiroRapido**.
2. **`:2690` `EXP-Absorb` non assorbe.** Costante `ENCHANT_DISTURB_GROWTH`,
   giapponese 成長を妨げる, distesa `:650` «Ostacola la crescita». L'inglese fa
   sembrare un vantaggio (assorbi esperienza) quel che e' un **malus**.
   -> **FrenaCrescita**.
3. **`:2743` `Reveal Religion` non rivela niente** — e qui a sbagliare e' anche
   la sigla giapponese. 信仰を明らか vuol dire «rende manifesta la fede», ma la
   costante e' `ENCHANT_PRESERVE_PIETY` e la distesa `:697` dice «Impedisce il
   calo naturale della Pieta'». La sigla di monte e' scollegata dal suo stesso
   effetto in tutt'e due le lingue: si segue la costante e la distesa.
   -> **MantieneFede**.

💡 E' la lezione della 95a in un'altra forma: quando due testimoni litigano, il
terzo e' il **nome della costante**, che nessuno traduce e nessuno sbaglia.

⭐⭐ LA SECONDA: IL TETTO NON E' PER ETICHETTA, E' PER RIGA — E STA SCRITTO NEL
SORGENTE. `command.hsp:12740` chiama `equipinfo_mmah p(1), wx + 260, …` e
`item_func.hsp:2751`-`:2753` scrive le sigle **una in fila all'altra**
(`locvar_equipinfo_x += strlen(s) * 8`). A destra, `command.hsp:12749` disegna
il peso a `wx + 640`. Quindi il budget e' **380 px, cioe' 47 caratteri per tutte
le enchant di un oggetto messe insieme**, non per una.

E' il motivo per cui l'inglese scrive `SpellPow+` e non `Enhances your spells`:
sono sigle **per progetto**, e l'italiano deve stare nello stesso registro.

⚠️ **E qui il conto va detto per intero, perche' il primo giro di questo modulo
diceva una cosa falsa.** C'era scritto «nessuna riga italiana e' piu' larga
della corrispondente inglese»: il controllo in coda al modulo, scritto dopo,
dice che **19 sigle su 53 sono piu' larghe della loro inglese**, da +1 a +4
caratteri. Quel che e' vero e' un'altra cosa, piu' debole: nessuna italiana
supera la **piu' lunga** inglese del sito (`Poison/Nerver-Comine`, 20), e la
piu' lunga italiana e' 13 (`SucchiaSangue`, `FrenaCrescita`, `Anti-nonmorti`,
`ManaInAttacco`).

⭐ **E il tetto lo sfonda gia' l'inglese.** 47 caratteri per riga; la sigla
inglese media di questo sito e' 11 caratteri, piu' `:N` fa 13: **quattro**
enchant riempiono la riga gia' in inglese (52 > 47), e il `repeat 15` di
`:2656` ne ammette molte di piu'. Il traboccamento non lo introduce l'italiano,
c'era; l'italiano lo anticipa di frazioni. Percio' le sigle si tengono corte per
disciplina, non per stare sotto una soglia che nessuno rispetta.

⚠️ Nessuna rete misura questo sito — ne' la larghezza della riga ne' la
crescita rispetto all'inglese. Le due misure qui sopra le fa **il modulo
stesso**, in coda, e restano una guardia da scrivere
(vedi `RIPRESA-sessione.md`).

⚠️ NIENTE ACCENTI IN QUESTO LOTTO, ED E' UNA SCELTA. `applica.py` degrada
«a'» in due caratteri: in un campo dove ogni carattere sono 8 px in fila,
«Pieta'» ne costa sette invece di sei. Dove l'accento serviva — «Ridà MP»,
«Pietà» — la resa gira sulla parola senza accento («CuraMP», «MantieneFede»).

⚠️ DEROGA — `:2667` E' MEZZA SIGLA. La riga compone
`capitalize(skillname(elemento)) + lang("ダメ", "Dmg") + ":" + n`, cioe'
l'elemento lo scrive `skillname()` (gia' tradotto) e la `lang()` e' solo il
pezzo «danno»: a schermo esce «FuocoDann:4». Non si puo' riordinare, perche' la
`lang()` non contiene l'elemento.

LESSICO EREDITATO (da `item_data.hsp`, non deciso qui):
  - tiro rapido, perfora, critico, mischia, soffio, sassi, carica
  - levitazione (`command.hsp:2185`), riflette magia (`buff.hsp:461`)
  - Vento d'etere, maltempo, alieni, mutazioni, ladri
  - fuoco/gelo, mentali/sonori, veleno/neurali, oscurita'/oltretomba

PERIMETRO: 53 firme su 53 nel ramo `showresist == 4`. Le sigle a un kanji di
`:2474` — 筋 耐 器 感 … — **non sono in questo lotto e non sono lavoro**: il
loro `mes` e' commentato (`:2485`-`:2491`, il pannello disegna icone al posto
loro) e stanno gia' tutte in `rinviate.jsonl`.

⚠️ Accenti veri se ce ne fossero; niente virgolette tipografiche, niente
caratteri a due byte.
"""
import io, json, sys

RESE = {
    # --- il danno elementale: mezza sigla, l'elemento lo scrive skillname()
    2667: 'Dann',

    # --- quel che l'oggetto ti fa addosso (i malus)
    2674: 'TeleCasuale',
    2678: 'BloccaTele',
    2682: 'SucchiaSangue',
    2686: 'SucchiaMP',
    2690: 'FrenaCrescita',
    2694: 'AttiraMostri',

    # --- quel che ti restituisce
    2697: 'CuraMP',
    2698: 'CuraSP',

    # --- quel che ti lascia fare
    2700: 'Levita',
    2701: 'MangiaMarcio',
    2702: 'Viaggi+',
    2703: 'VedeInvisib',

    # --- le protezioni
    2704: 'ResMalediz',
    2705: 'ResLadri',
    2706: 'ResEtere',
    2707: 'ResMaltempo',
    2708: 'ResAlieni',
    2709: 'ResMutazioni',

    # --- le potenze
    2711: 'Magia+',
    2712: 'Soffio+',
    2713: 'Sassi+',
    2714: 'Carica+',

    # --- i quattro doppi incantesimi
    2716: 'Fuoco/Gelo',
    2717: 'Mente/Suono',
    2718: 'Veleno/Nervi',
    2719: 'Oscur/Oltret',

    # --- come colpisce
    2721: 'ColpoLontano',
    2722: 'Perfora',
    2723: 'Critico',
    2724: 'Mischia+',
    2725: 'Tiro+',
    2726: 'TiroConcat',
    2727: 'Appoggio',
    2728: 'FermaTempo',

    # --- come incassa e come rende
    2730: 'RendeTaglio',
    2731: 'RiflMagia',
    2732: 'TiroRapido',
    2733: 'MenoCritici',
    2734: 'ResFisico',
    2735: 'AnnullaDanni',

    # --- contro chi
    2737: 'Anti-draghi',
    2738: 'Anti-nonmorti',
    2739: 'Anti-volanti',
    2740: 'Anti-dei',
    2741: 'Anti-metalli',

    # --- gli dei, il tempo, la musica
    2743: 'MantieneFede',
    2744: 'SegnaliDei',
    2746: 'PortaLaFine',
    2747: 'ManaInAttacco',
    2748: 'Ricompense+',
    2749: 'PortaIlTempo',
    2750: 'Inebria',
}

LOTTO = 'lavoro/96-item_func-incanti.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
mancanti = [v['riga'] for v in voci if v['riga'] not in RESE]
in_piu = [r for r in RESE if r not in {v['riga'] for v in voci}]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

# il tetto misurato: la sigla inglese piu' lunga del sito
piu_lunga_en = max(voci, key=lambda v: len(v['en']))
piu_lunga_it = max(RESE.values(), key=len)
print('sigla inglese piu\' lunga: %r (%d)' % (piu_lunga_en['en'], len(piu_lunga_en['en'])))
print('sigla italiana piu\' lunga: %r (%d)' % (piu_lunga_it, len(piu_lunga_it)))
oltre = [(v['riga'], RESE[v['riga']], v['en']) for v in voci
         if len(RESE[v['riga']]) > len(v['en'])]
if oltre:
    print('⚠️ piu\' larghe dell\'inglese, da guardare a mano: %d' % len(oltre))
    for r, it, en in oltre:
        print('   %6d  %-16s (%2d)  contro  %-22s (%2d)' % (r, it, len(it), en, len(en)))

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[v['riga']]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
