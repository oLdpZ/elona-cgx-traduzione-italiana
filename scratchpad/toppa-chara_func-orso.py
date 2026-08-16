# -*- coding: utf-8 -*-
"""Rifa' le due toppe della battuta dell'orso, che erano morte come previsto.

⚠️⚠️ **La toppa vecchia diceva da sola quando sarebbe scaduta, e nessuno e'
tornato a leggerla.** Il suo motivo si chiude cosi':

    «La toppa allinea i due letterali alla resa italiana; **quando si tradurra'
    il necrologio (`chara_func.hsp:6850` e `main.hsp:4409`) andra' rifatta.»

Il necrologio e' stato tradotto. `chara_func.hsp:6850` adesso rende
`"was killed by " + cdatan(...)` con `"perse la vita contro " + cdatan(...)`,
e le due chiavi cercano ancora `"was killed by lo sbudellatore"`: **non
agganciano piu' niente**. La battuta di James e' spenta una seconda volta, per
la stessa ragione della prima — un `cnv_str` che cerca dentro una stringa che
nel frattempo ha cambiato lingua.

💡 **Trovata a schermo nel collaudo della 49ª**, non da una misura.

✅ **Quel che la toppa vecchia aveva fatto BENE e va conservato: l'ordine.**
«lo sbudellatore» e' prefisso di «lo sbudellatore marmocchio» (l'inglese
`motuhegui` non era prefisso di `gaki-motuhegui`), e `cnv_str` sostituisce sul
primo riscontro. Siccome una toppa e' una sostituzione 1:1 sulla **riga**, lo
scambio si ottiene incrociando i due contenuti: la riga del sorgente che porta
l'orso adulto riceve la chiave **lunga** (il cucciolo), e viceversa. Stesso
criterio di `fix_wish` (`module.hsp:4805`): forme lunghe prima.

⚠️ **E la sostituzione era rimasta inglese** — `"was mauled to death by a bear"`.
Anche se la chiave avesse agganciato, il necrologio sarebbe uscito in inglese.
La resa nuova segue il registro delle altre venticinque cause di morte, che sono
tutte al passato remoto e tutte **senza genere** («mori' in una trappola»,
«cadde in cenere», «si tolse la vita»): il morto puo' essere di qualunque sesso,
e «fu sbranato» non andrebbe bene.

⚠️⚠️ **Perche' questo script non riscrive a mano la chiave.** La toppa vecchia
e' morta perche' teneva una copia congelata di una resa che stava altrove. Qui
la chiave si **ricava** dalle stesse voci di dizionario da cui dipende — il
prefisso da `chara_func.hsp:6850`, i due nomi da `db_creature.hsp:37656` e
`:37748`. Se una di quelle cambia, le reti fermano lo script invece di lasciarlo
produrre una toppa che non aggancia.
"""
import io
import json
import sys

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chara_func.hsp'
NOME = 'chara_func.hsp'

RIGA_CAUSA = 6850          # `ndeathcause = lang(..., "<prefisso>" + cdatan(...))`
RIGA_ORSO = 37656          # db_creature.hsp: motuhegui
RIGA_CUCCIOLO = 37748      # db_creature.hsp: gaki-motuhegui

# Le due righe del sorgente, nell'ordine in cui ci stanno.
CERCA_ORSO = ('\t\t\tcnv_str ndeathcause, "was killed by motuhegui", '
              '"was mauled to death by a bear"')
CERCA_CUCCIOLO = ('\t\t\tcnv_str ndeathcause, "was killed by gaki-motuhegui", '
                  '"was mauled to death by a bear cub"')

# Quel che le toppe dicono ADESSO, cioe' la versione scaduta.
VECCHIA_ORSO = ('\t\t\tcnv_str ndeathcause, "was killed by lo sbudellatore marmocchio", '
                '"was mauled to death by a bear cub"')
