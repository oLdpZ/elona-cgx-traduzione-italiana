# -*- coding: utf-8 -*-
"""I sessanta nomi di mappa che sforavano il tetto della barra in basso.

`screen.hsp:153` taglia `mdatan(MDATAN_NAME)` con `strmid` a **16 caratteri**,
**12** se la mappa mostra il numero di piano. Il taglio e' netto, a meta'
parola, e si legge in ogni schermata del gioco: la 62a lo ha trovato col
collaudo del pannello degli dei, dove la barra diceva «La Terra della T».

Il tetto non si alza: il passo e' 7 px, il nome comincia a `inf_raderw + 24` e
la prima piastrella di stato sta a `inf_raderw + 148`, cioe' 124 px = 17
caratteri. Vedi [[nomi_mappa.py]], che e' il referto.

⚠️ **Non si toccano i nomi che sfora anche l'inglese di monte.** Su 197 nomi
l'inglese ne taglia 46 e noi 104: la differenza — **60** — e' l'unica che sia
lavoro nostro. Sulle nefia generate, che sono le mappe piu' visitate del gioco,
upstream ne taglia 51 su 80 («Beginner's Cave» diventa «Beginner's C»): li' il
taglio e' una condizione del gioco, non un difetto della traduzione.

⚠️ **Le voci si trovano per (file, riga del sorgente)**, non per contenuto: lo
stesso italiano puo' stare anche in una riga che non e' un nome di mappa, e
cambiarla la' sarebbe un danno silenzioso. Il perimetro lo decide il referto.

⚠️ Si compone tutto in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nomi_mappa as N

# vecchio nome -> nuovo. Il vecchio fa anche da guardia: se il dizionario non
# lo dice piu', lo script si ferma invece di sovrascrivere qualcos'altro.
NUOVI = {
    # --- text.hsp, i posti fissi -----------------------------------------
    'Antico Campo di Battaglia degli Dei': 'Campo degli Dei',
    'Grotta Eremitica di Lustor': 'Grotta di Lustor',
    'Nave del Raccolto Stellare': 'Nave Messe',          # tetto 12
    'Bacino della Nave Divina': 'Bacino navale',
    'Allevamento abbandonato': 'Ranch in rovina',
    'il cimitero di Lumiest': 'Cimitero Lumiest',
    "l'Ambasciata di Palmia": 'Ambasciata',
    'Villa delle Domestiche': 'Villa Domestiche',
    'la Terra della Tregua': 'Terra di Tregua',
    'Gabbia Oscura di Amur': 'Gabbia di Amur',
    'Nave Magica Eulderna': 'Nave di Eulderna',
    'Dimora della Strega': 'Dimora Strega',
    'Il tuo sotterraneo': 'Sotterraneo',
    'Cupola Cibernetica': 'Cibercupola',
    'Arena delle Bestie': 'Colosseo',                    # コロシアム, alla lettera
    'Campo di prigionia': 'Campo prigionia',
    'Torre del Miraggio': 'Torre Miraggio',
    'Santuario del Caos': 'Tempio Caos',                 # tetto 12
    'Cupola delle Case': 'Casa modello',
    'Rovine di Remido': 'Remido',                        # tetto 12
    # --- map.hsp, i nomi assegnati dritti --------------------------------
    'Nave divina dormiente - ponte alto': 'Ponte superiore',
    'Castello del Drago a Nove Teste': 'Rocca del Drago',
    'Presso le rovine di Suginoko': 'Presso Suginoko',
    'Nuovo laboratorio biologico': 'Nuovo sito prova',
    'Sigillo Eterno <ricomposto>': 'Sigillo Eterno',
    'Sigillo Eterno <in rovina>': 'Sigillo Eterno',
    'Palazzo Infero - ingresso': 'Palazzo Infero 1',
    'Palazzo Infero - livello 2': 'Palazzo Infero 2',
    'Palazzo Infero - livello 3': 'Palazzo Infero 3',
    'Palazzo Infero - livello 4': 'Palazzo Infero 4',
    'Palazzo Infero - livello 5': 'Palazzo Infero 5',
    'Palazzo Infero - livello 6': 'Palazzo Infero 6',
    'Presso il palazzo reale': 'Presso la reggia',
    'Villa dei gatti di Tam': 'Villa dei gatti',
    'Grande palude di Merca': 'Palude di Merca',
    'Laboratorio biologico': 'Sito di prova',
    'Acque di Capo Diavolo': 'Acque del Capo',
    'Castello di Ghiaccio': 'Rocca Ghiacciata',
    'Presidio di Eulderna': 'Base di Eulderna',
    'Gilda dei Guerrieri': 'Gilda Guerrieri',
    'Miniera degli slime': 'Miniera di slime',
    'Salone del piano 15': 'Salone piano 15',
    'Salone del piano 20': 'Salone piano 20',
    'Salone del piano 25': 'Salone piano 25',
    'Salone del piano 30': 'Salone piano 30',
    'Campo di battaglia': 'Campo battaglia',
    'Collina dei funghi': 'Monte dei funghi',
    'Sala dei concerti': 'Sala concerti',
    'Bisca clandestina': 'Bisca',
}


def perimetro():
    """{ (file, riga del sorgente): (vecchio, tetto) } per i nomi da accorciare."""
    tipi = N.tipi_delle_aree(N.SORGENTE)
    sorgente = N.raccogli(N.SORGENTE)
    build = N.raccogli(N.BUILD)
    fuori = {}
    for k, (n_build, it, area) in build.items():
        if k not in sorgente:
            continue
        n_sorg, en, _ = sorgente[k]
        t = N.tetto_di(area, tipi)
        if en and len(en) <= t < len(it):
            fuori[(k[0], n_sorg)] = (it, t)
    return fuori


def main():
    da_fare = perimetro()
    print(f'il referto nomina {len(da_fare)} nomi da accorciare')

    # 1. il tavolo delle rese nuove regge il tetto?
    guai = []
    for vecchio, nuovo in NUOVI.items():
        tetti = [t for (it, t) in da_fare.values() if it == vecchio]
        if not tetti:
            guai.append(f'«{vecchio}» non sta fra i nomi da accorciare')
            continue
        t = min(tetti)
        if len(nuovo) > t:
            guai.append(f'«{nuovo}» e\' {len(nuovo)}, il tetto e\' {t}')
    mancanti = {it for (it, t) in da_fare.values()} - set(NUOVI)
    for m in sorted(mancanti):
        guai.append(f'«{m}» non ha una resa nuova')
    if guai:
        for g in guai:
            print('  ⚠️', g)
        raise SystemExit('il tavolo non e\' a posto: non tocco niente')

    # 2. si compone in memoria, un file per volta
    #
    # ⚠️ Le voci del dizionario sono **una per contenuto**, non una per sito:
    #    `estrai` accorpa le righe identiche e `applica` stende la resa su tutti
    #    i siti uguali. I sei piani del Palazzo Infero stanno in map.hsp in tre
    #    posti ciascuno, ma nel dizionario hanno una riga sola. La guardia
    #    giusta e' quindi «ogni NOME del perimetro e' stato cambiato», non
    #    «ogni SITO ha una riga».
    scritture = {}
    fatte = 0
    cambiati = set()
    for nomefile in sorted({f for (f, n) in da_fare}):
        percorso = f'dizionario/{nomefile}.jsonl'
        righe = io.open(percorso, encoding='utf-8').read().split('\n')
        nuove = []
        for riga in righe:
            if not riga.strip():
                nuove.append(riga)
                continue
            d = json.loads(riga)
            chiave = (nomefile, d.get('riga'))
            if chiave in da_fare and d.get('it') == da_fare[chiave][0]:
                cambiati.add(d['it'])
                d['it'] = NUOVI[d['it']]
                fatte += 1
                nuove.append(json.dumps(d, ensure_ascii=False))
                continue
            nuove.append(riga)
        scritture[percorso] = '\n'.join(nuove)

    attesi = {it for (it, t) in da_fare.values()}
    if cambiati != attesi:
        for m in sorted(attesi - cambiati):
            print(f'  ⚠️ «{m}» non e\' stato agganciato in nessuna voce')
        raise SystemExit('perimetro non coperto: non scrivo')

    for percorso, testo in scritture.items():
        io.open(percorso, 'w', encoding='utf-8', newline='\n').write(testo)
        print(f'  scritto {percorso}')
    print(f'{fatte} nomi accorciati')


if __name__ == '__main__':
    main()
