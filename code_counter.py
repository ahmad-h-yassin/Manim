import os
import json

total_lines = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ipynb'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    notebook = json.load(f)
                    for cell in notebook['cells']:
                        if cell['cell_type'] == 'code':
                            total_lines += len(cell['source'])
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total lines of code: {total_lines}")
