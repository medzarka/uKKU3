
from pip._internal.operations import freeze
from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent
requirements_file = os.path.join(BASE_DIR, 'requirements.txt')

x = freeze.freeze()

print(f'Start writing the requirement file to {requirements_file}')
f = open(requirements_file, mode='w', encoding='iso-8859-1')
for p in x:
    f.write(f'{p}\n')
f.close()
print(f'Done.')