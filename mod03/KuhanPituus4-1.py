kuhanPituus = int(input("Anna kuhan pituus (cm), kalastaja: "))
if kuhanPituus < 37:
    print("Kuhan pituus on liian pieni, se pitää päästää takaisin veteen.")
    print(f"Kuha pitäisi olla {37 - kuhanPituus} cm pidempi.")