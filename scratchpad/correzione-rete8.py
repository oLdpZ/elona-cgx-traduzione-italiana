# -*- coding: utf-8 -*-
"""Le sei rese che stampano «di il», «a il», «in il», «su il».

⚠️ **La rete 8 e' nata nel lotto 009 (35a) e da allora ferma i lotti nuovi, ma
nessuno l'aveva mai passata su quello che c'era prima.** Passata all'indietro su
tutto il dizionario (`scratchpad/rete8_dizionario.py`) trova **sei** rese gia'
entrate che mettono una preposizione semplice davanti a un nome che porta gia'
l'articolo:

    action.hsp:11810   «Hai dato istruzioni a » + cdatan   -> «a il putit»
    action.hsp:12706   «i movimenti di »        + name     -> «di il putit»
    action.hsp:18997   «i geni di »/«in »       + cdatan   -> due in una riga
    action.hsp:19004   «i geni di »             + cdatan
    proc.hsp:1966      «piomba giu' su »        + cdatan   -> «su il putit»

💡 **E il motivo per cui `cdatan` conta quanto `name` sta in una toppa.**
`init.hsp:1717` diceva `return "the " + cdatan(CDATAN_NAME, name_arg1)`, e la
toppa toglie il `"the "` perche' in italiano l'articolo dipende da genere ed
elisione e lo porta il **nome della creatura** (`db_creature.hsp`: «il cultista
del fuoco», «la medusa purificata»). Da quel momento `name(x)` e
`cdatan(CDATAN_NAME, x)` restituiscono la **stessa identica stringa**, articolo
compreso: quello che vale per l'una vale per l'altra.

⚠️ **Otto delle quattordici segnalazioni erano falsi positivi**, e vanno sapute
perche' la stessa misura si rifara':
  - «**con**» non si fonde in italiano moderno — «con il putit» e' corretto, «col»
    e' facoltativo. Sono cinque: `action.hsp:1929`, `:6389`, `:10249`,
    `adv.hsp:268`, `proc.hsp:4326`;
  - «Hai tirato **su** » + `itemname` (`proc.hsp:5055`) e' un **verbo
    sintagmatico**, non una preposizione che regge il nome;
  - `proc.hsp:11893` e `:11898` (lotto 014) hanno `valn = skillname(i)`, e i nomi
    di abilita' non portano articolo.

La strada e' sempre la stessa del lotto 014: il nome diventa **soggetto** o
**complemento oggetto**, mai un genitivo. Lo script e' ripetibile.
"""
import io
import json

CORREZIONI = {
    'dizionario/action.hsp.jsonl': {
        # cdatan da complemento di termine a complemento oggetto
        (11810, 'You instructed  what to do while bored.'): (
            '"Hai dato istruzioni a " + cdatan(CDATAN_NAME, tc) + "."',
            '"Hai istruito " + cdatan(CDATAN_NAME, tc) + " sul da farsi."',
        ),
        # «i movimenti di X» -> «come si muove X»
        (12706, 'You also analyzed the movements of .'): (
            '"Hai analizzato anche i movimenti di " + name(tc) + "."',
            '"Hai analizzato anche come si muove " + name(tc) + "."',
        ),
        # due preposizioni in una riga sola: tutt'e due i nomi diventano soggetti
        (18997, "Really add 's gene to ?"): (
            '"Vuoi davvero innestare i geni di " + cdatan(CDATAN_NAME, tc) '
            '+ " in " + cdatan(CDATAN_NAME, rc) + "?"',
            'cdatan(CDATAN_NAME, tc) + " cede i geni, " + cdatan(CDATAN_NAME, rc) '
            '+ " li riceve. Procedere?"',
        ),
        (19004, " has inherited 's gene!"): (
            'cdatan(CDATAN_NAME, rc) + " ha ereditato i geni di " '
            '+ cdatan(CDATAN_NAME, tc) + "!"',
            'cdatan(CDATAN_NAME, tc) + " cede i geni e " + cdatan(CDATAN_NAME, rc) '
            '+ " li eredita!"',
        ),
    },
    'dizionario/proc.hsp.jsonl': {
        (1966, ' attacked  with the gravitational potential of drop!'): (
            'name(cc) + " piomba giù su " + cdatan(CDATAN_NAME, tc) '
            '+ " con tutto il peso della caduta."',
            'name(cc) + " piomba giù e travolge " + cdatan(CDATAN_NAME, tc) '
            '+ " con tutto il peso della caduta."',
        ),
    },
}

fatte, saltate, corrette = 0, 0, []
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
        # rete 1: si corregge solo quello che dice ancora la resa vecchia
        if d.get('it') != vecchia:
            raise SystemExit(f'rete 1: {percorso}{k} non dice la resa attesa '
                             f"ma {d.get('it')!r}")
        print(f"{percorso.split('/')[-1]}:{d['riga']}\n    {d['it']}\n -> {nuova}")
        d['it'] = nuova
        corrette.append(dict(d))
        fatte += 1
    # rete 2: nessuna correzione deve restare senza voce
    if viste != set(correzioni):
        raise SystemExit(f'rete 2: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    with io.open(percorso, 'w', encoding='utf-8', newline='\n') as f:
        for d in righe:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

# rete 3: le rese nuove devono passare `verifica` come se fossero un lotto.
# ⚠️ `verifica --dizionario` NON le guarda: confronta il dizionario col sorgente
#    e conta orfane e non tradotte, non valida le rese. Una correzione fatta a
#    mano nel dizionario non incontra nessuna guardia, ed e' il buco per cui
#    questa rete esiste.
if corrette:
    from strumenti.verifica import controlla_lotto
    problemi = controlla_lotto(corrette)
    if problemi:
        for chiave, elenco in problemi.items():
            print(f'rete 3: {chiave}: ' + '; '.join(elenco))
        raise SystemExit('le rese nuove non passano verifica')
    print(f'rete 3: {len(corrette)} rese nuove passano verifica')

print(f"--- {fatte} rese corrette, {saltate} gia' a posto")
