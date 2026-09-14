nimet = set()
while True:
    uusiNimi = input("Anna nimi: ")
    if uusiNimi == "":
        break
    elif(uusiNimi in nimet):
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(uusiNimi)

for nimi in nimet:
    print(nimi)