

class Bil:
    antalBilar = 0

    def __init__(self, maxHastighet):
        self.__maxHastighet = maxHastighet
        Bil.antalBilar += 1

    def get_maxHastighet(self):
        return self.__maxHastighet


bil1 = Bil(180)
bil2 = Bil(220)
bil3 = Bil(230)

print(f"Bil 1 MaxHastighet: {bil1.get_maxHastighet()} km/h")
print(f"Bil 2 MaxHastighet: {bil2.get_maxHastighet()} km/h")
print(f"Bil 3 MaxHastighet: {bil3.get_maxHastighet()} km/h")

print(f"Antal skapade bilar: {Bil.antalBilar}")
