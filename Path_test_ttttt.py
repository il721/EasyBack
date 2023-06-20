import shutil
from pathlib import Path

path = ['f:\\!_____back_1\\', 'f:\\!_____back_2\\', 'f:\\!_____back_3\\']
for item in path:
    for _ in Path.iterdir(Path(item)):
        print(*list(Path.iterdir(Path(item))), end='\n')
        if _.is_dir():
            shutil.rmtree(_)
        else:
            _.unlink()
