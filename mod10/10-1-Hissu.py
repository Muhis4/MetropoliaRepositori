class Hissi:
    def __init__(self):
        self.kerros = 0

    def KerrosYlos(self):
        self.kerros += 1

    def KerrosAlas(self):
        self.kerros -= 1

    def SiirryKerrokseen(self, kerros=0):
        while self.kerros != kerros:
            if(kerros > self.kerros):
                self.KerrosYlos()
            elif(kerros < self.kerros):
                self.KerrosAlas()
            print(f"Nykyinen kerros: {self.kerros}")

hissi = Hissi()

hissi.SiirryKerrokseen(5)