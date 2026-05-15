

def smart_input():
    inpt = input("введите марку: ")
    inpt = inpt.replace(',', ' ')
    inpt = inpt.split()
    return tuple(inpt)