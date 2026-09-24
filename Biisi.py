import Playlist

class Biisi:
    def __init__(self, laulaja, nimi):
        self.laulaja = laulaja
        self.nimi = nimi

b1 = Biisi("Arnold", "Rembo")
b2 = Biisi("Rameo", "Lover")
b3 = Biisi("Cool Band", "Monster")

biisit = [b1, b2, b3]

class Playlist:
    def __init__(self):
        self.playlist = []

    def AddMusic(self, music):
        self.playlist.append(music)

playL = Playlist()

playL.AddMusic(biisit)