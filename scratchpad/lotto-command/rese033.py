import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # *com_wear — togliere un pezzo di equipaggiamento (:12791-:12804)
    # ================================================================
    # ⚠️ Impersonale, non participio: itemname(ci) puo' essere «la spada» o
    #    «il martello», e «non e' togliibile» dovrebbe accordarsi.
    (12791, " can't be taken off."):
        'itemname(ci) + " non si può togliere."',
    # ⚠️ Gli helper da togliere sono DUE: `is(cc)` e `his(cc)` a un argomento,
    #    tutt'e due in MORFOLOGIA_INGLESE. Resta `name`, e la rete 11 pretende
    #    esattamente quello.
    # ⭐ Terza persona perche' c'e' `name()`: init.hsp:1704 rende
    #    name(CHARA_PLAYER) come «il viandante», non come «tu».
    (12795, "  confused and can't change  equipment."):
        'name(cc) + " ha la mente annebbiata e non riesce a cambiare '
        'equipaggiamento."',
    # ⚠️ Seconda persona come l'inglese, e l'inglese qui sbaglia: *com_wear si
    #    apre anche su un alleato. Correggerlo vorrebbe `name(cc)`, cioe' una
    #    funzione che l'inglese non ha: e' la rete 11. Vedi il docstring.
    (12804, 'You unequip .'):
        '"Ti togli " + itemname(ci) + "."',

    # ================================================================
    # I gesti sulla mappa (:12890-:12999)
    # ================================================================
    # 芽 e' il germoglio, 枯れた草 l'erba secca: il giapponese distingue le due
    #    piante, e l'inglese pure («young» / «dead»).
    (12890, 'You nip a young plant.'): 'Cogli il germoglio.',
    (12895, 'You nip a dead plant.'): "Cogli l'erba secca.",
    # ⭐ Gia' deciso: text.hsp:14 e command.hsp:15708.
    (12929, 'Your inventory is full.'): 'Il tuo zaino è pieno.',

    # ================================================================
    # La demolizione di un edificio del mondo (:12952-:12969)
    # ================================================================
    (12952, 'You can not remove the building until relocation.'):
        'Questo edificio non si può demolire finché non viene trasferito.',
    # ⭐⭐ L'inglese butta via l'avviso, e quel che segue non e' reversibile
    #    (:12963 azzera l'area, :12964 licenzia i lavoranti, :12967 SALVA).
    #    E' una statica: nessun contratto, la resa segue il giapponese.
    #    Il registro viene da map.hsp:1297. Vedi il docstring.
    (12955, 'Really remove this building?'):
        'Vuoi davvero demolire questo edificio? (Attenzione: l\'edificio e '
        'tutto quello che contiene andranno perduti per sempre.)',
    (12969, 'You remove the building.'): "Demolisci l'edificio.",

    # ================================================================
    # La neve e il gesto a vuoto (:12982-:12999)
    # ================================================================
    (12982, 'You rake up a handful of snow.'):
        'Raccogli una manciata di neve.',
    # ⭐ Gia' deciso: proc.hsp:3467.
    (12985, 'You are too exhausted!'):
        'Troppa stanchezza: il tentativo fallisce!',
    # 「あなたは空気をつかんだ。」 — la mano si chiude sul niente.
    (12999, 'You grasp at the air.'): 'Stringi solo aria.',
}
