class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettuMatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettuMatka = kuljettuMatka

auto = Auto("ABC-123", "142 km/h")

print(f"Uusi auto: rekisteritunnus: {auto.rekisteritunnus}, huippu nopeus: {auto.huippunopeus}")