import random

def heitto():
    return random.randint(1, 6)

while True:
    tulos = heitto()
    print(tulos)
    if(tulos == 6):
        break