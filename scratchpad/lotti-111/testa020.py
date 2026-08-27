# -*- coding: utf-8 -*-
"""111a - Lotto 020 di `db_item.hsp`: il rapporto degli ANELLI.

`FILTER_ACCESSORY_RING`, `description(3)`: **11 righe del sorgente, 11 firme**,
11 giapponesi distinti. La gemella della categoria degli amuleti (lotto 018), e
due righe sono **la stessa riga** con 指輪 al posto di 首輪.

### ⭐⭐ `:99165` E' `:99451` CON UN'ALTRA PAROLA

    :99451  上げた人との友好度が上がる首輪。返ってくることはない。  (amuleto)
    :99165  上げた人との友好度が上がる指輪。返ってくることはない。  (anello)

Stessa resa, cambiato il genere: **«Dato a qualcuno, alza la simpatia. Non
torna indietro.»**, che a sua volta viene da 「人に渡すと友好度が上がるアイテム
だ」 -> «Dato a qualcuno, alza la simpatia.», gia' nel dizionario. Una riga
scritta tre volte nel sorgente, e una sola volta da noi.

### ⭐ DUE RITROVAMENTI

- 運勢 e' **«fortuna»**, e la riga esiste gia': 「運勢が上昇する食物だ」 ->
  «Un cibo che alza la fortuna». Quindi `:107184` e' «Un anello che alza la
  fortuna».
- **PV** resta **PV**: e' la sigla che il giocatore legge nella scheda del
  personaggio, spiegata in `chat.hsp` («il DV, che ti fa schivare, e il PV»).
  `:107393` e' «Un anello dal PV altissimo».

### ⚠️ 指輪 «anello» CONTRO 輪 «cerchio»

`:99236` non dice 指輪, dice 指にはめる**輪**だ — un *cerchio* da infilare al
dito, cioe' la definizione della parola, non la parola. Si rende «Un cerchio da
infilare al dito», se no la descrizione dell'anello dice «anello».
Stessa cosa per `:99308`, 指にはめる加工品 «un pezzo lavorato».

ⓘ Il dono divino `:75584` e' il **quinto** della famiglia 身に着けると変形して:
l'elenco completo sta nella testa del lotto 024.
"""
