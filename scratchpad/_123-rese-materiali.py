# -*- coding: utf-8 -*-
"""123a - Le rese di `material_data.hsp`: i 59 materiali, nome e descrizione.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-rese-materiali.py \
        --lotto lavoro/fase6-material_data-001.jsonl

Legge `scratchpad/_123-material_data.jsonl` (l'estrazione), ci scrive dentro le
rese e produce il lotto da dare a `strumenti.reimporta`.

⚠️⚠️⚠️ **VENTISETTE NOMI SU CINQUANTANOVE ERANO GIA' DECISI**, e non nel
dizionario: in `glossario.md`, in una tabella scritta da una sessione che aveva
incontrato gli stessi nomi **dentro una frase** di `command.hsp` e aveva
previsto che questo file un giorno si sarebbe aperto. Ogni riga porta il numero
di riga di `material_data.hsp`.

⭐ **Tre delle rese scritte a mano prima di leggerla erano sbagliate:**

    :249  Pebble             «sasso»                -> **pietruzza**
    :179  Sap of Yaggdrasil  «linfa dell'albero del mondo» -> **linfa di Yaggdrasil**
    :119  Element fragment   «pietra tagliavento»   -> **scheggia elementale**

⚠️⚠️ L'ultima e' la piu' istruttiva: il giapponese dice 風切石, «pietra che
taglia il vento», e ragionando dal giapponese si arriva a «pietra tagliavento»
— che e' la lettura giusta della fonte e la **decisione sbagliata**. Il
glossario spiega perche': la costante e' `MATERIAL_ELEMENT_FRAGMENT` e nel gioco
ci sono altre quattro schegge (etere, mithril, ferro, memoria, magia). E' la
formula della 42a — **la coerenza batte il giapponese** — ed e' l'unico dei
ventisette in cui le due lingue non dicono la stessa cosa.

⭐ E' la regola che nessuna rete sa far rispettare: `glossario.md` e
`invariati.md` sono prosa, e i cancelli del lotto non li aprono. Qui il costo
di non averlo letto sarebbe stato di tre nomi su cinquantanove, tutti e tre
plausibili.

ⓘ I trentadue restanti si decidono qui, dal giapponese, e la tabella del
glossario va estesa a cinquantanove in chiusura.
"""
import argparse
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
ESTRAZIONE = os.path.join(QUI, '_123-material_data.jsonl')

# ⭐ I VENTISETTE DEL GLOSSARIO. Copiati da `glossario.md`, non ricordati:
#   la riga accanto e' quella che il glossario stesso porta.
GLOSSARIO = {
    249: 'pietruzza',
    269: 'pietra pregiata',
    49: 'scheggia di etere',
    119: 'scheggia elementale',      # ⚠️ NON «pietra tagliavento»: coerenza > jp
    264: 'pietra del caos',
    34: "goccia d'acqua",
    134: 'acqua calda',
    109: 'neve',
    64: 'lacrima di strega',
    59: "lacrima d'angelo",
    39: 'bastone',
    239: 'ramo',
    94: 'erba sacra',
    154: 'erba lucente',
    179: 'linfa di Yaggdrasil',      # ⚠️ la storpiatura del canone, non Yggdrasil
    164: 'gene umano',
    104: 'gene di troll',
    99: 'coda di coniglio',
    169: 'occhio di strega',
    114: 'polvere di fata',
    234: 'pezza di stoffa',
    224: 'carta',
    199: 'pazzo urlante',
    189: 'inchiostro magico',
    159: 'massa magica',
    229: 'macchina generatrice',
    124: 'elettricità',
}

