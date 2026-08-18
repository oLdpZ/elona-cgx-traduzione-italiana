import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1025-:1108 l'allevamento: disinfezione, codici, funzione di riordino.
    (1025, 'You need a disinfectant.'): 'Non hai il disinfettante.',
    # ⚠️ Il giapponese non nomina nessuno («ho disinfettato i locali»), l'inglese
    #    nomina due cose: la rete 11 pretende le funzioni dell'inglese.
    (1036, ' sprinkled .'):
        'name(CHARA_PLAYER) + " disinfetta i locali con " + itemname(ci, 1) + "."',
    (1073, 'Breeding will be prevented in this area.'):
        'In questo allevamento non ci saranno nascite.',
    (1082, 'Production will be prevented in this area.'):
        'In questo allevamento non ci sarà produzione.',
    (1091, 'Breeding is no longer prevented in this area.'):
        'Le nascite tornano regolari.',
    (1100, 'Production is no longer prevented in this area.'):
        'La produzione torna regolare.',
    (1108, 'This is a function to collect all the dropped items at your feet.'):
        'È la funzione che raccoglie ai tuoi piedi tutti gli oggetti a terra.',

    # --- :1150-:1253 il campo di prigionia.
    (1150, 'You cannot contain more than 30 in this camp.'):
        'Qui puoi rinchiuderne al massimo 30.',
    # ⚠️ Stesso giapponese di :937 («放せない», lasciar libero) ma inglese
    #    diverso: li' si libera all'allevamento, qui si rinchiude nel campo.
    #    E' l'inglese che sa di piu', e si segue lui.
    (1164, 'You can not contain escort target in this camp.'):
        'Non puoi rinchiudere chi devi scortare.',
    (1173, ' stay at this camp.'):
        '"Hai rinchiuso " + cdatan(CDATAN_NAME, c) + "."',
    # 💡 Stesso giapponese di command.hsp:7098.
    (1177, ' changed to original cloth.'):
        'cdatan(CDATAN_NAME, c) + " riprende l\'aspetto di prima."',
    (1250, "You don't have enough Toil-Energy..."):
        'Non hai abbastanza Energia da Lavoro...',
    # 💡 Stesso giapponese di map.hsp:9914 e text.hsp:3.
    (1253, 'Something is put on the ground.'): 'Qualcosa viene posato per terra.',

    # --- :1376-:1487 il negozio: premi, ingrandimento, tipo, addestramento.
    # 💡 «chip da casino'» viene da text.hsp:2197.
    (1376, 'You get 10 Casino chips.'): 'Hai ricevuto 10 chip da casinò.',
    (1385, "You don't have enough money..."): 'Non hai abbastanza soldi...',
    (1392, 'You extend your shop! You can display a total of  items now!'):
        '"Hai ingrandito il negozio! Adesso puoi esporre " + mdata(MDATA_MAX_INV)'
        ' + " oggetti!"',
    (1400, 'This Shop will be changeable again at .'):
        '"Il prossimo cambio sarà possibile il "'
        ' + cnvdate(adata(ADATA_SHOP_TYPE_CHANGE_COOLDOWN, gdata(GDATA_AREA)), 1) + "."',
    (1437, 'Shop type changed: .'): '"Tipo di negozio cambiato: " + shops + "."',
    # ⚠️ `his(sc)` a un argomento e' morfologia e se ne va. «accresce il
    #    potenziale» viene da ai.hsp:1893, la stessa cosa fatta al trainer.
    (1455, ' calls a trainer and develops  potential!'):
        'cdatan(CDATAN_NAME, sc) + " chiama un allenatore e accresce il potenziale!"',
    (1459, "You don't have enough bronze coins..."):
        'Non hai abbastanza monete di bronzo...',
    # 💡 «vendite» e' il contatore di :407, «[Vendite: N]».
    (1469, '120 sales exp is needed...'): 'Servono almeno 120 vendite...',
    (1476, '360 sales exp is needed...'): 'Servono almeno 360 vendite...',
    (1482, " can't earn any more feats."):
        'cdatan(CDATAN_NAME, sc) + " non può ottenerne altri."',
    (1487, ' has earned enough sales exp to learn a new feat! Which is...'):
        'cdatan(CDATAN_NAME, sc) + " ha venduto abbastanza da prendere un talento! Ed è..."',
    # ⚠️ Qui l'inglese sbaglia la reazione. `shopval == 0` vuol dire che il
    #    giocatore ha annullato il menu: il giapponese fa fare al negoziante una
    #    ずっこけ, la caduta comica della delusione, e l'inglese scrive «smiled».
    #    Decide il sito: dopo un annullamento un sorriso non vuol dire niente.
    (1510, ' smiled.'): 'cdatan(CDATAN_NAME, sc) + " ci resta male."',
    (1531, ' already has that feat.'):
        'cdatan(CDATAN_NAME, sc) + " ha già quel talento."',
    (1542, ' got a new feat.'):
        'cdatan(CDATAN_NAME, sc) + " ha preso un talento nuovo."',

    # --- :1599-:1669 le porte, le piastrelle, l'aspetto esterno.
    (1599, 'You changed door to Japan type.'):
        'Adesso le porte sono in stile giapponese.',
    (1603, 'You changed door to normal type.'): 'Adesso le porte sono normali.',
    (1607, 'You changed door to SF type.'): 'Adesso le porte sono meccaniche.',
    # 💡 片開き e' la porta a un battente solo; l'inglese scrive «EW type», che
    #    non dice niente a nessuno.
    (1611, 'You changed door to EW type.'):
        'Adesso le porte hanno un battente solo.',
    (1614, 'You have to enter the map again to apply the changes.'):
        'Per applicare del tutto le modifiche bisogna rientrare nella mappa.',
    # 💡 map0..map3 sono nomi di file, non parole: restano.
    (1637, 'You changed tile group to map0.'):
        'Gruppo di piastrelle cambiato in map0.',
    (1641, 'You changed tile group to map1.'):
        'Gruppo di piastrelle cambiato in map1.',
    (1645, 'You changed tile group to map2.'):
        'Gruppo di piastrelle cambiato in map2.',
    (1649, 'You changed tile group to map3.'):
        'Gruppo di piastrelle cambiato in map3.',
    (1661, 'Input the number of map_ . (1-33) / If input 0, undo.'):
        "Che numero ha l'immagine? (da 1 a 33; con 0 si torna a quella di prima.)",
    (1669, 'You put back the original graphic.'):
        "Hai rimesso l'aspetto di prima.",

    # --- :1792-:1980 gli ospiti, i domestici, il banco vuoto.
    (1792, 'You already have too many guests in your home.'):
        'La casa è già piena di gente.',
    (1877, 'Who do you want to hire?'): 'Chi vuoi assumere?',
    (1892, 'You hire .'): '"Hai accolto in casa " + cdatan(CDATAN_NAME, tc) + "."',
    (1980, "[Shop] Your shop doesn't have a shopkeeper."):
        '[Negozio] Il negozio non ha nessuno al banco.',

    # --- :2182-:2417 il rendiconto del negozio.
    # 💡 Stesso giapponese di action.hsp:1207 e main.hsp:6912.
    (2182, 'You gain  fame.'):
        '"Hai guadagnato " + bookfame + " punti fama."',
    (2300, "[Shop] customers visited your shop but  couldn't sell any item."):
        '"[Negozio]" + customer + " clienti sono passati, ma "'
        ' + cdatan(CDATAN_NAME, worker) + " non ha venduto niente."',
    # ⚠️ :2308 e :2310 sono i pezzi con cui `s` si compone a :2308-:2311, e
    #    finiscono dentro :2315: lo spazio in testa e' quel che li attacca al
    #    numero che li precede.
    (2308, ' gold pieces'): " monete d'oro",
    (2310, ' and  items'): '" e " + income(1) + " oggetti"',
    (2315, '[Shop] customers visited your shop and  sold  items.  put  in the'
           ' shop strong box. You got  YacaPoints.'):
        '"[Negozio]" + customer + " clienti sono passati e "'
        ' + cdatan(CDATAN_NAME, worker) + " ha venduto " + sold + " oggetti. "'
        ' + cdatan(CDATAN_NAME, worker) + " ha messo " + s + " nella cassaforte."'
        ' + " Hai guadagnato " + yaca + " YacaPoint."',
    (2417, '[Shop] imported and sold some goods for the shop, earning  gold and'
           ' put them in the shop strong box. You got  yaca points.'):
        '"[Negozio]" + cdatan(CDATAN_NAME, worker) + " ha comprato e rivenduto'
        ' merce per conto suo, guadagnando " + dokuzi + " monete d\'oro, e le ha'
        ' messe nella cassaforte. Hai guadagnato " + yaca + " YacaPoint."',

    # --- :2594-:2775 i rendiconti di rango, che escono a fine mese.
    (2594, 'Museum Rank:-> Your museum is now known as <>.'):
        '"Rango del museo: " + cnvrank(rankorg / 100) + " -> "'
        ' + cnvrank(rankcur / 100) + " Adesso il tuo museo è <" + ranktitle(3) + ">."',
    (2692, 'Unique Level:-> '):
        '"Livello unico: " + rankorg + " -> " + gdata(STARTING_GDATA_FLAG + 365) + " "',
    (2693, '/ Next stage: '): '"/ Prossima tappa: " + nokori + " "',
    (2775, 'Furniture Value: Heirloom Value: Home Rank:-> Your home is now known as <>.'):
        '"Arredi: " + gdata(GDATA_HOME_FURNITURE) / 100 + " Cimeli: "'
        ' + gdata(GDATA_HOME_VALUE) / 100 + " Rango della casa: "'
        ' + cnvrank(rankorg / 100) + " -> " + cnvrank(rankcur / 100)'
        ' + " Adesso la tua casa è <" + ranktitle(4) + ">."',
}
