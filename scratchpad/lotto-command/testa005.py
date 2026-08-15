# -*- coding: utf-8 -*-
"""Lotto `command-005`: le 45 partenze di `*setHistory2`, la seconda riga del
«Background».

Segue il `command-004` e sta nella stessa schermata: dove la prima riga dice da
dove vieni, questa dice **perche' sei partito**. Stesso vincolo — il soggetto e'
il giocatore o un alleato (`chat.hsp:8588`) — e stesso registro nominale.

⭐ **Qui il giapponese e' al PRESENTE, e l'inglese lo mette al passato.**
Quarantadue voci su quarantacinque finiscono in 「〜旅に出る。」/「〜冒険に出る。」/
「〜冒険者になる。」, cioe' *si parte*, non *sei partito*; l'inglese scrive «You
left on adventure to…» per tutt'e quarantadue. Il nominale tiene il presente del
giapponese senza doverlo coniugare: «In viaggio per…», «All'avventura per…».

💡 **E le tre code giapponesi sono tre, non una**, quindi la resa le distingue
come le distingue il sorgente:
  - 「旅に出る」  -> «In viaggio per…»   (ventidue voci)
  - 「冒険に出る」 -> «All'avventura…»    (nove)
  - 「冒険者になる」 -> «Avventura, …»     (sei)
L'inglese le appiattisce tutt'e tre su «left on adventure»: e' un
appiattimento della specie che la 42a ha censito in `map.hsp`, e qui si
disfa gratis.

⚠️ **Due volte l'inglese dice piu' del giapponese, e vince il giapponese**
(la regola della 42a, «il giapponese e' l'arbitro sul contenuto»):
  - `:9672` 「寝ている間に船に積み込まれる。」 non nomina nessuna nave, e l'inglese
    ci mette **«the Queen Sedona»**;
  - `:9615` 「ロマンを求めて」 e' la **meraviglia**, il sogno d'avventura, e
    l'inglese lo legge come «romance», cioe' l'amore. Le due parole si scrivono
    uguali e vogliono dire cose diverse.

⚠️ `:9672` e `:9684` finiscono tutt'e due su una nave — uno addormentato, l'altro
morto — e stanno sulla **stessa riga** della schermata, quindi non si vedono mai
insieme; le rese restano comunque distinte («il risveglio in una stiva» contro
«il ritorno in se' su una nave») perche' due voci uguali su una lista tirata a
sorte si notano.

Tetto 61 caratteri (`:9627`), misurato con `scratchpad/misura-background.py`.
Zero copie da `dossier.py`, come nel lotto prima.
"""