# I TRENTADUE NOMI NUOVI, decisi dal giapponese.
NOMI = {
    9: 'scarti',                     # クズ — non «cianfrusaglia», che e' l'OGGETTO junk
    14: 'fiche da casinò',           # カジノチップ — invariabile al plurale
    19: 'carbone',                   # 炭
    24: 'legno di deriva',           # 流木
    29: "penna d'uccello",           # 鳥の羽
    44: 'scheggia di mithril',       # ミスリルの欠片 — mithril e' invariato (dizionario)
    54: 'scheggia di ferro',         # 鉄の欠片
    69: 'acqua di mare',             # 海水
    74: 'erba che geme',             # 唸る草
    79: 'erba rossa',                # 赤い草
    84: 'erba azzurra',              # 青い草
    89: 'erba della maledizione',    # 呪いの草
    129: 'nebbia nera',              # 黒い霧
    139: 'pietra di fuoco',          # 火炎石
    144: 'pietra di ghiaccio',       # 冷凍石
    149: 'pietra elettrica',         # 帯電石
    174: 'cuoio',                    # 革
    184: 'carta magica',             # 魔法の紙
    194: 'bastone storto',           # 曲がった杖 — «bastone» dal glossario, :39
    204: "coda d'orso",              # クマの尻尾 — come «coda di coniglio», :99
    209: 'moneta da 100 yen',        # 100Yen硬貨
    214: 'moneta da 500 yen',        # 500Yen硬貨
    219: 'erba medicinale',          # 薬草
    244: 'ramo robusto',             # 頑丈な枝 — «ramo» dal glossario, :239
    254: 'scheggia di memoria',      # 記憶の欠片
    259: 'scheggia di forza magica', # 魔力の欠片
    274: 'liana',                    # ⚠️ ツル e' la LIANA, non la vena: «Vein» e' un refuso di monte per «Vine»
    279: 'colla',                    # 接着剤
    284: 'carta di qualità',         # 上質紙 — «carta» dal glossario, :224
    289: 'stoffa resistente',        # 丈夫な布
    294: 'tronco',                   # 丸太
    299: 'erba bianca',              # 白い草
}

