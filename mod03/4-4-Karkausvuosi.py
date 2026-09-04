vuosi = input("Anna vuosi: ")
if(int(vuosi) % 4 == 0 and int(vuosi) % 100 != 0) or (int(vuosi) % 400 == 0):
    print(f"{vuosi} on karkausvuosi.")