import sqlite3, os,query,viewer
from rich.console import Console
from rich.table import Table
from pathlib import Path

file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../DB"))
desktop = Path.home() / "Desktop"

mark_inpt = None
connection = sqlite3.connect(file_path)
console = Console()

mrk_numbers = 1
while True:
    os.system('cls')
    print("0 : открыть каталог")
    print("1 : отфильтровать по марке")
    print("5 : выйти")
    inpt = int(input("введите вариант: "))
    if inpt == 0:
        os.system('cls')
        table=viewer.table_creator("Каталог",["Марка","Цена","Пробег","Год"])
        response = connection.execute(query.filtr_marks(mark_inpt))
        viewer.table_filler(response,table)
        # table.add_row(i[0], str(i[1]), str(i[2]), str(i[3]))
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
            mrk_table = viewer.table_creator("Марки",["№","Название"])
            os.system('cls')
            print("    --===--  ")
            mrk_numbers = 1
            for j in connection.execute(query.asking_marks()):
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
