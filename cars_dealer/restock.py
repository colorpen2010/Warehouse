import random, sqlite3, time
connection = sqlite3.connect("C:/base/DB")
"""
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
"""
def restock():
    connection.execute(f'DELETE FROM car')
    for i in range(1000):
        date = random.randint(1957, 2026)
        marka = random.choice(["Toyota","Audi","BMW","Fiat","Tesla"])
        probeg = random.randint(0, 400)
        price = random.randint(1000, 10000)
        connection.execute(f'INSERT INTO car (date,marka,probeg,price) \n VALUES ({date},"{marka}",{probeg},{price});')
    connection.commit()
while True:
    restock()
    break