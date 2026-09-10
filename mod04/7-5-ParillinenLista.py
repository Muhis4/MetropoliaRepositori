lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def ParillinenLista():
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

print(ParillinenLista())