import sqlite3, os, query, viewer, controller,pages
# from rich.console import Console
# from rich.table import Table
# from pathlib import Path
choice=pages.page_main()
while True:
    choice=pages.pages_list[choice]()


















"""OLD CODE"""
# file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../DB"))
# desktop = Path.home() / "Desktop"
#
# mark_inpt = None
# connection = sqlite3.connect(file_path)
# console = Console()
#
# mrk_numbers = 1
# while True:
#     os.system('cls')
#     print("0 : открыть каталог")
#     print("1 : отфильтровать по марке")
#     print("5 : выйти")
#     inpt = int(input("введите вариант: "))
#     if inpt == 0:
#         os.system('cls')
#         response = connection.execute(query.filtr_marks(mark_inpt))
#         table = viewer.table_creator("Каталог", {"Марка": 0, "Цена": 1, "Пробег": 2, "Год": 3}, response)
#         console.print(table)
#         input()
#     if inpt == 5:
#         break
#     if inpt == 1:
#         os.system('cls')
#         print("0 : убрать фильтр")
#         print("1 : выбрать марку")
#         print("2 : показать фильтр")
#         insrt = int(input("введите вариант: "))
#         if insrt == 2:
#             if mark_inpt != None:
#                 mark_output = ', '.join(mark_inpt)
#                 print(f"выбраны: {mark_output}")
#             else:
#                 print("фильтры отключены")
#             input()
#         elif insrt == 1:
#
#             os.system('cls')
#             print("    --===--  ")
#             mrk_table = viewer.table_creator("Марки", {"№": 1, "Название": 0}, connection.execute(query.asking_marks()))
#             console.print(mrk_table)
#             print("    --===--  ")
#             mark_inpt = controller.smart_input()
#         elif insrt == 0:
#             mark_inpt = None
#
#         else:
#             print("введено неверное число")
#     else:
#         print("введено неверное число")
