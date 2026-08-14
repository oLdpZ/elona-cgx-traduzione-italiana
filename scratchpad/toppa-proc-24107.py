# -*- coding: utf-8 -*-
"""La toppa di `proc.hsp:24107` e il rinvio che la accompagna.

L'azione `SKILL_SPACT_JYUSOU_GOUSHIN` e' `TARGET_TYPE_SELF_ONLY`
(`skill.hsp:1411`) e `proc.hsp:7565` fa `tc = cc`: chi lancia e chi subisce sono
lo stesso personaggio. Il giapponese lo dice, l'inglese di monte no — e' la riga
dell'incantesimo Maledizione (`proc.hsp:14703`) ricopiata parola per parola, e
nomina **due** personaggi. Nessuna resa italiana puo' conservare due `name()`
senza stampare due volte lo stesso nome, quindi la riga non si aggiusta dal
dizionario: si toppa, riportando il ramo inglese alla forma del giapponese.

⚠️ Le toppe **non passano da `degrada()`** (`applica.py` le applica alla lettera):
la sostituzione non porta accenti, e la resa e' costruita per non averne bisogno
(«si scaglia addosso», non «su se stesso», che avrebbe anche fatto concordare
l'aggettivo col genere).

⚠️ **E scrive solo dopo aver validato il testo intero.** La prima versione
apriva `toppe.jsonl` in scrittura e falliva dentro `write()` per un surrogato
nel motivo: il file era gia' stato **troncato a zero byte**, e a salvarlo e'
stato solo `git checkout`. Adesso il testo si compone, si codifica in memoria e
solo allora si apre il file.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())

from strumenti import percorsi  # noqa: E402

CERCA = ('\t\ttxt lang(name(cc) + "は自分自身に強烈な呪いをかけた！", '
         'name(cc) + " point" + _s(cc) + " " + name(tc) + " and mutter" + _s(cc) + " a curse.")')
SOSTITUISCI = ('\t\ttxt lang(name(cc) + "は自分自身に強烈な呪いをかけた！", '
               'name(cc) + " si scaglia addosso una maledizione tremenda!")')

MOTIVO = (
    "proc.hsp:24107. **Non e' una resa mancante: e' una riga che il dizionario non "
    "puo' aggiustare**, ed e' la seconda della famiglia dopo :11481 della 36a. "
    "L'azione e' `SKILL_SPACT_JYUSOU_GOUSHIN`, che `skill.hsp:1411` dichiara "
    "`TARGET_TYPE_SELF_ONLY`: `proc.hsp:7565` fa `tc = cc`, quindi chi lancia e chi "
    "subisce sono **lo stesso personaggio**. Il giapponese lo dice — "
    "「自分自身に強烈な呪いをかけた！」 — e `skill.hsp:1413` lo conferma nella "
    "descrizione dell'abilita', 「Si maledice e si rafforza」. ⚠️ L'inglese di monte "
    "invece nomina **due** personaggi: e' `proc.hsp:14703` (l'incantesimo Maledizione, "
    "dove i due sono davvero due) **ricopiata parola per parola**, e a schermo stampa "
    "lo stesso nome due volte. 💡 La rete 11 e `verifica.py:367` pretendono che le "
    "funzioni di contenuto della resa coincidano con quelle dell'inglese, e nessuna "
    "frase italiana nomina due volte lo stesso personaggio senza sembrare rotta: e' "
    "il rovescio di :18280 della 38a, dove l'inglese aveva **un** `name()` e il "
    "giapponese due. La strada e' la toppa, che riporta il ramo inglese alla forma "
    "del giapponese — un nome solo. Fatta nella 39a insieme al rinvio."
)


def riscrivi(percorso, righe_nuove) -> int:
    """Compone, valida e solo allora scrive: un errore non deve troncare il file."""
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    testo = '\n'.join(righe) + '\n'
    dati = testo.encode('utf-8')          # ⚠️ prima si valida, poi si apre
    with io.open(percorso, 'wb') as f:
        f.write(dati)
    return len(righe)


sorgente = io.open(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp',
                   encoding='cp932').read()
if sorgente.count(CERCA) != 1:
    sys.exit(f'la riga cercata compare {sorgente.count(CERCA)} volte nel sorgente, non una')
SOSTITUISCI.encode('cp932')  # la toppa non passa da degrada(): dev'essere scrivibile

toppe = percorsi.PROGETTO / 'toppe.jsonl'
if any(json.loads(r).get('cerca') == CERCA
       for r in io.open(toppe, encoding='utf-8').read().splitlines() if r.strip()):
    sys.exit('toppa gia\' presente')
quante = riscrivi(toppe, [json.dumps({'file': 'proc.hsp', 'cerca': CERCA,
                                      'sostituisci': SOSTITUISCI, 'motivo': MOTIVO},
                                     ensure_ascii=False)])
print(f'toppe.jsonl: {quante} toppe')

voce = None
for l in io.open('lavoro/_proc.jsonl', encoding='utf-8'):
    if l.strip() and json.loads(l)['riga'] == 24107:
        voce = json.loads(l)
if voce is None:
    sys.exit('voce 24107 non trovata nell\'estrazione')

rinviate = percorsi.PROGETTO / 'rinviate.jsonl'
if any(json.loads(r).get('firma') == voce['firma']
       for r in io.open(rinviate, encoding='utf-8').read().splitlines() if r.strip()):
    sys.exit('rinvio gia\' presente')
quante = riscrivi(rinviate, [json.dumps(
    {'firma': voce['firma'], 'file': 'proc.hsp', 'en': voce['en_grezzo'],
     'rinviata_a': 'nessuna fase: risolta da toppa (proc.hsp:24107, 39a)',
     'motivo': MOTIVO}, ensure_ascii=False)])
print(f'rinviate.jsonl: {quante} rinvii')
