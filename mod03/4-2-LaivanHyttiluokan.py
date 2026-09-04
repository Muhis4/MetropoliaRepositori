laivanHyttiluokan = input("Anna laivan hyttiluokka (LUX, A, B, C): ").upper()

if laivanHyttiluokan == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif laivanHyttiluokan == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laivanHyttiluokan == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laivanHyttiluokan == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")