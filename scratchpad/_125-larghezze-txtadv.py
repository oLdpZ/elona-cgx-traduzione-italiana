# -*- coding: utf-8 -*-
"""125a - Le tre geometrie della schermata `txtadv`, misurate sul sorgente.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-larghezze-txtadv.py

⚠️⚠️ **PERCHE' SERVE.** La schermata dell'esplorazione e del casino' non e'
nessuno dei contenitori che il progetto misura: non e' la pergamena del dialogo
(`menu_dialogo`), non e' `*prompt_key` (`larghezze`), non e' un riquadro
(`riquadri`), non e' una linguetta (`linguette`). Ha una geometria sua, scritta
in `txtadv.hsp` e in `screen.hsp`, e fino alla 125a nessuno l'aveva letta:
centodiciassette rese sono entrate in gioco senza che niente le misurasse.

⚠️ **La finestra piu' stretta e' 800x600**, e non per convenzione:
`screen.hsp:2` la alza a 800 se e' piu' piccola, e `:23` ci torna quando la
risoluzione non e' valida. Tutti i conti qui sotto sono su 800.

## Le tre geometrie, e da dove viene ciascun numero

**1. Le righe di messaggio** — `txtadv.hsp:135`, `pos 170` con
`font …, 16 - en*2`, cioe' **font 14**. Corrono fino al bordo destro: 630 px.
⚠️ **Il passo di questo carattere NON e' misurato a schermo**, e non lo si
inventa: `larghezze.py` ha 7,7 px per il font 13 e `menu_dialogo.py` 7 px per il
font 12, ma la 118a ha gia' insegnato che prendere una costante da un'altra rete
dicendo «tanto e' lo stesso carattere» e' esattamente il difetto. Quindi qui il
metro **e' monte**: la riga inglese piu' lunga che il gioco disegna gia' oggi.
E' un metro conservativo e onesto, ed e' la stessa forma dei nomi di mappa
(124a): si misura il **peggioramento**, non uno zero inventato.

**2. Le voci di menu** — ⭐ **dalla 125a questa classe non vive piu' qui**: la
geometria e' entrata in `strumenti/menu_dialogo.py` come **quinto contenitore**
(`SCHERMATA_TXTADV`), perche' e' li' che il progetto misura le voci di menu e
perche' un test ci si appoggia — ed e' stato proprio quel test a cadere sulle
prime rese di questo file. Il conto qui sotto resta come controprova
indipendente. `:173`, `cs_list s, 170 + 30, …` con
`font …, 14 - en*2`, cioe' **font 12**, lo stesso della pergamena del dialogo.
Li' il passo e' **7 px** e non e' una supposizione: lo scrive il gioco,
`module.hsp:70`, `limit(strlen(…) * 7 + 32 + arg5, 10, 480)`.

⚠️⚠️ **Qui non c'e' un taglio: c'e' una SCIA.** Il rettangolo che il ciclo
ridisegna a ogni giro e' largo **400** e parte da 170 (`x = 170, 400`,
`:157`-`:161`), quindi ripulisce fino a **570**. La barra evidenziata parte da
200 e finisce a `200 + strlen*7 + 34`: perche' resti dentro il pulito serve

    strlen <= (570 - 200 - 34) / 7 = 48 caratteri

Quel che sfora **non viene ripulito al giro dopo** e resta a schermo.

⚠️⚠️⚠️ **E monte stesso puo' sforare, su una riga sola.** `:1256` e'
`"(Cheat) Slow time using " + itemname(…) + "!"`: la parte fissa e' 25
caratteri, ma `itemname()` porta il nome di un oggetto con l'incantamento del
tempo fermo, che oltre i 23 caratteri manda la barra oltre i 570. E' un difetto
di monte, non una regressione italiana — per questo la resa italiana di quella
riga e' stata accorciata **sotto** la parte fissa inglese invece che allungata.

**3. Il pannello in alto** — `screen.hsp:100`-`:108`, font 11.
`atxinfon(1..3)` partono da `sx = 220 + en*40 = 260`, e a destra si fermano dove
comincia il riquadro dell'immagine, `window2 windoww - 208` (`txtadv.hsp:38`),
cioe' 592. Restano **332 px**. Il passo lo dichiara il gioco stesso a `:100`,
dove posiziona la cornice del titolo a `sx + strlen(atxinfon(0)) * 13 / 2 + 14`:
**6,5 px per carattere**. Budget: **332 / 6,5 = 51 caratteri**.

⭐ **Il titolo `atxinfon(0)` non ha un tetto ma ha una cornice che si sposta**:
la parentesi destra la mette il gioco a `265 + strlen*6,5 + 14`, quindi cresce
col testo e non lo taglia mai. Entra nel referto per il margine, non come
cancello.

## Che cosa NON e' contato

Le chiamate `itemname()`, `matname()` e `skillname()` portano un nome che il
dizionario rende altrove e che questo lotto non decide. Le righe che ne hanno
una sono marcate **+nome**: il loro margine vero e' piu' stretto di quel che si
legge qui, e vale per l'inglese quanto per l'italiano.
"""
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

