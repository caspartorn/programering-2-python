# def is_consonant(char):
# return char.lower() in "bcdfghjklmnpqrstvwxyz"


# def translate_to_rovarspraket(text):
#     rovarspraket = ""
#     for char in text:
#         if is_consonant(char):
#             rovarspraket += char + "o" + char.lower()
#         else:
#             rovarspraket += char
#     return rovarspraket


# input_text = input("Skriv in en mening på svenska: ")
# translated_text = translate_to_rovarspraket(input_text)
# print("Rövarspråket: ", translated_text)


# text = input("Skriv in en text: ")

# baklanges_text = text[::-1]

# print("Texten baklänges: ", baklanges_text)

# lander_huvdstäder = {
#     "sverige": "stockholm",
#     "norge": "oslo",
#     "Finland": "hälsingfors",
#     "island": "reykjavik",
# }

# lander_huvdstäder.update({"Danmark": "köpenhamn"})
# lander_huvdstäder.pop("Finland")

# set1 = {"Banana", "Pear", "Apple"}
# set2 = {"Kiwi", "Pineapple", "Pear"}

# result_set = set1.union(set2)


# print("The resulting set:", result_set)

# print("Number of elements in the resulting set:", len(result_set))

# class Person:
#     __weight = 0                    # privat attribut

#     def setWeight(self, weight):    # publik setter-metod
#         if type(weight) == int and weight > 0:
#             self.__weight = weight
#         else:
#             print("Du måste ange ett positivt heltal!")

#     def getWeight(self):		# publik getter-metod
#         return self.__weight


# p = Person()
# p.setWeight(-2)     			# Du måste ange ett positivt heltal
# p.setWeight(70)
# print(p.getWeight())


# class elev:
#     def __init__(self, ålder, namn):
#         self.namn = namn
#         self.ålder = ålder


# elev1 = elev(15, "Anna")
# print(f"namn: {elev1.namn}, Ålder: {elev1.ålder}")


# class Elev:
#     def __init__(self, namn, ålder, godkänd):
#         self.namn = namn
#         self.ålder = ålder
#         self.glad = godkänd


# elev1 = Elev("Anna", 15, True)
# print(f"Namn: {elev1.namn}, Ålder: {elev1.ålder}, Glad: {elev1.glad}")

# elev2 = Elev("Oskar", 16, False)
# print(f"Namn: {elev2.namn}, Ålder: {elev2.ålder}, Glad: {elev2.glad}")
#

# ---------------------------
# |           Elev           |
# ---------------------------
# | - namn: str              |
# | - ålder: int             |
# | - glad: bool             |
# ---------------------------
# | + __init__(namn, ålder,  |
# |            godkänd):     |
# ---------------------------

# class Bil:
#     antalBilar = 0

#     def __init__(self, maxHastighet):
#         self.__maxHastighet = maxHastighet
#         Bil.antalBilar += 1

#     def get_maxHastighet(self):
#         return self.__maxHastighet


# bil1 = Bil(180)
# bil2 = Bil(220)
# bil3 = Bil(230)

# print(f"Bil 1 MaxHastighet: {bil1.get_maxHastighet()} km/h")
# print(f"Bil 2 MaxHastighet: {bil2.get_maxHastighet()} km/h")
# print(f"Bil 3 MaxHastighet: {bil3.get_maxHastighet()} km/h")

# print(f"Antal skapade bilar: {Bil.antalBilar}")


# class Media:
#     def __init__(self, titel):
#         self.titel = titel


# class Bok(Media):
#     def __init__(self, titel, antal_sidor):
#         super().__init__(titel)
#         self.antal_sidor = antal_sidor


# class Ljudspår(Media):
#     def __init__(self, titel, speltid):
#         super().__init__(titel)
#         self.speltid = speltid


# class Film(Ljudspår):
#     def __init__(self, titel, speltid, upplösning):
#         super().__init__(titel, speltid)
#         self.upplösning = upplösning


# b = Bok("Bröderna Karamazov", 840)
# print(b.titel)
# print(b.antal_sidor)

# if isinstance(b, Media) and isinstance(b, Bok):
#     print("b är samtidigt av typen Media och Bok")

# f = Film("De sju samurajerna", "3:27:02", "1080")
# print(f.titel)
# print(f.speltid)
# print(f.upplösning)

# if isinstance(f, Media) and isinstance(f, Ljudspår) and isinstance(f, Film):
#     print("f är samtidigt av typen Media, Ljudspår och Film")

# l = Ljudspår("beat it", "3:45")
# print(l.titel)
# print(l.speltid)

# if isinstance(l, Media) and isinstance(l, Ljudspår):
#     print("l är samtidigt av typen Media, bok och Ljudspår")

def click_handler(self):
    print("Button clicked")