# LE CINQUANTANOVE DESCRIZIONI. Vanno nella colonna stretta del pannello
# (`material.hsp:460`, da wx+308 in un riquadro largo 490 da wx+70): si tengono
# corte. ⚠️ Il budget in caratteri NON e' misurato — va tarato su uno
# screenshot, come vuole la lezione della 112a.
DESCRIZIONI = {
    10: 'Scarti che non valgono niente.',        # 何の価値もないクズ
    15: 'Fiche che si usano al casinò.',         # カジノで使うチップ
    20: 'Carbone di buona qualità.',             # 良質な炭
    25: 'Legname di qualità scadente.',          # ⚠️ jp: あまり質の良くない木材. EN dice «Common driftwood»
    30: "Una penna d'uccello comune.",           # 普通の鳥の羽
    35: "Una goccia d'acqua.",                   # 水滴 — il jp ripete il nome
    40: 'Un pezzo di legno di forma insolita.',  # ⚠️ jp: 杖, che ripete il nome. Qui la fonte e' l'inglese
    45: 'Scheggia di minerale con mithril.',     # ミスリルを含んだ鉱石の欠片
    50: "Scheggia di minerale con etere.",       # エーテルを含んだ鉱石の欠片
    55: 'Scheggia di minerale con ferro.',       # 鉄分を含んだ鉱石の欠片
    60: 'Una lacrima di strano splendore.',      # ⚠️ jp: 不思議な輝きを放つ涙. EN dice «Hard to gather»
    65: 'Una lacrima che non si asciuga mai.',   # 決して乾かない涙
    70: 'Acqua salata.',                         # しょっぱい水
    75: 'Un\'erba che fa un suono strano.',      # 変な音を出す草
    80: "Un'erba appena rossastra.",             # ほんのり赤い草
    85: "Un'erba appena azzurrina.",             # ほんのり青い草
    90: "Un'erba maledetta.",                    # 呪われた草
    95: "Un'erba benedetta.",                    # 祝福された草
    100: 'Una coda che porta fortuna.',          # 幸運を呼ぶ尻尾
    105: 'Un gene che si rigenera.',             # 再生する遺伝子
    110: 'Chissà perché non si scioglie.',       # なぜか溶けない
    115: 'La polvere che lasciano le fate.',     # 妖精の燐粉
    120: 'Una strana pietra che taglia il vento.',  # ⚠️ jp: 風を裂く不思議な石. Il NOME e' «scheggia
                                                 #   elementale» per coerenza, ma la DESCRIZIONE
                                                 #   puo' dire quel che dice il giapponese
    125: 'Sta scaricando.',                      # 放電している
    130: 'Una nebbia nerissima.',                # 真っ黒な霧
    135: 'Chissà perché non si raffredda.',      # なぜか冷めない
    140: 'Una pietra che porta calore.',         # 熱を帯びた石
    145: 'Una pietra fredda.',                   # 冷たい石
    150: 'Una pietra che porta elettricità.',    # 電気を帯びた石
    155: "Un'erba che risplende.",               # 光輝く草
    160: 'Un blocco di forza magica ignota.',    # 謎の魔力の塊 — 魔力 «forza magica» (dizionario)
    165: 'Un gene comune.',                      # 普通の遺伝子
    170: 'Si muovono ancora.',                   # まだ動いている — l'inglese ha il plurale, il jp no
    175: 'Pelle conciata.',                      # なめした皮
    180: 'Una linfa che guarisce ogni ferita.',  # ⚠️ jp: どんな傷も癒す樹液. EN dice «It's pretty rare»
    185: 'Carta che cela forza magica.',         # 魔力を秘めた紙
    190: 'Inchiostro che cela forza magica.',    # ⚠️ jp: 魔力を秘めたインク. EN dice «Wizards love to use it»
    195: 'Non fa il suo mestiere di bastone.',   # 杖の役割を果たさない
    200: 'Non sta mai zitto.',                   # 黙らない
    205: 'Molto corta.',                         # とても短い
    210: 'Denaro di un paese straniero.',        # 異国のお金
    215: 'Denaro di un paese straniero.',        # 異国のお金 — ⚠️ IDENTICA a :210, e va tenuta identica
    220: 'Guarisce un poco le ferite.',          # 少し傷を癒す
    225: 'Carta bianca.',                        # 白紙
    230: 'Una macchina che produce qualcosa.',   # 何かを生み出す機械
    235: 'Solo una pezza di stoffa.',            # ただの布きれ
    240: 'Spezzato da un albero.',               # ⚠️ jp: 枝, che ripete il nome. Fonte: l'inglese
    245: 'Non si spezza facilmente.',            # なかなか折れない
    250: 'Se ne trovano dappertutto.',           # どこにでも落ちている
    255: 'Ci sono rimasti dei ricordi.',         # 思い出が残っている
    260: 'Ci è racchiusa forza magica.',         # 魔力が込められている
    265: 'Una pietra che sigilla la forza del caos.',  # 混沌の力が封じられた石
    270: 'Una pietra in buono stato.',           # 状態の良い石
    275: 'Una liana.',                           # ツル — il jp ripete il nome
    280: 'È tutta appiccicosa.',                 # ネトネトしている
    285: 'Carta piacevole al tatto.',            # 手触りのよい紙
    290: 'Non si straccia.',                     # 裂けない
    295: 'Di grossezza maneggevole.',            # 手ごろな太さ
    300: "Un'erba biancastra.",                  # 白っぽい草
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lotto', required=True)
    scelte = ap.parse_args()

    rese = {}
    rese.update(GLOSSARIO)
    rese.update(NOMI)
    rese.update(DESCRIZIONI)

    voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]

    mancanti, scritte = [], 0
    fuori = sorted(set(rese) - {v['riga'] for v in voci})
    for v in voci:
        resa = rese.get(v['riga'])
        if not resa:
            mancanti.append((v['riga'], v['en']))
            continue
        v['it'] = resa
        scritte += 1

    with io.open(scelte.lotto, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            if v.get('it'):
                f.write(json.dumps(v, ensure_ascii=False) + '\n')

    print()
    print('  voci estratte      : %d' % len(voci))
    print('  rese scritte       : %d  (%d dal glossario, %d nomi nuovi, %d descrizioni)'
          % (scritte, len(GLOSSARIO), len(NOMI), len(DESCRIZIONI)))
    print('  ⚠️ senza resa      : %d   (atteso 0)' % len(mancanti))
    for riga, en in mancanti:
        print('       :%-6d %s' % (riga, en))
    print('  ⚠️ rese senza riga : %d   (atteso 0 — una chiave che non esiste' % len(fuori))
    print('                          nel file e\' una resa che non arriva)')
    for riga in fuori:
        print('       :%d' % riga)
    print()
    print('  lotto: %s' % scelte.lotto)
    print()
    return 1 if (mancanti or fuori) else 0


if __name__ == '__main__':
    sys.exit(main())
