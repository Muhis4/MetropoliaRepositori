import random

correctNumber = random.randint(1, 10)

while True:
    numb = int(input("Arvaa numero: "))
    if(numb == correctNumber):
        print("Oikein!")
        break 
    if(numb < correctNumber):
        print("Liian pieni arvaus.")
    elif(numb > correctNumber):
        print("Liian iso arvaus.")