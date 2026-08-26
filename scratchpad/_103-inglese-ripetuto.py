# -*- coding: utf-8 -*-
"""103a - Le carte di `db_card.hsp` a cui monte ha dato l'inglese di un'altra.

Nata da `:4125`, lotto 9: il giapponese e' la **mandragora zappatrice** che
picchia le cosce con una bardana, l'inglese e' il **cavallo di cetriolo** di
`:4112` — anzi, e' la resa *piu' completa* del giapponese di `:4112`, con in
piu' la frase sul sudore che l'inglese di `:4112` non ha. Monte ha tradotto due
volte la stessa carta e ha scritto la seconda nel blocco sbagliato.

⚠️ **Un lotto da solo non lo vede.** La rete 13 dei lotti confronta gli inglesi
**dentro la zona**, e qui le due carte cadevano nella stessa zona per caso: se
`:4112` fosse stato nel lotto 8 la coppia sarebbe passata liscia. Questa guarda
tutte le 1.146 voci del file in un colpo.

⚠️ Non tutti gli inglesi ripetuti sono difetti: le carte che di mestiere
ripetono la stessa formula (le cameriere demoniache del lotto 8, i tre unimorti
del lotto 7) hanno l'inglese uguale *perche' ce l'hanno uguale in giapponese*.
Il segnale e' l'inglese uguale con il **giapponese diverso**: quello e' un
referto da leggere a mano, non una guardia a zero.

⭐ **Misurata sulle 1.146 voci del file: TRE coppie, e nessun falso positivo.**

    :4112 / :4125   il cavallo di cetriolo -> la mandragora zappatrice
    :6959 / :6972   il passero in stormo   -> il mostro spaghetto di un altro astro
    :9637 / :9624   la coccinella antica   -> l'ente che sorveglia Nefia

Solo la seconda ha l'inglese **identico**; le altre due monte le ha riscritte
con altre parole, e un confronto per stringa le lascia passare. Per questo la
rete gira due volte: prima sull'uguaglianza, poi sugli **insiemi di parole**.

⚠️ **La soglia e' 0,30 e non e' un caso.** A 0,60 la coppia `:4112`/`:4125`
sfugge (si somigliano solo al **30%**, perche' monte ha cambiato le parole).
Scendendo a 0,30 le coppie restano tre: **il rumore non e' cresciuto di una**,
e sotto quella soglia le due frasi non parlano piu' della stessa cosa. Chi la
alzasse riavrebbe il difetto che ha fatto nascere la rete.

⚠️ Il secondo filtro e' il giapponese: si passa solo se i due giapponesi si
somigliano **meno del 20%** in bigrammi. E' quello che tiene fuori le famiglie
di carte scritte con la stessa formula (le cameriere demoniache del lotto 8,
i tre unimorti del lotto 7), che hanno l'inglese vicino perche' ce l'hanno
vicino anche in giapponese.

⭐ **E si vede che quel filtro lavora davvero, non che avanza.** Le cameriere
`:4021` e `:4034` hanno l'inglese al **36%**, cioe' sopra la soglia: a fermarle
e' il giapponese al **42%**. Idem `:4034`/`:4047`, 39% contro 53%. Senza il
secondo filtro il referto conterrebbe tutte le famiglie a formula.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_103-inglese-ripetuto.py
"""
import collections
import io
import json
import sys

LAVORO = 'lavoro/_102-dacard.jsonl'


def main() -> None:
    voci = [json.loads(l) for l in io.open(LAVORO, encoding='utf-8') if l.strip()]
    per_en = collections.defaultdict(list)
    for v in voci:
        per_en[v['en']].append(v)

    sospette = 0
    for en, gruppo in sorted(per_en.items(), key=lambda kv: kv[1][0]['riga']):
        giapponesi = {v['jp'] for v in gruppo}
        if len(gruppo) < 2 or len(giapponesi) < 2:
            continue
        sospette += 1
        righe = ', '.join(':%d' % v['riga'] for v in gruppo)
        print(f'--- {righe}   {len(giapponesi)} giapponesi diversi, 1 inglese solo')
        print(f'    EN  {en[:150]}')
        for v in gruppo:
            print(f'    :{v["riga"]}  JP  {v["jp"][:80]}')
        print()

    ripetuti = sum(1 for g in per_en.values() if len(g) > 1)
    print(f'voci: {len(voci)}   inglesi che tornano piu\' volte: {ripetuti}   '
          f'di cui con giapponese diverso: {sospette}')

    # ⚠️⚠️ **L'uguaglianza esatta non basta, ed e' il caso che ha fatto nascere
    # questa rete.** `:4112` e `:4125` NON hanno lo stesso inglese: monte ha
    # riscritto la stessa carta con altre parole (*an ego in a cucumber* contro
    # *its soul in a cucumber*). Un confronto per stringa li lascia passare.
    # Qui si guardano gli **insiemi di parole**: inglesi che si somigliano molto
    # su giapponesi che non si somigliano per niente.
    print()
    print('=== inglesi che si SOMIGLIANO su giapponesi diversi ===')
    parole = [(v, {p.strip('.,').lower() for p in v['en'].split() if len(p) > 3}) for v in voci]
    bigrammi = {id(v): {v['jp'][i:i + 2] for i in range(len(v['jp']) - 1)} for v, _ in parole}
    vicine = 0
    for i, (a, pa) in enumerate(parole):
        for b, pb in parole[i + 1:]:
            if not pa or not pb or a['en'] == b['en']:
                continue
            en_simile = len(pa & pb) / len(pa | pb)
            if en_simile < 0.30:
                continue
            ja, jb = bigrammi[id(a)], bigrammi[id(b)]
            jp_simile = len(ja & jb) / len(ja | jb) if (ja or jb) else 1.0
            if jp_simile > 0.2:
                continue
            vicine += 1
            print(f'--- :{a["riga"]} e :{b["riga"]}   inglese {en_simile:.0%} simile, '
                  f'giapponese {jp_simile:.0%}')
            print(f'    :{a["riga"]}  EN  {a["en"][:120]}')
            print(f'             JP  {a["jp"][:70]}')
            print(f'    :{b["riga"]}  EN  {b["en"][:120]}')
            print(f'             JP  {b["jp"][:70]}')
            print()
    print(f'coppie con inglese simile e giapponese diverso: {vicine}')
    print('⚠️ referto da leggere, non una guardia: il valore atteso non e\' zero.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
