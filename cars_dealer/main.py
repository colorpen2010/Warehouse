import sqlite3,os
from rich.console import Console
from rich.table import Table
from pathlib import Path

file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../DB"))
desktop = Path.home() / "Desktop"
print(file_path)
zagatovka="""
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
marks = []
mark_inpt = None
connection = sqlite3.connect(file_path)
console = Console()
strk = f"""
        SELECT marka,price,probeg,date 
        FROM car
        """
ask_strk = """
SELECT DISTINCT marka
FROM car
ORDER BY marka"""
# another_ask_strk="""
# SELECT  marka, COUNT (ID)
# FROM car
# GROUP BY marka
# ORDER BY car.marka"""
mrk_numbers = 1
while True:
    os.system('cls')
    print("0 : открыть каталог")
    print("1 : отфильтровать по марке")
    print("5 : выйти")
    inpt = int(input("введите вариант: "))
    if inpt == 0:
        os.system('cls')
        table = Table(title="Каталог")
        table.add_column("Марка")
        table.add_column("Цена")
        table.add_column("Пробег")
        table.add_column("Дата")
        if mark_inpt == None:
            response = connection.execute(strk)
        else:
            mark = f"(UPPER('{"'), UPPER('".join(mark_inpt)}'))"
            strk_addon = f"""WHERE UPPER(car.marka) IN {mark}"""
            print(strk + strk_addon)
            response = connection.execute(strk + strk_addon)
        for i in response:
            table.add_row(i[0], str(i[1]), str(i[2]), str(i[3]))
        console.print(table)
        input()
    if inpt == 5:
        break
    if inpt == 1:
        os.system('cls')
        print("0 : убрать фильтр")
        print("1 : выбрать марку")
        print("2 : показать фильтр")
        insrt = int(input("введите вариант: "))
        if insrt == 2:
            if mark_inpt != None:
                mark_output = ', '.join(mark_inpt)
                print(f"выбраны: {mark_output}")
            else:
                print("фильтры отключены")
            input()
        elif insrt == 1:
            mrk_table = Table(title="Марки")
            mrk_table.add_column("№")
            mrk_table.add_column("Название")
            os.system('cls')
            print("    --===--  ")
            mrk_numbers = 1
            for j in connection.execute(ask_strk):
                mrk_table.add_row(str(mrk_numbers), str(j[0]))
                mrk_numbers += 1
            console.print(mrk_table)
            print("    --===--  ")
            mark_inpt = input("введите марку: ")
            mark_inpt = mark_inpt.replace(',', ' ')
            mark_inpt = mark_inpt.split()
            mark_inpt = tuple(mark_inpt)
        elif insrt == 0:
            mark_inpt = None

        else:
            print("введено неверное число")
    else:
        print("введено неверное число")
