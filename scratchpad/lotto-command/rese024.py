import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15001 il bozzolo che schiude solo a febbraio.
    #     ⭐ parola per parola action.hsp:12728, stesso inglese.
    (15001, 'You have to wait until next February.'):
        'Bisogna aspettare il prossimo febbraio.',

    # --- :15007-:15027 il regalo di San Valentino rifiutato.
    #     Le prime due sono le due facce di un rnd(2) e devono restare diverse.
    #     ⭐ rete 3: 「いらん」 è già «Non mi va.» in action.hsp:9799.
    (15007, 'No way.'): 'Non se ne parla.',
    (15010, 'No way.'): 'Non mi va.',
    # 「盗んできたチョコレートなんて…」: l'inglese appiattisce, il giapponese dice
    # perché il regalo è rifiutato — è rubato (ITEM_BIT_STOLEN, :15026).
    (15027, 'No way.'): 'Cioccolatini rubati, poi...',

    # --- :15088 l'alleato già sazio (HUNGER >= 8000).
    #     ⚠️ «Sono pieno» accorderebbe col parlante: il nome al posto dell'aggettivo.
    (15088, "I'm full now!"): 'Adesso ho la pancia piena!',

    # --- :15101 e :15115 il bestiame che mangia. ⚠️ rete 4: stesso giapponese e
    #     stessa firma, quindi una resa sola. Tutt'e due i rami pretendono
    #     CHARA_BIT_LIVESTOCK, quindi «mangime» vale per l'uno e per l'altro.
    #     ⚠️ rete 8: «dare da mangiare a » + name si fonde. «Nutrire» regge
    #        l'oggetto diretto e la preposizione sparisce.
    (15101, 'You gave  food for livestock.'):
        '"Hai nutrito " + name(tc) + " con del mangime."',
    (15115, 'You gave  food.'):
        '"Hai nutrito " + name(tc) + " con del mangime."',

    # --- :15103 le cinque lagne sul mangime secco (パッサパサ).
    #     ⚠️ l'accordo cade sul mangime, mai su chi parla.
    (15103, 'This is hard!'): 'Che roba secca!',
    (15103, 'This dries your mouth!'): 'Mi si secca la bocca!',
    (15103, 'Ugh, this is so dry!'): 'Uff, ho la bocca tutta secca!',
    (15103, 'Ugh, this is hard!'): "Uff, ma quanto è secco!",
    (15103, 'Ugh, this is hard.'): 'Uff, che roba secca.',

    # --- :15108 il bestiame ingrassa.
    #     ⚠️ «è ingrassato» accorderebbe col soggetto: «mette su peso» non ha genere.
    (15108, ' grew fatter and now weighs kg.'):
        'name(tc) + " mette su peso: adesso pesa " + cdata(CDATA_WEIGHT, tc) + "kg."',

    # --- :15129-:15135 i due rifiuti del cibo.
    (15129, "I don't want it. I'm full."): 'No! Non ho più fame!',
    # 「ふかふかパン」: db_item.hsp:141763 fissa «pane soffice»
    (15135, "I-I don't want it! Get that puff puff bread away from me!!"):
        'N-no, non lo voglio! Basta con il pane soffice!!',

    # --- :15141 i quattro capricci del figlio appena nato.
    #     💡 «Nooooo!» si scrive identica all'inglese: va in invariati.md.
    (15141, 'Nooooo!'): 'Nooooo!',
    (15141, 'No!'): 'Nooo!',
    (15141, 'No! No!'): 'No e no!',
    (15141, 'No!!!!!!'): 'Nooo!!!!!!',

    # --- :15188 i quattro esiti della borraccia filtrante (:15169-:15186).
    #     ⚠️⚠️ l'inglese è l'array di :15196 copiato addosso: lo slot 2 è la
    #     borraccia vuota e lo slot 4 è l'alleato che beve e ringrazia. Si rende
    #     il GIAPPONESE. Vedi il docstring.
    (15188, 'Too heavy!'): 'Troppo pesante!',
    # 「からっぽ！」 = «vuota»: PARAM2 == 0. La borraccia filtrante è femminile
    # (db_item.hsp:135432).
    (15188, 'No way.'): "È vuota!",
    # ⚠️ rete 4: stesso 「いらん」 di :15196, una resa sola per tutt'e due.
    (15188, "I don't want it."): 'Non mi serve!',
    # ⭐ rete 3: 「ありがとう！」 è già «Grazie!» in text.hsp:1994. L'inglese dice
    #    «Never!», ed è lo slot sbagliato.
    (15188, 'Never!'): 'Grazie!',

    # --- :15196 i quattro rifiuti veri: troppo pesante, mobilio, cianfrusaglia,
    #     peso negativo.
    (15196, 'No way.'): 'Non posso!',
    (15196, "I don't need it."): 'Non mi serve!',
    (15196, 'Never!'): 'Mai!',

    # --- :15208-:15243 i rifiuti dell'oggetto da usare.
    (15208, "I don't want it. It's too creepy."):
        'Non lo voglio, non si sa nemmeno cosa sia!',
    # ⭐ stesso inglese di proc.hsp:11358, che è genderless per lo stesso motivo:
    #    l'oggetto maledetto può essere maschile o femminile.
    (15213, "It's cursed!"): 'Porta una maledizione!',
    (15230, 'Enough for me.'): 'Non riesco più a bere!',
    # 「おろす…」: l'alleata incinta a cui dai del veleno.
    (15243, 'Abortion...'): 'Meglio abortire...',

    # --- :15250-:15268 la consegna, l'anello di fidanzamento e la pozione d'amore.
    #     ⚠️ rete 8: «a » + name si fonde. Il ricevente va in testa, e la rete 11
    #        guarda l'insieme delle funzioni, non l'ordine (misura della 40a).
    (15250, 'You hand  to .'):
        'name(tc) + " riceve " + itemname(ci, 1) + "."',
    # ⭐ rete 3: parola per parola action.hsp:10757.
    (15253, ' blushes.'): 'name(tc) + " arrossisce."',
    # ⚠️ rete 11: il giapponese nomina l'oggetto con itemname, l'inglese no.
    #    La resa segue l'inglese e dice «il regalo», nome fisso e maschile.
    (15264, ' throws it on the ground angrily.'):
        'name(tc) + " va su tutte le furie e scaglia a terra il regalo."',
    # ⚠️ «pervertito» accorderebbe con chi ascolta, cioè col giocatore:
    #    l'accordo si sposta sull'atto.
    (15268, 'You scum!'): 'Sei il peggio!!',
    (15268, 'What are you trying to do!'): 'Che porcata!',
    (15268, 'Guards! Guards! Guards!'): 'Guardie! Guardie! Guardie!',
}
