# -*- coding: utf-8 -*-
"""Il primo lotto della 128a: gli AP di `chara_func.hsp`, e la premessa era falsa.

`RIPRESA-sessione.md`, `decisioni.md` e `invariati.md` descrivevano questo
fronte cosi': «tre basi per cinque code», una frase che si compone **per
ricorsione** con quattro frammenti inglesi nudi, uno dei quali porta `his()` a
un argomento, cioe' morfologia inglese. Da li' la conclusione: «e' una toppa a
blocco di una certa dimensione e vuole una sessione sua».

⚠️⚠️⚠️ **NON E' COSI', E LE CODE NON ESCONO MAI.** Le otto chiamate ricorsive
(`:8533`, `:8536`, `:8540`, `:8546`, `:8548`, `:8553`, `:8556`, `:8560`) stanno
tutte dentro `gain_ap_old`, e `gain_ap_old` ha **un solo chiamante in tutto il
sorgente**: `action.hsp:8992`, che gli passa `"destone"`. I due blocchi che
contengono le chiamate sono `if ( gain_ap_source == "talk" )` (`:8530`) e
`if ( gain_ap_source == "kill" )` (`:8543`): dentro `gain_ap_old` quella
variabile vale sempre e solo `"destone"`, non viene mai riassegnata (i sei
riferimenti nel file sono tutti confronti `==`), quindi **quei due blocchi sono
irraggiungibili**. Nessuna coda, nessun `his()`, nessuna ricorsione.

⭐ E l'autore del mod lo dice lui stesso, tre righe sopra la funzione viva:
`// Ano made ap gain functions a lot simpler in 2.29, but he didn't change the
destone formula.` — la vecchia funzione e' rimasta in piedi **solo** per la
pietra, con dentro la sua coda morta.

Quindi i valori possibili sono TRE e sono fissi, non «tre basi per cinque code»:

    :8430   gain_ap      (viva)  gain_ap_source in {"talk", "kill"}
                                 chiamata da chara_func.hsp:3991 e :4135
    :8522   gain_ap_old  (viva)  gain_ap_source == "destone"
                                 chiamata da action.hsp:8992

⚠️ L'operando resta intatto in tutt'e due i siti: e' `gain_ap_source` a decidere
sette rami del codice, e tradurlo li spegnerebbe in silenzio. La resa si separa
dall'operando **al sito di stampa**, che e' la strada gia' scritta in
`invariati.md` — solo che non serve una tabella: serve un `if` in un sito e una
stringa fissa nell'altro.

Le tre parole non si sono scelte, si sono riscosse dal progetto:

    "talk"     e' la sconfitta per PERSUASIONE (proc.hsp:2338 `dmgsptalk`,
               skillexp SKILL_NORMAL_NEGOTIATION). skill.hsp:222 rende
               «Negotiation» -> «Trattativa», e action.hsp:15250 / proc.hsp:26922
               rendono «switched to talking mode!» -> «passa in assetto di
               trattativa!». La parola c'e' gia' ed e' una sola.
    "kill"     l'uccisione (chara_func.hsp:4135, dentro *check_kill).
    "destone"  NON e' una parola che il giocatore possa capire: e' il nome
               interno dell'oggetto ITEM_ID_AWAKE_DESTONE, 覚醒の閃石 /
               «awakening stone», che il dizionario rende gia'
               «pietra del risveglio» (db_item.hsp:134581, femminile).
               ⭐ E' l'unico oggetto che accende EFFECT_AWAKE_DESTONE
               (db_item.hsp:45502, unica assegnazione).
"""
import io
import json
import os

BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
SORGENTE = os.path.join(BASE, 'chara_func.hsp')
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

_MORTA = (
    "⚠️⚠️⚠️ E LA PREMESSA EREDITATA ERA FALSA: RIPRESA/decisioni/invariati "
    "descrivevano «tre basi per CINQUE CODE» e un `his()` da togliere. Le "
    "otto chiamate che compongono quelle code (:8533 :8536 :8540 :8546 :8548 "
    ":8553 :8556 :8560) stanno tutte dentro `gain_ap_old`, che ha un solo "
    "chiamante in tutto il sorgente — action.hsp:8992, con \"destone\" — e "
    "stanno dentro `if ( gain_ap_source == \"talk\" )` (:8530) e "
    "`if ( gain_ap_source == \"kill\" )` (:8543): dentro quella funzione la "
    "variabile vale sempre \"destone\" e non e' mai riassegnata, quindi i due "
    "blocchi sono IRRAGGIUNGIBILI. Le code non escono mai a schermo. ⭐ Lo "
    "dice l'autore del mod tre righe sopra la funzione viva: «Ano made ap "
    "gain functions a lot simpler in 2.29, but he didn't change the destone "
    "formula» — la vecchia funzione sopravvive solo per la pietra, con dentro "
    "la sua coda morta. "
)

_OPERANDO = (
    "⚠️ `gain_ap_source` e' OPERANDO E TESTO INSIEME: sette confronti lo "
    "leggono per decidere il ramo (:8415 :8436 :8455 :8509 :8524 :8530 :8543), "
    "quindi l'operando NON si tocca e la resa si separa da lui al sito di "
    "stampa. E' la strada gia' scritta in invariati.md; quel che cambia e' che "
    "non serve una tabella, perche' i valori vivi sono tre e fissi. "
)

