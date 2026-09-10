Pitsa1Hinta = int(input("Anna pitsa 1 hinta: "))
Pitsa2Hinta = int(input("Anna pitsa 2 hinta: "))

Pitsan1Diametri = float(input("Anna pitsa 1 halkaisija: "))
Pitsan2Diametri = float(input("Anna pitsa 2 halkaisija: "))

def YksikkoHinta(hinta, halkaisija):
    pinta_ala = 3.14 * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta


yksikkohinta1 = YksikkoHinta(Pitsa1Hinta, Pitsan1Diametri)
yksikkohinta2 = YksikkoHinta(Pitsa2Hinta, Pitsan2Diametri)
if(yksikkohinta1 < yksikkohinta2):
    print("Pitsa 1 on edullisempi")
elif(yksikkohinta1 > yksikkohinta2):
    print("Pitsa 2 on edullisempi")
else:
    print("Pitsat ovat yhtä edullisia")