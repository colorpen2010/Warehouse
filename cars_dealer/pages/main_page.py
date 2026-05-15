import os
def page_main():
    os.system('cls')
    choices={
        0:"catalog",
        1:"marks"
    }
    print("0 : открыть каталог")
    print("1 : отфильтровать по марке")
    print("2 : выйти")
    choice = int(input("введите число:"))
    return choices[choice]