VECCHIA_CUCCIOLO = ('\t\t\tcnv_str ndeathcause, "was killed by lo sbudellatore", '
                    '"was mauled to death by a bear"')

RESA_ORSO = 'morì fra le zanne di un orso'
RESA_CUCCIOLO = "morì fra le zanne di un cucciolo d'orso"


def _voce(percorso: str, riga: int) -> dict:
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if v['riga'] == riga:
            return v
    sys.exit(f'rete 0: nessuna voce a {percorso}:{riga}')


# --- da dove viene la chiave ------------------------------------------------
causa = _voce('dizionario/chara_func.hsp.jsonl', RIGA_CAUSA)
if causa['en'] != 'was killed by ':
    sys.exit(f"rete 1: {NOME}:{RIGA_CAUSA} non e' il necrologio atteso: {causa['en']!r}")
reso = causa.get('it') or ''
if not reso.startswith('"') or '" +' not in reso:
    sys.exit(f'rete 2: la resa del necrologio non comincia con un letterale: {reso!r}')
PREFISSO = reso[1:reso.index('" +')]
if not PREFISSO.endswith(' '):
    sys.exit(f'rete 3: il prefisso non finisce con uno spazio: {PREFISSO!r}')

orso = _voce('dizionario/db_creature.hsp.jsonl', RIGA_ORSO)
cucciolo = _voce('dizionario/db_creature.hsp.jsonl', RIGA_CUCCIOLO)
if orso['en'] != 'motuhegui' or cucciolo['en'] != 'gaki-motuhegui':
    sys.exit(f"rete 4: i due nomi non sono quelli attesi: "
             f"{orso['en']!r} / {cucciolo['en']!r}")
NOME_ORSO, NOME_CUCCIOLO = orso['it'], cucciolo['it']

CHIAVE_ORSO = PREFISSO + NOME_ORSO
CHIAVE_CUCCIOLO = PREFISSO + NOME_CUCCIOLO

# rete 5: l'ordine. Se la chiave corta e' prefisso della lunga, la lunga va
# cercata per prima, o il cucciolo diventa un orso adulto.
if not CHIAVE_CUCCIOLO.startswith(CHIAVE_ORSO):
    sys.exit(f'rete 5: {CHIAVE_ORSO!r} non e\' piu\' prefisso di {CHIAVE_CUCCIOLO!r}: '
             "l'incrocio delle due righe non serve piu' e va rifatto il ragionamento")

# --- le righe nuove ---------------------------------------------------------
def _riga(chiave: str, resa: str) -> str:
    return degrada(f'\t\t\tcnv_str ndeathcause, "{chiave}", "{resa}"')


# ⚠️ Incrociate: la riga del sorgente con l'orso adulto prende la chiave LUNGA,
#    perche' nel file viene prima e `cnv_str` aggancia il primo riscontro.
NUOVA_SU_ORSO = _riga(CHIAVE_CUCCIOLO, RESA_CUCCIOLO)
NUOVA_SU_CUCCIOLO = _riga(CHIAVE_ORSO, RESA_ORSO)

