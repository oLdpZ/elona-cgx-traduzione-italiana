import io, json
v = [json.loads(l) for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
for x in v:
    if x.get('file') == 'command.hsp' and '2954' in (x.get('motivo') or ''):
        print(repr(x['en']), '|', x['firma'][:12], '|', x['rinviata_a'])
print('---')
for x in v:
    if x.get('file') == 'command.hsp' and '2954' in (x.get('motivo') or ''):
        print('MOTIVO:', x['motivo'])
        break
