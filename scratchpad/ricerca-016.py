# -*- coding: utf-8 -*-
"""Le ricerche nel dizionario che servono al lotto 016."""
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
    ('脱出 / escape', lambda jp, en, it: '脱出' in jp or 'escape' in en.lower()),
    ('帰還 / return', lambda jp, en, it: '帰還' in jp or 'return' in en.lower()),
    ('妹 / 姉 sister (creature)', lambda jp, en, it: 'sister' in en.lower() and len(en) < 40),
    ('執事 / butler, お嬢さん / lady', lambda jp, en, it: 'butler' in en.lower() or 'young lady' in en.lower()),
    ('ワンワン / Wrang', lambda jp, en, it: 'wrang' in en.lower() or 'foma' in en.lower()),
    ('銘 / name an artifact', lambda jp, en, it: '銘' in jp or 'called' in en.lower()),
    ('遺産 / inherit', lambda jp, en, it: '遺産' in jp or 'inherit' in en.lower()),
    ('霧/煙/蜘蛛の巣 (terreno)', lambda jp, en, it: any(x in jp for x in ('霧', '黒煙', '蜘蛛の巣', '火柱', '水溜'))),
    ('エーテル / ether', lambda jp, en, it: 'エーテル' in jp or 'ether' in en.lower()),
    ('この場所では効果がない', lambda jp, en, it: '効果がない' in jp or "doesn't work in this area" in en.lower()),
    ('マナが回復 / mana restored', lambda jp, en, it: 'マナが回復' in jp or 'mana is restored' in en.lower()),
    ('支配 / dominate', lambda jp, en, it: '支配' in jp or 'dominat' in en.lower()),
    ('再生成 / reconstruct', lambda jp, en, it: '再生成' in jp or 'reconstruct' in en.lower()),
]

for titolo, prova in DOMANDE:
    print('=' * 70)
    print('###', titolo)
    trovate = [v for v in voci if prova(v[2], v[3], v[4])]
    for nome, riga, jp, en, it in trovate[:12]:
        print(f'  {nome}:{riga}  jp={jp[:28]}  en={en[:42]}\n      -> {it[:84]}')
    if len(trovate) > 12:
        print(f'  ... e altre {len(trovate) - 12}')
    if not trovate:
        print('  (niente)')
