import winreg

KEY = winreg.HKEY_LOCAL_MACHINE
SUBKEY_PATH: str = r'SOFTWARE\EasyBack'
KEY_NAME: str = 'settings_path'
KEY_VALUE: str = r'f:\!_____back_test\SETTINGS'


def create_key(key, subkey: str, name: str, value: str) -> None:
    try:
        rez = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
    except FileNotFoundError:
        winreg.CreateKey(key, subkey)
        rez = winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(rez, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(rez)


def delete_key(key, subkey: str) -> None:
    winreg.DeleteKey(key, subkey)
    # print(f"key HKEY_LOCAL_MACHINE\\{subkey}{KEY_NAME} was deleted from regitry")


create_key(KEY, SUBKEY_PATH, KEY_NAME, KEY_VALUE)
# delete_key(KEY, SUBKEY_PATH)
