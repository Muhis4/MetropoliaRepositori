biggest = 0
smallest = 0
while True:
    number = input("Anna luku: ")
    if number == "":
        print(f"Suurin luku: {biggest}")
        print(f"Pienin luku: {smallest}")
        break
    elif  biggest < int(number):
        biggest = int(number)
    elif int(number) < smallest or smallest == 0:
        smallest = int(number)