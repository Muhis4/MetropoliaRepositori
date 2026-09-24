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

    def Kulje(self, tunti):
        matka = self.nopeus * tunti
        self.kuljettuMatka += matka
        return

auto = Auto("ABC-123", 142, 0, 2000)

print(f"Uusi auto: rekisteritunnus: {auto.rekisteritunnus}, huippu nopeus: {auto.huippunopeus} km")

auto.Kiihdytä(60)

auto.Kulje(1.5)

print(f"Kuljettu matka: {auto.kuljettuMatka:.0f}")