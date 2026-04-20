import sqlite3
from rich.console import Console
from rich.table import Table
mark_inpt=None
connection = sqlite3.connect("C:/base/DB")
console = Console()




while True:
    print("0 : открыть каталог")
    print("1 : отфильтровать по марке")
    print("5 : выйти")
    inpt = int(input())
    if inpt == 0:
        table = Table(title="Каталог")
        table.add_column("Марка")
        table.add_column("Цена")
        table.add_column("Пробег")
        table.add_column("Дата")
        response = connection.execute(f"""
        SELECT marka,price,probeg,date 
        FROM car
        WHERE car.marka = '{mark_inpt}'""")
        for i in response:
                table.add_row(i[0], str(i[1]), str(i[2]), str(i[3]))
        console.print(table)
    if inpt == 5:
        break
    if inpt == 1:
        mark_inpt=input("введите марку: ")

