import os
import shutil
import stat
from pathlib import Path

import win32con
import win32security
import win32api

path_src = 'f:\\!___GD\\BackUp_BIG\\Adobe\\AI'
path_dst = 'f:\\!_____back_1\\'
path = 'f:\\!_____back_1\\'


# path = ['f:\\!_____back_1\\', 'f:\\!_____back_2\\', 'f:\\!_____back_3\\']

def copy_dir():
    shutil.copytree(path_src, path_dst, dirs_exist_ok=True)


# def rmtree_error(func, path_err, exc_info):
#     # path_err contains the path_err of the file that couldn't be removed
#     # let's just assume that it's read-only and unlink it.
#     os.chmod(path_err, stat.S_IWRITE)
#     os.unlink(path_err)
def rmtree_error(func, path_err, exc_info):
    # path_err contains the path_err of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    print(path_err)
    print(stat.filemode(os.stat(path_err)[0]))
    file_attr = win32api.GetFileAttributes(path_err)
    print(file_attr)
    # win32api.SetFileAttributes(path_err, win32con.FILE_ATTRIBUTE_NORMAL)
    os.chmod(path_err, stat.S_IWRITE)
    os.unlink(path_err)


def del_all():
    # print(list(Path.iterdir(Path(path))))
    for _ in Path.iterdir(Path(path)):

        if _.is_dir():
            # os.chmod(_, stat.S_IWRITE)
            shutil.rmtree(_, ignore_errors=False, onerror=rmtree_error)
            # try:
            #     shutil.rmtree(_, ignore_errors=False)
            # except PermissionError:
            #     rez = os.stat(_)
            #     print(_)
            #     print(stat.filemode(rez[0]))
            #     os.chmod(_, stat.S_IWRITE)
            #     # print(stat.filemode(rez[0]))
        else:
            try:
                _.unlink()
            except PermissionError:
                print('PERMISSION ERROR!')
                os.chmod(_, stat.S_IWRITE)
                os.unlink(_)


# copy_dir()
del_all()

# os.chmod("f:\\!_____back_1\\rrr", stat.S_IREAD)

# for item in path:
#     for _ in Path.iterdir(Path(item)):
#         print(*list(Path.iterdir(Path(item))), end='\n')
#         if _.is_dir():
#             shutil.rmtree(_)
#         else:
#             _.unlink()
