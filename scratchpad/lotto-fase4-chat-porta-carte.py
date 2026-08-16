# -*- coding: utf-8 -*-
"""Lotto fase4-chat-porta-carte: **una voce sola**, la porta del negozio delle
carte, e apre `chat.hsp` nel perimetro.

⭐⭐ **E' la lezione della 52ª applicata prima del collaudo, non dopo.** Allora
il primo difetto del pannello dei ritocchi lo trovo' la **porta** e non la
schermata: il menu diceva «Regolazioni» mentre il pannello diceva «Ritocchi», e
chi cercava i ritocchi non trovava la porta. Qui la 54ª ha appena tradotto il
negozio delle carte per intero — 70 firme, 29 set, 141 nomi — e la voce di menu
che lo apre era rimasta **inglese**:

    chat.hsp:9206    chatList 12346, lang("カードを引き換えたい", "I want to redeem Cards.")
    chat.hsp:19379   la stessa riga, nell'altro elenco del negoziante

Due occorrenze, **una firma sola**: una voce di dizionario le copre tutt'e due.

⚠️ **La resa usa lo stesso verbo della stanza in cui porta.** Dentro, la
negoziante dice «Per riscattare i codici serve un mazzo» e «Ecco l'elenco dei
set che puoi riscattare» (`tcg_custom.hsp:1899` e `:1909`): la porta dice
«Vorrei riscattare delle carte». Se la porta dicesse «scambiare» e la stanza
«riscattare», il giocatore che cerca il negozio non lo riconoscerebbe.

⚠️ **Apre `chat.hsp`, che e' il file di testo piu' grande rimasto**: 4.373
firme, di cui questa e' **una**. Da adesso `verifica --dizionario` lo nomina e
dice quante ne restano, invece di tacere. E' lo stesso guadagno di
`db_card.hsp` oggi: un file fuori dal perimetro non e' un file finito, e' un
file che nessun conteggio guarda.
"""
import io
import json
import re
import unicodedata

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'
ESTRAZIONE = 'lavoro/_chat.jsonl'
USCITA = 'lavoro/fase4-chat-porta-carte.jsonl'

RESE = {
    (9206, 'I want to redeem Cards.'): 'Vorrei riscattare delle carte.',
}
RESE = {k: unicodedata.normalize('NFC', v) for k, v in RESE.items()}

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
tutte = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]
voci = [v for v in tutte if (v['riga'], v['en']) in RESE]

errori = []
if len(voci) != len(RESE):
    errori.append(f'rete 2: {len(RESE)} rese ma {len(voci)} voci agganciate')

# rete 6: la riga dev'essere viva.
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' spenta")

# rete 7: non dev'essere un confronto.
for v in voci:
    if re.search(r'[=!]=', sorgente[v['riga'] - 1].split('lang(')[0]):
        errori.append(f"rete 7: riga {v['riga']} e' un confronto")

# ⚠️ La rete che conta qui e' un'altra, e non e' automatica: la porta e la
# stanza devono usare la stessa parola. Si controlla che il verbo della resa
# compaia gia' nelle rese del negozio.
negozio = [json.loads(l)['it'] for l in io.open('dizionario/tcg_custom.hsp.jsonl',
                                                encoding='utf-8') if l.strip()]
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    if 'riscatt' in resa and not any('riscatt' in t for t in negozio):
        errori.append('rete «porta»: il negozio non usa il verbo della porta')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
        print(f":{v['riga']}  {v['en']!r} → {v['it']!r}")
print(f'{len(voci)} voce scritta in {USCITA}')
