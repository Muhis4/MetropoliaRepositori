while True:
    amount = int(input("Anna määrä: "))
    if amount < -0:
        print("Määrän on negatiivinen. BREAK!")
        break
    print(f"{amount} tuumaa = {amount * 2.54} cm.") 