MOTIVO = (
    "La battuta dell'orso di James. `cnv_str` cerca un letterale dentro "
    "`ndeathcause`, che a runtime contiene il nome della creatura preso da "
    "`cdatan(CDATAN_NAME, cc)`. ⚠️ E' morta DUE volte per la stessa ragione: la "
    "prima quando i nomi sono stati tradotti (`motuhegui` -> «lo sbudellatore», "
    "db_creature.hsp:37656), la seconda quando e' stato tradotto il necrologio "
    "(`chara_func.hsp:6850`, da `\"was killed by \"` a `\"perse la vita contro \"`), "
    "che ha lasciato le chiavi a cercare `was killed by` dentro una stringa che "
    "non lo dice piu'. La toppa vecchia lo aveva previsto per iscritto e nessuno "
    "e' tornato a leggerla: trovata a schermo nel collaudo della 49ª. "
    "✅ Adesso la chiave si RICAVA dal dizionario invece di essere ricopiata: "
    "prefisso da chara_func.hsp:6850, nomi da db_creature.hsp:37656 e :37748, con "
    "le reti che fermano lo script se una delle tre cambia. "
    "⚠️ E la sostituzione era rimasta inglese: la resa nuova segue il registro "
    "delle altre 25 cause di morte, passato remoto e senza genere, perche' il "
    "morto puo' essere di qualunque sesso. "
    "⚠️ L'ordine e' incrociato rispetto al sorgente: la chiave corta e' prefisso "
    "della lunga, e `cnv_str` sostituisce sul primo riscontro; siccome una toppa "
    "e' una sostituzione 1:1 sulla riga, lo scambio si ottiene incrociando i due "
    "contenuti. Stesso criterio di `fix_wish` (module.hsp:4805): forme lunghe prima. "
    "⚠️ Sostituzione 1:1 sulle righe; il ramo giapponese resta intatto."
)

# --- le reti sul sorgente ---------------------------------------------------
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
posizioni = {}
for etichetta, cerca in (('orso', CERCA_ORSO), ('cucciolo', CERCA_CUCCIOLO)):
    quante = [i for i, r in enumerate(righe) if r == cerca]
    if len(quante) != 1:
        sys.exit(f'rete 6: la riga «{etichetta}» compare {len(quante)} volte nel '
                 f'sorgente, non una: toppa ambigua')
    if 'lang(' in cerca:
        sys.exit(f'rete 7: la riga «{etichetta}» ha una lang(): servirebbe un rinvio')
    posizioni[etichetta] = quante[0]
# rete 8: l'incrocio ha senso solo se l'orso adulto viene PRIMA nel file
if posizioni['orso'] > posizioni['cucciolo']:
    sys.exit("rete 8: nel sorgente il cucciolo viene prima dell'orso: "
             "l'incrocio va rovesciato")

# --- si riscrivono le due toppe --------------------------------------------
attese = {
    CERCA_ORSO: (VECCHIA_ORSO, NUOVA_SU_ORSO),
    CERCA_CUCCIOLO: (VECCHIA_CUCCIOLO, NUOVA_SU_CUCCIOLO),
}
toppe = [json.loads(l) for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]
toccate, gia = 0, 0
viste = set()
for t in toppe:
    # ⚠️ `cerca` puo' essere una LISTA (le toppe su piu' righe): non e' hashabile
    #    e va scartata prima del confronto, o `in attese` esplode.
    cerca = t.get('cerca')
    if t['file'] != NOME or not isinstance(cerca, str) or cerca not in attese:
        continue
    viste.add(cerca)
    vecchia, nuova = attese[cerca]
    if t['sostituisci'] == nuova:
        gia += 1
        continue
    # rete 9: si riscrive solo quello che dice ancora la versione scaduta
    if t['sostituisci'] != vecchia:
        sys.exit(f'rete 9: la toppa non dice la versione attesa ma '
                 f'{t["sostituisci"]!r}')
    print(f'  - {t["sostituisci"].strip()}')
    print(f'  + {nuova.strip()}')
    t['sostituisci'] = nuova
    t['motivo'] = MOTIVO
    toccate += 1
# rete 10: tutt'e due le toppe devono esistere
if viste != set(attese):
    sys.exit(f'rete 10: toppe non trovate -> {sorted(set(attese) - viste)}')

# ⚠️ si compone e si codifica PRIMA di aprire il file in scrittura: nella 39ª
#    un errore di codifica dentro `write()` ha lasciato `toppe.jsonl` a zero byte.
dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('toppe.jsonl', 'wb') as f:
    f.write(dati)

print(f'--- chiave ricavata: {PREFISSO!r} + {NOME_ORSO!r} / {NOME_CUCCIOLO!r}')
print(f"--- {toccate} toppe rifatte, {gia} gia' a posto (totale {len(toppe)})")
