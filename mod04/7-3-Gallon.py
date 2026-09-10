def muunna(gallonit):
    litrat = gallonit * 3.785
    return litrat

while(True):
    gallonit = float(input("Anna gallonit: "))
    if(gallonit < 0):
        break
    litrat = muunna(gallonit)
    print(gallonit, "gallonit on", litrat, "litraa")