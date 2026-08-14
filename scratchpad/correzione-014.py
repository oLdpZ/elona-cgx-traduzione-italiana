# -*- coding: utf-8 -*-
"""Le due divergenze vecchie trovate cercando i precedenti del lotto 014.

Nessuna delle due nasce in questo lotto: sono decisioni prese due volte in due
file diversi, che nessuna guardia confronta fra loro. ⚠️ `--divergenti` non le
vede: misurato nella 29a, `rese_gia_decise()` apre `db_creature.hsp` e basta.

### 1. «Nothing happens...» in due modi, e uno dei due e' un macro

`text.hsp:1` non e' una riga qualunque: e'

    #define global txt_nothinghappens txt lang("何もおきない… ", "Nothing happens...")

cioe' la resa che esce **dappertutto**, ogni volta che un oggetto non fa niente.
`action.hsp:8936` scrive lo stesso identico giapponese e lo stesso identico
inglese come `lang()` a mano, ed era reso «Non succede **nulla**...». Vince il
macro, perche' e' quello che il giocatore legge cento volte contro una.

### 2. Si trovava una «monetina» e nello zaino c'era una «medaglietta»

`db_item.hsp:144256` chiama 「小さなメダル」 **«medaglietta»**, ed e' il nome che
l'oggetto porta nell'inventario, nei negozi e nelle liste. `action.hsp:6254` — il
messaggio che esce quando la si trova — diceva «Trovi una **monetina**!».

⚠️ **E l'errore viene dall'inglese di monte**, che nel messaggio scrive `small
coin` e nel nome dell'oggetto `small medal`: chi ha reso il messaggio ha tradotto
l'inglese che aveva davanti, senza sapere che l'oggetto aveva gia' un nome. E' il
`Bolt` della 35a in miniatura — una decisione presa una volta e mai applicata
altrove — con l'aggravante che qui a sviare e' la lingua di mezzo.

💡 La stessa trappola tocca `proc.hsp:12022` di questo lotto, che ha lo stesso
inglese (`You find a small coin!`) e un giapponese diverso (感知した invece di
見つけた): reso «Trovi una medaglietta!» d'accordo con `db_item.hsp`.

### 3. 「首をちょんぎった」 al passato in un file e al presente nell'altro

L'ha trovata la **rete 3** del lotto, scrivendo `proc.hsp:12287`.
`action.hsp:18755` e' il *kaishaku* — il seguace che decapita il giocatore dopo
il seppuku — e diceva «`name(cnt) + " ha decapitato " + ...`». Non e' una scena
diversa: e' una riga di **log di combattimento**, sorella di quella che il lotto
014 scrive per l'azione speciale Decapitazione, con lo stesso identico
giapponese.

⚠️ E il log di `proc.hsp` e' tutto al **presente** — «morde», «assale»,
«scaglia», «ferma il tempo», «piomba giu'» — quindi a muoversi e' la vecchia.
Mettere il presente qui non cambia la scena: la mette in fila con le altre
duecento righe che il giocatore legge nello stesso riquadro.

Lo script e' ripetibile: una voce gia' corretta si salta.
"""
import io
import json

# file -> {(riga, en): (vecchia attesa, nuova)}
CORREZIONI = {
    'dizionario/action.hsp.jsonl': {
        (8936, 'Nothing happens...'):
            ('Non succede nulla...', 'Non succede niente...'),
        (6254, 'You find a small coin!'):
            ('Trovi una monetina!', 'Trovi una medaglietta!'),
        (18755, ' cut  head.'):
            ('name(cnt) + " ha decapitato " + name(CHARA_PLAYER) + "."',
             'name(cnt) + " decapita " + name(CHARA_PLAYER) + "."'),
    },
}

# rete 1: il bersaglio a cui ci si allinea deve esistere davvero, se no si sta
# copiando una resa immaginaria. E' la rete 1 di correzione-bolt.py.
BERSAGLI = [
    ('dizionario/text.hsp.jsonl', 1, 'Non succede niente...'),
    ('dizionario/db_item.hsp.jsonl', 144256, 'medaglietta'),
]
for percorso, riga, atteso in BERSAGLI:
    trovato = None
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d['riga'] == riga and d.get('it'):
            trovato = d['it']
            break
    if trovato is None or atteso not in trovato:
        raise SystemExit(f'rete 1: {percorso}:{riga} non dice {atteso!r} ma {trovato!r}')

fatte, saltate = 0, 0
for percorso, correzioni in CORREZIONI.items():
    righe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    viste = set()
    for d in righe:
        k = (d['riga'], d.get('en'))
        if k not in correzioni:
            continue
        vecchia, nuova = correzioni[k]
        viste.add(k)
        if d.get('it') == nuova:
            saltate += 1
            continue
        # rete 2: si corregge solo quello che dice ancora la resa vecchia
        if d.get('it') != vecchia:
            raise SystemExit(f'rete 2: {percorso}{k} non dice {vecchia!r} '
                             f"ne' e' gia' corretta, ma {d.get('it')!r}")
        print(f"{percorso.split('/')[-1]}:{d['riga']}  {d['it']!r} -> {nuova!r}")
        d['it'] = nuova
        fatte += 1
    # rete 3: nessuna correzione deve restare senza voce
    if viste != set(correzioni):
        raise SystemExit(f'rete 3: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    with io.open(percorso, 'w', encoding='utf-8', newline='\n') as f:
        for d in righe:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

print(f'--- {fatte} rese corrette, {saltate} gia\' a posto')
