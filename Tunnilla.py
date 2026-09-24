while True:
    try:

        Luku = int(input("Anna luku: "))
        print("Good job.")
        break
    except ValueError as aiti:
        print(aiti)