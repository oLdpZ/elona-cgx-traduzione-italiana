# -*- coding: utf-8 -*-
"""Le rese del lotto 068 — LE CINTURE: `FILTER_GIRDLE` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 068 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa068.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 068`: **9 righe su 9** con lo spazio prima del `\\n`,
9 su 9 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 068`: **+9** per 9 rese,
nessuna gemella.

⭐⭐ `_122-sorelle-per-frase`: cinque frasi con una sorella, **quattro gia'
rese**, tutte la stessa famiglia. `:100392` e' la **quinta** riga dei materiali
speciali, e la sesta — `:130450`, gli stivali — e' l'unica che resta.
"""

IT = {
    # =====================================================================
    # LA FAMIGLIA DEI MATERIALI SPECIALI — quinta riga di sei
    # =====================================================================
    # ⭐⭐⭐ :100849 scudo (058), :101769 corazza (060), :99872 elmo (063),
    #    :101114 guanti (066), :100392 cintura (068)  <- questa,
    #    e resta :130450, gli stivali.
    #    L'apertura e' la stessa frase in tutt'e sei.
    # ⓘ 素材の長所を伸ばした e' il rovescio dell'elmo, che parlava di coprire
    #   i difetti: qui il giapponese dice che hanno spinto i PREGI, e da li'
    #   viene la leggerezza. Le due righe si leggono insieme.

    100392: "Una cintura che, incrociando materiali speciali, ha ottenuto una protezione più solida. Forse perché ne hanno spinto i pregi, è venuta più leggera del solito. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LE CINTURE COMUNI
    # =====================================================================
    # ⓘ 考案された invece di 作られた: e' una variante della famiglia
    #   〜を守る為に作られた (testa 063, collo 064, polso 066), e la rete non
    #   l'accosta perche' il verbo cambia. La resa dice «pensata» dove le
    #   altre dicono «fatta»: il giapponese distingue e l'italiano pure.
    # ⚠️ L'inglese aggiunge «elderly» che il giapponese non ha: 婦人 sono le
    #   signore, non le anziane. Reso dal giapponese.
    126712: "Un'armatura pensata per proteggere la parte bassa del corpo senza intralciare i movimenti. Pare che nella stagione fredda certe signore ne portino una fatta di materiale leggero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100327: "Una cintura che alza la protezione sovrapponendo strato su strato. Oltre a pesare di più, ha la controindicazione che i pezzi sovrapposti sbattono l'uno contro l'altro e fanno rumore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》
    # =====================================================================
    # ⚠️ L'inglese apre con «Giant belt buckle with an ego»: quell'«ego» nel
    #   giapponese non c'e' da nessuna parte. Reso dal giapponese.
    # ⓘ 得意属性 e' l'attributo in cui si e' forti, e l'indice 3 gia' in gioco
    #   dice «Cambia l'attributo di certe abilità»: stessa parola.
    61581: "Una cintura con una fibbia enorme. Manda una luce che cambia per un po' l'attributo in cui si è forti. È cosparsa di gemme fatte a somiglianza di occhi, e ognuna governa un attributo diverso. Anche il corpo della fibbia ha la forma di un occhio gigante, ma pare sia venuto così per caso, mentre la costruivano senza pensarci troppo. \\n# ~Dizionario Fantastico di Irva~",

    # ネイン -> «<Nein>», che in gioco e' «<Nein> la strega volante» e parla
    # al femminile. L'indice 3 dice gia' «Una scopa che ti fa levitare».
    64276: "Una scopa a cui <Nein> ha dato la facoltà di volare. All'inizio la si pensava da cavalcare a gambe larghe, ma siccome in salita improvvisa c'è il rischio di spaccarsi l'inguine conviene sedercisi sopra di traverso. Ha caratteristiche inutilmente spinte e arriva alla velocità del suono, ma a provarci davvero chi ci sta sopra viene sbalzato giù di sicuro. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐⭐ L'ULTIMA FRASE L'INGLESE LA BUTTA. 投げたりしないで穿こう —
    #    «mettiamocele, invece di tirarle» — e' una battuta su un gesto che
    #    nel gioco si fa davvero, e l'inglese la sostituisce con «Put them
    #    on, yes, right now!». Il giapponese ha DUE esortazioni di fila e
    #    l'italiano le tiene tutt'e due.
    # ⓘ 白虎 -> «la tigre bianca» (dizionario, creatura).
    64343: "Fatte cucendo pelliccia di tigre con un filo magico estratto dall'anima dei maghi. Sono famose per la tenacia, e infatti a portarle cent'anni non si strappano e non prendono odore. Siccome lasciano muoversi bene si usano come abbigliamento sportivo, e ne esiste anche una versione di marca fatta con la pelliccia di tigre bianca. Mutande sì, ma nel senso di pantaloncini, quindi non c'è da vergognarsi se qualcuno le vede. Mettiamocele tutti. E mettiamocele, invece di tirarle. \\n# ~Dizionario Fantastico di Irva~",

    # 魔石 -> «pietra magica» (dizionario: la pietra magica del folle, del
    # conquistatore). レシマス «Lesimas», パルミア «Palmia», エウダーナ
    # «Eulderna», tutti dal dizionario.
    68112: "Una cintura cosparsa di imitazioni di pietre magiche. Le pietre magiche originali nascondevano una forza legata al sigillo di Lesimas, e da lì era nato il piano di costruire un impianto difensivo per proteggere Palmia. Con l'aiuto di un avventuriero venuto da Eulderna le imitazioni si riuscirono a produrre, ma una parte della forza non fu riproducibile e il piano si arenò. Di tutto rimase soltanto un prototipo: un'armatura che copre per un momento il solo portatore con un muro magico. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ 収穫の神 -> «il dio del raccolto», che e' la forma gia' nel
    #   dizionario (due battute). Vedi la testa: il progetto rende 富の神 al
    #   FEMMINILE e 収穫の神 al maschile, ed e' una divergenza da decidere,
    #   non da sistemare di straforo dentro un lotto del corpo.
    76049: "Quello che il dio del raccolto adopera perché le cose a cui tiene non gli scappino. A distrarsi un attimo, si avvolge addosso da sé come una cintura. \\n# ~Dizionario Fantastico di Irva~",

    82342: "Una cintura fatta di metallo antico unito a scaglie. Ci è passata sopra una sostanza rossa particolare, e dicono che protegga il corpo di chi la indossa e le cose che porta con sé. \\n# ~Dizionario Fantastico di Irva~",
}
