# -*- coding: utf-8 -*-
"""97a - Per ogni file col dizionario: quanto delle «non tradotte» sia lavoro vero.

⚠️ `verifica --dizionario` conta le firme del **sorgente** che non stanno fra le
rese, e **le rinviate ci stanno dentro**. Da quando i file si chiudono
(`chat.hsp` nella 95a, `item_func.hsp` nella 96a, `command.hsp` e `system.hsp`
nella 97a) quel numero non dice piu' «quanto manca»: dice «quanto manca **piu'**
quanto e' gia' stato deciso di non fare».

Il conto giusto e' la differenza, e finora si e' **scritto a mano nella
ripresa**, un file per sessione: la 95a «il 6 di `chat.hsp` vuol dire zero», la
96a «il 37 di `item_func.hsp` vuol dire zero». Una frase per file, ricopiata di
sessione in sessione, che nessuno rimisurava.

⚠️ **Al primo giro questo modulo dava zero su tutta la riga**, e lo zero era
falso: leggeva le voci **senza `it`** dentro `dizionario/*.jsonl`, e li' dentro
non ce ne sono — `reimporta` scrive solo le rese. Le firme da fare non stanno in
un file, si ricavano **dal sorgente**, ed e' quel che fa `verifica.py`. Uno zero
che arriva subito e su ogni riga non e' una buona notizia: e' una domanda posta
al posto sbagliato.

    python scratchpad/_97-quanto-resta.py
"""
import io
import json

from strumenti import percorsi
from strumenti.verifica import confronta_col_sorgente
from strumenti.estrai import estrai_da_testo

rinviate = set()
for l in io.open('rinviate.jsonl', encoding='utf-8'):
    if l.strip():
        rinviate.add(json.loads(l)['firma'])

righe = []
tot_dafare = tot_rinv = 0
for percorso in sorted(percorsi.DIZIONARIO.glob('*.jsonl')):
    nome = percorso.stem
    _, non_tradotte = confronta_col_sorgente(nome)
    if non_tradotte == 0:
        continue
    sorgente = percorsi.SORGENTE_HSP / nome
    tradotte = {json.loads(r)['firma']
                for r in percorso.read_text(encoding='utf-8').splitlines()
                if r.strip() and json.loads(r).get('it')}
    nel_sorgente = {v['firma'] for v in
                    estrai_da_testo(nome, sorgente.read_bytes().decode('cp932'))}
    aperte = nel_sorgente - tradotte
    rinv = len(aperte & rinviate)
    dafare = len(aperte) - rinv
    tot_dafare += dafare
    tot_rinv += rinv
    righe.append((dafare, nome, len(aperte), rinv))

righe.sort(reverse=True)
print(f'{"file":<24} {"non tradotte":>12} {"rinviate":>9} {"DA FARE":>8}')
for dafare, nome, aperte, rinv in righe:
    marca = '   ⭐ CHIUSO' if dafare == 0 else ''
    print(f'{nome:<24} {aperte:>12} {rinv:>9} {dafare:>8}{marca}')
print(f'\n{"TOTALE":<24} {tot_dafare + tot_rinv:>12} {tot_rinv:>9} {tot_dafare:>8}')
print('\n⚠️ Solo i file che HANNO un dizionario: quelli senza non compaiono '
      '(nove, punto 17 della ripresa).')
