# -*- coding: utf-8 -*-
"""113a - Lotto 027 di `db_item.hsp`: IL MOBILIO, prima parte.

`FILTER_FURNITURE`, righe 55.600-80.200, indici 0 e 2: **42 righe su 41
oggetti**. Il fronte intero e' di 251 righe sull'indice 0 piu' 10 sull'indice 2
— la categoria piu' grossa del corpo — e questo e' il primo taglio.

⚠️ L'indice 1 qui non c'e': in tutta la categoria e' vuoto.

### ⭐ DIECI TITOLI-FONTE, e il mobilio ne porta molti piu' del cibo

Il cibo stava su otto code, e trentotto righe su cinquanta erano lo stesso
libro. Qui i libri sono **sedici** in quarantadue righe, e i due che pesano
sono `~Catalogo d'Arte di Lumiest~` (10) e `~Grande Enciclopedia dei Mobili di
Tyris del Nord~` (14). ⚠️ Quest'ultimo l'inglese lo scrive in **tre** forme
diverse — con e senza lo spazio dopo il `#`, con e senza lo spazio dopo la
tilde — e la tabella le riconduce a una.

### ⚠️⚠️ DIECI TITOLI DELLA TABELLA AVEVANO L'APOSTROFO AL POSTO DELL'ACCENTO

`~Scoperta! Le Rarita' del Mondo~`, `~Parole di un Avventuriero che si e'
Risvegliato~` e altri otto: la forma **degradata**, che nel dizionario e' un
errore che `verifica.py` segnala. La degradazione la fa `applica.py`, e la
fonte di verita' porta l'accento vero.

💡 Non se n'era accorto nessuno perche' il cibo non usava nessuno di quei dieci:
il primo lotto che ne tocca due e' questo. ⓘ La lunghezza non cambia — `à`
degrada in `a'`, due caratteri come prima — quindi il cancello dei 66 resta a
55 con margine 11, identico.

### ⭐⭐ L'INGLESE SBAGLIA SEI VOLTE, E SEI VOLTE SI SEGUE IL GIAPPONESE

1. **`:72884`, il koma-inu 吽形.** L'inglese scrive «with its mouth **open**»,
   copiato dal gemello `:72822`: il giapponese dice 口を**閉じた**, chiusa. E'
   la coppia che sta ai due lati del cancello, e l'inglese ne fa due uguali —
   perfino la frase «sometimes called a lion», che il giapponese ha solo sul
   primo. ⚠️ Un difetto che nessuna rete puo' vedere: gli inglesi sono quasi
   identici, e la differenza sta in due kanji.
2. **`:65331`, il cuscino-pecora.** L'inglese ha **perso una frase intera** —
   「広大な草原で、心地よい風に吹かれながら寝ている羊になった夢」, il sogno di
   essere una pecora che dorme in una prateria sconfinata — e attacca diretto
   con «However, on rare occasions». Senza quella frase il «pero'» non regge su
   niente, e la riga non vuol dire piu' nulla.
3. **`:78789`, il piatto grande.** «They range from the most expensive to the
   most expensive»: e' ピンからキリまで, *dal meglio al peggio*.
4. **`:66575`, il Budda.** «Sacred trees such as sacred trees» per 御神木などの
   神聖な木.
5. **`:66703`, la cuccia.** «constructed to prevent **ventilation**»: e'
   隙間風, gli **spifferi**.
6. **`:57707`, il busto di Itzpalt, e `:57769`, il dipinto di Ehekatl.**
   Tutt'e due perdono la prima proposizione — il lato di 猛る炎の魔神 nel primo,
   e nel secondo il pittore che *assiste* alla scena, che l'inglese riduce a
   un'apposizione senza verbo.

### ⭐ I TERMINI CERCATI A MANO

    魔導船      -> nave magica            (`db_item.hsp`, gia' nel dizionario)
    クリスマスツリー -> albero di Natale
    狛犬        -> koma-inu               (invariato, e il nome dell'oggetto)
    地蔵        -> zizou                  (la statua austera, decisa nella 109a)
    癒しの女神    -> la dea della cura      (癒しのジュア «Jure della Cura»)
    聖夜祭      -> la festa
    <Gould's Piano> -> <Pianoforte di Gould>

⚠️ **`:68913`, il flauto dolce, perde un gioco di parole e non si puo' fare
altrimenti.** 「記録するもの、の名を持つ縦笛」: il flauto che porta il nome di
*chi registra*, perche' in inglese `recorder` e' tutt'e due. In italiano si
chiama flauto dolce, e il rimando si tiene dicendo che quel nome ce l'ha **in
un'altra lingua** — che e' vero, e non spiega la battuta.
"""
