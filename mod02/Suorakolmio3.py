kanna = input("Anna kolmion kanta: ")
korkeus = input("Anna kolmion korkeus: ")
pinta_ala = 0.5 * float(kanna) * float(korkeus)
piiri = float(kanna) + 2 * (float(korkeus) ** 2 + (float(kanna) / 2) ** 2) ** 0.5
print("Kolmion pinta-ala on:", pinta_ala, " ja kolmion piiri on:", piiri)