TOPPE = [
    {
        'cerca': [
            '\t\t\t\t\t\ttxt "" + name(cnt) + " obtained " + ( cdata(CDATA_AP_TOTAL, cnt) - gain_ap_total ) + " AP from the " + gain_ap_source + "."',
        ],
        'sostituisci': [
            '\t\t\t\t\t\tif ( gain_ap_source == "talk" ) {',
            '\t\t\t\t\t\t\ttxt "" + name(cnt) + " ottiene " + ( cdata(CDATA_AP_TOTAL, cnt) - gain_ap_total ) + " AP dalla trattativa."',
            '\t\t\t\t\t\t} else {',
            '\t\t\t\t\t\t\ttxt "" + name(cnt) + " ottiene " + ( cdata(CDATA_AP_TOTAL, cnt) - gain_ap_total ) + " AP dall\'uccisione."',
            '\t\t\t\t\t\t}',
        ],
        'attese': 1,
        'motivo': (
            NUDO +
            "chara_func.hsp:*gain_ap (:8343), la riga di combattimento con cui "
            "un compagno annuncia gli AP guadagnati. A schermo oggi si legge "
            "«X obtained 3 AP from the kill.» " +
            _OPERANDO +
            "⚠️⚠️ TOPPA A BLOCCO, e il blocco serve: «from the » + operando + "
            "«.» non si puo' rendere in italiano senza spaccare le due vie, "
            "perche' «dalla trattativa» e «dall'uccisione» hanno preposizioni "
            "diverse e l'operando deve restare inglese. ⭐ La forma dell'`if` "
            "non e' inventata: e' COPIATA da :8415-:8419, quindici righe piu' "
            "su, DENTRO LA STESSA FUNZIONE — stesso confronto "
            "`gain_ap_source == \"talk\"`, stesso `} else {`. "
            "⭐ I due valori sono ESATTAMENTE due e sono contati: `gain_ap` ha "
            "due soli chiamanti in tutto il sorgente, chara_func.hsp:3991 "
            "(\"talk\") e :4135 (\"kill\"), quindi l'`else` e' l'uccisione e "
            "non un ripiego. "
            "⭐ «talk» qui NON e' il chiacchierare: e' la sconfitta per "
            "persuasione — proc.hsp:2338 sfonda gli SP con `dmgtalk` e "
            ":2340 da' esperienza in SKILL_NORMAL_NEGOTIATION — e la parola "
            "italiana e' gia' decisa: skill.hsp:222 rende «Negotiation» -> "
            "«Trattativa», action.hsp:15250 e proc.hsp:26922 rendono "
            "«switched to talking mode!» -> «passa in assetto di trattativa!». " +
            _MORTA
        ),
    },
    {
        'cerca': [
            '\t\t\t\t\ttxt "" + name(gain_ap_chara_id) + " obtained " + ( cdata(CDATA_AP_TOTAL, gain_ap_chara_id) - gain_ap_total ) + " AP from the " + gain_ap_source + "."',
        ],
        'sostituisci': [
            '\t\t\t\t\ttxt "" + name(gain_ap_chara_id) + " ottiene " + ( cdata(CDATA_AP_TOTAL, gain_ap_chara_id) - gain_ap_total ) + " AP dalla pietra del risveglio."',
        ],
        'attese': 1,
        'motivo': (
            NUDO +
            "chara_func.hsp:*gain_ap_old (:8443), la gemella vecchia della "
            "riga qui sopra. A schermo oggi si legge «X obtained 3 AP from the "
            "destone.» " +
            _OPERANDO +
            "⭐⭐ QUI L'OPERANDO E' UNO SOLO, contato: `gain_ap_old` ha un "
            "chiamante solo in tutto il sorgente, action.hsp:8992, che gli "
            "passa \"destone\"; e :8509 e :8524 fanno uscire la funzione "
            "prima e dopo la stampa proprio su quel valore. Quindi la resa e' "
            "una stringa fissa e non serve nessun `if`. "
            "⚠️⚠️ E «destone» non e' una parola inglese che il giocatore possa "
            "capire: e' il NOME INTERNO dell'oggetto, "
            "ITEM_ID_AWAKE_DESTONE / EFFECT_AWAKE_DESTONE. L'oggetto e' "
            "覚醒の閃石 / «awakening stone», che il dizionario rende gia' "
            "«pietra del risveglio» (db_item.hsp:134581, femminile) — quindi "
            "la resa non si inventa, si riscuote. ⭐ Ed e' l'unico oggetto che "
            "accende quell'effetto: db_item.hsp:45502 e' l'unica assegnazione "
            "di EFFECT_AWAKE_DESTONE in tutto il sorgente, e action.hsp:8947 "
            "l'unico posto che lo legge. ⓘ La pietra si usa su un compagno e "
            "gli da' AP; se non ne da', :8995 dice gia' in italiano che «non "
            "sembra servirgli a niente». " +
            _MORTA
        ),
    },
]

# ---------------------------------------------------------------------------

for t in TOPPE:
    cerca = t['cerca']
    quante = sum(1 for i in range(len(righe) - len(cerca) + 1)
                 if righe[i:i + len(cerca)] == cerca)
    if quante != t['attese']:
        raise SystemExit('«{}»: attese {} occorrenze, trovate {}'
                         .format(cerca[-1].strip()[:60], t['attese'], quante))
    for riga in t['sostituisci']:
        riga.encode('cp932')   # solleva se CP932 non sa scrivere
        for c in riga:
            if c != '♪' and len(c.encode('cp932')) != 1:
                raise SystemExit('carattere a due byte {!r} in: {}'.format(c, riga))
    if t['sostituisci'] == cerca:
        raise SystemExit('la toppa non cambierebbe niente')
    print('{:4d} occorrenza   {}'.format(quante, cerca[-1].strip()[:66]))

fuori = [{'file': 'chara_func.hsp', 'cerca': t['cerca'],
          'sostituisci': t['sostituisci'], 'motivo': t['motivo']}
         for t in TOPPE]

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in fuori).encode('utf-8')
with io.open('lavoro/toppe-128-ap.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-128-ap.jsonl'.format(len(fuori)))
