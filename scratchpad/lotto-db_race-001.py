# -*- coding: utf-8 -*-
"""I 76 nomi di razza di `db_race.hsp` — la finestra di scelta della razza.

Aperto nella 64a dopo il collaudo della creazione del personaggio: la finestra
«Scelta della razza» e' **la prima cosa che un giocatore nuovo legge**, ed era
tutta inglese. `db_race.hsp` non aveva un file di dizionario, quindi
`verifica --dizionario` non lo nominava (la lezione della 54a: un file senza
dizionario non e' un file finito, e' un file che nessun conteggio guarda).

⚠️⚠️ **`racename` e' l'etichetta, `CDATAN_RACE` e' la chiave: non sono la stessa
cosa e solo la prima si traduce.** `db_race.hsp` le tiene affiancate --
`cdatan(CDATAN_RACE, rc) = "metal"` (letterale nudo) accanto a
`racename = lang("メタル", cnven("metal"))`. La chiave e' confrontata in **535
siti**: `== "spider"`, `== "snail"`, `== "doggod"`, `== "golem"`. Tradurla
spegnerebbe mezzo gioco. E' la stessa famiglia di `CDATAN_NEWSEX` (63a) e di
`mdatan` (62a), ma qui il progetto e' facile: la chiave non passa mai dal
dizionario, perche' non e' dentro una `lang()`.

⚠️ `cnven()` non e' una trappola come `cnv_str`: fa **solo la maiuscola
iniziale** (`init.hsp:191`). Verificato prima di tradurre.

## Il tetto

La colonna dei nomi va da `wx + 64` a `wx + 210`, dove comincia il testo della
descrizione (`chara.hsp:4569`, `tx = wx + 230` e `pos tx - 20`): 146 px, cioe'
**20 caratteri** a 7 px. Misurato sulla schermata della 64a: i nomi cominciano a
x=690 e le righe della descrizione a x=831.

## Le convenzioni, e da dove vengono

⭐ **Dal bestiario, che ha gia' nominato queste creature** (`db_creature.hsp`,
1131 nomi resi): coboldo, uomo lucertola, draco, fuoco fatuo, quickling,
scheletro, spettro, mandragora, folletto, cupido, arpia. Qui si prende la forma
**nuda**, senza l'articolo che il bestiario porta: la razza e' un'etichetta
(«Razza: Fata»), non il nome di una creatura in una frase.

⭐ **Dal giapponese dove e' piu' preciso dell'inglese**, che e' la regola della
63a: 巨獣 «bestia gigante» dove l'inglese dice `largeanimal`; 昆虫 «insetto»
dove dice `beetle`; 鉱物 «minerale» dove dice `rock`; 幻獣 «bestia fantastica»
dove dice `beast`; 甲殻 «crostaceo» dove dice `shell`; 海魔 «mostro marino» dove
dice `seamonster`; 駒 «pedina» dove dice `piece`; 乗用機械 «veicolo».

⚠️ **Restano invariati i nomi propri delle razze di Elona**: Yerles, Norland,
Eulderna, Juere, Elea, Karune, Zanan, Roran, Yeek, Yith, Mazin — e Ent, Lich,
Golem, Goblin, Medusa, Asura, Quickling, che l'italiano ha adottato tali e quali
e che il bestiario scrive gia' cosi'.
"""
import io
import json

ESTRAZIONE = "lavoro/_db_race.jsonl"
USCITA = "lavoro/fase4-db_race-001.jsonl"
TETTO = 20

