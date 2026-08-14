import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il corpo che si rimette in piedi, e lo scafo che si spacca.
    # ⚠️ genitivo: 「name の身体が…」 sarebbe «il corpo di X»
    (6168, '  quickly restored!'):
        'name(dmghp_charid) + " si ricompone in un lampo!"',
    # copiata da action.hsp:9265, stesso giapponese e stesso inglese
    (6182, ' returned to the original form.'):
        'name(dmghp_charid) + " ha ripreso l\'aspetto di prima."',
    # ⚠️ rete 13: lo stesso inglese per 中破 e 大破. Il ramo lo conferma:
    #    :6194 guarda HP > MAX/4, :6198 guarda HP <= MAX/4.
    (6196, '<Medium damaged>'):
        '<Danno medio>',
    (6200, '<Medium damaged>'):
        '<Danno grave>',
    # わらわ e' il «io» arcaico di una nobildonna: la nave parla di se'
    (6202, "My ship's hull has been torn apart again...!"):
        'Il mio scafo è di nuovo a pezzi...!',

    # --- chi si rigenera e chi viene guarito.
    (6212, '  healed.'):
        'name(dmghp_charid) + " si rigenera."',
    (6218, '  regenerated.'):
        'name(dmghp_charid) + " si rigenera."',
    # レイハンド e' l'imposizione delle mani: katakana che l'originale legge
    # come descrizione, quindi si rende (regola di invariati.md, lotto 023)
    (6258, ' shout, Lay on Hands!'):
        'name(cnt) + " grida, " + cnvtalk("Imposizione delle mani!")',
    # copiata da proc.hsp:8199, stesso giapponese
    (6260, '  healed.'):
        'name(dmghp_charid) + " si riprende."',
    (6271, '<Continue> '):
        '<Continua> ',

    # --- i tre gradini del dolore. ⚠️ l'inglese li mette in disordine:
    #     «scream» al primo e «severely hurt» al terzo. Sale il giapponese.
    (6351, ' scream.'):
        'name(dmghp_charid) + " incassa un colpo doloroso."',
    # stessa resa di action.hsp:8778
    (6358, ' writhe in pain.'):
        'name(dmghp_charid) + " si contorce dal dolore."',
    (6365, '  severely hurt!'):
        'name(dmghp_charid) + " lancia un urlo straziante!"',

    # --- l'equipaggiamento che si rovina. ⚠️ genitivo: 「name の itemname は…」.
    #     Il dativo riflessivo lascia il possesso implicito.
    (6399, '  is damaged.'):
        'name(dmghp_charid) + " si vede rovinare " + itemname(locvar_dmghp_ci, , 1) + " dal colpo."',
    (6411, '  is melted by acid.'):
        'name(dmghp_charid) + " si vede sbriciolare " + itemname(locvar_dmghp_ci, , 1) + "."',

    # --- il terrore, il sonno rotto, il parassita, il clic e la furia.
    (6441, ' is frozen in fear.'):
        '"Il terrore inchioda " + name(dmghp_charid) + " sul posto."',
    # ⚠️ genitivo: «il sonno di X»
    (6544, ' sleep  disturbed.'):
        'name(dmghp_charid) + " si sveglia di soprassalto."',
    # ⚠️ genitivo: «il parassita cerebrale di X»
    (6634, "'s brain parasite died from the damage."):
        'name(dmghp_charid) + " prende un colpo al cervello, e il parassita che ci vive muore."',
    (6665, '*click*'):
        '*clic*',
    # copiata da action.hsp:263 e proc.hsp:20851, stesso giapponese
    (6682, '  engulfed in fury!'):
        'name(dmghp_charid) + " freme di rabbia!"',
    # katakana preso a prestito anche in giapponese: l'italiano ha il suo
    (6750, '*Knockout*'):
        '*K.O.*',

    # --- LE VENTITRE MORTI. Per ognuna: la riga di log (dinamica, nomina chi
    #     muore) e il frammento di epigrafe (statico, che main.hsp:4409 incolla
    #     dopo il nome del morto).
    #     ⚠️⚠️ I frammenti vanno al PASSATO REMOTO: seguono il nome e ne sono il
    #     predicato, quindi un participio concorderebbe col personaggio. Il
    #     passato remoto italiano non ha genere.
    # ⚠️ «contro» non si fonde con l'articolo che cdatan porta dentro; «di» sì
    (6850, 'was killed by '):
        '"perse la vita contro " + cdatan(CDATAN_NAME, cc)',
    (6857, ' revealed the true appearance!!'):
        'name(dmghp_charid) + " si mostra nella sua vera forma!"',
    (6859, 'got assassinated by the unseen hand'):
        'sparì per una mano invisibile',
    (6863, '  assassinated by the unseen hand.'):
        '"Una mano invisibile porta via " + name(dmghp_charid) + "."',
    (6869, '  caught in a trap and die.'):
        'name(dmghp_charid) + " finisce in una trappola e muore."',
    (6871, 'got caught in a trap and died'):
        'morì in una trappola',
    (6875, ' shielded you and turned to ashes.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " ti fa scudo e si riduce in cenere."',
    (6877, 'crumbled to ashes'):
        'cadde in cenere',
    (6881, ' turned to ashes and collapsed.'):
        'name(dmghp_charid) + " si accascia e si riduce in cenere."',
    (6887, ' die from over-casting.'):
        '"Il contraccolpo del mana uccide " + name(dmghp_charid) + "."',
    (6889, 'was completely wiped by magic reaction'):
        'svanì nel contraccolpo del mana',
    (6893, '  starved to death.'):
        'name(dmghp_charid) + " muore di fame."',
    (6895, 'was starved to death'):
        'morì di fame',
    (6899, '  killed with poison.'):
        '"Il veleno consuma " + name(dmghp_charid) + " fino alla morte."',
    (6901, 'miserably died from poison'):
        'morì fra i tormenti del veleno',
    (6905, ' die from loss of blood.'):
        'name(dmghp_charid) + " perde tutto il sangue e muore."',
    (6907, 'died from loss of blood'):
        'perse tutto il sangue',
    (6911, ' dried up in the desert and die.'):
        'name(dmghp_charid) + " si prosciuga e muore."',
    (6913, 'dried up in the desert'):
        'si prosciugò nel deserto',
    # ⚠️ rete 13: «melt down» sta qui per il cioccolato bollente e a :6959 per
    #    l'acido. Il giapponese distingue, e il ramo pure (CHOCO / ACID).
    (6917, ' melt down.'):
        '"Il cioccolato bollente ustiona " + name(dmghp_charid) + " a morte."',
    (6919, 'melted down'):
        'morì nel cioccolato bollente',
    (6923, ' die from a curse.'):
        '"Una maledizione uccide " + name(dmghp_charid) + "."',
    (6925, 'died from a curse'):
        'morì per una maledizione',
    (6929, ' tumble down the stairs and die.'):
        'name(dmghp_charid) + " rotola giù per le scale e muore."',
    (6931, 'tumbled down the stairs and died'):
        'cadde dalle scale e morì',
    (6935, '  killed by an audience.'):
        '"Il pubblico uccide " + name(dmghp_charid) + "."',
    (6937, 'was killed by an audience'):
        'morì per mano del pubblico inferocito',
    (6941, '  burnt and turned into ash.'):
        'name(dmghp_charid) + " brucia fino a morire."',
    (6943, 'was burnt and turned into ash'):
        'bruciò fino a sparire',
    (6947, '  killed by food poisoning.'):
        '"Un\'intossicazione uccide " + name(dmghp_charid) + "."',
    (6949, 'got killed by food poisoning'):
        'morì per un\'intossicazione',
    # l'etere corrode: stessa immagine di proc.hsp:25789 e chara_func:2903
    (6953, ' die of Ether Disease.'):
        '"L\'etere corrode " + name(dmghp_charid) + " fino alla morte."',
    (6955, 'died of Ether Disease'):
        'morì della malattia dell\'etere',
    (6959, ' melt down.'):
        'name(dmghp_charid) + " si scioglie in una pozza di liquido."',
    (6961, 'melted down'):
        'si sciolse in una pozza di liquido',
    (6965, ' was consumed by the remnants of the elements and died..'):
        '"I residui degli elementi inghiottono " + name(dmghp_charid) + "."',
    (6967, 'consumed by the remnants of the elements'):
        'sparì fra i residui degli elementi',
    # copiata da action.hsp:3102, stesso inglese e stesso senso
    (6971, ' shatter.'):
        'name(dmghp_charid) + " va in pezzi."',
    (6973, 'committed suicide'):
        'si tolse la vita',
    (6977, '  turned into atoms.'):
        '"L\'esplosione atomica riduce " + name(dmghp_charid) + " in polvere."',
    (6979, 'was killed by an atomic bomb'):
        'morì in un\'esplosione atomica',
    (6983, ' step in an iron maiden and die.'):
        '"La vergine di ferro trafigge " + name(dmghp_charid) + "."',
    (6985, 'stepped in an iron maiden and died'):
        'morì nella vergine di ferro',
    # ⚠️ «stacca la testa a X» fonderebbe: «a il putit». Verbo transitivo
    (6989, '  guillotined and die.'):
        '"La ghigliottina decapita " + name(dmghp_charid) + "."',
    (6991, 'was guillotined'):
        'morì sotto la ghigliottina',
    (6995, ' was executed by result of fair vote.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " finisce al patibolo per voto regolare."',
    (6998, ' weakened and died.'):
        'cdatan(CDATAN_NAME, dmghp_charid) + " deperisce fino a spegnersi."',
}
