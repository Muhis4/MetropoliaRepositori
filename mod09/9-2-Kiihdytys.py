class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettuMatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettuMatka = kuljettuMatka

    def Kiihdytä(self, Uusinopeus = 0):
        if self.nopeus + Uusinopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
            return
        elif(self.nopeus + Uusinopeus < 0):
            self.nopeus = 0
            return

        self.nopeus += Uusinopeus

auto = Auto("ABC-123", 142)

print(f"Uusi auto: rekisteritunnus: {auto.rekisteritunnus}, huippu nopeus: {auto.huippunopeus} km")

auto.Kiihdytä(30)
print(f"Nopeus: {auto.nopeus} km")

auto.Kiihdytä(70)
print(f"Nopeus: {auto.nopeus} km")

auto.Kiihdytä(50)
print(f"Nopeus: {auto.nopeus} km")

auto.Kiihdytä(-200)
print(f"Nopeus: {auto.nopeus} km")