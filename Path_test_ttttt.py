from pathlib import Path

path = Path('f:\\!_____back_2\\')
if tuple(path.iterdir()):
    print("not empty")
else:
    print("empty")
