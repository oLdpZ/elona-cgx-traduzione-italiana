# -*- coding: utf-8 -*-
"""Le rese del lotto dei DUE FABBRI LEGGENDARI (84a): Garok :2399-:2966 e
Miral :2967-:3124, un sistema solo.

Il lessico non e' stato deciso: e' stato letto dal dato.

    素材槌            material kit              kit di materiali   db_item:144134
    *素材変化*の巻物   scroll of superior mat.   pergamena di materiale superiore
                                                (nome «materiale superiore» +
                                                 parola-contatore «pergamena»)
    ブロンズ硬貨       bronze coin               moneta di bronzo   chat:2408
    小さなメダル       small medal               medaglietta        db_item:144256
    音楽用のディスク   music disc                disco musicale     text:2179
    荷車              cart / cargo              carretto           action:1906
    ジュークボックス   Juke box                  jukebox            db_item:139282
    ポーショマン       potioman                  potioman           action:12938

Il registro dei due si legge in `db_creature.hsp:118314` e `:118391`, dove le
loro battute italiane gia' li fanno sfottere a vicenda: Garok brusco, Miral
ciarliero. Officina di Miral e Garok, `text.hsp:2839`.

⚠️ La deroga: `:2747`. L'inglese di monte e' un COPIA-INCOLLA di `:2632` (con
«small medal» al posto di «bronze coin»), e non c'entra niente col posto dove
sta: quella riga e' il cartello sopra il menu dei materiali. Il giapponese dice
un'altra cosa, giusta. Si segue il giapponese — come Pael e Lily nella 82a — ma
`itemname(ci)` RESTA: nel ramo giapponese non c'e', e la prima stesura l'aveva
lasciato cadere; `verifica` l'ha respinta («interpolazioni non conservate»), e
ha ragione lei — quello che si toglie e' il testo sbagliato di monte, non il
dato che la riga porta. La resa e' quindi il senso giapponese col posto
dell'oggetto dentro: «Che materiale vuoi per » + itemname(ci) + «?».

💡 `:2632` tiene `itemname(ci)` e ci mette «di » davanti: si puo' perche'
`:2618` fissa `ci` sul KIT DI MATERIALI (se non lo trova, `:2625` manda via
prima di arrivarci), quindi l'articolo che esce e' sempre indeterminativo e
«di un kit di materiali» regge. Con un oggetto qualunque non si poteva:
`item_func.hsp:1976` mette l'articolo DETERMINATIVO sui capolavori, e «di la
Ragnarok» sarebbe sgrammaticato.

💡 Le voci di menu all'infinito sono la forma gia' decisa a `:11217`
(«Far evolvere il potioman») e `:2993` («Dare le monete di bronzo»).
"""
import io, json, sys

RESE = {
    # ---------------- GAROK, il fabbro brusco ----------------
    2401: 'Cambiare il materiale del kit di materiali',
    2402: 'Cambiare nome e aspetto a un oggetto',
    2403: 'Costruire un jukebox',
    2405: 'Non lo vedi che sono occupato? Se hai bisogno, sbrigati.',
    2626: 'Allora procurati un kit di materiali e una pergamena di materiale '
          'superiore. E anche una moneta di bronzo.',
    2632: '"Ah. Vuoi che usi la pergamena di materiale superiore per cambiare '
          'il materiale di " + itemname(ci) + "? Una moneta di bronzo per il '
          'disturbo."',
    2747: '"Con l\'umore di oggi passa questa roba. Che materiale vuoi per " '
          '+ itemname(ci) + "?"',
    2896: 'Ecco, è fatto. Su, portalo via.',
    2919: 'Ah sì? Allora procurami 76 dischi musicali. Doppioni compresi, fa lo stesso.',
    2925: 'Ehilà, li hai raccolti davvero. Cinque monete di bronzo per il disturbo: va bene?',
    2956: "Fatto. Guarda un po'.",

    # ---------------- MIRAL, il fabbro ciarliero ----------------
    2969: 'Scambiare le medagliette',
    2970: 'Migliorare il carretto',
    2971: 'Migliorare il potioman',
    2973: 'Oh oh, chi si vede, roba rara! Un viandante? Ti avrei offerto un '
          'banchetto, se non fosse che oggi la cena tocca a Garok. Sappi che '
          'cucina rozzo come lavora. Vabbè, sei venuto fin quaggiù: che posso '
          'fare per te?',
    2976: 'Oh oh oh! Hai delle medagliette! Fammi vedere, fammi vedere! Le vuoi '
          'scambiare con uno dei miei lavori migliori?',
    2988: '"Migliorare il carretto? Non è un lavoro che mi entusiasmi, ma se mi '
          'dai " + ccpc + " monete di bronzo, ci posso pensare."',
    3000: 'Bah.',
    3004: '"Il limite di peso del carretto è aumentato di " + '
          'cnvweight(calccargoupdate()) + "."',
    3013: 'Tieni.',
    3017: 'Quale potioman?',
    3024: 'Oh! Vuoi far migliorare questo potioman?',
    3033: 'E allora bastano due monete di bronzo! Ah, mi prudono le mani.',
    3040: "Va bene così com'è",
    3041: 'Voglio che dia una rotazione pazzesca',
    3042: 'Voglio aumentarne la potenza di base',
    3043: 'Voglio che spari due colpi insieme',
    3044: 'Voglio che sia più facile sparare a raffica',
    3045: 'Voglio che spari con precisione',
    3046: 'Voglio poterne cambiare la traiettoria',
    3047: 'E allora, che razza di potioman ne vuoi fare?',
    3118: 'Ecco fatto. Tieni... il tuo nuovo potioman!',
}

LOTTO = 'lavoro/84-chat-fabbri.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
mancanti = [v['riga'] for v in voci if v['riga'] not in RESE]
in_piu = [r for r in RESE if r not in {v['riga'] for v in voci}]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print('in piu\' : %s' % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[v['riga']]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