RESE = {
    707: "Coboldo",              # コボルト — bestiario: il coboldo
    775: "Orco",                 # オーク
    843: "Bestia gigante",       # 巨獣 — il jp dice «bestia gigante», non «animale grande»
    911: "Uomo lucertola",       # 竜人 — bestiario: l'uomo lucertola
    979: "Minotauro",            # ミノタウロス
    1047: "Yerles",              # イェルス — nome proprio
    1120: "Norland",             # ノーランド — nome proprio
    1193: "Eulderna",            # エウダーナ — nome proprio
    1266: "Fata",                # 妖精 — bestiario: la fata
    1346: "Asura",               # 阿修羅
    1415: "Melma",               # スライム — bestiario: la melma
    1483: "Dio dei cani",        # 犬の神
    1550: "Nano",                # 丘の民 «popolo delle colline», ma la razza e' il nano
    1619: "Juere",               # ジューア — nome proprio
    1692: "Zombi",               # ゾンビ — bestiario: lo zombi
    1764: "Elea",                # エレア — nome proprio
    1837: "Coniglio",            # ウサギ
    1905: "Pecora",              # 羊
    1973: "Rana",                # 蛙
    2041: "Verme",               # ワーム — bestiario: il verme
    2109: "Chiocciola",          # かたつむり — bestiario: la chiocciola
    2175: "Mandragora",          # マンドレイク — bestiario: la mandragora
    2244: "Insetto",             # 昆虫 — il jp dice «insetto», l'inglese «beetle»
    2312: "Fungo",               # きのこ — bestiario: il fungo
    2380: "Pipistrello",         # コウモリ — bestiario: il pipistrello
    2449: "Ent",                 # エント — bestiario: l'ent
    2517: "Lich",                # リッチ — bestiario: il lich
    2590: "Batterio",            # バクテリア
    2659: "Spettro",             # 幽霊 — bestiario: lo spettro
    2732: "Spirito",             # 精霊 — bestiario: lo spirito
    2800: "Occhio",              # 目
    2868: "Mazin",               # 魔人 — razza propria di Elona
    2936: "Vespa",               # ワスプ — bestiario: la vespa
    3004: "Gigante",             # 巨人
    3072: "Folletto",            # 悪魔 — bestiario: il folletto (imp)
    3140: "Mano",                # 手
    3208: "Serpente",            # 蛇
    3276: "Draco",               # 亜竜 — bestiario: il draco
    3344: "Goblin",              # ゴブリン — bestiario: il goblin
    3413: "Orso",                # 熊
    3481: "Armatura",            # 鎧
    3550: "Medusa",              # メデューサ — bestiario: la medusa
    3618: "Cupido",              # 天使 — bestiario: il cupido
    3687: "Karune",              # カルーン — nome proprio
    3760: "Arpia",               # 鳥人 — bestiario: l'arpia
    3828: "Drago",               # ドラゴン
    3896: "Dinosauro",           # 恐竜
    3964: "Bestia fantastica",   # 幻獣 — il jp distingue la belva mitica
    4032: "Ragno",               # 蜘蛛 — bestiario: il ragno
    4100: "Golem",               # ゴーレム — bestiario: il golem
    4169: "Minerale",            # 鉱物 — il jp dice «minerale», non «roccia»
    4238: "Zanan",               # ザナン — nome proprio
    4311: "Scheletro",           # 骸骨 — bestiario: lo scheletro
    4384: "Pedina",              # 駒
    4453: "Gatto",               # 猫 — bestiario: il gatto
    4521: "Cane",                # 犬 — bestiario: il cane
    4589: "Roran",               # ローラン — nome proprio
    4662: "Ratto",               # ねずみ — bestiario: il ratto
    4730: "Crostaceo",           # 甲殻
    4800: "Dio dei gatti",       # 猫の神
    4868: "Dio delle macchine",  # 機械の神
    4936: "Dio dei non morti",   # 死霊の神
    5003: "Macchina",            # 機械
    5073: "Fuoco fatuo",         # ウィスプ — bestiario: il fuoco fatuo
    5141: "Uccello",             # 鳥
    5209: "Mostro marino",       # 海魔
    5277: "Uomo bestia",         # ケモビト — «kemono-bito», non solo gatti
    5345: "Mutante",             # カオスシェイプ — bestiario: il mutante
    5417: "Yeek",                # イーク — nome proprio
    5485: "Yith",                # 異星主 — nome proprio (i Miti)
    5553: "Incarnazione",        # 神の化身 — l'avatar del dio, non un «servitore»
    5629: "Cavallo",             # 馬 — bestiario: il cavallo
    5697: "Dio",                 # 神
    5783: "Quickling",           # クイックリング — bestiario: il quickling
    5852: "Metallo",             # メタル
    5921: "Veicolo",             # 乗用機械
}


def main():
    voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding="utf-8") if l.strip()]
    per_riga = {v["riga"]: v for v in voci}

    guai = []
    for riga, resa in RESE.items():
        if riga not in per_riga:
            guai.append(f"la riga {riga} non sta nell'estrazione")
            continue
        if len(resa) > TETTO:
            guai.append(f"«{resa}» e' {len(resa)}, il tetto e' {TETTO}")
    # ogni voce corta dell'estrazione deve avere una resa
    for v in voci:
        if len(v["en"]) <= 80 and v["riga"] not in RESE:
            guai.append(f"la riga {v['riga']} ({v['en']}) non ha una resa")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("il tavolo non e' a posto: non scrivo niente")

    fuori = []
    for riga, resa in sorted(RESE.items()):
        d = dict(per_riga[riga])
        d["it"] = resa
        fuori.append(d)

    testo = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in fuori)
    io.open(USCITA, "w", encoding="utf-8", newline="").write(testo)
    print(f"{len(fuori)} voci in {USCITA}")
    print(f"la piu' lunga: {max(len(r) for r in RESE.values())} caratteri (tetto {TETTO})")


if __name__ == "__main__":
    main()
