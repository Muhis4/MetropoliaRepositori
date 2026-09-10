import random

max = int(input("Anna nopan silmäluku: "))
def heitto():
    return random.randint(1, max)

while True:
    tulos = heitto()
    print(tulos)
    if(tulos == max):
        break