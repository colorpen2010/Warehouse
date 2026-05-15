import os

def page_marks():
    os.system('cls')
    choices = {
        1: "page_choose_mark",
        3: "main"
    }
    print("opened_marks")
    print("0 : убрать фильтр *")
    print("1 : выбрать марку")
    print("2 : показать фильтр *")
    print("3 : вернуться назад")
    choice = int(input("введите число:"))
    return choices[choice]
