

class Media:
    def __init__(self, titel):
        self.titel = titel


class Bok(Media):
    def __init__(self, titel, antal_sidor):
        super().__init__(titel)
        self.antal_sidor = antal_sidor


class Ljudspår(Media):
    def __init__(self, titel, speltid):
        super().__init__(titel)
        self.speltid = speltid


class Film(Ljudspår):
    def __init__(self, titel, speltid, upplösning):
        super().__init__(titel, speltid)
        self.upplösning = upplösning


b = Bok("Bröderna Karamazov", 840)
print(b.titel)
print(b.antal_sidor)

if isinstance(b, Media) and isinstance(b, Bok):
    print("b är samtidigt av typen Media och Bok")

f = Film("De sju samurajerna", "3:27:02", "1080")
print(f.titel)
print(f.speltid)
print(f.upplösning)

if isinstance(f, Media) and isinstance(f, Ljudspår) and isinstance(f, Film):
    print("f är samtidigt av typen Media, Ljudspår och Film")

l = Ljudspår("beat it", "3:45")
print(l.titel)
print(l.speltid)

if isinstance(l, Media) and isinstance(l, Ljudspår):
    print("l är samtidigt av typen Media, bok och Ljudspår")


def click_handler(self):
    print("Button clicked")
