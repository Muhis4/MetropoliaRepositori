tunnus = "Python"
salasana = "rules"
attempts = 5

print("Tervetuloa.")

while attempts > 0:
    inputTunnus = input("Anna tunnus: ")
    inputSalasana = input("Anna salasana: ")

    if(inputTunnus != tunnus or inputSalasana != salasana):
        attempts -= 1
        print(f"Väärin. Kokeile uudestaan. Attempts left {attempts}")
    else:
        break

if(attempts <= 0 ):
    print("Pääsy evätty.")