# -*- coding: utf-8 -*-
"""Il terzo lotto della 127a: le quattro PAROLE di `*txttargetnpcextrainfo`.

Il blocco ne ha otto di righe nude, ma quattro non portano nessuna parola:
`" Lv:"`, `" DV:"`, `" PV:"` e `" HP: … MP: "` sono sigle che il ramo
giapponese scrive tali e quali (command.hsp:17679-17680 le mette dentro una
`lang()` con lo stesso testo dalle due parti). Restano quattro parole vere, e
tutt'e quattro hanno gia' una resa altrove **nella stessa finestra**.

    :154  "Target: "       -> «Bersaglio: »        da config.hsp:612, skill.hsp:480
    :191  "  Gauge:"       -> «  Carica:»          da command.hsp:1361
    :193  "  GUARD BREAK"  -> «  ROTTURA GUARDIA»  da command.hsp:3559
    :195  " Guard:"        -> « Guardia:»          il complemento di :3627
"""
import io
import json

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

NUOVE = {}
MOTIVI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

_PANNELLO = (
    "command.hsp:*txttargetnpcextrainfo, il pannello che il tratto "
    "TRAIT_NORMAL_DISCERNMENT (il «discernimento» del mod MMAH) disegna sotto "
    "la mappa quando si guarda un personaggio: e' testo che il giocatore legge "
    "a ogni turno, non roba da sviluppatore. ⓘ Il pannello e' gia' meta' "
    "italiano — le righe con `lang()` (:160, :169) passano dal dizionario — e "
    "queste sono le nude rimaste. ⓘ Nessun tetto: `bmes` disegna a `pos 100` "
    "su una riga libera larga quanto la finestra. "
)

NUOVE[154] = (
    'bmes "Bersaglio: " + cdatan(CDATAN_NAME, cdata(CDATA_TARGET, txttargetnpc_arg_tc)) '
    '+ "(" + cdata(CDATA_AI_AGGRO, txttargetnpc_arg_tc) + ")", 255, 2552, 255'
)
MOTIVI[154] = (
    NUDO + _PANNELLO +
    "Chi il personaggio sta prendendo di mira, col suo livello di aggro fra "
    "parentesi. ⭐ «Bersaglio» e' la resa che il progetto ha gia' scelto per "
    "`Target` in ventisette voci di dizionario: config.hsp:612 «Bersaglio (L)» "
    "e' l'etichetta del tasto che lo sceglie, skill.hsp:480-495 sono le "
    "abilita' «Bersaglio(Magia)», «Bersaglio(Caos)»."
)

NUOVE[191] = 's += "  Carica:" + cdata(CDATA_POWER_GAUGE, txttargetnpc_arg_tc) + "/100"'
MOTIVI[191] = (
    NUDO + _PANNELLO +
    "La barra di potenza del personaggio. ⭐⭐ LA RESA E' RISCOSSA DALLA STESSA "
    "FAMIGLIA: command.hsp:1361 e' `' PGauge:%'` -> «\" Carica:\" + "
    "cdata(CDATA_POWER_GAUGE, i) + \"%\"», ed e' il pannello dei compagni, "
    "cioe' lo stesso dato nella finestra accanto. Scrivere «Gauge» qui e "
    "«Carica» li' sarebbe due nomi per lo stesso numero. ⓘ Il progetto "
    "traduce `gauge` con «barra» quando e' il meccanismo (buff.hsp:530, "
    "config.hsp:588) e con «Carica» quando e' l'etichetta del valore: qui e' "
    "il valore."
)

NUOVE[193] = 's += "  ROTTURA GUARDIA"'
MOTIVI[193] = (
    NUDO + _PANNELLO +
    "L'avviso che la guardia del personaggio e' saltata "
    "(`CDATA_GUARD_BREAK >= 100`). ⭐⭐ RESA RISCOSSA: command.hsp:3559 rende "
    "gia' `GuardBreak` con «Rottura guardia», e :3627 la usa come etichetta di "
    "valore nel pannello dei compagni. ⓘ Le maiuscole restano: qui non e' "
    "un'etichetta ma un allarme, ed e' scritto in maiuscolo di monte."
)

NUOVE[195] = 's += " Guardia:" + (100 - cdata(CDATA_GUARD_BREAK, txttargetnpc_arg_tc))'
MOTIVI[195] = (
    NUDO + _PANNELLO +
    "L'altro ramo del `GUARD BREAK` qui sopra: finche' la guardia regge, "
    "stampa quanta ne resta — `100 - CDATA_GUARD_BREAK`, cioe' il "
    "COMPLEMENTO del numero che :3627 chiama «Rottura guardia:». ⚠️ Per "
    "questo l'etichetta non e' la stessa: li' e' quanta guardia e' andata, qui "
    "quanta ne rimane, e chiamarle tutt'e due «Rottura guardia» direbbe due "
    "cose opposte con la stessa parola. L'inglese fa la stessa distinzione "
    "(`GuardBreak:` contro `Guard:`)."
)

# ---------------------------------------------------------------------------


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(n: int) -> list:
    for altezza in range(1, 25):
        blocco = righe[n - altezza:n]
        quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                     if righe[i:i + len(blocco)] == blocco)
        if quanti == 1:
            return blocco
    raise SystemExit('riga {}: nessun blocco unico entro 24 righe'.format(n))


toppe = []
for n in sorted(NUOVE):
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(NUOVE[n])
    residuo = [c for c in nuova if not _codificabile(c)]
    if residuo:
        raise SystemExit('riga {}: caratteri che CP932 non sa scrivere: {}'.format(n, residuo))
    if nuova == originale:
        raise SystemExit('riga {}: la toppa non cambierebbe niente'.format(n))
    cerca = blocco_unico(n)
    sostituisci = cerca[:-1] + [nuova]
    toppe.append({
        'file': 'command.hsp',
        'cerca': cerca if len(cerca) > 1 else cerca[0],
        'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
        'motivo': MOTIVI[n],
    })
    print('{:6d}  blocco di {} riga/e   {}'.format(n, len(cerca), nuova.strip()[:70]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-command-3.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-command-3.jsonl'.format(len(toppe)))
