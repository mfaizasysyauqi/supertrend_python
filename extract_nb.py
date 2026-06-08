import json

with open('supertrend_python.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

all_code = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        all_code.append(f'# === Cell {i} ===\n{src}')

full = '\n'.join(all_code)

with open('extracted_code.py', 'w', encoding='utf-8') as f:
    f.write(full)

print(f'Total code length: {len(full)} chars')
print(f'Total code lines: {len(full.splitlines())}')
print('Done writing extracted_code.py')
