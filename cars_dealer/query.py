def filtr_marks(mark_inpt):
    strk = f"""
        SELECT marka,price,probeg,date 
        FROM car
        """
    if mark_inpt == None:
        return strk
    else:
        mark = f"(UPPER('{"'), UPPER('".join(mark_inpt)}'))"
        strk_addon = f"""WHERE UPPER(car.marka) IN {mark}"""
        return strk + strk_addon


def asking_marks():
    ask_strk = """
        SELECT DISTINCT marka,
ROW_NUMBER() OVER (ORDER BY marka) AS num
FROM (
SELECT DISTINCT marka
FROM car
ORDER BY marka
)
ORDER BY marka"""
    return ask_strk

# another_ask_strk="""
# SELECT marka, COUNT (ID)
# FROM car
# GROUP BY marka
# ORDER BY car.marka"""

zagatovka = """
import os
from pathlib import Path
from win32com.client import Dispatch

# путь к рабочему столу
desktop = Path.home() / "Desktop"

# путь к твоему скрипту
target = Path(__file__).resolve()

# путь к ярлыку
shortcut_path = desktop / "MyProgram.lnk"

# создаём ярлык
shell = Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(str(shortcut_path))

shortcut.Targetpath = "python"  # что запускаем
shortcut.Arguments = f'"{target}"'  # аргумент — путь к скрипту
shortcut.WorkingDirectory = str(target.parent)
shortcut.IconLocation = "python.exe"  # иконка (можно поменять)

shortcut.save()

print("Ярлык создан:", shortcut_path)"""