FILE = 'txtadv.hsp'

RE_NOTEADD = re.compile(r'^\s*(noteadd|txt)\s')
RE_CHATLIST = re.compile(r'^\s*chatList\s')
RE_INFON = re.compile(r'^\s*atxinfon\(')

# tre cifre per ogni pezzo interpolato: sono azioni, fiche e livelli
CIFRE = 3

# I tetti geometrici, dal docstring. `None` = il metro e' monte.
TETTI = {
    'messaggio': None,      # passo del font 14 non misurato: metro = monte
    'menu': (570 - 200 - 34) // 7,   # 48: la barra evidenziata deve finire
                                     # dentro il rettangolo ridisegnato (vedi sopra)
    'pannello': int(332 / 6.5),   # 51, (592 - 260) / 6,5 px (screen.hsp:100)
}

# La prova al contrario: tre stringhe che DEVONO accendere ciascuna classe.
# Non sono inventate a caso — sono la resa lunga scartata di `:1256` piu' due
# allungamenti plausibili delle righe piu' cariche di ciascuna classe.
PROVA = {
    'menu': '"(Trucco) Rallenta lo scorrere del tempo servendoti di questo "'
            ' + itemname(sandevistanci@txtadv) + "!"',
    'pannello': '"Livello di sospetto: " + ikasama'
                ' + "  Livello del premio: " + keihin + ""',
    'messaggio': 'Alle slot bisogna fermare i rulli al momento giusto per '
                 'far combaciare le figure e vincere il premio.',
}


def testo_reso(espressione, cifre=CIFRE):
    """(quanti caratteri a schermo, porta un nome dal dizionario)."""
    if not espressione.lstrip().startswith('"'):
        return len(espressione), False
    pezzi = re.findall(r'"((?:[^"\\]|\\.)*)"', espressione)
    fisso = ''.join(pezzi).replace('\\n', '')
    resto = re.sub(r'"(?:[^"\\]|\\.)*"', '', espressione)
    nome = bool(re.search(r'(itemname|matname|skillname|cnvitemname)\s*\(',
                          resto))
    numeri = len(re.findall(r'\+', resto)) - (2 if nome else 0)
    return len(fisso) + max(numeri, 0) * cifre, nome


def classe_di_riga(righe, numero):
    riga = righe[numero - 1]
    if RE_INFON.match(riga):
        return 'pannello'
    if RE_CHATLIST.match(riga):
        return 'menu'
    if RE_NOTEADD.match(riga):
        return 'messaggio'
    return 'altro'


def main():
    from strumenti import percorsi

    sorgente = (percorsi.SORGENTE_HSP / FILE).read_text(encoding='cp932')
    righe = sorgente.split('\n')

    percorso = os.path.join(RADICE, 'dizionario', FILE + '.jsonl')
    voci = [json.loads(r) for r in io.open(percorso, encoding='utf-8')]

    per_classe = {}
    for v in voci:
        classe = classe_di_riga(righe, v['riga'])
        if classe == 'altro':
            continue
        quanto_en, _ = testo_reso(v.get('en_grezzo') or ('"%s"' % v['en']))
        it = v.get('it') or ''
        quanto_it, nome = testo_reso(
            it if it.lstrip().startswith('"') else '"%s"' % it)
        per_classe.setdefault(classe, []).append(
            (quanto_it, quanto_en, nome, v['riga'], it))

    fuori = 0
    accese = 0
    for classe in ('messaggio', 'menu', 'pannello'):
        gruppo = per_classe.get(classe, [])
        if not gruppo:
            continue
        monte = max(x[1] for x in gruppo)
        tetto = TETTI[classe]
        metro = tetto if tetto is not None else monte
        etichetta = ('geometria %d' % tetto) if tetto else ('monte %d' % monte)
        print('=== %s: %d righe   metro: %s   (il piu\' lungo di monte: %d)'
              % (classe, len(gruppo), etichetta, monte))
        for q_it, q_en, nome, riga, it in sorted(gruppo, reverse=True)[:4]:
            segno = '✗' if q_it > metro else ' '
            print('  %s %3d (monte %3d)%s :%-5d %s'
                  % (segno, q_it, q_en, ' +nome' if nome else '      ',
                     riga, it[:64]))
        quante = len([x for x in gruppo if x[0] > metro])
        fuori += quante
        print('    --- oltre il metro: %d' % quante)

        prova, _ = testo_reso(PROVA[classe])
        if prova > metro:
            accese += 1
            print('    prova al contrario: %d > %d, si accende ✓\n' % (prova, metro))
        else:
            print('    ⚠️ PROVA AL CONTRARIO SPENTA: %d <= %d\n' % (prova, metro))

    if accese != 3:
        print('⚠️ la prova al contrario non si accende su tutte e tre le classi')
        return 2
    print('righe fuori misura: %d   (prova al contrario accesa su 3 classi su 3)'
          % fuori)
    return 1 if fuori else 0


if __name__ == '__main__':
    raise SystemExit(main())
