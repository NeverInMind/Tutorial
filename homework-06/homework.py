from normalize import normalize
from pathlib import Path

p = Path('.\Мотлох_1;№')
file_tree = [x for x in p.iterdir() if x.is_dir()]
for child in file_tree:
    file_tree2 = [x for x in child.iterdir() if x.is_dir()]
    print(file_tree2)
