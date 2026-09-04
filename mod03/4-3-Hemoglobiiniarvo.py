sukupuoli = input("Anna sukupuoli (mies/nainen): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on liian korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

elif sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on liian korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")