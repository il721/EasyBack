import os
import shutil
import stat
from pathlib import Path

import win32api

path_src = 'c:\\Users\\il720506\\AppData\\Roaming\\Adobe\\Adobe Illustrator 27 Settings\\'
path_dst = 'f:\\!_____back_1\\'
path = 'f:\\!_____back_1\\'
path_list = ['f:\\!_____back_1\\', 'f:\\!_____back_2\\', 'f:\\!_____back_3\\']


# path = ['f:\\!_____back_1\\', 'f:\\!_____back_2\\', 'f:\\!_____back_3\\']

def copy_dir():
    shutil.copytree(path_src, path_dst, dirs_exist_ok=True)


def rmtree_error(func, path_err, exc_info):
    print(func, path_err, exc_info, sep='\n')
    os.chmod(path_err, stat.S_IWRITE)
    os.unlink(path_err)


def del_all():
    # print(list(Path.iterdir(Path(path))))
    for _ in Path.iterdir(Path(path)):

        if _.is_dir():
            try:
                shutil.rmtree(_, ignore_errors=False, onerror=rmtree_error)
            except PermissionError:
                rez = os.stat(_)
                print(_)
                print(stat.filemode(rez[0]))
                os.chmod(_, stat.S_IWRITE)
                # print(stat.filemode(rez[0]))
        else:
            try:
                _.unlink()
            except PermissionError:
                print('PERMISSION ERROR!')
                os.chmod(_, stat.S_IWRITE)
                os.unlink(_)


def del_from_os(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.chmod(name, stat.S_IWRITE)
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


# copy_dir()
# del_all()

# os.chmod("f:\\!_____back_1\\rrr", stat.S_IREAD)

for item in path_list:
    for _ in Path.iterdir(Path(item)):
        print(*list(Path.iterdir(Path(item))), end='\n')
        if _.is_dir():
            shutil.rmtree(_)
        else:
            _.unlink()

# shutil.rmtree('f:\\!_____back_1\\SETTINGS\\')
