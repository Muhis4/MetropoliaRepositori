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

class SahkoAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettuMatka=0, kWh=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettuMatka)
        self.kWh = kWh

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettuMatka=0, bensatanki=0):
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettuMatka)
        self.bensatanki = bensatanki

PAuto = Polttomoottoriauto("ABC-123", 120, 0, 0, 50)
SAuto = SahkoAuto("ABC-228", 90, 0, 0, 52)

PAuto.Kiihdytä(110)
SAuto.Kiihdytä(85)

PAuto.Kulje(4)
SAuto.Kulje(4)

print(PAuto.kuljettuMatka)
print(SAuto.kuljettuMatka)