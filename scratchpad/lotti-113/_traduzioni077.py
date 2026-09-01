# -*- coding: utf-8 -*-
"""Le rese del lotto 077 — IL CIBO DA VIAGGIO: `FILTER_CARGO_FOOD` si chiude,
e con lei il CORPO di `db_item.hsp`.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 077 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa077.py`.

⚠️⚠️ Forma, da `_forma.py 077`: 1 su 1 con lo spazio prima del `\\n`, 1 su 1
con lo spazio dopo il `#`. Previsione di `applica`: **+1**, nessuna gemella.
ⓘ `_gia-reso 077`: 0 su 1.

⭐⭐ `_122-sorelle-per-frase 077`: **una sorella a 0.89, ed e' GIA' RESA** —
`:109023`, che e' la `description(3)` di **questo stesso oggetto**:

    qui  荷車に積み込むタイプの食糧      (indice 0, da rendere)
    la   荷車に積み込むタイプの食物だ    (indice 3, gia' reso)
    IT   «Un cibo del tipo che si carica sul carretto.»

La resa ricopia quella frase **parola per parola**, cosi' il pannello si apre
due volte con la stessa immagine, come fa il giapponese.
"""

IT = {
    # ⓘ 保存性が極めて高い -> «si conserva benissimo»: «si conserva a lungo»
    #   sta gia' nel dizionario su tre alimenti, e qui il giapponese ha 極めて.
    # ⓘ 質より量 e' il modo di dire, e l'italiano ce l'ha uguale e rovesciato:
    #   «quantita' piu' che qualita'».
    # ⓘ 凌駕する e' «superare, avere la meglio»: qui e' la quantita' che batte
    #   il sapore, ed e' la battuta della riga.
    109020: "Un cibo del tipo che si carica sul carretto. Si conserva benissimo, e nemmeno il sapore è male. Ma roba così è quantità più che qualità: in viaggio, spesso è quanto ne hai stipato a contare più di com'è buono. Nella dotazione c'è anche da bere, così anche la sete si placa un poco. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
}
