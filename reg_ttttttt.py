import winreg

KEY = winreg.HKEY_LOCAL_MACHINE
REG_PATH: str = r'SOFTWARE\EasyBack'


def create_key(key, subkey):
    try:
        rez = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
    except FileNotFoundError:
        winreg.CreateKey(key, subkey)
        rez = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(rez, 'settings', 0, winreg.REG_SZ, 'exist')
    print(rez)
    winreg.CloseKey(rez)


def delete_key():
    pass


create_key(KEY, REG_PATH)
