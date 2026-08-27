# -*- coding: utf-8 -*-
"""Le rese del lotto 015 (le ARMATURE del corpo, `FILTER_ARMOR`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 015 scratchpad/lotti-111

**20 righe del sorgente, 20 firme**, 20 giapponesi distinti.

⭐ **Tre parole giapponesi per «cosa che si indossa», e vanno tenute distinte**:

    服     -> vestito     (cinque righe: :51643, :56673, :101382, :101512,
                           :101642, piu' :130717)
    鎧     -> corazza     (i nomi degli oggetti dicono gia' cosi': 軽鎧
                           «corazza leggera», 輪鎧 «corazza ad anelli»,
                           重層鎧 «corazza a piastre», 厚鎧 «corazza a bande»)
    アーマー / スーツ -> armatura / tuta   (katakana: :51710 e le tre tute)
    防具   -> armatura    (:130782, come nel lotto 014)

⚠️ 衣服 e' gia' «vestiti» in `db_item.hsp` (i vestiti sporchi nel cesto): 服
segue quella parola, non i nomi degli oggetti, che sono tutti diversi
(giubbotto, cappotto, veste papale) proprio perche' il giapponese li' e'
generico.

### ⭐ DUE FORMULE, e si scrivono in fila o non si leggono come formule

**「〜ために作られた服だ」, tre righe:**

    銃弾を防ぐために作られた服 -> fatto per fermare i proiettili  (:101382)
    攻撃を防ぐために作られた服 -> fatto per parare i colpi         (:101512)
    法王のために作られた服     -> fatto per il papa                (:101642)

**「〜を束ねて作った鎧だ」, due righe** — 束ねて e' gia' «legando insieme» in
`db_creature` (il mostro-occhio che lega nervi e muscoli):

    薄片を束ねて作った鎧 -> fatta legando insieme delle lamelle  (:101707)
    輪を束ねて作った鎧   -> fatta legando insieme degli anelli   (:101837)

### ⭐ LA SCALA DEL PESO E DELLA DUREZZA CONTINUA DAL LOTTO 014

Gli scudi e le corazze usano le **stesse** parole, e le rese devono combaciare
o la scala si spezza a meta' categoria:

    非常に重い  -> pesantissimo/a   (:100720 scudo, :101902 corazza)
    固い        -> duro/a           (:100852 scudo, :101772 corazza)
    分厚い      -> spessa           (:101967) — gia' «spesso» nel dizionario
                                     (分厚い魔法書 «libro spesso»)

### ⭐⭐ `:75986` — 拘束具 ERA GIA' «GABBIA», E LA RIGA E' LA GEMELLA DI `:57965`

`chat.hsp` ha gia' 「これは装甲板ではない、拘束具だ。…これを身に着け抑え込む
がいい」 reso **«Questa non è una piastra d'armatura: è una gabbia»** — stesso
verbo (身に着ける), stesso oggetto. Quindi:

    :57965  身に着けると変形して手枷になる   -> si trasforma in ceppi   (lotto 014)
    :75986  身に着けると変形して拘束具になる -> si trasforma in una gabbia

Sono due artefatti gemelli — 《神々の枷鎖》 e 《機械拘束具》 — e la coppia si
legge solo se la costruzione resta la stessa e cambia **solo** il nome della
cosa, come nel giapponese.

### ⚠️ 何度でも使用することができる ERA GIA' RESO, OTTANTA VOLTE

`:51643` porta la coda 「何度でも使用することができる。」, che il dizionario
rende **«Si può usare sempre.»** in piu' di ottanta voci. Non e' una scelta di
questo lotto: e' un ritrovamento, il sesto in due sessioni.

### ⓘ Una parola su 高性能

`:70533` e' 高性能な特殊スーツだ e diventa «ad alte prestazioni». Il lotto 013
aveva reso 高性能だが重い光子銃 con «potente, ma pesante»: li' la parola stava
in una coppia contrapposta («potente **ma** pesante») e «potente» reggeva il
contrasto; qui e' sola, e la tuta non e' potente — e' fatta bene.
"""

IT = {
    # === la formula 「〜ために作られた服だ」
    101382: "Un vestito fatto per fermare i proiettili.",
    101512: "Un vestito fatto per parare i colpi.",
    101642: "Un vestito fatto per il papa.",

    # === la formula 「〜を束ねて作った鎧だ」
    101707: "Una corazza fatta legando insieme delle lamelle.",
    101837: "Una corazza fatta legando insieme degli anelli.",

    # === le corazze comuni — la scala del lotto 014 continua qui
    101577: "Una corazza leggera.",
    101772: "Una corazza dura.",
    101902: "Una corazza pesantissima.",
    101967: "Una corazza spessa.",
    101447: "Un vestito con del metallo sul davanti.",
    130717: "Un vestito da monaco.",
    130782: "Un'armatura da combattimento, per proteggere il corpo.",

    # === i due artefatti gemelli che si indossano e si trasformano
    75986: "Se lo indossi, si trasforma in una gabbia.",

    # === le tute e gli altri artefatti
    70466: "Una tuta fragilissima nella struttura molecolare.",
    70533: "Una tuta speciale ad alte prestazioni.",
    77564: "Una tuta speciale che sembra un costume da bagno.",
    51643: "Un vestito che cambia aspetto. Si può usare sempre.",
    51710: "Un'armatura di bambù che sbatacchia forte.",
    56673: "Un vestito pieno di cinghie.",
    65812: "Una corazza fatta per le terre fredde.",
}
