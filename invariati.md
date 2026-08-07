# Invariati

Stringhe che restano identiche all'inglese **per scelta esplicita**, non perché
la traduzione è stata dimenticata. `verifica.py` legge questo file e non le
segnala.

Senza il file `verifica.py` si comporta come prima: è un'aggiunta, non un
requisito. Un progetto senza eccezioni è un progetto senza il file.

Il confronto è sulla **stringa intera** e sensibile alle maiuscole: una riga
qui copre `Vernis` come valore completo di `en`, non la parola `Vernis` dentro
una frase più lunga. Una frase che contiene un nome proprio si traduce
normalmente.

Una riga qui è una decisione: va motivata. Se il motivo non si riesce a
scrivere, probabilmente la stringa va tradotta.

| valore | motivo |
|---|---|
| Vernis | nome proprio di città, canone Elona |
| Palmia | nome proprio di città, canone Elona |
| Derphy | nome proprio di città, canone Elona |
| Noyel | nome proprio di città, canone Elona |
| Yowyn | nome proprio di città, canone Elona |
| Lumiest | nome proprio di città, canone Elona |
| Melugas | nome proprio di luogo, canone Elona |
| Karma | termine acquisito in italiano |
| Mana | termine acquisito nei giochi di ruolo |

## Da decidere nel glossario

Nomi propri presenti nel sorgente come valore intero, che appartengono al
canone Elona ma su cui la scelta lessicale non è ancora stata presa (Task 5).
Finché restano qui e non nella tabella sopra, `verifica.py` li segnala: è
voluto, così la decisione non passa inosservata.

| valore | occorrenze | nota |
|---|---|---|
| Larna | 3 | città |
| Port Kapul | 1 | città; `Port` potrebbe volere `Porto` |
| Cyber Dome | 1 | luogo Elona+ |
| Arcbelc | 3 | luogo Elona+ |
| Lesimas | 1 | il dungeon sotto Vernis |
