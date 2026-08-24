print("Anna leiviskit, naulat ja luodit.")
leiviskat = input("Leiviskät: ")
naulat = input("Naulat: ")
luodit = input("Luodit: ")

luodin_paino = 13.3
naulan_paino = luodin_paino * 32
leiviskan_paino = naulan_paino * 20

massaGrammeina = float(leiviskat) * leiviskan_paino + float(naulat) * naulan_paino + float(luodit) * luodin_paino

kiloGrammeina = massaGrammeina / 1000
print("Massa on:", int(kiloGrammeina), "kg ja", massaGrammeina % 1000, "g.")