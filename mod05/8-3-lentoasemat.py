lentoasemat = {}

while True:
    command = int(input("Haluatko syöttää uuden lentoaseman, hakea jo olevan, tai lopettaa? (1-3)"))
    if(command == 3):
        break

    elif(command == 1):
        ICAO = input("Anna ICAO-koodi: ")
        name = input("Anna lentoaseman nimi: ")
        lentoasemat[ICAO] = name
    elif(command == 2):
        for lentoasema in lentoasemat:
            print(f"ICAO: {lentoasema}, nimi: {lentoasemat[lentoasema]}")