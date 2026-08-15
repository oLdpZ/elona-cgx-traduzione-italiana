import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Le tre della fame (:14741) — scritte sulla forma delle tre della sete
    # ================================================================
    (14741, 'You are too full to eat.'):
        'Non riesci a mangiare altro.',
    # ⚠️ 「腹がさける」 e' la pancia che si spacca, come 「膀胱がやぶける」 e' la vescica.
    (14741, 'You are too bloated to eat any more.'):
        'La pancia sta per scoppiarti...',
    # 💡 Stesso inglese di :14799 su un giapponese diverso (腹 contro 喉): upstream
    #    ha copiato la riga della fame dentro il ramo della sete. La rete 13 lo
    #    dira'.
    (14741, "Your stomach can't digest any more."):
        'Non hai ancora fame.',

    # ================================================================
    # Equipaggiare (:14752-:14778)
    # ================================================================
    # ⚠️ «pesante» e' invariabile, «equipaggiato» no: il genere dell'oggetto non
    #    si conosce a scrittura. Stessa forma di action.hsp:63.
    (14752, "It's too heavy to equip."):
        'È troppo pesante da equipaggiare.',
    # ⭐ Stesso giapponese di :12795, ricopiata parola per parola.
    # ⚠️ `is(cc)` e' morfologia e sparisce: resta il solo `name`.
    (14758, "  confused and can't change their equipment."):
        'name(cc) + " ha la mente annebbiata e non riesce a cambiare equipaggiamento."',
    # ⭐ «equipaggiare» e' il verbo di questo stesso schermo: :13924 chiede «Che
    #    cosa vuoi equipaggiare?» e :17020 dice «Devi equipaggiare frecce».
    #    Il gemello :12804 fa «Ti togli " + itemname(ci) + "."».
    (14769, 'You equip .'):
        '"Equipaggi " + itemname(ci) + "."',

    # ⚠️ Le tre righe del ramo maledetto / votato alla rovina / benedetto: le
    #    vede chiunque equipaggi, e il sesso di chi gioca non si conosce. Nessun
    #    participio riferito al giocatore.
    # ⭐ chara_func.hsp:2714 dice gia' «sente un brivido di freddo» per 寒気.
    (14772, 'You suddenly feel a chill and shudder.'):
        "D'improvviso ti prende un brivido di freddo.",
    # 💡 Il giapponese conta il cammino, l'inglese conta i passi: la resa tiene
    #    tutt'e due. 「破滅」 e' «rovina» in skill.hsp:1576 («Canto di rovina»).
    (14775, 'You are now one step closer to doom.'):
        'Hai mosso un passo sulla via della rovina.',
    # ⚠️ 見守る e' vegliare, non spiare: e' il ramo BENEDETTO.
    (14778, 'You feel as someone is watching you intently.'):
        'Hai la sensazione che qualcosa vegli su di te.',

    # ================================================================
    # Le tre della sete (:14799) — stesso giapponese di action.hsp:8274,
    # ricopiate parola per parola tutt'e tre.
    # ================================================================
    (14799, 'Your are too full to drink.'):
        'Non riesci a bere altro.',
    (14799, 'You are too bloated to drink any more.'):
        'La vescica sta per scoppiarti...',
    (14799, "Your stomach can't digest any more."):
        'Non hai ancora sete.',

    # ================================================================
    # Il marchio d'immagine (:14828)
    # ================================================================
    # ⭐ 「アイテム画像」 e' «icona» in :6068, :6073 e :6076, e questa resa e' il
    #    gemello speculare di :6825, «name(tc) + " ha perso l\'icona."».
    (14828, 'You attached an item mark to .'):
        'name(tc) + " ha ricevuto un\'icona."',
}
