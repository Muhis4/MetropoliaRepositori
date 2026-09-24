class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def TulostaTiedot(self):
        print(f"Nimi: {self.nimi}.\nKirjoittaja: {self.kirjoittaja}.\nSivumäärä: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def TulostaTiedot(self):
        print(f"Nimi: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")

kirja = Kirja("Toy Story", "Patrick Payman", 250)
lehti = Lehti("Brand New News", "Some Important Guy")

kirja.TulostaTiedot()
lehti.TulostaTiedot()