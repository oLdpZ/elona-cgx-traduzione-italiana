# -*- coding: utf-8 -*-
"""Le rese del lotto 009 (le BACCHETTE, `FILTER_ITEM_ROD`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 009 scratchpad/lotti-110

**32 righe del sorgente, 30 firme.** E' la categoria piu' formulaica
dell'indice 3: **trenta righe su trenta** cominciano con 「振ることで」 e
finiscono con 「魔法の杖だ。」.

    振ることで〜魔法の杖だ。 -> Una bacchetta che, agitata, ...

⭐ Il verbo non e' stato scelto: 「を振った。」 e' gia' nel dizionario come
«Hai agitato ...», il messaggio che il giocatore legge quando usa la bacchetta.
La riga del rapporto e la riga del gioco ora dicono la stessa parola.

⚠️ `:94105` e `:122824` hanno lo **stesso identico inglese** e due giapponesi
che differiscono per un carattere solo — `HP` a mezza larghezza contro `ＨＰ` a
larghezza piena. Sono la stessa frase: stessa resa.
"""

IT = {
    # --- gli attacchi ad area
    61949: "Una bacchetta che, agitata, fa un attacco ad area di tipo PV/DV.",
    62397: "Una bacchetta che, agitata, fa un attacco ad area di veleno.",
    70754: "Una bacchetta che, agitata, fa un attacco ad area di fulmine.",
    71859: "Una bacchetta che, agitata, fa un attacco ad area d'oscurità.",

    # --- le saette e i dardi: i nomi vengono da `skill.hsp`
    62317: "Una bacchetta che, agitata, tira una saetta arcana.",
    119624: "Una bacchetta che, agitata, tira una saetta di fulmine.",
    122967: "Una bacchetta che, agitata, tira una saetta di fuoco.",
    123047: "Una bacchetta che, agitata, tira una saetta di gelo.",
    123207: "Una bacchetta che, agitata, tira un dardo magico.",

    # --- quel che si crea nel punto scelto
    92065: "Una bacchetta che, agitata, apre porte nei muri vicini.",
    92800: "Una bacchetta che, agitata, alza muri di fiamme dove vuoi.",
    93152: "Una bacchetta che, agitata, crea una pozza d'acido dove vuoi.",
    94537: "Una bacchetta che, agitata, alza muri magici dove vuoi.",
    98579: "Una bacchetta che, agitata, tende una ragnatela sul bersaglio.",
    123127: "Una bacchetta che, agitata, evoca mostri ostili qui intorno.",

    # --- quel che fa a te o a chi ti sta accanto
    94105: "Una bacchetta che, agitata, cura te o chi ti sta accanto.",
    122824: "Una bacchetta che, agitata, cura te o chi ti sta accanto.",
    104945: "Una bacchetta che, agitata, ti recupera gli MP.",
    103508: "Una bacchetta che, agitata, purifica gli oggetti qui intorno.",
    105384: "Una bacchetta che, agitata, para le maledizioni a te e ai vicini.",
    105969: "Una bacchetta che, agitata, accelera te o chi ti sta accanto.",

    # --- quel che fa al bersaglio
    96358: "Una bacchetta che, agitata, ricostruisce il bersaglio.",
    98957: "Una bacchetta che, agitata, ti sottomette il bersaglio.",
    106769: "Una bacchetta che, agitata, mette il bersaglio in silenzio.",
    119544: "Una bacchetta che, agitata, rallenta il bersaglio.",

    # --- il resto
    96278: "Una bacchetta che, agitata, ricostruisce l'oggetto scelto.",
    111780: "Una bacchetta che, agitata, dà modo di esprimere un desiderio.",
    117762: "Una bacchetta che, agitata, rivela le zone non esplorate.",
    129953: "Una bacchetta che, agitata, teletrasporta a caso.",
    130033: "Una bacchetta che, agitata, identifica gli oggetti che porti.",
}
