import sqlite3,rich
import time

connection = sqlite3.connect("C:/base/DB")

while True:
    print("enter: 1 to add new material")
    print("enter: 2 to open material list")
    print("enter: 3 to delete material")
    print("enter 0 to stop program")
    choose = float(input("choose: "))
    if choose == 0:
        break
    elif choose == 1:
        name = input("enter name: ")
        radioactivity = input("enter radioactivity (0/1): ")
        count = int(input("enter count: "))
        for i in range(count + 1):
            bar = "#" * i + "-" * (count - i)
            print(f"\r[{bar}] {i}/{count}", end="")
            print("\n")
            time.sleep(0.1)
        connection.execute(
            f"""
            INSERT INTO material (name,radioactivity,count) 
            VALUES ("{name}",{radioactivity},{count});""")
        connection.commit()
    elif choose == 2:
        response = connection.execute("""SELECT * 
        FROM material""")
        for i in response:
            print(i)
    elif choose == 3:
        choosen_one = input("enter id (if you wanna pass enter any letter): ")
        if choosen_one.isnumeric():
            connection.execute(f"""
                    DELETE FROM material
                    WHERE material.ID = {choosen_one}""")
