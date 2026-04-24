import sqlite3
from rich.console import Console
from rich.table import Table

mark_inpt = None
connection = sqlite3.connect("..\\DB")
console = Console()
strk = f"""
        SELECT marka,price,probeg,date 
        FROM car
        """

while True:
    print("0 : открыть каталог")
    print("1 : отфильтровать по марке")
    print("5 : выйти")
    inpt = int(input("введите вариант: "))
    if inpt == 0:
        table = Table(title="Каталог")
        table.add_column("Марка")
        table.add_column("Цена")
        table.add_column("Пробег")
        table.add_column("Дата")
        if mark_inpt == None:
            response = connection.execute(strk)
        else:
            strk_addon = f"""WHERE car.marka IN '{mark_inpt}'"""
            response = connection.execute(strk + strk_addon)
        for i in response:
            table.add_row(i[0], str(i[1]), str(i[2]), str(i[3]))
        console.print(table)
    if inpt == 5:
        break
    if inpt == 1:
        print("0 : убрать фильтр")
        print("1 : выбрать марку")
        insrt = int(input("введите вариант: "))
        if insrt == 1:
            mark_inpt = input("введите марку: ")
        elif insrt == 0:
            mark_inpt = None
            if ' ' in mark_inpt:
                ','.
        else:
            print("введено неверное число")
    else:
        print("введено неверное число")
