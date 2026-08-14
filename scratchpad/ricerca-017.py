# -*- coding: utf-8 -*-
"""Le ricerche nel dizionario che servono al lotto 017 (proc.hsp 15500-16999)."""
import glob
import io
import json

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it'):
            voci.append((nome, d.get('riga'), d.get('jp') or '', d.get('en') or '', d['it']))

DOMANDE = [
    ('乗り物 / vehicle', lambda jp, en, it: '乗り物' in jp or 'vehicle' in en.lower()),
    ('馬車 / carriage, 郊外 / suburb', lambda jp, en, it: '郊外' in jp or 'suburb' in en.lower() or 'carriage' in en.lower()),
    ('充填 / recharge, charge', lambda jp, en, it: '充填' in jp or 'recharg' in en.lower()),
    ('魔力の貯蓄 / mana charge', lambda jp, en, it: '魔力' in jp or 'mana charge' in en.lower()),
    ('金が足りない / not enough money', lambda jp, en, it: '金が足りない' in jp or 'enough money' in en.lower()),
    ('出航 / set sail, 保険 / insurance', lambda jp, en, it: '出航' in jp or '保険' in jp or 'set sail' in en.lower() or 'insurance' in en.lower()),
    ('海に面した街 / town by the sea', lambda jp, en, it: '海に面' in jp or 'town by the sea' in en.lower()),
    ('読む必要がある / need to read it', lambda jp, en, it: 'need to read it' in en.lower()),
    ('ストラックアウト / Struck Out', lambda jp, en, it: 'ストラックアウト' in jp or 'struck out' in en.lower()),
    ('スウォーム / Swarm', lambda jp, en, it: 'スウォーム' in jp or en.strip().lower().startswith('swarm')),
    ('地面を砕く / smash the ground', lambda jp, en, it: '地面' in jp or 'the ground' in en.lower()),
    ('破片 / debris', lambda jp, en, it: '破片' in jp or 'debris' in en.lower()),
    ('重力 / gravity', lambda jp, en, it: '重力' in jp or 'gravity' in en.lower()),
    ('隕石 / meteor', lambda jp, en, it: '隕石' in jp or 'meteor' in en.lower()),
    ('マナ / mana', lambda jp, en, it: 'マナ' in jp or 'mana' in en.lower()),
    ('目が眩む / dazzle, blind', lambda jp, en, it: '目が眩' in jp or 'dazzl' in en.lower()),
    ('変化 / change, polymorph', lambda jp, en, it: '変化した' in jp or '変容' in jp or 'metamorphos' in en.lower()),
    ('壁 / wall, 扉 / door', lambda jp, en, it: '扉が出現' in jp or '壁' in jp or 'a door appears' in en.lower() or 'a wall appears' in en.lower()),
    ('羽 / feather, 重く / heavy', lambda jp, en, it: '羽が生えた' in jp or 'as light as a feather' in en.lower() or 'becomes heavy' in en.lower()),
    ('黄金の光 / golden aura', lambda jp, en, it: '黄金の光' in jp or 'golden aura' in en.lower()),
    ('読書会 / reading party, どの本 / which book', lambda jp, en, it: '読書' in jp or 'which book' in en.lower() or 'reading party' in en.lower()),
    ('ひとりぼっち / all alone', lambda jp, en, it: 'ひとりぼっち' in jp or 'all alone' in en.lower()),
    ('繰り出した / blast, unleash', lambda jp, en, it: '繰り出' in jp or 'blast' in en.lower()),
    ('命中 / hits', lambda jp, en, it: '命中' in jp),
    ('解き放った / release', lambda jp, en, it: '解き放' in jp or 'released own' in en.lower()),
    ('抵抗した / resist', lambda jp, en, it: '抵抗した' in jp),
    ('崩壊 / break tissue', lambda jp, en, it: '体組織' in jp or '癒しの力' in jp or 'tissue' in en.lower()),
    ('投下 / drop something', lambda jp, en, it: '投下' in jp or 'drop' in en.lower() and 'something' in en.lower()),
]

for titolo, prova in DOMANDE:
    print('=' * 70)
    print('###', titolo)
    trovate = [v for v in voci if prova(v[2], v[3], v[4])]
    for nome, riga, jp, en, it in trovate[:14]:
        print(f'  {nome}:{riga}  jp={jp[:26]}  en={en[:40]}\n      -> {it[:88]}')
    if len(trovate) > 14:
        print(f'  ... e altre {len(trovate) - 14}')
    if not trovate:
        print('  (niente)')
