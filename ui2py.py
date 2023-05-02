from pathlib import Path
import os


def all_ui_grc_to_py(path_in: str, extension: str) -> None:
    """
    Convert all .ui (if extension in parameters == 'ui') and .qrc (... =='qrc') in .py files.
    All .ui and .qrc files must be in [path_in] SUB(!)folder.
    .py files exist in the same ui2py.py folder.
    Of coгrce, Pyside lib  with pyside6-rcc and pyside6-uic must be installed

    Sample:
        all_ui_grc_to_py(ui, 'ui')
        all_ui_grc_to_py(ui, 'qrc')

        [root]
            ui
                [name_01].ui
                [name_02].qrc
            ui2py.py
            [name_01].py    <--- after run
            [name_02].py    <--- after run
    """
    path = Path(f'./{path_in}')
    ext = f"*.{extension}"
    if extension == 'ui':
        command = 'pyside6-uic'
    else:
        command = 'pyside6-rcc'
    out_list = list(path.glob(ext))
    # print(out_list)
    for item in out_list:
        cmd = f"{command} {item.absolute()} -o {item.name.split('.')[0]}.py"
        in_file = cmd.split('\\')[-1].split()[0]
        out_file = cmd.split('\\')[-1].split()[-1]
        print(f'{in_file} --> {out_file}', end='\n')
        os.popen(cmd)


if __name__ == '__main__':
    ui_grc_path = 'ui'
    all_ui_grc_to_py(ui_grc_path, 'ui')
    all_ui_grc_to_py(ui_grc_path, 'qrc')
